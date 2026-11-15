# Handoff — review of the return step's commit

Stage: the review of the commits of the return step, by an agent that made none of the change. Method: read whole `task-cycle/review/SKILL.md` and follow it; a file it names only when the step that names it comes. The return step's commits are reviewed as section 2 of that skill gives, against the task and the foundation entries the return step writes or corrects. Variant: the return step's commits.

## Delegation

The person who requested this cycle has delegated the intermediate choices to the orchestrator. Your questions go to the orchestrator, in your report. You are read-only: no commit, no full gate (`python -B gate/run_tests.py` without a directory); a check that only reads, or the tests of one directory run from your own working directory, is yours to run.

## What you review

- Worktree, read from its root: `the task's worktree`, branch `task/foundation-review-reminder`; the-way itself, no product pins it here.
- Range: base `31f7507bce088ecf6ee825889bfada949076db68` to head `e5ae875`; one commit, `e5ae875`. Read its full diff: `foundations/decisions.md` (WAY-300 *Verification* begins with a clause `tests:` and its pair of examples is cut to the cycle's and the request's part; a ragged paragraph of the binding sentences rewrapped) and `task-cycle/test_review_reminder.py` (six comment lines `decision: WAY-300 "…"`, no code).
- The return step's report: `docs/task-cycles/foundation-review-reminder/reports/return-step-report.md`; its rule: `task-cycle/skill/return_step.md`, whose passage on a decision that carries a pair of examples while a test holds part of its sentence is what the commit applies.
- The entry it changes is WAY-300, in `foundations/decisions.md`; the entries and the rules for how a test holds a sentence of a decision are WAY-12 and the invariant `test-method-citation`. The frozen task, `docs/task-cycles/foundation-review-reminder/task.md`, and your own selection of the foundation as `way_of_working.md` "Reading the foundation" gives it; you did not see the change before, so select the parts `decisions`, `task-cycle` and `foundation-review` for what this commit touches, and write your index of decisions into `.runs/review-return/`.
- Context: the change this follows passed the review of the whole change (`PASS b7ec371`) and its fix passed (`PASS 31f7507`); the reports are `reports/review-whole-report.md` and `reports/review-whole-fix-report.md`. They are no part of what you judge; read them only where a question of this commit needs them. The fix review's one new Minor finding (the lines of WAY-300 *Rejected* over 100 columns) is the cycle's to list in the request; it is not a finding of this review and the return step did not fix it by the handoff.

## What to check

That the lines `decision:` give the number of WAY-300 and the start of a sentence that stands in its binding sentences, at tests that hold it; that the clause `tests:` names, in words and with no path, no test name and no number, what the tests hold; that the pair of examples keeps only what no test holds and no example still describes a held part; that WAY-300's wording otherwise is unchanged (the rewrap changes no word); that `python -B elements/common/foundation_check.py` still reports `0 errors`; and anything the commit brings that the return step's rule or the task does not allow.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/review-return/`. Your report: `docs/task-cycles/foundation-review-reminder/reports/review-return-report.md`, first line `PASS <sha>` or `FAIL <sha>`.

## Return

That first line, your commits (none), a one-line check result naming what failed or did not run, the path of your report. In the report: your **Unread material** (your own selection included) and **Searches not found or unclear**, and your working copies.
