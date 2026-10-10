### Task 2 — Describe the product layout and pin movement

- **Goal:** Installer documentation and the instruction-files skill describe the single guidance route through `AGENTS.md` and root `CLAUDE.md`; pin-move instructions handle the old installed rule only when a product is migrating from an older pin, and no text treats that rule as a file the current installer writes.
- **Change:** `installation/README.md` · `instruction-files/SKILL.md`
- **Read:** `.runs/task-cycles/installer-claude-md/task-frozen.md` · `foundations/decisions.md` · `foundations/invariants.md:2061-2070` · `foundations/part_map.md:200-248` · `instruction-files/principles.md:126-151` · `instruction-files/tool_loading.md:14-53` · `installation/install.py`
- **Checks:** Run `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`, `python -B gate/run_tests.py instruction-files`, and `python -B gate/run_tests.py gate`. Inspect references with `rg -n 'the-way\.md|CLAUDE\.md|AGENTS\.md' installation/README.md instruction-files/SKILL.md foundations/decisions.md`, checking the full context of each remaining legacy-rule mention. Read the foundation guards' reports and the test reports, including warnings and unchecked results.
- **Depends on:** Slice 1 · Settlement 1 · WAY-132/1 verification edit
