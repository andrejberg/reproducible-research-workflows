# M3 reference solution

The exercises are in `modules/m3/README.md` (in your project:
`work/rrw-workshop/M3_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-05_ecoli-growth-temperatures/`
  that the exercises change: `metadata.yml` (inputs, outputs, author, dates, status) and
  `code/growth_curves.ipynb` (one possible answer per exercise). The files the notebook writes or downloads are not
  included: run the notebook to create them.
- `journal-entry.md` — the entry at the top of `work/rrw-workshop/journal.md`.

Names and dates in the solution (author, `2026-11-30`) are examples.

## Results that do not depend on the LLM

Every LLM run and every service gives different code. Check the results, not the code.
These values follow from the data:

- Each of the three CSV files has 289 readings; `time_h` runs from 0.07 to 24.06 (29 and
  45 °C) or 24.07 (37 °C).
- First time the optical density (`Average`) is above 0.4, 1 % glucose: 29 °C 6.4 h,
  37 °C 2.3 h, 45 °C 10.2 h. With 2 % glucose: 6.6 h, 2.2 h and 14.2 h.
- Optical density at the end, 1 % glucose: 29 °C 0.527, 37 °C 0.580, 45 °C 0.425.
- The record lists five files. Their MD5 checksums: `Repo0·1pct.xlsx`
  `d4abd96f8b3cc135eba7f341308baec6`, `Repo0·5pct.xlsx` `bf807e8d5ab42a8adbd863aa2d06d739`,
  `Repo1pct.xlsx` `b52a4e3556b1d401799a4b43094bf2a5`, `Repo2pct.xlsx`
  `4b23a459726b4e37260e89a9bf322e98`, `Porcentaje_glucosa_1hoja.xlsx`
  `5739845d5007a0c10797a0f84b54499f`.
- `Repo2pct.xlsx` has nine sheets, `29_2%` to `45_2%`; three of them carry a suffix
  (`37_2%n2`, `39_2%n`, `43_2%n`).

## EX1: Read, write and plot

- Step 1: the first rows show the columns `Time`, `tcultivo (min)`, `T° 600`, the wells
  `A7` to `H7` and `Average`. `hours[above][0]` picks the first hour at which `od > 0.4`
  is `True`.
- Steps 2–3: `data/processed/` holds `ecoli-growth-29c-1pct-hours.csv`,
  `ecoli-growth-37c-1pct-hours.csv` and `ecoli-growth-45c-1pct-hours.csv`, each the raw
  table plus `time_h`. Answer styles tested: a loop over the three temperatures, or three
  separate reads; `/ 60` on the column or on `.to_numpy()`. What to watch for: an answer
  that writes into `RAW` or overwrites the raw files breaks the rule of the experiment;
  an answer without `index=False` adds an unnamed index column, which works but is not an
  unchanged table; an answer with an absolute path such as `/home/jovyan/work/...` runs
  only on this account.
- Step 4: three curves in one figure, with the axis labels "Culture time (h)" and
  "Optical density", a legend and a title. 37 °C rises first and levels off at about
  0.53 after 4 h; 45 °C rises early but levels off lowest, near 0.4; 29 °C starts late.
  What to watch for: a figure saved before the labels are set, or with `plt.show()`
  before `savefig`, can come out empty or without labels. Open the PNG to check. An
  answer that ends in `plt.close()` saves the PNG but shows no figure below the cell: it
  was written as a script, not for a notebook. Delete that line, or ask again and say
  that you work in a Jupyter notebook.
- Step 5: the commit holds `growth_curves.ipynb`, the three processed files and
  `results/figures/growth-curves-1pct.png`.

## EX2: Fetch data from a repository

- Step 1: the answer is one dictionary. Under `metadata` are the title, the authors and
  the licence; `files` is a list with one dictionary per file, each with `key` (the file
  name), `size`, `checksum` and `links`, where `links["self"]` is the download link.
- Step 2: the title is "Optical Density Data from the Growth of Escherichia coli at
  Different Temperatures and Glucose Concentrations", and the five files are listed
  under "Results that do not depend on the LLM". `record['metadata']['title']` picks a
  field in two steps: first the dictionary under `metadata`, then its `title`.
- Step 3: both lines show `4b23a459726b4e37260e89a9bf322e98`. Answer styles tested:
  `urllib.request.urlopen` or `urllib.request.urlretrieve`, a search for the file with a
  loop or with `next(...)`. What to watch for: an answer that compares the MD5 with the
  whole checksum string `"md5:4b23…"` never matches; strip the `md5:` first. An answer
  that saves the file first and checks afterwards leaves a bad file in `data/raw/` when
  the checksum differs. An answer that builds the URL by hand works for `Repo2pct.xlsx`,
  but fails with `UnicodeEncodeError` for names such as `Repo0·1pct.xlsx`; the link from
  the API always works.
- Step 4: nine files, `ecoli-growth-29c-2pct.csv` to `ecoli-growth-45c-2pct.csv`.
  `pd.read_excel(..., sheet_name=None)` reads all sheets into a dictionary. The
  temperature is the part of the sheet name before `_`. What to watch for: an answer that
  uses the whole sheet name gives file names with `%` and suffixes such as `n2`, against
  the naming rule.
- Step 5: the Git panel lists `growth_curves.ipynb`, `data/raw/Repo2pct.xlsx` and the
  nine CSV files, and no changed file in `data/raw/`: nothing there has changed since the
  setup. The commit holds these eleven files.
- Step 6: the History tab shows your commit on top. Clicking
  `Add the starting state of m3` lists the files the setup added, among them the raw data
  in `data/raw/`.

## EX3: Fetch in a loop

- Step 2: the file name is in one line, for example `wanted = "Repo2pct.xlsx"`. A loop
  repeats the download for each file in `record["files"]`, with the file name taken from
  each entry's `key` instead of written by hand; a file already in `RAW` is only checked,
  not downloaded again.
- Steps 3–4: four lines, in the record's order: `Repo2pct.xlsx present`,
  `Repo0·5pct.xlsx downloaded`, `Repo1pct.xlsx present`, `Repo0·1pct.xlsx downloaded`,
  each with a matching checksum. The second run shows all four as present.
  `Porcentaje_glucosa_1hoja.xlsx` is left out: its name does not start with `Repo`.
  What to watch for: an answer that downloads every file again on each run sends more
  requests than needed and overwrites raw files.
- Steps 5–6: see `experiment/metadata.yml` and `journal-entry.md`.
- Step 7: the Git panel lists the two workbooks and no changed file in `data/raw/`. The
  commit holds `growth_curves.ipynb`, the two workbooks, `metadata.yml` and `journal.md`.

## Skills covered

Each M3 skill, with the exercise step that practises it:

- import modules — EX1 1 (the cell `# Import the modules`), EX2 1 (`json`,
  `urllib.request`), EX2 3 (`hashlib`)
- use relative paths — EX1 1–3 (`RAW`, `PROCESSED`, `FIGURES`, relative to the notebook)
- read CSV and text files with pandas — EX1 1 and 2–3 (CSV), EX2 4 (the workbook's
  sheets); the API's JSON text in EX2 1–2 is read with `json`
- write files with pandas — EX1 2–3, EX2 4
- apply file naming conventions — EX1 2–3 and EX2 4, by the rule in the experiment's
  README § Files and names
- keep raw data read-only — EX1 2–3 (results go to `data/processed/`), EX2 3 (a download
  is added, nothing is overwritten), EX3 2–4 (files already present are only checked)
- separate raw and processed data — EX1 3, EX2 4
- fetch data from a repository via API — EX2 1–3, EX3 2–4
- verify a download by checksum — EX2 3, EX3 3–4
- use numpy arrays — EX1 1 (`to_numpy()`, a division for all readings, a True/False
  array as a filter)
- create plots with matplotlib — EX1 4
- label and style plots — EX1 4 (axis labels with units, legend, title)
- save figures — EX1 4
- view a file's history in Git — EX2 6 (the History tab of the Git panel)
- check in Git that raw data is unchanged — EX2 5, EX3 7 (the Git panel lists no changed
  file in `data/raw/`)

Requirements from earlier modules used here: run cells (EX1 1), the experiment entry
(EX3 5–6), prompting an LLM and reviewing its code (EX1 2–4, EX2 3–4, EX3 2–3), reading
error messages (whenever an answer fails), a commit in the Git panel (EX1 5, EX2 5,
EX3 7).
