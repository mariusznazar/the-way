# Handoff 01 — the one author of the whole change

## Delegation

You are the one author of this change, dispatched by the orchestrator of `implement-task`. The
person who requested the cycle delegated every intermediate choice to the orchestrator; ask no
human. Send a question to the orchestrator in your report (status `questions`); never start the
next stage, never ask for approval.

## Where you work

- Worktree (work only here, from its root): `C:\Storage\repos\the-way\.runs\worktrees\part-boundaries-test`
- Branch: `task/part-boundaries-test`, base `dfd50e513c09bebe9d09d74209cd28612565da83` (`foundations`)
- Commit on this branch only. Use `git add <path> <path>…` by explicit paths, never `git add -A`, `.` or `commit -a`. Commit messages in English, in the style of the repository's existing commits (`feat:`, `docs:`, `test:` …). No push, no merge, no other branch. Touch nothing outside the worktree except your report.
- The ignored directory `.runs/` in the worktree holds the cycle's record; do not read or edit it except to write your report to the path below (and to read the frozen task).

## Your method and your variant

- Method: `task-cycle/change/SKILL.md` in the worktree — read it whole.
- Your variant, in the words of its row: **the whole change as the one author**.
- Read a file that method names only when the step or variant that names it comes.
- The foundation step is yours: read `task-cycle/skill/foundation_step.md` whole when you write the entries of *Settlements to record*, and the skill of each element when you write an entry of it — `elements/decisions/skill/SKILL.md` for rows 1 and 2, `elements/invariants/skill/SKILL.md` for row 3 — with the files they name, as their steps come.
- Do not take the return step; the orchestrator dispatches it after the review.

## The task

- Frozen task, read whole: `C:\Storage\repos\the-way\.runs\worktrees\part-boundaries-test\.runs\task-cycles\part-boundaries-test\task.md`
  (original: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_test_granic_czesci.md`, `Status: ready for cycle`, answers of 2026-11-06). Its *To do* items 1–3 and its *Acceptance criteria* are the change. Do not open the original. The task is in Polish; everything you write in the repository is in English.
- Line numbers in the task are for `foundations` @ `3177e10`; your base is `dfd50e5`. Where a quoted line no longer matches, find the passage by its text and name the correction in your report.
- No spec and no plan: the orchestrator found no open design choice. The rows of *Settlements to record* are entries you write (WAY-134); their meaning was approved with the task document (WAY-30, WAY-114), the wording is yours:
  - Row 1 — a **new** decision (next free identifier; the log ends at WAY-298 — check). Its *Rejected* carries the ways of the *Not chosen* lists of questions 1 (A, C), 2 (b, c) and the question on coexistence with an accepted dependency (b, c), as row 1's last column names them. It states why a marked invariant "the part X does not depend on Y" is no list of known violations (WAY-40's *Verification*).
  - Row 2 — an addition **in place** to WAY-44 (Mariusz agreed to it, *Questions to settle*, question 3; WAY-07 for editing in place). Keep its *Rejected* "tests as a part of their own" coherent with the addition (the task's answer explains why: the helper tests nothing).
  - Row 3 — a new invariant in `foundations/invariants.md`, with its test; its entry becomes an example line in `elements/invariants/examples.md` (*To do* 3).
- Template edits: *To do* 1 (`elements/part-map/template.md`, section "Allowed dependencies", keeping the paragraph on an accepted dependency and pointing it to the new rule) and *To do* 2 (section "Assigning files").
- Answers to the questions at start: trust boundary — no; irreversible operation — no; open design choice — none; route — one author without a plan.

## The orchestrator's answer to the question carried to the cycle (binding)

*Questions carried to cycle* asks whether running another part's script (`runpy.run_path`, a new process) counts as an import. Answer: **no**. The invariant and its test cover imports — `import` and `from … import` statements, resolved to Python files git tracks against the importing file's own directory, the repository root, and the directories a file adds to `sys.path` — and not running another file as a script or a process. Source: row 3 and *To do* 3. If the entry or the decision needs to say so, say it in one clause; do not widen the sentence.

## Notes on the test (how to make it is yours; name each choice in your report)

- Its part: put the test where its part's *Depends on* allows what the test imports — the test itself falls under the invariant (task *Context*, last item). If it reuses `elements/common/foundation_check.py` to assign files to parts, its part must allow `elements-common` (e.g. `elements/part-map/`, `Depends on: elements-common · invariants`). A test file in a new directory runs only once it is added to git; `gate/run_tests.py` finds every directory holding a tracked `test_*.py`.
- Assign files to parts by git, as the part map's rules and WAY-44 require (no fnmatch dialect).
- Read imports with `ast`, so that imports inside string literals (fixtures that write test files) are not counted. Directories added to `sys.path`: today's forms include `sys.path.insert(0, os.path.join(HERE, "..", "relation-model"))` (`project-level/readiness_check.py:45`), `sys.path.insert(0, str(Path(__file__).resolve().parent))`, `sys.path.insert(0, str(SOURCE / "installation"))` (`installation/test_install.py:16`) and `sys.path[0] = os.getcwd()` (`gate/run_tests.py:131`). A modification of `sys.path` the test cannot resolve must not pass in silence: decide whether it fails the test or is reported, and name it. A module name that resolves to no tracked file (standard library) is no dependency.
- The two exceptions of row 3: an import from a test file to a part of test helpers (the-way has none today; the test names such parts by identifier, as the task's last answer under *Questions to settle* gives — say what the-way's test holds for it), and an import covered by an invariant "the part `<X>` does not depend on `<Y>`" marked `Violated: yes` in `foundations/invariants.md`. Decide how a test file is recognised in the-way (`test_*.py` is what the gate runs) and name it.
- The test cites its invariant at the test that checks it, as `invariant: <identifier>` (WAY-65).
- Show that the test has teeth: beside the run on the-way's own tree (the acceptance criterion: it passes, the one known cross-part import `project-level` → `relation-model` being allowed), tests on small repositories made for them, in a temporary directory with `git init`, where a forbidden import fails, an import through `sys.path` is seen, and each exception lets its import pass. Record a failing run (a mutation or the fixture) and the passing run, with command and exit code.
- Scripts of the-way use the standard library alone and start only git and the running interpreter (WAY-38, invariants `script-imports`, `script-subprocesses`).
- When you rewrite a file with a script, keep its line endings (`newline=''`, or bytes); check `git ls-files --eol <file>`. Write script output meant to be read to a UTF-8 file, not to the console. In Python literals write paths with `/`, and text holding backslashes as raw strings.
- Do not change any skill's description; the entry points need no regeneration.

## What the orchestrator selected for you to read

- Foundation entries, each whole, by identifier in `foundations/decisions.md`: the task's *Decisions in play* — WAY-225, WAY-51, WAY-40, WAY-44, WAY-38, WAY-11, WAY-28, WAY-62, WAY-65, WAY-215, WAY-16 — and WAY-07, WAY-21, WAY-22, WAY-33, WAY-45, WAY-48, WAY-56, WAY-61, WAY-63, WAY-69, WAY-89, WAY-114, WAY-134. In `foundations/invariants.md`: `script-imports`, `script-subprocesses`, `script-language`, `fingerprint-definition`, `derived-file-content`. The whole part map `foundations/part_map.md` (short).
- The search of the foundation once the entries are settled (WAY-33), as `elements/common/way_of_working.md` "2. Search the foundation" gives it — e.g. everything that names allowed dependencies, *Depends on*, "does not depend on", known violations, tests belonging to the part they test.
- Parts touched: `part-map` (`elements/part-map/template.md`, and the test if it lives there), `invariants` (`foundations/invariants.md`, `elements/invariants/examples.md`), and the decision log `foundations/decisions.md` whose touched parts follow the *Scope* of the entries you write.
- Templates and examples: `elements/part-map/template.md`, `elements/decisions/template.md`, `elements/decisions/examples.md`, `elements/invariants/template.md`, `elements/invariants/examples.md`.
- The product's guidelines: none — the-way has no `guidelines/` directory; the task records that it does not wait for them (*Questions to settle*, last question; WAY-215 departure, which the request names).

## Boundaries

- Out of scope (task, *Out of scope*): the invariant and test in loop2 and its current violations. Touch no other repository.
- Do not run the product's gate (`python -B gate/run_tests.py` with no argument) — that run is the orchestrator's, and one is running elsewhere on the base. Run focused checks of the directories your edits touch (`python -B gate/run_tests.py <directory>`, e.g. the test's directory, `elements/common`, `gate`) and the foundation form check `python -B elements/common/foundation_check.py` as its usage gives.

## Report

Write your full report to `C:\Storage\repos\the-way\.runs\worktrees\part-boundaries-test\.runs\task-cycles\part-boundaries-test\reports\02-author-report.md` as `task-cycle/change/SKILL.md` gives (status, commits, each check with its command and exit code, concerns, reaches beyond this handoff, **Searches not found or unclear**, the own-work check, and the meaning sentences with their mark for the entries you write). Return your status, your commits, a one-line check result and the report's path.
