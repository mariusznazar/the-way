**State: draft** — the result of the tests on the last head is not in yet; two items below (1 and 2) wait for your answer

## What you will see

The check of the foundation now stops a change that adds a decision, or alters the binding sentences of one, when a paragraph of those sentences has more than three sentences or more than 300 words. The error names the decision, the paragraph and the measure that is over, with its value. Every other decision over the limit is only listed, and the list stops nothing, so the twelve entries of the-way that are over the limit today stay as they are until the task you parked for them. A change that only divides a decision's sentences into paragraphs differently, with no word changed, counts as altering it, so joining two paragraphs into one over the limit is caught.

- The rule you chose is written where the process keeps it: the rule for how a decision is written now has the limit of 300 words beside the limit of three sentences, says that the check reports an excess as an error in an added or altered decision and only lists it in any other, and carries the reasons and the ways you did not choose.
- The template of a decision gives both limits where it gives the shape of an entry, and says that the check counts them in every decision a change adds or alters, so an older entry over the limit meets the rule when a change next alters it.
- The description of what the check reports is updated in the three other places that give it: the head of the check's script, the guide to working on the-way, and the readme.
- The check's script grew past the size the process allows for a script file, so the code that reads an entry's text moved into a new module with no change of behaviour.

### Underneath

One script with its tests and a new module beside it, the decision template, two readmes, one rule of the decision log and one sentence of the map of the parts; no product is touched.

## For you to decide

### Needed from you

none

### Fix or let through

1. The guidance for the shared modules of the process's code lists three directories of the repository and not the one where the foundation check and its new module stand. An agent that changes a shared module there is therefore not handed that guidance, and may write the module without its one rule: the top level only imports and defines. The new module follows the rule as it stands, and the gap was there before this change; it only grows by one file. Fixing it here costs one line in the guidance and a round of review, and undoing it costs nothing. Making a task of it leaves the gap until that task runs, and undoing it costs nothing. Letting it through leaves agents without the guidance until someone notices, and the next module that breaks the rule costs a fix. I recommend making a task of it, since it is a gap of the guidance and not of this change. Its weak point: the next agent that adds a module to that directory before the task runs is not given the guidance. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)
2. The review of the whole change read the index of everything it selected, 118 decisions, and opened 14 of them whole, among them the rule for how a decision is written, the one on how a decision is checked and the one on the size of a script. It named six others as read only in part: it read the binding sentences of four of them (one about a script that meets a missing field, one about how a task carries what its refinement settles, two about how decisions are kept and numbered) and only the headings of two (one about how skills choose what to read, one about when the check reports an invariant that has no test). If one of them hides a collision with the new rule, the collision shows when a later change meets it, and fixing it then costs a correction with a review. Having a fresh reviewer read what stayed unread costs one more session of the strongest model and a round of review; undoing it costs nothing. Making a task of it leaves the gap until that task runs. Letting it through accepts the risk. I recommend letting it through, since the reviewer read the new check, its tests and the real log closely (twelve mutations and six probes) and the six decisions bear on its neighbours, not on the limit. Its weak point: the reviewer read only the headings of two of them and the binding sentences of the other four, and a reason or a rejected way written in the prose of one of them can say something its binding sentences do not. Read it in this request, make a task of it, or let it through? (Checks)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The script file was at 1141 lines, and the new check would have taken it to about 1206, over the 1200 that the process allows a script file. The cycle moved the code that reads an entry's text into a new module, as the first commit that changes code, and left the other scripts that import those names as they are, since the old file still passes them on. The other ways were to squeeze the new check into the 59 lines left, which leaves no room for the next check, and to move a different part of the file, which is a less coherent part. If this reading is wrong, the cost is that a reader looking for those functions in the old file finds an import, and moving the block back undoes it.
4. The reasons for the ways not chosen are written into the rule without the counts you quoted when you chose (how many old entries would need rework, one entry in ten, 478 words in one entry), because the same rule keeps counts of entries out of its prose, and a figure like 478 becomes false the day the long entries are shortened. Each reason is kept without the figure. The other way is to write the figures in, which breaks that rule.
5. Two entries carry text you did not see in the task, so they are marked as the cycle's own. The rule for how a decision is written has one sentence of reason that no row gave: a limit in words beside the limit in sentences keeps a paragraph short when its sentences are joined to fit under the count, which is the reason the task gives for choosing both limits. The map of the parts now names the new module in the sentence about the part that holds the foundation check. (Foundation entries)
6. Twelve new tests hold what the rule says about the check, each by a line that cites the rule and the start of one of its two new sentences; the check accepts each line. No invariant's sentence was corrected, no invariant test was changed and no surface of the process changed: the command that checks the foundation keeps its path, its argument and its exit codes. (Foundation entries)

## Cost

About 50 minutes of work (the orchestrator, one author on Sonnet 5.5 in three turns and one reviewer on Fable 5.2 in two turns), 36.2 million tokens in all, of which 15.8 million on Fable 5.2; one review round with its fix (one blocking finding and four Minor ones, all fixed, passed). The table of stages is added to this description after the record is committed.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation has waited for a review through 25 merges since the tag of the last review, with the threshold at 60, so no reminder is due.

<details>
<summary>W Twoim języku</summary>

**Stan: wersja robocza** — wyniku testów na ostatnim commicie jeszcze nie ma; dwie pozycje poniżej (1 i 2) czekają na Twoją odpowiedź

## Co zobaczysz

Sprawdzenie fundamentu zatrzymuje teraz zmianę, która dodaje decyzję albo zmienia jej zdania wiążące, gdy akapit tych zdań ma więcej niż trzy zdania albo więcej niż 300 słów. Błąd nazywa decyzję, akapit i przekroczoną miarę z jej wartością. Każdą inną decyzję ponad limit sprawdzenie tylko wypisuje, a lista niczego nie zatrzymuje, więc dwanaście wpisów the way, które dziś stoją ponad limitem, zostaje, jak jest, do zadania, które dla nich zaparkowałeś. Zmiana, która tylko dzieli zdania decyzji na akapity inaczej, bez zmiany słów, liczy się jako zmiana decyzji, więc sklejenie dwóch akapitów w jeden ponad limit zostaje złapane.

- Wybrana przez Ciebie reguła stoi tam, gdzie proces ją trzyma: reguła o tym, jak pisze się decyzję, ma teraz limit 300 słów obok limitu trzech zdań, mówi, że sprawdzenie zgłasza przekroczenie jako błąd w decyzji dodanej albo zmienionej, a w każdej innej tylko je wypisuje, i niesie powody oraz warianty, których nie wybrałeś.
- Szablon decyzji podaje oba limity tam, gdzie podaje kształt wpisu, i mówi, że sprawdzenie liczy je w każdej decyzji, którą zmiana dodaje albo zmienia, więc starszy wpis ponad limitem spotka tę regułę, gdy zmiana następnym razem go zmieni.
- Opis tego, co zgłasza sprawdzenie, jest uzupełniony w trzech innych miejscach, które go podają: na początku skryptu sprawdzającego, w przewodniku po pracy nad the way i w readme.
- Skrypt sprawdzający urósł ponad rozmiar, który proces dopuszcza dla pliku skryptu, więc kod czytający tekst wpisu przeniesiono do nowego modułu bez zmiany działania.

### Pod spodem

Jeden skrypt z testami i nowy moduł obok niego, szablon decyzji, dwa readme, jedna reguła dziennika decyzji i jedno zdanie mapy części; żaden produkt nie jest ruszony.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Wytyczne dla modułów współdzielonych w kodzie procesu wymieniają trzy katalogi repozytorium, a nie ten, w którym stoją sprawdzenie fundamentu i jego nowy moduł. Agent, który zmienia moduł współdzielony w tym katalogu, nie dostaje więc tych wytycznych i może napisać moduł bez jego jedynej reguły: na poziomie pliku tylko importy i definicje. Nowy moduł tę regułę spełnia, a luka była przed tą zmianą; rośnie tylko o jeden plik. Poprawa tutaj kosztuje jedną linię wytycznych i rundę przeglądu, a cofnięcie nic. Zadanie zostawia lukę do czasu, aż się wykona, a cofnięcie nic nie kosztuje. Przepuszczenie zostawia agentów bez wytycznych, aż ktoś to zauważy, a następny moduł łamiący regułę kosztuje poprawkę. Rekomenduję zadanie, bo to luka wytycznych, nie tej zmiany. Słaby punkt: następny agent, który dołoży moduł do tego katalogu przed wykonaniem zadania, nie dostanie wytycznych. Poprawić w tym requeście, zrobić zadanie czy przepuścić? (Findings outside the task's scope, 1)
2. Przegląd całej zmiany przeczytał indeks wszystkiego, co wybrał, czyli 118 decyzji, i otworzył w całości 14 z nich, w tym regułę o tym, jak pisze się decyzję, regułę o tym, jak decyzję się sprawdza, i regułę o rozmiarze skryptu. Sześć innych wskazał jako przeczytane tylko w części: zdania wiążące czterech przeczytał (jedna o skrypcie, który trafia na brak pola, jedna o tym, jak zadanie niesie to, co ustaliło doprecyzowanie, dwie o tym, jak decyzje są prowadzone i numerowane), a z dwóch tylko nagłówki (jedna o tym, jak skille wybierają, co czytać, jedna o tym, kiedy sprawdzenie zgłasza niezmiennik bez testu). Jeśli któraś z nich ukrywa kolizję z nową regułą, kolizja wyjdzie, gdy trafi na nią późniejsza zmiana, a poprawa wtedy kosztuje poprawkę z przeglądem. Nowy recenzent czytający to, co zostało nieprzeczytane, kosztuje jedną sesję najmocniejszego modelu i rundę przeglądu; cofnięcie nic. Zadanie zostawia lukę do czasu, aż się wykona. Przepuszczenie przyjmuje ryzyko. Rekomenduję przepuszczenie, bo recenzent dokładnie przeczytał nową kontrolę, jej testy i prawdziwy dziennik (dwanaście mutacji i sześć prób), a tych sześć decyzji dotyczy sąsiednich spraw, nie limitu. Słaby punkt: recenzent przeczytał tylko nagłówki dwóch z nich i zdania wiążące pozostałych czterech, a powód albo odrzucony wariant zapisany prozą jednej z nich może mówić coś, czego jej zdania wiążące nie mówią. Przeczytać to w tym requeście, zrobić zadanie czy przepuścić? (Checks)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

3. Plik skryptu miał 1141 linii, a nowa kontrola zaniosłaby go do ok. 1206, ponad 1200, które proces dopuszcza dla pliku skryptu. Cykl przeniósł kod czytający tekst wpisu do nowego modułu jako pierwszy commit zmieniający kod i zostawił inne skrypty, które importują te nazwy, bez zmian, bo stary plik nadal je przekazuje. Inne sposoby to wciśnięcie nowej kontroli w 59 pozostałych linii, co nie zostawia miejsca na następną, i przeniesienie innej części pliku, która jest mniej spójna. Jeśli to czytanie jest błędne, koszt to taki, że kto szuka tych funkcji w starym pliku, znajdzie import; przeniesienie bloku z powrotem to cofa.
4. Powody dla niewybranych wariantów są zapisane w regule bez liczb, które podałeś przy wyborze (ile starych wpisów wymagałoby przeróbki, co dziesiąty wpis, 478 słów w jednym wpisie), bo ta sama reguła nie wpuszcza do swojej prozy liczb wpisów, a liczba 478 staje się fałszywa w dniu skrócenia długich wpisów. Każdy powód zostaje bez liczby. Inny sposób to wpisanie liczb, co łamie tę regułę.
5. Dwa wpisy niosą tekst, którego nie widziałeś w zadaniu, więc są oznaczone jako własne cyklu. Reguła o tym, jak pisze się decyzję, ma jedno zdanie powodu, którego nie dał żaden wiersz: limit w słowach obok limitu w zdaniach pilnuje, żeby akapit nie rósł, gdy zdania sklejono, by zmieścić się w liczbie, czyli powód, który podaje zadanie, wybierając oba limity. Mapa części nazywa teraz nowy moduł w zdaniu o części, która trzyma sprawdzenie fundamentu. (Foundation entries)
6. Dwanaście nowych testów trzyma to, co reguła mówi o sprawdzeniu, każdy linią, która cytuje regułę i początek jednego z jej dwóch nowych zdań; sprawdzenie przyjmuje każdą linię. Zdanie żadnego niezmiennika nie zostało poprawione, żaden test niezmiennika się nie zmienił i żadna powierzchnia procesu się nie zmieniła: polecenie sprawdzające fundament zachowuje ścieżkę, argument i kody wyjścia. (Foundation entries)

## Koszt

Około 50 minut pracy (prowadzący, jeden autor na Sonnet 5.5 w trzech turach i jeden recenzent na Fable 5.2 w dwóch turach), łącznie 36,2 mln tokenów, z czego 15,8 mln na Fable 5.2; jedna runda przeglądu z poprawką (jedna uwaga blokująca i cztery drobne, wszystkie poprawione, przeszły). Tabelę etapów dopiszę do tego opisu po zapisaniu rekordu cyklu.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy. Fundament czekał na przegląd przez 25 scaleń od tagu ostatniego przeglądu, przy progu 60, więc przypomnienie nie jest należne.

</details>

## Technical changes

Four commits of the change, then two of the fix of the review's findings:

- `0f738707`: `elements/common/foundation_text.py` (new): `blocks`, `fields`, `located`, `binding`, `begins_sentence`, `table`, `items` and the patterns they use, moved unchanged out of `elements/common/foundation_check.py`, which imports them and still passes them on to `elements/common/decision_index.py` and `elements/part-map/test_cross_part_imports.py`; the script stood at 1141 lines, the limit of WAY-385 is 1200, and it stands at 1111 after the move and the new check.
- `58f9937d`: `foundations/decisions.md`, WAY-05 only: the limit of 300 words, the second paragraph on the error and the list, `tests:` in *Verification* with the pair of examples cut to what no test holds, one sentence of *Rationale*, six ways not chosen in *Rejected*.
- `9dc811af`: `elements/common/foundation_check.py`: `check_length`, `excess` and `base_paragraphs` report a paragraph of binding sentences over three sentences or 300 words, as an error in a decision that is added or whose paragraphs, in words or in division, differ from those at the base, and as a `listed:` line in any other; `elements/common/test_foundation_check.py`: twelve tests, each with a line `decision:`.
- `e8b76178`: `elements/decisions/template.md` (the limit in the shape of an entry, the new bullet in "Binding sentences", the row "binding sentences" of "Fields and their readers"), `README.md` and `agent-instructions/README.md`.
- `67933213`, `9c7f9b71` (the fix of the review's findings): the two readmes and the template row restated as WAY-05 says (the length error stands apart from "that nothing holds", and a different division counts); `QUOTED` in `foundation_text.py` written with escapes again, as at the base; a test replacement that matched nothing now matches; the sentence of `elements-common` in `foundations/part_map.md` names the new module.

## Checks

- **Final gate:** the CI run on this request's last head; its result is added when the run ends, in a later edit. The cycle ran no full gate on its own system and has no local time of it.
- **Failing before the change:** none, taken from the merged request https://github.com/mariusznazar/the-way/pull/151, whose CI run on its last head (https://github.com/mariusznazar/the-way/actions/runs/44597152256) passed in both checks; the base `1b6fe1c1` is a merge commit with the tree of its second parent, so no gate ran on the base.
- **Focused runs** (`python -B gate/run_tests.py <directory>`, exit 0): `elements/common` 283 tests, `elements/part-map` 40, `agent-instructions` 52, `product-guidelines` 14, `installation` 73 (at the reviewed head), by the author and the reviewer; the new tests failed before the code (`python -B -m unittest test_foundation_check` with ten `-k` filters in `elements/common`: exit 1, 10 of 12 failing, each on its assertion; the author's first run of the whole directory after it ended `FAILED (failures=10)` and its exit code was not captured, since a pipe took it) and passed after it (exit 0, 12 tests).
- **The check of the foundation** (`python -B elements/common/foundation_check.py`, no switch): exit 0, `0 errors`, twelve `listed:` lines, all of the length of a paragraph (WAY-134, 136, 139, 148, 150, 154, 256, 287, 289, 339, 344, 405, as the task counts them), by the author, the reviewer and the writer of this description.
- **Linter:** the pinned Ruff, `ruff check .` and `ruff format --check .`, exit 0 each, by the author at the head of the change and of the fix.
- **Own-work check:** the author named its weakest point (that a decision a change alters, not only one it adds, turns an excess into an error while an unaltered one stays listed, on the real foundation) and checked it by adding one word to WAY-405 in the real log, which gave exit 1 with the error while the other eleven entries stayed listed, and then reverting the edit; the reviewer repeated it with six probes on the real log (P1–P6: a paragraph cut in two, a rationale alone changed, a fourth sentence added, full stops inside quotation marks, a doubled space, two paragraphs joined) and with twelve mutations of the new code, each caught by the new tests.
- **Walk through the running product:** not performed; the foundation of the-way settles no way to a running product for itself, and the change is a checking script, texts of instructions and a decision, with no screen, answer of an interface or command of a product.
- **Reviews:** whole change, `FAIL e8b76178` (1 blocking, 4 Minor within the task, 1 outside it), run on Fable 5.2; the fix by the same author, the review of the fix `PASS 9c7f9b71` (0 blocking, 0 remaining, 0 new); the return step committed nothing and so had no review. The reviewer read the index of its whole selection (118 decisions, 48 in full and 70 by heading) and 14 decisions whole; of WAY-344, WAY-134, WAY-18, WAY-19, WAY-150 and WAY-321 it read parts only (item 2 of *For you to decide*).
- **Review of the foundation:** 25 merges since the tag `foundation-review/2026-11-15`, threshold 60: no reminder.
- **Form check** of this description: `python -B task-cycle/request_check.py .runs/task-cycles/decision-length-check/request.md --task .runs/task-cycles/decision-length-check/task.md`; **check of private paths** on the description: `python -B task-cycle/private_paths_check.py .runs/task-cycles/decision-length-check/request.md`; their last runs are recorded in the cycle's record; the checks on the copy of the record are added after it is committed.
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

- **1.** `guidelines/coding-shared-module.md:4`: "The guidelines of the kind `shared-module` do not name `elements-common`. `guidelines/coding-shared-module.md:4` gives *Applies to* as `relation-model · process-audit · task-cycle`, and its *Where in code* (lines 40-42) the same three directories. `elements/common/` held a shared module before this change (`foundation_source.py`) and holds two after it. By `product-guidelines/reading.md` an agent is given a guideline file whose *Applies to* names a part its work touches, so an agent changing these modules is not given the file of their kind. The gap stood at the base; the change adds one more file to it. The author did read the file, on the handoff's word, and the new module keeps its one rule: its top level only imports, sets `sys.dont_write_bytecode`, and defines three patterns and seven functions." (Minor, outside the scope, reviewer of the whole change)

## Course of the cycle

- **Task and sources:** an independent task: the check of the foundation reports a paragraph of binding sentences over three sentences or 300 words as an error in a decision a change adds or alters, and lists the others; the sources are the task document (frozen in the record), the decision log at `1b6fe1c1`, the decision template and the check's script.
- **Process pin:** none; the-way itself, the checkout of the worktree is the process.
- **Spec:** none; the task settles each point and no open design choice stood.
- **Route:** one author without a plan, class `same` (Sonnet 5.5), because one agent holds the change; reviewed by an agent that did not make it, on the strongest class (Fable 5.2).
- **Plan:** none.
- **Choices:** 4 choices of the cycle in the questions table (the class of the author; the split of the script into a new module; the gap in the author's reading; the gap in the reviewer's reading), the record linked below.
- **Blocking findings left:** none.
- **Record:** added to this description after the record's commit.
