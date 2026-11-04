# Reproducible research workflows with Jupyter and Python

Teaching materials on reproducible research workflows: structuring a research project,
writing Python with the help of an LLM, reading and writing data, visualising and
fitting models, managing environments, handling tables and metadata, writing reusable
functions, and turning a notebook into a workflow.

The materials run in JupyterLab. The repository is meant to be built with
[Repo2Docker](https://repo2docker.readthedocs.io), so a JupyterHub that builds from Git
repositories (for example [Jupyter4NFDI](https://hub.nfdi-jupyter.de) or
[Binder](https://mybinder.org)) can start a ready-to-use session from it.

Modules are added here as they are ready. Each module will have its own README with its
starting state and how to run its exercises.

## Branches

`main` holds the materials without reference to any particular event. A course or
workshop that uses them gets its own branch, which adds the event-specific information
and the selection of modules taught there.

## Contents

| Path | What it is |
|---|---|
| `requirements.txt` | The software environment: JupyterLab with the Git extension and the analysis packages, each pinned to an exact version |
| `runtime.txt` | The Python version |
| `postBuild` | Run once when the environment is built; sets the defaults of the Git panel |
| `start` | Run at every session start; keeps your Git settings in `work/`, the folder that is kept between sessions |
| `self-test.ipynb` | Checks that the environment works: packages, example data, the persistent `work/` folder, terminal, kernels and Git. Run it before the first session |
| `template/` | A reusable project structure: self-contained experiment entries, a journal, READMEs and metadata, with a finished example |
| `data/ecoli-growth/` | The example dataset: *E. coli* growth curves, with source, licence and a script that regenerates the sample |

## Licence and citation

The materials are licensed under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/);
the full text is in `LICENSE`. When you reuse them, credit Andrej Berg
([ORCID 0000-0002-5232-1995](https://orcid.org/0000-0002-5232-1995)) and link this
repository. `CITATION.cff` holds the citation metadata.

The example data in `data/` comes from third parties under its own licence (also
CC BY 4.0). Its README names the creators and the DOI to credit.
