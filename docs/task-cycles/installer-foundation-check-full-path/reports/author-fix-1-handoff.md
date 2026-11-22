# Handoff — the fix of a review's findings (the one author, resumed)

The variant of `task-cycle/change/SKILL.md` is "the fix of a review's findings": read `task-cycle/change/fix.md` as the method gives.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

## Where you work

- The same worktree and branch as before (`the task's worktree`, `task/installer-foundation-check-full-path`), reviewed head `1c222ce238c2194900ec246de5f8cc6cfa7faa5b`; the fix's range runs from it.
- Your directory for working copies: `.runs/author/` as before.
- Your report: `.runs/task-cycles/installer-foundation-check-full-path/reports/author-fix-1-report.md` (the file is the input of the cycle's scripts; the rule against a subagent writing a file whose name starts with `report` does not apply to it; if refused, return the report whole as your answer).
- The review's report is not yours to read; the findings file is yours.

## The findings

`reports/review-whole-findings.md` (in the record directory `.runs/task-cycles/installer-foundation-check-full-path/`): one blocking finding (Important, marked as contradicting WAY-12) and two Minor findings of the review of the whole change within the task. Fix all three in one fix, as the findings file gives each. For the blocking finding, WAY-418's *Verification* is edited in place through `record-decision` (`elements/decisions/skill/SKILL.md`, read whole, with the files it names where the step that names them comes); its binding sentences do not change. The orchestrator's earlier answer that WAY-418 stays unchanged is withdrawn by this finding (the review holds the foundation requires the link: WAY-12, `elements/decisions/template.md` section Verification, `elements/invariants/skill/write.md` step 4.4). The reviewer reads WAY-30 as not needing the human here: the edit adds the link WAY-12 requires and changes no binding sentence; where you hold otherwise, say so in your report instead of editing, with the evidence.

If you hold a finding wrong, answer it with evidence in the report instead of changing the code. Run the affected checks again: the tests of the files you change (`python -B gate/run_tests.py installation`, which takes about ten minutes, or the focused tests), `python -B elements/common/foundation_check.py`, the linter and formatter as before. For Minor finding 2, show the reviewer's mutation (an `@` import with a full stop in the block's sentence) failing the test after your change. Run no full gate. Commit by path, English message; remove your working copies in `.runs/author/` before you return, as the first handoff's paragraph on working copies gave.

Return status, the fix's commits, one line on the checks, and the report's path; the report holds **Unread material** and **Searches not found or unclear** and each check with its command and exit code.
