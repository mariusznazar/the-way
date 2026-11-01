# Handoff — reviewer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/guidelines-audit-report`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, base `2f51e6c`, task branch `task/guidelines-audit-report`. You make
  no commit and change no file of the repository. You write one file, ignored by Git, your report:
  `.runs/task-cycles/guidelines-audit-report/reports/spec-review.md`.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **reviewer** of the spec. Read each file
it names when the step that names it comes. You did not write this spec. Your boundary: you return
your report's first line, `PASS` or `FAIL`; you start no later stage.

## What you review

- The spec: `.runs/task-cycles/guidelines-audit-report/spec.md`.
- The designer's report, for the readings it asks a reviewer to look at first:
  `.runs/task-cycles/guidelines-audit-report/reports/designer.md`.
- The frozen task, read it whole: `.runs/task-cycles/guidelines-audit-report/task.md`, with
  `Status: ready for cycle`, `Project relation: independent`. Its citations stand at `foundations`
  `2f51e6c`, the base. Read no skill of the course it names and no note of the author beyond it.
- The open choices the cycle gave the designer: the English words of the four grades; how the audit
  shows the cost of a fix; the English words for a finding of an audit and for a cause, and what
  happens to `charge`; whether rows 1–6 enter as one decision, as changes of WAY-187, WAY-201 and
  WAY-250, or as several entries; who merges the causes of a task joining code and tests, at which
  step; and where each result stands in the task document, with the form of the list. The task's
  *To do*, its answers to questions 1–9 and its six rows of *Settlements to record* are settled; a
  spec that changes one of them is a finding.

## Answers of step 4

- Trust boundary: no at the start. Where the spec changes a file the part map names as one, it says
  so.
- Operation that cannot be undone: no.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-05, WAY-14, WAY-19, WAY-22,
WAY-24, WAY-25, WAY-26, WAY-27, WAY-29, WAY-30, WAY-33, WAY-36, WAY-51, WAY-100, WAY-114, WAY-120,
WAY-134, WAY-135, WAY-161, WAY-172, WAY-173, WAY-174, WAY-178, WAY-185, WAY-187, WAY-198, WAY-199,
WAY-200, WAY-201, WAY-204, WAY-205, WAY-206, WAY-207, WAY-215, WAY-216, WAY-235, WAY-247, WAY-250,
WAY-251, WAY-256, WAY-265, WAY-266; each opens at its heading `### WAY-<n> — `. Read the log by those
ranges, not whole. From `foundations/part_map.md`, the entries `product-guidelines`, `project-level`
and `decisions`. From `foundations/glossary.md`, `critical flow`, `exemplar`, `guidelines`, `part`,
`standing check`, `open design choice` and any entry on a grade or a blocking finding you find by
search. From `foundations/invariants.md`, those whose *Part* names `product-guidelines` or `every`,
as far as the work reaches them.

Files, whole: `product-guidelines/reading.md`, and of `product-guidelines/coding/`,
`product-guidelines/styleguide/` and `product-guidelines/testing/` each `SKILL.md`, `settle.md`,
`hand_back.md`, `task_document.md`, `orchestrated_mode.md`, `recognize.md`; `coding/kinds.md`,
`coding/trial_run.md`, `styleguide/audit.md`, `testing/audit.md`, `testing/new_level.md`;
`project-level/task/template.md`, `project-level/task/skill/SKILL.md`,
`project-level/task/skill/guideline_findings.md`, `project-level/task/skill/orchestrated_mode.md`,
`elements/common/critique/SKILL.md`, `task-cycle/review/SKILL.md` (for its grades only),
`task-cycle/skill/foundation_step.md`, `elements/decisions/template.md`,
`elements/glossary/template.md`.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Write the report as `task-cycle/spec/review.md` gives, with **Searches not found or unclear**, and
return only its first line and the report's path.
