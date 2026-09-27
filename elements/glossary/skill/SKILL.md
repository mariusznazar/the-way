---
name: record-glossary-term
description: Use when a product's glossary, foundations/glossary.md, has to gain or change an entry — a word a binding sentence or a template's rule uses in two meanings or in a meaning a reader of the field would not give it, a word a task's return step or a search of the foundation found, a sentence that defines a word, a reworded definition, a renamed term, a second meaning moved to another word, or a word added to Avoid.
---

# Record a glossary term

Turns a word the product's rules stand on into an entry of its glossary. Every rule of an entry
lives in `template.md`; this skill holds only the way of working. A correction that concerns a rule
of the entry goes to the template, not here (WAY-35).

## 1. Read the rules and the foundation

This skill lives in `elements/glossary/skill/` of the-way repository. Installed globally, its base
directory is a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in
PowerShell. Read in full `template.md` from the parent of the resolved directory, `examples.md` where
it exists, and the product's `foundations/glossary.md`; the other files of `foundations/` and the
elements' templates are where a term's uses and the carriers of *Not* stand, so search them rather
than recall them. In a product other than the-way, read also the-way's `foundations/glossary.md` in
the pinned copy, three directories above the resolved one (WAY-34, WAY-92). With no
`foundations/glossary.md` where the word belongs, ask whether the product starts its glossary here;
if not, stop; if so, the same change claims the new file for a part of the map through
`update-part-map`. With no part map, `update-part-map` writes it first.

## 2. Decide what the entry is

- Find what asks for the entry: a word a binding sentence or a template's rule uses in two meanings,
  or in one a reader who knows the product's field would not give it; a sentence that says what a
  word is; a word the return step of a task found (WAY-11); a finding of the search of WAY-33; a
  definition to reword; a term to rename; a word for *Avoid*; a `TODO` in *Not* whose word the human
  has chosen; a term the guard reports with no use.
- Entering a product that already exists, a candidate found in its documents or in its rule files
  for agents goes to the human as a question at once, and no list of candidates is kept (WAY-28).
- Choose the glossary: a word of the process goes to the-way's, a word of the product's domain to the
  product's (WAY-92). A product session does not edit its pinned copy of the-way; a word of the
  process it needs goes to the human as a change for the-way.
- List the word's uses before judging it, as the template's section on uses bounds them: the guard's
  list where the guard exists, otherwise a search of the same files for each form the endings give,
  with line breaks read as spaces so that a multi-word term split across lines is found
  (`rg -U -i -w` with `\s+` between its words), and the left-out text removed by hand. Read every
  use; the uses, never a sense of the word, settle what follows.
- Put the word through the template's section "Which words take an entry". A word that takes none:
  show the human why, with the uses, and stop once they agree.
- Search for the same meaning under another word, in the glossary — the-way's too, in a product — and
  in the whole foundation: a sentence whose use fits the meaning under another word, or a parallel
  sentence in another file saying the same with a different word. Found under this word — a change
  to that entry; found under a term, or as a word with no entry — one concept with two words, and the
  human chooses which is the term; not found — a new entry. Keep each other word with its uses for
  step 3.
- Compare the term with the identifiers of the part map, the invariants and the environment facts as
  the template reads them alike; a match this change brings is a question in step 4.
- Search the whole foundation for entries this term touches with no written link (WAY-33), asking
  directly for a sentence that says what the word is, a sentence that spells out the definition
  instead of using the term, and a use in another meaning. Each finding becomes a rewrite in step 4.6
  or a question in step 4.

## 3. Draft

Fill the entry according to the template, with extra care for these:

- The definition: take it from what the uses share, and where a sentence of the foundation already
  says what the word is, from that sentence; where two such sentences, or a sentence and the uses,
  disagree, that is a question in step 4. Read the entry of every term the definition uses as genus
  or difference, and use it in that meaning. Put each clause through the template's test for a rule;
  a clause that holds a rule stays in the entry that sets it, and a rule no entry sets yet is a
  question in step 4, never part of the definition.
- *Avoid* and *Not*: sort each other word found in step 2 and each other meaning by its uses, and
  keep the uses beside it to show in step 4. The word for a meaning not yet carried is the human's
  choice: propose one in step 4.

## 4. Ask, review, show, write

1. Ask in one round about everything the uses leave open — which of two meanings keeps the word and
   what the other takes, which of two words is the term, a match with an identifier, a word used both
   plainly and in place of a term, a clause that may be a rule — each with a proposed answer and the
   reason for it.
2. For a changed definition, hand the human an instruction for another agent to review the uses
   (WAY-97) — the term, its definition on `{fork-point}`, or, with no main branch, at the last commit
   that holds the entry, the new definition and the list of uses from step 2, never the
   conversation. That agent puts the new definition in place of the word in every use listed and in
   every other form it finds — a short form, an irregular form, a verb split by its object — and lists
   each use whose meaning moves, the sentence before and after. A moved use in an entry on the main
   branch means the new meaning takes a new word and an entry of its own; the draft goes back to
   step 3. An entry new on this branch has no uses to review.
3. Show the whole entry with its list of uses. For a changed entry, show the definition step 4.2
   started from beside the new one, with the moved uses. Write nothing before the human accepts it.
4. Write the entry in its place. Where the format guard exists, run it from the repository root,
   `python -B <parent of the resolved directory>/format_guard.py foundations/glossary.md --base <the
   commit the branch left the main branch from>`, leaving out `--base` with no main branch; fix what
   the entry broke and rerun, and give an error elsewhere in the file to the human.
5. A word put into *Avoid*: search the elements' skills, the README files and the code for it
   (WAY-98, WAY-37), and give each hit to the human as a change to that file.
6. What follows goes one at a time, wherever the foundation may still be edited: a sentence that said
   what the word is, or spelt out its definition, rewritten to use the term (WAY-95, WAY-100); every
   use of a meaning that moved to another word, rewritten to that word; a use a changed definition
   moved, rewritten or accepted by the human in step 4.3. Each goes through the skill of the element
   its entry belongs to; a sentence of an element's template is rewritten in that template, for the
   decision template together with a decision in the log (WAY-05).

## A renamed term, and a term with no use

- A renamed term follows the template's section "Where entries go"; its uses are rewritten through
  step 4.6.
- A term the guard reports with no use, on a task branch: ask whether its uses come later in this
  change; if not, the entry is taken out.
