# Fix report — whole-change review findings

**Status:** done with concerns
**Commit:** `8f26dd665897d56da1b50cd83514484035aec0c4`
**Return:** before review of the fix; the full gate remains with `/root`.

## Blocking findings

**R1 — fixed.** The readiness-gate instruction now sits in common step-1 source reading at
`project-level/task/skill/read_sources.md:12-16`. Both project-plan and source-only routes pass
through that file before relying on an approved definition. A missing gate finding returns to
`define-project`. I removed the duplicate from `source_only_task.md`; plan members now receive the
same check, while `plan_check.py` remains the separate plan consistency check.

**R2 — fixed.** I reassessed all skill fragments by their actual step/variant trigger and moved
multi-instruction procedures out of the main file. Step 2 drafting, step 3 gap resolution (including
Human actions and deployment checks), step 4 decision handling, step 5 candidate search and step 6
final review now have named files and pointers. The main skill keeps its shared route, cross-step
rules and the one-instruction exclusion rule. The full fragment-by-fragment assessment and refreshed
counts are at `reports/assessment.md`. The prior Minor M3 remains unchanged in the review record;
the newly required step-6 procedure move overlaps its observation but does not make a separate fix
to that report-only finding.

**R3 — fixed.** `installation/test_install.py` now derives its tested names from all entries in
`install.SKILLS`, and asserts the complete required sentence including the actual skill path. It
still rejects the old blanket-read wording. The focused installer test passed with all 20 generated
skills in its loop.

## Files changed

| File | Added | Removed |
|---|---:|---:|
| `installation/test_install.py` | 5 | 20 |
| `project-level/task/skill/SKILL.md` | 17 | 122 |
| `project-level/task/skill/carry_foundation.md` | 15 | 0 |
| `project-level/task/skill/draft.md` | 23 | 0 |
| `project-level/task/skill/final_review.md` | 26 | 0 |
| `project-level/task/skill/find_settlements.md` | 22 | 0 |
| `project-level/task/skill/read_sources.md` | 31 | 0 |
| `project-level/task/skill/resolve_gaps.md` | 34 | 0 |
| `project-level/task/skill/source_only_task.md` | 1 | 4 |
| **Total** | **174** | **146** |

## Checks

- `python -B -m unittest installation.test_install.InstallTest.test_preview_apply_rerun_and_preserve_foundation` — exit 0; one test passed, and its generated-entrypoint loop checks all 20 installed skills.
- `python -B agent-instructions/skill_entry_points.py` — exit 0; entry points current.
- `python -B instruction-files/check_instructions.py .` — exit 0; 0 errors, 1 existing dead-path warning for the private `_zadania\` path, 3 info lines.
- `python -B -c "from pathlib import Path; import re; p=Path('project-level/task/skill/SKILL.md'); links=re.findall(r'\]\(([^)]+\.md)\)',p.read_text(encoding='utf-8')); missing=[x for x in links if not (p.parent/x).is_file()]; assert not missing, missing; print('skill_links',len(links),'missing',len(missing))"` — exit 0; 10 Markdown targets, none missing.
- `git diff --cached --check` — exit 0.
- Word counts used Python UTF-8 `str.split()` with this command — exit 0:

  ```powershell
  python -B -c "from pathlib import Path; base=Path('project-level/task/skill'); names=['SKILL.md','read_sources.md','draft.md','resolve_gaps.md','carry_foundation.md','find_settlements.md','final_review.md']; counts={n:len((base/n).read_text(encoding='utf-8').split()) for n in names}; extras={n:len((base/n).read_text(encoding='utf-8').split()) for n in ['project_plan_task.md','source_only_task.md','orchestrated_mode.md','guideline_findings.md']}; print('core',counts); core=sum(counts.values()); print('core_total',core); print('manual_plan',core+extras['project_plan_task.md']); print('orchestrated_plan',core+extras['project_plan_task.md']+extras['orchestrated_mode.md']); print('source_only',core+extras['source_only_task.md']); print('guideline_add',extras['guideline_findings.md']); print('template',len(Path('project-level/task/template.md').read_text(encoding='utf-8').split()))"
  ```
- `python -B .runs/task-cycles/refine-task-skill-shape/reports/reviewer_probes.py` — exit 1 at its stale assertion that `lead-project`, `maintain-styleguide`, and `maintain-testing-guidelines` remain missing. Its output instead reports installer skills 20, assertion loop 20, and no unchecked names. This probe was written to demonstrate the pre-fix defect; the changed focused test is the passing post-fix check.
- The exact focused-test command was `python -B -m unittest installation.test_install.InstallTest.test_preview_apply_rerun_and_preserve_foundation` for both earlier attempts and the passing run above. Attempt 1 exited 1 with a SyntaxError where the rewritten `NAMES` assignment and `BLOCK` assignment had joined; attempt 2 exited 1 with a SyntaxError where the sentence assertion and old-wording assertion had joined. Both failures were in the temporarily malformed test source; after correcting those line joins, the identical command exited 0.
- The full task-cycle gate was not run because the fix handoff assigns it to `/root` after review. The base gate passed before this fix; plan/readiness implementation files were not changed.

## Weakest-point check

The likeliest miss was leaving a multi-action procedure loaded from the main skill before its step,
especially final review or Human actions. I compared the reviewed source at
`9f9001cf51812cdcfbbc16b12c819571e1769454:project-level/task/skill/SKILL.md` with each destination
and checked the resulting main file under WAY-256/257: each numbered step points to its detailed
file, the shared acceptance and document-scope rules stay in the main route, and the one-instruction
exclusion rule stays beside its step-4 pointer. The full assessment records every retained or moved
fragment and when it is needed. The command `git show 9f9001cf51812cdcfbbc16b12c819571e1769454:project-level/task/skill/SKILL.md` — exit 0 — supplied the source while I matched each original paragraph to its destination. The direct link check above confirms every pointer resolves; that check does not substitute for the criterion judgment.

## Reaches beyond the handoff

- Read the full `instruction-files/judging.md` and `instruction-files/kind_skill.md` for the required
  fragment criterion and one-instruction exception.
- Read `project-level/plan_check.py`, `project-level/readiness_check.py` and
  `project-level/test_plan_check.py` to verify the distinct checks named by R1. The retained probe
  uses valid controls and shows a missing approver yields zero plan findings but one readiness
  finding.
- Read `task-cycle/skill/foundation_step.md` whole to compare step-5 search scope with what the
  cycle later searches before writing foundation entries.
- Read the relevant place-only `project-level/task/template.md` only to preserve its role as the
  task document's form source; its content was not judged or changed.
- Read WAY-259 whole for the installed-entry-point rule and its rationale; its Polish meaning
  sentence is in the assessment. The selected foundation entries were already read whole during
  the original author step and are retained in `author-handoff.md`.

## Autonomous choices

- I used one adjacent file per common workflow step so the route remains legible and each detailed
  procedure loads at its trigger. A larger shared “procedures” file would cost fewer files but
  would again load later steps' procedures together.
- I put the approval-gate command in common step-1 reading because both project relations use an
  approved definition. Keeping it only in `source_only_task.md` caused R1; copying it into two
  variant files would duplicate the rule and risk drift.
- The tested skill population is derived from `install.SKILLS`, so a future installed skill joins
  the exact-sentence assertion automatically. A fixed list would preserve the known omission risk.

## Questions / concerns

No question remains for the orchestrator. The retained reviewer probe exits 1 because its expected
pre-fix gap is now absent; the focused post-fix test passes. The full gate has not been run here and
remains for `/root` after review.

## Path correction

An initial file-add attempt named
`C:/Storage/repos/the-way-refine-task-shape/project-level/task/skill/find_settlements.md`, missing
`-skill` from the worktree name. The correct file is
`C:/Storage/repos/the-way-refine-task-skill-shape/project-level/task/skill/find_settlements.md`.
The patch that replaced it removed the wrong-path artifact; a later `Resolve-Path` check returned
exit 1 for `Resolve-Path 'C:/Storage/repos/the-way-refine-task-shape/project-level/task/skill/find_settlements.md'` because that file no longer existed. All tracked edits and the commit below are in the intended worktree.

## Commit

`8f26dd665897d56da1b50cd83514484035aec0c4` (`fix: restore project readiness and step-level guidance`).
