# Handoff — review of the whole change

You are the reviewer (agent type `the-way-stage`) of the whole change of a task cycle of the-way. You did not make the change. The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval. You are read-only: you change no tracked file and make no commit.

- Worktree: `the task's worktree`, branch `task/relations-todo-for-unwritten-decision`. Work from its root.
- Method: read `task-cycle/review/SKILL.md` whole; your variant is the review of the whole change, so read `task-cycle/review/whole_change.md` as it says and follow it. You select your own foundation and guidelines by the parts of the change (`elements/common/way_of_working.md`, "Reading the foundation"; `product-guidelines/reading.md`), each guideline file whole; write your index of decisions to a file in your own directory below.
- Range to review: base `30c947f686b3d304f5a952cb6efe547762cfa247` to head `452f123` (one commit by the one author; changed files: `elements/common/foundation_check.py`, `elements/common/test_foundation_check.py`, `elements/common/rules.md`, `elements/decisions/template.md`, `foundations/decisions.md` (WAY-71 and WAY-126), `task-cycle/skill/request_template.md`).
- Frozen task (read it whole; judge the change against every item of its *To do* 1–6, its *Questions to settle* answers, *Decisions in play*, *Out of scope*): `.runs/task-cycles/relations-todo-for-unwritten-decision/task.md`. No spec, no plan, route: one author without a plan.
- The author's report: `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-report.md` (status `done with concerns`).
- Answers of step 4: trust boundary **no**; irreversible operation **no**.
- Facts the orchestrator found against the current sources, for you to weigh, not to take as settled: (1) the task says the-way has no `guidelines/`; it has `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md`, which bind the change. (2) The task's *Decisions in play* names WAY-37 and WAY-32 as unchanged entries; both are withdrawn, their rules standing in `elements/common/way_of_working.md` and `elements/decisions/template.md`. (3) The author's concerns, which the orchestrator did not judge: WAY-287 (left unchanged, as the task says) lists three fields for the descriptive `TODO` while item 16 of the request template now lists four; the author put the WAY-126 sentence in a second paragraph and added one example each to its *Verification* complies and violates lines, and marked both entries `the cycle's`; the author added one sentence to the "Relations and precedence" part of `elements/decisions/template.md` that the task does not list; `ruff` was not installed in the author's environment, so the blocking rules of the linter were not run on the two changed Python files (run the linter yourself where it is available, or say it was not); `elements/common/way_of_working.md` was read in part only by the author — judge whether a step there needs a sentence for the *Relations* `TODO`.
- You run no full gate (`python -B gate/run_tests.py` without a directory): that run is the orchestrator's alone (WAY-160). You may run the tests of one directory (`python -B gate/run_tests.py elements/common`) and `python -B elements/common/foundation_check.py`.
- Report: write your full report to `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/review-whole-report.md` (first line `PASS <sha>` or `FAIL <sha>`), by the report form `task-cycle/review/SKILL.md` gives: graded findings with their place, which of them are outside the task's scope, the checks you ran with command and exit code, how many decisions of your index you read whole, **Unread material**, **Searches not found or unclear**, working copies. Return the first line, the report path and one line of the checks.
- Your directory for working copies and your index: `.runs/review-whole/`.

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.
