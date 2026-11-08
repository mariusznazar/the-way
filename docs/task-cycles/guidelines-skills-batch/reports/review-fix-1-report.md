PASS 2c46cb75cbcf30e5d495dda9dfe2f919ef0325fc

# Review of fix 1 — guidelines-skills-batch

Range: `e66e8e790b370f1f04baf8cc73a6f9913cef2fe2..2c46cb75cbcf30e5d495dda9dfe2f919ef0325fc` (one commit,
9 files). `git rev-parse HEAD` = `2c46cb75cbcf30e5d495dda9dfe2f919ef0325fc`. Bounded by
`reports/findings-1.md` (I1, M1-M8), as `task-cycle/review/fix.md` gives. No finding is contested.

Counts: blocking 0; Minor remaining 0; new Minor 1 (does not block); out of scope 0 new.

## Findings of the findings file

| Finding | Status | Evidence |
|---|---|---|
| I1 (Important) | fixed | `product-guidelines/testing/settle.md:16-20` now settles, "for a new level, whether of step 3 (`new_level.md`) or one the task's extension adds with its recipe, that the task's first test of it becomes the exemplar (WAY-242, WAY-251)". Step 4 reads `settle.md` on every route (`testing/SKILL.md` step 4), so a level with no recipe now reaches it through the extension. `new_level.md:7-9` says the same and points to `settle.md`. `recognize.md:21-25` ("takes step 2 as well") no longer contradicts it, and `guideline_findings.md:44-48` is now carried out by a step of the testing skill. The step-3 condition from item 10 stays as the item asked. |
| M1 | fixed | `product-guidelines/coding/template.md:276`: "nothing else" is gone. *Goes with it* lists the rule's own content, and the statement that kept rules keep the meaning of "failure" and "expected refusal" now stands under *Stays*. |
| M2 | fixed | WAY-311 *Rationale* (`foundations/decisions.md:9735-9737`): "two more sentences in what is read at every judgement, and a departure from the order of the sections stays as it is". This matches the weak point of question 3 and names no file. |
| M3 | fixed | `project-level/task/skill/guideline_findings.md:14-15` and `:58`: `project-level/task/skill/read_sources.md`, full path; the file exists there. |
| M4 | fixed (smaller reading) | `product-guidelines/coding/SKILL.md:129-132`: the author's definition of "touches" is removed. A grep for "reads the language" in `product-guidelines/coding/` finds only the extension trigger that row 5 gives (`recognize.md:21`, `SKILL.md:130-131`). |
| M5 | fixed | WAY-240 `- **Scope:** product-guidelines, glossary`; `foundation_check.py` 0 errors. |
| M6 | fixed | `instruction-files/judging.md:30`: "(WAY-311)". |
| M7 | fixed | `product-guidelines/styleguide/SKILL.md:38`: "…except as a decision proposed at a blocked draft request (WAY-172)", which agrees with the paragraph at `:40-46`. |
| M8 | fixed (smaller reading) | `product-guidelines/coding/settle.md:27-30`: the rerun is "for the split alone and before it is proposed", so the audit's list stays as step 3 left it. |

## New in the fix diff

No Critical or Important finding.

Minor (within the task, does not block): **N1. `product-guidelines/coding/template.md:276`, column
*Goes with it* of the row `### Recording a failure`.** It now restates the departed rule's own
content ("the way a failure is written, with its cause, once, where code handles it, and the
last-resort handler"). The other rows use this column for what goes *besides* the departed heading
("the form of a line", "the events of the list…"), and the row for `### Hiding a failure` still reads
"nothing else". The row is correct but reads in a different way from its neighbours. Nothing a reader
does changes; polish only.

## Declined to judge

none. Out-of-scope O1 and O2 of the review of the whole change were not to be fixed and were not
re-examined.

## Checks run

- `git rev-parse HEAD` → `2c46cb75cbcf30e5d495dda9dfe2f919ef0325fc` (matches `2c46cb7`).
- `git log --stat e66e8e7..HEAD`, `git diff e66e8e7..HEAD`: read whole.
- `python -B elements/common/foundation_check.py` → "0 errors", exit 0.
- `python -B -m unittest installation.test_coding_guidelines_installation installation.test_testing_guidelines_installation`
  → 4 tests OK, exit 0. `git status --short` afterwards was empty.
- Manual: grep of `reads the language|touches` in `product-guidelines/coding/*.md` (M4). Read
  `testing/settle.md`, `new_level.md` and `recognize.md` together for the paths of a level with and
  without a recipe (I1).
- Not run: the full gate (the cycle's own run).

## Reaches

none beyond the findings file, the fix report and the files of the fix diff.

## Searches not found or unclear

- What a standing check "touches" (M4) now has no criterion in the skill or in WAY-216. This is the
  reading the review offered, and the sources give none. The question of the audit of dependencies
  stays open for a later refinement.
