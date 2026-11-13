# Handoff — the return step, `defects-found-after-merge`

Same delegation, worktree (`the task's worktree, which is the repository's root`),
branch and rules for commits as `reports/author-handoff.md`. Stage: the return step (step 11 of
`implement-task`), by the one author resumed. It is no variant of a row of `make-change`; read
`task-cycle/skill/return_step.md` and, since the return step writes as the foundation step writes,
`task-cycle/skill/foundation_step.md`, each whole, and the skill of an element when you write an
entry of that element.

Head now: `6d3298b8c440002471c68198ae782a807331627f` (range from the base
`6814c6f6c9ff2b29d34612fa5cc86945ec3a2812`: your four commits and the fix). The review of the whole
change passed (`reports/reviewer-report.md`), and the review of its Minor fix passed
(`reports/reviewer-fix-report.md`).

What to do: compare with the code the entries the change writes or changes (WAY-353 to WAY-357,
WAY-287), those the task names under *Decisions in play* and the part map entries of `project-level`,
`task-cycle` and `process-audit`, and correct in the same change whatever no longer matches. Write
nothing for behaviour merely because no entry covers it. The task's rows of *Settlements to record*
are already written (your foundation step); say in the report which row each entry carries and that
none is missing. Where nothing needs a correction, commit nothing.

Report to `.runs/task-cycles/defects-found-after-merge/reports/author-return-report.md` under the
headings of the record's *Return step* section (`task-cycle/record_template.md`): foundation
compared with code, decisions written or changed, invariants, environment facts, glossary terms,
part-map changes, projected entries, rows of *Settlements to record* written; then checks with
command and exit code, **Unread material** and **Searches not found or unclear** (each `none` where
none). Do not run the full gate (the orchestrator's). Return status, commits, a one-line check
result and the report path.
