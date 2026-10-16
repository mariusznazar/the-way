# Plan -- One author for a change one agent can hold

- Task: .runs/task-cycles/one-author-small-change/task.md
- Spec: none
- Base: dc433059ffc7f94f9aaa43588dfe94ac869fb635

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| WAY-136/1: one author makes foundation entries, code and return step; separate review, assessment and invariant authors remain | decision revision | Settlement row 1; To do 1, 2, 6 | Slice 1 |
| WAY-136/1: orchestrator selects from task in step 4; discard an oversized author's whole attempt, foundation entries included, then plan | decision revision | Settlement row 2; To do 1, 3 | Slice 1 |
| WAY-135/1 and WAY-136/1: selection also follows a reviewed spec, using the same size judgment | decision revisions | Settlement row 3; To do 4, 7 | Slice 1 |
| WAY-136/1: whole-change review covers task, settlement rows, projected entries and foundation-before-dependent-code order | decision revision | Settlement row 4; To do 5 | Slice 1 |
| WAY-135/1 and WAY-136/1: review conditions without token counts | decision field revisions | Settlement row 5; To do 8 | Slice 1 |
| WAY-13/1: align only verification example and rationale with no-plan preparation | decision consistency revision, binding sentences unchanged | Consequence of rows 1-2; foundation search; orchestrator ruling | Slice 1 |
| WAY-30/1: known decision revision has an accepted carrier when no task plan exists | decision carrier consistency revision | Consequence of row 1; foundation search; orchestrator ruling | Slice 1 |
| WAY-36/1: temporary choices have a cycle-record carrier when no task plan exists | decision carrier consistency revision | Consequence of row 1; foundation search; orchestrator ruling | Slice 1 |

The current cycle remains on its base process: a separate foundation agent writes these entries
before the implementation slice. Use record-decision and required shared references; edit in place
before main, preserving human approval of known decision revisions and stopping for a newly found
contradiction under WAY-30. Do not interpret carrier changes as new approval authority.

Keep WAY-136's four required review triggers: five cycles under the revised rule; an oversized
one-author return in two cycles out of three; more than one slice out of three returned oversized;
check by 2026-11-30. WAY-135 keeps its non-token review conditions and date. Search every foundation
element for unlinked effects and incoming fingerprints; none for WAY-30/36/135/136 exists at the
base. WAY-13's binding part stays unchanged, so its dependents need no fingerprint refresh for
its example/rationale correction. Recheck this against the actual changes.

No projected entry is carried. No invariant sentence or check change is planned: the affected
route decisions currently use level-2 cycle assessment. Their workflows and authorship are not
proved by a string test over instructions. The foundation author must still attempt derivation
under WAY-12/22 and report a newly necessary invariant before dependent code: a separate agent
writes its sentence and another its check under WAY-69, with its method and acceptance evidence.
There is no map responsibility, file-assignment, glossary meaning or environment-fact change
identified by planning. Existing assignments already cover every changed file.

## Slices

### Slice 1 — Make the one-author route usable throughout the cycle

- **Goal:** A cycle can choose one author without a plan before implementation and after a spec;
  that author performs foundation work before dependent code and the return step, with the same
  independent checks, coverage review and fallback to planning if too large. The planned route,
  record, generated entry points and decision-writing instructions agree with that behavior.
- **Change:** `task-cycle/skill/SKILL.md` `task-cycle/plan/SKILL.md` `task-cycle/record_template.md` `task-cycle/slice_size.py` `elements/decisions/template.md` `elements/decisions/skill/SKILL.md` `.claude/skills/the-way-implement-task/SKILL.md` `.agents/skills/the-way-implement-task/SKILL.md` `.claude/skills/the-way-plan-task/SKILL.md` `.agents/skills/the-way-plan-task/SKILL.md`
- **Read:** `AGENTS.md` `agent-instructions/README.md` `.runs/task-cycles/one-author-small-change/task.md` `elements/common/way_of_working.md` `elements/common/rules.md` `elements/decisions/examples.md` `foundations/part_map.md` `foundations/decisions.md:6-1131` `foundations/decisions.md:1233-1383` `foundations/decisions.md:1428-1576` `foundations/decisions.md:1607-1649` `foundations/decisions.md:1697-1854` `foundations/decisions.md:1895-2127` `foundations/decisions.md:2320-2348` `foundations/decisions.md:2377-2537` `foundations/decisions.md:2606-2651` `foundations/decisions.md:2686-2942` `foundations/decisions.md:2992-3017` `foundations/decisions.md:3181-3245` `foundations/decisions.md:3277-3333` `foundations/decisions.md:3368-4244` `foundations/decisions.md:4284-4338` `foundations/decisions.md:4453-4489` `foundations/decisions.md:4576-4726` `foundations/invariants.md` `foundations/glossary.md` `foundations/environment_facts.md` `agent-instructions/skill_entry_points.py` `task-cycle/test_slice_size.py` `agent-instructions/test_skill_entry_points.py` `gate/test_skills_reach_the_way_sessions.py`
- **Checks:** Run `python -B agent-instructions/skill_entry_points.py --write`, then
  `python -B agent-instructions/skill_entry_points.py` (no remaining changes);
  `python -B gate/run_tests.py task-cycle`;
  `python -B gate/run_tests.py agent-instructions`;
  `python -B gate/run_tests.py elements/decisions`;
  `python -B gate/run_tests.py gate`;
  `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`;
  `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`;
  `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`;
  `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none`;
  `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none`;
  `git diff --check`. Record warnings and unchecked output. This is a prose/docstring change, with
  no new automated executable behavior to start with a failing test; keep existing parser behavior,
  numeric limits and CLI unchanged and do not add wording-mirroring tests. Independently walk the
  scenarios below against the final text and task. A real new-route pilot remains unchecked.
- **Depends on:** all Foundation entries above

The slice aligns the full implement-task skill, including its description, steps 4 and 6-11,
shared foundation requirements, error/oversize recovery, request contents and correction route.
Both execution routes share the record, gate, assessment and request steps; do not copy those into
a second workflow. Make plan-task describe when a planner is actually dispatched and the return
from an oversized whole attempt versus an oversized planned slice. Keep a plan for a change that
needs division; a plan which legitimately finishes with one useful slice retains its single
whole-change review. Update the record's route/rationale, optional plan artifacts, author identity,
review coverage and discarded-attempt evidence. Update slice_size's description to measure plans
that exist, never to select the no-plan route. Align both temporary-rule references in the decision
template and the corresponding stop in record-decision; leave project-definition exclusions as
project-definition exclusions. Generate only the four entry points listed, from the two changed
skill descriptions. Investigate and replan any additional changed files rather than omitting them
from the write set.

Scenario review: (1) small settled task with foundation entries and no spec; (2) no-plan task
writing an invariant, with distinct sentence/check/code authors and unchanged deliberate-break
order; (3) a reviewed spec that remains small, and one that grows beyond one author; (4) an author
returning oversized, whose whole attempt including its entries is discarded before planning;
(5) an open design choice discovered in execution or review correction, preserving the existing
report/discard/spec rule; (6) an oversized planned slice, preserving completed reviewed slices;
(7) independent whole-change review covering every task item, settlement and projected entry,
foundation chronology, and the unchanged gate/return/assessment duties; (8) blocked human action
and human-reserved contradiction authority remain unchanged. These are review cases, not a
claim that the new workflow has run.

## Independence and execution

One cohesive slice: the route, its record, its optional planner and its entry-point descriptions
must agree to be reviewable. Splitting them would leave contradictory instructions in intermediate
slices and repeat the same scenario review. There is no useful parallel slice work. Foundation
writing precedes implementation under this cycle's current process. Separately, adopted
Superpowers 6.4.1 subagent-driven-development forbids parallel implementation agents; the
orchestrator records its execution ruling before dispatch. The one slice gets one independent
whole-change code review under requesting-code-review, followed by fixes and affected review;
WAY-10's filtered foundation assessment remains separate.

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome: lower preparation/execution overhead for changes one agent can hold | WAY-136; Slice 1, shared one-author route |
| To do 1: one author, no plan, foundation/code/return step; step-4 selection | WAY-136, WAY-13/30/36 consequences; Slice 1 |
| To do 2: invariant sentence, check and code have different authors | WAY-136 retaining WAY-69; Slice 1 scenario 2 |
| To do 3: oversized author returns no code, whole attempt including entries discarded, then planner | WAY-136; Slice 1 scenario 4 |
| To do 4: route also follows a spec | WAY-135/136; Slice 1 scenario 3 |
| To do 5: independent whole-change review inherits plan-coverage/order duties | WAY-136; Slice 1 scenario 7 |
| To do 6: independent assessment, gate and return step retained | WAY-136 retaining WAY-10/11/13/69/149; Slice 1 scenarios 2, 7 |
| To do 7: WAY-135 consistent with selection after a spec | WAY-135; Slice 1 |
| To do 8: no token review conditions; all four stated WAY-136 conditions retained | WAY-135/136 foundation field revisions |
| To do 9: cycle skill, planner skill, record template and sizing description | Slice 1, with generated entry points |
| Settlement row 1 | WAY-136; Slice 1 |
| Settlement row 2 | WAY-136; Slice 1 |
| Settlement row 3 | WAY-135/136; Slice 1 |
| Settlement row 4 | WAY-136; Slice 1 |
| Settlement row 5 | WAY-135/136 |
| No carried project entries, no human actions, no carried design questions | Frozen task; no additional source assignment |
| Exclusions: orchestrator optimization, work outside the cycle, later stack task | No slice changes these |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| One cohesive prose slice after the current process's separate foundation step | Several slices dividing coupled instructions | At ten changed files, another necessary file requires replanning; splitting now would repeat reviews of incomplete route instructions |
| Preserve one common cycle with explicit execution selection and shared checks | Duplicate complete workflows | Shared branches need careful scenario review; duplicated steps would drift and cost more to maintain |
| Use task/cycle-record carriers where a task plan is absent, preserving human decision authority and temporary/permanent distinction | Keep obligatory plan wording or relax approval | A broader reading could accidentally grant authority; keep the carrier change narrow and review it independently |
| Keep slice_size's algorithm, limits and CLI; change only its description | Use the size script to select no-plan work | Judgment can be wrong, bounded by author discard; requiring a plan to measure would restore the overhead the task removes |
| Use existing tests/guards and semantic scenario review for instructions | Add assertions mirroring prose | Agent compliance and cost savings remain unmeasured until a real pilot; string tests would not establish them |
| Complete selected decision ranges at the base and conservative whole-file allowance for other foundation reads; receiving agent refreshes ranges by current IDs after the foundation step | Freeze base line ranges across foundation edits | Other whole-file allowances overestimate input; reusing ranges after foundation edits could omit moved entry tails |
