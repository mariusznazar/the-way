# Handoff — review of the fix (resume of the whole-change reviewer)

Review the fix of your findings once, as `task-cycle/review/fix.md` gives (read it now).

- Worktree (read-only, from its root): `the task's worktree root`. Fix range: `6349019187409079f93cc41bf3f39df9d90b1adb..HEAD` (compute with `git diff 6349019..HEAD` and `git log`; HEAD should be `75fe0e3`; confirm).
- The findings the fix answers: `.runs/task-cycles/cycle-technology-decisions-batch/reports/16-fix-findings.md` (your blocking findings 1–2 and Minor 1–4, 6–8, in your words). The fix report (claims to verify, not evidence): `.runs/task-cycles/cycle-technology-decisions-batch/reports/17-fix-report.md`.
- The fix may not touch WAY-298 or any decision; its report names a remaining wording difference between step 4 of `task-cycle/skill/SKILL.md` and WAY-298's last sentence — judge whether it is a finding of the fix (grade it).
- Trust boundary: yes (`project-level/plan_state.py`, Minor 1–3 of your findings touch it): crafted input again.
- Bounds (fix.md): a new Critical or Important finding in the fix counts as remaining; a Minor finding that remains or is new does not block. You may run focused checks only (never the whole gate).
- Report: `.runs/task-cycles/cycle-technology-decisions-batch/reports/18-fix-review-report.md`, first line `PASS <sha>` or `FAIL <sha>`, with **Searches not found or unclear**. Return the first line, a one-line check result and the report path.
