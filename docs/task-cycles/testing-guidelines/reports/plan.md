# Planner report — testing-guidelines (`plan-task`)

Status: done with concerns

- Plan: `.runs/task-cycles/testing-guidelines/plan.md`
- Size report: `.runs/task-cycles/testing-guidelines/plan-size.md` — `python -B task-cycle/slice_size.py .runs/task-cycles/testing-guidelines/plan.md`
  from the worktree root, exit 0, every slice `fits` (S1 110 874, S2 93 988, S3 152 786, S4 136 458,
  S5 53 390 estimated tokens; 1, 2, 4, 3 and 5 files to change).
- Base: `4302f72ba638fb222fc3d9de73decacdf7ca6682`; nothing written outside the three files of the
  dispatch; `git status --short` clean (`.runs/` is ignored).

## Shape of the plan

Foundation step (one agent, before Slice 1): WAY-231–WAY-250 new, WAY-228/174/215/218/214 edited
in place, glossary `exemplar` edited, a new fact under WAY-232 and, if relied on, one under WAY-236;
row 25 tied per C3. Then five slices, one after another:

1. Testing template `product-guidelines/testing/template.md` — model `same`, risk none.
2. Coding template and skill give up the rule of tests; kinds exclude tests; WAY-247 clause —
   `cheaper`, none.
3. Skill `product-guidelines/testing/SKILL.md`, the-way `README.md`, generator run
   (`python -B agent-instructions/skill_entry_points.py --write`) with its output committed —
   `same`, none.
4. `product-guidelines/reading.md`, `project-level/task/skill/SKILL.md` step 3,
   `project-level/plan/skill/SKILL.md` step 2 — `cheaper`, none.
5. Installer `SKILLS`, `installation/README.md`, new test
   `installation/test_testing_guidelines_installation.py`, counts 38→40 in two tests — `cheaper`,
   trust boundary `installation/install.py`. Failing test first.

Every *To do* item, every *Questions carried to cycle*, rows 1–25 (row 25 as tied per C3) and every
entry of the spec's *Foundation entries* are mapped in *Coverage*.

## Open design choice (step 2 of the method)

None found. Reading the code confirmed the spec: `product_guidance` builds the block's list from
`SKILLS` (`installation/install.py:143-160`), so the block needs no text change; the only tests
counting entry points are the two the spec names (`grep` for `38` in `installation/`); the
generator discovers skills from git (`agent-instructions/skill_entry_points.py:68-80`), so the new
skill needs no registration there; `.runs/` is ignored (`.gitignore`), so the skill's reports under
`.runs/testing/` need nothing in a product's `.gitignore` beyond what the installer writes
(`installation/install.py:53`).

## Concerns

1. **Volume of the foundation step.** Twenty new decisions, five edits, a glossary edit and up to two
   facts, with about twelve quotations to re-read on their pages (spec "Quotations"). Kept as one
   agent as the method gives; if it proves too large, the orchestrator can split it into two
   dispatches (rows 1–13 with the facts; rows 14–24 with the edits and the glossary). Recorded in
   *Choices*.
2. **Generated entry points named by two glob paths.** The generator rewrites all 21 skills' entry
   points in both directories — 42 files, over the size script's limit of 10 — though no agent
   edits them. Slice 3's *Change* names them as `.claude/skills/the-way-*/SKILL.md` and
   `.agents/skills/the-way-*/SKILL.md`, which the script counts as two files. The earlier styleguide
   cycle instead cut them into batches of ten written in process
   (`C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.runs/task-cycles/product-guidelines-styleguide/plan.md:243-343`),
   with the gate red between batches. If the orchestrator prefers that, four batch slices follow
   Slice 3. The mechanical check of Slice 3 should compare the changed files against the glob and
   the two named files.
3. **Unmeasured reads.** The size script reads only files that exist at the base under the root, so
   three reads stand in *Read* outside backticks and are not measured:
   `product-guidelines/testing/template.md` (created by Slice 1, read by Slices 2 and 3) and section 1
   of `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/research_wytyczne_testow/raport_wytyczne_testow.md:25-63`
   (read by Slice 1; outside the repository, in the author's private notes). Each is far smaller than
   the margin left (largest slice about 153k of 250k tokens). The orchestrator copies the research
   passage into Slice 1's handoff, as with any passage.
4. **The research table holds a cut item.** Its row "Czy błąd złapał dopiero test wysoki albo
   człowiek?" answers "test najniższego poziomu, który ten błąd łapie, czerwony przed poprawką";
   "red before the fix" is on Q14's cut list ("poprawka dostaje test czerwony bez poprawki"), and its
   sources column cites the private 10xDevs course (WAY-27). Slice 1's goal renders the table without
   both; listed in *Choices*.
5. **Installer tests install the committed `HEAD`.** Slice 5's tests need
   `product-guidelines/testing/SKILL.md` committed (the setUp of the coding test asserts it), so
   Slice 5 depends on Slice 3's commit; its failing-first run fails on the missing `CREATE` lines,
   the intended reason.
6. **Pre-existing, not fixed:** the non-UTF-8 case of the crafted-input test stops on an uncaught
   `UnicodeDecodeError` (C37 of the coding cycle, comment at
   `installation/test_coding_guidelines_installation.py:150-152`); the new test mirrors that
   assertion.

## Guidelines

The-way has no `guidelines/` of its own (as the dispatch says), so no guideline file is named in any
*Read*; nothing found missing or uncertain beyond that. No user interface is touched, so the
styleguide's order-of-work example does not apply.

## Reaches beyond the dispatch

- `task-cycle/skill/SKILL.md:95-300` — how the foundation step and slices are dispatched and how the
  orchestrator rebuilds ranges, to shape *Foundation entries* and the *Read* fields.
- `elements/common/way_of_working.md:58-96` "Reading the foundation" — to select each slice's
  decisions by *Scope*; decision ranges computed by a scratch script over `foundations/decisions.md`
  headings and *Scope* lines at the base.
- `task-cycle/slice_size.py` whole — how it reads paths (backticks only; existing files only in
  *Read*; a missing path in *Change* counts as created).
- `C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.runs/task-cycles/product-guidelines-styleguide/plan.md:240-349`
  and `C:/Storage/repos/the-way-wt/lead-project/.runs/task-cycles/lead-project/plan.md` (grep) —
  precedent for entry-point regeneration in a plan.
- `agent-instructions/skill_entry_points.py:1-80`, `gate/test_skills_reach_the_way_sessions.py:1-60`,
  `.claude/skills/the-way-critique/SKILL.md` — that every entry point lists every sibling, so the
  generator rewrites all of them.
- `elements/common/foundation_check.py:1-30` — that a decision number cited in any tracked file
  must name an entry, which orders the foundation step before every slice.
- `installation/test_coding_guidelines_installation.py` whole, `installation/test_install.py:15-40`,
  `installation/test_styleguide_installation.py:80-95`, `installation/install.py:20-55, 140-165`,
  `installation/README.md:50-60, 160-178` — Slice 5's files and checks.
- `foundations/part_map.md` whole — trust boundaries and the parts of each file (`README.md` is left
  out on purpose).
- The research report's section 1 (path in concern 3) — the table Slice 1 renders.
- `.runs/task-cycles/testing-guidelines/cycle.md`, `reports/design.md`, `reports/spec-review.md` —
  rulings C1–C5 and the spec's revision history.

## Questions

None.
