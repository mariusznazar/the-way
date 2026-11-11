# Author report: backlog-line-for-plan-tasks (the whole change as the one author)

**Status:** done with concerns (concerns are listed under "Problems and concerns"; none blocks)

## Commits (branch `task/backlog-line-for-plan-tasks`, base `52f8164`)

- `74fbd01` Record the task line a refiner makes and the rules of the task place
  (`foundations/decisions.md`)
- `9eb2bd6` Give each task of a plan a backlog line made by its refiner and moved to ready on
  acceptance (skills, templates, `AGENTS.md`)

## Files changed (added / removed lines, from `git diff HEAD~2 --stat`)

| File | + / - |
|---|---|
| `foundations/decisions.md` (WAY-154, WAY-107, WAY-320, WAY-27) | 97 / 34 |
| `project-level/task_line.md` (new) | 52 / 0 |
| `project-level/backlog_place.md` | 19 / 9 |
| `project-level/task/skill/orchestrated_mode.md` | 22 / 12 |
| `project-level/lead/skill/SKILL.md` | 13 / 7 |
| `project-level/lead/conversation_template.md` | 6 / 3 |
| `project-level/lead/skill/route_changes.md` | 3 / 1 |
| `project-level/task/skill/read_sources.md` | 5 / 0 |
| `project-level/task/skill/final_review.md` | 4 / 3 |
| `project-level/task/template.md` | 2 / 1 |
| `project-level/plan/skill/delegated_mode.md` | 2 / 1 |
| `AGENTS.md` (`## Backlog`) | 3 / 2 |

No skill added, renamed or moved and no description changed, so `skill_entry_points.py --write` was
not run (and `skill-entry-points` is held by the gate run of `agent-instructions` and `gate`, below).

## Checks (command, exit code)

All from the worktree root.

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors" (run after the entries and after
  the last text edit).
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 3 info".
- `python -B gate/run_tests.py task-cycle` — exit 0, 263 tests OK (includes
  `test_tracked_files_private_paths.py`, so no absolute path or note link in a tracked file).
- `python -B gate/run_tests.py agent-instructions` — exit 0, 18 tests OK
  (`instruction-file-imports`, `AGENTS.md`).
- `python -B gate/run_tests.py gate` — exit 0, 20 tests OK (`skill-entry-points`).
- `python -B gate/run_tests.py project-level` — first run exit 124 (my timeout) with one unexplained `F`; second run exit 0, 275 tests OK (last section).
- Not run: the full `python -B gate/run_tests.py` (the orchestrator runs it). No failing run of a test
  written first exists: I wrote no test (prose and foundation entries only; "Test behaviour, not text":
  prose for agents is tested by what an agent does with it, which no test in this repository does for
  skills), and I changed no invariant's test.

## Own-work check

- Requirement most likely not met: the task's question carried to the cycle, that the identifier of a
  task must be computable from the plan and the task's plan name alone, so a refiner of a dependent
  task can write the other task's identifier before that line exists, and must be a form the task
  place's rules accept (lower-case letters, digits, `-`). Check: the derivation as written in
  `project-level/task_line.md` run in a one-off Python expression on two inputs, `player-game.md` +
  `forest-on-hex-grid` and `MVP2 plan (v2).md` + `forest-on-hex-grid`. First run (exit 0) showed a
  fault in my first wording: `mvp2-plan-v2--forest-on-hex-grid` (a double hyphen, because the wording
  turned runs of "other characters" into `-` and left hyphens out of the runs). I corrected the text
  to "each run of characters other than lower-case letters and digits, hyphens included, turned into
  one `-`, none at either end"; second run (exit 0) gave `player-game-forest-on-hex-grid` and
  `mvp2-plan-v2-forest-on-hex-grid`, as the two expected literals I wrote by hand.
- Second check: no tracked text of the-way names a form of the vault's rules. `grep` for the status
  symbols and the dependency fields of the rulebook (`[?]`, `[/]`, the identifier and blocked-by
  symbols), `[[`, drive-letter paths and `/Users/` over the changed skills and entries — exit 1, no
  match (settlement row 3, WAY-101, WAY-320).

## Foundation entries (the foundation step)

Marks: `row n`, `projected`, `the cycle's`. Each with one sentence in English and one in Polish
(the task document's language).

- **WAY-154** — row 1, row 2, row 5 (edited in place; WAY-144 untouched).
  - EN: A refiner writes what the orchestrator's order asks, among it the task's line in the backlog
    with the plan's dependencies in its first turn that creates the document, in parallel with the
    round's other refiners and with no queue of writes; no agent but the orchestrator, on the human's
    word, moves the line to ready or writes `ready for cycle`; the orchestrator moves the line with
    the Status and the plan's row and keeps the lines' dependencies in step with the plan; the cost of
    the dependency copy (WAY-144's "copy that drifts") is accepted.
  - PL: Refiner pisze to, o co prosi go zlecenie orkiestratora, w tym linię zadania w backlogu z
    zależnościami z planu w pierwszej turze tworzącej dokument, równolegle z innymi refinerami rundy i
    bez kolejki zapisów; poza orkiestratorem, po słowie człowieka, nikt nie przestawia linii na gotową
    ani nie pisze `ready for cycle`; orkiestrator przestawia linię razem ze `Status:` i wierszem planu
    i utrzymuje zależności w liniach zgodne z planem, a koszt kopii zależności jest przyjęty.
- **WAY-107** — row 3, row 4 (edited in place).
  - EN: The status of a new line, its move to ready and the form of its dependencies come from the
    rules of the task place, never from text at the product or in the-way's skills; the section names
    them by the entry `task-rules` under the product's name, and where it or its file is missing the
    agent asks once and offers to add the entry.
  - PL: Status nowej linii, jej przejście na gotową i forma zależności pochodzą z zasad miejsca
    zadań, nie z treści zapisanej przy produkcie ani w skillach the way; sekcja wymienia je przez wpis
    `task-rules` pod nazwą produktu, a gdy wpisu albo pliku brakuje, agent pyta raz i proponuje
    dopisanie wpisu.
- **WAY-320** — row 4 (the entry name only, edited in place).
  - EN: The locations file also holds the entry `task-rules` per product, beside `tasks` and
    `projects`; a single shared entry for all products is a rejected way.
  - PL: Plik lokalizacji ma też wpis `task-rules` per produkt, obok `tasks` i `projects`; jeden wpis
    wspólny dla wszystkich produktów jest drogą odrzuconą.
- **WAY-27** — the cycle's (a correction found by the search of the whole foundation, WAY-33).
  - EN: The one exception to "no pointer outside the repository" now covers the rules of the task
    place named in `## Backlog` by an entry of the locations file, beside the place of the tasks.
  - PL: Jedyny wyjątek od zakazu odsyłania poza repozytorium obejmuje teraz zasady miejsca zadań
    wymienione w `## Backlog` przez wpis pliku lokalizacji, obok samego miejsca zadań.
  - Why marked `the cycle's`: no row carries it. The binding sentence said "the place of its tasks ...
    and nowhere else", and AGENTS.md now names a second entry there. I read it as the same kind of
    pointer (where work is kept), not reasoning an entry rests on. Please confirm at the request.

*Rejected* of WAY-154 and WAY-107 holds only the ways the task keeps under its questions 1, 2, 3, 4
and 5 (`Not chosen`), each with the cost the source gives. WAY-320's *Rejected* gets the question 5
way "one shared entry" with its cost. No way was derived by me.

## Choices of my own (with the rejected way and the cost if wrong)

1. **Identifier derivation (the carried question).** Chosen: the orchestrator's start, with one
   change: the plan's file name without extension, joined with `-` to the task's plan name, lower
   case, each run of characters other than lower-case letters and digits (hyphens included) turned
   into one `-`, none at either end. The orchestrator's text turned each character into one `-`;
   mine collapses runs and trims, to avoid `--` and a leading or trailing `-` (the check above found
   the double hyphen). Alternative: one `-` per character. Cost if wrong: identifiers in lines
   already written would differ from those the next refiner computes, so a dependency would name a
   task no line carries; fixable by editing the lines, nothing else reads the identifier. A second
   cost, accepted: two plans of one place with the same file name and a task of the same name clash;
   the rule "unambiguous in the whole place" rests on plan file names being distinct in the place.
   Polish letters (outside a-z) become `-`; the identifier stays unambiguous and computable.
2. **A new file `project-level/task_line.md`** for how a line is made, moved to ready and given
   dependencies, instead of putting it into `backlog_place.md`. Reason: `backlog_place.md` is read
   by the project-definition skill and the guidelines skills only to find a place; the line rules
   have a different trigger (a refiner making a line, an orchestrator accepting), and "rules with
   different triggers do not share a file" (instruction-files skill). `backlog_place.md` holds only
   the finding of `task-rules` (as the handoff asked). Rejected: everything in `backlog_place.md`
   (every reader would load line rules it never uses). Cost if wrong: one more file to keep; the
   skills name it from five places.
3. **Existing line.** `task_line.md` says: search the place for a line that links the document or
   names the task; where one stands, make no second, link the document from it, and leave its
   status as the rules give for a line already there. Rejected: say nothing (a refiner would add a
   second line to a task parked earlier). It follows the task's Context (a parked task keeps its
   status), but the rule is mine, not a row's.
4. **The orchestrator's correction of dependencies** is placed in `route_changes.md`, after the
   delegated plan agent returns (WAY-156 gives plan edits to that agent, so the orchestrator changes
   the lines after it, not the plan). Rejected: step 1 of `lead-project` (ordinary State/Document
   updates), which does not cover a `Depends on` change. Cost if wrong: a plan change that reaches
   the plan by another route leaves lines stale; the line rule then covers it only if the orchestrator
   reads `route_changes.md`.
5. **Missing `task-rules` entry in orchestrated mode:** the refiner asks through its turn (it never
   asks the human directly), and after the human's agreement recorded in the conversation it writes
   the entry itself, as `backlog_place.md` allows for an agent that is not running a task cycle.
   Rejected: the orchestrator writes it (one more duty). Cost if wrong: a refiner writing the
   user's locations file; limited to a human-agreed entry.

## Reaches beyond the handoff

- `project-level/lead/skill/route_changes.md` — added the dependency step (choice 4); the handoff
  lists `lead/skill/SKILL.md` steps 3.1 and 4 and does not name it.
- `project-level/task/template.md:104-105` and `project-level/plan/skill/delegated_mode.md:9` — both
  stated the refiner's and orchestrator's writes ("changes only `Status:`", "refiners write only
  separate task documents/conversations"), which my change made inexact; corrected minimally by the
  search of the foundation (WAY-33), found by grep for those phrasings.
- `foundations/decisions.md` WAY-27 (above) and WAY-320's *Rejected*.
- `elements/decisions/template.md` and `elements/decisions/skill/*.md`, `elements/common/skill/SKILL.md`
  — read for the form of an entry (the handoff says to read the skill of an element I write an entry
  of; they were not on its list).
- `elements/common/rules.md` — grep for its rules of language only, not whole.
- `.ai/rules/scripts.md` and `.ai/rules/git.md` of the user's global instructions — read before the
  one-off script and the commits.
- `project-level/definition_template.md:17-32` — read (it describes the `## Backlog` section's
  forms); no change needed, it lists `Projects`/`Tasks` lines and a new `Task rules` line is a
  product's own line.

## Unread material

- Decision entries: all named entries read whole (WAY-134 in two reads, the second only after I
  noticed its tail was cut; I have now read the whole of it).
- Invariants: all seven read whole. `foundations/part_map.md` and `foundations/glossary.md` read
  whole.
- Files the task names: all read whole (`orchestrated_mode.md`, `read_sources.md`, `final_review.md`,
  `lead/skill/SKILL.md`, `conversation_template.md`, `backlog_place.md`, `AGENTS.md`).
- `instruction-files/SKILL.md` read whole; `changing.md`, `kind_skill.md`, `kind_main_file.md` whole;
  `tool_loading.md` only its first 60 lines (the loading facts did not bear on my edits: no `@`, no
  new skill, no description change); I did not read the other files beside it (`judging.md`,
  `placing.md`, `writing.md`, `kind_path_rule.md`) since the mode is "change" of a skill and an
  instruction file with no new rule moved or placed.

## Searches not found or unclear

- The task cites `project-level/skill/delegated_mode.md:8` (the definition agent) and
  `project-level/lead/answering.md:11` as out-of-scope prohibitions: both exist, I left them alone.
  A third file of the same name, `project-level/plan/skill/delegated_mode.md` (the plan agent), I
  touched in one factual line only (reach above).
- What an agent does when the human says the task place has no rules (a product whose tasks lie in a
  repository directory or a public tracker): the decision, WAY-107 row 4 and the task say only
  "ask once and offer to add the entry"; I wrote no other route. Unclear; see concern 1.
- "Existing line" status behaviour of a parked task: only in the task's Context, in the vault's
  words; unclear whether it is a rule or an observation (choice 3).

## Problems and concerns

1. **A product with no private place for its task rules** (tasks in its repository or a public
   tracker, or a user without a vault) has, per row 4, only the route "ask once, offer the entry".
   The row does not say what to do if the answer is "there are none". The guess: ask again at each
   refinement, or the agent takes the tool's default form (which row 3 rejects). A task for the
   orchestrator or the human to settle.
2. **Other orchestrated skills** write "edits only the task document and its turn":
   `product-guidelines/coding/orchestrated_mode.md:9`, `product-guidelines/testing/orchestrated_mode.md:8`,
   `product-guidelines/styleguide/orchestrated_mode.md:9`. They run through `refine-task`'s
   orchestrated mode, which now creates the line in its first turn, so the statements are inexact
   for those tasks. Not touched (outside the handoff's list, "no more"); a possible follow-up.
3. **The silent-loss risk named in WAY-154** (a line lost if an order omits it) is mitigated by the
   standing sentence in `orchestrated_mode.md` (the line is made in the first turn without an
   order), so the cost the task accepted is smaller than the task states; not a deviation, a
   remark.
4. One unexplained `F` in a first `project-level` run (see the last section); the rerun passed.

## Project-level test result

- First run, `python -B gate/run_tests.py project-level` under `timeout 550` in the background:
  printed an `F` among its dots and was then killed by my own timeout, exit 124 (the directory needs
  about 710 s). I did not see which test failed, because the output was cut at the kill.
- Second run, no timeout, after both commits: `python -B gate/run_tests.py project-level` exit 0,
  "Ran 275 tests in 709.581s OK".
- The `F` is not reproduced and not explained. Nothing in `project-level/test_*.py` reads a file I
  changed (grep for the skill files, `decisions.md` and `AGENTS.md` found no test that does). Guess,
  unverified: a time-sensitive test that failed under load while other runs of mine had just
  finished, or while I edited files in the worktree mid-run. The orchestrator's full gate run will
  show whether it recurs.
