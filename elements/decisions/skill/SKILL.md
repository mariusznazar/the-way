---
name: record-decision
description: Use when a decision has to be written into a product's decision log, foundations/decisions.md — a choice just settled in conversation that binds later work, a new answer to a question the log already holds, a decision recovered from existing code, or a due review of a decision whose review-when date has come.
---

# Record a decision

Turns a decision into an entry of a product's decision log. Every rule of the entry lives in
`template.md`; this skill holds only the way of working. A fix to a rule of the entry goes to
the template, together with a decision in the log (WAY-05).

## 1. Read the rules and the log

This skill lives in `elements/decisions/skill/` of the-way repository. Installed globally, its
base directory is a link, so resolve it first: `realpath <base>` in Bash,
`(Get-Item <base>).Target` in PowerShell. Read in full `template.md` and `examples.md` from the
parent of the resolved directory, and the product's `foundations/decisions.md`. Entries take the
prefix and the language of the log; when the log has no entries, ask for both. When the
repository has no `foundations/decisions.md`, ask whether the product starts its decision log
here; if not, stop.

## 2. Decide what the entry is

- Find what was decided and where it is said: the conversation, a document the human names, or
  existing code (then the template's section on inherited decisions applies).
- Name the one question the binding sentences answer. When they answer two independent
  questions, propose two entries, or keep the question the rest serves.
- Search the log for that question: found on the main branch — a new version, with its kind of
  change from the template's table; found only on this branch — a correction in place, shown for
  acceptance again when it changes the meaning; not found — a new number.
- Search the whole foundation, not only the decisions with an overlapping *Scope*, for entries
  this one touches that no written link joins to it. Each finding becomes a relation, a question
  about a collision in step 4, or a sentence that answered this question in passing and now needs
  a version or a correction without it.

## 3. Draft

Fill every field according to the template, with extra care for these:

- *Based on*: take each fact about the world from a source the human gives, never from memory.
  What is not yet known, or the decider's own motive, is not such a fact: it belongs in
  *Rationale*, or in *Review when* when the decision waits for it.
- *Verification*: before choosing level 2 or 3, try to state an invariant in working form — a
  sentence about the product that is false on a commit which breaks this decision. Level 1
  names only such sentences; level 2 or 3 covers the rest of the decision.
- `none` and `none considered` are the human's statements. Where the source is silent, the
  field becomes a question in step 4.
- *Approved by* reads `on acceptance` in the draft.

## 4. Ask, show, append

1. Ask in one round about everything the source leaves open, each question with a proposed
   value and the reason for it.
2. Show the whole entry. Apply corrections; on acceptance, write who accepted and the date in
   *Approved by*.
3. Check the entry against the template's list "What the format guard checks", then append it
   at the end of the log.
4. Entries that follow from this one — a version or a correction of a neighbour found in
   step 2, and, when this entry changes a decision's binding sentences, every decision that
   derives from it or narrows it — go through steps 3 and 4 one at a time.

## Review entry

When a *Review when* date has come, ask the human what has been observed and write a review
entry in one of the template's three forms. When the condition is met and the decision
changes, the new version goes through steps 2–4 first, and the review names it.
