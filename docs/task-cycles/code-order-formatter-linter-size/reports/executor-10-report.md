# Executor-10 report — slice 10, "entry" kept for an entry of the foundation

**Status:** done with concerns

**Commit:** `462add5d` on `task/code-order-formatter-linter-size` — "Replace the word entry where it does not mean an entry of the foundation" (base `0ccdc807`).

**Check result:** all focused checks pass (task-cycle 534 tests OK, process-audit 276 OK, project-level 281 OK, foundation check 0 errors, ruff format and ruff check exit 0). The full gate was not run, by design.

## Files changed (6 files, +62 / −60 lines)

| File | Change |
|---|---|
| `task-cycle/gate_times.py` | 22 lines: "entry" for a registry file → "file" (description, docstrings, local names, one warning message) |
| `task-cycle/test_gate_times.py` | 18 lines: comments of the tests of `gate-times-refuses-impossible-entry`, two test names, one local name → "file" |
| `project-level/lead/skill/SKILL.md` | 1 line: "their change-log entries" → "their change-log lines" |
| `project-level/lead/conversation_template.md` | 1 line: "file/entry/section" → "file/item/section" |
| `project-level/lead/answering.md` | 1 line: "file/section/entry" → "file/section/item" |
| `process-audit/test_record_items.py` | 37 lines: sub-item uses → "sub-item" / "sub_item" (names, helpers, constant, class, locals, comment) |

Before/after copies of the three Python files were kept only in my working directory, which is removed (see below).

## Checks run

Each run from the worktree root `the worktree's root`.

1. `the Ruff of the quality environment of the main checkout format --config ruff.toml task-cycle/gate_times.py task-cycle/test_gate_times.py process-audit/test_record_items.py` — exit 0; reformatted `test_record_items.py` (long `def` lines only); the other two were unchanged.
2. `<ruff> format --check --config ruff.toml` on the same three files — exit 0 ("3 files already formatted").
3. `<ruff> check --config ruff.toml --ignore-noqa` on the same three files — exit 0 ("All checks passed!").
4. `python -B gate/run_tests.py task-cycle` — exit 0; `Ran 534 tests in 84.124s`, `OK (skipped=2)`. Log: `reports/test_task_cycle.log`.
5. `python -B gate/run_tests.py process-audit` — exit 0; `Ran 276 tests in 309.528s`, `OK`. Log: `reports/test_process_audit.log`.
6. `python -B gate/run_tests.py project-level` — exit 0; `Ran 281 tests in 107.913s`, `OK`. Log: `reports/test_project_level.log`.
7. `python -B elements/common/foundation_check.py` — exit 0; `0 errors`. Log: `reports/foundation_check.log`.
8. `git grep -n -i "entr"` on the six files — remaining hits are listed under *Kept uses* below; none is a use this slice was meant to replace, except the two record literals noted under the choices.
9. Trust-boundary comparison of `task-cycle/gate_times.py`, old copy from `0ccdc807` against new copy: `python -B compare_gate_times.py <old> <new> <work>`, exit 0, `mismatches: 0`. Five crafted cases, each run as its own registry with a command that succeeds, a command that exits 3, and mixed states:
   - `all_ok`: SAME (exit 0 both, record rows same, surviving files same, stderr same)
   - `all_fail`: SAME (exit 3 both)
   - `only_malformed`: SAME (malformed files deleted in both)
   - `only_valid`: SAME (valid running and near-ending files kept, counted the same)
   - `none`: SAME
   Timestamps of created file names were masked in the comparison, since each copy names files from its own clock reading a few milliseconds apart.

Not run: the full gate (`python -B gate/run_tests.py` with no directory), by the handoff. No invariant test was added or changed in its body, so no break-and-restore run was needed.

## Own-work check (WAY-164)

- **Requirement most likely missed:** the script's behaviour must not change, though its messages and names change. The message wording changed in one place.
- **Check:** the crafted-input comparison above, plus the grep and the test runs.
- **Result:** verdicts, exit codes, record rows and surviving files are identical on all five cases. The only textual difference is the one warning, `cannot end this run's entry in the registry` → `cannot end this run's file in the registry`, which the comparison maps back before comparing.
- **Weakest point:** that warning fires only when the rename of a finished run's file fails. None of the crafted cases triggers it, so the new wording was not run; only read. The change is one word inside an f-string.

## Choices made, with the way rejected and its cost if wrong

1. **Word for the lead's source locators: "item".** Alternatives were "row" (the lead's files already use "row" for table rows) and "heading". "Item" fits both a bullet and a table row. Cost if wrong: a one-word edit in two files.
2. **Renames beyond the test names in `test_record_items.py`.** The handoff says "the names of about 24 tests". The check's grep requires that every sub-item use in that file be replaced, so I also renamed the helper `read_entries`, the constant `ENTRIES_IN_NEITHER_FORM`, the class `RoundEntries`, and the local variables. No behaviour changes. Cost if wrong: a wider diff than the handoff named (37 lines in that file, 38 edits).
3. **Local names in `gate_times.py` and its tests.** `entry` local variables became `file`, and the test local `entries` became `files`, so that the grep finds no leftover use. Cost if wrong: none for behaviour.
4. **Sub-item words in test names.** A line deeper than a sub-item was renamed from "sub entry" to "deeper line" (`test_a_deeper_line_under_the_first_sub_item_is_no_sub_item_of_the_list`), because the old name meant a line under a sub-item, not a sub-item.
5. **Ruff format** made the long `def` lines in `test_record_items.py` into wrapped form. Nothing else.

## Concerns for the orchestrator (decision needed)

A. **Message wording vs. the trust-boundary rule.** The handoff says `gate_times.py` must give "the same verdict, exit code and message for the same input". The goal of this slice also says to change "messages". These conflict for the one warning above. I followed the goal: the verdict, exit code and record are identical; only the one word changed. Ways open: (a) keep the wording and accept the word "entry" in one warning; (b) keep my change, as done. Cost of (a): the registry's word stays inconsistent in one message. Cost of (b): a reviewer may read the wording change as breaking the "same message" rule.

B. **Two record literals left as data.** `process-audit/test_record_items.py` lines 58 and 128 hold the text `entries none` inside a sub-item fixture. No parser reads the word, but changing a fixture string is not a name or a comment. Left unchanged. If you want the grep clean, the change is `entries none` → `sub-items none` in both places; the tests should not change result.

C. **WAY-03: invariant tests with changed names.** The tests that cite `invariant: gate-times-refuses-impossible-entry` changed their names, not their bodies or assertions: `test_entries_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing` → `test_files_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing`, and `test_a_malformed_entry_that_cannot_be_deleted_still_counts_for_nothing` → `test_a_malformed_file_that_cannot_be_deleted_still_counts_for_nothing`. The invariant's sentence did not change. The request should name these two tests, per WAY-03.

## Kept uses of "entr"

- `project-level/lead/skill/SKILL.md:11` "foundation entries" — a foundation entry.
- `project-level/lead/skill/SKILL.md:142` "a choice enters an entry's binding meaning" — a foundation or decision entry. Not named by the handoff; kept.
- `task-cycle/test_gate_times.py:428,456` `# invariant: gate-times-refuses-impossible-entry` — the invariant's identifier, which stays.
- `process-audit/test_record_items.py:58,128` `entries none` — the data literal in B.

## Unread material

- `.runs/task-cycles/code-order-formatter-linter-size/task.md` lines 36 and 96 — read.
- `foundations/part_map.md:81-112` and `:125-136` — **not read**. The slice's *Read* names them. I did not need them to make the change, since the slice names the files, and the trust boundary was identified from the handoff's list. Flagging as unread.
- `foundations/decisions.md` WAY-48 (`:2566-2595`) — read only its heading and first lines. Not needed for the change.
- WAY-03, WAY-95, WAY-145, WAY-350, the invariant `gate-times-refuses-impossible-entry`, and the glossary entry for "entry" — read.
- Guidelines `guidelines/coding.md`, `guidelines/coding-command-runner.md`, `guidelines/testing.md` — read whole.
- `task-cycle/change/SKILL.md` and `slice.md` — read whole.
- Foundation entries F6, F7, F8 — read as above.

## Searches not found or unclear

- The phrase "file/entry/section" in the lead files: the handoff gives no replacement word; I chose "item" (choice 1).
- The handoff's phrase "the entries of the decision log in the scripts that compare it" — no such use appeared in the six files, so nothing was kept under it.

## Reaches beyond the handoff

- Read the user's rule file for writing scripts (`a private rule file of the author`) before writing the rename and comparison scripts, and the git rules file (`a private rule file of the author`) before the commit (the first commit attempt was held by a hook until the file was read; the second attempt was the same command).
- Read `project-level/lead/answering.md` and `conversation_template.md` around the locator lines, to choose the word.

## Working copies

- `.runs/executor-10/` — contained the pre-change copies of three `.py` files (`before/`), the rename script, the comparison script, the comparison's case folders (`work/`), and the logs. Removed with `rm -rf`, and the removal was checked: `.runs/` no longer lists `executor-10`. No git worktree was made, so no `git worktree remove` was needed.
- The four check logs were moved into `.runs/task-cycles/code-order-formatter-linter-size/reports/` (`test_task_cycle.log`, `test_process_audit.log`, `test_project_level.log`, `foundation_check.log`).
- No copy remains outside the reports directory.
