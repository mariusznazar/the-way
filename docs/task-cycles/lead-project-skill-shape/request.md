**State: ready** — nothing blocks the merge; below wait your yes to a few choices of the rebuild, a set of new connecting sentences, three corrected places of the foundation and one difference between the task's figures and the files.

## What you will see

`lead-project` is the skill that leads a handed-over project plan through rounds of task refinement. It was one file of 2580 words that every agent read whole, whichever part of it the session used. After this change its main file has 2044 words and holds the picture of the whole, the rules that hold across the steps and steps 0 to 4, as they were. Four things moved into files beside it, each named in the main file at the step that leads to it, with the condition for reading it: the return of a task from a closed request to refinement, the run of the step that settles technology, the routing of plan and definition changes (step 5), and the change of the definition with the readiness gate. The step headings and the numbers 3.1 to 3.6 stay, so every file and dispatch that cites a step still points right.

The rule that decides what moves is changed with it: a step of a skill stays in the main file as long as records of real sessions do not show that part of the uses pass it by, and only variants, and steps that part of the uses pass by, go to files beside the skill. The records of the eight real uses of `lead-project` show steps 0 to 4 in all eight, so they stay; the return of a task and the run of the technology step were in none, and step 5 in seven.

What an agent reads of the skill, in words (counted as `wc -w` counts them in the C locale, on the files before and after; "with the step-0 files" adds the templates and the other files the orchestrator reads beside the skill at step 0, which did not change):

| Use | Skill text before | Skill text after | Change | With the step-0 files, before | After | Change |
|---|---:|---:|---:|---:|---:|---:|
| 1. Plan and definition change with the gate | 2580 | 2491 | −3.4% | 9833 | 9746 | −0.9% |
| 2. Plan change without a definition change | 2580 | 2220 | −14.0% | 9833 | 9475 | −3.6% |
| 3. No step 5, up to agreeing the progress | 2580 | 2044 | −20.8% | 9833 | 9299 | −5.4% |
| 4. Return of a task, then a plan change | 2580 | 2466 | −4.4% | 9833 | 9721 | −1.1% |
| 5. A round with a technology run, then a plan change | 2580 | 2349 | −9.0% | 9833 | 9604 | −2.3% |
| 6. A critic or refiner sent to the definition-change route | 2580 | 2491 | −3.4% | 9833 | 9746 | −0.9% |

The five files together have 2866 words, 286 more than the old single file. These are counts of files, not a measurement of how agents behave or of tokens; the next real use of the skill in `loop2` shows it. The saving is small where a session uses the definition change (use 1: −89 words of 2580) and large where it does not (use 3: −536). No rule disappeared or changed meaning: every fragment of the old file stands in the main file or in the file of the step or variant that needs it. A few short sentences are new; they are listed below. The merge does not change the description of the skill, any code, the entry points, or the two files the lead skill reads beside it.

### Underneath

The change applies the rule that a procedure which only one variant of a skill needs stands in a file beside the skill that the step names, and that a variant file one step points to is named by the main file at that step too; it also edits that rule in the foundation so that a step every use comes to is not moved.

## For you to decide

1. Five choices of the rebuild that the task did not fix and that change what an agent meets in the skill. Decide them together. (a) The sentences of step 5 that serve both a plan change and a definition change (12 lines of the old file) stay with the plan-change file; the other choice was to put them in the definition file, so that a plan change alone would not read them. (b) The rule "never run `git fetch --prune`" stays in the main file, 29 words carried by sessions that never return a task; it sat inside the paragraph of that variant, but its reason (it would erase the evidence of other tasks' closed requests) does not depend on the variant. (c) The bullet on closing a finished project (46 words) stays in the main file, although no real use reached it; the task names which variants move, and this one is a candidate for the follow-up task. (d) One sentence of step 3.3 on the technology run moved with a 22-word pointer in its place: 20 words saved. (e) The opening line of each of the four new files is one or two sentences that restate the pointer's condition and add no road. Keep these choices? (Choices, Course of the cycle.)
2. The rebuild added a few sentences that the old file did not hold, to keep every route once the text stands in several files: the pointers at steps 0, 1, 3.1, 3.3 and 5, the opening lines of the four files, and the changed connectors of seven moved sentences (for example "step 6" in the moved text became "3.6 of the main file"). Each is quoted, with what it switches off, under "New sentences" below. Accept them? (New sentences.)
3. Three places of the foundation repeated the old rule that a step of a skill goes to a file beside it also when every use comes to it: the paragraph on skills in the rules for instruction files, and the reasons of two earlier decisions. The cycle reworded them to the new rule, as the task asked; their wording is the cycle's. Accept? (Foundation entries.)
4. The task gave 37 session records of Codex that mention the skill; the cycle found 31 with the same pattern in the same directory, and none of them is a use of the skill. The judgement of the skill therefore rests on the eight Claude Code uses, as the task's own list; by the new rule a step stays where records are few. Merge as it stands? (Discrepancies.)

## Cost

About 45 minutes of working time in the turns of the orchestrator and of the agents, and 58,011,564 tokens in all, every one on Sonnet 5.5, as counted before this description was written. Two code reviews ran, both passed: the review of the whole change (six Minor findings) and the review of the one fix for them; the return step found nothing to correct and committed nothing, so it had no review. [Table of stages](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/lead-project-skill-shape/stages.md).

## How to merge

Merge keeping the commits, with no squash and no rebase: the links in this request lead to the commit that holds the record of the cycle, and they survive only then.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — nic nie blokuje scalenia; poniżej czekają na Twoją zgodę: kilka wyborów przy przebudowie, zestaw nowych zdań łączących, trzy poprawione miejsca fundamentu i jedna różnica między liczbami z zadania a plikami.

### Co zobaczysz

`lead-project` to skill, który prowadzi przekazany plan projektu przez rundy doprecyzowania zadań. Był jednym plikiem o 2580 słowach, który każdy agent czytał w całości, niezależnie od tego, której części sesja używała. Po zmianie jego główny plik ma 2044 słowa i zawiera obraz całości, reguły obowiązujące na wszystkich krokach oraz kroki 0–4, bez zmian. Cztery rzeczy przeszły do plików obok, a główny plik wymienia każdą przy kroku, który do niej prowadzi, z warunkiem jej czytania: powrót zadania z zamkniętego requestu do doprecyzowania, przebieg kroku, który rozstrzyga technologię, kierowanie zmian planu i definicji (krok 5) oraz zmiana definicji z bramką gotowości. Nagłówki kroków i numery 3.1–3.6 zostają, więc każdy plik i zlecenie, które powołuje się na krok, nadal trafia.

Razem zmienia się reguła, która rozstrzyga, co się przenosi: krok skilla zostaje w głównym pliku, dopóki zapisy prawdziwych sesji nie pokażą, że część użyć go pomija; do plików obok idą tylko warianty oraz kroki, które część użyć pomija. Zapisy ośmiu prawdziwych użyć `lead-project` pokazują kroki 0–4 we wszystkich ośmiu, więc zostają; powrotu zadania i przebiegu kroku technologii nie było w żadnym, a krok 5 był w siedmiu.

Co agent czyta ze skilla, w słowach (liczone jak `wc -w` w locale C, na plikach przed i po; „z plikami kroku 0” dodaje szablony i inne pliki, które orkiestrator czyta obok skilla w kroku 0 i które się nie zmieniły):

| Użycie | Tekst skilla przed | Tekst skilla po | Zmiana | Z plikami kroku 0, przed | Po | Zmiana |
|---|---:|---:|---:|---:|---:|---:|
| 1. Zmiana planu i definicji z bramką | 2580 | 2491 | −3,4% | 9833 | 9746 | −0,9% |
| 2. Zmiana planu bez zmiany definicji | 2580 | 2220 | −14,0% | 9833 | 9475 | −3,6% |
| 3. Bez kroku 5, do uzgodnienia postępu | 2580 | 2044 | −20,8% | 9833 | 9299 | −5,4% |
| 4. Powrót zadania, potem zmiana planu | 2580 | 2466 | −4,4% | 9833 | 9721 | −1,1% |
| 5. Runda z przebiegiem technologii, potem zmiana planu | 2580 | 2349 | −9,0% | 9833 | 9604 | −2,3% |
| 6. Krytyk albo doprecyzowujący skierowany na drogę zmiany definicji | 2580 | 2491 | −3,4% | 9833 | 9746 | −0,9% |

Pięć plików razem ma 2866 słów, o 286 więcej niż dawny pojedynczy plik. To liczby słów w plikach, nie pomiar zachowania agentów ani tokenów; pokaże to następne prawdziwe użycie skilla w `loop2`. Oszczędność jest mała tam, gdzie sesja używa zmiany definicji (użycie 1: −89 słów z 2580), a duża tam, gdzie nie używa (użycie 3: −536). Żadna reguła nie zniknęła ani nie zmieniła znaczenia: każdy fragment dawnego pliku stoi w głównym pliku albo w pliku kroku lub wariantu, który go potrzebuje. Kilka krótkich zdań jest nowych; stoją na liście poniżej. Scalenie nie zmienia opisu skilla, żadnego kodu, wejść ani dwóch plików, które skill czyta obok.

### Do rozstrzygnięcia

1. Pięć wyborów przy przebudowie, których zadanie nie przesądziło, a które zmieniają to, na co agent trafia w skillu. Rozstrzygnij je razem. (a) Zdania kroku 5, które służą i zmianie planu, i zmianie definicji (12 wierszy dawnego pliku), zostają przy pliku zmiany planu; drugi wybór to plik definicji, wtedy sama zmiana planu by ich nie czytała. (b) Reguła „nigdy nie uruchamiaj `git fetch --prune`” zostaje w głównym pliku, 29 słów niesionych przez sesje, które nigdy nie wracają zadania; stała w akapicie tego wariantu, ale jej powód (skasowałaby ślad zamkniętych requestów innych zadań) nie zależy od wariantu. (c) Punkt o zamykaniu skończonego projektu (46 słów) zostaje w głównym pliku, choć żadne prawdziwe użycie do niego nie doszło; zadanie wskazuje, które warianty przechodzą, a ten jest kandydatem do zadania następczego. (d) Jedno zdanie kroku 3.3 o przebiegu technologii przeszło do pliku, a w jego miejscu stoi odsyłacz o 22 słowach: oszczędność 20 słów. (e) Zdanie otwierające każdy z czterech nowych plików to jedno–dwa zdania, które powtarzają warunek odsyłacza i nie dodają drogi. Zostawić te wybory? (Choices, Course of the cycle.)
2. Przebudowa dodała kilka zdań, których dawny plik nie miał, żeby zachować każdą drogę, gdy tekst stoi w kilku plikach: odsyłacze w krokach 0, 1, 3.1, 3.3 i 5, zdania otwierające czterech plików oraz zmienione spójniki siedmiu przeniesionych zdań (np. „krok 6” w przeniesionym tekście stał się „3.6 głównego pliku”). Każde jest zacytowane, z tym, co wyłącza, w części „New sentences” poniżej. Przyjąć je? (New sentences.)
3. Trzy miejsca fundamentu powtarzały starą regułę, że krok skilla idzie do pliku obok także wtedy, gdy dochodzi do niego każde użycie: akapit o skillach w regułach plików instrukcji i uzasadnienia dwóch wcześniejszych decyzji. Cykl przeredagował je według nowej reguły, jak chciało zadanie; ich brzmienie jest dziełem cyklu. Przyjąć? (Foundation entries.)
4. Zadanie podało 37 zapisów sesji Codexa, które wspominają skill; cykl znalazł 31 z tym samym wzorcem w tym samym katalogu i żaden nie jest użyciem skilla. Ocena skilla opiera się więc na ośmiu użyciach Claude Code, jak na liście zadania; według nowej reguły krok zostaje tam, gdzie zapisów jest mało. Scalić tak, jak stoi? (Discrepancies.)

### Koszt

Około 45 minut czasu pracy w turach orkiestratora i agentów oraz 58 011 564 tokenów łącznie, wszystkie na Sonnet 5.5, liczone przed napisaniem tego opisu. Odbyły się dwa przeglądy kodu, oba przeszły: przegląd całej zmiany (sześć uwag Minor) i przegląd jednej poprawki do nich; krok zwrotny nie znalazł nic do poprawienia i niczego nie zatwierdził, więc nie miał przeglądu. [Tabela etapów](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/lead-project-skill-shape/stages.md).

### Jak scalić

Scal z zachowaniem commitów, bez squasha i bez rebase: linki w tym requeście prowadzą do commita z zapisem cyklu i przetrwają tylko wtedy.

</details>

## Technical changes

- Four commits on top of `foundations` `57795e4`. `e98f46b`: the decision log entry that says where a fragment of a skill stands, edited in place (the step every use comes to stays in the main file; the rule for a skill with no records), its *Rationale* and *Rejected*; the paragraph on skills in the rules for instruction files (`instruction-files/kind_skill.md`); and the reasons of two earlier decisions that repeated the old rule. `b9e19f7`: `project-level/lead/skill/SKILL.md` cut to steps 0 to 4, the pointers and a stub of step 5, and four new files beside it: `task_return.md` (the return of a task, 246 words), `technology_run.md` (the run of the technology step, 129), `route_changes.md` (step 5, plan changes, 176) and `definition_change.md` (the change of the definition and its gate, 271). `038a330`: line breaks only in the rationale. `08e70be`: the fix for the Minor findings of the whole-change review (see below).
- Files after the change, in words: `SKILL.md` 2044, `route_changes.md` 176, `definition_change.md` 271, `task_return.md` 246, `technology_run.md` 129. The description of the skill, every Python file, `answering.md`, `conversation_template.md` and the other skills are unchanged.
- The fix `08e70be` for the six Minor findings of the whole-change review took the four that concern files: the figure of "five to fifteen percent more words" in the decision's reasoning now says it is an estimate made before any rebuild from the word counts of one skill's files; the pointer of step 5 now also sends the road of a gate or recheck found pending in step 0 to the plan-change file; "this route" in the definition file became "the definition change"; lines of the decision over 100 characters were rewrapped. The other two findings concern this description and are met here (Minor findings).

## Checks

1. `python -B gate/run_tests.py` on the final tree `08e70be`: exit **0**, 804 tests in 9 directories, every directory passed; the target branch had not moved since the base, so this is the tree that merges. The base `57795e4` gave exit 0, 804 tests in 9 directories, every directory passed. Five tests were skipped on Windows in every run, so they are unchecked: four in `instruction-files/test_check_instructions.py` that need the real path of a link as on POSIX, and one that needs a FIFO. No test failed and passed again.
2. The change touches only Markdown that no test reads, so no test was written. The author's and the reviewers' focused checks exited 0: `elements/common/foundation_check.py`, `instruction-files/check_instructions.py` (one warning, `dead-path AGENTS.md:21`, which stood before the change), and `gate/run_tests.py` for `instruction-files`, `agent-instructions`, `elements/common`, `project-level` and `installation`.
3. Own-work check: the author named "the condition of each pointer covers every road and is worded as reaching the step, and each moved sentence reads alone" as the requirement most likely not met, and checked it with a script of 33 assertions on the roads of the criterion and the moved sentences (it found nothing after the last edit, so it drove no change), a word-level comparison of the old file with the five new files (the differences are the pointers, the opening lines and the rewords of the assessment), and an independent recount of every number of its report. The whole-change reviewer recomputed every number, compared 40 quoted fragments with the old file, walked roads 1, 4 and 6 by hand, and found no lost or changed rule.
4. Not checked: no agent has been sent through the rebuilt skill, so whether an agent recognises the moment of the return of a task and of the technology run is argued, not measured; no real use passed either in the eight records, and the next use in `loop2` shows it.
5. The numbers: `verify_request.py` recounts, with `wc -w` in the C locale, every figure of the word counts and of this description's prose and compares it with the files at the head after the last change of a counted file: exit 0, all numbers agree (79 allowed values, 6 routes, 56 assessment rows, and the table of the top part against the table of the block); a control copy with three wrong numbers gave exit 1, each named.
6. The remarks check of the record: `python -B task-cycle/remarks_check.py .runs/task-cycles/lead-project-skill-shape` listed 11 items at its first run; the check did not read the report of the author, whose section heading carries a number before the words, so the six items of that report were copied into the remarks by hand and the case is an entry of the remarks (it is a matter of the-way's script, not of the product). Last run on the original: exit 0, `checked: 5 reports, 11 items other than none, 0 not in the process remarks` (2 runs).
7. The form check of this description, `python -B task-cycle/request_check.py .runs/task-cycles/lead-project-skill-shape/request.md --task .runs/task-cycles/lead-project-skill-shape/task.md`, and the check of private paths on it, `python -B task-cycle/private_paths_check.py .runs/task-cycles/lead-project-skill-shape/request.md`: last runs before publishing: exit 0 and exit 0 (`checked: 1 files, 0 listed`). The check of private paths on the copy of the record and the remarks check on it: written after the record's commit.

## Foundation entries

- **Where a fragment of a skill stands (the entry the task changed, `row 1`)**: a step of a skill stays in its main file until records of sessions a person can open show that part of the uses pass it by, also where no record exists; variants, and steps some uses pass by, stand in files beside the skill; the sentence on a fragment some steps need is unchanged. Edited in place in `foundations/decisions.md` (WAY-256), three binding sentences; its reason is taken from the source of row 1 and its *Rejected* ways are the ones the task did not choose.
- **`the cycle's`** — three places that repeated the old rule, corrected to the new one in the same change (the search of the whole foundation): the paragraph on skills in `instruction-files/kind_skill.md`, which now has a bullet for a step every use comes to; and the *Rationale* of WAY-125 and of WAY-127, which now say that only a variant, or a step some uses pass by, stands beside the method, and that a step every use comes to stays in the main file.
- No invariant test, surface or *Violated* mark changed; no invariant, environment fact, glossary term or part-map entry was written or changed (the return step compared the entries the change edits, the twelve decisions the task names, the part-map entries of `decisions`, `project-level` and `instruction-files`, and the entry-point files with the files and found nothing to correct).

## Minor findings

1. The six Minor findings of the whole-change review were all within the task. Four were fixed in the one fix (`08e70be`): the unmeasured figure in the decision's reasoning, the missing road of a pending gate at the step-5 pointer, "this route" with no antecedent, and seven over-long lines. The review of the fix passed with no new Critical or Important finding.
2. Not fixed in code, because they concern this description: in the reviewer's words, "the request's word-count columns 'with the step-0 files' mix two bases": the side files stand at 7253 words at the task's base and at 7255 at the head, because a merge between them lengthened `conversation_template.md` by two words; so the change in the right-hand columns is the real change of the skill text plus 2 words. Met here: the skill-text columns are exact, and the right-hand columns of the table above use 9833 before and the head's side files after; use 1 is −89 in the skill text and −87 with the side files. Also: "two opening lines are given 'no exclusion' or an exclusion that is the pointer itself": the opening line of the technology file restates the pointer's condition, adds none and excludes nothing the pointer did not; the opening line of the file on the return of a task restates the pointer's condition and adds no road, the transitions made from evidence are excluded by that condition and not by the line.
3. A note of the review of the fix, outside the intent of the fix: the skill text of use 5 is 2349 words, one under the top of the task's estimate (2150–2350); a later added word on that road leaves the estimate. A margin, not a defect.

## Findings outside the task's scope

None. Two things the reviewer and the author declined to judge or flagged for the follow-up task of the series, not findings: the bullet on closing a finished project (`SKILL.md:86–88`), which no real use reached, and the earlier-rebuilt skills that carry a file for a step every use comes to; both are the follow-up task's material.

## Assessment of the skill

The full table has 56 rows: each fragment of the old file quoted literally with its line range on `a3206c1`, when an agent needs it, whether the agent recognises that moment, the verdict, its ground and its place after the rebuild. Verdicts: 31 keep, 9 move, 16 reword (no row is a remove). The 16 rewords are the connectors that a moved sentence needed to read alone in its file, the pointers, and the opening lines of the files; none changes the content of a rule. The reviewer compared every row with the place where its fragment stands: 40 quotes confirmed against the old file, the rest are the new text. [The table in full, with the search of the session records, the readers outside the skill and the new sentences](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/lead-project-skill-shape/reports/assessment.md).

Proposals that change the content of a rule: none. The task asked for "remove" and "reword" verdicts that change a rule to be listed as proposals; there are none, so there is nothing left unapplied. Two observations for the follow-up task, not applied: the bullet on closing a finished project (46 words, no real use reached it); and a sentence in the rules for instruction files (`instruction-files/SKILL.md:143–151`) that could name the records that tell which uses pass a step by.

The session records searched (Claude Code, the eight uses of the task and one session that only mentions the skill): steps 0 to 4 in 8 of 8; step 5 with a plan change in 7 of 8; a definition change with the gate in 4 of 8; no return of a task from a closed request; no run of the technology step.

## New sentences

Each sentence below is new or has a new condition; for each, what it switches off:

1. Step 0, `SKILL.md`: "Step 5 gives that recovery." It adds the pointer the recovery of a pending gate needs so that the definition file is reached; it does not repeat the recovery and names no file, so the condition for the file stays in one place (step 5).
2. Step 1, `SKILL.md`: "One more transition is supported, only on the human's word (WAY-269): a task whose blocked request the human closed returns to refinement. Each time you reach this step, at the session start or after a merge in the middle of it, read `task_return.md` beside this skill when the human has said so." It switches off transitions made from evidence, a request closed by anyone but the human, and any moment other than reaching step 1.
3. Step 3.1, `SKILL.md`: "For a refiner's *Child-work request* for a run of the step that settles technology (WAY-267), in any turn of a round, one resumed from the conversation files included, read `technology_run.md` beside this skill." It switches off other child-work requests (critiques, answerers).
4. Step 3.3, `SKILL.md`: "A run of the step that settles technology in the conversations enters the package as `technology_run.md` gives; read it unless 3.1 did." It switches off a round without a run and a 3.3 after a 3.1 that already read the file.
5. Step 5, `SKILL.md`: "On reaching this step, from a refiner's result `plan change`, from a changed definition in step 0 or from a gate or recheck found pending there, read `route_changes.md` beside this skill. For a change of the definition, its gate or the plan recheck after it, a gate or recheck found pending in step 0 included, read `definition_change.md` beside this skill too." It switches off a plan change without a definition change (the definition file is not read) and a step 5 never reached.
6. The opening line of each new file: `task_return.md` "Read from step 1 of `SKILL.md` when the human has said that the blocked request of a task is closed."; `technology_run.md` "Read from 3.1 and 3.3 of `SKILL.md`."; `route_changes.md` "Read from step 5 of `SKILL.md`. The edit of the definition and its gate stand in `definition_change.md`."; `definition_change.md` "Read from step 5 of `SKILL.md`, and from step 0 when a definition gate or plan recheck is found pending." Each restates the pointer's condition and adds no road; the opening line of `route_changes.md` switches off the definition's edit, gate and recheck, which stand in the other file, and that of `definition_change.md` a plan change without a definition change.
7. The connectors of the moved sentences that would not read alone in their files: `after step 3` → `after item 3` and `as before` → `the reader (plan_state.py)` and `as SKILL.md step 1 gives for a conflicting trace` (`task_return.md`); `go in the package once` → `go in the round package of 3.3 once` and `(step 6)` → `(3.6 of SKILL.md)` (`technology_run.md`); `by definition_change.md` added at the end of the route (`route_changes.md`); `from step 0` → `from its step 0` and `this route` → `the definition change` (`definition_change.md`). Each keeps the meaning of the sentence and names a thing the moved sentence no longer sits beside.

## Readers outside the skill

What each reader outside the skill meets after the rebuild and what it loses:

| Reader | After the rebuild | Loses |
|---|---|---|
| `project-level/plan/template.md:102` ("only as `lead-project` gives") | opens the main file at step 1, where the pointer bullet says that a task whose blocked request the human closed returns to refinement and names the file | one file read; nothing else |
| `project-level/plan/skill/hand_over.md:16` | names `lead-project` as the next step; the name leads to the same skill | nothing |
| `project-level/plan/skill/delegated_mode.md:3–4`, `project-level/plan/skill/SKILL.md:25` | a `plan-project` agent dispatched by `lead-project` reads its conversation file and the conversation template, not the lead skill | nothing |
| `project-level/skill/delegated_mode.md:4–7`, `project-level/skill/SKILL.md:28` | a `define-project` agent dispatched for a definition edit does not read the lead skill | nothing |
| `orchestrated_mode.md` of the task skill and of the three skills of guidelines, `product-guidelines/coding/SKILL.md:88`, `testing/SKILL.md:79` | a refiner dispatched by the orchestrator does not read the lead skill | nothing |
| a critic or refiner told "`SKILL.md` (definition-change route and what it blocks)" | finds the heading "5. Route plan and definition changes" with the pointer that names both files; what the route blocks stands in step 4 and in the definition file | two file reads to reach the route; a critic that read the whole file read 2580 words and now reads 2044 + 176 + 271 |
| `installation/install.py:33`, `installation/test_lead_installation.py`, the entry points of `lead-project` | the name still maps to the main file; the entry point already tells the session to read a named file when its step comes | nothing; the `installation` tests passed |

## Word counts

The table of the top part, with the same figures; counted as `wc -w` in the C locale after the last change to a counted file, the state before on `a3206c1` (2580 words in the main file) and the state after at the head `08e70be`. The skill's own text is the main file and the files the route reads beside it; "with the step-0 files" adds the files the orchestrator reads at step 0 and which did not change: `project-level/plan/template.md` (1855), `project-level/task/template.md` (2213), `project-level/lead/conversation_template.md` (1419 at `a3206c1`, 1421 at `57795e4`), `project-level/lead/answering.md` (775), the sections "How a skill asks" (204) and "Reading the foundation" (496) of `elements/common/way_of_working.md`, and `project-level/plan/skill/reading_definition_and_plan.md` (291); together 7253 words at `a3206c1` and 7255 at `57795e4`, so 9833 before. Files after: `SKILL.md` 2044, `route_changes.md` 176, `definition_change.md` 271, `task_return.md` 246, `technology_run.md` 129; together 2866 (+286 against 2580). The pointers in `SKILL.md` have 174 words. The task's own estimates of the skill text per use (1: 2400–2550, 2: 2050–2250, 3: 1950–2100, 4: 2300–2500, 5: 2150–2350, 6: 2400–2550) all contain the measured number; its estimate of the growth of the five files together (+170 to +370) contains +286.

Route 6 counts the whole main file and the two files its pointers name; a critic that opens only the part named in its order reads less, and the step-0 files are read by the orchestrator, not by that critic, so the right-hand columns of route 6 are given because the task asks for two numbers on each route. [The counts in full](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/lead-project-skill-shape/reports/word-counts.md).

## Discrepancies

The task's figures that do not agree with the files in the given range, or that were not checked:

1. The count of Codex session files that mention the skill (task, *Context*): 37 stated, 31 found with the same pattern in the same directory; none of the 31 is a use of the skill. (For you to decide, 4.)
2. The task calls lines `:7605`, `:7609` and `:7634` of the decision log at `a3206c1` sentences that contradict the new rule: the first two do and are reworded; `:7634` (moving a one-instruction fragment is rejected) does not contradict it and stays.
3. The 7261 words of the files read at step 0, given in an earlier question of the task, count the headings of the following sections; the files give 7253 at `a3206c1` (the task's own later figure agrees).
4. Between the task's base `a3206c1` and the target `57795e4`, two lines of the main file (130–134, "table of choices" → "message on the choices", one word more) and three of the conversation template changed; the line ranges of the task still hold, and the table quotes `a3206c1`.
5. Not checked, because they are no counts of the files: the 19 agents and the 2.4 million tokens of the task's *Need* and *Context*.
6. The following figures of the task agree with the files: `SKILL.md` 2580 words; lines `:61–77` 240 words; `:113–118` 67; `:189–219` 399 (counting the heading).

## Course of the cycle

- **Task and sources:** an independent task, the tenth of eleven in the series that rebuilds the skills of the-way and the last one not merged; the document was accepted on 2026-11-08; the base is `foundations` `57795e4`, and the files this task changes or counts differ from the task's base `a3206c1` only in the lines named under Discrepancies.
- **Process pin:** none — the session worked on the-way itself; no pin to move.
- **Spec:** none, because the task's questions 1 to 11 and its *To do* settle the split, the limits of the change, the routes counted and the rule; the names of the files and the wording of the pointers are a way of making what the task settles.
- **Route:** one author without a plan, on the same class of model as the orchestrator (Sonnet 5.5), because the change edits a binding decision in place and rewrites instruction text where a lost or reworded rule fails no test, across three parts. The review of the whole change passed with six Minor findings; one fix took four of them, and the review of the fix passed. The return step committed nothing.
- **Plan:** none on the one-author route.
- **Choices:** seven other choices of the cycle, listed under *For you to decide* 1 and in the questions table of the record: the boundary of the definition file, the rule on `git fetch --prune`, the closing bullet, the 3.3 pointer, the opening lines, the estimate in the decision's reasoning (kept in both places, stated as an estimate), and the base of the numbers (Q1). [Questions table](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/lead-project-skill-shape/cycle.md).
- **Blocking findings left:** none.
- **Record:** [the record of the cycle](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/lead-project-skill-shape/cycle.md).
