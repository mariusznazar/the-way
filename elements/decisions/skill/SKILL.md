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

- Select and read current log entries by "Reading the foundation" in
  `elements/common/way_of_working.md`. Read the existing entry this operation changes, and inspect
  the log's numbers and its withdrawn numbers before assigning one. When the log has no entries,
  ask the human for the product's prefix — except in projected mode, where a new decision has no
  prefix yet.

## 2. Decide what the entry is

- Find what was decided and where it is said: the conversation, a document the human names, or
  existing code — then the template's section on recovered decisions applies.
- Apply the template's plan test. When the rule ends with the work, stop and name its place:
  the plan, or the choices of the cycle record where no plan is written; no entry is written.
- Name the one question the binding sentences answer. When they answer two independent
  questions, propose two entries, or keep the question the rest serves.
- Search the log for that question. A question the log already answers takes an edit of that entry
  in place, and a new one takes the next number, as the template's "Changing a decision" gives it.
- The search of the foundation also looks for a collision with another decision, which is a
  question in step 4 (WAY-25), and for a sentence of another decision that answered this question
  in passing, which moves as "Changing a decision" says.

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

Projected mode runs as `elements/common/way_of_working.md` gives it, with these differences for a
decision (WAY-117):

- Step 1: ask for no prefix for a new decision; the task that writes it into the log asks for the
  prefix when the log has no entries. A projected change of an existing decision keeps its
  number.
- Step 2: apply the plan test first. An exclusion or a rule that ends with the project stays in the
  definition, under "Out of scope", and no entry is written (WAY-36, WAY-26).
- Step 3: the heading reads `#### (new) — <question>` for a new decision, or
  `#### <PREFIX>-<NN> — <question>` for a change of a current one.
- Step 3: for a technology choice `settle-technology` hands over, the lacks of the option chosen
  and the risks the human took with it stand where the template's "Decision entry" puts them,
  beside its rule for *Rationale*.
- Step 4.4: an invariant the verification names is a projected invariant, which follows from this
  entry as `way_of_working.md` gives it for projected mode.
