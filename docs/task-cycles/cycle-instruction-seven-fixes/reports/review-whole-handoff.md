# Handoff — the review of the whole change

You review, as an agent that did not make it, the whole change of one task of the-way, made by one author without a plan. You are read-only: you change no tracked file and make no commit.

## Delegation

The person who requested this cycle has delegated the intermediate choices to the orchestrator. Never label an answer as that person's approval. You return at your boundary: you ask no human; a question goes to the orchestrator in your report.

## Where you work

- Worktree: `the root of the repository`, branch `task/cycle-instruction-seven-fixes`. The-way is this worktree; `<the-way>` below is its root. Read from it only.
- The range to review: base `0b43a27d` to head `bcaddc2b` (3 commits: `2a0df03c`, `fc88ee2c`, `bcaddc2b`). Compute the diff yourself: `git diff 0b43a27d..bcaddc2b`, `git log 0b43a27d..bcaddc2b`; confirm that `git rev-parse HEAD` is `bcaddc2b`.
- The directory for your working copies: `.runs/review-whole/` of the worktree.
- Your report: `.runs/task-cycles/cycle-instruction-seven-fixes/reports/review-whole-report.md`. Its first line is `PASS <sha>` or `FAIL <sha>`, or `questions`. If your harness refuses that write, return the report whole as your answer.

## Your method

Read `<the-way>/task-cycle/review/SKILL.md` whole. Your variant: **the review of the whole change**; it names `whole_change.md` for what you read and check besides section 2: read that file and follow it. Read another file it names only when the step or variant that names it comes.

## What you are given

- The frozen task, whole: `.runs/task-cycles/cycle-instruction-seven-fixes/task.md` (its *To do* points 1–7 with sub-points, its *Questions to settle*, *Decisions in play* and *Settlements to record* rows 1–3). The task gives the wording of each change; judge fidelity to it word for word. The rejected variants under *Questions to settle* are not to be restored.
- The author's report: `.runs/task-cycles/cycle-instruction-seven-fixes/reports/author-report.md` — a set of claims to verify, not evidence.
- The route: one author without a plan, so there are no slices and no slice reviews; the review of the whole change is the only review of the change. No spec was written.
- The answers at start: no trust boundary touched; no irreversible operation. The task did not move the pin: the-way's pin is itself.
- Two choices of the author that the orchestrator accepted provisionally and that you judge: (a) a file that *Read* names both whole and by ranges counts whole in `task-cycle/slice_size.py`; (b) the ways "only the skill, the decision unchanged" (WAY-136's source) and "only the two skills" (WAY-255's source) stay out of those decisions' *Rejected* as ways of the process, which the sentence of point 5 keeps out; and the author's addition to the *Verification* and *Rationale* of the three decisions, and the extension of the *Rejected* of WAY-136.
- Unread material of the author (parts of WAY-316, WAY-148, WAY-140 and WAY-03): you select your own foundation, so read what your selection and the change need.
- No full gate has run on this tree and none is run before the request opens; the product's final gate is the CI run on the request. The author ran focused checks (see its report). You may run focused checks yourself (`python -B gate/run_tests.py <directory>`, `python -B elements/common/foundation_check.py`) and mutations in your own working copy; run no full gate.

## What you read

You select your own foundation and guidelines, as `task-cycle/review/SKILL.md` and `whole_change.md` give. The parts the change touches: `task-cycle` (the four skills, `task-cycle/slice_size.py`, `task-cycle/test_slice_size.py`) and `decisions` (`elements/decisions/template.md`, `foundations/decisions.md`). The decisions in play: WAY-136, WAY-255, WAY-134 (changed), WAY-140, WAY-316, WAY-373, WAY-148 (unchanged). Do not read `foundations/decisions.md` whole; use the index script.

`cycle.md` and the other files of the cycle's record directory — other agents' handoffs and reports — are not yours to read unless this handoff names them. It names the frozen task and the author's report.

## Working copies (word for word)

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

(Your directory is `.runs/review-whole/`. Remove a copy by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.)

## Your return

Return your status (the first line of the report), the report's path, a one-line check result naming what failed or did not run, your questions and concerns, your **Unread material** and **Searches not found or unclear** (each `none` where there is nothing); all of them stand in the report as the method gives.
