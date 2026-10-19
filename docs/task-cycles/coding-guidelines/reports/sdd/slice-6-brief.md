### Slice 6 — The skill `maintain-coding-guidelines` and its entry points

- **Goal:** `product-guidelines/coding/SKILL.md` holds spec §6.1–§6.5: frontmatter
  `name: maintain-coding-guidelines` and a one-line, safe plain YAML description starting "Use
  when"; where the-way lies, `the-way-` names, no Superpowers method, the order of the work only and
  no rule restated; steps 0–5, orchestrated mode, what reaches the task document, writing only
  under `.runs/coding/`; it follows WAY-193–WAY-212 and describes what it takes from outside sources
  without naming them (WAY-27). Its two entry points exist exactly as the generator produces them.
  The root `README.md` names `product-guidelines/coding/` beside the styleguide's directory in its
  list of directories and of skill directories.
- **Change:** `product-guidelines/coding/SKILL.md`
  `.claude/skills/the-way-maintain-coding-guidelines/SKILL.md`
  `.agents/skills/the-way-maintain-coding-guidelines/SKILL.md` · `README.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `product-guidelines/styleguide/SKILL.md` · `product-guidelines/template.md`
  `project-level/task/skill/SKILL.md` · `project-level/task/template.md`
  `project-level/technology/SKILL.md` · `elements/common/way_of_working.md`
  `elements/common/critique/SKILL.md` · `instruction-files/SKILL.md`
  `agent-instructions/skill_entry_points.py` · `installation/README.md`
  `foundations/glossary.md` · `foundations/part_map.md`
  `foundations/decisions.md:775-804` · `foundations/decisions.md:838-867`
  `foundations/decisions.md:1024-1056` · `foundations/decisions.md:3193-3256`
  `foundations/decisions.md:3407-3437` · `foundations/decisions.md:3517-3613`
  `foundations/decisions.md:3665-3725` · `foundations/decisions.md:3774-3899`
  `foundations/decisions.md:4765-4801` · `foundations/decisions.md:5439-7262`
- **Checks:** process prose, no test asserts it. The two entry points are written with the
  generator's own `discover` and `produce`, in process, for these two paths only — never by hand,
  never by `--write`; their bytes equal `produce(discover(ROOT))` for those paths.
  `python -B agent-instructions/skill_entry_points.py` then prints no `would create` and exactly 32
  `would change` lines, the paths of S7–S10; output kept. `python -B gate/run_tests.py agent-instructions`
  and `python -B gate/run_tests.py gate` fail on the 32 stale entry points until S10 — recorded by
  test name, never suppressed. `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  (the new files claimed). The report carries a table of rows 2, 3, 5, 8, 14, 18–22 and *To do* 2,
  3, 4, 7 against the sentence of the skill or of the coding template that carries each.
  `git diff --check`.
- **Depends on:** Slice 2 · Slice 1 · F1a (WAY-167, WAY-193–WAY-202) · F1b (WAY-203–WAY-212) · F2

