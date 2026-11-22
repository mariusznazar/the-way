# Handoff — the review of the fix of the findings of the whole-change review

You are the reviewer who reviewed the whole change (same delegation, same worktree
`the worktree root`, same bounds: you did not make the
change, you write nothing in the repository, the person reviews the finished request, you ask no
one). You review the fix once, with `task-cycle/review/SKILL.md` and, for a fix, `task-cycle/review/fix.md`
(read it and follow it: what you read and what bounds the review).

## What is reviewed

- The fix's range: base `ae37fca3310ce6efe7e7939413b8b7a1205b0ead` (the head you reviewed), head
  `41921006168c95b1de449ea546fab2271ec815e9` (`git diff ae37fca3..41921006`, `git log`; five
  commits, 7 files). Confirm `git rev-parse HEAD` is that head.
- The findings the fix answers: `reports/fix-1-findings.md` in the cycle's record directory
  (`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/fix-1-findings.md`) — your four
  Important findings I1–I4 (I2 and I4 marked `Contradiction: yes`) and the Minor finding M1 within
  the task, in your words, which the cycle fixes before the request opens.
- The fix report of the author, a set of claims to verify, not evidence:
  `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-fix-1-report.md`; and the
  author's original report, whose section "Walkthrough" the fix rewrote for I4 (the report is not
  tracked; read it as the file): `reports/author-report.md` of the same directory.
- The frozen task: `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/task.md`, as before.
- Trust boundary: yes (`task-cycle/gate_times.py`, `instruction-files/check_instructions.py`);
  the fix touches the second again (I3).
- The orchestrator notes: for I1 the author wrote the orchestrator's duties into
  `task-cycle/skill/planning.md` and step 9 of `task-cycle/skill/SKILL.md`; for M1 it did not put
  the script's own path into `task-cycle/review/whole_change.md`, since `task-cycle` has no
  dependency on `instruction-files` in the part map, and referred to the README instead. Judge both
  yourself.

## Your bounds

Judge whether each finding is fixed, and whether the fix itself holds anything new that is Critical
or Important. A new Critical or Important finding in the fix counts as one that remains; a Minor
finding that remains or that you find new does not block. Grade and scope are yours.

## Working copies and what you do not read

Your directory for working copies is `.runs/review-fix-1/` of the worktree; the first paragraph of
"Working copies" of `task-cycle/skill/SKILL.md` binds you as it did in the first handoff (a copy only
in that directory, removed by its full path before you return, the report says where each stood and
that it was removed; keep a probe's input and command in `reports/` beside your report). The files
of the cycle's record directory other than those this handoff names are not yours to read.

## Your report

`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/review-fix-1-report.md`; its first line
`PASS <sha>` or `FAIL <sha>`; the sections `review-change` gives, **Unread material**, **Searches not
found or unclear**, each reach beyond what this handoff names and the line on your working copies. If
the harness refuses the write, return the report whole as your answer. Return the first line, the
changed files with their line counts, a one-line check result and the report's path.
