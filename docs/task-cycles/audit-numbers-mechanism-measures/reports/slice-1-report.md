# Report — slice 1 (the measures script, for Claude Code sessions)

**Status:** done

**Commits:** `a030dbf..f0a3829` on `task/audit-numbers-mechanism-measures`
- `f0a3829` Add the measures script of the cycle run for Claude Code sessions

**Files changed** (both new; the slice's files only):
- `task-cycle/cycle_measures.py` — +368
- `task-cycle/test_cycle_measures.py` — +448

**Checks** (run from the worktree root, after the commit unless noted):
1. `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` — exit 0, 30 tests OK.
2. `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` — exit 0.
3. `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` — exit 0.
4. `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` — exit 0.
- Not run: the product gate (`gate/run_tests.py`), by instruction.

**Failing run before the code (test first):** with the script holding only `def main(argv=None) -> int: return 0`, `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` exited 1 (6 failures, 18 errors; the import test passed). That stub stands in for the base, where the file did not exist. The first run with the real script exited 0.

**Own-work check (section 3):** the most likely miss is a wrong figure in the file, so the hand-worked cycle test (orchestrator plus three subagents, every line of the file written as a literal before the run) is the check; it passed on the first real run. Mutation check in a scratchpad copy, with the tests: a `>=` threshold, strict shrink, no minimum with the write, first line not the one of most output, a 200001 limit, synthetic not skipped, wrong middle index, mean without half-up, share without decimal, Codex refusal off, 1-hour field read as zero, id fallback off, bar not replaced, collapse ignored, no sort. Each was caught, after tests were added for the middle index on even counts, the Codex refusal, the id fallback, the bar and control character, and the time order (both orchestrator and subagent). No mutant survives.

**Real-session run (read-only):** `python -B task-cycle/cycle_measures.py` with the current session id from the environment exits 0, prints LF-only text, and reads every needed field in that transcript. Its rewrite count is 0: the raw per-call numbers (read from the transcript with a probe in the scratchpad) show each call reading what the previous one held, so no rewrite is expected.

**Reaches beyond the handoff:**
- Read `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md` whole, as the method names them.
- Read `task-cycle/cycle_stages.py` lines 1–400 and 473–645, 955–1008, and its `cell` helper (822–831); read `task-cycle/test_cycle_stages.py` lines 1–60 and 248–275 for helper shape.
- Read the user's rules `.ai/rules/scripts.md` and `.ai/rules/git.md` before the probe and the commit.
- Ran a read-only probe script (scratchpad) on the current session transcript.

**Unread material:**
- `task-cycle/cycle_stages.py` 400–473 (Codex subagents) and 645–955 (stages and report) — not needed for the Claude Code reading.
- `task-cycle/test_cycle_stages.py` 60–225 and 275 onward — not read.
- The task document and plan were not opened, per the handoff; the passages were taken from the handoff.
- Foundation entries named by the handoff (WAY-344, WAY-328, WAY-38, WAY-347, WAY-351, the four invariants, part-map ranges) were read in the ranges the handoff gives.

**Searches not found or unclear:**
- Whether a nested subagent sits in the same `subagents` folder as its parent or in the parent's own folder: the handoff says "beside it" and `cycle_stages.py` reads one folder only. I read the one folder (as `cycle_stages.py` does); the nested test uses that layout.
- Whether a Codex session can be given to this script: the handoff scopes the script to Claude Code, so a Codex rollout is refused (see choice 1).
- The gate's foundation check (`--skip-test-citations`) was not run; it is not this slice's.

**Choices made** (each with the rejected way and its cost if wrong):
1. A Codex rollout, given by path or id, ends with exit 2 and `Error:`. Rejected: counting it as zero calls. Cost if wrong: slice 2 must relax the refusal.
2. Every non-synthetic assistant line must carry all six needed usage fields, not only the line chosen. Rejected: checking the chosen line only. Cost: a stricter reading than the handoff strictly needs, and a stale line with a missing field stops the run.
3. A response line with no `message.id` counts as a call of its own, keyed by line number. Rejected: exit 2. Cost: a response written over several lines with no id would count more than once; no id appears in real transcripts.
4. A line with no readable timestamp sorts first; calls with the same time keep line order. Rejected: exit 2, since `timestamp` is not among the handoff's needed fields. Cost: order may be wrong for such a line.
5. A usage value that is not a non-negative whole number ends with exit 2 (`not a whole number`). Rejected: accepting it. Cost: a transcript with a float would stop the run; none is known.
6. A call's time is the time of its chosen line (the line with most output tokens), as `cycle_stages.py` does.
7. Sums over no calls are `0`; means and shares with nothing to average are `unknown`.
8. Agent names are cleaned: control characters become spaces, the whitespace collapses, and each bar becomes `/`.
9. Sessions are output in the order of their ids, so the same input gives the same bytes; the script writes bytes so the output has LF line ends on Windows.
10. A subagent's meta file that cannot be read ends with exit 2, as `cycle_stages.py` does. A meta file that is not a JSON object is treated as missing.

**Problems as observed:** none beyond those above. No check failed.
