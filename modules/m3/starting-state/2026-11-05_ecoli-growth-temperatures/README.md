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

- <processed data file and its meaning>
- <figure and its meaning>

## Observations and interpretation

- What was expected?
- What was observed?
- What errors, warnings or unexpected results occurred?

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
