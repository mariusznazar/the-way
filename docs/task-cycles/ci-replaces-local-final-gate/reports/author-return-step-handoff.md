# Handoff — the return step (the one author, resumed)

You are the one author, resumed, for the return step. The person who requested this cycle delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`, head `1b03ef71fb4fbd634282b6a9123913c06c0387e6`; base `8f0c1c3e89c8e8151f64cf82a3b8bf07d004b999`. Do not push.
- Stage: the return step, and its boundary. Read `task-cycle/skill/return_step.md` whole and follow it, together with `task-cycle/skill/foundation_step.md` (the return step writes as the foundation step writes) and the `SKILL.md` of an element where you write an entry of it. The range the change made is `8f0c1c3..1b03ef7` (your three commits, the move and the fix).
- Frozen task: `docs/task-cycles/ci-replaces-local-final-gate/task.md` (*Settlements to record* rows 1–6 and *Decisions in play* bind what you compare and write).
- The reviews of the change (context, not instructions): `reports/review-whole-report.md`, `reports/review-fix-report.md`. Both ended in PASS; Minor findings left for the request's list are not yours to fix here, but a foundation entry that no longer matches the code is.
- Do not run the product's full gate (the orchestrator's alone, WAY-160); run only what the return step names, with command and exit code (`python -B elements/common/foundation_check.py` at least).
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-return-step-report.md`, in the form `return_step.md` gives, with **Unread material**, **Searches not found or unclear**, the working copies line. Return status, commits (none if nothing was corrected), a one-line check result, report path.
- Your directory for working copies: `.runs/author-return-step/`.

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
