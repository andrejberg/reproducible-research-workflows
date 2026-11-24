## 2026-11-30

- Completed M2: asked an LLM for code on the pasilla read counts and checked its results,
  fixed a bug in the code that parses the sample names, had the LLM comment the code for
  the mean per condition, and made the parser report malformed sample names.
- Problem: `ValueError: invalid literal for int() with base 10: 'rep1'`.
- Solution: the replicate part of a sample name is `rep1`; removed `rep` before
  converting it to a number.
- Learned: read the error message from the bottom up.
- Next step: read the counts from a file instead of typing them into the notebook.
