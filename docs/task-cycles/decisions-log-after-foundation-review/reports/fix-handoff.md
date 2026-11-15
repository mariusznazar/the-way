# Handoff — the fix of a review's findings — decisions-log-after-foundation-review

You are the one author, resumed. The review of the whole change returned `FAIL dfe14f7`.

- Your variant of `make-change`: **the fix of a review's findings** (`task-cycle/change/SKILL.md`; read `fix.md` beside it, as its table says).
- Worktree: `the task's worktree`, branch `task/decisions-log-after-foundation-review`, reviewed head `dfe14f7`. The fix's range runs from `dfe14f7`. Do not reset, rebuild or rewrite the six existing commits; add new commits on top. Do not push.
- Findings file: `.runs/task-cycles/decisions-log-after-foundation-review/reports/fix-findings.md` (the reviewer's words from `reports/review-whole-report.md`): one blocking finding (I-1) and six Minor findings within the task (M-1 … M-6). Fix all seven; the Minor ones are fixed in this one fix (WAY-161).
- A finding you hold wrong, you answer with evidence in the report instead of changing the text; you do not skip one silently. Fix lines you rewrap to the width of their neighbouring lines and change no word where a finding asks only for a rewrap; after the fix compare words of the entries you rewrap with `git diff --word-diff` to show that no word changed.
- Run the affected checks again: `python -B elements/common/foundation_check.py` (exit code in the report), the focused `python -B gate/run_tests.py <directory>` of each directory a file you change lies in. No full gate (the orchestrator's run).
- Directory for working copies: `.runs/fix/` under `.runs/` of the worktree; the paragraph of "Working copies" of `task-cycle/skill/SKILL.md` binds you as before: remove each copy before you return and state it in the report.
- Report path: `.runs/task-cycles/decisions-log-after-foundation-review/reports/fix-report.md`: status, the new commits, each finding with how it was fixed (or your evidence), checks with command and exit code, the own-work check, **Unread material**, **Searches not found or unclear**, reaches beyond this handoff, working copies.
