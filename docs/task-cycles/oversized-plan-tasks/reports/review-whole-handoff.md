# Handoff: review of the whole change

You review the whole change of one task cycle of the-way, as an agent that did not make it. You are
read-only: change no file of the worktree. The orchestrator has delegated the cycle's intermediate
choices; nothing here is a human's approval. You never ask the human; questions go to the
orchestrator in your report.

- Worktree: `the task's worktree, the repository's root`, branch `task/oversized-plan-tasks`. Read from there.
- Method: read `task-cycle/review/SKILL.md` whole in the worktree; your variant is the review of the whole change. Read a file it names only when the step or variant that names it comes.
- Range to review: `5a24ac97277fa1c04fbb967da5c6a2854d17cb8f..44c1d99` (two commits: `0ed5ad7`, `44c1d99`). The route is one author without a plan; no spec, no slices.
- Frozen task (read whole): `.runs/task-cycles/oversized-plan-tasks/task.md`. It is the requirement: *To do* 1-4, *Acceptance criteria*, the two rows of *Settlements to record*, *Out of scope*. Check every item of it, each settlement row, and source fidelity (the wording the task asks for, no widening).
- Author's report: `.runs/task-cycles/oversized-plan-tasks/reports/author-report.md`. The report lists two orchestrator rulings you should judge, not take as settled: (1) the orchestrator allowed the author to add one clause to `project-level/plan/template.md`, a file the task does not name, because that paragraph restates WAY-146's list of what the critique judges; (2) WAY-146's *Rejected* holds a third item (the author splitting a task after the critique's remark), the not-chosen way of settlement row 2. Also judge the author's change of the cut-tasks bullet ("A large task is split" became "A task too large is split ... the author never splits a task for its size alone").
- Answers of step 4: touches a trust boundary: no (the part map's boundary files of `project-level` are untouched); holds an operation that cannot be undone: no; open design choice: none.
- The change edits the foundation entry WAY-146 in place (WAY-07). You select your own foundation and guidelines by the parts of the change, as `review-change` gives. The-way has no coding or testing guidelines (WAY-328).
- Checks you may run: `python -B elements/common/foundation_check.py` and `python -B -m unittest discover -s project-level -p "test_*.py"`. Do not run the product's gate (`gate/run_tests.py`): it is the orchestrator's.
- Report path: `.runs/task-cycles/oversized-plan-tasks/reports/review-whole-report.md`, first line `PASS <sha>` or `FAIL <sha>` as the method gives; it carries changed files with line counts, each check with its command and exit code, the numbers of decisions read whole and by title, **Unread material** and **Searches not found or unclear**. Return the first line, a one-line check result and the path.
