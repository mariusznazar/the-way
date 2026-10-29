PASS 90e826a63b07ce029d7aefad907a3730a6eb26fa

# Whole-change review

Reviewed the entire committed range `76cbe0ea4e766eb9561052355e370d6424c1d32f..90e826a63b07ce029d7aefad907a3730a6eb26fa`, including the full diff and log. HEAD matched the dispatched commit. The range contains one commit and changes only `task-cycle/plan/SKILL.md` (9 additions, 9 deletions). I made none of the reviewed change and changed no tracked product file during review.

## Findings

- Critical: none.
- Important: none.
- Minor: none.
- Out of scope: none.

## Requirement coverage and manual checks

| Requirement or scenario | Evidence and result |
|---|---|
| To do 1 / Q1: include projected entries the task carries, whole or the part made true, including an entry assigned elsewhere | `task-cycle/plan/SKILL.md:105` now starts the table rule with the projected entries the task carries; the following line explicitly covers assignment to another task. A source-only task carrying a two-part projected decision, whose code realizes only its first part while the plan assigns writing the entry elsewhere, must now list that first part. This agrees with WAY-126 and the task's narrowed Q1. |
| Include every entry assigned by the task's plan item | `task-cycle/plan/SKILL.md:106` retains this as a separate inclusion rule. An assigned entry still belongs in the table even when the task's code does not make it true. This matches the assigned-task case in WAY-126. |
| Preserve settlements and spec entries | `task-cycle/plan/SKILL.md:107` retains each settlement row by row number and each entry the spec names. The task itself carries no settlement rows or projected entries to write; its three Decisions in play are existing rules, not new entries. |
| To do 2: remove the premature part-map example | The complete committed diff removes the example from Foundation entries. The instruction at `task-cycle/plan/SKILL.md:117` places the necessary map change with the slice adding the file. |
| New file in a later slice | For a new tracked file requiring a new map pattern in slice 3, the revised Change instruction puts the map change in slice 3 as well. It does not direct the planner to create a pattern before the file exists. The real check rejects both the premature pattern and the unassigned tracked file (`elements/common/foundation_check.py:550` and `elements/common/foundation_check.py:560`); focused tests below confirm both sides. |
| Preserve the plan-member boundary | An entry neither carried by the task nor assigned by its item does not enter the table through the revised projected-entry clause. `task-cycle/skill/foundation_step.md:15` remains unchanged and continues to return a plan member to its project plan when another item's entry would be written. This is the task's explicit exclusion, not an unimplemented requirement. |
| No additional approval, wording, or implementation responsibility | The table still names entries rather than wording them, retains invariant checks, and leaves slice implementation to its executor. No new foundation meaning is introduced. |

The author's weakest-requirement check addresses the actual risk: losing the partial entry because a different task is named as its writer. Its three reported scenarios are relevant and agree with the final text. I independently checked those scenarios and additionally checked the boundary for entries the task does not carry. No permanent wording test is needed for this prose correction; the existing checker tests give executable evidence for the file/map constraint rather than pretending to test an agent's interpretation of prose.

The touched part is `task-cycle`. Its part-map entry names no trust boundary, and this change performs no irreversible operation. No UI, executable code, tests, invariant tests, foundation entries, skill description, skill name, or skill path changes. The existing entry points therefore need no regeneration. The selected guidelines are empty under the task's Q2 and the repository's current integration route. The reached review-method invariants are unaffected by this prose change; the return-step and integration work remaining after this review belongs to the orchestrator's route.

## Declined to judge

None. No encountered behavior was set aside as an out-of-scope finding.

## Executed checks

Commands below ran in `C:/Storage/repos/the-way-plan-partial-foundation` unless a different directory is stated.

- `git rev-parse HEAD` — exit 0; returned `90e826a63b07ce029d7aefad907a3730a6eb26fa`.
- `git -C .agents/skills/the-way-review-change rev-parse --show-superproject-working-tree` — exit 0; empty output.
- `git ls-files --stage -- ':/.the-way'` — exit 0; empty output. The two entry-point checks confirm this is the-way itself, not a product using its submodule.
- `git log --oneline 76cbe0ea4e766eb9561052355e370d6424c1d32f..HEAD` — exit 0; one commit, `90e826a`.
- `git diff 76cbe0ea4e766eb9561052355e370d6424c1d32f HEAD --` — exit 0; read the full diff.
- `git diff --numstat 76cbe0ea4e766eb9561052355e370d6424c1d32f..HEAD` — exit 0; one changed file, 9 additions and 9 deletions.
- `git diff --check 76cbe0ea4e766eb9561052355e370d6424c1d32f..90e826a63b07ce029d7aefad907a3730a6eb26fa` — exit 0.
- In `elements/common`: `python -B -m unittest test_foundation_check.FoundationCheckTest.test_good_product_passes test_foundation_check.FoundationCheckTest.test_pattern_of_the_map_matching_no_file test_foundation_check.FoundationCheckTest.test_file_no_part_claims` — exit 0; 3 tests passed. The tests create their own temporary repositories, leaving the reviewed tree and index unchanged. The valid-product case is the positive control; the other cases assert the check fails for a map pattern matching no tracked file and a tracked file with no part.
- `git status --short` — exit 0; clean tracked worktree before writing this ignored report.

The full gate was deliberately not run: the dispatch and WAY-160 reserve it to the orchestrator after review. There were no failed or unavailable focused checks. The manual checks above establish the changed instruction's meaning; the executable tests establish the existing checker behavior, not autonomous planner compliance.

## Reaches

Beyond the dispatched task, report, changed skill and the foundation/guideline selection required for a whole-change review:

- `task-cycle/skill/foundation_step.md`, whole — checked how the table's output is consumed and confirmed the unchanged plan-member restriction.
- `project-level/plan/template.md`, Projected entries section — checked the distinction between tasks realizing an entry and the one assigned to write it, and the requirement that each realizing task carries the entry in its document.
- `elements/common/foundation_check.py`, `check_files` — checked the actual file/map validation that motivates To do 2.
- `elements/common/test_foundation_check.py`, temporary-product helper and the three focused test methods — verified that the chosen tests check the real script with positive and negative cases and do not mutate this worktree.
- WAY-114, WAY-118 and WAY-146, each whole — followed links needed to understand approved projected wording, partial-entry acceptance and project assignment.
- Environment facts `git-path-patterns`, `single-rule-compliance` and `instruction-density-accuracy`, each whole — followed the relevant grounding of file assignment and the skill-fragment placement rule.

## Searches not found or unclear

None. An initial local extraction assumed decision headings used `##` rather than `###`; its overbroad output exposed the mistake, and it was corrected before using the independently selected entries. Truncated reading batches were reread in smaller selections; no truncated passage was treated as evidence of absence.
