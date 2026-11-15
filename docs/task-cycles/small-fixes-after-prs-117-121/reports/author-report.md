# Report of the one author — task `small-fixes-after-prs-117-121`

**Status:** done with concerns (the concerns are the four small adaptations named under "Problems and concerns"; no question blocks the cycle).

## Commits (base `b6b3416`)

| Commit | What |
|---|---|
| `ac3c96f` | move: `git`, `fork_point`, `at_commit`, `read`, `MAIN_BRANCHES` out of `foundation_check.py` into the new `elements/common/foundation_source.py`, no change of behaviour |
| `677ad78` | To do 1, 2: gate test module records each event as a file of its own |
| `52b122b` | decisions (WAY-139, WAY-344, WAY-60, WAY-61, WAY-229, rationale of WAY-160) and the templates (decisions, invariants, task, three guidelines templates) |
| `76c2bd2` | To do 8, 19: `foundation_check.py`, its tests, `agent-instructions/README.md` |
| `e9aea95` | skills: `resolve_gaps.md`, `task-cycle/plan/SKILL.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md` |

Files changed against the base, 17 files, +320 −148 (added −removed lines, `git diff --numstat b6b3416..HEAD`): `agent-instructions/README.md` +2 −2; `elements/common/foundation_check.py` +38 −57 (the move takes 42 lines out; before it the file stood at 1003 lines, now 983); new `elements/common/foundation_source.py` +57; `elements/common/test_foundation_check.py` +46 −5; `elements/decisions/skill/SKILL.md` +2 −1; `elements/decisions/template.md` +4 −1; `elements/invariants/template.md` +6 −4; `foundations/decisions.md` +81 −30; `gate/test_run_tests.py` +34 −19; `product-guidelines/coding/template.md`, `styleguide/template.md`, `testing/template.md` +3 −2 each; `project-level/task/skill/resolve_gaps.md` +3 −1; `project-level/task/template.md` +3 −1; `task-cycle/plan/SKILL.md` +8 −2; `task-cycle/skill/SKILL.md` +9 −5; `task-cycle/skill/foundation_step.md` +18 −14.

## The move before the code that adds (WAY-365)

`elements/common/foundation_check.py` stood at 1003 lines, over the 1000 of WAY-385, and To do 8 and 19 add to it. First commit that changes code, `ac3c96f`: the four functions that read the repository (`git`, `fork_point`, `at_commit`, `read`) and `MAIN_BRANCHES` move as they stand into `elements/common/foundation_source.py`; `foundation_check.py` imports them by name, so `decision_index.py` (`binding`, `blocks`, `fields`, `located`) and `elements/part-map/test_cross_part_imports.py` (`git`, `read`, constants) still import the same names from `foundation_check`. File now 960 lines before my additions, 983 after. Rejected: moving the text readers (`blocks`, `fields`, `located`, `binding`, … with the regular expressions they need, about 195 lines) into a module — a larger move that drags eleven constants across and changes more of what `decision_index.py` depends on; cost if wrong: none for behaviour, only a later further move. No function stands over 80 lines in my additions (`list_invariants` 49 lines, `check_decision_line` 42). `agent-instructions/test_size_invariant.py` keeps its two expected failures (the invariant is marked violated; unchanged).

## Choices (each with the way rejected and its cost if wrong)

1. **Fix of the trial module (To do 1).** Technique: each event is an **empty file in a directory**, its name `<time in nanoseconds, 19 digits>-<text>`; the reader lists the directory and sorts the names. Helpers `log_event` and `logged_events` stand once in `gate/test_run_tests.py`; `timed_module` embeds their source with `inspect.getsource`, so the test process and the module in each directory run the same code. Rejected: one file per process (the order across processes is lost, and the ordered tests read it); an explicit lock file with `os.open(O_CREAT|O_EXCL)` and retries (a spin on Windows, where deleting a file another process is opening raises `PermissionError`). Cost if wrong: if a clock gave two events the same nanosecond, the order falls to the text; the clock of this machine resolves 100 ns (measured, 2000 samples) and the ordered tests lie 0.3 s apart or are ordered by a wait.
   - How the order tests still see the lines: `self.logged()` is `logged_events(self.log())`; `runner_noting` records its note with the same `log_event`; the tests `--jobs 1` (exact order `start a, end a, …`), the jobs limit (`sorted(first two) == start a, start b`) and the interrupt test (`["start a", "end a"]`) were not changed in their assertions and pass.
   - The log path is now the directory `timeline` (was the file `timeline.log`).
2. **Item 8, when the line is written.** One `listed:` line for an invariant that reads `test` now, has both fields now, whose sentence differs from the base, and whose base copy lacks *Method* or *Part*; it names both fields in one line where both are lacking; it is written whether or not a citing file changed (the comparison could not be made). An invariant lacking a field *now* stays unlisted (the report of fields names it as an error). A base-lacking invariant with an unchanged sentence is not listed. Rejected: listing only where no citing file changed — the base gap hides exactly the case the listing exists for; listing every invariant whose base lacks a field — noise with no reworded sentence.
3. **Item 19.** A sentence start after `". "` counts only where the full stop lies outside a passage matched by the check's existing `QUOTED` pattern (straight `"…"` or curly `“…”`). Rejected: a new pattern for quotation marks — the check already has one; cost if wrong: an unbalanced quotation mark in a binding sentence makes the sentence start after it unrecognised, then the decision line fails visibly and the author rewords it.
4. **Wording of each clause** is mine as the task leaves it; each clause stands where the item names it. Where an item quotes the text, I used the quoted text; where I added to it, see "Adaptations".
5. **Item 5 / WAY-139 (what the pointer covers).** Both say: each *To do* item that writes into the skill the answer to one of the three items — from a decision or definition, from the run of `settle-technology`, or the record of the human's refusal — points to the guide. I included the item recording the human's refusal, since the guide has a part for each of the three. Rejected: only the item from a decision. Cost if wrong: one more pointer on an item that records a refusal.
6. **Item 20, the setting.** The binding sentence of WAY-229 now names the setting `availableModels`. The rationale said "the log names no model and no setting"; I changed that sentence (it now says the log names no model and gives the reason for the list: a request for a model outside it gets the session's own model) and extended the *Rejected* item "the strongest class of the family" and WAY-229's *Verification* (both examples). The other places that say "the strongest available" (the slice classes in the plan skill, steps 4 and 10 of the cycle skill) name the class, not the source of the model, and are left; the two steps the item names carry the setting. WAY-33 search for the old sentence "lets its agents use" found nothing outside WAY-229.

## Adaptations of the task's text and what I added beyond it

- Q1 of the handoff applied: WAY-328 is withdrawn; I read `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md` whole and did not edit WAY-328.
- *To do* 17: I kept the quoted dopisek and added "and a link written into its *Relations* does not", because the item's next sentence says a link of *Relations* does not change the entry to `the cycle's`; and I rewrote the tail "which the request puts before the human" as "the request puts each entry so marked before the human (WAY-114)" so that the sentence reads after the insert.
- *To do* 11: the dopisek stands after "(WAY-134)" as the item says.
- *To do* 7: the three sentences gain the same clause: the stop is for a choice or meaning that "carries a real cost"; "a rule that only says how to write code / the look of the product / tests is the cycle's own, which the human accepts at the merge (WAY-172)". The second half is mine, from WAY-172 ("where the cycle found the rule itself, at the merge").
- `elements/invariants/template.md` table row for *sentence* and `agent-instructions/README.md` ("The form of the foundation") also describe the listing; I added the base-copy case to both (WAY-33 search finding). The README is the file the cycle's return step compares with item 8, as the task's *Context* says.
- *To do* 14: the *Checks* bullet in the plan skill; the sentence of WAY-160's rationale changed with it, as the item says.

## Entries written (foundation step)

Mark / one sentence in English / one sentence in Polish.

| Entry | Mark | English | Polish |
|---|---|---|---|
| WAY-139 (sentence, *Verification*, *Rationale*, *Rejected*) | row 1 | Each item of the To do that writes into the skill the answer to how to read the logs, how long the record lives or how a human learns of a failure, or the record of the human's refusal, points to the guide too. | Każdy punkt *To do*, który wpisuje do skilla odpowiedź o czytaniu logów, o czasie życia zapisu albo o awarii (albo zapis odmowy człowieka), też wskazuje przewodnik. |
| WAY-344 (sentence, *Verification*, *Rationale*, *Rejected*) | row 3 | A field missing from the copy of a file at the commit the branch left is listed by a `listed:` line naming the entry and the field, with no error and no change of the exit code. | Brak pola w kopii pliku z commita bazowego jest wypisany linią `listed:` z nazwą wpisu i pola, bez błędu i bez zmiany kodu wyjścia. |
| WAY-60 (sentence, *Verification*, *Rationale*, *Rejected*) | row 5 | A decision identifier written into an invariant's sentence because the decision holds the condition is part of the condition, not a link WAY-17 requires; the link stands beside the sentence in its own field. | Identyfikator decyzji wpisany w zdanie niezmiennika, bo ta decyzja trzyma jego warunek, jest częścią warunku, a nie powiązaniem z WAY-17; powiązanie stoi obok zdania w swoim polu. |
| WAY-61 (*Scope*) | the cycle's (To do 15; no row) | The *Scope* of WAY-61 names `task-cycle` as well. | *Scope* WAY-61 wymienia też `task-cycle`. |
| WAY-229 (sentence, *Verification*, *Rationale*, *Rejected*) | the cycle's (To do 20; no row) | The strongest class available is the strongest of the models the session's settings allow, taken from `availableModels`, never from the name of the strongest model of the family. | Najmocniejsza dostępna klasa to najmocniejszy z modeli dozwolonych w ustawieniach sesji, z listy `availableModels`, a nie nazwa najmocniejszego modelu rodziny. |
| WAY-160 (*Rationale* only) | the cycle's (To do 14; no row) | The focused checks of a slice are those of the code it reaches and of the invariants its change may make false. | Skoncentrowane sprawdzenia kawałka to testy kodu, do którego sięga, i niezmienników, które jego zmiana może zepsuć. |

Rows 2, 4, 6, 7, 8, 9 go to no element and write no entry: rows 2 (three guidelines templates), 4 (`elements/decisions/template.md`, `task-cycle/skill/foundation_step.md`), 6 and 8 (`task-cycle/plan/SKILL.md`), 7 (`project-level/task/template.md`), 9 (`task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md`) are written in their places by those files' own rules. WAY-173 and WAY-172, WAY-134, WAY-17, WAY-62, WAY-142, WAY-321 and WAY-328 are unchanged. No invariant, glossary term, environment fact or part-map entry is written or changed (the new file `foundation_source.py` falls to the part `elements-common` by its pattern `elements/common/**`).

## Checks run (all from the worktree root `the task's worktree`)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py elements/common` (after the move) | 0 | 242 tests OK |
| `python -B gate/run_tests.py elements/part-map` before `git add` of the new file | 1 | 1 failure: `test_the_way_imports_only_from_allowed_parts` named `foundation_source` as no file it sees (it reads `git ls-files`) |
| the same after `git add elements/common/foundation_source.py` | 0 | 40 tests OK |
| the loss reproduction (a throw-away script in my directory, removed): 3 processes recording one event at the same moment, 20 trials, the old technique (`open(..., 'a')`) | 0 | lost an event in 19 of 20 trials |
| the same with the new technique | 0 | 0 of 20 |
| `python -B gate/run_tests.py gate`, six runs in a row after the fix | 0 ×6 | 36 tests OK each |
| `test_by_default_every_directory_runs_at_the_same_time` with `max_workers` of the runner forced to 1 (temporary edit of `gate/run_tests.py`, restored with `git checkout`): `python -B -m unittest test_run_tests.DirectoriesAtOnce.test_by_default_every_directory_runs_at_the_same_time` from `gate/` | 1 | fails in 240.6 s: directories `a` and `b` "did not meet the others" after 120 s each |
| `python -B -m unittest discover -s elements/common -p test_foundation_check.py -k lacking` before the code (three new tests of item 8) | 1 (FAILED failures=3; I read the output, not the exit code) | each failed on `0 != 1` listed lines |
| `… -k full_stop` before the code (the test of item 19) | 1 (FAILED, same remark) | `0 != 1`: the check passed a quotation that begins inside a quoted string |
| the same two after the code, with `-k decision_line` | 0 | 24 tests OK |
| `python -B gate/run_tests.py elements/common` (final) | 0 | 245 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 37 tests OK (expected failures=2, the same as on the base) |
| `python -B gate/run_tests.py task-cycle` | 0 | 534 tests OK (skipped=1) |
| `python -B gate/run_tests.py project-level` | 0 | 279 tests OK |
| `python -B gate/run_tests.py product-guidelines` | 0 | 14 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 36 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 105 tests OK (skipped=5) |
| `python -B gate/run_tests.py installation` | 0 | 62 tests OK |
| `python -B elements/common/foundation_check.py` (no switch, final tree) | 0 | `0 errors` |

Not run: the full gate (`python -B gate/run_tests.py` without a directory) — the orchestrator's (WAY-160); `relation-model` and `process-audit` directories — no file of theirs changed and none imports what I moved. The plan has none, so no *Checks* mismatch.

## Own-work check (section 3)

- Requirement most likely not met: *To do* 1 and 2 together — "no run loses a line, and the test still fails when directories run one after another". Check: the reproduction above (19/20 lost before, 0/20 after, the same trial script with only the technique changed), six gate runs in a row, and the forced serial run, which fails after 120 s. Showed: the loss is real on this machine, the fix removes it, the guard test is still a guard. A random failure of once in four runs cannot be proved gone by six runs; the reproduction is the evidence.
- Second: item 8's "one line, not a change of the exit code" — `listed_lines` in the test asserts exit code 0 and the last line `0 errors` besides the one `listed:` line.
- Mutation in the head: base copy lacking *Method* but sentence unchanged → test `test_invariant_lacking_a_field_at_base_whose_sentence_is_unchanged_is_not_listed`; both fields lacking → one line naming both; a full stop after a closing quote (`"…". `) — not inside, the sentence start counts (not tested separately; the pattern's span ends at the closing mark, and the stop lies after it); a quote whose first word follows `". "` inside the string — the new test, in the straight and curly forms.

## Reaches beyond the handoff

- `agent-instructions/README.md` (read the section "The form of the foundation" and changed one sentence) — the item 8 listing is described there; the task's *Context* names it.
- `elements/invariants/template.md` table row *sentence* — the same listing; WAY-33 search.
- `agent-instructions/test_size_invariant.py` (first 80 lines) — to learn what the size invariant counts; and the part map line `elements/common/**` — to be sure the new file has an owner.
- `foundations/invariants.md`: `gate-exit-code`, `map-reference-target`, `test-method-citation`, `function-and-file-size` (the first ten lines of each) — the invariants the changed tests cite or the move touches.
- `elements/common/decision_index.py` first 60 lines and the test imports of `elements/part-map/test_cross_part_imports.py` and `elements/common/test_guidelines_place.py` — to see what is imported from `foundation_check`.
- `project-level/task/deployment_skill_guide.md` lines 1–45 — what the guide says of who reads it.
- `guidelines/coding-shared-module.md` — the kind of the new module (it applies to `relation-model` only; I followed its rule "importing runs nothing" by hand, the module defines only functions and one constant).

## Unread material

- `elements/common/rules.md`, `elements/decisions/skill/read.md` and `decide_entry.md`, `elements/common/glossary` and `foundations/glossary.md`, and `foundations/part_map.md` — named in the handoff list; I read none of them whole (I searched the part map and the glossary for `foundation_check` and `fork_point`: no hit) and used the decisions template (read the sections I changed, not the whole file), `elements/invariants/template.md` (the sentence section and the table of readers), and `elements/common/way_of_working.md` (whole).
- The decision index was read whole; of the entries WAY-134, WAY-172, WAY-173, WAY-17, WAY-321, WAY-62, WAY-142, WAY-114 I read the index lines and, for WAY-134, WAY-172, WAY-114, WAY-321 and WAY-62, the binding sentences (WAY-321 whole); I did not open WAY-173, WAY-142, WAY-62's rationale, WAY-17's rationale or WAY-114's rejected options whole.
- Of the invariants with *Part* `every` (17) I read only the three the changed tests cite and `function-and-file-size`; not each of the 17.
- `guidelines/coding-check.md` and `guidelines/coding.md` — read whole; `guidelines/testing.md` — read whole.
- The files I changed: each read whole before changing, save `foundations/decisions.md` (the entries I changed were read whole: WAY-139, WAY-344, WAY-60, WAY-61, WAY-229 and the rationale part of WAY-160) and `elements/common/test_foundation_check.py` (read lines 1–300 and 1060–1624).

## Searches not found or unclear

- The handoff names `task-cycle/skill/foundation_step.md` as giving where an entry's mark `row <n>` / `the cycle's` is written for an entry changed by a *To do* item that is not a row (items 14, 15, 20): the file marks only `row <n>`, `projected`, `the cycle's`. I marked WAY-61 *Scope*, WAY-229 and the rationale of WAY-160 `the cycle's`; the orchestrator may prefer another mark for entries the accepted task carries as *To do* items.
- Item 7 names "the sentence of three templates" but not what the cycle does with a rule that only says how to write; I took WAY-172 for it (see Adaptations).
- No test holds WAY-139, WAY-60, WAY-61 or WAY-229 by a line `decision:`; their *Verification* is an agent's comparison with a pair of examples, which I changed, not a test.

## Problems and concerns (observed)

- A concern the orchestrator should see in the review: `foundations/decisions.md` carries changes of six entries in one commit (`52b122b`) because the file cannot be split by hunk without an interactive tool; the commit message names the entries.
- `test_cross_part_imports` reads `git ls-files`, so a new file of the-way must be added to the index before that test sees it; observed once (table above), fixed by the commit.
- The question of the later cycle (the author's task note on the scripts after the foundation review) will meet my edit of the same sentence of WAY-344 and of `foundation_check.py`; no dependency, as the handoff says; the new sentence of WAY-344 stands between the sentence on a file of a tool the cycle changed and the sentence on the test per reading.
- The wording `a request for a model outside that list gets the session's own model` in WAY-229's rationale rests on the task's own description of the incident (To do 20), not on a source I checked; if the orchestrator wants it out, it is one sentence of the rationale.

## Questions

None.

## Working copies

My directory `.runs/author/` held throw-away scripts and outputs (the loss reproduction, the edit scripts, the focused-run outputs); I removed all of it (`find .runs/author -mindepth 1 -delete`; the directory itself stands, empty). One temporary edit of `gate/run_tests.py` for the serial run was restored with `git checkout -- gate/run_tests.py` before the commit; nothing of it is in any commit. No worktree, clone or screenshot was made. Remainder: none.
