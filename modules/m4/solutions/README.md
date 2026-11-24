# M4 reference solution

The exercises are in `modules/m4/README.md` (in your project:
`work/rrw-workshop/M4_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-06_project-on-a-remote/`
  that the exercises change: `README.md`, with the remote's address.
  The notebook is unchanged and not repeated here.
- `journal-entry.md` — the entry at the top of `work/rrw-workshop/journal.md`, written on
  another computer in EX3.

Names, addresses and dates in the solution (`ada-lovelace`, `2026-11-30`) are examples.
GitHub and GitLab name their menus slightly differently, and both change them from time to
time: look for the same words nearby.

## EX1: Put your project on a remote

- Step 1: the repository must be empty. A repository created with a README already has a
  commit of its own, and Git refuses the first push because the two histories differ.
- Step 2: a fine-grained GitHub token for one repository, with Contents read and write, can
  push and pull that repository and nothing else. A GitLab token with `write_repository`
  can read and write every repository of your account. Both expire on the date you chose;
  after that, Git asks for a password again and you create a new token.
- Step 3: the remote is now known to the project as `origin`. The cell `# The remote` of
  `repository_status.ipynb` would show it twice, once for fetch and once for push.
- Step 4: the commit holds only `README.md`. The first push sends every commit of the
  project, from "Create the project from the template" on. The token is not stored in the
  project: "Save my login temporarily" keeps it in memory for about an hour, and after a
  restart of the lab Git asks again. The address in the README has no token in it.

## EX2: Sync, ignore and go back

- Step 1: editing on the web page makes a commit on the remote. Pull brings it into the
  project; since nothing else changed in the lab, Git only moves the project forward to
  that commit.
- Step 2: running the notebook stores outputs in it, so it is changed, and writes
  `results/repository-status.txt`. "Ignore this file" adds the line
  `experiments/2026-11-06_project-on-a-remote/results/repository-status.txt` to the
  project's `.gitignore`, which already lists `.ipynb_checkpoints/` (JupyterLab's
  automatic copies of notebooks) and `__pycache__/`. The status file then disappears from
  the Git panel, and `.gitignore` appears as changed.
- Step 3: Discard replaces the notebook with its version from the last commit. Its outputs
  and any other unsaved or uncommitted change are gone; this cannot be undone.
- Step 4: `git switch --detach <code>` puts the whole project in the state of that commit;
  Git calls this a "detached HEAD". The address and the line from the web are missing,
  because they were committed later. The changed `.gitignore` stays, because Git keeps
  uncommitted changes when it switches. `git switch main` returns to the newest commit.
- Step 5: the commit holds only `.gitignore`. On the web page the repository has no
  `results/` folder in the experiment.

## EX3: Work on another computer

- Step 1: the clone has the full history of the project. Each clone is complete: the
  project in the lab and the one on your computer are equal copies, kept in sync through
  the remote.
- Step 2: see `journal-entry.md`. `git push` sends the new commit to the remote.
- Step 3: the pull brings the journal entry into the lab, the same way as the web edit in
  EX2.
- Step 4: `git log --oneline -- <file>` lists only the commits that changed that file:
  the web edit, your EX1 commit and "Add the starting state of m4". `git restore --source`
  replaces the file with its version from your EX1 commit and leaves every other file as
  it is. The history keeps the web edit: nothing is lost.
- Step 5: the commit holds only `README.md`; see `experiment/README.md` for the result.

## Skills covered

Each M4 skill, with the exercise step that practises it:

- create a private remote repository — EX1 1
- create a personal access token — EX1 2
- add a remote — EX1 3
- push commits — EX1 4, EX2 5, EX3 2 and 5
- pull changes — EX2 1, EX3 3
- clone a repository — EX3 1
- exclude outputs and checkpoints with .gitignore — EX2 2 (outputs: the status file;
  checkpoints: `.ipynb_checkpoints/`, already in `.gitignore`), EX2 5
- switch to an earlier commit and back — EX2 4
- restore a file from an earlier commit — EX3 4
- discard uncommitted changes — EX2 3

Requirements from earlier modules used here: the preparation's hosting account (EX1 1),
an experiment entry and its README (EX1 4, EX3 5), a commit in the Git panel (EX1 4,
EX2 5, EX3 5), a file's history in Git (EX2 4, EX3 4).
