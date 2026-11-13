# Cycle record — the way: own subagent types for the stages of the cycle — lighter agent start and a one-hour prompt cache for the one author

- Task source: the task's note in the author's private backlog, status `ready for cycle`, updated 2026-11-13 (frozen copy: `task.md` beside this record)
- Task relation: independent
- Product repository: the-way (https://github.com/mariusznazar/the-way)
- Process pin: this checkout is the-way itself, `715ae20`
- Target branch and base: `foundations`, `715ae20`
- Task branch: `task/cycle-subagent-types`
- Status: request open

## Two questions at start

- Trust boundary: yes — `installation/install.py` is the trust boundary of the part `installation` (it takes in files from outside: what a product already holds in `.claude/agents/`, symlinks, encodings, names). The change adds the installer's handling of `.claude/agents/`, so every code review of the cycle is told so and checks crafted input there (a symlinked `.claude/agents`, a file of another owner at an owned path, non-UTF-8 text, a name that escapes the directory). Other touched parts (`agent-instructions`, `task-cycle` instruction files, the foundation) name no boundary file the change touches.
- Irreversible operation: no. The cycle writes in the task's worktree only; it never installs into a product.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. Every question of the task's *Questions to settle* carries the human's answer and source; the three rows of *Settlements to record* settle their entries. The two questions carried to the cycle (where the definitions stand as one source for the installer and for the-way's own `.claude/agents/`, whether a script generates the copies; the names and wording of the types) are choices of how to make what the task settles: WAY-127's entry points and the installer's own-file rule give the pattern, and the author makes and names each choice.
- Reserved choice: none. No language, framework, library, store of data, way of logging in or place to run is in play.
- Execution route and reason: one author without a plan — two short definition files, one generator (a variant of `agent-instructions/skill_entry_points.py`), the installer's new file group with its tests and README, word-level edits of a handful of cycle instruction files, one changed decision and three new ones; one agent can hold it.
- Author: class `same` as the orchestrator's, for its code, foundation entries and return step, since the change reaches four parts (`agent-instructions`, `installation`, `task-cycle`, the foundation) and a trust boundary and writes decisions that must be weighed against WAY-127, WAY-255, WAY-125 and WAY-229. Resumed for the fix and the return step.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: foreground `Agent` calls and completion notification; no limit hit so far
- Whole-change review: a fresh reviewer (same class, general-purpose agent) by `review-change`, range `715ae20`..`2245f08`, `reports/whole-review-report.md`, first line `PASS 2245f0867748452cc07a766fa80f8f01b3288abc`; 21 changed files (1136 added, 62 removed lines at that head); 0 blocking, 8 Minor within the task (M1–M8), 2 outside it (O1, O2); coverage of every To do item, the acceptance criterion, the four answers and the three settlement rows stated; source fidelity: the quotes of WAY-255, WAY-368, WAY-369, WAY-370 match both documentation pages word for word; it read 8 decisions whole and screened none by title (see Unread material of its report)
- Review rounds:
  - findings `reports/whole-review-findings.md`: the review of the whole change passed with eight Minor findings within the task and no blocking finding. One fix by the author, resumed, on `same`: commit `b0ab508` (range `2245f08`..`b0ab508`), `reports/fix-report.md`: M2, M3, M4, M5, M6, M8 fixed; M1 (the author's added rule about waits, which the reviewer itself recommends leaving) and M7 (a dependency on the acceptance probe, which has run) contested with evidence. The same reviewer, resumed, reviewed the fix once, `reports/fix-review-report.md`, `PASS b0ab508`: 6 findings fixed, M1 and M7 declinations kept, 3 new Minor in the fix (N1–N3, go to the request's list); crafted-input reruns against the fixed installer behaved. The return step's commit `f1ff7d6` had its own review, `reports/return-step-review-report.md`, `PASS f1ff7d6`: 0 blocking, 1 Minor within the task, 1 outside; not fixed.
- Weakest-point checks: author — requirement: an agent of either type starts without the list of skills (acceptance criterion); check: the definitions' fields against the installed Claude Code binary (it knows `disallowedTools`, `cacheTtl`, `omitClaudeMd`, `experimental`) and, being unable to run the probe, left to the orchestrator (`reports/author-report.md`); the orchestrator's probe then showed it (Events). Second requirement: the installer's trust boundary, 12 tests of crafted inputs each refused before anything was written, and five mutations of the own-file and stale rules each caught. The fix's own-work check: the new helper `is_agent_definition` made always false and always true, each caught by the installer tests (`reports/fix-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One author, no plan: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-13 | start | orchestrator | task document | `task.md` | `foundations` was behind `origin/foundations` by 7 commits; fast-forwarded to `715ae20` (SKILL.md of the cycle changed in that range; read again). Branch `task/cycle-subagent-types` and worktree `.runs/worktrees/cycle-subagent-types` created from `715ae20`. Gate on the base not run: `715ae20` is a merge commit whose tree equals the tree of its second parent (`3c1b04d…`, WAY-367); the list of failing tests is taken from the final gate of the merged branch's cycle (see Verification). |
| 2026-11-13 | author | author (same class as the orchestrator, general-purpose agent, foreground) | `reports/author-handoff.md`, `make-change` "the whole change as the one author", frozen `task.md` | `reports/author-report.md` | `done with concerns`; commits `07cb56a`, `1239ae2`, `2245f08` (base `715ae20`); mechanical check: clean worktree, non-empty range, 21 files (definitions, generator, installer, tests, README, cycle instruction files, decisions, part map), checks with commands and exit codes, own-work check, Unread material and Searches present; its concerns: the acceptance probe is the orchestrator's, the conditions of two figures of the task are not given, environment facts left to the return step; next: the probe |

| 2026-11-13 | acceptance probe | orchestrator, `claude -p` in the worktree (Claude Code 2.1.325, model claude-sonnet-5-5) | no handoff file: one prompt asking the main agent to dispatch `the-way-stage`, `general-purpose` and `the-way-author` and to ask each whether its context lists skills and whether it has a tool named Skill | scratchpad `probe.json`, `probe2.json`; subagent transcripts of sessions 35900c06 and 884d6d78 | passed for both types: neither lists skills nor has the Skill tool; first-call context 25,321 tokens (stage) and 25,369 (author, the whole write in the one-hour bucket) against 37,109 for a general-purpose agent of the same session; next: review of the whole change |
| 2026-11-13 | review of the whole change | reviewer (same class, general-purpose agent, fresh; the orchestrator's session started before `.claude/agents/` existed, so no stage of this cycle ran under the new types, WAY-370) | `reports/whole-review-handoff.md`, `review-change` "the whole change", range `715ae20`..`2245f08` | `reports/whole-review-report.md` | `PASS 2245f08`; 0 blocking; 8 Minor within the task (M1–M8), 2 outside (O1 junction at `.claude` accepted by `check_parents`, a pre-existing check shared with the skills' entry points; O2 duplicate name in a product's agent directory); coverage of every item, row and source fidelity stated; next: one fix of the 8 Minor findings and one review of it |
| 2026-11-13 | fix | author, resumed (same class) | `reports/fix-handoff.md`, findings `reports/whole-review-findings.md` | `reports/fix-report.md`; commit `b0ab508` | `done`; mechanical check: clean worktree, one commit, 11 files (the files of M2–M6 and M8; M1 and M7 contested with evidence), report with checks, own-work check (mutation of the new helper caught), Unread and Searches; next: review of the fix |
| 2026-11-13 | review of the fix | reviewer, resumed (same class) | `reports/fix-review-handoff.md`, findings `reports/whole-review-findings.md`, range `2245f08`..`b0ab508` | `reports/fix-review-report.md` | `PASS b0ab508`; 0 blocking; 3 new Minor in the fix (N1 over-long lines left by the fix in `SKILL.md`, `correction.md`, `foundation_step.md`, `planning.md`, `spec_review.md`; N2 one 101-column docstring line in `install.py`; N3 an odd line break in `record_template.md`) go to the request's list; M1 and M7 declinations kept; crafted-input reruns against the fixed installer behaved; next: return step |
| 2026-11-13 | return step | author, resumed (same class) | `reports/return-step-handoff.md`, `task-cycle/skill/foundation_step.md`, `task-cycle/skill/return_step.md` | `reports/return-step-report.md`; commit `f1ff7d6` | `done`; one commit (`foundations/decisions.md`, `foundations/environment_facts.md`): seven environment facts written, the *Based on* of WAY-255, WAY-368, WAY-369, WAY-370 now names them, WAY-370's *Rationale* corrected; no invariant, glossary term or projected entry; next: review of the return step's commit and then the gate |
| 2026-11-14 | review of the return step | reviewer (same class, general-purpose agent, fresh) | `reports/return-step-review-handoff.md`, `review-change` "the return step's commits", range `b0ab508`..`f1ff7d6` | `reports/return-step-review-report.md` | `PASS f1ff7d6`; 0 blocking; 1 Minor within the task (WAY-370's *Rationale* says "a setting for each" where the cited passage names the single setting `skills.config`), 1 outside (WAY-255 *Based on* still quotes the prompt-caching page directly, as before this task); neither fixed (a Minor finding of the review of the return step goes to the request's list) |
| 2026-11-14 | gate | orchestrator | `python -B task-cycle/gate_times.py --output docs/task-cycles/cycle-subagent-types/gate_times.md -- python -B gate/run_tests.py` on `f1ff7d6` (the final tree) | `gate_times.md`, `final-gate.log` | exit 0, 1265 tests in 10 directories passed (764 s); `origin/foundations` unmoved at `715ae20` after a fetch, no reconciliation merge |
| 2026-11-14 | stages and measures | orchestrator | `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py` on this session | `stages.md`, `mechanism_measures.md` | both exit 0 |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Class of the one author (step 4) | `same` (the orchestrator's class) | the change reaches four parts and a trust boundary and writes decisions | `cheaper` — a wrong weighing against WAY-127/255 costs a fix round and a review | one fix round | author |
| Q2 | Does the change need a spec (WAY-135)? | no | the choices left to the cycle (source location, generator, names, wording) follow the pattern of WAY-127 and the installer's own-file rule; none changes what the task settles | a spec — a longer cycle for choices a reviewer can still contest | a spec-less choice the review rejects costs a fix round | route |
| Q4 | Where the definitions stand, how the copies are made, their names and bodies (the task's *Questions carried to cycle*; the author's choices 1–7 and 9 in `reports/author-report.md`) | source `task-cycle/agent-types/`, a generator `agent-instructions/agent_type_copies.py` writing byte-identical tracked copies into `.claude/agents/`, names `the-way-stage` and `the-way-author`, `disallowedTools: Skill` with no `tools` list, own-file rule by name, header and a closing sentence of the description | WAY-127 and the installer's own-file rule; the acceptance probe confirmed `disallowedTools: Skill` | the author's rejected ways in its report: `.claude/agents/` as the only source; definitions inside `install.py`; one generator for skills and types; plain names; a `tools` list naming every tool | a rename or move touches the definitions, one constant of the installer and the tests | author |
| Q5 | To do 5 — the four method names remain as labels in the orchestrator's text, with the path of each file at step 3 | accepted by the reviewer as fulfilling To do 5 (M4 closed the remaining bare labels of `planning.md`, `spec_review.md`, `return_step.md`, `correction.md`) | `reports/whole-review-report.md`, `reports/fix-review-report.md` | replacing every label by a path in about 25 clauses | an orchestrator reading a bare label tells an agent to call a skill; step 3 says it never does | author, reviewers |
| Q6 | WAY-255's added sentence that the one author's waits stay under about four minutes (M1) | kept; goes to the request as the author's addition | `reports/fix-report.md`, `reports/whole-review-report.md` (M1) | removing it — the task's To do 6 gives only the hour | an author that waits long on the strength of the hour writes its whole context anew where the hour falls back to five minutes | author, request |
| Q7 | Class and kind of the review of the return step's commit | fresh reviewer, class `same` | `task-cycle/skill/SKILL.md` step 11 | `cheaper` — the review judges entries the human did not see | one more review round | return step |
| Q3 | One author or a plan (WAY-136) | one author | about ten files of code and instruction text plus entries; one agent can hold it | planning — a planner, slices and slice reviews for a change whose parts share one pattern | an author that returns for size costs a discarded attempt | route |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `task.md` | orchestrator | — |
| Change | commits `07cb56a` (definitions, generator, tests), `1239ae2` (installer, instruction files, entries), `2245f08` (rewrap), report `reports/author-report.md` | author | PASS, `reports/whole-review-report.md` |
| Fix of the Minor findings | commit `b0ab508`, report `reports/fix-report.md` | author, resumed | PASS, `reports/fix-review-report.md` |
| Return step | commit `f1ff7d6`, report `reports/return-step-report.md` | author, resumed | PASS, `reports/return-step-review-report.md` |
| Acceptance probe | scratchpad `probe.json`, `probe2.json` (not kept in the record); results in Events and Verification | orchestrator | — |
| Gate, stages, measures | `gate_times.md`, `final-gate.log`, `stages.md`, `mechanism_measures.md` | orchestrator | — |
| Request | `request.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| none run on the base: list taken from `docs/task-cycles/gate-parallel-directories/cycle.md`, *Verification*, at commit `575f286` (the merged branch's own copy of its cycle record) | orchestrator, base `715ae20` | the final gate of that cycle on `9282e6f`: exit 0, 1238 tests in 10 directories, every directory passed | none failing before the change |
| `python -B task-cycle/gate_times.py --output docs/task-cycles/cycle-subagent-types/gate_times.md -- python -B gate/run_tests.py` | orchestrator, `f1ff7d6` (final tree), the task worktree | 0; 1265 tests in 10 directories, every directory passed (764 s) | none |
| acceptance probe: `claude -p --model claude-sonnet-5-5 --output-format json --allowedTools Agent` from the worktree, twice (stage type and general-purpose agent; author type) | orchestrator, Claude Code 2.1.325, worktree at `2245f08` | 0 and 0; agents of both types: no list of skills in context, no Skill tool; the general-purpose agent: both; first-call context 25,321 (stage), 25,369 (author, 25,367 in the one-hour bucket), 37,109 (general-purpose) | none |
| `python -B elements/common/foundation_check.py` | author, reviewers, return step | 0; 0 errors | none |
| `python -B gate/run_tests.py agent-instructions`, `task-cycle`, `instruction-files`, `installation`; `python -B installation/test_agent_types_installation.py` | author on `1239ae2`, `2245f08`, `b0ab508` | 0; 25, 394, 104 (5 skipped, not by this change), 56 and 12 tests OK | none |
| mutations of the installer's own-file and stale rules, the generator, the definitions and the helper `is_agent_definition` | author, copies restored afterwards | each caught by the tests | none |
| crafted inputs at the installer's boundary (12 tests; reviewers' own: CRLF own file, stale own file, lookalike, symlinked agents folder, Windows junction at `.claude`) | author, reviewers | every case refused before anything was written except the junction (outside the task: Findings outside the task's scope, 1) | none within the task |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | 0; `tag: foundation-review/2026-11-06`, `merges: 34`, `threshold: 30`, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py --output docs/task-cycles/cycle-subagent-types/stages.md 1e39933f-4c26-427e-be30-00e812d5a036`; `python -B task-cycle/cycle_measures.py --output docs/task-cycles/cycle-subagent-types/mechanism_measures.md 1e39933f-4c26-427e-be30-00e812d5a036` | orchestrator | both 0 | none |
| `python -B task-cycle/request_check.py docs/task-cycles/cycle-subagent-types/request.md --task docs/task-cycles/cycle-subagent-types/task.md`; `python -B task-cycle/private_paths_check.py docs/task-cycles/cycle-subagent-types/request.md` | orchestrator | 0 and 0 (1 run each before publishing) | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/cycle-subagent-types` | orchestrator, on the copy before its commit | last run 0 (0 listed of 21 files), 3 runs; the first run listed 13 places (the task note's path, the worktree's path in six handoffs and reports, one rules-file path, five note links of the task copy), which the cleaning rewrote in every file | none |
| `python -B task-cycle/image_files_check.py docs/task-cycles/cycle-subagent-types` | orchestrator, on the copy | last run 0 (0 listed), 2 runs | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/cycle-subagent-types` (original) and `python -B task-cycle/remarks_check.py docs/task-cycles/cycle-subagent-types` (copy) | orchestrator | original: 3 runs, the first listed 19 items, which were appended to the process remarks word for word, the last exit 0 listing nothing; copy: last run 0 (0 not in the remarks), 2 runs | none |

The checks failing on the base: none. The move of the pin: none (the-way itself).

## Return step

- Foundation compared with code: the entries the change writes or changes (WAY-368, WAY-369, WAY-370, WAY-255, WAY-09, WAY-34), those the task names (WAY-125, WAY-127, WAY-148, WAY-229), the part-map entries `task-cycle`, `agent-instructions`, `installation` and `installation-command`, and the invariants `skill-entry-points`, `derived-file-content` and `installation-claude-guidance`, each compared with the repository on `b0ab508`; two things no longer matched and were corrected: WAY-370's *Rationale* (it said more of Codex than a cited passage says) and the four decisions' direct quotes of their sources, which became environment facts (`reports/return-step-report.md`)
- Decisions written or changed: WAY-368, WAY-369, WAY-370 (new, rows 1 to 3), WAY-255, WAY-09, WAY-34 (changed in place)
- Invariants written or changed: none
- Environment facts: seven written (`claude-code-subagent-skills-denied`, `claude-code-subagent-cache-ttl`, `claude-code-subagent-cache-ttl-credits`, `claude-code-subagent-agent-directories`, `claude-code-subagent-instruction-files`, `codex-project-agents`, `codex-agent-skills-config`)
- Glossary terms: none
- Part-map changes: `task-cycle`, `agent-instructions`, `installation-command`
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 and WAY-368; row 2 and WAY-369; row 3 and WAY-370

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/112 — draft at opening; to be marked ready after the record's link is added
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py docs/task-cycles/cycle-subagent-types/request.md --task docs/task-cycles/cycle-subagent-types/task.md` last exit 0, 1 run
- Writes to the task's backlog entry: none
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: The conditions of the figure "start without the instruction files: 10.5 thousand tokens" are not given in the task (version, model, tool list of the probe's agent); WAY-369's rationale gives the figure with the comparison the task's row 2 makes (21,759 − 10.5k = about 11k) and says no more.
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: The conditions (version, model) of the cache probe (6.9 minutes; 10,470 read, 123 written; 4,786 control) are not given in the task; WAY-368 and WAY-255 state them as "a probe of the cache, in a live session".
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: The estimate "about 4.5% of a cycle's cost" is stated in the task for a start lighter by 41% (the narrow list of tools); WAY-368 says that and gives 37% for these types; the task gives no figure of the gain for 37%.
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: Whether `disallowedTools: Skill` removes the list of skills from the start: the docs say omitting `Skill` from `tools` *or* adding it to `disallowedTools` prevents invoking skills; the task says only the route through `tools` was seen to remove the list. Unclear until the orchestrator's probe.
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: `claude agents --json` printed sessions (kinds, ids), not agent types, so I found no command that lists the types a checkout offers.
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: The task's context mentions the setting `subagentPromptCacheTtl` taking precedence over the field; the fetched page text I read has no sentence about it (the binary's schema text does mention it), so no decision quotes it.
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: The section names of two of the Claude Code quotes (the frontmatter reference table's `experimental` and `omitClaudeMd` rows; the note on the watcher) are my descriptions; the page's own headings were not given by the fetch.
  - author, docs/task-cycles/cycle-subagent-types/reports/author-report.md: No rule of size in the-way's own guidelines (WAY-328): none sought further.
  - return step, docs/task-cycles/cycle-subagent-types/reports/return-step-report.md: The archive's index lists, for the Codex page at its old address, only captures with status 308 (redirects); the captures with status 200 are of the new address, so the entries cite the new address. The decisions' earlier quotes cited the old address, which no entry now cites.
  - return step, docs/task-cycles/cycle-subagent-types/reports/return-step-report.md: The archive holds an HTML capture of the Claude Code page of 2026-11-09 at the address without `.md`, whose text does not hold `cacheTtl`, `disallowedTools` or `omitClaudeMd`; I did not find out why (the capture may be a shell of the page rendered by a script). The entries cite the `.md` address and its capture of 2026-10-19, in which all passages stand.
  - return step, docs/task-cycles/cycle-subagent-types/reports/return-step-report.md: The 2026-10-19 capture predates the read date by 25 days; the passages stand in both, and the template asks for "the closest archived copy that already exists".
  - review of the return step, docs/task-cycles/cycle-subagent-types/reports/return-step-review-report.md: The archive's capture of the Codex page at its old address `https://learn.chatgpt.com/codex/agent-configuration/subagents` (the one the earlier decisions cited): the author reports only redirect captures. I did not search it again; the new facts cite the address the old one redirects to, and the passages stand there.
  - review of the return step, docs/task-cycles/cycle-subagent-types/reports/return-step-review-report.md: The live and archived Claude Code page says in one sentence that, for a session run with `-p` as a custom agent, "`CLAUDE.md` files and project memory still load through the normal message flow, even when the agent's definition sets `omitClaudeMd`" (live `sub-agents.md` line 883), while the table cell the fact cites and the section "What loads at startup" say the opposite for a subagent. The sentence at line 883 follows a paragraph about running the session as an agent, not about a dispatched subagent, so I read it as another case; it is unclear to me. `claude-code-subagent-instruction-files` says what its passage says, and WAY-369's binding sentence (no definition sets the field) does not depend on the outcome. I mention it so the cycle's probe, not this page, stays the evidence of what a type starts with.
  - review of the return step, docs/task-cycles/cycle-subagent-types/reports/return-step-review-report.md: The date read, `2026-11-13`, of every fact: the commit is dated 2026-11-14 00:01 +0100, so the reading falls in the hours before it; I cannot check the day of the reading, only that the passages stand today.
  - review of the whole change, docs/task-cycles/cycle-subagent-types/reports/whole-review-report.md: How an orchestrator learns that its session has none of the types (M8): the files give the rule, not the means.
  - review of the whole change, docs/task-cycles/cycle-subagent-types/reports/whole-review-report.md: Whether the two decisions' figure "10.5 thousand tokens" has conditions anywhere in the task: no (M2).
  - review of the whole change, docs/task-cycles/cycle-subagent-types/reports/whole-review-report.md: Whether `subagentPromptCacheTtl`, which the task's Context says outranks the type's field, is documented on the page: not in the 100,000 characters I read nor in the rest; no decision quotes it, correct.
  - review of the whole change, docs/task-cycles/cycle-subagent-types/reports/whole-review-report.md: Whether Claude Code's handling of `disallowedTools: Skill` removes the list of skills: unclear until the probe.
  - review of the whole change, docs/task-cycles/cycle-subagent-types/reports/whole-review-report.md: A command listing the agent types a checkout offers: none found (the author found none either).
  - the orchestrator: the types this change adds could not be used by this cycle's own stages, since the orchestrator's session started before the folder of definitions existed; every stage ran as a general-purpose agent, as the fallback of WAY-370 gives.
