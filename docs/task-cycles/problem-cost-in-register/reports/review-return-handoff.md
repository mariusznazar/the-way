# Handoff — review of the return step's commit, `review-change`

You are a reviewer that did not make this change. Read-only; questions go to the orchestrator.

- Worktree `the task's worktree`.
- Method: the project skill `the-way-review-change`; its entry point sends you to
  `task-cycle/review/SKILL.md`. Read it whole, and a file it names only when the step or variant that
  names it comes. Your variant: the review of the return step's range.
- Range: `e6d05e2..ba2f0dc` (one commit, `ba2f0dc`, one file `process-audit/audit_count.py`, 4 lines
  added and 4 removed, in the paragraph the result prints above the table *Problems by cycle*). The
  return step is the stage in which the author compares the foundation entries the change writes with
  the code and corrects what no longer matches.
- Task, read whole: `.runs/task-cycles/problem-cost-in-register/task.md`. The return step's report:
  `reports/return-step-report.md`. The change it follows already passed two reviews
  (`reports/review-whole-report.md`, `reports/review-fix-report.md`); do not repeat them, but you
  may read them for what they leave open.
- Judge: whether the commit does what the return step says it does and nothing else; whether the
  corrected text is true of the code (a row refused for a cost that is no level); whether the report's
  comparison of the entries with the code (WAY-345, WAY-346, WAY-330, the glossary term, WAY-333,
  WAY-336, WAY-337, WAY-339, WAY-344, the part map entry `process-audit`) misses a mismatch you can
  find. Select your own foundation by the parts of the range (`process-audit`).
- Trust boundary: yes (`process-audit/audit_count.py` is a trust boundary of the part map), but the
  commit changes only text the command prints, no logic. No irreversible operation.
- Run `python -B gate/run_tests.py process-audit` and `python -B elements/common/foundation_check.py`;
  not the whole gate.
- Report to `reports/review-return-report.md`: the first line `PASS <sha>` or `FAIL <sha>`, graded
  findings with scope, checks with command and exit code, **Unread material**, **Searches not found or
  unclear**. Return the first line, a one-line check result and the path.
