# Assessment settlement handoff — author, turn 5

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product`, at `0c1dfd5`.
Read: [assessment.md](assessment.md) remarks A1, A2, A8 and the orchestrator's settlement [assessment-settlement.md](assessment-settlement.md). Apply exactly the rows marked "Apply" there, nothing else:

- **A1** — rewrite WAY-121's gate clause as the settlement states (state, "approved or not"; pin move and refinement stay in *Verification* examples and *Rationale*). Keep rows 1, 4, 5's meaning. Renew WAY-121's fingerprint everywhere it is carried: WAY-122, WAY-123, WAY-165 relations and the *Derives from* of `project-technology-record/1` in `foundations/invariants.md` — that one is a link renewal only; do not change the invariant's sentence or any `# invariant:` test. Update the Polish meaning sentence of WAY-121 in your report if it changes.
- **A2** — cut the additions of this change in `project-level/plan/skill/SKILL.md` and `project-level/task/skill/SKILL.md`; in `project-level/lead/skill/SKILL.md` shorten the addition to one clause naming no mark string, pointing to `define-project`.
- **A8** — cut the two duplicated cases from `project-level/test_readiness_marks.py`.

## Checks

Outputs under `reports/` with prefix `settlement-`, exit codes recorded: decisions and invariants format guards (`--base none --merge-onto none`), `python -B gate/run_tests.py elements/decisions`, `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl`, `python -B gate/run_tests.py gate`, `python -B agent-instructions/skill_entry_points.py`, `git diff --check 77c8a8b..HEAD`, fingerprint recount (0 stale). Rerun your weakest-point check (`ApprovedBefore`) — it is in the project-level run.

## Output

Append "Assessment settlement (turn 5)" to `reports/author-return.md`: what changed per remark, new fingerprints, new Polish sentence of WAY-121 if changed, commands, exit codes, outputs, changed files with line counts for `0c1dfd5..HEAD`, concerns. Same write rules as before (explicit paths, English message, no `.runs/`, no push, no agents, no human). Return a short message.
