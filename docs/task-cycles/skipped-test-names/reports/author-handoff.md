# Handoff — one author

Delegation: the person who requested this cycle has delegated intermediate choices to the
orchestrator of `implement-task`. Send questions to the orchestrator, never to the human.

- Worktree: `C:\Storage\repos\the-way\.runs\worktrees\skipped-test-names`, branch
  `task/skipped-test-names`, base `2f51e6c`. Work from its root; commit there, push nothing.
- Method: `task-cycle/change/SKILL.md` in this worktree, variant "the whole change as the one
  author". Read that `SKILL.md` whole, and a file it names only when the step or variant that names
  it comes.
- Stage and boundary: make the whole change and return before review. Do not start the next stage.
- Frozen task: `.runs/task-cycles/skipped-test-names/task.md`, read it whole. The task document's
  numbers of lines in `gate/` stand at `2f51e6c`.
- Spec and plan: none. No open design choice stands; the task's *Context* gives a checked way, which
  the cycle may keep or change.
- Answers of step 4: trust boundary no (`gate` has none); operation that cannot be undone no; one
  author without a plan.
- Report: `.runs/task-cycles/skipped-test-names/reports/author.md`. Return your status, your commits,
  a one-line check result naming what failed or did not run, and the report's path. A check the
  report says it ran carries its command and exit code. The report keeps **Searches not found or
  unclear**, each thing looked for and not found or unclear, or `none`.

## What to read

- Parts: `gate`, `foundations/part_map.md` entry `## gate`, and the surface `## test-runner-command`.
- Decisions, each whole, in `foundations/decisions.md`: WAY-16, WAY-38, WAY-55, WAY-61, WAY-63,
  WAY-65, WAY-69, WAY-03.
- Invariants, each whole, in `foundations/invariants.md`: `gate-exit-code`, `script-imports`,
  `script-subprocesses`, `script-language`.
- Guidelines: the-way holds no `guidelines/` directory. The task's *Questions to settle* settles that
  this task does not wait for them; read none.
- `agent-instructions/README.md`, section "Check the change".
- Code: `gate/run_tests.py`, `gate/test_run_tests.py`.

## Focused checks

The change to `gate/run_tests.py` is checked by both of these, from the worktree's root, with their
commands and exit codes in the report:

```
python -B gate/run_tests.py gate
python -B -m unittest discover -s gate -p "test_*.py"
```
