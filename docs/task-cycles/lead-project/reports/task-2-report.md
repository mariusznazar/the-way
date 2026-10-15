# Slice 2 implementation report

## Method and RED before edits

These are semantic inspections of instructions, not executed agent trials. No text-match assertion is claimed to prove agent compliance.

1. Setup: an orchestrated refiner cannot determine the task location. Action: follow original refine-task step 1. Static result: it says "ask once" and has no orchestrated routing override; the refiner would address the human rather than return a file turn. Expected contract fails.
2. Setup: a question asks how behavior is to be, and current code suggests an answer. Action: inspect current refinement instructions and lead companions. Static result: step 1 says to read product files for factual questions, but no answering-agent contract distinguishes current code facts from prescriptions; both lead companions are absent. Expected authority boundary is undefined.
3. Setup: a manual task has no candidate rows and all other checks pass. Action: follow original step 6. Static result: "Mark Status: ready for cycle only when its applicable checks pass" follows the checklist without requiring acceptance of the complete document. Showing a draft is not acceptance. Expected final acceptance fails.

## Source selection

Worktree: C:/Storage/repos/the-way-wt/lead-project, branch task/lead-project. Foundation read-only. Touched part: project-level. Complete Scope inventory selected WAY-09, 106-124, 126, 127, 134, 137-140, 142-147, 150-156 (only IDs present in the inventory); selection retained in slice2-foundation-selection.md. Shared workflow, task/template, plan/template, common source-finding skill and frozen task/spec read. Whole map/glossary and relevant project-level invariant methods inspected. No global skills, vault files or generated entry points edited.

## Implementation and choices

Four paths only:
- project-level/lead/conversation_template.md: single-file identity, role ownership, serialized turns, numbered questions, provenance, human material, canonical answers, closed refiner results, resumption and acceptance/cleanup.
- project-level/lead/answering.md: round-level source authority and deduplication, document quotations versus current code facts, human escalation and rejected-quotation handling.
- project-level/task/skill/SKILL.md: one routing override over the existing workflow, no duplicate refinement body; every otherwise-human step returns through the file; complete-document acceptance in manual and orchestrated modes.
- project-level/task/template.md: retained answered questions and source provenance, shared answers, final acceptance, candidate-source survival.

Choices within spec:
1. Extend the current skill with an overriding orchestrated-mode section. Keeping current wording alone fails file routing; a duplicated workflow would drift at every later change. The override costs a mode check and an explicit resumption rule; the steps remain single-sourced.
2. Identify the final document by path plus revision/content identity, rather than a mandated new hash command. Path alone cannot distinguish accepted and later edited text; a new hashing tool adds an interface not required by the spec. Agents must retain the actual identity/content they reviewed.
3. Store canonical answer and original source in each affected task before any canonical conversation cleanup. Only cross-links cost less text but break after deletion; the retained repetition is required by the durable-result contract.
4. Keep accepted questions under Questions to settle. Removing answered questions saves space but loses the provenance the frozen task requires. The template now says questions whose answers are or were needed, resolving its old gaps-only wording.

## GREEN semantic walkthroughs

All cases below are static instruction walkthroughs with hypothetical inputs. They are not agent executions, observed user decisions, or evidence that an agent complied. Locations refer to the four changed paths above. Each turn terminates before another actor writes.

| Scenario setup | Action across turns | Static result from final wording |
|---|---|---|
| Missing outcome choice; no authorized source answers | Refiner writes Q1, Blocks and Asks, ends `questions` and returns exactly `questions`; answerer reads all files, prepares human options/costs/recommendation; project orchestrator records human answer; fresh refiner transfers it and checks readiness | Mode routes every human question to file and ends turn; template result table keeps plan to refine until package presentation, then waiting for human. No agent invents the answer. |
| Question needs unfinished task 3's produced result | Refiner records exact question/reason in task and conversation; final line and return are both `waits for task 3`; project orchestrator logs wait; after evidence of task 3 done, proposes it in a round; fresh refiner revisits that question | Template/mode require a real plan number and question-specific need. Ordinary Depends on does not itself cause a wait. |
| All questions/candidates/actions/checks settled, complete task not accepted | Refiner supplies complete document, leaves task waiting for human, final line/return `ready for approval`; project orchestrator presents one complete document; hypothetical explicit acceptance is recorded before final writes | Only project orchestrator writes Status ready for cycle and plan/log. Turn result is not a task Status. Another task or package acceptance cannot substitute. |
| Task work mismatches approved plan scope | Refiner records full mismatch evidence and requested owning-workflow change, ends/returns `plan change`; project orchestrator routes upstream work; fresh refiner resumes against corrected sources | No task-body scope expansion, no implied readiness, no autonomous plan/definition/foundation write by refiner. |
| Required source unreadable or child capability missing | Refiner records exact missing source/capability and what resolves it, ends/returns `obstacle`; project orchestrator supplies source/capability or obtains human resolution; fresh refiner rechecks | A missing file is not a passed check; no nested dispatch or invented critique. No automatic progress. |
| Same choice in task 1 Q1 and task 2 Q4 | Answerer reads all round files, picks task 1 Q1 canonical, cross-references paths/IDs and affected tasks, prepares one human question; project orchestrator records answer; each fresh refiner copies answer and original source into its task | One human choice; different scopes remain separate. Cleanup cannot delete task 1 conversation while task 2 still depends only on its cross-link. |
| Document quotation answers Q1 but human strikes it | Project orchestrator records strike, answerer marks struck and prepares canonical human question with ways/costs/recommendation; fresh refiner treats it as pending until a new answer | answering.md forbids recycling struck quote; mode/template forbid treating it as settled. Quote/source stay visible for context. |
| Question asks intended product behavior; only current code fact exists | Answerer labels how product is to be, sees code is not authorized, leaves intended answer pending and prepares human question; current observation remains separately sourced | Code cannot prescribe a requirement. Definition/plan/foundation/task quotation is needed or the human decides. This closes RED 2. |
| Question asks current behavior; inspected code establishes it | Answerer fills code fact, file:line and revision; project orchestrator keeps it separate from document-quotation list; fresh refiner transfers observation and original source | Current fact allowed without presenting it as a human choice or approved requirement. |
| Human action unplaced, then placed before cycle but not done | Refiner proposes placement in file and ends `questions`; project orchestrator records human placement; fresh refiner leaves waiting for human; completion later recorded by human; refiner repeats checks before ready for approval | TODO placement and not-done pre-cycle action both block readiness; agent neither places nor performs action. Action in the cycle does not require premature completion. |
| Candidate accepted with binding choice requiring challenge; another rejected | Refiner returns full five-column table plus IDs/state; project orchestrator presents and records selection, asks source-anchored WAY-113 question unless stated exception applies; fresh refiner consumes answers, retains accepted row whole, removes rejected row, preserves counts | Pending candidate/challenge prevents readiness; selection and final document acceptance remain distinct. Neither refiner nor answerer accepts on human behalf. |
| Accepted document answer at a precise source revision | Refiner checks source still holds, transfers full answer and source to task Questions to settle and records Transferred; updates required behavior only from that authorized answer | Retained task has answer and provenance; cleanup no longer loses source. |
| Interrupted after human final acceptance but before both status writes | Resumer reads header/all turns/acceptance identity, compares actual task/plan, completes only supported status writes; if document body changed returns to fresh refiner and renewed acceptance | Record-before-write and exact-document identity prevent inference from empty questions or agent readiness. |
| Manual task has no candidates and no moves | Step 6 checks readiness then shows complete final document, explicitly asks acceptance and waits in waiting for human; only explicit acceptance enables ready for cycle | No-candidates still waits. This closes RED 3. |
| Missing task location or conflicting decisions during orchestrated borrowed step | Mode overrides direct ask/show instructions; write whole material, alternatives/costs/recommendation where applicable, end with questions or obstacle/plan change as evidence warrants; resume by consuming recorded answers | Covers location, which item, scope/wording, deployment split, conflicts, actions, candidates/challenges and final approval. This closes RED 1. |

## Automated command evidence

Working directory for every command: C:/Storage/repos/the-way-wt/lead-project.

`python -B gate/run_tests.py project-level` - exit 0:
```
Ran 227 tests in 45.260s
OK
```

`python -B gate/run_tests.py gate` - exit 0:
```
Ran 98 tests in 16.966s
OK
```

Both outputs contained progress dots and the summaries above, with no failures/warnings. These are existing automated suites, not a full gate or agent-behavior trial. No invariant tests or foundation files were changed. No tautological source-string tests were added. No new skill name/description/frontmatter change; entry-point regeneration remains for the later inventory slice.

`git diff --check` - exit 0, empty output before commit.

## Self-review

Read all changed files and existing-skill diff. Corrected resumption to consume recorded answers instead of repeating already accepted presentations, and clarified Questions to settle to retain resolved questions. Used ASCII separators in new template headers after checking the written files. Existing task files were read/written with newline='' to preserve EOL. No backslash literal introduced. Four-path scope retained, no implementation launch or foundation writes.

No unresolved design concern identified in this slice. Semantic compliance remains unproven by runtime agent execution, as the brief explicitly distinguishes; independent review is the controller's next step. Root owns later orchestration/inventory/integration work.

## Commit and final state

Commit: 6e8efc5 - feat: add file-mediated project task refinement.
Base: 2233cffd031838f9e68272824fb4899c93471cc3.
Explicit git add named only the four changed paths. git commit exited 0. git status --short after commit was empty. Author email verified as the configured private address.

Git add reported its ordinary EOL normalization warning for the two new files (working-copy CRLF will be replaced by LF on Git touch). The existing files were preserved; no whole-file EOL churn is in the committed diff. git diff --check exited 0. No amend, merge or push performed.
