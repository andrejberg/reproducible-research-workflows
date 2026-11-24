# M1 – How do I work in JupyterLab and structure my research?

You run a notebook, see what its kernel keeps and loses, and turn an unfinished experiment
into a complete experiment entry that you commit in Git.

## EX1: JupyterLab and the kernel (15 min, on your own)

A colleague left you a notebook that plots an *E. coli* growth curve. Before you build on
it, you find out how a notebook runs and why it sometimes forgets what it knew.

1. In `experiments/2026-11-03_ecoli-growth-37c/`, open `code/growth_curve.ipynb` and run
   its cells one by one (Shift + Enter). You should see a summary and a growth curve.
2. Restart the kernel (Kernel → Restart Kernel) and run only the third cell. Which
   variable is missing, and why? Then run all cells (Run → Run All Cells).
3. Create a new notebook in `code/` (File → New → Notebook, kernel Python 3) and run:

   ```python
   print(growth.head())
   ```
   <br>
   You should see `NameError: name 'growth' is not defined`: each notebook has its own
   **kernel**, a running process of the Python interpreter that holds its variables. Close
   the new notebook and delete it.
4. Save `growth_curve.ipynb` (Ctrl + S) and open the Git panel (Git icon in the left
   sidebar). It should list `growth_curve.ipynb` and `results/figures/growth-curve.png`.
   Write a short message, for example `run growth curve`, and commit.

## EX2: A complete experiment entry (20 min, in groups)

In a few months, nobody will remember what this experiment was for. Write it down now, so
the entry explains itself, and commit it.

1. In the experiment's `README.md`, replace the title and the one-sentence description,
   and answer the purpose and the method. Keep the data credit.
2. In `metadata.yml`, fill in the title, the start date, your name, the status
   (`in_progress`), the module (`M1`) and the project (`rrw-workshop`). Under `outputs`,
   enter `results/figures/growth-curve.png` with the role `figure`. Leave unknown values
   `null`.
3. In `work/rrw-workshop/journal.md`, add an entry for today at the top: what you did and
   what you decided.
4. In your group, compare what you put in the README and what in the journal. Agree on a
   rule for which information belongs where.
5. Open the Git panel. It should list `README.md`, `metadata.yml` and `journal.md`. Write
   a short message, for example `add meta data`, and commit.

## EX3: Metadata from the data record (30 min, homework)

The data comes from a public repository record. Complete the metadata from it, so anyone
can trace the data back to its source.

1. Open `work/rrw-workshop/README.md` and the template experiment
   `experiments/YYYY-MM-DD_experiment-name/`. Which folders does the template have that
   your experiment does not, and what would go into them?
2. Open the Zenodo record from the DOI in the experiment README's data credit.
3. In `metadata.yml`, fill in `source`, `source_version`, `licence` and `checksum` of the
   input, and `reuse.licence`. The record lists a checksum for `Repo1pct.xlsx` under its
   file name; note in a comment that the CSV was exported from it.
4. In `journal.md`, update today's entry.
5. Open the Git panel. It should list `metadata.yml` and `journal.md`. Write a short
   message, for example `add data source`, and commit.

## Solutions

The reference solution is in `~/modules/m1/solutions/`: answers per step in `README.md`,
the completed files in `experiment/` and a journal entry in `journal-entry.md`. Try the
exercise first, then compare.

## Data credit

The data is by María Isabel González Siso, Manuel Becerra, Daniel Torrecilla,
Ana-María Díaz-Díaz, Jorge López-Beceiro and Ramón Artiaga, published on Zenodo under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
<https://doi.org/10.5281/zenodo.19416053>. See `~/data/ecoli-growth/README.md`.
