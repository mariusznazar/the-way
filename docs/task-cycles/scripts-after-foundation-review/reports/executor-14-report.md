# Report — executor of slice 14, task `scripts-after-foundation-review`

**Status:** done

## Commits (branch `task/scripts-after-foundation-review`)

- `b8c72ea` Add a test that finds a dead pointer in a skill of product-guidelines or project-level
  — `product-guidelines/test_skill_references.py` (new, about 510 lines).
- `f080915` Name the file each dead pointer of a skill of product-guidelines or project-level stands
  for — 11 skill files, 38 lines added, 37 removed.

Files changed in the second commit: `product-guidelines/coding/SKILL.md`,
`product-guidelines/testing/SKILL.md`, `project-level/lead/skill/SKILL.md`,
`project-level/lead/skill/task_return.md`, `project-level/lead/skill/technology_run.md`,
`project-level/plan/skill/assign_entries.md`, `project-level/plan/skill/critique_plan.md`,
`project-level/plan/skill/hand_over.md`, `project-level/technology/SKILL.md`,
`project-level/technology/research.md`, `project-level/technology/task_run.md`.

## What the test reads (rule, written in the test)

Skill files: every `.md` under a directory of `product-guidelines/` or `project-level/` that holds a
`SKILL.md` (84 files: `SKILL.md` and the method files beside and below it). Not read: other files of
the two parts (templates, `reading.md`, `audit_end.md`, `deployment_skill_guide.md`, ...) and the
skills of other parts.

- File pointer: each word of a code span, each word of a fenced block, and each relative link target
  that ends in `.md/.py/.json/.yml/.yaml/.txt`.
  - `<the-way>/` and `.the-way/` prefix: the-way's file whatever the first directory.
  - Product's (passes): first directory `.runs`, `.github`, `guidelines`, `foundations` or a
    `<placeholder>`; bare `AGENTS.md`, `CLAUDE.md`; paths in `~`, absolute or with a drive letter.
  - First directory a directory of the-way: the file must exist. First directory none of these:
    reported (neither a the-way directory nor a known product path).
  - Bare name: must exist beside the skill or below it (nearest ancestor directory with a `SKILL.md`).
  - `<x>` and `*` stand for one segment; such a path needs one matching file.
  - A link to a URL is dropped (with its text) before reading.
- Step pointer: "step(s) N of `X`" and "`X` step(s) N"; X a file or the name of a skill of the-way
  (looked up by `name:` of all `SKILL.md` files outside dot-directories). Steps of a file: numbered
  headings, else numbered list items at the line start. A skill name that names no skill is reported.
- Heading pointer: `"H" in|of [step N of] [the] [skill] X`. Headings: Markdown headings plus the bold
  lead-in opening a list item or a paragraph (see choice 1), compared without number, emphasis,
  code marks and trailing full stop.
- Trust boundary: a pointer is looked up in a set of paths made by `os.walk` (dot-directories
  pruned), never opened; `..`, absolute, NUL, backslash and drive paths cannot reach the file system;
  a file not readable as UTF-8 is a problem, not an exception; every message quotes pointer text with
  `ascii()` cut at 200 characters, one line. Tested by `test_crafted_text_gives_problems_and_no_error`
  and the not-UTF-8 case.

## Dead pointers found on the base, and their correction (16 findings, 11 files)

1. `product-guidelines/coding/SKILL.md` and `product-guidelines/testing/SKILL.md` (step 3):
   bare `audit_end.md` -> `product-guidelines/audit_end.md` (it lies in the parent directory).
2. `project-level/lead/skill/SKILL.md` (two), `project-level/plan/skill/assign_entries.md`,
   `critique_plan.md` (two), `hand_over.md` (two): bare `plan_check.py` -> `project-level/plan_check.py`.
3. `project-level/lead/skill/task_return.md`: bare `plan_state.py` -> `project-level/plan_state.py`.
4. `project-level/lead/skill/technology_run.md`: bare `settle.md` -> `project-level/technology/settle.md`
   (it named the file beside `task_run.md` of another directory).
5. `project-level/technology/SKILL.md` (1), `research.md` (3, incl. the sentence that said the
   template "lies in `project-level/`, one directory above it", now "`project-level/definition_template.md`
   lies one directory above it"): bare `definition_template.md` -> `project-level/definition_template.md`.
6. `project-level/technology/task_run.md`: bare `find_settlements.md` ->
   `project-level/task/skill/find_settlements.md` (the file of `refine-task`, not beside this skill).

No dead pointer stood in a `description:`; none changed. No step pointer was dead on the base; none
of the 31 heading pointers read were dead once choice 1 holds. Counts the test reads today: 84 skill
files, 463 file pointers, 43 step pointers, 31 heading pointers.

## Checks (all from the worktree root)

- Red on the base (skill files at `ef0a5ae`, test present):
  `python -B gate/run_tests.py product-guidelines` -> exit 1; `test_no_skill_file_holds_a_dead_pointer`
  fails with 16 dead pointers (the first: `product-guidelines/coding/SKILL.md:128: 'audit_end.md'
  names no file of the-way`); the 13 other tests pass. Run with `git stash` of the 11 skill files.
- After the correction: `python -B gate/run_tests.py product-guidelines` -> exit 0 (14 tests).
- `python -B gate/run_tests.py project-level` -> exit 0 (278 tests; run again after the last wrap).
- `python -B agent-instructions/skill_entry_points.py` -> exit 0, "entry points are current".
- `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"` -> exit 0 (2 tests).
- Part-map reach: `python -B gate/run_tests.py elements/part-map` -> exit 0 (40 tests, includes the
  cross-part-imports test). The new test imports only the standard library; it reads other parts
  as text by path, which the imports test does not count as a dependency.
- Lines of 100 columns or fewer in the added lines of the skill files and the test (pre-existing long
  lines of `research.md` that the edit touched were wrapped too).

No run of the whole gate (WAY-160).

## Own-work check (WAY-164)

Requirement most likely not met: the test passes over a dead pointer of a kind it should find (a
mistyped directory, a step number, a heading, a skill name, a bare name), or misses a form. Check:
a copy of the tree under `.runs/executor-14/copy` (removed) with seven edits of live pointers; the
test's `check_tree` on it reported each: `A new kinds` heading; `element/common/way_of_working.md`
(unknown first directory); `project-level/plan_stat.py`; the bare `definition_template.md` (twice);
`step 9 of refine-task`; `step 7 of SKILL.md`; skill name `refine-tasks`. One edit was not
reported: "`refine-task` did not read at its step 9" -- the rule reads only "`X` step N" and
"step N of `X`", not "its step N" after other words (an accepted limit, below). The clean copy gave
no problem. Unticked paths in skill files (no code span) were listed and are all link targets, read.

## Choices (way rejected, cost if wrong)

1. **A bold lead-in of a list item or a paragraph counts as a heading.** The skills of the coding,
   testing and styleguide guidelines name "A new kind", "The route of one kind" and "How to show" in
   their `SKILL.md`; these are `- **A new kind.**` items, not Markdown headings. Rejected: counting
   only `#` headings and rewording eight pointers to the enclosing section ("Rules that hold across
   the steps"), which loses the precision of the pointer. Cost if wrong: a reviewer who holds that
   the row says "heading" strictly gets 8 more pointers to rewrite, one test-regex change.
2. **Unknown first directory is reported**, not passed as a product's. A closed list of product
   roots (`PRODUCT_DIRECTORIES`) catches a mistyped directory. Cost: a future skill that names a
   product path under a new root (`src/...`) fails until its root is added to the list; the failure
   message says neither of the-way nor known as a product's.
3. **A bare name is only the sibling rule**: a `plan_check.py` that stands elsewhere in the-way is
   dead; the 11 corrections gave the full path. Rejected: accepting a bare name that equals a basename
   named in full in the same file (less editing, a pointer still unresolved for a reader).
4. **Anaphoric pointers are not read** ("its step 3", "that skill's step 1", "step 5 of a skill of
   ..."): the target is not named in the same phrase, a false hit across 84 files is the cost of
   reading them. Cost: a dead "its step N" passes.
5. Scanning fenced blocks too (their words are read as file words without backticks); the rule is shown
   by a fixture (whether a fence of today's skills holds a pointer I did not count).

Tests that hold a sentence of a decision (`decision:`) or an invariant test: none changed or added
(WAY-03 not reached).

## Reach beyond the handoff

- None beyond the *Read* list, except: `elements/part-map/test_cross_part_imports.py` header
  (lines 1-80 read) to settle what "reach" means for the part-map check; `grep` over the two parts
  for the pointer forms; files I changed (read whole): the 11 above, except
  `product-guidelines/coding/SKILL.md` read whole in two ranges.
- Read of `foundations/part_map.md:195-205`: product-guidelines *Depends on* does not list
  `relation-model`, `foundation-review` or `process-audit`; the test names no import from them and
  reads them by path only.

## Unread material

- `.runs/.../task.md`: read lines 38-93 and 140-155 (To do 15, Questions 1-8 shown, row 7); not the
  rest. `foundations/decisions.md:2545-2570`, `foundations/invariants.md:114-147` and
  `foundations/part_map.md:78-113, 193-207` read whole as named. `product-guidelines/reading.md` read
  whole. `task-cycle/change/SKILL.md` and `slice.md` read whole.

## Searches not found or unclear

- The plan's *Checks* ask the "new test run on the base fails on the dead pointers": done as above;
  the handoff's *Checks* name no whole-gate run, so there is no mismatch to report.
- "Skill file" is not defined in the plan beyond "SKILL.md and the method files beside and below it":
  read as the files under each directory holding a `SKILL.md` (choice recorded in the test's
  docstring); `project-level/lead/answering.md` and the other files of the parts outside such a
  directory are not read.

## Problems observed

- None open. The first version of the rule tests had three of my own fixture mistakes (a placeholder
  that legally matched, a backticked word in a fence, a step number out of range); fixed in the tests
  before the commit, not in the rule.

## Working copies

`.runs/executor-14/` held my scripts and one copy of the tree (`copy/`, for the mutation check); both
removed before return. Nothing outside `.runs/executor-14/`, no worktree, no run log left. Nothing
under `.runs/` committed.
