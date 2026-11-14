# Handoff to the agent of the fix

You make "the fix of a review's findings" under `make-change` for one task cycle of the-way. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`, reviewed head `6a984c5`, base of the task `ec7929d`). The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Commit by path (`git add <path>`), an English message, never push, never run the product's whole gate (`python -B gate/run_tests.py` without a directory).

- Method: `task-cycle/change/SKILL.md` whole, then `fix.md` beside it (the findings file, what is not yours to fix, what the report of a fix holds).
- Findings file: `reports/review-whole-findings.md` (in `.runs/task-cycles/decision-log-second-round/`), the reviewer's words: four blocking findings (1-4) and the Minor findings within the task (5-11). Fix 1-5 and 7-10. Findings 6 (which entries the request puts before the human) and 11 (the own-work checks of the slices) are the orchestrator's: do not touch WAY-202 or any keep/withdraw decision; take finding 11 as a rule for your own own-work check: read each rule you touch against its entry at the base (`git show ec7929d:foundations/decisions.md`) and say so in the report.
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490); the plan `plan.md` and the reviewer's full report `reports/review-whole-report.md` for the evidence behind each finding (read the paragraph of each finding you fix, with its evidence, whole).
- Files you may change: the files each finding names; for findings 4 and 5 `foundations/decisions.md` (the entry WAY-258 only, by the pattern of the addition to WAY-100 as it stands in the log, and the relations it needs) and `foundations/part_map.md`. Where a finding asks for a sentence of reason, write it from the *Rationale* of the withdrawn entry at the base; where a finding asks for a clause of a rule, take it from the entry at the base, word for word where it fits. Never invent.
- Finding 2 asks to take out of `elements/environment-facts/skill/read.md` what slice 4 restated; where the rule it restated stands in `elements/common/way_of_working.md`, nothing else is needed there; check that it does and say so.
- Finding 10 concerns only the lines this change added: do not rewrap lines it did not touch.
- Checks (focused only): `python -B elements/common/foundation_check.py` must exit 0 (with the one `listed:` line for `tracked-file-private-paths`, which is expected), `python -B gate/run_tests.py <directory>` for each directory whose files you change and which holds tests (say where a directory holds none), `python -B agent-instructions/skill_entry_points.py` if you touch a skill. Record every check as command and exit code. Run the affected checks again after your last change.
- Where you hold a finding wrong, answer it in your report with evidence instead of changing; where a finding cannot be fixed without a choice of the human, say so and leave it.

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

Your directory for working copies: `.runs/fix-whole/` (remove its files one by one by path before you return; no recursive delete).

## Report

Write your report to `.runs/task-cycles/decision-log-second-round/reports/fix-whole-report.md`: status, commits, for each finding what you did or why you did not, each check with command and exit code, the own-work check (each touched rule read against its entry at the base), **Unread material**, **Searches not found or unclear**, working copies. Return the status, commits, one-line check result and the report path.
