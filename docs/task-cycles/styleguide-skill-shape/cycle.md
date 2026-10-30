# Cycle record — maintain-styleguide in the WAY-256 shape

- Task source: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_4_maintain_styleguide.md; accepted 2026-10-30 (`Status: ready for cycle`); frozen copy [task.md](task.md).
- Task relation: independent.
- Product repository: C:/Storage/repos/the-way (the-way itself; route of agent-instructions/README.md); worktree C:/Storage/repos/the-way/.runs/worktrees/styleguide-skill-shape.
- Process pin: none; the-way works on itself, methods read from the task's worktree (task question 5).
- Target branch and base: `foundations`, `525cde1dd53c474f56ea0ece289cb60e868aa90d`.
- Task branch: `task/styleguide-skill-shape`.
- Status: request open.
- Source reconciliation: fetched origin/foundations equals the task's base 525cde1; no drift.

## Two questions at start

- Trust boundary: no. The change touches product-guidelines (no boundary) and instruction-files/kind_skill.md; the only boundary of instruction-files is check_instructions.py, which the change does not touch.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. Question 2 settles that every step's procedure goes beside the skill; question 1 settles which files change; To do 3 settles the meaning of kind_skill.md. Names and grouping of the files beside the skill are choices of how to make what the task settles, made and named by the author (WAY-135).
- Execution route and reason: one author without a plan; one skill's relocation with one sentence's correction in another part, which depend on one judgement (WAY-136).
- Author: fresh general-purpose agent, class `cheaper`, Sonnet 5.5 (orchestrator is Opus 5.5).
- Plan: none. Spec: none.
- Discarded attempt: none.
- Slices returned too large: none.
- Agent waiting: Claude Code background agent, native completion notification; no polling.
- Whole-change review: fresh reviewer, Opus 5.5, review-change; 525cde1..802b56d, FAIL with 2 Important and 6 Minor, 0 out of scope ([review.md](reports/review.md)); 12 Markdown files +211/-173; fix 802b56d..d32f76d, one file +2/-1, PASS d32f76d with 2 Minor in fix.md ([review-fix.md](reports/review-fix.md)). Coverage of every task item and acceptance criterion and source fidelity reported; no settlement row or projected entry.
- Review rounds: one whole-change round, one fix and its review. Blocking: the word counts left out the section "Reading the foundation", read twice on the base; recognize.md had the session read again the guidelines refine-task read. Both closed at d32f76d; no blocking finding remains.
- Weakest-point checks: author named rule preservation (acceptance 1): base and rebuilt files compared sentence by sentence, 15 base fragments not verbatim, each accounted for ([author.md](reports/author.md), [fix.md](reports/fix.md)); the reviewer repeated it with its own comparison, 18 clauses, and walked the seven routes.

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

Not applicable: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-10-30 | start | orchestrator, Opus 5.5 | frozen task, agent-instructions/README.md, task-cycle/skill/SKILL.md | task.md | status ready for cycle; no human action; branch and worktree from fetched foundations 525cde1 |
| 2026-10-30 | baseline gate started | orchestrator | `python -B gate/run_tests.py` in the unchanged checkout C:/Storage/repos/the-way at 525cde1 | base-gate.log, base-gate.exit | running beside the author in another worktree |
| 2026-10-30 | author dispatch | fresh author, Sonnet 5.5, class cheaper | [author-handoff.md](reports/author-handoff.md); task-cycle/change/SKILL.md, variant "the whole change as the one author"; base 525cde1 | reports/author.md, reports/assessment.md, reports/word-counts.md | sent |
| 2026-10-30 | author returned | fresh author, Sonnet 5.5 | as above | [author.md](reports/author.md); commits b63f7cd, 802b56d | done with concerns; report read whole. Mechanical check: clean worktree, 12 Markdown files +211/-173, no Python, every check with command and exit code. Author read 23 listed decisions, and the part-map entries, invariants and glossary terms, not whole; carried to the reviewer, who selects and reads its own foundation |
| 2026-10-30 | whole-change review dispatch | fresh reviewer, Opus 5.5 | [review-handoff.md](reports/review-handoff.md); task-cycle/review/SKILL.md; 525cde1..802b56d; frozen task, author report | reports/review.md | sent |

| 2026-10-30 | whole-change review returned | fresh reviewer, Opus 5.5 | as above | [review.md](reports/review.md) | FAIL 802b56d; 2 Important, 6 Minor, 0 out of scope. Reviewer read 21 of the 23 decisions the author left unread (WAY-155 and the tail of WAY-134 excepted), none broken. Checks with exit codes complete |
| 2026-10-30 | fix dispatch | same author, Sonnet 5.5, resumed | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md); variant "the fix of a review's findings"; fix base 802b56d | reports/fix.md | sent |
| 2026-10-30 | fix returned | same author, Sonnet 5.5 | as above | [fix.md](reports/fix.md); commit d32f76d | done; recognize.md +2/-1, materials regenerated; clean worktree; checks with exit codes; gate tests of the author's directories not rerun, the fix being one line of Markdown they do not read |
| 2026-10-30 | review of the fix dispatch | same reviewer, Opus 5.5, resumed | [review-fix-handoff.md](reports/review-fix-handoff.md); 802b56d..d32f76d | reports/review-fix.md | sent |
| 2026-10-30 | gate on the fix head started | orchestrator | `python -B gate/run_tests.py` in the task worktree at d32f76d; beside the read-only review | final-gate.log, final-gate.exit | running |
| 2026-10-30 | review of the fix returned | same reviewer, Opus 5.5 | as above | [review-fix.md](reports/review-fix.md) | PASS d32f76d; both findings closed; 2 Minor in fix.md, not in the commit; checks with exit codes complete. Return step waits for the gate, since it may commit |
| 2026-10-30 | gate on the fix head complete | orchestrator | `python -B gate/run_tests.py`, d32f76d, tree aae9118 | [final-gate.log](final-gate.log) | exit 0; 614 tests in 8 directories, every directory passed; same 5 Windows skips |
| 2026-10-30 | return step dispatch | same author, Sonnet 5.5, resumed | [return-handoff.md](reports/return-handoff.md); return_step.md and foundation_step.md | reports/return.md | sent |
| 2026-10-30 | return step returned | same author, Sonnet 5.5 | as above | [return.md](reports/return.md) | done; no change, no commit; head stays d32f76d |
| 2026-10-30 | reconciliation | orchestrator | `git fetch origin foundations`; origin/foundations 525cde1 is an ancestor of the head | none | nothing to merge; the tree stays aae9118, the gated one |
| 2026-10-30 | draft publication | orchestrator, Opus 5.5 | `git push --set-upstream origin task/styleguide-skill-shape`; `gh pr create --draft --base foundations` | PR 60 | both exit 0; upstream matches the branch |
| 2026-10-30 | assessment publication | orchestrator, Opus 5.5 | `gh pr comment 60 --body-file request-comments/assessment.md` | [comment](request-comments/index.md) | exit 0; whole table, 50 rows and 2 proposals |
| 2026-10-30 | stage accounting | orchestrator, Opus 5.5 | `python -B task-cycle/cycle_stages.py da5f3fbe-3569-48c8-a993-d28779b79354 --output .runs/task-cycles/styleguide-skill-shape/stages.md` | [stages.md](stages.md) | exit 0, no warnings; snapshot before the record's commits |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | What does a route's word count hold? Task To do 4 and question 3 say a file read twice in "before" counts twice; the task's estimate 8850 → 5900 leaves refine-task's own first reading out | Count every read of the route, refine-task's first reading of a file the skill makes the session read again included, in both states; add one line per route without those first reads, so the figures meet the task's estimate | Task To do 4, question 1 (Source), question 3; project-level/task/skill/read_sources.md:3-4 | Counting only what the skill itself makes read: the "twice" of question 3 would have no first read to stand on | Percentages differ between the two bases; the absolute saving is the same, and both are shown | author, reviewer, request |
| C2 | Which state of the human does route 3, "pierwszy styleguide, są ekrany", take? Task To do 4 does not say | No preference, so research and audit both run, the longest form of that route; stated beside the route | Task To do 4 | The human with a preference: hides the cost of research on a route that has it | One route's figure answers a slightly different question; it is labelled | author, reviewer, request |
| C3 | Who accepts the judgement, which judging.md says edits wait for? | The frozen task does for keep, move and meaning-preserving rewordings; remove and meaning-changing reword stay proposals; the human reads them at the request | Task To do 1 and To do 4; series note, "Ustalone" | Stop for the human's acceptance of the table: the cycle has one human contact, the request | A move the human disagrees with comes back as a remark at the request | author, reviewer |
| C4 | instruction-files step 1 asks which tools and where sessions start | Claude Code and Codex by the project entry points, Cursor through the shared layout; sessions start in the-way's checkout or in a product that pins it | AGENTS.md "Skills"; installation/install.py entry points; task Context (20 session records, 7 in `loop2`) | Asking the human: the sources answer it | A loading path missed for one tool; pointers are plain "read `path`", which every tool carries out (WAY-129) | author |
| C5 | Which foundation entries does the author read? (WAY-150) | The selection in the handoff: the decisions in play, those whose *Scope* names a touched part and that concern a styleguide or all guidelines, and those SKILL.md cites; the Scope's decisions only about coding guidelines or tests are left out | Scope search of foundations/decisions.md: 89 decisions, titles read | All 89: decisions on linters, exemplars and test levels bear on no sentence moved here | A reach; the author names it and reads the entry | author |
| A1 | File layout of the rebuilt skill (author) | Ten files beside the skill, one per step plus variants | author.md, choice 1 | Fewer files with variants inside the step's file | Small variants cost a pointer each | author, reviewer |
| A2 | "How to show" and "Write each answer" (author) | Stay in `SKILL.md` as rules that hold across steps | author.md, choice 2; WAY-174 | Place them in settle.md with step 4: they would stop reaching steps 1 and 2 | About 150 more words in `SKILL.md` | author, reviewer |
| A3 | The list of what reaches the task document (author) | `task_document.md`, read at step 4 and checked at step 5 | author.md, choice 3 | Keep in `SKILL.md`, or read at step 1 | An entry written at step 2 without it; the task template gives the form | author, reviewer |
| A4 | When each template is read (author) | Styleguide template at step 2, template of guidelines at step 4 | author.md, choice 4; reviewer checked both | Both at step 2 | One template read later than a step needs it | author, reviewer |
| A5 | When the critique files are read (author) | At the first critique: step 2 where research ran, else step 4 | author.md, choice 5 | One pointer in `SKILL.md` for both critiques | An agent misjudges whether step 2 read it | author, reviewer |
| A6 | Where variant pointers stand (author) | In the step's file, not in `SKILL.md` | author.md, choice 6; refine-task's read_sources.md has the same shape | In `SKILL.md`, one level deep | Two levels deep, against a principle of instruction-files that names no decision; review Minor 4 | author, reviewer, request |
| A7 | Step 5 (author) | A file of its own, two instructions | author.md, choice 7 | Stay in `SKILL.md` | One small file more | author, reviewer |
| A8 | Order inside step 1 (author) | The product's `AGENTS.md` and `guidelines/` read after the interface is named | author.md, choice 8; WAY-185 | Read them before naming the interface | A product without an interface reads less; the order differs from the base's step 0 | author, reviewer |
| A9 | The refresh clause (author) | Stays in starting_rules.md, with the pointer to research.md | author.md, choice 9 | With the research | None seen | author, reviewer |
| A10 | Proposals P1 and P2 (author) | Not applied; both change a rule's meaning | author.md, choice 10; task To do 4 | Apply them | Waiting for a separate change | author, reviewer, request |
| C6 | Review finding 8 asks the orchestrator to confirm word-counts.md:8: do the files refine-task sends the session to (read_sources.md, draft.md, resolve_gaps.md, reading.md and others) count? | No; the stated exclusion stands: they are equal in both states and leave the difference unchanged | review.md finding 8; C1's purpose, setting the figures beside the task's estimate | Counting them: the absolute saving stays the same and the comparison with the estimate blurs | Percentages rest on a narrower base; the exclusion is stated in the materials | fix author, reviewer, request |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | [task.md](task.md) | source copy | accepted 2026-10-30 |
| Author handoff and report | [author-handoff.md](reports/author-handoff.md), [author.md](reports/author.md) | orchestrator, author | concerns read; own account superseded by fix.md |
| Assessment and counts | [assessment.md](reports/assessment.md), [word-counts.md](reports/word-counts.md) | author | rechecked independently by the reviewer |
| Change | b63f7cd, 802b56d, d32f76d | author | FAIL, then PASS d32f76d |
| Whole-change review | [review-handoff.md](reports/review-handoff.md), [review.md](reports/review.md) | orchestrator, reviewer | FAIL: 2 Important, 6 Minor |
| Fix | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md), [fix.md](reports/fix.md) | orchestrator, author | done |
| Review of the fix | [review-fix-handoff.md](reports/review-fix-handoff.md), [review-fix.md](reports/review-fix.md) | orchestrator, reviewer | PASS, 2 Minor |
| Return step | [return-handoff.md](reports/return-handoff.md), [return.md](reports/return.md) | orchestrator, author | no change, no commit |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `git fetch origin foundations`; `git rev-parse HEAD origin/foundations`; `git status --short` | orchestrator, C:/Storage/repos/the-way, Windows | 0; both 525cde1; clean | none |
| `python -B gate/run_tests.py` | orchestrator, base 525cde1, C:/Storage/repos/the-way, Windows | 0; 614 tests in 8 directories, every directory passed ([base-gate.log](base-gate.log)) | no failure on the base; 5 instruction-files checks skipped on Windows (unrun, not passed) |
| `python -B gate/run_tests.py` | orchestrator, reviewed head d32f76d, tree aae91187, task worktree, Windows | 0; 614 tests in 8 directories, every directory passed ([final-gate.log](final-gate.log)) | no failure; same 5 instruction-files checks skipped on Windows (unrun, not passed) |

## Return step

- Foundation compared with code: the task's *Decisions in play*, each whole, and the part-map entries of product-guidelines and instruction-files, compared with the rebuilt files; nothing no longer matches ([return.md](reports/return.md)). Searches for what points at a moved section or step, and for another copy of what kind_skill.md:8-14 said, found nothing to correct.
- Decisions written or changed: none.
- Invariants written or changed: none.
- Environment facts: none.
- Glossary terms: none.
- Part-map changes: none.
- Projected entries written whole or in part: none.
- Rows of *Settlements to record* written: none.

The step committed nothing, so it has no review of its own. The author's comparison left out 20 decisions of its handoff's list; the reviewer read them whole, the tail of WAY-134 excepted, and none is broken by the change.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/60; opened as a draft, marked ready after the record's commits. Not merged.
- Cycle and its reasons: no spec, no open design choice; one author without a plan; one whole-change review with one fix and its review.
- Process pin: none; the-way works on itself, base 525cde1.
- What this request settles: no foundation entry; no row of *Settlements to record*.
- What the foundation puts in front of the human at the merge: none.
- Checks: `python -B gate/run_tests.py`, exit 0 on d32f76d, 614 tests in 8 directories; 5 instruction-files checks skipped on Windows, named in the request; none failed. No agent session was run on the rebuilt skill.
- Human actions the request waits for: none.
- Questions: none.
- Review findings listed: the Minor findings of [review.md](reports/review.md) and [review-fix.md](reports/review-fix.md) in the reviewer's words, in the request; findings outside the task's scope: none.
- Blocked by review: none.
- Choices within the request: 16, in the questions table.
- Writes to the task's backlog entry: none.
- Process remark of the orchestrator: a shell command of the orchestrator stalled on a stray `cat` waiting for input and was stopped before it wrote anything; the record was then updated by edits. No effect on the repository.
- Process remarks of the stages, copied word for word:

- Stage author, report .runs/task-cycles/styleguide-skill-shape/reports/author.md, **Searches not found or unclear**:
  - A mistake any fragment of the file was added for, in the history of the file and in PRs #50, #51, #52: not found (see concern 5).
  - A recorded definition of "first reads" in the task or the foundation: not found; I took the handoff's rule (the first reading of the three files step 0 had the session read again) and stated it in `word-counts.md`.
  - Where the task's estimates of 8850 and 5900 words come from, beyond "`SKILL.md` 2830 and about 6000 words of step 0 files": unclear; my route 2 figures are explained above.
  - Whether `tools/` under `.runs/task-cycles/styleguide-skill-shape/` should hold helpers: the handoff says so; they are untracked (`.runs/` is ignored by git).
- Stage whole-change review, report .runs/task-cycles/styleguide-skill-shape/reports/review.md, **Searches not found or unclear**:
  - A statement anywhere in `word-counts.md` that "Reading the foundation" was left out on purpose: not found (finding 1).
  - How often sessions open `maintain-styleguide` directly rather than through refine-task: not found; the records are outside this worktree (finding 6).
  - Whether WAY-256 sends a fragment of two steps beside the skill or keeps it in `SKILL.md`: unclear from its text (finding 3).
  - Whether "one instruction" in WAY-256 covers a sentence with a rider: unclear (finding 5).
  - For the orchestrator, unverified and from memory: GitHub limits a request's body to 65536 characters, as far as I recall. `assessment.md` is 50209 characters and `word-counts.md` 18081, 68290 together, so the two may not fit in one body.
- Stage fix, report .runs/task-cycles/styleguide-skill-shape/reports/fix.md, **Searches not found or unclear**:
  - The composition of the task's estimate of about 5900 words: not found in the task or the foundation (see above).
  - Whether other base reads of step 0 repeat a refine-task read besides the four now counted: I compared each item of base step 0 and `read_sources.md` again; the only other overlap is the root `AGENTS.md`, which refine-task reads in its `## Backlog` section only, so the whole file is a different read. Not found beyond the four.
- Stage review of the fix, report .runs/task-cycles/styleguide-skill-shape/reports/review-fix.md, **Searches not found or unclear**:
  - One sentence in the task stating how 5900 was reached: not found; Minor 2 is my inference from its figures.
  - GitHub's limit on a request's body, from the first review: now tighter, as `assessment.md` grew to 50929 bytes and `word-counts.md` to 20005; still unverified and from memory.
