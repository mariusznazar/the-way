# Cycle record — settle-technology in the shape of WAY-256

- Task source: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_9_settle_technology.md; `Status: ready for cycle`, last updated 2026-10-30; frozen copy [task.md](task.md).
- Task relation: independent.
- Product repository: C:/Storage/repos/the-way (the-way itself), worktree C:/Storage/repos/the-way/.runs/worktrees/technology-skill-shape.
- Process pin: none; the-way works on itself, the process is this worktree at `525cde1dd53c474f56ea0ece289cb60e868aa90d`. No pin move.
- Target branch and base: `foundations`, `525cde1dd53c474f56ea0ece289cb60e868aa90d`. `git fetch origin foundations` matched the task's base: no source drift.
- Task branch: `task/technology-skill-shape`, created with `--no-track`.
- Status: request open

## Two questions at start

- Trust boundary: no. The change writes `project-level/technology/**`; the part `project-level` names `readiness_check.py`, `plan_check.py` and `plan_state.py` as its boundary, and none of them changes.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. *Settlements to record* reads `none` (0 of 6 candidates accepted); the task's To do items and questions 1–7 settle the shape, what stays and what moves, and the measurement. The names and division of the files beside the skill are choices of how to make what the task settles, reversible by a later edit, and bind nothing after the merge.
- Execution route and reason: one author without a plan; one skill in one part, a relocation whose fragments depend on each other, so splitting it would only add hand-offs.
- Author: fresh subagent, class `cheaper`, model sonnet (default class of step 4: ordinary implementation that takes decisions of its own, in one part, needing no design).
- Guidelines: empty selection; the-way has no `guidelines/` and the task's question 6 settles it; the change is Markdown only.
- Plan: none. Spec: none.
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` tool; subagents run in the background and report by completion notification, so the orchestrator yields the turn. No polling.
- Whole-change review: fresh reviewer, class same, opus, by `review-change`; 525cde1..c2e70f9, `FAIL c2e70f9f1e01e1ebfbeed0ff69352c498b674a8a`, [review.md](reports/review.md); 7 Markdown files, +203 -132. Final range 525cde1..c7a4008: 7 Markdown files, +204 -132. Every task item covered by name in the report; no settlement row or projected entry to carry; 37 quotations checked against 525cde1 and all route figures recounted independently. No plan: blocking findings come from the one author's commit and its reports.
- Review rounds: one. Whole change 525cde1..c2e70f9 FAIL with 2 Important: (1) a resuming leader whose human changes the list never reaches `list.md`; (2) route "leader, resuming, open choices" counted without `close.md`. Findings [findings.md](reports/findings.md); fix range c2e70f9..c7a4008 [fix.md](reports/fix.md); review of the fix `PASS c7a4008b48b09d17c76f120608c43e16cf544c33` [review-fix.md](reports/review-fix.md). No blocking finding remains.
- Weakest-point checks: author named rule preservation and reach; `checks/preservation.py` 71 pieces, 51 word for word, 20 listed with exact new wording, exit 0, negative control exit 1; `checks/reach.py` 77 assertions, later 82, exit 0, negative controls exit 1; both walks by hand in [author.md](reports/author.md). The reviewer noted both checks test presence of named text and took the route lists from the author, so neither could catch the two blocking findings; they came from the reviewer's own walk of the routes and recount. The fix extended `reach.py` to assert both cases, shown failing without the fix.

## Slices

Not applicable: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-10-30 | start | orchestrator, claude-opus-5-5 | frozen task, agent-instructions/README.md, task-cycle/skill/SKILL.md | task.md, this record | ready; no human action; branch and worktree created from fetched foundations |
| 2026-10-30 | baseline gate started | orchestrator | `python -B gate/run_tests.py` in the unchanged original checkout at 525cde1, background | .runs/base-gate-technology-skill-shape.log in the original checkout | running beside the author; its checkout does not hold the change |
| 2026-10-30 | author dispatch | fresh author, class cheaper, sonnet | [author-handoff.md](reports/author-handoff.md); make-change, variant "the whole change as the one author"; base 525cde1 | [author.md](reports/author.md) | done with concerns at c2e70f9; full report read for that status |
| 2026-10-30 | mechanical reading of the author's return | orchestrator | git status, git diff --numstat, git ls-files --eol, recount of the seven files at c2e70f9 | this record | clean worktree; non-empty range; 7 Markdown files in project-level/technology/, +203 -132; LF; private address; every check has command and exit code. Correction: author.md and its return give research.md 446, close.md 102 and the research route -1676, stale from before its last edit of research.md; the files hold 467 and 96, and reports/word-counts.md (467, 96, -1655) matches them, so word-counts.md is the source for the request |
| 2026-10-30 | whole-change review dispatch | fresh reviewer, class same, opus | [review-handoff.md](reports/review-handoff.md); review-change; 525cde1..c2e70f9; task, author report, assessment, counts | [review.md](reports/review.md) | FAIL c2e70f9: 2 Important (resuming leader whose human changes the list has no pointer to list.md; route count omits close.md), 5 Minor, 1 out of scope; focused checks exit 0; full gate not run by it |
| 2026-10-30 | fix dispatch | resumed author, class cheaper, sonnet | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md); make-change, variant "the fix of a review's findings"; fix base c2e70f9 | [fix.md](reports/fix.md) | done at c7a4008, +4 -3 in SKILL.md and start.md; focused checks exit 0, negative controls exit 1, full gate and project-level tests not run. Correction: fix.md:31 explains 6455 by 21 words of research.md and calls the reviewer's 6427 stale; research.md is on no leader route. Orchestrator's recount from git show: 6427 was right at c2e70f9, the fix adds 28 words (SKILL.md +7, start.md +21), so 6455; word-counts.md matches the recount on all five routes and is the source for the request |
| 2026-10-30 | review of the fix dispatch | same reviewer, resumed, opus | [review-fix-handoff.md](reports/review-fix-handoff.md); c2e70f9..c7a4008; findings.md, fix.md | [review-fix.md](reports/review-fix.md) | PASS c7a4008; both findings closed, no new blocking finding; 2 new Minor notes, on reports only; focused checks exit 0 |
| 2026-10-30 | full gate | orchestrator | `python -B gate/run_tests.py` on reviewed c7a4008 in the task worktree | [final-gate.log](final-gate.log) | exit 0 |
| 2026-10-30 | return step dispatch | resumed author, class cheaper, sonnet | [return-handoff.md](reports/return-handoff.md); return_step.md, foundation_step.md; head c7a4008 | [return.md](reports/return.md) | done; no correction, no commit, so no review of the return step |
| 2026-10-30 | reconciliation | orchestrator | `git fetch origin foundations; git merge --no-edit FETCH_HEAD` | head c7a4008, tree e95f1283743552f801ffae8e0050cc555abb91d4 | both exit 0, already up to date; final tree is the gated tree; no review or gate needed |
| 2026-10-30 | draft publication | orchestrator | `git push --set-upstream origin task/technology-skill-shape`; `gh pr create --draft --base foundations` | https://github.com/mariusznazar/the-way/pull/59 | both exit 0; upstream has the branch's own name |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the cycle need a copy of the methods at the base commit? Task question 5 | No: agents read their methods from the task worktree | task question 5; `task-cycle/` at 525cde1 names no `settle-technology` | copy at the base commit; one more step at the start | none: the cycle does not read this skill | all agents |
| Q2 | Does the cycle wait for the-way's own guidelines? Task question 6 | No: route of agent-instructions/README.md, empty guideline selection | task question 6 | waiting; the series stands still | none for a Markdown-only change | all agents |
| C2 | Files beside the skill and their names; author's choice 1 | `start.md`, `list.md`, `running_product.md`, `settle.md`, `research.md`, `close.md` | task question 7; WAY-256 | steps 0, 1, 3 left in SKILL.md; one file for steps 0 and 1 | one file more or fewer to keep | author, reviewer |
| C3 | Where the look at the running product stands; author's choice 2 | its own file, reached from `list.md` and `start.md` | acceptance criterion 3 | inside `list.md`, read whole by a resuming leader | a seventh file | author, reviewer |
| C4 | When a resuming leader reads `list.md`; author's choice 3, widened by review finding 1 | when the look adds an item or the human adds or changes one | review.md finding 1; fix.md | on every resume, +373 words | a leader adding an item without the rules names it badly | author, reviewer |
| C5 | Does the leader read `research.md`? author's choice 4 | no: it gives the path | task question 3 | leader reads it too, +446 words at that time | the leader cannot vouch for what it handed over | author, reviewer |
| C6 | Report name rule and foundation rule in two files; author's choice 5 | stand in both `SKILL.md` and `research.md` | acceptance criteria 3 and 4 | one copy and a pointer: one of the readers would not read it | two copies to keep in step | author, reviewer |
| C7 | Where the critique pointer stands; author's choice 6 | `SKILL.md` step 2 and sub-steps 4 and 5 of `settle.md` | To do 3 | bare "following `critique`"; pointer in `start.md` | a resume reads it late or early | author, reviewer |
| C8 | Person in `research.md`; author's choice 7 | second person | acceptance criterion 4 | third person, word for word | rewordings to check | author, reviewer |
| C9 | Glosses in `research.md`; author's choice 8 | the three matters, what a WAY reference is, the location sentences | acceptance criterion 4 | leaving terms unexplained | a new statement read as a rule | author, reviewer |
| C10 | Numbering of `settle.md`; author's choice 9 | stub items 2 and 3 keep the numbers | references to sub-steps | renumbering | 30 words | author, reviewer |
| C11 | Step numbers in moved files; author's choice 10 | named by step and file, except `define-project step 5` and `its step 4.1` | a file read by path has no numbering of the whole | keeping numbers | a reference goes stale | author, reviewer |
| C12 | Paths in moved files; author's choice 11 | `project-level/definition_template.md` and `elements/common/way_of_working.md` in full | acceptance criterion 2 | plain names | none significant | author, reviewer |
| C13 | Stale figures in author.md and fix.md | word-counts.md is the source for the request | orchestrator's recount from git show, confirmed by the reviewer | repairing the reports | none: the reports are archived as written, with their correction here | orchestrator, request |
| C1 | Which class for the one author? Step 4 | `cheaper`, sonnet | step 4's default; one part, one skill, no design left open | `same`, as tasks 3 chose for six parts | a weaker judgement of fragments, caught by the review of the whole change | author |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | [task.md](task.md) | source copy | accepted before the cycle |
| Author handoff | [reports/author-handoff.md](reports/author-handoff.md) | orchestrator | dispatched |
| Change | c2e70f9 | author | FAIL, 2 Important |
| Fix | c7a4008 | author | PASS |
| Author report | [reports/author.md](reports/author.md) | author | commands and exit codes complete; figures corrected under Events |
| Assessment and counts | [reports/assessment.md](reports/assessment.md), [reports/word-counts.md](reports/word-counts.md) | author | quotations and figures independently verified |
| Author's checks | [checks/](checks/) | author | scripts and outputs, not tracked by the change |
| Reviews | [reports/review-handoff.md](reports/review-handoff.md), [reports/review.md](reports/review.md), [reports/review-fix-handoff.md](reports/review-fix-handoff.md), [reports/review-fix.md](reports/review-fix.md) | orchestrator, reviewer | FAIL then PASS |
| Fix material | [reports/findings.md](reports/findings.md), [reports/fix-handoff.md](reports/fix-handoff.md), [reports/fix.md](reports/fix.md) | orchestrator, author | done |
| Return step | [reports/return-handoff.md](reports/return-handoff.md), [reports/return.md](reports/return.md) | orchestrator, author | no change, no review needed |
| Gate logs | [baseline-gate.log](baseline-gate.log), [final-gate.log](final-gate.log) | orchestrator | both exit 0 |
| Stages | [stages.md](stages.md) | orchestrator | written at the request |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `git fetch origin foundations; git rev-parse HEAD origin/foundations` | orchestrator, original Windows checkout | 0; both 525cde1dd53c474f56ea0ece289cb60e868aa90d | none |
| `python -B gate/run_tests.py` (baseline) | orchestrator, unchanged base 525cde1, original Windows checkout | 0; 614 tests in 8 directories, every directory passed; log [baseline-gate.log](baseline-gate.log) | no check failing on the base; 5 instruction-files checks skipped on Windows (4 POSIX-only, 1 FIFO), unrun, not passed |
| `python -B gate/run_tests.py` (final) | orchestrator, reviewed c7a4008, tree e95f1283743552f801ffae8e0050cc555abb91d4, task worktree on Windows | 0; 614 tests in 8 directories, every directory passed; log [final-gate.log](final-gate.log) | same 5 skips: test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does, test_an_absolute_link_out_of_the_repository_is_not_read, test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on, test_every_directory_link_is_reported_wherever_it_points, test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run |
| recount of every route from `git show` at c7a4008 | orchestrator | 0; 5111, 6828, 6455, 4738, 1621 | matches word-counts.md; the reviewer's own recount agrees |
| agent behaviour with the new files | not applicable | not run | no run exists; the task places it outside (question 4) |

Each author and reviewer check, with its command and exit code, stands in [author.md](reports/author.md), [fix.md](reports/fix.md), [review.md](reports/review.md) and [review-fix.md](reports/review-fix.md). No user interface, so no screenshot check. No invariant test altered.

## Return step

Taken by the resumed author on c7a4008: [return.md](reports/return.md). No commit, so no review of the return step.

- Foundation compared with code: the 16 decisions the task names, the part-map entry `project-level`, the glossary and three environment facts against the seven files, with a search of the whole foundation; nothing no longer matched.
- Decisions written or changed: none
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none written. "read off" and "gate" stand against their entries, in text unchanged in meaning from 525cde1; named in the request.
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: none

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/59, ready for review once the record's commits are pushed. Not merged.
- Cycle and its reasons: no spec, no open design choice; one author, class cheaper, one part and one skill; one review round with one fix.
- Process pin: none; the-way itself at 525cde1, no pin move.
- What this request settles: no foundation entry; no settlement row; no projected entry.
- What the foundation puts in front of the human at the merge: none.
- Checks: `python -B gate/run_tests.py` exit 0 on c7a4008; failed none; 5 named Windows skips did not run.
- Human actions the request waits for: none
- Questions: none
- Review findings listed: 7 Minor, 1 out of scope, in the request's body in the reviewer's words.
- Blocked by review: none
- Choices within the request: 15 rows, the questions table above.
- Writes to the task's backlog entry: none
- Process remarks on the-way, stage reports' *Searches not found or unclear*, word for word:
  - author, reports/author.md: "Environment facts `single-rule-compliance`, `instruction-density-accuracy`, `claude-skill-nested-references`, the glossary, and the guidelines (empty selection) were not read as files: the handoff lists them, but their content is quoted in `instruction-files/SKILL.md` and in WAY-256 and WAY-258, which I read whole. If the review needs a glossary reading of a term, it was not done here."
  - author, reports/author.md: "The Claude Code session records were not searched again; the task's Context states there is no invocation of the skill there."
  - author, reports/author.md: "The text the leader gave its research agents in the Codex run is encrypted in the rollout; read from `brief.md:13` instead."
  - author, reports/author.md: "No record shows an agent missing a rule of the skill (details in the assessment, section 2)."
  - author, reports/author.md: "The handoff says the task's Context line "Skrypt serii `skill_carry_cost.py` liczy każdy plik .md": I did not look for that script; it belongs to the next real use."
  - whole-change review, reports/review.md: "`author.md` choice 7 and the handoff say 9 changes of person in `research.md`. I find 7 verbs changed in 5 sentences: finds, gives, reads off, says, also says, writes, ends. Listing is not at issue, and no meaning changes on either count."
  - whole-change review, reports/review.md: "`author.md:102` sets 387 against the task's 800 and points to the assessment for the section list and bounds; `assessment.md` gives those but never mentions 800 (finding 3)."
  - whole-change review, reports/review.md: "`.claude/skills/` entry points state that they serve a session on the-way; a product's entry point was not read, since `installation/` did not change."
  - whole-change review, reports/review.md: "`cycle.md` not read, as the handoff requires."
- Other process remarks: the author's handoff named the glossary and three facts and the author left them to the return step, which read them; the reviewer's departure on WAY-139 onward stands in its report under *Reaches*. The Write tool and `pathlib.write_text` write CRLF in this environment; the author converted before committing. `reports/fix.md:31` explains the figures wrongly (corrected under Events and in the reviewer's note 3).
