# Handoff — review of the return step's commits (task cycle `test-artifacts`)

You are a fresh reviewer; you did not make this change. Method: `task-cycle/review/SKILL.md` whole (read-only), section for the return step's commits: review them against the task and the foundation entries the return step writes or corrects.

- Worktree: `the worktree's root`, branch `task/test-artifacts`. Range: `ef0195edb7128b30f9768aab89e3b8846d2d8d5e`..`25dd4ba` (one commit, a docstring edit of `task-cycle/image_files_check.py`).
- Return step's rule: `task-cycle/skill/return_step.md`. Author's return report (claims to verify): `docs/task-cycles/test-artifacts/reports/return_report.md`. Frozen task: `...\.runs\task-cycles\test-artifacts\task.md` (Polish). The change as a whole already passed review (`reports\review2_report.md`, `PASS ef0195e`); you judge only this range, plus whether the return step missed a mismatch between the foundation entries the change writes (WAY-316..319, WAY-121, WAY-165, invariants `record-copy-image-check`, `record-copy-image-files`) and the code.
- Report path: `...\reports\review3_report.md`, first line `PASS <sha>` or `FAIL <sha>`, with checks (command + exit code) and **Searches not found or unclear** (or `none`). Do not run the full gate. Return the first line, a one-line check result and the report path.
