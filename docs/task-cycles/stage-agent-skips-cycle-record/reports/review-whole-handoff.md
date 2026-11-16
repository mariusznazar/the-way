# Handoff — review of the whole change

Stage: the review of the whole change, as an agent that did not make it. You are read-only: you change no tracked file and make no commit.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Never label an answer as that person's approval. Where you need an answer, return `questions` with the question in your report.

## Where you work

- Worktree (your working directory): `the root of the task's worktree`, branch `task/stage-agent-skips-cycle-record`.
- Range: base `3cbaeb9ff188b77c8a96c4f3194db07e8a8a2898` to head `de24e5b8` (one commit by the one author; there was no plan, no spec and no slice, so no slice had a review of its own — you judge the whole change). Compute the diff yourself and confirm that `git rev-parse HEAD` is the head you were given.
- Your directory for working copies: `.runs/review-whole/` of the worktree.
- Your report path: `.runs/task-cycles/stage-agent-skips-cycle-record/reports/review-whole-report.md`

## Method

Read `task-cycle/review/SKILL.md` whole, for the review of the whole change; it names `whole_change.md`, which you read when it tells you to. You select your own foundation and guidelines as it gives.

The cycle record directory `.runs/task-cycles/stage-agent-skips-cycle-record/` holds the cycle's log (`cycle.md`) and the files of other agents. `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not yours to read unless this handoff names them. This handoff names two: this handoff and the two files below.

## What you are given

- Answers of step 4: trust boundary — no; irreversible operation — no; no open design choice; route — one author without a plan. Checks failing on the base: none.
- The frozen task, to read whole: `.runs/task-cycles/stage-agent-skips-cycle-record/task.md`. Check every item of its *To do*, each settlement row of *Settlements to record* and each of its *Decisions in play*, and source fidelity of what the change writes against the task's *Questions to settle*.
- The author's report (claims to verify, not evidence): `.runs/task-cycles/stage-agent-skips-cycle-record/reports/author-report.md`. Its **Unread material** says it did not read `elements/decisions/examples.md` and `foundations/part_map.md` whole; judge the form of the decision entry against the element's template and examples yourself. Its **Searches not found or unclear** says the line the task cites for the skill sentence ("ending 'and the report path.'") no longer matches the file; judge whether the place the author chose is right.
- Minor and out-of-scope findings of earlier reviews: none.

## Checks

You may run focused checks of the directories the change touches and `python -B elements/common/foundation_check.py`. No handoff tells an agent to run the product's gate and you run none. Give each check with its command and exit code.

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

## Your return

Write the full report to your report path as `review-change` gives it; its first line is `PASS <sha>` or `FAIL <sha>`. Include **Unread material** and **Searches not found or unclear** (each `none` or the items) and the working copies line. Return the first line of the report, the one-line result of the checks, and the report's path.
