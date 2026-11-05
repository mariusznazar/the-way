# Report 06 — the return step

**Status:** `done`. Nothing to write or correct; no commit made. Head stays `3023f604d5517ca157b3cb6bb9135a360d7e29f3`, worktree clean (`git status --short` empty).

I read whole `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`, and the handoff, the frozen task and report 04 (the review). I took no row of `task-cycle/change/SKILL.md`. The Minor findings M1-M4 and out-of-scope O1 of report 04 are not edited for here, as the handoff says. The sentence of To do 1 in `return_step.md` does not apply to a choice of this task: it excludes no entry.

## The record's *Return step* fields

- **Foundation compared with code:** compared WAY-293, WAY-05, WAY-148 and `elements/decisions/template.md` (written or changed by the change), the entries the task names (WAY-18, WAY-22, WAY-25, WAY-30, WAY-35, WAY-36, WAY-60, WAY-159, WAY-164, WAY-260) and the part map of the touched parts `decisions` and `task-cycle`, with the instruction files the change edits. Found nothing that no longer matches:
  - the WAY-05 fragment stands alike in the decision and in the template; no other file restates the ban on counts (grep for "script or count" and "names no file");
  - WAY-148's new clause agrees with `task-cycle/spec/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/spec/review.md` and the parenthetical in `task-cycle/skill/SKILL.md`; WAY-159, WAY-164 and WAY-260 (derived from WAY-148) say nothing a stage without a check result contradicts;
  - the repair rule of WAY-148/159/164/260 is stated in the two places `task-cycle/skill/SKILL.md` has (general rule and mechanical check of a slice executor's report); other mentions of WAY-159, WAY-164 and WAY-260 in `task-cycle/change/SKILL.md`, `task-cycle/review/whole_change.md` and `task-cycle/skill/request_template.md` name the checks and do not restate the repair rule, so they stay true;
  - `foundations/invariants.md`, `foundations/glossary.md`, `foundations/part_map.md` and `foundations/environment_facts.md` hold no mention of WAY-05, 18, 22, 25, 36, 148, 159, 164, 260 or 293 (grep, no hit), so no invariant derives from them and no entry waits for this change;
  - the part map gains or loses no file and changes no part's responsibility: the change edits files already assigned to `decisions` and `task-cycle`.
- **Decisions written or changed:** none in this step. (Of the change: WAY-293 new, WAY-05 and WAY-148 changed in place, already in `b2a52f6`.)
- **Invariants written or changed:** none. No rule of the task, a decision or the human calls for one.
- **Environment facts:** none. The change rests on no source outside the product.
- **Glossary terms:** none. The change uses "exclusion", "questions table", "check result" and "own-work check" in their plain sense; the glossary holds none of them.
- **Part-map changes:** none.
- **Projected entries:** none; the task carries none.
- **Rows written:** none in this step. Rows 1-3 of *Settlements to record* were written by the foundation step (WAY-293, WAY-05, WAY-148); the review of report 04 found the three met. No row was missed.

## Checks

| Command (from the worktree root) | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (output `0 errors`) | 0 |

Not run: the product's gate (the orchestrator ran it on this head: exit 0, 667 tests, per the handoff). No code changed in this step, so no further focused check.

## Reaches beyond this handoff

- Grep over `foundations/invariants.md`, `foundations/glossary.md`, `foundations/part_map.md` and `foundations/environment_facts.md` for the ten identifiers above, and over `task-cycle`, `project-level`, `elements` and `agent-instructions` for WAY-159, WAY-164 and WAY-260 — to see whether another file restates the repair rule. Read `task-cycle/skill/request_template.md:152-162` and `task-cycle/skill/SKILL.md:320-328` around the hits. Why: the return step compares the entries the search found with the code, and the handoff names no list.

## Searches not found or unclear

- The planner's return (`task-cycle/plan/SKILL.md:202-203`) against WAY-148's new clause: unclear whether the planner returns a check result. Same place as O1 of report 04 and as my report 02; I did not change it (not mine to fix, and the wording was approved with the task document).
- `task-cycle/test_request_check.py:60-62` still quotes the old first sentence of WAY-148 in a fixture task document; no test compares it with the log. Left as is, as in report 02.
