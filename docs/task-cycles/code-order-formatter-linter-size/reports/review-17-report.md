PASS 6c748289faddbbd41893ae99abe17dd0c92c5d68

# Review of slice 17 (review-change), range a30a04ff..6c748289

`git rev-parse HEAD` in the worktree is 6c748289faddbbd41893ae99abe17dd0c92c5d68, the head given.
Two commits: fb43e234 (the slice as planned) and 6c748289 (the orchestrator's widening: the audit's
result text and the docstring of `process-audit/audit_count.py`).

Changed files of the range (added/removed lines): `process-audit/SKILL.md` 2/1,
`process-audit/audit_count.py` 7/4 (docstring only), `process-audit/audit_report.py` 9/4,
`process-audit/test_audit_count.py` 95/64, `process-audit/test_audit_series_scripts.py` 31/15,
`process-audit/version_analysis.py` 4/2 (148 added, 90 removed in all, 6 files).

## Findings

### Blocking (Critical / Important)

None.

### Minor, within the slice

1. `process-audit/audit_report.py:86-87` names the two cost files from the constants `COST_SCRIPT` and
   `COST_MODULE`, while the two other changed sentences of the result (`audit_report.py:150-152` and
   `:323`) write the same two paths as literals. Effect: a later change of `COST_SCRIPTS` moves the
   first sentence and leaves the other two naming the old files; no test reads these sentences (the
   executor says so, and `guidelines/testing.md` gives no test to a text for people, so this is no
   missing test). Evidence: the diff of `audit_report.py`. Grade Minor: the wording is right today,
   and the literals were literals before.

### Minor, out of scope (outside the slice's Change and the Goal's sentence)

2. `process-audit/price_list.md:21` and `process-audit/audit_count.py:62` and `:76` name
   `task-cycle/cycle_stages.py` alone as the script that writes `stages.md` / "folds" the cache writes
   into *Input*. The fold now lives in `task-cycle/stage_transcripts.py:604-615` (`claude_usage`). These
   sentences do not say "the script that measures the cost", so the Goal's sentence is not reached by
   them, and `audit_count.py:62` and `:76` describe what `cycle_stages.py` writes; a reader of
   `price_list.md` would be pointed to the file that no longer holds the fold. Nothing in the slice
   asked for them; named so the orchestrator may decide.

## Judgement of the second commit (6c748289) against the Goal's sentence, WAY-339 and F9

The Goal: "where the report names the script that measures the cost, it names both files". I searched
`cycle_stages` in `process-audit/*.py` and `*.md` and in every `.md` outside `.runs` and `foundations`.
Every place that names the script *as the one that measures the cost / starts the series of the cost*
now names both files: `audit_report.py:86-87` (Process versions), `:150-152` (Measure versions),
`:323` (Cost), `audit_count.py:123-124`, `:196`, `:240-241` (docstring) and `SKILL.md:54-55`. The
remaining single-file mentions (above, Minor 2; `stage_pricing.py`, `record_items.py` comments) name the
file as the writer of `stages.md`. The text agrees with WAY-339 ("`task-cycle/cycle_stages.py` with the
module `task-cycle/stage_transcripts.py` that it imports") and with the invariant
`audit-series-script-paths`, which says the same.

`audit_count.py` code is unchanged: the syntax tree of `audit_count.py` at a30a04ff and at 6c748289 is
the same once the module docstring is dropped (check 9), and `Parser(description=__doc__.split("\n\n")[0])`
takes the first paragraph, which is untouched; so the exit codes, the messages and the verdict for
crafted input at this trust boundary file are the same before and after. The widening changes only the
three sentences of the result text and the docstring.

## Judgement of the changed expected values (WAY-233, WAY-03)

Each expected value that changed in a test, with its cause and the pointer to the evidence:

- `process-audit/test_audit_series_scripts.py`, `test_each_path_the_audit_reads_the_history_of_is_a_file_git_tracks`:
  the tuple now holds `*COST_SCRIPTS` (two files). Cause on the side of the requirement: the script that
  measures the cost spans two files (F9: WAY-339 and the invariant). The comment names the cause,
  WAY-339 and WAY-233, and that the request names the invariant test (WAY-03). Accepted.
- same file, `test_the_paths_are_those_that_start_the_series`: the set now holds
  `"task-cycle/cycle_stages.py"` and `"task-cycle/stage_transcripts.py"` written out, beside the three
  constants as before. The expected value is written out and not taken from `COST_SCRIPTS`, as
  `guidelines/testing.md` ("Test inputs and expected values") asks. Same comment. Accepted. Seen failing
  once with the cause removed (check 6).
- `process-audit/test_audit_count.py`, `test_each_path_that_starts_a_series_is_a_path_git_tracks`:
  `("task-cycle/cycle_stages.py", "task-cycle/stage_transcripts.py")` is written out; comment with the
  cause (WAY-339, WAY-233). Accepted.
- `test_a_git_that_cannot_compare_the_two_versions_counts_as_a_change_of_both_kinds`: the reason string
  now names both files. The slice said "No other expected value changes", so this is a value beyond the
  slice's list; the orchestrator accepted it. My judgement: it is the same cause (when git cannot compare,
  the reason names each path of the list, and the list now holds two files), the comment states it and
  cites WAY-339 and WAY-233, the old value would be red on the right code, and no branch for the test's
  input exists in the code (`audit_count.py` and `version_analysis.py` have none). Accepted as WAY-233
  gives: cause on the side of the requirement, with the evidence stated.
- No assertion was loosened, no test deleted or skipped; the other changes of the test file are import
  changes (names taken from `version_analysis`, `problem_register`, `record_reading`, `stage_pricing`,
  `record_items`) and added cases: the row `task-cycle/stage_transcripts.py` of `BOUNDARIES`, the case
  `{STAGE_MODULE: ...}` of `test_a_cycle_that_changed_the_stage_script_stays_in_its_version_with_no_known_cost`,
  and the new test `test_a_changed_stage_module_gives_the_times_the_cost_and_the_share_unknown_too`
  (values written out; the reason is asserted to name the module and not the script).

For the request (WAY-03): the invariant test `process-audit/test_audit_series_scripts.py`
(`audit-series-script-paths`) is altered (the import, the tuple, the expected set, the docstring); the
tests with a `decision: WAY-339` line that this range alters or adds are
`test_a_changed_stage_module_gives_the_times_the_cost_and_the_share_unknown_too` (added),
`test_a_cycle_that_changed_the_stage_script_stays_in_its_version_with_no_known_cost` (a case added),
`test_a_date_of_the_list_of_classes_starts_a_series_of_the_count_alone`,
`test_a_new_price_list_splits_no_series_of_measures` and
`test_a_new_price_list_starts_a_new_series_of_the_cost_and_of_the_count_of_remarks` (imports only).

**Changed invariant test, named (section 2):** `process-audit/test_audit_series_scripts.py` for
`audit-series-script-paths`.

## Against the foundation and the guidelines

- F9 / WAY-339 / `audit-series-script-paths`: `COST_SCRIPTS = (COST_SCRIPT, COST_MODULE)` is the one
  list; `TOOL_GROUPS` and `cost_boundary` read it (`version_analysis.py:92-99`, `:692`), so a change of
  either file starts a series and marks a cycle that changes only the module as having changed the tool
  (the new test, and check 7). The foundation text and the code agree.
- WAY-233 / WAY-03: above.
- `guidelines/testing.md`: the expected values stay written out; a test of the new behaviour was seen
  failing without it (check 7); the test file stands outside the size rule (`coding.md`, size section).
- `guidelines/coding.md`: formatter and linter exit 0 on the five changed `.py` files; no `noqa`
  switches off a blocking rule that was not there before (the `noqa: E402` imports are the file's
  existing form; `--ignore-noqa` run exits 0).
- `guidelines/coding-shared-module.md`: `version_analysis.py` still defines only constants and
  functions at its top level; the change adds a constant.
- Slice's own text: the files are formatted; no `audit_count.` before a moved name remains in the two
  test files (check 5; only `audit_count.fill`, which did not move, and the file name `audit_count.py`).
  The stale `__all__` of `audit_count.py` is the work of Slice 18 (plan decision 14), not a finding here.
- Reserved choices: none taken. Screenshots: none.
- Code made to pass a test: none found; no branch, value or comparison in `version_analysis.py` or
  `audit_count.py` exists for a test's input.

## Declined to judge

- The size of `process-audit/test_audit_count.py` (about 5700 lines): the size rule covers scripts, not test files.
- The 6-minute run of the directory: a matter of the gate's budget, not of this change.

## Checks run (from the worktree root; `<ruff>` = `the Ruff of the quality environment of the main checkout`)

1. `git rev-parse HEAD` gives 6c748289faddbbd41893ae99abe17dd0c92c5d68; `git log a30a04ff..6c748289` and
   `git diff a30a04ff..6c748289` read whole: exit 0.
2. `<ruff> format --check --config ruff.toml` on `test_audit_count.py`, `test_audit_series_scripts.py`,
   `version_analysis.py`, `audit_count.py`, `audit_report.py`: exit 0 ("5 files already formatted").
3. `<ruff> check --config ruff.toml --ignore-noqa` on the same five files: exit 0.
4. `python -B elements/common/foundation_check.py`: exit 0, `0 errors`, no reworded invariant listed.
5. `grep -n "audit_count\." process-audit/test_audit_count.py process-audit/test_audit_series_scripts.py`:
   only the module docstring lines, the file name, comments and `audit_count.fill` (line 2920).
6. Mutation in a worktree of the head (`COST_SCRIPTS = (COST_SCRIPT,)`):
   `python -B -m unittest discover -s process-audit -p test_audit_series_scripts.py` exit 1 (the second
   test names `'task-cycle/stage_transcripts.py'` missing from the series); the same command on the
   unmutated head exits 0 (3 tests OK).
7. In the same mutated copy: `python -B -m unittest process-audit.test_audit_count -k each_path_that_starts -k each_file_starts -k cannot_compare -k stage_module`
   exit 1, 4 failures out of 4: the tests of the new behaviour fail without it.
8. `python -B gate/run_tests.py process-audit` (directory run, in the background, waited for): exit 0,
   277 tests OK in 359.2 s; output kept in `reports/review-17-gate-process-audit.txt`.
9. Syntax tree of `process-audit/audit_count.py` at a30a04ff against 6c748289, module docstring dropped
   (a one-off script of mine): identical (`True`).
10. Trust boundary `process-audit/audit_count.py`: by check 9, the code is the same, so the same crafted
    input gives the same verdict, exit code and message; I did not rebuild the executor's crafted
    repositories and did not repeat its before/after run, and I take its claim of three differing lines
    of the result (the three sentences) as consistent with the diff of `audit_report.py`, not as evidence.
    The other trust-boundary files named in the handoff are untouched by the range (the diff names none).
11. Not run: the full gate (the handoff forbids it).

## Reaches beyond the handoff

- `process-audit/price_list.md:15-26` and `task-cycle/stage_transcripts.py:586-616`: to see whether the
  sentences naming `cycle_stages.py` as the writer / folder (Minor 2) name the script that measures the cost.
- `process-audit/audit_count.py:386-450` (the `__all__` and its comment) and `plan.md` lines naming
  `__all__` (grep only): to see whether the stale list is another slice's work (it is: Slice 18).
- `grep -rln cycle_stages --include=*.md` outside `.runs` and `foundations`, and `grep -n cycle_stages foundations/decisions.md`:
  to find the places that name the script outside `process-audit/` (the `task-cycle/skill/` files and the
  guidelines name it as the stage script, not as the series boundary; not read, not in the slice).
- `foundations/part_map.md:100-112`: the part map lists `task-cycle/stage_transcripts.py` among the trust
  boundaries of task-cycle beside the files the handoff lists; the range touches neither.

## Working copies

`.runs/review-17/wt` (a detached worktree of 6c748289, with a one-line mutation) was removed with
`git worktree remove --force` and `git worktree prune`; `.runs/review-17/` (my script `ast_same.py` and the
raw gate output) was removed afterwards; the gate output was kept in `reports/review-17-gate-process-audit.txt`.
No remainder; no background run is left.

## Unread material

none of what the handoff names was left unread: the handoff, `task-cycle/review/SKILL.md`, WAY-339,
WAY-233, WAY-03, `audit-series-script-paths`, `guidelines/testing.md`, `guidelines/coding.md` and
`guidelines/coding-shared-module.md` were read whole; `task.md` lines 32 and 108 read; the executor's
report read whole; the diffs read whole. Read in part: `process-audit/test_audit_count.py` (the diff, not
the 5700-line file whole), `process-audit/audit_count.py` (the changed docstring parts, lines 1-10, 386-450
and the grep for `__doc__`), `process-audit/audit_report.py` (the changed hunks), `process-audit/version_analysis.py`
(lines 50-100 and the grep for the constants). The `F9` entries were read as WAY-339 and the invariant, which the handoff says they are.

## Searches not found or unclear

- None not found. Unclear: whether `price_list.md:21` / `audit_count.py:62,76` ("`cycle_stages.py` folds
  them in") are meant to name the script that measures the cost; read as the writer of `stages.md`,
  hence Minor 2 and out of scope.
