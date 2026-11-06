# Handoff — review of the return step

You review the return step of one task as an agent that did not make it, and did not review the
change before. You are read-only: change no file of the worktree, commit nothing.

- Worktree (work from its root): `C:\Storage\repos\the-way\.runs\worktrees\logging-scope-decision-section`,
  branch `task/logging-scope-decision-section`. Do not touch `.runs/gate-check` or `.runs/gate-check-2`,
  checkouts the orchestrator runs the whole gate in.
- Method: `task-cycle/review/SKILL.md` of this worktree; read it whole, and the file it names for this
  dispatch as it directs. Your dispatch: **the return step's range**.
- Range to review: `f604e93b024ce0eb9d0f70895b69331c3fbfe2e3..87377b2` (one commit, `87377b2`,
  `task-cycle/skill/request_template.md`). The earlier range `61c72fb..f604e93` was reviewed by another
  agent (`FAIL fa445fd`, one fix, `PASS f604e93`); you review only the return step's own change and its
  report, against the task and the entries the return step writes or corrects.
- Frozen task, whole: `.runs/task-cycles/logging-scope-decision-section/task.md`. No spec, no plan; the
  route is one author without a plan. Answers of the start: no trust boundary, no irreversible
  operation.
- The return step's report: `.runs/task-cycles/logging-scope-decision-section/reports/06-return-step-report.md`.
  Judge in particular (1) whether the two sentences it changed in the template (the rule at the head of
  *The skeleton* and the line at the head of *The variants*) are right against the template's own
  skeleton, `task-cycle/request_check.py` and the task's item 5; (2) its reading that WAY-286's
  *Verification* ("a section with nothing in it is left out" as a violation) is compatible with an
  own-sections heading omitted where the task has none, and whether that needs a decision of the human
  instead of a return-step edit; (3) whether the return step missed any entry to write or correct.
  The foundation entry WAY-287 was written in the earlier range; you need not re-review it.
- You may run focused checks (`python -B gate/run_tests.py task-cycle`,
  `python -B elements/common/foundation_check.py`), each reported with command and exit code. The whole
  gate is the orchestrator's.
- Write the full report to `.runs/task-cycles/logging-scope-decision-section/reports/07-return-review-report.md`; its
  first line is `PASS <sha>` or `FAIL <sha>`. Include grades (Critical, Important, Minor, outside the
  task's scope) and **Searches not found or unclear**. Return that first line, a one-line check result
  and the report path.
