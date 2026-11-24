# M4 – How do I share and sync my work with Git?

You put your project on a private remote repository, keep it in sync, tell Git which files
to leave out, and go back to earlier states of your work.

You leave with a project that lives outside the workshop platform and that you can clone
to the computer where you do your research.

## Before you start

1. Sign in to your hosting account from the preparation in a second browser tab: GitHub,
   or your institution's GitLab.
2. In `experiments/2026-11-06_project-on-a-remote/`, open `code/repository_status.ipynb`.
   It shows your project's remote, its latest commits, what has changed and what Git
   ignores. You run it in EX2.

When you work with an access token:

- A token is a password. Paste it only into Git's password prompt: never into a file, a
  notebook, a commit or an LLM chat.
- If a token got into a file or a commit, delete the token on the website and create a new
  one.

## EX1: Put your project on a remote (15 min, on your own)

Your project lives only on the workshop platform. Put a copy on a remote repository, so
your work is safe and you can take it with you.

1. Create an empty private repository named `rrw-workshop`, without a README, licence or
   `.gitignore`, and copy its HTTPS address.
   - GitHub: **+** → New repository, visibility Private. The address looks like
     `https://github.com/<username>/rrw-workshop.git`.
   - GitLab: New project → Create blank project, visibility Private, and untick
     "Initialize repository with a README". The address is under Code → Clone with HTTPS.
2. Create a personal access token for this repository and copy it. It is shown only once.
   - GitHub: your picture → Settings → Developer settings → Personal access tokens →
     Fine-grained tokens → Generate new token. Repository access: Only select
     repositories, `rrw-workshop`. Permissions: Contents, Read and write.
   - GitLab: your picture → Edit profile → Access tokens → Add new token, scope
     `write_repository`.
3. In JupyterLab, open Git → Manage Remote Repositories. Enter the name `origin` and the
   address, and click Add.
4. In the experiment's `README.md`, replace the placeholder under "Remote" with the
   address. The Git panel should list only `README.md`. Commit it, then click Push (the cloud with the arrow up).
   Enter your username and, as password, the token; tick "Save my login temporarily".
   Reload the repository's web page: you should see `experiments/`, `journal.md` and
   `M4_INSTRUCTIONS.md`.

## EX2: Sync, ignore and go back (20 min, in pairs)

You will change your project in more than one place, and not every file belongs in it.
Practise pulling a change, leaving a file out and looking at an earlier state.

1. On the repository's web page, open the experiment's `README.md`, edit it (pencil
   icon, or Edit → Edit single file) and add a line under "Observations and
   interpretation". Commit the change there. In the Git panel, click Pull (the cloud with
   the arrow down) and open the `README.md`: you should see your line.
2. Run all cells of `repository_status.ipynb`. The Git panel lists the notebook as changed
   and `results/repository-status.txt` as untracked. That file changes at every run, so
   leave it out: right-click it in the Git panel → Ignore this file (add to .gitignore).
   Run the cell `# What Git ignores`: you should see the file's path at the end, and
   `.ipynb_checkpoints/`, JupyterLab's automatic copies, near the top.
3. Save and close the notebook. In the Git panel, right-click `repository_status.ipynb` →
   Discard. Open the notebook again: it is back as in the last commit, without outputs.
4. Open a terminal (File → New → Terminal) and run:

   ```bash
   cd ~/work/rrw-workshop
   git log --oneline
   ```
   <br>
   Copy the short code of the commit "Add the starting state of m4" and run
   `git switch --detach <code>`. Open the experiment's `README.md`: the address and your
   line from the web are not there. Run `git switch main`: both are back.
5. The Git panel lists `.gitignore`. Commit it and push. On the web page, `.gitignore`
   now ends with the path of `repository-status.txt`, and that file is not in the
   repository.

## EX3: Work on another computer (30 min, homework)

Your research happens on your own computer. Clone the project there, work on it, and bring
the change back, then restore a file as it was in an earlier commit.

1. On the computer where you do your research, open a terminal and run
   `git clone <address>`, with the address from EX1. Enter your username and the token
   when Git asks. You should see a folder `rrw-workshop` with your experiments. If Git is
   missing, ask the LLM how to install it on your system. With no other computer at hand,
   clone in a lab terminal into `/tmp/` instead: it is lost at the next start, which is
   fine for this exercise.
2. In the clone, add an entry for today at the top of `journal.md`: where you cloned the
   project and what you did in this module. Then run:

   ```bash
   git add journal.md
   git commit -m "add a journal entry from my computer"
   git push
   ```
   <br>
   If Git asks who you are, set your name and email as it says, and commit again.
3. Back in JupyterLab, click Pull in the Git panel. `journal.md` should show the new entry.
4. The line you added on the web in EX2 was a test. Restore the experiment's `README.md` as
   it was in your EX1 commit. In a terminal, run:

   ```bash
   cd ~/work/rrw-workshop
   git log --oneline -- experiments/2026-11-06_project-on-a-remote/README.md
   ```
   <br>
   Copy the short code of your EX1 commit and run
   `git restore --source <code> experiments/2026-11-06_project-on-a-remote/README.md`.
   The `README.md` should show the address, but not the line from the web.
5. The Git panel lists `README.md` as changed. Commit it and push. On the web page, the
   `README.md` no longer has the line.

## Solutions

A reference solution for all three exercises is in `~/modules/m4/solutions/`. Its
`README.md` gives the answers step by step and what each step changes in the repository;
`experiment/` shows the completed experiment files and `journal-entry.md` a journal entry.
Try the exercise first, then compare.
