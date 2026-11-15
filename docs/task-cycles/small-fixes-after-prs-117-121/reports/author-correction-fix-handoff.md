# Handoff — the fix of the review of correction 1 (task slug `small-fixes-after-prs-117-121`)

You are the one author, resumed for the fix of the blocking finding of the review of your correction.
The orchestrator dispatches you; nothing here is the human's approval; ask the human nothing.

- Worktree: `the task's worktree`, reviewed head `5cb2e1f`. Your fix's range runs from it.
- Method: `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**; read `task-cycle/change/fix.md` as it says.
- Findings file (the reviewer's words): `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-correction-findings.md` — one blocking finding, I1. The reviewer's full report: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-correction-report.md`. The reviewer's Minor findings m1 and m2 are not yours to fix.
- I1 needs no commit by the reviewer's words: the fix is a corrected account in your fix report. Give in it WAY-114's mark as `the cycle's` (the entry changed by the correction, with a pair of examples you wrote: the two clauses the findings quote), the two clauses word for word as `foundations/decisions.md` holds them at `5cb2e1f`, and one English and one Polish sentence of the meaning of what the correction changed in WAY-114, in the form your earlier tables used. If you hold the finding wrong, answer with evidence and change nothing. If the check of the clauses against the file finds the quoted wording differs from the file, say so.
- Do not run the full gate. Run no checks that do not apply; where you change no file, say so and that no check ran.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-fix-report.md` (**Unread material**, **Searches not found or unclear**, own-work check, working copies as before). Directory for working copies: `.runs/author/`.

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
