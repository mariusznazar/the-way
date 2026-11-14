# Handoff - executor of slice 1

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The base of this slice: `d629ed8622521ef0aa6a719416d4329ebe5947ac` (its range is `d629ed8622521ef0aa6a719416d4329ebe5947ac..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "a slice, or the retry of a slice"; read a file it names, one beside it included, only when the step or variant that names it comes. Read no skill by calling it. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: you run only the focused checks below, each with its command and exit code in your report. A focused check in the section's *Checks* that you cannot run, or that fails for a reason of the base, goes into your report as such.

## The slice

The section of the plan below is copied word for word from `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`. Its *Read* gives the passages and entries to read; the line ranges of the foundation entries and the files (`foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md`) are those of the plan's base and are stale: use the current ones in the notes below, which hold where they differ. The record's files (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md`, `plan.md`) are read by the line ranges the *Read* gives (they have not moved).

> ### Slice 1 — The line `decision:` read by the check
>
> - **Goal:** `elements/common/foundation_check.py` reads, in every run, the comment line `decision:` of a tracked file other than Markdown as D3 gives it — a decision number and one quotation to the end of the line — and reports each error D3 lists, at the line (a number naming no decision or a withdrawn one; no number; no quotation; text after the quotation; a quotation that stands nowhere in the binding sentences of its entry, does not begin at a sentence start or has fewer than three words); a line in a Markdown file or an untracked file counts for nothing. The script also keeps, for each decision number, that a line names it, valid or not, so that Slice 3 can use it, and the binding sentences of an entry are read by one helper that Slice 3 reuses. The docstring of the script states the line. The tests of D9 for the line `decision:` are written first, each failing before the code; the tests that hold the sentence of WAY-12 about the line carry a `decision:` line quoting its start, written as a one-line string with `\n` where the product's test file holds it (spec, Constraints). Behaviour of every existing test and the names the part map's import test takes from the script stay.
> - **Change:** `elements/common/foundation_check.py` · `elements/common/test_foundation_check.py`
> - **Read:** `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:27-38` Constraints · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:86-101` D3. The line decision: and how the script reads it · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:147-153` D8 and D9 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:40-40` To do 6 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:76-81` Question 6 · `foundations/decisions.md:383-411` WAY-12 · `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:1621-1642` WAY-65 · `foundations/decisions.md:1482-1529` WAY-61 · `foundations/decisions.md:10620-10655` WAY-321 · `foundations/decisions.md:11414-11525` WAY-344 · `foundations/decisions.md:1030-1054` WAY-38 · `foundations/invariants.md:156-164` test-method-citation · `foundations/invariants.md:116-134` script-imports and script-subprocesses · `foundations/invariants.md:146-154` map-reference-target · `foundations/invariants.md:328-336` cross-part-imports · `foundations/glossary.md:19-23` binding sentence · `foundations/glossary.md:91-95` invariant test · `foundations/part_map.md:65-75` elements-common · `foundations/part_map.md:215-219` foundation-check-command · `elements/part-map/test_cross_part_imports.py`
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** `python -B gate/run_tests.py elements/common` (the new tests fail before the code and pass after it) · `python -B gate/run_tests.py elements/part-map` · `python -B elements/common/foundation_check.py` on this repository, exit code 0
> - **Depends on:** none

## Notes of the orchestrator

- Current start lines in `foundations/decisions.md` (an entry runs to the next `### ` heading): WAY-02 line 37; WAY-12 line 435 (main paragraph and the attached paragraph as the foundation step wrote them, commit `d629ed8`); WAY-61 line 1583; WAY-65 line 1722; WAY-38 line 1131; WAY-321 line 10786; WAY-344 line 11580. In the other files the plan's ranges stand (the foundation step edited only `foundations/decisions.md`).
- The foundation step wrote the entries before this slice (commit `d629ed8`); read WAY-12 and WAY-02 as it left them. The starts of sentences a test of this slice may quote with `decision:` (each begins a sentence and holds at least three words before the first punctuation): WAY-12 main paragraph, "A test that holds a sentence of a decision carries beside it a line"; WAY-12 attached paragraph, "A decision is held when its", "The check of the foundation reports as an error", "Any other decision that nothing holds stands" (the last two belong to Slice 3's tests, not yours). Use only the first for the test of this slice, quoted exactly as the entry stands (the script of the spec's D3 reads the quotation word for word after whitespace normalisation); check it against the entry, never from memory.
- The spec's Constraints and D3 are binding on the form of the line, how a test file holds it (a one-line string with `\n` where the product's test file holds it) and the `decision:` lines of this slice's tests. The rulings of the orchestrator the spec carries: the switch `--skip-test-citations` is not changed (WAY-321 stays); an unknown base writes its line only where the log holds a decision (Slice 2's work, not yours).
- Red then green: write the tests first, run them, see each fail for the reason the slice gives, then write the code; record the failing and the passing run of the tests that check the new line in your report.
- `elements/common/foundation_check.py` is a surface (`foundation-check-command`): path, argument and exit codes stay; no new argument, switch or exit code in this slice.


## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/slice-1-report.md` as `task-cycle/change/SKILL.md` gives: your status, the commits, each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
