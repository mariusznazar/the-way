# Slice 10 report — entry points, last batch

Status: DONE. Python 3.13.16 (`python3`; repository declares 3.14). BASE 66424e1, commit 8901da0 (not pushed).

## Implemented
Ran `python3 -B agent-instructions/skill_entry_points.py --write`. It changed exactly the eight paths of the brief
(record-invariant, refine-task, settle-technology, update-part-map; `.claude/skills` and `.agents/skills`). Each diff is one line:
the sibling list gained `maintain-coding-guidelines` between `maintain-instruction-files` and `maintain-styleguide`. No hand edits.
No TDD (generated files).

## Checks
| Command | Exit | Output |
|---|---|---|
| `skill_entry_points.py --write` | 0 | slice-10-generator.txt (8 x "changed") |
| `git status --short` after write | - | exactly the eight paths, nothing else |
| `skill_entry_points.py` (check) | 0 | prints `entry points are current`, no orphan (slice-10-generator.txt) |
| `gate/run_tests.py agent-instructions` | 0 | 18 tests OK — slice-10-agent-instructions.txt |
| `gate/run_tests.py gate` | 0 | 98 tests OK — slice-10-gate.txt |

All outputs are in `docs/task-cycles/coding-guidelines/reports/sdd/` (`slice-10-*.txt`). No stale-entry-point failure. Failed checks: none. Unchecked: none.

## Weakest point (WAY-164)
Requirement: "every entry point of the-way current" — most likely missed if some project skill (including ones outside slices 7-10, or the new skill's own) still lacks the new name. Check: grep for `` `maintain-coding-guidelines` `` in every `.claude/skills/the-way-*/SKILL.md` and `.agents/skills/the-way-*/SKILL.md`. Result: 34 of 34 files (17 skills x 2 tools) contain it, 0 missing (slice-10-weakest.txt). The generator check agrees.

## Diff (`git diff --numstat 66424e1..HEAD`)
Eight files, 1 added / 1 removed each.

## Sharpness inputs
Parts touched: skill entry points of project skills (generated, `.claude/skills`, `.agents/skills`). Trust-boundary files touched: none. Irreversible operations: none (local commit, not pushed). Foundation files and the read-only invariant tests untouched.

## Questions / concerns / self-review
No open choice met. Diff reviewed: only the sibling-list line differs. Concerns: none. The untracked report files under `.runs/` were not committed.
