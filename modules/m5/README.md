# M5 – How do I install modules and manage environments?

You add packages to your project with the package manager uv, read a single-cell dataset
with one of them, and see how adding another package changes the environment your earlier
results ran on.

You leave with a project whose `pyproject.toml` and `uv.lock` record every package and
version it needs, so that you can recreate the same environment on another computer.

## Before you start

1. In `experiments/2026-11-09_pbmc3k-first-look/`, open `code/first_look.ipynb`. EX1 is
   in its markdown cells, and below. EX2 and EX3 work in the terminal and in the
   project's files: their instructions are only here.
2. Your notebook runs on the kernel "Python (rrw-workshop)", shown at the top right of
   the notebook. It uses the packages that your project lists in `pyproject.toml`, in the
   versions that `uv.lock` records. The lab installs them at every start, and `uv add`
   adds a package to all three: `pyproject.toml`, `uv.lock` and the environment.

## EX1: Add a package to your project (15 min, on your own)

The dataset is an `.h5ad` file, a common format for single-cell data, and no package in
your project reads it yet. Add the package anndata to the project, so that the notebook
can read the file and anyone who recreates the project gets the same package.

1. Run the first two code cells (Shift + Enter). `# Which Python runs this notebook`
   shows a path that ends in `.venvs/rrw-workshop/bin/python`: the project's environment.
   `# Read the dataset` stops with `ModuleNotFoundError: No module named 'anndata'`. This
   error is expected: the package is missing.
2. Open a terminal (File → New → Terminal), go to the project and add the package:

   ```bash
   cd ~/work/rrw-workshop
   uv add anndata
   ```
   <br>
   uv lists the packages it installs, each with a `+`, for example `+ anndata==0.13.4`.
   Then restart the kernel (Kernel → Restart Kernel), so that the notebook sees the new
   package.
3. Run the first two code cells again. You should see
   `AnnData object with n_obs × n_vars = 2694 × 13714`. In the cell
   `# your task: cells and genes`, print the number of cells, `adata.n_obs`, and the
   number of genes, `adata.n_vars`. You should see 2694 and 13714.
4. Save the notebook (Ctrl + S) and open the Git panel. It should list
   `first_look.ipynb`, `pyproject.toml` and `uv.lock` as changed. Click `pyproject.toml`
   to see what changed: one new line, such as `"anndata>=0.13.4"`. Stage all three files,
   write a short message, for example `add anndata and count cells and genes`, and commit.

## EX2: Add a package in the middle of a project (20 min, in pairs)

A colleague's code reads single-cell data straight from public cloud storage and needs
the package s3fs. Adding a package can change packages you already have, and then your
EX1 results ran on a different environment than your project has now. Each of you adds
s3fs to your own project and writes down where the environment of the EX1 results is
kept.

1. In the terminal, in `~/work/rrw-workshop`, run `uv add s3fs`. Read what uv prints:
   `+` marks a package it installs and `-` one it removes. You should see
   `- python-dateutil==4.0.0` and `+ python-dateutil==2.9.0.post0`. pandas uses
   python-dateutil to read dates, and s3fs needs a version below 3, so uv replaced the
   version your project had. You never added python-dateutil yourself.
2. See the same change in `uv.lock`, then find the last commit that changed it before:

   ```bash
   git diff uv.lock | grep -A2 '^ name = "python-dateutil"'
   git log --oneline -1 -- uv.lock
   ```
   <br>
   The first command shows `-version = "4.0.0"` and `+version = "2.9.0.post0"`. The
   second shows your EX1 commit, for example
   `3f2a1b7 add anndata and count cells and genes`. Its `uv.lock` records the
   environment your cell counts ran with.
3. In the experiment's `README.md`, under "Software environment", replace the line in
   `<…>` with the hash of that commit, for example: "The cell counts ran with the
   environment of commit `3f2a1b7` (python-dateutil 4.0.0). On 2026-12-01, s3fs was
   added, which changed python-dateutil to 2.9.0.post0."
4. Add an entry for today at the top of `journal.md` (in `work/rrw-workshop/`): which
   package you added, which version it changed, and which commit holds the environment
   of the EX1 results.
5. Open the Git panel. It should list `pyproject.toml`, `uv.lock`, `README.md` and
   `journal.md` as changed. Stage them all, write a short message, for example
   `add s3fs and record the environment of the cell counts`, and commit. Compare with
   your partner: did uv print the same changes?

## EX3: Recreate the environment on your own computer (30 min, homework)

Your project should run on the computer where you do your research, with the same
packages as in the lab. Recreate its environment there from `pyproject.toml` and
`uv.lock`. The workshop gives no support for installing software on your own computer: if
a step does not work on your system, ask an LLM how to do it there, and note what you had
to change.

1. Get the project onto your computer. If it is on a remote repository, push it from the
   lab's Git panel, then clone it on your computer, or pull it into a clone you already
   have. Otherwise, in the lab's file browser, download `pyproject.toml` and `uv.lock`
   from `work/rrw-workshop/` (right-click → Download) into an empty folder on your
   computer.
2. Install uv on your computer:
   <https://docs.astral.sh/uv/getting-started/installation/>. uv also installs
   Python 3.13 if your computer does not have it.
3. In a terminal, in the project folder, install the packages and check two of their
   versions:

   ```bash
   uv sync
   uv run python -c "from importlib.metadata import version; print(version('anndata'), version('python-dateutil'))"
   ```
   <br>
   You should see the versions your project has in the lab, for example
   `0.13.4 2.9.0.post0`.
4. If you cloned the whole project, run the notebook on your computer:
   - Without JupyterLab on your computer, run `uv run --group jupyter jupyter lab`. It
     installs JupyterLab into the project's environment and opens it in your browser.
     Choose the kernel "Python 3 (ipykernel)": it runs on the project's packages.
   - With JupyterLab on your computer, run this once so that your JupyterLab offers the
     project's packages as the kernel "Python (rrw-workshop)", then start JupyterLab as
     usual:

     ```bash
     uv run python -m ipykernel install --user --name rrw-workshop --display-name "Python (rrw-workshop)"
     ```
     <br>
   Open `experiments/2026-11-09_pbmc3k-first-look/code/first_look.ipynb` and run all
   cells (Run → Run All Cells). You should see 2694 cells and 13714 genes, as in the lab.
5. Back in the lab, add an entry for today at the top of `journal.md`: which system you
   used, whether the versions matched, and what you had to do differently from these
   steps. Commit it.

## Solutions

A reference solution for all three exercises is in `~/modules/m5/solutions/`. Its
`README.md` gives what uv and Git show and the answers step by step; `experiment/` shows
the completed experiment files and `journal-entry.md` the journal entries. Try the
exercise first, then compare.

## Data credit

The dataset is the "PBMC3k teaching dataset (filtered AnnData)" by Melisa Ağrı, published
on Zenodo under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
<https://doi.org/10.5281/zenodo.22655336>. It is derived from the dataset "3k PBMCs from a
Healthy Donor" by 10x Genomics, released under a Creative Commons Attribution licence. See
the experiment's README.
