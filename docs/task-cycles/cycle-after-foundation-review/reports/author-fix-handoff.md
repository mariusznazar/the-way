# Handoff — the fix of the Minor findings of the review of the whole change

You are the one author, resumed. The review of the whole change returned `PASS` with two Minor
findings within the task; the cycle fixes them once before the request opens (WAY-161, WAY-162). The
person who requested the cycle has delegated the intermediate choices to the orchestrator; nothing
you or the orchestrator say is that person's approval.

- Worktree: `.`, branch
  `task/cycle-after-foundation-review`, reviewed head `6727b67`. The range of the fix runs from there.
- Method: `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**; read `fix.md`
  beside it as the skill gives.
- The findings file: `.runs/task-cycles/cycle-after-foundation-review/reports/whole-findings.md`
  (findings 1 and 2, in the reviewer's words; the reviewer's full report is
  `reports/review-whole-report.md`, which you read only where a finding needs its evidence). A
  third Minor finding of the review, marked outside the task's scope, is not yours to fix.
- The frozen task, as before: `.runs/task-cycles/cycle-after-foundation-review/task.md`. Do not
  widen the task: fix the two findings and nothing else. For finding 1 the reviewer names the fix:
  one clause in the sentence of *Findings outside the task's scope* of
  `task-cycle/skill/request_template.md`, saying where the task that fixes the flaky test, or the
  proposal of one, stands (name the test and the task that fixes it, or propose one — as WAY-261's
  second paragraph and `task-cycle/skill/SKILL.md` step 10 say it); keep the wording consistent with
  those two texts and with the template's own checks (`task-cycle/request_check.py` reads the
  template's items — run its tests). For finding 2 the reviewer names the fix: add "standing alone"
  after "a copy of a base" in WAY-375's sentence, keeping the quoted start the tests read intact.
  Where you hold a finding wrong, answer it with evidence in your report.
- Run again the checks the fix affects: `python -B elements/common/foundation_check.py` (full),
  `python -B gate/run_tests.py task-cycle`, `elements/common` and `agent-instructions`, with command and
  exit code. Do not run the whole gate (`python -B gate/run_tests.py` without a directory).
- Commit by path; leave the worktree clean; the lines you add stay within 100 columns (a table row
  excepted) and hold no absolute path.
- Agent directory for working copies: `.runs/author/`.
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/author-fix-report.md`.

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

Status, your commits, a one-line check result naming what failed or did not run, and the report's
path; in the report the checks with command and exit code, the own-work check, reaches, **Unread
material**, **Searches not found or unclear**, and working copies.
