# Handoff — the review of the reconciliation with the target branch, `review-structure-form-class`

## Delegation

You review, as an agent that did not make it, the merge of the target branch into the task branch of one the-way task cycle. The orchestrator of the
cycle is the one you ask; no human answers during the cycle. You change nothing.

## Where

- Worktree (read-only for you): `the worktree's root`; confirm `git rev-parse HEAD` is `3e934b6`.
- Range to review: `b596eec..3e934b6`, two commits on `task/review-structure-form-class`:
  - `c756236` renumbers the decisions this branch wrote, WAY-355 to WAY-360, as WAY-360 to WAY-365, in 12 files (35 places), because
    `origin/foundations` (`8079485`) gained its own WAY-355 to WAY-359 while the task ran;
  - `3e934b6` merges `origin/foundations` (`8079485`, merged base `65b6d70`); the one conflict, in `foundations/decisions.md` (both sides
    appended at the end of the log), is resolved by keeping the target branch's WAY-355 to WAY-359 first and this branch's WAY-360 to WAY-365 after.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/review-merge-report.md`; its first line is
  `PASS 3e934b6`, `FAIL 3e934b6` or `questions`.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it for "the reconciliation with the target branch". The question of this dispatch: do the two sides
still hold together? Judge the whole change as it stands on the merged tree against the frozen task
(`docs/task-cycles/review-structure-form-class/task.md`, Polish) only where the merge could have changed the answer; the change itself was reviewed
(`reports/review-whole-change-report.md`, `reports/review-fix-report.md`, `reports/review-return-step-report.md`) and is not to be reviewed again.

## What to check

1. The renumbering: every use of the old numbers that meant this branch's entries now carries the new one, and no use of WAY-355 to WAY-359 in this
   branch's files (`git diff 65b6d70..b596eec --name-only` lists them) means one of this branch's entries; WAY-360 to WAY-365 are this branch's six
   entries in the order of their old numbers (old 355 = new 360 … old 360 = new 365); WAY-353 and WAY-354 stay (an earlier cycle's). Compare with
   `git diff b596eec c756236`: only the numbers change.
2. The conflict's resolution: `git diff b596eec 3e934b6 -- foundations/decisions.md` must hold the target branch's additions and nothing of this branch's, and
   `git diff 8079485 3e934b6 -- foundations/decisions.md` this branch's six entries (renumbered) and the in-place edits of WAY-229 and WAY-164, and nothing else.
   `python -B elements/common/foundation_check.py` must exit 0.
3. Whether this branch's text still holds against what the target branch brought: the entries that came in and bear on the parts this change touches
   (`task-cycle`, `product-guidelines`, `decisions`) are WAY-355, WAY-356, WAY-357, WAY-358 and WAY-359 (defects found after a merge: the line `Defect introduced by`
   of the task document, the record's item for corrections, kind 17 of the request template, the register of problems) and the in-place addition to WAY-287;
   files: `task-cycle/record_template.md`, `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md`, `project-level/task/template.md`,
   `project-level/task/skill/draft.md`, `process-audit/problem_register.md`, `task-cycle/test_remarks_check.py`, `process-audit/test_audit_count.py`.
   Read each of those entries whole. Does a sentence of this branch's entries or files contradict one of them, or restate it differently
   (for example a list of what the request or the record carries that now lacks an item)?
4. Run `python -B elements/common/foundation_check.py` and `python -B gate/run_tests.py task-cycle`, each with command and exit code (the orchestrator
   ran `task-cycle` 385 tests, `process-audit` 180 tests, both exit 0, and runs the whole gate itself; do not run it).

## Boundaries

- Read-only. Your report holds each finding graded as the skill gives, marked within or outside the task, **Unread material** and **Searches not found or
  unclear** (each `none` where there is nothing). A Minor finding here is not fixed in this cycle; it goes to the request's list. Return the first line,
  the counts of blocking, Minor and out-of-scope findings, a one-line check result and the path of the report.
