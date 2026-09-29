---
name: record-invariant
description: Use when a product's invariants file, foundations/invariants.md, has to gain or change an entry — a rule the product must keep, from conversation, a task's return step, the behaviour of the critical flows and the parts they run through or an invariant a decision's verification calls for; a changed, split, merged or withdrawn invariant; or a row on the list of violated or quarantined invariants.
---

# Record an invariant

Turns a rule the product has to keep into an entry of its invariants file. Every rule of an entry
stands in this element's `template.md` and in `elements/common/rules.md`, and the way of working
the skills share stands in `elements/common/way_of_working.md`; this skill holds only what is
particular to an invariant (WAY-35).

This skill lives in `elements/invariants/skill/` of the-way. Installed globally, its base
directory is a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in
PowerShell. The element's directory is the parent of the resolved one, and the-way the directory
three above it. Follow the steps of `elements/common/way_of_working.md` there; below is what an
invariant adds to each.

## 1. Read

- Read the product's `foundations/invariants.md`, `foundations/part_map.md` and
  `foundations/decisions.md` — an entry names parts of the map and decisions of the log.

## 2. Decide what the entry is

- Find the rule and where it is said: the conversation, a decision's verification, the list a
  task's return step made, or the product's code when the process enters an existing product.
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
  rule, a flow of the part map carrying its sentence, a failure mode it detects, and a named link
  whose entry's binding part has changed, to recheck and carry its new fingerprint (WAY-66).

## 3. Draft

- *Method*: take its form from the template, tell the human which form it is and why, and do not
  write the check to have something to name.
- *Part*: for each part named, say which change there could make the sentence false.
- *Rests on*: put through the test in the template's section "Links" every fact quoted in the
  *Based on* of the decisions it derives from, and every fact that neither the product nor the-way
  at the commit it pins writes, such as a standard, a library or a law, found behind what the
  sentence names, a value it copies, or a meaning the product's rules hand elsewhere, as the part
  map hands the matching of a pattern to git.
- An entry the human chose from what the product already does: search the decision log, the
  product's documents and the history of the code, and draft its row on the list of recovered
  invariants; the human deciding the change sets it, as the template's "Recovered" says.

## 4. Ask, show, write

- Step 4.2: for a changed entry, show the wording on `{fork-point}` beside the new one, with the
  checks that cite it, so that the human settles a raise or a correction as the template's
  "Version and correction" says.
- Step 4.4: what follows from this entry is a decision whose level 1 verification gains, loses or
  renames it, through `record-decision`; and a flow or a failure mode that names it, or names an
  identifier this change retires, through `update-part-map`.
- After step 4.4, where the method is a command, hand the human two instructions for two other
  agents: for the check — the entry, its method, and the checks citing an identifier this change
  retires or a version it raises; for the deliberate break — the sentence, without the check and
  the files it reads (WAY-69). Where it is not a command, there is nothing to hand on.

## Violated and quarantined invariants

For a row on the list of violated invariants, ask first whether the product is to be fixed
instead, and whether the entry is one the product does not meet or one with no runnable method,
which the template reports `unchecked` instead (WAY-67). Before a quarantine, ask for the `pass`
and `fail` recorded on one commit, whether a change of the invariant test's mechanics answers it
instead, and the end date.
