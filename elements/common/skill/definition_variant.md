# The project definition variant

When `define-project` calls `find-foundation-entries` with a project definition as the source: the
values the caller gives and the lines for steps 1, 2, 4 and 5, which you carry out at those steps.

## What the caller gives

- the source: the definition, the conversation that wrote it, and the material it started from, in
  the part the project concerns;
- the next reader: the breakdown of the project into tasks;
- the mode of the entries: projected, into its section "Projected foundation changes".

## Step 1 — read

- Read in `project-level/definition_template.md` the section "Projected foundation changes" in
  full.
- Read `elements/common/projected_mode.md` for the mode in which the element skills write the
  accepted rows.

## Step 2 — build the table

- Take each line of "In scope", "Out of scope", "Inputs and constraints" and "Success", each answer
  of the human, and the material in the part the project concerns, and name the settlement each
  carries: a rule that still binds once the project is done, what a word means, a sentence a commit
  can make false, a fact a settlement rests on.
- Write the table into the definition as the template's working table: proposed rows start
  `waiting`, a row that repeats a choice the human made between ways shown starts `accepted` and is
  marked as the human's choice (`build_table.md`), and rows with no concrete next-reader consequence
  start `rejected`. Show the whole table, including the source and next-reader column, with a
  reason for each rejected row.
- `define-project` makes the one search of the whole foundation at the readiness gate, once every
  entry is written (WAY-118).

## Step 4 — row by row

For each accepted row, in the table's order:

1. Ask what the entry needs and the source does not give, as `way_of_working.md` gives the asking.
   A question that challenges the settlement stands only where both hold: its anchor can be quoted
   from the human's words or from the material, and its answer goes into a named field of this
   entry — the binding sentence, the rationale, a rejected option, the verification. Three moves
   give such questions:
   - implication — "you wrote X; from X follows Y — does Y hold?";
   - collision — two sentences of the human, both quoted; the material against the conversation is
     no such move (WAY-113), a looser rule that holds only until a task's cycle starts (WAY-315);
   - the reason — where neither the human's words nor the material give the reason of a decision
     that is costly to reverse; a reason the material gives is written without asking.

   Ask at most three questions at a time.
2. Write each answer into the definition before the next question — into the row, or into the
   section it settles.
3. Hand the row to the skill of its element in projected mode, naming the definition, with the
   answers as its source: `record-decision`, `record-invariant`, `record-glossary-term`,
   `record-environment-fact` or `update-part-map`. Once the entry is written, set the row to
   `written`.
4. An entry that skill reports as following from this one becomes a row of the table, `waiting`,
   with its source naming the entry it follows from and the concrete choice the next reader would
   otherwise have to guess. Show the whole added row and ask the human to accept or reject it
   before handing it to a skill. If the human rejects a row required by an accepted entry, reopen
   that entry with the human; do not silently remove its link or weaken its verification.

## Step 5 — close

- Once every row is `rejected` or `written`, take the working table out and write as the section's
  first line `Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD`, as the
  template gives it; the rows shown are every row the table held, the rows step 4 added included.
  With no row accepted, `none` stands below the line.
- Tell the caller how many entries of each kind were written.
