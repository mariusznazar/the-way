# Handoff — the return step of correction 1, `defects-found-after-merge`

Same delegation, worktree (`the task's worktree, which is the repository's root`),
branch and rules for commits as `reports/correction-1-author-handoff.md`. Stage: the return step
(step 11 of `implement-task`) of the correction, by the author resumed. It is no variant of a row of
`make-change`; read `task-cycle/skill/return_step.md` and, since the return step writes as the
foundation step writes, `task-cycle/skill/foundation_step.md`, each whole, and the skill of an
element when you write an entry of that element.

Head now: `a3152c967c05f4013e37598104174ce0280eec64` (your correction commit on the request's head
`716b22a`). The review of the correction passed (`reports/correction-1-reviewer-report.md`, first
line `PASS a3152c9`; its Minor findings are not fixed in a correction and go to the request's list).

What to do: repeat the return step only for what the remark touches — the sentence of kind 17 of
`task-cycle/skill/request_template.md` for a refresh-only correction. Compare with the code the
entries that sentence touches (WAY-287, WAY-355, WAY-356 and the part-map entry of `task-cycle`) and
correct whatever no longer matches. Write nothing for behaviour merely because no entry covers it. No
row of *Settlements to record* is new. Where nothing needs a correction, commit nothing.

Report to `.runs/task-cycles/defects-found-after-merge/reports/correction-1-author-return-report.md`
under the headings of the record's *Return step* section (`task-cycle/record_template.md`):
foundation compared with code, decisions written or changed, invariants, environment facts, glossary
terms, part-map changes, projected entries, rows of *Settlements to record* written; then checks
with command and exit code, **Unread material** and **Searches not found or unclear** (each `none`
where none). Do not run the full gate (the orchestrator's). Return status, commits, a one-line check
result and the report path.
