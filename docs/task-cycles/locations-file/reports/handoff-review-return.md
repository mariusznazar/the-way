# Handoff — review of the return step's commits (`review-change`)

You did not make this change. Review the return step's commit as `task-cycle/review/SKILL.md`
section 2 gives, against the task and the foundation entries the return step writes or corrects
(read `task-cycle/review/SKILL.md` whole; `fix.md` and `whole_change.md` do not apply).

- Worktree (read-only): the root of the task's worktree, branch
  `task/locations-file`. Range: base `ba36539`, head `2984b5f` (one commit, one decision field).
  Compute `git diff ba36539..2984b5f`; confirm `git rev-parse HEAD` is `2984b5f`.
- Return step report (claims to verify): .runs\task-cycles\locations-file\reports\report-return-step.md
- Frozen task: .runs\task-cycles\locations-file\task.md. Foundation entries to read whole: decision
  WAY-309 (the one edited), WAY-320, WAY-308, and the invariant `tracked-file-private-paths` in
  `foundations/invariants.md`; the decisions' template `elements/decisions/template.md` for the
  *Verification* form. The earlier change (`17b83bf..ba36539`) already passed its review.
- Judge also whether the return step MISSED a mismatch between the foundation entries the change
  writes or changes and the files (part map, the two new files, other entries naming the backlog
  place); name each by its entry.
- Checks you may run: `python -B elements/common/foundation_check.py`,
  `python -B gate/run_tests.py task-cycle`. The full gate is the orchestrator's.
- Report: try `.runs/task-cycles/locations-file/reports/review-return-report.md` once; if the Write tool
  refuses, return the full report as text. First line `PASS 2984b5f` or `FAIL 2984b5f`. Include
  checks with command and exit code, reaches, and **Searches not found or unclear**.
