# Cycle record - Align research and tool recommendations

- Task source: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/wyrownanie_researchu_testow.md; approved 2026-10-25; frozen in [task.md](task.md).
- Task relation: independent.
- Product worktree: C:/Storage/repos/the-way-wt/guidelines-research.
- Process pin and target base: 2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c.
- Target: foundations; task branch: task/guidelines-research, no tracking mismatch.
- Implementation and reviewed head: a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5.
- Status: final handoff in progress.
- Stage time, model and token evidence: [stages.md](stages.md), generated from the orchestrator and its child sessions.

## Two questions at start

- Trust boundary: no. Process guideline instructions and foundation prose hold none for this change.
- Irreversible operation: no. The change is text only. No human action outside the repository is needed.

## Spec and execution route

No open design choice: the approved task settles research triggers, refresh/extension definitions, recommendation criteria and preference precedence. One author without a plan holds the coherent change. No spec, plan, slices, discarded attempt or retry was needed. No fix/re-review round was needed.

Author: /root/author. Independent whole-change reviewer: /root/reviewer. Both inherited the orchestrator model; actual transcript model names are in stages.md. Agents waited through completion notifications or collaboration.wait_agent, at a maximum of 60 seconds to meet live progress-update instructions.

Whole-change review: PASS a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5; zero Critical, Important, Minor or out-of-scope findings. Full [review report](reports/review-report.md).

Weakest-point checks: manual tracing of seven scenarios found no mandatory research-report dependency on refresh or preference-only paths and no recommendation overriding a preferred tool. These were instruction walkthroughs, not executed refinement sessions.

## Events

| Stage | Actor | Handoff and inputs | Output and result |
|---|---|---|---|
| Start, 2026-10-25T01:19:11Z | Orchestrator | Frozen task, project instructions, foundation/guideline reading; fetched target | Ready task, isolated branch/worktree, no prerequisite human actions or source drift |
| Author dispatch | Orchestrator to /root/author | [Author handoff](reports/author-handoff.md), the-way-make-change, whole frozen task and named foundation entries | Implement and commit, return before review |
| Author clarification | Orchestrator | Task To do 1 versus old WAY-186 exception | C3 below; apply first-guidelines trigger to existing screens as well as preserve audit |
| Author return | /root/author | Same task and method | [Author report](reports/author-report.md), implementation a6453b7, done |
| Whole-review dispatch | Orchestrator to /root/reviewer | [Review handoff](reports/review-handoff.md), whole task, author report, range 2895e0e..a6453b7, the-way-review-change | Independent whole review |
| Whole-review return | /root/reviewer | Independent foundation/guideline reading and all changed files | PASS, no findings; checks and reaches read by orchestrator |
| Gate, 01:31:09 to 01:41:57 UTC | Orchestrator | Reviewed a6453b7, python -B gate/run_tests.py | Exit 0, 605 tests in 8 directories, five platform skips |
| Return-step dispatch | Orchestrator to /root/author | [Return handoff](reports/return-handoff.md), passing gate, frozen task and reports, make-change and cycle step 11 | Done; no mismatch, no changes or commit; all four settlements accounted for, no new reach or choice. See [return report](reports/return-report.md). |
| Target reconciliation | Orchestrator | git fetch origin foundations; git merge --no-edit origin/foundations | Exit 0, already up to date, tree/head unchanged |

All full dispatches and reports are kept in reports/. Times not captured in this table are available from the session-derived stage report where supported.

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Spec or slices needed? | One author, no spec or plan | All four settlements and To do 1-3 specify the result | Additional design/slicing | Revisit route if an open choice or excessive size appears | Author |
| C2 | Missing product guidelines a prerequisite? | No, this edits process and foundation prose, not executable code/tests/UI | Part map and changed files; guidelines directory absent | Treat skill text as product code | Reassess if scope reaches code/tests | Author and reviewer |
| C3 | First styleguide for existing screens: audit only? | Apply first-guidelines research trigger and preserve audit | Frozen task To do 1 explicitly covers all three skills and names WAY-186 as changing | Preserve old audit-only exception | More work for first styleguides without preference; otherwise task requirement would be missed | Author and reviewer |
| C4 | Where to record refresh/extension boundary? | New shared WAY-251, cited by three disciplines | Settlement 2 is an independently answerable shared question | Repeat independent definitions in three decisions | One extra reference; duplicates would drift | Foundation author |
| C5 | Add glossary terms? | No; ordinary meanings retained and operational rule lives in decision | Task settles classification, not a new product-specific meaning | Duplicate rule in glossary | Reconsider if a distinct meaning appears; duplication costs ongoing maintenance | Foundation author |
| C6 | Preference versus cheapest recommendation? | State preference precedence beside recommendation | Settlement 4 and preferred-tool clause | Rely on distant preference paragraph alone | Local repetition costs text, omission could override preference | Three skills and six decisions |
| C7 | Coding version/recommended rules without research? | Read chosen tool docs or product files directly | Existing sourcing obligation; refreshed flow skips alternative research | Require a research report anyway | Direct lookup still costs work; old requirement would make no-research paths impossible | Coding trial and initial recommendation |

No unresolved question, declined finding or unrecorded binding choice remains. All choices are the orchestrator/author's delegated interpretations, not new human approvals.

## Artifacts

| Kind | Path or commit | Author | Review |
|---|---|---|---|
| Frozen approved task | [task.md](task.md) | Human-approved source | Ready for cycle |
| Implementation | a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5 | /root/author | PASS |
| Author report | [author-report.md](reports/author-report.md) | /root/author | Checks/reaches inspected |
| Review report | [review-report.md](reports/review-report.md) | /root/reviewer | Independent PASS |
| Return report | [return-report.md](reports/return-report.md) | /root/author | Done; no mismatch, no changes or commit; all four settlements accounted for, no new reach or choice. See [return report](reports/return-report.md). |
| Request text | [pr-body.md](reports/pr-body.md) | Orchestrator | Includes settlement meanings, checks and limitations |
| Gate evidence | [result](reports/gate-result.json), [log](reports/gate.log) | Orchestrator | Exit 0 |

## Verification

| Command or manual check | Actor and tree | Exit/result | Failed or unchecked |
|---|---|---|---|
| python -B elements/common/foundation_check.py | Orchestrator, base 2895e0e | 0, zero errors | Full base gate not run; no known base failures |
| python -B elements/common/foundation_check.py | Author, implementation | Initial 0; intermediate 1; repaired and final 0 | Five Rejected labels joined to prior paragraphs during formatting; repaired |
| python -B agent-instructions/skill_entry_points.py | Author and reviewer, a6453b7 | 0, entry points current | Names, descriptions and paths unchanged; no regeneration needed |
| git diff --check | Author, implementation | 0 | None |
| git diff --check 2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c..a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5 | Reviewer | 0 | None |
| python -B elements/common/foundation_check.py | Reviewer, a6453b7 | 0 | None |
| python -B gate/run_tests.py | Orchestrator, a6453b7, Windows | 0; 605 tests in 8 directories | Five platform skips named below |
| Seven scenario walkthroughs | Author and independent reviewer | All task paths consistent | No actual fresh refinement session |
| Runtime/UI and screenshots | No executable code/UI change | Not applicable | No product runtime or screenshot check |
| New or changed invariant test | No invariant/test change | Not applicable | No first-failing test run |

Exact discovery commands and repeated focused checks, with exits, remain in the full author/reviewer reports. One intermediate multi-command batch ended with exit 0 despite a prior foundation check failing; author reran that check alone, captured exit 1 and corrected it before final success.

Five skipped tests in instruction-files/test_check_instructions.py:
- test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does (POSIX only).
- test_an_absolute_link_out_of_the_repository_is_not_read (POSIX only).
- test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on (POSIX only).
- test_every_directory_link_is_reported_wherever_it_points (POSIX only).
- test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run (requires os.mkfifo).

No wording-only tests added. Final published tree will be compared with the gated implementation after adding/removing the record, so that record-only commits cannot obscure a product change.

## Return step

Done; no mismatch, no changes or commit; all four settlements accounted for, no new reach or choice. See [return report](reports/return-report.md).

The return handoff carries the author's additional WAY-03 and element-skill reading and the reviewer's template/common-rule reaches via their full reports. It requires comparing edited/named/previously found entries and the map without a second whole-foundation hunt.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/43, draft; ready publication follows the record commit pair.
- Cycle and reasons: one author, no spec/plan; no discarded attempt; one independent whole review, no fix rounds.
- What this request settles: WAY-185/186/210/211/248/249 revised; new WAY-251 for settlement 2. Polish meanings and every row mapping are in [request text](reports/pr-body.md) and [author report](reports/author-report.md).
- No new foundation rule beyond the four settlements; no invariant, invariant test, public surface, Violated mark or glossary change.
- What the human accepts by merge: the three revised workflows and seven decision entries.
- Checks: full gate exit 0 and independent PASS; no open failure; platform skips and unexecuted refinement sessions explicitly named.
- Human actions or questions blocking request: none.
- Minor findings: none. Out-of-scope findings: none.
- Other choices: 7, table above.
- Writes to the task's backlog entry: Added [url::https://github.com/mariusznazar/the-way/pull/43] to the own task line in C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_tasks_active.md; state [>] unchanged; no vault commit.
- Process remarks on the-way: none.
- Archive/publication: after draft creation and stage accounting, copy this directory to docs/task-cycles/guidelines-research, commit the addition, immediately commit its removal, push both, link the adding SHA and mark ready. Do not merge; keep worktree for corrections.

## Publication evidence at snapshot

- Return report read: done, no changes, no new reaches/questions/choices. No repeat gate or review needed.
- Target reconciliation after return: git merge --no-edit origin/foundations, exit 0, already up to date.
- git push -u origin task/guidelines-research: exit 0, matching upstream.
- gh pr create --draft --base foundations --head task/guidelines-research --title "Align research and tool recommendations across guideline skills" --body-file docs/task-cycles/guidelines-research/reports/pr-body.md: exit 0, PR 43.
- task-cycle/cycle_stages.py with --output and session 01a170a1-ab5f-7990-a89c-0754fa138da8: exit 0, two child agents found, no warnings; see stages.md for its accounting through draft creation.
- Frozen task bytes still match source. Static unittest discovery identifies exactly the five named platform skips without rerunning tests.
- All dispatches, seven choices, checks, no-fix result and skipped spec/plan stages accounted for.
- Pending mechanical publication steps: record addition/removal commits, push, SHA link, ready flag, final tree equality check. This snapshot precedes its own adding commit.
