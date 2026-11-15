# Handoff — review of correction 1

You are the reviewer of the whole change, resumed, to review a correction made for the human's
remarks on the request. You review read-only: no file changed, no commit. The person who owns the task
answered through the day's advisor, who acts for them; the remarks bind. Nothing you or the
orchestrator say is that person's approval.

- Worktree: `.` (the root of the repository; your working directory), branch
  `task/cycle-after-foundation-review`.
- Method: `task-cycle/review/SKILL.md`; for the review of a correction, read `fix.md` beside it and
  follow it (what you read and what bounds the review). The remarks stand in the place of a
  findings file.
- The range reviewed: `bd50b60` to `f92d9dd` (one commit by the one author; the target branch
  `foundations` has not moved from `739c813`, so no merge came in). Compute the diff yourself.
  `bd50b60` is the head of the earlier reviewed work plus the commits that add and remove the
  record's copy.
- The remarks, word for word: `.runs/task-cycles/cycle-after-foundation-review/reports/correction-1-remarks.md`.
  Remark 1 binds this correction: for a screenshot shown to the human, the rule that keeps it where
  the product's foundation settles it prevails over WAY-373, which keeps its reach over every other
  screenshot and every copy made to check something, recorded in the foundation's own form for one
  rule narrowing another. Remark 2 (WAY-138's missing source let through) asks for no change, and the
  range must hold none for it. Your own Minor finding 3 of the earlier review
  (`reports/review-whole-report.md`) is what remark 1 answers.
- The foundation entry the correction writes is WAY-316 (a third paragraph of binding sentences,
  *Relations*, *Rationale*). Judge it against WAY-25 and the decisions template (the form of
  precedence), against the remark, and against what you selected for the earlier review; read the
  entries you need whole; the author's report claims that WAY-373 and nothing else narrows each
  other and that the skill and `ui_check.md` already agree — verify, do not take it.
- The correction's report: `.runs/task-cycles/cycle-after-foundation-review/reports/author-correction-1-report.md`
  (claims to verify, not evidence). The frozen task:
  `.runs/task-cycles/cycle-after-foundation-review/task.md` (the correction does not widen it).
- Run only the checks the review needs; not the whole gate (the orchestrator's run).
- Agent directory for working copies: `.runs/review-whole/`.
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/review-correction-1-report.md`.
  Its first line is `PASS <sha>` or `FAIL <sha>`. The review ends as the end of a code review gives:
  a Minor finding of a correction is not fixed and goes to the request's list.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

## What you return

First line `PASS <sha>` or `FAIL <sha>`; graded findings; the checks you ran with command and exit
code; **Unread material**; **Searches not found or unclear**; working copies.
