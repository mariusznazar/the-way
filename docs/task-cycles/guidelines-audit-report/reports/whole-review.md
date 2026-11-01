PASS 0ee0cd9

# Review of the whole change — guidelines-audit-report

Range `2f51e6c..0ee0cd9`, three commits, one author, no plan, so no slice stands apart and every
finding comes from none. `git rev-parse HEAD` in the worktree is `0ee0cd9`, the head given. Blocking
findings: 0. Minor: 5. Out of scope: 3 (the lines of *Declined to judge*).

I read the change as its agents would: one audit alone in each of the three skills, at setting up,
at a refresh and at an extension; a task joining code and tests, each discipline first; a joint task
with the route of one kind and with a new level; orchestrated mode; and the session of `refine-task`
that takes the hand-back. Each reaches the end the spec gives. Nobody has tried an agent on this
text, this review included: it is a reading, not a run.

## Findings

### Critical

None.

### Important

None.

### Minor

**1. A stopped audit whose other audit never runs leaves a list no skill ends.**
`product-guidelines/audit_end.md:57-59`, `product-guidelines/coding/hand_back.md:18-22`,
`product-guidelines/testing/hand_back.md:10-14`.

- What is wrong: the first audit stops because the other skill's step 1 gives the other audit. Where
  the human then separates the work, which `product-guidelines/reading.md:72` allows, no audit runs
  last. The causes stay in *Context* with no number, no top and no check, no one puts them to the
  human, and `project-level/task/skill/final_review.md` has no check that would notice.
- Why it matters: for that task To do 4 to 7 do not happen, silently. An agent reading
  `audit_end.md:53` could reason that the stop no longer applies, but nothing tells it to go back
  and finish.
- Why Minor: the case needs a change of mind between two skills of one refinement, and the human
  sees the whole document at acceptance, with a list that has no top. The review of the spec
  (`reports/spec-review-2.md:102-104`) and the author's report name the case and leave it. I grade
  it myself and reach the same place, as Minor and not as nothing, since the change brings the stop
  that makes the case possible.
- Evidence: reading of the three files named and of `final_review.md:7-16`. One sentence under "The
  audit that stops" would close it: where the other audit no longer runs, the session that knows it
  takes the causes up through the sections below.

**2. "Step 1's document conventions" points to the wrong step for an agent arriving from a skill of
guidelines.** `project-level/task/skill/guideline_findings.md:51`.

- What is wrong: the sentence is copied from the prerequisite's paragraph at line 14, where the
  reader is in `refine-task`. The new section is reached from step 5 of a skill of guidelines
  (`product-guidelines/coding/SKILL.md:140-142`), whose own step 1 is `recognize.md` and holds no
  document conventions. Spec decision 10 names `read_sources.md` here.
- Why it matters: at the one place where a task is written into a product's backlog, the agent has
  to guess whose step 1 is meant. The session did read `read_sources.md` through `refine-task`, or
  went through it by WAY-266, so the guess comes out right.
- Evidence: `project-level/task/skill/read_sources.md:17-21` holds the conventions;
  `product-guidelines/coding/recognize.md` holds none. Writing "`read_sources.md`'s document
  conventions" closes it.

**3. Running the other skill's step 1 also runs the question of the rules on failures and logs.**
`product-guidelines/audit_end.md:52`, `product-guidelines/testing/SKILL.md:99-101`,
`product-guidelines/coding/recognize.md:27-32`.

- What is wrong: the text says "Run the other skill's step 1 now", when the audit needs only the
  mode that step gives. In a joint refresh with the testing audit first, where `guidelines/coding.md`
  lacks the required headings, the coding recognition proposes those rules to the human (WAY-278),
  inside the testing skill's step 3, by "`settle.md` beside this skill", which from there means
  another skill's file.
- Why it matters: one question reaches the human out of its order, and its answer does not bear on
  the stop, since a refresh and an extension both give the audit. Nothing is lost: the answer stands
  in the document, and the coding skill finds it when it leads.
- Evidence: `recognize.md:25-26` gives step 3 for both; lines 27-32 are the proposal. "Read off the
  mode the other skill's step 1 gives" would avoid it.

**4. WAY-281 lacks the qualifier its file adds.** `foundations/decisions.md:8372`,
`product-guidelines/coding/trial_run.md:21-24`.

- What is wrong: WAY-281 says the list holds "the rules of a linter's set broken for one reason";
  `trial_run.md` narrows that to the rules that block and says the rules among the examples yield no
  cause, as spec decision 11 gives. WAY-204 and WAY-205 say "that block" where they mean it.
- Why Minor and not Important under WAY-263: the file does not do what the entry forbids, and it
  drops no qualification of the entry. A rule among the examples binds no code (WAY-203), so nothing
  breaks it, and the entry's rationale speaks of debt, which the glossary defines as a breach of a
  rule the foundation holds (`foundations/glossary.md:33`). The entry read with those says what the
  file says, so I find no second account that changes it. The risk is a later reader taking the
  entry alone.
- Evidence: `foundations/decisions.md:8367-8399` against `trial_run.md:21-24`. Adding "that block"
  to the entry's sentence closes it, and that is the meaning decision 11 already settled.

**5. The example of forty spacings shifts from wrong to hand-typed.**
`product-guidelines/audit_end.md:41-42`, `foundations/decisions.md:8337`.

- What is wrong: question 2 of the task gives "czterdzieści źle wpisanych odstępów", forty wrongly
  entered spacings. The change has "forty spacings typed by hand" and "written by hand". A spacing
  typed by hand can be right.
- Why it matters: the weight is `light` either way, so no agent weighs differently; it is a small
  departure from a source the spec says to keep in meaning. Spec decision 1 and the review of the
  spec did not raise it.
- Evidence: `.runs/task-cycles/guidelines-audit-report/task.md:51` against the two lines named.

## Coverage of the task

| Item | Met by | Result |
|---|---|---|
| To do 1, weight on one scale, described once | `audit_end.md:25-44`, three `SKILL.md` steps 3-5 | met; stops and examples match question 2 in meaning, finding 5 apart |
| To do 2, merging, boundary and linter in the list | `audit_end.md:19-23`, `testing/audit.md:14-18`, `coding/trial_run.md:21-24` | met; finding 4 |
| To do 3, places, categories | `audit_end.md:127-141`, `styleguide/audit.md:15-17` | met |
| To do 4, order | `audit_end.md:73-86` | met |
| To do 5, going back | `audit_end.md:95-118` | met; `Unchecked:` kept with its weight |
| To do 6, the top, one list | `audit_end.md:46-71`, `88-93` | met; rule checked by a simulation below |
| To do 7, proposal, question on a `grave` cause, route, causes below the top | `audit_end.md:156-187`, `guideline_findings.md:44-54`, three `settle.md`, three `hand_back.md` | met; finding 2 |
| To do 8, `task_document.md` | the three files | met; each names weights, causes with places, order, deferred causes |
| Settlements rows 1-6 | WAY-280 to WAY-285 | each row whole, each weak point in *Rationale*, each *Rejected* only the ways its source keeps; the rejection moved from WAY-250 stands in WAY-283 |
| WAY-187, WAY-201, WAY-250 | `foundations/decisions.md` | changed in place as the spec gives; the limit left WAY-187 and WAY-250 |
| Questions carried to cycle, four | spec decisions 1, 2, 3, 4 | settled and carried into the files |
| Questions 1-8 | as the rows above | met |
| Question 9 | no entry of the foundation; the thread stands in the backlog | met; line 39 of the note named under *Reaches* |

The spec's decisions 1 to 14 were each compared with the files, the form of the list, the checks of
`hand_back.md`, the `Withdrawn:` item, the `do not copy` mark and the settled status included.
Nothing the change adds goes beyond the task and the spec. No reserved choice is taken. No invariant
test changes, and no test reads this text, as the spec gives.

**Author's own-work check.** It names the rule of the top and the quoted section names. Those are
real weak points, though the joint flow is weaker, and the author also walked that flow by reading,
which found what `0ee0cd9` fixes. A simulation of the rule and a resolution of the names would catch
either requirement unmet. I repeated both, below.

## Declined to judge

- A joint task with fewer than two audits, and who then starts the other skill: as unsaid before the
  change as after it; `hand_back.md`'s "Otherwise" line keeps the old behaviour.
- A rule the human turns down at step 4 that a cause was measured against: the old charges had the
  same exposure, and the task does not reach it.
- A task joining a styleguide with another discipline: WAY-247 covers code and tests alone, and the
  task asks one list for those two.

## Checks

| Check | Result |
|---|---|
| `git diff 2f51e6c 0ee0cd9` and `git log 2f51e6c..0ee0cd9`, read whole | three commits, 19 files |
| `git rev-parse HEAD` | `0ee0cd9fb2b374ad569c40579bd6049502a4410c`, the head given |
| `python -B elements/common/foundation_check.py .` | exit 0, 0 errors, at `0ee0cd9` |
| `python -B gate/run_tests.py agent-instructions` | exit 0, 18 tests, at `0ee0cd9`; no skill entry point needs writing |
| `git diff --check 2f51e6c 0ee0cd9` | exit 0 |
| `git ls-files --eol product-guidelines/audit_end.md` | `i/lf w/lf`, as `reading.md` |
| `git grep -i "\bcharge"` over the tree | two hits, both in `foundations/decisions.md`, lines 3401 and 7324, the ordinary sense the spec keeps |
| `git grep -i "three to five"` over the tree | WAY-283 alone |
| `git grep` of `audit_end` and `WAY-28[0-5]` outside the log | each pointer resolves; step 3, 4 and 5 of all three `SKILL.md` name the file with its condition |
| A scratch script of the rule of the top on every order of up to nine causes, four weights | exit 0: 715 orders, 0 outside To do 6's bounds. Samples: `gggghh` gives four, `ggggggh` six, `gghml` three, `gh` two. The script encodes my reading of the sentence |
| Quoted section names, by a search of the headings | "Before handing back", "At step 4", "The list", "A task joining code and tests", "A deferred cause of an audit": one heading each |
| Installer | `installation/install.py` names `product-guidelines` only by the three `SKILL.md`; no sparse checkout, so the new file reaches a product with the submodule |
| Manual walk of the routes named at the head | method and result stated there |

Not run, each with its reason:

- `gate/run_tests.py` on `elements/common`, `project-level`, `installation`: the commit after the
  author's runs changes two Markdown files no test reads, and the full suite is the cycle's own run.
- A trial of an agent following this text: no such tool exists in this cycle.

## Reaches beyond the dispatch

The foundation and the guidelines are my own selection (WAY-150, WAY-213). The-way has no
`guidelines/` directory, so no guideline file applies. Parts touched: `product-guidelines`,
`project-level`, and `decisions` through the log.

- **Selection not read whole.** All 94 decisions whose *Scope* names `product-guidelines` were read
  whole. Of the 47 further decisions whose *Scope* names `project-level`, I read whole WAY-101,
  WAY-106, WAY-107, WAY-113, WAY-124, WAY-134, WAY-152, WAY-154, WAY-155 and WAY-156, and took the
  other 37 by their headings alone, as matters of definitions, plans and technology that the one
  changed section of `project-level` does not reach. That is short of "each read whole", and I say
  so rather than call the selection complete.
- WAY-19, WAY-25, WAY-33, WAY-36, WAY-263 in `foundations/decisions.md`: entries the change cites or
  the grade rests on.
- `foundations/glossary.md:31-35`, `debt`; `foundations/part_map.md:155-164`, `product-guidelines`.
- `project-level/task/skill/SKILL.md`, `orchestrated_mode.md`, `project_plan_task.md`,
  `read_sources.md`, `resolve_gaps.md`, `final_review.md`, `find_settlements.md`,
  `project-level/task/template.md`: what the hand-back and the deferred route meet.
- `project-level/lead/skill/SKILL.md:140-209` and `project-level/lead/conversation_template.md:130`:
  what `plan change` does, to test "nothing waits". The turn ends and the plan is routed, then
  refinement resumes; no wait of the task's own follows.
- `product-guidelines/*/orchestrated_mode.md`, `recognize.md`, `settle.md`, `coding/kinds.md`,
  `coding/trial_run.md`, `coding/template.md:222-232`, `testing/new_level.md`: as the agents read
  them.
- `elements/common/way_of_working.md`, "Reading the foundation", "How a skill asks", "Critique
  before collective review"; `product-guidelines/reading.md`.
- `installation/install.py`, by search.
- Outside the repository, read-only, to check question 9: the task list named in `AGENTS.md`, lines
  44 and 87, and `zadanie_the_way_przeglad_zasad_produktu_uruchamiany_po_okr.md`, line 39, in the
  folder `_zadania`.

## Searches not found or unclear

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
