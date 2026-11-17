# M1 – How do I work in JupyterLab and structure my research?

You run a notebook in JupyterLab, see what the kernel keeps and what it loses, and turn an
unfinished experiment into a complete, self-describing experiment entry that you commit
in Git.

## Starting state

The experiment `2026-11-03_ecoli-growth-37c`, a first look at *E. coli* growth at 37 °C
with 1 % glucose:

- `data/raw/ecoli-growth-37c-1pct.csv`: optical density of eight wells, read every
  5 minutes for 24 hours
- `code/growth_curve.ipynb`: reads the data, prints a summary and plots the growth curve
- `README.md` and `metadata.yml`: almost empty. Completing them is part of the exercises.

## Set up the module

Work inside `work/` only: everything outside it is reset at the next start.

1. Open a terminal (File → New → Terminal) and run:

   ```bash
   python ~/setup_module.py m1
   ```

   You should see "Module m1: copied the experiment folder … and committed it in Git."
2. In the file browser, open `work/rrw-workshop/M1_INSTRUCTIONS.md` (right-click → Open
   With → Markdown Preview). It is a copy of these instructions, next to your project.
3. Go to `work/rrw-workshop/experiments/2026-11-03_ecoli-growth-37c/`. Open `README.md`
   and `metadata.yml` and see what they already say.

You need nothing from other modules, and you can run the command again: it never
overwrites what is already there.

## Small exercise (15 min, on your own)

1. Open `code/growth_curve.ipynb` and run its cells one by one (Shift + Enter).
2. Change a cell: in the second cell, replace `growth["Average"]` with one well, for
   example `growth["A7"]`. Run the second and the third cell again and compare the plot.
3. Restart the kernel (Kernel → Restart Kernel). Run only the third cell. Read the error:
   which variable is missing, and why? Then run all cells (Run → Run All Cells).
4. Create a new notebook in the experiment's `code/` folder (File → New → Notebook, kernel
   Python 3). In its first cell, type and run:

   ```python
   print(growth.head())
   ```

   You should see `NameError: name 'growth' is not defined`. `growth` exists in the
   notebook `growth_curve.ipynb` only: each notebook has its own **kernel**, a running
   Python process that holds the notebook's variables.
5. In the next cell of the new notebook, type and run:

   ```python
   import os
   import sys

   print("Interpreter:", sys.executable)
   print("Kernel process:", os.getpid())
   ```

   Restart the kernel (Kernel → Restart Kernel) and run the cell again. The
   **interpreter**, the Python program installed in the lab, stays the same. The kernel
   process number changes: a restart starts a new kernel from the same interpreter, which
   is why step 3 lost the variables. Close the new notebook and delete it.
6. Back in `growth_curve.ipynb`, add a Markdown cell at the top: click the first cell,
   press Esc, A (new cell above), then M (Markdown). A Markdown cell holds text, which
   JupyterLab formats when you run it; a code cell holds Python, which the kernel runs.
   Write two or three sentences on what the notebook does and which data it reads, and
   run the cell (Shift + Enter): you should see formatted text. Every notebook should
   start with such a description. Save the notebook (Ctrl + S).

## Larger exercise (20 min, in groups)

Bring the experiment up to the project's template. The template experiment is in
`work/rrw-workshop/experiments/YYYY-MM-DD_experiment-name/`, and
`work/rrw-workshop/README.md` explains it.

1. `README.md`: give the experiment a title and a one-sentence description, then add the
   template's sections. Fill in at least the purpose (the question this experiment
   answers), the method, what you observed in the plot and how to reproduce the result.
   Keep the data credit.
2. `metadata.yml`: fill in the title, dates, your name, the status, the module (`M1`) and
   the project (`rrw-workshop`). Add the figure that the notebook writes to `outputs`,
   with its role.
3. `work/rrw-workshop/journal.md`: add an entry for today at the top. What did you do,
   what did you decide, and what comes next?
4. Commit: open the Git panel (the Git icon in the left sidebar). It should list
   `README.md`, `metadata.yml`, `growth_curve.ipynb`, `journal.md` and the new
   `results/figures/growth-curve.png`. Write a short message, for example
   `add meta data`, and commit.
5. In your group, compare what you put in the README and what in the journal. Agree on a
   rule for which information belongs where.

## Bonus exercise (homework)

Complete the metadata from the dataset's repository record.

1. Open the record from the DOI in the README's data credit.
2. In `metadata.yml`, fill in `source`, `source_version`, `licence` and `checksum` of the
   input, and `reuse.licence`. The record lists a checksum for the workbook
   `Repo1pct.xlsx`; note in a comment that the CSV was exported from it.
3. In the journal, note what the record does not tell you.
4. Commit your changes.

## Solutions

A reference solution for all three exercises is in `~/modules/m1/solutions/`. Its
`README.md` gives the answers step by step; `experiment/` shows the completed experiment
files and `journal-entry.md` a journal entry. Try the exercise first, then compare.

## Data credit

The data is by María Isabel González Siso, Manuel Becerra, Daniel Torrecilla,
Ana-María Díaz-Díaz, Jorge López-Beceiro and Ramón Artiaga, published on Zenodo under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
<https://doi.org/10.5281/zenodo.19416053>. See `~/data/ecoli-growth/README.md`.
