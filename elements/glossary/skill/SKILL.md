---
name: record-glossary-term
description: Use when a product's glossary, foundations/glossary.md, has to gain or change an entry — a word that means in the product something other than a reader of its field takes it to mean, a word used in two meanings, a word a task's return step or a search of the foundation found, a changed meaning, a second meaning moved to another word, or a term a project definition projects.
---

# Record a glossary term

Turns a word the product uses in a meaning of its own into an entry of its glossary. Every rule of
an entry stands in this element's `template.md` and in `elements/common/rules.md`, and the way of
working the skills share stands in `elements/common/way_of_working.md`; this skill holds only what
is particular to a glossary entry (WAY-35).

This skill lives in `elements/glossary/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/glossary/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what a glossary entry adds to each.

## 1. Read

At step 1, read `read.md` beside this skill for the reading this entry needs.

## 2. Decide what the entry is

At step 2, read `decide_entry.md` beside this skill to decide what the entry is and what
the search of the foundation adds for this element.

## 3. Draft

- The definition: one sentence, from what the uses share, and where a sentence of the foundation
  already says what the word is, from that sentence; where two such sentences, or a sentence and
  the uses, disagree, that is a question in step 4.
- *Not*: each other meaning the uses show that the template's *Not* names — never the meaning a
  reader who knows the product's field gives the word — with what carries it now. The word for a
  meaning not yet carried is the human's choice: propose one in step 4.

## 4. Ask, show, write

At step 4, read `write.md` beside this skill for what to check, show and write, and what
follows from the entry.

## Projected mode

In projected mode, read `elements/common/projected_mode.md`, with these differences for a
term (WAY-117):

In projected mode, read `projected.md` beside this skill for choosing the words and
rewriting their uses.
- Step 4.3: the heading reads `#### <term>`.
