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

- Select and read foundation context by "Reading the foundation" in
  `elements/common/way_of_working.md`. Search the files where the word stands rather than recall
  its uses.

## 2. Decide what the entry is

- Find what asks for the entry: a word met in the work — writing an entry, the search of the
  foundation, a task's return step (WAY-11) — that means in the product something other than a
  reader who knows its field takes it to mean; a word used in two meanings; a definition to change;
  a `TODO` in *Not* whose word the human has chosen.
- Choose the glossary by the template's "Two glossaries". A product session does not edit its
  pinned copy of the-way; a word of the process it needs goes to the human as a change for the-way
  (WAY-34).
- List the word's uses before judging it: search every file git tracks for each form of the word,
  with line breaks read as spaces so that a multi-word term split across lines is found
  (`git grep -i -w`, or `rg -U -i -w` over the files `git ls-files` lists, with `\s+` between its
  words). Read every use; the uses, never a sense of the word, settle what follows.
- Put the word through the template's "Which words take an entry". A word that takes none: show
  the human why, with the uses, and stop once they agree.
- Search the glossary — the-way's too, in a product — for the same meaning: found under this word,
  a change to that entry; found under another term, a question in step 4; not found, a new entry.

## 3. Draft

- The definition: one sentence, from what the uses share, and where a sentence of the foundation
  already says what the word is, from that sentence; where two such sentences, or a sentence and
  the uses, disagree, that is a question in step 4.
- *Not*: each other meaning the uses show that the template's *Not* names — never the meaning a
  reader who knows the product's field gives the word — with what carries it now. The word for a
  meaning not yet carried is the human's choice: propose one in step 4.

## 4. Ask, show, write

- Step 4.1 asks about what the uses leave open: which of two meanings keeps the word and which word
  the other takes, and which of two terms holds a meaning found under both.
- Step 4.2: show the entry with its list of uses; for a changed definition, the old definition
  beside the new one, with the uses whose meaning moves.
- Step 4.4: what follows, in the same change, is every use whose meaning a changed definition
  moves, and every use of a meaning moved to another word, rewritten as the template's "A changed
  meaning" and "Which words take an entry" say. Each goes through the skill of the element its entry
  belongs to; a sentence of an element's template or of `elements/common/` is rewritten there, as a
  fix to a rule is. In a product, a use in the-way's files goes to the human as a change for the-way
  (WAY-34).

## Projected mode

Projected mode runs as `elements/common/way_of_working.md` gives it, with these differences for a
term (WAY-117):

- Step 2: the candidate words are those the binding sentences of the definition's projected
  entries use, weighed by the template's "Which words take an entry"; a projected term has no uses
  on the main branch.
- Step 4.3: the heading reads `#### <term>`.
- Step 4.4 rewrites to the term only the projected entries of the same definition.
