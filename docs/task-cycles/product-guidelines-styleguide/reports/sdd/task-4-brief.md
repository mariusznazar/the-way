### Task 4 — The skill `maintain-styleguide` and its entry points

- **Goal:** `product-guidelines/styleguide/SKILL.md` holds the frontmatter of spec §6.1 (one-line,
  safe plain YAML description saying "user interface") and steps 0–5 of §6.3, the split of §6.2,
  the orchestrated mode of §6.4, §6.5 and the instruction-file guidance of §6.6, describing what it
  takes from outside sources without naming them (WAY-27) and restating no rule of the templates
  or element skills; it follows WAY-172–WAY-175 and WAY-182–WAY-192; its two entry points exist
  exactly as the generator produces them; the root `README.md` names `product-guidelines/` and
  the skill directory beside the others.
- **Change:** `product-guidelines/styleguide/SKILL.md`
  `.claude/skills/the-way-maintain-styleguide/SKILL.md`
  `.agents/skills/the-way-maintain-styleguide/SKILL.md` · `README.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:91-91`
  `.runs/task-cycles/product-guidelines-styleguide/reports/research-outside_sources.md`
  `project-level/task/skill/SKILL.md` · `project-level/task/template.md`
  `project-level/technology/SKILL.md` · `elements/common/way_of_working.md`
  `elements/common/critique/SKILL.md` · `elements/common/skill/SKILL.md`
  `instruction-files/SKILL.md` · `agent-instructions/skill_entry_points.py`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/decisions.md:6-36`
  `foundations/decisions.md:806-901` · `foundations/decisions.md:1024-1085`
  `foundations/decisions.md:1709-1743` · `foundations/decisions.md:1799-1828`
  `foundations/decisions.md:1938-1970` · `foundations/decisions.md:2072-2103`
  `foundations/decisions.md:2140-2285` · `foundations/decisions.md:2454-2486`
  `foundations/decisions.md:2800-2824` · `foundations/decisions.md:3030-3054`
  `foundations/decisions.md:3193-3256` · `foundations/decisions.md:3407-3725`
  `foundations/decisions.md:3774-4098` · `foundations/decisions.md:4765-4801`
  `foundations/decisions.md:4913-4984` · `foundations/decisions.md:5357-5485`
  `foundations/decisions.md:5657-6368` · `foundations/invariants.md:2133-2152`
- **Checks:** process prose, no test asserts it. The two entry points are written with the
  generator's own `discover` and `produce`, in process, for these two paths only — never by
  hand, never by `--write` here; their bytes equal `produce(discover(ROOT))` for those paths.
  `python -B agent-instructions/skill_entry_points.py` then prints no `would create` and
  exactly 30 `would change` lines, the paths of S5–S7; output kept. `python -B gate/run_tests.py agent-instructions`
  and `python -B gate/run_tests.py gate` fail on the 30 stale entry points until S7 — recorded,
  never suppressed. The report carries the row-to-text table of spec §10: each of rows 5–24, 26
  and 27 against the sentence of the skill or a template that carries it. `git diff --check`.
- **Depends on:** Slice 1 · F1 (WAY-167, WAY-172–WAY-175, WAY-182–WAY-192) · F2

