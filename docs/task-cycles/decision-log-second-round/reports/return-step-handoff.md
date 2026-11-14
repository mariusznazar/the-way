# Handoff to the agent of the return step

You take the return step (step 11 of `implement-task`) of one task cycle of the-way, as a fresh agent with `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`, head `0364c08`, base `ec7929d`). Commit by path (`git add <path>`) with an English message, never push, never run the product's whole gate (`python -B gate/run_tests.py` without a directory) — its run is the orchestrator's.

- Method: `task-cycle/change/SKILL.md` whole, with `task-cycle/skill/foundation_step.md` and `task-cycle/skill/return_step.md` whole (this handoff names the return step; take no row of the table of variants of `make-change`).
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490); plan `plan.md`; the foundation agent's report `reports/foundation-report.md`; the review reports `reports/review-whole-report.md` and `reports/review-fix-report.md`; the fix report `reports/fix-whole-report.md`.
- What the change did: it withdrew 137 entries of the decision log into the rules of their skills and templates (the ten entries WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364 stay), merged six into others, added to WAY-100 the rule of how a decision names a practice taken from outside, added the commit-description source to WAY-29 and the recovered-decisions rule of the template, and applied the pattern of the relation `derives from WAY-100` to 36 decisions; in the same range every reference to a withdrawn number in the repository was repointed or removed. `git diff --stat ec7929d HEAD` shows the files.

## What to do

1. Compare, as `return_step.md` gives, the foundation entries the change wrote or changed (WAY-100, WAY-29, the 36 of the pattern, the merged targets WAY-288, 316, 309, 339, 368, the invariants and part map the foundation agent edited), those the task names (WAY-293, WAY-19, WAY-02, WAY-90, WAY-27) and the entries your own search of the foundation for the changed rules finds (WAY-33), with the code and files of the repository, and the part map of the touched parts. Correct in the same change whatever no longer matches (a sentence in an entry that says a rule stands in a file it no longer stands in, a part-map line, a stale count). The log's entries that name a withdrawn rule's old place must still say what is true.
2. Environment facts, glossary terms, settlements, invariants: write one only where `return_step.md` gives the rule for it; write none for what the task or the plan says is out. The choice "an entry that `narrows` a staying decision stays in the log, because it is the one record of the precedence (WAY-25)" and the choice of the ten kept entries: decide whether `return_step.md` makes either a choice that binds after the merge and so a decision of the log (WAY-36), or a row of the questions table; say what you did and why in the report. Do not write a decision whose meaning the human has not accepted: where in doubt, leave it a question to the orchestrator.
3. Do not undo or re-judge the reviewed change; correct only a mismatch of the foundation with the code that the change left.
4. Checks (focused only): `python -B elements/common/foundation_check.py` (exit 0 with the one expected `listed:` line for `tracked-file-private-paths`), `python -B gate/run_tests.py <directory>` for each directory whose files you change. Record each as command and exit code.
5. If you change nothing, say so and show the comparison (what you compared and found equal).

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/return-step/` (remove its files one by one by path before you return; no recursive delete).

## Report

Write your report to `.runs/task-cycles/decision-log-second-round/reports/return-step-report.md`: status, commits, and the lines of the record's *Return step* (foundation compared with code, decisions written or changed, invariants, environment facts, glossary terms, part-map changes, projected entries, rows of *Settlements to record* written), each check with command and exit code, **Unread material**, **Searches not found or unclear**, working copies. Return the status, commits, one-line check result and the report path.
