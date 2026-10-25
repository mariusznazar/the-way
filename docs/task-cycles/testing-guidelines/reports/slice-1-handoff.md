# Handoff — slice 1 executor (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the executor of slice 1 of the plan. Follow the project skill
`the-way-make-change` (read `task-cycle/change/SKILL.md` in this worktree whole, and what it
names) as a planned slice's executor. Change only the files of the slice's *Change*; read what its
*Read* names below (and report every reach beyond it). Questions go to the orchestrator (status
`questions`); an open design choice returns `returned` with no code; a slice too large returns
`returned` with where the size lies. Never ask the human, never start another slice.

## Worktree and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  slice base `57917c3d37e57fdcfa0d352ec9ffc625225d8f82` (HEAD at dispatch). The-way is the top-level repository;
  `agent-instructions/README.md` gives its route and checks.
- Commit with explicit paths (`git add <file> …`, never `-A` or `.`), English messages in the
  style of `git log`; `git log -1 --format='%h %ae'` shows `mariusznn@gmail.com`. No push.
  Leave the worktree clean (the ignored `.runs/` aside).
- Report: `.runs/task-cycles/testing-guidelines/reports/slice-1.md`.

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

### Slice 1 — The template of the testing discipline

- **Goal:** `product-guidelines/testing/template.md` exists as spec D3 gives it: the opening on the
  pattern of the coding and styleguide templates, "Required form" with its fenced block (header,
  `## When to read`, `## Levels`, `## Rules` with the nine required rules in D3's order,
  `## Recipes`, `## Not tested on purpose`, `## Examples`, `## Where in code`), "What each section
  carries" and "Writing the file". Each rule and section cites the decision of the-way that sets it,
  as the foundation step wrote it (WAY-228, WAY-231–WAY-243, WAY-246). `### Test inputs and
  expected values` carries WAY-228 as edited, its property-test clause and the sentence on fixtures
  and builders the coding template holds today. The yes/no table of the research's section 1 stands
  in English under `### Choosing the level`, with its four questions about a property test, without
  the research's column of sources and without "red before the fix" (cut by Q14). Nothing of the
  Q14 cut list stands in the file; no proportion of levels; no command of a test tool.
- **Change:** `product-guidelines/testing/template.md`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:17-56` Need, To do
  `.runs/task-cycles/testing-guidelines/task.md:58-101` Questions to settle
  `.runs/task-cycles/testing-guidelines/task.md:103-112` Context
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/task.md:190-193` Out of scope
  `.runs/task-cycles/testing-guidelines/spec.md:59-136` Constraints
  `.runs/task-cycles/testing-guidelines/spec.md:139-163` D1. Words (open choice 1)
  `.runs/task-cycles/testing-guidelines/spec.md:164-183` D2. Where it lives (units)
  `.runs/task-cycles/testing-guidelines/spec.md:184-323` D3. The template of the testing discipline (product-guidelines/testing/template.md)
  `.runs/task-cycles/testing-guidelines/spec.md:324-351` D4. WAY-228 and the coding discipline
  `.runs/task-cycles/testing-guidelines/spec.md:533-572` D9. Rows onto the foundation
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `.runs/task-cycles/testing-guidelines/spec.md:645-659` Left to the maker
  `product-guidelines/template.md` · `product-guidelines/coding/template.md`
  `product-guidelines/styleguide/template.md`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:182-285` WAY-08 · WAY-09
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:1113-1141` WAY-48
  `foundations/decisions.md:1167-1211` WAY-51 · `foundations/decisions.md:2102-2124` WAY-100
  `foundations/decisions.md:2146-2170` WAY-102 · `foundations/decisions.md:2579-2678` WAY-120 · WAY-121
  `foundations/decisions.md:4390-5910` WAY-167–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:5992-6011` WAY-226 · `foundations/decisions.md:6036-6058` WAY-228
  · Foundation entries rows WAY-231–WAY-243, WAY-246, WAY-228 and the glossary term exemplar, as written
  · outside the repository, not measured: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces
  pracy nad produktem/research_wytyczne_testow/raport_wytyczne_testow.md:25-63, section 1 "Poziom
  wybiera się po zepsuciu, nie po proporcjach piramidy" (the yes/no table)
  · guidelines: none — the-way has no guidelines directory
- **Model:** same — it words a long template of fifteen sections and renders the research's table
  in English, taking wording choices of its own within the spec.
- **Risk:** none
- **Checks:** prose; no test asserts the template. `python -B elements/common/foundation_check.py`
  exits 0 once the file is committed (every decision number it cites names an entry);
  `python -B gate/run_tests.py elements/common` exits 0; `git grep -n "^### " -- product-guidelines/testing/template.md`
  lists the nine required rules in D3's order; `git diff --check 4302f72 -- product-guidelines/`
  prints nothing.
- **Depends on:** Foundation entries (WAY-228, WAY-231–WAY-243, WAY-246, `exemplar`)


## Current ranges (worktree at `57917c3`; these hold where they differ from the plan's)

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
