# Handoff - executor of slice 3

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The base of this slice: `269fecc7525d4e706d075e3622b999f1e5dfbb87` (its range is `269fecc7525d4e706d075e3622b999f1e5dfbb87..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "a slice, or the retry of a slice"; read a file it names, one beside it included, only when the step or variant that names it comes. Read no skill by calling it. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: you run only the focused checks below, each with its command and exit code in your report. A focused check in the section's *Checks* that you cannot run, or that fails for a reason of the base, goes into your report as such.

## The slice

The section of the plan below is copied word for word from `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`. Its *Read* gives the passages and entries to read; the line ranges of the foundation entries and the files (`foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md`) are those of the plan's base and are stale: use the current ones in the notes below, which hold where they differ. The record's files (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md`, `plan.md`) are read by the line ranges the *Read* gives (they have not moved).

> ### Slice 3 — Decisions that nothing holds
>
> - **Goal:** `elements/common/foundation_check.py` reports, as D2 gives it, a decision that is held by none of: an invariant after `invariants:` in its *Verification*; a valid or stale line `decision:` that names its number (Slice 1); a pair of `- complies:` and `- violates:` lines in its *Verification*. A decision changed by the change — absent at the base, or its binding sentences differing after the normalisation of D2 — and not held is an error at its heading line; any other decision not held is a listed item (Slice 2); an entry of the earlier form and an entry lacking *Verification* are left to the existing check of fields, with no second report and no crash. The switch `--skip-test-citations` skips nothing of this. The docstring states the report. The tests of D9 for point 7 are written first: a new decision with no invariant, line or pair (error, exit 1) and the same with each of the three (passes); a decision whose binding sentence changed and none held (error); only *Rationale* changed (listed, exit 0); an old decision none holds (listed, exit 0); an entry with no *Verification*; the switch skipping nothing. The tests carry `decision:` lines that quote the start of the sentences of the attached paragraph of WAY-12 that the foundation step wrote. The foundation of the-way itself passes: every decision the task edits stays held.
> - **Change:** `elements/common/foundation_check.py` · `elements/common/test_foundation_check.py`
> - **Read:** `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:27-38` Constraints · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:60-84` D2. The report of decisions that nothing holds · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:86-101` D3. The line decision: and how the script reads it · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:147-153` D8 and D9 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:41-41` To do 7 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:70-75` Question 5 · `foundations/decisions.md:383-411` WAY-12 (with its attached paragraph, as the foundation step leaves it) · `foundations/decisions.md:594-617` WAY-22 · `foundations/decisions.md:124-161` WAY-05 · `foundations/decisions.md:549-572` WAY-19 · `foundations/decisions.md:10620-10655` WAY-321 · `foundations/decisions.md:11414-11525` WAY-344 · `foundations/glossary.md:13-23` binding part and binding sentence · `foundations/invariants.md:156-164` test-method-citation · `foundations/part_map.md:65-75` elements-common · `foundations/part_map.md:215-219` foundation-check-command
> - **Model:** same — the comparison of entries at the base and in the tree decides whether a product's gate stops
> - **Risk:** none
> - **Checks:** `python -B gate/run_tests.py elements/common` (the new tests fail before the code and pass after it) · `python -B gate/run_tests.py elements/part-map` · `python -B elements/common/foundation_check.py` on this repository, exit code 0
> - **Depends on:** Slice 1 · Slice 2

## Notes of the orchestrator

- Current start lines in `foundations/decisions.md` (an entry runs to the next `### ` heading): WAY-12 line 435 (with its attached paragraph as the foundation step wrote it, commit `d629ed8`); WAY-22 line 679; WAY-05 line 156; WAY-19 line 626; WAY-321 line 10786; WAY-344 line 11580. The other files keep the plan's ranges (only `foundations/decisions.md` was edited by the foundation step).
- Slices 1 and 2 are made (commits `6440ca9` and `269fecc`, range `d629ed8..269fecc`): `elements/common/foundation_check.py` reads the line `decision:` (it keeps a map of the decision numbers a line names, valid or not, and a helper that reads the binding sentences of an entry) and reads the base (`foundations/decisions.md` and `foundations/invariants.md` at the commit the branch left, the `listed:` kind of line, the unknown-base rule). Read the code as it stands and use these helpers; the reports of those slices are not yours to read.
- The attached paragraph of WAY-12 that your tests quote (read it as the entry stands): its sentences begin "A decision is held when its", "The check of the foundation reports as an error" and "Any other decision that nothing holds stands"; a `decision:` line of a test quotes the start of a sentence word for word after whitespace normalisation, at least three words, as the spec's D3 gives. Check each quotation against the entry; never from memory.
- The rulings of the orchestrator the spec carries: the switch `--skip-test-citations` is not changed and skips nothing of this report (WAY-321 stays); a "changed" decision is one whose binding sentences differ at the base and now after the normalisation, or that is absent at the base; where the base is unknown or lacks `foundations/decisions.md`, no decision counts as changed and a not-held decision is listed only, never an error.
- The foundation of the-way itself must pass this slice's check: the 13 decisions the foundation step edited each keep a pair of examples, so each is held. Run `python -B elements/common/foundation_check.py` on this repository as the *Checks* gives: the report may print one `listed:` line (WAY-17, whose *Verification* is `none`) and ends `0 errors`, exit 0; if it reports an error for an edited decision, return `blocked` with the decision named, since the log is not yours to edit.
- Red then green: write the tests first, run them, see each fail for the reason the slice gives (a test that passes before the code only by checking what the old script already did is named as such in your report), then write the code; record the failing and the passing runs in your report.
- `elements/common/foundation_check.py` is a surface (`foundation-check-command`): path, argument and exit codes stay; no new argument, switch or exit code.
- Before you return, stop every background process or monitor you started (the cycle receives your result as soon as you return, and a monitor left running keeps sending notices).


## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/slice-3-report.md` as `task-cycle/change/SKILL.md` gives: your status, the commits, each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
