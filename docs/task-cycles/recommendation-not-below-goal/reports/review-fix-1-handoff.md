# Handoff — the review of the fix (`review-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. No answer or go-ahead here is that person's approval. You are the reviewer of the whole change, resumed; grade and scope of every finding are yours.

## Where and what

- Worktree: `the task's worktree`, branch `task/recommendation-not-below-goal`. Read only.
- Method: `task-cycle/review/SKILL.md`, the review of a fix; read `fix.md` as it says and follow it.
- Fix range: from the reviewed head `7c2502a73f8360d9e47af85863c522392ec6c192` to `42298f2a81d8d4600b7a3769ab5ab6795510f0f6`. Compute the diff yourself and confirm `git rev-parse HEAD`.
- Findings the fix was given: `.runs/task-cycles/recommendation-not-below-goal/reports/review-whole-findings.md` (your own findings I1, I2 and M1, in your words). The author's fix report: `.runs/task-cycles/recommendation-not-below-goal/reports/author-fix-1-report.md` — claims to verify, not evidence. Frozen task: `.runs/task-cycles/recommendation-not-below-goal/task.md`.
- What the fix did, per the author: I2 and M1 fixed; I1 not changed, because the author found no passage of the accepted task or WAY-25 that gives the outcome of the collision with WAY-166, and returned it as a question for the human (the orchestrator does not settle it either, `task-cycle/skill/foundation_step.md`). Judge each: whether I2 and M1 are fixed without a new blocking finding, and whether I1 still stands exactly as you found it (it remains and goes to the human; do not ask for a fix of it here). A new Critical or Important finding that the fix introduces counts as one that remains; a new Minor finding does not block.
- Run no gate. Record each check you run with its command and exit code. `cycle.md` and the other files of the record directory are not yours to read.

## Report

Write the report to `.runs/task-cycles/recommendation-not-below-goal/reports/review-fix-1-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`. Return that line, your checks and the path. It holds **Unread material**, **Searches not found or unclear** (each `none` where nothing), the state of I1, I2 and M1 after the fix and, for every blocking finding, the mark `Contradiction: yes` or `no`. The report file is the input of the cycle's scripts; if the write is refused all the same, return the report whole.

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

Your directory for working copies: `.runs/review-whole/` (the same as before).
