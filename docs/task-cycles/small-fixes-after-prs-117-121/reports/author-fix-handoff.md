# Handoff — the fix of a review's findings (task slug `small-fixes-after-prs-117-121`)

You are the one author of this change, resumed for the fix of the findings of the review of the
whole change. The orchestrator dispatches you; the person who started the cycle delegated its
intermediate choices to the orchestrator, so nothing here is the human's approval. Ask the human
nothing.

- Worktree: `the task's worktree`, branch `task/small-fixes-after-prs-117-121`, reviewed head `e9aea95`. Your fix's range runs from that head.
- Method: `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**; read `task-cycle/change/fix.md` as it says.
- Findings file (the reviewer's words): `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-whole-findings.md` — two blocking findings (I1, I2) and the Minor findings m1–m8 within the task. The reviewer's full report, for the places and evidence it cites: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-whole-report.md`. Fix all of them: the Minor ones too (the cycle fixes the Minor findings of the whole-change review within the task before the request opens). Finding `o1` is outside the task's scope: do not fix it.
- Where you hold a finding wrong, answer it with evidence in your report instead of changing the file; a suggestion of the reviewer is a suggestion, the wording of the fix is yours, the smallest that removes the finding.
- I2 is no change of a commit: the marks of WAY-139, WAY-344 and WAY-60 in your report's table "Entries written" are wrong by the rule you wrote in `task-cycle/skill/foundation_step.md`. In your fix report give a corrected table: those three entries marked `the cycle's`, each with the added pair(s) of examples word for word (the *complies* and *violates* sentences) and the one English and one Polish sentence of the entry's meaning, as before. For WAY-139 mark only the entry as `the cycle's` once; keep the mapping to row 1 stated beside the mark. The orchestrator carries the corrected table into the request. Where the fix of m1 changes one of these pairs, the corrected table holds the changed text.
- I1: the fix includes the test for the third form of the quotation (`„…”`, opening U+201E, closing U+201D) and its failing run before the code, as for your earlier tests; the docstring and the template wording name the third pair too.
- Do not run the full gate (the orchestrator's). Run the focused checks of what you change, with their commands and exit codes, and `python -B elements/common/foundation_check.py`. Commit by explicit paths, English messages, no push. Your own-work check, **Unread material** and **Searches not found or unclear** come in the report as before.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/author-fix-report.md`. Your directory for working copies is the one you had, `.runs/author/`.

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
