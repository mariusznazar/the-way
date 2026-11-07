PASS e9c900a7b19ad00cf2d89b726e6d35556c876676

# Review of the fix - Minor findings of the review of the whole change

Range: `a15de0906961981bc58982f97cb1443875341518..e9c900a7b19ad00cf2d89b726e6d35556c876676`, one commit
(`git log a15de09..e9c900a`). `git rev-parse HEAD` printed `e9c900a7b19ad00cf2d89b726e6d35556c876676`.
Method: `task-cycle/review/SKILL.md` with `task-cycle/review/fix.md`. Bounded by
`reports/findings.md` (three Minor findings within the task, no blocking finding). The fix report
`reports/fix.md` was checked as claims.

Counts: blocking 0, Minor 1 (new, cosmetic), out of scope 0.

## Each finding

1. `elements/common/skill/SKILL.md:32-33`: **fixed**. The sentence now reads "Read the file of your
   variant in full once, at step 1; where you come to step 2, 4 or 5 without having read it, read it
   first." A resumed task-mode use whose first row is `waiting` goes resume rule -> step 3 -> step 4.
   It comes to step 4 without the file, so it now reads the file in full, its "What the caller gives"
   included, before carrying out the step 4 lines. A use that read the file at step 1 is not sent to
   read it again (WAY-256: "unless an earlier step did"). Step 3 needs nothing of the file, so leaving
   step 3 out of the list loses nothing. Adds no route, loses none.
2. `elements/common/skill/task_variant.md:38`: **fixed**. "In its place" became "In place of step 4".
   The antecedent is now explicit and matches what the base meant (base `SKILL.md:95-96`, where the
   words followed "this step does not run"). No other word of the paragraph changed. Adds no route,
   loses none.
3. `reports/assessment.md`: **fixed**. "Before the table" (line 9) now says the search that
   `instruction-files/judging.md:7-9` puts before the table was not made, and that every verdict
   rests on cost or a carried decision. Proposal 3 (line 77) now says that none of the five conditions
   of "When to remove a rule" (`judging.md:72-81`) is met or claimed, because the sentence is a
   statement of plan and not a rule. It names the five conditions, and it grounds the removal in a
   stated cost, which `judging.md:32` allows. The table, its rows and its quotes are unchanged
   (`verify_counts.py` still finds every nonblank base line in exactly one row).

## What the fix diff could have broken

- The diff changes only the three lines above (3 insertions, 3 deletions in two files).
  `git diff --stat a15de09 e9c900a -- . ':!elements/common/skill'` printed nothing, and
  `git status --short` is clean. The description and the Python are unchanged, and the entry points
  are current.
- No new Critical or Important finding.
- **Minor (new, within the task, cosmetic):** `elements/common/skill/task_variant.md:38` is now 103
  characters long. Every other prose line of the five files wraps at 100. No check reports it and no
  reader is misled. Re-wrapping the paragraph would match the file.

## Word counts recomputed at `e9c900a`

My own script (whitespace split, as `wc -w`):

| Figure | Mine | `word-counts.md`, `author.md`, `fix.md` |
|---|---|---|
| `SKILL.md`, `read.md`, `build_table.md`, `definition_variant.md`, `task_variant.md` | 598, 126, 198, 624, 475 | same |
| together | 2021 | same |
| task sum 1 / 2 / 3, after | 1397 / 3554 / 2438 (598+126+198+475; +1752+405; -405-208-503) | same |
| definition sum 1 / 2, after | 1546 / 4391 (598+126+198+624; +1752+674+419) | same |
| before (unchanged) | 1584; 3741; 2625; 1584; 4429 | same |
| change | -11.8%, -5.0%, -7.1%, -2.4%, -0.9%, so -12, -5, -7, -2, -1 | same |
| `assessment.md` proposal 1 | 3554-952 = 2602; 2438-952 = 1486 | 2602; 1486 |

A search of `author.md`, `word-counts.md` and `assessment.md` for the old figures (599, 473, 2020,
1396, 3553, 2437, 1547, 4392, 2601, 1485) finds none. `word-counts.md` names commit `e9c900a`, and
`author.md:7` names the fix commit. The 405-against-424 note stands as before.

## Declined to judge

none

## Checks

| Command (from the worktree root) | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD`; `git log --oneline a15de09..e9c900a`; `git diff a15de09..e9c900a`; `git status --short` | 0 | head as given; one commit; 3 lines changed in 2 files; clean |
| `git diff --stat a15de09 e9c900a -- . ':!elements/common/skill'` | 0 | nothing |
| `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" |
| `python -B gate/run_tests.py elements/common` | 0 | OK |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn (as before) |
| `python -B instruction-files/check_instructions.py --file elements/common/skill/SKILL.md` and `.../task_variant.md` | 0 each | 0 errors, 3 warnings each (dead-path warnings, as before) |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/verify_counts.py` | 0 | 0 problems; note on 424 |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/route_check.py` | 0 | 0 problems |
| `python -I -B C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\3a9bd485-0e4a-4608-a08e-b723e098f59b\scratchpad\counts2.py <worktree> <out> e9c900a` | 0 | the figures in the table above |
| Manual: line lengths of the two changed files (PowerShell, lines over 100 characters outside tables and front matter) | - | one line, `task_variant.md:38`, 103 |
| Manual: walk of a resumed task-mode use through `SKILL.md` and `task_variant.md` | - | as in finding 1 |

Not run: the `installation` and `agent-instructions` tests and the whole gate. Both suites passed at
`a15de09` in the review of the whole change, and the fix changes only Markdown lines that they do not
read. The whole gate is the orchestrator's run.

## Reach beyond the dispatch

none beyond the files the dispatch names and `instruction-files/judging.md`, read in the review of
the whole change.

## Searches not found or unclear

none
