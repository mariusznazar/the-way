---
name: update-part-map
description: Use when a product's part map, foundations/part_map.md, has to gain or change an entry — a part whose responsibility or files change, a part split or merged, a new critical flow or a new surface, failure modes or a trust boundary recorded at a part, a file no part claims, or the first map written for a product.
---

# Update the part map

Turns a change in what a product is made of into entries of its part map. Every rule of an entry
lives in `template.md`; this skill holds only the way of working. A fix that concerns a
rule of the entry goes to the template, not here (WAY-35).

## 1. Read the rules and the map

This skill lives in `elements/part-map/skill/` of the-way repository. Installed globally, its
base directory is a link, so resolve it first: `realpath <base>` in Bash,
`(Get-Item <base>).Target` in PowerShell. Read in full `template.md` from the parent of the
resolved directory, `examples.md` where it exists, and the product's whole
`foundations/part_map.md` — its three kinds of entry refer to one another. When the repository
has no `foundations/part_map.md`, ask whether the product starts its map here; if not, stop.
Before drafting, read in full the product's `foundations/glossary.md` where it exists and, in a
product other than the-way, the-way's `foundations/glossary.md` in the pinned copy, three
directories above the resolved one (WAY-34, WAY-92, WAY-95).

## 2. Decide what the entry is

- Find what changed in the product and where it is said: the conversation, a document the human
  names, or the code itself.
- Name the kind: a part, a critical flow, a surface. A dependency and a known violation are not
  entries of their own — one is a field of the part it starts from, the other a row of the
  derived list beside the map.
- Search the map for an entry that already records the same part, flow or surface: found — an
  edit in place; not found — a new identifier.
- A part that splits or merges: each entry that comes out of it takes a new identifier, the one
  left behind becomes a withdrawn identifier naming its successors, and every reference to it is
  rewritten in the same change — the scope of a decision, a test that names it, a generated rule
  file.
- Search the whole foundation, not only the decisions whose scope names this part, for entries
  this one touches that no written link joins to it: a decision resting on a boundary this change
  moves, an invariant naming a flow, a sentence that waits for the map (WAY-33, WAY-37). An entry
  of the map carries no relation, so each finding becomes a change to an entry or a question in
  step 4.
  The search also asks whether the entry uses a glossary term in another meaning than its entry
  gives, or spells out a term's definition instead of using the term (WAY-33): a paraphrase is
  rewritten to the term, and another meaning, or a word the glossary does not yet settle, goes
  through `record-glossary-term`.

## 3. Draft

Fill every field according to the template, with extra care for these:

- The binding sentence — a part's responsibility, a flow's description, a surface's promise — is
  what every reference to the entry rests on. Write it about what the entry answers for, not
  about where its files sit today.
- Path patterns, the place of a surface's declaration and the files of a trust boundary come from
  the repository, never from memory. Propose a pattern together with the files it claims and the
  files it takes from another part.
- Dependencies are what the part may depend on, not what the code reaches for today. Where the
  two differ, the entry keeps the rule and the difference becomes a row of the list of known
  violations, which the human accepts in step 4.
- Failure modes come from the human: ask what fails, what damage it does, how severe it is and
  what detects it before release. A criticality dictated by hand is a question about failure
  modes.
- A degree of the scale, a level of promise or an exchange with the external context that the
  entry needs and the map's lists do not hold is a question in step 4, and the row goes into the
  same change.

## 4. Ask, show, write

1. Ask in one round about everything the source leaves open, each question with a proposed value
   and the reason for it.
2. Show the whole entry, with the files its patterns claim and the files they take from another
   part. Apply fixes, and write nothing into the map before the human accepts it.
3. Write the entry in its place in the map and run the format guard from the product's repository
   root: `python -B <parent of the resolved directory>/format_guard.py`. Fix what the entry broke
   and run it again; an error or warning elsewhere in the map goes to the human.
4. What follows from this entry goes through steps 3 and 4 one at a time: the references a
   changed binding sentence flags (WAY-02), the renames a withdrawn identifier leaves behind, and the
   entries of the foundation found in step 2. A decision that has to change goes through
   `record-decision`.

## The first map of a product

A product with no map gets its parts written one at a time, by the steps above, until the format guard
reports every file git tracks assigned to a part or left out on purpose. What the code holds
against the map at that moment goes onto the list of known violations once, and only then
(WAY-28, WAY-51).
