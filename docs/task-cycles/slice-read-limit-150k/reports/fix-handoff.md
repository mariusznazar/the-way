# Handoff — the fix of the whole-change review's findings

You are the one author, resumed for the fix. Variant of `task-cycle/change/SKILL.md`: "the fix of a review's findings". Worktree `the task's worktree root`, branch `task/slice-read-limit-150k`, reviewed head `888eb6150e13bee2337368114c4f1cd760b3d274`; your fix range starts there.

- Findings file (the reviewer's words): `reports/review-whole-findings.md` in `docs/task-cycles/slice-read-limit-150k/`. Finding 1 blocks; findings 2 to 5 are Minor within the task and are fixed too. Finding 6 (outside the task) is not in the file and is not fixed.
- Frozen task: `docs/task-cycles/slice-read-limit-150k/task.md`. The numbers you write come from its *Need* and *To do* only, and the reviewer's remark that the 21 000 figure belongs to "powyżej 150 tys." (above 150 000) and that the 25% belongs to the 20 slices binds the wording of both files alike.
- Orchestrator's rulings for the fix:
  - Finding 1: say "long runs of executors" (task's wording), never "longest"; attach the 25% to the 20 slices; the 21 000 figure on "above 150 000 tokens" in both the script's description and WAY-371; use the same sentence of the measurement in both where the numbers are the same.
  - Finding 2 (`CONTEXT_WINDOW_TOKENS` unused): the earlier handoff's choice 4 to keep it rested on a misreading — the task's point 2 replaces only the "quarter" sentence and does not forbid removing the constant. Remove the constant and its docstring bullet together only if nothing else uses them (search the repository outside `.runs/`); `CHARACTERS_PER_TOKEN` and its source stay, and the source's quotation of the window stays only if it is still needed to explain the characters-per-token estimate, otherwise cut to what the estimate rests on. If you judge removal wrong, answer with evidence instead.
  - Finding 3: rewrite the sentence so it states what is true of both limits now.
  - Finding 4: keep in the entry's binding text only what row 2 settles (the value and what the script reports); leave the conversion in the script's description where it already stands, unless your search shows a reason to keep it.
  - Finding 5: as the reviewer says.
- Run the affected checks again: `python -B gate/run_tests.py task-cycle` and `python -B elements/common/foundation_check.py`; each with command and exit code in your report. Commit on the task branch by path; no `git add -A`.
- Report: `docs/task-cycles/slice-read-limit-150k/reports/fix-report.md`, with **Unread material**, **Searches not found or unclear**, and your own-work check; one line per finding: fixed, or answered with evidence.
