# Handoff — review of the fix of the whole-change review (task slug `small-fixes-after-prs-117-121`)

You reviewed the whole change (`review-whole-report.md`, `FAIL e9aea95`); you are resumed to review
its fix once. The orchestrator dispatches you; nothing here is the human's approval; ask the human
nothing.

- Worktree: `the task's worktree`, branch `task/small-fixes-after-prs-117-121`. Range of the fix: base `e9aea95` (the head you reviewed), head `eaf815c` (confirm `git rev-parse HEAD`). Two commits: `b23275b`, `eaf815c`.
- Method: `task-cycle/review/SKILL.md`, the review of a fix; read `task-cycle/review/fix.md` as it says.
- Findings the fix answers, in your words: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-whole-findings.md` (I1, I2, m1–m8; `o1` was outside the scope and is not fixed).
- The author's fix report, a set of claims to verify: `docs/task-cycles/small-fixes-after-prs-117-121/reports/author-fix-report.md`. For I2 it changes no commit: it gives a corrected table of entries written, with WAY-139, WAY-344 and WAY-60 marked `the cycle's`, which the orchestrator carries into section 6 of the request description; judge that table against the added pairs in the files.
- Bounds: judge whether each finding of the findings file is removed, and whether the fix introduces a new Critical or Important finding (only such a finding fails this review); a Minor finding that remains or that you find new goes to the request's list, graded and marked as within or outside the task's scope. Keep to the fix range; the rest of the change you already judged.
- No full gate (the orchestrator's run). Focused checks and `python -B elements/common/foundation_check.py` are yours to run in your own working copy where needed.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-fix-report.md`, first line `PASS <sha>` or `FAIL <sha>`. Your directory for working copies: `.runs/review-whole/` as before (or `.runs/review-fix/`, named in your report).

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
