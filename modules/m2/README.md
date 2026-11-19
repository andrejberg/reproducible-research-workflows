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

- `code/explore_counts.ipynb`: where you work. Its first cell holds the data (the sample
  names as a list, the read counts of six genes as a dictionary). Then comes one section
  per exercise, and each section says what to do.
- `README.md` and `metadata.yml`: describe the experiment and the data source. The
  observations in the README are still open.

You work in the notebook. This file tells you where each exercise starts and stops in it,
and gives tips the notebook does not repeat.

## Module-specific preparation

1. In `experiments/2026-11-04_pasilla-knockdown-counts/`, open `README.md` and read what
   the experiment is about and how the sample names are built.
2. Open [GWDG Chat AI](https://chat-ai.academiccloud.de) in a second browser tab, or
   another chat service you use. You copy code from the notebook into the chat, and the
   answer back into a notebook cell.
3. Open `code/explore_counts.ipynb` and run the first code cell (Shift + Enter). Run it
   again after every kernel restart.

When you work with the LLM:

- Put only public or made-up data into an LLM. The counts in this experiment are
  published, so you may paste them.
- Say what you have and what you want: paste the cell with the data and name the
  variables.
- Ask for plain Python. Packages such as pandas come in a later module.
- The LLM gives different code each time, and other services give different code again.
  Your code does not need to look like your neighbour's. Judge it by its result, which
  you check yourself.

## Small exercise (15 min, on your own)

**Start:** the section "Small exercise" in the notebook.

1. Run the cell under "Python syntax", as the notebook says. You should see the gene, its
   type, `1000`, its type and `92` in the first line, then one line per gene. Two genes
   have fewer reads than 1000.
2. For the cell that starts with `# your task`, copy the first code cell and the task line
   into the chat. For example:

   > Using the dictionary `counts` above, write plain Python that prints the genes whose
   > mean count over all seven samples is above `threshold = 100`.

3. Read the code before you trust it. Which line computes the mean, which line is the
   condition? If you cannot tell, ask the LLM to add a comment to each line. Then paste it
   into the `# your task` cell and run it. If it fails, paste the error message into the
   chat and ask for a fix.
4. Check the result by hand for two genes, one listed and one not: add a cell such as
   `sum(counts["FBgn0039155"]) / 7` and compare.

**Stop:** when the `# your task` cell lists the genes and your hand check agrees. Commit:
open the Git panel (the Git icon in the left sidebar), write a short message and commit.

## Larger exercise (20 min, in pairs)

**Start:** the section "Larger exercise" in the notebook. Read its text: it explains why
the sample names are parsed and what to do.

1. Before you run the parser cell, read it together. One of you explains to the other what
   each line should do.
2. Run it. You should see `ValueError: invalid literal for int() with base 10: 'rep1'`.
   Read the traceback from the bottom up: which error, in which line, and which line of
   your cell called it?
3. In the empty cell below the parser, run the failing step on one name, for example
   `"ctrl_rep1".split("_")`, and look at what comes back. What does `int()` get?
4. Paste the parser cell and the error message into the chat and ask for a fix. Read the
   fix before you run it. Then run the cell `# check the result`: you should see all seven
   names, each with its condition and replicate number, such as
   `'ctrl_rep1': {'condition': 'ctrl', 'replicate': 1}`.
5. For the last cell, `# Compute and print the mean count per condition for each gene`,
   copy the first code cell and your fixed cell into the chat and ask, for example:

   > Using `counts`, `samples` and `sample_info` above, write plain Python that computes
   > and prints the mean count per condition for each gene.

   Paste the answer into that cell and run it. You should see one line per gene with a
   `ctrl` and a `kd` mean. Check one by hand: the `kd` mean of `FBgn0039155` from its last
   three counts.
6. Document what you did:
   - in the notebook, a Markdown cell under the fixed code: what was wrong, how you found
     it and how you fixed it
   - in `journal.md` (in `work/rrw-workshop/`), an entry for today at the top

**Stop:** when the means cell runs and your notes are written. Commit: the Git panel should
list `explore_counts.ipynb` and `journal.md`. Write a short message and commit.

Be ready to show the group the error message, the line that caused it and your fix.

## Bonus exercise (30 min, homework)

**Start:** the section "Bonus exercise" in the notebook. Its cell defines `more_samples`,
made-up names to test the parser with.

1. The rule is `<condition>_rep<number>`, where the condition is `ctrl` or `kd`. Ask the
   LLM to change your fixed `parse_sample_name` so that it prints which name is malformed
   and why, and goes on with the next name. Give it the rule.
2. Run it on `samples + more_samples`. Check by hand which names break the rule and
   compare with what the code reports. Does it accept every valid name and report every
   malformed one?
3. Look at the output of your means cell: which genes have a lower mean in the knockdown
   samples than in the controls? Look at the size of the difference too: the counts are
   not normalised.
4. In the experiment's `README.md`, answer the questions under "Observations and
   interpretation". In `metadata.yml`, fill in `date_started`, `author` and `status`
   (its comment lists the values).

**Stop:** when the parser reports the malformed names and the experiment entry is filled
in. Add a line to `journal.md` and commit your changes.

## If something fails

- `NameError: name 'counts' is not defined` → the kernel was restarted or the first cell
  was not run → run the first code cell, then the cell you were working on.
- `KeyError: 'ctrl_rep1'` in the cell for the means → `sample_info` is empty because the
  parser cell still fails → fix the parser, run its cell, then the cell for the means.
- The LLM's code uses other variable names or made-up data → it did not see your data →
  paste the first code cell into the chat and name `samples` and `counts`.

## Solutions

A reference solution for all three exercises is in `~/modules/m2/solutions/`. Its
`README.md` gives the results that do not depend on the LLM and the answers step by step;
`experiment/` shows the completed experiment files and `journal-entry.md` a journal entry.
Try the exercise first, then compare.

## Data credit

The counts are an excerpt of `pasilla_gene_counts.tsv` in the Bioconductor data package
[pasilla](https://bioconductor.org/packages/pasilla/) 1.40.0 by Wolfgang Huber and
Alejandro Reyes (LGPL), derived from RNA-seq data by Brooks et al., *Genome Research* 21
(2011) 193–202, <https://doi.org/10.1101/gr.108662.110>. See the experiment's README.
