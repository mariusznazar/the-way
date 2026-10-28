FAIL 9f9001cf51812cdcfbbc16b12c819571e1769454

# Independent whole-change review

Reviewed `3aee7d958835cc19b95519f4d21b37538b78e3e1..9f9001cf51812cdcfbbc16b12c819571e1769454`, one commit, without editing tracked source, index or branch. No plan, spec or previously reviewed slices. Findings below belong to the single author change, not to a slice. Counts: **3 blocking Important, 3 Minor, 0 out-of-scope**. No Critical finding.

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

## Minor findings

### M1. The foundation's list of decisions governing entry points omits the new decision

**Grade / scope / thread:** Minor; in scope; new thread.

**Anchor:** `C:/Storage/repos/the-way-refine-task-skill-shape/foundations/decisions.md:2997` (WAY-128).

**Do wklejenia:** WAY-128 still says process skills and their entry points answer to WAY-35, WAY-127 and WAY-256, while this change adds WAY-259 for product entry points. Add the new reference to that routing sentence so a reader following it reaches the installation rule too.

**Dlaczego to zgłaszam:** This sentence directs a reader away from the general always-loaded-file rule toward the decisions that govern skills and entry points. After adding WAY-259, its enumeration is incomplete. The frozen task's Context explicitly identifies this dependency, so it was available to the foundation reconciliation. A reader arriving through WAY-128 can miss the product-specific rule, although a correct installation Scope selection still finds WAY-259; that independent route limits the consequence and is why I grade it Minor. The diff adds only WAY-259 to the log and leaves this sentence unchanged. This is a reference reconciliation, not a request to change WAY-127's meaning.

### M2. The assessment incorrectly says semantic proposals were unauthorized

**Grade / scope / thread:** Minor; in scope; new thread.

**Anchor:** `C:/Storage/repos/the-way-refine-task-skill-shape/.runs/task-cycles/refine-task-skill-shape/reports/assessment.md:120`.

**Do wklejenia:** The task prohibits applying semantic removals or rewordings, but explicitly allows their verdicts to appear in the request as proposals. Replace this exclusion with the actual scope of judgment and state whether any such proposal was warranted after considering it; do not describe proposal-making as unauthorized.

**Dlaczego to zgłaszam:** The last section currently says “No `remove` or semantic `reword` proposal: both would exceed the task's authorization”. To do 3 says those verdicts belong in the request as proposals. This misstates the user's delegation and makes the absence of proposals look like a scope constraint instead of a judgment. For example, a semantic contradiction found during the assessment could be proposed for later decision without changing source in this task. `instruction-files/judging.md` includes remove and reword among its available verdicts. Correct the boundary and reconsider any conclusion actually excluded on that basis. I do not require inventing a proposal: I found no independently demonstrated semantic removal/rewording that the task necessarily needed, so the inaccurate exclusion alone is Minor. R2 separately identifies the concrete deficient placement judgments.

### M3. The conditional word-count explanation omits the step-6 trigger

**Grade / scope / thread:** Minor; in scope; new thread.

**Anchor:** `C:/Storage/repos/the-way-refine-task-skill-shape/.runs/task-cycles/refine-task-skill-shape/reports/assessment.md:85`; corresponding routing at `project-level/task/skill/SKILL.md:152`.

**Do wklejenia:** The count explanation says `guideline_findings.md` is read only when the shared reading reports a finding, but step 6 also sends the agent there for a newly reached part. Include that trigger in the count assumptions, even when reading that part ultimately finds its guidelines complete.

**Dlaczego to zgłaszam:** The numbers themselves reproduce exactly. The issue is which sessions belong in each row: a session whose final scope reaches an uncovered part follows the step-6 pointer and reads the 453-word file before it knows whether the new part has a finding. Such a session can have no missing or malformed guidelines and still incur that cost. Stating the clean-path assumption as “no guideline finding” alone therefore understates that session by 453 words. Qualify the main table with neither the step-3 nor the step-6 branch being taken, and list both triggers for the conditional addition. This is a reporting correction, not a reason to remove the valid readiness route.

## Good

- The generator contains the exact agreed sentence, and its ownership markers, pin verification, initialization route and sibling-skill routing are unchanged.
- The orchestration variant preserves its read-before-work trigger, conversation ownership, source handling, no-child-agent rule, result vocabulary and human-only final Status ownership. The plan/source distinctions and guideline finding responses otherwise remain accessible with recognizable conditions.
- WAY-259 has the accepted installation scope, derives from WAY-256, uses a complies/violates pair and leaves WAY-127 unchanged. Its two binding sentences preserve the accepted settlement.

## Coverage of the frozen task

| Requirement | Judgment against the whole range |
|---|---|
| To do 1: exact generator wording | Met in `installation/install.py:135`; inspected the full function and actual generated output. |
| To do 1: README description | Met in `installation/README.md:57`; describes reading the source and each named file at its step. |
| To do 1: new sentence and no old wording for every skill | Not met as specified: R3. Current output is correct; promised test coverage is incomplete. |
| To do 1 / Settlements row 1: narrow new installation decision | Binding content, Scope, derivation and example pair met by WAY-259. Reference reconciliation has Minor M1. WAY-127 unchanged. |
| To do 2: judgment with the instruction-files skill, kind skill, and rebuild under WAY-256 | Assessment exists with fragment, trigger/recognition, verdict and ground columns. Its treatment of retained step-specific procedures fails the requested criterion: R2. Read the assessment against `judging.md`, `kind_skill.md` and WAY-256/257. |
| To do 3: assessment and counts ready for the request | Materials exist. Counts reproduce; reporting trigger needs M3. The judgment's authorization statement needs M2. The request itself has not been created at this review boundary. |
| Acceptance: no refinement rule disappears or changes meaning | Fails: R1 narrows the reach of the definition check. Compared the full baseline skill against the complete revised main file and four siblings, including context around every move. No other lost baseline rule established. |
| Acceptance: only the generator sentence and its test change in Python | Met: the Python diff has only those two files and only the sentence/assertions. |
| Carried question: task-template treatment | Accepted place-only interpretation respected: template unchanged, separately counted at 1,580 words. This review does not reopen the accepted scope. |
| Settled empty guideline selection | Honored for this narrow change under the frozen task and integration guide. No additional guideline prerequisite invented. No product UI is changed. |
| Process copy, no product pin/install, no external task effect | Worktree methods used. No product pin moved and no actual product installation or external action performed; installer tests use disposable temporary repositories. |

Manual mode routes were checked separately: independent uses the common file; plan-member uses the plan sibling; orchestrated plan-member reads its routing sibling before the common steps. The source-only route was also checked because it carries a moved baseline rule. Deferred triggers are recognizable from relation, dispatch, findings and final scope; R1 is a wrong allocation of a broadly scoped rule, not an unreadable trigger. R2 concerns placement before the correct step even where a rule remains reachable.

The author identified availability at the right step as the weakest requirement, but its own-work check followed Move rows and pointer existence. It did not catch a shared instruction grouped into a narrower variant (R1), and it accepted the assessment's Keep judgments without applying the step criterion (R2). Thus that check addresses the right risk but is insufficient to establish the claimed result.

## Checks and evidence

All commands below ran from `C:/Storage/repos/the-way-refine-task-skill-shape`. These were separate prose and code/test passes: first the task, assessment, baseline/current skill and foundation; then the generator, consumers, tests and scratch probes. No full gate was run by this reviewer.

| Command / method | Result |
|---|---|
| `git rev-parse HEAD` | Exit 0; exact dispatched head. |
| `git log --oneline 3aee7d9..9f9001c` | Exit 0; one commit, `9f9001c refactor: split refine-task variant instructions`. |
| `git diff 3aee7d958835cc19b95519f4d21b37538b78e3e1..9f9001cf51812cdcfbbc16b12c819571e1769454` | Exit 0; reviewed all nine changed paths. |
| `git diff --check 3aee7d9..9f9001c` | Exit 0. |
| `git diff --name-only 3aee7d9..9f9001c -- '*.py'` | Exit 0; only `installation/install.py` and `installation/test_install.py`. |
| `git diff --exit-code 3aee7d9..9f9001c -- project-level/task/template.md` | Exit 0; unchanged. |
| `python -B .runs/task-cycles/refine-task-skill-shape/reports/count_baseline.py` | Exit 0; 2,933 skill words, 1,580 template words. |
| `python -B .runs/task-cycles/refine-task-skill-shape/reports/count_variants.py` | Exit 0; 1,888 independent; 2,093 manual plan-member; 2,663 orchestrated plan-member; 453 conditional guideline words. Source-only: 2,074 plus conditional 453. |
| `python -B .runs/task-cycles/refine-task-skill-shape/reports/reviewer_probes.py` | Exit 0; valid fixture positive controls, missing-approver plan/readiness difference, 20-vs-17 skill population, incomplete-sentence mutation surviving the actual assertions, old wording rejected. |
| `python -B -m unittest installation.test_install.InstallTest.test_preview_apply_rerun_and_preserve_foundation installation.test_install.InstallTest.test_a_file_without_every_mark_of_an_entry_point_is_the_products installation.test_install.InstallTest.test_rejects_conflicting_integration_file_before_writing installation.test_install.InstallTest.test_rejects_symlink_at_claude_without_touching_target` | Exit 0; 4 tests, 90.749 seconds, no skips. |
| `python -B elements/common/foundation_check.py` | Exit 0; 0 errors. Structural validity does not detect M1's missing reference. |
| `rg -n 'WAY-259\|WAY-35, WAY-127 and WAY-256' foundations` | Exit 0; new decision and unchanged WAY-128 routing sentence identified, then whole entries read. |
| `git status --short` | Exit 0; no tracked changes. Review artifacts are ignored scratch files. |

The executable scratch probe is retained beside this report; it modifies no reviewed source or product. Its assertions use the repository's fixture definitions and actual changed test assertion AST, rather than a hand-waved assertion about coverage.

Trust-boundary pass: followed `plan()` generating wrappers, `owned_entry_point()`, parent checks and conflict rejection. The changed guidance does not participate in ownership recognition: the unchanged name, description suffix and pin marker do. Focused hostile-input tests covered forged/incomplete ownership marks, product-owned conflicting wrapper files for both agent directories and a symlinked root Claude file pointing outside the target; they passed and verified preservation of user files/target bytes. Preview/apply/rerun also passed. No changed executable branch at that boundary was found beyond constructing the guidance text.

Skill-directory file sets and their arithmetic are complete for the specifically declared no-branch paths, subject to M3's trigger correction and the changes required by R1/R2. They are not total session context counts: shared files, selected product foundation/guidelines and sources vary with a task; the unchanged task template is explicitly separate. No live agent refinement session was run, so source reachability and generated text are verified, not actual reading behavior or compliance rates.

## Reaches beyond the dispatch

- `instruction-files/SKILL.md`, `instruction-files/judging.md`, `instruction-files/kind_skill.md`: checked the method and criterion used by the requested assessment. This was verification of the author's assessment, not another independent skill-cleanup project.
- `project-level/task/template.md`: read to verify the moved instructions against the form they serve, confirm no alternative mandatory readiness command repairs R1 and check the separately reported cost; no content changes proposed.
- `project-level/plan_check.py`, `project-level/readiness_check.py`, `project-level/test_plan_check.py`: traced whether the remaining plan check preserves the lost readiness-check protection and used their existing fixtures for a discriminating probe.
- `elements/decisions/template.md`: checked WAY-259's form and verification against the rules for its element.
- Selected the touched parts' foundation independently by whole Scope/Part fields, including continuation lines, then read whole selected entries; expanded to WAY-33, WAY-35, WAY-128 and the placement/judgment decisions to check reconciliation and the assessment. The part map and glossary were read whole. Product guideline selection follows the explicitly accepted empty route.

## Declined to judge

None. The limits above describe checks not run and the scope of the evidence; they do not silently downgrade an identified out-of-scope defect.
