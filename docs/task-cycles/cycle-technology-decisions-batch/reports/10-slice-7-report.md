# Slice 7 report — two files named settle.md, and the order of step 2 of find-foundation-entries

**Status:** done
**Commits:** `22c626c` on `task/cycle-technology-decisions-batch`
**Worktree:** `the task's worktree root`
**Class:** cheaper (prose and one rename; no tests written, so no failing-test run)

## Files changed

| File | Change | Added | Removed |
|---|---|---|---|
| `elements/common/critique/settle.md` → `elements/common/critique/settle_review.md` | `git mv`, content unchanged | 0 | 0 |
| `elements/common/critique/SKILL.md` | line 37 now names `settle_review.md` | 1 | 1 |
| `elements/common/skill/build_table.md` | exclusion of settled candidates moved before the table is written; collision rule kept | 4 | 3 |

Total: 3 files, 5 insertions, 4 deletions.

## Item 14 (rename)

- The critique's file is renamed to `elements/common/critique/settle_review.md`; the only reference to it, `elements/common/critique/SKILL.md:37`, now names the new file.
- The technology step's `project-level/technology/settle.md` and all its references (`project-level/technology/SKILL.md`, `start.md`, `close.md`, `task_run.md`, `running_product.md`, and the lead skill's `technology_run.md`) are unchanged.
- Other `settle.md` references in `product-guidelines/` (testing, styleguide, coding, audit_end) are to files beside those skills, not to the critique's file, and are unchanged.
- The `.claude/skills/the-way-critique/SKILL.md` and `.agents/skills/the-way-critique/SKILL.md` entry points are stubs that do not quote line 37; the description of no skill changed.

## Item 26 (order in build_table.md)

- The current text already contained the rule that a candidate an entry read in step 1 already states is no candidate, but it sat in the last bullet, after "Write the table" — so the table could be written and shown with such a row.
- Changed: the rule now stands as its own bullet directly after "Take the candidates", so the excluded candidate is dropped before the rows are built and the table is written. The sentence "No search of the whole foundation runs here; those lines say who makes it" stays in the last bullet.
- The rule that a candidate colliding with such an entry is shown beside it stays, unchanged in wording, in the last bullet.
- `task_variant.md:31`-area (step 2 hand-off, table shown at step 3) and `definition_variant.md` step 2 expect this order; no change to those files was needed.
- Consistent with WAY-134 (`foundations/decisions.md:3454-3456`): "a settlement that a current entry the refinement reads ... already states is no candidate".

## Checks

Commands run from the worktree root, after the edits and before the commit:

| Check | Command | Exit code | Result |
|---|---|---|---|
| Skill entry points, no write | `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" (no change reported) |
| Element common tests | `python -B gate/run_tests.py elements/common` | 0 | Ran 117 tests, OK |
| Agent instructions tests | `python -B gate/run_tests.py agent-instructions` | 0 | Ran 18 tests, OK |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | "0 errors" |
| Whitespace, unstaged | `git diff --check` | 0 | clean |
| Whitespace, staged | `git diff --cached --check` | 0 | clean (run before the commit) |

Not run: the full `python -B gate/run_tests.py` (the handoff forbids it without a directory).

Own-work check (section 3 of make-change):
- Requirement most likely unmet: the critique's pointer to a file that no longer exists, or a leftover `settle.md` under `elements/common/critique/`.
- Check: `grep -rn "settle\.md" elements/common/critique/` and `grep -rn "settle_review" elements/`.
- Result: the first returns nothing; the second returns only `elements/common/critique/SKILL.md:37`. Met.
- Requirement: the rule about settled candidates comes before the table is written and is not duplicated.
- Check: read `build_table.md` after the edit. Result: met, the rule is one bullet before "Write the table"; the collision rule is one bullet after it.

No failing run was needed; no test was written or weakened.

## Reaches beyond the handoff

- `grep -rn "settle\.md\|settle_review"` across the worktree (excluding `.runs/`) to find every reference to the critique's file. Why: to confirm the rename breaks no pointer.
- Read `elements/common/critique/SKILL.md` whole, `elements/common/critique/settle.md` whole, `elements/common/skill/SKILL.md`, `task_variant.md`, `definition_variant.md`, `build_table.md` whole. Why: the slice names them.
- Read `task-cycle/change/SKILL.md`, `task-cycle/change/slice.md`, `agent-instructions/README.md` whole, as the handoff directs.
- Read the decision passages the handoff lists (WAY-115, WAY-120, WAY-134, WAY-256, WAY-267 and the nearby WAY-257/258 text at the given ranges) at their current ranges. Why: the handoff asks for them; WAY-134 is the one this slice's rule rests on.
- Not read: `project-level/technology/SKILL.md:56-62` (the technology step's pointer to its `settle.md`) and the plan's *Foundation entries* table and the report `reports/02-foundation-entries-report.md`. Why not: this slice does not edit the technology step, and the slice section quoted in the handoff was sufficient for the edits. Flagged so the orchestrator sees the gap in my reading.

## Searches not found or unclear

- Whether the `.claude/skills/the-way-critique/SKILL.md` and `.agents/skills/the-way-critique/SKILL.md` copies carry a copy of the critique's body: they do not (each is a 15-line entry point), so no second edit was needed. Found, not unclear.
- The handoff's cite `task_variant.md:31` for "the table shown": the text at that point is the step 2/3 hand-off of `task_variant.md` (step 2 builds, step 3 the human cuts); no edit there was needed.

## Choices made

- Placed the exclusion as a new bullet right after "Take the candidates" rather than merging it into "Each candidate is a row". Rejected: merging, because it would bury the rule in the row description. Cost if wrong: a reader of the bullet list may see one more bullet; trivial.
- Kept the rename content-identical (`git mv` with no edits) so the history follows the file. Rejected: a new file with different wording, which would have changed the critique's meaning.

## Problems observed

None blocking. The slice's handoff said the technology step's `project-level/technology/settle.md` stays; confirmed by the grep above.
