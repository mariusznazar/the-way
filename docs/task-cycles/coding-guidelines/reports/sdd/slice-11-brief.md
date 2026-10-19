### Slice 11 — The installer gives products the skill

- **Goal:** `installation/install.py` `SKILLS` holds `"maintain-coding-guidelines":
  "product-guidelines/coding/SKILL.md"`, so a product gets both wrappers, every wrapper's sibling
  list and the `AGENTS.md` block name it, and no other text of the installer changes (the
  `installation-command` surface keeps its wording); `installation/README.md` names the skill in
  its table of installed files and in its list of what the tests check; a new ordinary test file,
  `installation/test_coding_guidelines_installation.py`, on the pattern of
  `installation/test_styleguide_installation.py`, shows the install and the refusals. The F4
  `NAMES` test passes.
- **Change:** `installation/install.py` · `installation/README.md`
  `installation/test_coding_guidelines_installation.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md` · `installation/test_install.py`
  `installation/test_styleguide_installation.py` · `installation/test_installed_guidance.py`
  `foundations/part_map.md` · `foundations/decisions.md:995-1022`
  `foundations/decisions.md:1114-1142` · `foundations/decisions.md:1370-1394`
  `foundations/decisions.md:3030-3054` · `foundations/decisions.md:3774-3831`
  `foundations/decisions.md:4409-4431` · `foundations/decisions.md:5439-5508`
  `foundations/invariants.md:2065-2073` · `foundations/invariants.md:2095-2103`
- **Checks:** start from a failing test in the new file (a preview from the committed checkout lists
  no `the-way-maintain-coding-guidelines` wrapper) and the F4 `NAMES` test, RED. Then preview, apply
  and repeat from a committed checkout: both wrappers byte-identical, the pinned source path, the
  sibling sentence, the block naming `the-way-maintain-coding-guidelines`, product files preserved.
  WAY-48, crafted input: a conflicting file at the new wrapper's path in `.claude/skills/` and in
  `.agents/skills/`, a directory there, a non-UTF-8 file there — each stops the run before anything
  is written. Run `python -B gate/run_tests.py installation` (all pass) and
  `python -B gate/run_tests.py gate`. Final, by the executor, every exit code and unchecked line
  kept: `python -B gate/run_tests.py <directory>` for `gate`, `elements/decisions`,
  `elements/invariants`, `elements/glossary`, `elements/part-map`, `elements/environment-facts`,
  `relation-model`, `agent-instructions`, `installation`, `instruction-files` (3 platform failures
  expected, as at the base), `task-cycle`, `project-level`, `product-guidelines`; the five format
  guards with `--base none` and, where available, `--merge-onto none`; both form-check runs on
  the-way; `python -B agent-instructions/skill_entry_points.py`; `git diff --check 235b0b4..HEAD`.
- **Depends on:** Slice 6 (the skill committed) · Slice 10 (gate green) · F4 (`NAMES`)

