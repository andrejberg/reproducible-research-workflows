# Research journal

This journal records the chronological progress of the project. It complements, but does
not replace, the self-contained experiment entries.

Add new days at the bottom. Keep each entry short: what happened, what you decided, what
went wrong and what comes next. Details belong in the experiment's README.

*The entries below are examples. Replace them with your own.*

## 2026-11-03

- Explored the JupyterLab interface and created the first experiment entry.
- Decision: use one folder per experiment under `experiments/`.
- Next step: read the growth-curve data and write a cleaned table.

## 2026-11-04

- Fitted a logistic model to the growth curve at 37 °C and 1 % glucose, in
  `experiments/2026-11-04_m04-fit-growth-curves/`.
- Problem: the first attempt used an absolute path and failed on another computer.
- Solution: switched to a path relative to the notebook.
- Next step: compare the fitted parameters across temperatures.
