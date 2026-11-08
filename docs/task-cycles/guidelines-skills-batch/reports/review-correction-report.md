PASS 9703d0bf55d54a1e8b6b45ec6ebd4fd717e86381

# Review of the correction for the human's remarks — guidelines-skills-batch

Range: `120917c6d414390fbe1bdff01b7a2b7286f85a6e..9703d0bf55d54a1e8b6b45ec6ebd4fd717e86381` (one commit,
two files). `git rev-parse HEAD` = `9703d0bf55d54a1e8b6b45ec6ebd4fd717e86381` (matches `9703d0b`).
Bounded by `reports/remarks-correction.md` (the human: fix O1 and O2 in this request), as
`task-cycle/review/fix.md` gives for a correction.

Counts: blocking 0; Minor 0; out of scope 0.

## Remarks

| Remark | Made | Evidence |
|---|---|---|
| O1: the coding and testing skills name the second way a meaning reaches the code | yes | The paragraph "A meaning reaches the code by one of two ways…" in `product-guidelines/coding/SKILL.md` and `product-guidelines/testing/SKILL.md` is byte-identical to the one in `product-guidelines/styleguide/SKILL.md`: the same md5 for all three extracted paragraphs. The row "Never writes" of each now ends "…, except as a decision proposed at a blocked draft request (WAY-172)" (`coding/SKILL.md:45`, `testing/SKILL.md:44`), the same clause as `styleguide/SKILL.md:38`, so the row and the paragraph agree in all three skills. No "only through the task document" remains in any `SKILL.md`. |
| O2: steps 2 and 4 of the testing skill point directly | yes | `testing/SKILL.md` step 2: "read `research.md` beside this skill too (WAY-265)"; step 4: "read `new_tools.md` beside this skill too (WAY-265)". This is the wording of the coding skill, one level deep. `testing/starting_set.md:11-12` and `testing/settle.md:3-4` still name the same files under the same conditions ("first testing guidelines where the human has no preference, and at every extension"; "each new tool or library left as a technology question"), so the step and the variant file agree, as WAY-265 asks. No "sends you to" remains in any `SKILL.md`. |

## Findings

none. Against the templates: both say "A choice the task did not settle is a question that stops the
cycle at a blocked draft request" (`coding/template.md:316`, `testing/template.md:273`), which agrees
with the new paragraph and row. Against WAY-172 (the task's quotation: "…or, where that document does
not settle it, at a blocked draft request on whose branch the cycle proposes the decision"): the
paragraph says the same. Nothing was added that the remarks did not ask for. The diff touches only
the paragraph, the row and the two pointers.

## Declined to judge

none

## Checks run

- `git rev-parse HEAD` → `9703d0bf55d54a1e8b6b45ec6ebd4fd717e86381`; `git log --oneline 120917c..HEAD` (one
  commit); `git diff 120917c..HEAD` read whole.
- Manual: extracted the paragraph "A meaning reaches the code…" from the three `SKILL.md` and
  compared with `md5sum` → identical. `grep -n "Never writes\|only through\|sends you to"
  product-guidelines/*/SKILL.md` → three identical clauses, no "only through", no "sends you to".
  `grep -n -i "blocked draft"` in both templates. Read `testing/starting_set.md:11-13` and
  `testing/settle.md:1-5`.
- `python -B -m unittest installation.test_coding_guidelines_installation installation.test_testing_guidelines_installation`
  → 4 tests OK, exit 0.
- `python -B instruction-files/check_instructions.py .` → exit 0.
- `git status --short` afterwards was empty, so the worktree is unchanged.
- Not run: the full gate (the cycle's own run); `foundation_check.py` (the foundation is untouched).

## Reaches

- `product-guidelines/styleguide/SKILL.md`, the paragraph and row compared against.
- `product-guidelines/coding/template.md:316`, `product-guidelines/testing/template.md:273`, for
  agreement with the templates.
- `product-guidelines/testing/starting_set.md`, `product-guidelines/testing/settle.md`, for WAY-265
  agreement.

## Searches not found or unclear

none
