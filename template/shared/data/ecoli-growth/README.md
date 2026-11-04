# E. coli growth curves

This folder contains the shared reference data that experiments in this project copy from.

## Source

- Creators: María Isabel González Siso, Manuel Becerra, Daniel Torrecilla,
  Ana-María Díaz-Díaz, Jorge López-Beceiro, Ramón Artiaga
- Title: Optical Density Data from the Growth of *Escherichia coli* at Different
  Temperatures and Glucose Concentrations
- DOI: <https://doi.org/10.5281/zenodo.19416053>
- Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the creators
  and the DOI wherever the data or files derived from it are shared.
- Contents of the full dataset: optical-density growth curves at nine temperatures
  (29–45 °C) and four glucose concentrations (0.1, 0.5, 1 and 2 %).

## Files here

`raw/ecoli-growth-37c-1pct.csv` is one sheet of the published workbook `Repo1pct.xlsx`
(sheet `37_1%n2`: 37 °C, 1 % glucose), exported to CSV unchanged. It has 289 readings.
SHA-256: `b7d99a36eed7cbfcd567a3ca4e9950f92a70a808176c92c9c7a1bb64e4d82324`

The published workbooks hold the other conditions. They stay on Zenodo.

## Use in experiments

Experiment folders may contain copied subsets of these data in their own `data/raw/`
folders. The copied files remain unmodified.

## Provenance

- Original files are stored in `raw/`.
- Do not edit files in `raw/`.
- Any cleaned, filtered, converted or derived version belongs in the relevant experiment
  folder under `data/processed/`.
