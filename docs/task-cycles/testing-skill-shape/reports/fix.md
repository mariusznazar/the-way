# Fix report - the review's five blocking findings

**Status:** done. **Commit:** `c17f4f8` (docs: fix the review's blocking findings on the testing skill rebuild), on top of `5dc4b3b`; author address `mariusznn@gmail.com`. No push, no history rewritten. The worktree is clean.

## What each finding became (all five fixed; none contested)

1. **Stale word counts - fixed.** `tools/word_counts.py` was run again at the head after the last change of a counted file; `reports/word-counts.md` is regenerated. `tools/verify_reports.py` now also compares every listed count (204 lines: files and sections, "after" lists against the head, the "before" `SKILL.md` against 00c0a74) with the file itself; it reports no mismatch. (I did not run a negative case that makes the new comparison fail; its code is a plain equality of the listed number and `len(text.split())`.) Counted files at the head, in words: `SKILL.md` 1200, `recognize.md` 363, `settle.md` 654, `new_level.md` 62, `audit.md` 230, `hand_back.md` 73, `new_tools.md` 69, `orchestrated_mode.md` 98, `research.md` 232, `starting_set.md` 143, `task_document.md` 364, testing `template.md` 3187. New figures (after; to step 4 / total / change of total; without the first reading: to step 4 / total), "before" unchanged:

   | Route | After: to 4 / total / change | Without first reading |
   |---|---|---|
   | 1 | 8791 / 11272 / -20.2% | 5956 / 8437 |
   | 2 | 7728 / 11040 / -21.8% | 4893 / 8205 |
   | 3 | 9021 / 11502 / -18.5% | 6186 / 8667 |
   | 4 | 7958 / 11270 / -20.2% | 5123 / 8435 |
   | 5 | 7647 / 10959 / -22.4% | 4812 / 8124 |
   | 6 | 8889 / 11370 / -19.5% | 6054 / 8535 |

   `author.md` stays as written; its figures of routes and of files are those of the earlier head and are superseded by this table and by `word-counts.md`.

2. **Extra mode "tests at a level its cycle chooses" - fixed.** `recognize.md` keeps only the case with the recipe standing and an empty *Exemplar* (no step 2) and the extension clause; `SKILL.md` step 3 loses "or its tests are at a level its cycle chooses". The sentence "Where the level of a task's tests is its cycle's choice, the refinement designates no exemplar test: ..." moved, with its words unchanged (full stop turned into the item's semicolon), from `new_level.md` into the exemplar item of `settle.md`, which every route reads. `new_level.md` now holds the first sentence only (62 words). Assessment rows 120 and 174-179 (now a SPLIT) and the "Text added" row are rewritten; proposal P2 stands.
3. **"Extend what exists" in the file of step 1 - fixed.** The bullet moved unchanged from `recognize.md` to "Rules that hold across the steps" in `SKILL.md` (verdict KEEP in the assessment row of lines 123-125; +about 52 words in `SKILL.md`, counted).
4. **Four binding sentences in WAY-256 - fixed.** The last two sentences are joined: "...unless an earlier step did; fragments that stand unchanged are not bound by it." The paragraph has three sentences. (My repair report's "the third" was a miscount, as the review says.)
5. **WAY-265's exemption - fixed.** Now "A step's file that stands unchanged, with the variant file it points to, is not bound by it."; the *Rationale*'s last clause matches ("a step's file that stands unchanged, with the variant file it points to, differs from one rebuilt"). The styleguide skill, whose step files `starting_rules.md`, `settle.md` stand unchanged, is thereby outside it.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` - 0, "0 errors".
- `python -B instruction-files/check_instructions.py .` - 0, "0 error, 1 warn, 3 info" (the `_zadania\` warning of the base).
- `python -I -B .../tools/verify_reports.py` - quotes 46, mismatches 0, overlaps none, missing none; sums consistent; no missing path; 204 listed counts checked against files, no mismatch.
- `python -B agent-instructions/skill_entry_points.py --write` - 0, "entry points are current" (changed nothing).
- `python -B gate/run_tests.py agent-instructions` - OK. The whole gate was not run.
- `compare_sentences.py` - 18 base fragments not verbatim (one more than before): the extra one is the moved cycle's-choice sentence cut at the colon, whose closing punctuation changed from a full stop to the item's semicolon in `settle.md`; accounted for, no rule lost.

## Walks of the six routes (by hand, from `SKILL.md` to the last step's file)

All routes: `SKILL.md` whole (picture, "Rules that hold across the steps" now with "Extend what exists", step pointers), then:

1. First guidelines, no tests, no preference: step 0 sentence; step 1 `recognize.md` (parts, product files and foundation additions, what the product has, mode "no tests"); step 2 testing template, `starting_set.md`, `research.md`, `critique/SKILL.md` and its three files; step 3: not run (no tests, no first test of a level); step 4 `product-guidelines/template.md`, `settle.md` (its exemplar item now carries the cycle's-choice sentence), `task_document.md`, section "Critique before collective review"; step 5 `hand_back.md`.
2. Same with a preference: as 1 without `research.md`; the first critique is at step 4, so `settle.md` has `critique/SKILL.md` and its files read there.
3. Tests, no guidelines, no preference (or an extension): as 1, plus step 3 `audit.md` (template already read; `new_level.md` not read, since no outcome is a first test of a level - this is what finding 2 repairs).
4. Refresh: step 2 `starting_set.md` only, step 3 `audit.md`, step 4 with the first critique, step 5.
5. "A new level", recipe standing: `recognize.md` (mode: new-level case, no step 2); step 3 testing template and `new_level.md`; no `audit.md`, no `starting_set.md`, no `research.md`; step 4 and step 5 as above.
6. Route 1 plus `orchestrated_mode.md` before step 1.

## Choices

1. The moved cycle's-choice sentence goes into the exemplar item of `settle.md` with a full stop before it and a semicolon after (list form), as the finding names the item. Not taken: a bullet of its own (a new line the finding does not ask for).
2. The "Extend what exists" bullet sits last among the rules before "Write each answer" in `SKILL.md`. Not taken: first (no ground for an order).

## Reaches

None.

## Concerns

- The tests in `settle.md` item now put a sentence on a condition ("the level of a task's tests is its cycle's choice") beside the new-level item; the reviewer may prefer a bullet of its own.
- The "before" figures count the base skill's step 0 reads; the task's estimate of the after totals (11 100 to 11 800) holds for routes 1 to 4 and 6; route 5 (10 959) is below it, as `author.md` reported for the earlier head.

## Searches not found or unclear

none
