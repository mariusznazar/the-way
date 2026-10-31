# Cycle record — maintain-testing-guidelines in the WAY-256 shape

- Task source: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_5_maintain_testing_guidelines.md; accepted 2026-10-31 (`Status: ready for cycle`); frozen copy [task.md](task.md).
- Task relation: independent.
- Product repository: C:/Storage/repos/the-way (the-way itself; route of agent-instructions/README.md); worktree C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape.
- Process pin: none; the-way works on itself, methods read from the task's worktree (task question 9).
- Target branch and base: `foundations`, `00c0a747272a9a179b7a855f256daff985ea2ee1`.
- Task branch: `task/testing-skill-shape`.
- Status: request open.
- Source reconciliation: fetched origin/foundations equals the task's base 00c0a74; no drift.

## Two questions at start

- Trust boundary: no. The change touches product-guidelines (no boundary), instruction-files/kind_skill.md and foundations/decisions.md; the only boundary of instruction-files is check_instructions.py, which the change does not touch.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. Questions 1–10 settle what changes and how; rows 1–3 of *Settlements to record* settle their entries; names and grouping of the files beside the skill are choices of how to make what the task settles, made and named by the author (WAY-135).
- Execution route and reason: one author without a plan; one skill's relocation, with one sentence in another skill, one answer in kind_skill.md and three settled foundation rows, all depending on one judgement (WAY-136).
- Author: fresh general-purpose agent, class `cheaper`, Sonnet 5.5 (orchestrator is Opus 5.5).
- Plan: none. Spec: none.
- Discarded attempt: none.
- Slices returned too large: none.
- Agent waiting: Claude Code background agent, native completion notification; no polling.
- Whole-change review: fresh reviewer, Opus 5.5, review-change; 00c0a74..5dc4b3b, FAIL with 5 Important and 5 Minor, 0 out of scope ([review.md](reports/review.md)); 14 Markdown files +326/-195; fix 5dc4b3b..c17f4f8, 5 files +17/-18, PASS c17f4f8 with 1 new Minor ([review-fix.md](reports/review-fix.md)). Coverage of every task item, acceptance criterion and settlement row and source fidelity reported; no projected entry. The reviewer read 40 of its 151 selected decisions whole and 111 by heading only, and says so.
- Review rounds: one whole-change round, one fix and its review. Blocking: stale word counts on all six routes; a mode the base and To do 3 do not have ("tests at a level its cycle chooses"); "Extend what exists" in the file of the first step, the layout WAY-256 names as violating; four binding sentences in WAY-256 against WAY-05; WAY-265's exemption not covering the styleguide skill. All closed at c17f4f8; no blocking finding remains.
- Weakest-point checks: author named rule preservation (acceptance 1): base and rebuilt files compared sentence by sentence, each base fragment not verbatim accounted for ([author.md](reports/author.md), [fix.md](reports/fix.md)), 18 at the head; the reviewer repeated it with its own comparison in both directions, recomputed every count and walked the six routes by hand twice. The author's check took a mode's meaning as preserved, which the reviewer refuted (finding 2).

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

Not applicable: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-10-31 | start | orchestrator, Opus 5.5 | frozen task, agent-instructions/README.md, task-cycle/skill/SKILL.md | task.md | status ready for cycle; no human action; branch and worktree from fetched foundations 00c0a74 |
| 2026-10-31 | baseline gate started | orchestrator | `python -B gate/run_tests.py` in the unchanged checkout C:/Storage/repos/the-way at 00c0a74 | base-gate.log, base-gate.exit | running beside the author in another worktree |
| 2026-10-31 | baseline gate complete | orchestrator | as above | [base-gate.log](base-gate.log) | exit 0; 614 tests in 8 directories, every directory passed |
| 2026-10-31 | author dispatch | fresh author, Sonnet 5.5, class cheaper | [author-handoff.md](reports/author-handoff.md); task-cycle/change/SKILL.md, variant "the whole change as the one author"; task-cycle/skill/foundation_step.md; base 00c0a74 | reports/author.md, reports/assessment.md, reports/word-counts.md | sent |
| 2026-10-31 | author returned | fresh author, Sonnet 5.5 | as above | [author.md](reports/author.md); commits 1c66173, d024d56 | done with concerns; report read whole. Mechanical check: clean worktree, 14 files +335/-191, Markdown only, LF, every check with command and exit code. Foundation reading partial, carried to the reviewer. The search of WAY-33 not shown; row 1 written as new WAY-265, named unclear |
| 2026-10-31 | author repair dispatch | same author, Sonnet 5.5, resumed | [author-repair-handoff.md](reports/author-repair-handoff.md); base d024d56 | reports/author-repair.md | sent; row 1 goes into WAY-256 in place (C6), the search of WAY-33 made, rows 2 and 3 renumbered |
| 2026-10-31 | author repair returned | same author, Sonnet 5.5 | as above | [author-repair.md](reports/author-repair.md); commit 5dc4b3b | done; row 1 in WAY-256, rows 2 and 3 are WAY-265 and WAY-266, search of WAY-33 made, no question. Mechanical check: clean worktree, 14 files +326/-195, every check with command and exit code |
| 2026-10-31 | whole-change review dispatch | fresh reviewer, Opus 5.5 | [review-handoff.md](reports/review-handoff.md); task-cycle/review/SKILL.md; 00c0a74..5dc4b3b; frozen task, author reports | reports/review.md | sent |
| 2026-10-31 | gate on the author's head started | orchestrator | `python -B gate/run_tests.py` in the task worktree at 5dc4b3b, beside the read-only review | head-gate.log, head-gate.exit | running |
| 2026-10-31 | gate on the author's head complete | orchestrator | as above | [head-gate.log](head-gate.log) | exit 0; result in *Verification* |
| 2026-10-31 | whole-change review returned | fresh reviewer, Opus 5.5 | as above | [review.md](reports/review.md) | FAIL 5dc4b3b; 5 Important, 5 Minor, 0 out of scope. Checks with exit codes complete; 111 of 151 selected decisions read by heading only, stated by the reviewer |
| 2026-10-31 | fix dispatch | same author, Sonnet 5.5, resumed | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md); variant "the fix of a review's findings"; fix base 5dc4b3b | reports/fix.md | sent |
| 2026-10-31 | fix returned | same author, Sonnet 5.5 | as above | [fix.md](reports/fix.md); commit c17f4f8 | done; all five fixed, none contested; 5 Markdown files +17/-18; clean worktree; checks with exit codes |
| 2026-10-31 | review of the fix dispatch | same reviewer, Opus 5.5, resumed | [review-fix-handoff.md](reports/review-fix-handoff.md); 5dc4b3b..c17f4f8 | reports/review-fix.md | sent |
| 2026-10-31 | gate on the fix head started | orchestrator | `python -B gate/run_tests.py` in the task worktree at c17f4f8, beside the read-only review | final-gate.log, final-gate.exit | running |
| 2026-10-31 | review of the fix returned | same reviewer, Opus 5.5 | as above | [review-fix.md](reports/review-fix.md) | PASS c17f4f8; all five closed; 1 new Minor; checks with exit codes complete; the reviewer ran the negative case the fix report left out |
| 2026-10-31 | gate on the fix head complete | orchestrator | as above | [final-gate.log](final-gate.log) | exit 0; result in *Verification* |
| 2026-10-31 | return step dispatch | same author, Sonnet 5.5, resumed | [return-handoff.md](reports/return-handoff.md); task-cycle/skill/return_step.md and foundation_step.md; head c17f4f8 | reports/return.md | sent |
| 2026-10-31 | return step returned | same author, Sonnet 5.5 | as above | [return.md](reports/return.md) | done; no change, no commit; head stays c17f4f8, so the return step has no review of its own |
| 2026-10-31 | reconciliation | orchestrator | `git fetch origin foundations`: moved to 2dbf1e7 (PR #61); `git merge --no-ff origin/foundations` | b510f40 | clean merge; only task-cycle/skill/SKILL.md comes in, no file of the change, so no review of the merge (C7); tree 94bcd63 differs from the gated one |
| 2026-10-31 | gate on the merged tree | orchestrator | `python -B gate/run_tests.py`, b510f40, task worktree | [merge-gate.log](merge-gate.log) | exit 0; result in *Verification* |
| 2026-10-31 | draft publication | orchestrator, Opus 5.5 | `git push --set-upstream origin task/testing-skill-shape`; `gh pr create --draft --base foundations` | PR 62 | both exit 0; upstream matches the branch |
| 2026-10-31 | assessment publication | orchestrator, Opus 5.5 | `gh pr comment 62 --body-file request-comments/assessment.md` | [comment](request-comments/index.md) | exit 0; whole table |
| 2026-10-31 | stage accounting | orchestrator, Opus 5.5 | `python -B task-cycle/cycle_stages.py 2ccd66d4-d0c4-460a-9f99-587b25362648 --output .runs/task-cycles/testing-skill-shape/stages.md` | [stages.md](stages.md) | exit 0; snapshot before the record's commits |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Who accepts the judgement, which instruction-files says edits wait for? | The frozen task does for keep, move and meaning-preserving rewordings; remove and meaning-changing reword stay proposals; the human reads them at the request | Task To do 1 and To do 7; series note, "Ustalone" | Stop for the human's acceptance of the table: the cycle has one human contact, the request | A move the human disagrees with comes back as a remark at the request | author, reviewer |
| C2 | instruction-files step 1 asks which tools and where sessions start | Claude Code and Codex by the project entry points, Cursor through the shared layout; sessions start in the-way's checkout or in a product that pins it | AGENTS.md "Skills"; installation/install.py entry points; task *Context* | Asking the human: the sources answer it | A loading path missed for one tool; pointers are plain "read `path`", which every tool carries out (WAY-129) | author |
| C3 | Which foundation entries does the author read? (WAY-150) | The selection in the handoff: the decisions in play, those whose *Scope* names a touched part and that concern tests, all guidelines, instruction files or skills, and those SKILL.md cites; the Scope's decisions only about styleguides or coding guidelines are left out | Scope search of foundations/decisions.md: 89 decisions, titles read | All 89: decisions on colour roles, linters and exemplars of code bear on no sentence moved here | A reach; the author names it and reads the entry | author |
| C4 | Question 8 says "WAY-256 się nie zmienia", while row 1 of *Settlements to record* is "Rozszerzenie WAY-256" | They do not collide: question 8 rejects a first-step exception to WAY-256; row 1 adds the case of question 2. Row 1 is written, and the third answer of kind_skill.md cites the entry that carries it | Frozen task, questions 2 and 8, row 1 and its last column | Treating question 8 as forbidding row 1: leaves row 1 unwritten | A reviewer reads the row otherwise and says so at the review | author, reviewer |
| C5 | How to treat the task's counts of 2835, 1336, 3187, 54, 322 and 509 words | As figures to check, not to assume; a difference is reported, never bent to | Task To do 2 and 7; series note on estimates | Copying them into the count | A wrong base for every route | author, reviewer |
| C6 | The author names as unclear whether row 1 extends WAY-256 itself, and wrote it as a new entry | Row 1 is an edit of WAY-256 in place; rows 2 and 3 stay entries of their own | elements/decisions/skill/decide_entry.md:9-10; WAY-30 on a row of *Settlements to record*; row 1's wording; *Decisions in play* marks only WAY-256 without "nie zmienia się" | Keep WAY-265 as a new entry deriving from WAY-256: a second answer to the question the log already answers | The human reads the row otherwise and asks for one more entry at the request; one entry's text moves | author, reviewer, request |
| C7 | The target branch moved to 2dbf1e7 during the cycle; does the merge need a review? | No: the merge brings task-cycle/skill/SKILL.md alone, a file the change does not touch and the skill does not read; the gate runs again on the merged tree | `git diff 00c0a74 origin/foundations --stat`; identifiers WAY-265 and WAY-266 free on the target | A fresh review of a merge that leaves the reviewed code as it was | A collision the gate does not see; the reviewed files are unchanged by the merge | request |
| A1 | File layout of the rebuilt skill (author) | Ten files beside the skill, one per step plus variants | author.md, choice 1 | One file for steps 2 and 3 | A file more or less | author, reviewer |
| A2 | "How to show" and "Write each answer" (author) | Stay in `SKILL.md` as rules that hold across steps | author.md, choice 2; WAY-256 | `how_to_show.md` named by steps 2 and 4 | About 130 words carried through steps that do not ask | author, reviewer |
| A3 | The new-level mode (author) | Reworded to what `product-guidelines/reading.md:77-78` says; its clause on a level the cycle chooses removed by the fix of finding 2 | author.md, choice 3; fix.md | Leaving the base's words | An agent on a level with no recipe skips step 2; guarded by the extension clause | author, reviewer |
| A4 | Foundation additions and trust boundaries (author) | Read at step 1, after the parts are named | author.md, choice 4; WAY-248 | Boundaries at step 3 only | Step 4 lacks them on one route | author, reviewer |
| A5 | When `product-guidelines/template.md` is read (author) | Step 4, as in the styleguide skill | author.md, choice 5 | Step 2 | A starting set drafted without the general form, caught at step 4 | author, reviewer |
| A6 | Step 3's pointer (author) | Names `audit.md` and `new_level.md` directly and separately | author.md, choice 6 | `audit.md` pointing on to `new_level.md` | The new-level agent reads the audit first | author, reviewer |
| A7 | Row 1 as a new entry (author) | Superseded by C6: written into WAY-256 in place | author.md, choice 7; author-repair.md | Kept as a new entry | See C6 | discarded in 5dc4b3b |
| A8 | The exemption in the entry of row 3, now WAY-266 (author) | "Skills of guidelines whose text stands unchanged are not bound by it until they are rebuilt" | author.md, choice 8 | No clause: the coding skill breaches the entry on the day of the merge | The human wanted it to bind all three at once; drop the clause | author, reviewer, request |
| A9 | *Rejected* of the entries (author) | The ways not chosen of questions 2, 3 and 4, without counts; "two levels as in task 4" rendered as the variant named only in the step's file | author.md, choice 9 | Copying the lines with their counts | One line of WAY-265's *Rejected* reads the question otherwise than the human meant | author, reviewer |
| R1 | Place of the new sentence in WAY-256 (author) | Within the binding paragraph, joined to the closing sentence after finding 4 | author-repair.md, choice 1; findings.md, 4 | A separate paragraph | The paragraph reads densely | author, reviewer |
| R2 | Wording of WAY-256's *Rationale* (author) | The author's own words from what the removed entry carried, no count or file name | author-repair.md, choice 2 | Copying that entry's text | None seen | author, reviewer |
| F1 | Form of the moved cycle's-choice sentence (author) | Inside the exemplar item of `settle.md`, its full stop now a semicolon | fix.md, choice 1 | A bullet of its own | The reviewer declined to judge it | author, reviewer |
| F2 | Order of "Extend what exists" in `SKILL.md` (author) | Last among the rules before "Write each answer" | fix.md, choice 2 | First | None | author, reviewer |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | [task.md](task.md) | source copy | accepted 2026-10-31 |
| Author handoff and report | [author-handoff.md](reports/author-handoff.md), [author.md](reports/author.md) | orchestrator, author | concerns read; own figures superseded by fix.md and word-counts.md |
| Repair before review | [author-repair-handoff.md](reports/author-repair-handoff.md), [author-repair.md](reports/author-repair.md) | orchestrator, author | done |
| Assessment and counts | [assessment.md](reports/assessment.md), [word-counts.md](reports/word-counts.md), [sentence-diff.txt](reports/sentence-diff.txt) | author | rechecked independently by the reviewer |
| Change | 1c66173, d024d56, 5dc4b3b, c17f4f8; merge b510f40 | author; orchestrator for the merge | FAIL, then PASS c17f4f8 |
| Whole-change review | [review-handoff.md](reports/review-handoff.md), [review.md](reports/review.md) | orchestrator, reviewer | FAIL: 5 Important, 5 Minor |
| Fix | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md), [fix.md](reports/fix.md) | orchestrator, author | done |
| Review of the fix | [review-fix-handoff.md](reports/review-fix-handoff.md), [review-fix.md](reports/review-fix.md) | orchestrator, reviewer | PASS, 1 new Minor |
| Return step | [return-handoff.md](reports/return-handoff.md), [return.md](reports/return.md) | orchestrator, author | no change, no commit |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `git fetch origin foundations`; `git rev-parse HEAD origin/foundations`; `git status --short` | orchestrator, C:/Storage/repos/the-way, Windows | 0; both 00c0a74; clean | none |
| `python -B gate/run_tests.py` | orchestrator, base 00c0a74, C:/Storage/repos/the-way, Windows | 0; 614 tests in 8 directories, every directory passed ([base-gate.log](base-gate.log)) | no failure on the base; skips as the log names them (unrun, not passed) |
| `python -B gate/run_tests.py` | orchestrator, author's head 5dc4b3b, task worktree, Windows | 0; 614 tests in 8 directories, every directory passed ([head-gate.log](head-gate.log)) | no failure; same 5 skips (unrun, not passed); head reviewed FAIL, so the gate runs again on the fixed tree |
| `python -B gate/run_tests.py` | orchestrator, reviewed head c17f4f8, task worktree, Windows | 0; 614 tests in 8 directories, every directory passed ([final-gate.log](final-gate.log)) | no failure; same 5 instruction-files checks skipped on Windows (unrun, not passed) |
| `python -B gate/run_tests.py` | orchestrator, merged head b510f40, tree 94bcd63, task worktree, Windows | 0; 614 tests in 8 directories, every directory passed ([merge-gate.log](merge-gate.log)) | no failure; same 5 instruction-files checks skipped on Windows (unrun, not passed) |

## Return step

- Foundation compared with code: WAY-256, WAY-265, WAY-266, each decision of *Decisions in play*, each entry the search found and the part-map entries of product-guidelines, instruction-files and decisions, compared with the files at c17f4f8; nothing no longer matches ([return.md](reports/return.md)).
- Decisions written or changed: WAY-256 changed in place; WAY-265 and WAY-266 new (foundation step).
- Invariants written or changed: none.
- Environment facts: none.
- Glossary terms: none.
- Part-map changes: none.
- Projected entries written whole or in part: none.
- Rows of *Settlements to record* written: 1 — WAY-256; 2 — WAY-265; 3 — WAY-266.

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/62; opened as a draft, marked ready after the record's commits. Not merged.
- Cycle and its reasons: no spec, no open design choice; one author without a plan; one repair before review, one whole-change review with one fix and its review.
- Process pin: none; the-way works on itself, base 00c0a74, foundations 2dbf1e7 merged at b510f40.
- What this request settles: WAY-256 changed, row 1; WAY-265 new, row 2; WAY-266 new, row 3; meaning sentences in the request.
- What the foundation puts in front of the human at the merge: none.
- Checks: `python -B gate/run_tests.py`, exit 0 on b510f40, 614 tests in 8 directories; 5 instruction-files checks skipped on Windows, named in the request; none failed. No agent session was run on the rebuilt skill.
- Human actions the request waits for: none.
- Questions: none.
- Review findings listed: Minor findings 6 to 10 of [review.md](reports/review.md) and 11 of [review-fix.md](reports/review-fix.md) in the reviewer's words, in the request; findings outside the task's scope: none.
- Blocked by review: none.
- Choices within the request: 20, in the questions table.
- Writes to the task's backlog entry: none.
- Process remark of the orchestrator: the report of the author did not show the search of the foundation, and the foundation's text says the search leaves no record, so a report that omits it cannot be told from a search not made; the orchestrator asked for it in a repair. The base gate ran in the unchanged main checkout at 00c0a74, as the cycle's text stood when it started; PR #61, merged during the cycle, now names a separate checkout under `.runs/` or a run before anything changes.
- Process remarks of the stages, copied word for word:

- Stage author, report .runs/task-cycles/testing-skill-shape/reports/author.md, **Searches not found or unclear**:
  - No remark of PRs #50, #51, #52, #59 or #60 (their comments, reviews and inline comments, read by `gh pr view <n> --comments` and `gh api`) mentions this skill; #51 has no comment. No mistake that a fragment of this skill was added for was found in the five commits of its history (judged from their messages and the PRs; I did not read the five diffs line by line).
  - `rg`-style search for incoming references to sections of this skill (`What reaches the task document`, `A new level`, `Starting set`, `Orchestrated mode`) found them only inside this skill and in `product-guidelines/coding/SKILL.md`, which has its own sections of the same names (not touched). `product-guidelines/reading.md:79`, `testing/template.md:7`/`:105`, `project-level/task/skill/guideline_findings.md`, `project-level/plan/skill/SKILL.md:122` and `installation/*` name the skill, not a section.
  - The task text "`product-guidelines/testing/SKILL.md:53-54`" (the name "Writing the file") is the template's section; it stands in `task_document.md` unchanged and the template's `## Writing the file` exists (`template.md:264`).
  - Unclear: whether row 1 should extend WAY-256 itself (choice 7); what "two levels as in task 4" in Question 3 means exactly (concern 2).
  - Nothing else was looked for and not found.
- Stage whole-change review, report .runs/task-cycles/testing-skill-shape/reports/review.md, **Searches not found or unclear**:
  - Unclear: `author.md` describes choices 7 and 8 in the old form; its repair note says so, and I judged the tree.
  - Unclear: whether row 2's "pliki" means a skill's every file or the step and variant files. I took the second, which the row's own example requires.
  - Otherwise none.
