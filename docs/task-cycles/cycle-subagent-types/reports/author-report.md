# Author report — cycle `cycle-subagent-types`

**Status:** done with concerns (concerns: the acceptance probe is the orchestrator's; two figures of the
task's sources have conditions the task does not give; the environment facts for the three decisions'
citations are left to the return step — see "Problems and concerns").

## Commits

Base `715ae20`, head `2245f08`:

- `07cb56a` — Add the definitions of the task cycle's two agent types and the generator of their tracked copies
- `1239ae2` — Install the cycle's agent types into a product and dispatch the stages with them
- `2245f08` — Rewrap the lines the agent type paragraph left long in the cycle skill (line breaks only; `task-cycle` 394 tests, `agent-instructions` 25 tests and `foundation_check.py` run again on it, exit 0)

The worktree is clean (`git status --short` prints nothing).

## Files changed (added / removed lines, `git diff --numstat 715ae20 HEAD`)

| File | + | − |
|---|---|---|
| `task-cycle/agent-types/the-way-stage.md` (new, the definition) | 9 | 0 |
| `task-cycle/agent-types/the-way-author.md` (new, the definition) | 11 | 0 |
| `.claude/agents/the-way-stage.md`, `.claude/agents/the-way-author.md` (new, generated copies) | 9 + 11 | 0 |
| `agent-instructions/agent_type_copies.py` (new, the generator) | 145 | 0 |
| `agent-instructions/test_agent_type_copies.py` (new) | 192 | 0 |
| `task-cycle/test_agent_types.py` (new, content checks of the definitions) | 105 | 0 |
| `installation/install.py` | 58 | 4 |
| `installation/test_agent_types_installation.py` (new) | 332 | 0 |
| `installation/README.md` | 27 | 8 |
| `task-cycle/skill/SKILL.md` | 20 | 8 |
| `task-cycle/skill/foundation_step.md` | 10 | 3 |
| `task-cycle/skill/return_step.md` | 2 | 2 |
| `task-cycle/change/SKILL.md` | 3 | 2 |
| `task-cycle/plan/SKILL.md` | 5 | 3 |
| `task-cycle/record_template.md` | 3 | 2 |
| `foundations/decisions.md` (WAY-368, WAY-369, WAY-370 new; WAY-255, WAY-09, WAY-34 edited) | 160 | 12 |
| `foundations/part_map.md` (`task-cycle`, `agent-instructions`, `installation-command`) | 14 | 9 |
| `AGENTS.md` | 4 | 1 |
| `README.md` | 10 | 6 |
| `instruction-files/judging.md` | 2 | 1 |

## Checks run (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` (before the part map was edited, with the new copies tracked but unclaimed, it printed 2 errors: "no part claims it" for the two copies; fixed by the `agent-instructions` *Files* pattern) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 394 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK (5 skipped, not by my change) |
| `python -B installation/test_agent_types_installation.py` | 0 | 12 tests OK in 125 s; no test skipped (symlinks could be created on this machine) |
| `python -B gate/run_tests.py installation` | 0 | 56 tests OK in 477 s (run on `1239ae2`) |
| `python -B agent-instructions/agent_type_copies.py` | 0 | `agent type copies are current` |

Not run: the product's full gate (`python -B gate/run_tests.py` with no directory) — the orchestrator runs it. The acceptance probe (an
agent of either type starts without the list of skills) — the orchestrator's, on the Claude Code in use.

Mutation checks (each mutation applied, the named tests run, the file restored; all caught):

- installer: `owned_agent_definition` always true → 10 failures; the stale rule without the own check → 2; `rmdir` of the agents directory
  after a delete → 1; own check without the mark → 4; own check without the name comparison → 2.
- generator: mark check off → 1 failure; copy loses a byte → 3; orphans not listed → 1; name not compared to the file's → 1.
- definitions: a `tools` list added, the skill tool not denied, `omitClaudeMd` set, the hour on the stage type, the hour at the top level
  of the author's frontmatter → each fails 1–2 tests of `task-cycle/test_agent_types.py`.

## Own-work check (WAY-164)

- **Requirement my work most likely does not meet:** acceptance criterion — an agent of either type starts without the list of skills.
  I cannot run that probe (it is the orchestrator's, on the Claude Code in use). What I could check: the definitions take the route the task fixes
  (no `tools`, `disallowedTools: Skill`, no `omitClaudeMd`, `cacheTtl: 1h` inside `experimental` of the author's type only), and the locally
  installed Claude Code (2.1.325, `claude.exe`) knows each field the definitions use: `grep -a -c` of its binary for `disallowedTools` 98,
  `cacheTtl` 13, `omitClaudeMd` 22, `experimental` 145 hits, exit 0, and the binary's schema line for `experimental` reads
  `experimental:u({cacheTtl:$_().optional()...` ("5m" or "1h"). `claude agents --json` lists sessions, not types, so loading the definitions was not
  shown. What the probe settles that I did not: that the list of skills vanishes by `disallowedTools` — the task's source saw it only for the route through a
  `tools` list (see Searches).
- **Second requirement:** the installer's trust boundary, strict as for skill entry points. Check: `test_agent_types_installation.py`, below. It showed
  every crafted input refused before anything was written.

## Choices (each with the way rejected and its cost if wrong)

1. **Where the definitions stand.** The source is `task-cycle/agent-types/<name>.md` (two files, the part `task-cycle`); the installer reads
   them from the pinned commit; a new script `agent-instructions/agent_type_copies.py` writes byte-identical copies into `.claude/agents/`
   (part `agent-instructions`, generated files belong to the part of their generator, WAY-44), and `TrackedCopies` in its test compares the tracked
   copies with its output (`# invariant: derived-file-content`) and lists a tracked or stray copy no definition produces.
   Rejected: (a) `.claude/agents/` as the only source, the installer reading the copy of the commit — no generator and no copy to drift, but it needs a
   new *Depends on* of `installation` on `agent-instructions` and leaves the file the installer ships and the file a session loads one file with two
   owners; cost if wrong: a part-map edit and a move of two files. (b) the definitions inside `install.py`, as `skill_wrapper` holds its text — a
   second copy of the text that the-way's own sessions would then need generated from it; (c) one generator for skills and types
   (`skill_entry_points.py`) — its docstring, outputs and tests are written around skills, so the types would stretch a script whose contract the
   invariant `skill-entry-points` names; cost if wrong: two commands to remember, which `AGENTS.md` and the root `README.md` now name. Cost of the
   chosen way if wrong: the cross-script import (`agent_type_copies` imports `git` and `GeneratorError` from `skill_entry_points`, one part).
2. **Names:** `the-way-stage` and `the-way-author`, with the `the-way-` prefix the skills use, so that a product's own agent of a plain name cannot
   be taken for them and the installer owns by prefix. Rejected: `stage` and `author` (a product may hold agents of those names; Claude Code
   resolves two definitions of one name by scope). Cost if wrong: a rename touches the definitions, one constant of the installer and the tests.
3. **How the installer tells a file of its own:** a regular UTF-8 file `the-way-<words>.md` whose header names the type of its file name and whose
   description ends with the sentence `Dispatched only by the task cycle of the-way.` (the mark, stable across commits). Rejected: a name rule alone
   (a product's own `the-way-x.md` would be rewritten or deleted); a comment line in the body (the body changes with the commit and a mark in
   it is hidden from the frontmatter Claude Code reads). Cost if wrong: a product file that copies the whole header is taken for the installer's —
   the same limit the skills' entry points have.
4. **Tools:** no `tools` list, `disallowedTools: Skill`. Rejected: a `tools` list naming every tool — it cannot name the tools of connected
   servers a product has, which the task's answer 3 keeps. Cost if wrong: if Claude Code kept the list of skills with `disallowedTools`, the
   orchestrator's probe shows it and the definitions change to a list of tools.
5. **Bodies:** two paragraphs each (what the type is, what the dispatch gives, that the method is a file read and no skill called; the author's adds
   why its cache lives an hour). No `model` field, so the class set at the dispatch stands (WAY-229). Rejected: an empty body (the task's probe: a
   shorter system prompt), a body that repeats the method (a second copy of text that changes with the pin).
6. **Registry in the installer:** `AGENT_TYPES = ("the-way-stage", "the-way-author")`, a literal like `SKILLS`; a test lists the directory of the
   commit and compares it with the tuple. Rejected: reading the list from the directory of the pinned commit at run time — the stale rule needs
   the list of the running installer's commit, and the installer for a moved pin runs from the new commit's checkout, so the literal and the
   directory can be compared by a test where the run would hide a mismatch.
7. **Stale definitions leave the directory:** the installer never removes `.claude/agents/` when it empties (a skill's own directory it does
   remove); the directory may hold the product's own agents. Rejected: removing an empty directory — a change to a path the product may own.
8. **WAY-255:** the exception is the cache lifetime only; the author's waits stay under about four minutes, since Claude Code falls back to five
   minutes where a subscription spends usage credits (doc quote in the decision). Rejected: lifting the waits of the author to the hour — the
   fallback would then write its whole context anew.
9. **Where the cycle's text says it** (`task-cycle/skill/SKILL.md`): one paragraph after the handoff paragraph, and one clause at step 9 for the author
   and at step 2 for what the installer owns; the record's rows get the type in the actor cell and the *Author* line gets "agent type", with no
   rename of a column (the audit's tests fix a header). Rejected: a new step (the paragraph is as short as its neighbours); renaming the
   `Actor and model` column (a fixture in `process-audit/test_audit_count.py` holds the header).
10. **To do 5 — names kept as labels.** The names `write-spec`, `plan-task`, `make-change`, `review-change` stay in the orchestrator's text as labels of the four method files, and step 3 now says so
    with the path of each; I did not rewrite each of the ~25 "dispatch ... with `make-change`" clauses. Rejected: replacing every label by a path —
    the text would repeat four paths 25 times for no change in what an agent does, since the handoff paragraph already requires the path. Cost if
    wrong: an orchestrator reading "with `make-change`" tells an agent to call a skill; the new paragraph and step 3 say it never does.
11. **Decisions' *Based on* cite the page and passage directly** (as WAY-255 does), not environment facts: the environment-facts element asks for the
    archive of a source (`archived: …`) which I cannot make; the return step writes them (see Concerns).
12. **No invariant.** No decision, the task or a rule I hold sets one; the generator's test cites the existing `derived-file-content`.
13. **No glossary entry.** The words I use — "stage", "the one author", "type" — are used as the foundation already uses them; "agent type" is
    the harness's own term. The return step decides.
14. **The size move of WAY-365 does not apply:** the-way holds no coding guidelines of its own (WAY-328 departs from them), so no rule of size
    stands; `install.py` grew from 614 to 668 lines with no move.

## The entries written (foundation step) — meaning in English and in the task's language

| Entry | Mark | English | Polish |
|---|---|---|---|
| WAY-368 | row 1 | In Claude Code the cycle runs the one author as `the-way-author` and every other stage agent as `the-way-stage`, two types without the skill tool, so a method is a file read by its path; the installer writes the definitions, the copies of the-way's own sessions are generated. | W Claude Code cykl zleca jednego autora typem `the-way-author`, a każdego innego agenta etapu typem `the-way-stage` — oba bez narzędzia skilli, więc metodę czyta się jako plik po ścieżce; instalator wpisuje definicje do produktu, a kopie dla sesji na samym the way są generowane. |
| WAY-369 | row 2 | The two types start with the instruction files of the session; no definition sets `omitClaudeMd`. | Oba typy startują z plikami instrukcji sesji; żadna definicja nie ustawia `omitClaudeMd`. |
| WAY-370 | row 3 | Where the session has none of the types — another harness or a session started before they could load — the cycle dispatches as before and records that in the row of the dispatch; there are no types for Codex. | Gdy sesja nie ma typów — inna uprząż albo sesja uruchomiona, zanim mogły się załadować — cykl zleca etap jak dziś i zapisuje to w wierszu zlecenia; Codex nie dostaje typów. |
| WAY-255 (edited in place, *Rejected* kept with the account by kind of agent) | the cycle's (To do 6) | The one author's cache lives an hour, set by its type; its waits stay under about four minutes; the hour for every agent stays rejected, with the account by kind of agent. | Pamięć podręczna jednego autora żyje godzinę, ustawia ją jego typ; jego oczekiwania nadal mieszczą się w ok. czterech minutach; godzina dla wszystkich agentów zostaje odrzucona, z rachunkiem według rodzaju agenta. |
| WAY-09 (edited) | the cycle's | The repository also holds the copies of the cycle's agent type definitions under `.claude/agents/`, files of `agent-instructions`. | Repozytorium zawiera też kopie definicji typów agentów cyklu w `.claude/agents/`, pliki części `agent-instructions`. |
| WAY-34 (edited) | the cycle's | The move of the pin's first commit carries the agent type definitions the installer rewrote. | Pierwszy commit przesunięcia przypięcia niesie też definicje typów agentów, które przepisał instalator. |
| part map: `task-cycle`, `agent-instructions` (*Files* + sentence), `installation-command` | the cycle's | The map names the definitions, their copies and what the installer rewrites and deletes. | Mapa wymienia definicje, ich kopie oraz to, co instalator przepisuje i usuwa. |

The search of the whole foundation (WAY-33) found: WAY-09 (files of the repository), WAY-34 (what a move carries), WAY-127 (about skills only, left; WAY-368
derives from it), WAY-255 (the exception), `installation-command` and `agent-instructions` in the part map. Nothing else names `.claude/` files or the
skill list; no entry gains a glossary term. Each decision passes `foundation_check.py` (exit 0). A *Rejected* of a decision from a row holds only the ways of the
row's source (question 3, 1 and 4 of the task): done.

## Trust boundary (`installation/install.py`) — crafted inputs tried and what each showed

All in `installation/test_agent_types_installation.py`, each both as preview and with `--apply`; every case ended with a non-zero exit before anything was
written, the whole product tree (every path with its bytes) unchanged, `git ls-files --stage` empty:

| Input at `.claude/agents/the-way-stage.md` (or the parent) | Showed |
|---|---|
| a user's file; a header naming another type; no mark in the description; the mark outside the description; no frontmatter | `Existing integration file differs: <path>` |
| non-UTF-8 bytes; an own header followed by a non-UTF-8 byte | same message |
| a directory at `.claude/agents/the-way-author.md` | same message |
| `.claude` or `.claude/agents` a regular file | `Parent path is not a regular directory` |
| `.claude` a symlink to a directory outside; `.claude/agents` a symlink; the definition a symlink to a file; a dangling symlink | `Parent path is not a regular directory` / `Existing integration file differs`; the outside directory holds only its own file with its bytes |
| an own definition of an earlier commit | `REPLACE`, diff shown, rewritten on apply; the product's own `reviewer.md` and a lookalike `the-way-mine.md` untouched |
| `the-way-gone.md` (own, type removed) | `DELETE … (its agent type is no longer in the-way)`, deleted on apply; files without a mark, with another name, non-UTF-8, a directory `the-way-directory.md`, a symlink named like an own file, `the-way-notes.txt` are kept |
| a name that would leave the directory | the installer's names come from its own tuple and from a listing of the directory, never from a file's content; a source whose header names another type than its file is refused (`Unexpected agent definition`) — not tested with a crafted commit; the generator rejects a source file named off the form (the cases `stage.md`, `the-way-Stage.md`, `the-way-..%2fx.md`, a subdirectory) |

Not covered by a test: a crafted definition in the-way's own *commit* (the installer takes the commit as trusted; it verifies the header and the
mark and refuses with `Unexpected agent definition`, shown by reading, not by a test).

## Each reach beyond the handoff

- `https://code.claude.com/docs/en/sub-agents.md` (WebFetch, twice) — the frontmatter fields and the passages quoted in the decisions (the handoff
  fixed the form but the quotes had to be read verbatim; the task quotes some of them).
- `https://learn.chatgpt.com/codex/agent-configuration/subagents` (WebFetch) — the quotes of WAY-370's *Based on*, which the task cites without passage.
- `foundations/decisions.md` WAY-09 (read whole) — found by the search of the whole foundation; edited.
- `README.md` (root), `instruction-files/judging.md` — found by a search for "entry point"; both name what the installer writes; edited.
- `process-audit/test_audit_count.py:690` (a grep hit) — why the record's column header is not renamed.
- `elements/part-map/skill/*`, `elements/part-map/template.md`, `elements/decisions/template.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md` — the skills of the elements, as the handoff says (named here for completeness).
- `claude --version`, `claude agents --json`, `grep -a` on the Claude Code binary — to see whether the local version knows the fields.

## Unread material

- The last 16,972 characters of the Claude Code subagents page (the fetch returned the first 100,000 of 116,972).
- Invariants not read: the entries `foundation-file-kinds`, `foundation-change-merge-route`, `return-step-record`, `ci-checking-commands`,
  `map-reference-target`, `test-method-citation`, `python-version-declared`, the invariants of `project-level` and `relation-model`, `gate-exit-code`
  (lines 1–25, 66–85, 136–260 and 301–325 of `foundations/invariants.md` were not opened; the handoff's selection named the invariants of
  `agent-instructions` and `installation` and `skill-entry-points`, all read whole, and `derived-file-content`, `repository-file-location`,
  `script-*`, `cross-part-imports`, `generated-overview`, `tracked-file-private-paths`, read).
- `task-cycle/record_template.md` lines 130–end (I read 1–129 and edited within them).
- `task-cycle/review/SKILL.md`, `task-cycle/spec/SKILL.md`, `task-cycle/skill/planning.md`: lines 1–30 or 1–40 only, read in a search for a skill named as a thing to call (none).
- The files of `product-guidelines/coding/` that WAY-328 points to: WAY-328 departs from them for the-way, so none binds; not opened.
- `gate/test_skills_reach_the_way_sessions.py`: first 80 lines (the invariant's end-to-end test; unaffected).
- Installation tests other than `test_install.py` and `test_coding_guidelines_installation.py` (`test_lead_*`, `test_styleguide_*`, `test_testing_guidelines_*`,
  `test_installed_guidance.py`): not read, only run by the gate of `installation`.

## Searches not found or unclear

- The conditions of the figure "start without the instruction files: 10.5 thousand tokens" are not given in the task (version, model, tool list of the probe's agent);
  WAY-369's rationale gives the figure with the comparison the task's row 2 makes (21,759 − 10.5k = about 11k) and says no more.
- The conditions (version, model) of the cache probe (6.9 minutes; 10,470 read, 123 written; 4,786 control) are not given in the task; WAY-368 and WAY-255 state them as "a probe of the cache, in a live session".
- The estimate "about 4.5% of a cycle's cost" is stated in the task for a start lighter by 41% (the narrow list of tools); WAY-368 says that and gives 37% for these types; the task gives no figure of the gain for 37%.
- Whether `disallowedTools: Skill` removes the list of skills from the start: the docs say omitting `Skill` from `tools` *or* adding it to `disallowedTools` prevents invoking skills; the task says only the route through `tools` was seen to remove the list. Unclear until the orchestrator's probe.
- `claude agents --json` printed sessions (kinds, ids), not agent types, so I found no command that lists the types a checkout offers.
- The task's context mentions the setting `subagentPromptCacheTtl` taking precedence over the field; the fetched page text I read has no sentence about it (the binary's schema text does mention it), so no decision quotes it.
- The section names of two of the Claude Code quotes (the frontmatter reference table's `experimental` and `omitClaudeMd` rows; the note on the watcher) are my descriptions; the page's own headings were not given by the fetch.
- No rule of size in the-way's own guidelines (WAY-328): none sought further.

## Problems and concerns

- **For the orchestrator, the probe:** run it on a type from `.claude/agents/` after a session starts in the worktree (the directory did not exist when this session started, so Claude
  Code does not load the types in it before a restart: WAY-368's price, the same fact the cycle's fallback records).
- **Environment facts for the return step:** the three Claude Code quotes (skills prevented by omitting the tool, `experimental.cacheTtl` with the usage-credits fallback, the
  watcher covering only existing directories) and the two Codex quotes sit as direct citations in WAY-368, WAY-369, WAY-370 and WAY-255; the return step may turn them into entries of
  `foundations/environment_facts.md` (the archive of the source is part of that form).
- A cycle run in the-way's own checkout dispatches stages with types only where the session started after `.claude/agents/` held the copies; the first cycle after the merge
  runs its stages without them where the orchestrator's session is older, and records it (WAY-370).
- The 12 tests of the new installation test file take 125 s, since each clones the repository; the gate of the whole `installation` directory is long, and I ran it in the background.
- The installed `.claude/agents/the-way-*.md` have no pointer to a commit (they name none); a product's own `.gitignore` of `.claude/` is warned about by the existing
  warning for ignored paths (tested).
