**State: ready** — nothing blocks the merge; six proposals not applied, a set of new connecting sentences and one listing of a record check wait for your yes below.

## What you will see

`define-project` is the skill that leads a project definition from an idea to its readiness gate. It was one file of 1937 words that every agent read whole, whichever way it used the skill: writing a definition from an idea, resuming one, a turn that `lead-project` dispatches to change a definition and take it through the gate, or reopening an approved definition. After this change its main file has 570 words: the picture of the whole, four rules that hold at every step, step 0 and one line per step that names the file to read. The procedure of each step from 1 to 7 stands in a file of its own beside it, and so do the two variants: the resumed definition of step 0 and the dispatched turn. The steps keep their numbers 0 to 7 and 7.1 to 7.5, so every file and every dispatch that cites a step still points right.

What an agent reads of the skill, in words (counted as `wc -w` counts them under a UTF-8 locale, on the files before and after; "with the files beside" adds the definition template and the other files the route reads beside the skill):

| Use | Skill text before | Skill text after | Change | With the files beside, before | After | Change |
|---|---:|---:|---:|---:|---:|---:|
| 1. A definition from an idea, steps 0–7 | 1937 | 1840 | −5.0% | 5869 | 5772 | −1.7% |
| 2. Resumed while entries are found, steps 0, 5, 6, 7 | 1937 | 1516 | −21.7% | 5366 | 4945 | −7.8% |
| 3a. A dispatched turn reading its own steps | 1937 | 1684 | −13.1% | 6785 | 6532 | −3.7% |
| 3b. A dispatched turn reading every file | 1937 | 2387 | +23.2% | 6785 | 7235 | +6.6% |
| 4. An approved definition reopened, steps 0 and 7 | 1937 | 1342 | −30.7% | 5366 | 4771 | −11.1% |
| 5. No technology section, reopened, steps 0, 6, 7 | 1937 | 1408 | −27.3% | 5366 | 4837 | −9.9% |

The ten files together have 2387 words, 450 more than the old single file. These are word counts of files, not a measurement of how agents behave or of tokens; whether a dispatched turn reads only its own steps (3a) or everything (3b) shows at the next real use of the skill. No rule disappeared and none changed meaning: each fragment of the old file now stands either in the main file or in the file of the step or variant that needs it. A handful of short sentences are new; they connect the files and are listed under *For you to decide*. The merge does not change the foundation, the definition template, the callers of the skill, its description or any code.

### Underneath

The change applies the rule that a procedure which only one step or one variant of a skill needs stands in a file beside the skill that the step names, and that a variant file one step points to is named by the main file at that step too.

## For you to decide

1. Six proposals that would change what a rule says and were therefore not applied; each is described under "Assessment of the skill" below. Decide each separately. (a) Remove from the dispatched turn's file the sentence on when the project orchestrator may edit a definition itself: 31 words fewer in every dispatched turn, the rule stays in `lead-project` and in its decision, at the price of a review of meaning in a change of its own. Remove it? (b) The other repetitions between the dispatched turn's file and `lead-project`: five, all recommended to keep, since each side states its own half of one hand-over. Keep them? (c) The repetitions between the skill and the definition template: ten, all recommended to keep, since each is a pointer or applies the template's rule at the step that asks. Keep them? (d) "The gate" for the readiness gate, while the glossary gives "gate" as the command that runs all tests: not recommended now, since the same words stand in a decision and in the template, outside this task. Leave it? (e) Write the template's path in full, `project-level/definition_template.md`, where the skill names it bare, since every other file it names now lies beside the skill: two words longer, no rule changes. Apply it? (f) In four other rebuilt skills, change "each skill named below" to "each skill named below or in the files beside this skill", as this skill now reads: a few words in each, outside this task. Make a task of it? (Assessment of the skill.)
2. The rebuild added a few short sentences that the old file did not hold, to keep the routes it had once the text stands in several files. Each is quoted, with what it switches off, under "New sentences" below: the resume line of step 0 also names a dispatched turn's definition; the file of step 7 opens with the three things a dispatched turn does differently there; the rule to write each answer into the definition before the next question now holds from the first write onward instead of only in the rounds; step 6 sends a finding of the readiness check to the file of step 7, which says where it goes (added after the review found that route lost); "named below" now also covers the files beside the skill; and the file of step 7 is named `readiness_gate.md`, not `gate.md`, because the glossary gives "gate" another meaning. Accept them? (New sentences.)
3. A check of the cycle's record listed, once, a line of a report as a search item the record did not hold; the line is a test result the author appended at the end of the report, not an item. The cycle did not copy it as an item; it named the case in the record's remarks, after which the check lists nothing. Merge as it stands? (Checks, 6.)

## Cost

About 54 minutes of working time in the turns of the orchestrator and of the agents, and 46,956,624 tokens in all, every one on Opus 5.5, as counted before this description was written. Three code reviews ran: the review of the whole change, which failed on one blocking finding; the review of the one fix, which passed; and the review of the return step, which passed. [Table of stages](https://github.com/mariusznazar/the-way/blob/4f508f8ca006ada60fa71ae79c445ef0589e5805/docs/task-cycles/define-project-skill-shape/stages.md).

## How to merge

Merge keeping the commits, with no squash and no rebase: the links in this request lead to the commit that holds the record of the cycle, and they survive only then.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — nic nie blokuje scalenia; poniżej czekają na Twoją zgodę: sześć propozycji, których nie zastosowano, zestaw nowych zdań łączących i jedno wskazanie sprawdzenia zapisu cyklu.

### Co zobaczysz

`define-project` to skill, który prowadzi definicję projektu od pomysłu do bramki gotowości. Był jednym plikiem o 1937 słowach, który każdy agent czytał w całości, niezależnie od tego, jak skilla używał: pisząc definicję od pomysłu, wznawiając ją, w turze zleconej przez `lead-project` (zmiana definicji i bramka) albo otwierając ponownie zatwierdzoną definicję. Po tej zmianie jego plik główny ma 570 słów: obraz całości, cztery reguły obowiązujące na każdym kroku, krok 0 i po jednym wierszu na krok, który wskazuje plik do przeczytania. Procedura każdego kroku od 1 do 7 stoi we własnym pliku obok, tak samo dwa warianty: wznowienie definicji w kroku 0 i tura zlecona. Kroki zachowują numery 0–7 i 7.1–7.5, więc każdy plik i każde zlecenie, które powołuje się na krok, dalej trafia we właściwe miejsce.

Co agent czyta ze skilla, w słowach (liczonych jak `wc -w` w locale UTF-8, na plikach przed zmianą i po niej; „z plikami obok” dolicza szablon definicji i pozostałe pliki, które droga czyta obok skilla):

| Użycie | Tekst skilla przed | Tekst skilla po | Zmiana | Z plikami obok, przed | Po | Zmiana |
|---|---:|---:|---:|---:|---:|---:|
| 1. Definicja od pomysłu, kroki 0–7 | 1937 | 1840 | −5.0% | 5869 | 5772 | −1.7% |
| 2. Wznowienie w trakcie szukania wpisów, kroki 0, 5, 6, 7 | 1937 | 1516 | −21.7% | 5366 | 4945 | −7.8% |
| 3a. Tura zlecona czytająca swoje kroki | 1937 | 1684 | −13.1% | 6785 | 6532 | −3.7% |
| 3b. Tura zlecona czytająca wszystkie pliki | 1937 | 2387 | +23.2% | 6785 | 7235 | +6.6% |
| 4. Zatwierdzona definicja otwarta ponownie, kroki 0 i 7 | 1937 | 1342 | −30.7% | 5366 | 4771 | −11.1% |
| 5. Bez sekcji technologii, otwarta ponownie, kroki 0, 6, 7 | 1937 | 1408 | −27.3% | 5366 | 4837 | −9.9% |

Dziesięć plików razem ma 2387 słów, o 450 więcej niż dawny pojedynczy plik. To liczby słów w plikach, nie pomiar zachowania agentów ani tokenów; czy tura zlecona czyta tylko swoje kroki (3a), czy wszystko (3b), pokaże następne prawdziwe użycie skilla. Żadna reguła nie zniknęła i żadna nie zmieniła znaczenia: każdy fragment dawnego pliku stoi teraz w pliku głównym albo w pliku kroku lub wariantu, który go potrzebuje. Kilka krótkich zdań jest nowych; łączą pliki i są wymienione w „Do rozstrzygnięcia”. Scalenie nie zmienia fundamentu, szablonu definicji, wołających skilla, jego opisu ani żadnego kodu.

#### Pod spodem

Zmiana stosuje regułę, że procedura potrzebna tylko jednemu krokowi albo jednemu wariantowi skilla stoi w pliku obok skilla, który ten krok wymienia, a plik wariantu, do którego odsyła plik kroku, plik główny też wymienia przy tym kroku.

### Do rozstrzygnięcia

1. Sześć propozycji, które zmieniłyby treść reguły, więc ich nie zastosowano; każda jest opisana niżej w „Assessment of the skill”. Rozstrzygnij każdą osobno. (a) Usunąć z pliku tury zleconej zdanie o tym, kiedy orkiestrator projektu może sam edytować definicję: 31 słów mniej w każdej turze zleconej, reguła zostaje w `lead-project` i w swojej decyzji, kosztem przeglądu znaczenia w osobnej zmianie. Usunąć? (b) Pozostałe powtórzenia między plikiem tury zleconej a `lead-project`: pięć, wszystkie zalecane do zostawienia, bo każda strona mówi o swojej połowie jednego przekazania. Zostawić? (c) Powtórzenia między skillem a szablonem definicji: dziesięć, wszystkie zalecane do zostawienia, bo każde jest odsyłaczem albo stosuje regułę szablonu na kroku, który pyta. Zostawić? (d) „The gate” w znaczeniu bramki gotowości, choć słownik podaje „gate” jako polecenie uruchamiające wszystkie testy: niezalecane teraz, bo te same słowa stoją w decyzji i w szablonie, poza tym zadaniem. Zostawić? (e) Pisać ścieżkę szablonu w całości, `project-level/definition_template.md`, tam gdzie skill podaje samą nazwę, bo każdy inny plik, który wymienia, leży teraz obok skilla: dwa słowa dłużej, żadna reguła się nie zmienia. Zastosować? (f) W czterech innych przebudowanych skillach zmienić „each skill named below” na „each skill named below or in the files beside this skill”, jak brzmi teraz ten skill: kilka słów w każdym, poza tym zadaniem. Zrobić z tego zadanie? (Assessment of the skill.)
2. Przebudowa dodała kilka krótkich zdań, których dawny plik nie miał, żeby zachować jego drogi, gdy tekst stoi w kilku plikach. Każde jest zacytowane, razem z tym, co wyłącza, niżej w „New sentences”: wiersz wznowienia w kroku 0 wymienia też definicję tury zleconej; plik kroku 7 zaczyna się od trzech rzeczy, które tura zlecona robi tam inaczej; reguła wpisywania każdej odpowiedzi do definicji przed następnym pytaniem obowiązuje od pierwszego zapisu, a nie tylko w rundach; krok 6 odsyła znalezisko sprawdzenia gotowości do pliku kroku 7, który mówi, dokąd ono idzie (dodane po tym, jak przegląd znalazł tę drogę zgubioną); „named below” obejmuje też pliki obok skilla; a plik kroku 7 nazywa się `readiness_gate.md`, nie `gate.md`, bo słownik daje słowu „gate” inne znaczenie. Przyjąć? (New sentences.)
3. Sprawdzenie zapisu cyklu raz wskazało wiersz raportu jako pozycję poszukiwań, której zapis nie zawierał; ten wiersz to wynik testu, który autor dopisał na końcu raportu, a nie pozycja. Cykl nie przepisał go jako pozycji; nazwał przypadek w uwagach zapisu, po czym sprawdzenie nic nie wskazuje. Scalić tak, jak jest? (Checks, 6.)

### Koszt

Około 54 minut czasu pracy w turach orkiestratora i agentów oraz 46 956 624 tokeny łącznie, wszystkie na Opusie 5.5, liczone przed napisaniem tego opisu. Odbyły się trzy przeglądy kodu: przegląd całej zmiany, który nie przeszedł z powodu jednego blokującego ustalenia, przegląd jednej poprawki, który przeszedł, i przegląd kroku zwrotnego, który przeszedł. [Tabela etapów](https://github.com/mariusznazar/the-way/blob/4f508f8ca006ada60fa71ae79c445ef0589e5805/docs/task-cycles/define-project-skill-shape/stages.md).

### Jak scalić

Scal z zachowaniem commitów, bez squasha i bez rebase: linki w tym requeście prowadzą do commita z zapisem cyklu i przetrwają tylko wtedy.

</details>

## Technical changes

- The old single file became ten files in one directory, in three commits. The rebuild `c0a0f52` cut `project-level/skill/SKILL.md` down to the picture of the whole, the section "Delegated definition change and gate" with its pointer, a new section "Rules that hold across the steps" (four rules several steps keep), step 0 and the pointer of each step, and added nine files beside it: `existing_definition.md` (the variant of step 0 for an existing definition), `idea.md`, `read_foundation.md`, `first_write.md`, `rounds.md`, `find_entries.md`, `technology.md`, the file of step 7 (items 7.1–7.5) and `delegated_mode.md` (the dispatched turn). The fix `eeca32c` answered the review: step 6 names the file of step 7 for a finding of the readiness check, "below" covers the files beside the skill, `delegated_mode.md` opens with a line saying whose variant it is, one line rewrapped. The return step `09b0dd0` renamed the file of step 7 from `gate.md` to `readiness_gate.md`. Nothing outside `project-level/skill/` changed; 10 files, +197 −132 over the range `2754675..09b0dd0`.
- Files after the change, in words: `SKILL.md` 570, `delegated_mode.md` 342, `existing_definition.md` 205, `idea.md` 82, `read_foundation.md` 109, `first_write.md` 98, `rounds.md` 240, `find_entries.md` 108, `technology.md` 66, `readiness_gate.md` 567.

## Checks

1. `python -B gate/run_tests.py` on the final tree `09b0dd0`: exit **0**, 804 tests in 9 directories, every directory passed; the target branch had not moved since the base, so this is the tree that merges. The base `2754675` gave exit 0, 804 tests in 9 directories, every directory passed, and the run on the reviewed fix `eeca32c` the same. Five tests were skipped on Windows in every run, so they are unchecked: four in `instruction-files/test_check_instructions.py` that need POSIX paths of links, and one that needs a FIFO (`test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`). No test failed and passed again.
2. The change touches only Markdown that no test reads, so no test was written; the author's and reviewers' focused checks (`gate/run_tests.py` for `project-level`, `agent-instructions` and `installation`, `foundation_check.py`, `skill_entry_points.py`, `check_instructions.py` on the ten files) exited 0.
3. Own-work check: the author named "every fragment stands where the step or variant that needs it names it" as the requirement most likely not met, and checked it with three scripts, each shown able to fail: every nonblank line of the old file in exactly one row of the assessment and each row's text in the file it names; every sentence of the old file against all ten files (121 units, 7 not word for word, each a named rewording); each file named at its step and the jumps between steps. The scripts did not catch the hand-back from the technology step to 7.1, which the review found; after the fix the pointer script checks it too.
4. Not checked: no agent has been sent through the rebuilt skill, so whether a dispatched turn reads only its own steps and keeps the dispatched rules through steps 0 to 6 is argued, not measured; question 5 of the task leaves that to the next real use in `loop2`.
5. The numbers: `verify_counts.py` recounts every figure of the word counts, the assessment and the reports (279 figures, 0 differ) and checks `wc -w` under both locales; `verify_request.py` recomputes with code of its own every file count, route sum, percentage, run sum, gate, stage and assessment figure and checks every number of this description against them and against the task's figures: exit 0, 0 numbers unmatched, after the last change to a counted file (a control copy with four wrong numbers gave exit 1, each named); counts of twelve or fewer, such as the number of list items, it leaves to the eye. The base file has 1937 words under a UTF-8 locale, the task's figure, and 1929 with `wc -w` in the C locale: the 8 words between them are standalone em dashes, which the C locale does not count.
6. The remarks check of the record: `python -B task-cycle/remarks_check.py .runs/task-cycles/define-project-skill-shape` listed once the line `verify_counts result: exit 0, 279 figures compared, 0 differ` of the return step's report as a search item; the cycle holds the listing wrong (the line is a check result appended after the section's one item, not an item) and named the case in the record's remarks; the last run on the original: exit 0, `checked: 6 reports, 16 items other than none, 0 not in the process remarks`. On the copy of the record: `python -B task-cycle/remarks_check.py docs/task-cycles/define-project-skill-shape`, exit 0 on every run, the same count. The check of private paths on the copy: `python -B task-cycle/private_paths_check.py docs/task-cycles/define-project-skill-shape`, first run exit 1 with 12 places listed (the worktree's absolute path in handoffs and scripts, the paths of the task's note and of the author's rules, a note link in the task copy), cleaned by one rewriting together with the names of private notes it does not list; every later run exit 0, `checked: 28 files, 0 listed`. The form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/define-project-skill-shape/request.md --task .runs/task-cycles/define-project-skill-shape/task.md`, exit 0. The check of private paths on it: `python -B task-cycle/private_paths_check.py .runs/task-cycles/define-project-skill-shape/request.md`, exit 0. The change touches no user interface, so screenshots do not apply.

## Foundation entries

none — the task carries no row of *Settlements to record* and no projected entry. The return step compared the twelve decisions in play, the five more the skill cites, six invariants, the part-map entry `project-level` and the glossary, with a search of the whole foundation, against the new files; its one correction was the file name `gate.md`, inside the change. No invariant test, surface or *Violated* mark changed.

## Minor findings

1. The three Minor findings of the review of the whole change were fixed with its blocking finding in the one fix. The review of the return step found one, not fixed; it concerns only the cycle's record, not the skill. In the reviewer's words: "`.runs/task-cycles/define-project-skill-shape/reports/fix_report.md:39-40, :58-77, :151-166`, and likewise `review_report.md`, `findings.md`, `review_fix_report.md`. These records name `gate.md` with no note that the file is now `readiness_gate.md` […] a passage carried from `fix_report.md` into it word for word would name a file that no longer exists. Nothing in the tree is affected." This description carries no passage naming the old file as current.

## Findings outside the task's scope

1. A note, not a finding, from the review of the fix, on text that stands unchanged from the old file: when step 0 checks an approved definition, it says where a mismatched fingerprint goes (step 7) but not where any other finding of that check goes; the old file said no more. In the reviewer's words: "giving step 0 a routing for such findings would be new content. Out of scope of the fix (outside its diff; fix.md); a note, not a finding." Place: `project-level/skill/existing_definition.md:8-12`.

## Assessment of the skill

The full table has 54 rows: each fragment of the old file quoted literally with its line range on `dfd50e5` (the file is identical on the cycle's base `2754675`), when an agent needs it, whether the agent recognises that moment, the verdict, its ground and its place after the rebuild. Every nonblank line of the old file stands in exactly one row. Verdicts: 15 keep and 39 move; none removed or reworded in the files. The reviewer compared every row with the place where its fragment stands. [The table and the proposals in full](https://github.com/mariusznazar/the-way/blob/4f508f8ca006ada60fa71ae79c445ef0589e5805/docs/task-cycles/define-project-skill-shape/reports/assessment.md).

The proposals, which change the content of a rule and were not applied (each is also an item of *For you to decide*):

1. **Remove the orchestrator's own-edit sentence from the dispatched turn's file** (`delegated_mode.md`, old lines 36–38: "The project orchestrator may make the initial text edit only when that full text is already before it and needs no other definition-section or foundation reading; otherwise it delegates the edit."). The orchestrator holds it in `project-level/lead/skill/SKILL.md:206-207` and in WAY-156; the dispatched agent does nothing by it. If left: 31 words in every dispatched turn and three wordings of one rule that can drift apart. If taken: 31 words fewer, at the price of a review of meaning; recommended in a change of its own.
2. **The other repetitions between the dispatched turn's file and `lead-project:202-219`** — five rows (the subagent performs step 7; observations come back through files; approval presented through the orchestrator; the pending state kept visible; the next action and the block on `ready for cycle`): keep each, since each side states its own half; the last could be reworded, not recommended now.
3. **The repetitions between the skill and the definition template** — ten rows (language; backlog; `TODO` until a step; Background, Success and Risks asked; no deadline; sections left open; no number for a new projected decision; the status line; the gate record approves every entry; a change after the gate goes through it again): keep each, as a pointer or as the template's rule applied where the step asks.
4. **"The gate" against the glossary**, which gives "gate" as the command that runs all of a product's tests: not recommended now, since WAY-118 and the template use the same words; the fix would change the foundation or the template.
5. **The path of the template**: write `project-level/definition_template.md` at `SKILL.md:13` and `:45` instead of the bare name, since every other file the skill names now lies beside it.
6. **"each skill named below" in `plan-project`, `maintain-styleguide`, `maintain-coding-guidelines` and `maintain-testing-guidelines`**: the same reword this skill got from the review's finding, outside this task.

## New sentences

Each sentence below is new or has a new condition; for each, the comparison with the old file and what it switches off (from the author's and the fix's reports, checked by the reviewers):

1. Step 0, `SKILL.md`: "When the human names an existing definition — in a dispatched turn, the definition its conversation file names — read `existing_definition.md` beside this skill." The old resume line stood in front of every reader; behind a pointer, a dispatched agent could read "the human named nothing" and skip the check of an approved definition. It switches off that reading and adds no route: a dispatched turn always works on a named definition.
2. `readiness_gate.md`, before 7.1: "In a turn dispatched through a refinement conversation path, `delegated_mode.md` beside this file changes this step: never speak to the human directly, request the critique of 7.3 through the conversation instead of running it, and write the fingerprint, the gate record and the `approved` status only after the human's approval is recorded through the project orchestrator." It switches off, in a dispatched turn only, three acts step 7 states without reservation; each limb stands in the old delegated section.
3. Rules, `SKILL.md`: "Once the definition is written (step 3), write each answer into it, with its status line, before the next question …" The old rule stood in step 4; the opening clause switches it off for steps 0 to 2 of a new definition, where no file exists yet.
4. Step 6, `SKILL.md`: "Where the readiness check reports a finding at this step, in the run `technology.md` gives or handed back by `settle-technology`, read `readiness_gate.md` beside this skill: the finding goes where its 7.1 sends it." And step 7: "Read `readiness_gate.md` beside this skill unless step 6 had you read it." In the old single file, 7.1 stood before every reader; the sentence restores the route the review found lost (I-1), and "unless step 6 had you read it" switches off a second reading.
5. `SKILL.md`: "cited below and in the files beside this skill" and "each skill named below or in the files beside this skill is the project skill of that name with the `the-way-` prefix" (review finding M-1): the files beside now hold most cited decisions and every named skill; it switches off reading "below" as the main file only.
6. `delegated_mode.md` opening: "The variant of the skill `define-project`, whose `SKILL.md` lies beside this file, for a turn that `lead-project` dispatches; "this same workflow" below is the steps that `SKILL.md` gives." (review finding M-2): orientation for a reader handed the file alone; no instruction. Every step file opens with a like line.
7. The name `readiness_gate.md` (return step): "gate" in the glossary is the one command that runs all tests.

## Word counts

The table of the top part, with the same figures. Counted as `wc -w` under a UTF-8 locale after the last change to a counted file, the state before on `dfd50e5` (identical on `2754675`). The skill's own text is the main file and the files beside it the route reads; "with the files beside" adds what question 4 of the task lists: the definition template in full, 3221 words (every route); the section "How a skill asks", 208 (every route); the section "Reading the foundation", 503 (route 1); and `project-level/lead/conversation_template.md`, 1419 (routes 3a and 3b). Route 3a counts the variant file of an existing definition, since a dispatched turn always works on a named definition; without it, 205 words fewer. The file of step 7 counts once on every route, read at step 6 where the readiness check reports a finding there, otherwise at step 7. Over the six recorded runs of the skill (one from an idea, four dispatched turns, one approved definition reopened): skill text 11622 → 9918 (−14.7%), with the files beside 38375 → 36671 (−4.4%), reading the dispatched turns as 3a; as 3b, 11622 → 12730 (+9.5%) and 38375 → 39483 (+2.9%). Against the task's estimates: the main file 570 fits 500–600, route 3a 1684 fits 1550–1750, route 4 1342 fits 1250–1400; route 1, 1840, falls outside 2350–2550, an estimate that matches none of the routes counted (every file, route 3b, gives 2387). [The counts in full](https://github.com/mariusznazar/the-way/blob/4f508f8ca006ada60fa71ae79c445ef0589e5805/docs/task-cycles/define-project-skill-shape/reports/word-counts.md).

## Course of the cycle

- **Task and sources:** an independent task, the eleventh of eleven in the series that rebuilds the skills of the-way; the document was accepted on 2026-11-06; the base is `foundations` `2754675c`, and the files this task changes or counts are identical to `dfd50e5`, the base the task names.
- **Process pin:** none — the session worked on the-way itself; no pin to move.
- **Spec:** none, because questions 1–4 and To do 1–2 of the task settle the split, the limits of the change and the routes counted; the names of the files and the wording of the pointers are a way of making what the task settles.
- **Route:** one author without a plan, on the same class of model as the orchestrator (Opus 5.5), because the change rewrites instruction text where a lost or reworded rule fails no test. The review of the whole change failed on one blocking finding, which one fix closed; the review of that fix and the review of the return step passed.
- **Plan:** none.
- **Choices:** 9 rows in the [table of questions and choices](https://github.com/mariusznazar/the-way/blob/4f508f8ca006ada60fa71ae79c445ef0589e5805/docs/task-cycles/define-project-skill-shape/cycle.md#questions-and-autonomous-choices).
- **Blocking findings left:** none.
- **Record:** [the record of the cycle](https://github.com/mariusznazar/the-way/blob/4f508f8ca006ada60fa71ae79c445ef0589e5805/docs/task-cycles/define-project-skill-shape/cycle.md), in a commit of its own that the next commit removes, so that the target tree holds only the change. The task's backlog entry was not changed; closing the series after the merge is outside this request.
