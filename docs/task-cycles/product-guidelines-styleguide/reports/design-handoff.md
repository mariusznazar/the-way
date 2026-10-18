# Design-stage handoff

The user invoked `the-way-implement-task` on the task frozen at
`.runs/task-cycles/product-guidelines-styleguide/task.md` and delegated every intermediate choice to
the root orchestrator. You run step 6 of `task-cycle/skill/SKILL.md` (this worktree) only: the
design that writes a reviewed-ready spec. Send questions to the root orchestrator by returning them;
never ask the human. Return at the spec — before any plan, foundation entry or product file.

## Where

- Worktree: `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, branch
  `task/product-guidelines-styleguide`, base `96623ed7710100fe6e11a0ce3c052fc44d4af52d`
  (`foundations`, equal to `origin/foundations`, clean). the-way is the top-level repository here;
  its own `foundations/` is the product's foundation.
- Task: independent, `Status: ready for cycle`, settlements accepted 2026-10-18, Human actions none.
  Its sources cite `foundations` `96623ed` (the base).

## Method

Use Superpowers 6.4.1 `brainstorming`, read whole from
`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/brainstorming/SKILL.md`
with its linked files (not the 7.0.0 install the Skill tool would load). Classify the task with that
skill and follow its architectural path to a spec. Write the spec to
`.runs/task-cycles/product-guidelines-styleguide/spec.md` instead of the skill's default location.
Where the skill expects a human design or spec approval, return the proposed sections and questions
to the root; the root answers provisionally under the user's delegation. Stop before the skill hands
on to writing a plan.

Before drafting the skill design, read the user's skill conventions:
`C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/konwencje_skilli_i_commandow.md`.
The repository's own layout and decisions take precedence over personal skill locations.

## Authoritative inputs (read whole)

- The frozen task — every *To do* item, every question with its answer, source and control
  question, *Context*, *Questions carried to cycle*, *Decisions in play*, all 27 rows of
  *Settlements to record*, *Out of scope*. The task binds over anything else; its rows' meanings are
  accepted by the human and need no new approval, but their wording into entries is the cycle's.
- `AGENTS.md`, `agent-instructions/README.md`, `elements/common/way_of_working.md` (whole),
  `elements/common/rules.md`, the complete `foundations/part_map.md`.
- The current foundation selected by "Reading the foundation" (WAY-150): touched or candidate parts
  are decisions, glossary, part-map, invariants, agent-instructions, installation, instruction-files,
  project-level (the technology step's research discipline, WAY-122, as a model), task-cycle (only
  as far as the styleguide's use in a cycle touches it; the cycle change itself is out of scope),
  and a prospective new part. Inspect every decision's current *Scope*, read selected entries whole,
  expand along links, read the glossary entries the design uses or could collide with. Record the
  selection — revision, touched parts, expected *Scope* matches, identifiers read with locations,
  entries merely discovered — in `reports/foundation-selection.md`. The task's own *Decisions in
  play* lists a prior search at `96623ed`; use it as a starting map, not as proof.
- Relevant code and skills of the-way: `relation-model/fingerprint.py` and how
  `elements/decisions/format_guard.py` checks a relation's fingerprint; `installation/install.py`
  (its skill list) and `installation/` tests; `agent-instructions/skill_entry_points.py`;
  `instruction-files/` (principles, skill and `check_instructions.py`) as the model of a principles
  document + skill + check script; the element skills (`elements/*/skill/` or equivalent) the new
  skill would call to write a product's decisions, invariants and facts; `project-level/technology/`
  for WAY-122's research discipline.

## Outside sources (read only, never write; sanitize what you quote)

- `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Przejście 10xDEVS/mapa_pakietu_10x.md` — section
  `## m2l5`, its rows 1–25 and the *Notatki* of step 3 (group 1, rounds 3–9, the draft of the
  guidelines; group 3 weak points).
- `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Przejście 10xDEVS/10-praca-nad-interfejsem-graficznym-aplikacji-ui.md`
  (the lesson the m2l5 rows come from).
- `C:/Storage/repos/loop2-10x/.claude/skills/10x-ui/SKILL.md` and its `references/`.
- `om-ux-shape` and `om-ux-setup` from the `loop` repository at `origin/test` `715026e`
  (`git -C C:/Storage/repos/loop show 715026e:<path>`; find the paths with `git ls-tree -r`; in Git
  Bash prefix `MSYS_NO_PATHCONV=1`).
- The trial result in `loop` at `315c443`, `context/changes/run-screen-tokens/`.
- `C:/Storage/repos/loop2/foundations/part_map.md` (around line 84) for how a product names its
  agent-directing part.

## What the spec must settle

The design choices the task leaves open, each with the ways weighed, the chosen way, its reason and
the price of being wrong:

1. *Questions carried to cycle* 1–5 (part and directory of the-way for the guidelines template, the
   styleguide template, the skill and the form script, and the skill's name; the guidelines' path in
   a product and how an installed product gets the new skill's entry point; how the form script
   computes a reference's fingerprint under WAY-38; how `instruction-files` applies to a styleguide
   pointed to from `AGENTS.md`; role names that avoid "surface", "view", "token" collisions). Rule on
   each: an open design choice, or a way of making what a row and the foundation settle.
2. The entries the change writes: map every one of the 27 rows to an entry (a row may join others in
   one decision where their meanings form one choice; row 26 frames rows 5–13 and 15 as the-way's
   decisions about what the template carries and the skill proposes), plus the WAY-100 decision
   naming what the-way adopts from `10x-ui` and the Open Mercato skills, the glossary term (row 25),
   part-map changes, and any invariant of the-way the form script or the skill makes true (WAY-22).
   Name entries; do not write them.
3. The contracts of the new files: the guidelines template and the styleguide template (sections,
   what each carries, what is pointed to in code rather than copied, WAY-04); the skill's modes
   (before the first screen; audit of a product with screens; refresh or extension) and how it
   converses, researches (WAY-122 discipline), writes the product's decisions, invariants and
   environment facts through the element skills, proposes the WCAG adoption decision (row 21), the
   first three invariants (row 19) and the `{fork-point}` companion (row 20); the form script's
   command, inputs, outputs, exit codes, what it checks (form by the template, each reference's
   fingerprint, row 3's stop before merge) and whether and how it joins a gate or test run; the
   installer and entry-point changes; the instruction-file pointer and the hard-coded-values rule
   (row 22).
4. The test and verification approach a later plan can run (commands that exist or will exist),
   adversarial inputs for any script reading a product's files (WAY-48), and how the skill's text is
   checked given it is process prose.

Answer what you can from approved sources. Where none settles a point, choose the smallest reversible
interpretation that fulfills the task, note the alternatives and the price of being wrong, and mark
it an autonomous choice. Do not expand the task's scope (its *Out of scope* holds: the task cycle for
view changes, the blocking rule, `loop2`'s own styleguide, observability guidelines). Flag any
contradiction between a row and the current foundation instead of designing around it.

## Write boundaries

Write only `.runs/task-cycles/product-guidelines-styleguide/spec.md`,
`.runs/task-cycles/product-guidelines-styleguide/reports/design.md` and
`.runs/task-cycles/product-guidelines-styleguide/reports/foundation-selection.md`. The root keeps
`cycle.md`. No commits, no edits to tracked files, no writes outside the worktree, no network
requests carrying personal data. Do not copy git-held files or diffs into reports; name paths and
commits.

## Report

`reports/design.md`: the brainstorming classification, the sources read with versions, every
question you sent to the root with its answer, every choice with evidence, rejected alternatives and
their cost if wrong, the row-to-entry mapping, contradictions found, the spec's self-review,
unchecked work and unresolved concerns. Return message: stage status, artifact and report paths, and
every unresolved question or concern affecting the spec review or planning — not the full report.
