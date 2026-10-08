---
name: record-environment-fact
description: Use when a product's environment facts file, foundations/environment_facts.md, has to gain or change an entry — a fact an invariant's Rests on or a decision's Based on needs, a citation whose change would send its decision to review, a fact a task's return step found, a failed run of a fact's method, a fact shown false or left with nothing resting on it, or a fact a project definition projects.
---

# Record an environment fact

Turns a fact about the world around the product into an entry of its environment facts file.
Every rule of an entry stands in this element's `template.md` and in `elements/common/rules.md`,
and the way of working the skills share stands in `elements/common/way_of_working.md`; this skill
holds only what is particular to an environment fact (WAY-35).

This skill lives in `elements/environment-facts/skill/` of the-way. In the-way itself, the-way is
the checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/environment-facts/` there, and each the-way skill named below is
the project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what an environment fact adds to each.

## 1. Read

- Read the product's `foundations/environment_facts.md`, `foundations/invariants.md`,
  `foundations/decisions.md` and `foundations/part_map.md` where they exist.
- A product that starts its facts here also settles where the checks of its facts stand in the
  map, as the template's "Method" asks, and writes every fact an invariant's *Rests on* or a
  decision's *Based on* waits for (WAY-37, WAY-90) — one reaching a pending line going to the
  human first.

## 2. Decide what the entry is

- Find what asks for the fact: a `TODO` in an invariant's *Rests on*, a citation in a decision's
  *Based on*, a fact a task's return step listed (WAY-11), the conversation, a failed run of a
  method, or a fact left `unchecked` because its probe ran on a release outside *Holds for*
  (WAY-81).
- Put it through the template's "Which facts are written" and "The sentence", and send what
  fails them where they say — into an invariant through `record-invariant`, into a decision
  through `record-decision`.
- A requirement of a catalogue nothing has adopted goes to the human with the question the
  template's "Catalogues and obligations" gives, before any entry; for a binding rule, that
  question is asked in step 4.
- Search the file, withdrawn identifiers included, for an entry on the same thing: found — a
  change, split, merge or withdrawal; found among the withdrawn — show the human why it went: one
  shown false comes back under a new identifier only if the world has changed since, one withdrawn
  for want of dependants may come back under a new identifier; not found — a new identifier.
- The search of the foundation also looks for an obligation raising a part's criticality, which
  goes through `update-part-map` (WAY-46).
- A case needing a pending line to fill a field stops the entry, for the human and
  `record-decision`, before it is written; one about the check alone — the method — travels
  as an open question in the instruction handed on after step 4.4 instead.

## 3. Draft

- *Source*: open the address and copy the passage as the template's "Source" gives it; missing
  there, it is a question in step 4. For an observation, take the tool's version and platform from
  running the command yourself, never from the conversation. For a page without editions, find
  the archived copy through the archive's CDX index of captures, not its availability lookup,
  which misses captures that exist.
- *Method*: take its form from the template, and say which and why; do not write the probe or
  watch just to have something to name. Whether WAY-08's deliberate break binds a fact's method is
  the template's own pending question — say so, settling neither answer.

## 4. Check, ask, show, write

- Before step 4.1, check mechanically: the address opens, the passage stands word for word, a
  named tool or package exists in the release *Holds for* gives, and an observation repeats on a
  rerun. A failure sends the draft back to step 3.
- Step 4.2: for a changed entry, show the wording on `{fork-point}` beside the new one, with the
  checks and dependants that cite it.
- Step 4.4: what follows is each invariant this fact serves, or whose fingerprint in *Rests on* it
  moves, through `record-invariant`; and each decision naming it, through `record-decision`. A fact
  left with nothing naming it goes as WAY-73 and the template's "Withdrawn identifiers" say.
- After step 4.4, where the method is a command, hand the human an instruction for another agent
  (in a task cycle the orchestrator dispatches that agent itself): the entry, its method, the
  checks citing a retired identifier or raised version, and any open question about the check —
  never the conversation itself; a withdrawal hands on the checks still citing the withdrawn
  identifier. Where the method is a path, the human re-reads the
  source; write their verdict into `foundations/human_verdicts.md` in the row
  `elements/common/rules.md` gives, the first row giving that file to a part through
  `update-part-map`. `TODO` hands on nothing.

## Projected mode

Projected mode runs as `elements/common/way_of_working.md` gives it, with these differences for a
fact (WAY-117):

- Step 2: a fact is projected only where a projected decision's *Based on* or a projected
  invariant's *Rests on* names it (WAY-73, WAY-90).
- Step 3: the entry is written whole; its source exists today and is read now.
- Step 4: the mechanical check before step 4.1 runs as above. After step 4.4 nothing is handed on,
  and no verdict is written into `foundations/human_verdicts.md`.
- Step 4.3: the heading reads `#### <identifier>/1`, or the current identifier with its next
  version.

## A failed run and a withdrawal

- On a failed watch, show the human the old passage beside what stands now, with the decisions
  naming the fact; they decide whether it moves to the new edition, stays on the old, or is
  withdrawn as shown false.
- A failed probe: show its output beside the passage; whether the world changed, the probe is
  wrong, or the machine runs a release outside *Holds for* is theirs to settle, and a wrong probe
  goes back to its author. A human re-read giving `fail` is handled the same way as a failed
  watch; a verdict past *Until* is renewed by a fresh re-read.
- A withdrawal follows the template's "Withdrawn identifiers"; each dependant goes through
  `record-invariant` or `record-decision` in the same change.
