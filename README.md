# Reproducible research workflows with Jupyter and Python

## This workshop: Rhine-Main Universities, 30 November – 3 December 2026

This branch carries the materials for the online workshop for researchers at the
Rhine-Main Universities (JGU Mainz, Goethe University Frankfurt, TU Darmstadt).

- **Dates:** Monday 30 November to Thursday 3 December 2026, daily 09:00–12:15: one
  module 09:00–10:30, a break until 10:45, a second module 10:45–12:15
- **Format:** online and hands-on, in English; eight modules of 90 minutes, two per day
- **Where the materials run:** on [Jupyter4NFDI](https://hub.nfdi-jupyter.de), which
  builds a session from this branch. You need a computer with internet access and nothing
  installed
- **LLM:** [GWDG Chat AI](https://chat-ai.academiccloud.de) with an Academic Cloud login.
  You may use another chat service, but expect different results. Put only public or
  made-up data into any LLM
- **Preparation:** mandatory, as described in [`preparation.md`](preparation.md).
  Registered participants receive the instructions in advance; they include running
  `self-test.ipynb`
- **Setup help:** optional online session on Friday 27 November 2026, 10:00–11:00, for
  problems with the preparation

The modules, added to `modules/` as they are ready:

1. How do I work in JupyterLab and structure my research?
2. How do I write Python with an LLM?
3. How do I read and write data?
4. How do I visualise data and fit models?
5. How do I install modules and manage environments?
6. How do I handle tables and metadata?
7. How do I write reusable functions?
8. How do I turn a notebook into a workflow?

Teaching materials on reproducible research workflows: structuring a research project,
writing Python with the help of an LLM, reading and writing data, visualising and
fitting models, managing environments, handling tables and metadata, writing reusable
functions, and turning a notebook into a workflow.

The materials run in JupyterLab. The repository is meant to be built with
[Repo2Docker](https://repo2docker.readthedocs.io), so a JupyterHub that builds from Git
repositories (for example [Jupyter4NFDI](https://hub.nfdi-jupyter.de) or
[Binder](https://mybinder.org)) can start a ready-to-use session from it.

Modules are added here as they are ready. Each module has its own README with its starting
state and how to run its exercises.

## Where your work lives

Work inside `work/` only. On a hub with persistent storage (on Jupyter4NFDI, "Mount user
data"), only `work/` is kept between sessions. Everything else in your home folder,
including these materials, is reset at the next start, so whatever you create outside
`work/` is lost.

Your project is `work/rrw-workshop/`. All modules add their experiment to it, and it has
one Git repository. `SETUP.ipynb` creates it before the first session. To create it in a
terminal instead (File → New → Terminal), and to add a module's experiment, run:

```bash
python ~/setup_module.py          # creates the project, if it is missing
python ~/setup_module.py example  # also adds this module's experiment
```

You can run a module without having done the others, and you can run the command again:
it never overwrites what is already there. Use the name of the module's folder in `modules/`.

Do not click **Initialize a Repository** in the Git panel. It creates a repository in the
folder the file browser shows, and the project already has one.

`work/` is slow with many small files. Keep data as few, larger files, and keep software
environments out of it: keep the environment file in `work/` and rebuild the environment
from it after a restart.

## Module layout

```text
modules/<module>/
├── README.md
├── setup.json
└── starting-state/
    └── YYYY-MM-DD_experiment-name/
```

- `README.md` describes the starting state and how to run the exercises. It stays with the
  materials and is not copied. It tells readers to run `setup_module.py` with the module's
  folder name, and to work inside `work/` only.
- `setup.json` says what the setup command does for this module. `experiment` names the
  folder in `starting-state/`. `download` is optional and lists files to add to the
  experiment, each with its `url`, its `md5` checksum and its `path` inside the experiment:

  ```json
  {
    "experiment": "2026-11-03_first-look",
    "download": [
      {
        "url": "https://zenodo.org/api/records/19416053/files/Repo1pct.xlsx/content",
        "md5": "b52a4e3556b1d401799a4b43094bf2a5",
        "path": "data/raw/Repo1pct.xlsx"
      }
    ]
  }
  ```

- `starting-state/` holds one experiment, which follows the experiment convention in
  `template/README.md`. The setup command copies it to `experiments/` in the project, adds
  the downloads and commits it. A module with downloads needs network access at setup.
- A module needs nothing from another module, so its experiment brings its own data: small
  files in `starting-state/`, or files that `setup.json` downloads.
- Every file costs time in `work/`, so an experiment holds only what the module uses: about
  ten files at most, and no `.gitkeep` files or empty folders.

## Branches

`main` holds the materials without reference to any particular event. A course or
workshop that uses them gets its own branch, which adds the event-specific information
and the selection of modules taught there.

## Contents

- `requirements.txt`: The software environment: JupyterLab with the Git extension and the analysis packages, each pinned to an exact version
- `runtime.txt`: The Python version
- `postBuild`: Run once when the environment is built; sets the defaults of the Git panel
- `start`: Run at every session start; keeps your Git settings in `work/`, the folder that is kept between sessions, and fills in a Git name or email you have not set from your Jupyter4NFDI account
- `git_identity.py`: Fills in that name and email. Your email goes into every commit, and anyone can read it in a repository you publish. To use another one, set it with `git config --global user.email "you@example.org"`; a value you set is never replaced
- `SETUP.ipynb`: Gets your lab ready in five short steps: checks the analysis packages, the example data and the kept `work/` folder, sets your Git name and email, and creates your project. Run it before the first session
- `setup_module.py`: Creates your project in `work/` and adds a module's experiment to it
- `modules/`: The modules. `modules/example/` shows the layout and lets you try the setup command
- `template/`: A reusable project structure: self-contained experiment entries, a journal, READMEs and metadata
- `data/ecoli-growth/`: The example dataset: *E. coli* growth curves, with source, licence and a script that regenerates the sample

## Licence and citation

The materials are licensed under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/);
the full text is in `LICENSE`. When you reuse them, credit Andrej Berg
([ORCID 0000-0002-5232-1995](https://orcid.org/0000-0002-5232-1995)) and link this
repository. `CITATION.cff` holds the citation metadata.

The example data in `data/` comes from third parties under its own licence (also
CC BY 4.0). Its README names the creators and the DOI to credit.
