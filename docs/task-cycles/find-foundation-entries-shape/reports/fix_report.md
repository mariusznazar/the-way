# Fix report - Minor findings of the review of the whole change

**Status:** done. All three findings fixed; none contested.

**Commit:** `e9c900a` (`docs: find-foundation-entries names a variant file read at any step reached without it, and task step 4 says what it stands in place of`), from the reviewed head `a15de09`. It changes `elements/common/skill/SKILL.md` (+2 -2) and `elements/common/skill/task_variant.md` (+1 -1) and nothing else; the tree is clean after it. Finding 3 changes only files of `reports/`, which git ignores.

## Each finding

1. `SKILL.md`, the sentence on reading the variant file. Fixed. Now: "Read the file of your variant in full once, at step 1; where you come to step 2, 4 or 5 without having read it, read it first." The reviewer's reading holds: a resumed use whose first row is `waiting` starts at step 3 and comes to step 4 or 5 without a start there, so "where you start at" did not reach it.
   - What the new wording switches off: a use that comes to step 2, 4 or 5 without the variant file - by a start there, by a resume that passes step 1, or after step 3 - reading only the lines of that step and missing the file's "What the caller gives" ("in full" now holds on every such arrival). It switches off nothing a use that read the file at step 1 does: that use is not told to read it again.
   - Compared with the base: the base had one file and nothing to read first, so no route is added or lost; the sentence belongs to the rebuild (WAY-256: a later step has the file read unless an earlier step did).
   - Check: `git diff -U0 a15de09 HEAD` shows the two lines changed and no other line of the file; the walk of a resumed task-mode use is `SKILL.md` resume rule -> step 3 -> step 4 pointer "carry out in its place the lines for step 4 of `task_variant.md`" -> "come to step 4 ... without having read it, read it first" -> the whole file, then its step 4 lines.
2. `task_variant.md`, "In its place, a row that carries a choice ...". Fixed: "In place of step 4, a row that carries a choice ...". The reviewer is right that inside the file the nearest antecedent of "its" was "its entry".
   - What the new wording switches off: the reading of "its" as the entry, which would put the question against a choice in place of the entry's writing rather than in place of step 4. The base meaning is kept: on the base the words followed "this step does not run" and meant step 4, a step that now stands once in `SKILL.md` step 4.
   - Compared with the base: no route added, none lost; the words say what the base's context said.
   - Check: the diff above; `route_check.py` phrase for this sentence updated to the new words and it reports 0 problems.
3. `assessment.md`, proposal 3 and "Before the table". Fixed in the file (not committed). The proposal now has a line stating that none of the five conditions of "When to remove a rule" (`instruction-files/judging.md:72-81`) is met or claimed, because the section concerns rules and the sentence is a statement of plan: it tells the agent to do nothing and was not added against a mistake; the removal rests on a stated cost, which `judging.md` allows as the ground of a remove verdict. "Before the table" now says that the search `judging.md` puts before the table was not made, that no session records were opened, and that each verdict rests on cost or a carried decision. The tables, rows and quotes are unchanged, and `verify_counts.py` still finds every nonblank base line in exactly one row.

## Figures that changed against `author.md`

| Figure | `author.md` | Now |
|---|---|---|
| `SKILL.md` words | 599 | 598 |
| `task_variant.md` words | 473 | 475 |
| the five files together | 2020 | 2021 |
| Task mode, sum 1 (after) | 1396 | 1397 |
| Task mode, sum 2 (after) | 3553 | 3554 |
| Task mode, sum 3 (after) | 2437 | 2438 |
| Project definition, sum 1 (after) | 1547 | 1546 |
| Project definition, sum 2 (after) | 4392 | 4391 |
| Change of task sums against the base | -12%, -5%, -7% | -12%, -5%, -7% (unchanged when rounded) |
| Change of definition sums against the base | -2%, -1% | -2%, -1% (unchanged when rounded) |
| Files changed | 5 added or changed | the same five; the fix adds 3 lines and removes 3 |
| Commit the counts were made at | `a15de09` | `e9c900a` |

`author.md` was rebuilt with the new counts block, the reworded sentence in its two comparison tables, and a line naming this fix commit; `word-counts.md` was rewritten by `verify_counts.py --write` after the commit. The base figures are the same as before.

## Checks (from the worktree root)

| Command | Exit code | Result |
|---|---|---|
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests, OK |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 errors, 1 warning (`AGENTS.md:21`, as before) |
| `python -B instruction-files/check_instructions.py --file elements/common/skill/SKILL.md` and `.../task_variant.md` | 0 | 0 errors; 3 dead-path warnings each, as before |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/verify_counts.py` (after `--write` and the rebuild of `author.md` and `assessment.md`) | 0 | 0 problems; the same note on 424 |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/route_check.py` | 0 | 0 problems (first run after the commit: 1 problem, the phrase of finding 2 was still the old words in the script; I updated the phrase and it passes) |

Not run: the `installation` and `agent-instructions` tests and the whole gate. The fix changes two lines of Markdown that no script of those parts reads; both parts passed on `a15de09` and nothing they read changed.

## Own-work check

- Requirement most likely not met: that the fix adds no route and loses none, and that a counted number stated anywhere still equals the files.
- Check: the line diff of the fix (3 lines changed in 2 files, none else); `route_check.py` (presence of 30 phrases per variant and the callers' words) and `verify_counts.py` (counts, the author's block, the assessment's quotes and the numbers of its proposals) both run after the last change to a counted file, and the counts were written after the commit. Both show 0 problems; the first `route_check.py` run failed on its own stale phrase, which shows the script sees a changed sentence.

## Searches not found or unclear

none
