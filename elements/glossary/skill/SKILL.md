---
name: record-glossary-term
description: Use when a product's glossary, foundations/glossary.md, has to gain or change an entry — a word a binding sentence or a template's rule uses in two meanings or in a meaning a reader of the field would not give it, a word a task's return step or a search of the foundation found, a sentence that defines a word, a reworded definition, a renamed term, a second meaning moved to another word, a word added to Avoid, or a term a project definition projects.
---

# Record a glossary term

Turns a word the product's rules stand on into an entry of its glossary. Every rule of an entry
stands in this element's `template.md` and in `elements/common/rules.md`, and the way of working
the skills share stands in `elements/common/way_of_working.md`; this skill holds only what is
particular to a glossary entry (WAY-35).

This skill lives in `elements/glossary/skill/` of the-way. Installed globally, its base directory
is a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in
PowerShell. The element's directory is the parent of the resolved one, and the-way the directory
three above it. Follow the steps of `elements/common/way_of_working.md` there; below is what a
glossary entry adds to each.

## 1. Read

- Read the product's `foundations/glossary.md`. The other files of `foundations/`, the elements'
  templates and the Markdown files of `elements/common/` are where a term's uses and the carriers
  of *Not* stand, so search them rather than recall them.

## 2. Decide what the entry is

- Find what asks for the entry: a word a binding sentence or a template's rule uses in two
  meanings, or in one a reader who knows the product's field would not give it; a sentence that
  says what a word is; a word the return step of a task found (WAY-11); a finding of the search of
  the foundation; a definition to reword; a term to rename; a word for *Avoid*; a `TODO` in *Not*
  whose word the human has chosen; a term the guard reports with no use.
- Entering a product that already exists, each candidate found in its documents or in its rule
  files for agents goes to the human at once, as the template's "Which words take an entry" says.
- Choose the glossary by the template's "Two glossaries". A product session does not edit its
  pinned copy of the-way; a word of the process it needs goes to the human as a change for the-way
  (WAY-34).
- List the word's uses before judging it, as the template's "Uses and a changed definition" bounds
  them: the guard's list, asked for as its `--help` gives, where the guard exists; otherwise a
  search of the same files for each form the endings give, with line breaks read as spaces so that
  a multi-word term split across lines is found (`rg -U -i -w` with `\s+` between its words), and
  the left-out text removed by hand. Read every use; the uses, never a sense of the word, settle
  what follows.
- Put the word through the template's "Which words take an entry". A word that takes none: show
  the human why, with the uses, and stop once they agree.
- Search for the same meaning under another word, in the glossary — the-way's too, in a product —
  and in the files where uses stand: a sentence whose use fits the meaning under another word, or
  a parallel sentence in another file saying the same with a different word. Found under this word
  — a change to that entry; found under a term, or as a word with no entry — one concept with two
  words, and the human chooses which is the term; not found — a new entry. Keep each other word
  with its uses for step 3.
- Compare the term with the identifiers of the part map, the invariants and the environment facts
  as the template reads them alike; a match this change brings is a question in step 4.
- The search of the foundation also asks directly for a sentence that says what the word is. Each
  finding becomes a rewrite in step 4.4 or a question in step 4.

## 3. Draft

- The definition: take it from what the uses share, and where a sentence of the foundation or of a
  template already says what the word is, from that sentence; where two such sentences, or a
  sentence and the uses, disagree, that is a question in step 4. Read the entry of every term the
  definition uses as genus or difference. Put each clause through the template's test for a rule;
  a clause that holds a rule leaves the definition, and a rule no entry sets yet is a question in
  step 4.
- *Avoid* and *Not*: sort each other word found in step 2 and each other meaning by its uses, and
  keep the uses beside it to show in step 4. The word for a meaning not yet carried is the human's
  choice: propose one in step 4.

## 4. Ask, review, show, write

- Step 4.1 asks about what the uses leave open: which of two meanings keeps the word and what the
  other takes, which of two words is the term, a match with an identifier, a word used both
  plainly and in place of a term, a clause that may be a rule.
- Before step 4.2, for a changed definition, hand the human an instruction for another agent to
  review the uses as the template's "Uses and a changed definition" sets it (WAY-97): the term, its
  definition on `{fork-point}` — or, with no main branch, at the last commit that holds the entry —
  the new definition and the list of uses from step 2, never the conversation. That agent also
  looks for every other form of the word — a short form, an irregular form, a verb split by its
  object — and lists each use whose meaning moves, the sentence before and after. A moved use in
  an entry on the main branch sends the draft back to step 3, as that section says. An entry new
  on this branch has no main-branch uses to preserve; review its uses in the current tree before
  changing its definition.
- Step 4.2: show the entry with its list of uses; for a changed entry, the definition the review
  started from beside the new one, with the moved uses.
- After step 4.3, for a word put into *Avoid*, make the search the template's "Avoid" asks for, and
  give each hit to the human as a change to that file.
- Step 4.4: what follows, wherever the text may still be edited, is a sentence that said what the
  word is, or spelt out its definition, rewritten to use the term (WAY-95, WAY-97); every use of a
  meaning that moved to another word, rewritten to that word; and a use a changed definition moved,
  rewritten or accepted by the human in step 4.2. Each goes through the skill of the element its
  entry belongs to; a sentence of an element's template or of `elements/common/` is rewritten
  there, as a fix to a rule is.

## Projected mode

Projected mode runs as `elements/common/way_of_working.md` gives it, with these differences for a
term (WAY-117):

- Step 2: the candidate words are those the binding sentences of the definition's projected
  entries use, weighed by the template's "Which words take an entry"; a projected term has no uses
  on the main branch.
- Step 4: no other agent reviews uses before step 4.2, and no search for a word put into *Avoid*
  runs in the product's files after step 4.3; step 4.4 rewrites to the term only the projected
  entries of the same definition.
- Step 4.3: the heading reads `#### <term>`.

## A renamed term, and a term with no use

- A renamed term follows the template's section "Where entries go"; its uses are rewritten through
  step 4.4.
- A term the guard reports with no use, on a task branch: ask whether its uses come later in this
  change; if not, the entry is taken out.
