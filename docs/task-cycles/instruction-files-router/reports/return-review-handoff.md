# Review handoff — return step, instruction-files-router

The user invoked the-way-implement-task and delegated intermediate choices to the orchestrator. You
review the return step's commit as an agent that made none of the change.

- Worktree: `C:/Storage/repos/the-way-wt/instruction-files-router`, branch
  `task/instruction-files-router`. Work from its root; read-only except your report.
- Method: read `task-cycle/review/SKILL.md` of this worktree whole, with what it names, and review the
  return step's range. Also read `agent-instructions/README.md`.
- Range: `634fa3b..524d9b8` (one commit). The whole change `0b8c1bd..634fa3b` already passed its review
  (`reports/review-report.md`, `PASS 634fa3b`), and is context, not the subject.
- Against: the frozen task `.runs/task-cycles/instruction-files-router/task.md` (whole) and the entries
  the return step corrects the code to: WAY-256, WAY-258 (in `foundations/decisions.md`) and the fact
  `single-rule-compliance` (in `foundations/environment_facts.md`); select further foundation reading
  by your method.
- Return-step report: `.runs/task-cycles/instruction-files-router/reports/return-report.md`. The
  return step corrected three mismatches the whole-change review had listed as Minor 1, 2 and 6 and
  one further one it found (Place step 1 restating the rule on adding a rule). Minor 3, 4 and 5 were
  left on purpose.
- Answers of step 4: trust boundary — the range does not touch `instruction-files/check_instructions.py`;
  irreversible operation — no.
- Gate: do not run `python -B gate/run_tests.py` without a directory; run the focused checks your
  review needs, each with command and exit code.

Write the full report to
`C:/Storage/repos/the-way-wt/instruction-files-router/.runs/task-cycles/instruction-files-router/reports/return-review-report.md`,
first line `PASS <sha>`, `FAIL <sha>` or `questions`. Return only that first line, a one-line check
result naming what failed or did not run, and the report's path.
