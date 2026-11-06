# Handoff 01 — the one author of the whole change

## Delegation

You are the one author of this change, dispatched by the orchestrator of `implement-task`. The
person who requested the cycle delegated every intermediate choice to the orchestrator; ask no
human. Send a question to the orchestrator in your report (status `questions`); never start the
next stage, never ask for approval.

## Where you work

- Worktree (work only here, from its root): `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-3`
- Branch: `task/cycle-remarks-batch-3`, base `3177e1090f6000ed97fbbbab70ec7c7e622aa2c9` (`foundations`)
- Commit on this branch only. Use `git add <path> <path>…` by explicit paths, never `git add -A`, `.` or `commit -a`. Commit messages in English, in the style of the repository's existing commits. No push, no merge, no other branch. Touch nothing outside the worktree except your report.
- The ignored directory `.runs/` in the worktree holds the cycle's record; do not read or edit it except to write your report to the path below.

## Your method and your variant

- Method: `task-cycle/change/SKILL.md` in the worktree — read it whole.
- Your variant, in the words of its row: **the whole change as the one author**.
- Read a file that method names only when the step or variant that names it comes.
- The foundation step is yours: read `task-cycle/skill/foundation_step.md` whole when you write the entry (row 1 of *Settlements to record*), and the skill of the element, `elements/decisions/skill/SKILL.md` (and the files it names, as its steps come), when you write the decision, and `elements/common/way_of_working.md`.
- Do not take the return step; the orchestrator dispatches it after the review.

## The task

- Frozen task, read whole: `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-3\.runs\task-cycles\cycle-remarks-batch-3\task.md`
  (original: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_poprawki_z_uwag_cykli_2026_11_06.md`, `Status: ready for cycle`, answers of 2026-11-06). Its *To do* items 1–4 are the change. The task file is the frozen copy: do not open the original.
- No spec and no plan: the task leaves no open design choice. The *To do* items give the wording of each edit; copy a quoted sentence exactly where *To do* gives one. Where a quoted line number no longer matches the file, find the passage by its text (line numbers are for `origin/foundations` @ `3177e10`, which is your base) and name any correction in your report.
- Row 1 of *Settlements to record* is an entry you write (WAY-134): a **new** decision (next free identifier, WAY-298, check the log) stating the rule of *To do* 1 — fetch and fast-forward the checkout the session works in before the task branch, restart from the entry point, stop when it cannot fast-forward; the correction does the same, merging the remote target branch into the request's worktree. Its *Rejected* holds the two ways under *Questions to settle*, question 1 (reading the skill and the files it names from the base commit; a `git pull` habit or session-start hook outside the-way), and those of questions 2 and 3 as the task gives them. Wording of the entry is yours; the meaning is the row's. The meaning was approved with the task document (WAY-30, WAY-114). The other changes of the task (WAY-291 *Verification* example, the sentence in `way_of_working.md`) are edits in place of existing entries as *To do* gives them.
- Answers to the questions at start: trust boundary — no; irreversible operation — no; open design choice — none; route — one author without a plan.

## What the orchestrator selected for you to read

Foundation entries, each whole, by identifier in `foundations/decisions.md`: WAY-127, WAY-140, WAY-10, WAY-114, WAY-120, WAY-27, WAY-296, WAY-290, WAY-291, WAY-292, WAY-25, WAY-30, WAY-134, WAY-34; also the entries the search of the foundation (WAY-33) finds, as `elements/common/way_of_working.md` "2. Search the foundation" gives it (for instance everything that names `current target branch`, `cycle_remarks_digest`, or the corrected example of WAY-291).
Parts touched: `task-cycle`, `elements-common`, and the file `foundations/decisions.md` (`foundations/part_map.md`). Templates and examples: `elements/decisions/template.md` and `elements/decisions/examples.md`. The product's guidelines: none (the-way has no `guidelines/` directory; the task states that it does not wait for them, *Questions to settle* 4).

## Notes on the scripts and tests you change

- `task-cycle/request_check.py` (`english_share`) and `task-cycle/test_request_check.py`: follow the existing style of the file and its tests. Match quotes only within one line so that an unpaired quotation mark cuts nothing beyond its line; strip „…”, “…” and "…" text, and lines starting with `>`. The tests the task names: a Polish task with long English quotations gives `not English`; a block entirely in quotation marks gives `not judged` (the known gap, the task names it).
- When you rewrite a file with a script, keep its line endings (`newline=''` on read and write, or work in bytes); check `git ls-files --eol <file>`. Write script output meant to be read to a UTF-8 file, not to the console. In Python literals write paths with `/`, and text holding backslashes as raw strings.
- Do not change any skill's description; the entry points (`agent-instructions/skill_entry_points.py`) need no regeneration.

## Boundaries

- Out of scope (task, *Out of scope*): moving loop2's pin of the-way; changing the nightly review script `cycle_remarks_digest.py` (it lives outside this repository). Do not change the correction's other rules.
- Do not run the product's gate (`python -B gate/run_tests.py` with no argument) — that run is the orchestrator's. Run focused checks of the directories your edits touch (`python -B gate/run_tests.py <directory>`, e.g. `task-cycle`, `elements/common`, `agent-instructions`, `relation-model`, `instruction-files`) and the foundation form check `elements/common/foundation_check.py` as its usage gives. A full gate is running elsewhere on the base; do not start another.

## Report

Write your full report to `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-3\.runs\task-cycles\cycle-remarks-batch-3\reports\02-author-report.md` as `task-cycle/change/SKILL.md` gives (status, commits, each check with its command and exit code, concerns, reaches beyond this handoff, **Searches not found or unclear**, the own-work check, and the meaning sentences with their mark for the entries you write). Return your status, your commits, a one-line check result and the report's path.
