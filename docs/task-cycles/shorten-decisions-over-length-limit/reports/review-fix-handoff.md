# Handoff — the review of the fix (`review-change`, "the fix of earlier findings")

You are the reviewer of the whole change, resumed; you review the fix range once. Same worktree the root of the task's worktree, read-only, same delegation.

- Method: `task-cycle/review/SKILL.md`, the review of a fix: read `fix.md` beside it as it gives.
- Range: `ef8aa061..644cbe51` (one commit, `644cbe51`); confirm `git rev-parse HEAD` is `644cbe51…`.
- Findings the fix answers: `.runs/task-cycles/shorten-decisions-over-length-limit/reports/review-whole-findings.md` (your Minor 3, within the task; the other two Minor findings are outside the task and not to be fixed).
- The fix report: `.runs/task-cycles/shorten-decisions-over-length-limit/reports/author-fix-report.md` (claims to verify).
- What bounds the review: that the fix answers the finding, changes no word of any entry (compare binding sentences, fields, *Rationale*, *Rejected* of every entry of the log word for word between `ef8aa061` and `644cbe51`, line breaks apart), keeps the blank lines (between the heading and the first paragraph, between paragraphs and before each field), adds no new finding of grade Critical or Important, and leaves `python -B elements/common/foundation_check.py` at exit 0 with `0 errors` and no `listed:` line. No test file changed; no full gate (CI's).
- Report path: `.runs/task-cycles/shorten-decisions-over-length-limit/reports/review-fix-report.md`, first line `PASS <sha>` or `FAIL <sha>`; your working-copy directory `.runs/review-whole/` (you may reuse your comparison script); remove what you make and say so. The same sections as your first report apply: checks with command and exit code, **Unread material**, **Searches not found or unclear**, findings by grade.
- Working copies — the first paragraph of the rule, as in your first handoff: an agent of the cycle that makes a working copy to check something makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository.
