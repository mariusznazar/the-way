# Cycle record — the way: lżejsza ścieżka cyklu dla małej zmiany bez zmiany fundamentu

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\lzejsza_sciezka_cyklu_dla_malej_zmiany.md`;
  approved 2026-10-08 (the vault is not committed, so no source commit); frozen copy: `task_frozen.md`
- Task relation: independent
- Product repository: `C:\Storage\repos\the-way` (the-way itself; worktree `C:\Storage\repos\the-way-light-path`)
- Process pin: none — the-way has no `.the-way` submodule; the base commit c64a6071384fb57cdb9d7e9db4560ddc43e3b355
  takes the pin's place, and the skill, record template, element skills and critique are read from it.
  The gitlink check does not apply.
- Target branch and base: `foundations` at c64a6071384fb57cdb9d7e9db4560ddc43e3b355 (origin/foundations
  fetched 2026-10-08T01:15 and equal to the expected base)
- Task branch: `task/light-path-small-change` (created `--no-track`; upstream set to the same-name remote
  branch at first push)
- Foundation route: entry change — WAY-13/1 and WAY-125/1 edited in place (no main branch, guide);
  dependents found at start: invariant foundation-change-path/1 (*Derives from* WAY-13@c6b33aa9);
  the whole-foundation search (WAY-33) is in the foundation step
- Status: request open

## Sharpness at start and after the final diff

| When | Criticality and touched parts | Trust-boundary files | Reversibility | Consequent checks |
|---|---|---|---|---|
| start (01:18) | high — task-cycle (three high failure modes, not detected), decisions (high, not detected); invariants if a *Derives from* fingerprint moves (no failure modes recorded) | none — no touched file is a trust boundary of its part | reversible — text in a pinned process; a product takes it only by moving its pin; a revert undoes it | full subagent review loop; no WAY-48 adversarial input checks; nothing to stage for a human decision |
| final diff c64a607..5bbc817 (02:33) | high — same parts: task-cycle, decisions, invariants (one link); no new part | none | reversible | unchanged; nothing grew |

Unknown failure modes count as the highest criticality. Record the reason for each assessment,
then recalculate from the final diff. An irreversible operation waits for the human's decision at
the request; preparing reversible code for it does not authorize executing it.

## Events

| Time | Stage | Actor and model | Skill and input | Output or report | Result and next step |
|---|---|---|---|---|---|
| 01:15 | inputs | orchestrator, Opus 5.5 | fetch origin; `git rev-parse origin/foundations` | c64a607 = expected base | base unchanged; continue |
| 01:15 | inputs | orchestrator | read task, `agent-instructions/README.md`, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, `elements/common/critique/SKILL.md`, `elements/decisions/skill/SKILL.md`, `elements/common/skill/SKILL.md`, part map, WAY-10..14, WAY-124..126 at base (snapshot via `git archive c64a607`) | — | task `Status: ready for cycle`, relation independent; continue |
| 01:16 | inputs | orchestrator | `installed_plugins.json` | superpowers 6.4.1 at `~/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1` (git 5bf4e78); Agent tool available | harness requirement met |
| 01:16 | start | orchestrator | `git worktree add --no-track -b task/light-path-small-change ../the-way-light-path c64a607` | worktree | created; user.email <author email> |
| 01:17 | baseline | orchestrator | see Verification (baseline) | `reports/baseline-*.txt` | all green apart from `task-cycle` holding no tests |
| 01:20 | design | design agent (general-purpose, Opus 5.5 inherited) | Superpowers 6.4.1 `brainstorming`, frozen task, binding sources; prompt `reports/01-design-prompt.md` | `spec.md`, `reports/01-design-report.md` | dispatched; boundary: self-reviewed spec, questions returned first |
| 01:34 | design | design agent | — | `spec.md` (469 lines), `reports/01-design-report.md` | returned after 14 min 54 s, 58 tool uses, ~251k tokens; classification architectural (followed regardless, as the cycle requires); no questions; 15 choices D1–D15 for the orchestrator's ruling |
| 01:36 | spec review | spec reviewer (general-purpose, Opus 5.5 inherited; not the designer) | step 7; prompt `reports/02-spec-review-prompt.md` | `reports/02-spec-review.md` | dispatched |
| 01:42 | spec review | spec reviewer | — | `reports/02-spec-review.md` | Issues Found (3) + advisory R1–R7; 6 min 52 s, 36 tool uses, ~190k tokens; no requirement missing |
| 01:42 | baseline | orchestrator | glossary guard `--base none --merge-onto none` at c64a607 | `reports/baseline-glossary-guard.txt` | 0 errors, 0 warnings, 5 unchecked (R3) |
| 01:42 | design (revision 1) | design agent, resumed | rulings C2–C6 below sent by message | `spec.md`, `reports/01-design-report.md` "Revision 1" | dispatched |
| 01:44 | design (revision 1) | design agent | — | `spec.md` revised | returned after 1 min 55 s, 27 tool uses; all rulings applied; WAY-13 fp 97b17d59, WAY-125 fp 68b2d563 (base 4c302238); WAY-125 binding part 246 words (base 140) |
| 01:45 | spec go-ahead | orchestrator | — | — | provisional go-ahead for planning without a second spec review (C7) |
| 01:45 | plan | planner (general-purpose, Opus 5.5 inherited) | Superpowers 6.4.1 `writing-plans`; prompt `reports/03-plan-prompt.md` | `plan.md`, `reports/03-plan-report.md` | dispatched |
| 01:58 | plan | planner | — | `plan.md` (995 lines), `reports/03-plan-report.md` | returned after 13 min 25 s, 71 tool uses, ~221k tokens; no questions; dry run of every old/new text, fingerprints, guards and tests on a scratch clone at c64a607 |
| ~01:58 | plan review | orchestrator | step 8: coverage, source fidelity, order, runnable commands | — | plan covers spec §4, §6, §7, §11; Task 1 is the foundation step; departures 1–5 of the planner accepted (C8); provisional go-ahead for execution |
| ~01:58 | foundation step | foundation-step agent (general-purpose, Opus) | plan Task 1 via `record-decision`, `record-invariant`; prompt `reports/04-foundation-step-prompt.md` | `reports/04-foundation-step-report.md` | dispatched |
| ~02:00 | foundation step | foundation-step agent | steps 1–2 (read, WAY-33 search) | `reports/04-foundation-step-report.md` | stopped before step 3 with finding F1 (WAY-29 vs D13); searches as the plan expects; no edit; 3 min 15 s, 25 tool uses |
| ~02:00 | foundation step | foundation-step agent, resumed | ruling C9 | — | dispatched to continue from step 3 |
| 02:05 | foundation step | foundation-step agent | steps 3–13 | commit b977e5f; `reports/04-foundation-step-report.md`, `reports/t1-*.txt` | done (agent's own durations: 3 min 15 s + 6 min 31 s, 62 tool uses, ~299k tokens); every check as the plan expects; numstat `67 35` decisions (plan `68 35`, difference from C9), `1 1` invariants; fp WAY-13 97b17d59, WAY-125 68b2d563 |
| 02:05 | execute | orchestrator | Superpowers 6.4.1 `subagent-driven-development` setup: `sdd-workspace`, `task-brief` 2 and 3 | `.superpowers/sdd/plan/` (self-ignored), ledger `progress.md` with pre-flight scan | scan clean; one ruling (no tests for text-only tasks) |
| 02:06 | execute T2 | implementer (general-purpose, Sonnet) | brief `task-2-brief.md`; prompt `reports/05-task2-implementer-prompt.md`; BASE b977e5f | `task-2-report.md` | dispatched |
| 02:07 | execute T2 | implementer | — | commit 3bf1452; `task-2-report.md` | DONE in 1 min 25 s, 14 tool uses, ~73k tokens; numstat 62 12; gate 96 OK, installation 16 OK; task-cycle NO TESTS RAN |
| 02:07 | review T2 | task reviewer (general-purpose, Sonnet) | `task-reviewer-prompt.md`; brief, report, package `review-b977e5f..3bf1452.diff`; prompt `reports/06-task2-review-prompt.md` | `task-2-review.md` | dispatched |
| 02:08 | review T2 | task reviewer | — | `task-2-review.md` | spec ✅, quality approved; 0 critical, 0 important, 2 minor deferred (orphan short lines; foundation step's plan-member sentence has no light counterpart); 47 s |
| 02:08 | execute T3 | implementer (general-purpose, Sonnet) | brief `task-3-brief.md`; prompt `reports/07-task3-implementer-prompt.md`; BASE 3bf1452 | `task-3-report.md` | dispatched |
| 02:10 | execute T3 | implementer | — | commit c64d49a; `task-3-report.md` | DONE in 1 min 39 s, 11 tool uses, ~68k tokens; numstat 21 2; did not run the brief's word-diff reading |
| 02:10 | review T3 | task reviewer (general-purpose, Sonnet) | brief, report, package `review-3bf1452..c64d49a.diff`; prompt `reports/08-task3-review-prompt.md` | `task-3-review.md` | dispatched; asked to run the skipped word-diff reading |
| 02:11 | review T3 | task reviewer | — | `task-3-review.md` | spec ✅ (word-diff reading clean), quality approved; 2 minor deferred; 44 s |
| 02:11 | final review | final reviewer (general-purpose, Opus) | `requesting-code-review` `code-reviewer.md`; package `review-c64a607..c64d49a.diff`; prompt `reports/09-final-review-prompt.md` | `final-review.md` | dispatched |
| 02:12 | verify | orchestrator | step 10 checks on c64d49a (see Verification) | `reports/post-*.txt` | all as expected; fingerprints recomputed: WAY-13 97b17d59, WAY-125 68b2d563, carriers match |
| 02:18 | final review | final reviewer | — | `final-review.md` | With fixes: 0 critical, 1 important (WAY-125's touch clause not confined to the executor's work), 4 minor; ledger minors: none blocking; agrees with C9; 6 min 48 s, 34 tool uses, ~152k tokens |
| 02:19 | final fix | foundation-step agent, resumed (Opus; author of b977e5f) | ruling C10; SDD single fix dispatch | `reports/04-foundation-step-report.md` "Fix C10" | dispatched |
| 02:20 | final fix | foundation-step agent | — | commit 70f6bda | done in 1 min 30 s; WAY-125 fp 68b2d563 → f4d471cc (no carrier); decisions guard 0/7/5; decisions 169 OK; gate 96 OK |
| 02:20 | final re-review | re-reviewer (general-purpose, Sonnet) | `re-review-prompt.md`; package `review-c64d49a..70f6bda.diff`; prompt `reports/10-final-rereview-prompt.md` | `final-rereview.md` | dispatched |
| 02:21 | final re-review | re-reviewer | — | `reports/sdd/final-rereview.md` | Important 1 ADDRESSED, no new breakage; 24 s |
| 02:21 | verify | orchestrator | fingerprints recomputed on 70f6bda | — | WAY-13 97b17d59 (carriers match), WAY-125 f4d471cc (no carrier) |
| 02:21 | execute close | orchestrator | SDD finish: ledger, briefs, reports and reviews copied to `reports/sdd/` (review-package diffs not copied — git holds them: ranges b977e5f..3bf1452, 3bf1452..c64d49a, c64a607..c64d49a, c64d49a..70f6bda); `.superpowers/sdd/plan/` deleted | `reports/sdd/` | SDD rulings listed in `reports/sdd/progress.md` |
| 02:21 | return step | orchestrator | WAY-11 on c64a607..70f6bda and the choice log | "Return step" below | nothing further to write |
| 02:21 | assessment | independent assessor (general-purpose, Sonnet; the entries' authors ran on Opus) | `elements/common/critique/SKILL.md`; diff c64a607..70f6bda and `git archive 70f6bda` only, outside the repository; prompt `reports/11-assessment-prompt.md` | scratchpad `assess/assessment.md` → `reports/11-assessment.md` | dispatched |
| 02:22 | reconcile | orchestrator | `git fetch`; origin/foundations moved c64a607 → 4c19290 (PR #6, 1b22169: `installation/README.md` only) | — | no foundation or task-cycle file changed at the tip; WAY-33 search of the base holds for the tip (foundation files identical); merge of the tip planned after the settlement |
| 02:27 | assessment | independent assessor | — | `reports/11-assessment.md` | 7 observations (O1 main), 3 cuts; fingerprints and guard verified; 5 min 47 s, 28 tool uses, ~145k tokens |
| 02:28 | settlement | orchestrator | each remark settled (see Independent assessment); commit message with the assessment record written by the orchestrator | scratchpad `commit-msg-settlement.txt` | 2 cuts applied, 1 cut and O1–O7 rejected or noted |
| 02:28 | settlement | settlement agent (general-purpose, Sonnet) | prompt `reports/12-settlement-prompt.md` | `reports/12-settlement-report.md` | dispatched |
| 02:30 | settlement | settlement agent | — | commit 9318492 (message carries the assessment record) | 2 cuts applied; WAY-125 fp unchanged f4d471cc; decisions guard 0/7/5; decisions, gate OK; 1 min 23 s |
| 02:30 | settlement review | code reviewer (general-purpose, Sonnet) | `requesting-code-review` `code-reviewer.md`; range 70f6bda..9318492; prompt `reports/13-settlement-review-prompt.md` | `reports/13-settlement-review.md` | dispatched |
| 02:30 | reconcile | orchestrator | `git merge --no-ff origin/foundations` (4c19290) | merge commit adcfcc8 | only `installation/README.md` enters; no conflict (C12) |
| 02:31 | verify | orchestrator | all checks on adcfcc8 (see Verification) | `reports/final-*.txt` | as expected; fingerprints match; foundation files identical at base and tip |
| 02:31 | settlement review | code reviewer | — | `reports/13-settlement-review.md` | approved, no findings; 36 s |
| 02:32 | request | orchestrator | `git push -u origin task/light-path-small-change` (upstream = same-name remote branch); `gh pr create --draft --base foundations` | https://github.com/mariusznazar/the-way/pull/7 | draft opened |
| 02:33 | request | orchestrator | placeholder swap in *Approved by* of WAY-13/1, WAY-125/1; decisions guard (0 errors, 5 warnings, 5 unchecked); fingerprints unchanged | commit 5bbc817, pushed | no other text changed |
| 02:35 | request | orchestrator | record copy commit and removal commit (step 12) | see Request handoff | — |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Branch name (step 4, product git rules) | `task/light-path-small-change` | `task/lighter-cycle` already exists (PR #4) | reuse a similar name | rename of a branch before push; none after | branch |
| C2 | D1–D15 of `spec.md` §9 (designer's choices) | all accepted provisionally as written; D13 (agent-written *Rejected* reason) flagged for the request — later superseded by C9 | spec §8–9; spec review found every addition a necessary consequence or small justified growth | — (each row names its alternative in spec §9) | see spec §9, per row | spec §9; b977e5f, 3bf1452, c64d49a |
| C3 | Spec review issue 1: WAY-125 light clause demands test-first for every change | accept: "test-first where it changes behaviour" | base skill step 9 limits TDD to behaviour changes; task's own example is a copy change | keep — would condemn copy changes | a decision contradicting its skill | b977e5f (WAY-125) |
| C4 | Spec review issue 2: "simple and obvious" in WAY-125's binding part | state the four conditions in the binding sentence; no glossary entry; skill keeps the label | WAY-05, WAY-95 | glossary entry — one term and its guard for one sentence | low: a later reword | b977e5f (WAY-125), 3bf1452 |
| C5 | Spec review issue 3: ground for changing two approved decisions; does the foundation step's "ask … where an entry would change the meaning of an approved decision" force a blocked draft? | no: Mariusz approved the task document (2026-10-08) that orders both changes (points 4–6) and settles their questions — the approver's answer WAY-30/WAY-114 ask for; the guide governs and says to show the change of meaning at the merge (WAY-07); the request lists every wording beyond the task's words | guide "Start a change"; task points 4–6 and "Questions to settle" | a blocked draft request asking what the task already answered | if wrong, Mariusz rejects at the merge; nothing merges without him | pull/7 "What this request settles" |
| C6 | Review R1–R7 | accept all (trim WAY-125; UTF-8 bytes for fingerprints; glossary baseline; link to the report in the request; reasons per assessed finding; log form; discarded commit is historical) | review report | — | low | spec revision 1; 3bf1452, c64d49a |
| C7 | Re-review the revised spec? | no: the revision applies only the reviewer's own findings and rulings; the plan review and the code review read it again | step 7 asks to resolve findings, not to re-review | second spec review (~7 min) | a revision error reaches the planner; the plan review catches it | plan |
| C8 | Planner's departures: decisions guard expects 7 warnings (two `<request link>` placeholders), not "nothing new"; one-line `description` check plus `installation` tests; edits by exact text; untouched WAY-13/WAY-125 prose citations; rewrap only changed lines | accept all | `elements/decisions/format_guard.py:654`; `installation/install.py:111` | rewrap whole paragraphs — noisier acceptance diff | a short-line style commit later | plan Tasks 1–3 |
| C9 | F1: WAY-29 ("A rationale an agent proposes for a human's decision goes to the human as a question, never into the entry") vs the agent-written reason D13 in WAY-125 *Rejected* | drop the item "a task once made by one agent finishing that way …" from *Rejected*; the request says it was dropped and why | WAY-29 sentence 2; the binding sentence already states the switch-and-discard rule | (1) keep, reading WAY-29 as covering recovered decisions only — an agent's reason would pass as Mariusz's; (2) keep the option, ask for its reason in the request — one more question for a clause; (3) stop and ask now — the cycle waits on prose | low: Mariusz adds the item with his reason at the merge; outside the binding part, no fingerprint moves | b977e5f; pull/7 item 6 |
| C10 | Final review Important 1: WAY-125 says a change whose foundation touch writes an invariant is discarded, without the skill's window, so a finished light cycle whose return step writes an invariant reads as discardable | confine the clause to "while that agent makes it" in the binding sentence and the complies example | `task-cycle/skill/SKILL.md` switch window (spec §3.4, D7); WAY-11 return step writes invariants | leave it to the skill — the binding decision would contradict it | low: no carrier of `WAY-125@`; one recompute | 70f6bda |
| C11 | Final review minors 1–3 | parked with rulings in the SDD ledger (route line after a switch; switch report when the executor cannot resume; WAY-125 clause omits the request and is long) | `final-review.md` | fix now — more wording for Mariusz to re-accept for reading risks | a reader's ambiguity | `reports/sdd/progress.md` |
| C12 | `foundations` moved during the cycle (4c19290, `installation/README.md`): rebase or merge? | merge the tip into the task branch (`--no-ff`) | correction-after-review merges, never rebases; a rebase would rewrite the assessed and reviewed commits | rebase — new hashes for every assessed commit; leave unmerged — the request would not show the state that lands | none: one merge commit | adcfcc8 |
| C13 | Mark the request ready (skill step 12) or keep it a draft (the dispatch says "open a draft PR")? | open as a draft and mark it ready after the record links, as step 12 gives it; nothing is blocked | step 12; the dispatch names the route, not a final state | keep it a draft | Mariusz turns it back to draft; nothing merges without him | pull/7 state |
| C14 | Where does the WAY-10 assessment record go in git, when the change's commits exist before the assessment? | the settlement commit 9318492, the last commit carrying the change's foundation edits, as in c5c313c and 0bbf26b | guide "Integrate"; dispatch | amend b977e5f — rewrites the assessed range; an empty commit — carries no change | low | 9318492 |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task_frozen.md` | copied by orchestrator 01:18 | — |
| spec | `spec.md` | design agent (Opus) | spec review: 3 issues fixed (revision 1) |
| plan | `plan.md` | planner (Opus) | orchestrator plan review; dry run on a scratch clone |
| foundation step | b977e5f (`foundations/decisions.md`, `foundations/invariants.md`) | foundation-step agent (Opus) | whole-branch review; independent assessment |
| skill text | 3bf1452 (`task-cycle/skill/SKILL.md`) | implementer (Sonnet) | task review clean |
| record template | c64d49a (`task-cycle/record_template.md`) | implementer (Sonnet) | task review clean |
| final-review fix | 70f6bda (`foundations/decisions.md`) | foundation-step agent | scoped re-review: addressed |
| assessment settlement | 9318492 | settlement agent (Sonnet), message by orchestrator | code review clean |
| merge of the target tip | adcfcc8 | orchestrator | checks rerun |
| approval link | 5bbc817 | orchestrator | guard rerun |
| reports | `reports/` (prompts, reports, guard and test outputs; `reports/sdd/` for the SDD ledger, briefs, task reports and reviews) | — | — |

## Verification

| Command or manual check | Commit and environment | Result | Failed or unchecked details |
|---|---|---|---|
| baseline `python -B gate/run_tests.py gate` | c64a607, Python 3.14.3, Windows 11 | exit 0, 96 tests OK | — |
| baseline `python -B gate/run_tests.py task-cycle` | c64a607 | exit 1, "NO TESTS RAN" | the part holds no tests; its text is unchecked by any test |
| baseline `python -B gate/run_tests.py elements/decisions` | c64a607 | 169 tests OK | — |
| baseline `python -B gate/run_tests.py elements/invariants` | c64a607 | 233 tests OK | — |
| baseline decisions guard `--base none --merge-onto none` | c64a607 | exit 0, 0 errors, 5 warnings, 5 unchecked | warnings: passed check-by dates of WAY-03, 21, 52, 55, 69; unchecked: main-branch lines, template change, `TODO`, copies, relation fingerprints |
| baseline invariants guard `--base none --merge-onto none` | c64a607 | exit 0, 0 errors, 0 warnings, 3 unchecked | unchecked: identifiers/versions, `TODO`, link fingerprints; no human_verdicts.md |
| baseline glossary guard `--base none --merge-onto none` | c64a607 | exit 0, 0 errors, 0 warnings, 5 unchecked | — |
| `python -B gate/run_tests.py gate` (critical flows, WAY-45) | c64d49a | exit 0, 96 OK | — |
| `python -B gate/run_tests.py task-cycle` | c64d49a | exit 1, NO TESTS RAN | unchecked: the changed part holds no tests; skill and template checked by reading only (task reviews, final review) |
| `python -B gate/run_tests.py elements/decisions` | c64d49a | exit 0, 169 OK | — |
| `python -B gate/run_tests.py elements/invariants` | c64d49a | exit 0, 233 OK | — |
| `python -B gate/run_tests.py installation` | c64d49a | exit 0, 16 OK | reads the committed skill's one-line `description` |
| decisions guard `--base none --merge-onto none` | c64d49a | exit 0, 0 errors, 7 warnings, 5 unchecked | warnings: baseline 5 + `<request link>` placeholder at WAY-13 and WAY-125 *Approved by*; unchecked as baseline |
| invariants guard `--base none --merge-onto none` | c64d49a | exit 0, 0 errors, 0 warnings, 3 unchecked | as baseline |
| glossary guard `--base none --merge-onto none` | c64d49a | exit 0, 0 errors, 0 warnings, 5 unchecked | as baseline |
| part-map guard `--base none` (map unchanged; run for completeness) | c64d49a | exit 0, 0 errors, 0 warnings, 6 unchecked | no baseline taken; the map is not changed |
| fingerprints by hand: binding paragraphs written to UTF-8 files, `relation-model/fingerprint.py <` | c64d49a | WAY-13 97b17d59 (= WAY-125 *Relations*, `foundation-change-path/1`); WAY-125 68b2d563 (no carrier) | guards leave them unchecked with `--merge-onto none` |
| diagnostic, not a pass: decisions guard `--merge-onto c64a607` | b977e5f (foundation-step agent) | exit 1, 4 errors: edited copies of WAY-13 and WAY-125 differ from c64a607, two placeholders; no relation-fingerprint error | expected from in-place edits before `main` |
| diagnostic, not a pass: invariants guard `--merge-onto c64a607` | before renewal / b977e5f | red (1 error, stale `WAY-13@c6b33aa9`) / green (0 errors) | — |
| deliberate break of an invariant check (WAY-69) | — | not applicable | no invariant check written or changed; `foundation-change-path/1` *Method* is `TODO` |
| full gate of the-way | — | does not exist | unchecked; these are partial checks, never a pass of the full gate |
| visible behaviour in a running product | — | not applicable | process text; no running product |
| all five test directories and three guards, as above | adcfcc8 (merged tip) | gate 96 OK; decisions 169 OK; invariants 233 OK; installation 16 OK; task-cycle NO TESTS RAN; guards 0 errors (decisions 7 warnings, 5 unchecked; invariants 3 unchecked; glossary 5 unchecked) | task-cycle unchecked; fingerprints by hand: WAY-13 97b17d59, WAY-125 f4d471cc, carriers match |
| decisions guard after the placeholder swap | 5bbc817 | exit 0, 0 errors, 5 warnings, 5 unchecked | the two placeholder warnings gone |
| WAY-33 search against the target tip | 4c19290 | foundation files identical to c64a607 | the base search (foundation step report) holds |

## Return step

Performed by the orchestrator on the diff c64a607..70f6bda and the choice log (C1–C11, spec D1–D15),
after reading every touched part's decisions (*Scope* task-cycle, decisions) and the part map.

- Decisions written or changed: WAY-13/1 and WAY-125/1, edited in place (foundation step b977e5f, fix
  70f6bda). No other choice binds after the merge as a decision: D1 is carried by WAY-13's new
  sentence 3; the switch-and-discard rule and the four conditions by WAY-125 (D4, D9); naming,
  thresholds and mechanics (D2, D3, D5–D8, D12, D14, D15) live in the skill, which every task runs
  under; C1–C11 bind only this cycle.
- Invariants written or changed: `foundation-change-path/1` — *Derives from* renewed to
  `WAY-13@97b17d59`; sentence, version and `TODO` method unchanged. None new after search.
- Behavior with no invariant: none after search — "a task whose foundation route is changed never
  takes the light cycle" is the existing `foundation-change-path/1` read with WAY-13; the rest is a
  level-2 comparison WAY-125 already names. No commit-checkable sentence is left uncovered.
- Environment facts and glossary terms: none after search — "light cycle"/"full cycle" stand only in
  the skill, never in a binding sentence; WAY-47's "light path" keeps its own meaning; no decision
  rests on the console-encoding behaviour the fingerprint checks met.
- Part-map changes: none — `task-cycle/**` and `foundations/decisions.md` keep their parts and
  responsibilities. A failure mode of the light cycle (an orchestrator admitting a task that changes
  the foundation) is a human's to record (WAY-46); none written.
- Foundation compared with code in touched parts: the skill, the record template, WAY-13 and WAY-125
  agree (four conditions, test-first only for behaviour, switch window and discard) after C10; the
  full cycle's steps are unchanged apart from recording the choice (acceptance, spec §5; final review).
- Projected entries written whole or in part: none — independent task.

## Independent assessment

- Assessed range and its files: c64a6071384fb57cdb9d7e9db4560ddc43e3b355..70f6bda —
  `foundations/decisions.md`, `foundations/invariants.md`, `task-cycle/skill/SKILL.md`,
  `task-cycle/record_template.md`; assessor given the diff and `git archive 70f6bda` in the session
  scratchpad, no access to the repository's working copies (which hold `.runs/`).
- Assessment: `reports/11-assessment.md` — one agent on Sonnet (entries written on Opus), following
  `elements/common/critique/SKILL.md`. Call: mechanics correct, settle O1 before the merge.
- Settlement (orchestrator):
  - O1 (a light change to a high-criticality, trust-boundary or irreversible part gets one review, no
    spec or plan review) — reject: settled by the task owner (task "Questions to settle", answer 1:
    no extra condition for irreversible changes or trust-boundary files); step 10 runs in full on the
    light cycle, WAY-48 checks and the human's decision on what cannot be undone included. Shown in
    the request.
  - O2 (exit from the light cycle rests on the executor's judgement) — reject: task point 6 gives the
    executor that return and the orchestrator judges from its work; no tool measures an agent's time (D12).
  - O3 (WAY-125 answers two questions) — reject: the task places the light cycle in WAY-125 (point 5,
    answer 2); it still answers which methods the cycle adopts and for which task.
  - O4 (touch written "as the foundation step"; names absent from decisions) — reject: written under
    that step's rules, not called one; names kept out of binding sentences (D2, C4).
  - O5 (no part-map failure mode for a task wrongly taken light) — not written: a human records
    failure modes (WAY-46); process remark.
  - O6 (level-2 examples cover two of five triggers) — reject: a pair marks the line (WAY-12).
  - O7 ("path" in `foundation-change-path/1`) — noted, no change.
  - Cut WAY-125 *Rationale* last sentence — apply; cut record template *Foundation route* tail —
    apply; cut request-handoff "Cycle and its reasons" — reject (step 13 asks the request for it).
  - Applied in the settlement commit, whose message carries the assessment record (below in Events).

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/7 — opened as a draft, marked
  ready after the record links (C13); merge asked with a merge commit that keeps the commits.
- Cycle and its reasons: full cycle — the task changes the foundation (WAY-13, WAY-125), and the
  light cycle did not exist at the base.
- What this request settles:
  - WAY-13/1 — Rozmiar zadania może odchudzić przygotowanie i wykonanie zmiany (spec, plan, liczbę
    agentów), ale nigdy wyniku zadania ani sprawdzeń gotowej zmiany; to, czy zadanie zmienia
    fundament, i ostrość sprawdzeń dalej wyznacza wyłącznie to, czego zadanie dotyka.
  - WAY-125/1 — Metody Superpowers obowiązują w pełnym cyklu; małe zadanie bez zmiany fundamentu
    robi jeden wykonawca, od testów tam, gdzie zmienia zachowanie, z jednym końcowym przeglądem
    całości, a zmiana, która przerośnie tę ocenę albo w trakcie pracy wykonawcy dotknie fundamentu w
    sposób wymagający otwartego wyboru, zmiany znaczenia zatwierdzonej decyzji, sprzeczności z
    wpisem albo niezmiennika lub jego testu, jest odrzucana i zaczyna się od nowa od świeżego
    projektu z raportem wykonawcy bez kodu.
  - Both change meaning and are accepted again at the merge (WAY-07); the request lists seven
    wordings beyond the task's words, the dropped *Rejected* item (C9) among them.
- What the foundation puts in front of the human at the merge: none (no invariant kept under a
  correction, no fallen criticality, no recovered row, no moved definition, no WAY-97 term); the
  request also shows assessment remark O1 and its settlement.
- Questions: none — the foundation step allows none (C5).
- Choices within the request: 14 orchestrator choices (C1–C14, "Questions and autonomous choices")
  and the designer's D1–D15 (`spec.md` §9); SDD rulings in `reports/sdd/progress.md`.
- Writes to the task's backlog entry: `[url::https://github.com/mariusznazar/the-way/pull/7]` added
  after `[estimate::8]` in `_tasks_active.md`; state kept `[>]`; vault not committed.
- Process remarks on the-way:
  1. No `.the-way` pin or gitlink: the base commit stood in as the pin (snapshot by `git archive`);
     the gitlink check did not apply. The skill names no route for a cycle on the-way itself.
  2. No full gate, and the changed part `task-cycle/` holds no tests: `run_tests.py task-cycle` exits
     1 ("NO TESTS RAN"), so step 10's "full required gate" reduced to partial tests, guards and
     reading by reviewers. The skill text a product pins is checked by no test.
  3. Guards with `--merge-onto none` leave every relation fingerprint unchecked; the cycle computed
     them by hand. Piping a binding paragraph through a Windows PowerShell 5.1 or cp1252 console
     changes its em dashes and gives a wrong fingerprint (the spec reviewer hit a UnicodeDecodeError);
     only a UTF-8 file's bytes work. `--merge-onto c64a607` served as a red/green diagnostic.
  4. The foundation step says to ask the human, through a blocked draft request, when an entry
     changes an approved decision's meaning. On the-way most tasks exist to change decisions, and the
     step does not tell a change the approved task itself orders from one an agent originates; read
     literally it would block every such cycle. Adapted: the approved task counted as the approver's
     answer and the guide's "show the change of meaning at the merge" governed (C5).
  5. WAY-29's second sentence (an agent's reason for a human's decision stays out of the entry) was
     missed by the designer, the spec reviewer and the planner and caught by the agent running the
     element skills (C9): the element skills hold rules the spec and plan stages never read.
  6. The guide puts the WAY-10 record in "the message of the commit that carries the change", but the
     assessment can only follow that commit; the record went into the settlement commit (C14), as in
     earlier requests.
  7. Step 11 forbids the assessor the spec, plan and reports, yet the task's worktree holds them under
     `.runs/`; the skill gives no way to isolate them. Adapted: `git archive` of the assessed commit and
     the diff in the session scratchpad, with an instruction not to open the repository.
  8. SDD's review packages are diffs, which the record may not copy; the record names their ranges.
     SDD's workspace `.superpowers/sdd/` ignores itself, so it never reached `git status`.
  9. The return step cannot surface a candidate failure mode: WAY-46 leaves failure modes to a human,
     and step 11's "nothing is deferred" forbids listing it for later (assessment O5; return step).
  10. `project-level/task/template.md` and `project-level/task/skill/SKILL.md` still say "the cycle's
      plan chooses how", which a light cycle has no plan for (D11, final review minor 4).
  11. `foundations` moved during the cycle (#6 merged 02:20); the branch merged the tip (C12).
  12. The dispatch said "open a draft PR" while step 12 marks the request ready after the record
      links; the skill's step was followed (C13).
  13. The orchestrator first wrote several event times without reading the clock and corrected them
      (rows marked `~`); a record that requires times needs the clock read at each event.
  14. Cost against the change (153 lines added, 50 removed in four text files; no code): 13 subagent
      dispatches plus 4 resumptions — designer, spec reviewer, planner, foundation-step writer, two
      implementers, two task reviewers, final reviewer, re-reviewer, assessor, settlement agent,
      settlement reviewer — about 2.3M subagent tokens as the agents reported them, and 1 h 20 min
      from start to the request. The spec (469 lines) and plan (995 lines) each outgrew the diff;
      design and planning took 38 min of it. What the stages caught: the spec review three issues
      (test-first in a binding sentence contradicting the skill, an undefined label in a binding
      sentence, the ground for changing approved decisions); the foundation step a WAY-29 breach;
      the final review a binding clause that would discard a finished light cycle; the assessment two
      cuts and the O1 remark for the human. The per-task reviews of two transcription tasks found only
      minors.

## Stage times

| Stage | Start | End | Duration |
|---|---|---|---|
| inputs, start and baseline | 01:15 | 01:18 | 3 min |
| design (brainstorming, incl. revision 1) | 01:20 | 01:44 | 17 min of agent time (14:54 + 1:55) |
| spec review | 01:35 | 01:42 | 7 min |
| plan (writing-plans) and plan review | 01:45 | 01:58 | 13 min |
| foundation step (incl. F1 ruling) | ~01:58 | 02:05 | ~10 min |
| execution (SDD Tasks 2–3 with task reviews) | 02:05 | 02:11 | 6 min |
| final review, fix, re-review, verification | 02:11 | 02:21 | 10 min |
| return step | 02:21 | 02:21 | <1 min |
| independent assessment | 02:21 | 02:27 | 6 min |
| settlement, its review, merge of the tip, checks | 02:28 | 02:31 | 3 min |
| request, approval link, record commits, backlog | 02:32 | 02:40 | ~8 min |
