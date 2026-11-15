# Handoff — the fix of the review's findings of slice 4

You are the executor of slice 4, resumed for the one fix a review allows. The delegation, the
worktree, your directory for working copies (`.runs/executor-4/`), the identifiers of the entries and
the rules of your first handoff (`reports/executor-4-handoff.md`) stand.

- Variant of `task-cycle/change/SKILL.md`: **"the fix of a review's findings"**; read `task-cycle/change/fix.md` where the skill names it.
- Findings file: `reports/slice-4-findings.md` (the reviewer's blocking finding word for word; its full report is `reports/review-4-report.md`). Fix the one blocking finding: in the reading of the Codex rollout in `task-cycle/cycle_stages.py`, make required, with exit code 2 and the file/line/field message of the same helpers, the `thread_id` and the `turn_id` of a token record, `session_meta.payload.id` (both reads) and the `timestamp` of a line (a value that is no time ends with exit 2 as well, not `ValueError`/`TypeError`), one more test each, failing before and passing after, each with its command and exit code. The reviewer's evidence you may check: where you hold a finding wrong, answer with evidence instead of changing code. The fields the reviewer lists as a documented fallback stay as they are. Do not fix the Minor findings (they are not in the findings file).
- Range of the fix: from `ced0fd9`; commit by path, message in English.
- Affected checks: `python -B task-cycle/test_cycle_stages.py`, the audit test `python -B process-audit/test_audit_count.py Cost.test_the_stage_report_cycle_stages_writes_gives_the_share`, ruff on the two files, `python -B elements/common/foundation_check.py --skip-test-citations`; never the full gate.
- Report: `reports/executor-4-fix-report.md`, with the sections of your first report (status, commits, checks with command and exit code, **Unread material**, **Searches not found or unclear**, working copies).
