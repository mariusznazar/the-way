# Handoff — the return step, repeated for the correction

Stage: the return step again (step 11 of `implement-task`), for what the human's remarks touched,
by the one author resumed. Read `task-cycle/skill/return_step.md` whole.

- Worktree and branch as before; head `c8bf864ff75c2575be9d692906c552f0087ea06f` (the correction,
  reviewed: PASS; the orchestrator's full gate passed on it: exit 0, 804 tests).
- The remarks (bind): `docs/task-cycles/decisions-as-material-at-refinement/reports/correction_remarks.md`.
- Repeat only what the remarks touch: compare WAY-113 as it now stands (binding sentence,
  *Verification*, *Rationale*, *Rejected*) with `elements/common/way_of_working.md` "How a skill
  asks", `project-level/technology/settle.md` sub-step 6, `elements/common/skill/task_variant.md`
  step 4, `elements/common/skill/definition_variant.md` step 4, `project-level/lead/skill/SKILL.md`
  step 5 and `project-level/task/skill/orchestrated_mode.md`, and with the entries that link to it;
  correct in the same change whatever no longer matches. Last time you found nothing and the review
  of the fix then named the stale *Rationale*: read the whole entry sentence by sentence this time.
- Commit only if you correct something (by path, English message, clean worktree); say so if you
  do not. Run `python -B elements/common/foundation_check.py` after any edit. No full gate.
- Report: `docs/task-cycles/decisions-as-material-at-refinement/reports/return_correction_report.md`
  in the worktree, under the headings of the record's *Return step*, with checks (command, exit
  code), reaches and **Searches not found or unclear**. Return only status, commits (or none), a
  one-line check result and the report path.
