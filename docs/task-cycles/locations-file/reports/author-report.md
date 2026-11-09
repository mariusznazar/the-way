# Report — the one author (`make-change`, the whole change as the one author)

Saved by the orchestrator from the author's returned text: the author's Write tool refused the file
("Subagents should return findings as text, not write report files"), and the author did not work
around it. The words below are the author's.

Status: **done with concerns** (the concern: the report file could not be written by the author).

**Commit:** `973ee64` on `task/locations-file`, base `17b83bf`. The worktree is clean.

**Check result:** I broke nothing that I could see, and nothing failed. I did not run the full `python -B gate/run_tests.py`, since that is the orchestrator's. `foundation-review` and `product-guidelines` return exit 1 with "no test found" because neither holds a test. The change touches no screen, so no UI check applied.

## Files changed (added / removed lines)

- `AGENTS.md` 6/5: `## Backlog` now names the entry `tasks` under `the-way` in `~/.the-way/locations.json`, with no path. If the file or entry is missing, the agent asks the human and offers to add the entry. The Ready line keeps its command and names the author's rules for agent tasks in words.
- `foundations/decisions.md` 77/14: WAY-27 and WAY-107 edited in place (row 1), new WAY-320 (row 2).
- `foundations/invariants.md` 11/1: `outbound-link-reach` loses the `## Backlog` exception. New invariant `tracked-file-private-paths` (row 3).
- `project-level/backlog_place.md` 38/0, new: how a skill reads the section, resolves a locations-file entry, and records a missing place.
- Pointers to `backlog_place.md`:
  - `foundation-review/SKILL.md` 5/5
  - `project-level/skill/first_write.md` 2/2
  - `project-level/task/skill/read_sources.md` 5/5
  - `project-level/task/skill/final_review.md` 1/1
  - `project-level/lead/skill/SKILL.md` 2/1
  - `task-cycle/skill/SKILL.md` 2/1
- `project-level/definition_template.md` 5/3: the sample section allows a locations-file entry and says a place on the user's disk is never a path.
- `task-cycle/test_tracked_files_private_paths.py` 128/0, new: the test for *To do* 4.

I left the four `installation/test_*_installation.py` files and `product-guidelines/{coding,testing}/recognize.md` alone. They only mention the section name.

## Checks (command, exit code)

- **Failing run first:** `python -B gate/run_tests.py task-cycle` before the `AGENTS.md` change gave exit 1. The one failure was the new test, listing exactly `AGENTS.md:20` and `AGENTS.md:25`.
- **Passing run:** the same command after the change gave exit 0 (209 tests).
- **Break and restore:** I appended a path and a note link to `foundation-review/SKILL.md`. `python -B -m unittest task-cycle.test_tracked_files_private_paths` failed, naming `:106` and `:107`. I restored the file.
- `python -B elements/common/foundation_check.py`: exit 0, 0 errors.
- `python -B gate/run_tests.py <dir>` gave exit 0 for `gate` (20), `instruction-files` (104, 5 skipped), `agent-instructions` (18), `project-level` (271), `elements/common` (109), `installation` (44) and `relation-model` (20).
- `python -B -m unittest discover -s gate -p "test_*.py"`: exit 0. I ran it as a precaution; `gate/run_tests.py` is unchanged.
- `python -B task-cycle/private_paths_check.py foundations`: exit 0, 0 listed.

## Own-work check

The requirement most likely unmet was *To do* 3: every skill that looks for a backlog finds it when the section points to the locations file. I grepped tracked files for "## Backlog", "backlog" and "WAY-107" and read each hit. Six files find a place and now point to `backlog_place.md`: the five skills above plus `task-cycle/skill/SKILL.md`, which writes the request link into the task's entry. The other hits only name the section or reach it through those six. A skill that refers to the backlog by other words than "backlog" or "task area" could still be missed.

## Weakest point

- **Exempt list kept twice.** The four exempt files are named in the invariant's sentence (WAY-60 requires it) and in the test. `test_the_exempt_files_are_the_ones_the_invariant_names` reads the sentence and fails on drift. If the sentence is reworded so the names are not backticked `.py` files, that test fails rather than passes silently.
- **Skills have no behavioural test.** *To do* 3 is prose only, so the review should read `backlog_place.md` and the six pointers.
- **Two behaviours I added, not in the task text.** `backlog_place.md` says that an agent in a task cycle writes nothing outside the repository (WAY-140) and reports the missing entry. It also says that an entry whose path does not exist counts as a missing place. If you disagree, each is a sentence to remove.

## Foundation entries

| Entry | Mark | English | Polish |
|---|---|---|---|
| WAY-320 (new decision) | row 2 | A user's places outside every repository are kept in one file, `~/.the-way/locations.json`, in a fixed place with no environment variable: an object of repository names, each holding entries by name such as `tasks` and `projects`. Tracked files name an entry instead of a path. | Miejsca użytkownika poza każdym repozytorium stoją w jednym pliku `~/.the-way/locations.json`, w stałym miejscu i bez zmiennej środowiskowej: obiekt nazw repozytoriów, a pod każdą pozycje po nazwie, np. `tasks` i `projects`. Pliki repozytorium wskazują pozycję zamiast ścieżki. |
| WAY-107 (edited) | row 1 | A place on the user's disk outside every repository stands in `## Backlog` as a locations-file entry, never as a path. A directory of the repository or a public tracker stays as it is. A missing place, file or entry makes the agent ask and offer to record it where it fits. | Miejsce na dysku użytkownika poza repozytorium stoi w `## Backlog` jako pozycja pliku lokalizacji, nigdy jako ścieżka. Katalog w repozytorium albo publiczny tracker zostaje wprost. Gdy brakuje miejsca, pliku albo pozycji, agent pyta i proponuje wpis tam, gdzie pasuje. |
| WAY-27 (edited) | row 1 | The exception for the place of the tasks stays, but `## Backlog` names it by a locations-file entry, never by a path. | Wyjątek dla miejsca zadań zostaje, ale `## Backlog` wskazuje je pozycją pliku lokalizacji, nigdy ścieżką. |
| `tracked-file-private-paths` (new invariant, method `test`) | row 3 | No tracked file, outside four named files that write example paths, holds an absolute path or a note link as WAY-309 names them. | Żaden plik śledzony przez git, poza czterema nazwanymi plikami piszącymi przykładowe ścieżki, nie zawiera ścieżki bezwzględnej ani linku do notatki w rozumieniu WAY-309. |
| `outbound-link-reach` (edited, stays `review`) | row 3 | The exception for a link to the place of the tasks is removed. | Wyjątek dla linku do miejsca zadań znika. |

No entry is marked `the cycle's`.

- **Search of the foundation (WAY-33):** I grepped `foundations/` for backlog, absolute path, outbound-link, private note and locations. The other decisions that mention the backlog (WAY-101, 140, 153, 308, 309) stay true.
- **Not changed:** glossary and part map. No word takes a new meaning, and instructions read the locations file, not code of a part.
- **Rejected ways:**
  - WAY-320: the five ways of question 1, with their costs.
  - WAY-107: the way of question 4 and two ways of question 1.
  - WAY-27: the one way of question 1 that concerns the exception.

## Autonomous choices

1. **How the foundation records the new check.** It is a new invariant of its own, `tracked-file-private-paths` (method `test`, about paths and note links only). `outbound-link-reach` stays `review` and keeps its sentence about unreachable repositories and private note collections.
   - Not taken: turning `outbound-link-reach` itself to `test`. WAY-61 allows `test` only when a test checks the whole sentence, and this test checks half of it.
   - Not taken: splitting `outbound-link-reach` in two. It gives the same result with a withdrawn identifier and rewritten references.
   - Cost if wrong: merging two entries and the `Derives from` of one.
2. **The test stands in `task-cycle/`, not `gate/`.** `gate` depends on none, so a test there cannot import `private_paths_check.py` (invariant `cross-part-imports`). Copying the pattern would make a second pattern. Cost if wrong: someone looks in `gate/`, and moving the test means giving `gate` a dependency or copying the pattern.
3. The test reuses `private_paths_check.check_file`, so the script's rules for BOM, UTF-16 and binary files apply.
4. One shared `project-level/backlog_place.md` instead of six copies of the rule. Cost if wrong: a skill that reads only its own file misses the pointer. Each pointer names the file.
5. WAY-320 is a new decision rather than folded into WAY-107. Its *Scope* is agent-instructions, project-level, foundation-review, product-guidelines and task-cycle. I added foundation-review and product-guidelines to WAY-107's scope.
6. `AGENTS.md` names the key and entry in words ("the entry `tasks` under `the-way`"). `backlog_place.md` defines that form.

## Reach beyond the handoff

- The two element templates, `elements/common/rules.md`, `elements/common/way_of_working.md`, and the `skill/` files of the decisions and invariants elements. The record skills require them.
- Decisions WAY-101, WAY-153 and WAY-33's grep of the whole foundation, to find other entries that speak of the backlog place. None changed.
- `gate/run_tests.py`, `gate/test_skills_reach_the_way_sessions.py`, `elements/part-map/template.md`, `project-level/plan/template.md:21` and `task-cycle/skill/SKILL.md:70-80`, to place the test and settle the part-map question.
- I did not read `~/.the-way/locations.json`. The task text gave its form, which was enough.

## Searches not found or unclear

- I read WAY-27, 107, 308, 309, 61, 140 and 16 whole. WAY-07, 25, 33, 114 and 134 I read through the templates and the foundation step that carry their rules, not entry by entry.
- The task does not say whether a product's key in the locations file is its directory name or the name given in its `## Backlog` line. I made the line name it, so nothing is inferred.
- The task does not say what to do when the entry exists but its path does not. `backlog_place.md` treats that as a missing place (see the weakest point).
- The hint "about 15 files name `## Backlog`" matched 15 hits in 12 files. Six find a place (changed), four are installation test fixtures, and two only name the section.
- `guidelines/` is absent, as the handoff says.
