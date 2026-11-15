# Handoff — review of the fix — decisions-log-after-foundation-review

You are the reviewer of the whole change, resumed, to review the fix of your own findings, once.

- Variant of `review-change`: **the fix of earlier findings**; read `task-cycle/review/fix.md` beside `SKILL.md`, as the method's section 1 gives, and follow it.
- Worktree (read-only): `the task's worktree`. Range of the fix: base `dfe14f7` (the head you reviewed), head `cecc49e` (two commits: `03455ed`, `cecc49e`). Compute the diff yourself.
- Findings file the fix was given: `.runs/task-cycles/decisions-log-after-foundation-review/reports/fix-findings.md` (your own report's words: I-1 blocking; M-1…M-6 Minor within the task).
- The author's fix report (claims to verify): `.runs/task-cycles/decisions-log-after-foundation-review/reports/fix-report.md`. It says all seven findings were fixed and none contested, and that its earlier note on the archived copy of M-2 was wrong.
- Per WAY-162, a new Critical or Important finding in the fix fails this review; a Minor finding that remains or is new does not block. Judge whether each of the seven findings is fixed, and whether the fix introduced anything new (a changed word in a rewrap, a line too long, a contradiction with the entries it touches).
- Run `python -B elements/common/foundation_check.py` and the focused tests of the directories the fix changed; no full gate.
- Your directory for working copies: `.runs/review-fix/` under `.runs/` of the worktree (the paragraph of "Working copies" of `task-cycle/skill/SKILL.md` binds you as before).
- Report path: `.runs/task-cycles/decisions-log-after-foundation-review/reports/review-fix-report.md`; first line `PASS <sha>` or `FAIL <sha>`.
