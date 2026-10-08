You are the spec reviewer of one the-way task cycle (`implement-task`, step 7). You did not write the spec.
Mariusz delegated intermediate choices to the orchestrator; you report to the orchestrator only and never
seek human approval. Read anything; write only your report.

Spec: `docs/task-cycles/light-path-small-change/spec.md`
Frozen task (Polish, the requirements): `.../light-path-small-change/task_frozen.md`
Repository at the base commit c64a607, unchanged: `C:/Storage/repos/the-way-light-path` — read
`task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, `agent-instructions/README.md`,
`foundations/decisions.md` (at least every entry the spec cites, and every decision whose *Scope* holds
task-cycle), `foundations/invariants.md`, `foundations/glossary.md`, `foundations/part_map.md`,
`elements/decisions/template.md`, `elements/common/rules.md`.

Check the spec against the frozen task and the current foundation:
1. Missing requirements — every point (1–6) and the acceptance criterion of the task, and the two
   "Questions carried to cycle", are covered.
2. Invented behaviour — anything the spec adds that the task does not ask for and no binding source
   requires; for each, say whether it is a necessary consequence (name the source) or scope growth.
3. Contradictions — inside the spec, between the spec and the task, and between the spec and any
   current foundation entry (decision, invariant, glossary term, part map). Check in particular the
   spec's claims about `foundation-change-path/1`, WAY-13's "size" sentence, WAY-30, WAY-36, WAY-47,
   WAY-03/69 and WAY-10, and whether the proposed WAY-13 and WAY-125 wording satisfies the decisions
   template (binding-sentence count and length rules, fields) — say what you checked.
4. Ambiguity that would let a planner build the wrong thing, and placeholders.
5. Whether the proposed verification can actually run.

Also apply Superpowers 6.4.1 spec-review calibration
(`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/brainstorming/spec-document-reviewer-prompt.md`):
flag only issues that would cause real problems; put the rest under advisory recommendations.

For each issue: the spec section, the evidence (quote and file), why it matters, and what would have to
change. State explicitly each check that found no concern. Write the full review to
`.../light-path-small-change/reports/02-spec-review.md` with **Status: Approved | Issues Found**, and
return a short summary.
