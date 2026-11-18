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
- No mean equals the threshold 1000, so `>` and `>=` give the same genes.

## Small exercise

- Genes above 1000: `FBgn0000042`, `FBgn0025111`, `FBgn0261552`. `FBgn0039155` (797.0) is
  the near miss, a good gene for the hand check.
- Answer styles tested: a loop with `sum(values) / len(values)`, `statistics.mean`, a
  dictionary of means filtered afterwards, sorted or unsorted output. All give the three
  genes.
- What to watch for: an answer that hard-codes `/ 7` works here but breaks with another
  number of samples; an answer that imports pandas or numpy also works, but is not what
  was asked for. Both are review points, not errors.

## Larger exercise

- The traceback ends in `ValueError: invalid literal for int() with base 10: 'rep1'`,
  raised in `parse_sample_name` at `int(replicate)`, called from the loop
  `sample_info[name] = parse_sample_name(name)`.
- Step 3: `"ctrl_rep1".split("_")` gives `['ctrl', 'rep1']`, so `int()` gets `'rep1'`.
- Fix: `int(replicate.removeprefix("rep"))`. Equivalent fixes: `replicate[3:]`,
  `replicate.replace("rep", "")`, a regular expression. Everything after the parser was
  already right; the rest of the cell then runs.
- Step 5: `(70 + 38 + 52) / 3` = 53.33.
- Steps 6–7: the Markdown cell under the fixed code in
  `experiment/code/explore_counts.ipynb`, and `journal-entry.md`. The Git panel lists `explore_counts.ipynb` and `journal.md`.

## Bonus exercise

- Step 1: lower in `kd`: `FBgn0039155` and `FBgn0261552` clearly; `FBgn0000008` and
  `FBgn0000014` by a fraction of a read, which means nothing for raw counts.
  `FBgn0025111` and `FBgn0000042` are higher. The big changes are worth a closer look,
  the small ones are not.
- Step 2: see `experiment/README.md` § Observations and interpretation and
  `experiment/metadata.yml`.
- Steps 3–4, malformed: `kd-rep4` (no underscore), `kd_rep` (no number), `KD_rep5`
  (condition not `ctrl` or `kd`), `ctrl_rep6_new` (two underscores). Valid: `ctrl_rep5`,
  `kd_rep4` and the seven original names.
- Answer styles tested: checks with `split` and `isdigit`, or
  `re.fullmatch(r"(ctrl|kd)_rep(\d+)", name)`. Both report the four names.
- What to watch for: a regular expression with `re.IGNORECASE` accepts `KD_rep5`;
  `re.match` instead of `re.fullmatch` accepts `ctrl_rep6_new`. A check by hand
  (step 4) catches both.

## Skills covered

Each M2 skill, with the exercise step that practises it:

- work between JupyterLab and the LLM interface — "Module-specific preparation", small
  2–3, larger 4, bonus 3
- write comments — small 4 (comments on each line), larger 6 (Markdown cell on the fix);
  read in the second code cell
- use variables and data types — small 1 (`str`, `int` in the second code cell), small 5
- use lists and dictionaries — small 1, small 5 (`counts[...]`), larger 3, larger 5
- write loops — small 1–3, larger 1
- write conditions — small 1, small 4 (the threshold condition), bonus 3–4
- prompt an LLM for code — small 2, bonus 3; larger 4 for a fix
- review LLM-generated code — small 4–5, larger 1, larger 4, bonus 4
- read error messages and tracebacks — small 3, larger 2
- debug step by step — larger 3–5

Requirements from M1 used here: run cells and restart the kernel (the notebook asks to run
the data cell after every restart), Markdown cells (larger 6), the journal entry (larger 6,
bonus 5), the experiment entry (bonus 2), committing (small 6, larger 7, bonus 5).
