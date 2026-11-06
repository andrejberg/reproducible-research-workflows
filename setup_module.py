#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""Set up the folder work/rrw-workshop for your experiments. work/ is kept between sessions.

    python ~/setup_module.py            creates the folder work/rrw-workshop, if it is missing
    python ~/setup_module.py <module>   also adds the module's experiment to that folder

Run it as often as you like: it never overwrites what is already there.

The work folder is slow with many small files. To write fewer of them, this script builds
the folder on the local disk and packs its Git history into one file before copying it.
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MATERIALS = Path(__file__).resolve().parent
MODULES = MATERIALS / "modules"
WORK = Path.home() / "work"
PROJECT = WORK / "rrw-workshop"

# The script's own commits are marked as its own, and they work before you set your name.
GIT = ["git", "-c", "user.name=Setup script", "-c", "user.email=setup@example.invalid"]
NOT_CONTENT = (".ipynb_checkpoints", "__pycache__")


def git(folder, *args):
    command = [*GIT, "-C", str(folder), *args]
    return subprocess.run(command, check=True, capture_output=True, text=True).stdout


def init(folder):
    """Create a repository without Git's sample files, which would only slow down work/."""
    subprocess.run(["git", "init", "-q", "-b", "main", "--template=", str(folder)], check=True,
                   capture_output=True, text=True)


def copy_into_place(source, target):
    """Copy under a temporary name next to the project, so that an interrupted run leaves
    nothing half-made in the project or its repository."""
    unfinished = WORK / f".{target.name}.unfinished"
    shutil.rmtree(unfinished, ignore_errors=True)
    shutil.copytree(source, unfinished, ignore=shutil.ignore_patterns(*NOT_CONTENT))
    unfinished.rename(target)


def create_project():
    with tempfile.TemporaryDirectory() as local:
        build = Path(local) / "project"
        shutil.copytree(MATERIALS / "template", build, ignore=shutil.ignore_patterns(*NOT_CONTENT))
        init(build)
        git(build, "add", ".")
        git(build, "commit", "-q", "-m", "Create the project from the template")
        git(build, "repack", "-a", "-d", "-q", "-n")
        copy_into_place(build, PROJECT)
    init(PROJECT)  # lets Git check what the work folder supports, which can differ from the local disk
    print(f"Created the folder {PROJECT} from the template, with a Git repository and a first commit.")


def add_repository():
    """The folder exists without a repository: add what is missing and keep what is there."""
    for source in (MATERIALS / "template").rglob("*"):
        relative = source.relative_to(MATERIALS / "template")
        target = PROJECT / relative
        if source.is_file() and not target.exists() and not set(relative.parts) & set(NOT_CONTENT):
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    init(PROJECT)
    git(PROJECT, "add", ".")
    git(PROJECT, "commit", "-q", "-m", "Add a Git repository to the existing project")
    print(f"The folder {PROJECT} had no Git repository. Added the template files it was missing, "
          "kept the files it had, created a Git repository and committed everything in the folder.")


def modules():
    if not MODULES.is_dir():
        return []
    return sorted(path.name for path in MODULES.iterdir() if (path / "starting-state").is_dir())


def add_experiment(module):
    experiments = [path for path in (MODULES / module / "starting-state").iterdir()
                   if path.is_dir() and path.name not in NOT_CONTENT]
    if len(experiments) != 1:
        sys.exit(f"Module {module} should have one experiment in starting-state/ "
                 f"and has {len(experiments)}. Please tell your tutor.")
    source = experiments[0]
    target = PROJECT / "experiments" / source.name
    relative = target.relative_to(PROJECT).as_posix()

    if target.exists() and git(PROJECT, "ls-files", "--", relative):
        print(f"Module {module}: the experiment folder {target} already exists in Git, "
              "so nothing was changed.")
        return
    copied = not target.exists()
    if copied:
        target.parent.mkdir(exist_ok=True)
        copy_into_place(source, target)
    done = f"copied the experiment folder to {target}" if copied else f"found the experiment folder {target}"

    git(PROJECT, "add", "--", relative)
    # A restored folder can match the last commit, and then there is nothing to commit.
    if git(PROJECT, "status", "--porcelain", "--", relative):
        # Commits this folder only. Anything else you have staged stays as it is.
        git(PROJECT, "commit", "-q", "-m", f"Add the starting state of {module}", "--", relative)
        print(f"Module {module}: {done} and committed it in Git.")
    else:
        print(f"Module {module}: {done}. It matches the last Git commit, so there was nothing to commit.")


def setup(module):
    WORK.mkdir(exist_ok=True)
    if not PROJECT.exists():
        create_project()
    elif not (PROJECT / ".git").exists():
        add_repository()
    else:
        print(f"The folder {PROJECT} already exists with a Git repository, so it was not created again.")

    if module is None:
        print(f"No module was named, so no experiment was added. Available modules: {', '.join(modules()) or 'none'}.")
    else:
        add_experiment(module)


def main():
    if len(sys.argv) > 2 or sys.argv[1:] in (["-h"], ["--help"]):
        sys.exit(__doc__)
    module = sys.argv[1] if len(sys.argv) == 2 else None
    if module is not None and module not in modules():
        sys.exit(f"There is no module {module!r}. Available: {', '.join(modules()) or 'none'}.")

    try:
        setup(module)
    except subprocess.CalledProcessError as error:
        sys.exit(f"Git reported a problem, and the setup is not complete:\n"
                 f"{(error.stderr or error.stdout).strip()}\n"
                 "Close anything that may be using the repository and run this command again.")
    except OSError as error:
        sys.exit(f"The setup is not complete: {error}")

    if not os.path.ismount(WORK):
        print(f"WARNING: {WORK} is not a separate storage mount, so your work may be lost when the "
              "session stops. On Jupyter4NFDI, stop the lab (File → Hub Control Panel → Stop My "
              "Server) and start it again with 'Mount user data' switched on and the path "
              "/home/jovyan/work.")


if __name__ == "__main__":
    main()
