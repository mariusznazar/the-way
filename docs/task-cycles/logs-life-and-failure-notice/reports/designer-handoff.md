# Handoff — designer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logs-life-and-failure-notice`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Skills named below are this
  repository's files, listed here by path.
- Target branch `foundations`, base `5d66387`, task branch `task/logs-life-and-failure-notice`.
  You make no commit and change no file of the repository. You write two files only, both ignored
  by Git:
  - the spec: `.runs/task-cycles/logs-life-and-failure-notice/spec.md`
  - your report: `.runs/task-cycles/logs-life-and-failure-notice/reports/designer.md`
- The full test run of the base is running in this worktree in the background: touch no tracked
  file.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **designer**. Read each file it names
when the step that names it comes. Your boundary: you return with `questions`, `done` or
`reserved`, before any plan or code; you start no later stage.

## The task

Frozen task, read it whole: `.runs/task-cycles/logs-life-and-failure-notice/task.md`. It was copied
from the author's private notes on 2026-10-31, accepted there with `Status: ready for cycle`,
`Project relation: independent`. Its citations stand at `foundations` `f86fd71`; the base `5d66387`
differs from that commit only in `product-guidelines/coding/**` and in two passages of
`foundations/decisions.md` outside the entries in play, so its line numbers in that file from
WAY-219 on moved by about eleven lines.

The task's *To do*, its answers to questions 1–6 (read with the two marks of what answer 5
replaced) and its four rows of *Settlements to record* are settled. They bind you; your spec does
not reopen them.

**One restriction stands in the task's Context and binds you:** do not open
`C:\Storage\repos\loop2-10x`, the branch `10x/m3l5`, the tag `archive/10x-m3l5` of the repository
`loop2`, or the map of m3l5. The change must not know what lies there.

## Answers of step 4

- Trust boundary: no at the start. The part map names `project-level/readiness_check.py`,
  `project-level/plan_check.py` and `project-level/plan_state.py` among others, and To do 6 keeps
  the readiness gate as it is. Where your design changes one of these, say so in the spec, by file.
- Operation that cannot be undone: no.
- Open design choice: yes, the choices below.

## The choices this spec settles

These are the task's *Questions carried to cycle*, split. Settle each, with the ways weighed.

1. **A list written before this change (the main choice).** The step at a definition that is not
   yet approved resumes from its Technology section. `project-level/technology/start.md` adds "each
   matter it finds missing", and `project-level/technology/running_product.md` reads a matter as
   the template gives it. After this change, what a logs item standing `— held by:` or
   `— projected:` is held by may say nothing of how long the record lives: the item is on the list,
   so it is not "missing" in the sense of `start.md`, yet the task's Context says such a decision no
   longer settles the matter. Settle what a resumed step does with that item in each of the two
   markers, and with a list that has no failure item at all, keeping To do 6: an approved definition
   does not come back. Say who may open what: an agent never opens a held decision at a task
   (`project-level/technology/task_run.md`), and say whether that rule of a run at a task has any
   bearing at a definition. If the answer binds after the merge, name which entry carries it.
2. **Where the look at the failure item stands.** `running_product.md` describes an agent's way to
   the running product, and the failure item is outside that family by answer 1. Settle the file it
   stands in and how `SKILL.md`, `start.md` and `list.md` of the step reach it, including what
   `SKILL.md` says at its step 1, whose condition today is only behaviour a user sees.

## What the design has to fit, for you to check, not a design

Each of these is a place where the settled rows meet the existing text. Where one calls for a
design decision, make it in the spec; where it follows with no way open, name it under
*Foundation entries* or *Left to the maker*.

- Rows 2 and 3: one new decision or two; how it stands beside the exception of WAY-121, whose
  sentence and *Verification* say what the step lists; what WAY-100 asks of the adoption.
- Row 1: WAY-165's sentence, its compliant example and its rationale, which speaks only of
  checking a change; the template's logs bullet.
- Row 4: WAY-139's list and its procedure; `project-level/task/skill/resolve_gaps.md`; what the
  task's Context says about the case "the human asks for a run while the task is refined". A
  deployment skill that records a refusal counts as covering those two items under the check.
- To do 5: "świadomy brak" always enters the failure item's comparison, though it has no page of
  documentation, while `project-level/technology/research.md` and the template's research bullets
  ask each option for a page, and an option with no documentation is left out unless a human named
  it. Say what changes and where, and name no tool in the step's text.
- To do 5 and WAY-138: the deliberate absence, when recommended, is tested.
- `project-level/technology/task_run.md`: its line that the look of `running_product.md` is not
  taken, and what a run at a task does about the failure item; answer 5 leaves WAY-267 unchanged.
- WAY-166 and `research.md` step 3 and `settle.md` sub-step 5: they keep applying to the logs, its
  life included, and not to the failure item.
- Answer 3: the boundary between what the step settles and what code guidelines settle — whether
  any text of the-way states that boundary today and so has to change. Search; the task's quoted
  phrase may stand nowhere in this repository.
- The glossary entry `agent's way to the running product` in `foundations/glossary.md`: whether the
  new item needs a term of its own by the test of `elements/glossary/`.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-100, WAY-106, WAY-121, WAY-122,
WAY-123, WAY-135, WAY-137, WAY-138, WAY-139, WAY-140, WAY-143, WAY-165, WAY-166, WAY-219, WAY-267,
WAY-268; each opens at its heading `### WAY-<n> — `. From `foundations/invariants.md`, the invariant
`project-technology-record`. From `foundations/part_map.md`, the entries `project-level` and
`decisions`. From `foundations/glossary.md`, `agent's way to the running product`.

The step's files, whole: `project-level/technology/` — `SKILL.md`, `start.md`, `list.md`,
`running_product.md`, `settle.md`, `research.md`, `close.md`, `task_run.md`, `reserved_choices.md`.
Also `project-level/task/skill/resolve_gaps.md`, and of `project-level/definition_template.md` the
section "Technology".

The-way has no `guidelines/` directory of its own, so no guideline file applies.

The task's source note on the present question about logs, read only if a choice needs its reasons:
`C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\krok_technologii_droga_agenta_do_produktu.md`.

## Your return

Write the report as `task-cycle/spec/design.md` gives, with **Searches not found or unclear**, and
return only: your status, a one-line result and the report's path.
