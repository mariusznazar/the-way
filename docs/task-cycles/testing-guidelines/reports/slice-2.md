# Slice 2 report

**Status:** done
**Commit:** 87b600e (product-guidelines/coding/template.md, product-guidelines/coding/SKILL.md)

## Changes
- template.md: removed `### Test inputs and expected values` from the fenced block, from the order bullet (three standing checks remain), and from "What each section carries"; added "a kind is code of the product other than its tests (WAY-231)" to the `## Kinds of code` bullet and to the form-of-a-kind bullet on the file's name.
- SKILL.md: removed the step-4 bullet on the rule of tests; step 1 excludes tests from kinds (WAY-231); "Where the skill works" gains the one-task-both-disciplines sentence (WAY-247). Description unchanged.

## Checks
- git grep -n "WAY-228\|Test inputs and expected values" -- product-guidelines/coding/ : exit 1, no output
- python -B agent-instructions/skill_entry_points.py : exit 0, "entry points are current"
- python -B elements/common/foundation_check.py : exit 0, "0 errors"
- git diff --check 4302f72 -- product-guidelines/coding/ : exit 0, no output

## Own-work check
Requirement most likely missed: no leftover reference to the removed rule (e.g. "four" checks, mention of tests' rule in prose). Grep for WAY-228 and the heading is empty; the order bullet now says three standing checks. Line endings: files are LF in index and worktree.

## Reach beyond Read
None beyond the named files; I read only task.md 50-100, spec.md D4 and Foundation entries, WAY-231 and WAY-247 entries, and make-change SKILL.md. Did not open the other listed decisions or product-guidelines/template.md since the edits are removals plus two clauses the spec words.

## Choices
- Placed the WAY-231 clause in two spots (Kinds of code bullet, kind-file bullet) so both "introduces" places the plan names carry it; cost if wrong: one redundant sentence.
- Pointed in the Kinds-of-code sentence to the testing guidelines as where tests' rules stand; slice 1's testing template exists, not measured.

## Concerns
None.
