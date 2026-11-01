# Handoff — reviewer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logging-guidelines`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, base `ea4694e`, task branch `task/logging-guidelines`. You make no
  commit and change no file of the repository. You write one file, ignored by Git, your report:
  `.runs/task-cycles/logging-guidelines/reports/spec-review.md`.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **reviewer** of the spec. Read each file
it names when the step that names it comes. You did not write this spec. Your boundary: you return
your report's first line, `PASS` or `FAIL`; you start no later stage.

## What you review

- The spec: `.runs/task-cycles/logging-guidelines/spec.md`.
- The frozen task, read it whole: `.runs/task-cycles/logging-guidelines/task.md`, with
  `Status: ready for cycle`, `Project relation: independent`. Its citations stand at `foundations`
  `ea4694e`, the base.
- The open choices the cycle gave the designer: whether the product's decision on these rules is
  part of the decision adopting the coding template or an entry of its own, with what it holds and
  what a product's log ends up holding; the English words for "przepływ" and "część"; and the form
  of the rules in the template, the "reguła zakresu" of To do 3, the headings, their place, their
  fields and a product's departure. The task's *To do*, its answers to questions 1–12, read with the
  marks of which answer replaces which, and its eight rows of *Settlements to record* are settled; a
  spec that changes one of them is a finding.

**One restriction stands in the task's Context and binds you:** apart from that document, read no
note of the author and no repository of any product. Stay in this worktree's tracked files and the
cycle's directory.

## Answers of step 4

- Trust boundary: no at the start. The spec says no file of the trust boundary changes.
- Operation that cannot be undone: no.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-05, WAY-19, WAY-22, WAY-25,
WAY-27, WAY-30, WAY-33, WAY-86, WAY-95, WAY-100, WAY-104, WAY-134, WAY-135, WAY-161, WAY-165,
WAY-167, WAY-168, WAY-169, WAY-170, WAY-171, WAY-172, WAY-173, WAY-174, WAY-198, WAY-200, WAY-201,
WAY-202, WAY-203, WAY-207, WAY-208, WAY-209, WAY-210, WAY-211, WAY-213, WAY-221, WAY-225, WAY-251,
WAY-268, WAY-270; each opens at its heading `### WAY-<n> — `. Read the log by those ranges, not
whole. From `foundations/part_map.md`, the entries `product-guidelines`, `task-cycle`,
`project-level` and `decisions`. From `foundations/glossary.md`, `critical flow`, `part`,
`guidelines`, `standing check`, `exemplar`, `open design choice`.

Files, whole: `product-guidelines/template.md`, `product-guidelines/reading.md`, every file of
`product-guidelines/coding/`, `product-guidelines/testing/template.md`, `task-cycle/review/SKILL.md`,
`task-cycle/review/whole_change.md`, `elements/decisions/template.md`, `elements/glossary/template.md`,
`project-level/technology/reserved_choices.md`.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Write the report as `task-cycle/spec/review.md` gives, with **Searches not found or unclear**, and
return only its first line and the report's path.
