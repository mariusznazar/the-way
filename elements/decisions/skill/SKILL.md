---
name: record-decision
description: Use when a decision has to be written into a product's decision log, foundations/decisions.md — a choice just settled in conversation that binds later work, a new answer to a question the log already holds, a decision recovered from existing code, a due review of a decision whose review-when date has come, or a decision a project definition projects.
---

# Record a decision

Turns a decision into an entry of a product's decision log. Every rule of an entry stands in this
element's `template.md` and in `elements/common/rules.md`, and the way of working the skills share
stands in `elements/common/way_of_working.md`; this skill holds only what is particular to a
decision (WAY-35).

This skill lives in `elements/decisions/skill/` of the-way. Installed globally, its base directory
is a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in
PowerShell. The element's directory is the parent of the resolved one, and the-way the directory
three above it. Follow the steps of `elements/common/way_of_working.md` there; below is what a
decision adds to each.

## 1. Read

- Read the product's `foundations/decisions.md`. When the log has no entries, ask the human for
  the product's prefix.

## 2. Decide what the entry is

- Find what was decided and where it is said: the conversation, a document the human names, or
  existing code — then the template's section on inherited decisions applies.
- Apply the template's plan test. When the rule belongs to a plan, stop and say so; no entry is
  written.
- Name the one question the binding sentences answer. When they answer two independent
  questions, propose two entries, or keep the question the rest serves.
- Search the log for that question. What a question found there takes, and what a new one takes,
  the template's "Where entries go" and "Numbers and versions" give.
- The search of the foundation also looks for a collision with another decision, which is a
  question in step 4 (WAY-25), and for a sentence of another decision that answered this question
  in passing, which moves as "Numbers and versions" says.

## 3. Draft

- *Based on*: sort what the source offers as a reason before filling the field — what is not yet
  known, or the decider's own motive, is no fact about the world. What is not yet known goes to
  *Review when*, as the template's "Review" gives it; the decider's motive goes to *Rationale*.
- *Verification*: try first to state an invariant — a sentence about the product that is false on
  a commit which breaks this decision — before choosing levels by the template's "Verification".
  Each invariant level 1 names is written through `record-invariant` in step 4.4.
- `none considered` in *Rejected* is the human's statement.
- *Approved by* reads `on acceptance` in the draft.

## 4. Ask, show, write

- Step 4.2: on acceptance, write who accepted and the date in *Approved by*.
- Step 4.4: what follows from this entry is a version or an edit of a neighbour found in step 2;
  every invariant this entry's level 1 verification names that the invariants file does not hold
  yet, through `record-invariant`; and, when this entry changes a decision's binding sentences,
  every decision that derives from it or narrows it, and every invariant whose *Derives from*
  names it, the invariants through `record-invariant`.

## Projected mode

The skill `define-project` hands a decision to this skill in projected mode, naming a project
definition. Steps 1–4 run as above, with these differences
(`TODO — decision pending: which decision sets how a decision is projected in a project
definition`):

- Step 2: apply the plan test first. An exclusion or a rule that ends with the project stays in the
  definition, under "Out of scope", and no entry is written (WAY-36, WAY-26).
- Step 3: the heading reads `### (new) — <question>` for a new decision, or the current decision's
  number with its next version; *Approved by* reads `on acceptance`.
- Step 4.3: write the entry under "Projected foundation changes" of the definition, followed by its
  translation as the definition's template gives it, and nothing into `foundations/decisions.md`.
  Run no format guard, and tell the human that no script checked the entry's form: the guard
  checks it in the task that writes the decision into the log.
- Step 4.4: nothing that follows is written into the foundation either. A change to a neighbouring
  decision is another projected decision; an invariant the verification names is an open question
  of the definition, with its place of resolution.

## Review record

When a *Review when* date has come, ask the human what has been observed and write a review
record in one of the template's three forms. When the condition is met and the decision
changes, the new version goes through steps 2–4 first, and the review record names it. Before
the main branch, a decision that changes is instead edited in place: the edit rewrites *Review
when* from what was observed, and the decision's approver accepts it again, which answers the date
as well; a check-by date is moved in no other way (WAY-24).
