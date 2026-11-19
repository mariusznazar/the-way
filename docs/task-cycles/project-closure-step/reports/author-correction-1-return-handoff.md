# Handoff — the return step after correction 1 (task `project-closure-step`)

You are the one author, resumed (same class), for the return step of correction 1, which repeats the part of
step 11 that the human's remarks touch. The correction is committed (`43e9c4a7`, `4101de84`; head
`4101de84`; built from `935109fb`); its review runs in parallel and only reads. Work in the same worktree and
branch (`the task's worktree`, `task/project-closure-step`), commit by path (English
messages) only if something no longer matches, and no full gate. Your directory for working copies is
`.runs/author/` (the paragraph on working copies in your first handoff holds). Report:
`.runs/task-cycles/project-closure-step/reports/author-correction-1-return-report.md`, with **Unread material**,
**Searches not found or unclear** and the line on working copies.

Read `task-cycle/skill/return_step.md` whole and `task-cycle/skill/foundation_step.md` whole, as for the first return
step. The remarks of the human that started the correction are in
`.runs/task-cycles/project-closure-step/reports/correction-1-remarks.md`; only the one that asked for work
(the check of a closed plan against a loop of "delivered by another task" rows, answered by commits
`43e9c4a7` and `4101de84`) is the correction's subject.

Compare with the code at the head `4101de84` what the correction touches: the invariant `project-plan-check`
(its sentence now reaches a closed plan whose deliveries never reach a done task), `project-plan-form`
(through the template), WAY-142 and WAY-411 to WAY-415 where they restate the closed plan's rule or the
closing's condition of start, the part map's entry of `project-level`, and the entries of the task's *Decisions
in play* where the closed plan's rule appears (WAY-146, WAY-153), each against `plan_check.py`,
`plan_state.py`, `closure.md` section 1, the lead skill's step 1, and the plan template. Correct in this change
whatever no longer matches, and nothing else. The Minor findings of the earlier reviews that the request lists
are no entries and are not yours to fix.

Judge whether the cycle's choice of this correction (Q5 of the record: the closing step also holds a row whose
chain of deliveries never reaches a done task, as it already holds a row delivered in a dropped task) binds
after the merge in a way the foundation must hold (WAY-36): where an entry already carries it, say which;
where it stands only as text of the step's file, say so, as for Q1 and Q3 in the first return step's report.

Report as the record's *Return step* gives it: the foundation compared with the code (what no longer matched and
its correction, or none); decisions, invariants, environment facts, glossary terms, part-map changes, rows of
*Settlements to record* written or changed, each marked `row <n>`, `projected` or `the cycle's` with one
sentence of its meaning in English and one in Polish, and any pair of examples you add quoted word for word.
Return your status, your commits (or that the step committed nothing), the one-line check result and the report
path. Where the step commits anything, a reviewer of the strongest class reviews its range.
