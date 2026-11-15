PASS 61894c282d8e92625ba1730ee967975d9d32c4d9

# Review of slice 5 — task `scripts-after-foundation-review`

Range `aaed860..61894c2` (one commit, `61894c2`); `git rev-parse HEAD` is the head given. Variant: review of a slice. Blocking: 0. Minor: 1. Out of scope: 0.

## Findings

### Blocking

none

### Minor

1. `process-audit/audit_count.py:248-256` (the paragraph on exit codes) — the goal of the slice says the module description says, beside its exit codes, that the `Error:` line names the level. The change says it in the paragraph on the register's tables (`audit_count.py:204-207`), a screen above; the paragraph on exit codes still says only "a table of the register refused as a whole". The description does say it, and no reader is led wrong, so the effect is a reader of the exit codes who does not learn that the line names the level. Evidence: `git diff` of the file touches only the lines near 205.

## Verification of the claims

- The code: `level_faults` takes the names of the rows of width 2 (a row of another width counts for no level, and is refused on its own by `named_rows`), so a level written twice is not read as missing. `check_weight` and `check_cost_level` refuse a row only for a name that is no level, so the names of rows of the right width equal the valid names plus the doubled ones; the new check refuses the same tables as the old comparison of sorted names did, and only the text of the `Error:` line changes. The result is still written, the table is refused (values unknown), exit code 1 (`read_register` appends to `register.errors`, as before).
- Trust boundary: the level words in the `Error:` line come from the constants `LEVELS` and `COST_LEVELS`, never from the register's text, so crafted cells (backticks, newlines, long text, wrong width, a doubled name, an unknown level) cannot reach the line unescaped; a crafted row neither crashes `level_faults` nor changes the exit code (a row of another width is skipped, a name outside the levels matches nothing). No new write, no command run, no new file read.
- The entry `repository` under `the-way`: `the_way_checkout` (`audit_count.py:514-518`) already gave `OWN_CHECKOUT` when the entry is missing, `repositories` uses it for `--repository the-way`, `main` uses it for `Ancestry`; the sentence stays in the module description (`audit_count.py:26-27`). No code change was needed and none was made; no other reading of a file changed. This matches WAY-344 as it stands in `foundations/decisions.md:2741-2901` (the exception for levels and for the entry `repository`, with the "violates" and "complies" lines and the *Rejected* variants).
- The tests: the changed `test_a_table_of_costs_that_lacks_a_level_is_treated_as_the_table_of_weights_is` and the new `test_a_table_of_weights_that_lacks_a_level_names_the_level` give the table without one level, with one written twice and with both, and assert the whole line text, the unknown value `table ...` and exit code 1; the "both" case catches a missing count taken from the valid names. The new `Locations.test_the_way_with_no_repository_entry_is_the_checkout_the_script_lies_in` gives a locations file without the entry (asserted), a pin that is the commit of the checkout the script lies in, and asserts exit 0, empty stderr, the pin in *Cycles*, no unknown *Process pin*, and the fixed issue counted: it fails if the command read another checkout (the pin is no commit of the product) or ended with exit 2. It passes on the base, as the executor said, since it pins an existing behaviour; the slice asked for a pin.
- WAY-03: no test of the range holds a line `decision:` (`grep "decision:" process-audit/test_audit_count.py` gives nothing). The changed test `test_a_table_of_costs_that_lacks_a_level_is_treated_as_the_table_of_weights_is` holds the WAY-344 sentence on the table of the costs of an occurrence, and the two new tests hold its sentences for *Weights* and for the entry `repository`; named here as the executor named them. No invariant test changed.
- Slice's change files: only `process-audit/audit_count.py` and `process-audit/test_audit_count.py`; no screenshot, no foundation file, no reserved choice (the Python standard library, as the invariants `script-language`, `script-imports`, `script-subprocesses` ask).

## Declined to judge

- The failure of `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` in the full file: expected red until Slice 7 (the orchestrator's note), outside this slice.
- The wording of the WAY-344 sentence itself and the `foundation_check.py` reading of `decision:` lines: owned by the foundation step and the other task.

## Checks I ran

All in detached worktrees of the commits under `.runs/review-5/` (removed, see below); the reviewed worktree was not changed.

1. Head, `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k RegisterCount -k Locations`: `Ran 46 tests`, `OK`, exit 0.
2. Base `aaed860` code with the head's `test_audit_count.py` copied in, same command: `FAILED (failures=6)`, exit 1 — the six subtests of the two register tests (missing, doubled, both, for each table); the new `Locations` test passed. So the changed tests are red on the base for the reason named.
3. Head, `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`: `Ran 184 tests`, `FAILED (failures=1)`, exit 1; the one failure is `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share`, the expected one. No other test fails.
4. Head, `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: `Ran 3 tests`, `OK`, exit 0.
5. Reading of the diff, the callers (`read_register`, `named_rows`, `check_weight`, `check_cost_level`, `the_way_checkout`, `repositories`, `main`, `Ancestry`) and the WAY-344 entry, as above. No run of the whole gate (WAY-160).

Not run: nothing the dispatch asked for.

## Reaches beyond the dispatch

- `process-audit/audit_count.py` around `named_rows`, `check_weight`, `check_cost_level`, `Register.refuse`, `the_way_checkout`, `repositories`, `main`, `Ancestry`, and the module description's exit-code paragraph: to verify that the new check refuses exactly what the old comparison refused and that the entry `repository` needs no code.
- `process-audit/test_audit_count.py` `places` helper (line ~174): to see that the new test's locations file holds no `repository` under `the-way`.
- `grep "decision:"` in `process-audit/test_audit_count.py`: WAY-03.
- `task.md` read whole (the handoff names its passages; the rest read for context).

## Working copies

`.runs/review-5/head` (worktree of `61894c2`) and `.runs/review-5/base` (worktree of `aaed860`, with the head's test file copied in), and the output file `.runs/review-5/full.txt`. All removed with `git worktree remove --force`, then `git worktree prune`; the directory `.runs/review-5/` is removed. No remainder.

## Unread material

Read whole: the handoff, the method, the executor's report, `task.md`, WAY-344 at `foundations/decisions.md:2741-2901`. Not read at all, as not needed by a slice with no change of a foundation file: WAY-330 at `decisions.md:7357-7390`, the invariants `script-language`, `script-imports`, `script-subprocesses`, the part-map entry `process-audit`, and the glossary entry *cost of an occurrence*; the change adds no import, no subprocess and no word of a glossary entry, and its Python and standard-library use is plain in the diff.

## Searches not found or unclear

- none
