# Part map template

This file defines how a product's part map is written. The map holds the parts of a product and
what joins them: which part may depend on which, which flows run across several parts, and what
crosses the edge to the world outside. It says what is allowed, not what the code happens to
contain today — what the code contains is computed from it and checked against the map (WAY-04).
Alongside the joins it records how badly each part can fail and where it takes in what it does
not trust.

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, the terms of the glossary, the marks of where a value comes from, the form of an
identifier, when it stays and when a split or a merge replaces it, its one space with the
invariants and the environment facts, and the list of withdrawn identifiers — stand in
`elements/common/rules.md`; this template holds what is particular to the part map (WAY-35).

## Where entries go

- The whole map is one Markdown file, `foundations/part_map.md`, of the shape below (WAY-40).
- It holds three kinds of entry — a **part**, a **critical flow** and a **surface** (WAY-40) —
  and five lists that are not entries: the criticality scale, the external context, the change
  paths, the files left out on purpose and the withdrawn identifiers
  (`TODO — decision pending: which decision sets the lists the map holds besides its entries`).
- An allowed dependency is a field of the part it starts from, never an entry of its own (WAY-40).
- An entry is edited in place and carries no version; its history stays in git (WAY-43).
- One derived file lies beside the map: the list of known violations (WAY-51).
- The forms below give `none` to the fields that take it, and `TODO` to no field
  (`elements/common/rules.md`, WAY-71).

## Identifiers

The rules on when an entry's identifier stays, when a split or a merge replaces it, and how the
one left behind is withdrawn and never reused stand in `elements/common/rules.md` (WAY-41).

## Part

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

A part has no criticality field: its criticality is computed (WAY-46). What the code holds against
*Depends on* comes from the product's dependency graph, through the list of known violations
(`known-violation-coverage`, `known-violation-currency`); where the product declares no command
that reports its graph, that is reported as not checked, never as agreement (WAY-38, WAY-51).

## Critical flow

```markdown
## <identifier>

<one sentence: what this flow does, end to end>

- **Criticality:** <a degree from the criticality scale>
- **Parts:** <identifier> · <identifier> · …
- **Invariant:** <identifier of the invariant that has to stay true along the flow>
- **Coverage:** <path of the coverage file the flow's test leaves> | none
```

The flow's end-to-end test names the flow (WAY-45), in a comment line of its own reading
`# flow: <identifier>`; the map does not name the test
(`TODO — decision pending: which decision sets how a test names its flow`).

`Coverage: none` makes the format guard report the flow's list of parts as unchecked, never as
agreeing with the map (WAY-47).

## Surface

```markdown
## <identifier>

<one sentence: what the product promises to keep>

- **Declared at:** <file and item, in the code or the schema, carrying the declaration and its promise
  level> | not markable — test: <path of the test that protects it>
```

The promise level lives at the declaration, and so does the withdrawal date while a surface is
being withdrawn. Neither is written in the map (WAY-49).

## Criticality scale

The degrees a product uses, lowest first. Every degree named by a failure mode or by a flow
stands on this list. How many degrees a product needs follows from how many distinct sets of
steps its task cycle has
(`TODO — decision pending: which decision sets the criticality scale and how many degrees it
holds`).

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

A row names no part and no file
(`TODO — decision pending: which decision sets what a row of the external context names`). It is
read by whoever records a trust boundary at the part that
handles the exchange (WAY-48), and by whoever sets the change path of a promise level, which has to
allow for a consumer that does not update together with the product (WAY-50).

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

A file here belongs to no part and counts as the highest criticality
(`TODO — decision pending: which decision sets the criticality of a file left out on purpose`).
The list is the only exception to "every tracked file has a part" (WAY-44).

## Withdrawn identifiers

After the last entry the map carries its withdrawn identifiers, in the form, with the *Why* and the
*Successors*, that `elements/common/rules.md` gives (WAY-41). The format guard checks *Why* and the
successors (`map-withdrawal-successors`) (WAY-41).

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`). Each field carries the mark of where its value comes from (`elements/common/rules.md`); a
reader not built yet is named by the invariant it answers to
(`TODO — decision pending: which decision names a reader not built yet by its invariant`).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier | the format guards, in a decision's *Scope* (`decision-scope-names`), an invariant's *Part* (`invariant-part-names`), a flow's *Parts* and a part's *Depends on* (`flow-part-names`); a generated rule file (`generated-pattern-source`) | judgment |
| responsibility / description / promise | whoever changes the part, the flow or the surface; a generated rule file (WAY-52); the fingerprint (`map-fingerprint-input`) | judgment |
| Files | the format guard (`file-part-assignment`, `path-pattern-reach`); the gate, finding the invariants a change reaches (`change-reach`); a generated rule file (`generated-pattern-source`) | judgment |
| Depends on | the format guard (`flow-part-names`); the computation of criticality (`map-guard-dependency-report`); the comparison with the dependency graph (`known-violation-coverage`) | judgment |
| Depends on — separated | the computation of criticality, which stops inheriting there (`map-guard-dependency-report`) | judgment |
| Failure modes | the computation of criticality (`failure-mode-severity`, `map-guard-unrecorded-criticality`); whoever sets a severity, who reads the kind of damage | judgment |
| Failure modes — detected by | the format guard (`failure-mode-detection`, `map-invariant-names`); whoever asks which failures the gate would catch | read off |
| Trust boundary | the format guard (`path-pattern-reach`); the choice of how sharply a change is checked (WAY-13) | judgment |
| Criticality (flow) | the computation of the criticality of every part the flow runs through (WAY-46) | judgment |
| Parts (flow) | the format guard (`flow-part-names`, `flow-coverage-parts`); whether a change lies on the flow (WAY-45) | judgment |
| Invariant (flow) | the format guard (`flow-invariant-link`, `map-invariant-names`); the gate, which runs the flow's test on every change (`flow-test-run`) | judgment |
| Coverage (flow) | the format guard (`flow-coverage-parts`) | read off |
| Declared at | the format guard (`surface-declaration`); whoever changes the item | read off |
| criticality scale | the format guard, which rejects a degree not on the list (`failure-mode-severity`); the computation of criticality, which orders the degrees by it | judgment |
| external context | the format guard (`external-exchange-row`); whoever records a trust boundary or sets a change path (WAY-48, WAY-50) | judgment |
| change paths | whoever changes a surface at that level; the format guard (`surface-change-path`, `promise-level-policy`) | judgment |
| files left out on purpose | the format guard, as the only exception to file assignment (`file-part-assignment`, `left-out-file-assignment`) | judgment |
| withdrawn identifiers | the format guards, which reject a reference to one and its reuse (`decision-scope-names`, `identifier-holders`) and check why and the successors (`map-withdrawal-successors`) and, against `{fork-point}`, that every identifier held there stays (`map-identifier-persistence`) | as `elements/common/rules.md` gives it |

## The binding part

The binding part of an entry is one sentence: a part's responsibility, a flow's description, a
surface's promise. Path patterns, dependencies, failure modes and a flow's list of parts stay
outside it (WAY-42). What its fingerprint covers answers to the invariant `map-fingerprint-input`.

## Criticality: what is written and what is computed

- A human writes the failure modes and the separations. A failure mode names what fails, the
  kind of damage it does, its severity, and how it is detected before release — a named
  invariant, or an explicit "not detected" (WAY-46).
- The script computes a part's criticality: the highest of its own failure modes, of the flows
  it lies on, and of the parts that depend on it, stopping where a dependency records a
  separation (WAY-46).
- A part with no failure modes recorded counts as the highest degree (WAY-46).
- An obligation from a law or a contract that raises the criticality of a part enters the map as
  a failure mode of that part, whose detection names an invariant resting on the environment fact
  of that obligation (WAY-46).
- Raising a part's criticality needs no reason; lowering it is accepted by the human deciding the
  change, with the lowered criticality in front of them: the format guard, given the commit the
  task branch left the main branch from, reports every part whose computed criticality is lower
  than there (`criticality-lowering-report`) (WAY-46).
- A separation carries its reason in the dependency that records it: why a failure of that part
  does not damage this one (WAY-46).
- The kind of damage says what a failure does, for whoever sets its severity; the severity, not
  the kind, enters the computed criticality, and the criticality sets how sharply a change is
  checked (WAY-13, WAY-46).

## Assigning files

- Every file git tracks belongs to exactly one part, through the patterns in its *Files* field,
  matched by git rather than by a script of this process (WAY-44).
- A part whose tool does not exist yet holds no files (`Files: none`); every file git tracks
  still belongs to exactly one part
  (`TODO — decision pending: which decision lets a part hold no files`).
- Tests belong to the part they test. Generated files belong to the part of their generator
  (WAY-44).
- The files that serve the whole repository — the lockfile and the build configuration — are a
  part of their own, and a change to them lies on every critical flow (WAY-44, WAY-45).
- The files that only direct whoever carries out the repository's tasks — instructions for agents,
  skills, hooks and the configuration of agents' tools and of CI — are another part of their own
  (WAY-44).
- For a file that collects entries about many parts, the parts a change touches come from the
  field in which the entries it adds or changes name parts — a decision's *Scope*, an invariant's
  *Part*, where `every` names all — not from the file's own part (WAY-44, WAY-62).
- A file no pattern matches, and a file two parts claim, breaks the gate unless it stands on the
  list of files left out on purpose (WAY-44).

## Known violations

The derived file beside the map, `foundations/known_violations.md`, holds the map's debt:
every dependency the code holds that the map does not allow. A row names the source part, the target part, the file and what it reaches for — never a line
number. A new violation breaks the gate; a row the code no longer contradicts breaks it too and
goes in the same change; a row is added only by a change of the foundation that a human accepts.
The file is checked as a subset of the list on the commit the task branch left the main branch
from, never regenerated from scratch (WAY-51).

```markdown
## Known violations

| Source | Target | File | What it reaches for |
```

## What is generated from the map

From the map a product generates for its agents only rules pinned to path patterns (WAY-52); a
generated rule file answers to the invariants `generated-pattern-source` and `generated-overview`.

## Examples

`examples.md` names, by identifier, the entries of this repository's own map
(`foundations/part_map.md`) that show the form of an entry; they are read there, in the commit of
the-way a product pins, instead of being copied (WAY-09, WAY-34). The format guard checks that each
identifier it names is an entry of the map (`map-example-target`).
