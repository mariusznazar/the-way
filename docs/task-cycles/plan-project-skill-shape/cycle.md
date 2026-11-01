# Cycle record — plan-project in the WAY-256 shape

- Task source: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_6_plan_project.md; `Status: ready for cycle`, created and updated 2026-11-01; frozen copy [task.md](task.md).
- Task relation: independent.
- Product repository: C:/Storage/repos/the-way (the-way itself; route of agent-instructions/README.md); worktree C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape.
- Process pin: none; the-way works on itself, methods read from the task's worktree (task question 6).
- Target branch and base: `foundations`, `2f51e6c31f5911ac8a0292a80a4f599bd4bd0092`.
- Task branch: `task/plan-project-skill-shape`.
- Status: request open
- Source reconciliation: fetched origin/foundations equals the task's base 2f51e6c; no drift. The task's sources stand in the series note, whose "Ustalone" the cycle read whole.

## Two questions at start

- Trust boundary: no. The change touches Markdown files of `project-level/plan/skill/` and one sentence of `project-level/lead/skill/SKILL.md`; the part `project-level` names as boundary only `readiness_check.py`, `plan_check.py` and `plan_state.py`, which do not change (task acceptance).
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. Questions 1–7 and To do 1–9 settle what moves and what stays, *Settlements to record* is `none`, and the names and grouping of the files beside the skill that the task does not name are a choice of how to make what the task settles, made and named by the author (WAY-135).
- Reserved choice: none; the change adopts no technology.
- Execution route and reason: one author without a plan; one skill's relocation and one sentence elsewhere, all depending on one judgement (WAY-136).
- Author: fresh general-purpose agent, class `cheaper`, Sonnet 5.5 (orchestrator is Opus 5.5).
- Plan: none. Spec: none.
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code background agent, native completion notification; no polling.
- Whole-change review: fresh reviewer, Opus 5.5, review-change; 2f51e6c..db3845c, FAIL with 1 Important and 4 Minor, 3 lines out of scope ([review.md](reports/review.md)); 13 Markdown files +236/-156; fix db3845c..1fa823e, 1 file +2/-2, PASS 1fa823e with 2 new Minor and 2 lines out of scope ([review-fix.md](reports/review-fix.md)). Coverage of every task item and acceptance criterion and source fidelity reported; no settlement row and no projected entry. The reviewer read 70 decisions whole, every one of *Scope* `project-level`, of *Decisions in play* and those the moved text cites, and says the other 167 were not.
- Review rounds: one whole-change round, one fix and its review. Blocking: the sentence of `existing_plan.md` that has `read.md` read was given two effects by the materials, and routes 3 and 6 were counted on the reading task question 3 turned down. Closed at 1fa823e; no blocking finding remains.
- Weakest-point checks: author named rule preservation: base and rebuilt files compared sentence by sentence, 3 base sentences not verbatim, all pointers, each accounted for ([author.md](reports/author.md)); the reviewer repeated it with its own comparison (144 clauses, the same 3, 36 new), read each new clause for what it switches off, recomputed every figure and walked routes 2, 3, 4, 5 and 7 by hand. The sentence comparison could not see what the new sentence does, which the author raised as a concern and the reviewer made finding 1.

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

Not applicable: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-01 | start | orchestrator, Opus 5.5 | frozen task, agent-instructions/README.md, task-cycle/skill/SKILL.md | task.md | status ready for cycle; no human action; branch and worktree from fetched foundations 2f51e6c |
| 2026-11-01 | baseline gate started | orchestrator, Opus 5.5 | `python -B gate/run_tests.py` in the separate checkout `.runs/base-check` of the task's worktree at 2f51e6c | base-gate.log, base-gate.exit | running beside the author |
| 2026-11-01 | author dispatch | fresh author, Sonnet 5.5, class cheaper | [author-handoff.md](reports/author-handoff.md); task-cycle/change/SKILL.md, variant "the whole change as the one author"; base 2f51e6c | reports/author.md, reports/assessment.md, reports/word-counts.md | sent |
| 2026-11-01 | baseline gate complete | orchestrator, Opus 5.5 | as above; separate checkout removed | [base-gate.log](base-gate.log) | exit 0; 615 tests in 8 directories; no check failing on the base; 5 skipped |
| 2026-11-01 | author returned | fresh author, Sonnet 5.5 | as above | [author.md](reports/author.md); commit db3845c | done with concerns; checks, reaches and searches read. Mechanical check: clean worktree, 13 Markdown files +236/-156, LF, every check with command and exit code. Foundation reading partial, carried to the reviewer (C3) |
| 2026-11-01 | whole-change review dispatch | fresh reviewer, Opus 5.5 | [review-handoff.md](reports/review-handoff.md); task-cycle/review/SKILL.md; 2f51e6c..db3845c; frozen task, author report | reports/review.md | sent |
| 2026-11-01 | gate on the author's head started | orchestrator, Opus 5.5 | `python -B gate/run_tests.py` in the task worktree at db3845c, beside the read-only review | head-gate.log, head-gate.exit | running |
| 2026-11-01 | gate on the author's head complete | orchestrator, Opus 5.5 | as above | [head-gate.log](head-gate.log) | exit 0; 615 tests in 8 directories, every directory passed; 5 skipped |
| 2026-11-01 | whole-change review returned | fresh reviewer, Opus 5.5 | as above | [review.md](reports/review.md) | FAIL db3845c; 1 Important, 4 Minor, 3 lines declined as out of scope. Checks with exit codes complete; every decision of the part read whole |
| 2026-11-01 | fix dispatch | same author, Sonnet 5.5, resumed | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md); variant "the fix of a review's findings"; fix base db3845c | reports/fix.md | sent |
| 2026-11-01 | fix returned | same author, Sonnet 5.5 | as above | [fix.md](reports/fix.md); commit 1fa823e | done; the finding fixed, not contested; checks with exit codes; word counts regenerated after the last change |
| 2026-11-01 | review of the fix dispatch | same reviewer, Opus 5.5, resumed | [review-fix-handoff.md](reports/review-fix-handoff.md); db3845c..1fa823e | reports/review-fix.md | sent |
| 2026-11-01 | gate on the fix head started | orchestrator, Opus 5.5 | `python -B gate/run_tests.py` in the task worktree at 1fa823e, beside the read-only review | final-gate.log, final-gate.exit | running beside the review |
| 2026-11-01 | review of the fix returned | same reviewer, Opus 5.5 | as above | [review-fix.md](reports/review-fix.md) | PASS 1fa823e; finding 1 closed; 2 new Minor, 2 lines declined as out of scope; checks with exit codes complete |
| 2026-11-01 | return step dispatch | same author, Sonnet 5.5, resumed | [return-handoff.md](reports/return-handoff.md); task-cycle/skill/return_step.md and foundation_step.md; head 1fa823e | reports/return.md | sent |
| 2026-11-01 | return step returned | same author, Sonnet 5.5 | as above | [return.md](reports/return.md) | done; no change, no commit; head stays 1fa823e, so the return step has no review of its own (C6) |
| 2026-11-01 | gate on the fix head complete | orchestrator, Opus 5.5 | as above | [final-gate.log](final-gate.log) | exit 0; 615 tests in 8 directories, every directory passed; 5 skipped |
| 2026-11-01 | reconciliation | orchestrator, Opus 5.5 | `git fetch origin foundations`: still 2f51e6c, an ancestor of the head | none | no merge needed; the final tree is the gated one (C6) |
| 2026-11-01 | draft publication | orchestrator, Opus 5.5 | `git push --set-upstream origin task/plan-project-skill-shape`; `gh pr create --draft --base foundations` | PR 69 | both exit 0; upstream matches the branch |
| 2026-11-01 | assessment publication | orchestrator, Opus 5.5 | `gh pr comment 69 --body-file request-comments/assessment.md` | [comment](request-comments/index.md) | exit 0; whole table |
| 2026-11-01 | stage accounting | orchestrator, Opus 5.5 | `python -B task-cycle/cycle_stages.py 33b4f246-0e6f-405f-af21-13bb33c778c4 --output .runs/task-cycles/plan-project-skill-shape/stages.md` | [stages.md](stages.md) | exit 0; snapshot before the record's commits |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Where does the record live? (task-cycle/skill/SKILL.md step 5; "The cycle writes only in the task's worktree") | under the worktree's ignored `.runs/task-cycles/plan-project-skill-shape/` | the skill's text; the record of task/logging-guidelines stands there | the main checkout's `.runs/`, as some earlier cycles did | none: ignored either way | cycle |
| C2 | The task carries no row of *Settlements to record*: does the author take a foundation step? (task; implement-task step 9) | it writes no entry; a mismatch it finds goes to its report and to the return step | task *Settlements to record*: none; a search of the foundation finds no entry naming the sections that move | writing entries the task does not carry | a rule changed beyond the task | author, return step |
| C3 | The author read part of the handoff's foundation whole | carried to the reviewer, whose own selection covers the decisions the moved text cites; the return step reads every decision of *Decisions in play* whole | [author.md](reports/author.md) | a repair before the review | an unread decision's rule missed | review handoff, return handoff |
| C4 | Does "reads" in the last bullet of `existing_plan.md` make the session carry `read.md` out? (author's concern 3; review finding 1; task question 3 says "czyta go") | yes, and the sentence says so plainly; routes 3 and 6 are counted with step 1 carried out, the literal base beside it | task question 3: the way not chosen is a plan changed "bez fundamentu w głowie"; 14 of 14 sessions ran `readiness_check.py`, 11 reached `foundations/`; precedent `product-guidelines/testing/SKILL.md:79-81` | "reads" as sees and does not carry out, which leaves steps 1 of routes 4, 5a and 7 empty | a resumed draft reads more than a literal base did, about the foundation and guidelines words a route already pays | fix handoff |
| C5 | The reviewer lists Minor findings 2 to 7, some cheap to fix | not fixed; every Minor goes to the request, as "The end of a code review" gives | task-cycle/skill/SKILL.md, "The end of a code review" | fixing Minors in the round | a figure of the assessment reads 185 for 187; a reader loses nothing else | fix handoff, request |
| C6 | Review of the return step and of a merge | neither ran: the return step committed nothing, and the target did not move | step 11, step 12; head 1fa823e, `git merge-base --is-ancestor` | a review with nothing to review | none | request |
| A1 | One file per step 1-7 and four variant files | author's choice | [author.md](reports/author.md), choices | grouping steps 3-4; keeping steps 5-7 in `SKILL.md` | a little more upkeep | commit db3845c |
| A2 | Step 0's reading of the template and "Otherwise begin with step 1" stay in `SKILL.md` | author's choice | as above; WAY-256 | moving them, one instruction for one pointer | none | commit db3845c |
| A3 | Base lines 102-104 stand in the reading file, not in `SKILL.md` | author's choice; the reviewer confirmed the reach | as above; [review.md](reports/review.md) | keeping them in `SKILL.md` | about 55 words on every use the other way | commit db3845c |
| A4 | Step 0 pointer: "by the human or in a dispatched turn by its conversation file" | author's choice; the reviewer confirmed what it selects and listed a third source as Minor 4 | as above | the literal base wording, which would leave a dispatched turn without the file | a rare route with a wrong start | commit db3845c |
| A5 | A fragment needed in several places stays at its step and is restated where else it is needed | author's choice | as above | moving it to step 5 only | repeated text to change together | commit db3845c |
| A6 | The delegated file reaches steps 5-7 by an opener in each file and a clause in `SKILL.md` | author's choice | as above | one sentence in the delegated file, unseen when the step files are read | three short sentences to keep in line | commit db3845c |
| A7 | The condition of `guideline_tasks.md` carries "missing or uncertain" | author's choice; the reviewer found it widens only a read | as above | "missing" alone | an unneeded read of 176 words | commit db3845c |
| A8 | No entry written, none found out of line | author's choice | as above; [return.md](reports/return.md) | none | a mismatch missed | commit db3845c |
| A9 | Names of the eleven files | author's choice | as above | other names | none | commit db3845c |
| A10 | The readings of the routes the task leaves open (which steps run on routes 3, 4, 6, 7) | author's choice, stated in `word-counts.md` | as above; C4 for routes 3 and 6 | counting step 4 on route 4 | words of `place_questions.md` come on top where a question moves | word-counts.md |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | [task.md](task.md) | orchestrator | n/a |
| Change | commits db3845c, 1fa823e | author, Sonnet 5.5 | FAIL, then PASS 1fa823e |
| Assessment | [reports/assessment.md](reports/assessment.md), [published copy](request-comments/assessment.md) | author, Sonnet 5.5 | checked by the reviewer; Minor findings stand |
| Word counts | [reports/word-counts.md](reports/word-counts.md), `tools/word_counts.py`, `tools/verify_counts.py` | author, Sonnet 5.5 | every figure recomputed by the reviewer, 0 differ |
| Reports | [author](reports/author.md), [review](reports/review.md), [findings](reports/findings.md), [fix](reports/fix.md), [review of the fix](reports/review-fix.md), [return step](reports/return.md) | as named | n/a |
| Request text | [request-draft.md](request-draft.md) | orchestrator, Opus 5.5 | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (base, before any change) | orchestrator, 2f51e6c, separate checkout `.runs/base-check` deleted after the run, Windows | exit 0; 615 tests in 8 directories, every directory passed ([base-gate.log](base-gate.log)) | none failed; 5 skipped by the platform, unchecked (log line 30 `OK (skipped=5)`) |
| `python -B gate/run_tests.py` | orchestrator, db3845c, task worktree, Windows | exit 0; 615 tests in 8 directories ([head-gate.log](head-gate.log)) | none failed; the same 5 skipped |
| `python -B gate/run_tests.py` (reviewed change, the tree of the request) | orchestrator, 1fa823e, task worktree, Windows | exit 0; 615 tests in 8 directories ([final-gate.log](final-gate.log)) | none failed; the same 5 skipped: test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does, test_an_absolute_link_out_of_the_repository_is_not_read, test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on, test_every_directory_link_is_reported_wherever_it_points, test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run |
| `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`, `python -B agent-instructions/skill_entry_points.py --write` | author, db3845c, 1fa823e and at the return step | exit 0 each; `check_instructions.py` output as on the base; entry points unchanged | see the reports |
| Manual: walk of routes 2, 3, 4, 5 and 7, each assessment row against its place | reviewer, Opus 5.5, db3845c; routes 3 and 4 again at 1fa823e | not applicable; one blocking finding, then held | [review.md](reports/review.md), [review-fix.md](reports/review-fix.md) |

## Return step

- Foundation compared with code: every decision of *Decisions in play*, the decisions the moved text cites, the entries a search found and the part map entry `project-level` compared with the files at 1fa823e; nothing no longer matched ([return.md](reports/return.md))
- Decisions written or changed: none
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none; `project-level/**` covers the new files
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: none (the task carries none)

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/69, ready for review
- Cycle and its reasons: no spec, one author; see "Spec and execution route"
- Process pin: none; the-way works on itself
- What this request settles: no foundation entry; To do 4 and 5 change one sentence of `lead-project` and add the sentence that has a session on an existing plan go through step 1
- What the foundation puts in front of the human at the merge: none
- Checks: `python -B gate/run_tests.py`, exit 0; none failed; 5 skipped by the platform, named under *Verification*
- Human actions the request waits for: none
- Questions: none
- Review findings listed: Minor 2 to 5 of [review.md](reports/review.md), 6 and 7 of [review-fix.md](reports/review-fix.md), and the five lines of their *Declined to judge* as out of scope, in the request; no check failed and passed again
- Blocked by review: none
- Choices within the request: 16, in the questions table
- Writes to the task's backlog entry: none
- Process remarks on the-way, copied word for word from **Searches not found or unclear**:

- author (`reports/author.md`):

  - `gh pr view 51 --comments` returned nothing (no output); remarks of PR #51 were not read. The grep of the other six PRs found no remark about `plan-project`, its section names or its file path (only PR #50 names `task-cycle/plan/SKILL.md`, a different file). Mistake grounds in the table therefore read "not found in the records searched".
  - No session record was searched for the mistakes (the handoff names the git history, PR remarks and the task's Context; I did not open the Claude Code or Codex records).
  - The task does not say whether the dispatched turns of route 5 run step 1; I counted them as running it (concern in the route readings).
  - The task does not fix the readings of routes 3, 4, 6 and 7; the readings are mine and stated.
- fix (`reports/fix.md`):

  none
- review of the whole change (`reports/review.md`):

  - The handoff of the author says proposals stand "in rows of their own kind"; To do 9 asks only that
    the request give them. I read the first as a form, not a requirement (finding 5).
  - The task's question 3 says "czyta go" and its reasons speak both of what an agent saw and of the
    foundation in mind: unclear which it requires. Finding 1 rests on that.
  - The first search of the invariants was cut at 250 lines; I read the rest of the file directly.
- review of the fix (`reports/review-fix.md`):

  none
- return step (`reports/return.md`):

  - No glossary entry holds "step", "variant" or "pointer"; I judged them as used in their usual meaning.
  - Whether the human wants the C4 binding recorded as a decision is unclear; the task says no row (see above).
