# Slice 1 implementation report

## Result and boundary

Implemented and committed the planned ten-file slice. The cycle instructions now select one author without a plan for a change one agent can hold, including after a reviewed spec, while retaining the shared foundation, independent review, gate, return and assessment requirements. The planned route remains available when division is needed. This executing cycle still follows its existing planned route.

- Worktree: `C:/Storage/repos/the-way-wt/one-author-small-change`
- Branch: `task/one-author-small-change`; no upstream configured.
- Executing cycle base: `dc433059ffc7f94f9aaa43588dfe94ac869fb635`.
- Implementation base, with the completed foundation step: `7513de82cb144f36e01b12eb8ef02970a382c2d9`.
- Implementation commit: `10e36ef9be8194471661265edeeacf728fe8dfb9` (`feat: execute small task changes with one author`).
- Author: `/root/executor`, Codex. Tracked working tree clean after commit; commit author email verified as the private repository address.
- Stopped before independent review, return step, assessment, push and request creation. No unresolved design or scope question found.

## Files

| File | Change |
|---|---|
| `task-cycle/skill/SKILL.md` | Route judgment before planning and after spec review; same author across foundation/code/return; separate invariant authors; distinct oversize/design-choice recovery; no-plan review coverage; shared checks and conditional request content |
| `task-cycle/plan/SKILL.md` | Planner dispatch is conditional; whole-attempt oversize and planned-slice oversize have different retained inputs; legitimate one-slice plans remain supported |
| `task-cycle/record_template.md` | Route and rationale, author continuity, invariant authors, optional plan artifacts, discarded attempts and whole-change coverage evidence |
| `task-cycle/slice_size.py` | Module description only: measures an existing plan and does not select the no-plan route |
| `elements/decisions/template.md` | Temporary rules and task exclusions use cycle-record choices where no plan exists |
| `elements/decisions/skill/SKILL.md` | Temporary-rule stop names the corresponding carrier |
| `.claude/skills/the-way-implement-task/SKILL.md` | Generated description |
| `.agents/skills/the-way-implement-task/SKILL.md` | Generated description |
| `.claude/skills/the-way-plan-task/SKILL.md` | Generated description |
| `.agents/skills/the-way-plan-task/SKILL.md` | Generated description |

The changed-file set equals the plan exactly. No foundation file, invariant test or ordinary test changed in this slice. After normalizing line endings as Git does, every byte after the sizing module's closing docstring equals the implementation base: parser, limits, CLI and executable behavior are unchanged. Existing line endings were preserved when scripting edits.

## Inputs and foundation selection

Read the frozen task and plan, handoff, foundation report, repository instructions, shared foundation-reading rules, affected decision-writing instructions and all named code/test inputs. Applied installed Superpowers 6.4.1 test-driven-development: the deliverable has no executable behavior change, so no artificial test asserting the new prose was added. Read the vault rulebook and skill conventions before editing skill files; no writes outside this worktree.

Refreshed decision selection against the current `Scope` fields at the implementation base for `decisions`, `task-cycle` and `agent-instructions`, rather than relying only on inherited line ranges. The 102 matching entries all fit the refreshed plan ranges; no selected entry was missing. Full IDs, versions, scopes and matching ranges are recorded in [implementation-selection.json](implementation-selection.json). Read the full invariant, glossary, environment-fact and part-map files, plus the violated-invariant register. Supplemented selection with the governing human-authority, recovery, invariant-authorship and source-fidelity entries and a whole-foundation search for route and plan dependencies.

The project-planning provisions found by that search govern project task breakdown, not a mandatory implementation plan for each task. No further write-set expansion was needed. This refresh supplies implementation inputs; it does not replace the orchestrator's later integration-tip reconciliation, return search or independent assessment.

## Verification

All commands below exited 0. Complete stdout and stderr, including every warning and unchecked item, are in the linked UTF-8 reports. Machine-readable command lists are [implementation-checks.json](implementation-checks.json) and [implementation-final-checks.json](implementation-final-checks.json).

| Command | Result and evidence |
|---|---|
| `python -B agent-instructions/skill_entry_points.py --write` | Exactly the four planned entry points regenerated; [output](implementation-generator-write.txt) |
| `python -B agent-instructions/skill_entry_points.py` | Current; [initial output](implementation-generator-check.txt), [final output](implementation-final-generator-check.txt) |
| `python -B gate/run_tests.py task-cycle` | 41 tests passed; [output](implementation-task-cycle-tests.txt) |
| `python -B gate/run_tests.py agent-instructions` | 18 tests passed; [output](implementation-agent-instructions-tests.txt) |
| `python -B gate/run_tests.py elements/decisions` | 169 tests passed; [output](implementation-decision-tests.txt) |
| `python -B gate/run_tests.py gate` | 98 tests passed, including both critical-flow test modules; [output](implementation-gate-tests.txt) |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 errors, 10 warnings, 5 unchecked; [output](implementation-decisions.txt) |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 errors, 0 warnings, 3 unchecked; [output](implementation-invariants.txt) |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 errors, 0 warnings, 7 unchecked; [output](implementation-part-map.txt) |
| `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none` | 0 errors, 0 warnings, 3 unchecked; [output](implementation-environment-facts.txt) |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 errors, 0 warnings, 5 unchecked; [output](implementation-glossary.txt) |
| `git diff --check` | Clean; [initial output](implementation-diff-check.txt), [final output](implementation-final-diff-check.txt) |
| `python -B task-cycle/slice_size.py .runs/task-cycles/one-author-small-change/plan.md` | Final: 10 files, 560725 characters, 224290 estimated tokens, fits; [initial output](implementation-size.txt), [final output](implementation-final-size.txt) |

Suites and guards ran after the substantive change. Subsequent edits only tightened author-continuity prose and line wrapping; final generator, diff and size checks ran after those edits. Final verification also asserts the exact ten-file set and unchanged executable suffix of the sizing script. No broader runtime gate result is claimed.

### Warnings and unchecked work

The decision warnings are the existing overdue check dates (2026-10-02) for WAY-03, WAY-21, WAY-52, WAY-55 and WAY-69, and approval placeholders awaiting the request link for WAY-13, WAY-30, WAY-36, WAY-135 and WAY-136. No foundation text was edited here.

The no-main guard invocation leaves historical/merge checks unchecked: decision versions, template-version coupling, TODOs, shared versions and relation fingerprints; invariant identifiers/versions/corrections/violation lists, TODOs and fingerprints; environment-fact identifiers/versions, fingerprints and unused facts; glossary Avoid counts, colliding names/IDs, changed-definition uses, TODOs and unused terms; part-map known violations, identifiers and lowered computed criticality. Full names and reasons are retained in each output. There is no human-verdict file; no human verdict is asserted. The-way's own glossary is not compared as a product glossary against a pinned the-way glossary.

Four further part-map checks remain unchecked: the part lists for `wording-reaches-dependants` and `skills-reach-the-way-sessions` because those tests leave no coverage file, promise-level change paths because no product command reports them, and dependency/new-or-stale-violation checks because no command reports the dependency graph. Passing the critical-flow test modules does not claim these separate coverage checks passed.

A real one-author workflow pilot, agent compliance and saved effort remain unmeasured. No invariant sentence/check changed, so no new deliberate-break acceptance evidence is produced by this slice. Independent whole-change review, shared final gate duties, return work, integration-tip reconciliation, independent assessment and request approval remain for later stages of this cycle.

## Author scenario walkthrough

This is the implementer's semantic walkthrough of the final instructions against the task, not independent review and not evidence of executing the new workflow.

| Case | Final instruction path and result |
|---|---|
| 1. Small settled task, entries, no spec | Step 4 chooses one author directly from the task without a preliminary plan or size script. The shared foundation step takes entries from task/sources/spec and writes them before dependent code. The same author makes code and resumes for return. Covered. |
| 2. No-plan task needs an invariant | Shared foundation instructions pause the author, dispatch distinct sentence and check authors, then resume the code author; the same separation applies during return. Step 10 retains existing deliberate-break order and step 11 retains final-check review/assessment/break/restore/clean-verification order. Covered. |
| 3. Reviewed spec, small or large | Step 7 repeats step 4's judgment using the task in light of the reviewed spec, even across several parts. Small goes to one author; work needing division goes to the planner. An earlier plan no longer binds. Covered. |
| 4. One-author attempt oversized | Dedicated recovery paragraph requires report without code/diff, records historical last commit/files, discards the entire attempt including entries back to its base, and sends task/spec/report to planning. The record distinguishes this from an open choice and a planned-slice return. Covered. |
| 5. New design choice during implementation or correction | Existing report-without-code/diff recovery discards the attempt including entries, starts a fresh spec author, then repeats route selection after independent spec review. The correction section records its reset base and reuses this rule. A method choice remains the executor's recorded choice. Covered. |
| 6. Planned slice oversized | Only the current slice resets to its start; earlier completed and reviewed slices stay. The planner receives its report and plan, splits the slice and reruns sizing. This is distinct from discarding a whole one-author attempt. Covered. |
| 7. Independent whole-change review and shared duties | No-plan review explicitly checks every task item, settlement row, carried projected entry, source fidelity and entry-before-dependent-code order against commits. The reviewer did not make the work. Gate, return, assessment and request steps stay shared. Covered. |
| 8. Blocked human action and reserved contradiction authority | Step 4 still stages permitted repository work and opens a blocked draft for required human actions or unlisted external effects. The shared foundation step retains human resolution of contradictions and unspecified settlement values; new carriers do not authorize a different meaning. Covered. |
| Planned one-slice route | Conditional planning may legitimately produce one slice. It retains plan review, one independent whole-change code review and the existing fixes/affected-checks/fix-range-review sequence. Covered. |
| Planned multiple-slice route | Plan order, fresh executors, subagent-driven-development's task and quality reviews, execution ruling and final whole-change review remain. No parallel implementation introduced. Covered. |
| Review corrections | The original task branch/worktree, merge-not-rebase target refresh, affected-stage reruns, conditional assessment and record pair remain. Route is retained unless the existing new-choice or oversize recovery applies. Covered. |
| Record and decision carriers | A no-plan cycle records route/reason, same author, invariant authors, review coverage and choices; it does not claim plan artifacts or slices. Temporary rules/task exclusions use its choices table while product decisions and project-definition exclusions retain their existing scope. Covered. |

## Implementation choices

| Choice and evidence | Alternative rejected | Cost if wrong |
|---|---|---|
| Keep one shared foundation/gate/return/assessment/request sequence with route-specific author selection, as required by the plan and WAY-136 | Duplicate a complete small-task workflow | Branch points require scenario review; duplication would create two versions of independent-check and human-authority rules to maintain |
| Preserve author identity across foundation/code/return, explicitly pausing for the two invariant authors; retain the pre-existing harness fallback specifically for review fixes | Generic author replacement between stages | A harness unable to resume an author cannot claim normal one-author execution; silently allowing replacement would weaken the settled authorship rule |
| Use cycle-record choices only as the absent plan's temporary-rule/task-exclusion carrier | Require a stub plan, or treat these as product decisions | Carrier wording could be read too broadly; the stop still tests whether the rule survives the work, and human contradiction authority remains unchanged |
| Keep sizing behavior intact and clarify only its module description | Use sizing as a preliminary route gate | Initial size judgment may be wrong, but the whole-attempt discard/planner fallback bounds that error; preliminary planning would restore the preparation cost the task removes |
| Existing behavioral tests/guards plus semantic walkthrough for prose | Add tests that match the newly written sentences | Instruction compliance and effort remain unproved until a real pilot; mirrored wording assertions would not prove either |

No full source-file or diff copies are archived in these reports; the exact commit range identifies the implementation. Temporary editing/check helpers remain outside `reports/` and are not evidence for archival.
