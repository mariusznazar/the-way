# Correction report — O1 and O2 (the human's remarks)

**Status:** `done`. **Commit:** `9703d0b` Give the coding and testing skills the second way a meaning reaches the code and direct pointers (from head `120917c`; code base `f5ae96f`). Files: `product-guidelines/coding/SKILL.md` (+9/-6), `product-guidelines/testing/SKILL.md` (+11/-8).

## Remark O1 — fixed

- Changed in both `coding/SKILL.md` and `testing/SKILL.md`: the paragraph "A meaning reaches the code only through the task document: ..." is now the styleguide skill's paragraph word for word: "A meaning reaches the code by one of two ways. The first is the task document: ... The second is for a meaning the document does not settle: the cycle proposes the decision on the branch of a blocked draft request and builds on it only once the human has approved it there (WAY-172). Using a meaning that a decision of the product's log already carries takes no approval."
- The table row "Never writes ... a meaning the task did not settle (WAY-172)" in both files now ends "..., except as a decision proposed at a blocked draft request (WAY-172)", the same clause as the styleguide row.
- Own-work check: compared the three paragraphs and the three rows with `diff` by eye after the edit and with `grep "Never writes\|only through the task document" product-guidelines/*/SKILL.md`: no "only through the task document" remains; the rows are identical but for each skill's own list of files. The wording follows WAY-172 ("or, where that document does not settle it, at a blocked draft request on whose branch the cycle proposes the decision").

## Remark O2 — fixed

- `testing/SKILL.md` step 2: "`starting_set.md` sends you to `research.md`, also beside this skill (WAY-265)" is now "read `research.md` beside this skill too (WAY-265)".
- `testing/SKILL.md` step 4: "`settle.md` sends you to `new_tools.md`, also beside this skill (WAY-265)" is now "read `new_tools.md` beside this skill too (WAY-265)", the words the coding skill uses.
- The pointers inside `testing/starting_set.md` and `testing/settle.md` are untouched (WAY-265 asks for both places).
- Own-work check: `grep -n "sends you to" product-guidelines/*/SKILL.md` finds nothing now; `testing/starting_set.md:11-12` and `settle.md:3-4` still name `research.md` and `new_tools.md` with the same conditions as the step.

## Checks (command, exit code)

- `python -B -m unittest installation.test_coding_guidelines_installation installation.test_testing_guidelines_installation` — exit 0 (4 tests).
- `python -B instruction-files/check_instructions.py .` — exit 0 (0 errors, 1 warn from the unchanged root `AGENTS.md`).
- Not run: `foundation_check.py` (the decision log is untouched), the full gate. No test covers the text of these skills.

## Reaches beyond the dispatch

None. Read `product-guidelines/styleguide/SKILL.md` for the words to copy, as the remark says.

## Choices

- Copied the styleguide wording whole instead of rephrasing it for each discipline, so the three read the same. Cost if wrong: none beyond a sentence per file.
- Left the "Where the skill works" prose of the two files as it was; the remark names only the paragraph and the row.

## Searches not found or unclear

none
