# M2 – How do I write Python with an LLM?

You solve small programming tasks on RNA-seq read counts by asking an LLM for the code,
pasting it into a notebook, and checking what it does. When the code fails, you read the
error message and fix it step by step.

You see how Python looks (comments, variables, data types, lists and dictionaries, loops
and conditions) without learning it line by line. The skill is to ask for code, read it,
and check its result.

## Starting state

The experiment `2026-11-04_pasilla-knockdown-counts`, a first look at RNA-seq read counts
in four control samples and three samples in which the gene *pasilla* was knocked down:

- `code/explore_counts.ipynb`: the data in its first cell (the sample names as a list,
  the read counts of six genes as a dictionary), a cell that shows how Python code looks,
  and one section per exercise
- `README.md` and `metadata.yml`: describe the experiment and the data source. The
  observations in the README are still open.

## Set up the module

Work inside `work/` only: everything outside it is reset at the next start.

1. Open a terminal (File → New → Terminal) and run:

   ```bash
   python ~/setup_module.py m2
   ```

2. In the file browser, go to `work/rrw-workshop/experiments/2026-11-04_pasilla-knockdown-counts/`.
3. Open `README.md` and read what the experiment is about and how the sample names are
   built.

You need nothing from other modules, and you can run the command again: it never
overwrites what is already there.

## Working with an LLM

Open [GWDG Chat AI](https://chat-ai.academiccloud.de) in a second browser tab, or another
chat service you use. Copy code from the notebook into the chat, and the answer back into
a notebook cell.

- Put only public or made-up data into an LLM. The counts in this experiment are
  published, so you may paste them.
- Say what you have and what you want: paste the cell with the data and name the
  variables.
- Ask for plain Python. Packages such as pandas come in a later module.
- The LLM gives different code each time, and other services give different code again.
  Your code does not need to look like your neighbour's. Judge it by its result, which
  you check yourself.

## Small exercise (15 min, on your own)

1. Open `code/explore_counts.ipynb` and run the first two code cells (Shift + Enter).
   Read the second one: find a comment, a variable, a list, a dictionary, a loop and a
   condition.
2. Copy the first code cell into the chat and ask, for example:

   > Using the dictionary `counts` above, write plain Python that prints the genes whose
   > mean count over all seven samples is above `threshold = 1000`, with their mean.

3. Paste the answer into the cell under "Small exercise" and run it. If it fails, paste
   the error message into the chat and ask for a fix.
4. Read the code before you trust it. Which line computes the mean, which line is the
   condition? If you cannot tell, ask the LLM to add a comment to each line.
5. Check the result by hand for two genes, one listed and one not: add a cell such as
   `sum(counts["FBgn0039155"]) / 7` and compare.
6. Commit: open the Git panel (the Git icon in the left sidebar), write a short message
   and commit.

## Larger exercise (20 min, in pairs)

The notebook holds the answer an LLM gave to a prompt, pasted unchanged. It is meant to
turn sample names such as `ctrl_rep1` into a condition and a replicate number, and to
compute the mean count per condition. It contains a bug.

1. Before you run it, read the prompt and the code together. One of you explains to the
   other what each part should do.
2. Run the cell. Read the error message from the bottom up: which error, in which line,
   and which line of your cell called it?
3. Find the cause step by step. In a new cell, run the failing line on one name, for
   example `"ctrl_rep1".split("_")`, and look at what comes back. What does `int()` get?
4. Fix the line, by yourself or by pasting the error message into the chat. Read the fix
   before you run it.
5. Check one mean by hand: the `kd` mean of `FBgn0039155` from its last three counts.
6. Which genes have a lower mean in the knockdown samples than in the controls? Look at
   the size of the difference too: the counts are not normalised.
7. Document:
   - in the notebook, a Markdown cell under the fixed code: what was wrong, how you found
     it and how you fixed it
   - in the experiment's `README.md`, the observations
   - in `metadata.yml`, your name and the date
   - in `work/rrw-workshop/journal.md`, an entry for today at the top
8. Commit your changes in the Git panel.

Be ready to show the group the error message, the line that caused it and your fix.

## Bonus exercise (homework)

Make the parser report malformed sample names instead of failing on them.

1. The bonus cell defines `more_samples`, made-up names to test with. The rule is
   `<condition>_rep<number>`, where the condition is `ctrl` or `kd`.
2. Ask the LLM to change your fixed `parse_sample_name` so that it prints which name is
   malformed and why, and goes on with the next name. Give it the rule.
3. Run it on `samples + more_samples`. Check by hand which names break the rule and
   compare with what the code reports. Does it accept every valid name and report every
   malformed one?
4. Add a line to the journal and commit.

## Data credit

The counts are an excerpt of `pasilla_gene_counts.tsv` in the Bioconductor data package
[pasilla](https://bioconductor.org/packages/pasilla/) 1.40.0 by Wolfgang Huber and
Alejandro Reyes (LGPL), derived from RNA-seq data by Brooks et al., *Genome Research* 21
(2011) 193–202, <https://doi.org/10.1101/gr.108662.110>. See the experiment's README.
