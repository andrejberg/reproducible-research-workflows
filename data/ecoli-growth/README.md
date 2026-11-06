# E. coli growth curves — example dataset

The example dataset of these materials: optical density of
*Escherichia coli* growing at nine temperatures (29–45 °C) in media with four glucose
concentrations (0.1, 0.5, 1 and 2 %), read on a plate reader every 5 minutes for 24 hours.

## Source and licence

- **Creators**: María Isabel González Siso, Manuel Becerra, Daniel Torrecilla,
  Ana-María Díaz-Díaz, Jorge López-Beceiro, Ramón Artiaga
- **Title**: Optical Density Data from the Growth of *Escherichia coli* at Different
  Temperatures and Glucose Concentrations
- **Published**: Zenodo, 2026-04-04, <https://doi.org/10.5281/zenodo.19416053>
- **Licence**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the
  creators and the DOI wherever the data or files derived from it are shared, including
  every module README.

The source files are Excel workbooks. They stay unmodified on Zenodo and are not stored in
this repository. A module that needs one downloads it at setup: its `setup.json` names the
URL and the MD5 from the table below (see "Module layout" in the main `README.md`). The URL
of a file is `https://zenodo.org/api/records/19416053/files/<source file>/content`, with
`·` written as `%C2%B7`.

| Source file | Content | MD5 (as published by Zenodo) |
|---|---|---|
| `Repo0·1pct.xlsx` | 0.1 % glucose, one sheet per temperature | `d4abd96f8b3cc135eba7f341308baec6` |
| `Repo0·5pct.xlsx` | 0.5 % glucose, one sheet per temperature | `bf807e8d5ab42a8adbd863aa2d06d739` |
| `Repo1pct.xlsx` | 1 % glucose, one sheet per temperature | `b52a4e3556b1d401799a4b43094bf2a5` |
| `Repo2pct.xlsx` | 2 % glucose, one sheet per temperature | `4b23a459726b4e37260e89a9bf322e98` |
| `Porcentaje_glucosa_1hoja.xlsx` | all conditions on one sheet, as d(OD)/dt | `5739845d5007a0c10797a0f84b54499f` |

## Files here

| File | What it is |
|---|---|
| `make_sample.py` | Downloads `Repo1pct.xlsx`, checks its MD5, exports sheet `37_1%n2` to CSV unchanged |
| `ecoli-growth-37c-1pct.csv` | The smoke-test sample: 37 °C, 1 % glucose, 289 readings. SHA-256 `b7d99a36eed7cbfcd567a3ca4e9950f92a70a808176c92c9c7a1bb64e4d82324` |

Regenerate the sample from the repository root with `uv run data/ecoli-growth/make_sample.py`.

## Columns of a sheet

| Column | Meaning |
|---|---|
| `Time` | elapsed time as `HH:MM:SS` |
| `tcultivo (min)` | culture time in minutes (Spanish: *tiempo de cultivo*) |
| `T° 600` | temperature in °C logged by the reader with the 600 nm reading |
| `A7` … `H7` | optical density of one well each; the number is the plate column and differs between sheets |
| `Average` | mean of the wells, computed in the source workbook |

## Known gaps in the source metadata

The Zenodo record describes the data in one sentence. Not stated there:

- the strain, the medium apart from glucose, the instrument and the plate type
- what the sheet-name suffixes `b`, `n` and `n2` mean (e.g. `29_1%b`, `37_1%n2`)
- whether optical density was read at 600 nm (suggested by the column `T° 600`) and
  whether it is blank-corrected
- a linked publication

Each of the four `Repo*.xlsx` workbooks holds nine sheets (29–45 °C in 2 °C steps) with
eight wells, an `Average` column and 289 readings. In `Repo0·5pct.xlsx` the sheets are
not in temperature order.

The modules use these gaps as teaching material on metadata and provenance; do not fill
them with guesses.
