# Handoff — slice 5 executor (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the executor of slice 5 of the plan. Follow the project skill
`the-way-make-change` (read `task-cycle/change/SKILL.md` in this worktree whole, and what it
names) as a planned slice's executor. Change only the files of the slice's *Change*; read what its
*Read* names below (and report every reach beyond it). Questions go to the orchestrator (status
`questions`); an open design choice returns `returned` with no code; a slice too large returns
`returned` with where the size lies. Never ask the human, never start another slice.

## Worktree and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  slice base `467a2af8ae0d50fb6c6a031e6a3a83aa3d8f098e` (HEAD at dispatch). The-way is the top-level repository;
  `agent-instructions/README.md` gives its route and checks.
- Commit with explicit paths (`git add <file> …`, never `-A` or `.`), English messages in the
  style of `git log`; `git log -1 --format='%h %ae'` shows `mariusznn@gmail.com`. No push.
  Leave the worktree clean (the ignored `.runs/` aside).
- Report: `.runs/task-cycles/testing-guidelines/reports/slice-5.md`.

## Answers of step 4 and the cycle's rulings

- Trust boundary: yes — `installation/install.py` (slice 5 only). Irreversible operation: no.
- Spec reviewed (FAIL, one revision, re-review PASS). C3: row 25 carried by *Based on*/*Rejected*
  of other decisions. C4: WAY-242 carries WAY-200's split; the testing skill mirrors only the
  coding skill's "A new kind" ("A new level"). C10: WAY-235 narrows WAY-168 (trust-boundary rule's
  *Invariant* names each boundary's refusal invariant). C11: an exclusion's return condition is part
  of what the product decision allows, not a review trigger.
- The task's frozen copy is `.runs/task-cycles/testing-guidelines/task.md`; the spec
  `.runs/task-cycles/testing-guidelines/spec.md`; the plan `.runs/task-cycles/testing-guidelines/plan.md`.
- This slice touches the trust boundary `installation/install.py`: a fresh reviewer reviews it on
  its own, checking crafted input at that boundary (a foreign file, a directory or a non-UTF-8 file
  at the new entry-point path, and the `AGENTS.md` block and sibling entry points it rewrites).
- C9: the existing crafted non-UTF-8 case stops on an uncaught `UnicodeDecodeError`; the new test
  copies that assertion and this slice does not change the installer's decoding. Name it in your
  report.

## The slice's section, copied word for word (`plan.md`)

### Slice 5 — The installer brings the skill to products

- **Goal:** spec D7. `installation/install.py` `SKILLS` holds `maintain-testing-guidelines` →
  `product-guidelines/testing/SKILL.md`, and nothing else in the installer changes. A new test file
  `installation/test_testing_guidelines_installation.py`, mirroring
  `installation/test_coding_guidelines_installation.py`, shows: the preview lists both new entry
  points and changes nothing; `--apply` creates them byte-identical, with the skill's description
  and the `.the-way/product-guidelines/testing/SKILL.md` path; every sibling entry point names
  `maintain-testing-guidelines`; the block names `the-way-maintain-testing-guidelines`; a repeated
  run changes nothing; and, in each of `.claude` and `.agents`, a foreign file, a directory and a
  non-UTF-8 file at `the-way-maintain-testing-guidelines/SKILL.md` stop the preview and `--apply`
  with a non-zero exit, the tree byte for byte as before and nothing staged (WAY-48). The exact
  counts of entry points in `installation/test_coding_guidelines_installation.py` and
  `installation/test_styleguide_installation.py` read 40, kept exact. `installation/README.md`
  names the skill in the table's list of entry points and in the list of what the tests check.
  `installation/test_install.py` stays as it is.
- **Change:** `installation/install.py` · `installation/README.md`
  `installation/test_testing_guidelines_installation.py`
  `installation/test_coding_guidelines_installation.py`
  `installation/test_styleguide_installation.py`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:45-52` To do, item 2
  `.runs/task-cycles/testing-guidelines/task.md:119-119` Questions carried to cycle, the fourth
  `.runs/task-cycles/testing-guidelines/spec.md:106-113` Constraints, From the code as it stands
  `.runs/task-cycles/testing-guidelines/spec.md:477-524` D7. Installer (open choice 4; item 2)
  `installation/test_install.py:15-40` · `installation/test_install.py:278-319`
  `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:182-285` WAY-08 · WAY-09 · `foundations/decisions.md:387-425` WAY-13
  `foundations/decisions.md:450-473` WAY-16 · `foundations/decisions.md:668-694` WAY-27
  `foundations/decisions.md:851-879` WAY-34 · `foundations/decisions.md:955-979` WAY-38
  `foundations/decisions.md:1113-1141` WAY-48 · `foundations/decisions.md:1391-1425` WAY-61
  `foundations/decisions.md:1456-1483` WAY-63 · `foundations/decisions.md:1889-1912` WAY-89
  `foundations/decisions.md:2102-2124` WAY-100 · `foundations/decisions.md:2146-2170` WAY-102
  `foundations/decisions.md:2256-2277` WAY-107 · `foundations/decisions.md:2891-2945` WAY-127
  `foundations/decisions.md:3485-3504` WAY-141 · `foundations/decisions.md:4390-4458` WAY-167
  · guidelines: none — the-way has no guidelines directory
- **Model:** cheaper — one constant pair and a test copied from an existing example.
- **Risk:** trust boundary — `installation/install.py` (part `installation`): the new entry-point
  path in a product's `.claude/skills/` and `.agents/skills/`, and the block and sibling entry
  points it rewrites there.
- **Checks:** the failing test first: with `product-guidelines/testing/SKILL.md` committed (Slice
  3) and `SKILLS` not yet changed, the new test file and the counts of 40 are written and
  `python -B gate/run_tests.py installation` exits 1, the new test failing on the missing `CREATE`
  lines and the two counts on 38; after the `SKILLS` entry, `python -B gate/run_tests.py installation`
  exits 0 (the run takes about four minutes); `python -B elements/common/foundation_check.py` exits
  0; `git diff --check 4302f72 -- installation/` prints nothing.
- **Depends on:** Slice 3 (the skill file, committed: the installer's tests install the checkout's
  committed `HEAD`)


## Current ranges (worktree at `467a2af`; `product-guidelines/testing/template.md` added by slice 1 in `083ab5d`; the coding template and skill changed by slice 2 in `87b600e`; `product-guidelines/testing/SKILL.md`, `README.md` and the entry points by slice 3 in `2b5b1c0`; `product-guidelines/reading.md` and the two project-level skills by slice 4 in `467a2af`; these hold where they differ from the plan's)

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
