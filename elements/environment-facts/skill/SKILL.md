---
name: record-environment-fact
description: Use when a product's environment facts file, foundations/environment_facts.md, has to gain or change an entry — a fact an invariant's Rests on or a decision's Based on needs, a citation whose change would call its decision into question, a source a task's return step found, a source that no longer says what its fact says, a fact shown false or left with nothing resting on it, or a fact a project definition projects.
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

- Select and read facts and their actual decision and invariant dependents by "Reading the
  foundation" in `elements/common/way_of_working.md`, using the complete part map where it exists.
- A product that starts its facts here writes every fact an invariant's *Rests on* or a decision's
  *Based on* waits for (WAY-37, WAY-90) — one reaching a pending line going to the human first.

## 2. Decide what the entry is

- Find what asks for the fact: a `TODO` in an invariant's *Rests on*, a citation in a decision's
  *Based on*, a source a task's return step listed (WAY-11), the conversation, or a source found no
  longer saying what a fact's sentence says.
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
  goes through `update-part-map` (WAY-46). For a changed fact, it finds every invariant whose *Rests
  on* and every decision whose *Based on* names the fact, as the template's "Changing a fact" says.
- A case needing a pending line to fill a field stops the entry, for the human and
  `record-decision`, before it is written.

## 3. Draft

- *Source*: open the address and copy the passage as the template's "Source" gives it; missing
  there, it is a question in step 4. For a page without editions, find the archived copy through
  the archive's CDX index of captures, not its availability lookup, which misses captures that
  exist.

## 4. Check, ask, show, write

- Before step 4.1, check mechanically: the address opens and the passage stands there word for
  word. A failure sends the draft back to step 3.
- Step 4.2: for a changed entry, show the wording on `{fork-point}` beside the new one, with the
  invariants and decisions that name it.
- Step 4.4: what follows is each invariant this fact serves, or whose *Rests on* names it, through
  `record-invariant`; and each decision naming it, through `record-decision`, each checked against
  the new sentence. A fact left with nothing naming it goes as WAY-73 and the template's "Withdrawn
  identifiers" say.
- After step 4.4 nothing is handed to another agent: no check is written for a fact.

## Projected mode

Projected mode runs as `elements/common/way_of_working.md` gives it, with these differences for a
fact (WAY-117):

- Step 2: a fact is projected only where a projected decision's *Based on* or a projected
  invariant's *Rests on* names it (WAY-73, WAY-90).
- Step 3: the entry is written whole; its source exists today and is read now.
- Step 4: the mechanical check before step 4.1 runs as above.
- Step 4.3: the heading reads `#### <identifier>`.

## A withdrawal

- A fact shown false, or left with nothing naming it, follows the template's "Withdrawn
  identifiers"; each dependant goes through `record-invariant` or `record-decision` in the same
  change.
