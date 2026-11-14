# Handoff — review of the whole change

You review the whole change of a task cycle of the-way as an agent that did not make it, with the method `review-change`: read whole `task-cycle/review/SKILL.md` in the worktree below, and, for the review of the whole change, `task-cycle/review/whole_change.md` as it says. Read a file the method names only when the step that names it comes. You are read-only: change no file of the worktree except your report. The person who requested the cycle delegated choices to the orchestrator; nobody will answer a question, so judge from the files.

## What is reviewed

- Worktree (read from its root): `the worktree's root`, branch `task/installer-junction-refusal`.
- Range: base `6fa755ce9b7f749813bf2b2088bf3ce30ac90185`, head `474df77` (two commits by the one author: `54ed53c` installer, tests, README; `474df77` the invariant `installation-paths-through-links` in `foundations/invariants.md`). Changed files: `installation/install.py`, `installation/test_install.py`, `installation/test_agent_types_installation.py`, `installation/README.md`, `foundations/invariants.md`.
- Route: one author without a plan; no spec, no plan, no slices (so no slice reviews: this review is the only one of the code).
- The frozen task, whole: `docs/task-cycles/installer-junction-refusal/task.md` — check every item of its *To do*, its *Acceptance criteria*, the answers of *Questions to settle*, and row 1 of *Settlements to record* (kind invariant, written whole by the author), and the *Decisions in play*.
- The author's report: `docs/task-cycles/installer-junction-refusal/reports/author-report.md`.

## The two questions at start (told to you, as the cycle requires)

- **Trust boundary: yes.** `installation/install.py` is the trust boundary of the part `installation` (part map). Aim your review at that risk: check crafted input at it — a junction (and a symlink) at `.claude`, `.claude/agents`, `.claude/skills`, the folder of a current or stale skill entry, `.agents`, `.agents/skills`, `foundations`, `.the-way` with and without a pin; and any directory-level site that still tests only `is_symlink()` and so lets a junction through. Judge on the code, and run the checks you need yourself (a junction in a temporary directory is made with `_winapi.CreateJunction`, as the tests do), reporting the command and exit code of each.
- **Irreversible operation: no.** Check only that the change does not add one and that the installer's deletion of stale entries still deletes only its own files.

## What I ask you to look at beyond the method's own list

- The author's report names three junction checks that no test protects (`stale_agent_definitions`'s `.claude` and `.claude/agents`, and the `skills` folder in `stale_entry_points`), because `check_parents` refuses a junction there before they run. Judge whether that is acceptable and how to grade it.
- The author's choices in the invariant: sentence wording ("neither writes nor deletes ... and it refuses before it writes anything where ... on the path of a file it is to write or is `.the-way`"), `Rests on: none`, `Derives from: WAY-48 · WAY-235 · WAY-368`, Part `installation`, and that the part map surface `installation-command` was left unedited. Judge each against the element's template, `elements/common/rules.md` and the task's row 1; the author's concerns 1 and 2 are in its report.
- Two existing symlink tests in `installation/test_agent_types_installation.py` now cite the new invariant. Judge whether that is right.
- The tests make a junction through the private `_winapi.CreateJunction`; the author took this from `instruction-files/test_check_instructions.py:92-100` as precedent under the invariants `script-subprocesses` and `script-imports`. Judge it against those invariants.
- The README sentence about junctions.

## Foundation and guidelines

You select your own foundation by "Reading the foundation" in `elements/common/way_of_working.md`, and state in your report how many decisions you read whole and how many by title only (WAY-150). The decisions of the task's *Decisions in play* (WAY-48, WAY-13, WAY-38, WAY-328, WAY-235) concern the change. The-way holds its own code and tests to none of the product guidelines (WAY-328), so there are none to read for it.

## The base's checks

The product's whole gate passes on the base: `python -B gate/run_tests.py` exit 0, 1267 tests in 10 directories (the orchestrator's run, 2026-11-14). You do not run the whole gate (its run is the orchestrator's); `python -B gate/run_tests.py installation` takes about 15 minutes, so run only the tests you need, by `python -B -m unittest installation.test_install -k <pattern>`.

## Report

Write your full report to `docs/task-cycles/installer-junction-refusal/reports/review-whole-report.md` as `review-change` gives it: its first line `PASS 474df77` or `FAIL 474df77` (the full SHA), the graded findings with the grade and whether each is outside the task's scope, the checks you ran with command and exit code, the coverage of every task item, settlement row and decision in play, the count of decisions read whole and by title, **Unread material** (or `none`) and **Searches not found or unclear** (or `none`). Return only the status line, a one-line check result and the path.
