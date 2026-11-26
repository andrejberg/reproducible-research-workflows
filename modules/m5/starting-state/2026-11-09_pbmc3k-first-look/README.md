# A first look at the PBMC 3k single-cell dataset

This experiment reads a single-cell RNA-seq dataset of about 2,700 blood cells from a
healthy donor and reports how many cells and genes it holds. It records which software
environment the results came from.

Structured metadata, input and output paths and the software environment are recorded in
[`metadata.yml`](metadata.yml).

## Purpose

How many cells and genes does the dataset hold after quality filtering? Which packages,
in which versions, does it take to read it?

## Method

1. Peripheral blood mononuclear cells (PBMCs) of one healthy donor were sequenced by
   10x Genomics, one count of RNA molecules per gene and cell (see Data credit). The
   deposited file keeps cells with at least 200 detected genes and at most 10 %
   mitochondrial reads, and genes detected in at least 3 cells.
2. `code/first_look.ipynb` reads `data/raw/pbmc3k_ders.h5ad` with the package anndata and
   reports the number of cells and genes.

## Files

- `data/raw/pbmc3k_ders.h5ad`: the dataset as it came from its source, downloaded at
  setup. An `.h5ad` file holds a count matrix together with the names of its cells and
  genes. Nothing in `data/raw/` is ever changed.

## Software environment

The notebook runs on the kernel "Python (rrw-workshop)", with the packages listed in the
project's `pyproject.toml`. `uv.lock`, next to it, records the exact version of every
package. Git keeps every version of `uv.lock`, so a commit hash names the environment a
result came from.

- <the commit whose uv.lock the results ran with>

## Results

- <number of cells and genes>

## Reproducing this experiment

1. In a terminal, in the project folder `work/rrw-workshop/` (or your clone of it), run
   `uv sync`. It installs the packages that `uv.lock` records.
2. Run `code/first_look.ipynb` from top to bottom (Run → Run All Cells).

## Data credit

The data is the "PBMC3k teaching dataset (filtered AnnData)" by Melisa Ağrı, published on
Zenodo under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
<https://doi.org/10.5281/zenodo.22655336>. It is derived from the dataset "3k PBMCs from a
Healthy Donor" by 10x Genomics, released under a Creative Commons Attribution licence.
