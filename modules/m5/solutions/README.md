# M5 reference solution

The exercises are in `modules/m5/README.md` (in your project:
`work/rrw-workshop/M5_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-09_pbmc3k-first-look/`
  that the exercises change: `README.md` (software environment and results),
  `metadata.yml` (author, dates, status) and `code/first_look.ipynb` (the answer to EX1).
  The dataset is not included: the setup downloads it.
- `journal-entry.md` — the entries at the top of `work/rrw-workshop/journal.md`, from EX2
  and EX3.

Names, dates and commit hashes in the solution (author, `2026-11-30`, `3f2a1b7`) are
examples. Your commit hashes differ.

## What uv and Git show

The versions below are what uv installed in November 2026. A later run can show newer
versions of the added packages, because `uv add` takes the newest version that fits. The
change of python-dateutil stays the same as long as its newest version is 3 or higher:
s3fs needs botocore, and botocore needs python-dateutil below 3.

- `uv add anndata` installs 19 packages, among them `anndata==0.13.4`, `h5py==3.16.0` and
  `zarr==3.4.2`. It changes no package the project had before. `pyproject.toml` gets one
  line, `"anndata>=0.13.4"`, under `dependencies`.
- The dataset holds 2,694 cells and 13,714 genes.
- `uv add s3fs` installs 19 packages, among them `s3fs==2026.9.0` and
  `botocore==1.43.117`, and replaces one: `- python-dateutil==4.0.0`,
  `+ python-dateutil==2.9.0.post0`. `uv.lock` grows by about 290 lines; `pyproject.toml`
  gets one line, `"s3fs>=2026.9.0"`.

## EX1: Add a package to your project

- Step 1: `sys.executable` is `/home/jovyan/.venvs/rrw-workshop/bin/python`. The
  environment lives outside `work/`, on the lab's local disk, so it is lost when the lab
  stops; the lab installs it again from `pyproject.toml` and `uv.lock` at every start. The
  cell `# Read the dataset` stops with `ModuleNotFoundError: No module named 'anndata'`.
- Step 2: see "What uv and Git show". A path that does not end in
  `.venvs/rrw-workshop/bin/python` in step 1 means the notebook runs on another kernel,
  which `uv add` does not change: choose "Python (rrw-workshop)" in Kernel → Change
  Kernel. A kernel that was running during `uv add` still has the packages it has loaded;
  the restart makes it load them again.
- Step 3: `print(adata.n_obs, "cells")` and `print(adata.n_vars, "genes")` print
  `2694 cells` and `13714 genes`. The same numbers are in the first line of what `adata`
  shows: `n_obs × n_vars = 2694 × 13714`. In an AnnData object, the observations
  (`obs`) are the cells and the variables (`var`) are the genes.
- Step 4: the commit holds `first_look.ipynb`, `pyproject.toml` and `uv.lock`. Together,
  the commit records both the result and the environment it came from.

## EX2: Add a package in the middle of a project

- Step 1: see "What uv and Git show". The other lines with `+` are new packages that s3fs
  needs. Some of them, such as `six` and `urllib3`, were already in `uv.lock` for
  JupyterLab on another computer, but not installed in the lab's environment.
- Step 2: the first command prints three lines, `name = "python-dateutil"`,
  `-version = "4.0.0"` and `+version = "2.9.0.post0"`. `uv.lock` records the same change
  that uv printed. The second command prints the EX1 commit, the last one that changed
  `uv.lock`. A participant who did not commit in EX1 sees an earlier commit instead, for
  example `Create the project from the template`. Then the environment of the counts was
  never committed: run the counts again after the commit of this exercise.
- Step 3: see `experiment/README.md`, § Software environment.
- Step 4: see `journal-entry.md`, the entry of 2026-11-30.
- Step 5: the commit holds `pyproject.toml`, `uv.lock`, `README.md` and `journal.md`.
  Pairs see the same lines from uv. To go back to the environment of the counts, take the
  two files from that commit and install them:

  ```bash
  git checkout 3f2a1b7 -- pyproject.toml uv.lock
  uv sync
  ```

## EX3: Recreate the environment on your own computer

- Step 1: either route works for steps 2 and 3. Only a clone also brings the experiment
  and its data for step 4.
- Step 3: `uv sync` creates the environment in a folder `.venv` inside the project and
  installs exactly the versions in `uv.lock`. It prints `0.13.4 2.9.0.post0`, or the
  versions your project has, the same as
  `~/.venvs/rrw-workshop/bin/python -c "from importlib.metadata import version; print(version('anndata'), version('python-dateutil'))"`
  prints in the lab. `.gitignore` already lists `.venv/`, so Git does not track it.
- Step 4: the notebook prints the path of `.venv/bin/python` (on Windows
  `.venv\Scripts\python.exe`) in the project, `2694 cells` and `13714 genes`. With the
  first route, `uv run --group jupyter` installs JupyterLab into the project's
  environment, and the next `uv sync` removes it again, so that the environment holds
  exactly the packages of `pyproject.toml`. The second route adds the kernel "Python (rrw-workshop)" to your
  JupyterLab; it runs the `.venv` of this project folder.
- Step 5: see `journal-entry.md`, the entry of 2026-12-02. Possible differences: on
  Windows, the installer is a PowerShell command, and the terminal must be opened again
  before `uv` is found.

## Skills covered

Each M5 skill, with the exercise step that practises it:

- use the JupyterLab terminal — EX1 2, EX2 1–2
- add packages to a project with uv — EX1 2, EX2 1
- see which environment a kernel runs on — EX1 1 (`sys.executable`), EX1 2 (restart the
  kernel to load the new package), EX3 4
- pin package versions in a lock file — EX1 4 and EX2 2 (`uv.lock` records the exact
  version of every package)
- read how adding a package changes locked versions — EX2 1–2
- find the commit that holds an earlier environment — EX2 2
- record software versions in an experiment entry — EX2 3 (`README.md` § Software
  environment; `metadata.yml` § `software` names `pyproject.toml`, `uv.lock` and the
  kernel)
- commit `pyproject.toml` and `uv.lock` together with the experiment — EX1 4, EX2 5
- recreate an environment from its files with uv — EX3 1–3 (`uv sync`)
- open a project's environment in JupyterLab on another computer — EX3 4

Requirements from earlier modules used here: import modules (EX1 1–3), restart the kernel
(EX1 2), kernel and interpreter (EX1 1), the experiment's README (EX2 3), a journal entry
(EX2 4, EX3 5), a commit in the Git panel (EX1 4, EX2 5, EX3 5), push commits and clone a
repository (EX3 1).
