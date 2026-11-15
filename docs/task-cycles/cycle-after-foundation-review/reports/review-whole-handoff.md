# Handoff — review of the whole change

You review the whole change of a task cycle of the-way as an agent that did not make it. The person
who requested the cycle has delegated the intermediate choices to the orchestrator; nothing you or
the orchestrator say is that person's approval. You review read-only: you change no file of the
worktree and make no commit.

- Worktree (your working directory, the root of the repository):
  `.`, branch
  `task/cycle-after-foundation-review`.
- Method: read `task-cycle/review/SKILL.md` whole; for the review of the whole change it names
  `whole_change.md` — read it when the step that names it comes. You select your own foundation and
  guidelines, as that method gives (the-way has no `guidelines/` directory).
- What is reviewed: the whole change. Range: base `739c8139bc7f2e74ef0f4c2f0a76a4352614cfd6` to head
  `6727b67` (one commit by the one author; the route has no plan and no slices, so the review of the
  whole change is the only review of the code).
- The frozen task, read whole: `.runs/task-cycles/cycle-after-foundation-review/task.md` (a
  `ready for cycle` task; its *To do* items 1–11 and its 7 accepted rows of *Settlements to record*
  are what the change must carry out; its *Decisions in play* name the entries it touches). No spec
  and no plan exist: the task leaves no open design choice.
- The author's report: `.runs/task-cycles/cycle-after-foundation-review/reports/author-report.md`.
  It is a set of claims to verify, not evidence.
- Answers of the orchestrator at the start: the change touches no trust boundary; it holds no
  operation that cannot be undone (it words rules about a script that removes directories, and
  changes neither the script nor its run).
- The task moved no pin; no earlier review exists, so there are no Minor findings of slice reviews
  to carry.
- The change is the one of a one-author route: no slice had a review of its own, so you judge the
  whole of it.
- The product's gate is the orchestrator's run, not yours; run only the checks your review needs
  (`python -B elements/common/foundation_check.py`, the tests of one directory with
  `python -B gate/run_tests.py <directory>`), never the whole gate without a directory.
- Agent directory for working copies: `.runs/review-whole/` — and the directory for the index of your
  selection of decisions.
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/review-whole-report.md`. Its
  first line is `PASS <sha>` or `FAIL <sha>`.

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

Status as the first line of your report, then graded findings, the checks you ran with command and
exit code, **Unread material** (what this handoff names or your own selection left unread or read in
part, or `none`) and **Searches not found or unclear** (each thing looked for and not found or
unclear, or `none`), your count of decisions read whole (WAY-150), and your working copies. Return
the short result with the report's path.
