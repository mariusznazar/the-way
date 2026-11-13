PASS 1e2c028a939c302c4df5c5a8bf8169b01d174551

# Review of the fix of the whole change — range `1923ef446867b1b17a9ef749d9c811b1e2906c06..1e2c028a939c302c4df5c5a8bf8169b01d174551`

Method: `review-change`, the fix variant (`task-cycle/review/fix.md` read whole). `git rev-parse HEAD` is
`1e2c028a939c302c4df5c5a8bf8169b01d174551`, the head given; five commits (`8bb47d5`, `91c5298`, `7380a5d`, `6f4982d`,
`1e2c028`). The worktree, index and branch were not changed (`git status --short` empty). The product's gate was not run.

Counts: blocking 0; new Minor in the fix 3; Minor findings of the findings file that remain 1 (M10, contested).

## Changed files (`git diff --numstat 1923ef4..1e2c028`, added / removed)

| File | + | - |
|---|---|---|
| `foundations/decisions.md` | 32 | 19 |
| `process-audit/SKILL.md` | 4 | 3 |
| `process-audit/audit_count.py` | 70 | 28 |
| `process-audit/price_list.md` | 2 | 1 |
| `process-audit/problem_register.md` | 2 | 2 |
| `process-audit/test_audit_count.py` | 58 | 0 |
| `task-cycle/cycle_measures.py` | 36 | 15 |
| `task-cycle/test_cycle_measures.py` | 102 | 5 |
| `task-cycle/gate_times.py` | 21 | 5 |
| `task-cycle/test_gate_times.py` | 54 | 0 |
| `task-cycle/record_template.md` | 2 | 1 |
| `task-cycle/skill/SKILL.md` | 6 | 4 |

`task-cycle/cycle_stages.py`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and `task-cycle/spec` are untouched since
the base (`git diff --quiet 2292f33 HEAD -- ...` exits 0); no line of the fix diff of `audit_count.py` names `TREE_PATHS`.

## Each finding of the findings file

- **I1 fixed.** `process-audit/SKILL.md:197-200` now reads "The date starts a new series of the cost and of no mechanism measure or
  gate time (WAY-339)", which is what `instrument_series` does and what the rules bullet at lines 50-64 says.
- **I2 fixed, with one Minor beside it (N1).** WAY-344 (`foundations/decisions.md:11346-11356`, the *Verification* complies and
  violates lines, the *Rationale*) now says that a field an earlier form of a file never had is not missing where the file's other
  signs name that form, and that a file of that form gives the values unknown with no `Error:` and no change of the exit code.
  That is what the code does for the older table and for the pair of time lines. `foundation_check.py --skip-test-citations`
  exits 0; *Relations*, *Scope* and *Rejected* are unchanged. The wording is wider than the approved text by design and goes to
  the human's list (WAY-114), as the orchestrator ruled.
- **M1 fixed.** `process-audit/price_list.md:9-10` and `process-audit/problem_register.md:65-66` say "of the cost and of no
  mechanism measure or gate time".
- **M2 fixed.** The module docstring of `process-audit/audit_count.py` has a paragraph on `mechanism_measures.md` and
  `gate_times.md` (earlier form, fields, limits of 500 runs, 50 directories and 200 characters, exit 1), names the sections
  *Mechanism measures*, *Gate runs* and *Measure versions*, and names the three files in the exit-1 sentence. It matches
  `read_measures`, `read_gate` and `main`.
- **M3 fixed.** WAY-350 (`foundations/decisions.md:11593-11601`) says where the registry is kept (the user's own directory outside
  every repository), that it holds an empty file for each run, made at the start and marked ended at the end, and the six-hour
  and one-day limits. That is what `gate_times.py:17-23` and `count_others`/`prepare` do, and no wider: the default path and the
  file names stay in the code, and `--registry` is not mentioned.
- **M4 fixed.** `task-cycle/gate_times.py`: at most 50 blocks are kept (`MAX_DIRECTORIES`), a directory cell is cut at 200
  characters ending in `…` (`cut`, applied after `cell`), the blocks after the fiftieth only count (`not_listed`), and a last row
  says `… <n> more directories not listed` with `—` as seconds. A `Ran` line after a block not listed is not given to the last
  block listed (`Times.line`, `or self.not_listed`). Crafted-input check, my own run: `python -B task-cycle/gate_times.py --output <file> --registry <dir> -- python -c <200,000 blocks followed by a line of 5,000 `x|` pairs>` exits 0 and appends a
  3,214-byte file (it was 12,289,123 bytes on the earlier head), ending in `… 199951 more directories not listed | —`. The audit
  reads that row as the 51st directory and cuts it by its own limit of 50, with its reason, so no cut is read as a time. Tests
  `CapTest` (five) cover the flood, exactly 50, the time after a block not listed, a 5,000-character line and exactly 200.
- **M5 fixed.** `task-cycle/skill/SKILL.md:133-138`: "a separate checkout of the base commit directly under the worktree's ignored
  `.runs/`".
- **M6 fixed.** The sentence in `task-cycle/record_template.md:99-103` is wrapped.
- **M7 fixed.** `GATE_CODE = [0-9]{1,10}` (`audit_count.py:389`); `test_an_exit_code_above_255_is_read_as_written` asserts 3221225786
  is shown as written with no reason, and `-1` is `unknown` with the right reason.
- **M8 fixed, both parts.** (a) `read_gate` records `table_end` and, where a row stands after a line that ends the table outside a
  fence, adds the reason "holds a row after a line that is not a row of the table: the rows after it are not read"; text after the
  table with no row says nothing (two tests). The scan is one pass over the remaining lines. (b) `fill` reads the two optional files
  through `guarded_optional`, each with its own `try`, in the `else` of the `try` of the required files; the test
  `test_a_git_failure_on_the_gate_file_leaves_the_files_that_were_read` makes `cat-file` fail for the gate blob only and asserts
  the gate reason is "git could not read the copy" while the record's remarks stay counted and no reason stands for them.
- **M9 fixed.** `cycle_measures.py` `codex_subagents(home, root, since)`: a rollout last modified more than a second before the
  orchestrator's first call is not read (`since` is None when the orchestrator has no call, so then every rollout is read); every
  other rollout keeps the loud failure; a rollout with an id already found is left out and a `Warning:` line on stderr names its
  file, the exit code staying 0. The tests `CodexSearchTest` cover the old unreadable rollout skipped, a newer unreadable one
  giving exit 2, and the duplicate. The docstring says it.
- **M10 contested by the orchestrator's ruling; I keep the part about the double reason as Minor, and accept the rest.** The two
  sentences of the plan are in the cycle's record, not a product file, so nothing in the repository holds the disagreement. The
  second part, one reason put twice in *Unknown values* for every missing column, is unchanged
  (`audit_count.py` `add_cost`), tested as it is, and not blocking; it goes to the request's list.
- **M11 fixed in the parts the file names.** Lines wrapped in the docstring, `read_time`'s docstring now says a naive time is taken
  as UTC and another offset kept, `assert_error_names` takes no code, a test for the meta file nested too deeply, two blank lines
  before `class CodexTest`, and the cache figures of `Call` are ints (0 for a Codex call) with "unknown" held once in
  `Agent.cache_known` (`cache_sum` and `rewrite_totals` check it before any figure is used; `rewrites` is reached only through
  them). A few lines of 102 to 120 columns remain in `audit_count.py` (see N3).
- **M12 fixed.** `InterleavedTest` pairs rewrites within an agent while an orchestrator and a subagent call in turn, and takes the
  orchestrator's first, middle and last call over two sessions of one tool; both pass on the unchanged logic.

## What the fix itself could have broken

Nothing Critical or Important found. Points checked:

- `Call`'s cache fields are 0 for a Codex call and every consumer is behind `Agent.cache_known`; the 49 tests of the file,
  including the hand-worked Codex and mixed-cycle ones, pass.
- The floor of M9 uses the modification time, so a subagent rollout of this orchestrator, written after its first call, is never
  skipped; two orchestrator sessions each use their own first call. A rollout whose time cannot be read ends the run with
  `Error:` naming it.
- `guarded_optional` sits in the `else` of the required `try`, so `entries` is always defined there; the `except` branch still
  blanks the record and the stages when `ls-tree` or a required file fails, as before.
- The cut row of the gate script cannot be read as a time by the audit (seconds `—`, and it is the 51st row).
- WAY-344 and WAY-350 as edited say nothing wider than the code, except the corner in N1.

## New Minor findings of the fix (block nothing; for the request's list)

N1. `foundations/decisions.md:11349-11351` (WAY-344: "not missing where the file's other signs name that form") against
`process-audit/audit_count.py:1659-1670` (`has_working`, `has_waiting`): for the two time lines the code looks at no other sign. A
`stages.md` with the heading of the newer form and neither time line is read as the earlier form, with exit 0, where the entry's
qualification would call the lines missing. `task-cycle/cycle_stages.py` writes both lines in every file of the newer form
(`cycle_stages.py:904-912`), so only a damaged file reaches this, and the effect is a lost exit-1 signal for that one cycle. Either
the code checks the heading (neither line and the heading is a missing field) or the sentence drops the qualification for this
pair. The wording came from my own fix direction, which is why I grade it by its effect, Minor.

N2. `process-audit/audit_count.py:1568-1573` reads a table's trailing rows after a line that ends it as one reason; a run that
happens to follow a note line in a hand-edited file is still not read. That is what the reason says, so it is a limit, not a defect.

N3. Still over 100 columns after the wrapping: `process-audit/audit_count.py:147` (104, made by the rewrap), `:2716`, `:2744`, `:2780`
(120), `:2830`, `:2929`; `task-cycle/gate_times.py:8`, `:16`, `:20`, `:21`. Polish only.

## Declined to judge

- The findings outside the task (O1 to O6) of the earlier review: not part of this fix.
- Whether the human accepts the wider WAY-344: it goes to the request's list for the human (WAY-114), as ruled.

## Checks run

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `1e2c028a939c302c4df5c5a8bf8169b01d174551` |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` | 0 | 49 tests OK |
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` | 0 | 22 tests OK |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` | 0 | 177 tests OK in 301 s |
| `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 | 1 test OK |
| `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` | 0 | 59 tests OK |
| `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"` | 0 | 2 tests OK |
| `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` | 0 | 39 tests OK |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 0 warn, 3 info |
| `git diff --quiet 2292f33 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 | untouched |
| `git diff 1923ef4..1e2c028 -- process-audit/audit_count.py` searched for `TREE_PATHS` | 0 hits | the assignment is untouched |
| scratch: `gate_times.py` over a 200,000-block flood and a 5,000-pair line (files in the scratchpad) | 0 | 3,214-byte file |

Not run: the product's gate; the new tests against the previous head to see them fail (the fix report states they failed first; I
did not repeat it); mutation runs.

## Reaches beyond the dispatch

None beyond the handoff's files and the fix diff, except `task-cycle/cycle_stages.py:900-915` (read to settle N1) and the commit
that first wrote the time lines (`git log -S`) to see that the time lines and the section came together.

## Unread material

- `reports/whole-change-fix-handoff.md` (the orchestrator's rulings are given in the review handoff, which I read) and the earlier
  review's reports other than my own findings file.
- The bodies of the new tests of `task-cycle/test_cycle_measures.py` (`CodexSearchTest`, `InterleavedTest`) were read by name and by
  the fix report; the 49 tests pass. The tests of `test_gate_times.py` and `test_audit_count.py` of the diff were read whole.
- The foundation entries WAY-344 and WAY-350 were read in the diff and, for WAY-344, with the whole entry from the earlier review;
  no other decision was reopened (the decisions read for the earlier review of the whole change stand).

## Searches not found or unclear

none
