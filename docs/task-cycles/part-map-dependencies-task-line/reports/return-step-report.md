# Report of the return step — part-map-dependencies-task-line

**Status:** done. **Commits:** none (nothing no longer matched). Head stays `1b5aba9`.

## What the step compared

- The entries the change wrote or changed, with the files of the repository: the ten *Depends on*
  of the part map and the two sentences of `project-level` (against `project-level/task_line.md`,
  `backlog_place.md` and WAY-107); the glossary term `dependency of a part` (against every use of
  "dependency" and "dependencies" in the tracked files that speaks of parts, by a search whose
  result I read line by line for the part map, the part-map skill and template, the invariants
  examples and the decision log); the five invariants (`blocked-request-wording`,
  `blocked-request-label`, `gate-runner-path`, `review-tag-pattern`, `guidelines-file-place`)
  against their four test files and the constants and files they read; WAY-107 (sentence,
  *Verification*, *Rationale*, *Rejected*) against `task_line.md` and `backlog_place.md`; the
  *Verification* of WAY-153, WAY-300, WAY-339 and WAY-167 against the invariants that name them.
- The entries the task names: WAY-225 (sentence unchanged, as the task says), WAY-51, WAY-11,
  WAY-44, WAY-95, WAY-293, WAY-300, WAY-339: their sentences still agree with the files; WAY-300 and
  WAY-339 now name their invariant.
- The part map of the touched parts (`decisions`, `part-map`, `glossary`, `invariants`,
  `project-level`, `task-cycle`, `process-audit`, `elements-common`, `agent-instructions`):
  *Depends on* against the imports (the test `cross-part-imports` passes) and each part's sentence
  against what the change put in the part. No sentence is made false: the new test files are
  tests of the part they test and need no new mention in a sentence.
- The task's rows 1–7 and its seven items of *To do*: each stands where the author's report gives.
- The reviews' remarks: the fix review's one new Minor (the width of line 4 of
  `foundations/part_map.md`) is, as the handoff says, not fixed by the cycle; the note on the bare
  word in WAY-225 and WAY-51 stays with the task's "Bez zmiany".

## Found and corrected

Nothing. No entry the change writes or changes disagrees with the code; a search for the stale
identifier `blocked-request-line`, the phrases "three forms" and "invariant of allowed
dependencies" finds no use left (one hit, "three forms" in `elements/environment-facts/template.md`
speaks of the forms of a source and is unrelated).

## Written

- Sources outside the product, as environment facts: none; the change rests on none.
- Glossary terms: none beyond the row's `dependency of a part`, already written in the foundation
  step; a search found no other word used in a meaning that WAY-95 gives an entry. A term used
  against its entry: none found.
- Settlements: rows 1–7 were written in the foundation step (the places in the author's report);
  none missed. Row 1 went to the glossary, rows 2–5 to invariants, row 6 to WAY-107, row 7 to
  `project-level/task_line.md` (a file of a place, no entry).
- A choice that binds after the merge (WAY-36): none beyond the settled ones. That a test of a
  reader and writer pair belongs to the reader's part is WAY-44 applied, so no entry is written.
- Pair of examples and test (WAY-12): none of the decisions the change writes holds a pair beside a
  test holding part of its sentence; WAY-107's pair stays, no test holds its sentence.
- Invariants: none written; the five stand from the foundation step (rows 2–5 and the split of
  the review's fix).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`): exit 0, `0 errors`.
- `python -B agent-instructions/skill_entry_points.py`: exit 0, `entry points are current`.
- `python -B gate/run_tests.py elements/part-map`: exit 0 (39 tests, `cross-part-imports` among
  them).
- Not run: the whole gate (the orchestrator's); the other directories (no file changed in this
  step).

## Unread material

none beyond the earlier reports: `return_step.md`, `foundation_step.md` read whole; the foundation
files I compared were read in the earlier stages of this cycle.

## Searches not found or unclear

none.

## Working copies

`.runs/return-step/` held run outputs only; removed before return.
