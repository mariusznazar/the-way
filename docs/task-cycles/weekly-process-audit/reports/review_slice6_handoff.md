# Handoff — reviewer of slice 6 (`review-change`: a planned slice that touches a trust boundary)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Nothing here is that person's
approval. You review as an agent that made none of this change; grade and scope are yours. Your questions go to the
orchestrator.

## What you review

- Worktree (read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Method: `task-cycle/review/SKILL.md` — read it whole; `fix.md` and `whole_change.md` do not apply to you.
- Range: `7bb25c3..2e7168c` (compute the diff yourself with `git diff 7bb25c3..2e7168c` and `git log 7bb25c3..2e7168c`; confirm
  `git rev-parse HEAD` is `2e7168c`).
- Report path: `docs/task-cycles/weekly-process-audit/reports\review_slice6_report.md`.
- The executor's report (a set of claims to verify, not evidence): `docs/task-cycles/weekly-process-audit/reports\slice6_report.md`.

## Selection (what the executor was given; yours is the same)

The executor's handoff `docs/task-cycles/weekly-process-audit/reports\slice6_handoff.md` holds, in its sections "Current ranges", "Your slice, word for word
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

- The executor's report says it did not read WAY-334, WAY-336 and WAY-338 (the decisions this slice implements: whether a fix works, the cost of a cycle,
  when measures stop being comparable). Read WAY-336 and WAY-338 whole yourself and judge the code against them; this closes that gap.
- Judge the code against the orchestrator's binding choices 1–7 (executor's handoff, "Notes of the orchestrator"). The executor asks four questions
  (its report): (1) a new price list as a unit test of `series_boundary` instead of a subprocess test; (2) the conservative series rule gives 20 series
  for 53 versions of the-way's own history, so the third question is `unknown` everywhere; (3) the planned-slices count read as exactly one standalone
  figure before the word `slices`; (4) the sums of the second question cover only the cycles whose plan reads, shown as `k of m`. Say whether each
  reading is sound or a defect.
- Lessons of the earlier trust-boundary reviews: backtracking patterns, unguarded number/date conversions (the committer date of a pin, medians with
  `Decimal`), cells not through `cell()`, no size cap, a failure of one cycle or version aborting the run, a value given to git as an option, a refused or
  unreadable value shown as zero, quadratic grouping over many cycles or versions. Check each with crafted records (a *Plan* item with a huge integer,
  a *Discarded attempt* with control characters, a pin whose commit date is out of range, 10,000 cycles with distinct pins).
- Whether the result can compare numbers of two series directly anywhere (WAY-338).

## Report

Write the full report to the report path as the method gives, first line `PASS <head sha>` or `FAIL <head sha>`. Return only: the
first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result, and the report path. Include
**Declined to judge**, each check with its command and exit code, each reach, **Unread material** and
**Searches not found or unclear**.
