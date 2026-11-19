# M3 – How do I read and write data?

You read growth curves of *E. coli* from files, write processed tables and a figure into
the experiment, and fetch more of the dataset from its repository with code, checking each
download against its checksum.

You leave with an experiment in which raw data stays as it came, everything computed sits
in its own folder under a clear name, and every downloaded file can be traced to its
source.

## Before you start

1. In `experiments/2026-11-05_ecoli-growth-temperatures/`, open `README.md` and read
   "Files and names": which folder holds what, and how files are named.
2. Open [GWDG Chat AI](https://chat-ai.academiccloud.de) in a second browser tab, or
   another chat service you use. You copy code from the notebook into the chat, and the
   answer back into a notebook cell.
3. Open `code/growth_curves.ipynb`. The exercises are in its markdown cells, and below.

When you work with the LLM:

- Put only public or made-up data into an LLM. The growth curves are published, so you may
  paste them.
- Say what you have and what you want: paste the cells that define the names you use, such
  as `RAW` and `PROCESSED`.
- The LLM gives different code each time, and other services give different code again.
  Judge it by its result, which you check yourself.

## EX1: Read, write and plot (15 min, on your own)

You want to see how temperature changes the growth of *E. coli*. Read the three
temperature files, keep a processed copy with the time in hours, and plot the three curves
in one figure.

1. Run the first four code cells (Shift + Enter). You should see the first rows of the
   37 °C table, then `<class 'numpy.ndarray'> (289,)` and `OD above 0.4 after 2.3 h`.
   `hours` is a numpy array: one division turns all 289 readings into hours at once.
2. Copy the cells `# Import the modules` and `# Paths` into the chat and ask for the
   code, for example:

   > Using `RAW` and `PROCESSED` above, write pandas code that reads
   > `ecoli-growth-29c-1pct.csv`, `ecoli-growth-37c-1pct.csv` and
   > `ecoli-growth-45c-1pct.csv`, adds a column `time_h` with `tcultivo (min)` in hours,
   > keeps the tables in a dictionary `growth` with keys such as `"37c"`, and writes each
   > table to `PROCESSED` as `ecoli-growth-<temperature>-1pct-hours.csv`. Create
   > `PROCESSED` if it is missing.

3. Paste the code into the cell `# your task: read …` and run it. In the file browser,
   `data/processed/` should hold three files such as `ecoli-growth-37c-1pct-hours.csv`.
   Open one: its last column is `time_h`, ending near 24.1.
4. Ask for the figure, for example:

   > Plot the column `Average` against `time_h` for every table in `growth`, in one
   > figure, with axis labels that name the units, a legend with the temperatures and a
   > title. Save it to `FIGURES` as `growth-curves-1pct.png`. Create `FIGURES` if it is
   > missing.

   Run it in the cell `# your task: plot …`. You should see three curves: 37 °C rises
   first, 29 °C last, and 45 °C levels off lowest. `results/figures/` should hold the PNG
   file.
5. Save the notebook (Ctrl + S) and open the Git panel. It should list
   `growth_curves.ipynb` as changed, and the three processed files and the figure as
   untracked. Stage them all, write a short message, for example
   `plot growth at three temperatures`, and commit.

## EX2: Fetch data from a repository (20 min, on your own)

Your figure shows 1 % glucose only, and the dataset's repository also has a workbook for
2 % glucose. You fetch it with code, so the step can be rerun and checked, and you make
sure that the file arrived intact and your raw data stayed as it was.

1. Run the cell `# Ask Zenodo for the record`. You should see the record's title and its
   five files, each with its size and an `md5:` checksum. `record` holds the whole answer
   as dictionaries and lists.
2. Ask the LLM for the download, for example:

   > `record["files"]` is a list of dictionaries with the keys `key` (the file name),
   > `checksum` (such as `"md5:4b23…"`) and `links`, where `links["self"]` is the
   > download URL. Write Python with `urllib.request` and `hashlib` that downloads
   > `Repo2pct.xlsx`, computes its MD5 and saves it to `RAW` only if the MD5 matches the
   > checksum. Print both checksums.

   Run it in the cell `# your task: download …`. You should see the same checksum twice,
   and `Repo2pct.xlsx` in `data/raw/`.
3. Ask for the conversion to an open format, for example:

   > Write pandas code that reads every sheet of `RAW / "Repo2pct.xlsx"` and writes each
   > one to `PROCESSED` as CSV without the index, named like `ecoli-growth-29c-2pct.csv`
   > for a sheet named like `29_2%`.

   Run it in the cell `# your task: convert …`. `data/processed/` should hold nine new
   files, from `ecoli-growth-29c-2pct.csv` to `ecoli-growth-45c-2pct.csv`. The warning
   `Workbook contains no default style` is harmless.
4. Run the cell `# Check in Git`. `git status` should list `Repo2pct.xlsx` as new (`??`)
   and no changed file (`M`) in `data/raw/`. `git log` shows the history of `data/raw/`:
   the one commit of the setup, which added the raw data.
5. Save the notebook and open the Git panel. It should list `growth_curves.ipynb`,
   `Repo2pct.xlsx` and the nine CSV files. Stage them all, write a short message, for
   example `fetch the 2 % glucose workbook from Zenodo`, and commit.

## EX3: Fetch in a loop (30 min, homework)

A later analysis will compare all four glucose concentrations. Fetch their workbooks in
one loop that checks every file, so that you can rerun it at any time, and record the
files in the experiment's metadata.

1. After a kernel restart, run all cells above this one first (Run → Run All Above
   Selected Cell). Then ask the LLM to turn your download code into a loop over each file
   in `record["files"]` whose name starts with `Repo`: a file already in `RAW` gets its
   MD5 checked, a missing file is downloaded, checked and saved. Each file gets one
   printed line: its name, `present` or `downloaded`, and whether the checksum matches.
2. Run it in the cell `# your task: fetch in a loop`. You should see four lines:
   `Repo1pct.xlsx` and `Repo2pct.xlsx` present, `Repo0·1pct.xlsx` and `Repo0·5pct.xlsx`
   downloaded, all four checksums matching. Run it once more: all four are present and
   nothing is downloaded. The repository limits how many requests it answers per minute,
   so do not run the loop over and over.
3. Run the cell `# Check in Git` again. You should see the two new workbooks (`??`) and
   no changed file.
4. In `metadata.yml`, list the two new workbooks and `Repo2pct.xlsx` under `inputs`, the
   way `Repo1pct.xlsx` is listed, with the checksums from the record. List the processed
   files and the figure under `outputs`, and fill in `date_started`, `author` and
   `status`.
5. In `README.md`, replace the placeholders under "Data generated or processed" and answer
   the questions under "Observations and interpretation". Add an entry for today at the
   top of `journal.md` (in `work/rrw-workshop/`): what you fetched and how you checked it.
6. Save the notebook and open the Git panel. It should list `growth_curves.ipynb`, the two
   workbooks, `metadata.yml`, `README.md` and `journal.md`. Write a short message, for
   example `fetch all glucose workbooks in a loop`, and commit.

## Solutions

A reference solution for all three exercises is in `~/modules/m3/solutions/`. Its
`README.md` gives the results that do not depend on the LLM and the answers step by step;
`experiment/` shows the completed experiment files and `journal-entry.md` a journal entry.
Try the exercise first, then compare.

## Data credit

The growth curves are "Optical Density Data from the Growth of *Escherichia coli* at
Different Temperatures and Glucose Concentrations" by María Isabel González Siso, Manuel
Becerra, Daniel Torrecilla, Ana-María Díaz-Díaz, Jorge López-Beceiro and Ramón Artiaga,
published on Zenodo under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
<https://doi.org/10.5281/zenodo.19416053>. See the experiment's README.
