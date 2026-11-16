# Handoff to the reviewer of the fix of the return step

You reviewed the return step (`reports/review-return-report.md`, `FAIL d3068ed`). The one author made one fix for its
blocking finding I-1, cut into `reports/review-return-findings.md` (in
`.runs/task-cycles/audit-answers-contradiction-after-code/`), in your words. Review the fix range once, with
`review-change`, variant "the review of a fix", reading `task-cycle/review/fix.md` as the method says.

- Worktree (read-only for you): `the root of the task's worktree`.
- Range of the fix: base `d3068ed09017a0d0807c9e51d580ec3ba8b64589` to head `1d7d105` (`git rev-parse 1d7d105`): one commit.
- The author's fix report (claims to verify):
  `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-return-fix-report.md`.
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-return-fix-report.md`.
  Your directory for working copies: `.runs/review-return-fix/`.
- Trust boundary: yes (`process-audit/record_items.py`; the author states only docstrings changed — verify it).
  Irreversible operation: no.

Judge whether I-1 is fixed as you worded it: WAY-405's binding sentence and *Verification* and the docstrings must be no
wider than the code, must agree with the tests that cite WAY-405 (`process-audit/test_record_items.py`), keep the start of
the sentence that a test cites by a line `decision:`, and say nothing the human did not accept. A new Critical or
Important finding in the fix counts as one that remains (WAY-162); a Minor finding does not block. Focused checks only
(`python -B elements/common/foundation_check.py` without `--skip-test-citations`,
`python -B gate/run_tests.py process-audit`); **do not run the full gate**. Report each check with command and exit code,
**Unread material**, **Searches not found or unclear** and the line on your working copies (made in
`.runs/review-return-fix/`, removed with `git worktree remove --force` then `git worktree prune`; remainders named with
full path and reason). Return the first line (`PASS <sha>` or `FAIL <sha>`), a one-line check result and the report's path.
