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

At step 1, read `read.md` beside this skill for the reading this entry needs.

## 2. Decide what the entry is

At step 2, read `decide_entry.md` beside this skill to decide what the entry is and what
the search of the foundation adds for this element.

## 3. Draft

At step 3, read `draft.md` beside this skill to obtain and check the source material.

## 4. Check, ask, show, write

At step 4, read `write.md` beside this skill for what to check, show and write, and what
follows from the entry.

## Projected mode

In projected mode, read `elements/common/projected_mode.md`, with these differences for a
fact (WAY-117):

- Step 2: a fact is projected only where a projected decision's *Based on* or a projected
  invariant's *Rests on* names it (WAY-73, WAY-90).
- In projected mode, read `projected.md` beside this skill for reading the source and
  checking the proposal.
- Step 4.3: the heading reads `#### <identifier>`.

## A withdrawal

- A fact shown false, or left with nothing naming it, follows the template's "Withdrawn
  identifiers"; each dependant goes through `record-invariant` or `record-decision` in the same
  change.
