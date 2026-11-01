# Cycle record — Ustalić, co produkt zapisuje w logach, żeby dało się sprawdzać jego działanie

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_ustalic_co_produkt_zapisuje_w_logach_zeby_dalo_sie.md`, `Status: ready for cycle`, copied 2026-11-01 to `task.md` beside this record; its citations stand at `foundations` `ea4694e`
- Task relation: independent
- Product repository: `C:\Storage\repos\the-way` (the-way working on itself, under `agent-instructions/README.md`)
- Process pin: none — the process root is this worktree
- Target branch and base: `foundations`, `ea4694e`
- Task branch: `task/logging-guidelines`, worktree `.runs/worktrees/logging-guidelines`
- Status: request open

## Two questions at start

- Trust boundary: no at the start — the task changes `product-guidelines/coding/**`, `task-cycle/review/SKILL.md` and the foundation; the part map names no trust boundary in `product-guidelines`, `task-cycle` or `decisions`. Judged again after the spec.
- Irreversible operation: no

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: yes. The task's *Questions carried to cycle* leave open whether the product's decision on the part is the decision adopting the coding template or an entry of its own, which sets what a product's log holds and binds after the merge, and which English words the template uses for "przepływ" and "część", where the glossary holds "critical flow" and "part" in other meanings. To do 3 also names a "reguła zakresu" that the five rules of To do 1 do not name, so the form of the part in the template is not settled. No row of *Settlements to record* carries these, so settling them means designing (WAY-135). The eight rows and the answers to questions 1–12 settle the rest.
- Reserved choice: none. The task settles no tool for a product; a product's library stays with its human through `new_tools.md`.
- Execution route and reason: one author without a plan, judged at step 7 after the spec's review. The reviewed spec names nine files, all prose, no script and no test, and nine entries of the log; the six rules, their nine entries and the skill's steps bind one another word for word, so one agent reading them together makes a more consistent change than slices would, and nothing in the spec calls for division. Trust boundary and irreversible operation stay no.
- Author: fresh agent, class `same`, claude-opus-5-5, for its code, foundation entries and return step; class `same` because the change reaches four parts (`product-guidelines`, `task-cycle`, `project-level`, `decisions`)
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` tool, background; completion notification
- Whole-change review: fresh reviewer, claude-opus-5-5, by `review-change`; range `ea4694e..1740c02`; `FAIL 1740c02`, `reports/whole-review.md`, then `PASS d78f148` on the fix, `reports/whole-review-2.md`; changed files by `git diff --numstat ea4694e..d78f148`; coverage of every To do, row, carried question and answer in `reports/whole-review.md` under *Coverage*; no projected entry carried; no plan
- Review rounds: whole change, range `ea4694e..1740c02`, `reports/whole-review.md`: one Important finding (no rule tells a line of a case flow to carry the identifiers the list names); fix `1740c02..d78f148`, `reports/fix.md`; review of the fix `reports/whole-review-2.md`, `PASS d78f148`
- Weakest-point checks: one author, `reports/author.md`: that the eight rows stand each whole, each *Rejected* holding every way its row's source keeps and no other, with the template and the skill saying the same; checked by a scratch script of hand-written phrases, exit 0, 0 problems, and by reading; it shows presence of phrases, not meaning

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
| 2026-11-01 03:22 | start | orchestrator, claude-opus-5-5 | `implement-task`; task document | worktree at `ea4694e`, `task.md` | branch `task/logging-guidelines` created with no upstream |
| 2026-11-01 03:23 | base checks | orchestrator | `python -B gate/run_tests.py` on `ea4694e`, in the worktree before any tracked file changes | `base-gate.log`, `base-gate.exit`, `base-gate.head` | exit 0 at 03:27; 615 tests in 8 directories, every directory passed |
| 2026-11-01 03:24 | spec | fresh designer, inherited model | `reports/designer-handoff.md`, `task-cycle/spec/SKILL.md` | `spec.md`, `reports/designer.md` | `done`; one entry of its own for the product's decision, six required rules, words `case flow` and `the rules on failures and logs`, nine entries; no question sent |
| 2026-11-01 03:38 | spec review | fresh reviewer, inherited model | `reports/spec-review-handoff.md`, `task-cycle/spec/SKILL.md` | `reports/spec-review.md` | `FAIL`: four findings (the identifier exception widened to secrets; no form for a departure from the ban on personal data alone; D3 on a departure from `### Logging scope`; E2 and E5 on the last-resort line) |
| 2026-11-01 03:46 | spec revision | the designer, resumed | `reports/designer-revision-handoff.md` | `spec.md`, `reports/designer-revision.md` | `done`; all four findings answered; finding 2 settled by a `Personal data: none — <PREFIX-NN>` line inside the kept rule, not by the list alone |
| 2026-11-01 03:48 | spec review of the revision | the reviewer, resumed | message naming the revision, `task-cycle/spec/review.md` | `reports/spec-review-2.md` | `PASS`; four findings fixed, nothing broken besides |
| 2026-11-01 03:50 | route judged again (step 7) | orchestrator | `task-cycle/skill/spec_review.md`, reviewed spec | this record | one author, class `same`; see *Spec and execution route* |
| 2026-11-01 03:51 | one author | fresh author, claude-opus-5-5 | `reports/author-handoff.md`, `task-cycle/change/SKILL.md`, variant "the whole change as the one author" | `reports/author.md`, commits `8b563cd`, `fa85fa5`, `aa4a41c`, `1740c02` | `done with concerns`; foundation check and five test directories each exit 0; concern ruled in Q3; nine entries WAY-271 to WAY-279 |
| 2026-11-01 04:03 | whole-change review | fresh reviewer, claude-opus-5-5 | `reports/whole-review-handoff.md`, `task-cycle/review/SKILL.md`, range `ea4694e..1740c02` | `reports/whole-review.md` | `FAIL 1740c02`: 1 blocking (Important), 6 Minor, 1 line under Declined to judge |
| 2026-11-01 04:15 | fix | the one author, resumed, claude-opus-5-5 | `reports/fix-handoff.md`, `reports/whole-review-findings.md`, `task-cycle/change/SKILL.md`, variant "the fix of a review's findings" | `reports/fix.md`, commit `d78f148` | `done`; foundation check, `instruction-files`, `gate`, `agent-instructions` each exit 0; WAY-275 changed |
| 2026-11-01 04:16 | review of the fix | the whole-change reviewer, resumed | message naming the range `1740c02..d78f148`, `task-cycle/review/fix.md` | `reports/whole-review-2.md` | `PASS d78f148`: the finding fixed; 2 Minor from the fix diff, 0 out of scope |
| 2026-11-01 04:17 | gate on the change | orchestrator | `python -B gate/run_tests.py` on `d78f148` | `change-gate.log`, `change-gate.exit`, `change-gate.head` | exit 0; 615 tests in 8 directories, every directory passed; the return step's commit landed while it ran, so the final tree gets its own run |
| 2026-11-01 04:18 | return step | the one author, resumed, claude-opus-5-5 | `reports/return-handoff.md`, `task-cycle/skill/return_step.md` | `reports/return-step.md`, commit `70976ac` | `done`; three corrections: WAY-276 gains its precedence over WAY-275, WAY-168 and WAY-170 gain `task-cycle` in *Scope*, one clause of the template goes; focused checks each exit 0 |
| 2026-11-01 04:23 | review of the return step | fresh reviewer, claude-opus-5-5 | `reports/return-review-handoff.md`, `task-cycle/review/SKILL.md`, range `d78f148..70976ac` | `reports/return-review.md` | `PASS 70976ac`: 0 blocking, 1 Minor, 2 lines under Declined to judge; the three corrections stand |
| 2026-11-01 04:29 | reconciliation with the target branch | orchestrator | `git fetch origin foundations` | `origin/foundations` at `ea4694e`, the base | no merge needed; the final tree is `70976ac` |
| 2026-11-01 04:29 | gate on the final tree | orchestrator | `python -B gate/run_tests.py` on `70976ac` | `final-gate.log`, `final-gate.exit`, `final-gate.head` | exit 0; 615 tests in 8 directories, every directory passed |
| 2026-11-01 04:33 | request | orchestrator | draft, branch pushed | https://github.com/mariusznazar/the-way/pull/66 | opened as a draft; stages counted into `stages.md`; marked ready once the record's commit is named |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The label of the line `Personal data: none — <PREFIX-NN>` in a product that writes its guidelines in another language; reviewer of the spec, `reports/spec-review-2.md` | left to the author, in the template's bullet for that rule | the reviewer: no script reads it and either reading misleads no agent | settling it in the spec after its one revision | one word of a template | author |
| Q3 | The author read three files of rules for agents in the user's vault (git, scripts, knowledge artifacts) while its handoff said "read no note of the author"; `reports/author.md` | no effect on the measurement: the task's restriction is on notes and repositories of a product, these files name no product and nothing on logs, and the handoff's sentence was wider than the task's; the handoffs that follow use the task's wording | the author's report; the task's Context; the reviewer of the spec read `subagents.md` of the same folder, named there | treating the attempt as voided and discarding it | a measure read as clean that was touched; the human sees this in the request | whole-change review, request |
| Q2 | The class of the one author; step 4 | `same`: a change across four parts | spec *Units* | `cheaper`, the default | a dearer author | author |
| Q4 | The label `Personal data:` in a product writing in another language; left to the author by Q1 | stays in English, in the template's item on departing | `reports/author.md`, *Choices* | a translated label | one word; Minor 5 of the whole-change review argues against it | template |
| Q5 | Whether `settle.md` and `hand_back.md` ask for the decision at every extension; D4 against D5 | only where `guidelines/coding.md` does not yet hold the rules; WAY-279 reads "complete only once the product's log holds that entry" | `reports/author.md`, *Choices* | asking at every extension | Minor 3 of the whole-change review shows one case that goes differently | settle.md, hand_back.md, WAY-279 |
| Q6 | Where a cycle's agent meets row 7's rule | WAY-277 carries a third clause, "a cycle that needs such a library chooses none alone" | `reports/author.md`, *Choices*; D6 | the skill's text alone | one clause more | WAY-277 |
| Q7 | Where the departures stand | a new section `## Departing from the rules on failures and logs`, since a table does not sit in a bullet | `reports/author.md`, *Choices* | nesting them under a bullet | one heading moved | template |
| Q8 | How the shared fields of the six rules are stated | once, in a seventh bullet, then a bullet for each rule | `reports/author.md`, *Choices* | repeating them six times | a longer file avoided | template |
| Q9 | *Writing the files* against "copy no value" | it gains the word library and a sentence that the list is no copied value | `reports/author.md`, *Choices*, corrected by the return step | leaving the sentence out | WAY-171 reads against the list | template |
| Q10 | How the example of D6 stands in `reserved_choices.md` | two rows, one for each outcome, as the icons do | `reports/author.md`, *Choices* | one row | one row more | reserved_choices.md |
| Q11 | Where the review's two lines and `recognize.md`'s two additions stand | the review's after "Against the foundation"; the refresh's bullet after the list of modes; "what writes its log lines" in the bullet of what the product has | `reports/author.md`, *Choices* | other places | order only | review SKILL.md, recognize.md |
| Q12 | The order of the commits | the foundation first, so that the template's citations stand on existing entries | `reports/author.md`, *Choices* | the template first | none after the merge | commits |
| Q13 | "the logging scope" or the heading in WAY-275's sentence | "the logging scope", as the entry's first sentence opens it | `reports/fix.md`, *Choices* | the heading in the sentence | one phrase | WAY-275 |
| Q14 | Whether "the same name in every line" stays beside the finding's shorter wording | it stays, with "the name the list gives it" after it, so row 5's words stand | `reports/fix.md`, *Choices* | only "under the name the list gives" | a few words more | WAY-275, template |
| Q15 | An identifier the list does not name, under the rule on identifiers | neither required nor banned by the rule; whether it goes on the list is `### Logging scope`'s matter, a reading of row 5 by D3's chosen way and row 4 | `reports/fix.md`, *Choices*; note B of `reports/whole-review-2.md` | adding a ban | a case flow with an unlisted joining identifier requires nothing of its lines; the human sees it at the merge | WAY-275, template |
| Q16 | Whether WAY-275's *Verification* gains the finding's case | no: the handoff held the fix to what the finding needs | `reports/fix.md`, *Choices* | adding the example | one example fewer | WAY-275 |
| Q17 | Whether the return step's commit stands, as it acts on note A, a Minor finding the cycle leaves unfixed | it stands: the reviewer of the return step judged it on the entry's own comparison, WAY-25 and WAY-33, and the orchestrator moved no finding; the request names the precedence for the human to accept | `reports/return-review.md`, *Whether the commit stands* | reverting the clause and the relation | WAY-25 has a human record a precedence; the request says so | WAY-276 |
| Q18 | The language of the request; step 13 asks the sentences of meaning in the task document's language, Polish, while the backlog holds an open task on requests coming out partly in Polish | the request in English, as PR #65 ended, with the Polish sentences of meaning in a collapsed block under *What this request settles* | step 13; `_tasks_active.md` | Polish sentences alone in an English body | a longer body | request |

Include questions answered by a binding source as well as new micro decisions. A choice that binds
after the merge is written into the foundation (WAY-36); every other choice is its row here and
nothing else.

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `docs/task-cycles/logging-guidelines/task.md` | copied by the orchestrator | not applicable |
| Spec | `docs/task-cycles/logging-guidelines/spec.md` | the designer | `PASS`, `reports/spec-review-2.md` |
| Change | `ea4694e..1740c02` | the one author | `FAIL 1740c02`, `reports/whole-review.md` |
| Fix | `1740c02..d78f148` | the one author | `PASS d78f148`, `reports/whole-review-2.md` |
| Return step | `d78f148..70976ac` | the one author | `PASS 70976ac`, `reports/return-review.md` |
| Agent reports | `reports/` beside this record | each stage's agent | not applicable |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (base) | orchestrator, `ea4694e`, the task worktree before any tracked file changed | 0; 615 tests in 8 directories, every directory passed | none failing on the base |
| `python -B gate/run_tests.py` (reviewed change) | orchestrator, `d78f148`, the task worktree | 0; 615 tests in 8 directories, every directory passed | none; the tree moved to `70976ac` while it ran |
| `python -B gate/run_tests.py` (final tree) | orchestrator, `70976ac`, the task worktree | 0; 615 tests in 8 directories, every directory passed | none failed; not checked: how an agent acts on the text |
| `python -B elements/common/foundation_check.py .` | the author and the reviewer of the return step, `70976ac` | 0; 0 errors | none |

## Return step

- Foundation compared with code: WAY-271 to WAY-279, those the task names and those the search found, with the template, the skill's files, `task-cycle/review/SKILL.md` and `reserved_choices.md`, and the part map of the touched parts. Three mismatches, corrected in `70976ac`: WAY-275 and WAY-276 met with no relation; WAY-168 and WAY-170 did not reach `task-cycle/review/SKILL.md`, which now carries them; the template said the list is "never read off the code", against WAY-274 and the glossary's `read off`.
- Decisions written or changed: WAY-271 to WAY-279 written by the foundation step; WAY-275 changed by the fix; WAY-276, WAY-168 and WAY-170 changed by the return step.
- Invariants written or changed: none
- Environment facts: none; the three passages in WAY-276 stand as sources quoted in *Based on*
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: 1 WAY-271; 2 WAY-272; 3 WAY-273; 4 WAY-274; 5 WAY-275; 6 WAY-276; 7 WAY-277; 8 WAY-278. WAY-279 is the spec's own and carries no row.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/66, ready for review once the record's commit is named
- Cycle and its reasons: a spec, for the three open choices at *Spec and execution route*; one author without a plan, class `same`; no discarded attempt
- Process pin: not applicable, the-way working on itself
- What this request settles: WAY-271 to WAY-278 from rows 1 to 8, WAY-279 from the spec, WAY-168 and WAY-170 changed in *Scope*; the sentences of meaning stand in `reports/author.md`, `reports/fix.md` for WAY-275 and `reports/return-step.md` for WAY-276, WAY-168 and WAY-170, and in the request
- What the foundation puts in front of the human at the merge: none — no invariant test, surface or *Violated* mark changes
- Checks: `python -B gate/run_tests.py` on `70976ac`, exit 0; no check failed; how an agent acts on the text was not checked
- Human actions the request waits for: none
- Questions: none
- Review findings listed: in the request, six Minor of the whole-change review, two of the review of the fix, one of the review of the return step, three lines of Declined to judge; no check failed and passed again
- Blocked by review: none
- Choices within the request: 18, in the questions table above
- Writes to the task's backlog entry: request link added to its line in `_tasks_active.md`; its state left `[/]`
- Process remarks on the-way: below

## Process remarks kept for the request

Stage: designer of the spec; report `docs/task-cycles/logging-guidelines/reports/designer.md`.

- The handoff says rows 2 and 3 name the step of technology. Neither row does in the frozen task. I
  read this as question 5's source and the Context's line on where logs go, and checked agreement with
  WAY-165, WAY-268 and WAY-270 on that reading. No correction is needed; WAY-270's "two questions …
  nowhere else" stays true, since row 3 takes a different thing from the same lesson.
- To do 1 says a last-resort line carries no identifiers; row 2 says it may carry none. Read as row 2
  (D9).
- WAY-268's "the tools the skills of guidelines choose stay on those skills' routes" does not say
  whether such a tool is tested for reservation first. Row 7 needs that it is, and the spec reads it so.
  If the reviewer reads the clause as exempting every such tool, E7 needs `narrows WAY-268` with its
  area, a change of one field and one sentence.
- `elements/decisions/template.md` has *Rejected* hold the ways the row's source keeps. Row 7's source,
  question 4, keeps two ways that answer the form of a line and not who chooses a library. The spec
  gives them to E5 and `unknown` to E7. The literal reading would put them in E7 as well.
- "Each separately running program": whether a build script is one is not said. The word stays as
  written.
- The file `foundations/environment_facts.md` was searched for overlap, not read: nothing relevant.
- The base run of the gate had finished when last looked at: 615 tests, every directory passed. Noted
  only because the handoff said it was running.

Stage: reviewer of the spec; report `docs/task-cycles/logging-guidelines/reports/spec-review.md`.

- Unclear, in the task: To do 1 and row 2 differ on whether the last-resort line carries identifiers
  (see "Weighed and not reported").
- Unclear, in the foundation: whether WAY-134's "ways not chosen that the row's source keeps" covers a
  source whose ways answer only another limb of its question (E7).

Stage: designer's revision of the spec; report `docs/task-cycles/logging-guidelines/reports/designer-revision.md`.

- `task-cycle/spec/design.md` gives no separate form for a revision. I took the same four checks and
  this report's form.
- Row 6 lets a product depart from the ban on personal data and says nothing of a departure from any
  other limb of the rule. The spec gives no partial form for those: another limb goes only with the
  rule whole. If a product reports wanting to drop the ban on whole objects alone, the spec's answer is
  that it drops the rule or keeps it.
- After a departure from the ban on personal data, the boundary of row 4 still has an item that points
  to a person take the human's consent. The task does not say this case. The spec keeps the boundary
  while `### Logging scope` stands, since row 4 stands apart from row 6.
- From the review report's "Weighed and not reported", E7's *Rejected* remains `unknown`. The handoff
  asks for nothing there, and the reviewer says the build does not go wrong either way; the
  whole-change reviewer may ask.

Stage: reviewer of the revised spec; report `docs/task-cycles/logging-guidelines/reports/spec-review-2.md`.

- Unclear: whether the label `Personal data:` stays in English in a product that writes its guidelines
  in another language. WAY-171 and the *Language* bullet of `product-guidelines/template.md` keep the
  marker `none —` in English and name no such label, while D3 gives the line as a literal. No script
  reads it and either reading misleads no agent, so it is no finding; the maker can settle it in the
  template's bullet for this rule.
- Unclear, from the first report and unchanged: whether WAY-134's "ways not chosen that the row's
  source keeps" covers E7, whose *Rejected* stays `unknown`. The build does not go wrong either way;
  the whole-change reviewer may ask.
- Unclear, in the task and resolved by the spec: after a departure from the ban on personal data, an
  item that points to a person still takes the human's consent, since row 4 stands apart from row 6.
  The designer names this, and the spec's reading is sound.

Stage: one author; report `docs/task-cycles/logging-guidelines/reports/author.md`.

- The search of WAY-33, over all five files of the foundation for failure, swallow, secret, personal
  data, degraded, fallback, the logs, library, and the coding template and its skill, found no row
  already stated, no collision and no entry to correct. WAY-165, WAY-167, WAY-202, WAY-270 stay true,
  as the spec foretold. The return step found nothing to correct in the part map or in those entries.
- Unclear, settled by me: an extension of a product that already holds these rules. See the choices.
- Unclear, from the spec review and left as it stands: whether WAY-134's "ways not chosen that the row's
  source keeps" covers WAY-277, whose *Rejected* stays `unknown`, as the handoff binds.
- WAY-273's *Rejected* holds both ways of question 5, as the spec gives, though the second, each
  product defining a failure, bears on it less than on WAY-272.

Stage: whole-change review; report `docs/task-cycles/logging-guidelines/reports/whole-review.md`.

- WAY-277's *Rejected*, `unknown`, asked of this review by both spec reviews. Read literally, WAY-134's
  verification wants the two ways under question 4. I judge `unknown` sound and raise no finding: both
  ways answer the form of a line, stand in WAY-275, and say nothing of who chooses a library, so in
  WAY-277 they would be options nobody weighed for its question. The foundation does not say which
  reading holds where a source's ways answer another limb of its question.
- WAY-277 and WAY-268, asked by the designer: whether "the tools the skills of guidelines choose stay on
  those skills' routes" exempts a reserved library, which would need `narrows`. I read that clause as
  belonging to the sentence on "every other choice", so a reserved library is outside it, and a library
  on the skill's route is what the clause covers, so "a cycle chooses none alone" agrees with it. No
  finding. WAY-268's sentence does not settle this in so many words.
- Unclear: whether the audit at step 3 compares code with the six rules at an extension on another
  subject, since they are proposed only at step 4 and `kinds.md:15` speaks of a rule "the task settles".
  The task's Context expects the audit to show where code breaks them. At a refresh with a yes, and at a
  task about these rules, it does.
- Unclear: "each separately running program" is left undefined on purpose (D9), including whether a
  build script is one.
- Not found: any record of an agent having acted on this text. The author says so too.

Stage: fix; report `docs/task-cycles/logging-guidelines/reports/fix.md`: `none`.

Stage: return step; report `docs/task-cycles/logging-guidelines/reports/return-step.md`.

- Unclear: whether WAY-21's "governs" reaches every entry a part's files cite. For `product-guidelines`
  it plainly does not, as 25 of its 65 cited entries lack that part, most of them entries it only leans
  on. I corrected the two where the entry's own sentence says what the review does, and left the rest.
- Unclear: whether a collision over a state the rules already forbid needs a relation at all, as the
  second review also asks. WAY-25 speaks of two decisions that both apply and collide; I read a listed
  secret as that case.

Stage: review of the return step; report `docs/task-cycles/logging-guidelines/reports/return-review.md`.

- Unclear: whether an agent may write a precedence at all. WAY-25 has "a human" record one and
  `agent-instructions/README.md:32-34` sends "two decisions colliding with no precedence written" to
  Mariusz. I read the outcome here as already written, in substance, in row 6 and WAY-276, and the
  commit as supplying the form, for Mariusz to accept at the merge through the sentence for the request
  (WAY-114). The other reading would have had the step ask first. The result is the same text, so I do
  not grade it, but the sentence for the request should stay as the author wrote it, naming WAY-275.
- Unclear: whether a collision over a state the rules forbid needs a relation, as `whole-review-2.md`
  and the author both ask. I read it as yes, since WAY-274 does not keep a secret off the list.
- Unclear: WAY-161 speaks of the review of the whole change, and nothing says what a return step's own
  duty does when it lands on a Minor finding's matter. I judged by the ground, not the coincidence.
- Unclear: whether *Scope* is in an entry's binding part; the glossary's definition does not settle it
  field by field. The author's "no binding part moves" holds for what a decision requires. If *Scope*
  did count, no rule of guidelines would have anything to bring in line (WAY-169).
- Unclear: `task-cycle/skill/return_step.md:10-11` sends "a term used against its entry" through
  `record-glossary-term`, whose `decide_entry.md` has no such case: it starts from a word with another
  meaning or two meanings. The author corrected the use and wrote no entry, which fits the outcome. The
  report does not show that it listed the word's uses, and it calls `read off` "the one term used
  against its entry", true of this change's text; see *Declined to judge* for the rest.
- Not read: the author's `own_check.py` and `scope_check.py` in the session's scratchpad, since the
  handoff keeps me to this worktree's tracked files and the cycle's directory. The scope check is
  reproduced above; the own-work script is unverified.
- Not checked: the author's "25 of its 65 cited entries" for `product-guidelines`. Nothing in the
  verdict rests on it.

Stage: review of the fix; report `docs/task-cycles/logging-guidelines/reports/whole-review-2.md`.

- Unclear: whether a collision that arises only for a state the rules already forbid, a secret on the
  list, counts as one WAY-25 requires a relation for. Graded Minor in note A on the ground that the
  binding sentence of WAY-276 already states the outcome.
- The first review's points of this section stand unchanged; the fix touches none of them.
