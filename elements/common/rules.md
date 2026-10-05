# Rules of form the elements share

This file holds, once, the rules of form that the entries of more than one element keep (WAY-09,
WAY-35). Each rule names the entries it binds and cites the decision that sets it. What belongs to
one element alone — its fields, which word each field takes, how its entries are named — stands in
that element's template (WAY-35).

## Language

- An entry of every element is written in English, whatever language the product shows the people
  who use it and whatever language its team speaks (WAY-72).

## Every field, and the words `none` and `TODO`

- Every field an element's template gives an entry of its kind appears in every entry of that kind
  — in every version of a decision and every review record, the fields their forms give (WAY-71).
- A field holds a value, or `none` or `TODO` only where its element's template gives it that word:
  `none` states that nothing is there, `TODO` that something is known to be missing. `none` is a
  statement, not a blank: where a source is silent, the field reads `TODO` (WAY-71).
- The main branch holds `TODO` only in an invariant's or an environment fact's *Method*, and in an
  invariant's *Rests on* until the environment facts element has entries (WAY-71).
- A format guard reports a missing field, or a word its template does not give that field, as an
  error (WAY-71).

## Terms of the glossary

- Any sentence of an entry of any element, its rationale included, that speaks of what a glossary
  term defines uses the term, never a paraphrase of its definition, so that the list of the term's
  uses finds it (WAY-97).
- A term whose definition holds a word an invariant's sentence may not hold (WAY-60) enters such a
  sentence only where the request names it for the human who accepts the change at the merge (WAY-97).

## Where the value of a field comes from

Each template marks, for every field, where its value comes from, with one of three marks:

- *read off* — the value is read off, as a version the guard computes; a template asks for what a
  value follows from rather than for the name of a value (WAY-54);
- *transcribed* — a human copies the value unchanged from a record outside the product (WAY-54);
- *judgment* — the value is neither read off nor transcribed: it holds someone's call, and no
  question with a factual answer settles it. A reader takes such a value as a call, not as a
  reading (WAY-54).

A field whose parts come from different places carries a mark for each part: *judgment* for the
entry a link names, *read off* for its fingerprint (WAY-54).

## Identifiers

- Every entry of `foundations/invariants.md`, of the part map and of
  `foundations/environment_facts.md` carries an identifier of one or more words in lower case joined
  by hyphens, such as `relation-model` (WAY-41, WAY-64).
- The three files share one space of identifiers: no identifier is held by two entries or withdrawn
  identifiers of the three taken together, so that a reference resolves without naming its element;
  `none` is no identifier, since *Successors* uses that word (WAY-64).
- An identifier stays the same when anything else about its entry changes — its files, its fields,
  its wording or its version. Splitting or merging entries gives each entry that comes out of it a
  new identifier (WAY-41, WAY-64).

## Withdrawn identifiers

- An identifier the invariants file or the environment facts file held on the commit the task
  branch left the main branch from stays in it, as an entry or as a withdrawn identifier; one that
  never reached the main branch may go (WAY-64). An identifier of the part map left behind
  by a split or a merge stays in the map as a withdrawn identifier and is never reused (WAY-41).
- A withdrawn identifier stays withdrawn: it never names an entry again (WAY-41, WAY-64).
- Each of the three files carries its withdrawn identifiers in one list after its last entry, in
  this form (WAY-41, WAY-64):

  ```markdown
  ## Withdrawn identifiers

  | Identifier | Why | Successors |
  ```

- *Why* says why the identifier was withdrawn, and where entries were split or merged, it says so
  (WAY-41, WAY-64).
- *Successors* lists the identifiers that took its place, joined by ` · `, each an entry or a
  withdrawn identifier of the same file. In the invariants file and the environment facts file it
  may read `none` (WAY-64); in the part map it names one or more identifiers, never `none`:
  the map withdraws an identifier only on a split or a merge, which leaves entries in its place
  (WAY-41).
- The identifier and *Successors* are read off, and *Why* rests on a judgment (WAY-54).

## Human verdicts

- A human verdict on an invariant or an environment fact stands in a row of
  `foundations/human_verdicts.md`, one file for both elements (WAY-83), written by hand
  (`TODO — decision pending: which decision sets that the file of human verdicts is written by
  hand`):

  ```markdown
  | Entry | Version | Verdict | By | On | Commit | Until |
  ```

- The row names the entry, its version, the verdict — `pass` or `fail` — who gave it, when, and the
  commit assessed, and counts only for the entry's current version (WAY-83).
- An invariant's row reads `none` in *Until*, and its verdict lapses when a change since the
  assessed commit reaches the entry. A fact's row carries a date in *Until*, after which its verdict
  lapses; the gate compares that date with the committer date of the commit it checks, and the
  clock with the day it runs (WAY-83).
- The part of the map that holds the file is set with the first verdict written
  (`TODO — decision pending: which decision sets that the part holding the file of human verdicts
  is set with the first verdict`).
- The verdict and *Until* of a row rest on a judgment; the rest of the row is read off (WAY-54).

## `{fork-point}`

- `{fork-point}` is the commit the task branch left the main branch from — the last commit of the
  main branch the branch contains — a value the gate fills in; where that commit does not exist, the
  gate fills in `none` in its place (WAY-61).

## Version

- An entry of the invariants or of the environment facts carries a version, starting at 1, in its
  heading as `## <identifier>/<version>`, and holds only its current wording; earlier wordings are
  read from git (WAY-57, WAY-79).
- When the entry's fingerprint differs from its fingerprint on the commit the task branch left the
  main branch from, its version is one higher than there; when it does not differ, the entry keeps
  the version it has there (WAY-57, WAY-79). An invariant that declares a correction is the one
  exception, and the invariants template gives its form (WAY-57).
- The guard compares an entry with its state on the commit the task branch left the main branch
  from; where there is no main branch, it compares nothing and every entry stays at version 1
  (WAY-57, WAY-79), and it says so
  (`TODO — decision pending: which decision sets that the guard says when there is no main branch
  to compare with`).
- A check cites such an entry by identifier and version, as `<identifier>/<version>`, and a check
  citing a version other than the current one fails the gate (WAY-57, WAY-79).
