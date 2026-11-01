# Cycle record — the way: audyt w skillach wytycznych podaje wagę każdego ustalenia i kolejność naprawy

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_raport_audytu_wytycznych_z_waga.md`, `Status: ready for cycle`, copied 2026-11-01 to `task.md` beside this record; its citations stand at `foundations` `2f51e6c`
- Task relation: independent
- Product repository: `C:\Storage\repos\the-way` (the-way working on itself, under `agent-instructions/README.md`)
- Process pin: none — the process root is this worktree
- Target branch and base: `foundations`, `2f51e6c`
- Task branch: `task/guidelines-audit-report`, worktree `.runs/worktrees/guidelines-audit-report`
- Status: request open

## Two questions at start

- Trust boundary: no at the start — the task changes `product-guidelines/**` and the foundation; the part map names no trust boundary in `product-guidelines` or `decisions`. Judged again after the spec.
- Irreversible operation: no

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: yes. The task's *Questions carried to cycle* leave open the English words of the four grades, how the audit shows the cost of a fix, the English words for a finding and a cause, and whether rows 1–6 enter as one decision or as changes of WAY-187, WAY-201 and WAY-250. No row of *Settlements to record* carries these, and each binds after the merge, so settling them means designing (WAY-135). Also open and named to the designer: how a task joining coding and testing arrives at its one list, which skills share one order; where in the task document the full list stands. The six rows and the answers to questions 1–9 settle the rest.
- Reserved choice: none. The task settles no tool.
- Execution route and reason: one author without a plan, judged at step 7 after the spec's review. The reviewed spec names 19 files, all prose, no script and no test, and six new entries with three changed; the shared file, the discipline files and the entries bind one another word for word, so one agent reading them together makes a more consistent change than slices would, and nothing in the spec calls for division. Trust boundary and irreversible operation stay no: the spec changes no file the part map names as one.
- Author: fresh agent, class `same`, claude-opus-5-5, for its code, foundation entries and return step; class `same` because the change reaches three parts (`product-guidelines`, `project-level`, `decisions`)
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` tool, background; completion notification
- Whole-change review: fresh reviewer, claude-opus-5-5, by `review-change`; range `2f51e6c..0ee0cd9`; `PASS 0ee0cd9`, `reports/whole-review.md`; changed files by `git diff --numstat 2f51e6c..0ee0cd9`, 19 files, 587 added and 81 removed; coverage of every task item, row and carried question in `reports/whole-review.md` under *Coverage of the task*; no projected entry carried; no plan
- Review rounds: return step, range `0ee0cd9..aee18e4`, `reports/return-review.md`: one Important finding (`audit_end.md` repeats WAY-281 without the qualification the return step gave it); fix `aee18e4..ccb20de`, `reports/fix.md`; review of the fix `reports/return-review-2.md`, `PASS ccb20de`
- Weakest-point checks: one author, `reports/author.md`: To do 6, the rule of the top, and To do 8 with step 5, the pointers across files; checked by a scratch script over 715 orders of up to nine causes and every quoted section name, exit 0, 0 fails, with a positive control; and by walking a joint task through the files, which found the gap fixed in `0ee0cd9`; it shows the arithmetic and the pointers, not how an agent acts on the text

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-01 08:49 | start | orchestrator, claude-opus-5-5 | `implement-task`; task document | worktree at `2f51e6c`, `task.md` | branch `task/guidelines-audit-report` created with no upstream |
| 2026-11-01 08:49 | base checks | orchestrator | `python -B gate/run_tests.py` on `2f51e6c`, in the worktree before any tracked file changes | `base-gate.log`, `base-gate.exit`, `base-gate.head` | exit 0 at 08:56; 615 tests in 8 directories, every directory passed |
| 2026-11-01 08:50 | spec | fresh designer, inherited model | `reports/designer-handoff.md`, `task-cycle/spec/SKILL.md` | `spec.md`, `reports/designer.md` | `done`; words `weight` (`grave`, `heavy`, `medium`, `light`), `finding` and `cause` with `charge` retired; six new decisions with WAY-187, WAY-201, WAY-250 changed in place; shared file `product-guidelines/audit_end.md`; one list in *Context*; no question sent |
| 2026-11-01 09:05 | spec review | fresh reviewer, inherited model | `reports/spec-review-handoff.md`, `task-cycle/spec/SKILL.md` | `reports/spec-review.md` | `FAIL`: three findings (a withdrawn or lowered cause leaves no record of its check; the last audit lowers the other discipline's causes against decision 6 and WAY-247; a boundary left to the review under WAY-235 becomes a cause) |
| 2026-11-01 09:13 | spec revision | the designer, resumed | `reports/designer-revision-handoff.md` | `spec.md`, `reports/designer-revision.md` | `done`; all three findings answered; three further matters settled, as the handoff said two matters and named one (an orchestrator's slip, Q1) |
| 2026-11-01 09:16 | spec review of the revision | the reviewer, resumed | message naming the revision, `task-cycle/spec/review.md` | `reports/spec-review-2.md` | `PASS`; three findings resolved, the three further matters and the reading of WAY-247 hold, nothing broken besides |
| 2026-11-01 09:21 | route judged again (step 7) | orchestrator | `task-cycle/skill/spec_review.md`, reviewed spec | this record | one author, class `same`; see *Spec and execution route* |
| 2026-11-01 09:22 | one author | fresh author, claude-opus-5-5 | `reports/author-handoff.md`, `task-cycle/change/SKILL.md`, variant "the whole change as the one author" | `reports/author.md`, commits `5838d3a`, `ac27d26`, `0ee0cd9` | `done`; foundation check and focused directories each exit 0, `installation` exit 1 then 0 (the author committed while it ran); `gate`, `instruction-files`, `relation-model`, `task-cycle` not run; entries WAY-280 to WAY-285, WAY-187, WAY-201, WAY-250 changed |
| 2026-11-01 09:39 | whole-change review | fresh reviewer, claude-opus-5-5 | `reports/whole-review-handoff.md`, `task-cycle/review/SKILL.md`, range `2f51e6c..0ee0cd9` | `reports/whole-review.md` | `PASS 0ee0cd9`: 0 blocking, 5 Minor, 3 lines under Declined to judge; every To do, row and carried question covered |
| 2026-11-01 09:51 | gate on the change | orchestrator | `python -B gate/run_tests.py` on `0ee0cd9`; no agent commits while it runs | `change-gate.log`, `change-gate.exit`, `change-gate.head` | exit 0 at 09:55; 615 tests in 8 directories, every directory passed; HEAD `0ee0cd9` before and after |
| 2026-11-01 09:56 | return step | the one author, resumed, claude-opus-5-5 | `reports/return-handoff.md`, `task-cycle/skill/return_step.md` | `reports/return-step.md`, commit `aee18e4` | `done`; one correction: WAY-281 names the rules that block; foundation check and `elements/common` each exit 0 |
| 2026-11-01 09:58 | review of the return step | fresh reviewer, claude-opus-5-5 | `reports/return-review-handoff.md`, `task-cycle/review/SKILL.md`, range `0ee0cd9..aee18e4` | `reports/return-review.md` | `FAIL aee18e4`: 1 blocking (Important), 2 Minor, 1 line under Declined to judge |
| 2026-11-01 10:04 | fix | the one author, resumed, claude-opus-5-5 | `reports/fix-handoff.md`, `reports/return-review-findings.md`, `task-cycle/change/SKILL.md`, variant "the fix of a review's findings" | `reports/fix.md`, commit `ccb20de` | `done`; foundation check, `elements/common`, `git diff --check` each exit 0; no entry changed |
| 2026-11-01 10:05 | review of the fix | the reviewer of the return step, resumed | message naming the range `aee18e4..ccb20de`, `task-cycle/review/fix.md` | `reports/return-review-2.md` | `PASS ccb20de`: the finding fixed; 0 blocking, 0 Minor, 0 out of scope |
| 2026-11-01 10:06 | reconciliation with the target branch | orchestrator | `git fetch origin foundations` | `foundations` at `2f51e6c`, the base | no merge needed; the final tree is `ccb20de` |
| 2026-11-01 10:06 | gate on the final tree | orchestrator | `python -B gate/run_tests.py` on `ccb20de`; no commit landing during the run | `final-gate.log`, `final-gate.exit`, `final-gate.head` | exit 0 at 10:10; 615 tests in 8 directories, every directory passed; HEAD the same before and after |
| 2026-11-01 10:11 | request | orchestrator | draft, branch pushed | https://github.com/mariusznazar/the-way/pull/70 | opened as a draft; stages counted into `stages.md`; marked ready once the record's commit is named |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The revision handoff said two matters of the review's searches and named one; `reports/designer-revision.md` | the designer took every candidate, three in all; each stays subject to the review of the revision | `reports/designer-revision-handoff.md`; `reports/designer-revision.md`, *The matters left to the maker* | resuming the designer to narrow them | two sentences of the spec beyond what was asked; the reviewer judges them | spec |
| Q2 | The class of the one author; step 4 | `same`: a change across three parts | spec, *Foundation entries* and *Left to the maker* | `cheaper`, the default | a dearer author | author |
| Q3 | Whether naming the course and lesson in entry A's *Rationale* stands under WAY-27, left unclear by the designer and the reviewer | it stands: the log already names lesson m3l5 of the 10xDEVS course so, at `foundations/decisions.md:7960` and `:8074`, with the pattern described in the entry | those two passages; `reports/designer.md` | leaving the course unnamed, against WAY-100 and row 1 | one clause of a rationale | entry A |
| Q5 | The form of the list in `audit_end.md`; the spec names the fields, not the punctuation | a fenced example with items `- 1 — `heavy` — <cause>` | `reports/author.md`, *Choices made* | a Markdown numbered list, which renumbers itself and cannot hold the unnumbered `Withdrawn:` items in one run | a few lines of one file | `audit_end.md` |
| Q6 | Whether `Removes:` and `Reaches:` stand in the entries | they stand in `audit_end.md` alone, as spec decision 2 gives a field in one file | `reports/author.md`, *Choices made* | naming them in WAY-282 | a sentence in WAY-282 | WAY-282 |
| Q7 | What a stopped audit's list carries; the spec says only "writes its causes" | `Fix:`, `Removes:` and `Reaches:`, through "in the form of The list", since the audit running last orders by them and does not know the other discipline's fixes | `reports/author.md`, *Choices made* | causes alone | the last audit asks for or guesses the first audit's fixes | `audit_end.md` |
| Q8 | Where "The write is `refine-task`'s" stands | `guideline_findings.md`, so that a skill's table of what it never writes stays true | `reports/author.md`, *Choices made* | the skill's own files | one sentence moved | `guideline_findings.md` |
| Q9 | How WAY-280's *Rationale* describes the course's pattern, the task forbidding a reading of the course's skill | only as far as the task document does: what is adopted, not how the course words it | `reports/author.md`, *Choices made* | reading the skill | a thinner rationale | WAY-280 |
| Q10 | The wording of *Rejected* in WAY-285 and WAY-281, where a question speaks of "sam" and "zarzuty" | "it takes the check from the agent leading the audit"; "what the audit names as faults", since `charge` leaves the-way and an entry does not tell how it was reached; the meaning stands | `reports/author.md`, *Choices made* | quoting the task's words | two phrases | WAY-281, WAY-285 |
| Q11 | Whether the commits start with the foundation | yes, so that the files' citations stand on existing entries | `reports/author.md` | the files first | none after the merge | commits |
| Q12 | The return step's correction of WAY-281 lies on the matter of Minor finding 4, which the cycle leaves unfixed | it stands: the reviewer of the return step judged it sound on the entry's own comparison, and the orchestrator moved no finding | `reports/return-review.md`, opening | reverting the qualification | none; row 2's meaning is kept | WAY-281 |
| Q13 | The language of the request; step 13 asks the sentences of meaning in the task document's language, Polish | the request in English, as PRs #65 and #66 ended, with the Polish sentences of meaning in a collapsed block | step 13; PR #66 | Polish sentences alone in an English body | a longer body | request |
| Q14 | No gate or focused run while a commit lands: the author's first `installation` run failed for that reason | the orchestrator ran each gate with no agent active in the worktree, and the handoffs that followed bound it | `reports/author.md`, *Checks*; `reports/return-handoff.md` | running the gate beside the return step, as the last cycle did | a run to repeat | gate runs |
| Q4 | The times of this record's first rows were written ahead of the fact | corrected from the files' write times | `Get-ChildItem` of the record's directory, 09:20 | leaving them | none after the correction | this record |

Include questions answered by a binding source as well as new micro decisions. A choice that binds
after the merge is written into the foundation (WAY-36); every other choice is its row here and
nothing else.

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `docs/task-cycles/guidelines-audit-report/task.md` | copied by the orchestrator | not applicable |
| Spec | `docs/task-cycles/guidelines-audit-report/spec.md` | the designer | `PASS`, `reports/spec-review-2.md` |
| Change | `2f51e6c..0ee0cd9` | the one author | `PASS 0ee0cd9`, `reports/whole-review.md` |
| Return step | `0ee0cd9..aee18e4` | the one author | `FAIL aee18e4`, `reports/return-review.md` |
| Fix | `aee18e4..ccb20de` | the one author | `PASS ccb20de`, `reports/return-review-2.md` |
| Agent reports | `reports/` beside this record | each stage's agent | not applicable |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (base) | orchestrator, `2f51e6c`, the task worktree before any tracked file changed | 0; 615 tests in 8 directories, every directory passed | none failing on the base |
| `python -B gate/run_tests.py installation`, first run | the author, moved from `ac27d26` to `0ee0cd9` while it ran | 1; `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink`, `installation/test_install.py:228`, expected `ac27d26` and read `0ee0cd9` | failed: the author committed during the run; the test reads the current commit twice |
| `python -B gate/run_tests.py installation`, second run | the author, `0ee0cd9`, HEAD the same before and after | 0; 44 tests | none; the failing run stays recorded, one failed and one passed |
| `python -B gate/run_tests.py` (reviewed change) | orchestrator, `0ee0cd9`, the task worktree, no commit landing during the run | 0; 615 tests in 8 directories, every directory passed | none failed |
| `python -B gate/run_tests.py` (final tree) | orchestrator, `ccb20de`, the task worktree, no commit landing during the run | 0; 615 tests in 8 directories, every directory passed | none failed; not checked: how an agent acts on the text |
| `python -B elements/common/foundation_check.py .` | the author and the reviewer of the fix, `ccb20de` | 0; 0 errors | none |

## Return step

- Foundation compared with code: WAY-280 to WAY-285, WAY-187, WAY-201 and WAY-250, those the task names and those the search found, with `audit_end.md`, the discipline files and `guideline_findings.md`, and the part map of `product-guidelines`, `project-level` and `decisions`. Two mismatches: WAY-281 was wider than `coding/trial_run.md`, corrected in `aee18e4`; that correction left `audit_end.md` wider than the entry, corrected in `ccb20de` on the review's finding. The part map's sentences stay true.
- Decisions written or changed: WAY-280 to WAY-285 written by the foundation step, WAY-187, WAY-201 and WAY-250 changed by it; WAY-281 changed by the return step.
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: 1 WAY-280; 2 WAY-281; 3 WAY-282; 4 WAY-283, with WAY-187, WAY-201 and WAY-250 changed; 5 WAY-284; 6 WAY-285.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/70, ready for review once the record's commit is named
- Cycle and its reasons: a spec, for the choices at *Spec and execution route*; one author without a plan, class `same`; no discarded attempt
- Process pin: not applicable, the-way working on itself
- What this request settles: WAY-280 to WAY-285 from rows 1 to 6, WAY-187, WAY-201 and WAY-250 changed in place under row 4; the sentences of meaning stand in `reports/author.md` and, for WAY-281, `reports/return-step.md`, and in the request
- What the foundation puts in front of the human at the merge: none — no invariant test, surface or *Violated* mark changes
- Checks: `python -B gate/run_tests.py` on `ccb20de`, exit 0; `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink` failed in one cycle run and passed in four, its cause the author's commit landing during the run; how an agent acts on the text was not checked
- Human actions the request waits for: none
- Questions: none
- Review findings listed: in the request, five Minor of the whole-change review, two of the review of the return step, four lines of Declined to judge; beside them, `installation/test_install.py`, a check of a part outside the task's parts, one failed run and four passed
- Blocked by review: none
- Choices within the request: 14, in the questions table above
- Writes to the task's backlog entry: request link added to its line in `_tasks_active.md`; its state left `[/]`
- Process remarks on the-way: below

## Process remarks kept for the request

Stage: designer of the spec; report `docs/task-cycles/guidelines-audit-report/reports/designer.md`.

- How two skills of one joint task follow each other: neither WAY-247 nor any `SKILL.md` says. Decision
  6 settles it for the list alone.
- `elements/glossary/template.md:50-51` has `TODO — decision pending` on when two uses carry two
  meanings. Decision 3 used the sentence as it stands.
- Whether a weight's word should stand in the task document in English or the human's language: the
  template speaks of headings, status values and markers only. Decision 1 treats it as a marker.
- Whether naming the course and lesson in entry A's *Rationale* is a pointer under WAY-27: the
  verification there speaks of *Origin* and of a rationale resting on what is not said. The spec has it
  named with no address and the pattern described. WAY-256 does the same with no name of the course.
- That "moderate" is an advisory value of common tools is from my general knowledge, not from a source
  read here; it is only a side reason against one rejected way.
- No test reads these files: `git grep` over `*.py` for `product-guidelines` hit only `installation/`,
  each by the path of a `SKILL.md`; the same search for the names of the files beside a skill hit
  nothing. Positive control: `SKILL_SOURCE` and `kinds.md` both hit. The hits were opened.
- `README.md`, `installation/README.md`, `project-level/`, `agent-instructions/`: the only hit for
  `audit` is a Python audit hook in `project-level/test_plan_state_subprocesses_invariant.py`, which is
  no such audit.
- `product-guidelines/template.md` and the three disciplines' `template.md` were not read whole, not
  being named. Searches found no `charge` there, and `audit` only in `coding/template.md`: the audit of
  dependencies, and at lines 227-229 the audit that writes the table of a kind's files, read in place,
  which says nothing of how an audit ends.

Stage: reviewer of the spec; report `docs/task-cycles/guidelines-audit-report/reports/spec-review.md`.

- **Retired word and limit.** A first search over the repository, with a filter excluding `.runs/`,
  returned nothing, because the worktree itself lies under `.runs/`. Repeated with `git grep`:
  the eight lines of decision 3 and the two ordinary hits at `foundations/decisions.md:3401` and
  `7327` are as the spec says. WAY-250's "three to five" wraps across two lines, so the search for
  the limit misses it; it was read in place.
- **No test reads these files.** `git grep` over `*.py` for `product-guidelines` gives six lines in
  four files, each the path of a `SKILL.md`, as decision 14 says. Positive control: those hits.
- **Glossary.** No entry for `finding`, `cause`, `weight`, a grade or a blocking finding, from the
  list of headings read whole.
- **How two skills of one joint task follow each other.** Neither WAY-247 nor any `SKILL.md` says;
  each `hand_back.md` hands back to `refine-task` step 4, and nothing says who then starts the other
  skill. The gap stands today and is no finding of this spec, but decision 6 rests on it.
- **Joint task where the other discipline runs no audit.** Decision 6, item 2 reads "the product has
  what the other audit reads", which the route of one kind or a new level also meets. Read as
  settled by "A task with one audit to run ends as any other" (`spec.md:227`), so not reported; the
  maker has to word the condition by the audit that runs, not by what the product has.
- **Who writes the backlog.** Decision 10 says the skill writes no backlog and has the session add
  the task at the skill's step 5, by a file of `refine-task`. In coding and testing the table says
  the skill writes no other tracked file. Outcome unaffected, so not reported; it reads oddly only
  where a product's backlog is tracked.
- **Naming the course in entry A's *Rationale*.** WAY-27's verification speaks of *Origin* and of a
  rationale that rests on what is not said. The row names the course and the spec describes the
  pattern, so it was read as compliant. The designer reports the same doubt.
- **`elements/glossary/template.md:50-51`** holds a `TODO` on when two uses carry two meanings;
  decision 3 uses the sentence as it stands, and so did this review.

Stage: designer's revision of the spec; report `docs/task-cycles/guidelines-audit-report/reports/designer-revision.md`.

- The handoff says "two matters" and names one, the condition of decision 6, item 2. I could not tell
  which the second is, so I took both candidates; see above.
- WAY-48 itself was not read in this revision: the exception stands in WAY-235's binding sentences and
  in `testing/settle.md:35-36`, which were read.
- Whether a weight is a discipline's matter under WAY-247 is a reading: the decision's text does not
  define "that discipline's matters", and only its example points to what the guidelines carry.
- `elements/glossary/template.md:50-51` and naming the course in entry A's *Rationale* stand as the
  first report and the review left them.

Stage: reviewer of the revised spec; report `docs/task-cycles/guidelines-audit-report/reports/spec-review-2.md`.

- **`refine-task` step 3 names no discipline skill.** `resolve_gaps.md` does not start one; a
  discipline's `SKILL.md` says it takes over there. So the hand-back to step 3 works only by what
  `hand_back.md` itself says of the other skill. Decision 6 words it so, and the maker has to write
  it there, and correct "hands back to its step 4" at `coding/SKILL.md:31` and `testing/SKILL.md:30`,
  both among the files to change.
- **The other skill's `recognize.md`.** Item 2 has a session read a file of the other skill, which
  decision 5 does not list. Read as covered by the constraint on WAY-256 and WAY-265
  (`spec.md:54-55`): coding's and testing's step 3 name it, with its condition.
- **A joint task with fewer than two audits.** Who starts the other skill stays as unsaid as it is
  today, as the designer says. The revision does not worsen it.
- **An audit stopped, then the other audit dropped** because the human separates the work. No
  skill then ends the list and nothing in `final_review.md` would notice. Not reported: the case is
  rare, the earlier spec had it too, and the human sees the document whole at acceptance.
- **Naming the course in entry A's *Rationale*** and **`elements/glossary/template.md:50-51`** stand
  as the first review left them.

Stage: one author; report `docs/task-cycles/guidelines-audit-report/reports/author.md`.

- **WAY-13 uses "weight" for a task's process.** It is the ordinary sense, as the spec reads `weight`, so no glossary entry follows; the two meanings do stand in one log.
- **An audit stopped, then the other audit dropped**, which the review of the spec left unreported: no skill then ends the list. Unchanged by this change.

Stage: whole-change review; report `docs/task-cycles/guidelines-audit-report/reports/whole-review.md`.

- **WAY-281's "the rules of a linter's set":** whether it means the rules that block. Read so, with
  the reasons in finding 4.
- **The first item of a stopped audit's list.** "No number and no top" leaves unsaid whether the
  opening item, which names the top, stands at all. The audit that runs last writes it either way.
- **A cause placed partly on a place that shows no break.** "What does not hold is lowered or
  withdrawn" speaks of the whole cause; dropping one place from `Places:` is unsaid. An agent can
  do so without the text forbidding it.
- **A `do not copy` place that a linter's rule also reports:** `kinds.md:19-21` has its place stand
  in the `Places:` of its cause, while a linter's cause gives a number of files. Rare, and the list
  of `do not copy` keeps the line either way.
- **The part map's sentence on `product-guidelines`** (`foundations/part_map.md:157-159`) names the
  shared reading and not a shared end of the audits. The spec reads it as covered by "the skill that
  leads the work"; I agree, and the file is covered by `product-guidelines/**`.
- **The Glob tool** returned nothing for `product-guidelines/*/*`, and a Grep with a braced glob
  returned nothing. Both were false: `git ls-files` and `git grep` gave the files, and those are the
  results used here.

Stage: return step; report `docs/task-cycles/guidelines-audit-report/reports/return-step.md`.

- **Whether the two choices above bind as decisions:** unclear; the return step's "a choice that binds after the merge" and the spec's "No other entry" pull apart a little, and I followed the spec.
- **Finding 3's reach into `coding/recognize.md`:** the wording is the review's Minor finding and I left it. I name it because no entry disagrees with it: WAY-278 says what a refresh proposes and not which skill's step puts it.
- **WAY-284's complies example** reads "the backlog of an independent task"; the backlog is the product's. It matches the file in meaning, so I left it.
- **The Glob tool** was not used here; the comparisons rest on `git grep`, `grep` and whole reads.

Stage: review of the return step; report `docs/task-cycles/guidelines-audit-report/reports/return-review.md`.

- **What "a choice that binds after the merge" covers** where the choice stands in the text of a
  skill: `return_step.md`, `record_template.md:98-100` and WAY-36 do not say, and read literally they
  reach every sentence of a skill. I judged the two choices one by one, in finding 3.
- **`debt` where a set is only proposed.** The report says the rules that block "are rules the
  product's foundation holds". That is so once step 4 adopts the split; at the audit, on a first
  adoption, they are a proposal. WAY-281 keeps "debt" for what it reports then. No agent would act
  otherwise, so no finding.
- **`audit_end.md:131`, "for a linter's rules the number of files",** also lacks "that block". I read
  it as the label of a kind of cause and not as saying what enters the list, so it stands outside
  finding 1.
- **The Glob and Grep tools** were not used for any claim that something is absent; those rest on
  `git grep`.

Stage: fix; report `docs/task-cycles/guidelines-audit-report/reports/fix.md`.

none

Stage: review of the fix; report `docs/task-cycles/guidelines-audit-report/reports/return-review-2.md`.

none
