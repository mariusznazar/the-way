# Slice 3 implementation report

Base: 6e8efc5649044f5d79911370107b6f486068e81f.
Commit: 74750b3 — feat: lead project refinement rounds and route plan changes.

## Method and RED evidence before edits

These are static semantic walkthroughs, not observed consuming-agent trials. No child agent is
launched by this executor. The slice changes instructions; text matching would not demonstrate
agent behavior. Existing Python suites check their actual executable contracts separately.

Setup: a handed-over plan has tasks 1, 2, 3, 4; 2 and 3 depend on 1, and 4 depends on both 2 and 3.
Tasks 1 and 2 require refinement; task 2 has a question requiring task 3's eventual result.
Action: follow the current plan's handover to the next owning workflow.
RED result: project-level/plan/skill/SKILL.md:147 sends each task separately to refine-task;
project-level/lead/skill/SKILL.md does not exist (Test-Path returned False). The existing conversation
and answering contracts define exchange, but no leading actor selects a round, dispatches it,
reconciles state or performs the human package and acceptance. Ranking must count task 4 once
for task 1 even though two routes lead to it; no present lead instruction performs that action.

Setup: tasks 1 and 2 depend on one another only in the direction 2 -> 1, and both have enough
approved information to refine now. Action: interpret Depends on for parallel refinement and
cycle start. RED result: project-level/plan/template.md:84 calls this generic side-by-side work;
task-cycle/skill/SKILL.md:28 requires dependency sources but never explicitly requires completion
before the start. Thus the consuming workflows leave the changed WAY-144 distinction unstated.

Setup: a round produces a rejected quotation, an in-scope split, and a definition edit while a
second document awaits acceptance. Action: route each through its owning workflow. RED result:
the companion contract describes the requirement, but neither plan-project nor define-project
has a delegated-mode handoff for returning human/critique requests to the project orchestrator.
Their direct ask/dispatch steps can bypass that actor. No lead workflow gates readiness during
the definition gate or serializes shared-plan structural edits.

Commands used for baseline inspection: git status --short (clean), git branch -vv (task/lead-project,
no upstream), Test-Path project-level/lead/skill/SKILL.md (False), and rg of handover/dependency/gate
references in the four integration targets. No live product or source backlog was changed.

## Source selection and implementation

Touched parts: project-level and task-cycle, from the complete part map. Foundation revision is
the dispatch base above (all five new workflow decisions already present). Exhaustive current
Scope inspection selected 81 entries, retained whole in the ignored working evidence
task-3-foundation-selection.md beside this report; selection IDs are WAY-01,03,09,10,11,13,16,21,
25,26,27,28,30,33,34,36,37,38,44,45,46,47,48,51,55,57,62,63,65,68,69,82,89,100,101,102,103,
106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,134,
135,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156.
The expected Scope set equals the selected set. Relevant invariant entries, including every-Part
entries, were inspected and retained whole in task-3-invariant-selection.md; none was edited.
The product-orchestrator glossary meaning and current WAY-152..156, amended WAY-144, WAY-124,
WAY-134 and linked project/gate rules govern the exchange. Shared workflow/critique and the frozen
task/reviewed spec, full task skill/template, conversation/answerer contract, plan/definition
templates and current readiness/plan/state-reader implementations supplied the integration context.
Slice2 review supplies the existing contract's remaining lead integration obligations. No new
foundation rule was invented and no source or test was changed to pass this slice.

Implemented files:

- project-level/lead/skill/SKILL.md: the new leading workflow, bound to the existing conversation
  and answerer contract; recovery, state evidence, confirmed ranked rounds, writer ownership,
  human package, collective critique, final acceptance, safe transfer/deletion and change routes.
- project-level/plan/skill/SKILL.md: delegated file routing and serialized structural edits, fresh
  post-gate recheck from step0, explicit cycle/refinement distinction and leading handover.
- project-level/plan/template.md: dependency meaning, refinement-state meanings and delivered-in/
  dropped completion distinction. No machine-readable columns or state values were added.
- project-level/skill/SKILL.md: delegated definition edit/gate routing; project orchestrator
  dispatches critique and obtains human approval; gate agent writes the actual approval record.
- task-cycle/skill/SKILL.md: pre-start dependency completion and approval/recheck blockers, while
  preserving acceptance of a ready document waiting for dependencies.

Existing skill names/descriptions are unchanged. New frontmatter names lead-project and explicitly
excludes definition, breakdown, direct single-task refinement, implementation and closure. Wrapper
generation is intentionally left to Slices5-7 under the accepted bounded plan.

## GREEN semantic walkthroughs

These results are inspection of the full consumer instructions and their connected contracts;
they are not actual agent executions and not static-string tests. Each action below was walked
through against the final files to check that no delegated direct-human/nested-dispatch path or
unsafe writer ownership remained. The relevant sections are named so reviewers can repeat it.

| Setup | Action through final instructions | Semantic result |
|---|---|---|
| Handed-over plan; task2 depends on unfinished task1; both have refinable scope | plan-project step7 -> lead steps0/2/3 | Human confirms a round containing both; separate fresh refiners run in parallel. Depends on does not itself create a refinement wait. |
| Diamond graph: 2->1, 3->1, 4->2 and 4->3; disconnected 5 and 6 tie | lead step2 counts distinct transitive dependants | Counts for 1,2,3,4,5,6 are 3,1,1,0,0,0; proposal order is 1,2,3,4,5,6. Task4 is counted once for1 and ties use task number. Human may change the proposal. |
| Two refiner turns supply the same required-behavior question | lead step3.2 and answering contract read all files | One round answerer canonicalizes the same scoped question, retaining both affected task IDs; later answering turns resume that sole owner (or replace it after retiring the old writer). |
| Required behavior has no authorized document answer, but code shows a current implementation | lead step3.2/3 and answering authority | Code is retained only as sourced current fact. The behavior choice reaches the human with ways/costs/recommendation, once for affected tasks; no requirement is inferred. |
| Answerer supplies a document answer and candidate/action/wording proposals | lead step3.3-5 | One package contains full question/quotation/source plus all candidate columns, action placement and full wording. Code facts are separate. Project orchestrator dispatches one critic on the complete set before presentation. |
| Human strikes that quotation | lead step3.6, answering contract | Mark struck and preserve context/source; reopen the canonical human question with affected tasks and ways/costs/recommendation. A fresh refiner cannot transfer the struck answer as settled. |
| Critic requests a body correction | lead step3.4 | Project orchestrator verifies the remark and records its verdict; a fresh refiner owns the body edit. Human settlements are not changed silently. |
| Human selects a candidate then gives an answer entering binding meaning | lead step3.5/6, shared WAY-113 questions | Candidate selection is recorded separately, the source-anchored challenge is asked unless its stated exception applies, and the refiner carries the settled meaning whole. Selection is not final document acceptance. |
| An action is unplaced or placed before-cycle but not done | lead step4 first bullet and refine-task checks | Readiness remains blocked; only the human supplies placement/completion. No automatic acceptance or Status promotion. |
| TaskA ready for approval while taskB questions remain | lead step4 | Show complete A alone and wait for its explicit acceptance. Accepting A or the round does not accept B; a body correction returns to a fresh refiner and revised complete-document acceptance. |
| Acceptance recorded, interruption before Status write, or after Status before plan write | lead steps0/4 | Compare recorded exact document identity and current body, allow only intended Status change, recheck readiness and finish missing writes. No recorded approval or a changed body means no inferred approval; revised body needs renewed acceptance. |
| Canonical answer exists only in taskA conversation; taskB still needs it | lead step4 cleanup, companion transfer contract | Fresh refiners copy answer and original source into both task documents. Exact taskA file cannot be deleted until every affected transfer and remaining-conversation dependency check succeeds; no directory cleanup. |
| Refiner waits for task3 on named Q1; reconciliation proves3 done | lead steps1/2 | Wait/question/reason remains in task/conversation with to-refine row and logged reason. Task is reoffered in nearest human-confirmed round, never auto-started or forgotten. |
| Refiner asks for in-scope split/dependency change while ordinary state update is due | lead step5, plan delegated mode | Fresh plan-project owns the structural edit; project orchestrator pauses State/Document/log writes. Agent logs the change and checks original whole plan before ordinary updates resume. |
| Proposed task adds scope or changes projected-entry writer | lead step5 and plan delegated mode | Full change/consequences/costs reach human through project orchestrator; answer is recorded before plan agent applies it. No refiner expands its body to hide the mismatch. |
| Local definition edit only uses full text already before project orchestrator | lead step5, define delegated mode | Narrow edit is allowed; gate/recheck pending is recorded before edit. A subagent still performs step7, including search/checks. Broader edit delegates too. |
| Definition gate calls for critique and human approval while another task is ready for approval | lead step5, define delegated mode | Project orchestrator dispatches critic and passes observations by file; gate agent corrects. Human approves through orchestrator before agent writes record/fingerprint. No task becomes ready during gate or pending recheck. |
| Newly approved definition differs from old plan fingerprint | plan step0/delegated mode, lead step5 | A fresh plan-project agent starts step0, inventories/rechecks against new approval, logs new fingerprint/corrections and completes affected checks/critique/decisions. It does not send the same approved change through an endless second gate. Readiness resumes only after completed recheck. |
| Harness has no child agents or independent critic | lead step0/3.4/5 | Concrete capability obstacle; required delegated/independent work waits. Project orchestrator cannot impersonate agents, approve for human or launch cycles. |
| Evidence establishes final task done and every remaining goal delivered | lead step1 | Notice: closure is next, no closure skill exists; stop without closure or implement-task dispatch. Dropped alone is not delivery. |
| Ready task depends on task1 still in cycle | task-cycle Inputs1 | Completion is not established: no cycle/branch/implementation start; ready document retains acceptance. |
| Dependency state says done-goal-delivered-in-task3 | task-cycle Inputs1 | Follow named task's evidence; verified delivery permits source checks/start, unfinished or unsupported delivery blocks. Literal label is insufficient. |
| Dependency is dropped-approved-by-human | task-cycle Inputs1 | Human abandonment is not delivery: return mismatch to plan reconciliation before cycle start. |

## Executed checks

| Command | Exit | Exact result |
|---|---:|---|
| python -B gate/run_tests.py project-level | 0 | Ran 227 tests in 69.538s; OK |
| python -B gate/run_tests.py task-cycle | 0 | Ran 41 tests in 0.890s; OK |
| python -B gate/run_tests.py gate | 1 | Ran 98 tests in 26.234s; FAILED (failures=1) |
| git diff --check | 0 | No output |

Raw check output is retained in task-3-project-level-tests.txt, task-3-task-cycle-tests.txt and
task-3-gate-tests.txt beside this report. PowerShell wraps unittest's normal stderr dots in a
NativeCommandError formatting block when redirecting `2>&1`; recorded process exits above are
the actual Python exits, not an inferred failure from that wrapper.

The gate failure is exactly
`test_every_skill_reaches_a_session_on_the_way
(test_skills_reach_the_way_sessions.SkillsReachTheWaySessions.test_every_skill_reaches_a_session_on_the_way)`.
It reports absent `.claude/skills/the-way-lead-project/SKILL.md` and
`.agents/skills/the-way-lead-project/SKILL.md`, and existing sibling lists not naming lead-project.
This is the expected incomplete entry-point state until Slices5-7; no test was suppressed and no
generator output or invariant was changed. The other 97 tests passed. Unexpected failures: none.
The gate run is a partial suite, not the full gate, and none of these Python results proves agents
follow the instruction workflow. Live consuming-agent trials remain unperformed in this slice.

## Choices, self-review and boundary

- Used existing conversation fields/turns for plan/gate requests and pending recheck, rather than
  another state file. Leaving routing implicit would let borrowed direct-human/child steps bypass
  the project orchestrator; explicit delegated overrides cost a short section in two existing
  skills but retain one underlying workflow and resumable source identity.
- Made post-gate recheck explicit before readiness and avoided re-gating a definition already newly
  approved. Leaving the previous mismatch wording alone could repeatedly route an already approved
  change back through its gate; the clarification costs verifying approval and logging the new
  fingerprint while preserving every affected plan check and human-reserved decision.
- One round answerer resumes for subsequent turns; a replacement after interruption retires the
  prior writer. Multiple answering agents could race or ask duplicate questions; the chosen owner
  costs serialization but preserves parallel refinement on separate files.
- Kept live behavior claims out of the report. Static walkthroughs are repeatable semantic review,
  not executed agent evidence; actual trials would require dispatch beyond this executor's stated
  no-child boundary. No static source assertion was added as an agent-behavior test.

Self-review: read the complete new skill and full diff of four integration files against task/spec,
companion contract and selected foundation. Checked field/result/actor ownership, source authority,
all human decision points, shared writes, deletion and interruption ordering, stable names, no
implementation/closure launch, and scope of changed files. Added explicit approved-Status/gate
verification because readiness/fingerprint scripts alone cannot establish human approval; added
sole-answerer resumption to remove ambiguity across later turns. No remaining self-review finding.

Only the five allowed change paths are committed. Ignored evidence/report files remain untracked
by design. No global/vault writes, foundation or invariant-test edits, review dispatch, amend,
merge or push. Stage boundary: committed Slice3 with focused checks, returning before independent
slice review. Remaining concerns: intentionally incomplete wrappers and lack of live agent trials
as stated above; neither is concealed as a completed full gate or human approval.
