# Handoff — review of the reconciliation with the target branch

You review the merge of the target branch into a task branch as an agent that made none of it. You are
read-only: change no file of the worktree, commit nothing.

- Worktree (work from its root): `C:\Storage\repos\the-way\.runs\worktrees\logging-scope-decision-section`,
  branch `task/logging-scope-decision-section`. Do not touch `.runs/gate-check` or `.runs/gate-check-2`.
- Method: `task-cycle/review/SKILL.md` of this worktree; read it whole and the file it names for this
  dispatch as it directs. Your dispatch: **the reconciliation with the target branch**.
- What happened: `foundations` moved on the remote from `61c72fb` to `24268b2` (merged pull requests #72 and
  #73: WAY-293 to WAY-296, a new `task-cycle/remarks_check.py`, changes to `task-cycle/skill/SKILL.md`,
  `record_template.md` and others) while the task branch was made. The orchestrator merged
  `origin/foundations` (`24268b2`) into the task branch: merge commit `23bb052`, first parent `87377b2` (the
  reviewed change and its return step), second parent `24268b2`. One conflict, in
  `task-cycle/skill/request_template.md`: both sides added an item 10 to the list of *For you to decide*. The
  orchestrator kept the target's item (the listing of the remarks check held wrong, WAY-295) as item 10, and
  moved the task's item (additions to a product's logging scope) to 11, because the task says the numbers of
  existing items do not change.
- Range: `87377b2..23bb052` is what the merge brought into the task branch (it is large; most of it is the
  target's own already-merged work and not yours to judge). Judge: the conflict's resolution; that the
  change the task carries (`61c72fb..87377b2`, reviewed earlier: `PASS f604e93`, `PASS 87377b2`) is intact
  in the merged tree (`git diff 24268b2 23bb052` shows exactly the task's change on top of the target);
  that the merged files agree with each other (the list of items in `request_template.md`, WAY-287's list of
  kinds, `request_check.py` and its tests); and whether anything the target brought now needs a change in
  the task's work — for instance, WAY-287's list of kinds does not name the target's item 10, which the task
  did not ask to change; say whether you hold that a finding of the task or outside its scope.
- Frozen task, whole: `.runs/task-cycles/logging-scope-decision-section/task.md`. Route: one author without a
  plan. No trust boundary, no irreversible operation.
- You may run focused checks (`python -B gate/run_tests.py task-cycle`,
  `python -B elements/common/foundation_check.py`), each with command and exit code. The whole gate is the
  orchestrator's and runs on the merged tree.
- Write the full report to `.runs/task-cycles/logging-scope-decision-section/reports/08-merge-review-report.md`; its
  first line is `PASS <sha>` or `FAIL <sha>`. Grade findings (Critical, Important, Minor, outside the task's
  scope) and include **Searches not found or unclear**. Return that first line, a one-line check result and
  the report path.
