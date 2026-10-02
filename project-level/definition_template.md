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
  conversation in. The headings, the status line, the markers below and the projected decisions
  are in English, whatever that language (WAY-72 for the decisions;
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
| In scope | what the project delivers; the plan breaks the project into tasks from it |
| Out of scope | only exclusions that end with the project; an exclusion for good is a projected decision (WAY-26) |
| Inputs and constraints | what the project starts from — documents, code, systems, decisions — and what its surroundings impose on it; a constraint that outlives the project is a projected decision or a candidate environment fact |
| Deliverables | the concrete results |
| Success | the signals read after the fact and those read during the work; each carries its falsification condition |
| Risks | the risks, and the assumptions whose failure would change the result |
| Open questions | only questions for later, each with its place of resolution |
| Touched parts and decisions | what the foundation says of the project: the parts it touches, the decisions whose *Scope* names them, the invariants it may break |
| Projected foundation changes | new decisions and new versions of current ones, in the form of a log entry, each with its translation |
| Gate record | who approved the gate and when, the commit of the foundation searched, the fingerprint |

`TODO — decision pending: which decision sets the sections of a project definition`.

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
2. a decision not yet worded is a projected decision whose binding sentences read `TODO`;
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

Each projected decision is an entry in the form of `elements/decisions/template.md`, written by
the decisions skill in its projected mode. A new decision is headed `### (new) — <question>`; a new
version of a current decision is headed with that decision's number and its next version. Below
the entry stands its translation into the language of the definition, which helps the human weigh
the wording and is not approved:

```markdown
### (new) — What does the game exclude for good?

<the entry, its *Approved by* reading `on acceptance` until the gate>

> **Translation (pl):** <the same entry in Polish>
```

A section without projected decisions reads `none`
(`TODO — decision pending: which decision sets the form of a projected decision`).

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
