**State: ready** — corrected for your remarks: proposals 1, 5, 6 and proposal 4 inside the skill are applied; a set of new connecting sentences and one listing of a record check still wait for your yes below.

## What you will see

`define-project` is the skill that leads a project definition from an idea to its readiness gate. It was one file of 1937 words that every agent read whole, whichever way it used the skill: writing a definition from an idea, resuming one, a turn that `lead-project` dispatches to change a definition and take it through the readiness gate, or reopening an approved definition. After this change its main file has 572 words: the picture of the whole, four rules that hold at every step, step 0 and one line per step that names the file to read. The procedure of each step from 1 to 7 stands in a file of its own beside it, and so do the two variants: the resumed definition of step 0 and the dispatched turn. The steps keep their numbers 0 to 7 and 7.1 to 7.5, so every file and every dispatch that cites a step still points right.

After your remarks, four of the proposals are applied as well: the dispatched turn no longer carries the sentence on when the orchestrator may edit a definition itself; the main file names the definition template by its full path; the skill says "the readiness gate" wherever it means that gate, so the word no longer collides with the glossary's "gate", the command that runs all tests (the decision and the template keep their words); and five other skills of the-way now say that the prefix of a skill's name applies also to the skills their files beside them name.

What an agent reads of the skill, in words (counted as `wc -w` counts them under a UTF-8 locale, on the files before and after; "with the files beside" adds the definition template and the other files the route reads beside the skill):

| Use | Skill text before | Skill text after | Change | With the files beside, before | After | Change |
|---|---:|---:|---:|---:|---:|---:|
| 1. A definition from an idea, steps 0–7 | 1937 | 1844 | −4.8% | 5869 | 5776 | −1.6% |
| 2. Resumed while entries are found, steps 0, 5, 6, 7 | 1937 | 1522 | −21.4% | 5366 | 4951 | −7.7% |
| 3a. A dispatched turn reading its own steps | 1937 | 1662 | −14.2% | 6785 | 6510 | −4.1% |
| 3b. A dispatched turn reading every file | 1937 | 2365 | +22.1% | 6785 | 7213 | +6.3% |
| 4. An approved definition reopened, steps 0 and 7 | 1937 | 1348 | −30.4% | 5366 | 4777 | −11.0% |
| 5. No technology section, reopened, steps 0, 6, 7 | 1937 | 1414 | −27.0% | 5366 | 4843 | −9.7% |

The ten files together have 2365 words, 428 more than the old single file. These are word counts of files, not a measurement of how agents behave or of tokens; whether a dispatched turn reads only its own steps (3a) or everything (3b) shows at the next real use of the skill. Apart from the proposals you asked for, no rule disappeared and none changed meaning: each fragment of the old file now stands either in the main file or in the file of the step or variant that needs it. A handful of short sentences are new; they connect the files and are listed under *For you to decide*. The merge does not change the foundation, the definition template, the callers of the skill, any skill's description or any code.

### Underneath

The change applies the rule that a procedure which only one step or one variant of a skill needs stands in a file beside the skill that the step names, and that a variant file one step points to is named by the main file at that step too.

## For you to decide

1. The rebuild added a few short sentences that the old file did not hold, to keep the routes it had once the text stands in several files. Each is quoted, with what it switches off, under "New sentences" below: the resume line of step 0 also names a dispatched turn's definition; the file of step 7 opens with the three things a dispatched turn does differently there; the rule to write each answer into the definition before the next question now holds from the first write onward instead of only in the rounds; step 6 sends a finding of the readiness check to the file of step 7, which says where it goes (added after the review found that route lost); "named below" now also covers the files beside the skill; and the file of step 7 is named `readiness_gate.md`, not `gate.md`, because the glossary gives "gate" another meaning. Accept them? (New sentences.)
2. A check of the cycle's record listed, once, a line of a report as a search item the record did not hold; the line is a test result the author appended at the end of the report, not an item. The cycle did not copy it as an item; it named the case in the record's remarks, after which the check lists nothing. Merge as it stands? (Checks, 6.)

## Cost

About 74 minutes of working time in the turns of the orchestrator and of the agents, and 75,674,262 tokens in all, every one on Opus 5.5, across the one session of the cycle and its correction, as counted before this description was rewritten. Four code reviews ran: the review of the whole change, which failed on one blocking finding; the review of the one fix, which passed; the review of the return step, which passed; and the review of the correction for your remarks, which passed. [Table of stages](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/define-project-skill-shape/stages.md).

## How to merge

Merge keeping the commits, with no squash and no rebase: the links in this request lead to the commit that holds the record of the cycle, and they survive only then.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — poprawione według Twoich uwag: propozycje 1, 5, 6 i propozycja 4 w obrębie skilla są naniesione; zestaw nowych zdań łączących i jedno wskazanie sprawdzenia zapisu cyklu nadal czekają poniżej na Twoją zgodę.

### Co zobaczysz

`define-project` to skill, który prowadzi definicję projektu od pomysłu do bramki gotowości. Był jednym plikiem o 1937 słowach, który każdy agent czytał w całości, niezależnie od tego, jak skilla używał: pisząc definicję od pomysłu, wznawiając ją, w turze zleconej przez `lead-project` (zmiana definicji i bramka gotowości) albo otwierając ponownie zatwierdzoną definicję. Po tej zmianie jego plik główny ma 572 słowa: obraz całości, cztery reguły obowiązujące na każdym kroku, krok 0 i po jednym wierszu na krok, który wskazuje plik do przeczytania. Procedura każdego kroku od 1 do 7 stoi we własnym pliku obok, tak samo dwa warianty: wznowienie definicji w kroku 0 i tura zlecona. Kroki zachowują numery 0–7 i 7.1–7.5, więc każdy plik i każde zlecenie, które powołuje się na krok, dalej trafia we właściwe miejsce.

Po Twoich uwagach naniesione są też cztery propozycje: tura zlecona nie niesie już zdania o tym, kiedy orkiestrator może sam edytować definicję; plik główny podaje szablon definicji pełną ścieżką; skill mówi „the readiness gate” wszędzie, gdzie chodzi o tę bramkę, więc słowo nie zderza się już ze słownikowym „gate”, poleceniem uruchamiającym wszystkie testy (decyzja i szablon zachowują swoje słowa); a pięć innych skilli the way mówi teraz, że przedrostek w nazwie skilla obowiązuje też dla skilli wymienionych w plikach obok.

Co agent czyta ze skilla, w słowach (liczonych jak `wc -w` w locale UTF-8, na plikach przed zmianą i po niej; „z plikami obok” dolicza szablon definicji i pozostałe pliki, które droga czyta obok skilla):

| Użycie | Tekst skilla przed | Tekst skilla po | Zmiana | Z plikami obok, przed | Po | Zmiana |
|---|---:|---:|---:|---:|---:|---:|
| 1. Definicja od pomysłu, kroki 0–7 | 1937 | 1844 | −4.8% | 5869 | 5776 | −1.6% |
| 2. Wznowienie w trakcie szukania wpisów, kroki 0, 5, 6, 7 | 1937 | 1522 | −21.4% | 5366 | 4951 | −7.7% |
| 3a. Tura zlecona czytająca swoje kroki | 1937 | 1662 | −14.2% | 6785 | 6510 | −4.1% |
| 3b. Tura zlecona czytająca wszystkie pliki | 1937 | 2365 | +22.1% | 6785 | 7213 | +6.3% |
| 4. Zatwierdzona definicja otwarta ponownie, kroki 0 i 7 | 1937 | 1348 | −30.4% | 5366 | 4777 | −11.0% |
| 5. Bez sekcji technologii, otwarta ponownie, kroki 0, 6, 7 | 1937 | 1414 | −27.0% | 5366 | 4843 | −9.7% |

Dziesięć plików razem ma 2365 słów, o 428 więcej niż dawny pojedynczy plik. To liczby słów w plikach, nie pomiar zachowania agentów ani tokenów; czy tura zlecona czyta tylko swoje kroki (3a), czy wszystko (3b), pokaże następne prawdziwe użycie skilla. Poza propozycjami, o które prosiłeś, żadna reguła nie zniknęła i żadna nie zmieniła znaczenia: każdy fragment dawnego pliku stoi teraz w pliku głównym albo w pliku kroku lub wariantu, który go potrzebuje. Kilka krótkich zdań jest nowych; łączą pliki i są wymienione w „Do rozstrzygnięcia”. Scalenie nie zmienia fundamentu, szablonu definicji, wołających skilla, opisu żadnego skilla ani żadnego kodu.

#### Pod spodem

Zmiana stosuje regułę, że procedura potrzebna tylko jednemu krokowi albo jednemu wariantowi skilla stoi w pliku obok skilla, który ten krok wymienia, a plik wariantu, do którego odsyła plik kroku, plik główny też wymienia przy tym kroku.

### Do rozstrzygnięcia

1. Przebudowa dodała kilka krótkich zdań, których dawny plik nie miał, żeby zachować jego drogi, gdy tekst stoi w kilku plikach. Każde jest zacytowane, razem z tym, co wyłącza, niżej w „New sentences”: wiersz wznowienia w kroku 0 wymienia też definicję tury zleconej; plik kroku 7 zaczyna się od trzech rzeczy, które tura zlecona robi tam inaczej; reguła wpisywania każdej odpowiedzi do definicji przed następnym pytaniem obowiązuje od pierwszego zapisu, a nie tylko w rundach; krok 6 odsyła znalezisko sprawdzenia gotowości do pliku kroku 7, który mówi, dokąd ono idzie (dodane po tym, jak przegląd znalazł tę drogę zgubioną); „named below” obejmuje też pliki obok skilla; a plik kroku 7 nazywa się `readiness_gate.md`, nie `gate.md`, bo słownik daje słowu „gate” inne znaczenie. Przyjąć? (New sentences.)
2. Sprawdzenie zapisu cyklu raz wskazało wiersz raportu jako pozycję poszukiwań, której zapis nie zawierał; ten wiersz to wynik testu, który autor dopisał na końcu raportu, a nie pozycja. Cykl nie przepisał go jako pozycji; nazwał przypadek w uwagach zapisu, po czym sprawdzenie nic nie wskazuje. Scalić tak, jak jest? (Checks, 6.)

### Koszt

Około 74 minut czasu pracy w turach orkiestratora i agentów oraz 75 674 262 tokeny łącznie, wszystkie na Opusie 5.5, w jednej sesji cyklu i jego poprawki, liczone przed przepisaniem tego opisu. Odbyły się cztery przeglądy kodu: przegląd całej zmiany, który nie przeszedł z powodu jednego blokującego ustalenia; przegląd jednej poprawki, który przeszedł; przegląd kroku zwrotnego, który przeszedł; i przegląd poprawki według Twoich uwag, który przeszedł. [Tabela etapów](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/define-project-skill-shape/stages.md).

### Jak scalić

Scal z zachowaniem commitów, bez squasha i bez rebase: linki w tym requeście prowadzą do commita z zapisem cyklu i przetrwają tylko wtedy.

</details>

## Technical changes

- The old single file became ten files in one directory. The rebuild `c0a0f52` cut `project-level/skill/SKILL.md` down to the picture of the whole, the section "Delegated definition change and gate" with its pointer, a new section "Rules that hold across the steps" (four rules several steps keep), step 0 and the pointer of each step, and added nine files beside it: `existing_definition.md` (the variant of step 0 for an existing definition), `idea.md`, `read_foundation.md`, `first_write.md`, `rounds.md`, `find_entries.md`, `technology.md`, the file of step 7 (items 7.1–7.5) and `delegated_mode.md` (the dispatched turn). The fix `eeca32c` answered the review: step 6 names the file of step 7 for a finding of the readiness check, "below" covers the files beside the skill, `delegated_mode.md` opens with a line saying whose variant it is, one line rewrapped. The return step `09b0dd0` renamed the file of step 7 from `gate.md` to `readiness_gate.md`.
- The correction `3f25d61`, for your remarks, applied proposals 1, 5 and 6 and proposal 4 inside the skill: the orchestrator's own-edit sentence removed from `delegated_mode.md`; `project-level/definition_template.md` by its full path at `SKILL.md:13` and `:45`; "the readiness gate" at eight places in `SKILL.md`, `delegated_mode.md`, `existing_definition.md` and `readiness_gate.md`, the fixed names kept (the heading "Delegated definition change and gate", "gate record", the status `ready for gate`); and "each skill named below or in the files beside this skill" in `elements/common/skill/SKILL.md`, `product-guidelines/coding/SKILL.md`, `product-guidelines/styleguide/SKILL.md`, `product-guidelines/testing/SKILL.md` and `project-level/plan/skill/SKILL.md`. `task-cycle/plan/SKILL.md` keeps "each skill named below": its one file beside it names no skill. Over the range `2754675..3f25d61`: 15 files, +212 −147.
- Files of the skill after the change, in words: `SKILL.md` 572, `delegated_mode.md` 314, `existing_definition.md` 207, `idea.md` 82, `read_foundation.md` 109, `first_write.md` 98, `rounds.md` 240, `find_entries.md` 108, `technology.md` 66, `readiness_gate.md` 569.

## Checks

1. `python -B gate/run_tests.py` on the final tree `3f25d61`: exit **0**, 804 tests in 9 directories, every directory passed; the target branch had not moved since the base, so this is the tree that merges. The base `2754675` gave exit 0, 804 tests, and so did the runs on `eeca32c` and `09b0dd0`. Five tests were skipped on Windows in every run, so they are unchecked: four in `instruction-files/test_check_instructions.py` that need POSIX paths of links, and one that needs a FIFO (`test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`). No test failed and passed again.
2. The change touches only Markdown that no test reads, so no test was written; the author's and reviewers' focused checks (`gate/run_tests.py` for `project-level`, `elements/common`, `agent-instructions` and `installation`, `foundation_check.py`, `skill_entry_points.py`, `check_instructions.py` on the changed files) exited 0. The author's call of `gate/run_tests.py product-guidelines` in the correction exited 1 with "no test found", the same on the commit before it: that directory holds no test, so it is no failing test.
3. Own-work check: the author named "every fragment stands where the step or variant that needs it names it" as the requirement most likely not met, and checked it with three scripts, each shown able to fail: every nonblank line of the old file in exactly one row of the assessment and each row's text in the file it names; every sentence of the old file against all ten files (121 units, 7 not word for word, each a named rewording); each file named at its step and the jumps between steps. The scripts did not catch the hand-back from the technology step to 7.1, which the review found; after the fix the pointer script checks it too. For the correction, a fourth script confirms that each changed file differs from its parent only by the substitutions the remarks ask for.
4. Not checked: no agent has been sent through the rebuilt skill, so whether a dispatched turn reads only its own steps and keeps the dispatched rules through steps 0 to 6 is argued, not measured; question 5 of the task leaves that to the next real use in `loop2`.
5. The numbers: `verify_counts.py` recounts every figure of the word counts, the assessment and the reports (263 figures, 0 differ, after the correction) and checks `wc -w` under both locales; `verify_request.py` recomputes with code of its own every file count, route sum, percentage, run sum, gate, stage and assessment figure and checks every number of this description against them and against the task's figures: exit 0, 0 numbers unmatched, after the last change to a counted file (a control copy with four wrong numbers gave exit 1, each named); counts of twelve or fewer, such as the number of list items, it leaves to the eye. The base file has 1937 words under a UTF-8 locale, the task's figure, and 1929 with `wc -w` in the C locale: the 8 words between them are standalone em dashes, which the C locale does not count.
6. The remarks check of the record: `python -B task-cycle/remarks_check.py .runs/task-cycles/define-project-skill-shape` listed once the line `verify_counts result: exit 0, 279 figures compared, 0 differ` of the return step's report as a search item; the cycle holds the listing wrong (the line is a check result appended after the section's one item, not an item) and named the case in the record's remarks; the last run on the original: REMARKS_ORIG. On the copy of the record: REMARKS_COPY. The check of private paths on the copy: PRIVATE_COPY. The form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/define-project-skill-shape/request.md --task .runs/task-cycles/define-project-skill-shape/task.md`, exit 0. The check of private paths on it: `python -B task-cycle/private_paths_check.py .runs/task-cycles/define-project-skill-shape/request.md`, exit 0. The change touches no user interface, so screenshots do not apply.

## Foundation entries

none — the task carries no row of *Settlements to record* and no projected entry. The return step compared the twelve decisions in play, the five more the skill cites, six invariants, the part-map entry `project-level` and the glossary, with a search of the whole foundation, against the new files; its one correction was the file name `gate.md`, inside the change. The correction for your remarks writes and corrects no entry: the sentence it removes stays in WAY-156 and in `lead-project`, and WAY-118, the definition template and the glossary keep their words. No invariant test, surface or *Violated* mark changed.

## Minor findings

1. The three Minor findings of the review of the whole change were fixed with its blocking finding in the one fix. The review of the return step found one, not fixed; it concerns only the cycle's record, not the skill. In the reviewer's words: "`.runs/task-cycles/define-project-skill-shape/reports/fix_report.md:39-40, :58-77, :151-166`, and likewise `review_report.md`, `findings.md`, `review_fix_report.md`. These records name `gate.md` with no note that the file is now `readiness_gate.md` […] a passage carried from `fix_report.md` into it word for word would name a file that no longer exists. Nothing in the tree is affected." This description carries no passage naming the old file as current.
2. The review of the correction found one, not fixed; it concerns only the cycle's record. In the reviewer's words: "`assessment.md` section 4, proposals 4 and 5 (record file, not code). Each keeps its old reasoning for not applying ("Verdict: not recommended in this change", "Proposed rather than applied because the series keeps the rebuild to a change of place") and then adds "Applied (correction 1)". The "Applied" line resolves it, and the section's opening paragraph names the correction, but a reader skimming the bullets meets two answers. This is a record of the cycle, not a file of the-way; it blocks nothing."

## Findings outside the task's scope

1. A note, not a finding, from the review of the fix, on text that stands unchanged from the old file: when step 0 checks an approved definition, it says where a mismatched fingerprint goes (step 7) but not where any other finding of that check goes; the old file said no more. In the reviewer's words: "giving step 0 a routing for such findings would be new content. Out of scope of the fix (outside its diff; fix.md); a note, not a finding." Place: `project-level/skill/existing_definition.md:8-12`.

## Assessment of the skill

The full table has 54 rows: each fragment of the old file quoted literally with its line range on `dfd50e5` (the file is identical on the cycle's base `2754675`), when an agent needs it, whether the agent recognises that moment, the verdict, its ground and its place after the rebuild. Every nonblank line of the old file stands in exactly one row. Verdicts: 15 keep and 39 move; none removed or reworded by the rebuild itself. The reviewer compared every row with the place where its fragment stands. [The table and the proposals in full](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/define-project-skill-shape/reports/assessment.md).

The proposals that would change the content of a rule, and what became of them after your remarks:

1. **Remove the orchestrator's own-edit sentence from the dispatched turn's file** (old lines 36–38: "The project orchestrator may make the initial text edit only when that full text is already before it and needs no other definition-section or foundation reading; otherwise it delegates the edit."). The orchestrator holds it in `project-level/lead/skill/SKILL.md:206-207` and in WAY-156; the dispatched agent did nothing by it. Applied: 31 words fewer in every dispatched turn.
2. **The other repetitions between the dispatched turn's file and `lead-project:202-219`** — five rows (the subagent performs step 7; observations come back through files; approval presented through the orchestrator; the pending state kept visible; the next action and the block on `ready for cycle`): verdict keep, since each side states its own half; unchanged.
3. **The repetitions between the skill and the definition template** — ten rows (language; backlog; `TODO` until a step; Background, Success and Risks asked; no deadline; sections left open; no number for a new projected decision; the status line; the gate record approves every entry; a change after the readiness gate goes through it again): verdict keep, as a pointer or as the template's rule applied where the step asks; unchanged.
4. **"The gate" against the glossary**, which gives "gate" as the command that runs all of a product's tests: applied inside the skill only, "the readiness gate" at eight places; WAY-118, the definition template and the glossary keep "the gate", so the skill's words now differ from theirs.
5. **The path of the template**: applied, `project-level/definition_template.md` at `SKILL.md:13` and `:45`.
6. **"each skill named below"** in the other rebuilt skills: applied in five skills; `task-cycle/plan/SKILL.md` left, since its one file beside it names no skill.

## New sentences

Each sentence below is new or has a new condition; for each, the comparison with the old file and what it switches off (from the author's and the fix's reports, checked by the reviewers). The correction's changes are under "Technical changes" and "Assessment of the skill".

1. Step 0, `SKILL.md`: "When the human names an existing definition — in a dispatched turn, the definition its conversation file names — read `existing_definition.md` beside this skill." The old resume line stood in front of every reader; behind a pointer, a dispatched agent could read "the human named nothing" and skip the check of an approved definition. It switches off that reading and adds no route: a dispatched turn always works on a named definition.
2. `readiness_gate.md`, before 7.1: "In a turn dispatched through a refinement conversation path, `delegated_mode.md` beside this file changes this step: never speak to the human directly, request the critique of 7.3 through the conversation instead of running it, and write the fingerprint, the gate record and the `approved` status only after the human's approval is recorded through the project orchestrator." It switches off, in a dispatched turn only, three acts step 7 states without reservation; each limb stands in the old delegated section.
3. Rules, `SKILL.md`: "Once the definition is written (step 3), write each answer into it, with its status line, before the next question …" The old rule stood in step 4; the opening clause switches it off for steps 0 to 2 of a new definition, where no file exists yet.
4. Step 6, `SKILL.md`: "Where the readiness check reports a finding at this step, in the run `technology.md` gives or handed back by `settle-technology`, read `readiness_gate.md` beside this skill: the finding goes where its 7.1 sends it." And step 7: "Read `readiness_gate.md` beside this skill unless step 6 had you read it." In the old single file, 7.1 stood before every reader; the sentence restores the route the review found lost, and "unless step 6 had you read it" switches off a second reading.
5. `SKILL.md`: "cited below and in the files beside this skill" and "each skill named below or in the files beside this skill is the project skill of that name with the `the-way-` prefix" (a review finding): the files beside now hold most cited decisions and every named skill; it switches off reading "below" as the main file only.
6. `delegated_mode.md` opening: "The variant of the skill `define-project`, whose `SKILL.md` lies beside this file, for a turn that `lead-project` dispatches; "this same workflow" below is the steps that `SKILL.md` gives." (a review finding): orientation for a reader handed the file alone; no instruction. Every step file opens with a like line.
7. The name `readiness_gate.md` (return step): "gate" in the glossary is the one command that runs all tests.

## Word counts

The table of the top part, with the same figures. Counted as `wc -w` under a UTF-8 locale after the last change to a counted file, the state before on `dfd50e5` (identical on `2754675`). The skill's own text is the main file and the files beside it the route reads; "with the files beside" adds what question 4 of the task lists: the definition template in full, 3221 words (every route); the section "How a skill asks", 208 (every route); the section "Reading the foundation", 503 (route 1); and `project-level/lead/conversation_template.md`, 1419 (routes 3a and 3b). Route 3a counts the variant file of an existing definition, since a dispatched turn always works on a named definition; without it, 207 words fewer. The file of step 7 counts once on every route, read at step 6 where the readiness check reports a finding there, otherwise at step 7. Over the six recorded runs of the skill (one from an idea, four dispatched turns, one approved definition reopened): skill text 11622 → 9840 (−15.3%), with the files beside 38375 → 36593 (−4.6%), reading the dispatched turns as 3a; as 3b, 11622 → 12652 (+8.9%) and 38375 → 39405 (+2.7%). Against the task's estimates: the main file 572 fits 500–600, route 3a 1662 fits 1550–1750, route 4 1348 fits 1250–1400; route 1, 1844, falls outside 2350–2550, an estimate that matches none of the routes counted (every file, route 3b, gives 2365). [The counts in full](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/define-project-skill-shape/reports/word-counts.md).

## Course of the cycle

- **Task and sources:** an independent task, the eleventh of eleven in the series that rebuilds the skills of the-way; the document was accepted on 2026-11-06; the base is `foundations` `2754675c`, and the files this task changes or counts are identical to `dfd50e5`, the base the task names.
- **Process pin:** none — the session worked on the-way itself; no pin to move.
- **Spec:** none, because questions 1–4 and To do 1–2 of the task settle the split, the limits of the change and the routes counted; the names of the files and the wording of the pointers are a way of making what the task settles.
- **Route:** one author without a plan, on the same class of model as the orchestrator (Opus 5.5), because the change rewrites instruction text where a lost or reworded rule fails no test. The review of the whole change failed on one blocking finding, which one fix closed; the review of that fix and the review of the return step passed. Correction 1, for your remarks given in the conversation on 2026-11-08 ([the remarks](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/define-project-skill-shape/reports/remarks.md)), ran from the reset base `a0c56bb`, made `3f25d61` and passed its review; it touched no foundation entry, so the return step was not repeated.
- **Plan:** none.
- **Choices:** 11 rows in the [table of questions and choices](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/define-project-skill-shape/cycle.md#questions-and-autonomous-choices).
- **Blocking findings left:** none.
- **Record:** [the record of the cycle](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/define-project-skill-shape/cycle.md), in a commit of its own that the next commit removes, so that the target tree holds only the change; the record committed before the correction stands in `4f508f8`. The task's backlog entry was not changed; closing the series after the merge is outside this request.
