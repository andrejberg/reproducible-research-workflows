# M1 reference solution

The exercises are in `modules/m1/README.md` (in your project:
`work/rrw-workshop/M1_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-03_ecoli-growth-37c/`
  after all three exercises: `README.md` and `metadata.yml`. The notebook and the data
  file are unchanged and not repeated here.
- `journal-entry.md` — the entry at the top of `work/rrw-workshop/journal.md`.

Names and dates in the solution (author, `2026-11-30`) are examples. Your wording will
differ; what matters is that the same information is there.

## EX1: JupyterLab and the kernel

- Step 2: after the restart, the third cell fails with
  `NameError: name 'hours' is not defined`. A restart ends the kernel process and with it
  every variable; the notebook file keeps the code and the old output, but nothing is in
  memory until the cells run again from the top.
- Step 3: the new notebook fails with `NameError: name 'growth' is not defined`. Each
  notebook has its own kernel, so the new notebook does not see the variables of
  `growth_curve.ipynb`. The interpreter is the Python program installed in the lab; a
  kernel is one running process of it, started for one notebook.
- Step 4: running the notebook changed `growth_curve.ipynb` (its outputs) and created
  `results/figures/growth-curve.png`. With simple staging, one commit takes both.

## EX2: A complete experiment entry

- README and metadata: see `experiment/`, which also has the EX3 answers. After EX2
  alone, the values from the record (`source`, `source_version`, `licence`, `checksum`,
  `reuse.licence`) are still `null`. EX2 asks for the purpose and the method; the other
  sections of `experiment/README.md` are answered as an example, and in your entry they
  may keep their questions. Outputs list `results/figures/growth-curve.png` with
  role `figure`. Leaving an unknown value `null` is correct: a guessed value is worse than
  an empty one, and the file shows what is still open.
- Journal: see `journal-entry.md`, without its `EX3:` line.
- A good group rule: the README explains the experiment so that it can be understood
  without anything else (purpose, method, observations, how to reproduce); the journal
  records what happened when, briefly, across experiments, and points to the experiment
  for details.
- Commit: the Git panel lists the changed `README.md`, `metadata.yml` and `journal.md`.
  The notebook and the figure were committed in EX1.

## EX3: Metadata from the data record

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
- Journal: the `EX3:` line in `journal-entry.md` updates the entry. Gaps in the record (also in
  `~/data/ecoli-growth/README.md` § Known gaps in the source metadata): strain, medium
  apart from glucose, instrument and plate type; whether optical density was read at
  600 nm and blank-corrected; what the sheet-name suffixes mean; no linked publication.
- Commit: the Git panel lists the changed `metadata.yml` and `journal.md`.

## Skills covered

Each M1 skill, with the exercise step that practises it:

- navigate the JupyterLab interface — the set-up (terminal, file browser; repository
  README § Set up the module), EX1 step 1
- create and open notebooks — EX1 step 1 (open), EX1 step 3 (create)
- run cells — EX1 steps 1–2
- restart the kernel — EX1 step 2
- save notebooks — EX1 step 4
- explain kernel vs. interpreter — EX1 step 3
- apply the directory template — EX2 steps 1–2 (the template's sections and fields), EX3
  step 1 (the template experiment)
- create an experiment entry — the set-up adds the folder; EX2 steps 1–3 and 5 make it a
  complete entry
- write a journal entry — EX2 step 3, EX3 step 4
- write a README — EX2 step 1
- open the Git panel — EX1 step 4
- commit an experiment entry — EX1 step 4, EX2 step 5, EX3 step 5
