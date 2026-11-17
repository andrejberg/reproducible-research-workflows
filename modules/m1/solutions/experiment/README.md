# E. coli growth at 37 °C with 1 % glucose: a first look

This experiment plots the published growth curve of *E. coli* at 37 °C with 1 % glucose,
to see the phases of growth before the data is used in later analyses.

Structured metadata, input and output paths and the software environment are recorded in
[`metadata.yml`](metadata.yml).

## Purpose

What does a single growth curve of *E. coli* at 37 °C with 1 % glucose look like over
24 hours, and which growth phases can be seen in it?

## Method

1. Read the plate-reader data from `data/raw/ecoli-growth-37c-1pct.csv`.
2. Take the culture time in minutes, convert it to hours, and use the `Average` column,
   the mean optical density of the eight wells computed in the source workbook.
3. Plot optical density against culture time and save the figure.

No deviation from this plan.

## Data generated or processed

This experiment produces:

- `results/figures/growth-curve.png`: optical density against culture time

## Observations and interpretation

- Expected: a lag phase, exponential growth and a stationary phase.
- Observed: optical density rises from 0.14 to about 0.53 in the first 4 hours, with
  hardly any lag, then creeps up slowly to 0.58 at 24 hours.
- The single well `A7` has the same shape but stays below the average (about 0.49 at
  4 hours), so the wells differ.
- Interpretation: growth is fast at first and almost stops after 4 hours. No lag phase is
  visible at the 5-minute resolution. This is a description only; no growth rate was
  fitted.

## Reproducing this experiment

1. Open the experiment folder in JupyterLab.
2. Ensure that the environment recorded in `metadata.yml` is active.
3. Run `code/growth_curve.ipynb` from top to bottom (Run → Run All Cells).
4. Check that `results/figures/growth-curve.png` is created.

## Limitations and next steps

- The source record does not say which strain, medium or instrument was used, or whether
  the optical density is blank-corrected.
- One temperature and one glucose concentration only.
- Next: compare temperatures and glucose concentrations.

## Data credit

`data/raw/ecoli-growth-37c-1pct.csv` is the sheet `37_1%n2` of the workbook
`Repo1pct.xlsx`, exported to CSV unchanged. The workbook is part of "Optical Density Data
from the Growth of *Escherichia coli* at Different Temperatures and Glucose Concentrations"
by María Isabel González Siso, Manuel Becerra, Daniel Torrecilla, Ana-María Díaz-Díaz,
Jorge López-Beceiro and Ramón Artiaga, published on Zenodo under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
<https://doi.org/10.5281/zenodo.19416053>.
