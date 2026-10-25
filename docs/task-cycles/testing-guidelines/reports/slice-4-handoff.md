# Handoff — slice 4 executor (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the executor of slice 4 of the plan. Follow the project skill
`the-way-make-change` (read `task-cycle/change/SKILL.md` in this worktree whole, and what it
names) as a planned slice's executor. Change only the files of the slice's *Change*; read what its
*Read* names below (and report every reach beyond it). Questions go to the orchestrator (status
`questions`); an open design choice returns `returned` with no code; a slice too large returns
`returned` with where the size lies. Never ask the human, never start another slice.

## Worktree and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  slice base `2b5b1c004632188dcf11c7beb6b3699473d23de0` (HEAD at dispatch). The-way is the top-level repository;
  `agent-instructions/README.md` gives its route and checks.
- Commit with explicit paths (`git add <file> …`, never `-A` or `.`), English messages in the
  style of `git log`; `git log -1 --format='%h %ae'` shows `mariusznn@gmail.com`. No push.
  Leave the worktree clean (the ignored `.runs/` aside).
- Report: `.runs/task-cycles/testing-guidelines/reports/slice-4.md`.

## Answers of step 4 and the cycle's rulings

- Trust boundary: yes — `installation/install.py` (slice 5 only). Irreversible operation: no.
- Spec reviewed (FAIL, one revision, re-review PASS). C3: row 25 carried by *Based on*/*Rejected*
  of other decisions. C4: WAY-242 carries WAY-200's split; the testing skill mirrors only the
  coding skill's "A new kind" ("A new level"). C10: WAY-235 narrows WAY-168 (trust-boundary rule's
  *Invariant* names each boundary's refusal invariant). C11: an exclusion's return condition is part
  of what the product decision allows, not a review trigger.
- The task's frozen copy is `.runs/task-cycles/testing-guidelines/task.md`; the spec
  `.runs/task-cycles/testing-guidelines/spec.md`; the plan `.runs/task-cycles/testing-guidelines/plan.md`.

## The slice's section, copied word for word (`plan.md`)

### Slice 4 — Reading, refinement and breakdown name the testing discipline

- **Goal:** the edits of spec D6. `product-guidelines/reading.md`: the opening sentence and "Name the
  affected work" add whether the work writes or changes a test; the first bullet of "Distinguish the
  gaps" counts test work in a product with no `guidelines/testing.md` as lacking discipline
  guidelines; a new bullet there, shaped like the WAY-216 bullet, gives the first test of a level
  whose recipe has an empty *Exemplar* its designation in the same task through
  `maintain-testing-guidelines`, with no separate exemplar wait (WAY-242); "Select and read" and the
  kind bullets stay, selection by *Applies to* alone (WAY-213 unchanged). `project-level/task/skill/SKILL.md`
  step 3 names `maintain-testing-guidelines` beside the two other skills, the first-level
  exemplar-test case beside the first-kind case, and one clause that a missing coding and a missing
  testing guidelines may be one prerequisite task (WAY-247). `project-level/plan/skill/SKILL.md`
  step 2 names missing testing guidelines beside the styleguide and the general coding file, one
  guidelines task carrying both coding and testing (WAY-247), and a level's first exemplar test with
  the task writing that level's first test (WAY-242). No skill's `description` changes.
- **Change:** `product-guidelines/reading.md` · `project-level/task/skill/SKILL.md`
  `project-level/plan/skill/SKILL.md`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:54-56` To do, items 4–6
  `.runs/task-cycles/testing-guidelines/task.md:81-86` Questions to settle, Pytanie 8 and 9
  `.runs/task-cycles/testing-guidelines/task.md:118-118` Questions carried to cycle, the third
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/spec.md:434-476` D6. Reading, refinement and breakdown
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `elements/common/way_of_working.md:58-96` Reading the foundation
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:182-285` WAY-08 · WAY-09
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:955-979` WAY-38
  `foundations/decisions.md:1113-1141` WAY-48 · `foundations/decisions.md:1167-1211` WAY-51
  `foundations/decisions.md:1889-1912` WAY-89 · `foundations/decisions.md:2102-2170` WAY-100–WAY-102
  `foundations/decisions.md:2233-2819` WAY-106–WAY-124 · `foundations/decisions.md:2849-2945` WAY-126 · WAY-127
  `foundations/decisions.md:3140-3197` WAY-134 · `foundations/decisions.md:3316-3483` WAY-137–WAY-140
  `foundations/decisions.md:3506-3730` WAY-142–WAY-147 · `foundations/decisions.md:3792-4045` WAY-150–WAY-156
  `foundations/decisions.md:4315-5910` WAY-165–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:6036-6058` WAY-228 · `foundations/decisions.md:6119-6160` WAY-230
  · Foundation entries rows WAY-214, WAY-215, WAY-218, WAY-242, WAY-244, WAY-246, WAY-247, as
  written
  · guidelines: none — the-way has no guidelines directory
- **Model:** cheaper — it places in three files the clauses spec D6 settles.
- **Risk:** none
- **Checks:** prose; `python -B gate/run_tests.py project-level` exits 0;
  `python -B agent-instructions/skill_entry_points.py` prints `entry points are current`;
  `python -B elements/common/foundation_check.py` exits 0; `git grep -n "maintain-testing-guidelines" -- product-guidelines/reading.md project-level/task/skill/SKILL.md project-level/plan/skill/SKILL.md`
  shows each of the three files; `git diff --check 4302f72 -- product-guidelines/reading.md project-level/`
  prints nothing.
- **Depends on:** Slice 3 · WAY-214 · WAY-215 · WAY-218 · WAY-242 · WAY-244 · WAY-246 · WAY-247


## Current ranges (worktree at `2b5b1c0`; `product-guidelines/testing/template.md` added by slice 1 in `083ab5d`; the coding template and skill changed by slice 2 in `87b600e`; `product-guidelines/testing/SKILL.md`, `README.md` and the entry points by slice 3 in `2b5b1c0`; these hold where they differ from the plan's)

- `foundations/decisions.md`: WAY-02 37-67 · WAY-08 182-211 · WAY-09 212-286 · WAY-13 387-426 ·
  WAY-16 450-474 · WAY-27 668-695 · WAY-34 851-880 · WAY-38 955-980 · WAY-48 1113-1142 ·
  WAY-51 1167-1212 · WAY-61 1391-1426 · WAY-63 1456-1484 · WAY-89 1889-1913 · WAY-100 2102-2125 ·
  WAY-102 2146-2171 · WAY-107 2256-2278 · WAY-120–WAY-122 2579-2735 · WAY-127 2891-2946 ·
  WAY-141 3485-3505 · WAY-167 4390-4459 · WAY-167–WAY-219 4390-5930 (WAY-174 edited, 4694-4744;
  WAY-214 5730-5767, WAY-215 5768-5811, WAY-218 5861-5895, all edited) · WAY-221 5954-5980 ·
  WAY-226 6010-6030 · WAY-228 6054-6103 (edited) · WAY-230 6163-6205.
- Written by the foundation step (commits `4f207dd`, `57917c3`): WAY-231–WAY-243 6206-6733 ·
  WAY-244–WAY-250 6734-6979 (WAY-246 6789-6820). Find any single one by its heading
  `### WAY-<n> —`.
- `foundations/glossary.md`: `exemplar` (edited) at line 163.
- `foundations/environment_facts.md`: new facts `llm-test-oracle-actual-behaviour`,
  `computer-use-agent-web-testing`.
- The foundation agent's report, with each entry's meaning: `.runs/task-cycles/testing-guidelines/reports/foundation.md`.

## Report

Return a short message: status, commits, a one-line check result naming what failed or did not
run, the report's path. In the report: each check with its command and exit code, the weakest
point you checked and what it showed, every reach beyond the *Read*, the choices you made within
the spec, and concerns.
