# Slice 2 report — task refinement names human actions and checks the deployment skill

Status: DONE_WITH_CONCERNS

## Commits

- `fc03761` feat(project-level): Name a task's human actions outside the repository and check the
  deployment skill in refinement
- `51777aa` style(project-level): Rewrap refine-task's readiness check to the file's column (one
  line of the first commit ran past 100 columns)

Files changed: `project-level/task/template.md`, `project-level/task/skill/SKILL.md` only. Line
endings kept (both `i/lf w/lf`).

## What changed

`project-level/task/template.md`
- New section `## Human actions` in the document form, after *Questions carried to cycle*, with the
  line `- <action outside the repository> — before the cycle, done | before the cycle, not done | in
  the cycle`. It is not among the conditional sections, so it always appears.
- New rule under "What each section carries": each effect outside the product's repository (server,
  DNS, keys, external account) named as the human's action (WAY-140); reads stay with the agent;
  placement set by the human at refinement on the agent's proposal — `before the cycle` when the
  cycle's code needs the effect (with `done` / `not done`), `in the cycle` when the action uses code
  the cycle writes (WAY-140); placement `TODO` until placed; ready only when every action before the
  cycle is done (WAY-124); the cycle opens a blocked draft request listing the in-cycle actions and
  the human performs them at the request (WAY-140); `none` means no effect outside the repository;
  a task document written before the section existed names no action.

`project-level/task/skill/SKILL.md` (step numbering unchanged)
- Step 3, new bullet: name each effect outside the repository as a human action under *Human
  actions*; reads stay with the agent; propose each placement by that section's rule in the template
  (not restated, one home); the human places each, asked as "How a skill asks" says (WAY-140); an
  action before the cycle not yet done keeps `Status: waiting for human`, marked `done` once
  performed (WAY-124).
- Step 3, new bullet: when the outcome deploys the product or changes how or where it runs, check
  that the product has a deployment skill covering every item of the list WAY-139 holds (the list
  is not copied); where none or an item is missing, add a *To do* item or offer the human the split,
  which step 1 then handles (WAY-139); no such outcome, no check.
- Step 6 check: *Human actions* reads `none` or has every action placed and every action before the
  cycle done (WAY-124, WAY-140), before `Status: ready for cycle`.

## Checks

- `python -B gate/run_tests.py project-level` — 81 tests OK
- `python -B gate/run_tests.py gate` — 98 tests OK
- `python -B agent-instructions/skill_entry_points.py` — "entry points are current"; no
  `description` changed.
- `project-level/readiness_check.py` and its tests parse only the project definition's sections
  (`SECTIONS` at `project-level/readiness_check.py:50`), not the task template; no Python file reads
  `project-level/task/template.md`. Nothing pins the task template's section list.

## Self-review against the brief and WAY-124, WAY-139, WAY-140

- WAY-140: effect outside the repository made only by the human, named and placed before or in the
  cycle — template rule + step 3. Reads with the agent — both files. Human places each on the agent's
  proposal, by the rule "code needs the effect → before; action uses the cycle's code → in" —
  template rule; skill points to it. In-cycle actions → blocked draft request — stated in the
  template rule as what the placement means; the cycle's own behaviour is not in this slice's files.
- WAY-124: ready only when every action placed before the cycle is done — template rule, step 3
  status, step 6 check.
- WAY-139: list stays in WAY-139 only; the skill points to it; check runs only for a task that
  deploys the product or changes how or where it runs; missing skill or item → To do item or split
  by the human.
- No `foundations/` change; headings and markers in English; no history or dates.

## Concerns

1. The orchestrator's instruction said the template "already" says, for *Settlements to record*,
   that a document written before the section existed carries none. It does not: no such sentence
   exists in `project-level/task/template.md` (or elsewhere outside `.runs/`). I wrote the sentence
   for *Human actions* only, as instructed, and did not add one for *Settlements to record* (out of
   the slice's scope). Decide whether the asymmetry matters.
2. "A task document written before this section existed names no action" lets an older document be
   read as having no human action even when its To do has an effect outside the repository. That is
   the settled wording; a re-refinement of such a document would fill the section through step 3.
3. Status `waiting for human` for an undone before-cycle action is my reading of the existing status
   vocabulary (the status for a task blocked on the human), not a new rule; flag if the orchestrator
   prefers it left to step 6's "report an obstacle".
4. The skill says to "add an item to *To do*" for a missing deployment-skill item without asking
   first, and to "offer" the split, following the orchestrator's wording and WAY-139 ("the task gains
   an item ... or the human splits"). The added item still reaches the human when step 6 shows the
   whole document.
