# Cycle record — maintain-coding-guidelines in the WAY-256 shape

- Task source: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_8_maintain_coding_guidelines.md; accepted 2026-10-31 (`Status: ready for cycle`); frozen copy [task.md](task.md).
- Task relation: independent.
- Product repository: C:/Storage/repos/the-way (the-way itself; route of agent-instructions/README.md); worktree C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape.
- Process pin: none; the-way works on itself, methods read from the task's worktree (task question 7).
- Target branch and base: `foundations`, `f86fd71f3cb72a9eb1620c388af44bbd1198fb4a`.
- Task branch: `task/coding-skill-shape`.
- Status: request open.
- Source reconciliation: fetched origin/foundations equals the task's base f86fd71; no drift.

## Two questions at start

- Trust boundary: no. The change touches product-guidelines (no boundary) and foundations/decisions.md (part decisions); no Python changes (task acceptance).
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. Questions 1–8 settle what changes and how, and rows 1–3 of *Settlements to record* settle the three edits in place of WAY-216 and WAY-266; the fifth mode's content is To do 9–13. The names and grouping of the files beside the skill not named by the task are a choice of how to make what the task settles, made and named by the author (WAY-135).
- Reserved choice: none. The skill's "New tools" stays on that skill's route (WAY-268); the change adopts no technology.
- Execution route and reason: one author without a plan; one skill's relocation with one new mode and two edits of the foundation, all depending on one judgement (WAY-136).
- Author: fresh general-purpose agent, class `cheaper`, Sonnet 5.5 (orchestrator is Opus 5.5).
- Plan: none. Spec: none.
- Discarded attempt: none.
- Slices returned too large: none.
- Agent waiting: Claude Code background agent, native completion notification; no polling.
- Whole-change review: fresh reviewer, Opus 5.5, review-change; f86fd71..097123e, FAIL with 2 Important and 6 Minor, 0 out of scope ([review.md](reports/review.md)); 12 Markdown files +292/-210; fix 097123e..088717a, 3 files +9/-8, PASS 088717a with 3 new Minor ([review-fix.md](reports/review-fix.md)). Coverage of every task item, acceptance criterion and settlement row and source fidelity reported; no projected entry. The reviewer read 87 decisions whole, every decision of *Decisions in play* and every one the moved text cites among them, and 65 of the 140 selected by *Scope* by heading only, and says so.
- Review rounds: one whole-change round, one fix and its review. Blocking: the opening of `task_document.md` dropped items of the task document on the route of one kind (same form at `settle.md`); the *Rationale* of WAY-216 held a reason no source gave, false of a trial run. Both closed at 088717a; no blocking finding remains.
- Weakest-point checks: author named rule preservation: base and rebuilt files compared sentence by sentence, 13 of 157 base pieces not verbatim, each accounted for ([author.md](reports/author.md)); the reviewer repeated it with its own comparison, recomputed every figure and walked the seven routes by hand. The sentence comparison could not see an added sentence that switches old ones off, which the reviewer found (finding 1).

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

Not applicable: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-10-31 | start | orchestrator, Opus 5.5 | frozen task, agent-instructions/README.md, task-cycle/skill/SKILL.md | task.md | status ready for cycle; no human action; branch and worktree from fetched foundations f86fd71 |
| 2026-10-31 | baseline gate started | orchestrator, Opus 5.5 | `python -B gate/run_tests.py` in the separate checkout `.runs/base-check` of the task's worktree at f86fd71 | base-gate.log, base-gate.exit | running beside the author |
| 2026-10-31 | baseline gate complete | orchestrator, Opus 5.5 | as above; separate checkout removed | [base-gate.log](base-gate.log) | exit 0; 615 tests in 8 directories; no check failing on the base; 5 skipped |
| 2026-10-31 | author dispatch | fresh author, Sonnet 5.5, class cheaper | [author-handoff.md](reports/author-handoff.md); task-cycle/change/SKILL.md, variant "the whole change as the one author"; task-cycle/skill/foundation_step.md; base f86fd71 | reports/author.md, reports/assessment.md, reports/word-counts.md | sent |
| 2026-10-31 | author returned | fresh author, Sonnet 5.5 | as above | [author.md](reports/author.md); commit 097123e | done with concerns; report read whole. Mechanical check: clean worktree, 12 Markdown files +292/-210, LF, every check with command and exit code. Foundation reading partial (12 decisions of the handoff read whole), carried to the reviewer. Search of WAY-33 shown. The author reads "the wider mode governs" as not covering "A new kind" with one kind, named unclear |
| 2026-10-31 | whole-change review dispatch | fresh reviewer, Opus 5.5 | [review-handoff.md](reports/review-handoff.md); task-cycle/review/SKILL.md; f86fd71..097123e; frozen task, author report | reports/review.md | sent |
| 2026-10-31 | gate on the author's head started | orchestrator, Opus 5.5 | `python -B gate/run_tests.py` in the task worktree at 097123e, beside the read-only review | head-gate.log, head-gate.exit | running |
| 2026-10-31 | gate on the author's head complete | orchestrator, Opus 5.5 | as above | [head-gate.log](head-gate.log) | exit 0; 615 tests in 8 directories, every directory passed; 5 skipped |
| 2026-10-31 | whole-change review returned | fresh reviewer, Opus 5.5 | as above | [review.md](reports/review.md) | FAIL 097123e; 2 Important, 6 Minor, 0 out of scope. Checks with exit codes complete; 65 of 140 selected decisions read by heading only, stated by the reviewer |
| 2026-10-31 | fix dispatch | same author, Sonnet 5.5, resumed | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md); variant "the fix of a review's findings"; fix base 097123e | reports/fix.md | sent |
| 2026-10-31 | fix returned | same author, Sonnet 5.5 | as above | [fix.md](reports/fix.md); commit 088717a | done; both findings fixed, none contested; checks with exit codes; word counts regenerated after the last change |
| 2026-10-31 | review of the fix dispatch | same reviewer, Opus 5.5, resumed | [review-fix-handoff.md](reports/review-fix-handoff.md); 097123e..088717a | reports/review-fix.md | sent |
| 2026-10-31 | gate on the fix head started | orchestrator, Opus 5.5 | `python -B gate/run_tests.py` in the task worktree at 088717a, beside the read-only review | final-gate.log, final-gate.exit | running |
| 2026-10-31 | review of the fix returned | same reviewer, Opus 5.5 | as above | [review-fix.md](reports/review-fix.md) | PASS 088717a; both findings closed; 3 new Minor; checks with exit codes complete |
| 2026-10-31 | return step dispatch | same author, Sonnet 5.5, resumed | [return-handoff.md](reports/return-handoff.md); task-cycle/skill/return_step.md and foundation_step.md; head 088717a | reports/return.md | sent |
| 2026-10-31 | return step returned | same author, Sonnet 5.5 | as above | [return.md](reports/return.md) | done; no change, no commit; head stays 088717a, so the return step has no review of its own (C6) |
| 2026-10-31 | gate on the fix head complete | orchestrator, Opus 5.5 | as above | [final-gate.log](final-gate.log) | exit 0; 615 tests in 8 directories, every directory passed; 5 skipped |
| 2026-10-31 | reconciliation | orchestrator, Opus 5.5 | `git fetch origin foundations`: still f86fd71, an ancestor of the head | none | no merge needed; the final tree is the gated one (C6) |
| 2026-10-31 | draft publication | orchestrator, Opus 5.5 | `git push --set-upstream origin task/coding-skill-shape`; `gh pr create --draft --base foundations` | PR 64 | both exit 0; upstream matches the branch |
| 2026-10-31 | assessment publication | orchestrator, Opus 5.5 | `gh pr comment 64 --body-file request-comments/assessment.md` | [comment](request-comments/index.md) | exit 0; whole table, 63710 bytes |
| 2026-10-31 | stage accounting | orchestrator, Opus 5.5 | `python -B task-cycle/cycle_stages.py 41f2056f-3658-4eef-997b-34fd0fc1aa7a --output .runs/task-cycles/coding-skill-shape/stages.md` | [stages.md](stages.md) | exit 0; snapshot before the record's commits |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Does WAY-251, narrowed by WAY-216, gain a link in its own *Relations*? (row 1; task *Decisions in play*: "brzmienie się nie zmienia") | no; the link is written once, on WAY-216 | foundations/decisions.md, the decision whose *Verification* gives as violating "a decision that another narrows names that other in its own *Relations* as well" | a link at both ends | none: that entry forbids it | author |
| C2 | Does the fifth mode and its rule of To do 10 reach the route "A new kind"? (To do 8, 9, 10) | no; To do 10 limits steps 4 and 5 on the one-kind route, and To do 8 keeps the contradiction of "A new kind" with the whole-product items as a proposal the cycle does not fix | task To do 8 and 10 | extending the limit to "A new kind" | a rule changed beyond the task | author, review |
| C3 | Remarks of PRs #50–#52, #59, #60, #62 (task *Out of scope*) against the judgement's search for mistakes | they are read as records of mistakes for the judgement, as in the series' earlier tasks; none is applied unless it settles a question of this task | task *Out of scope*; instruction-files judge mode | not reading them | a known fault of the shape repeated | author |
| C4 | "The wider mode governs" (To do 9) with the fifth mode and "A new kind", where neither is wider ([author.md](reports/author.md), [review.md](reports/review.md)) | both narrow modes run side by side; `kinds.md` stays read on that combination; named in the request | the fifth mode's conditions exclude the modes it could lose to; the reviewer holds it right and names `SKILL.md:71` | one mode switching the other off | a rule unused so far reads loosely; no real case stands behind it | author, request |
| C5 | Reviewer recommends fixing Minor finding 3 in the fix round | not fixed; every Minor goes to the request, as "The end of a code review" gives | task-cycle/skill/SKILL.md, "The end of a code review" | fixing Minors in the round | the assessment keeps its order; a reader loses nothing | fix handoff, request |
| C6 | Review of the return step and of a merge | neither ran: the return step committed nothing, and the target did not move | step 11, step 12; head 088717a, `git merge-base --is-ancestor` | a review with nothing to review | none | request |
| C7 | The author read part of the handoff's foundation whole | carried to the reviewer, whose selection widened; the return step read every decision of *Decisions in play* whole; named in the request | [author.md](reports/author.md), [return.md](reports/return.md) | a repair before the review | an unread decision's rule missed; the reviewer's selection covers the decisions the moved text cites | review handoff, return handoff |
| A1 | Rule of one kind in `SKILL.md`, with a one-line pointer at the head of `settle.md`, `hand_back.md` and `task_document.md` | author's choice | [author.md](reports/author.md), choices | the rule only in `SKILL.md` | about 70 words and a pointer kept in line | commit 097123e |
| A2 | "Extend what exists" and "A choice found in the product's files" in "Rules that hold across the steps" | author's choice | as above | `recognize.md` and `kinds.md`, which "A new kind" reads neither of | about 100 words carried by routes with no step 3 | commit 097123e |
| A3 | The reading of `AGENTS.md`, `guidelines/` and the foundation as the second bullet of `recognize.md` | author's choice | as above | first bullet, turning WAY-210's order around; third bullet, after the finding | an order rule weakened | commit 097123e |
| A4 | Fifth mode's condition "where that file stands" | author's choice | as above; WAY-202 | the one-kind route without a general file | a product without decisions of the standing checks | commit 097123e |
| A5 | The step 3 pointer splits the routes by what step 1 gave | author's choice | as above | "only the mode of one kind" | `kinds.md` off for one kind with a new kind | commit 097123e |
| A6 | `kinds.md` keeps the lead-in "Where the product has code:" with the one-kind sentence at "the audit covers every one of them" | author's choice | as above; To do 12 | another place for the sentence | a sentence misplaced | commit 097123e |
| A7 | WAY-216's *Verification*, *Rationale* and *Rejected* edited with it | author's choice; the *Rationale* corrected at 088717a to its sources | as above; [findings.md](reports/findings.md) | leaving them | an entry out of line with its sentences | commits 097123e, 088717a |
| A8 | Route 6 "before": counted as an ordinary run of the base | author's choice, stated beside the route | as above | no "before" figures | a comparison of a route that did not exist | word-counts.md |
| A9 | Proposals P1 and P2, not applied | author's choice, P2 not recommended | as above | applying them | a rule changed beyond the task | request |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | [task.md](task.md) | orchestrator | n/a |
| Change | commits 097123e, 088717a | author, Sonnet 5.5 | FAIL, then PASS 088717a |
| Assessment | [reports/assessment.md](reports/assessment.md), [published copy](request-comments/assessment.md) | author, Sonnet 5.5 | checked by the reviewer; Minor findings stand |
| Word counts | [reports/word-counts.md](reports/word-counts.md), `tools/word_counts.py`, `tools/verify_counts.py` | author, Sonnet 5.5 | 371 figures recomputed by the reviewer, 0 differ |
| Reports | [author](reports/author.md), [review](reports/review.md), [findings](reports/findings.md), [fix](reports/fix.md), [review of the fix](reports/review-fix.md), [return step](reports/return.md) | as named | n/a |
| Request text | [request-draft.md](request-draft.md) | orchestrator, Opus 5.5 | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (base, before any change) | orchestrator, f86fd71, separate checkout `.runs/base-check` deleted after the run, Windows | exit 0; 615 tests in 8 directories, every directory passed ([base-gate.log](base-gate.log)) | none failed; 5 skipped by the platform, unchecked (log line 30 `OK (skipped=5)`) |
| `python -B gate/run_tests.py` | orchestrator, 097123e, task worktree, Windows | exit 0; 615 tests in 8 directories ([head-gate.log](head-gate.log)) | none failed; the same 5 skipped |
| `python -B gate/run_tests.py` (reviewed change, the tree of the request) | orchestrator, 088717a, task worktree, Windows | exit 0; 615 tests in 8 directories ([final-gate.log](final-gate.log)) | none failed; the same 5 skipped: test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does, test_an_absolute_link_out_of_the_repository_is_not_read, test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on, test_every_directory_link_is_reported_wherever_it_points, test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run |
| `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`, `python -B agent-instructions/skill_entry_points.py --write` | author, 097123e and 088717a; reviewer | exit 0 each; `check_instructions.py` output as on the base; entry points unchanged | see the reports |
| Manual: walk of the seven routes, each assessment row against its place | reviewer, Opus 5.5, 097123e; route 6 again at 088717a | not applicable; one blocking finding, then held | [review.md](reports/review.md), [review-fix.md](reports/review-fix.md) |

## Return step

- Foundation compared with code: WAY-216, WAY-266, every decision of *Decisions in play* read whole, the entries the search found and the part map entry `product-guidelines` compared with the files at 088717a; nothing no longer matched ([return.md](reports/return.md))
- Decisions written or changed: WAY-216, WAY-266 (foundation step)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none; `product-guidelines/**` covers the new files
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 and row 2 WAY-216; row 3 WAY-266

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/64, ready for review
- Cycle and its reasons: no spec, one author; see "Spec and execution route"
- Process pin: none; the-way works on itself
- What this request settles: WAY-216, edited in place (rows 1 and 2): neither a kind's first file nor the comparison of an unindexed kind's files makes a task an extension under WAY-251 or takes research of the standing checks; the comparison covers that kind alone, takes no trial run and is no audit under WAY-201. WAY-266, edited in place (row 3): its last sentence goes
- What the foundation puts in front of the human at the merge: none
- Checks: `python -B gate/run_tests.py`, exit 0; none failed; 5 skipped by the platform, named under *Verification*
- Human actions the request waits for: none
- Questions: none
- Review findings listed: Minor 3 to 8 of [review.md](reports/review.md) and A to C of [review-fix.md](reports/review-fix.md), in the request; none out of scope; no check failed and passed again
- Blocked by review: none
- Choices within the request: 16, in the questions table
- Writes to the task's backlog entry: none
- Process remarks on the-way, copied word for word from **Searches not found or unclear**:

- author (`reports/author.md`):

  - `gh pr view 51 --comments` returned no output (a PR comment search found nothing); the remarks of #50, #52 and #59 do not
    mention this skill.
  - The task's "ca. 400 words more" and the upper bounds of the route estimates (see "Word counts") do not match my count.
  - "wider mode governs" (To do 9): for the one-kind mode combined with "A new kind", neither mode is wider; I read the rule
    as covering the combination of the one-kind mode with the audit modes and let both narrow modes run side by side.
    Unclear in the task; a reviewer should say if the other reading was meant.
  - The task's acceptance criteria says steps 1 and 3 "say themselves what they add to the document". Step 1 does (*To do* gains a
    part). Step 3's files say what step 4 proposes (violated invariant, reformatting) and the *Context* items stay in
    `task_document.md`, as in the base; I found no sentence in the base's step 3 that writes into *Context* itself.
  - Unclear: whether the sentence "At step 3 ... A new kind" in `SKILL.md` should state its own condition for a product that has
    code (the base's list reached it from the mode list); I left it with the mode list's wording.
- fix (`reports/fix.md`):

  None new. The unclear points of `author.md` stand (the reading of "the wider mode governs" for the one-kind mode with "A new
  kind").

  `python -B gate/run_tests.py installation` after the fix: exit 0, 44 tests OK.
- review of the whole change (`reports/review.md`):

  - **"Steps 1 and 3 say themselves what they add to the document" (acceptance criterion).** Step 3 adds
    nothing itself: neither base nor rebuilt step 3 writes into the document; it hands to step 4 ("The split
    goes to step 4 with its evidence"), and *Context* is written from `task_document.md` at step 4. The
    author read it this way (`author.md:202-204`). I take the criterion as describing the base, loosely,
    and find no gap: the evidence reaches the document on every route that makes it.
  - **"The wider mode governs" (To do 9).** The fifth mode's own conditions exclude the modes it could lose
    to (it needs `guidelines/coding.md`, and neither a refresh nor an extension), so the clause bites only
    on a task that also creates a new kind, where neither mode is wider. The author ran both side by side,
    which I think right: `SKILL.md:111` reads `kinds.md` there and the paragraph of "A new kind" still holds.
    But `SKILL.md:71` then says "only what concerns that kind" with two kinds in play. No real case stands
    behind it; the task's wording is kept as ordered. Recommended answer if asked: both kinds are settled,
    the standing checks are not.
  - **`author.md` on the WAY-216 *Rationale*:** flagged by the author as its own wording, which is what led
    to finding 2.
  - No other instruction, handoff or task passage was unclear.
- review of the fix (`reports/review-fix.md`):

  none
- return step (`reports/return.md`):

  None.
