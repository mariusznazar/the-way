# The task document

A task document states what one task must change and why. It is written before the task cycle and
copied into the cycle's record at the cycle's start. A task may belong to a project, use a project's
approved settlements without belonging to its plan, or stand on its own. The document carries
the sources and scope needed for this task, and what its refinement settles for the foundation; the
cycle's record holds the implementation plan and results.

Write the title and content in the language in which the human opened the task. Keep the headings,
status values and `none` / `TODO` markers in English so an agent can resume the document.

```markdown
# <task title>

Status: refining
Project relation: independent | plan item: <project plan> — <the task's name in the plan> | source only: <project definition>

## Description

### Need

- <what is missing, for whom, and how this serves the project goal>

### To do

1. <one observable change per item>

### Acceptance criteria

- <only conditions not implied by the items above>

### Questions to settle

- <question whose answer is needed to take the task>
  - Answer: TODO
  - Source: <document location and revision, code file:line and revision, or human/date/words>

## Context

- <information that answers a likely question about Description, or none>

## Questions carried to cycle

<implementation questions carried from the task's sources, or none>

## Human actions

- <human action outside the repository> — before the cycle, <done|not done> | in the cycle | TODO

<or, in place of the list, the word none>

## Decisions in play

<current foundation decisions the task touches and relevant approved project settlements, or none>

## Settlements to record

Candidates: <rows shown> shown, <rows accepted> accepted — YYYY-MM-DD

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | <one sentence, in the human's words> | decision | <the human's answer or a line of this document> | <a concrete choice the cycle would make> |

## Out of scope

<exclusions that end with this task, or none>
```

`Acceptance criteria` and `Questions to settle` appear only when they have content. The other
sections always appear. `Status:` reads `refining`, `waiting for human`, or `ready for cycle`.
`Project relation:` records whether the task is independent, belongs to an item of an approved
project plan, or only uses an approved project definition as a source. A task that uses a
definition without plan membership never acquires that plan's assignments or dependencies.
`TODO` marks a missing answer; never use it to make an unfinished task look ready.
`ready for approval` is a conversation turn result, never a value of `Status:`. Every task,
including a manually refined one with no candidates, waits for the human to see and accept its
complete final document before `ready for cycle` (WAY-124). Candidate selection and Human-action
placement alone do not accept that document. In orchestrated refinement only the refiner edits
the body; the project orchestrator changes only `Status:` after final acceptance (WAY-154).

## What each section carries

- **Need:** the concrete absence or present problem and its recipient. For a project task, state
  how it serves the approved project goal; for another task, use its own stated purpose.
  Describe a claimed current behavior as a user's report until code or another source confirms it.
- **To do:** a numbered list of distinct, executable changes to behavior or deliverables. Keep
  data needed to make a change in its item. Do not prescribe classes, functions or implementation
  steps unless the approved source makes one a constraint. The cycle's plan chooses how, or the
  choices of its cycle record where no plan is written.
- **Acceptance criteria:** an additional observable condition only when completing every `To do`
  item might still leave it false. Do not repeat the work list in other words.
- **Questions to settle:** questions whose answers are or were needed to take the task. Keep each answer under
  its question. A product decision is settled by the human or by an already approved source;
  an implementation choice belongs to the cycle's plan, or to the choices of its cycle record
  where no plan is written. Keep settled questions and answers with their original provenance here,
  including answers transferred from a refinement conversation:
  exact document quotation and location/revision, factual code observation and `file:line`/revision,
  or the human's words and date. Code answers only how the product currently is, never how it is
  to be. A canonical answer shared by tasks is copied with its source into each affected task;
  a link to an ignored conversation or another question alone is insufficient. A struck quotation
  remains unresolved until answered again. This section also keeps a question/reason explicitly
  waiting for another task's result; plan dependencies alone do not delay refinement.
- **Context:** concise provenance, constraints, links and code entry points that a reader is
  likely to ask about. Never repeat Description or prove the writer's own inference here.
- **Questions carried to cycle:** name implementation questions taken from the task's sources.
  For a task belonging to a project, account for every open question assigned to its plan item.
  For a task using a project as a source only, include only the questions the task explicitly
  takes on. `none` means none is carried. A known question about required product behavior is
  answered before readiness rather than left as an unspecified implementation choice.
- **Human actions:** each effect the task has outside the product's repository — on a server, in
  DNS, on keys or on an external account — is made only by a human, through a human action this
  section names (WAY-140). Reading outside the repository is no human action; it stays with the
  agent. Each human action states its placement, which the human sets while the task is refined, on
  the agent's proposal: `before the cycle` when the cycle's code needs its effect, such as an
  account, a key or a database, with `done` or `not done`; `in the cycle` when it uses code the
  cycle writes, such as a deployment or a DNS record pointing to a new address (WAY-140). Until the
  human places a human action, its placement reads `TODO`. The task is ready only when every human
  action before the cycle is done (WAY-124); the cycle opens a blocked draft request listing the
  human actions in the cycle, and the human performs them at the request (WAY-140). `none` means the
  task has no effect outside the repository. A task document written before this section existed
  names no human action.
- **Decisions in play:** name and quote current foundation decisions this task touches with their
  identifiers and versions. If the task uses an approved project definition, copy the relevant
  projected wording and identify its heading there. A project plan determines which entries a
  member task is assigned to realize or write; a source-only task takes no assignment, and marks,
  among the projected wording it copies, each entry, or the part of one, that its code makes true,
  so that its cycle writes it (WAY-124, WAY-126). `none` means the search found no applicable
  entry; it is not a substitute for the search.
- **Settlements to record:** what the human settled while the task was refined and what still binds
  after the task's merge, kept for its cycle to write into the foundation (WAY-134). The skill
  `find-foundation-entries` builds the candidates and the human cuts them; only accepted rows stay.
  *Settlement* is one sentence in the human's words, in the document's language. *Kind* reads
  `decision`, `invariant`, `glossary term` or `environment fact`; an environment fact stands only
  where a kept decision or invariant rests on it, and a change of the part map is never a row.
  *Source* names the human's answer, or the line of this document, that carries the settlement.
  Keep enough of that answer and provenance in this document to survive removal of a temporary
  conversation; no accepted row may rely only on a deleted file. In orchestrated mode the project
  orchestrator presents the candidates and required questions against choices through the round
  package; the refiner records the human's selection without making it itself (WAY-134).
  The last column names a concrete thing the cycle would do or choose without the row. A settlement
  that an entry of the current foundation or a projected entry under *Decisions in play* already
  states is no row. The cycle writes each row whole, keeping its meaning and choosing its wording,
  and asks the human before the request where that meaning cannot hold (WAY-134). Until the
  candidates are cut, the section reads `TODO`; with no row accepted, `none` stands below the line.
- **Out of scope:** only task-bound exclusions. A lasting exclusion belongs in a projected or
  current decision, or in a row of *Settlements to record*, not here.

The title is one descriptive line without a final period. Each fact has one home in the document; a
row of *Settlements to record* restates in one sentence what its *Source* names, since the cycle
writes its entry from the row. Keep each sentence of Description and Context in a separate list
item. If the project source leaves a value open, ask or keep `TODO`; do not fill it from general
knowledge.
