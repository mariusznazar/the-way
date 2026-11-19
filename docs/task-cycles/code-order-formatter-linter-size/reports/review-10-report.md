PASS 462add5d612623e09c0137d6b2b923d748661c38

# Review of slice 10, "entry" kept for an entry of the foundation

Range `0ccdc807..462add5d` (one commit, `462add5d`), branch `task/code-order-formatter-linter-size`. `git rev-parse HEAD` in the worktree is the head given.

Changed files (lines changed in the diffstat): `task-cycle/gate_times.py` 22 · `task-cycle/test_gate_times.py` 18 · `process-audit/test_record_items.py` 76 · `project-level/lead/skill/SKILL.md` 2 · `project-level/lead/conversation_template.md` 2 · `project-level/lead/answering.md` 2 (62 insertions, 60 deletions in all).

Counts: blocking 0, Minor 2, out of scope 0.

## Findings

### Blocking

None.

### Minor

1. `process-audit/test_record_items.py:58` and `:128` — the fixture text `...; entries none` stays. It is the detail text of a first sub-item of *Discarded attempt* in a record, where "entries" can only mean sub-items of a list under the record's items (the sense this slice replaces). The slice's check says a search for `entr` in the six files finds none of the uses the slice replaces, and this is one. The executor left it on purpose (its concern B) because it is a data literal and not a name or comment. No parser reads the words: `process-audit/record_items.py` reads the leading marker `reason: ...` only, and the tests assert on that marker, so replacing the text with `sub-items none` changes no result. Grade Minor: the use is two lines of free text in a fixture, it misleads nobody who reads the tests, and it breaks no behaviour. Evidence: `git grep -n -i entr -- <the six files>` finds only these two lines besides foundation entries, the invariant identifier at `task-cycle/test_gate_times.py:428,456` and `project-level/lead/skill/SKILL.md:11,142`.

2. `process-audit/test_record_items.py` the test now named `test_a_deeper_line_under_the_first_sub_item_is_no_sub_item_of_the_list` (was `test_a_sub_entry_under_the_first_entry_is_no_entry_of_the_list`). Its record holds a nested list item (`      - reason: ...`) under the first sub-item; the new name calls it a "deeper line". The sentence is accurate but loses that the line is itself a list item, which is what the test is about (it is not counted as a sub-item of the list). Wording only; the body and assertion are unchanged. Minor.

### Other observations (not findings)

- The warning in `task-cycle/gate_times.py:323` changed from `cannot end this run's entry in the registry` to `... file in the registry`. The handoff's step 4 says the same input gives the same message; the slice's Goal lists "messages" among what changes. The two do not agree for this one message. I follow the slice, since its Goal states it and no test, foundation entry or script reads the text (`git grep "cannot end this run"` finds only the code). The message goes to stderr as a `Warning:` and fires only where renaming the run's file fails; I did not trigger it. No exit code or verdict differs. Not a finding.
- Eleven of the twenty tests that this slice renames in `process-audit/test_record_items.py` hold a line `decision:` (WAY-404, WAY-405, WAY-344); two tests that cite `invariant: gate-times-refuses-impossible-entry` in `task-cycle/test_gate_times.py` are renamed. WAY-03 asks that a change that alters such a test, or its `decision:` line, name it in the request. The slice changes only names (and one comment); the bodies, assertions and `decision:` / `invariant:` lines are unchanged, which I checked in the diff. The request should name them. The list, computed by `reports/review-10-renamed_tests.py`: the eleven renamed tests with a `decision:` line are
  `test_one_sub_item_for_each_attempt_gives_yes_where_any_marker_is_an_open_design_choice`,
  `test_a_sub_item_without_a_marker_gives_unknown_unless_another_sub_item_is_an_open_design_choice`,
  `test_a_plain_first_attempt_under_an_empty_item_beside_a_sub_item_gives_unknown`,
  `test_a_plain_line_beside_the_sub_items_gives_unknown_with_its_reason`,
  `test_a_sub_item_first_under_the_item_and_deeper_than_the_next_one_is_not_dropped`,
  `test_a_hundred_thousand_sub_items_with_a_plain_line_beside_them_are_read_at_once`,
  `test_a_marker_in_a_deeper_line_of_a_sub_item_is_a_detail_and_is_not_read`,
  `test_a_sub_item_marked_yes_gives_yes_whatever_the_other_item_says`,
  `test_every_sub_item_marked_no_and_a_review_that_passed_give_no`,
  `test_a_sub_item_without_its_mark_gives_unknown_with_the_one_reason`,
  `test_only_the_sub_items_at_the_first_indent_and_outside_a_fence_are_read`;
  and the two invariant tests are `test_files_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing` and `test_a_malformed_file_that_cannot_be_deleted_still_counts_for_nothing`. The executor's concern C names only the two invariant tests. A changed invariant test is named here as the method asks: those two, renamed only.
- The executor renamed 20 tests, one helper function (`read_entries` to `read_sub_items`), a constant, a class (`RoundEntries` to `RoundSubItems`) and local variables, beyond the "about 24 test names" of the plan; the grep check of the slice requires it, and every renamed use is an item of a list under the record's items. `project-level/plan_check.py`'s own `read_entries` (table entries of the plan) is a different thing and was not touched.
- The word chosen for the lead files, "item" (`file/item/section`, `file/section/item`), fits a bullet or a table row and is not a glossary word; "change-log lines" in `SKILL.md` is F6's word. `gate_times.py` uses "file", the word of F7 and F8 (the invariant says "a file of its registry"). No glossary entry was added (WAY-95).
- Remaining `entr` uses are all the kept ones: `SKILL.md:11` "foundation entries", `SKILL.md:142` "an entry's binding meaning" (a foundation entry), the invariant identifier at `test_gate_times.py:428,456`.

## Declined to judge

- The 0-valued remaining `entr` hits in `project-level/lead/skill/SKILL.md:142`: kept as foundation-entry use; outside the six places the slice names.
- Whether "item" is the best word for the lead's source locators: the plan gives none; outside a defect judgment.

## Checks run

Run in a detached worktree of `462add5d` under `.runs/review-10/wt` (removed), unless said otherwise. `<ruff>` is `the Ruff of the quality environment of the main checkout`.

1. `<ruff> format --check --config ruff.toml task-cycle/gate_times.py task-cycle/test_gate_times.py process-audit/test_record_items.py` — exit 0 (3 files already formatted).
2. `<ruff> check --config ruff.toml --ignore-noqa` on the same three files — exit 0.
3. `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
4. `python -B gate/run_tests.py task-cycle` — exit 0, `Ran 534 tests`, `OK (skipped=2)`. Log `reports/review-10-test_task_cycle.log`.
5. `python -B gate/run_tests.py process-audit` — exit 0, `Ran 276 tests`, `OK`. Log `reports/review-10-test_process_audit.log`.
6. `python -B gate/run_tests.py project-level` — exit 0, `Ran 281 tests`, `OK`. Log `reports/review-10-test_project_level.log`.
7. Trust boundary, crafted input at `task-cycle/gate_times.py`: `python -B compare.py <work> <old gate_times.py from 0ccdc807> <new gate_times.py>` (script kept as `reports/review-10-compare_gate_times.py`), exit 0. Each case starts a fresh registry holding a file with an end more than a minute ahead, a start 3 days ahead (running), an end before the start, an ended file 2 days old, a stale running file 7 days old, a valid running file, one ending 30 seconds ahead, a stray `junk.txt` and a malformed name `12_x.run`; it runs the old and the new script with a succeeding command (exit 0), a command that exits 3, and a command that cannot be started. Result: exit codes the same in every case (0/0, 3/3, 2/2), stdout and stderr the same, the record row the same (other runs counted: 2 in both), the files that survive the same (malformed and stale ones deleted; junk and the malformed name left alone). The script printed DIFF for two cases only because the name of the run's own file carries a random token, which differs between any two runs of the same script; with that token normalised the surviving-file lists are equal. No irreversible operation: all files lay under `.runs/`.
8. `git grep -n -i "entr"` on the six files at the head — only the uses listed above.
9. `git grep -n "read_entries\|RoundEntries\|ENTRIES_IN\|test_entries_with_a_time\|test_a_malformed_entry"` — only `project-level/plan_check.py` (unrelated `read_entries`); no foundation entry or other file refers to a renamed name.
10. `python -B reports/review-10-renamed_tests.py` (script `reports/review-10-renamed_tests.py`, run from `.runs/review-10`): parses the old and new `test_record_items.py`, 36 tests in each, 20 renamed, 11 of those with a `decision:` line.

Not run: the full gate (by the handoff). Not triggered: the one reworded warning in `gate_times.py` (read only).

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-350 (`:8538-8548`, found by searching for the identifier): to see whether the foundation fixes a message text or the word "file" for the registry. It speaks of "an empty file for each run" and "a file whose times cannot be"; it fixes no message.
- `a private rule file of the author` before writing my comparison scripts, and `...\rules\git.md` (a hook held the first `git worktree add` until I had read it).
- `process-audit/record_items.py` and `project-level/plan_check.py`, `git grep` only, for the other uses of the words.

## Working copies

- `.runs/review-10/wt` — a detached git worktree of `462add5d`: removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-10/` — the scripts, the work directories and the logs: removed with `rm -rf`. What the report needs is kept in `reports/`: `review-10-test_task_cycle.log`, `review-10-test_process_audit.log`, `review-10-test_project_level.log`, `review-10-compare_gate_times.py`, `review-10-renamed_tests.py`. `.runs/` now lists only `orchestrator/` and `task-cycles/`; `git worktree list` shows no copy of mine. No remainder.
- The reviewed worktree stayed unchanged (`git status --short` clean, `HEAD` `462add5d`).

## Unread material

- `foundations/part_map.md:81-112` and `:125-136` — the handoff's step 4 names the trust-boundary files, so I did not open the part map; not read.
- `foundations/glossary.md` entry `entry` — read whole (`:49-53`). WAY-95, WAY-03 — read whole. WAY-48 (`foundations/decisions.md:2566-2595`) — not read; the handoff's list of trust boundaries and the invariant stood in for it. The invariant `gate-times-refuses-impossible-entry` (`foundations/invariants.md:538-547`, the handoff's current range) — read whole. F6, F7, F8 — taken from the handoff's words ("line", "file") and checked against the invariant's sentence and WAY-350, not each read whole as separate entries; their wording was not otherwise opened.
- `guidelines/coding.md`, `guidelines/coding-command-runner.md`, `guidelines/testing.md` — not read; the change renames words and the rules of those files (size, structure, test form) are not reached by a rename with no changed behaviour or test body.
- Task passages `task.md:36` and `task.md:96` — read.
- The handoff's line addresses for the foundation entries are one line off from the range I found in the worktree (e.g. the invariant starts at `:538`, the handoff's Read says `:518-526`); I read by identifier.

## Searches not found or unclear

- The handoff's Read lists `foundations/invariants.md:518-526` for the invariant, whereas its range list says `:538-547`; the latter is correct in the worktree (the entry is at `:538`).
- The handoff's task passage speaks of "the entries of the decision log in the scripts that compare it" as a kept use; no such use occurs in the six files, so nothing was set against it (the executor found the same).
