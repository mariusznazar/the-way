# Handoff — designer (write-spec), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the designer of the spec. Follow the project skill `the-way-write-spec`
(read `task-cycle/spec/SKILL.md` in this worktree whole, and what it names) in the role of the
designer. Send every question to the orchestrator by returning `questions` with them in your
report; never ask the human, never write a plan or code, never write into `foundations/` or any
tracked file. Your boundary: `spec.md` and your report, then return.

## Worktree and paths

- Worktree (the process root and the product repository): `C:/Storage/repos/the-way-wt/testing-guidelines`,
  branch `task/testing-guidelines`, base `4302f72ba638fb222fc3d9de73decacdf7ca6682` (`foundations`).
  The-way is the top-level repository here; integration route `agent-instructions/README.md`.
- Frozen task (read whole): `.runs/task-cycles/testing-guidelines/task.md` (copy of
  `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/wytyczne_produktu_testy.md`,
  updated 2026-10-24, sources at `foundations` `4302f72`).
- Write the spec to: `.runs/task-cycles/testing-guidelines/spec.md`
- Write your full report to: `.runs/task-cycles/testing-guidelines/reports/design.md`

## Answers of step 4

- Trust boundary: yes — the change adds the new skill to `SKILLS` in `installation/install.py`, the
  trust boundary of part `installation`. The spec says how a crafted product file the installer
  reads cannot make that change write outside its own files.
- Irreversible operation: no.
- Open design choice: yes. At least these ways are open (from the task's *Questions carried to
  cycle*), and the spec settles each with the ways weighed:
  1. The English words the-way's entries use for a test level, a property test, a level's exemplar
     test and the source of the expected value; whether the glossary entry `exemplar` widens to a
     level's exemplar test or that test gets a word of its own (pytanie 9 excludes tests from kinds
     of code). New and changed terms go through `record-glossary-term` in the foundation step.
  2. The wording of WAY-228 in its new place: covering property tests (pytanie 13) and binding a
     product from the task that writes its testing guidelines instead of its coding guidelines.
  3. Whether `product-guidelines/reading.md`, WAY-213 and WAY-214 select the testing guidelines by
     *Applies to* alone, or also by its `## When to read` condition ("before writing or changing a
     test"), as a kind file's row of `guidelines/coding.md` is selected.
  4. How the installer and its tests (`installation/install.py:42-43`,
     `installation/test_coding_guidelines_installation.py`, `installation/README.md`) bring the new
     skill to a product that already pins the-way (e.g. `loop2`).
  5. How the 25 rows of *Settlements to record* map onto the foundation: which become new decisions
     (and their order and identifiers from WAY-231 on), which change an existing decision in place
     (WAY-174, WAY-213, WAY-214, WAY-215, WAY-218, WAY-228 and any other the task's items 3–6
     reach), which are carried by one decision together, and which tie to an entry already stated.
     Row 25 is a WAY-100-style adoption decision. A decision written from a row keeps the row's
     meaning; its wording is the writer's. Name the glossary, part-map and invariant entries the
     change writes or changes (e.g. the part map's `product-guidelines` responsibility, if it changes).

  Where the task and the foundation settle how to make something, that is no choice: state it in
  the spec as settled, with its source.

## What to read

- The whole frozen task and the sources it cites, outside the repository included (reading outside
  the repository is allowed; write nothing there):
  `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/research_wytyczne_testow/`
  (`raport_wytyczne_testow.md`, `propozycja_szablonu_i_skilla.md`, and the thread files as needed)
  and `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Przejście 10xDEVS/mapa_pakietu_10x.md`,
  section m3l1. The raport warns that most quotations were extracted by a page-fetch tool and must
  be checked on the page before entering an entry of the-way: the spec marks which quotations an
  entry will carry and that the writer checks them.
- The analogous artifacts, whole: `product-guidelines/template.md`, `product-guidelines/reading.md`,
  `product-guidelines/coding/template.md`, `product-guidelines/coding/SKILL.md`,
  `product-guidelines/styleguide/template.md`, `product-guidelines/styleguide/SKILL.md`;
  `installation/install.py`, `installation/README.md` and the installation tests of the
  coding-guidelines skill; `agent-instructions/skill_entry_points.py`;
  `project-level/task/skill/SKILL.md` (step 3) and `project-level/plan/skill/SKILL.md` where they
  name the guidelines disciplines; the-way's `README.md` where it lists the skills.
- The record of the cycle that wrote the coding discipline, as a precedent of shape, in git:
  `git show 3b36c02 --stat` and the files it adds under `docs/task-cycles/` (use
  `MSYS_NO_PATHCONV=1` before `git show <ref>:<path>` in Git Bash).
- Foundation, each entry whole (heading to next heading), selected by "Reading the foundation":
  - Decisions of the task's *Decisions in play*: WAY-08, WAY-13, WAY-16, WAY-48, WAY-51, WAY-121,
    WAY-167, WAY-168, WAY-171, WAY-172, WAY-173, WAY-174, WAY-198, WAY-199, WAY-200, WAY-209,
    WAY-212, WAY-213, WAY-214, WAY-215, WAY-218, WAY-228.
  - The other decisions whose *Scope* names `product-guidelines`: WAY-02, WAY-09, WAY-27, WAY-100,
    WAY-102, WAY-120, WAY-169, WAY-170, WAY-176, WAY-177, WAY-178, WAY-180, WAY-182, WAY-183,
    WAY-184, WAY-185, WAY-186, WAY-187, WAY-189, WAY-191, WAY-192, WAY-201–WAY-208, WAY-210,
    WAY-211, WAY-216, WAY-217, WAY-219, WAY-221 — at least those whose subject the change repeats
    for testing (the WAY-100 adoption decision of the styleguide and of the coding discipline, the
    skill's working decisions, the audit, the first invariants).
  - Decisions whose *Scope* names `installation` and that bear on adding a skill: WAY-34, WAY-89,
    WAY-107, WAY-127, WAY-141.
  - Glossary (`foundations/glossary.md`, short — read whole): especially `exemplar`, `guidelines`,
    `standing check`, `invariant test`, `user interface`.
  - Part map (`foundations/part_map.md`, short — read whole): parts `product-guidelines`,
    `installation`, `agent-instructions`, `project-level`, `task-cycle`.
  - Invariants: `skill-entry-points`, `skill-rule-source`, `installation-claude-guidance`,
    `generated-overview`, and those of `every` the change's files reach.
- Before naming any further entry, search the decision log by *Scope* as "Reading the foundation"
  gives; read more where relevance is uncertain.

## Report

Return a short message: your status (`questions` or `done`), the spec's path, the report's path,
and a one-line check result. In the report, give the ways weighed for each open choice, your
recommendation and its cost if wrong, every reach beyond this handoff, and your concerns.
