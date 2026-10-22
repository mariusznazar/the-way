---
name: update-part-map
description: Use when a product's part map, foundations/part_map.md, has to gain or change an entry — a part whose responsibility, files, allowed dependencies or trust boundary change, a part split or merged, a new surface or a changed one, a file no part claims, the first map written for a product, or a change a project definition projects.
---

# Update the part map

Turns a change in what a product is made of into entries of its part map. Every rule of an entry
stands in this element's `template.md` and in `elements/common/rules.md`, and the way of working
the skills share stands in `elements/common/way_of_working.md`; this skill holds only what is
particular to the part map (WAY-35).

This skill lives in `elements/part-map/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/part-map/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what the part map adds to each.

## 1. Read

- Follow "Reading the foundation" in `elements/common/way_of_working.md`, including the complete
  product part map, whose parts name one another in *Depends on*.

## 2. Decide what the entry is

- Find what changed in the product and where it is said: the conversation, a document the human
  names, or the code itself.
- Name the kind of entry from those the template's "Where entries go" lists; what it lists as no
  entry of its own is written where that section says.
- Search the map for an entry that already records the same part or surface: found — a change to
  it; not found — a new identifier.
- A part that splits or merges takes identifiers as the template's "Identifiers" says, and every
  reference to the identifier left behind is rewritten in the same change — the *Scope* of a
  decision, the *Part* of an invariant, the *Depends on* of another part.
- The search of the foundation also looks for a decision resting on a boundary this change moves,
  an invariant naming the part, and a sentence that waits for the map. An entry of the map carries
  no link to another entry, so each finding becomes a change to an entry or a question in step 4.

## 3. Draft

- The binding sentence — a part's responsibility, a surface's promise — is what every reference to
  the entry rests on. Write it about what the entry answers for, not about where its files sit
  today.
- Path patterns and the files of a trust boundary come from the repository. Write a pattern for a
  directory or for one kind of file, as the template's "Assigning files" says, and propose it
  together with the files it claims and the files it takes from another part.
- *Depends on*: write what the part may depend on, not what the code reaches for today, and never
  rewrite it to fit the code (WAY-225). Where the two differ, the difference goes to the human in
  step 4; a dependency the human accepts as it stands is written through `record-invariant` as an
  invariant that the one part does not depend on the other, marked violated, as the template's
  "Allowed dependencies" says.
- *Trust boundary*: only files that take in what the template's "Trust boundary" names — data from
  the network, keys, the deployment, files from outside the product.
- *Relied on by*: who relies on a surface comes from the sources of step 2; where none says it, it
  is a question in step 4.
- An exchange with the external context that the entry needs and the map's list does not hold is
  a question in step 4, and its row goes into the same change.

## 4. Ask, show, write

- Step 4.2: show the entry with the files its patterns claim and the files they take from another
  part.
- Step 4.4: what follows from this entry is every entry that names it, when its binding sentence
  changes, the renames an identifier left behind leaves, and the entries of the foundation found
  in step 2. A decision that has to change goes through `record-decision`.

## Projected mode

Projected mode runs as `elements/common/way_of_working.md` gives it, with these differences for
the part map (WAY-116):

- Step 2: project only an entry whose every field is known before the code: a change to an
  existing part — its sentence, *Depends on*, a *Trust boundary* over files it already holds. A new
  part or a new surface is an open question of the definition, `— resolved in: breakdown`,
  carrying what is known of it.
- Step 4.3: the heading reads `#### <identifier> (changed)` above the whole entry as it will read.
- "The first map of a product" below does not apply.

## The first map of a product

A product with no map gets its parts written one at a time, by the steps above. After the human
accepts the first part, the current invocation writes it in the new map without invoking
`update-part-map` again to create that map. Continue until `elements/common/foundation_check.py`
reports no file git tracks that no part claims and that the map does not leave out on purpose
(WAY-28).
