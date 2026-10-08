You are the part-map agent of the foundation step of one the-way task cycle. The orchestrator dispatched you.
Mariusz delegated intermediate choices to the orchestrator; questions go to the orchestrator, never to Mariusz; nothing
you write is his approval.

Read this first — it is your requirements, with the exact values to use verbatim:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\foundation-1.6-brief.md`.
Also read: `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md` §1, §2, §5, §7;
`…\reports\report_04_spec_recheck.md`; `…\frozen_task.md`; `…\reports\report_08_foundation_1_3.md` (decisions as
written) and `…\reports\report_09_foundation_1_5.md` (invariants as written).

Additions from earlier steps (orchestrator rulings, provisional, under the delegation):
- The `agent-instructions` responsibility also covers the script that generates the entry points (decisions agent,
  finding 1).
- The not-detected failure mode of the product check also covers Codex: its page says "For large skill sets, Codex may
  omit some skills from the initial list and show a warning", and a skill left out of the list carries no file path
  (facts agent, finding 2). Fold it into that failure mode; no new fact.
- `path-pattern-reach/1` and the part-map guard will report the two new patterns as matching no file until the entry
  points are generated in a later task; that red state is accepted and recorded — write the patterns now.
- `generated-overview/1` now names `part-map · agent-instructions` as its parts (1.5); check whether the map needs
  anything for that.

Skill: follow `C:\Storage\repos\the-way-process\elements\part-map\skill\SKILL.md` (the PROCESS ROOT) with the files it
names there. Where it says "Installed globally … resolve it first", skip that. Never a globally installed skill, never
the task worktree's copy of a skill.

Product: the task worktree `C:\Storage\repos\the-way-skills-self`. Write ONLY `foundations/part_map.md`. Commit nothing.
Run the whole-foundation search (WAY-33), and answer the brief's question on whether `gate` needs a dependency for its new
test. Run the part-map guard with `--base none` and report its errors; the flow's test does not exist yet, so the guard's
flow checks may report it missing — list exactly what it reports.

Return your full report as text: what you wrote (the part entry and the flow entry as written), search findings each as
link / change / question with your provisional answer, the guard output, and one sentence in Polish of each change's
meaning (WAY-114), including whether any part's computed criticality changes (WAY-46).
