# Handoff — review of the return step

You are a fresh reviewer, an agent that did not make this change, for the review of the range the
return step committed in a task cycle of the-way. No human is available during the cycle; return
`questions` to the orchestrator where you have one.

- Worktree: `the root of the worktree`, branch
  `task/weak-point-in-every-decision-question`. Method: `task-cycle/review/SKILL.md` (`review-change`),
  read whole; the review of the return step's range.
- Range: `d542af0..028b528` (one commit, `process-audit/SKILL.md` only, 13 insertions, 14 deletions).
  Read its full diff. The earlier range `bfb2e10..d542af0` was reviewed (whole-change PASS at
  `a3c97df`, fix PASS at `d542af0`); read `reports/review-whole-report.md` and `reports/review-fix-report.md`
  under `.runs/task-cycles/weak-point-in-every-decision-question/` for what is already judged.
- Against: the frozen task `.runs/task-cycles/weak-point-in-every-decision-question/task.md` (Polish),
  *To do* 7 and row 8 in particular, and the return step's report
  `reports/author-return-step-report.md`, read whole. The return step wrote no entry and no
  invariant; it removed from `process-audit/SKILL.md` the two path references to
  `elements/common/way_of_working.md` because the part map lets `process-audit` depend only on
  `task-cycle`, `project-level` and `gate`; the part map is unchanged. Judge: whether that removal is
  right by the part map's rules (`foundations/part_map.md`, the `process-audit` entry; the template
  of the part map's "Allowed dependencies"), whether the audit's text still carries *To do* 7 fully
  (the rule, the two untouched rules on returns and on the cost of an occurrence, the outcomes),
  whether the rewrap changed any wording, and whether the pointer "as 'How a skill asks' gives it
  (WAY-113)" alone is enough for an agent to find the section. You select your own foundation by
  "Reading the foundation" in `elements/common/way_of_working.md`.
- Answers of step 4 of the cycle: no trust boundary touched, no operation that cannot be undone.
- The product's full gate is the orchestrator's; do not run it. Run `python -B
  elements/common/foundation_check.py` and the focused `python -B gate/run_tests.py process-audit`
  if you need them.
- Directory for working copies: `.runs/review-return-step/`. Report path:
  `.runs/task-cycles/weak-point-in-every-decision-question/reports/review-return-step-report.md`,
  first line `PASS <sha>` or `FAIL <sha>`, with **Unread material** and **Searches not found or
  unclear**.

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
