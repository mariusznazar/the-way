# Report of correction 1 — the human's remarks on the open request

**Status:** done. Commits (range from `dcaa169c`; `git diff --numstat dcaa169c..HEAD`: `task-cycle/skill/SKILL.md` +3 / −3, `task-cycle/slice_size.py` +8 / −2, `task-cycle/test_slice_size.py` +16 / −2):

- `022a8b40` — Name the orchestrator in the sentence about reviews of groups of slices
- `8c97482a` — Count a changed code file whole in the slice size and narrow the count by ranges to the files of the foundation

## The remarks, as made, and how each was met

The remarks file (`reports/correction-1-remarks.md`), item 1 of *Fix or let through*, has two parts; items 2–5 are accepted and touch nothing of mine.

**Remark A — "the lead" in the new sentence about groups of reviews: use the name the process already gives the agent leading the cycle, as the sub-step around it does.**
- Met: `task-cycle/skill/SKILL.md`, step 9, sub-step 5 of the planned route: "the lead may dispatch" → "the orchestrator may dispatch". Nothing else of the sentence changed except the line break (a reflow of the three lines).
- Why this name and not "you": the skill opens "You are the orchestrator" and uses "the orchestrator" in the third person in the same step (step 10: "the orchestrator records it with the command", "the orchestrator does as step 12 gives"); WAY-136 as this change writes it says "the orchestrator". The sub-step's own sentences are imperatives with no named actor, so the name the skill uses for that agent is the choice; "you" would have changed the verb `records` of the sentence, which the handoff said not to touch.
- Search made once: `grep -rn "the lead may dispatch\|lead may"` over `*.md` and `*.py` of the worktree (outside `.runs`) found the one place only; no copy of the sentence stands in a record template, another skill or a decision.

**Remark B — the size measure counts a part of a code file while the agent reads that file whole: keep counting by part only for the files of decisions the task was about, count a code file the slice changes whole, as the agent reads it, with a test for a plan that names a range of a code file.**
- Met in `task-cycle/slice_size.py`: a file of *Change* that exists counts by the ranges *Read* names only where it is a file of the foundation; any other file of *Change* counts whole, whatever ranges of it *Read* names. Code: one constant `FOUNDATION_DIRECTORY = "foundations"` and one condition (`found not in ranges or found.relative_to(root).parts[0] != FOUNDATION_DIRECTORY`). A file that *Read* names whole still counts whole, and one named both whole and by ranges still counts whole (the accepted choice).
- What "a file of the foundation" is for the script, and where I took it: a file under `foundations/` of the repository the plan is for. Source: `foundations/part_map.md` lists exactly the five files `foundations/decisions.md`, `part_map.md`, `invariants.md`, `glossary.md` and `environment_facts.md` as the files of the parts `decisions`, `part-map`, `invariants`, `glossary` and `environment-facts`; WAY-04 names those five elements as the whole of a product's foundation. The docstring names both. The script tests the directory and not the five names: any file under `foundations/` counts as a file of the foundation. Way rejected: a closed list of the five names — it would break when the foundation gains a file, and it adds nothing the directory does not already say. Cost if wrong: a file under `foundations/` that is not one of the five (none exists today) would be counted by its ranges.
- Docstring: the paragraph that opens "A slice reads every file of *Read*" now says it — the task's sentence for a file of the foundation, then "A file of *Change* that is no file of the foundation counts whole, as its agent reads it, whatever ranges of it *Read* names", then the rest as before. The rest of the docstring and the code stay as they were.
- `task-cycle/plan/SKILL.md` (4(b)) and `task-cycle/change/SKILL.md` (4(c)) read again: both speak of entries and the section of the log / of a file of the foundation, so both agree with the corrected measure; unchanged. The three decisions and the template are unchanged, as the handoff says.

## Tests

- New: `test_changed_code_file_that_read_names_by_ranges_counts_whole` — a code file `task-cycle/tool.py` of 29 characters ("line one\n" 9, "line two\n" 9, "line three\n" 11) in *Change*, `task-cycle/tool.py:1-1` in *Read*; expects 29 characters and 12 tokens (29 / 2.5 = 11.6, rounded up), `fits`; the derivation stands in the comment. It catches the previous behaviour (9 characters, 4 tokens) — a bug the human named.
- **Red run, before the code:** `python -B -m unittest task-cycle/test_slice_size.py` → exit 1; `AssertionError: Lists differ: ['1', '9', '4', 'fits', …] != ['1', '29', '12', 'fits', …]`; 1 failure of 20 tests.
- Kept and adjusted: `test_changed_file_that_read_names_by_ranges_counts_only_those_lines` already used `foundations/decisions.md`; `test_changed_file_that_read_names_whole_and_by_ranges_counts_whole` now uses `foundations/decisions.md` too, so that it still holds "whole beats ranges" for the files where ranges count (for a code file the result is whole whatever). `test_changed_file_that_read_does_not_name_counts_whole` unchanged.

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| New test red, before the code | `python -B -m unittest task-cycle/test_slice_size.py` | 1 (1 failure, 20 tests) |
| Test file after the code | `python -B -m unittest task-cycle/test_slice_size.py` | 0 (20 tests OK) |
| Directory of the code | `python -B gate/run_tests.py task-cycle` | 0 |
| Entry points and copies, linter and formatter invariants | `python -B gate/run_tests.py agent-instructions` | 0 |
| Instruction files | `python -B gate/run_tests.py instruction-files` | 0 |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (0 errors) |

The last four ran in one background command (it ran longer than the foreground limit) and I read its result — all four exit codes — before this report. Not run: the full gate.

## Own-work check

- Requirement the correction most likely does not meet: that the measure counts a changed code file whole (the remark's 548 against 25 907 characters) while the log named by a range still counts by the range — both in one run against real files.
- Check: a plan of two slices in the worktree, `python -B task-cycle/slice_size.py <plan>`: slice 1 *Change* `foundations/decisions.md`, *Read* `foundations/decisions.md:6243-6338`; slice 2 *Change* `task-cycle/remove_merged_worktrees.py`, *Read* `task-cycle/remove_merged_worktrees.py:1-10`.
- Showed (exit 0): slice 1 — 8 514 characters, 3 406 tokens, `fits` (the log counted by its range, not the 916 K of the whole log); slice 2 — 25 907 characters, 10 363 tokens, `fits` (the whole code file; `wc -c` of the file gives 25 907, the number the review gave for the base). So the 548 of the head is gone.
- Mutation in the head: the directory name wrong or the condition dropped — caught by the new test (a code file counted by its range) and by the first test (the log counted whole, 160 004 tokens, `too large`); `!=` turned to `==` — caught by both; a file named whole in *Read* counted by its range — caught by the whole-and-ranges test.
- Behaviour a user sees in the running product: none (a script of the process and a skill's word); no walkthrough.

## Reaches beyond the handoff

- `grep -rn "the lead may dispatch\|lead may"` over the worktree (the one search the handoff asks for); `grep -n "orchestrator" task-cycle/skill/SKILL.md` to see how the skill names the agent; `grep -n "foundations/" foundations/part_map.md` and `WAY-04` (lines ~504–520 of `foundations/decisions.md`) for what the foundation's files are.
- The remarks file and the handoff, whole; `task-cycle/skill/SKILL.md` was read in part in this correction (the sub-step around the sentence, lines 498–516, and the grep above); I read it whole in the first turn of this session.

## Working copies

`.runs/author-correction-1/` held one test plan; removed (path written out in full). I wrote one scratch output (`red.txt`) directly under `.runs/` by mistake and removed it at once. `.runs/fc.txt` ("0 errors") appeared in `.runs/` during the background run; it is not a file I wrote (my commands wrote no such file), it is ignored by git and stays — remainder: `.runs\fc.txt`, reason: not mine to remove.

## Unread material

- `task-cycle/skill/SKILL.md`, whole: read in the first turn, in part (lines 498–516 and by grep) in this correction. The frozen task and my earlier reports: read in earlier turns, not again. Guidelines `coding.md`, `coding-measuring-report.md`, `testing.md`: read whole in the first turn, not again.
- The reviewer's two findings: read as quoted in the handoff, not from the review report (not mine to read).

## Searches not found or unclear

none
