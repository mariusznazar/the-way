# Executor report — slice 5 of `scripts-after-foundation-review`

**Status:** done

**Slice:** 5 — A register table without a level names the level; a missing `repository` entry under `the-way` is no missing field

**Worktree:** `the root of the task's worktree`, branch `task/scripts-after-foundation-review`

**Commit:** `61894c2` — "Name the level a register table lacks or writes twice, and pin the missing repository entry" (on top of base `aaed860`; the base of the task is `7f5c5a5`, the slice's own base is the branch head before this commit)

## Files changed

| File | Added | Removed |
|---|---|---|
| `process-audit/audit_count.py` | 34 | 12 |
| `process-audit/test_audit_count.py` | 67 | 2 |

## What the slice changes

- `process-audit/audit_count.py`
  - The two sentences "the table `Weights` must name the four levels, each once" and "the table `Costs of an occurrence` must name the five levels, each once" are replaced by one rule in a new helper `check_levels`, which calls `level_faults` for the words. The line now reads "the table `<title>` must name each level once: it lacks `<level>`", or "it writes `<level>` in two rows", or both joined by "and". The result is still written, the values depending on the table are unknown, exit code 1.
  - The module description (the paragraph on the register's tables, near line 205) says the `Error:` line names the level lacked or written twice.
  - The entry `repository` under `the-way` was already handled by `the_way_checkout` (checkout the script lies in) and its sentence is already in the module description (line 26-27). No code change was needed for it; the test pins it.
- `process-audit/test_audit_count.py`
  - `RegisterCount.test_a_table_of_costs_that_lacks_a_level_is_treated_as_the_table_of_weights_is` changed first: it now asserts the line that names `stage` (missing), `steps` (written twice), and both together. The WAY-344 decision sentence this test holds is the one about the table of the costs of an occurrence.
  - New `RegisterCount.test_a_table_of_weights_that_lacks_a_level_names_the_level`, the like test for *Weights* (missing `Minor`, written twice `Important`, both together).
  - New `Locations.test_the_way_with_no_repository_entry_is_the_checkout_the_script_lies_in`: a locations file with no `repository` under `the-way`; a product cycle whose pin is `HEAD` of the checkout the script lies in; a fixed issue whose fix is that same commit; asserts exit 0, empty stderr, the pin in the *Cycles* table, no *Unknown values* row for the pin, and the fixed issue counted as held.

## Checks

Each check, its command and exit code.

1. **Failing run on the base, before the code change** (tests changed, code not yet): `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k RegisterCount -k Locations`. Result: `FAILED (failures=6)`, all six subtests of the two register tests, each asserting the line that names the level, with the line the base gave: "the table `Costs of an occurrence` must name the five levels, each once" / "the table `Weights` must name the four levels, each once". The exit code was not captured (the output was piped through `tail`); unittest exits 1 on failure. The new Locations test passed on the base, as expected: the behaviour existed and the test pins it.
2. **Baseline before any change** (same command, `-k RegisterCount -k Locations`): `Ran 44 tests`, `OK` (exit not captured, piped through `tail`).
3. **Passing run after the change**, same command: `Ran 46 tests`, `OK`, **exit 0**. Run again on the final tree (after a cosmetic line wrap in the test file): `Ran 46 tests`, `OK`, **exit 0**.
4. **Full file** `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`: `Ran 184 tests`, `FAILED (failures=1)`. The one failure is `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` (line 885: expected `["0.014250", "1", "15.8%"]`, got `["unknown", "unknown", "unknown"]`). **The same test fails on the base commit `aaed860`** (run in a clean worktree, exit 1, `FAILED (failures=1)`), so it is pre-existing and not caused by this slice; it concerns the pricing of cache writes, which this slice does not touch. Its exit code is **1** (captured in the background run's output). The full file ran before the cosmetic wrap; the focused classes were re-run after it (check 3).
5. **Series file** `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: `Ran 3 tests`, `OK`, **exit 0**.

Not run: the whole gate (WAY-160), by the handoff.

## Own-work check (section 3)

- Requirement most likely unmet: a missing level or a doubled level still ends with the old line, or the new line names the wrong level; or the missing-level check counts a doubled level as missing, or the `repository` case starts ending with exit 2.
- Check: the two register tests (missing, doubled, both) for each table assert the exact line, and the Locations test asserts exit 0 and empty stderr with a pin resolved in the checkout.
- Shown: the failing run on base (check 1) and the passing run (check 3). No check failed and passed on rerun, so no paired runs are needed beyond check 1.
- Mutations considered in my head: dropping the `missing` list fails the "lacks" subtests; dropping the `doubled` list fails the "writes" subtests; computing `missing` from the *valid* names (after `named_rows` drops doubled names) would report a doubled level as missing, and the "both" subtest (stage missing and steps doubled) guards that; making `the_way_checkout` raise on a missing entry fails the Locations test; making `Ancestry` read another checkout fails the held-count assertion.

## Choices made

1. **Message wording**: "must name each level once: it lacks `stage`" / "it writes `steps` in two rows". Rejected: keep "must name the five levels" plus a second line (two lines, both must be read). Cost if wrong: a reader of stderr who greps the old sentence will miss it; the WAY-344 text does not fix a wording.
2. **Missing levels counted from rows of the right width, not from the valid names**: `named_rows` drops every row whose name is written twice, so a doubled level would look missing. Rejected: reuse the valid names. Cost if wrong: "lacks steps" for a doubled level. The "both" subtest guards it.
3. **One helper for both tables** (`check_levels` / `level_faults`) instead of two copies of the check. Rejected: duplicate the block. Cost: none known.
4. **The Locations test pins the checkout by `git rev-parse --verify HEAD` of the checkout the script lies in** (the test runs in a git checkout). Rejected: a fixture repository, which would not exercise the script's own checkout. Cost if wrong: in a copy without `.git` the test errors, it does not pass silently.
5. **No code change for the `repository` exception**: `the_way_checkout` already returned the own checkout when the entry was missing; the slice asked for a pin of that behaviour, not a new reading. Rejected: a new branch. Cost: none.

## Changed invariant tests, named (WAY-03)

- `test_a_table_of_costs_that_lacks_a_level_is_treated_as_the_table_of_weights_is` (RegisterCount): changed; it holds the sentence of WAY-344 about the table of the costs of an occurrence (the level named in the `Error:` line), now asserting the level, not the table.
- The new `test_a_table_of_weights_that_lacks_a_level_names_the_level` and `test_the_way_with_no_repository_entry_is_the_checkout_the_script_lies_in` hold the WAY-344 sentences for *Weights* and for the entry `repository`.

## Reaches beyond the handoff (what, where, why)

- Read `process-audit/audit_count.py` around `main`, `entry_path`, `repositories`, `read_register`, `named_rows`, `register_table` and the module description, to find the sentences and the flow of `register.errors`. Needed to locate the change.
- Read the test file's helpers (`TEMPLATE`, `register_text`, `issue_row`, `problem_row`, `record`, `Repository`, `AuditCountCase`) to write the tests the way the file writes them.
- Read `task.md` lines 28-30, 51-58, 134, 143-144 and `foundations/decisions.md` WAY-344 and WAY-330, invariants, part map, glossary passages named or ranged by the handoff. All were read as ranged.
- Did not read `project-level/technology/reserved_choices.md`: the work needed no language, library or place to run, so section 5 did not apply.
- Did not touch `elements/common/foundation_check.py` or the WAY-344 sentence in the foundation (the other task owns them).

## Working copies

- `.runs/executor-5/base`: a detached worktree of `aaed860`, used for check 4's failing-on-base run. **Removed** with `git worktree remove --force`, then `git worktree prune`; the prune listing no longer shows it. The directory `.runs/executor-5/` remains, empty.
- Temporary text outputs of the runs were written to the system temp folder and removed by me (`ac.txt`, `base_one.txt`, `focus_final.txt`). A file `as.txt` in the same temp folder was written by my background command's redirect but its content is node output from another run; I did not remove it.

## Unread material

- `project-level/technology/reserved_choices.md`: not read (not needed, see above).
- None other: the files and ranges the handoff names were read as ranged.

## Searches not found or unclear

- None found missing. The one unclear item: the pre-existing failure `test_the_stage_report_cycle_stages_writes_gives_the_share` on the base; its cause was not investigated (outside the slice).
