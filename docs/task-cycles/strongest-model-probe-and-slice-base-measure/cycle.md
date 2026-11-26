# Cycle record — the way: fixes of causes from the AI-layer review of 26.11 — the model of reviews in a cycle started on a weaker model, and the list of "expected red" tests between slices

- Task source: `the task's note in the author's backlog`, frozen at `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/task.md`; settlements accepted 2026-11-26 (*Settlements to record*: "Candidates: 5 shown, 3 accepted — 2026-11-26")
- Task relation: independent
- Product repository: the-way (`https://github.com/mariusznazar/the-way`)
- Process pin: this checkout is the-way itself; no pin
- Target branch and base: `foundations` at `b502011f53225451ddf121e2b772a903b87492db`
- Task branch: `task/strongest-model-probe-and-slice-base-measure`
- Status: running

## Two questions at start

- Trust boundary: no — the change is prose of `task-cycle/` skill files and two decisions of `foundations/decisions.md`; `task-cycle/cycle_stages.py` already prints the model each agent worked on from the session record (columns *Subagent model* and *Orchestrator model*), so it is not touched. If the author finds it must change that script, it returns that as a reach and a review aimed at crafted transcripts is added.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the three questions of the task are answered by the task's *Questions to settle* with the human's source, and its *Settlements to record* rows 1–3 write them into WAY-229 and WAY-136; what is left (the exact places of the five points in the four skill files, the wording of the probe) is how to make what the task settles. No reserved choice.
- Reserved choice: none
- Execution route and reason: one author without a plan. The change is prose in about eight files (`task-cycle/skill/SKILL.md`, `task-cycle/skill/planning.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/slice.md`, `task-cycle/record_template.md`, two decisions, perhaps the part of `task-cycle/review/SKILL.md` that repeats the class) that one agent can hold; the five points of the task depend on each other (the measure on the base replaces the list in all places), so division would split one rule.
- Author: `the-way-author`, class `same` as the orchestrator's — the change spans many files and rewrites two decisions with limits on sentences and words that the foundation check enforces; `cheaper` would risk a second round. Model asked for `sonnet`; worked on `claude-sonnet-5-5` (stages.md rows 2, 6, 12). Resumed twice, by SendMessage: for the fix of the whole-change review's findings and for the return step; no replacement.
- Strongest class: no probe ran in this cycle: it ran under the rule that stood before this change (WAY-229 took the strongest class from the settings' list, which the orchestrator cannot see), and the arguments of the entry point named `opus` as the strongest model allowed in the session. The model asked for, `opus`, was taken on that word (Q1) and the stage table then showed what worked: `claude-opus-5-5` in every turn of the reviewer (`stages.md` rows 4, 8, 10), so the review of the whole change and of its fix ran on the model asked for. The return step committed nothing and so had no review.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: foreground `Agent` call or background completion notification; no smaller limit of active instructions.
- Whole-change review: one reviewer other than the author, by `review-change`, model asked for `opus`, worked on `claude-opus-5-5` (stages.md rows 4, 8, 10). Range `b502011f..60561fba`, report `reports/review-whole-report.md`, first line `FAIL 60561fba1ca0cbb4d0045f8f407c9cd3f5292d0e`; 7 files changed, +115 lines net as the reviewer's size check gives it (`foundations/decisions.md` +102 −33, `task-cycle/skill/SKILL.md` +54 −23, `task-cycle/record_template.md` +14 −4, `task-cycle/change/slice.md` +17 −4, `task-cycle/plan/SKILL.md` +7 −6, `task-cycle/skill/planning.md` +7 −6, `task-cycle/change/SKILL.md` +1 −1). Coverage: every item of *To do* 1–5 and the three rows of *Settlements to record* judged in the report's coverage table, source fidelity judged; no spec, no plan. Blocking: I-1 and I-2, no slice (one author).
- Review rounds:
  - findings `reports/review-whole-findings.md`, contradiction yes: review of the whole change `FAIL 60561fba` (`reports/review-whole-report.md`), blocking I-1 (a correction's session read the model fixed by an earlier session's probe, with no probe of its own; contradiction with settlement row 1 and *Not chosen* 3 of the first question) and I-2 (the exception of the base measure covered every test of a slice's own *Checks*, wider than the owner's announced test; contradiction with rows 2 and 3); the four Minor findings of that review within the task (M-1 to M-4) fixed in the same fix; fix `15bf941a` (range `60561fba..15bf941a`, report `reports/author-fix-1-report.md`, the one author resumed, no finding held wrong); review of the fix by the same reviewer resumed, `PASS 15bf941a` (`reports/review-fix-1-report.md`); no blocking finding remained, no Minor finding remained.
- Weakest-point checks: the author named the probe's workability (that the orchestrator can read the model a probe agent worked on from `task-cycle/cycle_stages.py`) and checked it by running the script on the live session, which printed `claude-sonnet-5-5` in the row of the author (`reports/author-report.md`, own-work check); for the fix, the exception of WAY-136 limited to the owner's announced test in every place, checked by a search of all tracked files for the old wording (`reports/author-fix-1-report.md`).

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One author without a plan; no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 14:20 | start | orchestrator, Claude Sonnet 5.5 | `task-cycle/skill/SKILL.md` steps 1–5; task read whole | — | Status `ready for cycle`, no human actions, independent. The entry point's arguments name `opus` as the strongest model allowed in this session; the session's own settings list is not visible to the orchestrator, so the arguments are the source (as an earlier cycle did) and the stage table of `cycle_stages.py` will show the model that actually worked. |
| 14:25 | checkout | orchestrator | `git fetch`; checkout on `foundations` clean at `b502011f`, equal to `origin/foundations` | — | Nothing to fast-forward. |
| 14:26 | clean-up | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | exit 0 | Removed the directory of `recommendation-not-below-goal`; kept the main checkout and two detached checkouts that are no cycle's; directories of cycles kept: none. |
| 14:30 | branch | orchestrator | worktree `the-way-wt/strongest-model-probe-and-slice-base-measure` from `b502011f` | — | Base `b502011f` is a merge commit whose tree equals its second parent's (`dca0a541a53148179c33920e268c3e0b339af185` both); no gate on the base. |

| 14:41 | one author | `the-way-author`, asked for `sonnet` (class `same`), worked on `claude-sonnet-5-5` | `reports/author-handoff.md`; `task-cycle/change/SKILL.md`, variant "the whole change as the one author"; frozen task | `reports/author-report.md` | Dispatched in the background; completion notification. |
| 15:00 | one author, return | `the-way-author` | report read | commit `60561fba` (7 files, +189 −74); status `done with concerns` | Own-work check with command and exit code present; checks: foundation check exit 0, instruction check exit 0, tests of `task-cycle` (570), `project-level` (302), `process-audit`, `elements/common` (316) exit 0 each; mechanical: worktree clean, range non-empty. Unread material: the author did not run `decision_index.py` and did not read `elements/decisions/examples.md`; autonomous choice Q2 below carries the gap to the reviewer of the whole change, which selects its own foundation and is told of it. Concerns (no rule for every candidate substituted; no environment fact for the tool's silent substitution; the base measure cannot tell a new reason on a test already failing on the base) go to the review. |
| 15:01 | whole-change review | `the-way-stage`, asked for `opus` (class strongest, Q1), worked on `claude-opus-5-5` | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md`; range `b502011f..60561fba` | `reports/review-whole-report.md` | Dispatched. |
| 15:05 | whole-change review, return | `the-way-stage`, asked for `opus`, worked on `claude-opus-5-5` | report read | `reports/review-whole-report.md`: `FAIL 60561fba`; blocking I-1 (a correction session reads the fixed model instead of probing; Contradiction: yes) and I-2 (exception of the base measure wider than the owner's announced test; Contradiction: yes); Minor M-1 to M-4, all within the task | Checks with commands and exit codes, Unread material and Searches present. Reviewer read 4 decisions whole. Findings file `reports/review-whole-findings.md` written in the reviewer's words; fix next. |
| 15:07 | fix 1 | `the-way-author` resumed (same agent), asked for `sonnet`, worked on `claude-sonnet-5-5` | `reports/author-fix-1-handoff.md`; findings `reports/review-whole-findings.md`; variant "the fix of a review's findings" | `reports/author-fix-1-report.md` | Dispatched by SendMessage. |
| 15:14 | fix 1, return | `the-way-author` | report read | commit `15bf941a` (7 files, +74 −62); status `done`; all six findings fixed, none held wrong | Checks with commands and exit codes (foundation check, instruction check, `task-cycle`, `elements/common`, `project-level`: exit 0); Unread material none; Searches none; worktree clean. `remarks_check.py` run by the author listed two items of the review's report, not of the author's — entered at step 12. |
| 15:16 | review of fix 1 | `the-way-stage` resumed (same reviewer), asked for `opus`, worked on `claude-opus-5-5` | `reports/review-fix-1-handoff.md`; range `60561fba..15bf941a`; findings `reports/review-whole-findings.md`; fix report `reports/author-fix-1-report.md` | `reports/review-fix-1-report.md` | Dispatched by SendMessage. |
| 15:18 | review of fix 1, return | `the-way-stage` (same reviewer), asked for `opus`, worked on `claude-opus-5-5` | report read | `reports/review-fix-1-report.md`: `PASS 15bf941a`; 0 blocking, 0 new Minor | All six findings fixed. Unread material none, Searches none, working copy removed. The Minor findings of the whole-change review were fixed in this one fix (M-1 to M-4), none remain. Next: final gate is CI (`.github/workflows/tests.yml`, event `pull_request` into `foundations`), so no local gate; return step. |
| 15:20 | return step | `the-way-author` resumed, asked for `sonnet`, worked on `claude-sonnet-5-5` | `reports/author-return-handoff.md`; `task-cycle/skill/return_step.md` | `reports/author-return-report.md` | Dispatched by SendMessage. |
| 15:26 | return step, return | `the-way-author` | report read | `reports/author-return-report.md`: `done with concerns`, no commit, head stays `15bf941a` | Entries compared with code and the part map; no glossary term, invariant, part-map entry or projected entry needed; rows 1–3 of *Settlements to record* carried by WAY-229 and WAY-136. Concern: no environment fact written for the Claude Code documentation on what a subagent runs on when an allowlist blocks its model (the template needs the live passage word for word and an archived copy, which the handoff did not allow fetching) — goes to the request as an item for the human. Unread material none, Searches none. No commit, so no review of the return step. |
| 15:30 | reconciliation | orchestrator | `git fetch`; `origin/foundations` at `b502011f`, the base | — | Nothing new on the target branch: no renumbering of the task's decisions, no merge. |
| 15:31 | measures | orchestrator | `python -B task-cycle/cycle_stages.py 8b8b8599-10bb-4a35-926a-f251f6eb5bd2 --output .runs/task-cycles/strongest-model-probe-and-slice-base-measure/stages.md`; `python -B task-cycle/cycle_measures.py` with the same session and `--output …/mechanism_measures.md` | exit 0 each, `Warnings: none` | Models in the rows above set from `stages.md`: author turns `claude-sonnet-5-5`, reviewer turns `claude-opus-5-5`. |

## Questions and autonomous choices

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which model is the strongest class in this cycle, since the settings list is not visible to the orchestrator? Source: the arguments of the entry point ("najmocniejszy model dozwolony w tej sesji: opus") | Reviews of the whole change and of the return step run on `opus`; the actual model is read from `stages.md` afterwards and entered in the record | the task's *Context* describes the doradca's start command; WAY-229 as it stands asks for the setting `availableModels` | asking for `fable` (not allowed by the list the human started the session with, would silently fall back to the session's model) | a review on a weaker model, which the stage table would show | step 9 reviews |
| Q2 | The author reports that it did not run `decision_index.py` and did not read `elements/decisions/examples.md` (its **Unread material**); do they bear on what it judged? Source: `reports/author-report.md` | Carry the gap to the reviewer of the whole change, which selects its own foundation, writes its own index and is told to judge whether the gaps hid a collision or a wrong form; the author is not resumed to read | the author read WAY-229, WAY-136, WAY-227, WAY-160, WAY-125 whole and searched the foundation by `grep`; the foundation check passed | resume the author to read the index and examples (cost: another turn of the author, and the review would still select on its own) | a collision with a decision the grep did not reach, which the reviewer's index would show | whole-change review |
| Q3 | Does the trial of the model run once for the cycle or in every session of the orchestrator, a correction's included? Source: finding I-1 of `reports/review-whole-report.md`; task, first question, *Not chosen* 3 | In every session of the orchestrator, before its first dispatch of the strongest class | the review's reasoning: a correction session started with another list of models would otherwise take the model of an earlier session on faith | one trial per cycle, the model read from the record by a continuing session | one more small agent call per session, tens of thousands of tokens | fix 1, WAY-229 ¶2, `task-cycle/skill/SKILL.md` |
| Q4 | Is a model of the candidate's family but an older version a substitution? Source: finding M-1; Claude Code documentation quoted in the task's *Context* (a blocked family alias goes to the newest permitted version of the family) | No: a model of the candidate's family counts as the candidate, only another family is a substitution | the documentation passage in the task's *Context*; `reports/author-fix-1-report.md` | any difference of version triggers the next model down | an older version of the strongest family may be somewhat weaker than the newest; the record shows which worked | fix 1, `task-cycle/skill/SKILL.md` |
| Q5 | Does the orchestrator check that a test a *Goal* announces as left failing stands in the repairing slice's *Checks*? Source: `reports/author-report.md` choice; task *To do* 5 puts the duty on the planner | Yes, one clause in the check of the plan | the task's answer to the third question says the omission would otherwise show after all slices | leave the planner's duty unchecked | one clause to delete | `task-cycle/skill/planning.md` |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/task.md` | orchestrator | — |
| code commit | `60561fba` | one author (`the-way-author`, `claude-sonnet-5-5`) | `FAIL 60561fba` by the reviewer of the whole change (`claude-opus-5-5`), `reports/review-whole-report.md` |
| fix commit | `15bf941a` | the same author | `PASS 15bf941a` by the same reviewer, `reports/review-fix-1-report.md` |
| reports | `reports/author-report.md`, `reports/review-whole-report.md`, `reports/review-whole-findings.md`, `reports/author-fix-1-report.md`, `reports/review-fix-1-report.md`, `reports/author-return-report.md`, `reports/review-whole-decision-index.md`, and the handoffs `reports/*-handoff.md` | the agents named | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, taken from the final gate of the merged request https://github.com/mariusznazar/the-way/pull/160 (its *Checks* item 1: CI run https://github.com/mariusznazar/the-way/actions/runs/45691891142 on `7af4c81b`, `tests` and `tests-windows` passed; item 2 names none failing before) and from `docs/task-cycles/recommendation-not-below-goal/cycle.md` at `9b94b3f4`; the base `b502011f` is a merge commit with the tree of its second parent (`dca0a541a53148179c33920e268c3e0b339af185` both) | orchestrator | no run on the base; the list is empty | none |
| `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | orchestrator on `15bf941a`, own system | exit 0, `0 errors`, no `listed:` line | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0: `merges: 34`, `threshold: 60`, `reminder: no` | none |
| `python -B task-cycle/cycle_stages.py 8b8b8599-10bb-4a35-926a-f251f6eb5bd2 --output .runs/task-cycles/strongest-model-probe-and-slice-base-measure/stages.md` and `python -B task-cycle/cycle_measures.py` with the same session and `--output …/mechanism_measures.md` | orchestrator | exit 0 each, `Warnings: none` | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/strongest-model-probe-and-slice-base-measure` | orchestrator | run 1 exit 1 (2 items listed, appended word for word), run 2 exit 0; 2 runs | none |
| final gate: the CI run on the request's last head (`.github/workflows/tests.yml`, trigger `pull_request` into `foundations`); the cycle has no local time of it | its result stands in *Checks* of the request's description and not in this copy | none | none |

## Return step

- Foundation compared with code: WAY-229, WAY-136 and WAY-227 against the skill files and the record template the change edits: they agree, and no file holds the old wording (search of the tracked files by the old phrases); the part map's `task-cycle` entry needs no change (`reports/author-return-report.md`)
- Decisions written or changed: WAY-229 (`row 1`) and WAY-136 (`row 2`, `row 3`), both changed in place
- Invariants written or changed: none
- Environment facts: none written; the Claude Code documentation on the model a subagent runs on when an allowlist blocks the one asked for is a source the probe rests on, left unwritten because the element's template needs the passage word for word and an archived copy — carried to the request
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 in WAY-229, rows 2 and 3 in WAY-136

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/161 — draft at opening; marked ready after the CI run on the last head passes
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/strongest-model-probe-and-slice-base-measure/request.md --task .runs/task-cycles/strongest-model-probe-and-slice-base-measure/task.md` and `python -B task-cycle/private_paths_check.py .runs/task-cycles/strongest-model-probe-and-slice-base-measure/request.md`: exit 0 each, 1 run each before opening; the description was edited after this copy was committed: the record's link by the SHA of the commit that adds the copy, the CI result and the runs of the three checks on the copy were written into it then
- Writes to the task's line in the backlog: none (the cycle's account of the request is the human's to place; the backlog's task line is not written by this cycle)
- Working copies left: none so far
- Directories of earlier tasks kept: none
- Corrections after the request opened: none
- Process remarks on the-way:
  - whole-change review, .runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/review-whole-report.md: `installation/README.md` gives the command of the instruction-file check for a product (`python -B .the-way/instruction-files/check_instructions.py`); for the-way itself I ran `python -B instruction-files/check_instructions.py` from the root, by analogy.
  - whole-change review, .runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/review-whole-report.md: The run of `decision_index.py --sections` failed (exit 2) because the output directory did not exist yet; I took the list of sections from the `## ` headings of `foundations/decisions.md` (`grep -n "^## "`) instead of running it again, and chose the sections from that list.
