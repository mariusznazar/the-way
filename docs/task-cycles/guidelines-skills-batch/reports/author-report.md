# Report of the one author — guidelines-skills-batch

**Status:** `done with concerns` (the concerns are the open details under "Searches not found or unclear"; none blocks the change).

**Branch / commits** (base `05534d381b95a4e2692875263dd0d8875097b89d`):

- `e6d0f9e` Settle the open remarks on the skills of coding, testing and styleguide guidelines — items 1-20 (skill, template and shared files).
- `e66e8e7` Record the foundation entries of the guidelines skills batch — the 5 settlements and the glossary template line.

## Files changed (added / removed lines, `git diff --numstat 05534d3 HEAD`)

- `foundations/decisions.md` 130/25; `elements/glossary/template.md` 3/1
- `instruction-files/judging.md` 5/0
- `product-guidelines/audit_end.md` 17/5; `reading.md` 4/0
- `product-guidelines/styleguide/SKILL.md` 12/6; `audit.md` 5/3
- `product-guidelines/coding/SKILL.md` 26/17; `hand_back.md` 14/8; `recognize.md` 10/6; `settle.md` 12/3; `task_document.md` 10/8; `template.md` 11/9
- `product-guidelines/testing/SKILL.md` 15/10; `audit.md` 0/4; `hand_back.md` 9/4; `new_level.md` 6/4; `recognize.md` 4/2; `settle.md` 4/3; `template.md` 5/4
- `project-level/task/skill/guideline_findings.md` 15/9

## Checks run (command, exit code)

- `python -B elements/common/foundation_check.py` — "0 errors", exit 0 (run after the decision edits and again after the glossary template line).
- `python -B instruction-files/check_instructions.py .` — exit 0; 0 errors, 1 warn (`AGENTS.md:21 _zadania\ does not exist`, in the unchanged root `AGENTS.md`, not from this change), 3 info.
- `python -B gate/run_tests.py instruction-files` — exit 0 (104 tests, 5 skipped).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (18 tests).
- `python -B gate/run_tests.py elements/common` — exit 0 (109 tests).
- `python -B gate/run_tests.py project-level` — exit 0 (271 tests).
- Not run: the full gate (the handoff reserves it); `gate/run_tests.py` for `task-cycle`, `installation`, `elements/part-map`, `relation-model`, `gate` (no file of those directories changed). `python -B agent-instructions/skill_entry_points.py --write` not run: no skill was added, renamed or moved and no description changed.
- No test written first: the change is prose and foundation entries; the repository has no test for the text of these skills, and the task asks for none. No invariant added or changed.

## Items, weakest-point check

For each item: requirement, the check I made that the changed text says it, what it showed. The check for all of them was reading the changed passage against the item and the decision it names after the edit, and `git diff` of the file.

1. Styleguide `SKILL.md`, "A meaning reaches the code..." — requirement: say the second way of WAY-172 (approval at a blocked draft request when the document does not settle it). Text now names two ways. Showed: the table row above it ("Never writes ... a meaning the task did not settle") still says the cycle's author never writes such a meaning; I read "writes" as distinct from "proposes on the branch", left the row, and note it here. The same "only through the task document" sentence stands unchanged in `coding/SKILL.md` and `testing/SKILL.md` (not in the task).
2. `styleguide/audit.md` — the audit checks per screen (no data, from a link, after refresh) itself and asks the human about none; with the running product it opens each screen those three ways, without it it marks the three as unchecked where the code does not say. Showed: fine; "unchecked" was already the audit's own mark.
3. Direct pointers — styleguide `SKILL.md` step 2 names `research.md`, step 4 names `new_tools.md` and `staged_cleaning.md`, each with its condition; coding `SKILL.md` steps 2 and 4 now say "read `research.md` / `new_tools.md` beside this skill too" instead of "`starting_set.md` / `settle.md` sends you to". I kept the pointers inside `starting_rules.md`, `settle.md`, `starting_set.md`: WAY-265 requires the variant file to be named in both places. Showed: consistent with WAY-265. `testing/SKILL.md` has the same "sends you to" wording (lines for steps 2 and 4); the task names only styleguide and coding, so I left it.
4. Version of each standing check's tool — `coding/settle.md` new bullet ("What it settles"), `coding/task_document.md` "each tool and its version, set and edition". Showed: the bullet is placed under the standing-check decision bullet; the linter bullet still holds tool/set/edition/parts/split.
5. Split of the trial run for a chosen tool or set — `coding/settle.md` linter bullet ("where the human chooses a tool or a set other than the one the trial run tried, run the trial again... before the split is proposed") and `coding/SKILL.md` step 4 ("read `trial_run.md` ... again"). Showed: see "Searches ... unclear" 2 on the audit's causes.
6. "A new kind" — `coding/SKILL.md` step 3 bullet "A new kind", step 4 closing sentence, `recognize.md` mode bullet, `settle.md` and `hand_back.md` and `task_document.md` openings; decision WAY-216 (row 5). Showed: the rule reads the same in all of them: only the standing checks the kind touches; a kind in a language none of the product's checks reads makes the task an extension (steps 2 and 3 run as for one). See unclear 1 for "touches".
7. Headings of the rules on failures and logs — `coding/recognize.md` lists the six headings and says they stand in `coding/template.md`; `coding/SKILL.md` step 1 says to read that template in full at a refresh; steps 2 and 3 now say "unless step 1 did" / "unless an earlier step did". Checked the order of the template reads across steps 1-4: no step reads it twice.
8. `none —` among the rules on failures and logs at the first guidelines and an extension — `coding/settle.md` (after "WAY-271, WAY-278, WAY-279") and `coding/hand_back.md` ("A task that found those rules in place, a heading holding `none —` among them, checks nothing of them"). Showed: `hand_back.md` formerly limited this to a refresh; now it holds for any task.
9. `coding/template.md`: (a) the reason is removed from `### Identifiers in log lines` ("need carry none (WAY-275)"); (b) `### Logging scope` now says "only with the human's consent; adding an item changes no decision (WAY-274)"; (c) departure way 2 now calls `Personal data` a field of the rule `### Secrets and personal data` that the template adds (WAY-171), with the name staying in English (WAY-310); (d) the table row for the whole `### Secrets and personal data` now also lists the end of the narrowing of `### Identifiers in log lines`; (e) the last row is split: `### Recording a failure` keeps "nothing else" plus "each rule that stays keeps the meaning of every word it takes from this one, in its own text, as `### Hiding a failure` keeps what a failure is and that an expected refusal is no failure"; `### Hiding a failure` is its own row. Showed: for (e), see unclear 4.
10. `testing/new_level.md` rewritten: the route applies to a level whose recipe stands with an empty *Exemplar*, adds the exemplar to it, writes no recipe, a level with no recipe is an extension (WAY-251); `testing/SKILL.md` step 3 states the same condition.
11. `testing/SKILL.md` step 2 names "a product with no tests".
12. The "A choice found in the product's tests..." sentence moved from `testing/audit.md` to the rules that hold across the steps in `testing/SKILL.md` (so it reaches every path, new level included). Moved, not copied.
13. `testing/recognize.md` — "no step 2 for that level; where the same task also extends the testing guidelines, the extension goes through step 2 as well".
14. WAY-240 now carries the precedence over WAY-95 (binding sentence, `narrows WAY-95`, verification example, rationale with the weak point, the two ways not chosen of the answer); `testing/settle.md` and `testing/template.md` say "a narrower meaning included" and "whether or not a sentence would be read wrongly".
15. `reading.md` (new bullet after the empty-*Exemplar* bullet) and `guideline_findings.md` (new paragraph): a required outcome that is the first test of a level the testing guidelines do not name is an extension through `maintain-testing-guidelines`, and the task goes to the cycle only with it in *To do*.
16. `guideline_findings.md`: both places now say "by the rules of `read_sources.md` for the backlog and its task documents". Checked `read_sources.md`: it holds the backlog and task-document rules.
17. `audit_end.md` "Whether this audit stops" now takes from the other skill's step 1 "its mode alone", naming the withheld item; `coding/SKILL.md` and `testing/SKILL.md` step 3 say "for the mode it gives alone".
18. `audit_end.md` (new bullet "An audit that stopped, with no audit to follow"), `coding/hand_back.md`, `testing/hand_back.md` (return bullet); decision WAY-282 (third binding sentence, example, rationale, rejected way). The return numbers the causes, makes the top, goes back to each cause of it, puts the top to the human, then hands back to step 4.
19. `audit_end.md` (new bullet "Who hands back to step 4", and "the route of one kind and a new level ... this audit does not stop and closes the list here"), both `hand_back.md`: a skill hands back to step 3 while the other discipline's skill has not led its matters, also where that discipline has no audit; only the skill that leads last hands back to step 4. Showed: closing the list (audit that runs last) and handing back (skill that leads last) are now two separate rules; I read the four lines of the three files together for a contradiction and found none.
20. `instruction-files/judging.md` — one paragraph under item 2 of the output (a row for each part, each with one of the four verdicts, none of its own such as a split; a proposal to add or change a rule in a row of its own). The section order of the file is untouched. Decision WAY-311.

## Foundation entries (the 5 rows of *Settlements to record*)

Written through the element template (`elements/decisions/template.md`) and the shared steps; `foundation_check.py` passes.

| Row | Entry | Meaning in English | Znaczenie po polsku | Mark |
|---|---|---|---|---|
| 1 | WAY-240, edited in place (new third binding sentence; `narrows WAY-95`) | For the names of test levels WAY-240 prevails over WAY-95: a level named otherwise than in the field, a narrower meaning included, always takes a glossary entry. | Przy nazwach poziomów testów WAY-240 ma pierwszeństwo przed WAY-95: poziom nazwany inaczej niż w branży, także węziej, zawsze dostaje hasło słownika. | `row 1` |
| 2 | WAY-310, new (`derives from WAY-171, WAY-276`) | The line `Personal data: none — <PREFIX-NN>` is a field of the rule `### Secrets and personal data` that the coding template adds, and its name stays in English. | Linia `Personal data: none — <PREFIX-NN>` jest polem reguły `### Secrets and personal data`, które dodaje szablon kodu; nazwa pola zostaje po angielsku. | `row 2` |
| 3 | WAY-311, new (`derives from WAY-257`) | The judging table gives a fragment going to several places a row for each part with one of four verdicts, and each proposal to add or change a rule a row of its own. | Tabela oceny daje fragmentowi idącemu w kilka miejsc wiersz na każdą część z jednym z czterech werdyktów, a każdej propozycji dodania lub zmiany reguły własny wiersz. | `row 3` |
| 4 | WAY-282, edited in place (third binding sentence) | When the human separates the work after one audit stopped, so that the other will not run, the skill of the stopped audit closes the list as the audit that runs last does. | Gdy człowiek rozdzieli pracę po zatrzymaniu jednego audytu, tak że drugi nie ruszy, skill zatrzymanego audytu domyka listę jak audyt biegnący ostatni. | `row 4` |
| 5 | WAY-216, edited in place (first and third binding sentence; `narrows WAY-202` added) | A new kind in a product with coding guidelines settles and checks only the standing checks it touches; a kind in a language no standing check reads makes the task an extension. | Nowy rodzaj kodu w produkcie z wytycznymi rozstrzyga i sprawdza tylko stałe sprawdzenia, których dotyka; rodzaj w języku, którego żadne nie czyta, robi z zadania rozszerzenie. | `row 5` |

No entry is marked `projected` or `the cycle's`. No collision needed WAY-25 by the human's accepted passages beyond rows 1 and 5: row 1's `narrows WAY-95` rests on the answer to question 1 ("WAY-240 wygrywa przy nazwach poziomów testów, a WAY-240 dostaje zdanie o pierwszeństwie przed WAY-95"); row 5's `narrows WAY-202` rests on the row's anchor and answer ("tak — na wariant c ... zmieniający obie strony", with the anchor WAY-202). The *Rejected* of rows 1-5 hold the "Not chosen" ways of the task's answers and the row's *Source*, no way I derived.

Beyond the five rows (WAY-33 search, same change): `elements/glossary/template.md` restated WAY-95's rule for narrower meanings, so I added a sentence naming the exception for test level names (WAY-240).

Not done on purpose: WAY-95's own text and *Verification* were not edited; WAY-25 puts the record in the decision that prevails, and the narrower-meaning example in WAY-95's *violates* list now reads against WAY-240 only inside the area WAY-240 states. The orchestrator can judge whether WAY-95 should name WAY-240 too.

## Reaches beyond the dispatch

- `elements/decisions/skill/SKILL.md`, `decide_entry.md`, `read.md`, `elements/decisions/template.md`, `elements/common/way_of_working.md`, `task-cycle/skill/foundation_step.md`: to write the entries (the handoff names the skill for decisions; the template and the shared steps are what the skill points to).
- WAY-265 (where a variant file is named) — items 3, 7, 5 depend on it; the coding/testing `SKILL.md` text already cites it.
- Read whole beyond the handoff's list: WAY-265 (above), WAY-201, WAY-202, WAY-204, WAY-215, WAY-217 (all of them are in the task's *Decisions in play* or the handoff list except 265).
- Not read whole although the handoff listed them: WAY-168, WAY-272, WAY-273, WAY-275 (and WAY-204, WAY-201 were read). I worked from the quotations in the task and from the sentences of the templates that cite them; items 9(a), 9(d), 9(e) depend on WAY-272/275/276 and I read WAY-276 whole and WAY-274 whole, the sentences of 272 and 275 only as the coding template restates them.
- `elements/glossary/template.md` lines 44-55 (found by the search for "narrowly").
- `project-level/task/skill/read_sources.md` (item 16), `project-level/task/skill/SKILL.md` references to `guideline_findings.md`.

## Searches not found or unclear

1. Item 6: "the standing checks a new kind touches" has no definition in the task or in WAY-216. I wrote "those whose tool reads the language of the kind's files", the same criterion the row gives for the extension. This leaves unsaid how the audit of dependencies (which reads manifests, not a language) counts. A reviewer may want a sharper line.
2. Item 5: a second trial run for the chosen set produces new reports, and the audit's list of causes is built from the reports of the first run (`trial_run.md`, last bullet). The task and WAY-204 say nothing of redoing that list. I wrote nothing about it; step 3 has already ordered and "gone back" to the causes, so redoing them is a larger rule that needs a decision.
3. Item 18: the task does not say who starts the return of the stopped skill or where it resumes. I wrote "this skill returns" at the moment the human separates the work; the trigger (the human, or `refine-task`) is not named in any source I read.
4. Item 9(e): the task says the remaining rules keep the meaning of "failure" and "expected refusal" but not where the meaning stands once the departed rule's heading holds only `none — <PREFIX-NN>`. I wrote "in its own text" (the kept rule's), the least rule that follows from way 3 of the departures. If the intended place is the product's decision instead, the table row changes.
5. Item 20: the four verdicts have none for a proposal to add a rule. I wrote only "a row of its own" and left the verdict column of such a row unspecified.
6. Item 17: step 1 of the other skill reads files of the product (`AGENTS.md`, `guidelines/`); "its mode alone" drops the refresh check and its question, but the reads that give the mode remain. The task asks only for the question to leave the audit, so I left the reads.
7. Line numbers in the task all moved; I found each place by its content, none was missing.
8. The handoff names `instruction-files/check_instructions.py` as the check for skill files; it checks the repository's instruction files and listed only `AGENTS.md`, `CLAUDE.md` and `agent-instructions/README.md`; it does not read `product-guidelines/**`. So the skill files I changed were checked by reading only.

## Choices (way rejected, cost if wrong)

- Item 12: moved the sentence from `testing/audit.md` into `SKILL.md` rules; rejected: keep in `audit.md` and add copies in the other paths. Cost if wrong: a reviewer wants it in the audit file too (one line).
- Item 3: kept the pointers also in the step files (WAY-265 asks for both); rejected: remove them from the step files. Cost if wrong: one repeated line to delete.
- Item 14: edited WAY-240's binding sentences by adding a precedence sentence; rejected: leave the text and rely on `narrows`. WAY-25 requires the area stated in the binding sentences.
- Row 5 recorded as an edit of WAY-216, not a new entry: the question "What does refinement assign to a task creating an unindexed kind of code?" is the one WAY-216 answers.
- Rows 2 and 3 are new entries (WAY-310, WAY-311): the questions (the form of the departure line; the rows of the judging table) are not answered by WAY-171/276 or WAY-257. Numbers 310 and 311 were the next free ones in this checkout; if another branch took them, the orchestrator renumbers (nothing outside the log refers to them but `coding/template.md`).

## Problems as observed

None beyond the open details above. The warn of `check_instructions.py` (`_zadania\` in `AGENTS.md:21`) belongs to the Backlog paragraph of the root `AGENTS.md`, unchanged, and refers to a folder of the author's private notes.
