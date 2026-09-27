# Part map template

This file defines how a product's part map is written. The map holds the parts of a product and
what joins them: which part may depend on which, which flows run across several parts, and what
crosses the edge to the world outside. It says what is allowed, not what the code happens to
contain today — what the code contains is computed from it and checked against the map (WAY-15).
Alongside the joins it records how badly each part can fail and where it takes in what it does
not trust.

## Where entries go

- The whole map is one Markdown file, `foundations/part_map.md`, of the shape below (WAY-40).
- It holds three kinds of entry — a **part**, a **critical flow** and a **surface** — and five
  lists that are not entries: the criticality scale, the external context, the change paths, the
  files left out on purpose and the withdrawn identifiers.
- An allowed dependency is a field of the part it starts from, never an entry of its own.
- An entry is edited in place and carries no version; its history stays in git (WAY-43).
- One derived file lies beside the map: the list of known violations (WAY-51).
- Every field the form of an entry's kind gives appears in that entry, and holds `none` only where
  the form gives it that word; no field of the map holds `TODO` (WAY-71).
- An entry is written in English, whatever language the product shows the people who use it and
  whatever language its team speaks (WAY-72).

## Identifiers

- Every entry carries a permanent identifier of one or more words in lower case joined by
  hyphens (`relation-model`), unique across the three kinds, the product's invariant entries and
  its environment fact entries (WAY-64).
- It does not change when the entry's title, its files or its fields change.
- Splitting or merging gives each entry that comes out of it a new identifier; the one left behind
  goes to the list of withdrawn identifiers, names its successors and is never reused (WAY-41).

## Part

```markdown
## <identifier> — <title>

<one sentence: what this part is responsible for>

- **Files:** <git path patterns, one per line; `(generated)` after a pattern whose files this
  part's code writes> | none
- **Depends on:** <identifier> · <identifier> (separated — <why a failure of that part does not
  damage this one>) | none
- **Failure modes:** none | one line for each:
  - <what fails> — <kind of damage> — <severity> — detected by <invariant> | not detected
- **Trust boundary:** <git path patterns of the files that take in untrusted data> | none
```

A part has no criticality field: its criticality is computed (WAY-46).

## Critical flow

```markdown
## <identifier> — <title>

<one sentence: what this flow does, end to end>

- **Criticality:** <a degree from the criticality scale>
- **Parts:** <identifier> · <identifier> · …
- **Invariant:** <identifier of the invariant that has to stay true along the flow> — test: <path
  of the end-to-end test that names this flow>
- **Coverage:** <path of the coverage file that test leaves> | none
```

`Coverage: none` makes the format guard report the flow's list of parts as unchecked, never as
agreeing with the map (WAY-47).

## Surface

```markdown
## <identifier> — <title>

<one sentence: what the product promises to keep>

- **Declared at:** <file and symbol, or schema definition, carrying the declaration and its promise
  level> | not markable — test: <path of the test that protects it>
```

The promise level lives at the declaration, and so does the withdrawal date while a surface is
being withdrawn. Neither is written in the map (WAY-49).

## Criticality scale

The degrees a product uses, lowest first. Every degree named by a failure mode or by a flow
stands on this list. How many degrees a product needs follows from how many distinct sets of
steps its task cycle has (WAY-46).

```markdown
## Criticality scale

1. <degree> — <what a failure at this degree costs>
2. …
```

## External context

```markdown
## External context

| Partner | Direction | What comes in | Updates with the product |
|---|---|---|---|
| <who or what> | them → us · us → them · both | trusted · untrusted · — | yes · no |
```

The direction and the trust choose the checks a change at the boundary runs (WAY-48); the last
column chooses the change path a surface at that edge may take (WAY-50).

## Change paths

```markdown
## Change paths

| Promise level | What a change at this level may do | What it owes the consumer first |
```

One row per promise level, never per surface (WAY-50).

## Files left out on purpose

```markdown
## Files left out on purpose

| File | Why |
```

A file here belongs to no part and counts as the highest criticality. The list is the only
exception to "every tracked file has a part" (WAY-44).

## Withdrawn identifiers

```markdown
## Withdrawn identifiers

| Identifier | Successors |
```

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier | a decision's *Scope*, an invariant, a flow's list of parts, a generated rule file | prose |
| responsibility / description / promise | the agent working in the part; the fingerprint | prose |
| Files | the script that assigns a change to parts, computes coverage of the repository and generates rule files | judgment |
| Depends on | the script comparing the map with the dependency graph; the generator of rule files | judgment |
| Depends on — separated | the script computing criticality, which stops inheriting there | judgment |
| Failure modes | the computation of criticality; the choice of which checks a task runs | judgment |
| Failure modes — detected by | whoever asks which failures the gate would catch | read off |
| Trust boundary | the choice of how sharply a change is checked (WAY-13) | judgment |
| Criticality (flow) | the criticality of every part the flow runs through | judgment |
| Parts (flow) | the test that a change lies on this flow; the coverage check | judgment |
| Invariant (flow) | the gate, which runs that test on every change | judgment |
| Coverage (flow) | the check of the flow's list of parts | read off |
| Declared at | whoever changes the item; the tool computing shape and breaking change | read off |
| criticality scale | the format guard, which rejects a degree not on the list | judgment |
| external context | the checks at a trust boundary; the change path of a surface | judgment |
| change paths | whoever changes a surface at that level | judgment |
| files left out on purpose | the format guard, as the only exception to file assignment | judgment |
| withdrawn identifiers | a reference to an identifier that no longer names a part | read off |
A field marked *judgment* holds someone's call: no tool reads its value off the product, and no question with a factual answer settles it. A reader takes such a value as a call, not as a reading (WAY-54). A field marked *prose* carries text rather than a value.

## The binding part

The binding part of an entry is one sentence: a part's responsibility, a flow's description, a
surface's promise. Its fingerprint covers that sentence alone (WAY-42, WAY-39). Path
patterns, dependencies, failure modes and a flow's list of parts stay outside it; a change to a
part's patterns is shown instead as the list of files that changed part. Any sentence of an entry
that speaks of what a glossary term defines uses the term, never a paraphrase of its definition (WAY-100).

## Criticality: what is written and what is computed

- A human writes the failure modes and the separations. A failure mode names what fails, the
  kind of damage it does, its severity, and how it is detected before release — a named
  invariant, or an explicit "not detected".
- The script computes a part's criticality: the highest of its own failure modes, of the flows
  it lies on, and of the parts that depend on it, stopping where a dependency records a
  separation.
- A part with no failure modes recorded counts as the highest degree.
- Raising a severity needs no reason. Lowering one, or adding a separation, carries its reason
  in the row that changes.
- The kind of damage chooses which checks a task runs; the degree chooses how sharply (WAY-46).

## Assigning files

- Every file git tracks belongs to exactly one part, through the patterns in its *Files* field,
  matched by git rather than by a script of this process.
- A part whose tool does not exist yet holds no files (`Files: none`); every file git tracks
  still belongs to exactly one part.
- Tests belong to the part they test. Generated files belong to the part of their generator and
  carry `(generated)`.
- The files that serve the whole repository — the lockfile, the build and the CI configuration —
  are a part of their own, and a change to them lies on every critical flow.
- For a file that collects entries about many parts, the parts a change touches come from the
  field in which the entries it adds or changes name parts — a decision's *Scope*, an invariant's
  *Part*, where `every` names all — not from the file's own part (WAY-44, WAY-62).
- A file no pattern matches, and a file two parts claim, breaks the gate unless it stands on the
  list of files left out on purpose (WAY-44).

## Known violations

The derived file beside the map, `foundations/known_violations.md`, holds the map's debt. A
row names the source part, the target part, the file and what it reaches for — never a line
number. A new violation breaks the gate; a row the code no longer contradicts breaks it too and
goes in the same change; a row is added only by a change of the foundation that a human accepts. The file is checked as a subset of the list on the commit
the task branch left the main branch from, never regenerated from scratch (WAY-51).

```markdown
## Known violations

| Source | Target | File | What it reaches for |
```

## What is generated from the map

Rules pinned to path patterns, in the channels the tools read: a part's responsibility, its
allowed dependencies, and the binding sentences of the decisions whose scope names it. The
patterns come from the part's *Files*. No overview of the repository is generated for an agent
(WAY-52).

## What the format guard checks

- Every section of the map is an entry — a part, a critical flow or a surface — or one of the five
  lists above; the list of known violations stands in its own file (WAY-40, WAY-51).
- The map stands in `foundations/part_map.md`, and no other file git tracks is named
  `part_map.md` (WAY-40).
- Every identifier is made of words in lower case joined by hyphens, is unique, and is no
  withdrawn one; no identifier ends in a version and no entry carries a *Version* field (WAY-41,
  WAY-43).
- Every entry carries every field of its kind's form; `none` stands only where that form gives it
  the word, and `TODO` in no field of an entry and in no cell of a list, on every run, since the
  form gives `TODO` to no field (WAY-71).
- Every part a flow lists or a part depends on, and every name in the scope of the latest version
  of a decision, is a part of the map; a withdrawn one is reported as withdrawn (WAY-21, WAY-45).
- Where `foundations/invariants.md` stands beside the map, every invariant a flow or a failure
  mode names is an entry of it (WAY-64).
- Every file git tracks matches exactly one part's patterns, or stands on the list of files left
  out on purpose; no file on that list, tracked or not, matches a part's patterns; every pattern
  of *Files* and of *Trust boundary* matches at least one file git tracks (WAY-44, WAY-48).
- Every flow names an invariant, and a test that exists and names the flow; in this repository's
  own map, that test lies under `gate/` (WAY-45, WAY-55).
- Where a flow leaves a coverage file, every part that coverage names stands in its list;
  where it leaves none, the list is reported unchecked (WAY-47).
- Every degree used stands on the criticality scale; no part carries a criticality field (WAY-46).
- Every failure mode names a severity, a degree of the criticality scale, and either a detecting
  invariant or "not detected" (WAY-46).
- Every dependency running from a higher criticality to a lower one, with no separation
  recorded, is reported.
- Every surface names a declaration — a file that exists and holds the symbol named — or reads
  `not markable` and names a test that exists; no promise level is written in the map, and no
  withdrawal date anywhere in it; no surface carries a change path of its own, and no row of the
  change paths names a surface (WAY-49, WAY-50). Whether every declaration carries a level, and
  every level used has a change path, is reported unchecked until the product reports its levels.
- Every exchange with the external context records its direction, its trust and whether its
  consumer updates with the product.
- Every row on the list of known violations names a source part and a target part of the
  map, a file and what it reaches for, and no line number; given the commit the task branch left
  the main branch from, the list is a subset of the list there. Whether the code holds every
  row and no other violation is reported unchecked until the product reports its dependency
  graph (WAY-51).
- Every example in `examples.md` matches its entry in this repository's own map word for word.
- Given the path of a record, the format guard writes the-way's own record of the run there, with a
  verdict for each invariant its checks cite (WAY-61, WAY-74); given `none` as the commit the task
  branch left the main branch from, it records the check that needs that commit as `unchecked`; a
  call to git that fails is a failure of the run, never an unchecked check (WAY-61, WAY-63).

## Examples

Examples live in `examples.md`: entries copied word for word from a real map. The first ones come
from this repository's own map, so until that map exists only the forms above stand (WAY-05).
