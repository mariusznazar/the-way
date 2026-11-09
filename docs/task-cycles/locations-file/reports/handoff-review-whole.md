# Handoff — review of the whole change (`review-change`, the whole change)

You did not make this change. Review it as `review-change` gives. The person who requested the cycle
delegated every intermediate choice to the orchestrator; ask the human nothing.

## What you review

- Worktree (work from its root, read-only): `the root of the task's worktree`
- Branch `task/locations-file`; **base `17b83bf145653be0beeb43f5fa8175a4197a3700`, head `973ee64`**
  (one commit). Compute the diff yourself: `git diff 17b83bf..973ee64`, `git log 17b83bf..973ee64`;
  confirm `git rev-parse HEAD` is `973ee64` before you go on.
- Method: the project skill `the-way-review-change`; its method file is `task-cycle/review/SKILL.md`
  and, for the whole change, `task-cycle/review/whole_change.md`. Read both whole; read other files
  they name only when the step that names them comes.
- Frozen task, to read whole: `.runs/task-cycles/locations-file/task.md` (independent task,
  `Status: ready for cycle`, accepted 2026-11-08). No spec, no plan: the one-author route.
- The author's report (claims to verify, not evidence):
  `.runs/task-cycles/locations-file/reports/author-report.md`.
- You select your own foundation and guidelines by "Reading the foundation" in
  `elements/common/way_of_working.md`. The product has no `guidelines/`.
- Answers of step 4 of the cycle: trust boundary **no**; irreversible operation **no**. The cycle's
  human action (`~/.the-way/locations.json` exists with the `tasks` entry under `the-way`) is done.
  Do not copy the content of that file, nor any path from it, into your report. You may check that the
  file exists and what keys it has, never print its values.
- Settlements the change must carry: rows 1–3 of *Settlements to record* of the frozen task (marked
  `row <n>` by the author; none is marked `the cycle's`). The author made one autonomous choice the
  task left to the cycle (how the foundation records the new check — a new invariant
  `tracked-file-private-paths`, `outbound-link-reach` staying `review`) and placed the test in
  `task-cycle/` rather than `gate/`; judge both against the task and the foundation.
- Checks already run by the author are in its report. The orchestrator runs the gate
  (`python -B gate/run_tests.py`) after your review; you may run focused checks
  (`python -B gate/run_tests.py <directory>`, `python -B elements/common/foundation_check.py`) and
  name each with its command and exit code.

## Report

The method has you write the full report to
`.runs/task-cycles/locations-file/reports/review-whole-report.md`. If your Write tool refuses a report file
(an earlier agent of this cycle was refused), do not work around it: return the **full report as
text** and the orchestrator saves it. Either way the report's first line is `PASS 973ee64` or
`FAIL 973ee64` (or `questions`), and it holds coverage of every task item and settlement row, the
changed files with line counts, the graded findings (each marked blocking / Minor / outside the
task's scope, with the file and line and the evidence), every check with command and exit code, the
reaches beyond this handoff, and the section **Searches not found or unclear**.
