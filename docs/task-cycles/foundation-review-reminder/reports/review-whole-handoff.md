# Handoff — review of the whole change

Stage: the review of the whole change of one task, by an agent that made none of it.

Method: read whole `task-cycle/review/SKILL.md` and follow it; read a file it names, `whole_change.md` beside it included, only when the step that names it comes. Variant: the whole change. Your first line is `PASS <sha>` or `FAIL <sha>` as the method gives.

## Delegation

The person who requested this cycle has delegated the intermediate choices to the orchestrator. Your questions go to the orchestrator, in your report. You are read-only: you change no tracked file, make no commit and run no full gate (`python -B gate/run_tests.py` without a directory); a check of your own that only reads, or runs the tests of one directory from your own working directory, is yours to run.

## Where you work

- Worktree, which you read from its root: `the task's worktree`, branch `task/foundation-review-reminder`. This repository is the-way itself; no product pins it here. Read every file from this worktree, never from `the main checkout of the repository`.
- Range to review: base `ff88ca3bc6beae07dbe1ee5adb1792773d28bcac` (head of `foundations` at the start) to head `b7ec371`; three commits: `f96ddd2`, `c0ba78b`, `b7ec371`. Read the full diff of the range.
- Your directory for working copies: `.runs/review-whole/` of the worktree.
- Your report: `docs/task-cycles/foundation-review-reminder/reports/review-whole-report.md`.

## What the change carries out

- The frozen task, which you read whole: `docs/task-cycles/foundation-review-reminder/task.md` (Polish; the task document is the source; its five points of *To do* and the five rows of *Settlements to record* are what you check coverage of, with its *Out of scope*).
- Route: one author without a plan, no spec, no slices; so no slice had a review of its own and there are no Minor or out-of-scope findings of earlier reviews to carry. The task did not move any pin: this is the-way itself.
- The author's report: `docs/task-cycles/foundation-review-reminder/reports/author-report.md`. It names the entries the author wrote, with their marks (`row <n>`), its choices with the ways rejected, and two additions it made beyond the task (its choices 6 and 7). Check each against the task and the foundation yourself; the orchestrator has graded neither and decides nothing on them.
- Answers of the orchestrator at the start: trust boundary — no (no file of the change is one the part map lists as such); irreversible operation — no.

## What the orchestrator did not settle for you

- The author's report states that it read in part, and left the end unread of: WAY-161 (end of *Rejected*), WAY-150 (the rest of *Verification*), WAY-344 (the rest of *Verification*) and WAY-107 (the end of *Rationale*). You select and read your own foundation; open whole each of these four only if the change bears on it, and say in your report which you opened.
- The author asked which name the review's line must hold; it wrote "the repository's name as the product's `## Backlog` section of the root `AGENTS.md` names the product". The orchestrator kept that wording (record row Q4); judge it against the task's point 1 and question 3.
- The author's `THRESHOLD` comment gives the rhythm for 60 merges as "every 2 to 10 weeks in the-way", while the task's *Context* says "od 2,5 do 10 tygodni"; the author's reckoning is 60 / 26 = 2.3. Judge it.

## What you read

You alone among the reviewers select your own foundation and guidelines (WAY-150, WAY-213): the parts the change touches are `decisions`, `task-cycle` and `foundation-review`, and the root `README.md`, which the part map leaves out on purpose. WAY-328 departs, for the-way's own code and tests, from a product's coding and testing guidelines. Write the index of your selection of decisions as `way_of_working.md` "Reading the foundation" gives, into `.runs/review-whole/`, and state in your report how many decisions you read whole. The decisions the task's *Decisions in play* names are WAY-24, WAY-300, WAY-140, WAY-161, WAY-107, WAY-36, WAY-22, WAY-293, WAY-328 and WAY-344.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## What you return

Your report's first line, your commits (none), a one-line check result naming what failed or did not run, and the path of your report. In the report: the changed files with their added and removed line counts, your coverage of every point of *To do* and every row of *Settlements to record*, your **Unread material** (your own selection included), your **Searches not found or unclear**, the number of decisions you read whole, and your working copies.
