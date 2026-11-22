# Part map template

This file defines how a product's part map is written. The map holds the parts of a product and
what joins them: which part may depend on which, where a part takes in what the product does not
control, and what the product promises to someone outside it. It holds rules and a
description of the state that the return step compares with the code; a detail that changes with
every change of the code lives in the code or in a test, never in the map (WAY-225, WAY-44).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, the form of an identifier, when it stays and when a split or a merge replaces it, its
one space with the invariants and the environment facts, the list of withdrawn identifiers and the
absence of versions — stand in `elements/common/rules.md`; this template holds what is particular
to the part map (WAY-35).

## Where entries go

- The whole map is one Markdown file, `foundations/part_map.md`, of the shape below.
- It holds two kinds of entry — a **part** and a **surface** — and three lists that are
  not entries: the external context (WAY-48), the files left out on purpose (WAY-44) and the
  withdrawn identifiers. Each kind answers what the other cannot: a part, what it is responsible for
  and which files are its; a surface, what someone outside relies on.
- An allowed dependency of a part and a trust boundary are fields of the part they belong to, never
  entries of their own (WAY-48). A critical flow has no entry.
- An entry is edited in place and carries no version; its history stays in git (WAY-07). A change
  of the code that changes what a part answers for, which files are its or what it may depend on,
  or what a surface promises, rewrites the entry in the same change (WAY-11).
- The forms below give `none` to the fields that take it, and `TODO` to no field
  (`elements/common/rules.md`, WAY-71).

## Identifiers

The rules on when an entry's identifier stays, when a split or a merge replaces it, and how the
one left behind is withdrawn and never reused stand in `elements/common/rules.md`.

## Form of an entry

### Part

```markdown
## <identifier>

<what this part is responsible for, briefly, in as few sentences as that needs>

- **Files:** <git path patterns, one per line, each a directory or one kind of file> | none
- **Depends on:** <identifier> · <identifier> | none
- **Trust boundary:** <git path patterns of the files that take in what the product does not
  control> | none
```

### Surface

```markdown
## <identifier>

<what the product promises to keep, briefly, in as few sentences as that needs>

- **Relied on by:** <who outside the product relies on it>
```

## Assigning files

- Every file git tracks belongs to exactly one part, through the patterns in its *Files* field,
  matched by git rather than by a script of this process (WAY-44).
- A pattern names a directory, or one kind of file by a single pattern — every invariant test,
  say — rather than files one by one, so that adding or moving a file inside a directory leaves the
  map as it is (WAY-44).
- A part whose tool does not exist yet holds no files (`Files: none`); every file git tracks
  still belongs to exactly one part.
- Tests belong to the part they test. Generated files belong to the part of their generator
  (WAY-44).
- The files that serve the tests of several parts — a helper the tests of two parts import, say —
  are a part of their own, whose sentence says that it holds them; its entry takes no field of its
  own for it. The tests of every part may import from that part, and code that is no test may not
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
holds the rule, and the code shows the state (WAY-225). What counts as a dependency of a part is
what the glossary gives that term, any reach and not only an import, so *Depends on* covers every
such reach. The return step of a change compares the two for the parts the change touches
(WAY-11).

Every product whose parts import code from other parts holds one invariant of allowed imports,
with its test in the product's suite, that a file of a part imports only files of its own part, of
the parts its *Depends on* names, of a part of test helpers where the importing file is a test (see
"Assigning files"), and of a part that an invariant "the part `<part>` does not depend on `<part>`"
reading `Violated: yes` says it depends on today:

- the test reads this map and the imports of the product's own languages, and names the parts of
  test helpers by identifier; how it tells a test from other code is settled by the task that
  writes it;
- the product writes the invariant and its test in the change that brings into the map a second
  part holding such code, and a product that already holds such parts writes them in a task of its
  own;
- the-way's own is `cross-part-imports`, named in `elements/invariants/examples.md`.

This is a duty rather than advice, since a step nothing enforces is the step an agent leaves out,
and an import from outside the map then passes merge after merge unseen.

A dependency that a settlement of the task names, or that the human allows, is written into
*Depends on* by the change, its source named in the commit message, since the map holds no field
for it; a settlement that asks only for a behaviour allows no dependency. The route below is for a
dependency the human accepts as it stands without allowing it.

A dependency of a part that the code holds and *Depends on* does not allow goes to the human. Where
the human accepts it as it stands, it is written as an invariant — "the part `<part>` does not
depend on `<part>`" — that reads `Violated: yes`, its test standing as an expected failure until the
code meets it, as the invariants template's "Violated" gives it, while the invariant of allowed
imports above lets that import pass, where the dependency is an import, and keeps every other
boundary; *Depends on* is never rewritten to fit what the code reaches for today (WAY-225, WAY-51).
Each such invariant is a whole entry a human accepted, not a list of known violations, and the map
holds no list of such dependencies of a part.

## Trust boundary

- A trust boundary is a pattern of the code files of a part that take in what the product does not
  control: data from the network, keys, the deployment, files that come from outside the product,
  such as one on the user's disk. A script that only checks the product's own files is no trust
  boundary (WAY-48).
- A change that touches the files of a trust boundary is checked for crafted input, and its review
  is aimed at that risk (WAY-48).

## Surfaces

- A surface is what someone outside the product relies on — an API, a file format, a command — and
  its entry states the promise briefly, in as few sentences as it needs, and names in *Relied on by*
  who relies on it.
- A change that alters a surface names the surface in its request, since a broken promise falls on
  someone who took no part in the change, and the request names it for the agent reviewing the
  change and the human merging it.

## Critical flows

A critical flow has no entry in the map. What has to stay true along it is an invariant whose
*Part* names the parts the flow runs through, and its test is a test of the product's suite like
any other, run with the rest of the suite. The product's tests run whole on every change, so a
flow's test needs no list of parts to be chosen by, and the invariant's *Part* already names where a
change can break the flow.

## Exchanges with the external context

```markdown
## External context

| Partner | Direction | What comes in |
|---|---|---|
| <who or what> | them → us · us → them · both | trusted · untrusted · — |
```

A row names no part and no file. It is read by whoever records a trust boundary at the part that
handles the exchange (WAY-48).

## Files left out on purpose

```markdown
## Files left out on purpose

| File | Why |
```

The list is the only exception to "every tracked file has a part" (WAY-44).

## Withdrawn identifiers

After the last entry the map carries its withdrawn identifiers, in the form, with the *Why* and the
*Successors*, that `elements/common/rules.md` gives.

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when |
|---|---|
| identifier (heading) | `elements/common/foundation_check.py`, which finds every *Scope*, *Part* and *Depends on* naming it; whoever follows such a reference |
| sentence | the agent making a change to the part's files or to what the surface promises; the search of the foundation, when the sentence changes |
| Files | the agent naming the parts its work touches; `foundation_check.py`, which finds each tracked file in one part; the test of the invariant of allowed imports, which finds the part of each file |
| Depends on | the agent making a change, which keeps the code within it; the return step, which compares it with the code; `foundation_check.py`; the test of the invariant of allowed imports, which compares it with the imports |
| Trust boundary | the agent making a change that touches its files, and the agent reviewing it, who check crafted input |
| Relied on by | the agent making a change to the surface, and the human merging its request, who see whom the change reaches |
| external context | whoever records a trust boundary at the part that handles an exchange (WAY-48) |
| files left out on purpose | `foundation_check.py`, as the only exception to file assignment |
| withdrawn identifiers | whoever follows an identifier that no longer names an entry; `foundation_check.py`, which keeps a withdrawn identifier from naming an entry again |

## The binding part

The binding part of an entry is a part's responsibility or a surface's promise, each described
briefly, in as few sentences as it needs. *Files*, *Depends on*, *Trust boundary* and *Relied on by*
stay outside it. Whatever names an entry relies on what the entry answers for, and the other fields
change more often without changing that, so making them binding would send the author to the
entries naming it for changes that do not alter the promise.

## Examples

`examples.md` names, by identifier, the entries of this repository's own map
(`foundations/part_map.md`) that show the form of an entry; they are read there, in the commit of
the-way a product pins, instead of being copied (WAY-09, WAY-34).
