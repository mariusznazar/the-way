# Handoff - the review of the fix of the whole-change review's findings

The same delegation, place, method (`task-cycle/review/SKILL.md`) and rules as
`reports/review-whole-handoff.md`; you are the same reviewer, resumed. Your stage: the review of
the fix, once.

- Worktree: `the task's worktree`. Read only.
- Range of the fix: `60561fba1ca0cbb4d0045f8f407c9cd3f5292d0e..15bf941a` (head of the fix; confirm with
  `git rev-parse HEAD`). Read the full diff of the range.
- The findings the fix answers: `reports/review-whole-findings.md` (your own findings, I-1, I-2
  blocking and M-1 to M-4 Minor), under `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/`.
- The author's fix report: `reports/author-fix-1-report.md` (same directory).
- Judge whether each finding is fixed, whether the fix changes anything the task does not settle,
  and whether it breaks something else (a restated rule left behind, a limit of the foundation
  check, a place that still says the old words). Only a new Critical or Important finding in the fix
  fails this review.
- Report path: `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/review-fix-1-report.md`;
  first line `PASS <sha>` or `FAIL <sha>`; the same sections as before (checks with command and exit
  code, **Unread material**, **Searches not found or unclear**, working copies). It is the input of
  `task-cycle/remarks_check.py`. Return its first line, a one-line check result and its path.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way`
populated, and the dependencies those checks need installed as the product's own rules give,
before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and
command of a probe that shows a finding among them, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

Your directory for working copies: `.runs/review-fix-1/`.
