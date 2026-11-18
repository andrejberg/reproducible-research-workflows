# M1 reference solution

The exercises are in `modules/m1/README.md` (in your project:
`work/rrw-workshop/M1_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-03_ecoli-growth-37c/`
  after all three exercises: `README.md`, `metadata.yml` and `code/growth_curve.ipynb`
  (with the Markdown cell of the small exercise). The data file is unchanged and not
  repeated here.
- `journal-entry.md` — the entry at the top of `work/rrw-workshop/journal.md`.

Names and dates in the solution (author, `2026-11-30`) are examples. Your wording will
differ; what matters is that the same information is there.

## Small exercise

- Step 2: with `growth["A7"]` the curve has the same shape but lies a little lower
  (about 0.49 instead of 0.53 after 4 hours). Only the cells that are run again change.
- Step 3: after the restart, the third cell fails with
  `NameError: name 'hours' is not defined`. A restart ends the kernel process and with it
  every variable; the notebook file keeps the code and the old output, but nothing is in
  memory until the cells run again from the top.
- Step 4: the new notebook fails with `NameError: name 'growth' is not defined`. Each
  notebook has its own kernel, so the new notebook does not see the variables of
  `growth_curve.ipynb`.
- Step 5: the interpreter is, for example, `/srv/conda/envs/notebook/bin/python` in the
  Jupyter4NFDI image, before and after the restart. The kernel process number is
  different after the restart. The interpreter is the Python program; a kernel is one
  running process of it, started for one notebook, and holds that notebook's variables.
  A restart ends that process and starts a new one, so the variables are gone.
- Step 6: see the first cell of `experiment/code/growth_curve.ipynb`.

## Larger exercise

- README and metadata: see `experiment/`, which also has the bonus answers. After the
  larger exercise alone, the values from the record (`source`, `source_version`,
  `licence`, `checksum`, `reuse.licence`) are still `null`, and sections you could not
  answer yet keep their questions. Outputs list `results/figures/growth-curve.png` with
  role `figure`.
- Commit: the Git panel lists the changed `README.md`, `metadata.yml`, `growth_curve.ipynb`
  and the new `results/figures/growth-curve.png`. With simple staging, one commit takes
  all of them.
- What stays empty, and why: the licence, source version and checksum of the input are
  in the dataset's record, which you have not read yet (bonus). `date_completed` is known
  only when the experiment is done. `contact` and `related_experiment` may never apply.
  Leaving them `null` is correct: a guessed value is worse than an empty one, and the
  file shows what is still open.

## Bonus exercise

- Template: the template experiment also has `data/processed/` (derived data that code
  recreates from raw data) and `results/tables/` (generated tables). This experiment
  writes neither, so it does not need those folders: an experiment holds only what it
  uses. `work/rrw-workshop/README.md` § Experiment convention explains each folder.

From the record at <https://doi.org/10.5281/zenodo.19416053>:

- `source`: the DOI.
- `source_version`: the record has no version number. It is one version of the concept
  DOI 10.5281/zenodo.16944298, published 2026-04-04. Either the date or "not stated" is
  a good answer if the comment says why.
- `licence` and `reuse.licence`: CC BY 4.0.
- `checksum`: the record lists `md5:b52a4e3556b1d401799a4b43094bf2a5` for `Repo1pct.xlsx`.
  It is the workbook's checksum, not the CSV's, which the comment must say.
- Journal: see `journal-entry.md`. Gaps in the record (also in
  `~/data/ecoli-growth/README.md` § Known gaps in the source metadata): strain, medium
  apart from glucose, instrument and plate type; whether optical density was read at
  600 nm and blank-corrected; what the sheet-name suffixes mean; no linked publication.

## Skills covered

Each M1 skill, with the exercise step that practises it:

- navigate the JupyterLab interface — the set-up (terminal, file browser; repository
  README § Set up the module), small 1
- create and open notebooks — small 1 (open), small 4 (create)
- run cells — small 1–3
- restart the kernel — small 3, small 5
- save notebooks — small 6
- write Markdown cells — small 6
- explain kernel vs. interpreter — small 4–5
- apply the directory template — larger 1–2 (the template's sections and fields), bonus 1
  (the template experiment)
- create an experiment entry — the set-up adds the folder; larger 1–3 make it a complete
  entry
- write a journal entry — bonus 4
- write a README — larger 1
- open the Git panel — larger 3
- commit an experiment entry — larger 3, bonus 5
