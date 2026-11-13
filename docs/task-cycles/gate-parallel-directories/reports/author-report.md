# Author report — gate-parallel-directories

**Status:** done with concerns (the concerns are listed under "Problems and concerns"; none blocks).

## Commits (branch `task/gate-parallel-directories`, base `f749cfc`)

| Commit | What |
|---|---|
| `a6807f1` | `gate/run_tests.py` runs the directories at the same time, with `--jobs` and `--slowest`; its tests; the test that feeds the runner's output to `gate_times.py` |
| `9bea9a1` | `foundations/decisions.md`: WAY-366 and WAY-367 written, WAY-349 changed |
| `264703f` | `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, `task-cycle/skill/request_template.md`, `agent-instructions/README.md` |

## Files changed (added / removed lines, `git diff --stat f749cfc..HEAD`)

| File | added / removed |
|---|---|
| `gate/run_tests.py` | 91 / 38 |
| `gate/test_run_tests.py` | 258 / 0 |
| `task-cycle/test_gate_times.py` | 48 / 0 |
| `foundations/decisions.md` | 82 / 5 (WAY-349 edited in place, WAY-366 and WAY-367 added) |
| `task-cycle/skill/SKILL.md` | 21 / 5 (step 2: one clause; step 4: the rule; step 10: one clause) |
| `task-cycle/record_template.md` | 6 / 2 (*Verification*) |
| `task-cycle/skill/request_template.md` | 7 / 4 (item 4, *Checks*, the reserved-choice row) |
| `agent-instructions/README.md` | 7 / 3 (the paragraph of "Check the change") |

Total of the three commits: 8 files, 520 insertions, 57 deletions. `task-cycle/gate_times.py` is not changed (see the
own-work check and "Problems and concerns").

## What was made

**Runner (`gate/run_tests.py`, items 1 to 3 of the task).**

- Without DIRECTORY the directories run at the same time, each in a process of its own (`subprocess.run` in a
  `ThreadPoolExecutor`); the main thread prints each directory's whole report, `== <directory>` then the bytes the
  process printed (output and error output joined), when its process ends, in the order the directories end. A report
  that does not end with a line end gets one, so the next `== ` line stands on its own line; an empty report gets none.
  The last line counts the tests and names the failed directories in the order of their names, as before.
- Option `--jobs N` (whole number of at least 1): at most N directories at once. Default: all directories at once.
  `--jobs 1` runs them one after another. With DIRECTORY it changes nothing.
- Option `--slowest N` (whole number of at least 1): passes `durations=N` to `unittest.TextTestRunner`; each
  directory's report then holds `Slowest test durations` and the N slowest tests with their time, after the skipped
  tests and before `Ran ...`. In a run of every directory the option goes on to each directory's process. Without it
  the report is as before.
- A wrong value (0, negative, not a whole number, `1.5`) of either option is an error of the call: exit code 2 and a
  message on stderr naming the option, and no directory runs. On a `unittest` whose `TextTestRunner` takes no
  `durations` (Python before 3.12), `--slowest` gives exit code 2 and the message `--slowest needs a unittest that takes
  durations, Python 3.12 or later; this is Python X.Y`, found before anything runs, never a traceback.
  The Python the-way pins is 3.14 (`.python-version`) and WAY-89 makes a product provide exactly that version, so I
  found no lower version a product could use; the message is tested with a `TextTestRunner` that lacks `durations`
  put in its place, not on a real older Python (none on this machine).
- The docstring is brought up to date (usage, parallel by default, the options, the form of the report, the exit codes).

**Foundation step (WAY-33 search, then written through `the-way-record-decision`).**

| Entry | Mark | Meaning in English | Meaning in Polish |
|---|---|---|---|
| WAY-366 (new) | `row 1` | The test runner runs the directories of tests at the same time by default, prints each directory's report whole when it ends, and an option limits how many run at once (1 runs them one after another), which a product writes into its one gate command. | Skrypt bramki domyślnie uruchamia katalogi testów jednocześnie i wypisuje raport każdego w całości po jego zakończeniu; opcja ogranicza liczbę katalogów naraz (1 to po kolei), a produkt wpisuje ją w swoje jedno polecenie bramki. |
| WAY-367 (new) | `row 2` | A cycle skips the gate on its starting state when that is a merge commit whose tree equals the tree of the merged branch's head, takes the failing tests from that branch's final gate (red too) from its record in git history and records the source; otherwise it runs the gate there; when its final gate fails on a test outside the list it runs the failing tests on the starting state, for diagnosis only. | Cykl pomija bramkę na stanie wyjściowym, gdy jest on commitem scalenia o drzewie identycznym z głową scalonej gałęzi, bierze listę padających testów z końcowej bramki tamtego cyklu (także czerwonej) z jego zapisu w historii gita i zapisuje skąd; w przeciwnym razie uruchamia bramkę; gdy końcowa bramka pada na teście spoza listy, uruchamia padające testy na stanie wyjściowym, tylko do rozpoznania. |
| WAY-349 (changed in place, WAY-07) | `the cycle's` (it is no row: the task's *Decisions in play* carries it and the human's "1 a" accepts it; the orchestrator may re-mark it) | The run on the starting state goes through the script in a cycle that makes it (WAY-367), and *Verification* asks for that run only in such a cycle. | Przebieg na stanie wyjściowym idzie przez skrypt w cyklu, który go robi (WAY-367), a *Verification* wymaga tego przebiegu tylko w takim cyklu. |

WAY-366: *Scope* gate; *Relations* derives from WAY-16 and WAY-55; *Rejected* holds the two ways the row's source keeps.
WAY-367: *Scope* task-cycle; *Relations* derives from WAY-160 and WAY-349; *Rejected* holds the two ways the row's
source keeps. No invariant is written (the rows ask for none). `python -B elements/common/foundation_check.py` gives
`0 errors`.

Search of the whole foundation for what the entries touch (WAY-33): grep of the decision log, invariants, environment
facts and glossary for `starting state`, `on the base`, `already failing`, `checks failing`: only WAY-349 names the run
on the starting state. WAY-16, WAY-55, WAY-160, WAY-243, WAY-350, WAY-63, WAY-38, WAY-89 read and found not colliding
(WAY-350 counts runs by the script: a directory run inside one gate run is no other run). Invariant `gate-exit-code`
reads the same after the change (its tests still pass). The part map needs no change: `test-runner-command` keeps its
name, argument and exit codes, and the new exit code 2 for a wrong option is the existing exit code of an error of the
call. No glossary term is added.

**Instruction files (item 4 and 5 of the task).**

- `task-cycle/skill/SKILL.md` step 4, in its paragraph "Create a task branch ...": the check in git (`git rev-parse
  <base>^{tree}` against `git rev-parse <base>^2^{tree}`, a base with no second parent is no such commit); where it
  holds, no gate on the base, the list of failing tests from the final gate (red too) of the merged branch's cycle,
  found in its copy of the record `docs/task-cycles/<task-slug>/cycle.md` in git history (*Verification*), written
  into this cycle's *Verification* with the commit and file; where it does not hold or the merged branch holds no copy
  of a cycle record with the result of its final gate, the checks run on the base as before; and item 5: where the
  list was taken and the final gate fails on a test outside it, the failing tests run on the base in a checkout as
  already described, the result goes into *Verification*, for diagnosis only (WAY-243). Step 2: "passed on the base"
  became "is not among the checks failing on the base" (the base run may not exist). Step 10: "the run on the base
  where step 4 requires it".
- `task-cycle/record_template.md` *Verification*: where the cycle ran no gate on the base, the list stands there with
  the commit and file it came from, and the run of the failing tests on the base follows with its result; the pin
  clause got the same rewording as step 2.
- `task-cycle/skill/request_template.md`: item 4 ("save one that fails on the base too — by the run on the base or by
  the list step 4 took"), the *Checks* paragraph (the list, its source, the result of the run of the failing tests),
  and the reserved-choice row of the variants table ("the checks failing on the base, from its run or from the list
  step 4 took"). A cycle with no base run (reserved choice) still gets a valid description.
- `agent-instructions/README.md` "Check the change": the directories run at the same time, the form of the report, the
  two options, and the time sentence (see concerns).
- Read and judged to stay true, unchanged: `task-cycle/review/whole_change.md:43` (the run "on the base" there is the
  rule-of-size test in separate worktrees, not the gate), `task-cycle/plan/SKILL.md:177` (same), `task-cycle/skill/reserved_return.md`
  lines 39 to 46 ("the base, whose failing checks step 4 recorded" holds under both forms), `process-audit/SKILL.md`
  lines 50 to 70 (see concerns).

## Checks run (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py gate` before the runner was changed (new tests written first) | the shell piped it into `tail`, so the exit code of the runner was not captured | `FAILED (failures=8)` of 33 tests, each failing at its assertion (unrecognized `--jobs` / `--slowest`, or a run one after another where all at once was asked for); one run took 30 s of a rendezvous that never came |
| `python -B gate/run_tests.py gate` after | 0 | 35 tests, OK |
| `python -B -m unittest discover -s gate -p "test_*.py"` (the check the README gives for a change to the runner, which does not rest on the runner) | 0 | 35 tests, OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 386 tests, OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests, OK (see the failing run below) |
| `python -B gate/run_tests.py elements/common` | 0 | 144 tests, OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests, OK (5 skipped, no FIFO or POSIX links here) |
| `python -B gate/run_tests.py process-audit` | 0 | 180 tests, OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |

Failed and passed again: `python -B gate/run_tests.py elements/part-map` exited 1 once, on
`test_cross_part_imports.TheWay.test_the_way_imports_only_from_allowed_parts`: it could not read two uses of
`sys.executable` in my new tests (`gate/test_run_tests.py:489`, a `-c` code built by `"\n".join`, and
`task-cycle/test_gate_times.py:157`, a second `sys.executable` inside the command after `--`). The cause is verified
(the failure message names both lines and the file's rules say what it reads). I wrote the `-c` code as one string
literal and moved the gate command into its own list joined with `+`; the run after exits 0.

Directories not run, with the reason: `installation`, `project-level`, `relation-model` (no file of theirs changed and
none reads the runner or the files changed); the full run is the orchestrator's (WAY-160) and is not made here.

## Own-work check (section 3 of the method)

Requirement most likely not met: items 1 and 4 of the task, "the final line and the exit codes as before, the report
of each directory as `unittest` prints it". Check: a temporary git repository of four directories (passing; failing;
a skipped test; a process that exits 0 with no report), run with the runner of the base commit and with the new one at
`--jobs 1`, times replaced by `Xs`, the outputs compared with `diff`.

- First run: `diff old.n new1.n` exit 1. It showed one extra blank line under `== d` (the directory that prints
  nothing), a bug of mine (a line end added to an empty report).
- Fix in `gate/run_tests.py` (`if output and not output.endswith(...)`), plus the test
  `test_a_directory_that_prints_nothing_leaves_no_blank_line_under_its_name`. Second run: `diff old.n new1.n` exit 0:
  the whole output, summary line included (`5 tests in 4 directories; failed: b (exit code 1), d (exit code 0 without
  unittest's OK)`), is the same as the old runner's; the exit code of both is 1.
- Default (all at once) compared with the old output as a set of lines: the same lines, the reports in the order the
  directories end.

Mutations I made and the tests that caught them (each reverted, `gate/run_tests.py` restored byte for byte from a copy
before the loop): `--jobs` ignored (workers = number of directories): `test_a_number_of_jobs_limits...` and
`test_one_job_runs...` fail; reports taken in the order of submission instead of the order of ending:
`test_each_report_stands_whole_under_its_own_line_in_the_order_directories_end` fails; `--slowest` not passed on to the
directories' processes: `test_in_a_run_of_every_directory_each_report_holds_its_own_slowest_tests` fails; the line end
not added to a report that lacks it: `test_a_report_with_no_line_end_at_its_end_does_not_run_into_the_next_line` fails.
Not mutated: the failed list's sorting (a test, `test_failed_directories_are_named_in_sorted_order...`, covers it, I did
not run its mutation).

Proof that `gate_times.py` needs no change: `RunnerOutputTest` in `task-cycle/test_gate_times.py` runs the real runner
(`--slowest 1`) through `gate_times.py` in a temporary repository whose directory `a` ends after `b`; the rows come in
the order `b`, `a`, each with the seconds the runner printed in that block (read in the test from the output itself,
not by the script), including the slowest-tests list printed before the `Ran` line. It passes. The script is
unchanged.

## Reaches beyond the dispatch

- Decisions WAY-38, WAY-63, WAY-68 (from its *Scope* line on), WAY-89 (from its *Scope* line on), and the titles of the
  other decisions whose *Scope* names `gate` (WAY-51, 53, 60, 61, 62, 65, 69, 82, 321): found by the search of *Scope*
  the handoff asks for; read the first four; the rest were judged by title not to bear on the gate's times, base run or
  runner.
- `elements/part-map/test_cross_part_imports.py` (head and the parts that read `sys.executable`): needed to fix the
  failure above.
- `task-cycle/skill/reserved_return.md`, `task-cycle/review/whole_change.md`, `task-cycle/plan/SKILL.md`,
  `process-audit/SKILL.md`: to check that the places the handoff named stay true.
- `elements/decisions/skill/read.md`, `decide_entry.md`, `template.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md`, `elements/decisions/examples.md`: the skill `the-way-record-decision` names them.

## Unread material

- `task-cycle/skill/request_template.md`: read whole except lines 31 to 39 (the middle of "Write, check, publish").
- `task-cycle/skill/reserved_return.md`: read lines 28 to 55 only; `task-cycle/review/whole_change.md`: lines 25 to 60;
  `task-cycle/plan/SKILL.md`: lines 170 to 182; `process-audit/SKILL.md`: lines 50 to 70 (all four are outside what I
  changed; read for the one passage each that the handoff or my grep named).
- Decisions WAY-68 and WAY-89: read from their *Scope* line on, not from the heading and the binding sentences.
- Decisions WAY-51, 53, 60, 61, 62, 65, 69, 82, 321: by title only. `foundations/environment_facts.md`: searched with grep,
  not read.
- `elements/decisions/examples.md` names WAY-03; I did not read it (WAY-349 and WAY-365 served as the form).
- Everything else the handoff names I read whole: `agent-instructions/README.md`, the decisions WAY-16, 55, 160, 243,
  349, 350, `foundations/invariants.md`, `foundations/part_map.md`, `foundations/glossary.md`, the four files of the
  runner and `gate_times`, `task-cycle/skill/foundation_step.md`, `task-cycle/change/SKILL.md`, the task, `task-cycle/skill/SKILL.md`,
  `task-cycle/record_template.md`. Product guidelines: none apply.

## Searches not found or unclear

- The handoff says to grep the tracked files (not `.runs/`, not `docs/`) for what else names the run on the base,
  naming `starting state|run on the base|the base alone|checks already failing`. The words of the files are "the
  base" and "failing on it", not "starting state" (only WAY-349 says "starting state"); I searched also for
  `on the base`, `base.*(gate|check|fail)` and `gate_times`, and read each hit.
- The task says "the step 2 mention of the run on the commit that moved the pin" and the handoff "step 2's mention of the
  run on the base": step 2 does not run the gate on the base itself, it sends to step 4 ("record its base and the
  checks failing on it as step 4 gives"); I changed only its clause that reads "passed on the base", which presumed a
  base run. The rule itself stands once, in step 4.
- The task item 4 says the list is taken "z zapisu tamtego cyklu w historii gita" but names no command to find it. I
  named the file (`docs/task-cycles/<task-slug>/cycle.md`) and its section (*Verification*) in step 4 and wrote no
  `git log` recipe. I tried the rule on this very base: `git rev-parse f749cfc^{tree}` and `git rev-parse
  f749cfc^2^{tree}` both print `d84c44465c727f4067bbb048a7d0bc49a59d5ce6` (exit 0), and `git log --diff-filter=A
  --name-only --format=%h f749cfc^1..f749cfc^2 -- docs/task-cycles` finds the copy `45efc2d:docs/task-cycles/
  close-decision-pending-templates/cycle.md`, whose *Verification* holds the final gate (exit 0, 1221 tests), so the
  rule is workable on the-way's own history.
- I did not find in the task a way to run "the failing tests" on the base in general (a product's command for one test
  differs: for the-way it is `python -B gate/run_tests.py <directory>`, which runs a directory, not one test); step 4
  says "run the failing tests on the base" and leaves the command to the product's rules.

## Questions

none.

## Choices made, the way rejected, the cost if wrong

1. **Option names** `--jobs N` and `--slowest N`; no short form. Rejected: `-j` (an undocumented second spelling),
   `--parallel`. Cost if wrong: a rename plus a change of the gate command of any product that wrote the option.
2. **Default number of directories at once: all.** Rejected: the number of processors (hardware-dependent, so one
   gate takes different times on two machines; the handoff chose all). Cost if wrong: ten processes at once on the-way
   (more for a product with more directories) and the memory the task's Need names; a product writes `--jobs`.
3. **Form of the buffered report:** worker threads run `subprocess.run` with `stdout` piped and `stderr` joined; the
   main thread writes `== <directory>` and the whole bytes in the order of ending. Rejected: a temporary file per
   directory (more code, no gain here), streaming each line with a prefix (the task asks for whole reports). Cost: no
   live output while a directory runs, and `--jobs 1` no longer streams as it did (the report appears when the
   directory ends); a hung directory shows nothing until killed.
4. **Failed directories in the final line in the order of their names**, not of ending: the line stays the same whatever
   the order of ending. Rejected: the order of ending. Cost if wrong: none seen.
5. **`--jobs` given with DIRECTORY changes nothing** (no error). Rejected: exit 2. Cost: a product that appends a
   directory to a command with `--jobs` gets no warning; harmless.
6. **`--slowest` checked before anything runs**, by `inspect.signature(unittest.TextTestRunner)` having `durations`;
   no version number compared. Rejected: comparing `sys.version_info` (breaks on a backport or a change of version).
7. **WAY-366 and WAY-367 as two entries** with the numbers 366 and 367 (the log's last was 365). WAY-367 derives from
   WAY-160 and WAY-349, not from WAY-243 (its *Scope* is `product-guidelines`); WAY-243 is named in the binding
   sentence for the run of the failing tests. Rejected: one entry for both rows (two independent questions).
   WAY-366's *Scope* is `gate` alone (the product writes the option into its command, which is no part of the-way).
8. **"The last copy is the one"** in step 4 where the merged branch added the record copy more than once (a correction
   repeats the pair of commits). Rejected: the first copy (it holds an earlier final gate than the merged tree). This
   goes slightly past the task's words; it follows its item 4 ("the final gate of that cycle"), and I note it for the
   review.
9. **The README time sentence**: "The whole run takes about 16 minutes with `--jobs 1`, and less by default." I did
   not run the full gate, so I give no new number; the 16 minutes is the old time, which `--jobs 1` keeps. "Less by
   default" is by construction (directories at once) and unmeasured. Rejected: writing a new number (unmeasured), or
   leaving "about 16 minutes" (false for the default). Cost if wrong: a sentence the orchestrator can replace with the
   time of the final gate's `gate_times.md` row.

## Problems and concerns (observed; causes marked)

- **The audit reads the gate times as one series until `task-cycle/gate_times.py` changes** (`process-audit/SKILL.md`
  lines 57 to 60: a new series of the gate times begins only at a change of that script, which this change leaves
  untouched). After this change each directory's own `Ran ... in <s>s` is its time under the load of the other
  directories, and the total of a run falls; so the medians of the audit will put runs of two kinds in one series.
  This is the audit's rule (WAY-348, WAY-350), outside this task; I made no change. For the orchestrator to put before
  the human or leave as it is.
- A full run of the-way now starts ten processes at once by default; I could not measure the memory or the time here
  (another gate was running at the same time; my focused runs of seven directories at once on this machine took up to
  521 s for `process-audit` alone, against about 16 minutes for the whole old run, which is no measure of the new one).
- The tests of the runner that wait for each other (rendezvous, up to 30 s each) take the `gate` directory from about
  20 s to about 40 s under load; they pass deterministically on a correct runner, and fail on a runner that is
  sequential or ignores `--jobs` (observed with mutations, not guessed).
- The new tests cite `invariant: gate-exit-code` where they check exit codes of a run of every directory; the invariant
  and its sentence are unchanged.
