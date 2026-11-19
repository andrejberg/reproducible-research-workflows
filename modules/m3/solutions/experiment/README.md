# E. coli growth at three temperatures with 1 % glucose

This experiment compares the growth curves of *E. coli* at 29, 37 and 45 °C with 1 %
glucose, read from files, and fetches more of the same dataset from its repository.

Structured metadata, input and output paths and the software environment are recorded in
[`metadata.yml`](metadata.yml).

## Purpose

How does temperature change the growth of *E. coli* with 1 % glucose? Does more glucose
change the picture?

## Method

1. The optical density of eight wells per temperature was read on a plate reader every
   5 minutes for 24 hours (see Data credit). The column `Average` is the mean of the
   eight wells, computed in the source workbook; `tcultivo (min)` is the culture time in
   minutes.
2. `code/growth_curves.ipynb` reads the three CSV files in `data/raw/` with pandas, adds
   the culture time in hours, writes the tables to `data/processed/` and plots the three
   curves.
3. The same notebook fetches more workbooks of the dataset from Zenodo through its API and
   checks each download against the checksum the repository lists.

## Files and names

- `data/raw/` holds the data as it came from its source. Nothing in it is ever changed: a
  new download is added next to the other files.
  - `Repo1pct.xlsx`: the original workbook for 1 % glucose, one sheet per temperature,
    downloaded at setup.
  - `ecoli-growth-29c-1pct.csv`, `ecoli-growth-37c-1pct.csv`, `ecoli-growth-45c-1pct.csv`:
    the sheets `29_1%b`, `37_1%n2` and `45_1%b` of `Repo1pct.xlsx`, exported to CSV
    unchanged.
- `data/processed/` holds tables the code computes from raw data.
- `results/figures/` holds figures.
- File names are lowercase, with words joined by hyphens and no spaces: the dataset, the
  temperature, the glucose concentration, then what was done, for example
  `ecoli-growth-37c-1pct-hours.csv`.

## Data generated or processed

- `data/processed/ecoli-growth-29c-1pct-hours.csv`, `…-37c-…` and `…-45c-…`: the three
  raw tables with the added column `time_h`, the culture time in hours.
- `data/processed/ecoli-growth-29c-2pct.csv` to `ecoli-growth-45c-2pct.csv`: the nine
  sheets of `Repo2pct.xlsx` (2 % glucose), converted to CSV unchanged.
- `results/figures/growth-curves-1pct.png`: the mean optical density over 24 hours at 29,
  37 and 45 °C with 1 % glucose, in one figure.
- `data/raw/Repo2pct.xlsx`, `Repo0·1pct.xlsx` and `Repo0·5pct.xlsx`: the other glucose
  workbooks, fetched from Zenodo through its API, each checked against the record's MD5.

## Observations and interpretation

- What was expected? Fastest growth near 37 °C, slower growth at the lower and the
  higher temperature.
- What was observed? At 37 °C the optical density is above 0.4 after 2.3 h and levels off
  at about 0.53 after 4 h, then rises slowly to 0.58. At 45 °C it rises early but levels
  off lowest, at about 0.4; at 29 °C it starts late (above 0.4 after 6.4 h) and reaches
  about 0.53. With 2 % glucose the curves at 29 and 37 °C look almost the same; at 45 °C
  the optical density passes 0.4 only after 14.2 h instead of 10.2 h.
- What errors, warnings or unexpected results occurred? Reading the workbook gives the
  warning `Workbook contains no default style`, which is harmless. The sheets of a
  workbook do not all have the same columns: from 39 to 43 °C the temperature column is
  `T° Read 1:600`, not `T° 600`.

## Reproducing this experiment

1. Open the experiment folder in JupyterLab.
2. Run `code/growth_curves.ipynb` from top to bottom (Run → Run All Cells). It needs
   network access to fetch from Zenodo.

## Limitations and next steps

- Three of nine temperatures, and one plate reader run per condition.
- The source does not say whether the optical density is blank-corrected.

## Data credit

The data is "Optical Density Data from the Growth of *Escherichia coli* at Different
Temperatures and Glucose Concentrations" by María Isabel González Siso, Manuel Becerra,
Daniel Torrecilla, Ana-María Díaz-Díaz, Jorge López-Beceiro and Ramón Artiaga, published on
Zenodo under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
<https://doi.org/10.5281/zenodo.19416053>. The CSV files are sheets of its workbook
`Repo1pct.xlsx`, exported unchanged.
