## Blocking findings

### R1. The definition check no longer reaches project-plan tasks

**Grade / scope / thread:** Important; in scope; new thread.

**Anchor:** `C:/Storage/repos/the-way-refine-task-skill-shape/project-level/task/skill/source_only_task.md:9`; routing at `project-level/task/skill/SKILL.md:33`, missing counterpart at `project_plan_task.md:7`.

**Do wklejenia:** Moving “Whenever an approved definition is used, run … readiness_check.py” into the source-only file removes this check from both manual and orchestrated plan-member refinement. `plan_check.py` does not perform the same validation: a definition with its `Approved by` line removed still passes the plan check. Keep the readiness-check instruction reachable before relying on a definition in both project relations.

**Dlaczego to zgłaszam:** The old source-only paragraph ended with an explicitly broader instruction: “Whenever an approved definition is used”. That instruction applied to plan members too. The new common step directs a plan member to `project_plan_task.md` and explicitly reserves `source_only_task.md` for tasks without plan membership; only the latter contains the readiness-check command and its return to `define-project`. The general final instruction to check approval does not preserve the required command or its timing before reliance on that approval.

This is a change of rule reach, even though its words survive in another file. I checked the possible counterargument that the plan check covers it: `plan_check.py:199–226` checks selected sections and fingerprints, whereas `readiness_check.check()` also checks the gate record. The scratch probe uses the repository's valid definition and plan fixtures as positive controls, removes only the `- Approved by:` line, and gets **0 plan findings but 1 readiness finding**. No source file was changed. The old command would report that malformed approval record; the revised plan-member route can miss it. Restore the common conditional instruction or put it on both applicable routes, preserving the `define-project` return. This directly violates the task's first acceptance criterion.

### R2. The assessment uses “all modes” and shortness instead of the required step criterion

**Grade / scope / thread:** Important; in scope; new thread.

**Anchor:** `C:/Storage/repos/the-way-refine-task-skill-shape/project-level/task/skill/SKILL.md:140`; also `SKILL.md:87`, and `.runs/task-cycles/refine-task-skill-shape/reports/assessment.md:43` and `:60`.

**Do wklejenia:** Several procedures needed at one step remain in `SKILL.md` because the assessment calls them common to all modes or short. For example, final review still says to show the draft, propose moves/removals, apply accepted moves and handle the no-move case; the Human-actions branch likewise contains several separate actions. Reassess the retained fragments by when in the workflow they are needed, moving multi-instruction step/variant procedures while preserving their meanings and retaining only the actual one-instruction exceptions.

**Dlaczego to zgłaszam:** The requested outcome is a skill whose main file gives the whole route, cross-step rules and pointers. It is not merely extraction of the most conspicuous variants. WAY-256 explicitly distinguishes being needed across steps from being needed at one step, and its exception is one instruction, not one paragraph or a short procedure. The task expressly requires judgment of the skill under that criterion, so the decision's grandfathering of unrelated untouched fragments does not exempt the fragments this assessment judges for the requested rebuild.

Concrete counterexamples are the final-review procedure at lines 140–142, read by every session at entry although used only when the draft is complete, and the Human-actions procedure at lines 87–92: identify effects, propose placement, obtain the human's placement, wait for unfinished actions and mark completion. The assessment itself identifies the latter's conditional step-3 trigger and calls it “a short conditional procedure”; that is the very case the single-instruction exception does not cover. Its step-6 checklist row explicitly calls the fragment a “multi-instruction checklist” while keeping the common part merely because every use eventually reaches step 6. There are similar shortness/all-modes justifications in the step-2 rows.

Consequently the stated rebuild is incomplete and agents still carry instructions for later steps from entry. No runtime compliance effect is claimed or measured: this is a demonstrable mismatch with the required shape. Revisit these Keep judgments, separate actual cross-step rules from step-only procedures, implement the resulting meaning-preserving moves, and regenerate the word counts. Grouping and exact filenames remain the author's choice; this finding does not demand one file per bullet or a word-count target.

### R3. The changed test checks neither all generated skills nor the complete required sentence

**Grade / scope / thread:** Important; in scope; new thread.

**Anchor:** `C:/Storage/repos/the-way-refine-task-skill-shape/installation/test_install.py:98`; loop at `:87`, population at `:21`.

**Do wklejenia:** These assertions run for 17 entries, while the installer generates 20: `lead-project`, `maintain-styleguide` and `maintain-testing-guidelines` never reach them. They also check only the deferred-reading clause, so replacing “in full and follow it” with “partially” still passes the path and wording assertions. Check the complete agreed sentence, including the skill path, for every installed skill and retain the rejection of the old wording.

**Dlaczego to zgłaszam:** To do 1 explicitly requires that the test check the new sentence in every skill entry point. The generator currently emits the correct full sentence; the defect is the promised regression protection. `installation.install.SKILLS` has 20 entries but `installation.test_install.NAMES` has only 17. The loop still ensures byte equality between Claude and Codex for its selected entries, which is useful, but it does not enlarge that population.

The scratch probe computes that population difference from the actual module values and executes the actual AST assertion statements at lines 97, 98 and 100 on generated output. The unchanged output passes. Replacing the first clause with `Read .the-way/<path> partially` while retaining the second clause also passes, although the exact required sentence no longer exists. Reinstating the old blanket-read wording fails, which is the positive control that the new check does protect that narrower regression. Use the exact literal sentence with the expected path and cover the complete installed population, rather than weakening the requirement to the clause that happened to change. This stays within the task's permitted Python test change.
