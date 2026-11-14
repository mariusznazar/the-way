# Handoff — reviewer of the spec

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: put every question to the orchestrator in your report. Never label an answer as the human's approval.

## Worktree and branch

- Worktree (work from its root): `the root of the task's worktree`; branch `task/co-trafia-do-dziennika-decyzji`, base `ac753401de0bfaae0b9b8175c10c17387736f8d8` (the-way itself; no pin). You are read-only: write only your report.

## Method

Read whole `task-cycle/spec/SKILL.md` of the worktree (`write-spec`), the variant of the reviewer of a spec, and `task-cycle/spec/review.md` when its step comes. You did not write the spec.

## Stage and boundary

Stage: the review of the spec, before any plan or code. The first line of your report is `PASS` or `FAIL`.

## What to review, against what

- The spec: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md`.
- The frozen task, read whole: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md` (12 accepted rows, six answered questions; they are settled, not open).
- Three answers the orchestrator gave the designer as autonomous choices (the spec carries them): the switch `--skip-test-citations` skips only the report WAY-321 names and WAY-321 is unchanged; "a decision the change changes" means its binding part, whitespace-normalised; rows 11 and 12 become attached paragraphs of WAY-12 and WAY-03. Judge whether the spec follows them and whether a wrong one would break the build; do not reopen them as findings merely because you would choose otherwise.
- The foundation entries (in `foundations/decisions.md`, by heading `### WAY-NN`; read each whole): those of the task's *Decisions in play* (WAY-36, 293, 11, 134, 19, 05, 12, 22, 03, 02, 65, 168, 167, 171, 172, 173, 26), WAY-321, WAY-344, WAY-290, WAY-169, WAY-174, WAY-115, WAY-114, WAY-17, WAY-61 and the other decisions the spec lists under "Other decisions of the log the change reaches". Part map: `foundations/part_map.md` whole.
- Gaps the designer's report states, which you decide whether they matter, reading what is needed: (1) it read by title only WAY-41, 52, 53, 84, 85, 89, 101, 102, 103, 104, 121, 122, 123, 137, 138, 165, 166, 267, 270, 322; (2) it made no search of the *Scope* lines for `project-level`, `task-cycle` and `product-guidelines` beyond the entries named; (3) `foundations/invariants.md` was read by grep only: check the invariants whose *Part* names `decisions`, `elements-common`, `project-level`, `task-cycle`, `product-guidelines` or `every`, and those deriving from the changed decisions, against the spec; (4) `task-cycle/request_check.py` read only to its constants: check that the spec's change to what the description names (D4, D7) and its claim that the checker judges no content are right.
- The files the spec names for change, to check each claim the spec makes about them against the real file: `elements/common/foundation_check.py` and its test, `elements/decisions/template.md`, `elements/decisions/skill/decide_entry.md`, `elements/decisions/skill/SKILL.md`, `project-level/task/template.md`, `elements/common/skill/task_variant.md`, `build_table.md`, `task-cycle/skill/return_step.md`, `foundation_step.md`, `request_template.md`, `product-guidelines/template.md`, `elements/common/rules.md`.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/spec-reviewer-report.md` as the method gives it: first line `PASS` or `FAIL`, each finding with the spec's place, why a builder would go wrong, and the way to settle it; the sections **Unread material** and **Searches not found or unclear**. Return the first line and the path.
