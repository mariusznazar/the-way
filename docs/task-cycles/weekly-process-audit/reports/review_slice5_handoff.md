# Handoff — reviewer of slice 5 (`review-change`: a planned slice that touches a trust boundary)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Nothing here is that person's
approval. You review as an agent that made none of this change; grade and scope are yours. Your questions go to the
orchestrator.

## What you review

- Worktree (read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Method: `task-cycle/review/SKILL.md` — read it whole; `fix.md` and `whole_change.md` do not apply to you.
- Range: `9cf2633..c2a0169` (compute the diff yourself with `git diff 9cf2633..c2a0169` and `git log 9cf2633..c2a0169`; confirm
  `git rev-parse HEAD` is `c2a0169`).
- Report path: `docs/task-cycles/weekly-process-audit/reports\review_slice5_report.md`.
- The executor's report (a set of claims to verify, not evidence): `docs/task-cycles/weekly-process-audit/reports\slice5_report.md`.

## Selection (what the executor was given; yours is the same)

The executor's handoff `docs/task-cycles/weekly-process-audit/reports\slice5_handoff.md` holds, in its sections "Current ranges", "Your slice, word for word
from the plan", "The plan's Foundation entries" and "Notes of the orchestrator", the passages, entries and binding choices the
slice was made against. Read those sections; ignore its instructions addressed to the executor. Read each foundation entry it
names by identifier whole, at the ranges it gives. You judge the slice against the task passages it names
(`.runs/task-cycles/weekly-process-audit/task.md`), not the plan alone.

## Risk and answers of the start

- Trust boundary: **yes** — `process-audit/audit_count.py` reads from outside the repository the cycle records and `stages.md`
  of repositories the user names (through git history), the user's locations file, the user's register of problems and the
  results directory. Check hostile input at it: control characters and escape sequences in a record, a record path that leaves its
  directory, symlinks, a malformed or oversized table, a missing or doubled field, a locations file with wrong types or an
  entry that points inside a repository or to a place that must not be written, git options injected through a name or a
  commit (a value that starts with `-`), output that could break a Markdown table or pass for another row, and what the
  command may run (invariant `script-subprocesses`).
- Irreversible operation: no.
- Product guidelines: the-way has none.

## Also check in this slice

- Judge the code against the orchestrator's binding choices 1–7 in the executor's handoff (section "Notes of the orchestrator"), not against the
  choices themselves. The executor reports it read "an `Error:` of the register" for a missing table as exit 1 (written result) instead of exit 2;
  say whether that departs from the binding choice 1 and whether it is a defect.
- Lessons of the earlier trust-boundary reviews of this cycle (slices 3 and 4 failed on them): backtracking patterns, unguarded number or date
  conversions, cells not through `cell()`, no size cap, a failure of one row aborting the run, a value from the register given to git as an option
  (`--end-of-options`), a short hash that is ambiguous. Check each in the new code, with crafted registers (a name with a bar, control characters,
  a 4 MiB table, a doubled header, a `Fix` of a commit not in the-way's history, a pin `unknown`, an issue name in no row, a problem whose
  *Record* is a commit of another repository).
- No ranking and no priority from the number of returns: confirm the order of the result is the register's.
- The result's day of the run (`--today`): check that the same input and `--today` give the same bytes, and that the dated file name is chosen
  without a value from the register.

## Report

Write the full report to the report path as the method gives, first line `PASS <head sha>` or `FAIL <head sha>`. Return only: the
first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result, and the report path. Include
**Declined to judge**, each check with its command and exit code, each reach, **Unread material** and
**Searches not found or unclear**.
