# M4 – How do I share and sync my work with Git?

You put your project on a private remote repository, keep it in sync, look at what has
changed, and go back to earlier states of your work.

You leave with a project that lives outside the workshop platform and that you can clone
to the computer where you do your research.

## Before you start

1. Sign in to your hosting account from the preparation in a second browser tab: GitHub,
   or your institution's GitLab.
2. In `experiments/2026-11-06_project-on-a-remote/`, open `code/repository_status.ipynb`.
   It shows your project's remote, its latest commits and what has changed, and adds this
   to `results/repository-status.txt`. You run it in EX2.

Git reaches your remote with an SSH key, a pair of two files:

- The public key (`id_ed25519.pub`) goes to the website. You can show it to anyone.
- The private key (`id_ed25519`) is like a password: never put it into a file of the
  project, a notebook, a commit or an LLM chat. If it got there, delete the key on the
  website and create a new one.

## EX1: Put your project on a remote (15 min, on your own)

Your project lives only on the workshop platform. Put a copy on a remote repository, so
your work is safe and you can take it with you.

1. Create an empty private repository named `rrw-workshop`, without a README, licence or
   `.gitignore`, and copy its SSH address.
   - GitHub: **+** → New repository, visibility Private. The address is under Code → SSH
     and looks like `git@github.com:<username>/rrw-workshop.git`.
   - GitLab: New project → Create blank project, visibility Private, and untick
     "Initialize repository with a README". The address is under Code → Clone with SSH.
2. Open a terminal (File → New → Terminal) and create a key in `~/work/.ssh/`, which is
   kept when the lab restarts:

   ```bash
   # create a directory inside work
   mkdir -p ~/work/.ssh
   
   # generate an SSH key pair inside this directory
   ssh-keygen -t ed25519 -N "" -C "rrw-workshop lab" -f ~/work/.ssh/id_ed25519

   # tell git which SSH key to use
   git config --global core.sshCommand "ssh -i ~/work/.ssh/id_ed25519 -o UserKnownHostsFile=~/work/.ssh/known_hosts -o StrictHostKeyChecking=accept-new"
   
   # show public key
   cat ~/work/.ssh/id_ed25519.pub
   ```
   <br>
   The last command shows the public key: one line that starts with `ssh-ed25519`. Select
   it and copy it (right-click → Copy).
3. Add the public key to your account: paste it, give it the title `rrw-workshop lab`, and
   save it.
   - GitHub: your picture → Settings → SSH and GPG keys → New SSH key.
   - GitLab: your picture → Edit profile → SSH Keys → Add new key.

   Then, in JupyterLab, open Git → Manage Remote Repositories. Enter the name `origin` and
   the SSH address, click Add and close the window.
4. In the experiment's `README.md`, replace the placeholder under "Remote" with the
   address. The Git panel should list only `README.md`. Commit it, then click Push (the
   cloud with the arrow up). Reload the repository's web page: you should see
   `experiments/`, `journal.md` and `M4_INSTRUCTIONS.md`.

## EX2: Sync, look at changes and go back (20 min, in pairs)

You will change your project in more than one place. Practise pulling a change, seeing
what it changed, and looking at an earlier state.

1. On the repository's web page, open the experiment's `README.md`, edit it (pencil
   icon, or Edit → Edit single file) and add a line under "Observations and
   interpretation". Commit the change there. In Jupyter Lab in the Git panel, click Pull
   (the cloud with the arrow down).
3. In the Git panel, open the History tab and click the top commit, the one you made on
   the web. It lists `README.md`; click the file to see the change: your line is green.
4. Run all cells of `repository_status.ipynb`. The Git panel lists the notebook as changed
   and `results/repository-status.txt` as untracked. Save and close the notebook, then
   right-click it in the Git panel → Discard. Open it again: it is back as in the last
   commit, without outputs.
5. In the terminal, run:

   ```bash
   cd ~/work/rrw-workshop
   git log --oneline
   ```
   <br>
   Copy the short code of the commit "Add the starting state of m4" and run
   `git switch --detach <code>`. Open the experiment's `README.md`: the address and your
   line from the web are not there. Run `git switch main`: both are back.
6. Commit `results/repository-status.txt` and push. On the web page, the experiment now
   has a `results/` folder with the status file.

## EX3: Work on another computer (30 min, homework)

Your research happens on your own computer. Clone the project there and bring a change
back, then undo a commit you made by mistake.

1. On the computer where you do your research, create an SSH key in a terminal with
   `ssh-keygen -t ed25519` (press Enter to accept the default place `~/.ssh/`), and add the
   public key `~/.ssh/id_ed25519.pub` to your account as in EX1 step 3. If Git or
   `ssh-keygen` is missing, ask the LLM how to install it on your system.
2. Run `git clone <address>`, with the SSH address from EX1. You should see a folder
   `rrw-workshop` with your experiments. Instead of the terminal, you can also use a Git
   GUI, an app with buttons for clone, commit, push and pull, if you find one that works
   for you.
3. In the clone, add an entry for today at the top of `journal.md`: where you cloned the
   project and what you did in this module. Then run:

   ```bash
   git add journal.md
   git commit -m "add a journal entry from my computer"
   git push
   ```
   <br>
   If Git asks who you are, set your name and email as it says, and commit again.
4. Back in JupyterLab, click Pull in the Git panel. `journal.md` should show the new entry.
5. Make a mistake: in the experiment's `README.md`, delete the address under "Remote",
   save, and commit with the message "delete the remote address". Do not push.
6. Undo it: in the Git panel's History tab, click the commit below your mistake (the
   journal entry). Click its icon "Discard changes introduced *after* this commit (hard
   reset)" (hover over the icons to see their names) and confirm. The `README.md` has the
   address again, and the mistake is gone from the History.
7. Under "Observations and interpretation", add a line on what the hard reset did. Commit
   and push. On the web page, the commit history goes from the journal entry straight to
   this commit.

## Solutions

A reference solution for all three exercises is in `~/modules/m4/solutions/`. Its
`README.md` gives the answers step by step and what each step changes in the repository;
`experiment/` shows the completed experiment files and `journal-entry.md` a journal entry.
Try the exercise first, then compare.
