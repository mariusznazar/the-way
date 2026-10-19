# Slice 8 report — entry points, second batch

Python: python3 3.13.16 (repository declares 3.14). Base d3f35b6. Commit 90580b4.

## Implemented
Wrote the eight entry points (lead-project, maintain-instruction-files, maintain-styleguide, plan-project, each in `.claude/skills/` and `.agents/skills/`) in process from `produce(discover(ROOT))` of `agent-instructions/skill_entry_points.py`, for exactly those eight paths (script: scratchpad `s8.py`). No `--write`, no hand edits. Each pair is byte-identical and equal to `produce`'s text (asserted). The only change per file: `maintain-coding-guidelines` added to the sibling list. No TDD (generated files).

## Checks
- `python3 -B agent-instructions/skill_entry_points.py` before: exit 0, 24 `would change` lines (`slice-8-before.txt`); after: exit 0, exactly 16 `would change` lines (`slice-8-after.txt`): record-decision, record-environment-fact, record-glossary-term, record-invariant, update-part-map, refine-task, settle-technology, plan-task, both tools each = S9 and S10. None for S7/S8 skills.
- `python3 -B gate/run_tests.py agent-instructions`: exit 1, 18 tests, 1 failure (`slice-8-agent-instructions.txt`): `test_the_tracked_entry_points_are_what_the_generator_produces (test_skill_entry_points.TrackedEntryPoints)`. Expected (S9-S10 files differ).
- `python3 -B gate/run_tests.py gate`: exit 1, 98 tests, 1 failure (`slice-8-gate.txt`): `test_every_skill_reaches_a_session_on_the_way (test_skills_reach_the_way_sessions.SkillsReachTheWaySessions)` - the remaining "none names `maintain-coding-guidelines`" elements are the 8 S9-S10 skills only. Expected.
- Failed unexpectedly / unchecked: none.

## Weakest point (WAY-164)
Requirement: only the eight paths, each exactly as the generator produces it. Likely miss: a file drifting from `produce`, an extra file touched, or CR/EOL changes. Check (manual; in process against `produce(discover(ROOT))`, actor me; `slice-8-weakest.txt`): 16 files still differ from `produce`, 8 changed in git, intersection 0; all 8 changed equal `produce` byte for byte, all contain `maintain-coding-guidelines`, no CR. `git status` clean after commit; commit touches only the eight paths. Met.

## Diff (git diff --numstat d3f35b6..HEAD)
8 files, each 1 added / 1 removed (8 + / 8 -).

## Sharpness inputs
Parts touched: project skill entry points (generated `.claude/skills`, `.agents/skills`). Trust-boundary files: none. Irreversible operations: none. Foundation files and read-only invariant tests untouched.

## Questions/choices, concerns
None. Self-review: one-line sibling-list change per file; no whitespace/EOL change. Extra untracked-by-commit files: only the slice-8-* evidence files in the reports dir (not committed).
