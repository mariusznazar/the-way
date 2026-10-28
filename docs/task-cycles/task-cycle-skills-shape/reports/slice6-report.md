# Slice 6 report

**Status:** done

**Commit:** b898353 (on task/task-cycle-skills-shape; not pushed)

**Files changed** (1 line added, 1 removed each; 8 insertions, 8 deletions):
.claude/skills/ and .agents/skills/ SKILL.md of the-way-review-change, the-way-settle-technology,
the-way-update-part-map, the-way-write-spec. Written by `python -B agent-instructions/skill_entry_points.py --write`; no hand edits.

**Checks**
- `python -B agent-instructions/skill_entry_points.py` before --write: listed exactly these 8 paths, exit 0.
- `... --write`: changed those 8 paths, exit 0.
- `python -B agent-instructions/skill_entry_points.py` after: "entry points are current", exit 0.
- `python -B gate/run_tests.py agent-instructions`: exit 0.
- `python -B gate/run_tests.py gate`: exit 0.
- `git diff --stat df95b4d..HEAD`: names these eight paths alone.
- Not run: whole `gate/run_tests.py` (the orchestrator's).

**Own-work check:** requirement "changes these eight paths and no other"; check was the dry run before --write and the diff stat after; both showed exactly the eight.

**Reaches beyond the dispatch:** none. The foundation entries and the generator source were not opened; the generator's own output and the tests were the evidence.
**Choices / adaptations / mismatches:** none. The plan's Checks match the dispatch (focused directory runs only).
**Problems:** none observed.
