PASS 264703fd074620f18a2b044a7f84761aef337998

# Review of the whole change — gate-parallel-directories

Range `f749cfc`..`264703f` (three commits `a6807f1`, `9bea9a1`, `264703f`), one author, no plan, no spec. `git rev-parse HEAD`
printed `264703fd074620f18a2b044a7f84761aef337998`, the head given. The reviewed worktree was left unchanged (`git status
--short` empty after my runs).

Blocking findings: 0. Minor findings within the task: 5. Out-of-scope findings: 1.

## Findings

### Critical

none

### Important

none

### Minor, within the task

1. **`gate/run_tests.py:122-132` — an interrupt of a run with `--jobs N` (N below the number of directories) leaves the
   queued directories running.** Leaving the `with ThreadPoolExecutor` block after a `KeyboardInterrupt` calls
   `shutdown(wait=True)` without cancelling the futures not yet started, so the pool goes on to start and finish every
   queued directory, and the interpreter's exit joins the same workers, so a second interrupt does not stop them. The old
   loop stopped at once. By default (no `--jobs`) every directory is already started and receives the interrupt with the
   runner, so the default is not touched. Evidence: scratch run `python -B <scratchpad>\intr.py` in a repository of four
   directories of 3 seconds each, with `concurrent.futures.as_completed` replaced by a function that raises
   `KeyboardInterrupt` after 0.5 s and `run_all(jobs=1)`: it printed `KeyboardInterrupt after 13.2s` — the three queued
   directories ran to the end (about 12 s of work), which for the-way with `--jobs 1` is the remaining part of about 16
   minutes. Matters for a person or a harness that stops a `--jobs 1` gate. The fix is small: catch the interrupt and call
   `pool.shutdown(wait=True, cancel_futures=True)`. Not covered by any test.
2. **`task-cycle/record_template.md:100` — a sentence the change leaves stale.** It says `gate_times.md` is "created by the
   first gate run, at step 2 where the pin moved, else at step 4". In a cycle that skips the run on the base (WAY-367,
   step 4) the first run is the one of step 10. The change edits this file's *Verification* paragraph (lines 135-141) and
   the rest of the files that name the run on the base, but not this line. A reader taking the line literally looks for the
   file after step 4. Within the task: the handoff asks that the files naming the run on the base agree with each other
   and with the decisions. A reader would not be misled about any rule; hence Minor.
3. **`task-cycle/skill/SKILL.md:138-141` (step 4) — `<task-slug>` in `docs/task-cycles/<task-slug>/cycle.md` reads as this
   cycle's name.** Step 5, two paragraphs below, fixes `<task-slug>` as the name step 2 gave this task, while the path here
   is the merged branch's copy, whose slug is another. The step also names no way to find the copy (the author's own
   check used `git log --diff-filter=A --name-only <base>^1..<base>^2 -- docs/task-cycles`, which I repeated: it lists
   `45efc2d` and the copy of `close-decision-pending-templates`). The task's item 4 says only "from the record of that
   cycle in git history", so a reader can still do it; Minor. Wording that the path is the merged branch's, and a
   `git log` recipe, would remove the doubt.
4. **`gate/test_run_tests.py` (`timed_module`, the `DirectoriesAtOnce` tests) and `task-cycle/test_gate_times.py`
   (`RunnerOutputTest`) — the rendezvous tests wait at most 30 s for the sibling directory's process to start.** The
   full gate now starts ten directories at once on a machine that may hold other cycles (the task's *Need*); under
   enough load a sibling's start beyond 30 s fails the test with `did not meet the others` — a flaky failure of the kind
   WAY-243 and WAY-68 refuse. The author saw the `gate` directory go from about 20 s to about 40 s under load and no
   failure; the margin is large for a Python start-up, so I rate the risk low. I ran the `gate` directory once on this
   machine under the load of the `task-cycle` run: 35 tests OK in 21.9 s. Minor.
5. **Wrapping left uneven by the edits, polish.** `task-cycle/skill/SKILL.md:52` is one line of about 150 characters after
   the change (its neighbours stand at about 100); `task-cycle/skill/SKILL.md:135-136` and `:394-395`,
   `task-cycle/skill/request_template.md:229-230`, `agent-instructions/README.md:55-60` and the WAY-349 lines of
   `foundations/decisions.md` (~11605-11607) have lines much shorter or longer than their paragraph. No effect on meaning.

### Out of scope (outside the task)

6. **The audit reads the gate times as one series across this change (`process-audit/SKILL.md:57-60`).** The author's
   concern is right: a new series of the gate times begins only at a change of `task-cycle/gate_times.py`, which this
   change leaves untouched (as the task requires). After this change each directory's own `Ran ... in <s>s` is its time
   under the load of the directories beside it, and the time of the whole run falls, so one median of the version before
   and one of the version after hold runs of two kinds: the per-directory medians rise, the run median falls, and the audit
   would compare them. WAY-350's count of "other gate runs" counts runs of the script, not the directories inside one run,
   so it does not separate them. The task did not ask for a change of the audit and its rule is WAY-348/WAY-350; a
   decision for the human (a new series by a marker of the runner's form, or accept the break). Does not block.

## Against the task

- *To do* 1: met. `gate/run_tests.py` starts every directory at once in its own process (`subprocess.run` in
  `ThreadPoolExecutor`); the main thread writes `== <directory>` and the process's whole bytes (output and error output
  joined) when it ends. Final line identical to the old form (checked by the author's `diff` against the base runner and
  by `test_a_run_of_one_directory_in_the_default_form_keeps_the_report_unittest_prints`); the failed list is in the
  order of names, which is also the old order. A report without a line end gets one; an empty one gets none (tests for
  both).
- *To do* 2: met. `--jobs N`, a whole number of at least 1, rejected otherwise with exit code 2 and a message naming the
  option, before any directory runs; 1 runs one after another (log test); default all at once (rendezvous test).
- *To do* 3: met. `--slowest N` passes `durations=N` to `unittest.TextTestRunner`; without it the report is as before
  (test). On a `unittest` without `durations` it gives exit code 2 and a message before anything runs (tested with a
  stand-in runner class; no older Python on the machine — see below).
- *To do* 4 and 5: met in `task-cycle/skill/SKILL.md` step 4. Check in git by the two trees (`<base>^{tree}`,
  `<base>^2^{tree}`; I ran both on the base `f749cfc`: the same tree `d84c444…`, exit 0); no gate on the base when they
  match; the list from the final gate of the merged branch's cycle, red too, from its record in git history, written
  into *Verification* with its commit and file; the fall back to the run on the base as before where the base is no such
  commit or the merged branch holds no copy of a record with the final gate's result; item 5's run of the failing tests
  on the base, its result into *Verification*, for diagnosis only (WAY-243). `record_template.md` *Verification* and
  `request_template.md` (item 4, *Checks*, the reserved-choice row) agree with it; step 2's and step 10's clauses are
  reworded to match.
- "The last copy is the one" (step 4) — the author says it goes slightly past the task. My judgment: it does not change
  what the task says. Item 4 names "the final gate of that cycle", and where a correction repeated the pair of commits
  the last copy is the one that holds the latest final gate; the first copy would hold an earlier gate than the merged
  tree. The task is silent on several copies, and this fills the silence in the direction its words point. Not a
  finding.
- *Questions to settle*: all three answered as the task answers (the cycle skips the gate on that base; the game's
  changes stay out — nothing of the game is touched; the option disables the parallel run, default parallel, the product
  writes the option into its command).
- *Settlements to record*: row 1 is WAY-366 and row 2 is WAY-367, written with *Rejected* holding the task's *Not chosen*
  (WAY-366: "parallel always, no option" and "one after another by default"; WAY-367: "the gate in every cycle as before"
  and "no run at all, failing tests checked only on failure — shown and not chosen, cost not given"). Source fidelity:
  the entries' binding sentences state the rows' words; WAY-367 *Rejected* says "red most of the time because of the
  machine" for the task's "w dwóch trzecich przypadków czerwony z powodu środowiska" (two thirds) — a loosening of the
  number, not of the meaning. `python -B elements/common/foundation_check.py`: `0 errors`.
- WAY-349 changed by one sentence and its *Verification* only (diff checked: the first sentence gains "included in a cycle
  that makes it (WAY-367)", *complies* is reworded, *violates*, *Rationale* and *Rejected* are untouched). That is what
  the task's *Decisions in play* carries. The author marked it `the cycle's` (it is no row; the task's *Decisions in
  play* carries it and the human's "1 a" accepts it): in line with `foundation_step.md` (the mark is for an entry no row
  and no projected entry carries whole, which the request puts before the human). I judge the mark right.
- Nothing added that nobody asked for. The two option names, the form of the buffered report and the numbers 366/367 are
  the author's choices; the names are plain and spelled in full, the numbers follow the log's last (365), and the report's
  form follows the task's item 1 word for word.

## Against the foundation

- WAY-16 (one command): the option is part of the one command; WAY-366 says so and the runner takes the same name and
  argument. WAY-55: runner changes are in `gate/`, rules of when it runs are in `task-cycle/`. WAY-160: the list rests on
  the earlier cycle's final-gate result, and WAY-367 keeps the orchestrator as the one who runs the gate.
  WAY-243/WAY-68: the run of the failing tests on the base is for diagnosis only and says so in step 4, WAY-367 and
  `request_template.md`. WAY-350: counts runs of the script; a directory inside a run is no other run. WAY-338, WAY-159,
  WAY-261: do not collide.
- Invariant `gate-exit-code` (read whole): the exit codes read the same; the new tests cite it
  (`invariant: gate-exit-code`) where they check them; the invariant and its sentence are unchanged; no invariant test
  is changed or removed (tests are added to `gate/test_run_tests.py` only).
- Part map `test-runner-command` (name, argument, exit codes kept): the new option does not break it; a wrong option's
  exit code 2 is the exit code of an error of the call that DIRECTORY already had.
- Reserved choice: none (stdlib `concurrent.futures`, `inspect`, `argparse`; WAY-38 holds).
- Guidelines: of the-way itself none apply (no `guidelines/coding.md`, `git grep` for the heading
  `Size of a function and a file` finds only decisions and skills of the process); the structure findings are therefore Minor
  by WAY-363, and I make none beyond the five above.

## The runner

- Report whole under its `== <directory>` line, no interleaving: the child's stdout and stderr go to one pipe read to its
  end by `subprocess.run`, and the main thread writes block by block. On Windows the child writes `\r\n`; the count and the
  OK test strip and match without an end anchor, as before.
- Final line and exit codes: same code paths as before for the counting and the summary; `gate-exit-code` tests
  (existing, unchanged) pass.
- Options: values `0`, `-1`, `1e2`, empty and `--5` (an option for argparse) give exit code 2 with a message naming the
  option; `1_0`, ` 2`, `+2`, Arabic-Indic `٣` and a 23-digit number are accepted (Python's `int`), none crashes
  (a huge `--jobs` is cut by `min(..., len(directories))`; a huge `--slowest` runs normally). `--jobs 2` with no value:
  argparse's "expected one argument". `--jobs=1 nonexist` exits 2 with `nonexist is not a directory`.
- `--slowest` on an older Python: the check is `inspect.signature` for `durations`; the message and exit code 2 come
  before any run (stand-in test). I could not run it on a real Python before 3.12 (none here) — unverified on a real one.
- Memory and a hung directory: output of every directory is held in memory until it ends (a test run prints kilobytes),
  and a directory that hangs shows nothing until it is killed, where the old runner streamed. Both follow from the
  task's item 1 (whole report after the end) and WAY-366 states the price; the hung process blocked the old run too. A
  full run starts ten processes at once — memory not measured by me (no full run allowed); the task names the 3-4 GB
  peak per gate as its own risk.
- A directory whose output has no line end: tested (`test_a_report_with_no_line_end_at_its_end_does_not_run_into_the_next_line`).
- Hostile input: the runner's only input is its options and the file list of `git ls-files`; commands are lists (no
  shell); the options are validated as above. A tracked directory whose name begins with `-` would be read by the
  child as an option — it was so before the change too.
- `task-cycle/gate_times.py` still reads the new output: `RunnerOutputTest` runs the real runner (`--slowest 1`) through
  the script and compares each row with the time the runner printed in that block, with directory `a` ending after `b`;
  the test passes (`task-cycle` 386 tests OK) and fails on a sequential runner (its test `a` waits 30 s for the file `b`
  makes).
- Tests prove what they claim: I made two mutations of a copy of the runner in the scratchpad and ran
  `DirectoriesAtOnce`: (a) `max_workers=1` — failed `test_by_default_every_directory_runs_at_the_same_time`,
  `test_a_number_of_jobs_limits_the_directories_that_run_at_once` and
  `test_each_report_stands_whole_under_its_own_line_in_the_order_directories_end` (3 failures of 10); (b) the failed list
  in the order of ending instead of the order of names (the one the author did not mutate) — failed
  `test_failed_directories_are_named_in_sorted_order_whatever_the_order_they_ended_in` (1 failure). The author's
  mutations (ignored `--jobs`, order of submission, `--slowest` not passed, no line end added) I did not repeat.

## The structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py f749cfc 264703f` (exit 0): `gate/run_tests.py` 136 to 189 (+53),
`gate/test_run_tests.py` 245 to 503 (+258), `task-cycle/test_gate_times.py` 366 to 414 (+48),
`foundations/decisions.md` 12265 to 12342 (+77), `task-cycle/skill/SKILL.md` 634 to 650 (+16),
`task-cycle/record_template.md` 219 to 223, `task-cycle/skill/request_template.md` 490 to 493,
`agent-instructions/README.md` 97 to 101; total +463. The-way has no rule of size, so no threshold test exists and no
second run in separate worktrees applies. `run_all` grew from about 45 to about 55 lines (the counting of one report now
stands inside the loop over completed directories); no function lost its user; the names (`run_all`, `run_directory`,
`supports_durations`, `whole_number`) stay true. Nothing to report beyond Minor 5.

## Declined to judge

- The run of the game's repository and its pinned version of the process (the task's out of scope): not looked at.
- Running the files of one directory at once (the task's out of scope).
- The unmeasured "less by default" of the README sentence (`agent-instructions/README.md:56-59`): true by construction (the
  directories overlap); it makes no number claim; the real time is the orchestrator's to read from the final gate's
  `gate_times.md`. Not a finding.
- No live output with `--jobs 1`, and nothing shown by a hung directory: the price the task's item 1 sets and WAY-366
  states. Not a finding.
- The 16-minute figure itself ("with `--jobs 1`"): I did not measure it (full run not allowed).

## Checks run

| Command | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD`; `git log --oneline f749cfc..HEAD`; `git diff --stat f749cfc..HEAD` | 0 | head `264703f`, three commits, 8 files, 520 insertions, 57 deletions |
| `git status --short` (before and after my runs) | 0 | empty |
| `python -B gate/run_tests.py gate` | 0 | 35 tests, OK, 21.9 s |
| `python -B gate/run_tests.py task-cycle` | 0 | 386 tests, OK, 45.7 s |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/change_file_sizes.py f749cfc 264703f` | 0 | table above |
| `git rev-parse 'f749cfc^{tree}' 'f749cfc^2^{tree}'` | 0 | the same identifier `d84c44465c727f4067bbb048a7d0bc49a59d5ce6` |
| `git log --diff-filter=A --name-only --format=%h f749cfc^1..f749cfc^2 -- docs/task-cycles` | 0 | `45efc2d`, the copy of `close-decision-pending-templates` (its `cycle.md` *Verification* holds the final gate, exit 0, 1221 tests) |
| `python -B <scratchpad>\intr.py` in the scratch repository `<scratchpad>\r1` (interrupt with `--jobs 1`) | 0 | `KeyboardInterrupt after 13.2s` (Minor 1) |
| `python -B "<runner>" --jobs V a` for V = `1_0`, ` 2`, 23 digits, `٣`, `1e2`, `+2`, `--5`, empty; `--slowest V a` for V = 23 digits, `0`, `-1`, `1_0` (scratch repository `r1`) | not captured (output piped to `tail`); the message `error: argument ...` was seen for the rejected values and a normal `OK` for the accepted | as listed under "The runner" |
| `python -B "<runner>" --jobs=1 nonexist` | 2 | `nonexist is not a directory` |
| `python -B -m unittest gate.test_run_tests.DirectoriesAtOnce` in `<scratchpad>\m1` (mutation `max_workers=1`) | not captured (piped to `grep`); output `FAILED (failures=3)` of 10 tests | the three tests named above fail |
| the same in `<scratchpad>\m2` (mutation: failed list in the order of ending) | not captured (piped to `grep`); output `FAILED (failures=1)` of 10 | the sorted-order test fails |

`<scratchpad>` is `the reviewer's scratchpad directory`
(files `intr.py`, `mut.py`, `gate.out`, `tc.out`, and the directories `r1`, `m1`, `m2`).

Not run: any other directory than `gate` and `task-cycle`, and the full gate (the orchestrator's); the `--slowest` message
on a real Python before 3.12 (none on this machine); a real Ctrl-C at a console (the interrupt was simulated in the
scratch script); memory and time of a full parallel run.

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md`: WAY-07, 63, 68, 159, 261, 338, 365 read whole (WAY-07 for the change in place; WAY-63 for the
  exit codes; WAY-68, 159, 261, 338 for a collision with the base run and the list; WAY-365 as the form of an entry); the
  list of titles of every decision whose *Scope* names `gate`, `task-cycle` or `agent-instructions` (143 of them) run
  through to find those. WAY-38 read whole (scripts: stdlib, git, the interpreter).
- `foundations/invariants.md` entries `gate-exit-code`, `ci-checking-commands` and `test-method-citation`; the part-map
  entries `gate`, `task-cycle`, `agent-instructions`, `test-runner-command`; the glossary entry `gate`; the environment
  fact `python-stdlib-modules` by its first lines: to judge the exit codes, the contract with products and the
  citation of the invariant by the new tests.
- `task-cycle/skill/foundation_step.md` lines 1-60: the meaning of the mark `the cycle's` (for the WAY-349 change).
- `task-cycle/skill/reserved_return.md` lines 28-56, `process-audit/SKILL.md` lines 50-72 and 180-190,
  `task-cycle/record_template.md` lines 94-160, `README.md` lines 148-165, `installation/README.md` lines 88-100,
  `task-cycle/skill/request_template.md` lines 20-60 (the lines the author left unread, 31-39, included) and the
  passages listed in the next section: to check what names the run on the base and the gate.
- `git grep` over the tracked files, outside `foundations/decisions.md` and `docs/`, for `on the base`, `base ... gate`,
  `failing on`, `starting state`, `gate_times`, `run_tests`, `one after another`: found `record_template.md:100`
  (Minor 2) and no other file that names the run on the base without being changed or judged.

## Unread material

Decisions of my selection: 16 read whole (WAY-07, 16, 38, 55, 63, 68, 159, 160, 243, 261, 338, 349, 350, 365, and the
change's own 366 and 367; WAY-07 is outside the scope list below), 128 by title only (the 143 decisions whose *Scope* names
`gate`, `task-cycle` or `agent-instructions`, less the 15 of them read whole). Of those by title, the ones that bear on the change by their subject and that I did not open:
WAY-33 (what the author of a foundation change searches for — the author's search was reported, I did not repeat it), WAY-89
(version of Python — the `.python-version` of 3.14 is the author's report and the `python-version-declared` invariant, I
did not read the entry), WAY-34, WAY-298 (cycle on the-way itself from the current rules), WAY-337, WAY-339, WAY-348 (not
in my title list since its *Scope* is `process-audit`; I read its effect only through `process-audit/SKILL.md:57-60`),
WAY-325/326 (unread material of a report). No decision that bears on the change stayed unread beyond these.

Not read whole: `task-cycle/skill/SKILL.md` (read lines 36-80, 126-160, 350-410 and the diff; the rest by `git grep`
for `base`, `gate_times`, `starting`), `task-cycle/skill/request_template.md` (read lines 20-60, 226-232, 427-433, 462-470,
485 and the diff), `task-cycle/record_template.md` (lines 94-160), `process-audit/SKILL.md` (lines 50-72, 180-190),
`task-cycle/skill/reserved_return.md` (lines 28-56), `gate/test_run_tests.py` and `task-cycle/test_gate_times.py` (the
diffs, not the whole test files), `foundations/invariants.md`, `foundations/glossary.md` and
`foundations/environment_facts.md` (the entries named above only; not every entry — the method asks for the entries of
the touched parts, and the invariants file was not selected whole). Product guidelines: none apply to the-way itself; read none.

## Searches not found or unclear

- A rule of size for the-way (`guidelines/coding.md`, heading `### Size of a function and a file`): not found (the-way
  has no such file); so no threshold test, and the structure judgment rests on the line counts.
- The handoff says to check "any file the author did not search that names the run on the base": the files name it as
  "the base" and "failing on it", not "starting state"; I searched the words `on the base`, `\bbase\b` near `gate|check|fail|run`,
  `failing on`, `already failing`, `starting state`, `gate_times`; the one stale hit is `record_template.md:100`.
- Whether the runner ever read a real Python older than 3.12: no such interpreter on this machine; unverified.
- The task's *Questions to settle* and *Decisions in play* point to notes of the author's private backlog (the author's report on process improvements,
  the author's note of measurements before changes of the process): not available to me; I judged source fidelity against the task's own quotation
  of them.
- Step 4 names no way to find the merged branch's copy of the record and its `<task-slug>` is ambiguous (Minor 3).
