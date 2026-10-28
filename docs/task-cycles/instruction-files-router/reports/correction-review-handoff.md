# Review handoff — correction after review, instruction-files-router (PR #49)

The user invoked the-way-implement-task and delegated intermediate choices to the orchestrator; the
human (Mariusz) then gave binding remarks on the open request. You review the correction as an agent
that made none of the change.

- Worktree: `C:/Storage/repos/the-way-wt/instruction-files-router`, branch
  `task/instruction-files-router`. Work from its root; read-only except your report.
- Method: read `task-cycle/review/SKILL.md` of this worktree whole, with what it names, and review a
  correction after review: the human's remarks take the place of a findings file. Also read
  `agent-instructions/README.md`.
- Range: `f4bbf06..44475cf` (one commit). `f4bbf06` and `8eec20a` only add and remove the cycle record
  under `docs/task-cycles/`. Earlier code passed its reviews: `review-report.md` (`PASS 634fa3b`) and
  `return-review-report.md` (`PASS 524d9b8`), beside this file; they are context, not the subject.
- Remarks: `.runs/task-cycles/instruction-files-router/reports/correction-remarks.md` (R1–R6) — check
  that each is met. R2 asks also for any other restatement of a rule between files of
  `instruction-files/`: check that no rule now stands in two of the skill's files (WAY-258), across
  the whole directory as it stands at `44475cf`, not only the lines the range changes.
- Author's report: `.runs/task-cycles/instruction-files-router/reports/correction-report.md`.
- Against: the frozen task `.runs/task-cycles/instruction-files-router/task.md` (whole), WAY-256,
  WAY-257, WAY-258, WAY-128 in `foundations/decisions.md`, the fact `single-rule-compliance`; select
  further reading by your method. No entry's meaning may change in this range; WAY-128 is reflowed only.
- Answers of step 4: trust boundary — `instruction-files/check_instructions.py` is the part's trust
  boundary; check that its change is to the module docstring only. Irreversible operation — no.
- Gate: do not run `python -B gate/run_tests.py` without a directory; run the focused checks your
  review needs, each with command and exit code.

Write the full report to
`C:/Storage/repos/the-way-wt/instruction-files-router/.runs/task-cycles/instruction-files-router/reports/correction-review-report.md`,
first line `PASS <sha>`, `FAIL <sha>` or `questions`. Return only that first line, a one-line check
result naming what failed or did not run, and the report's path.
