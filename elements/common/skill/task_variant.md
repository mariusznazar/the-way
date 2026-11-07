# The task variant

In task mode, when `refine-task` calls `find-foundation-entries` with a task document as the
source: the values the caller gives and the lines for steps 1, 2, 4 and 5, which you carry out at
those steps.

## What the caller gives

`refine-task` gives the task document, the conversation that refined it and the material the task
started from as the source; the task's cycle as the next reader; and rows of the document's section
"Settlements to record" as the mode (WAY-134). In this mode the skill hands no row to another skill
and no entry is written.

## Step 1 — read

- Read in `project-level/task/template.md` the section "Settlements to record" and its rule under
  "What each section carries" in full.
- Read the projected entries the task's *Decisions in play* carries, so that no candidate repeats
  one.

## Step 2 — build the table

- Take each item of "Need", "To do", "Acceptance criteria" and "Out of scope", each answer under
  "Questions to settle" and each answer of the human in the conversation. A candidate is a
  decision, an invariant, a glossary term, or an environment fact a candidate decision or
  invariant rests on — never a change of the part map.
- Its settlement is in the human's words, and the last column names what the task's cycle would do
  or choose without it.
- Write the table under "Settlements to record" with a column *State* after the template's
  columns: proposed rows start `waiting`, and rows with no concrete next-reader consequence start
  `rejected`. Show the whole table, including the source and next-reader column, with a reason for
  each rejected row.
- The task's cycle makes the one search of the whole foundation when it writes each kept row
  (WAY-33, WAY-134).

## Step 4 — in place of row by row

An accepted row stays a row, and the task's cycle writes its entry (WAY-134). In place of step 4, a row
that carries a choice the human made in the task's refinement, which the cycle will bring into a
binding part without asking, gets the question against the answer that "How a skill asks" in
`way_of_working.md` gives, unless an exception there covers it, at most three questions at a time;
write each answer into the row, with the ways that question showed and the human did not take in
the row's *Source* as `project-level/task/template.md` gives, before the next question (WAY-113,
WAY-134).

## Step 5 — close

Once no row is `waiting`, take out the rejected rows and the column *State*, and write above the
table the line `Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD`, as
`project-level/task/template.md` gives it, renumbering the rows that stay; with no row accepted,
`none` stands below the line in place of the table. Tell `refine-task` how many rows of each kind
were kept.
