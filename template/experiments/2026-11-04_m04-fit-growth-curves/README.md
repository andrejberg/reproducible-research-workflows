# Fit E. coli growth curves

*This is an illustrative example. It shows what a filled-in entry looks like; it is not a real result, and the files it names are not included.*

This experiment fits a logistic growth model to optical-density data
for *E. coli* grown at 24 °C in 1 % glucose.

Structured metadata, input/output paths, software environment,
and provenance links are recorded in [`metadata.yml`](metadata.yml).

## Purpose

Determine whether a logistic growth model describes the observed
optical-density increase and estimate the maximum growth rate.

## Method

1. Read the raw optical-density table.
2. Convert time and optical-density columns to numeric values.
3. Fit a logistic growth model using `scipy.optimize.curve_fit`.
4. Save the fitted curve and parameter estimates.

## Data generated or processed

This experiment produces:

- a cleaned data table in `data/processed/`
- a fitted growth curve in `results/figures/`
- fitted parameter estimates in `results/tables/`

## Observations and interpretation

- The initial optical density is not exactly zero.
- The fitted curve describes the observed growth trend well.
- The first two time points were excluded because of instrument equilibration.
- The fitted maximum growth rate should be interpreted only for this
  temperature and glucose concentration.

## Reproducing this experiment

1. Open the experiment folder in JupyterLab.
2. Ensure that the environment recorded in `metadata.yml` is active.
3. Run `code/01_clean_data.ipynb`.
4. Run `code/02_fit_growth_model.ipynb`.
5. Check that the outputs listed in `metadata.yml` have been created.

## Limitations and next steps

- The model assumes logistic growth and may not describe all growth phases.
- Only one temperature and glucose concentration are analysed here.
- Next step: compare fitted growth rates across temperatures.
