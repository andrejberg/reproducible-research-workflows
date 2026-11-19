# M2 reference solution

The exercises are in `modules/m2/README.md` (in your project:
`work/rrw-workshop/M2_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-04_pasilla-knockdown-counts/`
  after all three exercises: `README.md` (observations filled in), `metadata.yml` (author,
  dates, status) and `code/explore_counts.ipynb` (one possible answer per exercise).
- `journal-entry.md` — the entry at the top of `work/rrw-workshop/journal.md`.

Names and dates in the solution (author, `2026-11-30`) are examples.

## Results that do not depend on the LLM

Every LLM run and every service gives different code. Check the results, not the code.
These values follow from the data:

- Mean over all seven samples: `FBgn0000008` 99.6, `FBgn0000014` 1.4, `FBgn0000042`
  86,790.6, `FBgn0025111` 1,563.1, `FBgn0039155` 797.0, `FBgn0261552` 5,816.9.
- Mean per condition (`ctrl` → `kd`): `FBgn0000008` 99.75 → 99.33, `FBgn0000014`
  1.5 → 1.33, `FBgn0000042` 80,227 → 95,542, `FBgn0025111` 422.25 → 3,084.33,
  `FBgn0039155` 1,354.75 → 53.33, `FBgn0261552` 8,439 → 2,320.67.
- No mean equals the threshold 100, so `>` and `>=` give the same genes.

## Small exercise

- Genes above 100: `FBgn0000042`, `FBgn0025111`, `FBgn0039155`, `FBgn0261552`.
  `FBgn0000008` (99.6) is the near miss, a good gene for the hand check (step 5).
- Answer styles tested: a loop with `sum(values) / len(values)`, `statistics.mean`, a
  dictionary of means filtered afterwards, sorted or unsorted output. All give the four
  genes.
- What to watch for: an answer that hard-codes `/ 7` works here but breaks with another
  number of samples; an answer that imports pandas or numpy also works, but is not what
  was asked for. Both are review points, not errors. An answer that uses `threshold`
  without setting it takes `threshold = 1000` from the Python-syntax cell and lists only
  three genes; the hand check of `FBgn0039155` (797.0) shows it.

## Larger exercise

- The traceback ends in `ValueError: invalid literal for int() with base 10: 'rep1'`,
  raised in `parse_sample_name` at `int(replicate)`, called from the loop
  `sample_info[name] = parse_sample_name(name)`.
- Step 3: `"ctrl_rep1".split("_")` gives `['ctrl', 'rep1']`, so `int()` gets `'rep1'`.
- Fix: `int(replicate.removeprefix("rep"))`. Equivalent fixes: `replicate[3:]`,
  `replicate.replace("rep", "")`, a regular expression. The rest of the cell then runs, and
  `pprint(sample_info)` shows the seven names, for example
  `'kd_rep3': {'condition': 'kd', 'replicate': 3}`.
- Step 5: the means per condition are listed under "Results that do not depend on the
  LLM". Answer styles: a dictionary of lists per condition, or the sum and number of
  samples per condition. What to watch for: an answer that splits the names again instead
  of using `sample_info` works too; an answer that hard-codes the first four samples as
  `ctrl` breaks with other data.
- Step 6: `(70 + 38 + 52) / 3` = 53.33.
- Steps 7–8: the Markdown cell under the fixed code in
  `experiment/code/explore_counts.ipynb`, and `journal-entry.md`. The Git panel lists `explore_counts.ipynb` and `journal.md`.

## Bonus exercise

- Step 1: lower in `kd`: `FBgn0039155` and `FBgn0261552` clearly; `FBgn0000008` and
  `FBgn0000014` by a fraction of a read, which means nothing for raw counts.
  `FBgn0025111` and `FBgn0000042` are higher. The big changes are worth a closer look,
  the small ones are not.
- Step 2: see `experiment/README.md` § Observations and interpretation and
  `experiment/metadata.yml`.
- Steps 3–4, malformed: `kd-rep4` and `ctrl8` (no underscore), `kd_rep` (no number),
  `KD_rep5` (condition not `ctrl` or `kd`), `ctrl_rep6_new` (two underscores). Valid:
  `ctrl_rep5`, `kd_rep4` and the seven original names, 9 in all.
- Answer styles tested: checks with `split` and `isdigit`, or
  `re.fullmatch(r"(ctrl|kd)_rep(\d+)", name)`. Both report the five names.
- What to watch for: a regular expression with `re.IGNORECASE` accepts `KD_rep5`;
  `re.match` instead of `re.fullmatch` accepts `ctrl_rep6_new`. A check by hand
  (step 4) catches both.

## Skills covered

Each M2 skill, with the exercise step that practises it:

- work between JupyterLab and the LLM interface — "Module-specific preparation", small
  2 and 4, larger 4–5, bonus 3
- write comments — small 3 (comments on each line), larger 7 (Markdown cell on the fix);
  read in the second code cell
- use variables and data types — small 1 (`str`, `int` in the second code cell), small 5,
  larger 4 (`str` turned into `int`)
- use lists and dictionaries — small 1, small 5 (`counts[...]`), larger 3–6
- write loops — small 1 and 3, larger 1 and 5
- write conditions — small 1, small 3 (the threshold condition), bonus 3–4
- prompt an LLM for code — small 2, larger 5, bonus 3; larger 4 for a fix
- review LLM-generated code — small 3 and 5, larger 4–6, bonus 4
- read error messages and tracebacks — small 4, larger 2
- debug step by step — larger 1–4

Requirements from M1 used here: run cells and restart the kernel (the notebook asks to run
the data cell after every restart), Markdown cells (larger 7), the journal entry (larger 7,
bonus 5), the experiment entry (bonus 2), committing (small 6, larger 8, bonus 5).
