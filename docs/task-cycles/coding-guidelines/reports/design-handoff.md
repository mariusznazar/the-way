# Design handoff — coding guidelines (step 6 of the task cycle)

## Delegation

Mariusz asked for the-way's task cycle (`task-cycle/skill/SKILL.md`) to take this task to a pull
request. He delegated intermediate choices to the orchestrator; the only ordinary human contact is
the request. You are the design agent of step 6. You never ask Mariusz anything and never claim his
approval; questions go back to the orchestrator in your report.

## Worktree and write boundaries

- Worktree: `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc` at `235b0b4`
  (= `foundations` tip). **Do not edit any tracked file and do not commit.** This stage writes no
  code and no foundation entry.
- You write only:
  - the spec: `docs/task-cycles/coding-guidelines/spec.md`
  - your full report: `docs/task-cycles/coding-guidelines/reports/design.md`
  - any working notes beside it in `.../reports/` (prefix `design-`).
- Scratch reading copies outside the repository are read-only for you.

## Authoritative inputs (read whole)

1. Frozen task: `docs/task-cycles/coding-guidelines/task-frozen.md` (Polish;
   from the vault commit `cf7eefd`). Its *To do*, *Questions to settle* with their answers and
   sources, *Questions carried to cycle*, *Decisions in play*, *Settlements to record* (25 rows)
   and *Out of scope* are binding. The settlements' meanings are Mariusz's and may not change; your
   spec says how each row becomes an entry, not whether.
2. Research of the task (read-only copies of the vault at `cf7eefd`):
   `/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/brain-main/Notes/Projects/(P) Proces pracy nad produktem/research_wytyczne_kodowania/`
   — `research_open_mercato.md`, `research_podejscia.md`, `research_vault_kurs.md`,
   `research_the_way_stan.md`. The previous task document, for the styleguide discipline:
   `.../brain-main/Notes/Projects/(P) Proces pracy nad produktem/_zadania/wytyczne_produktu_styleguide.md`.
3. The-way at `235b0b4`: `AGENTS.md`, `agent-instructions/README.md`, the whole
   `foundations/part_map.md`; select and read the foundation by "Reading the foundation" in
   `elements/common/way_of_working.md` (WAY-150) for the parts this work touches (at least
   product-guidelines, decisions, invariants, glossary, gate, installation, agent-instructions,
   instruction-files, task-cycle). The task's *Decisions in play* lists the entries the refinement
   found, with fingerprints at this same commit — a starting map, not a substitute for reading
   them whole.
4. Code and templates you design against: `product-guidelines/template.md`,
   `product-guidelines/styleguide/template.md`, `product-guidelines/styleguide/SKILL.md`,
   `product-guidelines/form_check.py` and its tests, `installation/install.py` (`SKILLS`),
   `agent-instructions/skill_entry_points.py`, `gate/run_tests.py`, `gate/method_script.py`,
   `foundations/invariants.md` entries `guidelines-*`, `gate-fork-point-evidence/1`,
   `invariant-test-break/1`.
5. Reference only — how the previous cycle on this frame was designed (its spec and design report),
   from `git show cf27d79:docs/task-cycles/product-guidelines-styleguide/spec.md` and
   `.../reports/design.md`. Use it to stay consistent with the styleguide discipline's
   structure; it binds nothing.

## Method

Use Superpowers 6.4.1 `brainstorming`, read whole from
`/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/superpowers-6.4.1/skills/brainstorming/SKILL.md`
and the files it links (same tree). This is a clone of tag `v6.4.1`, the version the cycle
requires; the harness has no installed plugin. Classify the task with that skill (record the
classification) and follow its architectural path to a spec. Cycle-specific overrides:

- Your partner in the dialogue is the orchestrator, not the human. Where the skill would ask the
  human a question, either answer it from an approved source (task, its sources, the foundation,
  code) and record the answer and its evidence, or — where no source answers it — choose the
  smallest reversible interpretation that fulfils the task, record alternatives and the cost if
  wrong, and mark it **for orchestrator ruling** in your report. Return early with questions only
  when a choice blocks the rest of the design; otherwise finish the spec with your marked
  proposals and the orchestrator rules on them after.
- Where the skill expects human approval of the design or spec, treat it as a provisional
  orchestrator go-ahead; do not wait.
- The spec goes to `spec.md` above, not the skill's default location. Your boundary is the
  self-reviewed spec: return before the skill hands on to writing a plan. Do not invoke
  `writing-plans` or any other skill afterwards.
- Do not silently expand scope; *Out of scope* of the task is binding.

## What the spec must settle

- Every one of the seven *Questions carried to cycle*, each with the way chosen, the ways weighed,
  evidence and cost if wrong. Note which are mere "how to make" choices (WAY-135) versus open
  design choices.
- For each of the 25 settlement rows: which kind of entry (decision / invariant / glossary term),
  its proposed identifier (next free decision is WAY-193; glossary words through
  `record-glossary-term`), what it derives from or narrows, what invariants verify it, and for the
  rows that change an existing entry (WAY-167, WAY-168, WAY-114 departure, the `guidelines-*`
  invariants) whether the change is edited in place before `main` (`agent-instructions/README.md`)
  and what dependents must be renewed (WAY-31). The new gate invariant of row 13 and its method
  (`TODO` until the gate can, per question 12).
- The files the-way gains or changes: coding template(s) under `product-guidelines/`, the skill
  `maintain-coding-guidelines`, the changes to `form_check.py` (two file forms, the `coding.md` /
  `coding-<kind>.md` naming, the invariant-in-every-rule rule, the copy/do-not-copy status table
  and the existence of its files, the index of kind files), changes to the common template for
  good/bad examples as test cases, entry points, installer `SKILLS`, part map lines, tests.
- Adversarial inputs for the form check (trust boundary) under WAY-48.
- What could be checked mechanically versus left to review, and which checks are invariant
  tests (three authors under WAY-69).

## Report contract

Write your complete report to `reports/design.md`: inputs read (with commit), the classification,
every question with answer/evidence or your marked proposal, rejected alternatives and their
costs, the foundation selection you read (entries read whole vs discovered), concerns, and
anything unchecked. Return a short message: status, paths, the list of items marked for
orchestrator ruling, and blocking questions if any.
