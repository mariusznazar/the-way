# Handoff — review of the whole change

You review, as an agent that did not make the change, the whole change of one task cycle of the-way (variant: the whole change), with the method `.claude/skills/the-way-review-change/SKILL.md` of the worktree; read it whole, and a file it names only when the step or variant that names it comes. The person who requested the cycle delegated intermediate choices to the orchestrator; the orchestrator's answers are no human approval.

- Worktree (read-only; work from its root): `the root of the task worktree`, branch `task/guidelines-departure`.
- Range: `e3825a8..7442841` (one commit, `foundations/decisions.md` +47 lines, entry WAY-327). One author, no plan, no slices, no spec; no slice had a review of its own.
- Frozen task, read whole: `.runs/task-cycles/guidelines-departure/task.md`. Check every item of its *To do* and both rows of *Settlements to record* (rows 1 and 2) for coverage and source fidelity — the author wrote the two rows as one entry; judge whether that holds both rows' meaning.
- The author's report: `.runs/task-cycles/guidelines-departure/reports/author-report.md`. Its **Unread material** says the author did not read WAY-03 (the example of a decision's form) and did not run the skill's selection of the decisions whose *Scope* names `decisions` in full; you select your own foundation and guidelines by the parts of the change (part `decisions`).
- Answers of step 4: trust boundary — no; irreversible operation — no; open design choice — none.
- The change touches no code, test, user interface or skill; the product's guidelines reading finds nothing to read for it.
- Do not run the product's gate (the orchestrator runs it); you may run `python -B elements/common/foundation_check.py --skip-test-citations`.
- Your report goes to `.runs/task-cycles/guidelines-departure/reports/review-whole-report.md`, as your method gives it, with the first line `PASS <sha>` or `FAIL <sha>`, **Unread material** and **Searches not found or unclear**. Return the first line, the checks you ran with exit codes, and the report path.
