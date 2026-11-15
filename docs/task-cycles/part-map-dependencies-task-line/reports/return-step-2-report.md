# Report of the return step, repeated after correction 1 — part-map-dependencies-task-line

**Status:** done. **Commit:** `7d9bc5a` (two files). Head was `b8b1ce1`.

## What the step compared

- The entries correction 1 wrote or changed, with the files: WAY-225 (binding sentence, pair of
  examples) and the *Rejected* of WAY-51 against the glossary term and the part-map template; the
  invariant `audit-series-script-paths` and the *Verification* of WAY-339 that names it against
  `process-audit/audit_count.py` (`MEASURES_SCRIPT`, `GATE_SCRIPT`, `GATE_TEST_RUNNER`,
  `GATE_SCRIPTS`), the three scripts git tracks and the test
  `process-audit/test_audit_series_scripts.py`; the part-map template against the map (a part and a
  surface described briefly in as few sentences as needed; the map's `project-level`, `process-audit`
  and `installation-command` entries); the migration script against `foundation_check.py` (one
  source of the guidelines pattern).
- The entries the task names (WAY-225 beyond its term, WAY-51, WAY-11, WAY-44, WAY-95, WAY-107,
  WAY-293, WAY-300, WAY-339) and the search of the foundation for stale names and for the phrase
  "one sentence" about a part or a surface: no use of `gate-runner-path`, `test_gate_runner_path` or
  `blocked-request-line` is left; the only "one sentence" hits that touch the map's entries were
  corrected by the correction; the others speak of invariants, facts, glossary entries and replies.
- The part map of the touched parts (`decisions`, `part-map`, `invariants`, `elements-common`,
  `process-audit`): *Depends on* against the imports (`cross-part-imports` green in the correction's
  run; the migration script imports a file of its own part) and each part's sentence against the
  change. None is made false.

## Found and corrected

One mismatch, in an entry the correction wrote: the invariant `audit-series-script-paths` said "the
script that counts the measures of a cycle", which is looser than WAY-339, whose sentence names
"how a cycle's agents use context and the prompt cache" and "the script that counts them". The
invariant now reads "…to start a new series of the measures of how a cycle's agents use context and
the prompt cache or of the gate times — the script that counts those measures, the script that
records the gate times and the test runner of the gate — is a file git tracks"; the docstring of
its test follows. The test is unchanged in behaviour, so the invariant's meaning and the three
scripts it guards stand.

## Notes of the review of the correction, each answered

- `foundations/decisions.md:1740` and `:7360` past 100 columns: a convention of width, no mismatch
  with an entry; not corrected, as the handoff says. (`:1740` is in the *Rejected* of WAY-51 and
  `:7360` is the *Verification* of WAY-339, both lines the correction wrote.)
- `task-cycle/cycle_stages.py` in `TREE_PATHS` of `audit_count.py`: unguarded; no entry of the
  foundation names it as a script that starts a series, so it is no mismatch; not changed. (A task
  of its own, as the review says.)
- The looser wording of the invariant: a mismatch with WAY-339, corrected as above.

## Written

Environment facts: none. Glossary terms: none; a term used against its entry: none found. Settlements,
choices that bind after the merge, invariants: none new. The invariant `audit-series-script-paths`
stands from correction 1, set by the human's remark.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`): exit 0, `0 errors`.
- `python -B gate/run_tests.py process-audit`: exit 0 (185 tests, the invariant's test among them).
- Not run: the other directories (nothing else changed in this step); the whole gate.

## Unread material

none beyond the earlier reports; `return_step.md` and `foundation_step.md` read whole; the files of
the correction were read and edited in this cycle.

## Searches not found or unclear

none.

## Working copies

`.runs/return-step-2/` held run outputs and the commit message; removed before return.
