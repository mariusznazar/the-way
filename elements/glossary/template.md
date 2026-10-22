# Glossary entry template

This file defines how a glossary entry is written. A glossary entry gives one meaning to a word
that means, in the product, something other than a reader who knows the product's field takes it to
mean, so that the word does not mean one thing in a decision and another in an invariant (WAY-95,
WAY-99). When the meaning of a term changes, the author of the change corrects the texts
that use the word (WAY-97).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, references and the absence of versions — stand in `elements/common/rules.md`; this
template holds what is particular to a glossary entry (WAY-35).

## Two glossaries

- The glossary of the-way holds the words of the process — what its templates, decisions and
  entries name. A product's glossary holds the words of its domain. In the-way, whose product is
  the process, the two are one file (WAY-226).
- A product takes the words of the process from the-way at the commit it pins, and its glossary
  defines none of them again (WAY-226).
- A word of the product's domain that the glossary of the-way holds, or the last word of a term
  it holds, in any of its forms, is written in the product's foundation with a qualifier — "castle
  gate" for "gate", or "assembly step" for "step", the last word of "return step". The bare word
  there keeps the meaning of the process. The qualified word takes an entry only as "Which words
  take an entry" says. The product's code, its interface and talk about the product use the word
  of the domain unchanged (WAY-104).

## Where entries go

- A product's glossary entries stand in one file, `foundations/glossary.md`, which opens with a
  title and a paragraph saying what it holds (WAY-93).
- An entry is headed by its term: the word or words as the foundation writes them in running text,
  which no other entry of the file holds (WAY-93).
- A sentence depends on a term by using its word (WAY-97). An entry carries no version and is
  edited in place, its meaning included (WAY-07, WAY-97).
- The language of an entry follows `elements/common/rules.md` (WAY-72). How a word the product
  shows the people who use it in another language stands in an entry is
  `TODO — decision pending: how does a word the product shows in another language stand in a
  glossary entry? (WAY-72)`.

## Which words take an entry

- A word takes an entry when it means, in the product, something other than a reader who knows the
  product's field takes it to mean. A word whose every meaning is one such a reader gives takes
  none, however many meanings it has — "run", for a command and for text running across lines
  (WAY-95).
- The agent that meets such a word in its work — writing an entry, searching the foundation, in a
  task's return step — writes its entry; no search of every binding sentence looks for candidates
  (WAY-95, WAY-11). The human accepting the change at the merge accepts the meaning of each entry
  (WAY-114).
- Two uses carry two meanings when a definition true of one is false of the other
  (`TODO — decision pending: which decision sets when two uses of a word carry two meanings`).
- Where a word carries two meanings in the files git tracks, and one of them is a meaning a reader
  who knows the product's field would not give it, one of the two is renamed, the human choosing
  the new word, and the uses of the meaning that moves are rewritten to that word; a note beside
  the word, or a paraphrase, is no renaming (WAY-99). In a product, none of this applies to a word
  of its domain that the glossary of the-way holds: the word is written as "Two glossaries" says
  (WAY-104).

## Form of an entry

```markdown
## <term>

<one sentence: the definition>

- **Not:** <meaning> — <what carries it, or TODO> · … | none
```

- The definition is one sentence; it is the entry's binding part (WAY-94, WAY-96).
- *Not* names each meaning the word carried in the files git tracks, besides its
  definition and a meaning a reader who knows the product's field gives it, with what carries it
  now: the term of another entry, an identifier in backticks, a value of a template's closed list
  in backticks, or a word between quotation marks, never one holding the term or its forms
  (WAY-94, WAY-99). Where the human has not yet chosen the word for the other meaning, *Not* reads
  `TODO` in place of what carries it; a task branch may hold it, the main branch never does
  (WAY-99, WAY-71).

## A changed meaning

- The author of a change to a term's definition searches, in the same change, every file git tracks
  for the word in each of its forms, and rewrites each use whose meaning the new definition moves,
  so that every use left carries the new meaning (WAY-97).

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`).

| Field | Who reads it, when |
|---|---|
| term (heading) | whoever writes a sentence using the word; `elements/common/foundation_check.py`, which finds a term held twice |
| definition | whoever reads or writes a sentence using the term; the author of a change to the term's meaning |
| Not | whoever meets the word in a meaning it no longer carries, and the agent renaming a meaning |

## Examples

`examples.md` names, by term, the entries of this repository's own glossary
(`foundations/glossary.md`) that show the form of an entry; they are read there, in the commit of
the-way a product pins, instead of being copied (WAY-09, WAY-34).
