# Rules of form the elements share

This file holds, once, the rules of form that the entries of more than one element keep (WAY-09,
WAY-35). Each rule names the entries it binds. What belongs to one element alone — its fields,
which word each field takes, how its entries are named — stands in that element's template
(WAY-35).

## Language

- An entry of every element is written in English, whatever language the product shows the people
  who use it and whatever language its team speaks (WAY-72).

## Every field, and the words `none` and `TODO`

- Every field an element's template gives an entry of its kind appears in every entry of that kind
  (WAY-71).
- A field holds a value, or `none` or `TODO` only where its element's template gives it that word:
  `none` states that nothing is there, `TODO` that something is known to be missing. `none` is a
  statement, not a blank: where a source is silent, the field reads `TODO` (WAY-71).
- The main branch holds `TODO` only in an invariant's *Rests on* until the environment facts element
  has entries (WAY-71).
- `elements/common/foundation_check.py` reports a missing field, or a word its template does not
  give that field, as an error (WAY-71).

## Where the value of a field comes from

- A template asks for what the value of a field follows from rather than for the name of a value,
  so that the value is read off the product wherever a tool can read it (WAY-54).

## References

- Another entry, a test, a document or a comment in code refers to an entry of any element by the
  entry's identifier alone, with no fingerprint and no version beside it, and names an entry the
  foundation holds (WAY-02).

## Identifiers

- Every entry of `foundations/invariants.md`, of the part map and of
  `foundations/environment_facts.md` carries an identifier of one or more words in lower case joined
  by hyphens, such as `relation-model` (WAY-41, WAY-64).
- The three files share one space of identifiers: no identifier is held by two entries or withdrawn
  identifiers of the three taken together, so that a reference resolves without naming its element;
  `none` is no identifier, since *Successors* uses that word (WAY-64).
- An identifier stays the same when anything else about its entry changes — its files, its fields
  or its wording. Splitting or merging entries gives each entry that comes out of it a new
  identifier (WAY-41, WAY-64).

## Withdrawn identifiers

- An identifier the invariants file or the environment facts file held on the commit the task
  branch left the main branch from stays in it, as an entry or as a withdrawn identifier; one that
  never reached the main branch may go (WAY-64). An identifier of the part map left behind
  by a split or a merge, or of an entry removed with nothing in its place, stays in the map as a
  withdrawn identifier and is never reused (WAY-41).
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
  withdrawn identifier of the same file, or reads `none` where nothing took its place (WAY-41,
  WAY-64).

## Human verdicts

No human verdict is recorded for any entry. The earlier form below is read only by the format
guards, kept as a library of `product-guidelines/form_check.py` until the slimming plan's position
P17 removes both; it binds no entry: a row of `foundations/human_verdicts.md` in the form

  ```markdown
  | Entry | Version | Verdict | By | On | Commit | Until |
  ```

## `{fork-point}`

- `{fork-point}` is the commit the task branch left the main branch from — the last commit of the
  main branch the branch contains, which `git merge-base HEAD <main branch>` gives; a test or a
  review that reads it finds it so, and reads `none` where that commit does not exist (WAY-60).
- `{merge-onto}` is the tip of the main branch that a merge goes onto, which
  `git rev-parse <main branch>` gives; a test or a review that reads it finds it so, and reads
  `none` where the main branch does not exist (WAY-60).

## No version

- An entry of the decisions, of the invariants, of the environment facts, of the glossary or of the
  part map carries no version: it is edited in place and holds only its current wording, and its
  earlier wordings are read from git (WAY-07, WAY-43, WAY-57, WAY-79, WAY-97).
