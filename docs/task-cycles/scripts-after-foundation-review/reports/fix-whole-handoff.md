# Handoff — the fix of the Minor findings of the review of the whole change

You fix the Minor findings within the task that the review of the whole change listed (`make-change`, variant: **the fix of a review's findings**; read `task-cycle/change/fix.md` and `task-cycle/change/SKILL.md`). You are a fresh agent on the same branch (the change was made by many executors; none is resumed). Findings, in the reviewer's words: `reports/whole-findings.md` (in `.runs/task-cycles/scripts-after-foundation-review/`). Worktree `the root of the task's worktree`, branch `task/scripts-after-foundation-review`, head `84d062b817e2f8ba1cf141c0f9140cd5f178f61c`; the fix's range runs from it. Frozen task `.runs/task-cycles/scripts-after-foundation-review/task.md`, spec `spec.md`, plan `plan.md` beside; the review report `reports/review-whole-report.md` holds each finding's place and evidence.

- Fix **M1 to M7** as their remedies say, each in the place it names; nothing else (no other change to make the code better). Where a finding's remedy leaves a choice, make the smallest change and name it in your report.
- M1 and M3 change decisions (`foundations/decisions.md`, WAY-339 and WAY-344): follow `elements/decisions/skill/SKILL.md` and the template it names (edit in place, WAY-07; no history in the entry), read WAY-339 and WAY-344 whole first, and run `python -B elements/common/foundation_check.py --skip-test-citations` after the edit (exit 0). The meaning of an approved decision does not change: M1 states the rule the code and its test already follow; ask `questions` if you find it would change a meaning.
- M2 touches `elements/common/foundation_check.py` (another task changes it in parallel; the cycle that merges second reconciles): change only the words the finding names, as the foundation step did for the foundation files ("whose name does not end in `.md`" and the like); no behaviour changes.
- M5 changes `task-cycle/cycle_stages.py`: refuse a count longer than a stated number of digits as "not a whole number" (exit 2, as the other missing or malformed counts), the limit taken from how `process-audit/audit_count.py` bounds the same counts (`TOKEN_DIGITS`), and a test first (red on the head, green after).
- M7: rewrap the lines the finding names to the width the file uses; touch no other line.
- Run the affected checks again and list each with command and exit code: `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`, `"test_cycle_measures.py"`, `"test_private_paths_check.py"`, `"test_tracked_private_paths_check.py"`, `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` and `"test_audit_series_scripts.py"`, `python -B gate/run_tests.py elements/common`, `python -B gate/run_tests.py instruction-files`, `python -B gate/run_tests.py agent-instructions`, `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`. No run of the whole gate (WAY-160). Start no background watcher or wait-timer.
- Commit in English by path (one commit per concern is fine), nothing under `.runs/`. Report to `reports/fix-whole-report.md`: the commits, for each of M1–M7 what you changed and where, the checks, the own-work check, **Unread material**, **Searches not found or unclear**, the working copies line (directory `.runs/fix-whole/`; remove your copies and every log).
- Answer with evidence a finding you hold wrong. Do not touch the findings outside the task's scope.

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
