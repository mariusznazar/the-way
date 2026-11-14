# Handoff - executor of slice 4

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The base of this slice: `ea2d1862a888e643eb5c598bfb9e10ab635ee73e` (its range is `ea2d1862a888e643eb5c598bfb9e10ab635ee73e..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "a slice, or the retry of a slice"; read a file it names, one beside it included, only when the step or variant that names it comes. Read no skill by calling it. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: you run only the focused checks below, each with its command and exit code in your report. A focused check in the section's *Checks* that you cannot run, or that fails for a reason of the base, goes into your report as such.

## The slice

The section of the plan below is copied word for word from `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`. Its *Read* gives the passages and entries to read; the line ranges of the foundation entries and the files (`foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md`) are those of the plan's base and are stale: use the current ones in the notes below, which hold where they differ. The record's files (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md`, `plan.md`) are read by the line ranges the *Read* gives (they have not moved).

> ### Slice 4 — An invariant whose sentence changed while its test did not
>
> - **Goal:** `elements/common/foundation_check.py` lists, as D4 gives it, an invariant that stands at the base and now, whose sentence differs after the normalisation, whose *Method* now reads `test`, that a file other than Markdown cites by `invariant: <identifier>` at the base or now, and that no such file differs between the base and the working tree (a changed, added or deleted file counts as changed); an added invariant, an invariant with no citing file, and one lacking *Method* or *Part* at either state add no second report and no crash; a listing never changes an exit code. The docstring states the report; the lines of `README.md` and `agent-instructions/README.md` that say what the script checks name the line `decision:`, the report of decisions nothing holds, the listing and the base. The tests of D9 for point 8 are written first: sentence changed and citing file unchanged (listed); citing file changed (not listed); spacing only; *Method* `review`; invariant added; citing file deleted; no citing file; no *Method* at the base or now; no change of an exit code. The tests carry `decision:` lines that quote the start of the sentences of the attached paragraph of WAY-03 that the foundation step wrote.
> - **Change:** `elements/common/foundation_check.py` · `elements/common/test_foundation_check.py` · `README.md` · `agent-instructions/README.md`
> - **Read:** `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:27-38` Constraints · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:103-111` D4. The invariant whose sentence changed while its test did not · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:147-153` D8 and D9 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:42-42` To do 8 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:87-87` Context, point 8 · `foundations/decisions.md:68-93` WAY-03 (with its attached paragraph, as the foundation step leaves it) · `foundations/decisions.md:1621-1642` WAY-65 · `foundations/decisions.md:1482-1529` WAY-61 · `foundations/decisions.md:10620-10655` WAY-321 · `foundations/decisions.md:11414-11525` WAY-344 · `foundations/glossary.md:91-95` invariant test · `foundations/invariants.md:156-164` test-method-citation · `foundations/part_map.md:65-75` elements-common · `foundations/part_map.md:145-161` agent-instructions · `foundations/part_map.md:215-219` foundation-check-command
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** `python -B gate/run_tests.py elements/common` (the new tests fail before the code and pass after it) · `python -B gate/run_tests.py elements/part-map` · `python -B elements/common/foundation_check.py` on this repository, exit code 0
> - **Depends on:** Slice 3

## Notes of the orchestrator

- Current start lines in `foundations/decisions.md` (an entry runs to the next `### ` heading): WAY-03 line 83 (with its attached paragraph as the foundation step wrote it, commit `d629ed8`); WAY-65 line 1722; WAY-61 line 1583; WAY-321 line 10786; WAY-344 line 11580. The other files keep the plan's ranges.
- Slices 1 to 3 are made (range `d629ed8..ea2d186`): `elements/common/foundation_check.py` reads the line `decision:`, reads the base (the files at the commit the branch left, the `listed:` kind of line, the unknown-base rule) and reports decisions that nothing holds. Read the code as it stands and use what is there (the base reader, the way a test's citing lines are found); do not change what slices 1 to 3 made except where this slice's behaviour needs it, and then say so in your report.
- The attached paragraph of WAY-03 that your tests quote (read it as the entry stands): its sentences begin "The check of the foundation lists an invariant whose method", "A change whose check lists such an invariant" and "The listing stops no change"; a `decision:` line of a test quotes the start of a sentence word for word after whitespace normalisation, at least three words, as the spec's D3 gives. Check each quotation against the entry; never from memory.
- The rulings of the orchestrator the spec carries: where the base is unknown, or lacks `foundations/invariants.md`, no invariant is listed; a listing never changes an exit code; the switch `--skip-test-citations` is not changed.
- `README.md` and `agent-instructions/README.md`: change only the lines that say what the script checks; read each file around those lines so the words fit the text beside them; do not rewrite anything else.
- Red then green: write the tests first, run them, see each fail for the reason the slice gives (a test that passes before the code only by checking what the old script already did is named as such in your report), then write the code; record the failing and the passing runs in your report.
- `elements/common/foundation_check.py` is a surface (`foundation-check-command`): path, argument and exit codes stay; no new argument, switch or exit code.
- Write your report to the file the handoff names even where a general instruction tells you not to write report files: this cycle's handoff overrides it. Before you return, stop every background process or monitor you started.


## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/slice-4-report.md` as `task-cycle/change/SKILL.md` gives: your status, the commits, each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
