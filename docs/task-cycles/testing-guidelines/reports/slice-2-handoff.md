# Handoff — slice 2 executor (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the executor of slice 2 of the plan. Follow the project skill
`the-way-make-change` (read `task-cycle/change/SKILL.md` in this worktree whole, and what it
names) as a planned slice's executor. Change only the files of the slice's *Change*; read what its
*Read* names below (and report every reach beyond it). Questions go to the orchestrator (status
`questions`); an open design choice returns `returned` with no code; a slice too large returns
`returned` with where the size lies. Never ask the human, never start another slice.

## Worktree and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  slice base `083ab5d00a52b5177c8176af41dcfdf762ffdbad` (HEAD at dispatch). The-way is the top-level repository;
  `agent-instructions/README.md` gives its route and checks.
- Commit with explicit paths (`git add <file> …`, never `-A` or `.`), English messages in the
  style of `git log`; `git log -1 --format='%h %ae'` shows `mariusznn@gmail.com`. No push.
  Leave the worktree clean (the ignored `.runs/` aside).
- Report: `.runs/task-cycles/testing-guidelines/reports/slice-2.md`.

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

### Slice 2 — The coding discipline gives up the rule of tests

- **Goal:** `product-guidelines/coding/template.md` no longer holds `### Test inputs and expected
  values`: gone from the fenced block of "Required form", from the bullet on the order of the
  required rules (only the three standing checks remain, with their `none — <PREFIX-NN>`), and from
  "What each section carries"; where it introduces `## Kinds of code` and the form of a kind, it
  says a kind is code of the product other than its tests (WAY-231). `product-guidelines/coding/SKILL.md`
  loses the step-4 bullet on the rule of tests; its step 1's "kinds of code it already holds files
  of" excludes tests (WAY-231); "Where the skill works" gains that one task may carry the coding and
  the testing guidelines together, each skill leading its own matters (WAY-247). Its frontmatter
  `description` is unchanged. Nothing under `product-guidelines/coding/` names WAY-228 any more.
- **Change:** `product-guidelines/coding/template.md` · `product-guidelines/coding/SKILL.md`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:53-56` To do, items 3–6
  `.runs/task-cycles/testing-guidelines/task.md:84-86` Questions to settle, Pytanie 9
  `.runs/task-cycles/testing-guidelines/task.md:96-98` Questions to settle, Pytanie 13
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/spec.md:106-113` Constraints, From the code as it stands
  `.runs/task-cycles/testing-guidelines/spec.md:324-351` D4. WAY-228 and the coding discipline
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `product-guidelines/template.md`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:182-285` WAY-08 · WAY-09
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:1113-1141` WAY-48
  `foundations/decisions.md:1167-1211` WAY-51 · `foundations/decisions.md:2102-2124` WAY-100
  `foundations/decisions.md:2146-2170` WAY-102 · `foundations/decisions.md:2579-2678` WAY-120 · WAY-121
  `foundations/decisions.md:4390-5910` WAY-167–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:6036-6058` WAY-228
  · Foundation entries rows WAY-228, WAY-231, WAY-247, as written
  · created by Slice 1, not measured: product-guidelines/testing/template.md, where the rule now
  stands
  · guidelines: none — the-way has no guidelines directory
- **Model:** cheaper — it removes one rule and adds two clauses the spec settles.
- **Risk:** none
- **Checks:** `git grep -n "WAY-228\|Test inputs and expected values" -- product-guidelines/coding/`
  prints nothing (exit 1); `python -B agent-instructions/skill_entry_points.py` prints
  `entry points are current` (the description is unchanged); `python -B elements/common/foundation_check.py`
  exits 0; `git diff --check 4302f72 -- product-guidelines/coding/` prints nothing.
- **Depends on:** Slice 1 · WAY-228 · WAY-231 · WAY-247


## Current ranges (worktree at `083ab5d`; `product-guidelines/testing/template.md` added by slice 1 in `083ab5d`; these hold where they differ from the plan's)

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
