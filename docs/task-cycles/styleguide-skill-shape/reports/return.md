# Return step report

**Status:** done. Nothing in the foundation or the part map needs correcting; no commit. Head stays `d32f76d`.

## Reading done for the comparison

- Decisions of the task's *Decisions in play*, each whole: WAY-256, 257, 258, 127, 259, 185, 186, 187, 120 (read in the first run) and now WAY-154, 155 and 172. (WAY-155 is not in *Decisions in play* but sits beside WAY-154; read for context.)
- Part map entries `product-guidelines` and `instruction-files` (`foundations/part_map.md:136-165`), whole.
- Still not read whole: the other decisions of the first handoff's list (see my first report); the handoff of this step asked only for those of *Decisions in play*.

## Comparison

| Entry | Against | Result |
|---|---|---|
| WAY-154 (refiner ends its turn as `questions` ...; orchestrator hands only path and routing) | `orchestrated_mode.md`, pointer in `SKILL.md` | matches; the section's text is verbatim, only its place changed |
| WAY-172 (a meaning reaches the code only through the accepted document; using an existing meaning takes no approval) | the paragraph in `SKILL.md`, `task_document.md`, `hand_back.md` | matches; the paragraph stays in `SKILL.md`, the document's list is in `task_document.md` |
| WAY-185 (recognise the interface and what the product has first; extend, do not bring a new system) | `recognize.md` | matches; step 1 is still the first step, and nothing is read before the interface is named except what refine-task read |
| WAY-186 (research at every extension and never at a refresh; preferred tool stays the proposal; critique before the human sees) | `starting_rules.md`, `research.md` | matches; the condition and the refresh clause stand in `starting_rules.md`, the research and its critique in `research.md` |
| WAY-187 (audit both directions, three to five charges, four categories, standing question) | `audit.md` | matches; one read of the agent's-way decisions added |
| WAY-120 (fresh critic, author's verdict) | `research.md`, `settle.md` | matches; both critiques remain |
| WAY-127, WAY-259 (an entry point reads the skill whole and a named file when its step or variant comes) | `SKILL.md` step pointers | matches; step 0 no longer reads everything at the start |
| WAY-256 (a fragment of one step or variant stands beside the skill; one instruction stays) | the layout; assessment rows | matches; `hand_back.md`, `new_tools.md`, `staged_cleaning.md` each hold several instructions |
| WAY-257 (every row shows when needed and whether recognised) | `assessment.md` | matches: every row of the table has both columns |
| WAY-258 (layout of the files of `instruction-files`; no rule in two files) | `instruction-files/kind_skill.md:8-14` | matches; the edit changed the question of one rule in place, and the rule stands once |
| Part map `product-guidelines` (files `product-guidelines/**`; the template of each discipline with the skill that leads it) | the new files lie under `product-guidelines/styleguide/` | matches |
| Part map `instruction-files` (files `instruction-files/**`) | `kind_skill.md` | matches |

## Searches

All over the worktree, `.runs/`, `.claude/` and `.agents/` excluded, and the rebuilt files themselves excluded.

1. What points at the old place of `maintain-styleguide`'s sections. Patterns (extended regex, `grep -rnE`, `*.md`, `*.py`, `*.json`): `What reaches the task document`, `Orchestrated mode`, `styleguide/SKILL`, `maintain-styleguide.{0,80}(step|section)`, and "styleguide" within a line of "step 0" to "step 5". Result: `What reaches the task document` and `Orchestrated mode` are found only as the own headings of the sibling skills `product-guidelines/coding/SKILL.md` and `product-guidelines/testing/SKILL.md` (out of scope, tasks 8 and others) and of refine-task (`project-level/task/skill/SKILL.md:16`, its own section); `styleguide/SKILL` is found in `installation/install.py:42` and `installation/test_styleguide_installation.py`, which use the path of `SKILL.md`, not a section; the other patterns found nothing. Also in `foundations/*.md`, `instruction-files/*.md`, `agent-instructions/*.md` and `AGENTS.md`: `both templates`, `step 0`, `Writing the file`, `Orchestrated mode`, `critique/SKILL`; the only hit, `foundations/decisions.md:4102`, is about plan-project step 0, not this skill. Nothing points at a moved section or a step number of this skill.
2. An entry that says what `kind_skill.md:8-14` said before ("every use needs it"). Patterns: `every use (of the skill )?needs`, `every use of a skill`, `needs it every use`, `fragment ... every use`, `every use of the skill`, `only one step or one variant`. Result: only `kind_skill.md` itself (the edited lines); the foundation states the rule in WAY-256 ("whether a use of the skill needs it at that step"), which agrees with the new wording. No other file repeated the old wording.

## Commands and exit codes

- `python -B elements/common/foundation_check.py`: exit 0, "0 errors".
- `git status --short`: clean.

## Searches not found or unclear

- None unclear. Not found: any entry, section reference or instruction file that needed correcting.
- The decisions of the first handoff's list that I have still not read whole (WAY-128, 129, 134, 165, 167, 168, 173, 176, 177, 180, 182 to 184, 189, 191, 192, 213 to 215, 251) were not compared in this step; the handoff named *Decisions in play* only.
