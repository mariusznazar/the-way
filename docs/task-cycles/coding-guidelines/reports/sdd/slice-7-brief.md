### Slice 7 — Entry points, first batch

- **Goal:** the entry points of `critique`, `define-project`, `find-foundation-entries` and
  `implement-task`, in both tools, hold the sibling list with `maintain-coding-guidelines`, exactly
  as the generator produces them.
- **Change:** `.claude/skills/the-way-critique/SKILL.md` · `.agents/skills/the-way-critique/SKILL.md`
  `.claude/skills/the-way-define-project/SKILL.md` · `.agents/skills/the-way-define-project/SKILL.md`
  `.claude/skills/the-way-find-foundation-entries/SKILL.md`
  `.agents/skills/the-way-find-foundation-entries/SKILL.md`
  `.claude/skills/the-way-implement-task/SKILL.md` · `.agents/skills/the-way-implement-task/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** the eight paths written from `produce(discover(ROOT))` in process, nothing else; each
  pair byte-identical and equal to `produce`. `python -B agent-instructions/skill_entry_points.py`
  prints exactly the 24 `would change` lines of S8–S10. `python -B gate/run_tests.py agent-instructions`
  and `gate` still fail on those 24 — recorded.
- **Depends on:** Slice 6 · Slice 5 (`implement-task`'s skill file is final)

