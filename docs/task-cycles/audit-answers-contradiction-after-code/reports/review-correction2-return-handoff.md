# Handoff to the reviewer of the return step after correction 2

You are a fresh reviewer: you did not make the change and did not write any earlier review of it. Ask the human nothing; a question goes to the orchestrator in your report as `questions`.

## What you review

- The worktree (read-only for you): `the root of the task's worktree`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), read whole; a file it names only when the step or variant that names it comes. The review is of the return step: `task-cycle/skill/return_step.md` says what the step compares and writes.
- The range: base `5a39a328346ad9a8d12e37732f52a86a164e3d17` (the code the earlier reviews of correction 2 accepted) to head `9547acd4` (`git rev-parse 9547acd4` gives the full identifier). One commit. Diff: `git diff 5a39a328 9547acd4`. It changes `process-audit/SKILL.md`, `task-cycle/record_template.md` and docstrings of `process-audit/audit_count.py` and `process-audit/record_items.py` (verify that no executable line changed: compare the syntax trees without docstrings).
- The author's report (claims to verify): `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction2-return-report.md`.
- The task the change carries out: `.runs/task-cycles/audit-answers-contradiction-after-code/task.md` (frozen). The human's remarks of correction 2: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/correction-2-remarks.md`.
- Trust boundary: yes (`process-audit/record_items.py` reads records from git history, untrusted); no behaviour changed here, so a probe is needed only if you doubt the equality of the trees.
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-correction2-return-report.md`. Your directory for working copies: `.runs/review-correction-2-return/`.

Judge: does every sentence the return step corrected say what `process-audit/record_items.py` does now (probe it by `read_contradiction` where you doubt), does any sentence it left (WAY-337, WAY-344, WAY-404, WAY-405, the part-map line, the template's two items) still say more or less than the code, and did the step stay within `return_step.md` (no entry for later, no invariant written without a rule set, no widening). Findings that the earlier reviewers already carry as open Minor findings (M-1 of `reports/review-correction2-report.md`, m-1 and m-2 of `reports/review-correction2-fix-report.md`) are known; report them again only where this commit changes their picture. Say for each blocking finding whether it contradicts an entry of the foundation or a settled answer of the task document.

## Checks

Focused checks only, in a worktree of the head in your directory: `python -B gate/run_tests.py process-audit`, `python -B gate/run_tests.py task-cycle`, `python -B elements/common/foundation_check.py` without `--skip-test-citations`. **Do not run the product's full gate.** Report each check with command and exit code.

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

First line `PASS <sha>` or `FAIL <sha>` (or `questions`); graded findings with places; checks with commands and exit codes; **Unread material**; **Searches not found or unclear**; the line on your working copies. Return the first line, a one-line check result and the report's path.
