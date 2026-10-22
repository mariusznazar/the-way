---
name: find-foundation-entries
description: Use when a source has to be searched for what should become entries of a product's foundation — decisions, invariants, glossary terms, environment facts, changes to the part map — before any is written; for now, a project definition whose settlements are to be projected before the project is broken into tasks, or a task whose refinement's settlements are to be kept for its cycle.
---

# Find foundation entries

Finds in a source what should become entries of a product's foundation, puts it before the human as
a table of candidates, and hands every accepted one to the skill of its element, or, for a task,
keeps it as a row of the task document. It writes no entry itself. The rules of each entry stand in
its element's template; how a skill asks stands in `elements/common/way_of_working.md`. This skill
serves a project definition and the refinement of a task for now; the breakdown of a project, the
return step of a task (WAY-11) and the entry of the process into an existing product (WAY-28) will
call it too, each adding what it needs (WAY-115, WAY-134).

This skill lives in `elements/common/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`.
`elements/common/` is there, and each skill named below is the project skill of that name with the
`the-way-` prefix.

## What the caller gives

- the source — for a project definition: the definition, the conversation that wrote it, and the
  material it started from, in the part the project concerns;
- the next reader — for a project definition: the breakdown of the project into tasks;
- the mode of the entries — for a project definition: projected, into its section "Projected
  foundation changes".

For the refinement of a task (WAY-134), `refine-task` gives the task document, the conversation
that refined it and the material the task started from as the source; the task's cycle as the next
reader; and rows of the document's section "Settlements to record" as the mode. In that mode the
skill hands no row to another skill and no entry is written: step 4 does not run, and the
differences below each step name what changes.

When the section already holds a working table, resume from the first row whose state is neither
`rejected` nor `written`, or, for a task, from the first row still `waiting`.

## 1. Read

- Read `elements/common/way_of_working.md` in full, and in `project-level/definition_template.md`
  the section "Projected foundation changes" in full; for a task, in
  `project-level/task/template.md` the section "Settlements to record" and its rule under "What each
  section carries" in full.
- Read the source in full.
- Select and read the product's foundation by "Reading the foundation" in
  `elements/common/way_of_working.md`: the parts the source touches, and the entries they and the
  source lead to.
- Read in each element's template what makes something an entry of it: the plan test in the
  decisions' template (WAY-36, WAY-26); "Which words take an entry" in the glossary's; "Which facts
  are written" in the environment facts'; for an invariant, a sentence a commit can make false; for
  the part map, only an entry whose every field is known before the code.
- For a task, also read the projected entries its *Decisions in play* carries, so that no candidate
  repeats one.

## 2. Build the table

- Take each line of "In scope", "Out of scope", "Inputs and constraints" and "Success", each answer
  of the human, and the material in the part the project concerns, and name the settlement each
  carries: a rule that still binds once the project is done, what a word means, a sentence a commit
  can make false, a fact a settlement rests on.
- Each candidate is a row: its number; the settlement in one sentence, in the language of the
  conversation; its kind; its source — the human's words, the material and its place, or a section
  of the definition; what the next reader would have to guess without it.
- The last column names a concrete thing a task would do or choose — "the data model of a team and
  its chest", "whether a button may run an action at once". A row with nothing concrete there is
  shown as rejected, with its reason, and is not proposed.
- A candidate from the material is a proposal: it enters only on the human's word, and the
  conversation may change it.
- Write the table into the definition as the template's working table: proposed rows start
  `waiting`, and rows with no concrete next-reader consequence start `rejected`. Show the whole
  table, including the source and next-reader column, with a reason for each rejected row.
- For a task: take each item of "Need", "To do", "Acceptance criteria" and "Out of scope", each
  answer under "Questions to settle" and each answer of the human in the conversation. A candidate
  is a decision, an invariant, a glossary term, or an environment fact a candidate decision or
  invariant rests on — never a change of the part map. Its settlement is in the human's words, and
  the last column names what the task's cycle would do or choose without it. Write the table under
  "Settlements to record" with a column *State* after the template's columns, and show it whole as
  above.
- No search of the whole foundation runs here. For a project definition, `define-project` makes
  the one search at the readiness gate, once every entry is written (WAY-118); for a task, its
  cycle makes it when it writes each kept row (WAY-33, WAY-134). A settlement that an entry read
  in step 1 already states is no candidate; a candidate that collides with such an entry is shown
  beside it.

## 3. The human cuts

The human accepts or rejects rows, all at once or a few at a time. Write each state into the
working table as soon as it is given.

## 4. Row by row

For a task, this step does not run: an accepted row stays a row, and the task's cycle writes its
entry (WAY-134). In its place, a row that carries a choice the human made in the task's
refinement, which the cycle will bring into a binding part without asking, gets the question
against the answer that "How a skill asks" in `way_of_working.md` gives, unless an exception there
covers it, at most three questions at a time; write each answer into the row before the next
question (WAY-113). For a project definition, for each accepted row, in the table's order:

1. Ask what the entry needs and the source does not give, as `way_of_working.md` gives the asking.
   A question that challenges the settlement stands only where both hold: its anchor can be quoted
   from the human's words or from the material, and its answer goes into a named field of this
   entry — the binding sentence, the rationale, a rejected option, the verification. Three moves
   give such questions:
   - implication — "you wrote X; from X follows Y — does Y hold?";
   - collision — two sentences of the human, or the material against the conversation, both quoted;
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

## 5. Close

- For a project definition, once every row is `rejected` or `written`, take the working table out
  and write as the section's first line `Candidates: <rows shown> shown, <rows accepted> accepted —
  YYYY-MM-DD`, as the template gives it; the rows shown are every row the table held, the rows step
  4 added included. With no row accepted, `none` stands below the line.
- For a project definition, tell the caller how many entries of each kind were written.
- For a task, once no row is `waiting`, take out the rejected rows and the column *State*, and write
  above the table the line `Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD`,
  as `project-level/task/template.md` gives it, renumbering the rows that stay; with no row
  accepted, `none` stands below the line in place of the table. Tell `refine-task` how many rows of
  each kind were kept.
