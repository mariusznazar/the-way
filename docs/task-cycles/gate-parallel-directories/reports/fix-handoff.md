# Handoff — the fix of a review's findings

You are the author of this change, resumed for the fix. Variant of `make-change`: "the fix of a
review's findings" (read `task-cycle/change/fix.md` where the variant names it).

- Worktree and branch: as in `reports/author-handoff.md` (a worktree path as there); head now `264703f`.
- Findings file, read whole: `reports/whole-review-findings.md` — the five Minor findings within the task
  of the review of the whole change (`reports/whole-review-report.md`, `PASS 264703f`). No blocking finding.
  Finding 6 of the report (the audit's series) is outside the task and is not fixed.
- Your report: `docs/task-cycles/gate-parallel-directories/reports/fix-report.md`

## What the orchestrator decides for each finding

1. Fix as the reviewer proposes: on an interrupt cancel the queued directories
   (`shutdown(wait=True, cancel_futures=True)` or the equivalent), and add a test that fails without the fix
   (a short one — it must not wait on long sleeps and must not make the `gate` directory slower by more than
   a few seconds).
2. Fix `task-cycle/record_template.md:100`: `gate_times.md` is created by the first gate run of the cycle,
   which is the run of step 2 where the pin moved, else the run of step 4, and where step 4 skips the run, the
   run of step 10. Keep the sentence short.
3. Fix the wording of step 4: the path `docs/task-cycles/<task-slug>/cycle.md` is the merged branch's copy, so
   name it as that (not as this cycle's `<task-slug>`), and add the `git log` recipe your own check used
   (`git log --diff-filter=A --name-only --format=%h <base>^1..<base>^2 -- docs/task-cycles`) so a reader can
   find the copy. Stay within the task's item 4.
4. Widen the margin of the rendezvous tests so that a slow start of a sibling process does not fail them: raise
   the wait several times over (for example to 120 s), keeping a test that does not meet its sibling failing
   with its message. Do not make a passing run slower.
5. Re-wrap the lines the change left uneven in the places the finding names, to the width of their neighbours.
   Change no word.

After the fix: run the affected focused checks (`python -B gate/run_tests.py gate`, `... task-cycle`,
`python -B elements/common/foundation_check.py`, and the directories of any other file you touch) and report
their commands and exit codes. Do not run the full gate. Commit by path, English message. Report as the
method gives, with **Unread material** and **Searches not found or unclear**.
