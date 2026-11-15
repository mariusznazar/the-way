PASS b8b1ce1bb785d26e7f1bbb725f2eceb1aac11fdf

# Review of correction 1 for the human's remarks

Range `1e45b6e..b8b1ce1` (`git rev-parse HEAD` is `b8b1ce1bb785d26e7f1bbb725f2eceb1aac11fdf`; one
commit, six files). Method: `task-cycle/review/SKILL.md` and `fix.md`, the remarks of
`reports/correction-1-remarks.md` in place of a findings file. Read: the remarks, the handoff, the
correction report, the whole diff, WAY-225 and WAY-51 around the changed lines. My earlier
selection stands.

No new Critical or Important finding. Three Minor notes (none blocks; the request's list takes them).

## Each remark

- **Remark 1, first (the term in the rule on a dependency the map does not allow) — made.** WAY-225
  (`foundations/decisions.md:2487-2506`): the binding sentence, the *complies* and *violates*
  examples and the *Rejected* of WAY-51 (`:1739-1742`) now say "dependency of a part" / "allowed
  dependencies of a part"; I compared each rewritten sentence with its old text, word by word. The
  meaning is as before: a dependency of a part that the code holds and the map does not allow is
  recorded as an invariant the product does not meet (WAY-51), never by rewriting the allowed
  dependencies. Only the order inside one clause moved ("the code holds that the map does not
  allow" → "that the code holds and the part map does not allow"), which changes no meaning. No
  binding sentence beyond the term changed; the WAY-225 *Rationale* and *Rejected* and the rest of
  WAY-51 are untouched. No `decision:` line quotes either entry (`git grep "decision: WAY-225"` and
  `"decision: WAY-51"` find nothing), and `foundation_check.py` reports `0 errors`.
- **Remark 1, second (the template says one sentence for a part) — made.**
  `elements/part-map/template.md`: part placeholder (line 42), "Surfaces" (134-135) and "The binding
  part" (194-198) now say briefly, in as few sentences as needed. The correction also changed the
  surface placeholder (line 55), "Surfaces" and the surface part of "The binding part", which the
  remark names only for a part. That is within the remark: it asks to bring the template to what the
  map keeps, and the map's surfaces (`installation-command` and others) hold several sentences,
  the same disagreement; the old template was one rule over both kinds. No other file says "one
  sentence" of a part (`git grep -i "one sentence" -- elements/part-map` finds nothing left).
- **Remark 1, third (guard the two reads) — made, both ways the remark allows.**
  - The copy of `GUIDELINES` in `elements/common/migrate_foundation.py` is removed; the script
    inserts its own directory in `sys.path` and imports `GUIDELINES` from `foundation_check.py`
    (`:67-70`). The import resolves: I ran `python -B <worktree>/elements/common/migrate_foundation.py`
    on a product root outside the script's directory, from another working directory, and it ran to
    its normal message (`holds no foundation`, exit 2) with no `ImportError`; I loaded the module
    by path and `GUIDELINES.pattern` is `^guidelines/[^/]+\.md$`, as before.
    `foundation_check.py` imports no `migrate_foundation`, so no cycle. A pinned checkout runs the
    script from `.the-way/elements/common/` beside `foundation_check.py`: the `installation` suite,
    which runs it from a pinned `.the-way`, passes. `cross-part-imports` allows it (same part,
    `elements-common`), and `elements/part-map` passes (39 tests).
  - `gate-runner-path` is widened and renamed `audit-series-script-paths`
    (`foundations/invariants.md:398-406`): one rule, "each path of a script whose history
    `audit_count.py` reads … is a file git tracks", over the three paths `MEASURES_SCRIPT`,
    `GATE_SCRIPT`, `GATE_TEST_RUNNER`. `Method: test`, `Derives from: WAY-339`, `Part: process-audit ·
    task-cycle · gate`. WAY-339's *Verification* names it (`decisions.md:7360`). The test
    `process-audit/test_audit_series_scripts.py` cites it with `invariant: audit-series-script-paths`.
    `git grep -n "gate-runner-path\|test_gate_runner_path\|GateRunnerPath"` outside `.runs` finds
    nothing (exit 1). The old test file is deleted in the same commit.
- **Remark 2 (let through) — nothing to do; nothing done.**

## The test of the widened invariant fails on each side alone

Run in a worktree of the head under my directory, `python -B -m unittest
process-audit/test_audit_series_scripts.py`, each break reset afterwards. Unbroken: exit 0.

| Side | Break | Exit |
|---|---|---|
| reading | `MEASURES_SCRIPT = "task-cycle/cycle_measure.py"` in `audit_count.py` | 1 |
| reading | `GATE_SCRIPT = "task-cycle/gate_time.py"` | 1 |
| reading | `GATE_TEST_RUNNER = "gate/run_test.py"` | 1 |
| reading | `GATE_SCRIPTS` gains `MEASURES_SCRIPT` | 1 (the second test, the list of the gate series) |
| writing | `git mv task-cycle/cycle_measures.py …` | 1 |
| writing | `git mv task-cycle/gate_times.py …` | 1 |
| writing | `git mv gate/run_tests.py …` | 1 |

Each fails on the named test, not on an import error. The test reads the real constants and the real
tracked files; the oracle test (`gate/no_such_runner.py` is no file) stops a listing that names
everything.

## Nothing else changed; trust boundary

`git diff --stat 1e45b6e..b8b1ce1` lists exactly the six files of the correction. `process-audit/audit_count.py`
is untouched (the new test only reads its constants), and no other trust-boundary file of the map
is in the diff.

## Minor notes (not fixed; to the request's list)

- **m-1.** Two lines of the correction pass 100 columns, which the log's rewrap commits kept:
  `foundations/decisions.md:1740` (102 characters, WAY-51 *Rejected*) and `:7360` (108, the first line
  of WAY-339's *Verification*). No rule of width found for this file; polish only.
- **m-2.** `process-audit/audit_count.py:352-353` `TREE_PATHS` reads one more file path
  (`task-cycle/cycle_stages.py`) to start a series, unguarded by the new test. Outside the remarks
  (they name two paths) and outside the diff; a note for a later task.
- **m-3.** The first sentence of the invariant `audit-series-script-paths` calls the script of
  `task-cycle/cycle_measures.py` "the script that counts the measures of a cycle", while WAY-339
  speaks of the measures of context and cache use. It is the script both texts mean; the wording is
  looser than the decision's. Minor, within the sentence the change writes.

## Checks I ran (command, exit code)

- `git rev-parse HEAD` → `b8b1ce1…`; `git diff --stat 1e45b6e..HEAD`, six files.
- `python -B elements/common/foundation_check.py` (worktree of the head) → exit 0, `0 errors`.
- The seven breaks above → exit 1 each; unbroken → exit 0.
- `python -B elements/common/migrate_foundation.py <product root outside the script's directory>`
  → exit 2 with its `holds no foundation` message, no import error (the correct answer for an empty
  foundation); the module loaded by path → exit 0.
- `python -B -m unittest elements/common/test_migrate_foundation.py` → exit 0 (19 tests).
- `python -B gate/run_tests.py elements/common` (235 tests), `elements/part-map` (39), `process-audit`
  (185), `installation` (60) → exit 0 each. The whole gate not run.
- `git grep` for `gate-runner-path`, `test_gate_runner_path`, `GateRunnerPath` outside `.runs` → exit 1
  (none).

## Unread material

none beyond my earlier selection (counts of the whole-change report stand). The rest of
`foundations/decisions.md` beyond WAY-225, WAY-51, WAY-339 unread for this review.

## Searches not found or unclear

none.

## Working copies

`.runs/review-correction-1/` held a detached worktree of `b8b1ce1` (`wt`), a directory `prod` I made as
a product root for the migration run, and run outputs; all removed (`git worktree remove --force`,
`git worktree prune`, the directory deleted). One slip, said here: my first migration run, with `prod`
inside the task worktree, wrote its default report `.runs/foundation_migration.md` in the task
worktree's ignored `.runs/`; I deleted that file at once, and `git status` of the worktree is clean.
