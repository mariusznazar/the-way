# Slice 2 report

**Status:** done
**Commit:** 61cc5ab (on task/task-cycle-skills-shape, not pushed)

## Files changed (9, +14 -11)
- agent-instructions/skill_entry_points.py (+3 -2): sentence now "read a file it names under the same root when the step or variant that names it comes, not all of them at the start, never a copy in another checkout or worktree".
- agent-instructions/test_skill_entry_points.py (+2 -1): DECISION_ENTRY holds the same sentence.
- AGENTS.md (+3 -2): "each reads its skill, and each file the skill names when the step that names it comes, from the checkout or worktree the session works in."
- six entry points (critique, define-project, find-foundation-entries; .claude and .agents), 1 line each, written from the generator's own produce(discover(ROOT)) in process for those six paths; no script committed.

## Checks
- Test changed first: `python -B -m unittest discover -s agent-instructions -p test_skill_entry_points.py -k EntryPointText -k Writing` exit 1 (2 failures: the written-out-form test and one other test comparing against the generator's output), after generator change exit 0 (6 tests OK).
- `python -B agent-instructions/skill_entry_points.py`: "would change" for exactly 36 paths, nothing else.
- `python -B gate/run_tests.py gate`: exit 0 (18 tests OK).
- `python -B gate/run_tests.py agent-instructions`: 1 failure, test_the_tracked_entry_points_are_what_the_generator_produces (derived-file-content), on the 36 paths of Slices 3-6: the plan's expected state.
- `python -B instruction-files/check_instructions.py .`: 0 errors, 1 warning (AGENTS.md:21 `_zadania\` dead path, the private-notes folder named in the Backlog section; not from this slice).
- `git diff --check`: empty.
- Python diff: only the sentence and the assertion.

## Own-work check
Requirement most likely missed: the sentence must keep every phrase the gate test requires and the skill's path in backticks. Check: gate run exit 0 (gate/test_skills_reach_the_way_sessions.py unchanged).

## Reaches beyond the dispatch
None. Choices: wording of the sentence is mine (follows WAY-127 as in 40f0fd3); no rejected alternative of note. No plan/code mismatch.
