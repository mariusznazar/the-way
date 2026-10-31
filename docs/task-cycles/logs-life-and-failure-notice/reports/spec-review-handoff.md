# Handoff — reviewer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logs-life-and-failure-notice`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, base `5d66387`, task branch `task/logs-life-and-failure-notice`.
  You make no commit and change no file of the repository. You write one file, ignored by Git, your
  report: `.runs/task-cycles/logs-life-and-failure-notice/reports/spec-review.md`.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **reviewer** of the spec. Read each file
it names when the step that names it comes. You did not write this spec. Your boundary: you return
your report's first line, `PASS` or `FAIL`; you start no later stage.

## What you review

- The spec: `.runs/task-cycles/logs-life-and-failure-notice/spec.md`.
- The frozen task, read it whole: `.runs/task-cycles/logs-life-and-failure-notice/task.md`, with
  `Status: ready for cycle`, `Project relation: independent`. Its citations stand at `foundations`
  `f86fd71`; the base `5d66387` differs from that commit only in `product-guidelines/coding/**` and
  in two passages of `foundations/decisions.md` outside the entries in play, so its line numbers in
  that file from WAY-219 on moved by about eleven lines.
- The open choices the cycle gave the designer: what a resumed step does with a list written before
  this change, a logs item standing `— held by:` or `— projected:` and a list with no item on how a
  human learns of a failure included; and where the look at that item stands and how the step
  reaches it. The task's *To do*, its answers to questions 1–6 and its four rows of *Settlements to
  record* are settled; a spec that changes one of them is a finding.

**One restriction stands in the task's Context and binds you:** do not open
`C:\Storage\repos\loop2-10x`, the branch `10x/m3l5`, the tag `archive/10x-m3l5` of the repository
`loop2`, or the map of m3l5.

## Answers of step 4

- Trust boundary: no at the start. The spec says no file of the trust boundary changes.
- Operation that cannot be undone: no.

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

## Your return

Write the report as `task-cycle/spec/review.md` gives, with **Searches not found or unclear**, and
return only its first line and the report's path.
