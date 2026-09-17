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
- An entry is corrected in place and carries no version; its history stays in git (WAY-43).
- One derived file lies beside the map: the list of known violations (WAY-51).

## Identifiers

- Every entry carries a permanent identifier of one or more words in lower case joined by
  hyphens (`relation-model`), unique across the three kinds.
- It does not change when the entry's title, its files or its fields change.
- Splitting or merging gives every result a new identifier; the one left behind goes to the list
  of withdrawn identifiers, names its successors and is never reused (WAY-41).

## Part

```markdown
## <identifier> — <title>

<one sentence: what this part is responsible for>

- **Files:** <git path patterns, one per line; `(generated)` after a pattern whose files this
  part's code writes>
- **Depends on:** <identifier> · <identifier> (separated — <why a failure of that part does not
  damage this one>) | none
- **Failure modes:**
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
- **Invariant:** <invariant that has to stay true along the flow> — test: <path of the
  end-to-end test that names this flow>
- **Coverage:** <path of the coverage file that test leaves> | none
```

`Coverage: none` makes the checker report the flow's list of parts as unchecked, never as
agreeing with the map (WAY-47).

## Surface

```markdown
## <identifier> — <title>

<one sentence: what the product promises to keep>

- **Declared at:** <file and symbol, or schema element, carrying the declaration and its promise
  level> | not markable — test: <path of the test that guards it>
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

| Field | Who reads it, when |
|---|---|
| identifier | a decision's *Scope*, an invariant, a flow's list of parts, a generated rule file |
| responsibility / description / promise | the agent working in the part; the content fingerprint |
| Files | the script that assigns a change to parts, computes coverage of the repository and generates rule files |
| Depends on | the script comparing the map with the dependency graph; the generator of rule files |
| Depends on — separated | the script computing criticality, which stops inheriting there |
| Failure modes | the computation of criticality; the choice of which checks a task runs |
| Failure modes — detected by | whoever asks which failures the gate would catch |
| Trust boundary | the choice of how sharply a change is checked (WAY-13) |
| Criticality (flow) | the criticality of every part the flow runs through |
| Parts (flow) | the test that a change lies on this flow; the coverage check |
| Invariant (flow) | the gate, which runs that test on every change |
| Coverage (flow) | the check of the flow's list of parts |
| Declared at | whoever changes the element; the tool computing shape and breaking change |
| criticality scale | the checker, which rejects a degree not on the list |
| external context | the checks at a trust boundary; the change path of a surface |
| change paths | whoever changes a surface at that level |
| files left out on purpose | the checker, as the only exception to file assignment |
| withdrawn identifiers | a reference to an identifier that no longer names a part |

## What binds

The binding part of an entry is one sentence: a part's responsibility, a flow's description, a
surface's promise. Its content fingerprint covers that sentence alone (WAY-42, WAY-39). Path
patterns, dependencies, failure modes and a flow's list of parts stay outside it; a change to a
part's patterns is shown instead as the list of files that changed part.

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
- Tests belong to the part they test. Generated files belong to the part of their generator and
  carry `(generated)`.
- The files that serve the whole repository — the lockfile, the build and the CI configuration —
  are a part of their own, and a change to them lies on every critical flow.
- For a file that collects entries about many parts, the parts a change touches come from the
  *Scope* of the entries it adds or changes, not from the file's own part.
- A file no pattern matches, and a file two parts claim, breaks the gate unless it stands on the
  list of files left out on purpose (WAY-44).

## Known violations

The derived file beside the map, `foundations/known_violations.md`, holds what the code does not
meet today. A position names the source part, the target part, the file and what it reaches for
— never a line number. A new violation breaks the gate; a position the code no longer
contradicts breaks it too and goes in the same change; a position is added only by a change of
the foundation that a human accepts. The file is checked as a subset of the list on the main
branch, never regenerated from scratch (WAY-51).

```markdown
## Known violations

| Source | Target | File | What it reaches for |
```

## What is generated from the map

Rules pinned to path patterns, in the channels the tools read: a part's responsibility, its
allowed dependencies, and the binding sentences of the decisions whose scope names it. The
patterns come from the part's *Files*. No overview of the repository is generated for an agent
(WAY-52).

## What the checker checks

- Every entry is a part, a critical flow or a surface, and every identifier is unique.
- Every identifier referred to from the foundation, a test or a generated rule file exists in
  the map, as an entry or as a withdrawn identifier; no entry uses a withdrawn one.
- Every file git tracks matches exactly one part's patterns, or stands on the list of files left
  out on purpose; no pattern matches nothing.
- Every part named by a flow, and every part named in a decision's scope, exists.
- Every flow has an invariant with a test that names it, and the gate runs every such test.
- Where a flow leaves a coverage file, every part that coverage names stands in its list;
  where it leaves none, the list is reported unchecked.
- Every degree used stands on the criticality scale; no criticality is written at a part.
- Every failure mode names a severity and either a detecting invariant or "not detected".
- Every dependency running from a higher criticality to a lower one, with no separation
  recorded, is reported.
- Every trust boundary pattern matches at least one file.
- Every surface names a declaration that exists, or a test that guards it; no promise level and
  no withdrawal date is written in the map; every level used by a declaration has a change path.
- Every exchange with the external context records its direction, its trust and whether its
  consumer updates with the product.
- The list of known violations is a subset of the list on the main branch, and holds no position
  the code no longer contradicts.

## Examples

Examples live in `examples.md`: entries copied word for word from a real map. The first ones come
from this repository's own map, so until that map exists only the forms above stand (WAY-05).
