# Research project template

A reusable structure for documenting quantitative research. Copy this folder to start a
project of your own.

Each folder in `experiments/` is a self-contained experiment entry. It contains its own
documentation, data, code and results.

## Structure

```text
project/
├── README.md
├── journal.md
├── environment.yml
├── .gitignore
├── shared/
└── experiments/
```

| Path | What it is |
|---|---|
| `journal.md` | The chronological record of the project: decisions, progress, problems, next steps |
| `environment.yml` | The software environment, with exact package versions |
| `.gitignore` | Files Git should not track, such as Jupyter checkpoints |
| `shared/data/` | The complete reference dataset with its source, licence and provenance |
| `shared/code/` | Functions used by more than one experiment |
| `experiments/` | One folder per experiment |

## Experiment convention

```text
YYYY-MM-DD_experiment-name/
├── README.md
├── metadata.yml
├── data/
│   ├── raw/
│   └── processed/
├── code/
└── results/
    ├── figures/
    └── tables/
```

- `README.md` explains the experiment in human-readable form.
- `metadata.yml` records structured facts: paths, licences, environment and provenance.
- `data/raw/` holds original or copied source data. Never edit these files.
- `data/processed/` holds derived data that can be recreated from raw data and code.
- `code/` holds notebooks, scripts and configuration.
- `results/` holds generated figures and tables.

An experiment never reads files from another experiment. If two experiments need the same
data, each one copies it from `shared/data/` into its own `data/raw/`.

## Start a new experiment

Run these commands from this folder, with your own date and a short name:

```bash
cp -r experiments/YYYY-MM-DD_experiment-name experiments/2026-11-04_my-experiment
cp shared/data/ecoli-growth/raw/ecoli-growth-37c-1pct.csv experiments/2026-11-04_my-experiment/data/raw/
```

Keep the folder `YYYY-MM-DD_experiment-name` unchanged, so that you can copy it again.
You can delete a `.gitkeep` file once its folder holds a real file. It only makes Git keep
the empty folder.

Then:

1. Fill in `metadata.yml`: the experiment's ID, title and date, and its inputs.
2. Write the purpose and planned method in `README.md`.
3. Put your code in `code/`. Read and write with paths relative to the notebook, such as
   `../data/raw/`.
4. Write generated outputs to `data/processed/` and `results/`, and list them in
   `metadata.yml`.
5. Record your observations and interpretation in `README.md`.
6. Add a short entry to `journal.md`.
7. Commit the experiment folder in Git.

## Example

`experiments/2026-11-04_m04-fit-growth-curves/` is a finished entry that you can read and
rerun. Its README shows what a filled-in entry looks like, and its `metadata.yml` links
each output to its input and code.

## Data credit

The example data is by González Siso et al., published under CC BY 4.0 at
<https://doi.org/10.5281/zenodo.19416053>. See `shared/data/ecoli-growth/README.md`.
