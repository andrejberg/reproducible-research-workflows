#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""Set up the folder work/rrw-workshop for your experiments. work/ is kept between sessions.

    python ~/setup_module.py            creates the folder work/rrw-workshop, if it is missing
    python ~/setup_module.py <module>   also adds the module's experiment to that folder, and
                                        its instructions as <MODULE>_INSTRUCTIONS.md
    python ~/setup_module.py --environment
                                        only installs the project's packages and registers
                                        the kernel; the lab runs this at every start

Each module's setup.json says which experiment to add and which files to download for it.
Run it as often as you like: it never overwrites what is already there.
Each run also installs the project's packages with `uv sync` and registers that environment
as the kernel "Python (rrw-workshop)", so a run after a restart rebuilds both.

A project folder without pyproject.toml was made from an earlier version of the template.
If it holds only what the template gave it, the script creates it again. Otherwise it moves
the folder to work/rrw-workshop-old, where you can still read your earlier work, and creates
a new project.
Its commits carry your Git name and email. Where you have not set them, it takes them from
your Jupyter4NFDI account (see git_identity.py).

The work folder is slow with many small files. To write fewer of them, this script builds
the folder on the local disk and packs its Git history into one file before copying it.
"""

import hashlib
import http.client
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

import git_identity

MATERIALS = Path(__file__).resolve().parent
MODULES = MATERIALS / "modules"
WORK = Path.home() / "work"
PROJECT = WORK / "rrw-workshop"
OLD_PROJECT = WORK / "rrw-workshop-old"
FIRST_COMMIT = "Create the project from the template"

# Commits carry your Git name and email. Where one is still missing, after asking the hub
# (git_identity.py), the commit uses this placeholder, so it works before you set yours.
PLACEHOLDER = {"user.name": "Setup script", "user.email": "setup@example.invalid"}
GIT = ["git"]
NOT_CONTENT = (".ipynb_checkpoints", "__pycache__")
DOWNLOAD_TIMEOUT = 60  # seconds without a response

# The project's environment and the kernel that runs notebooks in it. The environment stays
# on the local disk, outside work/ (the start script sets this path; the default here is the
# same path, for a session started without it).
ENVIRONMENT = Path(os.environ.get("UV_PROJECT_ENVIRONMENT", Path.home() / ".venvs" / "rrw-workshop"))
KERNEL = "rrw-workshop"
KERNEL_DISPLAY_NAME = "Python (rrw-workshop)"


def use_identity():
    """Fill in a missing Git name or email from the hub, and use the placeholder for what is left."""
    git_identity.fill_in()
    GIT[1:] = [arg for key, value in PLACEHOLDER.items() if not git_identity.configured(key)
               for arg in ("-c", f"{key}={value}")]


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


def untouched():
    """True if the project holds only what the template gave it: its first commit and no changes."""
    if not (PROJECT / ".git").exists():
        return False
    try:
        history = git(PROJECT, "log", "--format=%s").splitlines()
        changes = git(PROJECT, "status", "--porcelain", "--untracked-files=all")
    except subprocess.CalledProcessError:
        return False
    return history == [FIRST_COMMIT] and changes == ""


def replace_old_project():
    """The project has no pyproject.toml, so it was made from an earlier version of the template.
    Remove it if it holds only what the template gave it; otherwise move it aside, so that
    nothing of yours is lost. Either way, the caller then creates the project again."""
    if untouched():
        # Rename first, so that an interrupted removal leaves no half-removed project.
        removing = WORK / f".{PROJECT.name}.removing"
        shutil.rmtree(removing, ignore_errors=True)
        PROJECT.rename(removing)
        print(f"The folder {PROJECT} was made from an earlier version of the template and held "
              "nothing of yours yet, so it is being created again from the current template ...", flush=True)
        shutil.rmtree(removing, ignore_errors=True)
        return
    aside, number = OLD_PROJECT, 1
    while aside.exists():
        number += 1
        aside = WORK / f"{OLD_PROJECT.name}-{number}"
    PROJECT.rename(aside)
    print(f"The folder {PROJECT} was made from an earlier version of the template. It was moved to "
          f"{aside}, and a new project is created from the current template. What you did in the "
          f"old folder is not part of the new project, but you can still open and read it in {aside}.")


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
    return sorted(path.parent.name for path in MODULES.glob("*/setup.json"))


def read_setup(module):
    """Return the module's experiment folder and its list of downloads, as setup.json defines them."""
    try:
        setup = json.loads((MODULES / module / "setup.json").read_text(encoding="utf-8"))
        source = MODULES / module / "starting-state" / setup["experiment"]
        downloads = [(item["url"], item["md5"], item["path"]) for item in setup.get("download", [])]
    except (ValueError, KeyError, TypeError) as error:
        sys.exit(f"The file setup.json of module {module} cannot be used ({error!r}). Please tell your tutor.")
    if not source.is_dir():
        sys.exit(f"Module {module} names the experiment {source.name} in setup.json, "
                 "but starting-state/ does not have it. Please tell your tutor.")
    return source, downloads


def download(url, md5, target):
    """Save the file at target only if its checksum matches."""
    try:
        with urllib.request.urlopen(url, timeout=DOWNLOAD_TIMEOUT) as response:
            content = response.read()
    except (OSError, http.client.HTTPException) as error:
        sys.exit(f"Could not download {target.name} from {url}: {error}\n"
                 "The experiment was not added. Check the network connection and run this command "
                 "again. If it keeps failing, please tell your tutor.")
    actual = hashlib.md5(content).hexdigest()
    if actual != md5:
        sys.exit(f"The download of {target.name} has the checksum {actual}, not the expected {md5}, "
                 "so it was not kept and the experiment was not added. Run this command again. "
                 "If it keeps failing, please tell your tutor.")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)


def copy_instructions(module):
    """Copy the module's README into the project, so its instructions are next to your work.
    Return the copy's path if it was made now, or None if it already existed."""
    source = MODULES / module / "README.md"
    target = PROJECT / f"{module.upper()}_INSTRUCTIONS.md"
    if target.exists() or not source.is_file():
        return None
    shutil.copy2(source, target)
    return target


def add_experiment(module):
    source, downloads = read_setup(module)
    target = PROJECT / "experiments" / source.name
    relative = target.relative_to(PROJECT).as_posix()
    instructions = PROJECT / f"{module.upper()}_INSTRUCTIONS.md"

    if target.exists() and git(PROJECT, "ls-files", "--", relative):
        print(f"Module {module}: the experiment folder {target} already exists in Git, "
              "so it was not changed.")
        if copy_instructions(module):
            git(PROJECT, "add", "--", instructions.name)
            git(PROJECT, "commit", "-q", "-m", f"Add the instructions of {module}", "--",
                instructions.name)
            print(f"Module {module}: copied its instructions to {instructions} and committed them in Git.")
        else:
            print(f"Module {module}: its instructions are in {instructions}.")
        return
    copied = not target.exists()
    missing = [item for item in downloads if not (target / item[2]).exists()]

    # Download before touching the project, so that a failed download leaves nothing half-made.
    with tempfile.TemporaryDirectory() as local:
        build = Path(local) / source.name
        if copied:
            shutil.copytree(source, build, ignore=shutil.ignore_patterns(*NOT_CONTENT))
        for url, md5, path in missing:
            print(f"Module {module}: downloading {Path(path).name} ...", flush=True)
            download(url, md5, build / path)
        if copied:
            target.parent.mkdir(exist_ok=True)
            copy_into_place(build, target)
        else:
            for _, _, path in missing:
                (target / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(build / path, target / path)

    done = f"copied the experiment folder to {target}" if copied else f"found the experiment folder {target}"
    if missing:
        done += f", downloaded {len(missing)} file(s) into it, checked their checksums"
    paths = [relative]
    if copy_instructions(module):
        paths.append(instructions.name)

    git(PROJECT, "add", "--", *paths)
    # A restored folder can match the last commit, and then there is nothing to commit.
    if git(PROJECT, "status", "--porcelain", "--", *paths):
        # Commits the experiment and the instructions only. Anything else you have staged stays as it is.
        git(PROJECT, "commit", "-q", "-m", f"Add the starting state of {module}", "--", *paths)
        print(f"Module {module}: {done} and committed it in Git.")
    else:
        print(f"Module {module}: {done}. It matches the last Git commit, so there was nothing to commit.")
    print(f"Module {module}: its instructions are in {instructions}.")


def sync_environment():
    """Install the packages that pyproject.toml and uv.lock record, and register the kernel."""
    if not (PROJECT / "pyproject.toml").is_file():
        print(f"The folder {PROJECT} has no pyproject.toml, so no software environment was installed.")
        return
    uv = shutil.which("uv")
    if uv is None:
        sys.exit("The lab has no uv, so the project's software environment was not installed. "
                 "Stop the lab and start it again from the workshop page.")
    environment = os.environ | {"UV_PROJECT_ENVIRONMENT": str(ENVIRONMENT)}
    print("Installing the project's software environment with uv sync ...", flush=True)
    for command in ([uv, "sync", "--quiet"],
                    [uv, "run", "--no-sync", "python", "-m", "ipykernel", "install", "--user",
                     "--name", KERNEL, "--display-name", KERNEL_DISPLAY_NAME]):
        result = subprocess.run(command, cwd=PROJECT, env=environment, capture_output=True, text=True)
        if result.returncode != 0:
            sys.exit(f"uv could not install the project's software environment:\n"
                     f"{(result.stderr or result.stdout).strip()}\n"
                     "Check the network connection and run this command again. "
                     "If it keeps failing, please tell your tutor.")
    print(f"Installed the packages of {PROJECT / 'pyproject.toml'} in {ENVIRONMENT} and registered "
          f"it as the kernel \"{KERNEL_DISPLAY_NAME}\".")


def setup(module):
    WORK.mkdir(exist_ok=True)
    use_identity()
    shutil.rmtree(WORK / f".{PROJECT.name}.removing", ignore_errors=True)
    if PROJECT.exists() and not (PROJECT / "pyproject.toml").is_file():
        replace_old_project()
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
    sync_environment()


def main():
    if len(sys.argv) > 2 or sys.argv[1:] in (["-h"], ["--help"]):
        sys.exit(__doc__)
    module = sys.argv[1] if len(sys.argv) == 2 else None
    if module == "--environment":
        sync_environment()
        return
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
