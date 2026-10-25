# Handoff — reviewer of the return step (review-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You review the return step's commit and made none of the change. Follow the
project skill `the-way-review-change` (read `task-cycle/review/SKILL.md` in this worktree whole, and
what it names). Read only; write only your report, whose first line is `PASS <sha>`, `FAIL <sha>`
or `questions`. Questions go to the orchestrator, never to the human.

## Range and worktree

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`.
- Range: `a2f1165..f3c7f7e` (the return step, one commit).
- Return-step agent's report: `.runs/task-cycles/testing-guidelines/reports/return.md`.
- Your report: `.runs/task-cycles/testing-guidelines/reports/return-review.md`.

## What to review against

- The frozen task `.runs/task-cycles/testing-guidelines/task.md` — Q13 (pytanie 13: "odwrócenie
  operacji, zdanie niezmiennika albo prostsza wersja napisana z wymagania"), row 14, row 16, item 4
  — and its source for Q13: `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/research_wytyczne_testow/raport_wytyczne_testow.md`, section 1.
- The entries the return step writes or corrects: WAY-228 (`### WAY-228 —` in
  `foundations/decisions.md`), WAY-215, and the glossary entry `invariant` it reads against
  (`foundations/glossary.md`); `product-guidelines/testing/template.md` and
  `project-level/task/skill/SKILL.md` where it changed them.
- Step 11 of `task-cycle/skill/SKILL.md` (lines 317–331): what a return step may write.

## Answers of step 4

- Trust boundary: yes (`installation/install.py`), not touched by this range. Irreversible: no.

## Report

Return a short message: the report's first line, its path, and a one-line check result naming what
you ran with exit codes and what you did not run.
