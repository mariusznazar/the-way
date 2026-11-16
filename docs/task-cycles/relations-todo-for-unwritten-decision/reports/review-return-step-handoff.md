# Handoff — review of the return step

You are a fresh reviewer (agent type `the-way-stage`) of the commits of the return step of a task cycle of the-way. You did not make the change. You are read-only. The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

- Worktree: `the task's worktree`, branch `task/relations-todo-for-unwritten-decision`. Work from its root.
- Method: `task-cycle/review/SKILL.md`, the review of the return step's commits, "against the task and the entries the return step writes or corrects". The orchestrator selected what you read (WAY-150): the passages and entries named here, each whole.
- Range to review: base `68d8645c78e55bf751161fedd26dedf31cb43dbc` (the reviewed fix) to head `763af69` (one commit; `foundations/decisions.md`, WAY-71's *Verification* only, and 2 comment lines in `elements/common/test_foundation_check.py`). Read the full diff of the range.
- The return step's report: `reports/author-return-step-report.md`; its method, which you check the commit against: `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`, and, for how an entry's *Verification* and the pair of examples are written when a test holds the sentence, `elements/decisions/template.md` ("Verification") and `elements/decisions/skill/SKILL.md` (the step on a pair carried for a test). Reports of the earlier stages, for context only: `reports/author-report.md`, `reports/author-fix-report.md`, `reports/review-whole-report.md`, `reports/review-fix-report.md`.
- Frozen task: `.runs/task-cycles/relations-todo-for-unwritten-decision/task.md` (in `.runs/task-cycles/relations-todo-for-unwritten-decision/`). The task's *To do* 1 says WAY-71's *Verification* follows the change; WAY-71 and WAY-126 are the entries it changes.
- Entries to read whole: WAY-71 and WAY-126 (`foundations/decisions.md`), WAY-22 and WAY-12 if their rules on tests that hold a decision and on the pair of examples bear on what the commit did. Guidelines: `guidelines/testing.md` whole (the commit touches a test file, comments only).
- Judge: (1) whether removing examples from WAY-71's pair and opening *Verification* with a `tests:` clause is what the rules for an entry held by tests give, and whether anything the removed examples said is now held by no test and no example (a meaning that fell out); (2) whether the two `decision:` lines hold the sentence they quote and name tests that check what the clause says; (3) whether WAY-126 was rightly left whole; (4) whether the return step missed an entry, part-map line or file that the change leaves out of line (the author searched; judge from the files); (5) the author's handling of WAY-287 (left unchanged, named for the human) and of the unread material it states. M4 and M5 of the earlier review and N1, N2 of the fix's review are known and go to the request's list; do not re-grade them.
- Trust boundary: no; irreversible operation: no. You run no full gate (`python -B gate/run_tests.py` without a directory); you may run `python -B gate/run_tests.py elements/common` and `python -B elements/common/foundation_check.py`.
- Report: `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/review-return-step-report.md`, first line `PASS <sha>` or `FAIL <sha>`, by the report form of `task-cycle/review/SKILL.md`, with graded findings, checks with command and exit code, **Unread material**, **Searches not found or unclear**, working copies. Return the first line, the report path and one line of the checks.
- Your directory for working copies: `.runs/review-return-step/` (remove your copy before you return).

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
