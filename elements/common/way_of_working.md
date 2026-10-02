# The way of working the skills share

This file holds, once, the steps every element's skill takes to write an entry (WAY-35). Each rule
of an entry stands in its element's template or in `rules.md` beside this file; a skill holds only
the way of working particular to its element, and adds it to the steps below at the places it
names (WAY-35). A fix to a rule goes to the template or to `rules.md`, with the decision that sets
it; in the decisions element, a rule changes only with a decision in the log (WAY-35, WAY-05).

Paths under `elements/` below are those of the-way at the commit the product pins, which the
skill reaches by resolving its own directory (WAY-34).

## 1. Read

- Read in full the element's `template.md`, `elements/common/rules.md` and this file.
- Read the element's examples: its `examples.md` where it has one. Where `examples.md` names
  entries by identifier or number, read each of them in the-way's `foundations/`, at the commit the
  product pins; where it holds entries itself, read them there. An element with no `examples.md`
  names in its template the entries of the-way that serve as its examples, and those are read
  (WAY-09, WAY-34).
- Read the product's file of the element's entries in full, and the other files of `foundations/`
  the skill names.
- Before drafting, read in full the product's `foundations/glossary.md` where it exists and, in a
  product other than the-way, the-way's `foundations/glossary.md` at the commit the product pins,
  so that the draft uses each term in its meaning (WAY-95, WAY-97).
- Where the product has no file of the element's entries, ask whether it starts that file here; if
  not, stop
  (`TODO — decision pending: which decision sets that a product starts an element's file only on
  the human's word`). If so, the same change gives the new file to a part of the map through
  `update-part-map` (WAY-44). Where the missing file is the part map itself, the current
  `update-part-map` invocation writes the first map directly, using its "The first map of a
  product" section. Where another element's file is missing and the product has no part map,
  `update-part-map` writes the map first (WAY-28, for a product the process enters;
  `TODO — decision pending: which decision sets that the part map is written before another
  element's first file`).

## 2. Search the foundation

Once the skill has settled what the entry is, search the whole foundation for entries it touches
that no written link joins to it — not only those a link, a shared *Scope* or a shared *Part*
leads to (WAY-33). Read each entry whole: a decision's *Rejected* holds an option already weighed
and refused, and nowhere else says so
(`TODO — decision pending: which decision sets that the search reads a decision's *Rejected*`).
The search also asks:

- whether the entry uses a glossary term in another meaning than its entry gives, or spells out a
  term's definition instead of using the term: a paraphrase is rewritten to the term, and another
  meaning, or a word the glossary does not yet settle, goes through `record-glossary-term`
  (WAY-33, WAY-97, WAY-99);
- whether the change brings what entries of the foundation wait for — an element's template, the
  part map, a script; each such entry is fixed in the same change (WAY-37).

Each finding becomes a link the element's template gives, a change to one of the entries, or a
question in step 4, before the entry is accepted (WAY-33). The skill names what else the search
looks for in its element.

## 3. Draft

- Fill every field as the element's template and `rules.md` give it.
- Take every value from its source — the conversation, a document the human names, the product's
  files, the output of a command run for it — never from memory. A value the source does not give
  is a question in step 4 that proposes where to look for it, never the value itself, and the draft
  takes it only as read there (WAY-80 for the source of a fact and of a citation;
  `TODO — decision pending: which decision sets that any other value the source does not give is
  asked for, never taken from memory`).
- A field its source is silent on is a question in step 4, never a `none` the agent writes
  (`TODO — decision pending: which decision sets that a field its source is silent on is asked
  about before anything is written in it`); what stays open after step 4 is written as `rules.md`
  gives it (WAY-71).
- A value that a closed list of the template does not hold is a question in step 4, never the
  nearest value on the list with a reason why it will do (WAY-54); the list grows as the template
  says.

## 4. Ask, show, write

1. Ask in one round about everything still open, each question with a proposed answer and the
   reason for it
   (`TODO — decision pending: which decision sets that the questions of one entry are asked in one
   round, each with a proposed answer`).
2. Show the whole entry, with what the skill adds beside it. Apply the fixes, and write nothing
   before the human accepts the entry
   (`TODO — decision pending: which decision sets that an entry is shown whole and accepted before
   it is written`).
3. Write the entry in its place in the file and run the element's format guard (WAY-09) from the
   product's repository root, `python -B <the element's directory>/format_guard.py`, with the
   arguments its `--help` gives for this file and for the commit the task branch left the main
   branch from, or for no main branch
   (`TODO — decision pending: which decision sets that the skill runs the format guard on the file
   it writes`). Fix what the entry broke and run it again; an error or a warning elsewhere in the
   file goes to the human. Of the report's `unchecked:` lines, those that a `none` given to an
   option leaves — the text after the dash begins with that option and `none` — go to the human
   once per run of the guard, as their number, and every other `unchecked:` line goes to the human
   on its own
   (`TODO — decision pending: which decision sets how the unchecked lines of a guard's report reach
   the human`).
4. What follows from the entry goes through these steps one at a time, each through the skill of
   its element
   (`TODO — decision pending: which decision sets that the entries following from one entry are
   written one at a time`): every entry that names this one with its fingerprint, when its binding
   part changes (WAY-31, WAY-90); every link the entry names that the foundation does not
   hold yet (WAY-17); and each finding of step 2. The skill names what follows in its element.
