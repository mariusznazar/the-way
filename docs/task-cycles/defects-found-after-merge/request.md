**State: blocked** — waits for your actions outside the repository: two changes in your own tools that this request cannot make for you.

## What you will see

From now on the process keeps count of mistakes that reach you after the review, in two places that did not exist before.

First, every task document gets one more line in its header, `Defect introduced by:`, filled in by the agent that refines the task, not by the cycle. It reads `none` when the task is not a repair; otherwise it names the request, or the requests, that brought the mistake in, or `unknown` with the reason the origin cannot be found. A task counts as a repair only when it removes a mistake against what the earlier task or the foundation required at the merge, or a regression, meaning something that worked and that the earlier task did not ask to change. A new need, a change of mind, a gap in the earlier task and maintenance do not count. A task document written before this line has no such line, and that means "not assessed", never `none`.

Second, when you send remarks on an open request, the correction now writes down why it was needed, in one line of the cycle record. Each line holds pairs of a source and a kind. The source says where the correction came from: an answer to an item of your list of decisions, a remark of yours outside any item, or only a refresh of the target branch that you asked for. The kind is the cycle leader's judgment by one test: did the task or the foundation require what the correction changes (`defect`), or not (`not-required`); a refresh of the branch has no kind. Your remarks go word for word into a file beside the record, also when you gave them in conversation. The description of the corrected request shows these pairs in one sentence under "You accept by merging", so you see the cycle's judgment before you merge.

Two numbers can then be counted: mistakes that the review let through and you found (your remark, kind `defect`), and mistakes the cycle saw and left (an item, kind `defect`). The template of the register of problems gets two new classes for them, `defect-found-at-request` and `defect-found-after-merge`.

### Underneath

Five new decisions in the decision log hold the rules (what counts as a repair, where the mistake is recorded, where the cause of a correction is kept, the closed list of sources and kinds, and the register classes), and one existing decision, on what the section for your decisions holds, now also names the cause of a correction. Two tests keep the record readers unchanged by the new record item.

## For you to decide

### Needed from you

1. Add two classes to your own register of problems: `defect-found-at-request` (a mistake the review let through that you found before the merge, the pair `remark · defect`) and `defect-found-after-merge` (a mistake found by a repair task after the merge, from the line `Defect introduced by:`), each with today's date as the day it is added; the pair `item · defect` goes to the existing class `known-problem-left`. The register is your tool and lies outside every repository, so only you can do it. Without it the audit refuses rows of these classes, and the count of mistakes found after the merge cannot start; each new class date also starts a new series of measures, so the sooner the better.
2. Teach the nightly review of cycles to read the line `Defect introduced by:` from the frozen task document in a record, and the correction lines of the record, and to write register rows from them as the template says: for a row after the merge the record column is the last copy of the record of the cycle that brought the mistake in, and the stages column reads `after the merge`; for a row at the request the record column is the copy that carries the correction's line, and the stages column reads `at the request`. The nightly review is your own tool and lies outside the repository. Without it the new line and the new item sit in the records and nothing counts them.

### Fix or let through

3. One sentence of the new kind of item for corrections is left to the writer. When a correction is only a refresh of the target branch, the description still has to carry the one sentence with its pair `target-branch · none`, and the template does not say what to write there, so the agent writing the description improvises the sentence. Nothing breaks: you read one odd sentence in a description you merge anyway, and different requests may word it differently. Fixing it in this request costs another round of correction with a review, and adds a sentence or an example to the template. Making a task of it costs a line in the backlog and a later cycle. Letting it through costs nothing today, and the first refresh-only correction shows whether the improvised sentence bothers you. I recommend letting it through, since no reader depends on its wording. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 2.)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

4. The cycle chose three things the task did not fix. The human's remarks go to a file in the record's reports, named after the correction's number and the word remarks, the pattern earlier cycles of the game already use; a name with the word findings in it would be taken for a findings file by the check of process remarks. Several pairs in one line are separated by a comma and a space, because a pair already holds the dot-separator ` · `. The description after correction number n shows the pairs of that correction only, as the task says ("pary tej poprawki"), so after a second correction the first one's pairs are in the record and not in the description. The line for refinement stands in the common step of the refinement skill, which serves all three kinds of task, since no file of that skill lists the header lines of a task.
5. One existing decision, on what the section for your decisions holds, was edited in place: it now names the cause of a correction after the request opened. The task names this change, but its wording is the cycle's.

## Cost

Working time of the cycle's agents: 45 minutes 35 seconds, of which 23 minutes waiting for tools; one orchestrator session and one author, one reviewer, each resumed for the fix round. Model: Claude Sonnet 5.5 throughout; about 41.4 million tokens (40.2 million of them cached input, 158 thousand output). One round of fix with its review (for the Minor findings within the task). The gate ran twice, on the base and on the final tree, 20 minutes and 11 minutes in the background. The table of stages is in the committed record, linked under Record.

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record survives only when the commits are kept. The request is blocked until you have done the two actions above; the code itself can be merged once you agree, and the actions can be done at any time after it, but until then the new line and the new item are not counted. The foundation has waited for a review through 29 merges since its last tag; the next reminder comes at 30, and nothing here waits for it.

<details>
<summary>Po polsku</summary>

**Stan: zablokowana** — czeka na Twoje działania poza repozytorium: dwie zmiany w Twoich własnych narzędziach, których ta prośba nie może zrobić za Ciebie.

## Co zobaczysz

Od teraz proces liczy błędy, które przechodzą przez przegląd, w dwóch miejscach, których wcześniej nie było.

Po pierwsze, każdy dokument zadania dostaje w nagłówku jeszcze jedną linię, `Defect introduced by:`, którą wypełnia agent doprecyzowujący zadanie, nie cykl. Czyta `none`, gdy zadanie nie jest naprawcze; w przeciwnym razie podaje prośbę albo prośby, które wprowadziły błąd, albo `unknown` z powodem, dla którego nie da się ustalić pochodzenia. Zadanie jest naprawcze tylko wtedy, gdy usuwa wadę wobec tego, czego w chwili scalenia wymagało zadanie tamtej zmiany albo fundament, albo regresję, czyli zepsucie czegoś, co działało, a czego tamto zadanie nie kazało zmieniać. Nowa potrzeba, zmiana zdania, luka w tamtym zadaniu i konserwacja się nie liczą. Dokument zadania napisany przed tą linią jej nie ma, a to znaczy „nie oceniano”, nigdy `none`.

Po drugie, gdy odeślesz uwagi do otwartej prośby, poprawka zapisuje teraz w jednej linii zapisu cyklu, dlaczego była potrzebna. Linia mieści pary źródło i rodzaj. Źródło mówi, skąd poprawka przyszła: odpowiedź na pozycję Twojej listy decyzji, Twoja uwaga spoza pozycji albo samo odświeżenie gałęzi docelowej na Twoją prośbę. Rodzaj to osąd agenta prowadzącego cykl jednym testem: czy to, co poprawka zmienia, wymagało zadanie albo fundament (`defect`), czy nie (`not-required`); odświeżenie gałęzi rodzaju nie ma. Twoje uwagi trafiają słowo w słowo do pliku obok zapisu, także gdy podałeś je w rozmowie. Opis poprawionej prośby pokazuje te pary jednym zdaniem w grupie „Przyjmujesz przez scalenie”, więc przed scaleniem widzisz ocenę cyklu.

Z tego wychodzą dwie liczby: błędy, które przegląd przepuścił, a Ty je znalazłeś (Twoja uwaga, rodzaj `defect`), oraz błędy, które cykl widział i zostawił (pozycja, rodzaj `defect`). Szablon rejestru problemów dostaje na nie dwie nowe klasy, `defect-found-at-request` i `defect-found-after-merge`.

### Pod spodem

Pięć nowych decyzji w dzienniku decyzji trzyma reguły (co jest zadaniem naprawczym, gdzie zapisuje się błąd, gdzie leży przyczyna poprawki, zamknięta lista źródeł i rodzajów oraz klasy rejestru), a jedna istniejąca decyzja, o tym, co trzyma sekcja Twoich decyzji, nazywa teraz także przyczynę poprawki. Dwa testy pilnują, żeby nowa pozycja zapisu nie zmieniła tego, co czytają narzędzia czytające zapis.

## Do twojej decyzji

### Wymagane od Ciebie

1. Dodaj do własnego rejestru problemów dwie klasy: `defect-found-at-request` (błąd przepuszczony przez przegląd, który znalazłeś przed scaleniem, para `remark · defect`) i `defect-found-after-merge` (błąd znaleziony przez zadanie naprawcze po scaleniu, z linii `Defect introduced by:`), każdą z dzisiejszą datą jako dniem dodania; para `item · defect` idzie do istniejącej klasy `known-problem-left`. Rejestr jest Twoim narzędziem i leży poza każdym repozytorium, więc zrobisz to tylko Ty. Bez tego audyt odrzuci wiersze tych klas, a liczenie błędów znalezionych po scaleniu nie ruszy; data każdej nowej klasy zaczyna też nową serię miar, więc im wcześniej, tym lepiej.
2. Naucz nocny przegląd zapisów cykli czytać linię `Defect introduced by:` z zamrożonego dokumentu zadania w zapisie oraz linie poprawek w zapisie i pisać z nich wiersze rejestru tak, jak podaje szablon: dla wiersza po scaleniu kolumna *Record* to ostatnia kopia zapisu cyklu, który błąd wprowadził, a kolumna *Stages* czyta `after the merge`; dla wiersza przy prośbie kolumna *Record* to kopia niosąca linię poprawki, a *Stages* czyta `at the request`. Nocny przegląd jest Twoim narzędziem poza repozytorium. Bez tego nowa linia i nowa pozycja leżą w zapisach i nic ich nie liczy.

### Do poprawienia albo przepuszczenia

3. Jedno zdanie nowego rodzaju pozycji dla poprawek zostaje na głowie piszącego. Gdy poprawka jest tylko odświeżeniem gałęzi docelowej, opis i tak musi nieść jedno zdanie z parą `target-branch · none`, a szablon nie mówi, co tam napisać, więc agent piszący opis wymyśla to zdanie sam. Nic się nie psuje: czytasz jedno dziwne zdanie w opisie, który i tak scalasz, a różne prośby mogą je ująć różnie. Poprawka w tej prośbie kosztuje jeszcze jedną rundę z przeglądem i dopisanie zdania albo przykładu do szablonu. Zadanie kosztuje linię w backlogu i późniejszy cykl. Przepuszczenie nie kosztuje dziś nic, a pierwsza poprawka samego odświeżenia pokaże, czy wymyślone zdanie Ci przeszkadza. Polecam przepuścić, bo żadne narzędzie nie zależy od jego brzmienia. Poprawić w tej prośbie, zrobić z tego zadanie czy przepuścić? (Uwagi poza zakresem zadania, 2.)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

4. Cykl wybrał trzy rzeczy, których zadanie nie ustalało. Uwagi człowieka idą do pliku w raportach zapisu, nazwanego numerem poprawki i słowem „remarks”, według wzoru, którego używają już wcześniejsze cykle gry; nazwa ze słowem „findings” zostałaby wzięta przez sprawdzenie uwag procesowych za plik uwag recenzji. Kilka par w jednej linii rozdziela przecinek ze spacją, bo para sama zawiera separator ` · `. Opis po poprawce numer n pokazuje pary tylko tej poprawki, jak mówi zadanie („pary tej poprawki”), więc po drugiej poprawce pary pierwszej są w zapisie, a nie w opisie. Linia dla doprecyzowania stoi we wspólnym kroku skilla doprecyzowania, który obsługuje wszystkie trzy rodzaje zadań, bo żaden plik tego skilla nie wylicza linii nagłówka zadania.
5. Jedna istniejąca decyzja, o tym, co trzyma sekcja Twoich decyzji, została zmieniona na miejscu: nazywa teraz przyczynę poprawki po otwarciu prośby. Zadanie nazywa tę zmianę, ale jej brzmienie jest brzmieniem cyklu.

## Koszt

Czas pracy agentów cyklu: 45 minut 35 sekund, z czego 23 minuty to oczekiwanie na narzędzia; jedna sesja orkiestratora, jeden autor i jeden recenzent, każdy wznowiony do rundy poprawki. Model: Claude Sonnet 5.5 przez cały cykl; około 41,4 mln tokenów (40,2 mln z nich to wejście z pamięci podręcznej, 158 tys. wyjście). Jedna runda poprawki z przeglądem (dla uwag Minor w zakresie zadania). Bramka biegła dwa razy, na bazie i na końcowym drzewie, po 20 i 11 minut w tle. Tabela etapów jest w zatwierdzonym zapisie, do którego link stoi w sekcji Record.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase: link do zapisu przetrwa tylko przy zachowanych commitach. Prośba jest zablokowana, dopóki nie zrobisz dwóch akcji wyżej; sam kod można scalić po Twojej zgodzie, a akcje zrobić w dowolnym momencie potem, lecz do tego czasu nowa linia i nowa pozycja nie są liczone. Fundament czeka na przegląd po 29 scaleniach od ostatniego tagu; kolejne przypomnienie przyjdzie przy 30, a nic tutaj na nie nie czeka.

</details>

## Technical changes

- `4fcec13` — templates and skills: the line `Defect introduced by:` in the task document template (`project-level/task/template.md`) and its fill-in step (`project-level/task/skill/draft.md`); the record item for corrections and the file of remarks (`task-cycle/record_template.md`, `task-cycle/skill/correction.md`); kind 17 of the description's items and the correction row of its variants (`task-cycle/skill/request_template.md`); the two classes and the sentences for *Record* and *Stages* in `process-audit/problem_register.md`. The counting command is unchanged.
- `aea8c2c` — decisions WAY-353 to WAY-357 written in `foundations/decisions.md`; WAY-287 changed in place.
- `15b1041`, `10c0f9e` — two tests in `task-cycle/test_remarks_check.py` and one in `process-audit/test_audit_count.py` that keep the record readers unchanged by the new item and the new remarks file.
- `6d3298b` — the fix of three Minor findings of the review of the whole change: "keeps no line" and "has no line" instead of "keeps none" and "has none" (so no one reads the value `none`), "item 8 below" instead of "above", and the `TODO` sentence of the task template back on its own line.

## Checks

- The gate on the final tree: `python -B task-cycle/gate_times.py --output .runs/task-cycles/defects-found-after-merge/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1203 tests in 10 directories, every directory passed. On the base commit the same command exited 0 with 1200 tests: no check fails on the base, and none failed and passed again in the cycle. No check failed or did not run.
- Own-work check of the author: the form check on a description with item 17 alone in *You accept by merging* returned no problem, and the header reader of the task document read the new header with one `Project relation` and one `Defect introduced by` field (`python -B -X utf8 own_check.py`, exit 0). The nightly review of cycles lies outside the repository and was not run; no one could check it against the new item.
- Mutation check by the reviewer: the corrections item moved after the process remarks makes the template test fail, as intended.
- The state of user-interface screens: not applicable, the change touches no screen.
- The form check, the check of private paths, the image check and the remarks check on the copy of the record: to be filled in by the edit that adds the record's link.
- `python -B task-cycle/remarks_check.py .runs/task-cycles/defects-found-after-merge` on the original record: exit 0 after 2 runs (the first listed 10 items, which were then added to the process remarks).
- `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` for the cycle's session: both exit 0.

## Foundation entries

- WAY-353, `row 2` — A task fixes a defect found after a merge only when it removes a defect against what the earlier change's task or the foundation required at the merge, or a regression; a new need, a change of mind, a gap of the earlier task and maintenance do not count.
- WAY-354, `row 1`, `row 3`, `row 7`, `row 8` — A defect found after a merge is recorded in two places: the line `Defect introduced by:` in the header of every task document (the source, filled by the refining agent) and a register class that counts it; a document written before the line has none, which means not assessed.
- WAY-355, `row 4`, `row 9` — The cycle record holds one line per correction after the request opened, before the process remarks, never a cause in a commit title, and the human's remarks go word for word into a file in the record's reports.
- WAY-356, `row 5`, `row 10` — A correction's line gives each pair source · kind once: the source (`item <n>`, `remark`, `target-branch`) is read, the kind (`defect`, `not-required`, `none` only for `target-branch`) is the cycle leader's judgment by one test; the request shows the pairs in one sentence.
- WAY-357, `row 6`, `row 11` — The register template starts with two more classes, `defect-found-at-request` and `defect-found-after-merge`, sends `item · defect` to `known-problem-left`, and names the *Record* and *Stages* of the two new rows.
- WAY-287, `the cycle's` — The section for the human's decisions also holds the cause of a correction after the request opened.

No invariant test changed, no surface changed and no *Violated* mark was set or cleared.

## Minor findings

none

## Findings outside the task's scope

1. Minor. The word "kind" has two meanings in one rule: "the number of that item's kind in the template" (a kind of request item) and "the pair source · kind" (`defect`, `not-required`, `none`). The words come from the task's own answers (Polish "rodzaj" for both), and each use is explained at its place, so no reading is wrong today. Renaming one of the two is a decision of the human, offered as a separate matter, not a defect of this change. Place: `foundations/decisions.md` WAY-356 and the matching passages in `task-cycle/record_template.md` and `task-cycle/skill/correction.md` (reviewer: "the word 'kind' has two meanings in one rule").
2. Minor. Kind 17 gives the sentence its content but not the "why" or an alternative that an item of *You accept by merging* carries, and for `target-branch · none` it asks for a judgment ("whether the cycle judged that the task or the foundation required what the correction changed") that WAY-356 sets as `none`; a writer of the description must improvise the sentence for a refresh-only correction. Place: `task-cycle/skill/request_template.md:314-319`. This is item 3 above.

## Course of the cycle

- **Task and sources:** an independent task from the author's backlog, ready for cycle (settlements accepted 2026-11-12): a measure of mistakes found after the merge — the line `Defect introduced by:` in every task, the cause of each correction after a request opens, and two register classes. Sources: the answers of the task's *Questions to settle* and the eleven accepted rows of *Settlements to record*; the-way at `6814c6f`.
- **Process pin:** none; the-way itself, base `6814c6f6c9ff2b29d34612fa5cc86945ec3a2812` of `foundations`; the gate on the base exited 0 with 1200 tests.
- **Spec:** none written; no open design choice.
- **Route:** one author without a plan, class `same`, because the change crosses three parts and eleven rows must match the wording across them; review of the whole change by a fresh reviewer (`PASS`, three Minor findings within the task fixed, two outside it listed); review of the fix `PASS`; return step with nothing to correct.
- **Plan:** none on this route.
- **Choices:** 4 choices of the cycle beyond the questions answered by a binding source (the record's questions table, Q1 to Q4).
- **Blocking findings left:** none.
- **Record:** the record is committed after this description is written; its link by commit is added in the edit that follows.
