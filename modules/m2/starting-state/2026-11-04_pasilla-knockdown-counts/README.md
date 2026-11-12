# Read counts after a pasilla knockdown: a first look

This experiment looks at the RNA-seq read counts of six genes in control and knockdown
samples, to practise writing and checking Python code with an LLM on small, real data.

Structured metadata, input and output paths and the software environment are recorded in
[`metadata.yml`](metadata.yml).

## Purpose

Which of the six genes have many reads, and how do their counts differ between the
control samples and the samples in which the gene *pasilla* was knocked down by RNAi?

## Method

1. The read counts are typed into the first cell of `code/explore_counts.ipynb`: a list
   `samples` with the seven sample names and a dictionary `counts` with one list of seven
   counts per gene. The counts are copied unchanged from the source (see Data credit).
2. Sample names follow the pattern `<condition>_rep<number>`: `ctrl` for the four control
   samples, `kd` for the three knockdown samples.
3. The notebook computes mean counts with plain Python: lists, dictionaries, loops and
   conditions. No package is needed.

The counts are raw read counts. They are not normalised for sequencing depth, which
differs between samples, so small differences between conditions mean little.

## Data generated or processed

This experiment produces no files. Its results are printed in the notebook.

## Observations and interpretation

- What was expected?
- What was observed?
- What errors occurred, and how were they fixed?

## Reproducing this experiment

1. Open the experiment folder in JupyterLab.
2. Run `code/explore_counts.ipynb` from top to bottom (Run → Run All Cells).

## Limitations and next steps

- Six of about 14,600 genes, chosen to show high, low and changing counts; they are not a
  sample of the transcriptome.
- Raw counts only: no normalisation and no statistical test.

## Data credit

The counts are an excerpt of `pasilla_gene_counts.tsv` in the Bioconductor data package
[pasilla](https://bioconductor.org/packages/pasilla/) 1.40.0 by Wolfgang Huber and
Alejandro Reyes, licensed under the LGPL. The excerpt keeps six genes (FlyBase gene IDs)
and all seven samples; the sample names `untreated1`–`untreated4` and
`treated1`–`treated3` are renamed `ctrl_rep1`–`ctrl_rep4` and `kd_rep1`–`kd_rep3`.

The package derives the counts from RNA-seq data of Brooks AN, Yang L, Duff MO, Hansen
KD, Park JW, Dudoit S, Brenner SE and Graveley BR, "Conservation of an RNA regulatory map
between *Drosophila* and mammals", *Genome Research* 21 (2011) 193–202,
<https://doi.org/10.1101/gr.108662.110>, with the reads in NCBI GEO under GSM461176 to
GSM461181.
