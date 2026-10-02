---
name: find-foundation-entries
description: Use when a source has to be searched for what should become entries of a product's foundation — decisions, invariants, glossary terms, environment facts, changes to the part map — before any is written; for now, a project definition whose settlements are to be projected before the project is broken into tasks.
---

# Find foundation entries

Finds in a source what should become entries of a product's foundation, puts it before the human
as a table of candidates, and hands every accepted one to the skill of its element. It writes no
entry itself. The rules of each entry stand in its element's template; how a skill asks stands in
`elements/common/way_of_working.md`. This skill serves a project definition for now; the breakdown
of a project, the return step of a task (WAY-11) and the entry of the process into an existing
product (WAY-28) will call it too, each adding what it needs
(`TODO — decision pending: which decision sets how foundation entries are found in a source`).

This skill lives in `elements/common/skill/` of the-way. Installed globally, its base directory is
a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in PowerShell.
`elements/common/` is the parent of the resolved directory, and the-way the directory two above
that. In a product, the-way is the product's pinned `.the-way`, and each skill named below is the
product's skill of that name with the `the-way-` prefix.

## What the caller gives

- the source — for a project definition: the definition, the conversation that wrote it, and the
  material it started from, in the part the project concerns;
- the next reader — for a project definition: the breakdown of the project into tasks;
- the mode of the entries — for a project definition: projected, into its section "Projected
  foundation changes".

When that section already holds a working table, resume from the first row whose state is neither
`rejected` nor `written`.

## 1. Read

- Read `elements/common/way_of_working.md` in full, and in `project-level/definition_template.md`
  the section "Projected foundation changes" in full.
- Read the source in full.
- Read the product's `foundations/`, so that no candidate repeats an entry that stands there, and a
  candidate that collides with one is shown beside it.
- Read in each element's template what makes something an entry of it: the plan test in the
  decisions' template (WAY-36, WAY-26); "Which words take an entry" in the glossary's; "Which facts
  are written" in the environment facts'; for an invariant, a sentence a commit can make false; for
  the part map, only an entry whose every field is known before the code.

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
- Write the table into the definition as the template's working table, every row `waiting`; then
  show it.

## 3. The human cuts

The human accepts or rejects rows, all at once or a few at a time. Write each state into the
working table as soon as it is given.

## 4. Row by row

For each accepted row, in the table's order:

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
4. An entry that skill reports as following from this one becomes a row of the table, `accepted`,
   its source naming the entry it follows from.

## 5. Close

- Once every row is `rejected` or `written`, take the working table out and write as the section's
  first line `Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD`, as the
  template gives it; the rows shown are every row the table held, the rows step 4 added
  included. With no row accepted, `none` stands below the line.
- Tell the caller how many entries of each kind were written.
