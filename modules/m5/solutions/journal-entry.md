## 2026-12-02

- EX3 of M5: recreated the project's environment on my laptop (Ubuntu 24.04) with
  `uv sync`, from a clone of the project. anndata 0.13.4 and python-dateutil 2.9.0.post0,
  the same versions as in the lab.
- JupyterLab was not installed, so I opened the notebook with
  `uv run --group jupyter jupyter lab` and the kernel "Python 3 (ipykernel)": 2,694 cells
  and 13,714 genes, as in the lab.
- Different from the steps: none; uv installed Python 3.13 itself.

## 2026-11-30

- M5: added anndata to read the PBMC 3k dataset (`.h5ad`): 2,694 cells and 13,714 genes.
- Added s3fs for a colleague's code. It changed python-dateutil from 4.0.0 to 2.9.0.post0,
  a package pandas uses for dates.
- The cell counts ran with the environment of commit `3f2a1b7`; its `uv.lock` records
  every version.
- Next step: rerun the counts with the new environment and check that they are the same.
