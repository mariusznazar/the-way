# The project definition

A project definition says what a project is to achieve and what it rests on, before the project
is broken into tasks. The skill in `skill/` beside this file writes it with a human, and
`readiness_check.py` checks what a script can decide at the readiness gate. The project level has
no decision in the log of the-way yet: every rule below ends with the decision it waits for.

## What a definition is not

- It changes nothing in the foundation. It reads the foundation and projects changes to it; the
  tasks of the project make them (WAY-01;
  `TODO — decision pending: which decision sets that the project level writes nothing in the
  foundation`).
- It holds no plan: phases, the order of work, the tasks and which task carries which decision
  stand in the plan of the project (WAY-36;
  `TODO — decision pending: which decision sets what the plan of a project holds`).

## Where it stands, and in what language

- The definition stands where the product keeps its projects. The product names that place in a
  `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer writes
  between `<!-- the-way:begin -->` and `<!-- the-way:end -->`:

  ```markdown
  ## Backlog

  - Projects: <a path or a tool>
  - Tasks: <a path or a tool>
  ```

  (WAY-101; `TODO — decision pending: which decision sets where a product names the place of its
  backlog`.)
- The text of the definition, its title included, is in the language the human opened the
  conversation in. The headings, the status line, the markers below and the projected entries
  are in English, whatever that language (WAY-72 for the entries;
  `TODO — decision pending: which decision sets the language of a project definition`).

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

## Projected foundation changes

## Gate record
```

The headings stand once each, in this order, and no other second-level heading stands in the
definition; a third-level heading may stand inside a section. A YAML front matter may stand above
the title where the place of the definition asks for one
(`TODO — decision pending: which decision sets the form of a project definition`).

## The status line

| Status | When |
|---|---|
| `definition — open: <sections>` | some section above the gate record still holds `TODO` |
| `ready for gate` | no section above the gate record holds `TODO` |
| `approved YYYY-MM-DD` | the gate record is written |

`TODO — decision pending: which decision sets that a project definition carries its state in a
status line`.

## Every section, and the words `none` and `TODO`

Every section holds text, `none` or `TODO`: `none` states that nothing is there, `TODO` that
something is known to be missing, as `elements/common/rules.md` gives them for an entry (WAY-71).
A section is never left empty
(`TODO — decision pending: which decision sets the words none and TODO in a project definition`).

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
| Projected foundation changes | what the definition settles about the product, as projected entries of the foundation, each with its translation, below the line that records the step finding them |
| Gate record | who approved the gate and when, the commit of the foundation searched, the fingerprint |

`TODO — decision pending: which decision sets the sections of a project definition`.

- **Background, Success and Risks** hold what the human answered. The agent asks for them; what it
  finds in the material enters a question as its anchor, never the section
  (`TODO — decision pending: which decision sets that a definition's background, success and risks
  come from the human's answers`).
- **A frame of success** — each signal or criterion under "Success" — carries one sentence saying
  what would show it false, marked `**OBALENIE:**` in a Polish definition and `**FALSIFIED IF:**`
  in an English one
  (`TODO — decision pending: which decision sets that every frame of success carries its
  falsification condition`).
- **A deadline** appears under "Inputs and constraints" only when the human names one imposed from
  outside, in the human's own words, with how firmly it binds. The agent never asks for a
  deadline, never derives one from the material, and never argues scope or cost from it
  (`TODO — decision pending: which decision sets how a deadline enters a project definition`).

## What is not yet known

What is not yet known stands in one of three places
(`TODO — decision pending: which decision sets the three places of an unknown in a project
definition`):

1. something missing from the definition itself — its goal, scope or success — is `TODO` in its
   section;
2. an entry not yet worded is a projected entry whose binding sentence or definition reads `TODO`;
3. a question for later is an item under "Open questions".

## Open questions

Each question is an item of a list ending with its place of resolution — the breakdown of the
project, or one task of it, named:

```markdown
- How is a program shown to fail on the second map? — resolved in: breakdown
- What tools does the author mode have? — resolved in: task: map editor
```

A section without questions reads `none`.

## Projected foundation changes

The section holds what the definition settles about the product before the breakdown, as entries
of the foundation, projected: decisions, invariants, glossary terms, environment facts, and the
changes to the part map whose every field is known before the code
(`TODO — decision pending: which decision sets which kinds of entry a project definition
projects`). The skill `find-foundation-entries` finds them with the human and hands each to the
skill of its element in projected mode, which writes it here. The section reads `TODO` until that
step begins.

While the step runs, the section holds its working table, so that a fresh agent resumes it from
the file. The headings of the columns stay in English; the rows are in the language of the
definition:

```markdown
### Candidates in progress

| # | Settlement | Kind | Source | What the next reader would guess | State |
|---|---|---|---|---|---|
| 1 | Postać należy do dokładnie jednej drużyny i korzysta z jej skrzynki | decision | material: koncepcja §5 | the data model of a team and its chest | accepted |
```

A row's state is `waiting`, `accepted`, `rejected` or `written`. Once every row is `rejected` or
`written`, the table goes and the section begins with the line that records the step:

```markdown
## Projected foundation changes

Candidates: 24 shown, 17 accepted — 2026-10-05

### Decisions

#### (new) — Who owns a character?

<the entry, its *Approved by* reading `on acceptance` until the gate>

> **Translation (pl):** <the same entry in Polish>

### Invariants

#### one-team-per-character/1

<the entry>

> **Translation (pl):** <the same entry in Polish>
```

- The line `Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD` stands first;
  with no row accepted, `none` follows it. Rejected rows are not kept
  (`TODO — decision pending: which decision sets the record of the step that finds foundation
  entries`).
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

- A projected entry needs no number and no prefix: the task that writes it into the foundation
  gives them.
- Below each entry stands its translation into the language of the definition, every line
  beginning with `>`; it helps the human weigh the wording and is not approved.
- At the gate the wording of every projected entry is whole; its fields need not be. `TODO` in a
  field — a line `- **<Field>:** …` and the indented lines that continue it — or in a translation
  is no gap the gate stops at: the format guard of the element checks the fields in the task that
  writes the entry. `TODO` anywhere else in the section is a gap
  (`TODO — decision pending: which decision sets that the gate asks a projected entry for its whole
  wording, not its whole fields`).

A section with no projected entry reads the line and `none`
(`TODO — decision pending: which decision sets the form of a projected entry`).

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
(`TODO — decision pending: which decision sets the readiness gate of a project`).
