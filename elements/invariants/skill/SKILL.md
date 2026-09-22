---
name: record-invariant
description: Use when a product's invariants file, foundations/invariants.md, has to gain or change an entry — a rule the product must keep, from conversation, a task's return step, a critical part's behaviour or a decision's working form; a changed, split, merged or withdrawn invariant; or a position on the list of violated or quarantined invariants.
---

# Record an invariant

Turns a rule the product has to keep into an entry of its invariants file. Every rule of an entry
lives in `template.md`; this skill holds only the way of working. A correction that concerns a
rule of the entry goes to the template, not here (WAY-35).

## 1. Read the rules and the foundation

This skill lives in `elements/invariants/skill/` of the-way repository. Installed globally, its
base directory is a link, so resolve it first: `realpath <base>` in Bash,
`(Get-Item <base>).Target` in PowerShell. Read in full `template.md` from the parent of the
resolved directory, `examples.md` where it exists, and the product's `foundations/invariants.md`,
`foundations/part_map.md` and `foundations/decisions.md` — an entry names parts of the one and
decisions of the other. Entries take the language of the file; when it has no entries, ask for
it. When the repository has no `foundations/invariants.md`, ask whether the product starts its
invariants here; if not, stop; if so, the same change claims the new file for the `invariants`
part of the map through `update-part-map`. When it has no part map, the map comes first: stop until
`update-part-map` has written it.

## 2. Decide what the entry is

- Find the rule and where it is said: the conversation, a decision's verification, the list a
  task's return step made, or the product's code when the process enters an existing product.
- Recovering from what a product does: list what the part does, each item as a candidate
  sentence with the place in the code that shows it, and let the human choose; only what the
  human chooses becomes an entry (WAY-28).
- Apply the test in the decision template's section "Decision or invariant": a rule that records
  a choice goes through `record-decision` first, and the invariant is written as derived from it.
  A reason found behind recovered behaviour is not recovered as a decision in this change; one the
  human gives is (WAY-58).
- When the rule holds more than one sentence can state, propose one entry per sentence; the
  template says what one sentence may join.
- Search the file, including its withdrawn identifiers, for an entry this rule would change:
  found — a change, split, merge or withdrawal, unless it guards a different aspect of the same
  thing, which takes its own identifier; not found — a new identifier.
- Search the whole foundation, not only the decisions this one derives from, for entries it
  touches that no written link joins to it, reading *Rejected* as well as what binds (WAY-33): a
  decision naming this rule in working form, a flow of the part map carrying its sentence, a
  failure mode it detects, or a named link whose entry has changed wording, to recheck and carry
  its new fingerprint (WAY-66). Each finding becomes a link, a change to an entry or a question in
  step 4.

## 3. Draft

Fill every field according to the template, with extra care for these:

- The sentence: every value it needs comes from the source; one the source does not give is a
  question in step 4, never a plausible number.
- *Method*: take its form from the template, tell the human which form it is and why, and do not
  write the check to have something to name.
- *Part*: for each part named, say which change there could make the sentence false.
- *Recovered*: for an entry the human chose from what the product already does, search the
  decision log, the product's documents and the history of the code, and draft the field; the
  human deciding the change sets it with the gate's report in front of them (WAY-58).
- A value the template's closed lists do not hold is a question in step 4, and the list grows by
  a new version of the decision that closed it. Do not reach for the nearest value (WAY-54).

## 4. Ask, show, write

1. Ask in one round about everything the source leaves open, each question with a proposed value
   and the reason for it.
2. Show the whole entry. For a changed entry, show the wording on `{fork-point}` beside the new
   one, with the checks that cite it: a test needing a different expected value makes it a raise;
   otherwise a correction stands only on the human's word. Write nothing before the human accepts
   it.
3. Write the entry in its place in the file and run the format guard from the product's
   repository root, `python -B <parent of the resolved directory>/format_guard.py --base <the
   commit the task branch left the main branch from>`, leaving out `--base` where there is no
   main branch; fix what the entry broke and run it again, and give an error or an unchecked line
   elsewhere in the file to the human.
4. What follows from this entry goes one at a time: a decision that named it in working form, or
   whose verification changes, through `record-decision`; a flow or a failure mode that names it,
   or names an identifier this change retires, through `update-part-map`.
5. Where the method is a command, hand the human two instructions for two other agents: for the
   check — the entry, its method, and the checks citing an identifier this change retires or a
   version it raises; for the deliberate break — the sentence, without the check and the files it
   reads (WAY-69). Where it is not a command, the entry enters unchecked; there is nothing to
   hand on.

## Violated and quarantined invariants

For a position on the list of violated invariants, ask first whether the product is to be fixed
instead; an entry with no runnable method is `unchecked`, not debt (WAY-67). Before a quarantine,
ask for the `pass` and `fail` recorded on one commit, whether a change of the test's form answers
it instead, and the end date.
