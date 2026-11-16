# Handoff — review of the fix of the Minor findings

## Delegation

As in `reports/review-whole-handoff.md`, which you already know: you review as an agent that made none of the change; grade and scope of
every finding are yours; you ask no human anything.

## What you review

- Variant of `task-cycle/review/SKILL.md`: "the fix of earlier findings"; read `task-cycle/review/fix.md`, which the skill names, whole,
  and follow it.
- Worktree `the root of the task's worktree`, branch `task/script-invariants-by-test`. You change nothing in it.
- Range of the fix: base `4bc1667c` (the head you reviewed) to head `540aed04`; compute the diff yourself (`git diff 4bc1667c..540aed04`)
  and confirm `git rev-parse HEAD`.
- The findings the fix answers: `reports/fix-findings.md` (the four Minor findings M1-M4 of your own report, cut in your words), under
  `docs/task-cycles/script-invariants-by-test/`.
- The author's fix report: `docs/task-cycles/script-invariants-by-test/reports/author-fix-report.md` — claims to verify, not evidence.
- Notable in the fix: the file of the three script tests moved from `elements/part-map/` to `agent-instructions/` (M3); a new list
  `PLACES` for the kind `.yml` (M1); `missing()` of `elements/common/test_element_directory_contents.py` now returns pairs (M2); the
  message of a missing `.python-version` (M4). The author did not repeat the manual break of `element-directory-contents` after rewriting
  `missing()` and did not rerun the moved `script-imports` test on Python 3.12: judge whether those need to be repeated by you.
- Your working copies stay in `.runs/review-whole/` (your own directory); remove them before you return.
- Your report: `docs/task-cycles/script-invariants-by-test/reports/review-fix-report.md`; first line `PASS <sha>` or `FAIL <sha>`.
- A new Critical or Important finding in the fix fails this review; a Minor finding that remains or is new does not block and is listed.
- You run no full gate (WAY-160); the focused directories (`elements/part-map`, `agent-instructions`, `elements/common`) and
  `python -B elements/common/foundation_check.py` you may run.
