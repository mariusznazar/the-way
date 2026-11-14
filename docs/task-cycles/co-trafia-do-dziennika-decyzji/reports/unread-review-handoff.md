# Handoff — reviewer of the decisions the review of the whole change left unopened

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator; the human's answer to item 2 of the open request binds this review (`reports/correction-1-remarks.md`, item 2: a fresh reviewer reads whole the 24 decisions the review named as bearing on the change and unopened, and the correction fixes what that reading finds). You have no human to ask: put every question to the orchestrator in your report. You did not make any part of this change and you did not write any earlier review of it. You are read-only except for your report.

## Worktree, range and method

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The change: base `ac753401de0bfaae0b9b8175c10c17387736f8d8`, head `306a122959b3d2e72d76ad3a2d01a2bd1655f9b4` (confirm with `git rev-parse HEAD`; a corrector may add a commit for another remark while you read: your range is `ac753401de0bfaae0b9b8175c10c17387736f8d8..306a122959b3d2e72d76ad3a2d01a2bd1655f9b4`, computed with `git diff` and `git log` by yourself).
- Method: read whole `task-cycle/review/SKILL.md` (`review-change`) and review as an agent reading what stayed unread: the first line of your report is `PASS <sha>` or `FAIL <sha>` for the range's head; each finding is graded Critical, Important or Minor and scoped (within the task or outside it); the report holds **Unread material** and **Searches not found or unclear**. The gate with no directory is not yours; focused checks are (command and exit code in the report), for example `python -B elements/common/foundation_check.py`.

## What to read

Read whole each of these 24 decisions of `foundations/decisions.md`, by the heading `### WAY-NN` (as they stand at the head), with its rationale and *Rejected*: WAY-25, WAY-30, WAY-38, WAY-61, WAY-113, WAY-124, WAY-126, WAY-150, WAY-161, WAY-169, WAY-170, WAY-173, WAY-174, WAY-213, WAY-235, WAY-241, WAY-263, WAY-268, WAY-286, WAY-287, WAY-290, WAY-315, WAY-321, WAY-364. Among them are the rules on the switch of the check of the foundation (WAY-321), on how an invariant's method of checking is written (WAY-61), on what a script does when a file lacks a field (WAY-38; read also WAY-344 whole), on tests of invariants, and on how the log is searched (WAY-150).

Then, for each, judge against the change (read the diff of the range: `elements/common/foundation_check.py` and its tests, `elements/decisions/template.md`, the thirteen decisions edited in place with two attached paragraphs and the decisions WAY-17 and WAY-115 edited by the fix, the skills and templates the change edited, the request and record templates): does any sentence of the decision contradict what the change wrote or changed, or the other way round; does the decision demand something the change leaves undone (a script's behaviour, a template line, a test, a reference); does a number, name or citation of the decision no longer match the entries it points at. Read the change's own entries and files as far as a decision's bearing needs, and name each such reach in your report.

## Context you need

The task and the spec of the cycle, for what the change is for: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md` and `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` (rows of *Settlements to record*, D1–D9). The cycle's rulings, which stand (judge whether one of the 24 decisions contradicts them, not whether you would choose otherwise): the switch `--skip-test-citations` is not changed and skips only the report WAY-321 names; "changed" means a change of a decision's binding sentences; the two new rules are attached paragraphs of two existing decisions; an unknown base writes its line only where the log holds a decision. The earlier reviews: `reports/whole-review-report.md`, `reports/fix-review-report.md`, `reports/return-review-report.md`, `reports/merge-review-report.md`; you need not read them whole, they hold the findings already settled (do not repeat a finding they already state as fixed).

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/unread-review-report.md` (this cycle's handoff overrides any general instruction not to write report files): first line `PASS <sha>` or `FAIL <sha>`; for each of the 24 decisions one line saying whether it was read whole and what its bearing on the change is (none, or the finding); each finding graded with its place and the way to settle it; **Unread material**; **Searches not found or unclear**; the checks you ran. Stop every background process you started before you return. Return the first line and the path.
