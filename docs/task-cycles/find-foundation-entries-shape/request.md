**State: ready** — nothing blocks the merge; four proposals that were not applied and one corrected figure wait for your yes below.

## What you will see

`find-foundation-entries` is the skill that searches a project definition or a task for what should become entries of a product's foundation. It was one file of 1584 words that every agent read whole, whichever of its two uses it was on. After this change its main file has 598 words: the picture of the whole, a table that says who calls the skill and how a caller's agent recognises its own use, the rule for resuming a half-made table, the third step and the pointers. The procedures stand in four files beside it: one for reading (step 1), one for building the table (step 2), and one for each use, a project definition and a task. The agent reads the file of its use once, at step 1, and carries out its lines at steps 1, 2, 4 and 5.

What an agent reads of the skill now, in words (counted as `wc -w` counts them, on the files before and after):

| Use and what is counted | Before | After | Change |
|---|---:|---:|---:|
| Task, the skill's own text | 1584 | 1397 | −12% |
| Task, with the files it reads beside the skill | 3741 | 3554 | −5% |
| Task, the same without what the task-refining skill already read | 2625 | 2438 | −7% |
| Project definition, the skill's own text | 1584 | 1546 | −2% |
| Project definition, with the files it reads beside the skill | 4429 | 4391 | −1% |

The five files together have 2021 words, 437 more than the old single file. These are word counts of files, not a measurement of how agents behave or of tokens. No rule disappeared and none changed meaning, with one exception the task itself settles: an agent working on a task no longer reads the section of the definition template on projected changes, which the old wording could be read to require beside the task's own section. The merge does not change the foundation, the callers of the skill, the skill's description or any code.

### Underneath

The change applies the rule that a procedure which only one step or one use needs stands in a file beside the skill that the step names; the skill's description, its Python and the entry points of the skills did not change.

## For you to decide

1. Four proposals that change what a rule says and were therefore not applied; each is described under "Assessment of the skill" below. Decide each separately. (a) Read in task mode only three sections of the shared file on the way of working (800 words) instead of the whole file (1752): the task route would be 952 words shorter, at the price of a second exception to the series' rule that a step's procedure is read whole and the risk that a rule outside the three sections binds a task. Apply it? (b) In the shared step-2 file, change "or a section of the definition" to "or a section of the source document": it saves no words, and the shared file then stops being literally the old text. Apply it? (c) Remove the sentence about future callers of the skill: it has 48 words and is read in every use, but the skill then no longer says that its list of callers is open. Remove it? (d) Move the reading of the projected-mode file from step 1 to step 4 in the definition use: not recommended, because the questions of step 4 depend on that file. Apply it? (The task's own sections, "Assessment of the skill".)
2. The task states 424 words for the task template's section "Settlements to record" with its rule. The section's own lines and the rule's bullet give 405; 424 is a different range of lines that leaves the section's own lines out. This request states 405. The figure appears on both sides of every before/after comparison that uses it, so no percentage in this request moves. Accept 405? (Checks; the reviewer recounted it.)

## Cost

About 38 minutes of working time in the turns of the orchestrator and of five agent turns, and 23,159,706 tokens in all (18,528,584 on Sonnet, 4,631,122 on Opus), as counted before this description was written. Two code reviews ran: the review of the whole change, which passed with three small remarks, and the review of the one fix for them, which passed. [Table of stages](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/find-foundation-entries-shape/stages.md).

## How to merge

Merge keeping the commits, with no squash and no rebase: the links in this request lead to the commit that holds the record of the cycle, and they survive only then. Nothing in this request waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — nic nie blokuje scalenia; poniżej czekają na Twoją zgodę cztery propozycje, których nie zastosowano, i jedna poprawiona liczba.

### Co zobaczysz

`find-foundation-entries` to skill, który przeszukuje definicję projektu albo zadanie pod kątem tego, co powinno stać się wpisami fundamentu produktu. Był jednym plikiem o 1584 słowach, który każdy agent czytał w całości, niezależnie od tego, do którego z dwóch zastosowań go użył. Po tej zmianie jego plik główny ma 598 słów: obraz całości, tabelę mówiącą, kto woła skill i po czym agent wołającego rozpozna swoje zastosowanie, regułę wznawiania rozgrzebanej tabeli, trzeci krok i odsyłacze. Procedury stoją w czterech plikach obok: jeden na czytanie (krok 1), jeden na budowanie tabeli (krok 2) i po jednym na każde zastosowanie — definicję projektu i zadanie. Agent czyta plik swojego zastosowania raz, na kroku 1, i wykonuje jego wiersze na krokach 1, 2, 4 i 5.

Co agent czyta ze skilla teraz, w słowach (liczonych jak `wc -w`, na plikach przed zmianą i po niej):

| Zastosowanie i co liczone | Przed | Po | Zmiana |
|---|---:|---:|---:|
| Zadanie, sam tekst skilla | 1584 | 1397 | −12% |
| Zadanie, z plikami czytanymi obok skilla | 3741 | 3554 | −5% |
| Zadanie, to samo bez tego, co skill doprecyzowania zadania już przeczytał | 2625 | 2438 | −7% |
| Definicja projektu, sam tekst skilla | 1584 | 1546 | −2% |
| Definicja projektu, z plikami czytanymi obok skilla | 4429 | 4391 | −1% |

Pięć plików razem ma 2021 słów, o 437 więcej niż dawny pojedynczy plik. To liczby słów w plikach, nie pomiar zachowania agentów ani tokenów. Żadna reguła nie zniknęła i żadna nie zmieniła znaczenia, z jednym wyjątkiem, który rozstrzyga samo zadanie: agent pracujący nad zadaniem nie czyta już sekcji szablonu definicji o rzutowanych zmianach, którą dawne brzmienie można było czytać jako wymaganą obok sekcji zadania. Scalenie nie zmienia fundamentu, wołających skilla, jego opisu ani żadnego kodu.

#### Pod spodem

Zmiana stosuje regułę, że procedura potrzebna tylko jednemu krokowi albo jednemu zastosowaniu stoi w pliku obok skilla, który ten krok wymienia; opis skilla, jego kod w Pythonie i wejścia skilli nie zmieniły się.

### Do rozstrzygnięcia

1. Cztery propozycje zmieniające treść reguły, których dlatego nie zastosowano; każda jest opisana niżej w „Assessment of the skill”. Rozstrzygnij każdą osobno. (a) W trybie zadania czytać tylko trzy sekcje wspólnego pliku o sposobie pracy (800 słów) zamiast całego pliku (1752): droga zadania byłaby krótsza o 952 słowa, kosztem drugiego wyjątku od reguły serii, że procedurę kroku czyta się w całości, i ryzyka, że reguła spoza tych trzech sekcji wiąże zadanie. Zastosować? (b) We wspólnym pliku kroku 2 zmienić „or a section of the definition” na „or a section of the source document”: nie oszczędza słów, a wspólny plik przestaje być dosłownie dawnym tekstem. Zastosować? (c) Usunąć zdanie o przyszłych wołających skilla: ma 48 słów i jest czytane w każdym użyciu, ale skill przestaje wtedy mówić, że lista jego wołających jest otwarta. Usunąć? (d) Przenieść czytanie pliku trybu rzutowanego z kroku 1 na krok 4 w zastosowaniu do definicji: niezalecane, bo pytania kroku 4 zależą od tego pliku. Zastosować? (Własne sekcje zadania, „Assessment of the skill”.)
2. Zadanie podaje 424 słowa dla sekcji „Settlements to record” szablonu zadania z jej regułą. Własne wiersze sekcji i punkt reguły dają 405; 424 to inny zakres wierszy, który pomija własne wiersze sekcji. Ten request podaje 405. Liczba stoi po obu stronach każdego porównania przed/po, które jej używa, więc żaden procent w tym requeście się nie zmienia. Przyjąć 405? (Checks; recenzent przeliczył ją osobno.)

### Koszt

Około 38 minut czasu pracy w turach orkiestratora i pięciu turach agentów oraz 23 159 706 tokenów łącznie (18 528 584 na Sonnecie, 4 631 122 na Opusie), liczone przed napisaniem tego opisu. Odbyły się dwa przeglądy kodu: przegląd całej zmiany, który przeszedł z trzema drobnymi uwagami, i przegląd jednej poprawki do nich, który przeszedł. [Tabela etapów](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/find-foundation-entries-shape/stages.md).

### Jak scalić

Scal z zachowaniem commitów, bez squasha i bez rebase: linki w tym requeście prowadzą do commita z zapisem cyklu i przetrwają tylko wtedy. Nic w tym requeście nie czeka na przegląd fundamentu.

</details>

## Technical changes

- The old single file became five files in one directory, in two commits. The rebuild commit `a15de09` split the skill into its main file (598 words), the two step files (126 and 198 words) and the two use files (624 and 475 words); the commit `e9c900a` is the one fix for the three small remarks of the review. Nothing outside `elements/common/skill/` changed: not the shared files `elements/common/way_of_working.md` and `elements/common/projected_mode.md`, not the callers of the skill, not its description, not any Python.
- The main file `elements/common/skill/SKILL.md` now holds a table of the two callers in the callers' own words, so that an agent sent by a caller recognises its use: `define-project` with projected entries into the section "Projected foundation changes", and `refine-task` with rows of the section "Settlements to record", "task mode" to `refine-task` and to the skills of guidelines that hand back to it. Each pointer says whether the agent reads a file or carries out its lines.
- In the task use, the table starts as the old wording reached by "show it whole as above": proposed rows start `waiting`, rows with no concrete consequence for the next reader start `rejected`, and the whole table is shown with its source and next-reader column and a reason for each rejected row. This is written out in `elements/common/skill/task_variant.md`.
- The fix `e9c900a` changed three lines in two files: the sentence on reading the use file now reads "where you come to step 2, 4 or 5 without having read it", so a resumed use that reaches step 4 from step 3 also reads the whole file; and "In its place" in the task use's step 4 now reads "In place of step 4". Its third part was in the uncommitted assessment of the skill.

## Checks

- `python -B gate/run_tests.py` on the final tree `e9c900a`: exit **0**, 765 tests in 9 directories, every directory passed. The base `f447bb6` gave the same: exit 0, 765 tests. Five tests were skipped on Windows both times, so they are unchecked: four in `instruction-files/test_check_instructions.py` that need POSIX paths of links, and one that needs a FIFO (`test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`). No test of the repository failed and passed again. One check of the author's own, `route_check.py`, failed once after the fix on a phrase of its own that the fix had reworded, and passed after the phrase was updated; it is a script's expectation, not a test of the repository.
- The change touches only Markdown that no test reads, so no test was written and no failing run exists; the author's and the reviewers' focused checks (`gate/run_tests.py` for `elements/common`, `agent-instructions` and `installation`, `foundation_check.py`, `skill_entry_points.py`, `check_instructions.py`) all exited 0.
- Own-work check: the author named "no rewritten condition or pointer adds a route or loses one" as the requirement most likely not met, and checked it with a script that looks for 30 distinctive phrases of the old text on the route of each use (it was shown able to fail), with a comparison by windows of five words, and by hand for each condition and each new sentence. It found no loss; the places where the text differs are listed in the author's report. The reviewer repeated the comparison with its own script and by walking both uses by hand from the main file to the last step.
- Not checked: no agent has been sent through the rebuilt skill, so whether it reads only its own use and follows every pointer is argued, not measured. The search of session records that the method of judging skills puts before the assessment table was not made; every verdict rests on a cost the task measured or on a decision it carries. The comparison of carried text waits for the next real use of the skill in `loop2` (question 5 of the task).
- The numbers of this request: `verify_counts.py` (0 problems) compares with the files the sums, the author's counts block, the quotes and the figures of the proposals, and `verify_request.py` (0 problems) checks every number of this description against them and against the stages and gate figures; both ran after the last change to a counted file.
- The form check of this description: FORM_CHECK_RUN. The remarks check of the record: `python -B task-cycle/remarks_check.py .runs/task-cycles/find-foundation-entries-shape`, exit 0, `checked: 5 reports, 8 items other than none, 0 not in the process remarks`. The change touches no user interface, so screenshots do not apply.

## Foundation entries

none — the task carries no row of *Settlements to record* and no projected entry. The return step compared the nine decisions in play (WAY-256, 257, 265, 35, 115, 134, 117, 127 and 259), the part-map entries `elements-common` and `agent-instructions`, five invariants and a search of the whole foundation with the new files, and nothing needed correcting, so it made no commit. No invariant test, surface or *Violated* mark changed.

## Minor findings

The three Minor remarks of the review of the whole change were all fixed by the one fix. The review of the fix found one new Minor remark, not fixed; it does not mislead any reader. In the reviewer's words: "`elements/common/skill/task_variant.md:38` is now 103 characters long. Every other prose line of the five files wraps at 100. No check reports it and no reader is misled. Re-wrapping the paragraph would match the file."

## Findings outside the task's scope

none from the reviews. One question that the author found and the reviewer declined to judge, because the text is unchanged: the resume sentence in the main file (`elements/common/skill/SKILL.md:35-36`) says a task resumes "from the first row still `waiting`", while the states of a task table are `waiting` and `rejected` and the skill does not name the accepted state (the template does). It was kept as written.

## Assessment of the skill

The full table has 30 rows: each fragment of the old file quoted literally with its line range on `dfd50e5` (the file is identical on `f447bb6`), when an agent needs it, whether the agent recognises that moment, the verdict, the reason and the place after the rebuild. Every nonblank line of the old file stands in exactly one row, and the Words column adds up to 1584. Verdicts: 11 keep and 19 move; none removed or reworded in the files. The reviewer compared every row with the place where its fragment stands after the rebuild. [The table and the proposals in full](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/find-foundation-entries-shape/reports/assessment.md).

The proposals, which change the content of a rule and were not applied (each is also an item of *For you to decide*):

1. **Lines 41 and 48–50 of the old file, reading the shared file on the way of working in task mode.** Reword so that task mode reads the sections "Critique before collective review" (89 words), "How a skill asks" (208) and "Reading the foundation" (503), 800 words of the file's 1752, instead of the whole file. If left: task mode reads the whole file, whose sections on how a skill writes an entry are not used by this skill, though in the records the whole file was read before the skill in 47 of 107 uses and not at all in 22. If taken: 952 fewer words on the task route (2602 instead of 3554 with the files beside the skill, 1486 instead of 2438 without what the task-refining skill already read), at the price of a second exception to the series' rule, of a reviewer judging content and not only place, and of the risk that a rule outside the three sections binds the task use.
2. **Row 18, lines 64–66 of the old file, "or a section of the definition".** Reword to "or a section of the source document". If left: the task use carries three words of the definition, which a task agent reads past as it did before. If taken: the shared file is no longer literally the old text and a reviewer reads one more difference. No words saved.
3. **Row 3, lines 11–14 of the old file, the sentence on future callers** ("This skill serves a project definition and the refinement of a task for now; the breakdown of a project, the return step of a task and the entry of the process into an existing product will call it too …"). Remove it. It is a statement of plan, not a rule, so none of the conditions for removing a rule applies; the removal rests on cost: 48 words in every use of both variants. If left: the words are read every time, and a caller that is never added leaves the sentence stating a plan. If taken: the skill no longer says its list of callers is open, and the foundation was not searched for another place that says so.
4. **Row 11, lines 45–46 of the old file, reading the projected-mode file in the definition use.** Move the reading from step 1 to step 4 (not recommended). In the rare run with no accepted row, 419 words would be saved; the file also shapes the questions of step 4, which would then be asked without it, and the use that gains is the rare one.

## Word counts

The table of the top part, with the same figures, and how each sum is made: the skill's own text read on the route; that text plus the files read beside it (the shared file on the way of working in full, 1752 words; the task template's section with its rule, 405; for a definition the definition template's section, 674, and the projected-mode file, 419); and for a task the same without what the task-refining skill read earlier (the whole task template and the sections "How a skill asks", 208, and "Reading the foundation", 503). Counts were made after the last change to a counted file, the state before on `f447bb6`, with `elements/common/skill/SKILL.md` identical to `dfd50e5`. Against the task's estimates: task use 1397 fits 1300–1450, definition use 1546 fits 1500–1650, and the files together add 437, which fits 370–550. The files after the rebuild: main file 598, step 1 file 126, step 2 file 198, definition file 624 and task file 475 words.

## Course of the cycle

- **Task and sources:** an independent task, the seventh of eleven in the series that rebuilds the skills of the-way; the document was accepted on 2026-11-06; the base is `foundations` `f447bb62ce4f8d4a4badb1b283a10f62651d65d7`, which has not moved up to this request; the files this task changes are identical to `dfd50e5`, the base the task names.
- **Process pin:** none — the session worked on the-way itself; no pin to move.
- **Spec:** none, because questions 1–7 of the task settle the split, the files read at each step and the limits of the change; the names of the files and the wording of the pointers are a way of making what the task settles.
- **Route:** one author without a plan, on the same class of model as the orchestrator (Sonnet 5.5), because the change rewrites instruction text where a lost or reworded rule fails no test; one skill and its assessment depend on one judgment of rule preservation. The review of the whole change was made by Opus.
- **Plan:** none.
- **Choices:** 6 rows in the [table of questions and choices](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/find-foundation-entries-shape/cycle.md#questions-and-autonomous-choices), among them the 405 and the author's choices of how to make the files.
- **Blocking findings left:** none.
- **Record:** [the record of the cycle](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/find-foundation-entries-shape/cycle.md), in a commit of its own that the next commit removes, so that the target tree holds only the change. The task's backlog entry was not changed; closing the series after the merge is outside this request.
