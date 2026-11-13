PASS 9282e6f408fba466b583eaec75118e4f87e8bbf6

# Review of the fix and the gaps of the first report — gate-parallel-directories

`git rev-parse HEAD` printed `9282e6f408fba466b583eaec75118e4f87e8bbf6`, the head given; the fix is one commit,
`264703f`..`9282e6f` (8 files, 115 insertions, 78 deletions). The reviewed worktree is unchanged (`git status --short`
empty after my runs). Read: the handoff, the findings file (`reports/whole-review-findings.md`, whole), the fix report
(`reports/fix-report.md`, whole), `task-cycle/review/fix.md`, the whole diff of the fix.

Blocking findings: 0. New Minor findings in the fix: 2 (both within the task, listed below). Findings of the findings
file that remain: 0. Out-of-scope finding 6 of the first report stands unchanged.

## Part 1 — the five findings of the findings file

1. **Interrupt with `--jobs N` leaves queued directories running: FIXED.** `gate/run_tests.py:124-151` wraps the loop in
   `try` and on `KeyboardInterrupt` calls `pool.shutdown(wait=True, cancel_futures=True)` and re-raises. The same scratch
   run as in my first report (`<scratchpad>\intr.py`, four directories of 3 s, `run_all(jobs=1)`, the interrupt raised
   0.5 s in) now prints `KeyboardInterrupt after 3.2s` (the one running directory finishes, the three queued ones do not
   start); it printed 13.2 s on `264703f`. The new test
   `DirectoriesAtOnce.test_an_interrupt_leaves_the_directories_still_queued_unstarted` fails on the fix without
   `cancel_futures=True` (a copy of the runner in `<scratchpad>\m3` with `pool.shutdown(wait=True)`: the log held
   `start a, end a, start b, end b, start c, end c`, `FAILED (failures=1)`), and passes on the head. I ran it 25 times
   alone and 30 times under 16 busy-loop processes: 55 of 55 passed, so I see no flakiness; a race remains in theory (the
   worker thread could not yet have taken directory `a` when the interrupt comes, and `a` would then be cancelled too and
   its log missing), which I did not observe and rate not worth a finding. The interrupt in the test is simulated by a
   patched `as_completed` (as the fix report says), not a real Ctrl-C; the same limit as my own repro.
2. **`record_template.md:100` stale sentence: FIXED.** It now reads "created by the first gate run: step 2's where the pin
   moved, else step 4's, and step 10's where step 4 skips its run; each later gate run appends to it". True of the cycle
   as step 4 and step 10 now describe it.
3. **Step 4's path and recipe: FIXED.** `task-cycle/skill/SKILL.md:138-143` now names
   `docs/task-cycles/<merged-task-slug>/cycle.md`, says `<merged-task-slug>` is the merged branch's task slug and not this
   cycle's, and gives `git log --diff-filter=A --name-only --format=%h <base>^1..<base>^2 -- docs/task-cycles`. I ran
   that recipe on `f749cfc`: exit 0, it lists `45efc2d` and the files of `close-decision-pending-templates` including
   its `cycle.md`. Word-by-word comparison of the diff (`git diff --word-diff=porcelain`-style on the five text files,
   only added or removed words listed): the only changes of words in the whole fix are in these two places (the
   `gate_times.md` sentence and step 4's path clause); every other changed line is a re-wrap.
4. **Rendezvous margin: FIXED.** `gate/test_run_tests.py`: 30 became 120 (`timed_module` and its docstring);
   `task-cycle/test_gate_times.py`: 1500 polls became 6000 of the same 0.02 s. A passing run is no slower; a runner that
   does not run the directories together now needs 120 s instead of 30 s to fail each such test (cost: a broken runner
   makes the `gate` directory take several minutes to fail — I accept it). `gate` ran in 19.2 s on the head.
5. **Wrapping: FIXED.** The word diff shows no word changed by the re-wraps (`SKILL.md` steps 2, 4 and 10,
   `record_template.md`, `request_template.md` item 4, `README.md` "Check the change", the WAY-349 binding paragraph of
   `decisions.md`). Some short lines remain at the seams of paragraphs the fix did not rewrap (for example
   `SKILL.md:56` "change checks that commit: it holds only the gitlink, at", `record_template.md:103` "directory. At the
   request, copy", `record_template.md:142`); polish only, below the first report's measure.

## Part 1 — the fix's own diff

No new Critical or Important finding. Two new Minor findings, both within the task:

- **M-a. `gate/run_tests.py:124-151` — only an interrupt cancels the queue; an exception of a worker does not.** If
  `run_directory` raises (a failure to start the process, say) `done.result()` raises inside the loop, the
  `with` block's exit waits for every queued directory, and the error shows only after they ended. Scratch run
  (`<scratchpad>\exc.py`: `run_directory` made to raise for `a` and sleep 3 s for the others, `run_all(jobs=1)`):
  `OSError after 9.1s`, the three other directories ran to the end, silently. The old runner raised at once. A rare
  failure (Python cannot start a child), and the same class as the first finding, so Minor. A `finally`/`except
  BaseException` that cancels the queue would cover both cases. Not covered by a test.
- **M-b. `gate/test_run_tests.py` `test_an_interrupt_...`: the test imports the runner with `runpy.run_path` and reaches
  `loaded['concurrent'].futures`, which names the module bound in the runner by `import concurrent.futures`.** A change
  of that import (`from concurrent.futures import ...`) would break the test with a `KeyError`, not with a message about
  the interrupt. Minor, and no effect today.

The check "the tests prove what they claim" for the fix: the new test fails on the runner without the cancellation
(above); the old tests of the runner pass on the head (`gate`: 36 tests OK).

## Part 2 — the gaps of the first report

Read now, whole, on the head `9282e6f`: the decisions WAY-33, WAY-34, WAY-89, WAY-298, WAY-337, WAY-339, WAY-348, WAY-325,
WAY-326; `task-cycle/skill/SKILL.md` (lines 1-653, every line) and `task-cycle/skill/request_template.md` (lines 1-495,
every line); the 21 invariants of the parts `gate`, `task-cycle`, `agent-instructions` and `every` (the part named in an
invariant's *Part* line); the glossary entries `foundation`, `gate`, `part`, `return step`, `slice` (the terms the
change's sentences use; the glossary's other entries I did not read — none of their terms stands in the change's
sentences, see below).

What each changes:

- **WAY-33** (a foundation change's author searches the whole foundation once): the author reported the search; nothing
  in the change contradicts the decision. No change of grade.
- **WAY-34** (a product takes a new process only by moving its pin): consistent with WAY-366's reason for an option
  instead of a forced parallel run; the product that cannot bear the load writes `--jobs 1` and takes the new pin. No
  change.
- **WAY-89** (Python 3.14 declared and exactly that): the `--slowest` check for a Python before 3.12 is code for a
  version no product can have under WAY-89, so it is unreachable in practice, harmless; my first report's "unverified
  on a real Python before 3.12" matters even less. No change; not a finding.
- **WAY-298** (a cycle on the-way fast-forwards the checkout before the base is taken): the base step 4 checks is the
  fast-forwarded target head; the merge-commit test applies to it. Consistent. No change.
- **WAY-337** (the cost of a cycle and its fix rounds): this fix round is one the audit will count by the findings file
  named in the messages; nothing in the change touches it.
- **WAY-339** (when measures stop being comparable): says the gate times start a new series only with a change of the
  script that counts or records them, and none by a change of the cycle's instructions; `gate_times.py` is that script
  and is untouched. This confirms my out-of-scope finding 6 as I wrote it: by the decision the audit puts the gate times
  from before and after this change in one series. The fall of the whole run's time is what the decision wants the audit to
  show; what misleads is the per-directory rows (each directory's time now includes the load of the others). Finding 6
  stays out of scope, and the human's question for it stays: a rule or a mark to tell the two forms apart in the audit,
  or accept. No change of grade.
- **WAY-348** (the weekly count reads and compares the gate times, by version, in one series): same as WAY-339; the
  medians of a version that contains this change will be taken over runs of both forms. Same note, same grade.
- **WAY-325 and WAY-326** (what the orchestrator does with a report's unread material, and what the report holds): they
  say what my **Unread material** section must hold; this report's section follows them.
- **`SKILL.md` whole:** nothing outside the changed places names the run on the base or the gate times file in a way that
  disagrees: line 38-39 ("every gate run of the cycle, the first included, writes its times to the record directory of
  that name") is true whether the first is step 2's, step 4's or step 10's; step 9.4 (line 357, "run the gate on the change
  as step 10 gives (at once, since no return step runs)") does not depend on a base run; step 12 (line 477-478, "where
  the final tree differs from the one step 10 checked, run the gate again") agrees with step 4's rule of taking the list
  from the last copy (the last copy holds the last gate). No stale statement found beyond the one the fix repaired.
- **`request_template.md` whole:** item 4, *Checks* and the reserved-choice row agree with step 4 and WAY-367. Kind 14 (an
  incomplete reading by the review of the whole change) reads the **Unread material** of the review and of its fix
  review: the counts and the named gaps of my first report fall under it; with the gaps closed in this report there is
  nothing left to name. No other line names the base run.
- **Invariants:** `gate-exit-code` unchanged and its tests pass; `script-imports` (stdlib only: `concurrent.futures`,
  `inspect`, `argparse`), `script-subprocesses` (the runner starts only git and the interpreter), `cross-part-imports`
  (the new tests run the runner inside the part `gate`; `elements/part-map` passes), `test-method-citation` (the new tests
  cite `gate-exit-code` in comment lines) and `tracked-file-private-paths` (nothing of the fix holds an absolute path)
  all hold. No invariant is changed. The invariants `return-step-record`, `foundation-change-merge-route` and the other
  review-method ones concern the cycle's commits, not the files of this fix.
- **Glossary:** `gate` ("the one command that runs all of a product's tests") agrees with WAY-366's "the one command" and
  the option written into it. The words "starting state" (WAY-349, WAY-367) and "base" (the instruction files) name the
  same commit and have no glossary entry; I judge it as WAY-297 gives: Minor at most, and no sentence is read wrongly
  for lack of it, so I make no finding.

**Does anything I read change a grade or the PASS?** No. The reading adds no Critical or Important finding, and the two
new Minor findings are both in the fix's own diff and block nothing.

## Declined to judge

- The unmeasured "less by default" in `agent-instructions/README.md` and the audit's series (finding 6 of the first
  report): outside this review's bound, unchanged.
- Whether `--jobs 1` behaves exactly as the old runner when a directory prints very much (memory): task item 1 sets it.

## Checks run

| Command | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD`; `git status --short` (before and after) | 0 | `9282e6f408fba466b583eaec75118e4f87e8bbf6`; empty |
| `git log --oneline 264703f..HEAD`; `git diff --stat 264703f..9282e6f` | 0 | one commit, 8 files |
| `git diff 264703f 9282e6f` with `--word-diff` on the five text files, filtered for changed words | 0 | only the `gate_times.md` sentence and step 4's path clause change words |
| `python -B gate/run_tests.py gate` | 0 | 36 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 386 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B -m unittest discover -s gate -p "test_*.py"` | 0 | 36 tests OK (the check that does not rest on the runner) |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B -m unittest gate.test_run_tests.DirectoriesAtOnce.test_an_interrupt_leaves_the_directories_still_queued_unstarted` 25 times | 0 each | all passed |
| the same 30 times under 16 busy-loop processes | 0 each | all passed |
| the same test in `<scratchpad>\m3` (copy with `pool.shutdown(wait=True)`, no `cancel_futures`) | 1 | `FAILED (failures=1)`: the log held all six lines |
| `python -B <scratchpad>\intr.py` in `<scratchpad>\r1` (on the head) | 0 | `KeyboardInterrupt after 3.2s` (13.2 s on `264703f`) |
| `python -B <scratchpad>\exc.py` in `<scratchpad>\r1` (on the head) | 0 | `OSError after 9.1s` (M-a) |
| `git log --diff-filter=A --name-only --format=%h f749cfc^1..f749cfc^2 -- docs/task-cycles` (recipe of step 4) | 0 | lists `45efc2d` and the files of the earlier cycle |

One run of `intr.py` with my working directory in the reviewed worktree (not in the scratch repository) ran the first
directory of the-way for 7.2 s under the interrupt and left the worktree clean (`git status --short` empty afterwards); I
repeated it in the scratch repository for the figure above. `<scratchpad>` is
`the reviewer's scratchpad directory`.

Not run: the full gate; a real Ctrl-C at a console; any directory beyond those named.

## Reaches beyond the dispatch

- `task-cycle/test_gate_times.py` diff (its one changed line) and the whole `gate/run_tests.py` and diff of
  `gate/test_run_tests.py`: the fix's range holds them.
- `foundations/decisions.md`: the nine decisions of Part 2 and the WAY-349 paragraph the fix re-wrapped.

## Unread material

Part 1: none; everything the dispatch names was read whole (handoff, findings file, fix report, `fix.md`, the diff of the
range).

Part 2: the nine decisions named (WAY-33, 34, 89, 298, 337, 339, 348, 325, 326), `task-cycle/skill/SKILL.md` and
`task-cycle/skill/request_template.md` were read whole, as were the 21 invariants of the parts `gate`, `task-cycle`,
`agent-instructions` and `every`. Of the glossary I read the five entries `foundation`, `gate`, `part`, `return step`,
`slice` whole and did not read the other 23 entries (the terms `binding part`, `critical flow`, `debt`, `exemplar`,
`standing check`, `transitional state` and the rest do not stand in the sentences of the change); the first report's
counts stand (16 decisions whole on the first head, plus these nine now, 25 in all; 120 of the 143 decisions whose
*Scope* names `gate`, `task-cycle` or `agent-instructions` by title only — 128 less the eight of the nine now read whose
*Scope* is among them, WAY-348's being `process-audit` alone — and none of those bearing on the change). Still not read whole: `task-cycle/record_template.md`
(read lines 94-160 and the fix's diff), `process-audit/SKILL.md` (lines 50-72 and 180-190), `task-cycle/skill/reserved_return.md`
(lines 28-56), the two test files outside the diffs, and the invariants of other parts.

## Searches not found or unclear

- A way to send a real Ctrl-C to a Python process from this shell: not found, so the interrupt is simulated (the same limit
  as the fix's test).
- The words "starting state" and "base" name one commit and only the first stands in the decisions (WAY-349, WAY-367); no
  glossary entry says so. Not a finding; named for the human's choice.
