# Handoff — review of the return step's commits

You review, as an agent that did not make them, the commits of the return step of a the-way task
cycle (`implement-task`). Read-only: change no file of the worktree, commit nothing.

- Worktree: `.`, branch
  `task/cycle-no-private-names`.
- Range: base `a5ea36f` to head `b241bb0` (one commit, `b241bb0`, touching `foundations/decisions.md`
  only). Compute the diff yourself (`git diff a5ea36f..b241bb0`) and confirm `git rev-parse HEAD`.
- Your method: `task-cycle/review/SKILL.md` in this worktree, whole; the return step's commits are
  reviewed as its section 2 gives, against the task and the foundation entries the return step
  writes or corrects.
- The frozen task, whole: `.runs/task-cycles/cycle-no-private-names/task.md`. The return step's own
  rule: `task-cycle/skill/return_step.md`.
- The author's report (claims to verify): `.runs/task-cycles/cycle-no-private-names/reports/return-report.md`.
- Foundation entries by identifier, each whole (from its heading to the next `###`): WAY-308, WAY-309
  (the entries the return step corrects), WAY-294, WAY-295, WAY-27, WAY-153; the invariants
  `outbound-link-reach` and `project-plan-state-evidence`. The code the entries are compared with:
  `task-cycle/skill/SKILL.md` section "The record before it is committed",
  `task-cycle/skill/request_template.md`, `task-cycle/record_template.md`,
  `task-cycle/private_paths_check.py`.
- Check: whether the two corrections say what the files do (the request tells the human of a cleaned
  relation line; the order of the two checks and the single rewriting), whether they add a rule the
  task or the accepted rows do not carry beyond what is marked `the cycle's`, whether the entries stay
  consistent with each other and with WAY-294/WAY-295, and whether `foundation_check.py` still holds.
  Orchestrator's note: the previous reviews passed the code at `a5ea36f`; do not re-review it.
- Focused checks only (no full gate). Give each command and exit code.
- Your report: `.runs/task-cycles/cycle-no-private-names/reports/return-review-report.md`; first line
  `PASS <sha>` or `FAIL <sha>`; with **Searches not found or unclear** (`none` is an answer). Return the
  first line, the report path and the files changed with line counts. Grade and scope are yours.
