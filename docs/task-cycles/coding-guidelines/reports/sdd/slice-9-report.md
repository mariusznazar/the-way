# Slice 9 report — entry points, third batch

Status: DONE. Commit 66424e1 (base 90580b4). Python 3.13.16 (`python3`; repository declares 3.14).

## Implemented
The eight entry points of plan-task, record-decision, record-environment-fact and
record-glossary-term (`.claude/skills/` and `.agents/skills/`) were written in process from the
generator's own `discover` and `produce` (agent-instructions/skill_entry_points.py), for exactly those
eight paths. No `--write`, no hand edit. Each file changed by one line (the sibling list, which now
names `maintain-coding-guidelines`); the pairs of each skill are byte-identical, no CR present. No TDD
(generated files).

## Checks (output files beside this report)
- `python3 -B agent-instructions/skill_entry_points.py` — exit 0; prints exactly the 8 `would change`
  lines of S10 (record-invariant, update-part-map, refine-task, settle-technology, each in .claude and
  .agents), no `create`, no orphan. Output: `slice-9-generator.txt`.
- `python3 -B gate/run_tests.py agent-instructions` — exit 1, 18 tests, 1 failure (expected):
  `test_skill_entry_points.TrackedEntryPoints.test_the_tracked_entry_points_are_what_the_generator_produces`,
  on `.claude/skills/the-way-record-invariant/SKILL.md` (S10). Output: `slice-9-agent-instructions-tests.txt`.
- `python3 -B gate/run_tests.py gate` — exit 1, 98 tests, 1 failure (expected): the test of
  `gate/test_skills_reach_the_way_sessions.py` listing the 4 skills record-invariant, update-part-map,
  refine-task, settle-technology (S10) as lacking `maintain-coding-guidelines`. Output:
  `slice-9-gate-tests.txt`.

## Weakest point (WAY-164)
Requirement: exactly these eight paths change, to exactly what the generator produces, and nothing
beyond (so the generator's remaining output is S10's alone). Check (manual; actor me; method):
`git status --short` before commit showed 8 entries, all SKILL.md among the named paths; `cmp` of each
.claude/.agents pair identical; `grep -c maintain-coding-guidelines` = 1 in each of the 8; the
generator rerun lists only S10's 8 paths and none of S7–S9's. Observed: all as required.

## Diff (`git diff --numstat 90580b4..HEAD`)
1/1 each for: .agents and .claude skills/the-way-{plan-task, record-decision,
record-environment-fact, record-glossary-term}/SKILL.md (8 files, 8 added, 8 removed).

## Sharpness inputs
Parts touched: the project skill entry points (generated files under .claude/skills and .agents/skills)
only; no trust-boundary file; no irreversible operation. Invariant tests and foundation untouched.

## Questions, choices, self-review, concerns
None. No open design choice. Worktree clean after commit; not pushed.
