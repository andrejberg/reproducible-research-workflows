# Fit an E. coli growth curve

This experiment fits a logistic growth model to optical-density data for *E. coli* grown
at 37 °C in 1 % glucose.

Structured metadata, input/output paths, software environment,
and provenance links are recorded in [`metadata.yml`](metadata.yml).

## Purpose

Determine whether a logistic growth model describes the observed optical-density increase,
and estimate the steepest growth slope.

## Method

1. Read the raw optical-density table and keep culture time, temperature and the mean of
   the eight wells.
2. Check for missing values and increasing time, and write a processed table.
3. Fit a logistic curve with a constant offset using `scipy.optimize.curve_fit`, over all
   289 readings.
4. Save the fitted parameters and a figure of the fit with its residuals.

No reading was excluded and there was no deviation from this plan.

## Data generated or processed

This experiment produces:

- `data/processed/ecoli-growth-37c-1pct-clean.csv`: the three columns used, renamed
- `results/figures/growth_curve_fit.png`: the data, the fitted curve and the residuals
- `results/tables/fit_parameters.csv`: the fitted parameters with standard errors

## Observations and interpretation

- Expected: a rise in optical density that levels off.
- Observed: optical density rises from 0.14 to about 0.53 within roughly the first
  250 minutes. After that it keeps rising slowly, to 0.58 at the end of the 24 hours.
- The fit gives R² = 0.981 and a steepest slope of 0.0026 OD per minute, at a midpoint of
  about 102 minutes.
- The residuals are not random. The model has a flat plateau, so it cannot follow the slow
  later rise: it lies above the data around 400 minutes and below it at the end.
- Decision: keep all readings, because no reading gives a documented reason to exclude it.
- Interpretation: the logistic curve describes the main growth phase, but it does not
  describe the whole experiment, despite the high R².

## Reproducing this experiment

1. Open the experiment folder in JupyterLab.
2. Ensure that the environment recorded in `metadata.yml` is active.
3. Run `code/01_clean_data.ipynb`.
4. Run `code/02_fit_growth_model.ipynb`.
5. Check that the outputs listed in `metadata.yml` have been created.

## Limitations and next steps

- Only one temperature and glucose concentration are analysed here.
- The source does not state whether optical density is blank-corrected, so the starting
  value of 0.14 and the fitted offset should not be read as a cell density.
- The fit uses the mean of the wells and ignores the differences between them.
- Next step: compare fitted parameters across temperatures.

## Data credit

María Isabel González Siso, Manuel Becerra, Daniel Torrecilla, Ana-María Díaz-Díaz,
Jorge López-Beceiro, Ramón Artiaga: Optical Density Data from the Growth of *Escherichia
coli* at Different Temperatures and Glucose Concentrations. Zenodo, 2026,
<https://doi.org/10.5281/zenodo.19416053>, CC BY 4.0.
