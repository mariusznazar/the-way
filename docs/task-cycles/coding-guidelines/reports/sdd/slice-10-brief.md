### Slice 10 — Entry points, last batch and the whole inventory

- **Goal:** the entry points of `record-invariant`, `refine-task`, `settle-technology` and
  `update-part-map`, in both tools, as the generator produces them, and every entry point of
  the-way current.
- **Change:** `.claude/skills/the-way-record-invariant/SKILL.md`
  `.agents/skills/the-way-record-invariant/SKILL.md`
  `.claude/skills/the-way-refine-task/SKILL.md` · `.agents/skills/the-way-refine-task/SKILL.md`
  `.claude/skills/the-way-settle-technology/SKILL.md`
  `.agents/skills/the-way-settle-technology/SKILL.md`
  `.claude/skills/the-way-update-part-map/SKILL.md` · `.agents/skills/the-way-update-part-map/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** `python -B agent-instructions/skill_entry_points.py --write`; `git status --short`
  shows only these eight paths changed by it; then `python -B agent-instructions/skill_entry_points.py`
  prints `entry points are current` and no orphan. `python -B gate/run_tests.py agent-instructions`
  and `python -B gate/run_tests.py gate` pass; no stale-entry-point failure is acceptable here.
- **Depends on:** Slices 6, 7, 8 and 9

