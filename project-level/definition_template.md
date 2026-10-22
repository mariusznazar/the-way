# The project definition

A project definition says what a project is to achieve and what it rests on, before the project
is broken into tasks. The skills in `skill/` and `technology/` beside this file write it with a
human, and `readiness_check.py` checks what a script can decide at the readiness gate. The
decisions that set the rules below are cited beside them.

## What a definition is not

- It changes nothing in the foundation. It reads the foundation and projects changes to it; each
  enters the foundation with the first task whose code makes it true, or, where no code does,
  with the task the plan assigns (WAY-01; WAY-106; WAY-126).
- It holds no plan: phases, the order of work, the tasks and which task carries which decision
  stand in the plan of the project, whose form `plan/template.md` gives (WAY-36; WAY-106;
  WAY-142).

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

Status: definition — open: <the sections still open>

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
| `definition — open: <sections>` | some section above the gate record still holds `TODO`, or the step that settles the technology has not ended |
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
| In scope | what the project delivers, as a list whose top-level items the plan numbers in order and breaks the project into tasks from (WAY-146); the step that finds foundation entries takes the rules its lines carry |
| Out of scope | only exclusions that end with the project; an exclusion for good is a candidate projected decision (WAY-26) |
| Inputs and constraints | what the project starts from — documents, code, systems, decisions — and what its surroundings impose on it; a constraint that outlives the project is a candidate projected decision or environment fact |
| Deliverables | the concrete results |
| Success | the signals read after the fact and those read during the work; each carries its falsification condition |
| Risks | the risks, and the assumptions whose failure would change the result |
| Open questions | only questions for later, each with its place of resolution |
| Touched parts and decisions | what the foundation says of the project: the parts it touches, the decisions whose *Scope* names them, the invariants it may break |
| Technology | the technology choices the project needs, each with the entry that settles it; the skill `settle-technology` writes it, and it reads `TODO` until that step begins |
| Projected foundation changes | what the definition settles about the product, as projected entries of the foundation, each with one sentence of its meaning, below the line that records the step finding them |
| Gate record | who approved the gate and when, and the fingerprint |

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

The place a question names is its first assignment: once the definition has passed its readiness
gate, the project plan decides where each question is resolved, and moving a question to another
task changes the plan, not the definition (WAY-145).

## Technology

The section lists the technology and architecture choices the project needs — a language, a
framework, a library, a store of data, a way of logging in, a place to run — each with the entry
that settles it (WAY-121). The skill `settle-technology` writes it before the readiness gate
(WAY-121), after the step that finds the definition's foundation entries; until then it reads
`TODO`.

```markdown
## Technology

- Język i miejsce działania aplikacji — held by: DOC-02
- Magazyn dokumentów i ich właścicieli — projected: Where are documents and their owners stored?
```

- A choice belongs on the list when settling it later could change how the work is cut into
  tasks, or when it adds something the product has to run, pay for or back up; a choice one task
  can make and change alone stays with that task
  (WAY-121).
- As an exception to that rule, where the project brings behaviour a user sees in the running
  product, three matters of an agent's way to the running product — its logs, its interface and its
  development data — are looked at, and each matter that no decision of the foundation settles for
  that behaviour stands on the list as a choice of its own, even where its answer adds nothing to
  run, pay for or back up, and even where the product has none of what the matter names, whose
  answer then says what an agent uses in its place; a matter a decision of the foundation already
  settles for that behaviour is not listed. No definition has to hold these matters; a matter
  listed is an ordinary choice of the list, with its marker as the table below gives it
  (WAY-121).
- The logs ask where the record of what the running product does goes and how an agent reads it;
  the interface asks how an agent operates the product as its user does — through a screen in a
  browser, a call to its API or a command in a terminal — and how it sees what the product answers;
  the development data asks where the data comes from on which an agent checks the product's
  behaviour outside production, and how an agent brings that data to the state a check needs. Data
  set up from scratch and a dedicated test environment that persists are both options of that
  choice
  (WAY-165).
- Each item names one choice in the language of the definition, by what the product needs it
  for, and ends with one marker in English
  (WAY-121; WAY-108 for the English form):

  | Marker | When |
  |---|---|
  | `— held by: <PREFIX>-<NN>` | a decision of the product's foundation settles the choice |
  | `— projected: <question>` | a projected decision of this definition settles it; the question reads as in that decision's heading |
  | `— open` | the step is still settling it; the readiness gate stops it |

- An item may hold nested items under it, such as the human's preference for the choice; they
  are no choices of the list
  (WAY-112).
- The section never reads `none`: it records the decision that holds each choice, and a project
  whose choices the foundation already holds lists each of them `held by`
  (WAY-121).
- A choice the section settles no longer stands under "Open questions"; a question that asks
  several choices narrows to what it still asks
  (WAY-108).
- The options of each open choice come from research of that choice against the definition,
  never from a fixed list of stacks; the research of every choice that depends on no unsettled
  choice starts once the list is confirmed, each in a report of its own. An option the project's
  code is written in or against — a language, a framework, a library, a store of data — is weighed
  by whether its documentation shows that it uses explicit types, follows conventions of layout
  and naming and has current, versioned documentation, and whether a public record of its use,
  such as a package registry or a survey, shows it widely used within its language family; for a
  store of data, its types are those it declares for what it stores, and its family is that of its
  query language. An option lacking one of these properties is offered with what each lack means
  for the product, which the decision records if the human chooses it; an option with no
  documentation or with a project no longer maintained is left out with that reason, unless the
  human named it or the definition holds it as a constraint, and then it is offered with that
  reason as such a lack; every option is offered only after a critique that refutes every claimed
  difference no source supports
  (WAY-122).
- The human sees the options through their consequences for the product — what each costs, where
  it runs, what keeping it running takes and what changing it later costs — and chooses between
  them; where no difference with a consequence remains, the step recommends the simplest and
  cheapest option. The choices whose research started together reach the human together, in one
  table, once every one of their comparisons has passed the critique, each with its recommendation
  and the weak point of the option recommended (WAY-123).
- In a choice of an agent's way to the running product, whether an agent can use an option is a
  consequence for the product: an option an agent cannot use stays in the comparison with that lack
  said as "an agent does not check the running product this way", and the recommendation passes
  over it
  (WAY-166).
- Where the options of a place to run differ in no consequence for the product and more than one
  of them is the simplest and cheapest, the step recommends, of those, the one an agent works with
  best: operated from a terminal, deployed by a script and documented in pages an agent can read.
  For a place to run, how well an agent works with an option decides nothing else: it leaves no
  option out of the comparison and is weighed against no consequence for the product
  (WAY-137).
- The option recommended for each choice the step settles, one a constraint of the definition
  settles included, is tested with a devil's advocate, a pre-mortem and a search for unknown
  unknowns; no choice a decision of the foundation holds is tested, and no decision already
  written is tested afterwards. The risks these tests give are hypotheses with no source, not
  differences claimed between options, so the critique of the comparison does not strike them,
  and they stand in the table beside the option recommended before the human chooses. The human
  who chooses that option takes its risks, and each risk taken reaches the decision of that choice
  in its *Rationale*, beside the lacks of the option chosen, marked as a hypothesis
  (WAY-138). `settle-technology` leads that.

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

Candidates: 3 shown, 2 accepted — 2026-01-01

### Decisions

#### (new) — Who owns a document?

<the entry>

> **Meaning (pl):** <one sentence of the entry's meaning in the definition's language>

#### (new) — Where are documents and their owners stored?

<the entry>

> **Meaning (pl):** <one sentence of the entry's meaning in the definition's language>

### Invariants

#### one-workspace-per-document

<the entry>

> **Meaning (pl):** <one sentence of the entry's meaning in the definition's language>
```

- The line `Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD` stands first;
  with no row accepted, `none` follows it. Rejected rows are not kept
  (WAY-115).
- A decision `settle-technology` projects stands under `### Decisions` among the others and
  leaves the line as it is: it is no row of the step that finds entries
  (WAY-115).
- A subsection stands for each kind that has entries, in this order: `### Decisions`,
  `### Invariants`, `### Glossary`, `### Environment facts`, `### Part map`. Each entry is in the
  form of its element's template, its heading two levels lower:

  | Kind | Heading |
  |---|---|
  | decision | `#### (new) — <question>`; for a change of a current decision, `#### <PREFIX>-<NN> — <question>` |
  | invariant | `#### <identifier>`; for a change of a current invariant, its identifier |
  | glossary term | `#### <term>` |
  | environment fact | `#### <identifier>`; for a change of a current fact, its identifier |
  | part map | `#### <identifier> (changed)` with the whole entry as it will read |

- A projected change of an existing entry keeps its identifier in the heading, with no version:
  the task that writes it edits the entry in place (WAY-07).
- A new projected decision needs no number and no prefix: the task that writes it into the
  foundation gives them. Other projected headings keep the identifier their element requires.
- Below each entry stands one sentence of its meaning in the language of the definition, a line
  beginning with `>`; the human approves the meaning at the gate, not the wording. No entry
  carries a field of approval: the gate record approves them all.
- At the gate a projected entry holds whole what only the human gives at the project level: its
  binding sentence or definition and, for a decision, its *Rationale* and *Rejected*
  (`none considered` being the human's statement). A field that waits for the code or the world —
  a source, a verification, the parts, the links, each a line `- **<Field>:** …` with the indented
  lines that continue it — may read `TODO`, as may a meaning sentence; the task that writes the
  entry into the foundation completes those fields, and `elements/common/foundation_check.py`
  checks the entry there. `TODO` anywhere else in the section is a gap
  (WAY-118).

A section with no projected entry reads the line and `none`
(WAY-117).

## Gate record

Until the gate the section reads `none`. It is written once the human approves the gate, in this
form and order:

```markdown
- Approved by: <who>, YYYY-MM-DD
- Definition fingerprint: <the fingerprint readiness_check.py --fingerprint prints>
```

The fingerprint is that of the definition's text from `## Goal` up to `## Gate record`, as
`relation-model/fingerprint.py` computes it. A definition whose text no longer gives its recorded
fingerprint changed after the gate, and goes through the gate again
(WAY-118).
