# M5 reference solution

The exercises are in `modules/m5/README.md` (in your project:
`work/rrw-workshop/M5_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-09_pbmc3k-first-look/`
  that change in a complete experiment: `README.md` (results),
  `metadata.yml` (author, dates, status) and `code/first_look.ipynb` (the answer to EX1).
  The dataset is not included: the setup downloads it.
- `journal-entry.md` — the entries at the top of `work/rrw-workshop/journal.md`, from EX2
  and EX3.

Names, dates and commit hashes in the solution (author, `2026-11-30`, `3f2a1b7`) are
examples. Your commit hashes differ.

## What uv and Git show

The versions below are what uv installed in November 2026. A later run can show newer
versions of anndata and of the packages it needs, because `uv add` takes the newest
version that fits. EX2 gives the version of s3fs, so that the change of python-dateutil
stays the same: s3fs 2026.9.0 needs aiobotocore, and aiobotocore and botocore both need
python-dateutil below 3. s3fs 2026.9.0 still accepts newer versions of aiobotocore, so the
change lasts as long as these two keep that limit; they have had it for years.

- `uv add anndata` installs 19 packages, among them `anndata==0.13.4`, `h5py==3.16.0` and
  `zarr==3.4.2`. It changes no package the project had before. `pyproject.toml` gets one
  line, `"anndata>=0.13.4"`, under `dependencies`.
- The dataset holds 2,694 cells and 13,714 genes.
- `uv add "s3fs==2026.9.0"` installs 19 packages, among them `s3fs==2026.9.0` and
  `botocore==1.43.117`, and replaces one: `- python-dateutil==4.0.0`,
  `+ python-dateutil==2.9.0.post0`. `uv.lock` grows by about 290 lines; `pyproject.toml`
  gets one line, `"s3fs==2026.9.0"`.

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
- Step 2: `git log` lists two commits, the EX1 commit on top and the setup's commit
  `Add the starting state of m5` below it. `git show 3f2a1b7:uv.lock | grep …` prints `name = "python-dateutil"` and
  `version = "4.0.0"`. `git show` reads the file as it was in that commit, so the change
  uv just made, which is not committed yet, does not appear. A participant who did not
  commit in EX1 sees the setup's commit on top. Its `uv.lock` has no anndata: the
  environment of the counts was never committed, so run the counts again after the
  commit of this exercise and commit the notebook.
  The `git checkout` block is for understanding only and is not run: it would replace
  `pyproject.toml` and `uv.lock` with the versions of that commit, and `uv sync` would
  install that environment again. `git checkout HEAD -- pyproject.toml uv.lock` and
  `uv sync` would bring back the current one.
- Step 3: see `journal-entry.md`, the entry of 2026-11-30.
- Step 4: the commit holds `pyproject.toml`, `uv.lock` and `journal.md`. Pairs see the same
  lines from uv. The experiment's files do not change: the EX1 commit stays the last one
  that changed the experiment, so step 2 still finds the environment of the counts.

## EX3: Recreate the environment on your own computer

- Step 1: either route works for steps 2 and 3. Only a clone also brings the experiment
  and its data for step 4.
- Step 3: `uv sync` creates the environment in a folder `.venv` inside the project and
  installs exactly the versions in `uv.lock`. It prints `0.13.4 2.9.0.post0`, or the
  versions your project has, the same as
  `~/.venvs/rrw-workshop/bin/python -c "from importlib.metadata import version; print(version('anndata'), version('python-dateutil'))"`
  prints in the lab. `.gitignore` already lists `.venv/`, so Git does not track it.
- Step 4: the one-time command adds the kernel "Python (rrw-workshop)" to your user's
  JupyterLab settings; it runs the `.venv` of this project folder. Both JupyterLabs find
  it, so the notebook opens on the same kernel name as in the lab. The notebook prints the
  path of `.venv/bin/python` (on Windows `.venv\Scripts\python.exe`) in the project,
  `2694 cells` and `13714 genes`. With the No route, `uv run --group jupyter` installs
  JupyterLab into the project's environment, and the next `uv sync` removes it again, so
  that the environment holds exactly the packages of `pyproject.toml`.
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
- find the environment a result ran with in the project's history — EX2 2 (the last
  commit that changed the experiment, and its `uv.lock`)
- commit `pyproject.toml` and `uv.lock` together with the experiment — EX1 4, EX2 4
- recreate an environment from its files with uv — EX3 1–3 (`uv sync`)
- open a project's environment in JupyterLab on another computer — EX3 4 (the same kernel
  name "Python (rrw-workshop)" as in the lab)

Requirements from earlier modules used here: import modules (EX1 1–3), restart the kernel
(EX1 2), kernel and interpreter (EX1 1), a journal entry (EX2 3, EX3 5), a commit in the
Git panel (EX1 4, EX2 4, EX3 5), push commits and clone a repository (EX3 1).
