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

At step 2, read `decide_entry.md` beside this skill to decide what the entry is and what
the search of the foundation adds for this element.

## 3. Draft

- *Method*: `test` where a cheap test can check the sentence on the product, `review` otherwise,
  as the template's "Method and test" gives it; tell the human which and why, and never write a test
  only so that *Method* can read `test`.
- At step 3, read `draft.md` beside this skill to check the parts and the facts the invariant
  rests on.
- An entry taken from a source outside the log, such as a ticket or a requirement of the product,
  which no decision of the log carries: *Derives from* quotes that source with its address, place,
  passage and date read, as the template's "Links" says.
- An entry the human chose from what the product already does, which neither a decision of the log
  nor such a source carries: *Derives from* reads `recovered from code —` and the place in the code
  that shows the behaviour, as the template's "Links" says.
- *Violated*: `yes` only for a rule the product does not meet today; ask first whether the product
  is to be fixed instead (WAY-51).

## 4. Ask, show, write

At step 4, read `write.md` beside this skill for what to check, show and write, and what
follows from the entry.

## Projected mode

In projected mode, read `elements/common/projected_mode.md`, with these differences for an
invariant (WAY-117):

- Step 3: *Method* reads `review`; the task that writes the invariant turns it to `test` with the
  test, where a cheap test can check the sentence; *Part* names parts the product's map holds, and `every` where the map holds
  no part yet; *Derives from* a projected decision reads
  `TODO — <the decision's question>, projected in <the definition's path>`.
- Step 4.3: the heading reads `#### <identifier>`.
- After step 4.4 nothing is handed on: the test waits for the task that writes the invariant.
