# Handoff to the one author — the return step after correction 2

Correction 2 passed its review (`PASS 5a39a328`, `reports/review-correction2-fix-report.md`; the merge of the target branch passed as well, `reports/review-merge-report.md`). Take the return step, step 11 of `implement-task`: read `task-cycle/skill/return_step.md` whole and, since it writes as the foundation step writes, `task-cycle/skill/foundation_step.md` whole, and the `SKILL.md` of an element when you write an entry of that element. Your directory for working copies: `.runs/author-correction-2-return/`. Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction2-return-report.md`. Delegation as before: ask the human nothing, do not run the product's full gate.

Worktree and branch as before; head `5a39a328346ad9a8d12e37732f52a86a164e3d17`. The range of this correction runs from `2e31b74b1a0dd3c9c787ed79a025bb7f372615a6`; the return step of the earlier round (`reports/author-return-report.md`) stands.

What changed since the earlier return step: the merge of PR #140 (CI is the final gate), the rule's wording of WAY-405 and WAY-404 (the `none` clause, the second reason read only as `reason: ` and a backtick, which second reason is read, which answer wins, the item with text after its colon, the margin line), the docstrings of `process-audit/audit_count.py` and `process-audit/record_items.py`, `task-cycle/record_template.md` (one clause) and the tests. The human's remarks: `reports/correction-2-remarks.md`; the author's reports: `reports/author-correction2-report.md` and `reports/author-correction2-fix-report.md`.

Compare with the code, as `return_step.md` gives: the entries this change writes or changes (WAY-337 new paragraph, WAY-344 narrowing, WAY-404, WAY-405), those the task names, the part-map line, the record template's items *Discarded attempt* and *Review rounds*, `process-audit/SKILL.md` and the docstrings — each against the final code — and correct in the same change whatever no longer matches. In particular check that every sentence that describes how the audit reads *Discarded attempt* or *Review rounds* says what `process-audit/record_items.py` does, the reviewer's open Minor remarks aside (they are not yours to fix: M-1 of `reports/review-correction2-report.md`, m-1 and m-2 of `reports/review-correction2-fix-report.md`). Do not change code. Where nothing no longer matches, commit nothing and say so in the report.

Focused checks, each with command and exit code: `python -B elements/common/foundation_check.py` without `--skip-test-citations`, `python -B gate/run_tests.py process-audit`, `python -B gate/run_tests.py task-cycle`. Commit by path, messages in English.

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

As the record's *Return step* gives it (what it compared, what it corrected, entries written), with **Unread material**, **Searches not found or unclear**, the own-work check and the range from `5a39a328346ad9a8d12e37732f52a86a164e3d17`. Return status, commits, a one-line check result and the report's path.
