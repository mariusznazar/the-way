# Spec review handoff

The user invoked `the-way-implement-task` and delegated intermediate choices to the root
orchestrator. You run step 7 of `task-cycle/skill/SKILL.md` only: an independent review of the spec.
You did not write it. No code, spec or foundation edits; no subagents of your own unless a whole-file
read would not fit; return questions to the root, never the human.

- Worktree: `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, base
  `96623ed7710100fe6e11a0ce3c052fc44d4af52d` (`foundations`).
- Read whole: the frozen task `.runs/task-cycles/product-guidelines-styleguide/task.md` (it binds
  over the spec; its 27 rows carry meanings the human accepted), the spec
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`, and the root's provisional answers C5–C10
  in `.runs/task-cycles/product-guidelines-styleguide/cycle.md` (questions table).
- Select the current foundation by "Reading the foundation" in `elements/common/way_of_working.md`
  yourself for the touched parts the spec names (decisions, glossary, part-map, invariants,
  agent-instructions, installation, instruction-files, project-level, task-cycle, and the new part
  `product-guidelines`). The designer's `reports/foundation-selection.md` may serve as a map, not as
  proof; do not read the designer's `design.md` or research reports unless a finding needs to check a
  claimed source, and say so when you do.
- Read the relevant code the spec builds on: `relation-model/fingerprint.py`,
  `elements/decisions/format_guard.py` (relation fingerprints, `--merge-onto`), `elements/common/guard_shared.py`,
  `installation/install.py` and its tests, `agent-instructions/skill_entry_points.py`, `instruction-files/`,
  `gate/run_tests.py`, the element skills the new skill calls.
- Outside sources the task cites (read only): `C:/Storage/repos/loop2-10x/.claude/skills/10x-ui/SKILL.md`;
  `om-ux-shape` in `C:/Storage/repos/loop` at `715026e` (`git show`, `MSYS_NO_PATHCONV=1` in Git Bash);
  `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Przejście 10xDEVS/mapa_pakietu_10x.md` section `## m2l5`.

Review for: every *To do* item and every row covered; invented behaviour (anything the spec adds that
no row, answer or foundation entry supports — including the designer's own choices: common form for
every domain, no new critical flow, the 1 MiB limit, guidelines prose in English); contradictions with
the current foundation (WAY-04, WAY-09, WAY-18, WAY-22, WAY-30, WAY-38, WAY-48, WAY-60, WAY-69, WAY-93,
WAY-100, WAY-114, WAY-128, WAY-133, WAY-134 and any other you find); whether the form check's contract
(commands, `--merge-onto` version rule, exit codes, crafted-input defences) can be built and tested
with the standard library; whether the refinement/cycle split (C5) is stated so that a cycle author
can write a product's styleguide from a task document; whether the entry mapping (G1–G25, glossary,
six invariants, part map) holds each row's meaning without another meaning. Treat stylistic
preferences as Minor at most.

Read the user's review playbook for evidence and anchor format:
`C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/playbook_code_review.md`.

Write only `.runs/task-cycles/product-guidelines-styleguide/reports/spec-review.md`: findings graded
Critical / Important / Minor, each anchored (`spec.md:<line>`, source `path:line`), with its concrete
consequence and a suggested resolution; explicit verdicts on task compliance and design coherence;
what you did not check. Return status, report path and concerns only.
