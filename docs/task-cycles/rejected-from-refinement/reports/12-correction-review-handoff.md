# Handoff — review of a correction, task `rejected-from-refinement`

## Delegation

Mariusz asked this session to carry the accepted task through the-way's task cycle to a reviewable
pull request into `foundations`; the request https://github.com/mariusznazar/the-way/pull/53 is
open and he asked for a correction. You review that correction as an agent that made none of the
change. Never ask Mariusz anything; questions go to the orchestrator.

## Where and how

- Worktree (read only, from its root): `C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement`,
  branch `task/rejected-from-refinement`.
- Method: `task-cycle/review/SKILL.md` in the worktree. Read it whole; read a file it names only
  when the step or variant that names it comes. You review a later change to an open request.
- The-way itself: `agent-instructions/README.md` governs it.
- Range: `718c9dc9ad0f728761c7c9ce2eee0a69e6c05b48..03411a5` (one commit; 2 files, +3/−4).
- In place of a findings file, the human's remarks: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\09-correction-remarks.md`.
- Author's report: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\11-correction-report.md`.
- Frozen task: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\task.md`.
- Entries the correction touches: WAY-35 and WAY-134 in `foundations/decisions.md`; the rule in
  `elements/decisions/template.md`. Select further reading yourself.
- The orchestrator's full gate runs in this worktree while you review: do not run test directories
  (`gate/run_tests.py`); `python -B elements/common/foundation_check.py`, `git diff --check` and
  reading are yours.
- Report: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\13-correction-review-report.md`;
  first line `PASS <sha>`, `FAIL <sha>` or `questions`. Return that line, the report path and a
  one-line check result.
