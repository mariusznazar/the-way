---
name: update-part-map
description: Use when a product's part map, foundations/part_map.md, has to gain or change an entry — a part whose responsibility or files change, a part split or merged, a new critical flow or a new surface, failure modes or a trust boundary recorded at a part, a file no part claims, or the first map written for a product.
---

# Update the part map

Turns a change in what a product is made of into entries of its part map. Every rule of an entry
stands in this element's `template.md` and in `elements/common/rules.md`, and the way of working
the skills share stands in `elements/common/way_of_working.md`; this skill holds only what is
particular to the part map (WAY-35).

This skill lives in `elements/part-map/skill/` of the-way. Installed globally, its base directory
is a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in
PowerShell. The element's directory is the parent of the resolved one, and the-way the directory
three above it. Follow the steps of `elements/common/way_of_working.md` there; below is what the
part map adds to each.

## 1. Read

- Read the product's whole `foundations/part_map.md` — its three kinds of entry refer to one
  another.

## 2. Decide what the entry is

- Find what changed in the product and where it is said: the conversation, a document the human
  names, or the code itself.
- Name the kind of entry from those the template's "Where entries go" lists; what it lists as no
  entry of its own is written where that section says.
- Search the map for an entry that already records the same part, flow or surface: found — a
  change to it; not found — a new identifier.
- A part that splits or merges takes identifiers as the template's "Identifiers" says, and every
  reference to the identifier left behind is rewritten in the same change — the scope of a
  decision, a test that names it, a generated rule file.
- The search of the foundation also looks for a decision resting on a boundary this change moves,
  an invariant naming a flow, and a sentence that waits for the map. An entry of the map carries no
  link to another entry, so each finding becomes a change to an entry or a question in step 4.

## 3. Draft

- The binding sentence — a part's responsibility, a flow's description, a surface's promise — is
  what every reference to the entry rests on. Write it about what the entry answers for, not
  about where its files sit today.
- Path patterns, the place of a surface's declaration and the files of a trust boundary come from
  the repository. Propose a pattern together with the files it claims and the files it takes from
  another part.
- *Depends on*: write what the part may depend on, not what the code reaches for today. Where the
  two differ, the difference becomes a row of the list of known violations, shown in step 4.
- Failure modes come from the human: ask what fails, what damage it does, how severe it is and
  what detects it before release. A criticality dictated by hand is a question about failure
  modes.
- A degree of the scale, a level of promise or an exchange with the external context that the
  entry needs and the map's lists do not hold is a question in step 4, and its row goes into the
  same change.

## 4. Ask, show, write

- Step 4.2: show the entry with the files its patterns claim and the files they take from another
  part.
- Step 4.4: what follows from this entry is the references a changed binding sentence flags
  (WAY-02), the renames an identifier left behind leaves, and the entries of the foundation found
  in step 2. A decision that has to change goes through `record-decision`.

## The first map of a product

A product with no map gets its parts written one at a time, by the steps above, until the format guard
reports every file git tracks assigned to a part or left out on purpose. What the code holds
against the map at that moment goes onto the list of known violations once, and only then
(WAY-28, WAY-51).
