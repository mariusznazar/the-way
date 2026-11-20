**State: draft** — corrected for your answers to two items; the result of the tests on the last head is added when the run ends, and one item below (1) asks whether to make a task of three small findings

## What you will see

The check of the foundation now stops a change that adds a decision, or alters the binding sentences of one, when a paragraph of those sentences has more than three sentences or more than 300 words. The error names the decision, the paragraph and the measure that is over, with its value. Every other decision over the limit is only listed, and the list stops nothing, so the twelve entries of the-way that are over the limit today stay as they are until the task you parked for them. A change that only divides a decision's sentences into paragraphs differently, with no word changed, counts as altering it, so joining two paragraphs into one over the limit is caught.

- The rule you chose is written where the process keeps it: the rule for how a decision is written now has the limit of 300 words beside the limit of three sentences, says that the check reports an excess as an error in an added or altered decision and only lists it in any other, and carries the reasons and the ways you did not choose.
- The template of a decision gives both limits where it gives the shape of an entry, and says that the check counts them in every decision a change adds or alters, so an older entry over the limit meets the rule when a change next alters it.
- The description of what the check reports is updated in the three other places that give it: the head of the check's script, the guide to working on the-way, and the readme.
- The check's script grew past the size the process allows for a script file, so the code that reads an entry's text moved into a new module with no change of behaviour.
- After your answers: the guidance for the shared modules of the process's code now names the directory where the check and its new module stand, so an agent that changes a shared module there is handed it. A fresh reviewer also read the six decisions that the first review had read only in part, whole, against the new rule and the check, and found no collision with the limits.

### Underneath

One script with its tests and a new module beside it, the decision template, two readmes, one rule of the decision log, one sentence of the map of the parts and one line of the guidance for shared modules; no product is touched.

## For you to decide

### Needed from you

none

### Fix or let through

1. The review of the correction found three small things outside this task. (a) The rule for how a decision is written gives the paragraph rule for "a part of another question", while the rule on numbering decisions calls the same thing a part of "the question the entry answers" and gives it one sentence, not a paragraph; with the new error, a reviewer has only these two wordings to decide whether a part earns a paragraph of its own, and the task that shortens the long entries meets it at once. (b) The rule on which material to read names its own first paragraph by its place, and that paragraph has to be cut or divided when it is next changed, so the pointer can go stale with no check noticing. (c) The decision that designates the exemplar of shared modules names one part in its scope, while the guidance now applies to four, so an agent that finds decisions by scope does not find it. Nothing breaks today and each costs one change of an approved entry, which is yours to approve. Making a task of them costs a later session each or together; undoing it, nothing. Letting them through leaves (a) to the reviewer's judgment for as long as it stands. I recommend making a task of (b) and (c) and settling (a) in this request, since your later comment on this request already asks that the rule for a paragraph of the entry's own question be written and the numbering rule changed with it; (a) is then closed by that correction. Its weak point: (b) and (c) are only hazards, and a task of each may cost more than the next change that meets them. Make a task of them, or let them through? (Findings outside the task's scope, 1–3)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The script file was at 1141 lines, and the new check would have taken it to about 1206, over the 1200 that the process allows a script file. The cycle moved the code that reads an entry's text into a new module, as the first commit that changes code, and left the other scripts that import those names as they are, since the old file still passes them on. The other ways were to squeeze the new check into the 59 lines left, which leaves no room for the next check, and to move a different part of the file, which is a less coherent part. If this reading is wrong, the cost is that a reader looking for those functions in the old file finds an import, and moving the block back undoes it.
3. The reasons for the ways not chosen are written into the rule without the counts you quoted when you chose (how many old entries would need rework, one entry in ten, 478 words in one entry), because the same rule keeps counts of entries out of its prose, and a figure like 478 becomes false the day the long entries are shortened. Each reason is kept without the figure. The other way is to write the figures in, which breaks that rule.
4. Two entries carry text you did not see in the task, so they are marked as the cycle's own. The rule for how a decision is written has one sentence of reason that no row gave: a limit in words beside the limit in sentences keeps a paragraph short when its sentences are joined to fit under the count, which is the reason the task gives for choosing both limits. The map of the parts now names the new module in the sentence about the part that holds the foundation check. (Foundation entries)
5. Twelve new tests hold what the rule says about the check, each by a line that cites the rule and the start of one of its two new sentences; the check accepts each line. No invariant's sentence was corrected, no invariant test was changed and no surface of the process changed: the command that checks the foundation keeps its path, its argument and its exit codes. (Foundation entries)
6. This correction answered your two answers to items of this request, and the cycle judged that the task did not require what they changed: the line of guidance for shared modules and the reading of six decisions are the cycle's work at your request, and nothing you accepted before changed. One of your remarks took the numbering rule to give a rule of a paragraph, which it does not; the reviewer read it as asked and reported the difference as item 1(a).

## Cost

About 1 hour 15 minutes of work across the session so far (the orchestrator, one author on Sonnet 5.5 in six turns and three reviewers' turns on Fable 5.2), 57.1 million tokens in all, of which 19.8 million on Fable 5.2; two review rounds with one fix (one blocking finding and four Minor ones, all fixed, passed) and one correction with its review (passed). The table of stages is in the record: CORRECTION_STAGES_URL.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation has waited for a review through 25 merges since the tag of the last review, with the threshold at 60, so no reminder is due.

<details>
<summary>W Twoim języku</summary>

**Stan: wersja robocza** — poprawiony po Twoich odpowiedziach na dwie pozycje; wynik testów na ostatnim commicie dopiszę, gdy przebieg się skończy, a jedna pozycja poniżej (1) pyta, czy zrobić zadanie z trzech drobnych uwag

## Co zobaczysz

Sprawdzenie fundamentu zatrzymuje teraz zmianę, która dodaje decyzję albo zmienia jej zdania wiążące, gdy akapit tych zdań ma więcej niż trzy zdania albo więcej niż 300 słów. Błąd nazywa decyzję, akapit i przekroczoną miarę z jej wartością. Każdą inną decyzję ponad limit sprawdzenie tylko wypisuje, a lista niczego nie zatrzymuje, więc dwanaście wpisów the way, które dziś stoją ponad limitem, zostaje, jak jest, do zadania, które dla nich zaparkowałeś. Zmiana, która tylko dzieli zdania decyzji na akapity inaczej, bez zmiany słów, liczy się jako zmiana decyzji, więc sklejenie dwóch akapitów w jeden ponad limit zostaje złapane.

- Wybrana przez Ciebie reguła stoi tam, gdzie proces ją trzyma: reguła o tym, jak pisze się decyzję, ma teraz limit 300 słów obok limitu trzech zdań, mówi, że sprawdzenie zgłasza przekroczenie jako błąd w decyzji dodanej albo zmienionej, a w każdej innej tylko je wypisuje, i niesie powody oraz warianty, których nie wybrałeś.
- Szablon decyzji podaje oba limity tam, gdzie podaje kształt wpisu, i mówi, że sprawdzenie liczy je w każdej decyzji, którą zmiana dodaje albo zmienia, więc starszy wpis ponad limitem spotka tę regułę, gdy zmiana następnym razem go zmieni.
- Opis tego, co zgłasza sprawdzenie, jest uzupełniony w trzech innych miejscach, które go podają: na początku skryptu sprawdzającego, w przewodniku po pracy nad the way i w readme.
- Skrypt sprawdzający urósł ponad rozmiar, który proces dopuszcza dla pliku skryptu, więc kod czytający tekst wpisu przeniesiono do nowego modułu bez zmiany działania.
- Po Twoich odpowiedziach: wytyczne dla modułów współdzielonych w kodzie procesu nazywają teraz katalog, w którym stoją sprawdzenie i jego nowy moduł, więc agent zmieniający tam moduł współdzielony je dostaje. Nowy recenzent przeczytał też w całości sześć decyzji, które pierwszy przegląd przeczytał tylko w części, pod kątem nowej reguły i sprawdzenia, i nie znalazł kolizji z limitami.

### Pod spodem

Jeden skrypt z testami i nowy moduł obok niego, szablon decyzji, dwa readme, jedna reguła dziennika decyzji, jedno zdanie mapy części i jedna linia wytycznych dla modułów współdzielonych; żaden produkt nie jest ruszony.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Przegląd poprawki znalazł trzy drobiazgi poza tym zadaniem. (a) Reguła o tym, jak pisze się decyzję, daje regułę akapitu dla „części innego pytania”, a reguła o numerowaniu decyzji nazywa to samo częścią „pytania, na które odpowiada wpis” i daje jej jedno zdanie, nie akapit; przy nowym błędzie recenzent ma tylko te dwa sformułowania, żeby rozstrzygnąć, czy część zasługuje na własny akapit, a zadanie skracające długie wpisy trafia na to od razu. (b) Reguła o tym, jaki materiał czytać, nazywa swój pierwszy akapit po jego położeniu, a ten akapit trzeba skrócić albo podzielić przy najbliższej zmianie, więc odwołanie może stać się nieaktualne bez żadnego sprawdzenia. (c) Decyzja wskazująca wzorzec modułów współdzielonych wymienia w zakresie jedną część, a wytyczne dotyczą już czterech, więc agent szukający decyzji po zakresie jej nie znajdzie. Dziś nic się nie psuje, a każdy z drobiazgów kosztuje zmianę zatwierdzonego wpisu, którą Ty zatwierdzasz. Zadanie z nich kosztuje późniejszą sesję na każdy albo na wszystkie; cofnięcie nic. Przepuszczenie zostawia (a) ocenie recenzenta, dopóki stoi. Rekomenduję zadanie z (b) i (c), a (a) rozstrzygnąć w tym requeście, bo Twój późniejszy komentarz do tego requestu już prosi o zapisanie reguły akapitu dla części własnego pytania wpisu i zmianę reguły numerowania razem z nią; (a) zamyka wtedy ta korekta. Słaby punkt: (b) i (c) to tylko zagrożenia, a zadanie na każde może kosztować więcej niż najbliższa zmiana, która na nie trafi. Zrobić z nich zadanie czy przepuścić? (Findings outside the task's scope, 1–3)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Plik skryptu miał 1141 linii, a nowa kontrola zaniosłaby go do ok. 1206, ponad 1200, które proces dopuszcza dla pliku skryptu. Cykl przeniósł kod czytający tekst wpisu do nowego modułu jako pierwszy commit zmieniający kod i zostawił inne skrypty, które importują te nazwy, bez zmian, bo stary plik nadal je przekazuje. Inne sposoby to wciśnięcie nowej kontroli w 59 pozostałych linii, co nie zostawia miejsca na następną, i przeniesienie innej części pliku, która jest mniej spójna. Jeśli to czytanie jest błędne, koszt to taki, że kto szuka tych funkcji w starym pliku, znajdzie import; przeniesienie bloku z powrotem to cofa.
3. Powody dla niewybranych wariantów są zapisane w regule bez liczb, które podałeś przy wyborze (ile starych wpisów wymagałoby przeróbki, co dziesiąty wpis, 478 słów w jednym wpisie), bo ta sama reguła nie wpuszcza do swojej prozy liczb wpisów, a liczba 478 staje się fałszywa w dniu skrócenia długich wpisów. Każdy powód zostaje bez liczby. Inny sposób to wpisanie liczb, co łamie tę regułę.
4. Dwa wpisy niosą tekst, którego nie widziałeś w zadaniu, więc są oznaczone jako własne cyklu. Reguła o tym, jak pisze się decyzję, ma jedno zdanie powodu, którego nie dał żaden wiersz: limit w słowach obok limitu w zdaniach pilnuje, żeby akapit nie rósł, gdy zdania sklejono, by zmieścić się w liczbie, czyli powód, który podaje zadanie, wybierając oba limity. Mapa części nazywa teraz nowy moduł w zdaniu o części, która trzyma sprawdzenie fundamentu. (Foundation entries)
5. Dwanaście nowych testów trzyma to, co reguła mówi o sprawdzeniu, każdy linią, która cytuje regułę i początek jednego z jej dwóch nowych zdań; sprawdzenie przyjmuje każdą linię. Zdanie żadnego niezmiennika nie zostało poprawione, żaden test niezmiennika się nie zmienił i żadna powierzchnia procesu się nie zmieniła: polecenie sprawdzające fundament zachowuje ścieżkę, argument i kody wyjścia. (Foundation entries)
6. Ta poprawka odpowiedziała na Twoje dwie odpowiedzi na pozycje tego requestu, a cykl uznał, że zadanie nie wymagało tego, co zmieniły: linia wytycznych dla modułów współdzielonych i przeczytanie sześciu decyzji to praca cyklu na Twoją prośbę, a nic z tego, co przyjąłeś wcześniej, się nie zmieniło. Jedna z Twoich uwag uznała, że reguła numerowania daje regułę akapitu, a ona jej nie daje; recenzent przeczytał ją, jak prosiłeś, i zgłosił różnicę jako pozycję 1(a).

## Koszt

Około 1 godziny 15 minut pracy w sesji do tej pory (prowadzący, jeden autor na Sonnet 5.5 w sześciu turach i tury trzech recenzentów na Fable 5.2), łącznie 57,1 mln tokenów, z czego 19,8 mln na Fable 5.2; dwie rundy przeglądu z jedną poprawką (jedna uwaga blokująca i cztery drobne, wszystkie poprawione, przeszły) i jedna korekta z jej przeglądem (przeszła). Tabela etapów jest w zapisie cyklu: CORRECTION_STAGES_URL.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy. Fundament czekał na przegląd przez 25 scaleń od tagu ostatniego przeglądu, przy progu 60, więc przypomnienie nie jest należne.

</details>

## Technical changes

Four commits of the change, two of the fix of the review's findings, then one of correction 1:

- `0f738707`: `elements/common/foundation_text.py` (new): `blocks`, `fields`, `located`, `binding`, `begins_sentence`, `table`, `items` and the patterns they use, moved unchanged out of `elements/common/foundation_check.py`, which imports them and still passes them on to `elements/common/decision_index.py` and `elements/part-map/test_cross_part_imports.py`; the script stood at 1141 lines, the limit of WAY-385 is 1200, and it stands at 1111 after the move and the new check.
- `58f9937d`: `foundations/decisions.md`, WAY-05 only: the limit of 300 words, the second paragraph on the error and the list, `tests:` in *Verification* with the pair of examples cut to what no test holds, one sentence of *Rationale*, six ways not chosen in *Rejected*.
- `9dc811af`: `elements/common/foundation_check.py`: `check_length`, `excess` and `base_paragraphs` report a paragraph of binding sentences over three sentences or 300 words, as an error in a decision that is added or whose paragraphs, in words or in division, differ from those at the base, and as a `listed:` line in any other; `elements/common/test_foundation_check.py`: twelve tests, each with a line `decision:`.
- `e8b76178`: `elements/decisions/template.md` (the limit in the shape of an entry, the new bullet in "Binding sentences", the row "binding sentences" of "Fields and their readers"), `README.md` and `agent-instructions/README.md`.
- `67933213`, `9c7f9b71` (the fix of the review's findings): the two readmes and the template row restated as WAY-05 says (the length error stands apart from "that nothing holds", and a different division counts); `QUOTED` in `foundation_text.py` written with escapes again, as at the base; a test replacement that matched nothing now matches; the sentence of `elements-common` in `foundations/part_map.md` names the new module.
- `35796540` (correction 1, for your answer to item 1): `guidelines/coding-shared-module.md`: `elements-common` added to *Applies to* and `elements/common/` to *Where in code*; nothing else of the file.

## Checks

- **Final gate:** the CI run on this request's last head; its result is added when the run ends, in a later edit. The run before correction 1, on head `2ffff547`, https://github.com/mariusznazar/the-way/actions/runs/44726306276, first attempt: `tests` pass, 1m29s; `tests-windows` pass, 7m23s. The cycle ran no full gate on its own system and has no local time of it.
- **Failing before the change:** none, taken from the merged request https://github.com/mariusznazar/the-way/pull/151, whose CI run on its last head (https://github.com/mariusznazar/the-way/actions/runs/44597152256) passed in both checks; the base `1b6fe1c1` is a merge commit with the tree of its second parent, so no gate ran on the base.
- **Focused runs** (`python -B gate/run_tests.py <directory>`, exit 0): `elements/common` 283 tests, `elements/part-map` 40, `agent-instructions` 52, `product-guidelines` 14, `installation` 73 (at the reviewed head), by the author and the reviewers; after correction 1 `elements/common` 283, `product-guidelines` 14 and `relation-model` 13 by the reviewer, `agent-instructions` 52 by the author; the new tests failed before the code (`python -B -m unittest test_foundation_check` with ten `-k` filters in `elements/common`: exit 1, 10 of 12 failing, each on its assertion; the author's first run of the whole directory after it ended `FAILED (failures=10)` and its exit code was not captured, since a pipe took it) and passed after it (exit 0, 12 tests).
- **The check of the foundation** (`python -B elements/common/foundation_check.py`, no switch): exit 0, `0 errors`, twelve `listed:` lines, all of the length of a paragraph (WAY-134, 136, 139, 148, 150, 154, 256, 287, 289, 339, 344, 405, as the task counts them), by the author, the reviewers and the writer of this description; at the head of correction 1 by the author and the reviewer, same result.
- **Linter:** the pinned Ruff, `ruff check .` and `ruff format --check .`, exit 0 each, by the author at the head of the change and of the fix; not run after correction 1, since no Python file changed.
- **Own-work check:** the author named its weakest point (that a decision a change alters, not only one it adds, turns an excess into an error while an unaltered one stays listed, on the real foundation) and checked it by adding one word to WAY-405 in the real log, which gave exit 1 with the error while the other eleven entries stayed listed, and then reverting the edit; the reviewer repeated it with six probes on the real log and with twelve mutations of the new code, each caught by the new tests. For correction 1 the author's weakest point was whether the guidance reaches an agent that changes a shared module there; it stands on reading how the guidance is selected, since no test checks the selection, and the reviewer confirmed the reading and that the modules there import with exit 0 and no output.
- **Walk through the running product:** not performed; the foundation of the-way settles no way to a running product for itself, and the change is a checking script, texts of instructions and a decision, with no screen, answer of an interface or command of a product.
- **Reviews:** whole change, `FAIL e8b76178` (1 blocking, 4 Minor within the task, 1 outside it), run on Fable 5.2; the fix by the same author, the review of the fix `PASS 9c7f9b71` (0 blocking, 0 remaining, 0 new); correction 1, `PASS 35796540` (0 blocking, 3 Minor outside the task) by a fresh reviewer on Fable 5.2, which also read whole the six decisions the first review read only in part (WAY-344, WAY-134, WAY-18, WAY-19, WAY-150 and WAY-321: no collision with the limits or the check, three findings outside the task's scope, below); the return steps committed nothing and so had no review. The first reviewer read the index of its whole selection (118 decisions, 48 in full and 70 by heading) and 14 decisions whole.
- **Review of the foundation:** 25 merges since the tag `foundation-review/2026-11-15`, threshold 60: no reminder.
- **Form check** of this description: `python -B task-cycle/request_check.py .runs/task-cycles/decision-length-check/request.md --task .runs/task-cycles/decision-length-check/task.md` and **check of private paths** on it: `python -B task-cycle/private_paths_check.py .runs/task-cycles/decision-length-check/request.md`; both exit 0 (the last run, after each edit of the description); the checks on the copy of the record after correction 1 are added with the record's link.
- **Working copies left:** `.runs/quality-venv/` (author): the environment of the linter, installed as the readme gives and kept because the linter's tests in `agent-instructions` use it; it is under the ignored working directory of the task, nothing waits for it, and it goes when the task's directory goes. **Directories of earlier tasks kept:** none.

## Foundation entries

- **WAY-05** (marked `row 1`): a paragraph of the binding sentences of a decision has at most three sentences and at most 300 words.
- **WAY-05** (marked `row 2`): the check of the foundation reports as an error a paragraph over a limit in a decision a change adds or whose binding sentences it alters, a different division into paragraphs included, and only lists any other decision over a limit.
- **WAY-05** (marked `the cycle's`, one sentence of *Rationale*): a limit in words beside the one in sentences keeps a paragraph short when its sentences are joined to stand under the count.
- **Part map**, the sentence of `elements-common` (marked `the cycle's`): the part also answers for the module that reads the text of an entry for the foundation check.
- **Tests that hold a sentence of WAY-05 by a line `decision:`** (added by this change, WAY-03, WAY-12): the twelve tests of `check_length` in `elements/common/test_foundation_check.py`, each quoting the start of "A decision entry opens with one to three binding sentences that answer its question" or of "The check of the foundation reports as an error a paragraph of binding sentences"; no invariant test is changed and no *Violated* mark is set or cleared.

## Minor findings

none

## Findings outside the task's scope

- **1.** WAY-19 against WAY-05 (`foundations/decisions.md:871-872` and `:685-686`, `:730-732`, `elements/decisions/template.md:133-134`), from the review of correction 1: "**WAY-19 gives no rule of a paragraph, and it names the part in other words than WAY-05.** … What is wrong. The same thing has two names that read as opposites: for WAY-19 it is a part of *the question the entry answers*, for WAY-05's binding sentence and the template a part of *another question*; WAY-05's own *Rationale* uses the first ("A part of a question that an entry already answers is a paragraph of its own"). And WAY-19 gives the part one sentence, WAY-05 a paragraph of one to three. … Grade and scope. Minor: the words of both entries predate this request, the check works as WAY-05 says whichever reading is taken, and WAY-05's *Rationale* with the template's citation carry the intended reading. Outside the task's scope: the task changes WAY-05 in the five ways its *Decisions in play* list and leaves WAY-19 alone; aligning the words changes an approved binding sentence, which is the human's to approve." (Minor, outside the scope)
- **2.** WAY-150 (`foundations/decisions.md:1682`): "**WAY-150 names its own first paragraph by its place.** … The first paragraph of WAY-150 has 317 words, so the next change of WAY-150 has to cut or divide it, and WAY-05 now counts a new division as a change. If the passage that names the decisions opened whole lands in another paragraph, this sentence points to the wrong one, and no check reports it. … Minor, a hazard for the task that changes WAY-150 and no fault of this request's files. Outside the task's scope: the task shortens no entry." (Minor, outside the scope)
- **3.** WAY-391 (`foundations/decisions.md:11171`, `- **Scope:** relation-model`) against `guidelines/coding-shared-module.md:4`: "**WAY-391 does not name `elements-common` in its *Scope*, while the guidance that names it now applies there.** For the five other kinds the *Scope* of the decision that designates the exemplar is the same list as the *Applies to* of the kind's guidance (WAY-386 to WAY-390). For `shared-module` the *Scope* names `relation-model` alone, while WAY-391 also says "importing a file of the kind runs nothing" and the guidance applies to four parts. … An agent that changes a shared module in `elements/common/` and finds its decisions by *Scope* (WAY-21, WAY-150) does not find WAY-391; it reaches it only through the guidance, which names it. … Minor. Outside the task's scope: remark 1 asks for the two lines of the guidance and nothing else, and a change of a decision's *Scope* is not what it carries." (Minor, outside the scope)

## Course of the cycle

- **Task and sources:** an independent task: the check of the foundation reports a paragraph of binding sentences over three sentences or 300 words as an error in a decision a change adds or alters, and lists the others; the sources are the task document (frozen in the record), the decision log at `1b6fe1c1`, the decision template and the check's script.
- **Process pin:** none; the-way itself, the checkout of the worktree is the process.
- **Spec:** none; the task settles each point and no open design choice stood.
- **Route:** one author without a plan, class `same` (Sonnet 5.5), because one agent holds the change; reviewed by agents that did not make it, on the strongest class (Fable 5.2). Corrections: correction 1, remarks `reports/correction-1-remarks.md`, answering your two answers (items 1 and 2 of the first description), no reset of the branch.
- **Plan:** none.
- **Choices:** 4 choices of the cycle in the questions table (the class of the author; the split of the script into a new module; the gap in the author's reading; the gap in the reviewer's reading), the record linked below.
- **Blocking findings left:** none.
- **Record:** CORRECTION_RECORD_URL.
