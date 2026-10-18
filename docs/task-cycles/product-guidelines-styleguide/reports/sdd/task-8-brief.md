### Task 8 — The installer gives products the skill and names the form check

- **Goal:** `installation/install.py` `SKILLS` holds `maintain-styleguide` →
  `product-guidelines/styleguide/SKILL.md`, so a product gets both wrappers and every wrapper's
  sibling list names it; `product_guidance()` gains the one sentence of spec §8 naming both
  form-check commands, run before a merge in which a file of `guidelines/` or `foundations/`
  changed; `installation/README.md` names the skill in its table; a new ordinary test file
  shows both.
- **Change:** `installation/install.py` · `installation/README.md`
  `installation/test_styleguide_installation.py`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md` · `installation/test_install.py`
  `installation/test_lead_installation.py` · `installation/test_installed_guidance.py`
  `foundations/part_map.md` · `foundations/decisions.md:995-1022`
  `foundations/decisions.md:1114-1142` · `foundations/decisions.md:1370-1394`
  `foundations/decisions.md:3030-3054` · `foundations/decisions.md:3774-3831`
  `foundations/decisions.md:4409-4431` · `foundations/decisions.md:5439-5485`
  `foundations/decisions.md:6035-6057` · `foundations/invariants.md:2095-2104`
- **Checks:** start from a failing test in `installation/test_styleguide_installation.py`
  (preview of an install from the committed checkout lists no `the-way-maintain-styleguide`
  wrapper; the guidance lacks the form-check sentence); then preview, apply and repeat from a
  committed checkout: both wrappers byte-identical, the pinned source path, the sibling sentence,
  the guidance sentence with `python -B .the-way/product-guidelines/form_check.py` and its
  `--merge-onto <main commit>` form, product files preserved. `installation/test_install.py` and
  `installation/test_installed_guidance.py` stay unchanged (they hold tests citing
  `installation-claude-guidance/1`; WAY-03). Run `python -B gate/run_tests.py installation`
  and `python -B gate/run_tests.py gate`. WAY-48: the reviewer checks the changed installer
  against crafted product files as the existing tests do (an existing `AGENTS.md` block, a CRLF
  file), and that no product-chosen path enters the block (WAY-107). Final: the baseline set —
  `python -B gate/run_tests.py <directory>` for `gate`, `elements/decisions`, `elements/invariants`,
  `elements/glossary`, `elements/part-map`, `elements/environment-facts`, `relation-model`,
  `agent-instructions`, `installation`, `instruction-files`, `task-cycle`, `project-level` and
  `product-guidelines`, the five format guards with the no-main options of
  `agent-instructions/README.md`, `python -B agent-instructions/skill_entry_points.py` and
  `git diff --check 96623ed..HEAD` — every exit code and unchecked line kept.
  (`reports/run_checks.py all` also runs `elements/common`, which holds no test and exits 1 at the
  base as well.)
- **Depends on:** Slice 4 (the skill committed) · Slice 3 (the commands it names exist) · Slice 7
  (gate green before the installer's run) · F2 (`installation` *Depends on*)

