# Handoff — slice 3 executor (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the executor of slice 3 of the plan. Follow the project skill
`the-way-make-change` (read `task-cycle/change/SKILL.md` in this worktree whole, and what it
names) as a planned slice's executor. Change only the files of the slice's *Change*; read what its
*Read* names below (and report every reach beyond it). Questions go to the orchestrator (status
`questions`); an open design choice returns `returned` with no code; a slice too large returns
`returned` with where the size lies. Never ask the human, never start another slice.

## Worktree and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  slice base `87b600ea4a0b14c905b8e4a487eeb07d4629bc25` (HEAD at dispatch). The-way is the top-level repository;
  `agent-instructions/README.md` gives its route and checks.
- Commit with explicit paths (`git add <file> …`, never `-A` or `.`), English messages in the
  style of `git log`; `git log -1 --format='%h %ae'` shows `mariusznn@gmail.com`. No push.
  Leave the worktree clean (the ignored `.runs/` aside).
- Report: `.runs/task-cycles/testing-guidelines/reports/slice-3.md`.

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

### Slice 3 — The skill `maintain-testing-guidelines`, its entry points and the README

- **Goal:** `product-guidelines/testing/SKILL.md` exists as spec D5 gives it: frontmatter
  `name: maintain-testing-guidelines` and a one-line `description` starting "Use when", on the
  pattern of the two other skills and passing the generator's checks (spec *Constraints*, WAY-127
  bullet); the opening paragraphs, "Where the skill works" with its table, "What reaches the task
  document", "Orchestrated mode" and steps 0–5, mirroring `maintain-coding-guidelines` section for
  section with no mode or step the coding skill lacks — "A new level" mirrors its "A new kind"
  (ruling C4); reports under `.runs/testing/`. `README.md` names the testing discipline's directory
  in its `product-guidelines/` item and `product-guidelines/testing/` in "Using the skills" (spec
  D8). `python -B agent-instructions/skill_entry_points.py --write` has run and its output is
  committed: the two new entry points `the-way-maintain-testing-guidelines` and every existing one,
  whose list of sibling skills gains the name (invariant `skill-entry-points`); no entry point is
  edited by hand.
- **Change:** `product-guidelines/testing/SKILL.md` · `README.md`
  `.claude/skills/the-way-*/SKILL.md` · `.agents/skills/the-way-*/SKILL.md` (the generator's
  output: two new files and the forty existing ones it rewrites, none edited by hand)
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:17-24` Need
  `.runs/task-cycles/testing-guidelines/task.md:45-56` To do, items 2–6
  `.runs/task-cycles/testing-guidelines/task.md:58-101` Questions to settle
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/spec.md:59-136` Constraints
  `.runs/task-cycles/testing-guidelines/spec.md:139-163` D1. Words (open choice 1)
  `.runs/task-cycles/testing-guidelines/spec.md:164-183` D2. Where it lives (units)
  `.runs/task-cycles/testing-guidelines/spec.md:352-433` D5. The skill maintain-testing-guidelines (product-guidelines/testing/SKILL.md)
  `.runs/task-cycles/testing-guidelines/spec.md:525-532` D8. Entry points and READMEs
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `product-guidelines/coding/SKILL.md` · `product-guidelines/styleguide/SKILL.md`
  `product-guidelines/template.md` · `product-guidelines/reading.md`
  `project-level/task/skill/SKILL.md` · `project-level/task/template.md`
  `elements/common/way_of_working.md:11-36` Critique before collective review; How a skill asks
  `elements/common/critique/SKILL.md` · `agent-instructions/skill_entry_points.py`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:6-93` WAY-01–WAY-03 · `foundations/decisions.md:182-318` WAY-08–WAY-10
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-757` WAY-27–WAY-29 · `foundations/decisions.md:819-849` WAY-33
  `foundations/decisions.md:955-979` WAY-38 · `foundations/decisions.md:1053-1086` WAY-44
  `foundations/decisions.md:1113-1141` WAY-48 · `foundations/decisions.md:1167-1211` WAY-51
  `foundations/decisions.md:1889-1912` WAY-89 · `foundations/decisions.md:2102-2124` WAY-100
  `foundations/decisions.md:2146-2170` WAY-102 · `foundations/decisions.md:2256-2277` WAY-107
  `foundations/decisions.md:2579-2734` WAY-120–WAY-122 · `foundations/decisions.md:2774-2819` WAY-124
  `foundations/decisions.md:2891-3138` WAY-127–WAY-133 · `foundations/decisions.md:3946-4013` WAY-154 · WAY-155
  `foundations/decisions.md:4390-5910` WAY-167–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:5992-6011` WAY-226 · `foundations/decisions.md:6036-6058` WAY-228
  · Foundation entries rows WAY-174, WAY-215, WAY-228, WAY-231–WAY-250 and the glossary term exemplar, as written
  · created by Slice 1, not measured: product-guidelines/testing/template.md (whole; the skill's
  step 0 reads it and its sections name it)
  · guidelines: none — the-way has no guidelines directory
- **Model:** same — it words a new skill of six sections and steps 0–5 from the spec, taking wording
  choices of its own.
- **Risk:** none
- **Checks:** `python -B agent-instructions/skill_entry_points.py --write` exits 0; then
  `python -B agent-instructions/skill_entry_points.py` prints `entry points are current` and no
  directory without a skill; `git status --short` before the commit shows only the two new
  entry-point directories, the forty rewritten entry points, `product-guidelines/testing/SKILL.md`
  and `README.md`; `python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py gate`
  and `python -B gate/run_tests.py instruction-files` exit 0; `python -B elements/common/foundation_check.py`
  exits 0; `git diff --check 4302f72 -- product-guidelines/ README.md` prints nothing.
- **Depends on:** Slice 1 · Slice 2 (the coding skill it mirrors, as changed) · WAY-174 · WAY-215 ·
  WAY-228 · WAY-231–WAY-250 · `exemplar`


## Current ranges (worktree at `87b600e`; `product-guidelines/testing/template.md` added by slice 1 in `083ab5d`; the coding template and skill changed by slice 2 in `87b600e`; these hold where they differ from the plan's)

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
