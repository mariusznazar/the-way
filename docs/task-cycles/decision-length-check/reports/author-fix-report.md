# Author report — fix of the findings of the review of the whole change

**Status:** done

## Commits (range from the reviewed head `e8b76178`)

1. `67933213` Bring the summaries of the length check in line with WAY-05, restore the escapes of QUOTED, make a spacing test break lines — findings 1, 2, 3 and 4.
2. `9c7f9b71` Name the module that reads the text of an entry in the part elements-common — finding 5.

The worktree is clean. Files: `README.md`, `agent-instructions/README.md`, `elements/decisions/template.md`, `elements/common/foundation_text.py` (one line), `elements/common/test_foundation_check.py` (one replacement), `foundations/part_map.md` (the sentence of `elements-common`).

## Findings

- **1 (blocking), fixed.** `README.md` now says in separate sentences: "It reports as an error each decision that a change adds or whose binding sentences it alters and that nothing holds. It reports as an error too each paragraph of binding sentences over three sentences or 300 words in a decision that a change adds or whose binding sentences it alters, a different division of them into paragraphs included. It lists, without failing, the other decisions that nothing holds, the other decisions with a paragraph over those limits and each invariant …". "That nothing holds" no longer attaches to the length error and the division counts. `agent-instructions/README.md` gains "a different division into paragraphs counting as an alteration for this report alone", so a reader does not take the meaning of the check of what holds a decision (where a division does not count) for it. Check: both texts read against the second paragraph of WAY-05 (`foundations/decisions.md`); the tests of the code were unchanged and pass.
- **2 (Minor), fixed.** The row "binding sentences" of the table in `elements/decisions/template.md` now says the script counts the sentences and words of each paragraph "in every decision, reporting an excess as an error in one a change adds or alters, a different division into paragraphs included, and listing it in any other (WAY-05)".
- **3 (Minor), fixed.** In `test_a_decision_over_a_limit_whose_spacing_alone_changed_is_listed` the second replacement is `.replace("d. ", "d.\n")`. Checked by running the expression on the test's paragraph: the result has 3 line breaks and differs from the original (the earlier `"e. "` matched nothing). The test still passes, now with a line break and doubled spaces in the altered paragraph.
- **4 (Minor), fixed by restoring the escapes.** `QUOTED` in `foundation_text.py` is written again as at the base, `r"\"[^\"]*\"|[“„][^”]*”"`; the line is byte for byte the line of `foundation_check.py` at `1b6fe1c1` (`git show 1b6fe1c1:elements/common/foundation_check.py | grep '^QUOTED'` compared with `cmp` against the new line: identical). The move is then unchanged as its commit message and the first report say; the escapes also keep the three kinds of marks apart on a screen. The pattern was not changed in meaning, so no behaviour moves.
- **5 (Minor), fixed.** The sentence of the part `elements-common` reads "…with the module that reads the files and git for it and the module that reads the text of an entry for it, …". Written as `elements/part-map/skill/SKILL.md` gives (the template's "Form of an entry" and the `write.md` and `decide_entry.md` it names read): the binding sentence says what the part answers for and not where files sit; no other entry of the part map changed, and no entry names this sentence, so step 4.4 follows nothing. The file `foundation_text.py` stays claimed by `elements/common/**`.

Finding 6 of the review's report is outside the task and was not touched.

## Checks (command, exit code)

- `python -B gate/run_tests.py elements/common` — exit 0, 283 tests, OK.
- `python -B gate/run_tests.py elements/part-map` — exit 0, 40 tests, OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests, OK.
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, 12 `listed:` lines as before.
- `.runs/quality-venv/Scripts/ruff.exe check .` — exit 0; `ruff.exe format --check .` — exit 0 (86 files).
- Not run: the full gate (as handed); `installation` (nothing it reads changed beyond the part map sentence and README prose, and it passed on the earlier head).

## Own-work check

The weakest point of the fix is finding 4 (a pattern that the whole foundation check depends on). Check: byte comparison of the line with the base's (identical), and the whole of `elements/common` including the three-kinds-of-quotation-marks test passes. For finding 1 the weak point is the wording in `agent-instructions/README.md`, which now says the division counts "for this report alone"; I read it against WAY-05 and against WAY-12's check, where the division does not count — the two meanings are named apart.

## Unread material

- `elements/common/way_of_working.md` and `elements/common/rules.md` were not re-read (read whole in the first turn); for the part-map entry I read `elements/part-map/skill/SKILL.md`, `write.md`, `decide_entry.md` and `elements/part-map/template.md` whole. The reviewer's report `review-whole-report.md` was not read; the findings file was enough.

## Searches not found or unclear

- none

## Working copies

- `.runs/author-fix/` (a script and outputs): removed. `.runs/quality-venv/` stays as reported before (the environment of Ruff, needed by the linter tests).
