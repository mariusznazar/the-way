### Slice 8 — Entry points, second batch

- **Goal:** the entry points of `lead-project`, `maintain-instruction-files`, `maintain-styleguide`
  and `plan-project`, in both tools, as the generator produces them.
- **Change:** `.claude/skills/the-way-lead-project/SKILL.md` · `.agents/skills/the-way-lead-project/SKILL.md`
  `.claude/skills/the-way-maintain-instruction-files/SKILL.md`
  `.agents/skills/the-way-maintain-instruction-files/SKILL.md`
  `.claude/skills/the-way-maintain-styleguide/SKILL.md`
  `.agents/skills/the-way-maintain-styleguide/SKILL.md`
  `.claude/skills/the-way-plan-project/SKILL.md` · `.agents/skills/the-way-plan-project/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** as Slice 7, for these eight paths; the generator then prints exactly the 16
  `would change` lines of S9 and S10.
- **Depends on:** Slice 6 · Slice 7 (order of the batches only; no shared file)

