# Handoff — the fix of the review's findings (the one author, resumed)

You are the one author, resumed. The person who requested this cycle delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`; reviewed head `b64608400f4fb55bb5508f71e2c4c2aadbcd6a60`; the fix's range runs from it. Do not push.
- Method: `task-cycle/change/SKILL.md`, variant "the fix of a review's findings" (read `fix.md` whole). The foundation step rules of `task-cycle/skill/foundation_step.md` hold for any entry you change.
- Findings file: `reports/review-whole-findings.md` (full path `docs/task-cycles/ci-replaces-local-final-gate/reports/review-whole-findings.md`): four blocking findings (I-1 … I-4) and three Minor findings within the task (M-1 … M-3). The reviewer's full report is `reports/review-whole-report.md` beside it, if you need its context (task coverage, checks). Fix every one; where you hold one wrong, answer it with evidence in your report.
- The orchestrator's rulings that bind this fix:
  - I-4: the finding binds; WAY-365 asks for a move of a part of `process-audit/audit_count.py` without change of behaviour. Make it a separate move commit (or order your unpushed commits so the move comes first — your choice, the branch is not pushed). Choose a part whose lines the other branch `task/audit-answers-contradiction-after-code` (commit `6867078`) does not move, so the later merge of the two does not conflict in the same lines; record in the report which part you moved and why. If no part can be moved without a change larger than the finding, return `questions` with what you found, no half move.
  - I-1 and I-2: the task keeps the base run local and rare and puts the statement "the final gate ran in CI" into *Verification* of the record. Make the committed copy of the record hold the statement before it is committed (the decision that CI is the final gate is known at step 10), and give step 4 a source for the final gate's result when it was CI, so that no cycle after a CI-gated cycle runs a full local gate on its base for lack of one; the task's sources give no such source, so choose the smallest reversible reading and name it in your report as a choice with the way rejected and its cost if wrong. Keep the fallback run's time reaching the copy the audit reads, or say in the report why it cannot and what the audit then shows. Change test and sentence together where a test quotes a sentence you change.
  - I-3: add the clause for a request left blocked for unfinished code to WAY-160's first paragraph and its *Verification*.
  - M-2: do what the repository allows; you cannot read the ruleset (WAY-82's reading is the human's after the human action); make sure the request-ready text of the human action names the stale fact `foundations-branch-ruleset` and the reading to repeat; do not edit the fact to a state the source does not yet have.
- Run the affected checks again (the directories you change with `python -B gate/run_tests.py <directory>`, and `python -B elements/common/foundation_check.py`); not the product's full gate — that run is the orchestrator's alone (WAY-160).
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-fix-report.md`, with each finding answered (fixed, how, commit; or held wrong with evidence), the checks with command and exit code, **Unread material**, **Searches not found or unclear**, the own-work check and the working copies line. Return status, commits, a one-line check result, report path.
- Your directory for working copies: `.runs/author-fix/`.

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
