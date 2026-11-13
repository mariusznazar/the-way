PASS 2245f0867748452cc07a766fa80f8f01b3288abc

# Review of the whole change — cycle `cycle-subagent-types`

Range `715ae20..2245f08` (`git rev-parse HEAD` printed `2245f0867748452cc07a766fa80f8f01b3288abc` before I began; three commits `07cb56a`, `1239ae2`, `2245f08`). One author, no spec, no plan, no slice, so no finding below comes from a slice. The worktree was not changed (I wrote scratch products only under the scratchpad).

## Changed files (added / removed lines, `git diff --numstat`)

| File | + | − |
|---|---|---|
| `.claude/agents/the-way-author.md` | 11 | 0 |
| `.claude/agents/the-way-stage.md` | 9 | 0 |
| `task-cycle/agent-types/the-way-author.md` | 11 | 0 |
| `task-cycle/agent-types/the-way-stage.md` | 9 | 0 |
| `agent-instructions/agent_type_copies.py` | 145 | 0 |
| `agent-instructions/test_agent_type_copies.py` | 192 | 0 |
| `task-cycle/test_agent_types.py` | 105 | 0 |
| `installation/install.py` | 58 | 4 |
| `installation/test_agent_types_installation.py` | 332 | 0 |
| `installation/README.md` | 27 | 8 |
| `task-cycle/skill/SKILL.md` | 20 | 8 |
| `task-cycle/skill/foundation_step.md` | 10 | 3 |
| `task-cycle/skill/return_step.md` | 2 | 2 |
| `task-cycle/change/SKILL.md` | 3 | 2 |
| `task-cycle/plan/SKILL.md` | 5 | 3 |
| `task-cycle/record_template.md` | 3 | 2 |
| `foundations/decisions.md` | 160 | 12 |
| `foundations/part_map.md` | 14 | 9 |
| `AGENTS.md` | 4 | 1 |
| `README.md` | 10 | 6 |
| `instruction-files/judging.md` | 2 | 1 |

(21 files, +1136 −62; matches the author's table. Sizes before/after from `python -B task-cycle/change_file_sizes.py 715ae20 2245f08`: `install.py` 614 to 668, `decisions.md` 12341 to 12489, `task-cycle/skill/SKILL.md` 652 to 667, new files 9 to 332 lines.)

## Verdict

No Critical and no Important finding. Every item of *To do* 1 to 6, the acceptance criterion's preparation, the four answers and the three settlement rows are met by the commits, except what the acceptance criterion leaves to the cycle's own probe (below). Blocking findings: none. Minor findings: 8 within the task, 2 outside it.

## Findings

### Critical

none

### Important

none

### Minor, within the task's scope (list for the orchestrator to cut into the fix, or leave)

M1. `foundations/decisions.md` WAY-255, binding paragraph and *Verification*: "its waits stay under about four minutes as well, since Claude Code falls back to five minutes where a subscription spends usage credits", plus the complies/violates examples "the one author … reads the output … every four minutes as well" and "waits twenty minutes in one command on the strength of its hour". The task's To do 6 gives only "the one author's cache lives an hour"; its Context gives the fallback as a fact (the `1h` ignored while usage credits are spent) and prescribes no rule about waits. The sentence is therefore a binding rule the task does not give. It keeps today's behaviour for waits (no cost if left; the alternative gap is an author that waits long on the strength of the hour and, under the fallback, writes its whole context anew), and it follows from the page quote the entry carries, so I grade it Minor and recommend leaving it, naming it in the request so the human sees it was the author's addition. Not outside the task.

M2. `foundations/decisions.md` WAY-369 *Rationale*, "the start without them was measured at 10.5 thousand tokens, against 21,759 for the agent of the first probe with them": WAY-05 asks a measurement to stand "with what was measured and under which conditions". The task gives the 10.5k figure without version, model or tool list (the author reports this), and the entry pairs it with the 21,759 of another probe. Row 2 of the task makes the same comparison ("dodatkowych 11 tys."), so the pairing is the task's, but "measured" and the missing conditions leave the figure without the condition WAY-05 asks. Suggest: say the figure is of a probe whose conditions are not recorded, or drop the pairing and keep the task's "about eleven thousand tokens more". Within scope.

M3. `foundations/decisions.md` WAY-368, WAY-369, WAY-255 prose and `part_map.md` lines wrapped past the repository's column (about 100): 101 to 110 columns in about 25 added lines, and three lines of 122, 173 and 187 columns (WAY-369 "product's file together, and the product's file alone cannot be kept; the start without them…", WAY-369 "tokens, against 21,759 … A later decision…", WAY-368 "control with five minutes wrote its whole 4,786 anew (WAY-255 holds the account of the hour). The definitions come from…"). `task-cycle/record_template.md` line 93 ("dispatch's row the actor names … Name handoff and report paths …") and the `- Author:` line are also over-long after the edit. The author rewrapped `task-cycle/skill/SKILL.md` in `2245f08` for the same reason; these were left. Layout only.

M4. `task-cycle/skill/planning.md:8` ("dispatch a fresh planner with `plan-task`"), `task-cycle/skill/spec_review.md:5` ("review the spec with `write-spec`"), `task-cycle/skill/correction.md:29,37,38`, `task-cycle/skill/return_step.md:4` ("a fresh agent with `make-change`"): names of the four methods remain as labels. Step 3 of `task-cycle/skill/SKILL.md` now says "the name labels its method here and in the record; an agent reaches the method by its file's path, never by calling a skill", and the handoff paragraph already requires the path. I judge To do 5 fulfilled (see coverage), so this is only a remark: a reader of `planning.md` or `return_step.md` alone, who has not read step 3, still meets a bare skill name. One clause in each of the three files naming the path would close it; leaving it costs nothing the handoff paragraph does not already cover.

M5. `task-cycle/plan/SKILL.md:18` ("The planner has no skill tool: …") and `task-cycle/skill/foundation_step.md` ("since it has no skill tool"): stated without condition, while in the fallback WAY-370 allows (another harness, or a session without the types) the agent does have a skill tool. The instruction still works then (it reads the file), but the sentence is untrue there. Suggest "where it has no skill tool". Within scope.

M6. `installation/install.py` names that stopped being exact: the docstring of `plan()` ("the entry points it deletes") and `stale` now also hold agent definitions; `owned()`, the DELETE message and the apply loop choose between the two kinds by `path.name == "SKILL.md"`, a test of a file name standing in for a kind. Works for every path the installer writes (an agent definition can never be named `SKILL.md`); polish only. The-way has no rule of size (WAY-328, WAY-363), so the growth of `install.py` (+54) is Minor by that rule and I find nothing beyond it.

M7. `installation/README.md` row for the definitions and `foundations/decisions.md` WAY-368 *Rationale* state as fact that an agent of the types "starts without the list of skills" / that the list "is no longer shown". The task says only the route through a `tools` list was seen to remove the list, and the acceptance criterion makes the cycle's own probe the proof for these definitions (route `disallowedTools: Skill`). If the probe shows the list stays, these two statements and WAY-368's premise change together. Not a defect of the files today; a dependency on the probe the orchestrator must keep (see Unverified).

M8. `foundations/decisions.md` WAY-370 *Verification*, violates: "a cycle dispatches a stage without its type in a session that has the types and writes nothing of it into its record", and WAY-368's violates "dispatches a reviewer with the harness's general agent in a session that has the types and records no reason": both depend on the orchestrator seeing whether its session has the types. `task-cycle/skill/SKILL.md` says "Where the session has no such type" without saying how the orchestrator finds out (the list of agent types its dispatch tool offers). A half-sentence would remove the guess. Within scope.

### Outside the task (any grade)

O1. Minor, outside: `installation/install.py` `check_parents` accepts a Windows directory junction as a regular directory (`is_symlink()` is false for a junction, `is_dir()` true). I tried it: a product with `.claude` as a junction to a directory outside the product, `printf 'y\n' | python -B installation/install.py <product> --url <worktree> --apply` exit 0, and `outside1/agents/the-way-author.md`, `outside1/agents/the-way-stage.md` and the `skills/the-way-*` entry points were written outside the product. The same holds for the skills' entry points since before this change (the check is shared), so the new agent paths add no new exposure class; and a junction cannot arrive with a clone (git carries symlinks, not junctions), only from the product's own user. Pre-existing; a task of its own if the human wants it (`os.path.isjunction` in `check_parents`).

O2. Minor, outside: a stray product file `.claude/agents/the-way-ghost.md` whose header names `the-way-author` is kept (correct) but then two files of the product's agent directory carry the name `the-way-author`; Claude Code resolves the duplicate by its own rule. The installer cannot and should not decide it. Noted only.

## Declined to judge

- Whether `disallowedTools: Skill` removes the list of skills from an agent's start in Claude Code 2.1.3xx: the acceptance criterion gives that to the cycle's probe, run by the orchestrator; I did not run it (the directory `.claude/agents/` did not exist when my session started, and the handoff gives the probe to the orchestrator).
- The gate directories I did not run (the full gate is the orchestrator's).
- The wording of the types' two bodies beyond "at least two sentences about what the type is" and the checks in `task-cycle/test_agent_types.py`: the task leaves the wording to the cycle.
- The "about 25" `dispatch … with make-change` clauses in the orchestrator's text: judged under To do 5 below, not as defects.

## Coverage of the task

To do 1 (two definitions, own body of at least two sentences, every tool but the skill tool): met. `task-cycle/agent-types/the-way-stage.md` and `the-way-author.md`: no `tools`, `disallowedTools: Skill`, no `omitClaudeMd`, no `model`, `experimental: cacheTtl: 1h` in the author's only. `task-cycle/test_agent_types.py` fixes each field and the absent ones (8 tests pass).

To do 2 (installer inserts them from the pinned commit; rewrites and deletes only its own; plan shows them before confirmation): met. `AGENT_TYPES`, `agent_definition`, `owned_agent_definition`, `stale_agent_definitions` in `installation/install.py`; the preview prints CREATE with the diff, REPLACE with the diff, DELETE with the reason before "Apply these changes?" (a test asserts the order). Own-file rule: a regular UTF-8 file `the-way-<words>.md`, header name equal to the file name, description ending with the mark. Own-file rule differs from the skills' (no `OWN_MARK` in body) and rests on the mark in the description alone; same stated limit as the skills' ("a file that copies the whole header").

To do 3 (tracked copies for the-way's own sessions): met. `.claude/agents/the-way-*.md` byte-identical to the definitions; generator `agent-instructions/agent_type_copies.py`; its `TrackedCopies` test compares them (cites `# invariant: derived-file-content`); `python -B agent-instructions/agent_type_copies.py` prints "agent type copies are current". `AGENTS.md` and `README.md` name the command.

To do 4 (instruction names the type of each stage in Claude Code; the fallback; writing it in the record): met. `task-cycle/skill/SKILL.md` new paragraph after the handoff paragraph ("In Claude Code, dispatch each stage agent as an agent of one of the pinned the-way's two types: `the-way-author` … `the-way-stage` for every other stage agent … Where the session has no such type … write in the record's row of that dispatch that it ran without its type and why (WAY-370)"), step 9's one-author clause, step 2's list of what the installer owns, and `task-cycle/record_template.md` (the *Author* line and the actor cell). The fallback covers another harness and a session started before `.claude/agents/` held the definitions, as the task lists. See M8 for how the orchestrator finds out.

To do 5 (methods pointed to by a file path, not a skill name to call): met for the three places the task names and for the planner:
- `task-cycle/skill/foundation_step.md`: "written by following the pinned `SKILL.md` of its element" with the five element paths in the pinned the-way, and a rule for a skill that file or a file it reads names by name alone (the `SKILL.md` whose frontmatter `name:` is that name). I checked the five paths exist and their `name:` lines are `record-decision`, `record-invariant`, `record-glossary-term`, `update-part-map`, `record-environment-fact`, and that the elements' skills name other skills only as `record-invariant`, `record-decision` and the like, which that rule resolves.
- `task-cycle/skill/return_step.md`: "by following `elements/glossary/skill/SKILL.md`".
- `task-cycle/change/SKILL.md`: "by following an element's `SKILL.md`, as `task-cycle/skill/foundation_step.md` gives".
- `task-cycle/plan/SKILL.md`: the sentence "each skill named below is the project skill of that name with the `the-way-` prefix" is replaced; the planner's file names no other skill (I grepped every backticked name in it: only `implement-task` as the calling cycle).
- The orchestrator's text and the four methods' labels: step 3 now gives the path of each of the four method files and says the name is a label, and the handoff paragraph already requires the path. Not replacing the ~25 "dispatch … with `make-change`" clauses is a defensible reading of "zlecenie i metody etapów wskazują ścieżką": it is the handoff and the method files that must point by path, and they do. Residue: M4.
- Searches of the three files the handoff named: `task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`, `task-cycle/spec/SKILL.md`, `task-cycle/skill/planning.md`, `task-cycle/change/*.md`: no instruction to call a skill (every hit of "skill" is "this skill holds only…" or an entry-point path).

To do 6 (WAY-255 exception): met; *Rejected* "a longer cache lifetime for every agent" kept with the account by kind of agent: 4.7% and minus 1.4% for every subagent; minus 0.9% and minus 3.6% for the one author, plus 0.7% and plus 2.2% where it is not resumed; plus 1.6% for the executor; plus 0.4% and plus 1.0% for the reviewer of the whole change: each equals the task's Context line (corrected figures, not the earlier minus 1.2% and minus 4.3%). See M1 for the one sentence beyond the task.

Acceptance criterion: not verifiable by this review. The cycle's probe on the Claude Code in use, and its result in the request's description, are the orchestrator's (see Unverified).

Questions to settle, four answers:
- Q1 (no `omitClaudeMd`): WAY-369 and a test that the field is absent; *Rejected* holds only the task's "Not chosen". Met (M2 on the figure).
- Q2 (only the one author has the hour): WAY-255 edit, WAY-368, and `test_only_the_one_authors_type_has_the_hour_long_cache`. Met.
- Q3 (two types, both with every tool but the skill tool): WAY-368; *Rejected* holds the two "Not chosen" lines of the task only (three types with a browser type; two narrow types with plain subagents for interface stages). Met.
- Q4 (Claude Code only): WAY-370; *Rejected* holds the task's Codex "Not chosen" only. Met.

Settlements to record:
- Row 1 (decision, question 3): WAY-368. Source fidelity: binding sentence states two types, no skill tool, the one author's hour, the installer and the generated copies. The figures (72 of 625, 4 of 252; 36,711 and 21,759 tokens; 29,896, 31,547, 22,639, 23,658 characters; 13 and 9 tools; 1,722 and 3,158 characters; 37% against 41%; 4.5%; 6.9 minutes, 10,470 read, 123 written, 4,786) each equal the task's Context, with the conditions the task gives (Claude Code 2.1.322, Sonnet 5.5, a copy of one game product, a live session) and no more. WAY-05 and WAY-27: results described in the entry, no pointer to a private note; I grepped the added lines for disk paths, note titles and the owner's name: none.
- Row 2 (decision, question 1): WAY-369. See M2.
- Row 3 (decision, question 4): WAY-370. The binding sentence also names "a session started before Claude Code could load them", which To do 4 gives, not row 3; fine.
- Edit of WAY-09 (the copies join the files `agent-instructions` owns), WAY-34 (the pin's first commit carries the definitions the installer rewrote): the task lists both as "Bez zmiany" in *Decisions in play*; the edits are the consequence the entries' own wording needs once the installer writes a new kind of file (WAY-263), no binding sentence of WAY-34 changes. I judge them required, not a departure; the request should name them, as the task listed these decisions as unchanged.
- Part map: `task-cycle` (the definitions), `agent-instructions` (*Files* `.claude/agents/**` and the sentence), `installation-command` (lists the definitions rewritten and deleted) — met; `python -B elements/common/foundation_check.py` exit 0 with `0 errors`.

Quotes of the documentation (I fetched https://code.claude.com/docs/en/sub-agents.md and https://learn.chatgpt.com/codex/agent-configuration/subagents on 2026-11-13 and compared word for word): "To prevent a subagent from invoking skills entirely, omit `Skill` from the `tools` list or add it to `disallowedTools`." (section "Preload skills into subagents"; WAY-368 cites § "Preload skills", a shortened heading); the `experimental` row sentences in WAY-368 ("Set its `cacheTtl` key to `5m` or `1h` to choose the prompt cache lifetime for this subagent's requests") and WAY-255 ("Claude Code ignores any other value, ignores `1h` while your Claude subscription is using usage credits, and reads the field only from subagent files"); the `omitClaudeMd` row ("Set to `true` to start this subagent without the user, project, and local CLAUDE.md files"); the watcher sentence ("The watcher covers only directories that existed when the session started, so after creating a scope's first agent file in a new `agents` directory, restart to load it."); the Codex clauses "or `.codex/agents/` for project-scoped agents." and "Disable individual skills with `skills.config`" (the page continues "or bundled skills with `skills.bundled.enabled = false`"). All equal. The last 16,972 characters of the page (read from offset 100000) hold the end of the subagent transcript and compaction sections, the fork section and examples; nothing about skills, `disallowedTools`, cache lifetime, discovery or symlinks bears on the change.

## Open design choices (handoff question)

The two *Questions carried to cycle* are choices of how to make what the task settles, not open design choices as the glossary defines them. Source location and generator: they follow WAY-127 (generated tracked copies of a source, in the part of the generator, WAY-44) and the part-map and WAY-09 patterns; they set no foundation entry beyond what the part-map and WAY-09 edits state, and are cheap to turn back (a rename of two files, the author notes). Names and wording: `the-way-` prefix follows WAY-127's reason for the prefix; wording is checked by a test. No reserved choice (language, framework, library, store, login, place to run) is taken; the generator and installer are Python standard library and git only (`script-imports`, `script-subprocesses` hold).

## Trust boundary: `installation/install.py` (handoff: yes)

Reading the author's tests (`installation/test_agent_types_installation.py`, 12 tests, each preview and `--apply`, whole product tree compared before and after) and my own inputs:

| Input | Where | Result |
|---|---|---|
| a user's file, a header naming another type, no mark, mark outside the description, no frontmatter, non-UTF-8, own header plus a non-UTF-8 byte at `.claude/agents/the-way-stage.md` | author's test | `Existing integration file differs: <path>`, nothing written |
| a directory at an own file's path | author's test | same message |
| `.claude` or `.claude/agents` a regular file | author's test | `Parent path is not a regular directory` |
| symlinked `.claude`, `.claude/agents`, definition, dangling link | author's test (symlinks could be made on this machine; none skipped) | refused, target outside untouched |
| own stale file of a removed type next to the product's own `reviewer.md`, a lookalike `the-way-mine.md`, non-UTF-8 and unmarked files, a directory `the-way-directory.md`, a symlink named like an own file | author's test | only the stale own file is deleted; the others stay; a symlink is not deleted; the agents directory is never removed |
| own definition with CRLF line ends at `the-way-stage.md`, an own stale `the-way-gone.md`, and a file `the-way-ghost.md` whose header names `the-way-author` | mine, scratch product with preview (`python -B installation/install.py <product> --url <worktree>`) | `REPLACE .claude/agents/the-way-stage.md`, `CREATE .claude/agents/the-way-author.md`, `DELETE .claude/agents/the-way-gone.md (its agent type is no longer in the-way)`; `the-way-ghost.md` untouched (name differs from file name) |
| `.claude` a Windows directory junction to a directory outside the product | mine, with `--apply` | not refused: files written outside the product (O1, pre-existing check, shared with the skills' entry points) |
| a name that leaves the directory | the installer's file names come from its own tuple and a directory listing, never from a file's content | no path from input reaches a write; by reading |

The source side: a definition at the pinned commit is checked for its header and mark (`Unexpected agent definition`) and read with `git show`; I read it, not tested (the author says the same). A commit of the-way is trusted input.

Irreversible operation (handoff: no): the cycle installs nothing into a product; the change adds the installer's capability and tests it in temporary products. Confirmed: the preview writes nothing (a test compares the tree), `--apply` asks for "y" after the full plan, DELETE is limited to marked own files.

## Generator and tests

`agent-instructions/agent_type_copies.py` accepts only `the-way-<words>.md` directly in `task-cycle/agent-types/`, UTF-8, LF only, header `name:` then `description:` on single lines, description ending in the mark and a plain YAML scalar, closed frontmatter; prints orphans, deletes nothing; without `--write` prints and writes nothing. Its tests write the expected texts out (not built by the generator's own functions) and cover each refusal; `TrackedCopies` fails when a tracked copy differs or a stray copy exists. Mutations the author applied (reported; I did not repeat them) are the kind these tests catch; I read the tests and found none that asserts nothing.

## Foundation and invariants

The invariants I selected and read whole: `foundation-file-kinds`, `foundation-change-merge-route`, `repository-file-location`, `element-directory-contents`, `return-step-record`, `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `tracked-file-private-paths`, `skill-rule-source`, `script-language`, `script-imports`, `script-subprocesses`, `map-reference-target`, `test-method-citation`, `generated-overview`, `gate-exit-code`, `python-version-declared`, `skill-entry-points`, `instruction-file-imports`, `root-claude-md-import`, `installation-claude-guidance`, `cross-part-imports`. The change breaks none: new files are claimed by a part (`foundation_check.py` 0 errors), no import crosses a part (`agent_type_copies.py` imports `skill_entry_points`, one part; the installation test imports `install`), the only programs started are git and the interpreter, no disk path or note name is added, no changed invariant test (the one new citation `invariant: derived-file-content` is an existing invariant; no invariant file edit). The glossary: the words "stage", "the one author", "agent type" are used as the foundation and the harness use them; a missing glossary entry would be Minor by section 3 unless a sentence is read wrongly, and I cite none.

## Checks I ran

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `2245f0867748452cc07a766fa80f8f01b3288abc` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B agent-instructions/agent_type_copies.py` | 0 | `agent type copies are current` |
| `python -B gate/run_tests.py task-cycle` | 0 | 394 tests OK in 73.8 s |
| `python -B installation/test_agent_types_installation.py` | 0 | 12 tests OK in 160 s, none skipped |
| `python -B task-cycle/change_file_sizes.py 715ae20 2245f08` | 0 | table above |
| `python -B installation/install.py <scratch product> --url <worktree>` (preview) with a CRLF own file, a stale own file and a lookalike | 0 | REPLACE, CREATE, DELETE as the table says |
| `printf 'y\n' \| python -B installation/install.py <scratch product with a `.claude` junction> --url <worktree> --apply` | 0 | wrote through the junction (O1) |
| `grep` over the added lines for disk paths, owner name and note titles | 0 hits | none |
| `WebFetch` of the two documentation pages | — | quotes compared (above) |

Not run: the full gate (`python -B gate/run_tests.py` with no directory) and the full `installation` directory (about 8 minutes; the author ran it on `1239ae2`: 56 tests OK; `2245f08` changes line breaks only); `instruction-files` (the author ran 104 tests OK; `instruction-files/judging.md` changed by one sentence); the acceptance probe of the cycle. No rule-of-size test runs here (the-way has no rule of size, WAY-328): the numbers above are my material.

## Unverified

The acceptance probe: whether an agent of either type starts without the list of skills on the Claude Code the cycle uses. The task says the sondes saw it only for the route through a `tools` list; these definitions take the route `disallowedTools: Skill` (the only way to give every tool of the session but the skill tool). The page text quoted in WAY-368 supports the route; only the probe shows the list vanishing. If it does not, the definitions change to a list of tools (the author's own *Choices* 4 says so), and WAY-368, `installation/README.md` and the type bodies change with them (M7).

Also unshown, and the author says so: the types load in a session only where `.claude/agents/` existed when it started (WAY-368's price, WAY-370's fallback), so the first cycle after the merge in the-way itself may run without them.

## Reaches beyond the handoff

- `https://code.claude.com/docs/en/sub-agents.md` (WebFetch, whole page, then from offset 100000): to compare the quotes of WAY-368, WAY-369, WAY-255 with the page and to read the part the author did not.
- `https://learn.chatgpt.com/codex/agent-configuration/subagents` (WebFetch): to compare the two quotes of WAY-370.
- `foundations/glossary.md` "open design choice": to judge the handoff's question about the two carried questions.
- `foundations/decisions.md` WAY-127, WAY-44 (by its title and the part-map use), WAY-34, WAY-255, WAY-05, WAY-27: to judge the new entries against them.
- `foundations/invariants.md` (the entries listed above): the handoff gave them as gaps to select.
- Grep of `.claude/skills` and `.agents/skills` across tracked text, to see whether any other file lists what the installer owns (none found that needed `.claude/agents`).
- A Windows junction test and a CRLF test of my own, in scratch products under the scratchpad (not in the repository).

## Unread material

Decisions of my selection: 8 read whole (WAY-34, WAY-127, WAY-255, WAY-368, WAY-369, WAY-370, WAY-27; WAY-05 whole up to the end of its *Verification* and the opening of its rationale, the output of that read having been cut), 0 run through by title (I did not screen the other decisions of the log by title; I opened WAY-09 only at the changed passages of the diff, and WAY-125, WAY-148, WAY-229, WAY-347 only by the task's quotations of them). No decision that bears on the change stayed unread to my knowledge; the unscreened rest of the log is the gap.

Not read whole: `task-cycle/skill/SKILL.md` (667 lines): the changed passages and their surroundings, step 3, step 9 and the handoff paragraph; `task-cycle/record_template.md`: lines 1 to 129 only by the diff and lines 125 to the end read whole (no statement contradicts the new text); `task-cycle/review/SKILL.md` whole, `task-cycle/review/whole_change.md` whole, `task-cycle/spec/SKILL.md`, `task-cycle/skill/planning.md`, `task-cycle/skill/spec_review.md` and `task-cycle/skill/correction.md` by search for skill names and their lines of "skill", not whole; the installation tests other than `test_agent_types_installation.py` (I did not read `test_install.py` or the others; they are the gate's); `gate/test_skills_reach_the_way_sessions.py` not opened; the guideline files of `product-guidelines/coding/` not opened (WAY-328: the-way departs from them).

## Searches not found or unclear

- How an orchestrator learns that its session has none of the types (M8): the files give the rule, not the means.
- Whether the two decisions' figure "10.5 thousand tokens" has conditions anywhere in the task: no (M2).
- Whether `subagentPromptCacheTtl`, which the task's Context says outranks the type's field, is documented on the page: not in the 100,000 characters I read nor in the rest; no decision quotes it, correct.
- Whether Claude Code's handling of `disallowedTools: Skill` removes the list of skills: unclear until the probe.
- A command listing the agent types a checkout offers: none found (the author found none either).
