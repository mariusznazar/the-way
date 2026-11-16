# Handoff — review of the fix of the whole-change review's findings

You are the reviewer of the whole change, resumed (`the-way-stage`, model `opus`). You review the fix range once.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`.
- Method: `task-cycle/review/SKILL.md`; your variant is the review of a fix — read `task-cycle/review/fix.md` whole and follow what it reads and what bounds the review.
- Range of the fix: from the reviewed head `b64608400f4fb55bb5508f71e2c4c2aadbcd6a60` to `1b03ef71fb4fbd634282b6a9123913c06c0387e6` (two commits: `33c98c2` the move out of `process-audit/audit_count.py` into `process-audit/stage_pricing.py`, `1b03ef7` the other fixes). Compute the diff yourself.
- Findings file the fix was given: `reports/review-whole-findings.md` (full path `docs/task-cycles/ci-replaces-local-final-gate/reports/review-whole-findings.md`) — your own blocking findings I-1 … I-4 and Minor M-1 … M-3, in your words.
- The author's fix report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-fix-report.md` (claims to verify, not evidence). Points it asks to be judged: that the move commit stands after the reviewed commits (not first) as WAY-365 words it; the source chosen for step 4's list (the merged request's *Checks*); the part of I-2 it holds not possible (the time of a fallback local run reaches no committed copy) with what the audit then shows; the added `the cycle's` sentence in WAY-160; M-2 only as text for the human action.
- Task and foundation: the frozen task `docs/task-cycles/ci-replaces-local-final-gate/task.md` and the foundation entries you already selected; trust boundary is **yes** as before (`process-audit/audit_count.py` was edited again by the move; `process-audit/stage_pricing.py` is new — judge whether it enters the part map's trust boundary and whether its tests and invariants still hold). Irreversible operation: no.
- Do not run the product's full gate. Single directories with `python -B gate/run_tests.py <directory>` and `python -B elements/common/foundation_check.py` are yours to run, with command and exit code.
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/review-fix-report.md`, first line `PASS <sha>` or `FAIL <sha>` (head `1b03ef71fb4fbd634282b6a9123913c06c0387e6`), with the checks you ran, **Unread material**, **Searches not found or unclear**, the working copies line. Only a new Critical or Important finding in the fix fails this review; a remaining or new Minor finding does not.
- Your directory for working copies: `.runs/review-fix/`.

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
