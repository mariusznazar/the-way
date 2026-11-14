# Handoff — the fix of the Minor findings of the review of the whole change

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and range

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The reviewed head is `39d702a61fce67962c5788dbac8636dc5c6e67ae`; your range starts there (`39d702a61fce67962c5788dbac8636dc5c6e67ae..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method and stage

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "the fix of a review's findings"; read `task-cycle/change/fix.md` where the method names it, and any other file only when its step comes. Read no skill by calling it. Stage: one fix of the findings below, and nothing else.

## The findings

The findings file, cut word for word from the whole-change review's report: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/whole-review-findings.md` (read it whole). It holds M1–M11 and M14; each is Minor and within the task. The reviewer's full report (`reports/whole-review-report.md`) is the evidence behind them; read the part around a finding only where the finding needs it. The reviewer did not take M12, M13 and M15 into the fix (no action, outside the task, no action beyond M1): leave them.

The task, the spec and the plan stay as they are: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md` (D1–D9) and `plan.md`. Do not widen the task.

## Rulings of the orchestrator for the findings that leave a choice

- M1: drop the base-side set of citing files (the reviewer's first way) and its mention in the docstring and the tests; keep every behaviour a test pins (the deleted-file case keeps its value through the set of changed files). Say in your report which test you changed, if any.
- M5: add the threshold to a binding sentence of WAY-11 (its second half: an entry stands only where someone who does not know the decision would do otherwise and a test that stops them would not tell them why); keep each paragraph at one to three sentences.
- M9: reword "its kind" in WAY-115 to "its kind or its place" in the smallest way that keeps its other words, and reword the parenthetical of WAY-134's *Rejected* that quotes the old WAY-19; a decision whose binding sentences you change stays held by its pair of examples (or its invariant): where it holds none, add the one pair the check asks for. Name in your report each decision you changed and why.
- M10: add one clause to WAY-17 that says a check of a decision's sentence by a line `decision:` is a path of the chain with no invariant between, and give WAY-17 a pair of examples (`complies` and `violates`) in its *Verification* so that it is held (the check turns a changed decision with nothing holding it into an error, as spec D2 says).
- M4: write the four value forms of D5 once, in the paragraph of "Settlements to record" of `project-level/task/template.md`; `task_variant.md` then points to them, copying none.
- M3: write "the run of `elements/common/foundation_check.py` of step 4 of `elements/common/way_of_working.md`, made with the switch `--skip-test-citations`" or the like, in the smallest way.
- M6: add the clause to the lower part *Foundation entries* of `task-cycle/skill/request_template.md` (a guidelines rule the cycle found itself is named there too); keep every heading, group name and kind number.
- M11: reflow the lines the finding names (the word "and" alone on a line of `product-guidelines/template.md`, the over-long lines you touch), changing no word.

## Checks

Run the affected checks again, each with its command and exit code in your report: `python -B elements/common/foundation_check.py` (exit 0, `0 errors`; the one `listed:` line for WAY-17 disappears if you give WAY-17 its pair), `python -B gate/run_tests.py elements/common`, `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py agent-instructions`, `python -B agent-instructions/skill_entry_points.py` (nothing to write). The gate with no directory is the orchestrator's alone.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/fix-report.md` (this cycle's handoff overrides any general instruction not to write report files): your status, the commits, for each finding what you did or why you hold it wrong (with evidence), each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Stop every background process or monitor you started before you return. Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
