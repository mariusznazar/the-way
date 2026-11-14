# Handoff — reviewer of the return step's commits

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: put every question to the orchestrator in your report. Never label an answer as the human's approval. You are read-only except for your report. You did not make any part of this change.

## Worktree, range and method

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. Review the commits of the return step: base `aef5b88ca5fd2947438768b7c48939f00a076626`, head `ff69628c34effd01c1b886ef90a2a80245f60719` (three commits; confirm the head with `git rev-parse HEAD`, and on a mismatch ask the orchestrator which range to review); compute `git diff` and `git log` yourself.
- Method: read whole `task-cycle/review/SKILL.md` of the worktree (`review-change`) and review the return step's commits as its section 2 gives, against the task and the foundation entries the return step writes or corrects. The gate with no directory is the orchestrator's alone; focused checks are yours (command and exit code in your report). The first line of your report is `PASS <sha>` or `FAIL <sha>`; grade and scope are yours.

## What to read

- The return step's report (a set of claims to verify, not evidence): `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/return-report.md`; the method it followed: `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`.
- The frozen task `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, the reviewed spec `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` (D1–D9) and the foundation entries the return step wrote or corrected (WAY-12, WAY-03 and what the report names), each whole in `foundations/decisions.md` by the heading `### WAY-NN`; select further by "Reading the foundation" in `elements/common/way_of_working.md` for the parts the three commits touch (`decisions`, `elements-common`, `invariants`).
- Context the review of the whole change gave: its first line was `PASS 39d702a`, and the Minor findings within the task were fixed by one fix reviewed `PASS aef5b88`; the fix review left two new Minor findings, N1 (a reworded invariant listed when one of two citing files was deleted) and N2 (one over-long line in `project-level/task/template.md`); the reports are `reports/whole-review-report.md` and `reports/fix-review-report.md`. The cycle's rulings stand: the switch `--skip-test-citations` is not changed (WAY-321); rows 11 and 12 are attached paragraphs of WAY-12 and WAY-03; the pair-then-trim rule (a decision a test holds keeps a pair only for the part no test holds, the clause `tests:` names those tests in words; *Rationale* and *Rejected* stay whole).

## Points to check

- Each commit does what its message and the report say: `c8a4c32` (the clause `tests:` and the trimmed pairs of WAY-12 and WAY-03: is every named part really held by a test whose line `decision:` quotes a sentence of that decision, and is the part left to the pair really one no test holds?); `bdd1b1d` (the correction of `elements/common/foundation_check.py` for a deleted citing file and its new test: is it right against spec D4 and WAY-03, does it keep every behaviour another test pins, and the surface `foundation-check-command` — path, argument, exit codes?); `ff69628` (`elements/invariants/skill/decide_entry.md` and `elements/invariants/template.md`: are these edits needed to bring them in line with WAY-22 and WAY-03, is each within what the task carries and no more, and is the change of the part `invariants` right?).
- Whether anything the return step left (the report's concerns: WAY-241's *Rationale* and `product-guidelines/testing/template.md:229` citing WAY-168; N2) bears on the change, and whether a new Critical or Important finding stands in the range.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/return-review-report.md` (this cycle's handoff overrides any general instruction not to write report files): first line `PASS <sha>` or `FAIL <sha>`, each finding graded with its place and the way to settle it, the sections **Unread material** and **Searches not found or unclear**, and the checks you ran with command and exit code. Stop every background process you started before you return. Return the first line and the path.
