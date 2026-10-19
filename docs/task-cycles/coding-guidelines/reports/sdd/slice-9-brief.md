### Slice 9 — Entry points, third batch

- **Goal:** the entry points of `plan-task`, `record-decision`, `record-environment-fact` and
  `record-glossary-term`, in both tools, as the generator produces them.
- **Change:** `.claude/skills/the-way-plan-task/SKILL.md` · `.agents/skills/the-way-plan-task/SKILL.md`
  `.claude/skills/the-way-record-decision/SKILL.md` · `.agents/skills/the-way-record-decision/SKILL.md`
  `.claude/skills/the-way-record-environment-fact/SKILL.md`
  `.agents/skills/the-way-record-environment-fact/SKILL.md`
  `.claude/skills/the-way-record-glossary-term/SKILL.md`
  `.agents/skills/the-way-record-glossary-term/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** as Slice 7, for these eight paths; the generator then prints exactly the 8
  `would change` lines of S10.
- **Depends on:** Slice 6 · Slice 8 (order of the batches only; no shared file)

