# The project on a remote

This experiment puts the project `rrw-workshop` on a remote repository, so that it lives
outside the workshop platform and can be cloned to another computer. It holds no data:
its notebook shows the state of the project's Git repository.

Structured metadata and the software environment are recorded in
[`metadata.yml`](metadata.yml).

## Purpose

Can the project be kept in sync between the workshop platform, a remote repository and the
computer where I do my research, and can an earlier state be brought back?

## Method

1. A private repository on GitHub or on an institutional GitLab is the remote. Git
   reaches it over HTTPS with a personal access token, which is never stored in the
   project.
2. `code/repository_status.ipynb` shows the project's remote, its latest commits, what has
   changed and what Git ignores, and writes this status to `results/repository-status.txt`.

## Remote

- Remote repository: <HTTPS address of the repository, without the token>

## Files and names

- `code/repository_status.ipynb` shows the state of the repository. It reads no data.
- `results/repository-status.txt` is written by the notebook at every run, with the time
  it ran.

## Observations and interpretation

- What was expected?
- What was observed?
- What errors, warnings or unexpected results occurred?

## Reproducing this experiment

1. Clone the project from the remote repository.
2. Run `code/repository_status.ipynb` from top to bottom (Run → Run All Cells).

## Limitations and next steps

- The access token expires; after that, Git asks for a new one.
