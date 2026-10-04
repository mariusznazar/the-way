# The task document

A task document states what one task must change and why. It is written before the task cycle and
copied onto the task branch at the cycle's start. The project definition holds the project's
settlements; the project plan assigns work and dependencies; the task document carries only the
portion needed to execute this task. The cycle's record holds the implementation plan and results.

Write the title and content in the language in which the human opened the task. Keep the headings,
status values and `none` / `TODO` markers in English so an agent can resume the document.

```markdown
# <task title>

Status: refining
Plan item: <the exact task item in the project plan, or TODO>

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

## Context

- <information that answers a likely question about Description, or none>

## Questions carried to cycle

<project questions assigned to this task that concern implementation choices, or none>

## Decisions in play

<approved projected entries this task realizes or writes, and current foundation decisions it
touches, or none>

## Out of scope

<exclusions that end with this task, or none>
```

`Acceptance criteria` and `Questions to settle` appear only when they have content. The other
sections always appear. `Status:` reads `refining`, `waiting for human`, or `ready for cycle`.
`Plan item:` identifies one item of the approved project plan, including its dependencies and
assignment of projected foundation entries; it reads `TODO` before that match is established.
`TODO` marks a missing answer; never use it to make an unfinished task look ready.

## What each section carries

- **Need:** the concrete absence or present problem, its recipient, and its connection to the
  approved project goal. Describe a claimed current behavior as a user's report until code or
  another source confirms it.
- **To do:** a numbered list of distinct, executable changes to behavior or deliverables. Keep
  data needed to make a change in its item. Do not prescribe classes, functions or implementation
  steps unless the approved source makes one a constraint. The cycle's plan chooses how.
- **Acceptance criteria:** an additional observable condition only when completing every `To do`
  item might still leave it false. Do not repeat the work list in other words.
- **Questions to settle:** only gaps that prevent a task from being taken. Keep each answer under
  its question. A product decision is settled by the human or by an already approved source;
  an implementation choice belongs to the cycle's plan.
- **Context:** concise provenance, constraints, links and code entry points that a reader is
  likely to ask about. Never repeat Description or prove the writer's own inference here.
- **Questions carried to cycle:** reproduce by name every open question assigned to this task by
  the approved project definition that concerns how to implement an already settled behavior.
  `none` means no such question was assigned. An assigned question about product behavior must
  instead be answered in the task document before readiness.
- **Decisions in play:** copy the approved wording of each projected foundation entry this task
  realizes or writes, identifying its heading in the project definition. Name and quote the
  current foundation decisions this task touches with their identifiers and versions. A link
  alone is insufficient for projected wording that the cycle must carry. `none` means the search
  found no applicable entry; it is not a substitute for the search.
- **Out of scope:** only task-bound exclusions. A lasting exclusion belongs in a projected or
  current decision, not here.

The title is one descriptive line without a final period. Each fact has one home
in the document. Keep each sentence of Description and Context in a separate list item. If the
project source leaves a value open, ask or keep `TODO`; do not fill it from general knowledge.
