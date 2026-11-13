# Findings of the review of the whole change — to fix

Source: `reports/whole-review-report.md`, `PASS 264703fd074620f18a2b044a7f84761aef337998`, range `f749cfc`..`264703f`. No blocking finding. The five Minor findings within the task, in the reviewer's words, are fixed once (WAY-161); the out-of-scope finding 6 is not fixed.

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
