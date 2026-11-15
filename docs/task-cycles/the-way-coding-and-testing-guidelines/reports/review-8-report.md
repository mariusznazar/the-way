PASS 6cf3fa9b2a998499d5b0141e3ce1aed834db7d54

# Review of slice 8 (range 8ef214d..6cf3fa9), one file: `process-audit/test_audit_count.py` (+48 -28)

`git rev-parse HEAD` is `6cf3fa9`, the head given. `git diff 8ef214d..6cf3fa9 -- process-audit/audit_count.py` is empty.

## Findings

Blocking (Critical, Important): none.

Minor: none that I hold up. Notes that are not findings:

- `process-audit/test_audit_count.py:192` — `run_count` now has no limit of wall time unless a test passes one. A script
  that hangs now hangs the test (the gate has no timeout of its own). This is what the slice asks (a limit that is no
  oracle is removed), and the tests that ask whether the count stalls keep `timeout=60` (lines 678, 686, 2447, and
  `process.wait(timeout=60)` at 3130). No finding.
- `process-audit/test_audit_count.py:2388` — F541 remains: a line of the base the slice did not write; the report names
  it as the slice asks.

## What I checked against the slice

- (a) The two runs of `test_the_same_input_gives_the_same_bytes_in_both_files` (line 3140 and 3142) take
  `--today 2026-11-11`, and the names are asserted exactly (`["count-2026-11-11.md", "count-latest.md"]`). The helper's
  default limit 120 is gone. Each remaining `timeout=60` (678, 686: header-line stall tests; 2447: class-name blanks
  stall test; 3130: stdin) has the limit as its oracle; the executor names them.
- (b) `test_the_way_without_a_repository_entry_is_this_checkout` (line 3193) builds `Repository("checkout")` in the
  temporary directory with a copy of `audit_count.py`, `price_list.md` and `remarks_check.py` (the imports of the script,
  checked at `audit_count.py:329-342`; `remarks_check.py` imports only the standard library), runs the copy through the new
  `script=` argument, and asserts `[ ["the-way", "1", "yes"]]`. The count `1` cannot come from this checkout (105 cycles
  per the executor's run), so the assertion tells the two apart. The `Repository.cycle` helper puts the copy in
  history as the script reads it.
- (c) `NO_USER_GIT_CONFIG` (`GIT_CONFIG_GLOBAL=os.devnull`, `GIT_CONFIG_NOSYSTEM=1`) is in `GIT_ENV` and in the
  environment of `run_count`, as `project-level/test_plan_state_invariant.py:197-198` sets them. Beyond the slice's two
  places, the executor gave the same to the `rev-parse` (849), the `ls-files` (3532) and the stdin process (3128); the
  other git calls (`Repository.git` through `env()`, the clone at 2914) already used `GIT_ENV`. I found no git
  call in the file left without it; the `cycle_stages.py` call (1091) runs no git. The `dict(..., **NO_USER_GIT_CONFIG,
  **(env or {}))` would raise `TypeError` on a duplicate key, but the only test that passes `env` (3187) passes
  `GIT_DIR` and `GIT_WORK_TREE`; it runs green.
- (d) The linter reports no RUF059 in the file. The unused names are `_` (11 in `done, added` / `added, cycle, cost`
  and 3 `row, _` of the share tests per the diff: 14 places in all). In
  `test_findings_files_in_review_rounds_are_read_only_in_their_form` the reason is checked
  (`names no findings file`, line 1209) instead of dropped.
- (e) `# invariant: audit-count-refuses-record-links` stands above `def test_a_symbolic_link_leaving_the_record_is_not_followed`
  (line 637), the form of `task-cycle/test_gate_times.py:341`. The invariant (`foundations/invariants.md:528`) reads
  `test` and part `process-audit`; the full `foundation_check.py` no longer reports it as uncited.
- The test fails when the refusal breaks: in my own worktree of the head I reduced
  `if kind != b"blob" or not mode.startswith(b"100"):` (`audit_count.py:1580`) to `if kind != b"blob":`; the test
  fails (`AssertionError: 0 != 1`, exit 1); with the file restored, the test passes. This is not a test that computes its
  own expected value: it plants a symbolic link in a crafted history and expects unknown values.
- The code the slice writes breaks no rule of `ruff.toml` (the linter reports nothing on a changed line). Trust boundary:
  the script is not changed; the added citation only names the invariant of the refusal; no crafted input is added
  beyond what the test already held, and the change does nothing the slice does not say.
- Weakest point of the slice, as the executor says: (c) has no test that shows git failing under a hostile user
  configuration; the slice's *Checks* ask for none. I do not grade this.

## Declined to judge

none

## Checks run

| Check | Command | Exit |
|---|---|---|
| Range and head | `git rev-parse HEAD`; `git log --oneline 8ef214d..6cf3fa9`; `git diff 8ef214d 6cf3fa9` | 0 (one commit, one file) |
| Script unchanged | `git diff 8ef214d 6cf3fa9 -- process-audit/audit_count.py \| wc -c` | 0 bytes |
| Linter | `<ruff> check --config ruff.toml --no-cache --ignore-noqa process-audit/test_audit_count.py` | 1: one report, F541 at 2388, no RUF059 |
| Focused tests of the changed places (in `.runs/review-8/wt`, run in `process-audit/`) | `python -B -m unittest test_audit_count.CraftedInput.test_a_symbolic_link_leaving_the_record_is_not_followed test_audit_count.Run test_audit_count.Locations test_audit_count.Cost` | 0 (73 tests, 66 s) |
| Invariant test with the refusal broken (line 1580 of the script reduced, in my copy) | `python -B -m unittest test_audit_count.CraftedInput.test_a_symbolic_link_leaving_the_record_is_not_followed` | 1 (`0 != 1`), as it must |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 (`0 errors`) |
| Foundation check with citations | `python -B elements/common/foundation_check.py` | 1 (7 errors, all of other invariants whose slices are later; none names `audit-count-refuses-record-links`) |

Not run: the whole file `python -B process-audit/test_audit_count.py` (305 s per the executor; I relied on its
recorded run `reports/executor-8-full-run.txt` and reran the classes that hold every changed test except the
`Times`, `MechanismMeasures`, `GateRunsMeasures` and `ProcessVersions` classes, whose changes are `_` renames and
an `env=` argument). Unverified by me: the whole-file exit 0.

## Reaches beyond the dispatch

- `process-audit/audit_count.py:1575-1585` (to choose the break) and `:329-342` (imports) — what the test must hold.
- `task-cycle/remarks_check.py` imports (`grep`) — to confirm the copy holds all the script needs.
- `task-cycle/test_gate_times.py:341` — the form of the citation.
- `foundations/invariants.md:528` — E32, whole as printed.

## Unread material

The decisions WAY-48, WAY-235, WAY-08, WAY-344, WAY-243, E11, E12 and the task's passages: not read whole by me; I judged
the slice from the handoff's slice text and the diff and read no decision, since the change touches no behaviour of
the script they bear on. The invariants of the orchestrator's additions (`script-language`, `script-imports`,
`script-subprocesses`, `cross-part-imports`, `test-method-citation`): not read whole; the slice adds no import, no
file and no subprocess of the script, and `test-method-citation` was checked through `foundation_check.py`. The
executor's report: read whole. The foundation guidelines of the product: none are named.

## Searches not found or unclear

none

## Working copies

`.runs/review-8/wt` (a worktree of `6cf3fa9`, with a broken line in my copy that I undid with `git checkout`): removed
with `git worktree remove --force` and `git worktree prune`; `.runs/review-8/` holds nothing.
