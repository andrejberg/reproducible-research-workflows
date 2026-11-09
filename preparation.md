# Preparation for the RMU workshop

Workshop: Reproducible research workflows with Jupyter and Python, online,
Monday 30 November to Thursday 3 December 2026, daily 09:00–12:15.

Preparation is **mandatory**. When you have finished it, your environment works, your
project folder exists and the materials are open, so you can start with module one at
09:00 on Monday.

You need a computer with internet access and a current web browser. You install nothing.

**What to send, and by when**

- **Your login address**, right after step 1, at the latest by **Friday 27 November,
  18:00**. If there is a waiting list and we have no address from you by then, your place
  goes to the next person on the list.
- **Only if a step fails:** what failed, by **Thursday 26 November, 12:00** (step 8).

Send both by replying to the mail these instructions came with.

If something fails, see [If something goes wrong](#if-something-goes-wrong). For help,
come to the optional [setup slot](#the-setup-slot-if-you-need-help) on Friday
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
   **deNBI-Cloud**. A running lab uses credits, so stop it after each session (end of
   step 6).
5. **Report** the address from step 3, exactly as shown, by replying to the mail these
   instructions came with.

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

## 4. Run the self-test

The self-test is a notebook that checks in five short steps that your lab has what the
workshop needs: the analysis packages, the example data, the `work/` folder, your Git
name and email from step 3, and your project from step 4. Each step says what it checks.

This is a good oportunity to get familiar with the python synthax. You don't need to understand
everything but try to read the code and compare it to what you already know from other programming
languages.

1. In the file browser, find and open `self-test.ipynb`.
2. Choose **Run → Run All Cells**.
3. Every check prints `PASS` or `FAIL`. A failed check also prints **What to do**; follow
   it and run all cells again.

When everything passes, the last cell shows `All 5 checks passed. Your lab is ready for
the workshop.`

## 5. Initiate the workshop directory

Only the `work/` folder is kept when the lab stops. Everything else in the file browser,
including the workshop materials, is reset at the next start. Whatever you create outside
`work/` is lost.

Your project for the whole workshop is `work/rrw-workshop/`. Create it by running the setup script.
In the terminal (if you closed it open a terminal: **File → New → Terminal**), paste:

```bash
python ~/setup_module.py
```

It can take up to a minute, because `work/` is slow with many small files. It reports
that it created the folder `/home/jovyan/work/rrw-workshop` with a Git repository and a
first commit. A second line says that no module was named, which is expected: the
modules add their parts during the workshop.

Check the result:

1. In the file browser, open `work`, then `rrw-workshop`. It contains `README.md` and
   other files and folders.
2. In the left sidebar, select the **Git** tab (the icon with a branch symbol). With
   `work/rrw-workshop` open in the file browser, it shows the project's repository. Its
   **History** has one commit, "Create the project from the template".


## 6. Open the materials

1. In the file browser, open `template/` and read `template/README.md`. It describes the
   project structure you will use in the workshop.
2. Open `modules/` and check that the module folders are there.

**Stop the lab when you are done for the day:** **File → Hub Control Panel → Stop My
Server**. A running lab uses credits even when you are not working in it.

## 7. Log in to the LLM chat

The workshop uses GWDG Chat AI, a chat service with large language models (LLMs).

1. Go to <https://chat-ai.academiccloud.de> and log in with Academic Cloud. Use "Federated Login" 
   to use your university account.
2. Start a new chat and send a short message, for example "Hello". An answer appears.

If the login does not work, you may use another chat service of your choice. Expect its results 
to differ from the presented solutions. During the workshop we will use the LLM to write and debug
code snippets. There is no need to get a paid subscription for that. If you use a commercial service: 
**Put only public or made-up data into any LLM**, never personal data or unpublished research data.

## 8. Report a problem, if there is one

If you have reported your address (step 1) and every step worked, there is nothing more
to send.

If a step failed, reply to the mail these instructions came with by **Thursday
26 November, 12:00**, as described in [If something goes wrong](#if-something-goes-wrong).

## If something goes wrong

If a step fails, check that you have successfully finished all previous steps and try to run the failed step again.
If this does not solve the problem, send the output of the failed cell or a description of what you see, and
say which step it is. Then come to the setup slot.

## The setup slot, if you need help

**Friday 27 November 2026, 10:00–11:00, online:** <https://bbb.rlp.net/rooms/5fy-7tz-5d0-izu/join>

The slot is optional. If everything works, you do not need to come.

## Checklist

- [ ] I logged in to Jupyter4NFDI and reported my address (by 27 November, 18:00).
- [ ] The lab starts from the workshop page.
- [ ] `git config` shows the name and email I want in my commits.
- [ ] `work/rrw-workshop/` exists, and the Git tab shows its first commit.
- [ ] The self-test shows `All 5 checks passed`.
- [ ] `template/` and the module folders open.
- [ ] I can log in to GWDG Chat AI, or I have chosen another service.
- [ ] If a step failed, I reported it (by 26 November, 12:00).
- [ ] I stop the lab when I am done for the day.
