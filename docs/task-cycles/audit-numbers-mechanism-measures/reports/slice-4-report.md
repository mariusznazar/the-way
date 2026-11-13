# Report — slice 4 (the instruction and the record template)

Saved by the orchestrator, word for word from the executor's returned report: the executor's instructions forbade it to write a report file, and its handoff asked for one. Corrected only for the escaping of angle brackets.

Status: done. Commit `8a8f636` on `task/audit-numbers-mechanism-measures`, on top of `7916a21` (the slice's range is `7916a21..8a8f636`). All three checks exit 0; none failed or was left unrun. The gate was not run, as instructed.

## Files changed
- `task-cycle/skill/SKILL.md`: 31 added, 13 removed
- `task-cycle/record_template.md`: 3 added, 2 removed
- `task-cycle/skill/blocked_finding.md`: 1 added, 1 removed
- `task-cycle/skill/reserved_return.md`: 2 added, 1 removed

## What changed
- Naming moved ahead of step 4. Step 2 now names `<task-slug>` before any gate run, and step 5 keeps that name. This settles the "step 4 runs before step 5 names the slug" question.
- Gate runs go through `gate_times.py`. Steps 2, 4, 10 and the reruns of steps 9 and 12 all use it. Step 10 holds the full command: `python -B task-cycle/gate_times.py --output .runs/task-cycles/<task-slug>/gate_times.md -- <declared gate command>`, with `python -B gate/run_tests.py` as the-way's own command. The orchestrator still records the command and the gate's exit code, and an `Error: gate_times.py:` exit 2 is marked as the script's own failure.
- Base run path. The base checkout runs the script with `--output ../task-cycles/<task-slug>/gate_times.md`. That reaches the worktree's record directory from a checkout directly under `.runs/`.
- Measures script beside `cycle_stages.py`. Step 12, step 9 sub-step 4, `blocked_finding.md` and `reserved_return.md` each name `task-cycle/cycle_measures.py` with `--output .runs/task-cycles/<task-slug>/mechanism_measures.md`, naming the same sessions.
- Scope sentence. The "writes nothing outside the worktree" sentence gains the `~/.the-way/` gate registry exception.
- Cleaning and record list. The cleaning list in "The record before it is committed" and the record template's file list gain `mechanism_measures.md` and `gate_times.md`, each with the step that creates it.
- No `cycle_stages.py`, `change`, `plan`, `review` or `spec` line changed except by adding the beside-it mention. The skill's description is unchanged, so entry points are not regenerated.

## Checks
1. `python -B instruction-files/check_instructions.py .`: exit 0, `0 error, 0 warn, 3 info`. Same as the base, so no finding on the four files.
2. `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"`: exit 0, 59 tests OK.
3. `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"`, run after the commit: exit 0, 1 test OK.

No test was written first. The slice changes prose only, and the slice names no test for it.

## Own-work check
- Requirement: the base checkout's `--output` path must reach the worktree's record directory.
- Check: resolved by hand, not run. From `<worktree>/.runs/<checkout>/`, `..` is `<worktree>/.runs`, so `../task-cycles/<slug>` is the record directory.
- Result: it holds only if the checkout sits directly under `.runs/`. If it sits deeper, `gate_times.py` creates a stray directory silently.

## Unread material
- In `task.md` and `plan.md`, only the passages the handoff copies were read. The whole files were not opened, as the handoff says.
- `task-cycle/skill/planning.md`, `foundation_step.md` and `return_step.md` were not needed for a slice and were not read.
- Everything else the handoff names was read whole or in the stated range.

## Searches not found or unclear
- The plan's `Read` range for `task-cycle/skill/SKILL.md` lines differs from its current position. The anchors were found by grep.
- The slice's phrase "each with the step that creates it" for `gate_times.md` was unclear. The file is created by the first gate run, which is step 2 where the pin moved and step 4 otherwise. Both are written.
- The base checkout's directory name is not fixed by any instruction. A checkout directly under `.runs/` was assumed.

## Reaches beyond the handoff
- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`: the method and its variant.
- `task-cycle/skill/SKILL.md`, `blocked_finding.md`, `reserved_return.md`, `record_template.md`, `instruction-files/kind_skill.md` and `instruction-files/changing.md`: read whole before editing.
- `foundations/decisions.md` (WAY-148, 160, 308, 309, 347, 348, 349) and the `task-cycle` entry of `foundations/part_map.md`: read in the handoff's ranges.
- The user's rules `git.md`, read before the commit.

## Choices made
- Moved the naming, not a run file. The alternative was to keep step 5's naming and point the base run at a file step 5 names; rejected, because the base run needs the slug before step 5 exists. Cost if wrong: step 2's opening sentence changes order.
- Relative `../` path, not an absolute one. An absolute path would put a private path into the instruction file. Cost if wrong: the `../` path must match the checkout depth.
- Full command given once, in step 10; other steps refer to it. Cost: a change to the command is made in one place.
- Only the four named files changed. The skill's description and entry points are untouched.
