# Handoff — reviewer of the reconciliation with the target branch (`review-change`: the reconciliation with the target branch)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Nothing here is that person's approval. You review as an agent that
made none of this change; grade and scope are yours. Your questions go to the orchestrator.

## What you review

- Worktree (read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`; confirm `git rev-parse HEAD` is `8f9be27`.
- Method: `task-cycle/review/SKILL.md` sections 1–4 (the reconciliation with the target branch is reviewed as section 2 gives; not `fix.md`, not `whole_change.md`).
- What happened: the target branch `foundations` moved from `52f8164` to `e9a0f92` (request #102, "a backlog line for the tasks of a plan") while the cycle ran. Commit `897bc0c`
  renumbered the audit's fourteen decisions from WAY-329…WAY-342 to WAY-330…WAY-343, because the target branch took WAY-329 (every reference in the task's files changed with them:
  `foundations/decisions.md`, `process-audit/*`, `task-cycle/cycle_stages.py`, `task-cycle/test_cycle_stages.py`, `task-cycle/skill/SKILL.md`); commit `8f9be27` merges `origin/foundations`
  (`e9a0f92`); the one conflict was in the decision log, where both sides appended entries at the end: the target branch's WAY-329 now stands before the audit's WAY-330…WAY-343.
- Range: `git diff 897bc0c..8f9be27` is what the target branch brought in; `git diff b36014a..897bc0c` is the renumbering. The merge's first parent is `897bc0c`, the second `e9a0f92`.
- Report path: `docs/task-cycles/weekly-process-audit/reports\review_merge_report.md`.

## Question to answer: do the two sides still hold together?

- **The renumbering:** is every reference to an audit decision in the task's files one of the audit's own numbers moved by exactly one, and is no reference to a decision of the target branch (WAY-327, WAY-328,
  WAY-329) changed by it? (Search the task's files for `WAY-32[6-9]` and `WAY-3[3-4][0-9]` and read each hit in its sentence; compare `git diff b36014a..897bc0c`.) Does the decision log still read in order, each decision whole,
  with no half entry at the join? Does the *Relations* of the audit's decisions still name the right decisions?
- **The entries the merge brought in that bear on the parts the change touches:** WAY-329 and the changed WAY-154 and WAY-107 (the backlog place; `project-level/backlog_place.md` now also resolves the entry
  `task-rules`, and `project-level/task_line.md` is new), the root `AGENTS.md` (a new line `Task rules`), and the part map (`foundations/part_map.md`, three lines the target branch changed). The audit's skill
  `process-audit/SKILL.md` finds the user's places by "Resolve an entry of the locations file" in `project-level/backlog_place.md`: does the skill still say what the file now says? Does anything the target
  branch brought collide with an audit decision (the locations file's entries, WAY-320; the entries `problem_register`, `audit_results` and `repository` that WAY-342 names) or with the part map entry of `process-audit`
  and `task-cycle`?
- Run `python -B elements/common/foundation_check.py` (must be 0 errors) and any focused check you need (for example `python -B gate/run_tests.py process-audit`, `python -B gate/run_tests.py elements/part-map`;
  run long commands in the background and wait in stretches under four minutes; the full suite is the cycle's own run).

## Report

Write the full report to the report path, first line `PASS <head sha>` or `FAIL <head sha>`. Include the findings by grade with place, reasoning and evidence; **Declined to judge**; each check you ran as
command and exit code; each reach beyond the dispatch; **Unread material**; **Searches not found or unclear**. Return only the first line, the counts of blocking, Minor and out-of-scope findings,
a one-line check result and the report path.
