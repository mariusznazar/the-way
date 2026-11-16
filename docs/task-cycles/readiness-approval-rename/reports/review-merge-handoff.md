# Handoff to the reviewer of the reconciliation with the target branch

**Delegation.** The person who requested this cycle has delegated intermediate choices to the
orchestrator; nothing the orchestrator says is that person's approval. Put questions in your report
(first line `questions`). You are read-only on the branch; do not run the full gate
(`python -B gate/run_tests.py` without a directory).

**Worktree.** `the task's worktree (the repository's root)`. Method: `task-cycle/review/SKILL.md`
(`review-change`), read whole; a file it names only when the step that names it comes.

**What happened.** The change (the rename of the projected meaning of `gate`, of the locations-file and
backlog-line meanings of `entry`, of `read off`, and the glossary entry `projected entry`) was reviewed
and passed at head `cef14df7d49d57e40cd3c20dc77ea48e83e2a259` (range from the base
`4758840fbaf9562db960965c706d8681c3d23a43`). Meanwhile `origin/foundations` moved to `bec6c3d2` (the merge
of pull request #147, the task `agent-test-bypass`: WAY-409, WAY-410, WAY-100/WAY-134 narrowed,
three environment facts, edits to `task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`,
`task-cycle/review/fix.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`,
`task-cycle/skill/request_template.md`, `project-level/task/*`, `elements/decisions/template.md`,
`elements/common/skill/task_variant.md`). The orchestrator merged it into the task branch with no
conflict: merge commit `50bc1993620fa5ce6d0ef729d92b572b7c2bd886`. No decision of this task is new (it only
edits decisions), so no renumbering was made.

**Range to review.** `cef14df7..50bc1993` — the merge. Review the merge itself: the
files that both sides changed are `foundations/decisions.md` and `task-cycle/skill/SKILL.md`; the others
came from the target alone. Ask: do the two sides still hold together?
- Does any text the target brought in, in English, use a moved word in its old meaning — projected `gate`
  ("readiness gate", "gate record", bare "the gate" for the approval of a project definition, `ready for gate`),
  "entry" for a key of the locations file, "backlog entry" for a task's line — which this task's To do 2, 9
  and 10 would have renamed (the task: `.runs/task-cycles/readiness-approval-rename/task.md`, whole)? The
  orchestrator's grep of the old phrases finds none; judge the bare uses by meaning, in WAY-409, WAY-410, the
  narrowed WAY-100 and WAY-134, the three new environment facts and the edited files above.
- Does a sentence the target brought in rely on something this task removed or renamed (the heading
  `## Gate record`, the status `ready for gate`, the invariant `project-readiness-gate`, the file
  `project-level/skill/readiness_gate.md`, Python names `GATE_RECORD`, `check_gate_record`)?
- In `foundations/decisions.md` and `task-cycle/skill/SKILL.md`, does each side's text stand whole where
  the merge joined them (no lost line, no doubled line, no change of meaning)?
- Foundation entries the merge brought in that bear on the parts this change touches (WAY-150): WAY-409,
  WAY-410, WAY-100, WAY-134 (also in this task's *Decisions in play* as carrying `projected entry`), and the
  environment facts added to `foundations/environment_facts.md`; read each whole.
- Run `python -B elements/common/foundation_check.py` (the orchestrator got exit 0, "0 errors") and the
  focused checks that the merged files bear on: `python -B gate/run_tests.py task-cycle`,
  `project-level`, `elements/common`, `elements/decisions` (state each command and exit code); and
  `python -B agent-instructions/skill_entry_points.py` (the entry points must be current).
Trust boundary: yes (as before); the merge touches no file of it beyond what the task already changed.

Report to `.runs/task-cycles/readiness-approval-rename/reports/review-merge-report.md`; first line
`PASS <sha>` or `FAIL <sha>`; blocking findings (Critical, Important), Minor findings, those outside the
task apart; **Unread material**; **Searches not found or unclear** (`none` if nothing); working
copies (directory `.runs/review-merge/`; removed before return, say so). Return only the first line, a
one-line check result and the report path.
