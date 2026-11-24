# M4 reference solution

The exercises are in `modules/m4/README.md` (in your project:
`work/rrw-workshop/M4_INSTRUCTIONS.md`). This folder shows what a complete answer looks
like:

- `experiment/` — the files of `work/rrw-workshop/experiments/2026-11-06_project-on-a-remote/`
  that the exercises change: `README.md`, with the remote's address and two lines under
  "Observations and interpretation". The notebook is unchanged and not repeated here;
  `results/repository-status.txt` differs at every run.
- `journal-entry.md` — the entry at the top of `work/rrw-workshop/journal.md`, written on
  another computer in EX3.

Names, addresses and dates in the solution (`ada-lovelace`, `2026-11-30`) are examples.
GitHub and GitLab name their menus slightly differently, and both change them from time to
time: look for the same words nearby.

## EX1: Put your project on a remote

- Step 1: the repository must be empty. A repository created with a README already has a
  commit of its own, and Git refuses the first push because the two histories differ. The
  SSH address starts with `git@`; the HTTPS address would ask for a password instead.
- Step 2: `ssh-keygen` writes the private key `id_ed25519` and the public key
  `id_ed25519.pub`. `-N ""` gives the key no passphrase, so the Git panel can use it
  without asking. The lab's home folder is reset at every start except `~/work/`, so the
  key lives in `~/work/.ssh/`, and `core.sshCommand` (in `~/work/.gitconfig`, which is
  kept too) tells Git to use it. `known_hosts` there remembers GitHub's or GitLab's own
  key; `accept-new` adds it at the first connection without a question. `~/work/.ssh/` is
  outside `rrw-workshop/`, so the key can never be committed.
- Step 3: the public key lets the account recognise this lab; it reaches every
  repository of your account. The remote is now known to the project as `origin`. The
  cell `# The remote` of `repository_status.ipynb` would show it twice, once for fetch and
  once for push.
- Step 4: the commit holds only `README.md`. The first push sends every commit of the
  project, from "Create the project from the template" on. The address in the README is
  no secret.

## EX2: Sync, look at changes and go back

- Step 1: editing on the web page makes a commit on the remote. Pull brings it into the
  project; since nothing else changed in the lab, Git only moves the project forward to
  that commit.
- Step 2: the History tab lists the commits, newest first. A commit shows the files it
  changed; a file shows its lines before and after, removed lines in red and added lines
  in green. The same view opens for an uncommitted change when you click a file in the
  Changes tab.
- Step 3: each cell runs a Git command with `!`. `tee -a` shows its output under the cell
  and adds it to `results/repository-status.txt`; the first cell starts the file anew
  with `date >`. Running the notebook stores outputs in it, so it is changed. Discard
  replaces the notebook with its version from the last commit. Its outputs and any other
  uncommitted change are gone; this cannot be undone. The status file is new and
  untracked, so Discard does not touch it.
- Step 4: `git switch --detach <code>` puts the whole project in the state of that commit;
  Git calls this a "detached HEAD". The address and the line from the web are missing,
  because they were committed later. The untracked status file stays, because Git keeps
  files it does not track when it switches. `git switch main` returns to the newest commit.
- Step 5: the commit holds only `results/repository-status.txt`. It records the state of
  the project when you ran the notebook.

## EX3: Work on another computer

- Step 1: a key on your computer is a second key for the same account; each computer has
  its own. `ssh-keygen` asks for a passphrase: on your own computer, one is a good idea.
- Step 2: the clone has the full history of the project. Each clone is complete: the
  project in the lab and the one on your computer are equal copies, kept in sync through
  the remote. A Git GUI runs the same Git commands for you.
- Step 3: see `journal-entry.md`. `git push` sends the new commit to the remote.
- Step 4: the pull brings the journal entry into the lab, the same way as the web edit in
  EX2.
- Step 5: the mistake is a commit in the lab only. It is not pushed, so the remote does
  not know it.
- Step 6: the hard reset moves the project back to the journal entry and drops every
  commit after it, with their changes. Because the mistake was never pushed, nothing else
  has to change. A pushed commit would also be on the remote: there you would make a new
  commit that undoes it (the icon "Revert changes introduced by this commit") instead.
- Step 7: the new commit follows straight on the journal entry, as if the mistake had
  never happened. See `experiment/README.md` for the result.

## Skills covered

Each M4 skill, with the exercise step that practises it:

- create a private remote repository — EX1 1
- create an SSH key and add it to the account — EX1 2 and 3, EX3 1
- add a remote — EX1 3
- push commits — EX1 4, EX2 5, EX3 3 and 7
- pull changes — EX2 1, EX3 4
- see what a commit changed in the Git panel's History — EX2 2
- clone a repository — EX3 2
- switch to an earlier commit and back — EX2 4
- discard uncommitted changes — EX2 3
- undo a commit that was not pushed — EX3 5 and 6

Requirements from earlier modules used here: the preparation's hosting account (EX1 1),
an experiment entry and its README (EX1 4, EX3 7), a commit in the Git panel (EX1 4,
EX2 5, EX3 5 and 7), a file's history in Git (EX2 2 and 4).
