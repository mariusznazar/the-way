# Fix report — the Minor findings of the review of the whole change

**Status:** done. **Commit:** `9282e6f` (on `264703f`). Files, added / removed lines (8 files, 115 / 78 in all):
`gate/run_tests.py` (the larger part is the indent of the loop body), `gate/test_run_tests.py` 33 net,
`task-cycle/test_gate_times.py` 1 / 1, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`,
`task-cycle/skill/request_template.md`, `agent-instructions/README.md`, `foundations/decisions.md` (re-wrap only).

## Findings

1. **Interrupt with `--jobs N` left the queued directories running: fixed.** In `run_all` the loop is in a `try`; on
   `KeyboardInterrupt` it calls `pool.shutdown(wait=True, cancel_futures=True)` and raises again, so directories not yet
   started never start (the running ones got the interrupt with the runner). Test
   `DirectoriesAtOnce.test_an_interrupt_leaves_the_directories_still_queued_unstarted`: a `-c` script loads the runner with
   `runpy.run_path`, replaces `concurrent.futures.as_completed` by a function that raises `KeyboardInterrupt`, and runs
   `run_all(jobs=1)` in a temporary repository of three directories (0.3 s each); the log of the directories must hold
   `start a`, `end a` and nothing of `b` and `c`. Seen failing first: before the fix the log was `start a, end a, start b,
   end b, start c, end c` (1 test, 1.9 s, `FAILED`); after the fix `OK` in 1.2 s. The `gate` directory went from 35 to 36
   tests and about 1 s longer.
2. **`record_template.md:100`: fixed.** It now reads "created by the first gate run: step 2's where the pin moved, else
   step 4's, and step 10's where step 4 skips its run; each later gate run appends to it".
3. **Step 4's path and recipe: fixed.** The path is `docs/task-cycles/<merged-task-slug>/cycle.md`, with a clause that
   `<merged-task-slug>` is the slug of the merged branch's task and not this cycle's, and the recipe
   `git log --diff-filter=A --name-only --format=%h <base>^1..<base>^2 -- docs/task-cycles` is in the text. No other word
   of the rule changed.
4. **Rendezvous margin: fixed.** The wait is 120 s (was 30 s) in `timed_module` (its docstring too) and 6000 polls of 0.02 s
   (was 1500) in `RunnerOutputTest`; the polling step is the same, so a passing run is no slower, and a test that does not
   meet its sibling still fails with `did not meet the others`.
5. **Wrapping: fixed, no word changed.** Each re-wrap was done by a script that asserts the word list before and after is
   the same, to 100 columns like the neighbours: `SKILL.md` step 2, step 4 (the whole paragraph from "Record the base
   commit") and step 10 (to "Record its"), `record_template.md` (line 100 and *Verification*), `request_template.md` item 4,
   `README.md` "Check the change" paragraph, the WAY-349 binding paragraph in `decisions.md` (binding sentences unchanged
   in wording; the blank line after them kept). I also shortened one comment in `run_tests.py` that the new indent pushed
   over 100 columns.

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py gate` | 0 | 36 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 386 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK (it reads the `sys.executable` uses of the new test; the `-c` script keeps the form it reads) |
| `python -B gate/run_tests.py elements/common` | 0 | 144 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| the new test alone, before the fix | 1 | `FAILED (failures=1)`, run through `python -B -m unittest ...` |

Not run: the full gate (the orchestrator's). The mutation of the fix is the failing run above.

## Reaches beyond the handoff

`task-cycle/change/fix.md` (the variant names it). Nothing else.

## Unread material

none. (`fix-handoff.md`, `whole-review-findings.md` and `fix.md` read whole; the review report `whole-review-report.md` was
not opened, the findings file holds the five findings in the reviewer's words.)

## Searches not found or unclear

- The handoff says the interrupt test must "not wait on long sleeps"; the finding's own repro used 3 s directories. I made
  the interrupt come from a patched `as_completed`, as the reviewer's repro did, and used 0.3 s directories. It does not
  send a real interrupt to a process (not portable on Windows), so it shows that queued directories are cancelled, not that
  Ctrl-C reaches the running ones.
- Finding 5 named the lines of `README.md:55-60` and `decisions.md` ~11605-11607 only roughly; I re-wrapped the whole
  paragraph of each.
