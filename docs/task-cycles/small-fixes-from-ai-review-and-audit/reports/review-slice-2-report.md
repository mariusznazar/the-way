PASS 8359dc257827d7861ae97a8f1e9fbefddc673869

# Review of slice 2 — the times of the gate: the lines of a nested run are no directories

Range: `93d3e0d76faeb272042416ddbcb25dd3a8a3b7f2..8359dc257827d7861ae97a8f1e9fbefddc673869`, one
commit (`8359dc25`), files `task-cycle/gate_times.py` and `task-cycle/test_gate_times.py`.
`git rev-parse HEAD` in the worktree printed the reviewed head at the start and at the end of the
review. Trust boundary: yes (`task-cycle/gate_times.py`); the crafted-output checks are below.

## Blocking findings

None.

## Minor findings

### M1 — The rule the plan gives misreads two directories that each print a nested run, and a nested output cut off before its summary line ahead of one that has it

- **Place:** `task-cycle/gate_times.py:233-248` (`Times.nested`), the cap `taken = min(lines, directories, surplus)`.
- **What is wrong:** each earlier summary line takes up to its own `<m>` lines from the lines
  `== ` since the summary line before it. In a failure message the first nested directory stands
  after text, so a nested run has only `<m> - 1` lines at the start of a line; the cap of `<m>`
  therefore lets a summary line take one line more than its run printed, and the surplus is the only
  limit. Where the segment before a summary line also holds the real line `== <directory>` of the
  enclosing block, and an earlier nested run leaves surplus over, the real line is taken.
- **Evidence (a probe that fed hand-written output to `Times` of the head, run once):**
  - Case A: `other` passes; `gate1` fails with a nested run of `a` (after text) and `b`; `gate2`
    fails with a nested run of `c` (after text) and `d`; each nested summary is
    `2 tests in 2 directories; …`; the run's own summary counts 3 directories. Expected by hand:
    `other 0.002`, `gate1 0.500`, `gate2 0.600`. Got:
    `[['other', '0.002'], ['gate1', '0.001'], ['b', '0.600']]` — `gate2` and `d` are taken as
    nested, `b` is listed as a directory with `gate2`'s time, and `gate1` gets the nested run's
    `Ran` line. This is the very misreading point 8 of the task removes.
  - Case C: one block `gate` with two failing tests; the first prints a nested output cut off before
    its summary line (`p` after text, `q`, `r`), the second a whole nested run (`s` after text, `t`).
    Got `[['gate', '0.001'], ['q', '0.900']]`: the surplus of the cut-off output is charged to the
    second run's segment, `r` and `t` are taken, `q` stays a directory and takes the time of `gate`.
- **Why it matters, and why Minor:** the plan's Goal mandates "each such summary line taking at most
  its own `<m>`", so this is a defect of the planned rule, named as such, not a departure of the code
  from it. In the-way the case cannot arise today: of the test directories only `gate/`
  (`gate/test_run_tests.py`) prints a nested runner output in a failure message (the other test that
  runs the runner, `task-cycle/test_gate_times.py:438`, passes bytes as the message, which unittest
  prints as one `repr` line), so two such blocks never meet in one run; and the rows concerned are of
  failed runs, which WAY-350 does not compare. A product whose gate has two directories that test a
  copy of the runner would get case A. Case C needs a nested output without its summary line (an
  interrupted nested run) beside a whole one. A direction, if the orchestrator wants the rule
  tightened: start a nested run's lines after the last line of its segment that holds `== ` after
  text (the marker of a failure message), rather than capping by `<m>`; that is a change of the
  planned rule.

### M2 — The ceiling of memory for crafted output is four times today's

- **Place:** `task-cycle/gate_times.py:75` (`PIECES_KEPT = 100`), `:165` and `:167` (`Piece.own`,
  `Piece.after`), `:205-209`.
- **What is wrong:** a piece keeps the seconds of its first `Ran` line and of the first `Ran` line
  after a summary line, each as printed, and a line may hold up to `LINE_LIMIT` (1 MiB). Today 50
  blocks keep one such string each (about 50 MiB at worst); now 100 pieces keep two each (about
  200 MiB at worst), and `own` and `after` are separate copies even when they come from the same
  line. The probe measured 20 MB kept for 200 pieces with `Ran` lines of 100 KB each (100 kept × 2 ×
  100 KB).
- **Why Minor:** the memory stays bounded whatever the output holds, as the Goal requires; only the
  bound grew. Cutting the seconds at a length no real time reaches, or keeping one string where both
  fields come from one line, would bring it back; the executor names the same point under its
  weakest point and chose not to cut.

### M3 — A summary line is recognised with Unicode digits

- **Place:** `task-cycle/gate_times.py:82-84`, `SUMMARY` uses `\d`, while `RAN` (`:80`) uses
  `[0-9]`.
- **What is wrong:** in a `str` pattern `\d` matches every decimal digit of Unicode, so a crafted line
  `٣ tests in ٣ directories; every directory passed` (Arabic-Indic three) is a summary line with
  `<m>` = 3. The probe: `== a`, that line, `== b`, then `1 tests in 1 directories; …` gave
  `[ ['b', '0.002'] ]` — `a` was taken as nested. No crash: `int()` reads those digits.
- **Why Minor:** the runner prints only ASCII digits, so only crafted output reaches it, and the
  effect is a wrong row, no failure of the script and no change of its exit code. `[0-9]{1,9}`
  would match what the runner prints and nothing else, as `RAN` does.

## Out of scope

None beyond **Declined to judge**.

## Declined to judge

- A gate killed after a nested run printed its summary line (no summary line of its own): the probe
  gave today's reading (`gate` with the nested `Ran` time, the nested `b` listed). The Goal's first
  rule takes the last summary line of the output as the run's own, so this is the planned reading;
  set aside as the plan's choice, with no defect beyond M1's family that a rule without the run's own
  count could avoid.
- The failure of `python -B gate/run_tests.py agent-instructions` through
  `process-audit/test_process_versions.py`, a file of slice 1: outside this range, handled by the
  orchestrator in a separate commit, as the handoff says.
- Whether the change starts a new series of the gate times (WAY-339): the series follows from the
  changed script by the audit's own reading of versions; recording it is not a work of this slice.

## Against the task, the foundation and the guidelines

- Task point 8 (`task.md:39`) and the Goal: the shape of the Goal is read as it requires — the nested
  `== ` lines open no block, the failing directory takes the first `Ran` line after the last nested
  summary line, and a run with no earlier summary line, or with none, is read as before (the earlier
  tests pass unchanged, `test_block_without_a_ran_line_gives_unknown` and
  `test_first_ran_line_after_its_own_block_counts` among them). Every test the Goal lists is there:
  the hand-written shape, three directories, two nested runs in one block, a block that is not the
  first, a nested output cut off before its summary line, a nested run that passes. The "rows that
  count the blocks not listed" hold: a probe with 52 real directories and a nested run of three gave
  50 rows and `not listed: 2`, the number by hand.
- WAY-390 / `command-runner-passes-exit-code`: the diff touches neither `exit_code`, `main`, `relay`
  nor the `Error:` forms; `PassThroughTest` passes unchanged. WAY-199: an edit of the exemplar that
  keeps its checked rule; no approval needed.
- `gate-times-refuses-impossible-entry`: the registry code is untouched and its two tests pass
  unchanged. No invariant test changed.
- WAY-385 / `function-and-file-size`, `ruff-blocking-rules`, `formatter-layout`: the invariant tests
  pass at the head (checks below); `gate_times.py` has 450 lines, its longest function well under
  110.
- WAY-339 / WAY-350: the form of the record file is unchanged, so the audit's reading of
  `gate_times.md` (`process-audit/record_reading.py`) is untouched.
- `guidelines/coding.md`, "How a script starts and ends": the docstring keeps the run and the exit
  codes; it now states the nested rule and the bound of memory, and agrees with the code (the
  surplus as `count - <m>`, the cap per summary line, the time after the last held summary line,
  the first 100 lines `== ` and the last 100 summary lines with a line `== ` before them).
- `guidelines/testing.md`: inputs and expected values are written out in each test, with the way
  they were worked out in comments; the class docstring names the source (by hand from the written
  output). The flood test reaches `Times.line` and `Times.result` directly to measure memory in the
  process, the lowest level at which the bound can be seen; it asserts the peak and the cap of 50.
  The crafted-number test fails under the mutation `\d+` (a parse of 5000 digits raises), as the
  executor reports.
- Code made for a test (WAY-409): none found; no branch or value in `gate_times.py` names an input
  of the tests.

## The author's own-work check and claims

- The weakest point named (the real runner's shape and bounded memory) fits where the change is
  weakest; the executor's run on a real nested runner matches the Goal. It does not reach M1, which
  needs two blocks with nested runs.
- One claim of the executor's report is inexact: it says
  `test_a_later_ran_line_after_the_nested_summary_does_not_replace_the_first` passes on the base by
  design; on the base script it fails (the base gives `gate` the nested `0.003`, the test expects
  `0.539`). This changes nothing of the slice: the test is right, and it fails for the defect.

## Checks run

All in a worktree of `8359dc25` at
`.runs/review-slice-2/head`.

- `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` at the head → exit 0,
  `Ran 38 tests`, `OK (skipped=1)` (the skip is the signal test on Windows).
- The same command with `task-cycle/gate_times.py` replaced by the base's
  (`git show 93d3e0d7:task-cycle/gate_times.py`), then restored → exit 1, 8 failures and 1 error, all
  in `NestedRunTest` (the error: the flood test calls `Times.result`, which the base lacks); every
  earlier test passed.
- Mutations of the head script, each run with the command above, each restored:
  `PIECES_KEPT = 10**9` → exit 1, the flood test fails; `deque()` without `maxlen` → exit 1, the
  flood test fails; the cap by `<m>` removed (`min(lines, surplus)`) → exit 1,
  `test_the_lines_taken_are_those_before_a_summary_line_and_no_more_than_it_counts` fails; the
  condition `self.latest[1] > 0` removed → exit 0, no test fails (it only changes which summary
  lines a flood evicts, no required behaviour; not a finding).
- `python -B -m unittest discover -s agent-instructions -p "test_linter_invariant.py"` → exit 0,
  `Ran 5 tests`, OK (`ruff-blocking-rules`, `formatter-layout`).
- `python -B -m unittest discover -s agent-instructions -p "test_size_invariant.py"` → exit 0,
  `Ran 4 tests`, OK (`function-and-file-size`).
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` → exit 0,
  `Ran 3 tests`, OK (`audit-series-script-paths`).
- A probe script (`.runs/review-slice-2/probe.py`, removed) that fed hand-written output line by line
  to `gate_times.Times` of the head and printed `result()` → exit 0; its cases and results are in M1,
  M2, M3 and the paragraph on the rows not listed above.

Not run:
- `python -B gate/run_tests.py process-audit` whole (about nine minutes by the executor's run): no
  file of `process-audit/` imports or runs `task-cycle/gate_times.py` (`git grep gate_times --
  process-audit` names only the record file and the script's path), the form of the record is
  unchanged, and the one test the plan cites it for, `audit-series-script-paths`, was run above.
- `python -B gate/run_tests.py agent-instructions` whole: it fails at this head through slice 1's
  file, as the handoff says; the invariants of this slice's files in that directory (linter,
  formatter, size) were run above. The `script-imports` test was not run; the slice adds only the
  standard-library import `from collections import deque`.

## Reaches beyond the handoff

- `gate/test_run_tests.py` (its assertion lines, by `grep`): to see how the real nested output is
  printed in a failure message (`assertEqual(code, …, output)` with `output = done.stdout +
  done.stderr`), which grounds M1's claim that the first nested line stands after text.
- `git grep run_tests -- "*test_*.py"`: to find which test directories print a nested runner output,
  for M1's grade.
- `git grep gate_times -- process-audit`: to judge whether the process-audit run tells this change
  apart.
- `task-cycle/test_gate_times.py` and `task-cycle/gate_times.py` read whole at the head: the reach of
  the diff.
- `the author's global rule file for scripts` and `.../rules/git.md`: the user's rules, which
  the session's hooks gave before the probe script and the worktree.

## Working copies

- `.runs/review-slice-2/head`, a
  worktree of `8359dc25`: removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-slice-2/probe.py`:
  removed; the directory `.runs/review-slice-2/` removed with it.
- `.runs/review-slice-2-decisions.tmp`,
  a copy of `foundations/decisions.md` at the head made by mistake outside my directory: removed at
  once.
- Nothing remains.

**Unread material:** none. Read whole: `task.md` lines 39, 91-96 and 111-112; `foundations/decisions.md`
8607-8758 (WAY-339), 8759-8795 (WAY-350), 11279-11298 (WAY-390), 9763-9806 (WAY-199), 11143-11190
(WAY-385); `foundations/invariants.md` 441-550 (taking in 441-470, 491-500 and 541-550);
`foundations/part_map.md` 104-116; `guidelines/coding.md`, `guidelines/coding-command-runner.md`,
`guidelines/testing.md`; `gate/run_tests.py`; the executor's report; `task-cycle/review/SKILL.md`.

**Searches not found or unclear:**
- The Goal's "a run with a nested run that passes with every one of today's tests unchanged" can be
  read as one test or as a condition on the slice; the executor wrote a test of a passing test that
  prints a nested run and kept today's tests unchanged, which meets both readings.
- The Goal's "those that stand directly before an earlier summary line" does not say whether only
  the lines since the summary line before count; the executor took that segment. M1 shows where the
  segment and the cap of `<m>` together misread.
