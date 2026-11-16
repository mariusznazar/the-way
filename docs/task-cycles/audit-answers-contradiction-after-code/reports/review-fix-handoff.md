# Handoff to the reviewer of the fix

You reviewed the whole change (`reports/review-whole-report.md`, `FAIL ab2c8c8`). The one author made
one fix for the findings the orchestrator cut into `reports/review-whole-findings.md`, in your words:
I-1 (blocking), M-1 and M-2 (Minor within the task). You review the fix range once, with
`review-change`, variant "the review of a fix": read `task-cycle/review/fix.md` as the method says.

- Worktree (read-only for you): `the root of the task's worktree`.
- Range of the fix: base `ab2c8c801b2ba9170a00ed6056b8b7c56b062868` to head `428cc45` (one commit,
  `git rev-parse 428cc45` for the full identifier).
- The author's fix report (claims to verify, not evidence):
  `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-fix-report.md`.
- The findings: `reports/review-whole-findings.md`, in `.runs/task-cycles/audit-answers-contradiction-after-code/`.
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-fix-report.md`.
  Your directory for working copies: `.runs/review-fix/` (a worktree of the head there if you need one).
- Trust boundary: **yes** (as in the review of the whole change): `process-audit/record_items.py` and
  `process-audit/audit_count.py`. The fix adds a reading of entries under *Discarded attempt*; check
  crafted input at it as before.
- Irreversible operation: no.

## What to judge

1. Whether each of the three findings is fixed, as you worded it. For I-1: the route the orchestrator
   chose is WAY-30's — a proposed narrowing of WAY-344 on the task branch, marked `the cycle's`,
   which the request puts before the human; judge whether the sentence the author wrote states what
   the code does, whether its list of lines and items matches the readers in the code, whether the
   test that cites it holds it, and whether WAY-344 and its dependants (WAY-294 narrows it) still
   agree.
2. The extension for M-1 — one entry for each discarded attempt under *Discarded attempt* — in the
   template, the two paragraphs of `task-cycle/skill/SKILL.md`, `reserved_return.md`,
   `correction.md`, WAY-405, the reading in `record_items.py` and the tests; whether it agrees with
   task *To do* 3 and 6 and question 5 (markers only, no inference from text), and whether any old
   behaviour changed.
3. A new Critical or Important finding in the fix counts as one that remains (WAY-162); a Minor
   finding that remains or is new does not block.

Run focused checks only (`python -B gate/run_tests.py process-audit`, `... task-cycle`,
`python -B elements/common/foundation_check.py`); **do not run the product's full gate**. Report each
check with command and exit code, **Unread material**, **Searches not found or unclear**, and the
line on your working copies (made in `.runs/review-fix/`, removed with `git worktree remove --force`
then `git worktree prune`, remainders named with full path and reason). Return the report's first
line (`PASS <sha>` or `FAIL <sha>`), a one-line check result and the report's path.
