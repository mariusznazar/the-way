# Handoff — the fix of the correction review's finding (resumed one author)

You are resumed as the one author of this cycle, for the one fix the review of the correction
allows. The orchestrator's delegation and answers in `reports/author-handoff.md` stand. Nothing here
is a human's approval beyond what the remarks file quotes as his words.

- Variant of `make-change`: **the fix of a review's findings**. Read that part of
  `task-cycle/change/SKILL.md` again.
- Worktree: `the task's worktree root`, branch
  `task/backlog-line-for-plan-tasks`, reviewed head `047a9e7606e90dc164762bebb0c6bc48dcd46eeb`, tree
  clean. Your commit goes on top; the fix's range runs from that head. Never touch `docs/task-cycles/`.
- Findings file, the reviewer's words, copied without change:
  `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-fix-findings.md` — one blocking
  finding (B1). The reviewer's full report for the evidence:
  `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-review-report.md`. The three Minor
  findings of that report are **not** yours; do not fix them.
- The orchestrator's choice between the reviewer's two fixes: the first. WAY-154 gives the refiner
  the write the skills already carry — the refiner also brings the lines of the tasks tied to it
  into agreement with the plan's dependencies as the rules of the task place give — in its second
  binding sentence, in its *Verification* (a *complies* and a *violates* example) and in its
  *Rationale*'s accepted risk (lines of other tasks are written by a refiner, which the accepted
  race now also covers). The reason: the human's rule of item 1 says that a refiner that knows from
  the plan that one task depends on another brings the lines to agreement, whichever line it is;
  that is a write to the line of another task, and WAY-154 is the entry that says who writes what.
  What stays out of the-way is unchanged: how a line is handled (find it, one to a task, which
  fields, read before write, the clash) stays the task place's rules; do not write any of it into
  WAY-154 or a skill.
- Keep WAY-154 within one to three binding sentences, and no line you write longer than 100
  characters. Mark per the foundation step; the added write is the human's remark at the request, so
  the step's mark for it is `the cycle's` as for the added rule in WAY-107; name the human's remark
  as its source in your report, not in the entry. Edit in place (WAY-07).
- Then the return step again for what this fix touches: compare WAY-154 with the four skill files and
  `task_line.md`, and WAY-107, WAY-329 and the part map with the files; correct what no longer
  matches; say in the report what you compared and what you found, or `none`.
- Checks, each with command and exit code: `python -B elements/common/foundation_check.py`,
  `python -B instruction-files/check_instructions.py .`,
  `python -B task-cycle/test_tracked_files_private_paths.py`. Not the `project-level` directory and
  not the full gate.
- Commits: explicit paths, English messages.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-fix-report.md`
  — the finding as fixed (commit and place) or contested (evidence), the return step's comparison,
  **Unread material**, **Searches not found or unclear**, your own-work check (the requirement most
  likely unmet: that no skill file gives a refiner a write WAY-154 does not give it; run a check that
  would catch it, command and exit code), the checks, any reach beyond this handoff. Return status,
  commits, a one-line check result and the report path.
