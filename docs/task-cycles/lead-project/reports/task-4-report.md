# Slice 4 implementation report

Status: DONE_WITH_CONCERNS only for expected deferred generated-wrapper gate failure.

## Authority, inputs and source selection

Worked in C:/Storage/repos/the-way-wt/lead-project on task/lead-project. BASE and source pin exercised: 74750b340769fe1c397adaff12ece77acc8350e7, independently approved Slice 3 containing project-level/lead/skill/SKILL.md. Read the complete borrowed task-4 brief, frozen task/spec, global and worktree agent instructions, integration guide, complete part map, installer/readme and existing installation tests, and lead skill. Used Superpowers 6.4.1 implementer-prompt, test-driven-development and its writing-good-tests reference. The initial reference lookup at skills/writing-good-tests.md did not exist; read the actual test-driven-development/writing-good-tests.md.

WAY-150 selection: complete current Scope fields in foundations/decisions.md were parsed for touched part installation; whole selected entries were WAY-09,27,34,38,89,107,120,127,141. Expanded linked decisions WAY-01,10,21,44,101 and explicitly governing WAY-150. Read installation-claude-guidance and glossary-process-terms invariants plus relevant every-part repository-file-location, outbound-link-reach, script-language/imports/subprocesses, skill-entry-points and Python declaration; selected tool-loading/import and Python facts by links. No foundation edit. No vault operation. No protected tests or generated wrappers changed.

Environment: Windows PowerShell, Python 3.14.3, Git 2.55.0.windows.3; Python standard library and real temporary Git repositories. Tests call the working installer with the source checkout committed HEAD, not the task's old starting commit. Clone/submodule source is the actual committed Slice 3 pin. Product repositories use test@example.invalid identity.

## Changes

- installation/install.py: add only lead-project -> project-level/lead/skill/SKILL.md to installed skills. Existing generation supplies both identical tool wrappers, sibling routing and shared product inventory; no installer protocol or ownership change.
- installation/README.md: add lead-project to actual inventory and remove thirteen/twenty-four wrapper claims.
- installation/test_lead_installation.py: ordinary real CLI integration tests for preview/apply/repeat, exact pin and source path, byte-identical wrappers, sibling naming, fresh product clone then submodule initialization, product foundation/instruction preservation, conflict refusal for both tool directories, and refusal to move a differing gitlink. Existing invariant tests remain untouched.

## TDD evidence

RED command: python -B -m unittest discover -s installation -p test_lead_installation.py
Exit 1; 3 tests in 5.848s, FAILED (failures=4). Exact failures:
- test_preview_apply_repeat_exposes_lead_and_preserves_product: AssertionError: 'CREATE .claude/skills/the-way-lead-project/SKILL.md' not found in installer preview.
- test_clone_can_initialize_the_exact_lead_source: AssertionError: 128 != 0 : fatal: pathspec '.claude/skills/the-way-lead-project/SKILL.md' did not match any files.
- test_conflicting_lead_wrapper_refuses_before_writing, both directory subtests: AssertionError: 0 == 0 (installer wrongly accepted unowned conflicting lead wrapper).
These are absent installed lead behavior, not a broken fixture. Full raw output: task-4-red.txt beside this report (PowerShell redirected stderr includes its NativeCommandError presentation).

GREEN same command after minimal registry addition: exit 0; Ran 3 tests in 13.608s; OK. Raw output task-4-green.txt. Added pin-refusal coverage of deliberately unchanged existing behavior afterward; its final verification is in the installation suite below.

## Choices and costs

Registry addition reuses existing pinned wrapper generation. Leaving it absent prevents product sessions from reaching lead-project; implementing a separate generator or special guidance would duplicate protocol and broaden product writes. Cost of the chosen change is one inventory entry and ordinary tests. Documentation lists inventory without numeric totals so future skills do not leave multiple stale counts; leaving counts needs coordinated manual edits on every addition. Tests use real committed source and fresh clones rather than mocked install internals, costing seconds per scenario while observing the actual pin and preservation behavior. No new product-writing semantics or maintain-instruction-files installation introduced.

## Self-review

Read the three changed files/new test and checked git diff --check (exit 0, no output). Changes are limited to allowed paths. Existing LF/CRLF content preserved by byte edits. The production diff is one registry line; all expected wrapper text is asserted at installer output/product-file boundaries, not by reading the registry. Mental mutations caught: omitted lead registration, one missing wrapper, wrong pin/source path, absent sibling name, overwrite of foundation/CLAUDE, changed AGENTS/gitignore prefix, non-idempotent repeat and accepted wrapper/pin mismatch.

## Final verification

python -B gate/run_tests.py installation: exit 0; Ran 30 tests in 121.735s; OK. All four new ordinary tests included. Full output task-4-installation.txt beside report.

python -B gate/run_tests.py gate: exit 1; Ran 98 tests in 18.851s; FAILED (failures=1).
Exact failure: test_every_skill_reaches_a_session_on_the_way (test_skills_reach_the_way_sessions.SkillsReachTheWaySessions.test_every_skill_reaches_a_session_on_the_way). Reports missing .claude and .agents the-way-lead-project wrappers plus stale sibling lists in existing wrappers (16 findings). This is expected until Slice 7 regeneration. Full output task-4-gate.txt beside report. No suppression or protected correction attempted.

## Limits and concerns

The gate failure remains explicit for root/Slice 7. No full gate pass claimed. Semantic operation of the lead skill itself is outside this installer slice. Tests verify fresh installation; existing products still need their separate pin-move task and removal of old wrappers/guidance per existing installer documentation. No global skills, external product files, foundation or generated wrapper edits. Root owns review and any questions.

## Commit

9c471a2 feat: expose project leading in product installations
Explicitly staged only the three allowed installation paths. No amend, merge or push.
