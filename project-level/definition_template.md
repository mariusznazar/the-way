# The project definition

A project definition says what a project is to achieve and what it rests on, before the project
is broken into tasks. The skills in `skill/` and `technology/` beside this file write it with a
human, and `readiness_check.py` checks what a script can decide at the readiness gate. The
decisions that set the rules below are cited beside them.

## What a definition is not

- It changes nothing in the foundation. It reads the foundation and projects changes to it; the
  tasks of the project make them (WAY-01;
  WAY-106).
- It holds no plan: phases, the order of work, the tasks and which task carries which decision
  stand in the plan of the project (WAY-36;
  WAY-106).

## Where it stands, and in what language

- The definition stands where the product keeps its projects. The product names that place in a
  `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer writes
  between `<!-- the-way:begin -->` and `<!-- the-way:end -->`:

  ```markdown
  ## Backlog

  - Projects: <a path or a tool>
  - Tasks: <a path or a tool>
  ```

  (WAY-101; WAY-107.)
- The text of the definition, its title included, is in the language the human opened the
  conversation in. The headings, the status line, the markers below and the projected entries
  are in English, whatever that language (WAY-72 for the entries;
  WAY-108).

## The form

```markdown
# <project name>

Status: definition — open: <the sections still holding TODO>

## Goal

## Background

## In scope

## Out of scope

## Inputs and constraints

## Deliverables

## Success

## Risks

## Open questions

## Touched parts and decisions

## Technology

## Projected foundation changes

## Gate record
```

The headings stand once each, in this order, and no other second-level heading stands in the
definition; a third-level heading may stand inside a section. A YAML front matter may stand above
the title where the place of the definition asks for one
(WAY-108).

## The status line

| Status | When |
|---|---|
| `definition — open: <sections>` | some section above the gate record still holds `TODO` |
| `ready for gate` | `readiness_check.py --before-approval` reports nothing: no section above the gate record holds a `TODO` it counts as a gap |
| `approved YYYY-MM-DD` | the gate record is written |

WAY-108.

## Every section, and the words `none` and `TODO`

Every section holds text, `none` or `TODO`: `none` states that nothing is there, `TODO` that
something is known to be missing, as `elements/common/rules.md` gives them for an entry (WAY-71).
A section is never left empty
(WAY-108).

| Section | What it holds |
|---|---|
| Goal | one sentence: what the project is to achieve and why that matters |
| Background | what the people the project serves do today without it and where that hurts; for a revised definition, which premise broke |
| In scope | what the project delivers; the plan breaks the project into tasks from it, and the step that finds foundation entries takes the rules its lines carry |
| Out of scope | only exclusions that end with the project; an exclusion for good is a candidate projected decision (WAY-26) |
| Inputs and constraints | what the project starts from — documents, code, systems, decisions — and what its surroundings impose on it; a constraint that outlives the project is a candidate projected decision or environment fact |
| Deliverables | the concrete results |
| Success | the signals read after the fact and those read during the work; each carries its falsification condition |
| Risks | the risks, and the assumptions whose failure would change the result |
| Open questions | only questions for later, each with its place of resolution |
| Touched parts and decisions | what the foundation says of the project: the parts it touches, the decisions whose *Scope* names them, the invariants it may break |
| Technology | the technology choices the project needs, each with the entry that settles it; the skill `settle-technology` writes it, and it reads `TODO` until that step begins |
| Projected foundation changes | what the definition settles about the product, as projected entries of the foundation, each with its translation, below the line that records the step finding them |
| Gate record | who approved the gate and when, the commit of the foundation searched, the fingerprint |

WAY-108.

- **Background, Success and Risks** hold what the human answered. The agent asks for them; what it
  finds in the material enters a question as its anchor, never the section
  (WAY-109).
- **A frame of success** — each signal or criterion under "Success" — carries one sentence saying
  what would show it false, marked `**OBALENIE:**` in a Polish definition and `**FALSIFIED IF:**`
  in an English one
  (WAY-109).
- **A deadline** appears under "Inputs and constraints" only when the human names one imposed from
  outside, in the human's own words, with how firmly it binds. The agent never asks for a
  deadline, never derives one from the material, and never argues scope or cost from it
  (WAY-110).

## What is not yet known

What is not yet known stands in one of three places
(WAY-108):

1. something missing from the definition itself — its goal, scope or success — is `TODO` in its
   section;
2. an entry not yet worded is a projected entry whose binding sentence or definition reads `TODO`;
3. a question for later is an item under "Open questions".

## Open questions

Each question is an item of a list ending with its place of resolution — the breakdown of the
project, or one task of it, named:

```markdown
- Which records may a contractor view? — resolved in: breakdown
- How does the exporter handle a failed transfer? — resolved in: task: export records
```

A section without questions reads `none`.

## Technology

The section lists the technology and architecture choices the project needs — a language, a
framework, a library, a store of data, a way of logging in, a place to run — each with the entry
that settles it (WAY-121). The skill `settle-technology` writes it after the step that finds the
definition's foundation entries; until then it reads `TODO`.

```markdown
## Technology

- Język i miejsce działania aplikacji — held by: DOC-02/1
- Magazyn dokumentów i ich właścicieli — projected: Where are documents and their owners stored?
```

- Each item names one choice in the language of the definition, by what the product needs it
  for, and ends with one marker in English
  (WAY-121):

  | Marker | When |
  |---|---|
  | `— held by: <PREFIX>-<NN>/<version>` | a decision of the product's foundation settles the choice |
  | `— projected: <question>` | a projected decision of this definition settles it; the question reads as in that decision's heading |
  | `— open` | the step is still settling it; the readiness gate stops it |

- The section never reads `none`: every project runs on something, and the list shows on what. A
  project whose choices the foundation already holds lists each of them `held by`
  (WAY-121).
- A choice the section settles no longer stands under "Open questions"
  (WAY-121).
- The options of each open choice come from research against the definition, one choice at a
  time, pass the filter and the critique WAY-122 sets, and reach the human through their
  consequences for the product (WAY-123); `settle-technology` leads that.

## Projected foundation changes

The section holds what the definition settles about the product before the breakdown, as entries
of the foundation, projected: decisions, invariants, glossary terms, environment facts, and the
changes to the part map whose every field is known before the code
(WAY-116). The skill `find-foundation-entries` finds them with the human and hands each to the
skill of its element in projected mode, which writes it here. The section reads `TODO` until that
step begins.

While the step runs, the section holds its working table, so that a fresh agent resumes it from
the file. The headings of the columns stay in English; the rows are in the language of the
definition:

```markdown
### Candidates in progress

| # | Settlement | Kind | Source | What the next reader would guess | State |
|---|---|---|---|---|---|
| 1 | Dokument należy do dokładnie jednego obszaru roboczego | decision | material: opis produktu §5 | the document's ownership and access rules | accepted |
```

A row's state is `waiting`, `accepted`, `rejected` or `written`. Once every row is `rejected` or
`written`, the table goes and the section begins with the line that records the step:

```markdown
## Projected foundation changes

Candidates: 4 shown, 3 accepted — 2026-01-01

### Decisions

#### (new) — Who owns a document?

<the entry, its *Approved by* reading `on acceptance` until the gate>

> **Translation (pl):** <the same entry in Polish>

#### (new) — Where are documents and their owners stored?

<the entry>

> **Translation (pl):** <the same entry in Polish>

### Invariants

#### one-workspace-per-document/1

<the entry>

> **Translation (pl):** <the same entry in Polish>
```

- The line `Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD` stands first;
  with no row accepted, `none` follows it. Rejected rows are not kept
  (WAY-115).
- A subsection stands for each kind that has entries, in this order: `### Decisions`,
  `### Invariants`, `### Glossary`, `### Environment facts`, `### Part map`. Each entry is in the
  form of its element's template, its heading two levels lower:

  | Kind | Heading |
  |---|---|
  | decision | `#### (new) — <question>`; for a new version of a current decision, `#### <PREFIX>-<NN>/<version> — <question>` |
  | invariant | `#### <identifier>/1`; for a new version, the current identifier and its next version |
  | glossary term | `#### <term>` |
  | environment fact | `#### <identifier>/1`; for a new version, the current identifier and its next version |
  | part map | `#### <identifier> (changed)` with the whole entry as it will read; `#### <identifier> (new)` for a critical flow through existing parts |

- Before a product has a main branch, a proposed edit of an existing decision keeps its current
  identifier and version in the heading: the entry is edited in place when written (WAY-07).
- A new projected decision needs no number and no prefix: the task that writes it into the
  foundation gives them. Other projected headings keep the identifier their element requires.
- Below each entry stands its translation into the language of the definition, every line
  beginning with `>`; it helps the human weigh the wording and is not approved.
- At the gate a projected entry holds whole what only the human gives at the project level: its
  binding sentence or definition and, for a decision, its *Change*, *Rationale* and *Rejected*
  (`none considered` being the human's statement). *Review when* holds a condition and date, or
  `none` when the human knows none; it may read `TODO` when the human expressly defers it because
  the review timing depends on later work, and an item under "Open questions" names the
  breakdown or task that resolves it. A field that waits for the code or the world — a source, a
  verification, a method, the parts, the links, each a line `- **<Field>:** …` with the indented
  lines that continue it — may read `TODO`, as may a translation; *Approved by* reads
  `on acceptance` until the gate, never `TODO`. The format guard of the element checks those
  deferred fields in the task that writes the entry. `TODO` anywhere else in the section is a gap
  (WAY-118, WAY-119).

A section with no projected entry reads the line and `none`
(WAY-117).

## Gate record

Until the gate the section reads `none`. It is written once the human approves the gate, in this
form and order:

```markdown
- Approved by: <who>, YYYY-MM-DD
- Foundation searched at: <the commit of the product's foundation the search for collisions read>
- Definition fingerprint: <the fingerprint readiness_check.py --fingerprint prints>
```

The fingerprint is that of the definition's text from `## Goal` up to `## Gate record`, as
`relation-model/fingerprint.py` computes it. A definition whose text no longer gives its recorded
fingerprint changed after the gate, and goes through the gate again
(WAY-118).
