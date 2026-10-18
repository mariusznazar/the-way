### Task 6 — Entry points, second batch

- **Goal:** the entry points of `maintain-instruction-files`, `plan-project`, `plan-task`,
  `record-decision` and `record-environment-fact`, in both tools, as the generator produces them.
- **Change:** `.claude/skills/the-way-maintain-instruction-files/SKILL.md`
  `.agents/skills/the-way-maintain-instruction-files/SKILL.md`
  `.claude/skills/the-way-plan-project/SKILL.md` · `.agents/skills/the-way-plan-project/SKILL.md`
  `.claude/skills/the-way-plan-task/SKILL.md` · `.agents/skills/the-way-plan-task/SKILL.md`
  `.claude/skills/the-way-record-decision/SKILL.md` · `.agents/skills/the-way-record-decision/SKILL.md`
  `.claude/skills/the-way-record-environment-fact/SKILL.md`
  `.agents/skills/the-way-record-environment-fact/SKILL.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2074`
- **Checks:** as Slice 5, for these ten paths; the generator then prints exactly the 10
  `would change` lines of S7.
- **Depends on:** Slice 4 · Slice 5 (order of the batches only; no shared file)

