# Fix report — whole-change review's blocking finding, task `testing-guidelines`

**Status:** done

Range: `3bd9e37b60cb4c91613dddfa517c445841016688..a2f1165`, one commit:
`a2f1165` Approve a level's first exemplar test in refinement only where the task's outcome is that test.

## Files changed

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` (WAY-242, WAY-218) | 36 | 16 |
| `product-guidelines/testing/SKILL.md` | 9 | 5 |
| `product-guidelines/reading.md` | 6 | 3 |
| `project-level/task/skill/SKILL.md` | 5 | 3 |
| `project-level/plan/skill/SKILL.md` | 4 | 3 |

Not changed: `product-guidelines/testing/template.md` — its *Exemplar* field (lines 228-230) says
only "by its path, with the product's decision designating it; empty until a decision designates
one; designating another is a change of that decision", nothing about refinement, so it does not
say otherwise. WAY-238 unchanged. Nothing under `task-cycle/`.

## The finding — fixed, by the orchestrator's way (a), C13

Finding 1 (Important): WAY-242's "where it has none" clause had refinement approve the first test's
designation (and the skill settle its path), against WAY-238 (the level is the cycle author's
choice; refinement holds no plan of tests).

How:
- **WAY-242** binding sentences: where a level has no test, its first test becomes the exemplar;
  the designation is approved in a task's refinement only where the task's required outcome is
  itself a test of that level, its document naming the level and that the task's first test of it
  becomes the exemplar, with no list of tests and no path; where the change's author chooses in the
  cycle to write a level's first test, it is approved at a blocked draft request, as WAY-172 gives a
  meaning the task document does not settle. Three binding sentences. *Verification*: complies —
  a task whose outcome is the product's first e2e test (sign-up journey) carries the designation and
  its cycle writes the decision with the path; a cycle author who checks a query with the first
  integration test proposes the decision at a blocked draft request; violates — refinement of a
  discount-rule task designates its first unit test with a path; a cycle designates a level's first
  test it chose and leaves it to the merge (plus the three existing violations). *Rationale* names
  WAY-216 (outcome shows the level, as requirement shows the kind) and WAY-238; *Rejected* gains
  way "approve in refinement for every first-test task" and way "always the blocked draft request"
  (ways b of the finding).
- **WAY-218**: the designation goes with "a task whose required outcome is itself that level's first
  test"; complies example reworded the same way; violates gains "the plan assigns a level's exemplar
  test to a task whose tests its cycle chooses".
- **Testing skill**: "A new level" (step 3) now applies where the task's required outcome is the
  first test of a level, settles the level, its recipe and that the first test becomes the exemplar,
  no list of tests and no path (WAY-238); otherwise refinement designates nothing and the cycle's
  author proposes the designation at a blocked draft request (WAY-242, WAY-172). Step 1's mode bullet
  and step 4's "What it settles" bullet follow.
- **`product-guidelines/reading.md`** bullet, **`project-level/task/skill/SKILL.md`** step 3 bullet,
  **`project-level/plan/skill/SKILL.md`** step 2: the same split.

Check that shows it: a search of the repository (outside `.runs/`) for the old phrasings — "path
the test takes", "approved in the task's refinement", "task writing that level's first test", "task
that writes its first test", "writes the first test of a level", "each new level" — returns no hit
(exit 1). The collision is gone in meaning: refinement now designates only where the level follows
from the required outcome, never choosing a level or listing tests, which is what WAY-238 forbids.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0
- `python -B agent-instructions/skill_entry_points.py` — exit 0, "entry points are current"
- `python -B gate/run_tests.py project-level` — exit 0, 259 tests OK
- `python -B gate/run_tests.py elements/common` — exit 0, 109 tests OK
- `git diff --check 3bd9e37` — exit 0
- No test written: the change is prose of decisions and skills (make-change section 2, "Test
  behaviour, not text"); no invariant changed.

## Own-work check (section 3)

Requirement most likely missed: some text still routing a first test's designation through
refinement for any task (the finding named five places, more could exist). Check: the leftover
phrasing search above plus `grep -rn WAY-242` over the repo (references: WAY-218, WAY-250,
`reading.md`, testing `SKILL.md` and `template.md`, both project-level skills). Showed: every
reference read; WAY-250 (audit of existing tests, derives from WAY-242) and the template field are
unaffected; no leftover.

## record-decision steps

- Step 1/2: read WAY-25, WAY-172, WAY-198, WAY-199, WAY-200, WAY-216, WAY-218, WAY-238, WAY-242,
  WAY-250, WAY-21 whole; glossary `exemplar`. The question of WAY-242 stays the same, so it is an
  edit in place (template "Changing a decision").
- Step 2 search of the whole foundation once settled: `WAY-242` and "exemplar" across
  `foundations/` — entries touched are WAY-218 (edited) and WAY-250 (unaffected, its binding
  sentences concern the audit where tests exist). No glossary term used in a new meaning; invariants
  and part map name no exemplar test.
- Step 4.4: WAY-218 and WAY-250 derive from WAY-242; WAY-218 edited, WAY-250 needs no change. No
  invariant derives from WAY-242.

## Choices made

- **WAY-242 *Scope* gains `project-level`** (now `product-guidelines, project-level`). Reason: its
  binding sentences now say what a task's refinement and the breakdown approve, and the
  project-level skills cite it; by WAY-21 a refining agent finds governing decisions through
  *Scope*, as WAY-216 (`project-level, product-guidelines`) and WAY-238 are found. Rejected: leave
  *Scope* as it was — a refining agent selecting by "Reading the foundation" would not find the rule
  that limits what it may approve. `task-cycle` not added: the cycle's route is WAY-172, which
  already names `task-cycle`. Cost if wrong: one more decision read in refinement; revert one word.
- **No `derives from WAY-238`** added to WAY-242: the rationale names WAY-238; a new relation would
  be a meaning claim beyond the finding. Cost if wrong: the reviewer asks for one line.
- Commit message wording and the examples (sign-up e2e, query integration test, discount-rule unit
  test) are mine; chosen so none settles a product's order.

## Reaches beyond the dispatch

- WAY-250 (`foundations/decisions.md`, from 6904 before the edit) — derives from WAY-242, read for
  record-decision step 4.4.
- WAY-21 — read to judge the *Scope* choice.
- `task-cycle/skill/SKILL.md` lines 15-30 and 80-95 — read only to confirm the blocked draft request
  route exists; nothing changed there.
- `elements/decisions/skill/SKILL.md`, `elements/decisions/template.md` (80-175),
  `elements/common/way_of_working.md` (1-154) — the record-decision skill and the parts it names.

## Problems observed

- The frozen spec (`.runs/task-cycles/testing-guidelines/spec.md`: D5 "A new level" line 412-413,
  D6 the reading bullet line 461-463, *Foundation entries* WAY-242 row line 595 and WAY-218 bullet
  line 618-621) still carries the earlier wording ("the task writing its first test designates it,
  approved in refinement"; "step 4 settles its path"). Not changed — it is the cycle's artifact, not
  mine; the orchestrator decides whether the cycle record notes C13 against it.
