# M2 reference solution

The exercises are in `modules/m2/README.md` (in your project:
`work/rrw-workshop/M2_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-04_pasilla-knockdown-counts/`
  after all three exercises: `README.md` (observations filled in), `metadata.yml` (author,
  dates, status) and `code/explore_counts.ipynb` (one possible answer per exercise).
- `journal-entry.md` — the entry at the top of `work/rrw-workshop/journal.md` (EX3 step 4).

Names and dates in the solution (author, `2026-11-30`) are examples.

## Results that do not depend on the LLM

Every LLM run and every service gives different code. Check the results, not the code.
These values follow from the data:

- Mean over all seven samples: `FBgn0000008` 99.6, `FBgn0000014` 1.4, `FBgn0000042`
  86,790.6, `FBgn0025111` 1,563.1, `FBgn0039155` 797.0, `FBgn0261552` 5,816.9.
- No mean equals the threshold 100, so `>` and `>=` give the same genes.
- Mean per condition, as the cell `# mean count per condition` prints it (`ctrl`, `kd`):
  `FBgn0000008` 99.8, 99.3; `FBgn0000014` 1.5, 1.3; `FBgn0000042` 80227.0, 95542.0;
  `FBgn0025111` 422.2, 3084.3; `FBgn0039155` 1354.8, 53.3; `FBgn0261552` 8439.0, 2320.7.
  `round()` rounds an exact half to the even digit, so 422.25 prints as 422.2.

## EX1: Python syntax

- Genes above 100: `FBgn0000042`, `FBgn0025111`, `FBgn0039155`, `FBgn0261552`.
  `FBgn0000008` (99.6) is the near miss.
- Answer styles tested: a loop with `sum(values) / len(values)`, `statistics.mean`, a
  dictionary of means filtered afterwards, sorted or unsorted output. All give the four
  genes.
- What to watch for: an answer that hard-codes `/ 7` works here but breaks with another
  number of samples; an answer that imports pandas or numpy also works, but is not what
  was asked for. Both are review points, not errors. An answer that uses `threshold`
  without setting it takes `threshold = 1000` from the cell `# Variables and data types`
  and lists only three genes; the means under "Results that do not depend on the LLM"
  show it.
- Step 4: the commit holds `explore_counts.ipynb`.

## EX2: Debugging

- The traceback ends in `ValueError: invalid literal for int() with base 10: 'rep1'`,
  raised in `parse_sample_name` at `int(replicate)`, called from the loop
  `sample_info[name] = parse_sample_name(name)`.
- Step 3: `"ctrl_rep1".split("_")` gives `['ctrl', 'rep1']`, so `int()` gets `'rep1'`.
  Fix: `int(replicate.removeprefix("rep"))`. Equivalent fixes: `replicate[3:]`,
  `replicate.replace("rep", "")`, a regular expression. The rest of the cell then runs, and
  `sample_info` shows the seven names, for example
  `'kd_rep3': {'condition': 'kd', 'replicate': 3}`.
- Step 4: the commented cell `# mean count per condition` in
  `experiment/code/explore_counts.ipynb` is one possible answer. The comments differ with
  every LLM run; check that they say what each step does, and that the code itself is
  unchanged: it still prints the means above.
- Step 5: the commit holds `explore_counts.ipynb`.

## EX3: Improvement

- Steps 1–2, malformed: `kd-rep4` and `ctrl8` (no underscore), `kd_rep` (no number),
  `KD_rep5` (condition not `ctrl` or `kd`), `ctrl_rep6_new` (two underscores). Valid:
  `ctrl_rep5`, `kd_rep4` and the seven original names, 9 in all.
- Answer styles tested: checks with `split` and `isdigit`, or
  `re.fullmatch(r"(ctrl|kd)_rep(\d+)", name)`. Both report the five names.
- What to watch for: a regular expression with `re.IGNORECASE` accepts `KD_rep5`;
  `re.match` instead of `re.fullmatch` accepts `ctrl_rep6_new`. A check by hand
  (step 2) catches both.
- Step 3: see `experiment/README.md` § Observations and interpretation and
  `experiment/metadata.yml`.
- Step 4: see `journal-entry.md`.
- Step 5: the commit holds `explore_counts.ipynb`, `README.md`, `metadata.yml` and
  `journal.md`.

## Skills covered

Each M2 skill, with the exercise step that practises it:

- work between JupyterLab and the LLM interface — "Before you start", EX1 2–3, EX2 3–4,
  EX3 1
- write comments — EX2 4 (the LLM comments the cell `# mean count per condition`); read
  in the cell `# Variables and data types`
- use variables and data types — EX1 1 (`str`, `int`), EX2 3 (`str` turned into `int`)
- use lists and dictionaries — EX1 1, EX2 1–4
- write loops — EX1 1 and 3, EX2 1 and 4
- write conditions — EX1 1, EX1 3 (the threshold condition), EX3 1–2
- prompt an LLM for code — EX1 2, EX3 1; EX2 3 for a fix, EX2 4 for comments
- review LLM-generated code — EX1 3, EX2 3–4, EX3 2
- read error messages and tracebacks — EX1 3, EX2 2
- debug step by step — EX2 1–3

Requirements from M1 used here: run cells and restart the kernel ("Before you start" 3),
the experiment entry (EX3 3), the journal entry (EX3 4), a commit in the Git panel (EX1 4,
EX2 5, EX3 5).
