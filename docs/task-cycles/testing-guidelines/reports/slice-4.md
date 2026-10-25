# Slice 4 report

**Status:** done

Files: product-guidelines/reading.md (+9/-4), project-level/task/skill/SKILL.md (+6/-2), project-level/plan/skill/SKILL.md (+7/-4). One commit (see git log, "Name the testing discipline in reading, refinement and breakdown"), author mariusznn@gmail.com.

## Checks
- `python -B gate/run_tests.py project-level` exit 0 (259 tests OK)
- `python -B agent-instructions/skill_entry_points.py` exit 0, "entry points are current"
- `python -B elements/common/foundation_check.py` exit 0
- `git grep -c maintain-testing-guidelines -- <3 files>` shows all three (1, 2, 1)
- `git diff --check 4302f72 -- product-guidelines/reading.md project-level/` exit 0, no output

## Own-work check
Weakest point: the plan SKILL first draft named the testing skill nowhere, so the grep check would have missed that file. Found by running the grep; fixed by naming `maintain-testing-guidelines` in the exemplar-test clause (matches WAY-242 "designates ... through the skill"). No description changed.

## Reach beyond Read
WAY-216 entry (decisions.md, via heading search) as the shape of the new bullet; `product-guidelines/testing/SKILL.md:1-40` to confirm skill name and WAY-247 wording. Both are read-only.

## Choices
- reading.md "Select and read" and the kind bullets untouched (spec D6).
- New reading bullet placed before the "files of an unindexed kind already exist" bullet, after the WAY-216 bullet.
- Task SKILL: first-level exemplar-test case added as a sub-bullet after the first-kind bullet; WAY-247 clause placed in the "Use maintain-..." bullet. Rejected: a separate step; cost if wrong: only placement.
- Plan SKILL: the testing file joins the existing guidelines-task sentence; WAY-247 and WAY-242 added as clauses in the same bullet (one line ran past 100 columns; no check enforces it).

## Concerns
None. The CRLF question does not arise (files are i/lf).
