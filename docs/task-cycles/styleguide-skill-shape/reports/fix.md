# Fix report: the two blocking findings

**Status:** done. Both findings held; neither answered with evidence against.

Fix base `802b56d`. One commit (see the end); nothing pushed. `author.md` is unchanged; where it differs from this file, this file is the account the request takes.

## Finding 1: the section "Reading the foundation" counted

The finding is right: base step 0 (`SKILL.md:93`) has the session read the section "Reading the foundation" of `elements/common/way_of_working.md` (492 words), which refine-task's `read_sources.md:5` has it read at step 1, so it is a file read twice. It was in no list.

- `tools/word_counts.py`: the section is added to the first reads of refine-task and to the base step 0. The first reads are now 2835 words (the `SKILL.md` of refine-task 396, the task template 1739, "How a skill asks" 208, "Reading the foundation" 492). The sentence that said "three files" now names the four files and sections.
- `reports/word-counts.md` regenerated after the edit of `recognize.md` (below). It now says, in plain words, that the files refine-task sends the session to are equal in both states and stay out of the counts (the cycle's rule), and that the task's estimate of about 8850 did not count this section, which is why the before figure stands about 490 words above it.
- Figures (words), from the regenerated lists:

| Route | Before: to step 4 / total | After: to step 4 / total | Before without first reads (to 4 / total) | After without first reads (to 4 / total) |
|---|---|---|---|---|
| 1 | 12678 / 12678 | 7290 / 9672 | 9843 / 9843 | 4455 / 6837 |
| 2 | 12169 / 12678 | 6248 / 9461 | 9334 / 9843 | 3413 / 6626 |
| 3 | 12678 / 12678 | 7527 / 9909 | 9843 / 9843 | 4692 / 7074 |
| 4 | 12169 / 12678 | 6248 / 9461 | 9334 / 9843 | 3413 / 6626 |
| 5 | 12678 / 12678 | 7527 / 9909 | 9843 / 9843 | 4692 / 7074 |
| 6 | 12678 / 12678 | 7394 / 9776 | 9843 / 9843 | 4559 / 6941 |
| 7 | 12169 / 12169 | 4086 / 4086 | 9334 / 9334 | 1251 / 1251 |

The before figures equal the reviewer's. The after figures are nine words above the reviewer's, the words the edit of finding 2 adds to `recognize.md` (336 to 345). Anything in `author.md` that gives the old figures (the summary table, "2343 words", "three files") is replaced by these.

- `assessment.md` row `:93-96` now says the section is counted in the before figures.

## Finding 2: `recognize.md` read the guidelines again

The finding is right: `read_sources.md:28` and `product-guidelines/reading.md:40` have refine-task read whole the guidelines of the parts the task touches, and the bullet said "every file under `guidelines/`". `recognize.md:10` now reads "Read the product's root `AGENTS.md` and every file under `guidelines/` that `refine-task` did not read at its step 1." The set of files read after step 1 is the same, so the meaning of the rule is the same; it is not proposal P1, which narrows the reading and stays unapplied. `assessment.md` row `:92-92` is now a REWORD row saying so, and pointing to P1 as a different change. `SKILL.md:65-69` (step 0) was not changed: the sentence in `recognize.md` carries the exception where the read stands, as it already does for the foundation.

## The two statements of `author.md` corrected

1. **The 5900 estimate (`author.md:110`).** I said the gap came from `SKILL.md` at 906 words, not about 600, plus the 509 words of the files beside the critique, and that without them the figure would be about 5800. By the regenerated lists, route 2 after, total, without the first reads, is 6626 words: `SKILL.md` 906, `recognize.md` 345, styleguide template 1957, `starting_rules.md` 205, template of guidelines 1336, `settle.md` 576, `task_document.md` 343, the section "Critique before collective review" 54, `critique/SKILL.md` 322, its three files 509, `hand_back.md` 73. The gap to 5900 is 726 words. What can be said from my figures: the critique group (322 + 509 + 54 = 885 words) is read in the after state at the first critique and is in the 6626; `SKILL.md` is 306 words over 600. The task records no composition of its 5900, so I cannot say which of these it left out; my statement of a cause was a guess and is withdrawn. The task's estimate of about 8850 before is explained: route 2 before, to step 4, without the first reads, is 9334; without the second reading of the 492-word section it is 8842, which is the estimate. The 509 words of the critique's files come on top at the total (9843).
2. **216 lines (`author.md:76`).** The base file has 233 lines, of which 205 are nonblank. The figure 216 was the count of lines inside the row ranges, the blank lines between the lines of a row included. The check that matters, that each of the 205 nonblank lines stands in exactly one main row, passed (no overlap, none missing).

## Checks (command, exit code)

| Check | Result |
|---|---|
| `python -B instruction-files/check_instructions.py .` | exit 0, 0 errors, 1 warning (`_zadania\` in `AGENTS.md:21`, on the base), 3 info; identical to the base (`reports/check_instructions_after_fix.txt`) |
| `python -B elements/common/foundation_check.py` | exit 0, "0 errors" |
| `python -B agent-instructions/skill_entry_points.py --write` | exit 0, "entry points are current", no change |
| `python -B .runs/task-cycles/styleguide-skill-shape/tools/verify_reports.py` | exit 0: 52 quotes, 0 mismatches; no overlap, no nonblank base line missing; 22 route lists, all sums consistent; every named path exists |
| `tools/compare_sentences.py` | 15 base fragments differ (was 14): the extra one is the `guidelines/` bullet, accounted for as the reword of finding 2 |
| whole gate; `gate/run_tests.py agent-instructions` | not run again: the change is one line of Markdown and the tests do not read it |

## Searches not found or unclear

- The composition of the task's estimate of about 5900 words: not found in the task or the foundation (see above).
- Whether other base reads of step 0 repeat a refine-task read besides the four now counted: I compared each item of base step 0 and `read_sources.md` again; the only other overlap is the root `AGENTS.md`, which refine-task reads in its `## Backlog` section only, so the whole file is a different read. Not found beyond the four.
