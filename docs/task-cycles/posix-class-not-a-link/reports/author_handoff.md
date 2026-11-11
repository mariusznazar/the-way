# Handoff — the one author (`make-change`, "the whole change as the one author")

Delegation: Mariusz asked the orchestrator to run the whole task cycle for this task; intermediate
choices are the orchestrator's, never Mariusz's approval. You do not talk to him.

Worktree (work only here, from its root): `the root of the task's worktree`
Branch `task/posix-class-not-a-link`, base `e1726b78ad357791c5f84dd946f0edd26cdc3fe8`.
Method: read `.claude/skills/the-way-make-change/SKILL.md` whole; it points to `task-cycle/change/SKILL.md`
in this checkout — read that whole, and open a file either names (`fix.md`, `slice.md`, `ui_check.md`) only when its step or variant comes.
Your variant: **the whole change as the one author**. You also do the foundation step
(`task-cycle/skill/foundation_step.md`, read whole) and then return before review; the return step
(`task-cycle/skill/return_step.md`) is resumed later.
Report path (write the full report here): `.runs/task-cycles/posix-class-not-a-link/reports/author_report.md`.
The report must hold **Unread material**, **Searches not found or unclear** (each `none` if so), the own-work
check, and every check with its command and exit code.
Do not run the product's gate (`python -B gate/run_tests.py`); run focused tests only:
`python -B gate/run_tests.py task-cycle` is allowed for the one directory.

Answers of step 4: touches a trust boundary: no. Irreversible operation: no. Open design choice: none.

Frozen task (read whole): `.runs/task-cycles/posix-class-not-a-link/task.md` (in Polish; commands to
you are its "To do", "Questions to settle" answers and "Settlements to record" row 1).

## What to change (the task's own requirements, not restated further)

1. `task-cycle/private_paths_check.py`: the note-link pattern `NOTE_LINK` no longer takes
   `[ [:name:] ]` for a link when `name` is one of `alnum alpha blank cntrl digit graph lower print punct space upper xdigit`.
   The exception lives in the shared pattern list so it holds for every check that looks for a link
   (cycle-record copy, request description, tracked files — `tracked_private_paths_check.py` reuses the same patterns).
   `[ [:other:] ]` and every other `[[...]]` with a letter or digit stays listed; a real link and a path on the
   same line as such a class stay listed. Update the module docstring where it describes what is no link.
2. `task-cycle/test_private_paths_check.py`: tests written first, failing before the change: each of the
   twelve names is not listed; `[ [:other:] ]` is listed; a real link `[ [Notatka] ]` / `[ [(P) Loop] ]` and a path on the same line
   are still listed; `[^[:space:]]` stays unlisted; behaviour through `tracked_private_paths_check.py`
   needs a test too if its tests (`test_tracked_private_paths_check.py`) already cover Markdown link rules —
   follow the style of the neighbouring tests (fixtures with made-up names, backslash as `BS`).
3. Foundation step, row 1 of *Settlements to record*: edit **WAY-323** in place in `foundations/decisions.md`
   (`### WAY-323`, line ~10549) through the pinned skill `.claude/skills/the-way-record-decision/SKILL.md`
   (read whole; it names its template/rules). WAY-323 is decided "in place"
   (`agent-instructions/README.md`, "Edit an existing decision in place", WAY-07). Add the exception to its
   statement, its *Verification* complies/violates examples and its rationale as the skill requires; keep
   decision form checks green (`python -B elements/common/foundation_check.py` — see how the gate calls it).
   Text of the entry in English; the entry is the cycle's row 1, keep in your report one English and one Polish
   sentence of its meaning, marked `row 1`.
   Note: the tracked-files invariant `tracked-file-private-paths` (foundations/invariants.md) excludes the script and its
   test from the check, but not decisions.md; with the exception in place a `[[:space:]]` written in the decision is not listed — verify by running
   `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` from the worktree root.
4. WAY-328: you write code and a test in part `task-cycle`; the-way departs from the general coding and testing
   guidelines there, so nothing waits and none are read. Follow neighbouring style.
5. Part map: `foundations/part_map.md` — compare the touched files with the part `task-cycle`; change it only if something no longer matches.

## What to read (selected by the orchestrator)

Foundation entries by identifier: WAY-323, WAY-324, WAY-309, WAY-308, WAY-328 (and WAY-07 for in-place editing),
invariant `tracked-file-private-paths`. Part: `task-cycle` (part map). Source passages: task.md whole.
Files: `task-cycle/private_paths_check.py`, `task-cycle/test_private_paths_check.py`,
`task-cycle/tracked_private_paths_check.py` and its test, `task-cycle/test_tracked_files_private_paths.py`.
Also follow `agent-instructions/README.md` ("Make the change": the one search of the whole foundation, WAY-33).

Commit on the branch with explicit paths (`git add <path>…`, never `-A`); commit messages in English.
Do not merge, push, open a request, or touch anything outside the worktree.
Return: status (`done` / `done with concerns` / `questions` / `returned` / `reserved` / `blocked`), commits,
a one-line check result, the report path.
