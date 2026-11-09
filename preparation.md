# Preparation for the RMU workshop

Workshop: Reproducible research workflows with Jupyter and Python, online,
Monday 30 November to Thursday 3 December 2026, daily 09:00–12:15.

Preparation is **mandatory**. When you have finished it, your environment works, your
project folder exists and the materials are open, so you can start with module one at
09:00 on Monday.

You need a computer with internet access and a current web browser. You install nothing.

**Two reports and their deadlines**

- **Your login address**, right after step 1, at the latest by **Friday 27 November,
  18:00**. If there is a waiting list and we have no address from you by then, your place
  goes to the next person on the list.
- **Your setup result**, in step 10, by **Thursday 26 November, 12:00**.

Send both by replying to the mail these instructions came with. You can send them in one
reply if you finish everything at once.

If something fails, see [If something goes wrong](#if-something-goes-wrong). For help,
come to the optional [setup slot](#11-the-setup-slot-if-you-need-help) on Friday
27 November, 10:00–11:00.

## 1. Log in to Jupyter4NFDI and report your address

The workshop runs on Jupyter4NFDI, a service that runs JupyterLab in your browser.

1. Go to <https://hub.nfdi-jupyter.de> and log in with your university account.
2. **If the university login fails**, use the guest access instead: on the login page,
   choose **Guest Access**, then **Helmholtz ID**, and log in with GitHub, Google or
   ORCID. Use the same route every time, because each route is a separate account with
   its own files.
3. Open <https://hub.nfdi-jupyter.de/hub/api/user_email>. It shows the email address
   your account has on Jupyter4NFDI. It may differ from the address you registered with.
4. Open <https://hub.nfdi-jupyter.de/hub/credits> and note the credits per day for
   **deNBI-Cloud**. A running lab uses credits, so stop it after each session (step 4).
5. **Report** by replying to the mail these instructions came with:
   - the address from step 3, exactly as shown,
   - your login route: your university's name, or guest access with GitHub, Google or
     ORCID,
   - the deNBI-Cloud credits per day from step 4.

The tutor uses this address to give you access to the workshop. The deadline is
**Friday 27 November, 18:00**. Until then the workshop is open, so you can do all the
other steps before the tutor has your address. After 27 November, only reported addresses
can start the workshop lab. If you change your login route later, check the address
again and report the new one.

If you received these instructions from the waiting list after 27 November, report your
address as soon as you can. You can start the workshop lab once the tutor has entered it.

## 2. Start the lab

1. Open the workshop page: <https://hub.nfdi-jupyter.de/workshops/r3du839ryrclmzccsexel2a3w25tfq3>
2. Start the lab. The workshop's settings are already filled in.
3. Wait. The first start after a change to the materials builds the environment and can
   take several minutes. Later starts are faster.

JupyterLab opens with the file browser on the left. It shows the workshop materials,
including `README.md`, `self-test.ipynb`, `template/` and `modules/`, and the folder
`work/`.

**Tutor may join your lab.** During the workshop, the tutor can open your running lab
through Real Time Collaboration to help you. Please let the tutor know if you don't want
to use this function.

## 3. Check your Git name and email

Git records who made each change. The lab takes your name and email from your
Jupyter4NFDI account when it starts.

1. Open a terminal: **File → New → Terminal**.
2. Paste this line and press Enter:

   ```bash
   git config --global user.name; git config --global user.email
   ```

3. It shows two lines: your name and your email. If both are right, there is nothing to
   do.

**Your email goes into every change you record with Git (every commit).** Anyone can read
it in a repository you publish, for example on GitHub. To use another address, set it
before your first commit:

```bash
git config --global user.email "you@example.org"
```

If a line is empty, or you want another name, set it yourself in the same way:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.org"
```

A value you set yourself is kept in `work/` and never replaced. Commits you made before
keep the address they were made with.

## 4. Initiate the workshop directory

Only the `work/` folder is kept when the lab stops. Everything else in the file browser,
including the workshop materials, is reset at the next start. Whatever you create outside
`work/` is lost.

Your project for the whole workshop is `work/rrw-workshop/`. Create it now. In the
terminal, paste:

```bash
python ~/setup_module.py
```

It can take up to a minute, because `work/` is slow with many small files. It reports
that it created the folder `/home/jovyan/work/rrw-workshop` with a Git repository and a
first commit. A second line says that no module was named, which is expected: the
modules add their parts during the workshop.

NOTE AB: Add
- use the file browser to navigate to `work/rrw-workshop` and confirm it contains README.md and other files
- select Git Tab (bar on the left) and confirm that the workshop repo contains one commit "Create the project from the template"


## 5. Run the self-test, first run

1. In the file browser, open `self-test.ipynb`. For that navigate back to home.
2. Follow **How to run it** at the top of the notebook: paste the line from its step 1
   into the terminal, then choose **Run → Run All Cells**.
3. Every check prints `PASS` or `FAIL`. A failed check also prints **What to do**; follow
   it and run all cells again.

When everything passes, the last cell shows `All 8 checks passed. Your environment is
ready.` The persistence check says `first run: restart the lab and run this notebook
again`. This is expected: the first run cannot yet show that your files survive a
restart.

## 6. Restart the lab

1. **File → Hub Control Panel → Stop My Server**.
2. Start the lab again from the workshop page (step 2).

## 7. Run the self-test, second run

1. Open a terminal and paste the line from step 1 of `self-test.ipynb` again. Every run
   needs it, so the Terminal check fails without it.
2. Open `self-test.ipynb` and choose **Run → Run All Cells**.
3. Check that the output has both of these lines:
   - `PASS  Persistent work folder: ... found the note from <date and time of your first run>`
   - `All 8 checks passed. Your environment is ready.`

Only this second run shows that your work is kept. Also check that `work/rrw-workshop/`
is still there.

## 8. Open the materials

1. In the left sidebar, find the **Git** tab (the icon with a branch symbol).
2. In the file browser, open `template/` and read `template/README.md`. It describes the
   project structure you will use in the workshop.
3. Open `modules/` and check that the module folders are there.
4. Open `work/rrw-workshop/`. It has the same structure as `template/`.

**Stop the lab when you are done for the day:** **File → Hub Control Panel → Stop My
Server**. A running lab uses credits even when you are not working in it.

## 9. Log in to the LLM chat

The workshop uses GWDG Chat AI, a chat service with large language models (LLMs).

1. Go to <https://chat-ai.academiccloud.de> and log in with Academic Cloud. Use "Federated Login" 
   to use your university account.
2. Start a new chat and send a short message, for example "Hello". An answer appears.

If the login does not work, you may use another chat service of your choice. Expect its results 
to differ from the presented solutions. During the workshop we will use the LLM to write and debug
code snipets. There is no need to get a paid subscription for that. If you use a commercial service: 
**Put only public or made-up data into any LLM**, never personal data or unpublished research data.

## 10. Report your result

By **Thursday 26 November, 12:00**, reply to the mail these instructions came with:

NOTE AB: I only need the mail address from <https://hub.nfdi-jupyter.de/hub/api/user_email> and if smething failed.

## If something goes wrong

If a step fails check if you have succesfully finished all previous steps and try to run the failed step again.
If this does not solve the problem, send the output of the failed cell or a description of what you see, and
say which step it is. Then come to the setup slot.

## The setup slot, if you need help

**Friday 27 November 2026, 10:00–11:00, online:** <https://bbb.rlp.net/rooms/5fy-7tz-5d0-izu/join>

The slot is optional. If everything works, you do not need to come.

## Checklist

- [ ] I logged in to Jupyter4NFDI and reported my address, login route and credits
      (by 27 November, 18:00).
- [ ] The lab starts from the workshop page.
- [ ] `git config` shows the name and email I want in my commits.
- [ ] `work/rrw-workshop/` exists, and I work inside `work/` only.
- [ ] I see the Git tab, and `template/` and the module folders open.
- [ ] I can log in to GWDG Chat AI, or I have chosen another service.
- [ ] I reported my result (by 26 November, 12:00).
- [ ] I stop the lab when I am done for the day.
