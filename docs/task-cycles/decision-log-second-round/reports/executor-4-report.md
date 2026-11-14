# Executor 4 report (written by the orchestrator from the executor's return, which could not write the file)

Status: done with concerns. Commit `6283bb2`, six files, +23 / -12 (haiku executor).

## Checks
- `python -B elements/common/foundation_check.py`: exit 1, 480 lines in total, none in the six files of this slice.
- `python -B gate/run_tests.py elements/common`: exit 1; 201 tests, 1 failure `test_the_way_foundation_passes` (needs exit 0 of the foundation check; other slices' lines).
- `python -B gate/run_tests.py elements/part-map`: exit 0, 39 tests.
- `python -B agent-instructions/skill_entry_points.py`: exit 0.
Own-work check: a grep of the six files for the removed numbers (WAY-117, WAY-37, WAY-116) found none.

## Removals
- `elements/decisions/skill/SKILL.md`: `decision (WAY-117):` became `decision:`.
- `elements/environment-facts/skill/SKILL.md`: `fact (WAY-117):` became `fact:`.
- `elements/environment-facts/skill/read.md`: `(WAY-37, WAY-90)` became `(WAY-90)`.
- `elements/glossary/skill/SKILL.md`: `term (WAY-117):` became `term:`.
- `elements/invariants/skill/SKILL.md`: `invariant (WAY-117):` became `invariant:`.
- `elements/part-map/skill/SKILL.md`: `the part map (WAY-116):` became `the part map:`.

## Reasons added (written from the Rationale of the withdrawn entry at base ec7929d)
1. decisions SKILL, WAY-117: "Projecting keeps a future rule visible in the definition without claiming that it already holds, so a new decision carries no number yet." (second clause the executor's link)
2. environment-facts SKILL, WAY-117: "Projecting keeps a future fact visible in the definition without claiming that it already holds." (the entry's general first sentence)
3. environment-facts read.md, WAY-37: new bullet "A change that brings what entries of the foundation wait for also fixes every entry that waits for it, in the same change." and reason "An entry that says what holds until something exists turns false when it arrives, and nothing leads from what arrives to what waits for it, so a fix left for later goes missing."
4. glossary SKILL, WAY-117: "Projecting keeps a future term visible in the definition without claiming that it already holds."
5. invariants SKILL, WAY-117: (a) "Code-dependent evidence can be completed when the task writes the entry, so the method reads `review` until then."; (b) "Projecting keeps a future invariant visible in the definition without claiming that it already holds."
6. part-map SKILL, WAY-116: "Some map fields exist only once code and files do, so a part with a field still unknown waits for the breakdown." (first clause from the Rationale, consequence the executor's reading)
Items 2, 4, 5b reuse the general reason already in `projected_mode.md`; the Rationale gives no reason for the heading form itself: thin.

## Entries left under the "stay" rule
None of the ten stay numbers appears in these six files.

## Concerns (outside the slice)
- `elements/decisions/skill/SKILL.md` lines 61-62: a line "In projected mode, read `projected.md` ..." sits between the Step 1 and Step 3 bullets, which looks misplaced; left.
- `elements/invariants/skill/SKILL.md` line 58: a very long line already there.

## Unread material
- `foundations/decisions.md` WAY-293: read to its *Rationale*, not to the end.
- `elements/common/projected_mode.md`: by grep (lines 15-21) only.
- Glossary, invariants and part-map files: only their projected-mode sections.
- `foundation_check.py` source: not read.

## Searches not found or unclear
none

## Working copies
`.runs/executor-4/` made for check outputs and removed.
