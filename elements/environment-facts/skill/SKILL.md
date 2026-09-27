---
name: record-environment-fact
description: Use when a product's environment facts file, foundations/environment_facts.md, has to gain or change an entry — a fact an invariant's Rests on or a decision's Based on needs, a citation whose change would send its decision to review, a fact a task's return step found, a failed run of a fact's method, or a fact shown false or left with nothing resting on it.
---

# Record an environment fact

Turns a fact about the world around the product into an entry of its environment facts file.
Every rule of an entry lives in `template.md`; this skill holds only the way of working. A
fix that concerns a rule of the entry goes to the template, not here (WAY-35).

## 1. Read the rules and the foundation

This skill lives in `elements/environment-facts/skill/` of the-way repository. Installed globally,
its base directory is a link, so resolve it first: `realpath <base>` in Bash,
`(Get-Item <base>).Target` in PowerShell. Read in full `template.md` from the parent of the
resolved directory, `examples.md` where it exists, and the product's
`foundations/environment_facts.md`, `foundations/invariants.md`, `foundations/decisions.md` and
`foundations/part_map.md` where they exist, sharing one space of identifiers; with no part map,
`update-part-map` writes it first. With no `foundations/environment_facts.md`, ask whether the
product starts its facts here; if not, stop; if so, the change claims the new file for a part of
the map through `update-part-map` and settles there where the checks of its facts stand
(WAY-81), and writes every fact an invariant or a decision's *Based on* still waits for (WAY-90) —
one reaching a pending line going to the human first.
Before drafting, read in full the product's `foundations/glossary.md` where it exists and, in a
product other than the-way, the-way's `foundations/glossary.md` in the pinned copy, three
directories above the resolved one (WAY-34, WAY-92, WAY-95).

## 2. Decide what the entry is

- Find what asks for the fact: a `TODO` in an invariant's *Rests on*, a citation in a decision's
  *Based on*, a fact a task's return step listed (WAY-11, a warning until its dependant is written,
  WAY-88), the conversation, a failed run of a method, or a fact left `unchecked` because its probe ran
  on a release outside *Holds for* (WAY-91).
- Put it through "Which facts are written": a citation failing its test stays quoted; one resting
  only on being a reason, not a condition, leaves an invariant's *Rests on* through
  `record-invariant`. Through "The sentence": an invariant is no fact, what runs a method is no
  fact, and a study's measurement is the fact — its transfer to this process's agents goes to
  *Review when* of each decision citing it, via `record-decision` (WAY-85).
- A requirement of a catalogue nothing has adopted goes to the human as "do we adopt this?" before
  any entry. A binding rule is read as applying, with "does this bind us?" asked in step 4
  (WAY-86); while the template holds whether "the rule applies" is a fact as pending, such a case
  stops as the last bullet of this step says.
- Search the file, withdrawn identifiers included, for an entry on the same thing: found — a
  change, split, merge or withdrawal; found among the withdrawn — show the human why it went: one
  shown false comes back only if the world has changed since, one withdrawn for want of dependants
  may come back, either way under a new identifier; not found — a new identifier.
- Search the whole foundation for entries this fact touches with no written link (WAY-33) — an
  obligation raising a part's criticality included, through `update-part-map` (WAY-87). Each
  finding becomes a link, a change, or a question in step 4.
  The search also asks whether the entry uses a glossary term in another meaning than its entry
  gives, or spells out a term's definition instead of using the term (WAY-33): a paraphrase is
  rewritten to the term, and another meaning, or a word the glossary does not yet settle, goes
  through `record-glossary-term`.
- A case needing a pending line to fill a field stops the entry, for the human and
  `record-decision`, before it is written; one about the check alone — the method, or the
  deliberate break — travels as an open question in step 4.6 instead.

## 3. Draft

Fill every field according to the template, with extra care for these:

- *Source*: open the address and copy the passage as the template's "Source" section gives it, at
  its frozen edition; missing there, it is a question in step 4. For an observation, take the
  tool's version and platform from running the command yourself, never the conversation. For a
  page without editions, use the archive's CDX index of captures, not its availability lookup,
  which misses captures that exist.
- The sentence and *Holds for*: from the source as read there, never from memory; a value the
  source does not give is a question in step 4.
- *Set by*: who sets a setting kept outside the repository is the human's answer, never a guess.
- *Method*: take its form from the template, and say which and why; do not write the probe or
  watch just to have something to name. Whether WAY-08's deliberate break binds a fact's method is
  the template's own pending question — say so, settling neither answer.

## 4. Ask, check, show, write

1. Check mechanically before asking: the address opens, the passage stands word for word, a named
   tool or package exists in the release *Holds for* gives, and an observation repeats on a rerun;
   a failure sends the draft back to step 3.
2. Ask in one round about what is still open, each question with a proposed value and the reason
   for it. A question about a fact proposes where to look for it, never the fact from memory, and
   the draft takes it only as read there.
3. Show the whole entry. For a changed entry, show the wording on `{fork-point}` beside the new
   one, with the checks and dependants that cite it — a check needing a different expected value
   makes it a raise. Write nothing before the human accepts it.
4. Write the entry in its place. Where the format guard exists, run it from the repository root,
   `python -B <parent of the resolved directory>/format_guard.py foundations/environment_facts.md
   --base <the commit the branch left the main branch from>`, leaving out `--base` with no main
   branch; fix what broke and rerun.
5. What follows goes one at a time: each invariant this fact serves, or whose fingerprint in
   *Rests on* it moves, through `record-invariant`; each decision naming it, through
   `record-decision`. A fact that stood on `{fork-point}` and is left unnamed is withdrawn in the
   same change (WAY-88); one new on this branch waits for its dependant as a warning, and one still
   unnamed when the branch is to merge is taken out.
6. Where the method is a command, hand the human an instruction for another agent: the entry, its
   method, and the checks citing a retired identifier or raised version — never the conversation
   itself; a withdrawal hands on the checks still citing the withdrawn identifier. Where the method
   is a path, the fact stays unchecked until the human re-reads the source; write their verdict,
   *Commit* and *Until* into `foundations/human_verdicts.md`, its first row claiming that file
   through `update-part-map` (WAY-83). `TODO` hands on nothing.

## A failed run and a withdrawal

- A failed watch opens a review, not a verdict of falsehood: show the human the old passage beside
  what stands now, with the decisions naming the fact; they decide whether it moves to the new
  edition, stays on the old, or is withdrawn as shown false.
- A failed probe: show its output beside the passage; whether the world changed, the probe is
  wrong, or the machine runs a release outside *Holds for* is theirs to settle, and a wrong probe goes back to its author. A human re-read giving `fail` is
  handled the same way as a failed watch; a verdict past *Until* is renewed by a fresh re-read.
- A withdrawal follows the template's "Withdrawn identifiers"; each dependant goes through
  `record-invariant` or `record-decision` in the same change.
