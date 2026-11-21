# Cycle record — the way: skille do rozwijania frameworka nie mają trafiać do produktów, które podpinają go jako podmoduł

- Task source: `the task document in the author's private notes`, `Status: ready for cycle`, `updated: 2026-11-21`; frozen as `task.md` beside this record
- Task relation: independent
- Product repository: the-way (remote `mariusznazar/the-way`), the repository itself
- Process pin: `19e5774a` (the checkout is the-way itself; no gitlink to verify)
- Target branch and base: `foundations`, `19e5774aed6d1d628042e23deccc110ed9f112c0`
- Task branch: `task/hide-the-way-skills-from-models`
- Status: request open

User's instruction to the orchestrator at the start of the cycle (word for word, after the task path): "reviewers on the strongest class — start with model: opus". Applied to every `review-change` dispatch on the strongest class: the Agent tool call carries `model: opus`.

## Two questions at start

- Trust boundary: no — the change touches `agent-instructions/**`, skill files, foundation files, `AGENTS.md`, `README.md` and tests; none of them takes in data from the network, keys, the deployment or files from outside (the part map names no trust boundary for `agent-instructions`, `elements-common`, `project-level`, `task-cycle`, `decisions`, `invariants`, `environment-facts`, `gate`, `repository`)
- Irreversible operation: no — the change edits tracked files and regenerates entry points; nothing is published, deleted outside git or sent anywhere

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — settlements row 1 settles the field in the header and the hand-over of work by reading a file in the-way only, row 2 the environment fact; the task's answers a and a and their *Not chosen* leave no way open. What is left (how an entry point and the paragraphs of the skills phrase the reading of another skill's file, and which file gives the path of each skill) is a way of making what the task settles (the task's To do 2), made by the author and named in its report.
- Reserved choice: none
- Execution route and reason: one author without a plan — the change is one mechanism (a field in the generator, the regenerated entry points, the wording of one hand-over rule in the generator's text and in the paragraphs that name another the-way skill, a decision, an invariant, an environment fact, tests and two instruction paragraphs); one agent can hold it. No spec, no plan.
- Author: `the-way-author`, class `same` as the orchestrator's (the orchestrator is on Sonnet 5.5, so model `sonnet`), because the change spans many parts (agent-instructions, decisions, invariants, environment-facts, elements-common, project-level, task-cycle, instruction-files, gate, repository) and writes a decision, an invariant and an environment fact, not `cheaper`; resumptions: see Events
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification of background agents (Claude Code); no limit set by the cycle
- Whole-change review: `the-way-stage` on `opus` (Opus 5.5), `review-change`; range `19e5774a..7d063ef2`; `reports/review-whole-report.md`, first line `PASS 7d063ef278748884de28577f582b2ab0767d068d`; 70 files, +1285 lines (46 entry points 15 → 40 lines each, `AGENTS.md` 35 → 38, `README.md` 242 → 246, generator 282 → 287, its test 411 → 433, the gate test 316 → 335, `foundations/decisions.md` 11689 → 11715, the 15 skill files +3 or +4 each); covers every To do item, acceptance criterion and both settlement rows; found 6 Minor findings within the task, 0 blocking, 0 outside the scope; judged that the clause of the list of paths does not contradict the settlements
- Review rounds:
  - findings `reports/review-whole-findings.md`, contradiction no: fix of the six Minor findings of the review of the whole change (WAY-161), no blocking finding; fix range `7d063ef2..f1efc257` (`90ac8500`, `2bd0efde`, `f1efc257`), report `reports/author-fix-report.md`; review of the fix by the same reviewer resumed, `reports/review-fix-report.md`, `PASS f1efc257e7d2810d4072b0a82d2a98a78e889a3d`, 0 blocking, 3 new Minor findings left for the request's list; no third round
- Weakest-point checks: the author (`reports/author-report.md`, "Own-work check"): acceptance criterion 1 (a real session), checked on a probe repository with Claude Code 2.1.330 and `haiku`: only the skill without the field was named; second: a text that still tells a session to call a skill of the-way, checked by searches of every `SKILL.md` and its neighbours, all 15 paragraphs found and changed; not checked: Codex. The reviewer repeated the first with real generated entry points in two real sessions (`reports/review-whole-report.md`, `reports/review-whole-probe-evidence.txt`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One-author route: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-21 | start | orchestrator, Sonnet 5.5 | `/the-way-implement-task`, task path from the human | `task.md` frozen | the entry point checks (no `rev-parse --show-superproject-working-tree` path, no `.the-way` in the index) show the-way itself; read `task-cycle/skill/SKILL.md`, `agent-instructions/README.md`, the task |
| 2026-11-21 | checkout up to date | orchestrator | `git fetch`, `git status -sb` | `foundations` equals `origin/foundations` at `19e5774a` | nothing to fast-forward |
| 2026-11-21 | branch | orchestrator | `git worktree add --no-track -b task/hide-the-way-skills-from-models ../the-way-wt/hide-the-way-skills-from-models foundations` | base `19e5774a` | worktree stands |
| 2026-11-21 | working directories of finished tasks | orchestrator | step 4 | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations`, exit 0 | removed `shorten-decisions-over-length-limit` (clean, on origin, merged); kept the main checkout, two detached checkouts that are no cycle's and this cycle's own directory (its branch is not merged yet). The only line under "Directories of cycles that stay for a human decision" is this cycle's own directory, so no earlier task's directory is kept |
| 2026-11-21 | one author, change and foundation step | `the-way-author`, class `same`, model `sonnet` (Sonnet 5.5) | `task-cycle/change/SKILL.md` variant "the whole change as the one author", `task-cycle/skill/foundation_step.md`; frozen `task.md`; handoff `reports/author-handoff.md` | `reports/author-report.md` | dispatched in the background; wait for the completion notification |
| 2026-11-21 | one author returned | `the-way-author`, Sonnet 5.5 | handoff `reports/author-handoff.md` | `reports/author-report.md`, status `done with concerns`; commits `f9cae3a6`, `f3188faa`, `7d063ef2`; failing runs `reports/author-invariant-test-failing-run.txt` and `reports/author-generator-tests-failing-run.txt` | mechanical check by the orchestrator: worktree clean, range non-empty (70 files), each check of the report has its command and exit code, own-work check, Unread material and Searches present; unread WAY-44 and WAY-256 recorded as Q3; clause of the author recorded as Q4; next: review of the whole change |
| 2026-11-21 | review of the whole change | `the-way-stage`, model `opus` (the human's instruction) | `task-cycle/review/SKILL.md`, `whole_change.md`; range `19e5774a..7d063ef2`; frozen task; author report; handoff `reports/review-whole-handoff.md` | `reports/review-whole-report.md` | dispatched in the background |
| 2026-11-21 | review of the whole change returned | `the-way-stage`, model `opus`, Opus 5.5 | `reports/review-whole-handoff.md` | `reports/review-whole-report.md`: `PASS 7d063ef278748884de28577f582b2ab0767d068d`, 0 blocking, 6 Minor within the task, 0 outside; evidence beside it `reports/review-whole-probe-evidence.txt`; it read 3 decisions whole | the reviewer found the author's claim "46 problem lines" wrong (23); acceptance criterion 1 now met by the reviewer's run in a product layout; the reviewer left Codex, loop2, interactive mode and other releases unchecked; next: one fix of the six Minor findings (WAY-161) |
| 2026-11-21 | fix of the Minor findings | `the-way-author` resumed, Sonnet 5.5 (class `same`) | `task-cycle/change/SKILL.md`, `task-cycle/change/fix.md`; handoff `reports/author-fix-handoff.md`; findings `reports/review-whole-findings.md` | `reports/author-fix-report.md` | dispatched in the background |
| 2026-11-21 | fix returned | `the-way-author` resumed, Sonnet 5.5 | `reports/author-fix-handoff.md` | `reports/author-fix-report.md`, status `done`; commits `90ac8500`, `2bd0efde`, `f1efc257`; failing run `reports/author-fix-invariant-test-failing-run.txt` | worktree clean, range non-empty (67 files), checks with command and exit code, Unread material and Searches present; all six Minor findings fixed, none contested; the author did not read the review's report (it was not named for it): its unread list is no gap; next: review of the fix by the same reviewer |
| 2026-11-21 | review of the fix | `the-way-stage` resumed, model `opus` | `reports/review-fix-handoff.md`; range `7d063ef2..f1efc257`; findings `reports/review-whole-findings.md` | `reports/review-fix-report.md` | dispatched in the background |
| 2026-11-21 | review of the fix returned | `the-way-stage` resumed, model `opus` | `reports/review-fix-handoff.md` | `reports/review-fix-report.md`: `PASS f1efc257e7d2810d4072b0a82d2a98a78e889a3d`, 0 blocking, six findings fixed, 3 new Minor (A part map line 170-171 not limited to Claude Code; B failure message and `AGENTS.md` sentence name three causes; C two lines of WAY-127 over 100 columns) | the three new Minor findings go to the request's list, not fixed (WAY-161); next: return step by the author |
| 2026-11-21 | return step | `the-way-author` resumed, Sonnet 5.5 | `task-cycle/skill/return_step.md`; handoff `reports/author-return-handoff.md` | `reports/author-return-report.md` | dispatched in the background |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The task's *Questions carried to cycle*: does Codex load a skill of `.agents/skills/` whose header has `disable-model-invocation`, and does it still run it? | Unproven. Both copies carry the field (smallest reversible reading: the invariant keeps them byte-identical; the cycle opens no question to the human because nothing shows that Codex refuses the skill). The request names it as an unchecked point under *Needed from you*. | (a) https://developers.openai.com/codex/skills, redirected to https://learn.chatgpt.com/docs/build-skills, read 2026-11-21 by a web-fetch agent: the page names only `name` and `description` as fields of `SKILL.md`, puts the invocation policy in `agents/openai.yaml` (`allow_implicit_invocation`), and is silent on unknown fields. (b) https://agentskills.io/specification and https://agentskills.io/client-implementation/adding-skills-support, read the same day: the specification is silent on unknown fields; the client guidance says "don't block skill loading on cosmetic issues" and names "a `disable-model-invocation` flag" as a reason to hide a skill from model-driven activation. (c) A run of `codex exec` against two probe skills in a scratch repository stopped before the model answered: the default model of the installed Codex 0.163.0 (`gpt-6-astra`) is refused for this ChatGPT account (`model_not_found`). | Entry points that differ between `.claude/skills/` and `.agents/skills/` (breaks `skill-entry-points`; needs the human first) | If Codex drops or refuses such a skill: Codex sessions on the-way lose the `the-way-*` entry points until the field is taken out of the `.agents/` copy; a one-line change of the generator and the invariant | the author's handoff (the field goes in both copies) |
| Q2 | Step 4: is a reviewer's model named by the harness's list `availableModels`? | The settings of the session hold no `availableModels` list (`model` is `opus`); the human told the orchestrator to run reviewers on the strongest class with `model: opus`, so every review dispatch passes `model: opus`. | `~/.claude/settings.json` read 2026-11-21; the human's instruction in the command arguments | the name of the strongest model of the family chosen by the orchestrator | none — the human's instruction names the model | every `review-change` dispatch |
| Q3 | The author's report: WAY-44 and WAY-256 (named by WAY-127 under *Relations*, handed over as "as far as the change needs them") stayed unopened. Does the gap bear on a judgment? | It bears on nothing the author judged: the change touches neither entry's sentence, and the reviewer of the whole change selects its own foundation. No resumption. | `reports/author-report.md` "Unread material"; WAY-127 *Relations* | resume the author to read them | an entry that WAY-44 or WAY-256 holds and the change contradicts would show to the reviewer, who selects by the parts touched | review of the whole change |
| Q4 | The author's report: the clause "each entry point lists every skill with the path of its `SKILL.md`" in WAY-127 and in the invariant is not in the rows of *Settlements to record*. Keep it? | Keep it, and treat the part as one the rows do not give: the request lists both entries (WAY-127's second paragraph and the invariant) under what the human accepts by merging as the cycle's wording, with the rejected way (no list: a search by name in every hand-over). The task's To do 2 says a session reaches the skill "po ścieżce", which a name alone does not give. | `reports/author-report.md` "Choices" 1 and "Questions and concerns" 1; task row 1 and To do 2 | drop the list and leave the path to a search by name | one clause of two entries and the generator's list reworded; the invariant's test pins the list | review of the whole change (asked to judge a contradiction) |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` beside this record (copy of the task document, `updated: 2026-11-21`) | human | |
| code and foundation commits | `19e5774a..7d063ef2`: `f9cae3a6`, `f3188faa`, `7d063ef2` | `the-way-author` | `PASS 7d063ef2` (review of the whole change) |
| fix commits | `7d063ef2..f1efc257`: `90ac8500`, `2bd0efde`, `f1efc257` | `the-way-author` resumed | `PASS f1efc257` (review of the fix) |
| reports | `reports/author-report.md`, `author-fix-report.md`, `author-return-report.md`, `review-whole-report.md`, `review-fix-report.md`, the failing runs `author-invariant-test-failing-run.txt`, `author-generator-tests-failing-run.txt`, `author-fix-invariant-test-failing-run.txt`, the evidence `review-whole-probe-evidence.txt` | agents | |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, taken from the merged request https://github.com/mariusznazar/the-way/pull/153 (*Checks*: the CI run https://github.com/mariusznazar/the-way/actions/runs/44748054270 on its last head `dcc0afd0`, `tests` and `tests-windows` passed in the first attempt; the copy `docs/task-cycles/shorten-decisions-over-length-limit/cycle.md` at `31fd52ab` says the final gate ran in CI) | orchestrator; the base `19e5774a` is a merge commit with the tree of its second parent (`220604f36da14673c508272fe0932dd38747428d` both) | no run on the base; the list is empty | none |
| `python -B elements/common/foundation_check.py` on the head `f1efc257` | orchestrator, worktree | exit 0, `0 errors`, no `listed:` line | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0; `merges: 27`, `threshold: 60`, `reminder: no` | none |
| `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/hide-the-way-skills-from-models/stages.md bc1faf0d-ccd5-41c7-a59d-63a7a71fee45` and `python -B task-cycle/cycle_measures.py --output .runs/task-cycles/hide-the-way-skills-from-models/mechanism_measures.md bc1faf0d-ccd5-41c7-a59d-63a7a71fee45` | orchestrator | exit 0 each; 42,749,267 tokens, 0:58:31 working time | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/hide-the-way-skills-from-models` (original) | orchestrator | run 1 exit 1 (7 items listed, appended word for word to the process remarks), run 2 exit 0 (2 runs) | none |
| the checks on the copy of the record, `docs/task-cycles/hide-the-way-skills-from-models` | orchestrator | `python -B task-cycle/private_paths_check.py docs/task-cycles/hide-the-way-skills-from-models`: run 1 exit 1 (18 places listed: absolute paths and one note link), run 2 exit 0 after one rewriting of every text file (2 runs); `python -B task-cycle/image_files_check.py docs/task-cycles/hide-the-way-skills-from-models` exit 0 (1 run); `python -B task-cycle/remarks_check.py docs/task-cycles/hide-the-way-skills-from-models` exit 0 (1 run) | none |
| final gate | the CI run on the request's last head (`.github/workflows/tests.yml`, trigger `pull_request` into `foundations`); the cycle has no local time of it | its result stands in *Checks* of the request's description and not in this copy | none |

## Return step

- Foundation compared with code: WAY-127, the invariant `skill-entry-points`, the fact `claude-code-skill-model-hiding` and the part-map entry `agent-instructions` compared with the generator, the 46 entry points, the 15 skill paragraphs, `AGENTS.md`, `README.md` and the test; the search of `decisions.md`, `glossary.md` and `part_map.md` found no entry that says a session calls a skill of the-way; nothing no longer matched (`reports/author-return-report.md`)
- Decisions written or changed: WAY-127 (by the foundation step, `row 1`; clause on the list of paths `the cycle's`)
- Invariants written or changed: `skill-entry-points`, from row 1 (derives from WAY-127)
- Environment facts: `claude-code-skill-model-hiding` (row 2)
- Glossary terms: none
- Part-map changes: the sentence of the entry `agent-instructions` (`the cycle's`)
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — WAY-127 and `skill-entry-points`; row 2 — `claude-code-skill-model-hiding`
- Result: the return step committed nothing, so no review of it ran; the three new Minor findings of the review of the fix stand in the request's list

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/154, draft until the CI run on its last head ends, then ready for review
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; `python -B task-cycle/request_check.py .runs/task-cycles/hide-the-way-skills-from-models/request.md --task .runs/task-cycles/hide-the-way-skills-from-models/task.md` exit 0 and `python -B task-cycle/private_paths_check.py .runs/task-cycles/hide-the-way-skills-from-models/request.md` exit 0 (1 run each); written and checked after this commit: the record's link, the checks on the copy and the CI result
- Writes to the task's line in the backlog: none
- Working copies left: none
- Directories of earlier tasks kept: none
- Corrections after the request opened: none
- Process remarks on the-way
  - fix of the Minor findings, .runs/task-cycles/hide-the-way-skills-from-models/reports/author-fix-report.md: None unclear. The finding 1 listed `skill_entry_points.py:211`; the sentence stood at the text of `entry_point_text`, not at a line of the docstring, which already said "in Claude Code".
  - one author, change and foundation step, .runs/task-cycles/hide-the-way-skills-from-models/reports/author-report.md: The task's *Context* gives the table "Control who invokes a skill" and says only that a human "can still invoke it by `/name`"; the page's table row says "You can invoke: Yes". I quoted the row, not a sentence about `/name`. The sentence of the fact says "the user can still invoke it".
  - one author, change and foundation step, .runs/task-cycles/hide-the-way-skills-from-models/reports/author-report.md: No test in the repository cites WAY-127 or `skill-entry-points` besides `gate/test_skills_reach_the_way_sessions.py`; none other had to change.
  - one author, change and foundation step, .runs/task-cycles/hide-the-way-skills-from-models/reports/author-report.md: Whether Codex loads a skill with an unknown field: not found in the sources named by the handoff; not probed.
  - return step, .runs/task-cycles/hide-the-way-skills-from-models/reports/author-return-report.md: None. A count of line lengths in WAY-127 (awk, bytes) gives 3344 (106) and 3397 (117) as the two lines clearly over 100; five more lines count 101 bytes and may hold a multi-byte character, so I did not count them as over 100 columns.
  - review of the whole change, .runs/task-cycles/hide-the-way-skills-from-models/reports/review-whole-report.md: Codex's treatment of `disable-model-invocation`: not found in the foundation (no Codex fact covers it), not probed.
  - review of the whole change, .runs/task-cycles/hide-the-way-skills-from-models/reports/review-whole-report.md: In Probe A no `skill_listing` delta followed the `dynamic_skill` attachment, unlike the author's run, yet the model named the nested control. How Claude Code 2.1.330 hands a dynamically loaded skill to the model in `-p` mode is unclear. Both runs agree that the hidden entry points are absent from `dynamic_skill.skillNames`.
