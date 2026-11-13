# Handoff — review of the whole change

You review the whole change of a task in a the-way task cycle, as an agent that did not make it.
The person who requested the cycle has delegated intermediate choices to the orchestrator.

- Worktree (read-only for you; work from its root): `the task's worktree`, branch `task/gate-series-on-test-runner`.
- Method: read `task-cycle/review/SKILL.md` of this worktree whole; for the whole change it sends you
  to `task-cycle/review/whole_change.md`. Your variant: **the review of the whole change**. You select
  your own foundation and guidelines as that skill gives.
- Range: base `715ae20d9e817299bd81554e5fdcb6baaf465099` (the-way itself, target branch `foundations`) to head `909fcb9`; compute the diff yourself.
- Frozen task, read whole: `docs/task-cycles/gate-series-on-test-runner/task.md`. No spec, no plan (one author, no plan). No move of the pin.
- Author's report (claims to verify, not evidence): `docs/task-cycles/gate-series-on-test-runner/reports/author-report.md`. It flags one thing for you: the change removed the *Verification* "violates" bullet of WAY-339 that read "a change of the script that records the gate times leaves their series whole" and put another in its place; judge that edit and the other edits of WAY-339 (its *Scope*, *Rationale*, *Rejected*) against the settlement row and the rules of a decision entry.
- Answers of the cycle's start: the change touches a **trust boundary** — `process-audit/audit_count.py` is the part map's trust boundary of the part `process-audit` — so check crafted input at it (a path in the list of instrument files, a repository whose history lacks `gate/run_tests.py`, malformed `gate_times.md`). No operation that cannot be undone.
- Checks failing on the base (list taken from the final gate of the merged cycle `gate-parallel-directories`): none. The author ran `python -B gate/run_tests.py process-audit` (182 tests, exit 0) and `python -B elements/common/foundation_check.py` (exit 0). The product's whole gate is the orchestrator's run; do not run it. Run only what your skill asks of you and say what you ran, with command and exit code.
- Report path: `docs/task-cycles/gate-series-on-test-runner/reports/whole-review-report.md`. First line `PASS <sha>` or `FAIL <sha>`; the report holds **Unread material** and **Searches not found or unclear** (`none` where none), and the counts of decisions read whole and by title only.
