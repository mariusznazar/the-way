# Slice 7 report — entry points, first batch

Python: python3 3.13.16 (repository declares 3.14). Base aaaab9d.

## Implemented
Wrote the eight entry points (critique, define-project, find-foundation-entries, implement-task, each in `.claude/skills/` and `.agents/skills/`) in process from `produce(discover(ROOT))` of `agent-instructions/skill_entry_points.py`, for exactly those eight paths (script in scratchpad: `.../scratchpad/s7.py`). No `--write`, no hand edits. Each pair is byte-identical and equal to `produce`'s text (asserted in the script). The only change per file is one line: `maintain-coding-guidelines` added to the sibling list after `maintain-instruction-files`. No TDD (generated files).

## Checks
- `python3 -B agent-instructions/skill_entry_points.py` before: exit 0, 32 `would change` lines (`slice-7-before.txt`); after: exit 0, exactly 24 `would change` lines (`slice-7-after.txt`), all for lead-project, maintain-instruction-files, maintain-styleguide, plan-project, plan-task, record-decision, record-environment-fact, record-glossary-term, record-invariant, refine-task, settle-technology, update-part-map (both tools each) = S8-S10; none for the four skills of S7.
- `python3 -B gate/run_tests.py agent-instructions`: exit 1, 18 tests, 1 failure (`slice-7-agent-instructions.txt`): `test_the_tracked_entry_points_are_what_the_generator_produces (test_skill_entry_points.TrackedEntryPoints)` - first mismatch `.claude/skills/the-way-record-decision/SKILL.md` (S8-S10 file). Expected.
- `python3 -B gate/run_tests.py gate`: exit 1, 98 tests, 1 failure (`slice-7-gate.txt`): `test_every_skill_reaches_a_session_on_the_way (test_skills_reach_the_way_sessions.SkillsReachTheWaySessions)` - 12 additional elements, all "none names `maintain-coding-guidelines`" for the S8-S10 skills (the 12 listed above), none for S7's. Expected.
- Failed unexpectedly / unchecked: none.

## Weakest point (WAY-164)
Requirement: "only the eight paths, and each exactly as the generator produces it". Most likely miss: an S7 file drifting from `produce` or an extra file touched. Check (manual; method: Python in process against `produce(discover(ROOT))`, actor me): the 24 files still differing from `produce` vs the set changed in git. Observed: 24 differ (all S8-S10), changed set intersects differing set = empty, all 8 changed files contain `maintain-coding-guidelines`, `git status` shows exactly the eight paths. Met.

## Diff (git diff --numstat aaaab9d..HEAD)
Each of the 8 files: 1 added, 1 removed (8 + / 8 -).

## Sharpness inputs
Parts touched: project skill entry points (generated, `.claude/skills`, `.agents/skills`; not in the product-guidelines source). Trust-boundary files: none. Irreversible operations: none. Foundation files and read-only invariant tests untouched.

## Questions/choices, concerns
None. Self-review: diff per file is the single sibling-list line; no whitespace or EOL changes.
