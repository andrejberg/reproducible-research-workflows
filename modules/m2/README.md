# M2 – How do I write Python with LLM assistance?

You solve small programming tasks on RNA-seq read counts by asking an LLM for the code,
pasting it into a notebook, and checking what it does. When the code fails, you read the
error message and fix it step by step.

You see how Python looks (comments, variables, data types, lists and dictionaries, loops
and conditions) without learning it line by line. The skill is to ask for code, read it,
and check its result.

## Before you start

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

## EX1: Python syntax (15 min, on your own)

Genes with very few reads tell you little, so you want to know which genes have enough.
An LLM writes the code; to judge it, you first look at how Python code reads.

1. Run the cell `# Variables and data types`. Two genes have fewer reads than 1000.
2. Copy the first code cell and an instruction to solve `# your task` into the LLM chat,
   for example:

   > Using the dictionary `counts` above, write plain Python that prints the genes whose
   > mean count over all seven samples is above `threshold = 100`.

3. Paste the code into the `# your task` cell and run it. Which line is the condition? If
   it fails, paste the error message into the chat.
4. Save the notebook (Ctrl + S) and open the Git panel (Git icon in the left sidebar). It
   should list `explore_counts.ipynb`. Write a short message, for example
   `list genes above threshold`, and commit.

## EX2: Debugging (20 min, in groups)

You want to know the mean count over each set of replicates. Sample names look like
`ctrl_rep1`: a condition, an underscore, `rep` and a replicate number. To calculate
the mean you want to group the sets and for that you want to parse the sample names.

1. Read the parser cell together before you run it. One of you explains what each line
   should do.
2. Run it. You should see `ValueError: invalid literal for int() with base 10: 'rep1'`.
   Read the traceback from the bottom up: which line failed, and which line called it?
3. Paste

   - the data cell from above
   - the parser cell
   - the error message

   into the chat and ask for a fix. Read the fix, run it, then run `# check the result`.
   You should see seven names such as `'ctrl_rep1': {'condition': 'ctrl', 'replicate': 1}`.
4. The cell `# mean count per condition` computes the mean over each set of replicates,
   but its steps have no comments. Paste it into the chat and ask the LLM to add a comment
   to each step. Read the comments, paste the code back into the cell and run it. You
   should see a mean for `ctrl` and `kd` per gene, such as
   `FBgn0039155 {'ctrl': 1354.8, 'kd': 53.3}`.
5. Save the notebook and open the Git panel. It should list `explore_counts.ipynb`. Write
   a short message, for example `fix sample name parser`, and commit.

## EX3: Improvement (30 min, homework)

New samples are named by hand, and some names will break the naming rule. Make the parser
more reliable, then complete the experiment entry with what you found.

1. The rule is `<condition>_rep<number>`, where the condition is `ctrl` or `kd`. Ask the
   LLM to change your fixed `parse_sample_name` so that it reports each malformed name and
   why, and goes on with the next one. Give it the rule.
2. Run it on `samples + more_samples`. Check by hand which names break the rule: does the
   code report exactly those?
3. In the experiment's `README.md`, answer the questions under "Observations and
   interpretation". In `metadata.yml`, fill in `date_started`, `author` and `status` (its
   comment lists the values).
4. Add an entry for today at the top of `journal.md` (in `work/rrw-workshop/`): what you
   did in this module, which error you met and how you fixed it.
5. Save the notebook and open the Git panel. It should list `explore_counts.ipynb`,
   `README.md`, `metadata.yml` and `journal.md`. Write a short message, for example
   `report malformed sample names`, and commit.

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
