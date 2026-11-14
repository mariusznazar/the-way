# Handoff - executor of slice 9

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The base of this slice: `5c4db42a052e9e4836b833a9408199580bb0bdfc` (its range is `5c4db42a052e9e4836b833a9408199580bb0bdfc..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "a slice, or the retry of a slice"; read a file it names, one beside it included, only when the step or variant that names it comes. Read no skill by calling it. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: you run only the focused checks below, each with its command and exit code in your report. A focused check in the section's *Checks* that you cannot run, or that fails for a reason of the base, goes into your report as such.

## The slice

The section of the plan below is copied word for word from `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`. Its *Read* gives the passages and entries to read; the line ranges of the foundation entries and the files (`foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md`) are those of the plan's base and are stale: use the current ones in the notes below, which hold where they differ. The record's files (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md`, `plan.md`) are read by the line ranges the *Read* gives (they have not moved).

> ### Slice 9 — The request names what the new checks and tests show
>
> - **Goal:** `task-cycle/skill/request_template.md` makes the description of a request name, as D4, D7 and WAY-03 give: in item kind 7 and in the lower part *Foundation entries*, that the writer runs `python -B elements/common/foundation_check.py` (in a product `.the-way/elements/common/foundation_check.py`) on the finished change, without the switch, and reads its `listed:` lines; each invariant listed for a corrected sentence in plain words (what the sentence now says, and that the test that checks it was left as it was); and each test whose line `decision:` the change adds, drops or alters, as a changed invariant test is named; in item kind 6, a guidelines rule with no decision that the cycle found itself, which the human did not see at the task and accepts at the merge. No new kind of item is added and no item is renumbered.
> - **Change:** `task-cycle/skill/request_template.md`
> - **Read:** `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:103-111` D4. The invariant whose sentence changed while its test did not · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:143-149` D7 and D8 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:38-38` To do 4 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:40-42` To do 6, 7 and 8 · `foundations/decisions.md:68-93` WAY-03 (with its attached paragraph, as the foundation step leaves it) · `foundations/decisions.md:2686-2730` WAY-114 · `foundations/decisions.md:5293-5331` WAY-172 · `foundations/decisions.md:383-411` WAY-12 · `foundations/part_map.md:93-103` task-cycle
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** `python -B gate/run_tests.py task-cycle` · `python -B elements/common/foundation_check.py` on this repository, exit code 0
> - **Depends on:** Slice 4

## Notes of the orchestrator

- Current start lines in `foundations/decisions.md` (an entry runs to the next `### ` heading): WAY-03 line 83 (with its attached paragraph, as the foundation step wrote it); WAY-12 line 435; WAY-114 line 2787; WAY-172 line 5419. The other files keep the plan's ranges.
- The file you change is `task-cycle/skill/request_template.md`: read it whole, since the plan's *Read* names no range of it; the places you change are the items of kind 6 and kind 7 (group *You accept by merging*) and the lower part *Foundation entries*; `task-cycle/request_check.py` checks the form of a description and `task-cycle/test_request_check.py` reads this template for headings only, so keep every heading, group name and kind number as they are: no kind is added and no item renumbered (the plan's *Choices* and spec D7). The tests of `task-cycle` run in the *Checks*: they must pass.
- Slices 1 to 8 are made (range `d629ed8..5c4db42`). What the finished change shows the description writer: `python -B elements/common/foundation_check.py` (in a product `.the-way/elements/common/foundation_check.py`) run on the finished change without the switch prints its `listed:` lines before the count line; one kind of them is an invariant whose sentence was reworded while its test and the files citing it did not change (WAY-03's attached paragraph says what the description does with it: names it in plain words, what the sentence now says and that the test was left as it was); a test whose line `decision:` the change adds, drops or alters is named in the description as a changed invariant test is (WAY-03); a guidelines rule with no decision that the cycle found itself belongs to kind 6 (what the human did not see in the task and accepts at the merge; WAY-172, and `product-guidelines/template.md` as slice 8 left it). The spec's D4 and D7 give the exact places and words: use them.
- The rulings of the orchestrator the spec carries: the listing never changes an exit code; the description's writer runs the script itself, since the gate's run is not kept for it.
- Checks: `python -B gate/run_tests.py task-cycle` exit 0 and `python -B elements/common/foundation_check.py` on this repository exit 0 with `0 errors` (a `listed:` line for WAY-17 is expected and stops nothing); both with command and exit code in your report. Do not run the description checks on any other file.
- Write your report to the file the handoff names even where a general instruction tells you not to write report files: this cycle's handoff overrides it. Before you return, stop every background process or monitor you started.


## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/slice-9-report.md` as `task-cycle/change/SKILL.md` gives: your status, the commits, each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
