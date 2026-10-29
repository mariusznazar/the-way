---
name: record-decision
description: Use when a decision has to be written into a product's decision log, foundations/decisions.md — a choice just settled in conversation that binds later work, a new answer to a question the log already holds, a decision recovered from existing code, a decision no longer needed, or a decision a project definition projects.
---

# Record a decision

Turns a decision into an entry of a product's decision log. Every rule of an entry stands in this
element's `template.md` and in `elements/common/rules.md`, and the way of working the skills share
stands in `elements/common/way_of_working.md`; this skill holds only what is particular to a
decision (WAY-35).

This skill lives in `elements/decisions/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/decisions/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what a decision adds to each.

## 1. Read

At step 1, read `read.md` beside this skill for the reading this entry needs.

## 2. Decide what the entry is

At step 2, read `decide_entry.md` beside this skill to decide what the entry is and what
the search of the foundation adds for this element.

## 3. Draft

- *Based on*: sort what the source offers as a reason before filling the field — what is not yet
  known, or the decider's own motive, is no source outside the product.
- *Verification*: name the invariants the invariants file holds that derive from this decision,
  and those step 4.4 writes; add a pair of examples where the human gives one or accepts one you
  propose.
- `none considered` in *Rejected* is the human's statement.

## 4. Ask, show, write

- Step 4.4: what follows from this entry is an edit of a neighbour found in step 2; every invariant
  this entry's *Verification* names that the invariants file does not hold yet, through
  `record-invariant`; and, when this entry changes a decision's binding sentences or removes it,
  every decision that derives from it or narrows it, and every invariant whose *Derives from* names
  it, the invariants through `record-invariant`.

## Projected mode

In projected mode, read `elements/common/projected_mode.md`, with these differences for a
decision (WAY-117):

- Step 1: ask for no prefix for a new decision; the task that writes it into the log asks for the
  prefix when the log has no entries. A projected change of an existing decision keeps its
  number.
In projected mode, read `projected.md` beside this skill for the plan test and
what follows from the decision.
- Step 3: the heading reads `#### (new) — <question>` for a new decision, or
  `#### <PREFIX>-<NN> — <question>` for a change of a current one.
