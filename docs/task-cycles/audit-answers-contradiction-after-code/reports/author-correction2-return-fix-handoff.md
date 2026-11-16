# Handoff to the one author — the fix of the review of the return step after correction 2

The review of the return step returned `FAIL 9547acd470f7a05cba43193ab9bf4b2e56a12e22` (`reports/review-correction2-return-report.md`). The one blocking finding, I-1, stands in `reports/review-correction2-return-findings.md`, in the reviewer's words; fix it with `make-change`, variant "the fix of a review's findings", on the same branch from head `9547acd4`. Your directory for working copies: `.runs/author-correction-2-return-fix/` (keep every backup and probe inside it). Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction2-return-fix-report.md`. Delegation as before: ask the human nothing, do not run the product's full gate.

- Fix I-1 as the finding gives, or by a way you hold better with its reason. The code is the side to keep (point 4 of the task's *To do*: an entry in neither form still gives `unknown`); no code change. Say, in every place the finding names and in any other place that says the same (search the repository: `process-audit/SKILL.md`, the docstrings of `process-audit/audit_count.py` and `process-audit/record_items.py`, WAY-404's *Verification* and binding sentence, the template), that a round marked `contradiction yes` gives `yes` only where *Review rounds* is held once and in its form, and add the subtests the finding names (R1–R4 `unknown`, R7 `yes`) to the test that cites WAY-404. Probe each sentence you write against `read_contradiction` before you commit it: the earlier rounds of this change were each caught on a sentence that said more or less than the code.
- The Minor findings m-1 and m-2 of that report are **not** to be fixed: the cycle carries them to the request's list. Do not change code and do not widen beyond I-1.
- Run the affected focused checks (`python -B gate/run_tests.py process-audit`, `... task-cycle`, `python -B elements/common/foundation_check.py` without `--skip-test-citations`), each with command and exit code. Commit by path, messages in English.

## Working copies

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

## The report

As `make-change` gives it for a fix, with **Unread material**, **Searches not found or unclear**, the own-work check and the fix's range from `9547acd470f7a05cba43193ab9bf4b2e56a12e22`. Return status, commits, a one-line check result and the report's path.
