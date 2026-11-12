# Handoff — the return step, the one author resumed

Same delegation, worktree and rules as `reports/author-handoff.md`. No variant row of `make-change`
applies: your stage is the return step of the cycle.

- Worktree `the task's worktree`, branch
  `task/problem-cost-in-register`, head `e6d05e2` (base `55afa8e`; the change is the range
  `55afa8e..e6d05e2`: your commits `f5e1d45`, `18b4a3f` and the fix `e6d05e2`). Both reviews passed:
  `reports/review-whole-report.md` and `reports/review-fix-report.md`.
- Read, whole: `task-cycle/skill/return_step.md` (the method of this stage) and
  `task-cycle/skill/foundation_step.md` (the return step writes as the foundation step writes); and
  the skill of an element when you write an entry of it.
- The frozen task: `.runs/task-cycles/problem-cost-in-register/task.md`.
- The change as it stands now is the thing to compare with the foundation entries it writes or edits
  (WAY-345, WAY-346, WAY-330, the glossary term `cost of an occurrence`), those the task names (WAY-328,
  WAY-333, WAY-336, WAY-337, WAY-339, WAY-344) and the part map entry of `process-audit`. Correct in
  the same change whatever no longer matches; write an invariant only for a rule the task, a decision
  or the human sets.
- One thing to compare in particular, from the review: the reviewer's Minor finding 4 (the exit code
  1 for a missing or doubled level of *Weights* and *Costs of an occurrence* where WAY-344 counts "a
  row label" as a field). The task mandates the exit 1; it is outside the task's scope and goes to
  the request's list. Do not change code for it; if the foundation says something that disagrees with
  what the code does, correct the foundation entry you wrote, not the code, and say so.
- If the return step commits anything, commit by path, and the reviewer will review that range. If
  nothing no longer matches, commit nothing.
- No whole gate (`python -B gate/run_tests.py` with no argument); the orchestrator runs it once.
  Run `python -B elements/common/foundation_check.py` and the tests of any directory you change.
- Report: `reports/return-step-report.md` with the sections of the return step in
  `task-cycle/record_template.md` (*Return step*): foundation compared with code, decisions written
  or changed, invariants, environment facts, glossary terms, part-map changes, projected entries,
  rows of *Settlements to record* written — and **Unread material**, **Searches not found or
  unclear**, checks with command and exit code. Return status, commits, check result and the path.
