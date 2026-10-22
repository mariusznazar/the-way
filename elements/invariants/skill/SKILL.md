---
name: record-invariant
description: Use when a product's invariants file, foundations/invariants.md, has to gain or change an entry — a rule the product must keep, from conversation, a task's return step, the behaviour of the critical flows and the parts they run through or an invariant a decision's verification calls for; a changed, split, merged or withdrawn invariant; an invariant the product does not meet today, marked violated; or an invariant a project definition projects.
---

# Record an invariant

Turns a rule the product has to keep into an entry of its invariants file. Every rule of an entry
stands in this element's `template.md` and in `elements/common/rules.md`, and the way of working
the skills share stands in `elements/common/way_of_working.md`; this skill holds only what is
particular to an invariant (WAY-35).

This skill lives in `elements/invariants/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/invariants/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what an invariant adds to each.

## 1. Read

- Select and read invariant and decision entries by "Reading the foundation" in
  `elements/common/way_of_working.md`, using the complete part map — an entry names parts of the
  map and decisions of the log.

## 2. Decide what the entry is

- Find the rule and where it is said: the conversation, a decision's verification, the list a
  task's return step made, a ticket or a requirement of the product, or the product's code when
  the process enters an existing product.
- Recovering from what a product does: list what the part does, each item as a candidate
  sentence with the place in the code that shows it, and let the human choose; only what the
  human chooses becomes an entry (WAY-28).
- Apply the test in the decision template's section "Decision or invariant": a rule that records
  a choice goes through `record-decision` first, and the invariant is written as derived from it.
  A reason found behind recovered behaviour is not recovered as a decision in this change (WAY-28);
  one the human gives is (`TODO — decision pending: which decision sets that a reason the human
  gives for recovered behaviour is written as a decision`).
- When the rule holds more than one sentence can state, propose one entry per sentence; the
  template says what one sentence may join.
- Search the file, including its withdrawn identifiers, for an entry this rule would change:
  found — a change, split, merge or withdrawal, or an entry of its own where the template's "Where
  entries go" gives one; not found — a new identifier.
- The search of the foundation also looks for a decision whose level 1 verification calls for this
  rule, and an entry it names whose binding part has changed, to check it against that part again
  (WAY-31).

## 3. Draft

- *Method*: `test` where a cheap test can check the sentence on the product, `review` otherwise,
  as the template's "Method and test" gives it; tell the human which and why, and never write a test
  only so that *Method* can read `test`.
- *Part*: for each part named, say which change there could make the sentence false.
- *Rests on*: put through the test in the template's section "Links" every fact quoted in the
  *Based on* of the decisions it derives from, and every fact that neither the product nor the-way
  at the commit it pins writes, such as a standard, a library or a law, found behind what the
  sentence names, a value it copies, or a meaning the product's rules hand elsewhere, as the part
  map hands the matching of a pattern to git.
- An entry taken from a source outside the log, such as a ticket or a requirement of the product,
  which no decision of the log carries: *Derives from* quotes that source with its address, place,
  passage and date read, as the template's "Links" says.
- An entry the human chose from what the product already does, which neither a decision of the log
  nor such a source carries: *Derives from* reads `recovered from code —` and the place in the code
  that shows the behaviour, as the template's "Links" says.
- *Violated*: `yes` only for a rule the product does not meet today; ask first whether the product
  is to be fixed instead (WAY-51).

## 4. Ask, show, write

- Step 4.2: for a changed entry, show the wording on `{fork-point}` beside the new one, with the
  tests that cite it, and check each of those tests against the new wording.
- Step 4.4: what follows from this entry is a decision whose level 1 verification gains, loses or
  renames it, through `record-decision`.
- After step 4.4 nothing is handed to another agent. Where *Method* reads `test`, the test is
  written in the change that brings the entry and seen failing once, as the template's "Method and
  test" says; the change names in its request each invariant test it alters (WAY-03).

## Projected mode

Projected mode runs as `elements/common/way_of_working.md` gives it, with these differences for an
invariant (WAY-117):

- Step 3: *Method* reads `review`; the task that writes the invariant turns it to `test` with the
  test, where a cheap test can check the sentence; *Part* names parts the product's map holds, and `every` where the map holds
  no part yet; *Derives from* a projected decision reads
  `TODO — <the decision's question>, projected in <the definition's path>`.
- Step 4.3: the heading reads `#### <identifier>`.
- After step 4.4 nothing is handed on: the test waits for the task that writes the invariant.
