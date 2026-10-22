# Part map template

This file defines how a product's part map is written. The map holds the parts of a product and
what joins them: which part may depend on which, where a part takes in what the product does not
control, and what the product promises to someone outside it (WAY-40). It holds rules and a
description of the state that the return step compares with the code; a detail that changes with
every change of the code lives in the code or in a test, never in the map (WAY-04, WAY-44).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, the form of an identifier, when it stays and when a split or a merge replaces it, its
one space with the invariants and the environment facts, the list of withdrawn identifiers and the
absence of versions — stand in `elements/common/rules.md`; this template holds what is particular
to the part map (WAY-35).

## Where entries go

- The whole map is one Markdown file, `foundations/part_map.md`, of the shape below (WAY-40).
- It holds two kinds of entry — a **part** and a **surface** (WAY-40) — and three lists that are
  not entries: the external context, the files left out on purpose and the withdrawn identifiers
  (`TODO — decision pending: which decision sets the lists the map holds besides its entries`).
- An allowed dependency and a trust boundary are fields of the part they belong to, never entries
  of their own (WAY-40, WAY-48). A critical flow has no entry (WAY-45).
- An entry is edited in place and carries no version; its history stays in git (WAY-43). A change
  of the code that changes what a part answers for, which files are its or what it may depend on,
  or what a surface promises, rewrites the entry in the same change (WAY-43).
- The forms below give `none` to the fields that take it, and `TODO` to no field
  (`elements/common/rules.md`, WAY-71).

## Identifiers

The rules on when an entry's identifier stays, when a split or a merge replaces it, and how the
one left behind is withdrawn and never reused stand in `elements/common/rules.md` (WAY-41).

## Form of an entry

### Part

```markdown
## <identifier>

<one sentence: what this part is responsible for>

- **Files:** <git path patterns, one per line, each a directory or one kind of file> | none
- **Depends on:** <identifier> · <identifier> | none
- **Trust boundary:** <git path patterns of the files that take in what the product does not
  control> | none
```

### Surface

```markdown
## <identifier>

<one sentence: what the product promises to keep>

- **Relied on by:** <who outside the product relies on it>
```

## Assigning files

- Every file git tracks belongs to exactly one part, through the patterns in its *Files* field,
  matched by git rather than by a script of this process (WAY-44).
- A pattern names a directory, or one kind of file by a single pattern — every invariant test,
  say — rather than files one by one, so that adding or moving a file inside a directory leaves the
  map as it is (WAY-44).
- A part whose tool does not exist yet holds no files (`Files: none`); every file git tracks
  still belongs to exactly one part
  (`TODO — decision pending: which decision lets a part hold no files`).
- Tests belong to the part they test. Generated files belong to the part of their generator
  (WAY-44).
- The files that serve the whole repository — the lockfile and the build configuration — are a
  part of their own (WAY-44).
- The files that only direct whoever carries out the repository's tasks — instructions for agents,
  skills, hooks and the configuration of agents' tools and of CI — are another part of their own
  (WAY-44).
- For a file that collects entries about many parts, the parts a change touches come from the
  field in which the entries it adds or changes name parts — a decision's *Scope*, an invariant's
  *Part*, where `every` names all — not from the file's own part (WAY-44, WAY-62).
- A file no pattern matches, and a file two parts claim, is an error of
  `elements/common/foundation_check.py`, unless it stands on the list of files left out on purpose
  (WAY-44). So is a pattern of *Files* or *Trust boundary* that matches no file git tracks
  (WAY-44).

## Allowed dependencies

*Depends on* names the parts this part may depend on, not those its code reaches for today: the map
holds the rule, and the code shows the state (WAY-04). The return step of a change compares the two
for the parts the change touches (WAY-11).

A dependency the code holds that *Depends on* does not allow goes to the human. Where the human
accepts it as it stands, it is written as an invariant — "the part `<part>` does not depend on
`<part>`" — that reads `Violated: yes`, its test standing as an expected failure until the code
meets it, as the invariants template's "Violated" gives it; *Depends on* is never rewritten to fit
what the code reaches for today (WAY-04, WAY-51). The map holds no list of such dependencies.

## Trust boundary

- A trust boundary is a pattern of the code files of a part that take in what the product does not
  control: data from the network, keys, the deployment, files that come from outside the product,
  such as one on the user's disk. A script that only checks the product's own files is no trust
  boundary (WAY-48).
- A change that touches the files of a trust boundary is checked for crafted input, and its review
  is aimed at that risk (WAY-48).

## Surfaces

- A surface is what someone outside the product relies on — an API, a file format, a command — and
  its entry states the promise in one sentence and names in *Relied on by* who relies on it
  (WAY-49).
- A change that alters a surface names the surface in its request (WAY-49).

## Critical flows

A critical flow has no entry in the map. What has to stay true along it is an invariant whose
*Part* names the parts the flow runs through, and its test is a test of the product's suite like
any other, run with the rest of the suite (WAY-45).

## Exchanges with the external context

```markdown
## External context

| Partner | Direction | What comes in |
|---|---|---|
| <who or what> | them → us · us → them · both | trusted · untrusted · — |
```

A row names no part and no file
(`TODO — decision pending: which decision sets what a row of the external context names`). It is
read by whoever records a trust boundary at the part that handles the exchange (WAY-48).

## Files left out on purpose

```markdown
## Files left out on purpose

| File | Why |
```

The list is the only exception to "every tracked file has a part" (WAY-44).

## Withdrawn identifiers

After the last entry the map carries its withdrawn identifiers, in the form, with the *Why* and the
*Successors*, that `elements/common/rules.md` gives (WAY-41).

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`).

| Field | Who reads it, when |
|---|---|
| identifier (heading) | `elements/common/foundation_check.py`, which finds every *Scope*, *Part* and *Depends on* naming it; whoever follows such a reference |
| sentence | the agent making a change to the part's files or to what the surface promises; the search of the foundation, when the sentence changes |
| Files | the agent naming the parts its work touches; `foundation_check.py`, which finds each tracked file in one part |
| Depends on | the agent making a change, which keeps the code within it; the return step, which compares it with the code; `foundation_check.py` |
| Trust boundary | the agent making a change that touches its files, and the agent reviewing it, who check crafted input |
| Relied on by | the agent making a change to the surface, and the human merging its request, who see whom the change reaches |
| external context | whoever records a trust boundary at the part that handles an exchange (WAY-48) |
| files left out on purpose | `foundation_check.py`, as the only exception to file assignment |
| withdrawn identifiers | whoever follows an identifier that no longer names an entry; `foundation_check.py`, which keeps a withdrawn identifier from naming an entry again |

## The binding part

The binding part of an entry is one sentence: a part's responsibility or a surface's promise.
*Files*, *Depends on*, *Trust boundary* and *Relied on by* stay outside it (WAY-42).

## Examples

`examples.md` names, by identifier, the entries of this repository's own map
(`foundations/part_map.md`) that show the form of an entry; they are read there, in the commit of
the-way a product pins, instead of being copied (WAY-09, WAY-34).

## The earlier form, read by the format guard

The sections below hold the earlier form of the map, which `format_guard.py` beside this file reads:
failure modes and the separation of a dependency, a critical flow as an entry with its criticality
and its coverage, a surface's declaration at the item, the criticality scale, the column of the
external context on whether a partner updates with the product, the change paths of the promise
levels and the derived list of known violations. The guard is kept only as a library of
`product-guidelines/form_check.py` until the slimming plan's position P17 removes both; these
sections bind no entry and go with it.

## Part

Earlier form, read only by the format guard.

```markdown
## <identifier>

<one sentence: what this part is responsible for>

- **Files:** <git path patterns, one per line> | none
- **Depends on:** <identifier> · <identifier> (separated — <why a failure of that part does not
  damage this one>) | none
- **Failure modes:** none | one line for each:
  - <what fails> — <kind of damage> — <severity> — detected by <invariant> | not detected
- **Trust boundary:** <git path patterns of the files that take in untrusted data> | none
```

## Critical flow

Earlier form, read only by the format guard.

```markdown
## <identifier>

<one sentence: what this flow does, end to end>

- **Criticality:** <a degree from the criticality scale>
- **Parts:** <identifier> · <identifier> · …
- **Invariant:** <identifier of the invariant that has to stay true along the flow>
- **Coverage:** <path of the coverage file the flow's test leaves> | none
```

## Surface

Earlier form, read only by the format guard.

```markdown
## <identifier>

<one sentence: what the product promises to keep>

- **Declared at:** <file and item, in the code or the schema, carrying the declaration and its promise
  level> | not markable — test: <path of the test that protects it>
```

## Criticality scale

Earlier form, read only by the format guard.

```markdown
## Criticality scale

1. <degree> — <what a failure at this degree costs>
2. …
```

## External context

Earlier form, read only by the format guard.

```markdown
## External context

| Partner | Direction | What comes in | Updates with the product |
|---|---|---|---|
| <who or what> | them → us · us → them · both | trusted · untrusted · — | yes · no |
```

## Change paths

Earlier form, read only by the format guard.

```markdown
## Change paths

| Promise level | What a change at this level may do | What it owes the consumer first |
```

## Known violations

Earlier form, read only by the format guard. The derived file beside the map,
`foundations/known_violations.md`:

```markdown
## Known violations

| Source | Target | File | What it reaches for |
```
