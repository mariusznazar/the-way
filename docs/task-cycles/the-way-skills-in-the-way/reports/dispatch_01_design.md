You are the design agent of one the-way task cycle (`implement-task`). The orchestrator dispatched you.

## Delegation and authority

Mariusz (the task owner) delegated intermediate choices of this cycle to the orchestrator. You return
questions to the orchestrator, never to Mariusz, and you never present any go-ahead as Mariusz's approval.
This is a one-off run of the cycle on the-way itself, before `main` exists; the run brief is
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\run_brief.md` — read it.

## Method

Use Superpowers 6.4.1 `brainstorming`: read
`C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\brainstorming\SKILL.md`
and its linked files in full and follow its work. Classify the task using that skill, then follow its
architectural path — this cycle requires a written spec and plan for every ready task. Adapter changes:
- Where the skill asks the user a question or for design/spec approval, do not ask anyone interactively.
  Answer from the sources below where possible; otherwise take the smallest reversible interpretation that
  fulfils the task, and list it under "Questions and provisional answers" in your report (question, your
  provisional answer, alternatives, price of being wrong). Only if a question blocks the spec entirely,
  stop and return it.
- Write the spec to `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md`
  instead of the skill's default location. Do not commit it (the directory is git-ignored).
- Do the skill's own spec self-review. Your boundary is the reviewed spec: return BEFORE invoking
  `writing-plans`. Do not invoke any further Superpowers skill.

## Write boundary

You may write only `spec.md` and your report (path below). Everything else is read-only: the task worktree
`C:\Storage\repos\the-way-skills-self` (branch `task/the-way-skills-in-the-way`, at
c64a6071384fb57cdb9d7e9db4560ddc43e3b355), the process root `C:\Storage\repos\the-way-process` (same commit),
the vault, `C:\Users\Mariusz\.claude\`. Do not run commands that change any of them.

## Sources (binding)

- Frozen task: `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\frozen_task.md`
  (in Polish; `Project relation: independent`). Its "Questions carried to cycle" and "Decisions in play" are
  yours to settle in the spec.
- The-way's foundation in the task worktree: `foundations/decisions.md`, `invariants.md`, `part_map.md`,
  `glossary.md`, `environment_facts.md`. The task document is a starting map, not proof that nothing else
  applies: search the whole foundation for entries that bind or collide (e.g. WAY-09, WAY-44, WAY-34,
  WAY-101, WAY-107, WAY-125, invariants `repository-file-location` and the part-map/file-assignment ones,
  the `installation` and `agent-instructions` parts, `installation-command`).
- The-way's integration route: `AGENTS.md`, `agent-instructions/README.md` in the task worktree.
- What the task names: `installation/install.py`, `installation/README.md`, `installation/test_install.py`,
  every `SKILL.md` in the repository (11 today) and the paragraph each has about global and product mode
  (e.g. `project-level/task/skill/SKILL.md:12-14`, `elements/decisions/skill/SKILL.md:13-17`),
  `elements/common/way_of_working.md`, `gate/run_tests.py`.
- Absorbed task (from the ai-review ledger AIR-393, settled draft of an addition to
  `elements/common/way_of_working.md` after its line 10): "When the work is on the-way itself in a worktree
  of its own, use that worktree's `elements/` instead: the resolved link points to the main checkout,
  whatever branch it holds. The same holds for a skill handed over to by name (`record-decision`,
  `update-part-map`): read its `SKILL.md` from the same worktree." Treat it as material: the task's point 2
  is its successor, and the spec decides whether this sentence or a successor wording is needed once the
  entry points exist.
- Facts the orchestrator observed (verify what you rely on): `C:\Users\Mariusz\.agents\skills` is a link to
  `C:\Users\Mariusz\.claude\skills`; that directory links `record-decision`, `record-invariant`,
  `record-glossary-term`, `record-environment-fact`, `update-part-map` to the main checkout
  `C:\Storage\repos\the-way\elements\…\skill\`, and `refine-task`, `critique` to
  `C:\Storage\repos\vox-ai-tools\skills\…`. Several the-way worktrees exist side by side
  (`git -C C:\Storage\repos\the-way worktree list`).

## Constraints from the run brief that the design must respect

- Nothing may change outside the repository. Point 6 of the task (removing the five global links) is a step
  for the human after the merge: the spec gives the exact commands for the request description; the cycle
  does not run them.
- The-way must not install itself (no submodule, pin or product foundation files) — task point 1.
- Every tracked file must fit WAY-09 and the invariant `repository-file-location`, and belong to exactly one
  part (WAY-44). If the design needs a change of WAY-09's meaning, say so explicitly: a change of meaning of
  an approved decision has to go to Mariusz (WAY-07) and would block the request; prefer a design that does
  not need it if one fulfils the task, and state the price of each reading.
- Tests: `python -B gate/run_tests.py <directory>` for each changed part and always `gate`; format guards of
  changed foundation files with `--base none` and `--merge-onto none`.
- Name the foundation entries the task will write or change, with one sentence of meaning each; the cycle's
  foundation step writes them, not you.

## Report

Write your full report to
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\report_01_design.md`:
classification and why; path followed; sources read (paths); the design decisions with alternatives rejected
and price if wrong; "Questions and provisional answers"; the foundation entries named; the self-review result.
Return a short summary (under 300 words) with the report path.
