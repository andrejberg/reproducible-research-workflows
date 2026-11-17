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

- README and metadata: see `experiment/`. Outputs list `results/figures/growth-curve.png`
  with role `figure`.
- Journal: see `journal-entry.md`.
- Commit: the Git panel lists the changed `README.md`, `metadata.yml`, `growth_curve.ipynb`,
  `journal.md` and the new `results/figures/growth-curve.png`. With simple staging, one
  commit takes all of them.
- A good group rule: the README explains the experiment so that it can be understood
  without anything else (purpose, method, observations, how to reproduce); the journal
  records what happened when, briefly, across experiments, and points to the experiment
  for details.

## Bonus exercise

From the record at <https://doi.org/10.5281/zenodo.19416053>:

- `source`: the DOI.
- `source_version`: the record has no version number. It is one version of the concept
  DOI 10.5281/zenodo.16944298, published 2026-04-04. Either the date or "not stated" is
  a good answer if the comment says why.
- `licence` and `reuse.licence`: CC BY 4.0.
- `checksum`: the record lists `md5:b52a4e3556b1d401799a4b43094bf2a5` for `Repo1pct.xlsx`.
  It is the workbook's checksum, not the CSV's, which the comment must say.
- Gaps for the journal (also in `~/data/ecoli-growth/README.md` § Known gaps in the
  source metadata): strain, medium apart from glucose, instrument and plate type; whether
  optical density was read at 600 nm and blank-corrected; what the sheet-name suffixes
  mean; no linked publication.

## Skills covered

Each M1 skill, with the exercise step that practises it:

- navigate the JupyterLab interface — set-up steps 1–3 (terminal, file browser), small 1
- create and open notebooks — small 1 (open), small 4 (create)
- run cells — small 1–3
- restart the kernel — small 3, small 5
- save notebooks — small 6
- write Markdown cells — small 6
- explain kernel vs. interpreter — small 4–5
- apply the directory template — larger 1–2 (against the template experiment)
- create an experiment entry — set-up step 1 adds the folder; larger 1–4 make it a
  complete entry
- write a journal entry — larger 3, bonus 3
- write a README — larger 1
- open the Git panel — larger 4
- commit an experiment entry — larger 4, bonus 4
