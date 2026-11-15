# Report of the executor of slice 8

**Status:** done

**Commit:** `6cf3fa9` (base `8ef214d`). File changed: `process-audit/test_audit_count.py`, +48 -28.
`process-audit/audit_count.py` is unchanged (`git diff -- process-audit/audit_count.py` empty after the break was undone).

## What was done

- (a) Cause 4. The two runs of `test_the_same_input_gives_the_same_bytes_in_both_files` take `--today 2026-11-11`;
  the names are asserted as exactly `["count-2026-11-11.md", "count-latest.md"]` in place of a regex on a date.
  `run_count` has `timeout=None` as its default (was 120) and a new argument `script=SCRIPT`. A test that passes a
  limit keeps it.
  Limits that are the test's oracle and stay (named as the slice asks):
  `test_a_header_line_of_blanks_does_not_stall_the_count` and
  `test_a_long_continuation_of_a_header_line_does_not_stall_the_count` (`timeout=60`),
  `test_a_long_run_of_blanks_in_a_class_name_does_not_stall_the_count` (`timeout=60`), and
  `test_it_reads_nothing_from_stdin` (`process.wait(timeout=60)`: a command that read stdin would wait for ever).
  No test that passed 60 had a limit that was no oracle; the only limit that was no oracle was the helper's default 120.
- (b) Cause 6. `test_the_way_without_a_repository_entry_is_this_checkout` builds a repository in the temporary directory
  (`Repository("checkout")`) that holds a copy of `process-audit/audit_count.py`, `process-audit/price_list.md` and
  `task-cycle/remarks_check.py` (the script imports the last from `../task-cycle` and reads the price list beside it) and
  one cycle record, runs the copy and asserts `[ ["the-way", "1", "yes"]]`. The old assertion (`row[2]` starts with `yes`)
  passed on any checkout.
- (c) Cause 7. A constant `NO_USER_GIT_CONFIG = {GIT_CONFIG_GLOBAL: os.devnull, GIT_CONFIG_NOSYSTEM: "1"}` is in
  `GIT_ENV` and in the environment of `run_count`. Beyond the two places the slice names, git also runs in the
  file in: the `rev-parse` of the test of the checkout the script lies in and the `ls-files` of
  `test_each_path_that_starts_a_series_is_a_path_git_tracks` (both given `env=GIT_ENV`), and the process of
  `test_it_reads_nothing_from_stdin` (given the constant). The clone in the shallow-clone test already used `GIT_ENV`.
  The call that runs `cycle_stages.py` (no git) is untouched.
- (d) Cause 26. All 14 RUF059 places of the base are `_`: 11 times `added` of `done, added = self.count(...)` or
  `added, cycle, cost = ...`, and `why` in three places of the tests of the share (`row, _`). In
  `test_findings_files_in_review_rounds_are_read_only_in_their_form` the reason is checked, not dropped: for each
  crafted path `why` holds a reason with `names no findings file` (seen by running: "an entry of the item `Review
  rounds` names no findings file: it does not open with ...").
- (e) `# invariant: audit-count-refuses-record-links` stands above `test_a_symbolic_link_leaving_the_record_is_not_followed`
  (position as in `task-cycle/test_gate_times.py:341`).

## Left of the linter in this file

F541 at `process-audit/test_audit_count.py:2388:38` (an f-string with no placeholder in the expected pair of a crafted-register test, a line of the base that this slice did not write).
Left under the invariant marked violated, as the plan's *Choices* give.

## Checks (command, exit code)

| Check | Command | Exit |
|---|---|---|
| Whole file | `python -B process-audit/test_audit_count.py` (231 tests, 305.8 s; also the base before my edits: 231 tests, exit 0) | 0 |
| Invariant test failing, refusal broken for a moment (`kind != b"blob" or not mode.startswith(b"100")` reduced to `kind != b"blob"` in `read_file` of `audit_count.py`) | `python -B -m unittest test_audit_count.CraftedInput.test_a_symbolic_link_leaving_the_record_is_not_followed` (run in `process-audit/`) | 1 (`AssertionError: 0 != 1`) |
| Same test, break undone | same command | 0 |
| Script unchanged | `git diff --stat -- process-audit/audit_count.py` | empty |
| Linter | `<ruff> check --config ruff.toml --no-cache --ignore-noqa process-audit/test_audit_count.py` | 1: one report, F541 at line 2388, no RUF059, nothing on a line the slice wrote |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 (`0 errors`) |

The output of the whole-file run is in `reports/executor-8-full-run.txt`.

## Own-work check (WAY-164)

Requirement most likely not met: cause 6, that the test runs on the repository built in the temporary directory and not
on this checkout. Check: ran the test with `run_count` made to ignore `script` (the real script, the real checkout);
it fails with `[ ['the-way', '1', 'yes']] != [ ['the-way', '105', 'yes']]`, so the new assertion tells the two checkouts
apart and the passing run reads the copy's history. (`python -B` snippet that patched `AuditCountCase.run_count`, run in
`process-audit/`; the failing run took 54 s.)

Weakest point: (c) is checked by reading, not by a test: no test shows git failing under a hostile global
configuration, and the slice's *Checks* ask for none. Mutation in my head: removing `NO_USER_GIT_CONFIG` from
`run_count` makes no test fail on this machine.

## Choices (way rejected, cost if wrong)

- `run_count` default limit is none. Rejected: keeping 120, or a larger number: still a wall-clock red on a very slow
  machine, with no oracle. Cost if wrong: a script that hangs hangs the test (the gate has no timeout of its own); the
  tests that ask whether the count stalls keep their 60 s.
- The checkout of (b) holds the three files the script needs, listed in the test. Rejected: copying the whole of `process-audit/` and `task-cycle/`:
  larger and no better. Cost if wrong: a new import of the script into another file makes this test fail with an
  import error, which names the file.
- Citation comment above `def`, as the other tests of the repository place it.

## Reaches beyond the handoff

None, except reading `process-audit/audit_count.py` around `read_file` (to choose the break) and the rest of the slice's
named lines of the script (imports, lines 313-345), and `task-cycle/test_gate_times.py:341` for the form of the
citation.

## Working copies

`.runs/executor-8/` held the output of the whole-file run; copied to `reports/executor-8-full-run.txt` and the
directory removed. An abandoned first probe directory `.runs/executor-8/probe` (the result directory lay inside the
repository and the script refused it) was removed. No worktree or clone was made.

## Mismatches between handoff and code (small, adapted)

- The line numbers of the task's *Places* (2378, 2435, 182 ...) are not the worktree's; used the names of the tests.
- The handoff says "13 at the task's commit, 14 at the base" for RUF059: 14 found, all cleaned.
- `Read` names `foundations/decisions.md:2823-2968` for WAY-344: read whole to its end (2967).
- The test runs for 5 to 6 minutes; the whole-file run was done in the background.

## Unread material

- `.runs/task-cycles/.../task.md:34-35,41-44,46,92-97,161-168,177-181,253-259,267-279,391-397,543`: read.
- E11 (WAY-394) and E12 (WAY-395): read whole. E32: read whole. WAY-48, WAY-235, WAY-08, WAY-243, WAY-344:
  read whole.
- `foundations/invariants.md:166-175` (`test-method-citation`): read. The invariants named in the orchestrator's
  additions (`script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`) and
  `foundations/part_map.md` beyond lines 124-134: not read; the slice adds no import, subprocess of the script, or
  file. `part_map.md:124-134` read.
- `project-level/test_plan_state_invariant.py:195-205`: read. `process-audit/audit_count.py:1-60`, `:325-345`
  (`313-345` read), `:3240-3310`: read. The whole of the end of `plan.md`: read (the tail 60 lines); the rest of
  `plan.md`: not read (the handoff carries the slice).

## Searches not found or unclear

none
