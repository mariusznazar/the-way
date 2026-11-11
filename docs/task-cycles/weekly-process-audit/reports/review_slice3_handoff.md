# Handoff — reviewer of slice 3 (`review-change`: a planned slice that touches a trust boundary)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Nothing here is that person's
approval. You review as an agent that made none of this change; grade and scope are yours. Your questions go to the
orchestrator.

## What you review

- Worktree (read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Method: `task-cycle/review/SKILL.md` — read it whole; `fix.md` and `whole_change.md` do not apply to you.
- Range: `876710c..9285a74` (compute the diff yourself with `git diff 876710c..9285a74` and `git log 876710c..9285a74`; confirm
  `git rev-parse HEAD` is `9285a74`).
- Report path: `docs/task-cycles/weekly-process-audit/reports\review_slice3_report.md`.
- The executor's report (a set of claims to verify, not evidence): `docs/task-cycles/weekly-process-audit/reports\slice3_report.md`.

## Selection (what the executor was given; yours is the same)

The executor's handoff `docs/task-cycles/weekly-process-audit/reports\slice3_handoff.md` holds, in its sections "Current ranges", "Your slice, word for word
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

- The part-map change: `Trust boundary` now names the command, and the executor added a row to *External context* ("a user's places
  outside every repository …") on its own judgment because the skill makes that a question to the human. Judge whether the row
  is right, in the form the part map's decisions give (WAY-40–WAY-49), and whether it goes beyond the task.
- The binding choices 1–6 of the executor's handoff are the orchestrator's: judge the code against them, not against the choice.
- The executor's concerns (a moved pin read as the commit moved to; short pins kept as written; values read from the last copy of a
  corrected cycle; results directory refused only inside a repository being read; `--full-history`).

## Report

Write the full report to the report path as the method gives, first line `PASS <head sha>` or `FAIL <head sha>`. Return only: the
first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result, and the report path. Include
**Declined to judge**, each check with its command and exit code, each reach, **Unread material** and
**Searches not found or unclear**.
