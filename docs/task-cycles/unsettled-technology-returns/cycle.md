# Cycle record — Wybór technologii, której projekt nie ustalił, wraca do Mariusza zamiast zapaść po cichu w zadaniu

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_wybor_technologii_ktorej_projekt_nie_ustalil_wraca.md`, `Status: ready for cycle`, copied 2026-10-31; its citations stand at `foundations` `00c0a74`
- Task relation: independent
- Product repository: `C:\Storage\repos\the-way` (the-way working on itself, under `agent-instructions/README.md`)
- Process pin: none — the process root is this worktree
- Target branch and base: `foundations`, `2dbf1e7`
- Task branch: `task/unsettled-technology-returns`, worktree `.runs/worktrees/unsettled-technology-returns`
- Status: request open

## Two questions at start

- Trust boundary: no at the start — the task names no file the part map holds as a trust boundary. Judged again after the spec, which may reach `project-level/plan_state.py` through the task's carried question 2.
- Irreversible operation: no

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: yes. The task's *Questions carried to cycle* leave open what a blocked draft request holds when no code remains, how the next cycle of the same task names its record and who moves a plan row back from `in cycle`; a trace of an earlier cycle reads as a conflict in `project-level/plan_state.py:416-420`, and WAY-147 binds the record's name. To do 2 and 4 give the task template a place whose form the task does not settle. The rows of *Settlements to record* settle their own entries.
- Execution route and reason: planned slices, judged at step 7 after the spec's review; see Q7. Trust boundary and irreversible operation stay no: the spec changes no file the part map names.
- Author: none on the planned route; executors appear in Slices
- Plan: six slices, each `fits` in `plan-size.md`; slices 1 and 5 class `same`, the others `cheaper`; no slice marked with a risk
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` tool; completion notification
- Whole-change review: fresh reviewer, by `review-change`, range `2dbf1e7..e21d286` then `e21d286..9849f4b`; `FAIL e21d286` then `PASS 9849f4b`; `reports/whole-review.md`, `reports/whole-review-2.md`; every To do, row and carried question covered; no projected entry carried. Its limit, stated by the reviewer: of about 120 in-scope decisions it read 18 whole, the changed and new ones in the diff, the rest by targeted search
- Review rounds: whole change, range `2dbf1e7..e21d286`, `reports/whole-review.md`, FAIL: three Important findings (a run's new note lost at a document with a list, slice 1; the pointer in `make-change` gated on returning, slice 4; WAY-267 broader than its files, plan's *Foundation entries*); fix `e21d286..9849f4b`, `reports/fix.md`; review of the fix `reports/whole-review-2.md`, `PASS 9849f4b`; no blocking finding remained
- Weakest-point checks: stated in each report under its own-work check: `reports/slice-1.md`, `slice-2.md`, `slice-3.md`, `slice-4.md`, `slice-5.md`, `slice-6.md`, `fix.md`, `return.md`. The whole-change review found the checks of slices 2, 3 and 4 to be greps and rereads that could not catch an unmet requirement (its Minor 7), which is how its finding 2 passed

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|
| Foundation entries | `2dbf1e7` | same, fresh agent, inherited model | none | `443442f` | clean tree; one commit; `foundations/decisions.md`, `foundations/glossary.md` as the plan lists; `foundation_check.py` exit 0 | judged by the whole-change review |
| 1 | `2dbf1e7` | same, fresh agent, inherited model | none | `6fb58f6` | clean tree; one commit after the entries; files match *Change*, the entry points of `settle-technology` under its patterns; checks with command and exit code in the report | judged by the whole-change review |
| 2 | `6fb58f6` | cheaper, fresh agent, claude-sonnet-5-5 | none | `c2c2479` | clean tree; one commit; files match *Change*; checks with command and exit code in the report | judged by the whole-change review |
| 3 | `c2c2479` | cheaper, fresh agent, claude-sonnet-5-5 | none | `9c06170` | clean tree; one commit; files match *Change*; report returned once for a missing exit code, repaired (exit 0, no pipe) | judged by the whole-change review |
| 4 | `9c06170` | cheaper, fresh agent, claude-sonnet-5-5 | none | `dc13d6a` | clean tree; one commit; four of five *Change* files, `task-cycle/spec/SKILL.md` left unchanged as the plan allows; checks with command and exit code | judged by the whole-change review |
| 5 | `dc13d6a` | same, fresh agent, inherited model | none | `db126f6` | clean tree; one commit; files match *Change*; checks with command and exit code in the report | judged by the whole-change review |
| 6 | `db126f6` | cheaper, fresh agent, claude-sonnet-5-5 | none | `e21d286` | clean tree; one commit; files match *Change*; checks with command and exit code | judged by the whole-change review |

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-10-31 01:16 | Start | orchestrator, claude-opus-5-5 | `task.md`, base `2dbf1e7` | worktree and record created | Task frozen, byte-identical to its source; base gate started in the background |
| 2026-10-31 01:17 | Spec, designer | fresh agent, inherited model | `reports/designer-handoff.md`, `task-cycle/spec/SKILL.md` | `spec.md`, `reports/designer.md` | `done`, no questions; no check run (design only); no trust-boundary file changed; worktree clean. Three picks for the review: doubt leans to reserved, a third new decision no row carries, the icon-source boundary example |
| 2026-10-31 01:32 | Spec, reviewer | fresh agent, inherited model | `reports/spec-review-handoff.md`, `task-cycle/spec/SKILL.md` | `reports/spec-review.md` | `FAIL`, nine findings; read-only, no test run |
| 2026-10-31 01:44 | Spec, designer's revision | the same designer, resumed | `reports/designer-revision-handoff.md`, `reports/spec-review.md` | `spec.md`, `reports/designer.md` | `done`; answers Q3, Q4, Q5 given |
| 2026-10-31 01:50 | Spec, review of the revision | the same reviewer, resumed | message naming `spec.md`, `reports/designer.md`, `reports/designer-revision-handoff.md` | `reports/spec-review-2.md` | `FAIL`: all nine findings resolved, one new finding 10; no third round. Orchestrator settled it (Q6) in `spec.md`, decision 4, as `task-cycle/skill/spec_review.md` gives; route judged again (Q7) |
| 2026-10-31 01:58 | Plan, planner | fresh agent, inherited model | `reports/planner-handoff.md`, `task-cycle/plan/SKILL.md`, `task.md`, `spec.md` | `plan.md`, `plan-size.md`, `reports/planner.md` | `done with concerns`: six slices, ten entries; every slice fits, 94k-145k tokens; checks passed on the base, slices' own diffs not run. Plan reviewed by the orchestrator: coverage of every To do, row and carried question, no code, *Model* and *Risk* checked, `planning.md` kept in slice 5; go-ahead provisional |
| 2026-10-31 02:12 | Foundation entries | fresh agent, inherited model | `reports/foundation-handoff.md`, `task-cycle/change/SKILL.md`, `task-cycle/skill/foundation_step.md` | `reports/foundation.md` | `done with concerns`, commit `443442f`: WAY-265, WAY-266, WAY-267, term reserved choice, WAY-121, 122, 123, 135, 137, 138; `python -B elements/common/foundation_check.py .` exit 0; concerns for the request: WAY-266 narrows WAY-114; WAY-160 read as not reaching a blocked draft with no code |
| 2026-10-31 02:26 | Slice 1 | fresh agent, inherited model, class same | `reports/slice-1-handoff.md`, `task-cycle/change/SKILL.md` | `reports/slice-1.md` | `done`, commit `6fb58f6`; focused checks exit 0; full suite and any real agent run at a task document not run. Observation for the whole-change review: `settle.md` sub-step 1 gives no research agent the sentences of a decision the human opened |
| 2026-10-31 02:37 | Slice 2 | fresh agent, claude-sonnet-5-5, class cheaper | `reports/slice-2-handoff.md`, `task-cycle/change/SKILL.md` | `reports/slice-2.md` | `done`, commit `c2c2479`; `gate/run_tests.py project-level` exit 0, `check_instructions.py` exit 0, `git grep` lists the file; `refine-task`'s `SKILL.md` left unchanged |
| 2026-10-31 02:41 | Slice 3 | fresh agent, claude-sonnet-5-5, class cheaper | `reports/slice-3-handoff.md`, `task-cycle/change/SKILL.md` | `reports/slice-3.md` | `done`, commit `9c06170`; first report lacked the exit code of `gate/run_tests.py project-level`; returned and repaired (WAY-159): exit 0; `git grep` lists all three files |
| 2026-10-31 02:52 | Slice 4 | fresh agent, claude-sonnet-5-5, class cheaper | `reports/slice-4-handoff.md`, `task-cycle/change/SKILL.md` | `reports/slice-4.md` | `done`, commit `dc13d6a`; `gate/run_tests.py task-cycle` exit 0; `git grep` exit 0 lists all four |
| 2026-10-31 02:55 | Slice 5 | fresh agent, inherited model, class same | `reports/slice-5-handoff.md`, `task-cycle/change/SKILL.md` | `reports/slice-5.md` | `done`, commit `db126f6`; `gate/run_tests.py task-cycle` exit 0, `check_instructions.py` exit 0, `git grep` exit 0, `skill_entry_points.py` exit 0 |
| 2026-10-31 03:04 | Slice 6 | fresh agent, claude-sonnet-5-5, class cheaper | `reports/slice-6-handoff.md`, `task-cycle/change/SKILL.md` | `reports/slice-6.md` | `done`, commit `e21d286`; `test_plan_state.py` exit 0, `gate/run_tests.py project-level` exit 0 (268 tests), `git diff --exit-code` on `plan_state.py`, `plan_check.py`, `test_plan_state_invariant.py` exit 0 |
| 2026-10-31 03:11 | Whole-change review | fresh agent, inherited model | `reports/whole-review-handoff.md`, `task-cycle/review/SKILL.md`, range `2dbf1e7..e21d286` | `reports/whole-review.md` | `FAIL e21d286`: 3 Important (slice 1; slice 4; foundation entries), 8 Minor, 4 declined; focused checks exit 0; reviewer states it read 18 of about 120 in-scope decisions whole |
| 2026-10-31 03:25 | Fix of the whole-change findings | fresh agent, inherited model, class same (highest of the classes, several slices) | `reports/fix-handoff.md`, `reports/whole-review-findings.md`, `task-cycle/change/SKILL.md` | `reports/fix.md` | `done`, commits `58c0b7f`, `d83067c`, `9849f4b`; `foundation_check` exit 0, `check_instructions` exit 0, `gate/run_tests.py project-level` exit 0, `gate/run_tests.py task-cycle` exit 0 |
| 2026-10-31 03:33 | Review of the fix | the same reviewer, resumed | message naming range `e21d286..9849f4b`, `reports/fix.md`, `reports/whole-review-findings.md` | `reports/whole-review-2.md` | `PASS 9849f4b`: all three fixed, none contested, two new Minor notes, one Minor and one out-of-scope note outside the fix diff; focused checks exit 0; findings 1 and 2 count as fixed on reading and hand trace |
| 2026-10-31 03:52 | Gate | orchestrator, claude-opus-5-5 | `python -B gate/run_tests.py` on `9849f4b` | `change-gate.log`, `change-gate.exit` | exit 0, 615 tests |
| 2026-10-31 03:53 | Return step | fresh agent, inherited model | `reports/return-handoff.md`, `task-cycle/change/SKILL.md`, `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md` | `reports/return.md` | `done with concerns`, commit `6f34b64`: fact `github-closed-pull-request-branch`, WAY-267 *Based on* and *Rationale* corrected, no change of meaning; `foundation_check.py` exit 0, `gate/run_tests.py elements/common` exit 0; tree changed after the gate |
| 2026-10-31 04:03 | Review of the return step | fresh agent, inherited model | `reports/return-review-handoff.md`, `task-cycle/review/SKILL.md`, range `9849f4b..6f34b64` | `reports/return-review.md` | `PASS 6f34b64`: no blocking finding, one Minor, four declined; `foundation_check.py` exit 0; passage matches the live and archived pages |
| 2026-10-31 04:03 | Gate | orchestrator, claude-opus-5-5 | `python -B gate/run_tests.py` on `6f34b64` | `final-gate.log`, `final-gate.exit` | exit 0, 615 tests, 5 skipped |
| 2026-10-31 04:12 | Request | orchestrator, claude-opus-5-5 | branch pushed, `gh pr create --draft` | https://github.com/mariusznazar/the-way/pull/63 | draft open; target unchanged at `2dbf1e7`, so no merge and no review of a merge |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Task slug (step 5): the task is independent, so the cycle names it | `unsettled-technology-returns` | task title | a Polish slug — the repository's names are English | a less telling name | record, branch |
| Q2 | Does the base moved past the task's cited commit change the task? | No: `00c0a74..2dbf1e7` changes only one paragraph of `task-cycle/skill/SKILL.md` on where the base checks run | `git diff --stat 00c0a74 2dbf1e7` | stopping to reconcile | line numbers the task cites shift slightly | designer's handoff |
| Q3 | Spec review finding 6: which way does doubt about the rule lean? | No rule on doubt; the agent's judgment with the examples of To do 9 decides | task, question 2 answer: „o przypadkach granicznych decyduje osąd agenta”; row 2 | doubt leans to reserved — a meaning row 2 does not carry (WAY-134) | a doubtful choice reaches the human in the request with code on it | spec, designer's revision |
| Q4 | Spec review finding 5: on what does a finding that a change took a reserved choice stand? | The general grade of `task-cycle/review/SKILL.md` section 3, a missed requirement; WAY-263 stays unchanged | WAY-263 covers a departure from an entry the change writes or changes; no row carries a change of it | editing WAY-263 — beyond what the task carries (WAY-30) | none known; the finding still blocks | spec, designer's revision |
| Q5 | Spec review finding 8: may a run reopen a projected decision of an approved definition? | No: the list marks it `projected`, and a change goes by `resolve_gaps.md` and WAY-118 | question 7 speaks of a decision of the foundation; To do 6 keeps the definition untouched | reopening it in a run — the definition's gate would be needed again | a human who wants it changed takes the longer route | spec, designer's revision |
| Q6 | Spec review finding 10, left after the one revision: a request for a run written as a question reaches `project-level/lead/answering.md`, whose agent answers it unresearched | The request stays a *Child-work request*; the answering agent also reads these for one canonical request and answers none | `answering.md:21-25,34-36`; `orchestrated_mode.md`; WAY-122, WAY-138, WAY-155 | a new kind of question the agent leaves unanswered — a miss reaches the human as an ordinary question with no research | one sentence more in `answering.md`; a canonical run keeps one more field | `spec.md`, decision 4 |
| Q7 | Route after the spec's review (step 7) | Planned slices: about 28 files across five parts, three new decisions, six changed, one term; an author's failure would discard everything | `spec.md` tables of files and entries | one author of class `same` — no plan's cost, but one agent holds all of it and a return for size discards the whole attempt | a plan and its handoffs cost more than one author would have | route |
| P1 | Plan choice (planner) | Six slices, cut by who reads each text: the step, refinement, the orchestrated round, the stage agents, the orchestrator, the return of a plan row | `plan.md`, *Choices* | The orchestrator's four seams, with the stage agents and the orchestrator in one slice and the return of a row inside the cycle's slice | Two slices word one contract apart and drift; the review of the whole change finds it and one fix pays for it | plan, provisional |
| P2 | Plan choice (planner) | `elements/decisions/template.md` in Slice 1, so one agent names the three fields in both templates | `plan.md`, *Choices* | A slice of its own for a file of the part `decisions` | Slice 1's agent reads the decisions of a further part; an agent of its own would read most of them for two rules | plan, provisional |
| P3 | Plan choice (planner) | `reserved_choices.md` in Slice 2, where its first reader `resolve_gaps.md` stands, ahead of Slices 4 and 5 that point to it | `plan.md`, *Choices* | In Slice 1 beside the step's other files | Slice 1 cannot link the rule by path and speaks of it through the glossary term; the review of the whole change sees the whole | plan, provisional |
| P4 | Plan choice (planner) | `draft.md` in Slice 2 with the rest of `refine-task` | `plan.md`, *Choices* | In Slice 6 with the rest of the spec's decision 5 | A reader of Slice 6 alone does not see the document's half of the return; the whole-change review reads both | plan, provisional |
| P5 | Plan choice (planner) | `project-level/lead/skill/SKILL.md` changed by Slices 3 and 6, for steps 3 and 1, Slice 6 depending on Slice 3 | `plan.md`, *Choices* | Both in one slice, which would tie the removal of a cycle's trace to the orchestrated round | One more agent reads that file; no text overlaps | plan, provisional |
| P6 | Plan choice (planner) | `task-cycle/skill/planning.md` added to Slice 5, though the spec's table does not list it: its sentence sends what a planner returns to step 6, and a reserved choice is also an open design choice by the glossary | `plan.md`, *Choices* | Left as it stands, the status list of `task-cycle/skill/SKILL.md` alone carrying a planner's `reserved` | A planner's report takes the spec's route for a choice the human keeps; if the clause is not needed, one clause too many | plan, provisional |
| P7 | Plan choice (planner) | *Read* names every decision whose *Scope* names a touched part, with the invariants of that part or of `every`, as "Reading the foundation" selects (WAY-150) | `plan.md`, *Choices* | Only the entries that bear on the slice's text | Each agent reads more than its text needs, the cost the size report shows; the narrow way would be the breach WAY-150 names | plan, provisional |
| P8 | Plan choice (planner) | The entry points' two directories count in Slice 1 only, the one slice that changes a description | `plan.md`, *Choices* | The generator run in every slice that touches a `SKILL.md` | A maker who changes a description in another slice has to run it too, and the gate's tests say so | plan, provisional |
| P9 | Plan choice (planner) | Slice 6's test stands in `project-level/test_plan_state.py`, as the spec names, and cites no invariant | `plan.md`, *Choices* | In `project-level/test_plan_state_invariant.py` | It is not read as a test of `project-plan-state-evidence`; that invariant stays unchanged either way | plan, provisional |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `task.md` | copied by the orchestrator | not applicable |
| Spec | `spec.md` | designer; finding 10 settled by the orchestrator | `reports/spec-review.md` FAIL, `reports/spec-review-2.md` FAIL with one new finding, settled |
| Plan and size | `plan.md`, `plan-size.md` | planner | orchestrator's review, provisional |
| Foundation entries | `443442f`, corrected by `9849f4b`, `6f34b64` | foundation agent, fix, return step | reviewed with the whole change |
| Slices | `6fb58f6`, `c2c2479`, `9c06170`, `dc13d6a`, `db126f6`, `e21d286` | executors | `reports/whole-review.md`, FAIL |
| Fix | `58c0b7f`, `d83067c`, `9849f4b` | fix agent | `reports/whole-review-2.md`, PASS |
| Return step | `6f34b64` | return agent | `reports/return-review.md`, PASS |
| Stages | `stages.md` | `task-cycle/cycle_stages.py` | not applicable |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| Base: `python -B gate/run_tests.py` | orchestrator, base `2dbf1e7`, Windows 11 | 0 — 614 tests in 8 directories, every directory passed (`base-gate.log`) | none failing on the base |
| `python -B gate/run_tests.py` | orchestrator, `9849f4b`, Windows 11 | 0 — 615 tests in 8 directories, every directory passed (`change-gate.log`) | none failed; 5 tests skipped on Windows |
| `python -B gate/run_tests.py` | orchestrator, `6f34b64`, the tree of the request, Windows 11 | 0 — 615 tests in 8 directories, every directory passed (`final-gate.log`) | none failed; 5 tests skipped on Windows |
| Manual: no agent was run on the changed instruction texts | reviewers, by reading and hand trace | not applicable | whether an agent recognises a reserved choice in use is unchecked |

## Return step

- Foundation compared with code: WAY-121, WAY-122, WAY-123, WAY-135, WAY-137, WAY-138, WAY-265, WAY-266, WAY-267, the term `reserved choice`, WAY-114, WAY-160, the task's *Decisions in play* and the part map of the touched parts, against the files of the change. Two things in WAY-267 no longer matched, corrected in `6f34b64`: its *Based on* quoted a source WAY-90 holds as a fact, and its *Rationale* left out the commit that moved the pin and the case of a correction
- Decisions written or changed: WAY-267 (*Based on*, *Rationale*)
- Invariants written or changed: none
- Environment facts: `github-closed-pull-request-branch`, new
- Glossary terms: none by this step; `reserved choice` written by the foundation step
- Part-map changes: none
- Projected entries written whole or in part: none carried
- Rows of *Settlements to record* written: none by this step; the foundation step wrote row 1 as WAY-265, row 2 as WAY-266, row 3 as WAY-121, WAY-122, WAY-123, WAY-135, WAY-137, WAY-138

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/63, ready for review
- Cycle and its reasons: a spec, since the task left the place in its template and two carried questions open; planned slices, for the size of the change (Q7); one round of fix on the spec and one on the whole change
- Process pin: none, the-way working on itself
- What this request settles: WAY-265 from row 1; WAY-266 from row 2; WAY-121, WAY-122, WAY-123, WAY-135, WAY-137, WAY-138 from row 3; WAY-267 and the term `reserved choice` from the spec; the fact `github-closed-pull-request-branch` from the return step; the Polish sentence of each stands in the request
- What the foundation puts in front of the human at the merge: no invariant test, no surface and no *Violated* mark
- Checks: `python -B gate/run_tests.py` exit 0 on the tree of the request; none failed; 5 tests skipped on Windows
- Human actions the request waits for: none
- Questions: none
- Review findings listed: eight Minor of `reports/whole-review.md`, three Minor notes of `reports/whole-review-2.md`, one Minor of `reports/return-review.md`, one out-of-scope note of `reports/whole-review-2.md`
- Blocked by review: none
- Choices within the request: 16, in the questions table
- Writes to the task's backlog entry: none; the cycle changed nothing in the author's notes
- Process remarks on the-way:
  - Whole-change review (`reports/whole-review.md`): "Whether WAY-160 reaches a request with no code: unclear, read as not reaching it (Minor 1)."
  - Whole-change review (`reports/whole-review.md`): "No place found that tells a fix's agent to return `reserved`, other than through section 5's gate (finding 2)."
  - Whole-change review (`reports/whole-review.md`): "No instruction found for a run given a new note at a document with a list (finding 1)."
  - Whole-change review (`reports/whole-review.md`): "Where a canonical request's mark and ID stand: not found (Minor 4)."
  - Whole-change review (`reports/whole-review.md`): "Who corrects a technology report in an orchestrated run: not found (Minor 5)."
  - Whole-change review (`reports/whole-review.md`): "Whether \"a choice of how to make what they settle\" takes in a new library in the agent's reading is a judgment about agents, unverified: no agent was run."
  - Review of the return step (`reports/return-review.md`): "**Whether GitHub keeps a closed request's commits, and for how long.** The page says the head branch can be restored and gives no term. WAY-267's *Rationale* reads that as keeping the commits. The fact's sentence does not go past the page, and the author's report flags the same gap."
  - Review of the return step (`reports/return-review.md`): "**Later captures of the page.** The CDX index shows none after 2026-10-16. An index can lag behind the archive, so \"closest\" holds as of what the index shows on the day of this review."
  - Review of the return step (`reports/return-review.md`): "**Other hosts.** Not looked for: WAY-267 speaks of a host, the fact of GitHub alone, and the decision's *Rationale* gives the cost elsewhere."
  - Review of the return step (`reports/return-review.md`): "**The word \"closest\" in the template.** It does not say closest to what. I read it as closest to the date read, and no other reading changes the capture chosen."
  - Spec, designer (`reports/designer.md`): "No host's documentation found on whether a request with commits but no changed files can open, or whether one stays open when a later push empties its diff. The only source found is a remark in a third-party thread on Pagure (https://pagure.io/pagure/pull-request/5501) that GitHub and GitLab allow empty pull requests; I did not verify it. Decision 2's order avoids the first question; the second stays unverified, and the spec states the cost."
  - Spec, designer's revision (`reports/designer.md`): "A later task's choice that an earlier, unmerged task already settled, outside one round: finding 9 covers one round only, and the spec gives no form for two rounds. A second run would research it again and the human would see it again. The cost is one repeated run; nothing is written twice, since WAY-134 ties the second row."
  - Spec, designer's revision (`reports/designer.md`): "A plan row reading `ready for cycle` whose document a run set to `refining` outside a round: the spec leaves it to the next reconciliation, as `draft.md` already leaves an accepted document refined again. `implement-task` step 1 reads the document's status, so no cycle takes it."
  - Slice 5 (`reports/slice-5.md`): "`task-cycle/record_template.md:89-90` (the paragraph under *Events*) and step 12 say the removal of the record is committed \"immediately after\" the copy. The request now opens between the two for a reserved choice. The plan names only two edits of the template, so the sentence stands; `reserved_return.md` states the departure itself."
  - Slice 5 (`reports/slice-5.md`): "Whether \"that correction's commits\" takes in the correction's merge of the target branch: neither the spec nor WAY-267 says. Settled by choice 1 below."
  - Slice 5 (`reports/slice-5.md`): "WAY-267's *Verification* and the spec say the request names the spec, the plan and the reviews as not run. A stop met after a reviewed spec or after a slice's review has run those stages. Settled by choice 2 below."
  - Slice 1 (`reports/slice-1.md`): "`orchestrated_mode.md` has no routing for a run yet, and `resolve_gaps.md` and `find_settlements.md` have no text for it. `task_run.md` and `SKILL.md` point to them as the plan gives; until the later slices land these pointers lead to nothing specific."
  - Slice 1 (`reports/slice-1.md`): "`reserved_choices.md` does not exist yet. This slice names only the glossary term, not the file."
  - Slice 1 (`reports/slice-1.md`): "Unclear: the spec names no field or list that gives the research agent the decision a human opened. See *Observations*."
  - Return step (`reports/return.md`): "**Other hosts.** WAY-267 speaks of \"a host\", and the fact covers GitHub alone. Whether another host restores a closed request's branch was not looked for; the decision's *Rationale* gives the cost where one does not."
  - Return step (`reports/return.md`): "**A closed request's commits.** The page says the head branch can be restored; it does not say for how long, and it does not use the words \"keeps the commits\". WAY-267's \"keeps a closed request's commits\" is a reading of that sentence, and the fact's sentence does not go past the page."
  - Return step (`reports/return.md`): "**A draft whose diff empties.** No host's documentation was found on whether it stays open, as the designer reported. `reserved_return.md:58-59` holds either way, so the change does not rest on it and no fact is due."
  - Fix (`reports/fix.md`): "Whether the finding's lesser clause was to be fixed was unclear: its *Fix* line does not list it, while its *What is wrong* does. See *Choices*."
  - Foundation entries (`reports/foundation.md`): "Question 2's second way not chosen reads \"jak wyżej\". Unclear whether it means the answer or the way before it; its cost, one more line in a request, fits only the answer, so WAY-266 writes \"the same rule\"."
  - Foundation entries (`reports/foundation.md`): "Whether the template's rule on *Rejected* reaches a decision changed from a row, and how, when one row changes six decisions: not settled anywhere found; see *Choices*."
  - Foundation entries (`reports/foundation.md`): "The spec gives the GitHub passage with no place in the page. Found by fetching it: § \"Restoring a deleted branch\", passage as the spec quotes it, read 2026-10-31."
  - Foundation entries (`reports/foundation.md`): "`git grep` found \"reserved\" in `installation/` only as part of \"preserved\"; no other use."
  - Plan, planner (`reports/planner.md`): "`git log --diff-filter=A -- 'docs/task-cycles/*/plan.md'` returned nothing, and so did the same search for `cycle.md`, a false \"none\": records added and removed on a merged branch are dropped by history simplification. With `--full-history` they appear. Noted for whoever searches records next."
  - Plan, planner (`reports/planner.md`): "The handoff counts \"about 28 files\"; the plan counts 29 plus the entry points, for the reason of concern 1."
  - Plan, planner (`reports/planner.md`): "`task.md:97` gives an act after the merge, moving a line of the private note `mapa_pakietu_10x.md` to the number of row 2's decision. It belongs to a later session, so no slice covers it; it stands here so it is not lost."
  - Spec, reviewer (`reports/spec-review.md`): "Not checked: the GitHub sentence at `spec.md:371` carries no address, and the claim at `spec.md:180` that no host's documentation says a request with no net diff is accepted. The review reached no host documentation."
  - Spec, reviewer (`reports/spec-review.md`): "Unclear: `spec.md:139-141` says that the return step writes a choice whose row the human struck, while `spec.md:105-106` says that the cycle otherwise writes no decision of it. It stands under *Cost if wrong* and sets no behaviour, so it is no finding, but `task-cycle/skill/return_step.md:12-13` would have that step write what the human cut."
  - Spec, reviewer (`reports/spec-review.md`): "Unclear: `spec.md:365` speaks of \"that cycle's worktree\". Where a cycle ran in the product's main checkout, which step 4 of `implement-task` allows, `.runs/task-cycles/<name>` stays and the reader still counts it as a working cycle. The spec does not say what removes it."
  - Spec, reviewer (`reports/spec-review.md`): "Not found: `foundations/invariants.md` holds no `### ` heading for the four invariants the handoff names; they stand under `## `, and were read there."
  - Spec, review of the revision (`reports/spec-review-2.md`): "Not checked: the GitHub page at `spec.md:431` was not opened. The review reached no host documentation."
  - Spec, review of the revision (`reports/spec-review-2.md`): "Unclear: `spec.md:108-109` still gives as the reason for always showing the candidate that \"the cycle otherwise writes no decision of it\", while `spec.md:151-154` now says that the return step may still write such a choice. It stands under *Cost if wrong* and sets no behaviour, so it is no finding."
