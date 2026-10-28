# `refine-task` skill placement assessment

Review target: the skill directory under `project-level/task/skill/`, compared with its state at
base `3aee7d958835cc19b95519f4d21b37538b78e3e1` and the corrected state at the fix head. The task
template is judged for placement only; its contents remain outside this assessment.

## Check and evidence

`python -B instruction-files/check_instructions.py .` — exit 0, 0 errors, 1 warning, 3 info lines.
The warning is the repository's private `_zadania\` backlog path absent from this checkout. The
info lines give sizes for `AGENTS.md`, `CLAUDE.md` and `agent-instructions/README.md`; this check
does not inspect the body of the invoked skill. The root `CLAUDE.md` imports `AGENTS.md`; no
repository override or competing root instruction was found.

The changed skill wording carries the exact WAY-259 meaning: **„Wpis skilla w produkcie każe
przeczytać wskazany skill w całości, a plik nazwany przez skill — dopiero wtedy, gdy nadejdzie
krok lub wariant, który go wskazuje.”** WAY-259 requires the full skill first and each named file
at its triggering step or variant. That places step-only material out of the entry-point load and
costs the agent one later recognition/opening at the named step.

The targeted transcript search already recorded in `assessment-before-fix.md` was for an actual
`the-way-refine-task` invocation/read, not a tool inventory mention; it returned no matching
record. No broad transcript load or new behavior claim was made for this fix. The prior repository
review record and the R1/R3 probe remain the evidence for their respective findings. No personal
data or secrets are included.

## Judgment method

Each row below is one paragraph or bounded fragment in the resulting skill directory. The criterion
is when an agent needs it and whether the point is recognizable when it comes (WAY-256/257). A
fragment needed only at one step or in one variant belongs beside the skill and is named by that
step; the one-instruction exception stays in `SKILL.md`. Cross-step rules and the route stay in the
main file. Grounds are the carried workflow and foundation decisions; the targeted transcript
search found no matching invocation, so absence is not treated as evidence of correct behavior.

| Fragment | When needed; recognizable? | Verdict and reason | Ground |
|---|---|---|---|
| `SKILL.md:8-14` — “Turn one proposed task into a document…” and location/prefix rules | Every invocation; yes, entry and product/worktree distinction are explicit. | **Keep** as purpose, shared sources and skill identity. | WAY-34, WAY-35, WAY-127. |
| `SKILL.md:18-20` — orchestrated dispatch pointer | The dispatch condition is known at entry; yes. | **Keep** the variant pointer; the detailed round procedure stays in `orchestrated_mode.md`. | WAY-134, WAY-154/155. |
| `SKILL.md:22-25` — both-mode acceptance and task document's what/why boundary | Every route; yes, both rules govern the whole work. | **Keep** as cross-step rules. | WAY-114/124 and the cycle record's distinct role. |
| `SKILL.md:27-32` — step 1 route to source-reading and task-relation files | Step 1; yes, numbered step and task relation make the moment explicit. | **Keep** the route; the source-reading procedure is beside the skill. | WAY-150 and WAY-256. |
| `read_sources.md:3-16` — read template/foundation, classify relation, use plan/source-only routes, readiness check | Step 1; yes. | **Move/keep beside skill** as a multi-instruction source-selection procedure. The readiness check is common to both project relations and precedes reliance on approval. | WAY-150; R1 probe shows `plan_check.py` alone misses a missing approver. |
| `read_sources.md:18-27` — backlog location, one-task boundary, product files and guideline reading | Step 1; yes. | **Move/keep beside skill**; these are several intake actions used only at this step. | WAY-107, WAY-124, WAY-214/215. |
| `SKILL.md:34-36` and `draft.md:3-4` — drafting pointer and title/wording | Step 2; yes. | **Keep** the pointer; **move** the title rule with its preservation and structure actions as a step-only fragment. | WAY-109/114; step 2 is explicit. |
| `draft.md:6-9` — create/update, TODO/status, path, frozen-cycle scope | Step 2; yes. | **Keep beside skill**; the paragraph contains multiple actions and a branch used only while drafting. | WAY-124, WAY-154. |
| `draft.md:11-15` — resume accepted pre-cycle task text and retain settled rows | Step 2, when resuming such a document; yes, condition is explicit. | **Keep beside skill** as a conditional multi-part procedure. | WAY-124. |
| `draft.md:17-19` — Description/Context and acceptance-criteria guidance | Step 2; yes. | **Keep beside skill**; several drafting instructions. | Task-template form and WAY-109/114. |
| `draft.md:21-23` — show whole document for wording and keep unsupported proposals outside | Step 2, at a wording decision; yes. | **Keep beside skill** as a conditional, two-part procedure. | WAY-113/114. |
| `SKILL.md:38-42` and `resolve_gaps.md:3-6` — gap-resolution pointer and ask/update/source-quote sequence | Step 3; yes. | **Keep** the pointer; **move** the multi-action question procedure. | WAY-109, WAY-113, WAY-150. |
| `resolve_gaps.md:8-10` — show conflicts and route upstream changes | Step 3, when answers conflict; yes. | **Keep beside skill** as a conditional multi-action rule. | WAY-30/114. |
| `resolve_gaps.md:12-16` — known choices, cycle boundary, waiting status and cycle record | Step 3; yes. | **Keep beside skill**; distinct state and routing actions are step-only. | WAY-124 and cycle records. |
| `resolve_gaps.md:18-21` — reconcile relation-specific questions and retain implementation questions | Step 3 for plan/source-only tasks; yes, both relations are named. | **Keep beside skill**; several actions conditioned on the task relation. | WAY-145, WAY-154. |
| `resolve_gaps.md:23-27` — Human-actions identification, placement, waiting and completion | Step 3, when the task has an external effect; yes, trigger and status are explicit. | **Keep beside skill**; this multi-instruction conditional procedure is not the one-instruction exception (R2). | WAY-140/124. |
| `resolve_gaps.md:30-35` — deployment-skill coverage and missing-work route | Step 3, only for deployment/runtime outcomes; yes. | **Keep beside skill**; coverage check and task-split route are multiple instructions. | WAY-139. |
| `SKILL.md:44-46` and `carry_foundation.md:3-7` — step 4 pointer and carry current/projected decisions | Step 4; yes. | **Keep** the pointer; **move** the multi-part selection and quotation procedure. | WAY-124/126/150. |
| `carry_foundation.md:9-11` — compare plan work/dependencies/entries | Step 4 for a plan member; yes. | **Keep beside skill** as a variant-specific multi-part check. | WAY-142/145. |
| `carry_foundation.md:13-16` — expose decision conflicts and obtain human choice | Step 4, if a conflict occurs; yes. | **Keep beside skill**; conflict presentation and choice are separate actions. | WAY-114/116. |
| `SKILL.md:46-48` — surviving exclusion as a decision candidate | Step 4, only if an exclusion survives and later work builds on it; yes. | **Keep in the main skill** as the one-instruction exception at the pointer's position. | WAY-26/256. |
| `SKILL.md:50-52` and `find_settlements.md:3-9` — step 5 pointer and task-mode candidate search | Step 5; yes. | **Keep** the pointer; **move** the detailed caller/source/reader/mode procedure. | WAY-33/134. |
| `find_settlements.md:11-14` — limit refinement search and rely on cycle's full search | Step 5; yes. | **Keep beside skill**; the boundary and duplicate-entry consequence are step-specific. | WAY-33/134. |
| `find_settlements.md:16-19` — re-open changed rows and count candidate table | Step 5 when resuming accepted rows; yes. | **Keep beside skill** as a multi-part conditional procedure. | WAY-124/134. |
| `find_settlements.md:21-22` — route candidate conflicts or scope change | Step 5 when a candidate exposes either; yes. | **Keep beside skill**; it contains two distinct return routes. | WAY-134. |
| `SKILL.md:54-58` and `final_review.md:3-5` — step 6 pointer and draft review actions | Step 6 when draft is complete; yes. | **Keep** the pointer; **move** show/propose/apply/no-move procedure. | WAY-114/256; this is the concrete R2 counterexample. |
| `final_review.md:7-14` — readiness checklist, plan/definition checks and obstacle route | Step 6; yes. | **Keep beside skill**; a multi-instruction checklist, including both variant checks. | WAY-124/126/140/142; R1 readiness check is already required at step 1 before reliance. |
| `final_review.md:16-18` — unresolved guideline classification/metadata | Step 6, if such a finding remains; yes. | **Keep beside skill** with its related guideline branch. | WAY-214/215/216. |
| `final_review.md:20-26` — whole-document approval, wait, revision and status | Step 6; yes. | **Keep beside skill**; several human and state actions used only at final handoff. | WAY-114/124/154. |
| `project_plan_task.md:3-11,13-17,19-23,25-28` — plan-member input, question, assignment and final checks | Steps 1, 3, 4 and 6 only for plan members; yes, each heading names its step and variant. | **Keep** in the variant file named at step 1; R1 adds the shared readiness check outside this variant so both plan-member modes execute it. | WAY-142/145/147; plan check and readiness check have distinct coverage. |
| `source_only_task.md:3-19` — source-only input, question and projected-entry handling | Steps 1, 3 and 4 only for source-only tasks; yes, heading and variant pointer name the route. | **Keep** in the variant file. The duplicated readiness line was removed here because the common step-1 instruction now covers it for both project relations. | WAY-106/108/118/124/126/150. |
| `orchestrated_mode.md:3-20` — conversation file, verification, resume, presentations and question routing | Only for the dispatch-file variant; yes, the dispatch and file path identify it. | **Keep** in the variant file; several coordinated actions. | WAY-134/154/155. |
| `orchestrated_mode.md:22-39` — candidate, child-work, edit-boundary, answer and waits-for-task rules | Only for orchestrated refinement; yes. | **Keep** in the variant file; multi-part variant procedure. | WAY-113/145/154/155/156. |
| `orchestrated_mode.md:41-54` — exact result and final acceptance handoff | Only for orchestrated mode; yes. | **Keep** in the variant file; status/result protocol differs from manual mode. | WAY-154/155. |
| `guideline_findings.md:3-23` — missing discipline prerequisite and resume | Only after shared reading reports missing discipline guidelines; yes, step 3 pointer names the trigger. | **Keep** in the conditional file; multiple relationship-dependent actions. | WAY-172/215/217/218/247. |
| `guideline_findings.md:25-41` — existing guidance, unindexed kinds and exemplar test cases | Only for those guideline findings; yes, each kind is named. | **Keep** in the conditional file; these are several exceptional branches. | WAY-199/200/216/238/242. |
| `guideline_findings.md:43-47` — final readiness after scope change | Step 6, if scope reached a new part or a finding remains; yes. | **Keep** in the conditional file referenced by final review. | WAY-214/215. |

## Foundation step and search comparison

`task-cycle/skill/foundation_step.md` says the cycle searches the whole foundation before writing
kept entries; this refinement skill limits its own search to what step 1 reads and *Decisions in
play* carries. The new placement preserves that boundary: detailed refinement search stays in step
5, and the main skill keeps the sequence and pointer. The selected entries named in
`author-handoff.md` were read whole; the placement criterion is grounded especially in WAY-35,
WAY-127, WAY-134, WAY-150, WAY-154/155, WAY-256 and WAY-257. WAY-259 was read whole; its full-skill
then triggered-file rule is now stated by the generator and protected by a complete-sentence
assertion.

`project-level/task/template.md` is read in full at step 1 and remains the form/rules source for the
task document. This is a placement assessment only; its sections are not re-judged or edited.

## Contradictions and limits

The root `CLAUDE.md` imports `AGENTS.md`. Neither provides competing `refine-task` instructions.
The orchestrated and guideline files load only under their stated variants/triggers; they do not
contradict the main route. The source-only and plan-member files have distinct triggers. The main
file's readiness instruction is common to both approved-definition routes, while the plan checker
continues to check plan structure and consistency.

No semantic instruction was removed. The only duplicate removed was the source-only copy of the
readiness check after it became a common step-1 rule. No runtime adherence claim is made from
instruction-text checks. M1–M3 in the original review remain report-only and unfixed. The step-6
multi-instruction checklist and step-3 Human-actions procedure were moved under the actual
step-specific criterion; this overlaps M3's observation, but does not edit the prior M3 report.

## Counts

All counts use Python UTF-8 `str.split()`. Base `SKILL.md` has 2,933 words; the unchanged task
template has 1,580. Command used for the post-fix counts:

`python -B -c "from pathlib import Path; base=Path('project-level/task/skill'); names=['SKILL.md','read_sources.md','draft.md','resolve_gaps.md','carry_foundation.md','find_settlements.md','final_review.md']; counts={n:len((base/n).read_text(encoding='utf-8').split()) for n in names}; extras={n:len((base/n).read_text(encoding='utf-8').split()) for n in ['project_plan_task.md','source_only_task.md','orchestrated_mode.md','guideline_findings.md']}; print('core',counts); core=sum(counts.values()); print('core_total',core); print('manual_plan',core+extras['project_plan_task.md']); print('orchestrated_plan',core+extras['project_plan_task.md']+extras['orchestrated_mode.md']); print('source_only',core+extras['source_only_task.md']); print('guideline_add',extras['guideline_findings.md']); print('template',len(Path('project-level/task/template.md').read_text(encoding='utf-8').split()))"` — exit 0.

| Path | Baseline words | After words |
|---|---:|---:|
| Main skill plus common step files | 2,933 | 2,007 |
| Manual project-plan path (common plus `project_plan_task.md`) | 2,933 | 2,212 |
| Orchestrated project-plan path (common plus plan and `orchestrated_mode.md`) | 2,933 | 2,782 |
| Source-only path (common plus `source_only_task.md`) | Outside requested baseline variants | 2,172 |
| Conditional guideline file when triggered | Not in baseline every-use path | +453 |
| Task template (separate, unchanged) | 1,580 | 1,580 |

The seven common files counted above are `SKILL.md` (396), `read_sources.md` (298), `draft.md`
(240), `resolve_gaps.md` (391), `carry_foundation.md` (145), `find_settlements.md` (247) and
`final_review.md` (290). The plan, source-only and orchestrated additions are respectively 205,
165 and 570 words. The skill-only common path falls by 926 words from baseline; the orchestrated
path falls by 151. A triggered guideline reading adds 453 words to any applicable path.
