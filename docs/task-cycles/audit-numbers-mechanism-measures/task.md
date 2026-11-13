---
title: "the way: liczby audytu — koszt ze starszych zapisów cykli, miary liczone skryptem przy zamknięciu cyklu, czas bramki według katalogu"
status: draft
created: 2026-11-12T17:54
updated: 2026-11-12
tags: [zadanie]
related: "notatka projektu procesu pracy nad produktem"
---

# the way: liczby audytu — koszt ze starszych zapisów cykli, miary liczone skryptem przy zamknięciu cyklu, czas bramki według katalogu

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cotygodniowy audyt procesu zna koszt 7 ze 138 cykli (wynik liczenia z 12.11.2026): w 126 cyklach raport etapów (`stages.md`) ma starszą formę, którą polecenie liczące audytu pomija, a 5 cykli nie ma raportu etapów wcale.
- Liczb o tym, jak agenci cyklu używają kontekstu i pamięci podręcznej modelu — ile wywołań modelu robi cykl, jak duży kontekst niesie każde, ile tokenów zapisuje do pamięci ponownie — nic nie liczy na bieżąco; policzono je dwa razy ręcznie w analizach z 12.11.2026.
- Zapis cyklu nie podaje, ile trwał każdy katalog testów w przebiegu bramki.
- Odczuwa to Mariusz przy cotygodniowym audycie procesu oraz każda zmiana z programu usprawnień: bez liczby „po” nie da się powiedzieć, czy zmiana zadziałała.
- Bez tego zadania audyt przez kolejne tygodnie nie ma z czym porównać, a liczby „przed” zostają tylko w raportach z 12.11.2026.

### To do

1. Polecenie liczące audytu (`process-audit/audit_count.py`) podaje koszt cyklu także wtedy, gdy raport etapów nie ma sekcji `Stages: start, waiting for tools and tokens by model`: liczy go z tabeli tokenów według modelu (nagłówek `| Model | Total tokens | Input | Cached input | Output |`), tym samym cennikiem i wzorem co dziś — wejście bez części odczytanej z pamięci po cenie wejścia, część odczytana z pamięci po cenie odczytu, wyjście po cenie wyjścia. Starszą formę rozpoznaje po jej własnych znakach, osobną ścieżką odczytu. Udział rund poprawek zostaje dla takiego cyklu nieznany, z podanym powodem. Raport etapów, w którym brakuje pola potrzebnego którejkolwiek z obu form, daje koszt tego cyklu nieznany; polecenie zapisuje wynik i kończy kodem 1 z linią `Error:`, która nazywa plik i brakujące pole.
2. Nowy skrypt w `task-cycle/`, uruchamiany przy zamknięciu cyklu w tym samym kroku, w którym powstaje raport etapów, liczy z zapisów sesji cyklu i zapisuje do osobnego pliku w katalogu zapisu cyklu same liczby tokenów i wywołań, bez kwot:
   - liczbę wywołań modelu — w całym cyklu, osobno agenta prowadzącego cykl i każdego podagenta;
   - kontekst wywołania (wejście, odczyt z pamięci i zapis do pamięci razem) — dla każdego agenta w pierwszym, środkowym i ostatnim wywołaniu; dla cyklu średnią, osobno średnią agenta prowadzącego, oraz udział kontekstu przypadający na wywołania ponad 200 tys. tokenów;
   - tokeny zapisane do pamięci podręcznej, osobno z czasem życia 5 minut i godziny, dla każdego agenta;
   - tokeny zapisane do pamięci ponownie i liczbę wywołań z takim zapisem, osobno dla agenta prowadzącego i dla podagentów: w wywołaniu agenta po pierwszym ponownie zapisane jest to, co poprzednie wywołanie miało w pamięci (odczyt i zapis do pamięci), a obecne z niej nie odczytało, najwyżej tyle, ile obecne zapisało; liczy się tylko powyżej 2 tys. tokenów i tylko wtedy, gdy kontekst nie skurczył się o 30% lub więcej względem poprzedniego wywołania;
   - dla agenta Codexa zapis do pamięci i ponowny zapis są nieznane, nie zero: jego zapis sesji podaje tylko część wejścia odczytaną z pamięci.
3. Instrukcja cyklu (`task-cycle/skill/SKILL.md`) i szablon zapisu cyklu (`task-cycle/record_template.md`) wymieniają ten plik i krok, który go tworzy; plik trafia do kopii zapisu cyklu w repozytorium razem z resztą katalogu.
4. Agent prowadzący cykl uruchamia bramkę produktu przez nowy skrypt w `task-cycle/`, przy każdym przebiegu, ten na stanie wyjściowym też. Skrypt uruchamia bramkę, którą produkt deklaruje, mierzy czas całego przebiegu, wyciąga z jej wyjścia czas każdego katalogu testów, który wypisał program uruchamiający testy procesu (linia `== <katalog>` i czas z `unittest`), bez zakładania ich kolejności, i dopisuje przebieg do pliku w katalogu zapisu cyklu, razem z liczbą innych przebiegów bramki uruchomionych tym skryptem, które biegły w tym samym czasie na tej maszynie. Instrukcja cyklu i szablon zapisu cyklu wymieniają ten skrypt i ten plik.
5. Polecenie liczące audytu czyta plik miar z punktu 2 i czasy bramki z punktu 4 każdego cyklu i pokazuje je w osobnej sekcji wyniku: wartości każdego cyklu, a dla każdej wersji procesu medianę każdej miary i odpowiedź, czy spada względem poprzedniej wersji tej samej serii, jak dziś dla kosztu. Dla czasów bramki mediana i porównanie biorą tylko przebiegi, przy których nie biegła żadna inna bramka; pozostałe przebiegi wynik pokazuje osobno. Nową serię tych miar zaczyna tylko zmiana przyrządu, który je mierzy: skryptu z punktu 2 albo skryptu z punktu 4. Plik miar albo czasów bramki, w którym brakuje pola, daje wartości z niego nieznane; polecenie zapisuje wynik i kończy kodem 1 z linią `Error:`, która nazywa plik i brakujące pole.
6. Instrukcja sesji audytu (`process-audit/SKILL.md`) kładzie te miary przed Mariuszem na sesji.

### Acceptance criteria

- Zmiana nie dotyka pliku `task-cycle/cycle_stages.py` ani katalogów `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` i `task-cycle/spec`: każda zmiana w nich zaczyna w audycie nową serię miar, a osobny skrypt i osobny plik wybrano po to, żeby jej nie zaczynać.
- Wynik liczenia dzieli dawne cykle na te same serie kosztu co przed zmianą: dodanie skryptu miar i jego pliku nie zaczyna nowej serii kosztu.

### Questions to settle

- Czy cotygodniowe liczenie audytu ma czytać nowe liczby (plik miar z punktu 2 i czasy bramki z punktu 4) i pokazywać je w swoim wyniku, czy to zadanie tylko zaczyna je zbierać w zapisach cykli?
  - Answer: Czyta je i pokazuje razem z medianami każdej wersji procesu i porównaniem z poprzednią wersją tej samej serii (wariant pełny).
  - Not chosen:
    - tylko zbierać w zapisach cykli — liczby leżą w katalogach cykli, do których sesja audytu nie zagląda, a porównanie „przed i po” trzeba robić ręcznie
    - czytać i pokazywać wartości każdego cyklu, bez median i porównań wersji — „sam na oko to nic nie porównam sensownie”
  - Source: Mariusz, 2026-11-12: „wolę wariant pełny, bo sam na oko to nic nie porównam sensownie”
- Co zaczyna nową serię miar z punktu 2 i czasów bramki?
  - Answer: Tylko zmiana przyrządu: zmiana skryptu, który liczy miary z punktu 2, albo tego, czym zapis cyklu mierzy czasy bramki. Zmiana instrukcji cyklu — recenzenta i autora też — serii tych miar nie zaczyna, bo jej skutek ma być widać. Seria kosztu i reguły, które ją zaczynają, zostają jak są.
  - Not chosen:
    - te same pliki co dla kosztu, z dopisanym skryptem miar — porównania niemal nigdy by nie wystąpiły, bo prawie każda zmiana z programu usprawnień dotyka tych plików, a dopisanie skryptu miar do listy przerwałoby też serie kosztu
  - Source: Mariusz, 2026-11-12: „tak jak rekomendujesz”
- Skąd zapis cyklu bierze czas każdego katalogu testów w przebiegu bramki?
  - Answer: Ze skryptu, przez który agent prowadzący uruchamia bramkę: mierzy czas całego przebiegu, wyciąga z wyjścia czasy katalogów wypisane przez program uruchamiający testy procesu i zapisuje je do pliku w katalogu zapisu cyklu. Budowanie i testy Node gry zostają w czasie całości.
  - Not chosen:
    - agent prowadzący przepisuje czasy z wyjścia do zapisu cyklu — przepisane liczby bywają błędne, audyt czytałby tabelę pisaną ręcznie, a zmiana nawyku agenta zmienia przyrząd bez śladu w plikach
    - program uruchamiający testy procesu (`gate/run_tests.py`) sam zapisuje czasy do pliku — dziś z założenia nie zostawia śladu przebiegu, w grze nie objąłby budowania ani Node i zderzyłby się z zadaniem o równoległych katalogach
  - Source: Mariusz, 2026-11-12: „skrypt”
- Jak audyt porównuje czasy bramki między wersjami procesu, skoro ten sam przebieg trwa 15–16 minut na wolnej maszynie i 23–40 minut przy kilku sesjach obok?
  - Answer: Skrypt bramki zapisuje przy każdym przebiegu, ile innych bramek uruchomionych tym skryptem biegło w tym samym czasie; audyt porównuje medianę przebiegów, przy których nie biegła żadna inna, a resztę pokazuje osobno. Innego obciążenia maszyny ta liczba nie widzi, a wersja, w której każda bramka miała towarzystwo, nie dostaje porównania.
  - Not chosen:
    - najkrótszy przebieg każdej wersji — wersja z większą liczbą cykli ma więcej szans na szybki przebieg i wypada lepiej, a jeden szczęśliwy przebieg wyznacza wynik
    - mediana jak dla pozostałych miar — przy dzisiejszym rozrzucie porównanie mówi głównie o obciążeniu maszyny
  - Source: Mariusz, 2026-11-12: „tak jak rekomendujesz”
- Co robi liczenie audytu, gdy raport etapów dawnego cyklu nie pasuje ani do nowszej, ani do starszej formy: podaje koszt jako nieznany z powodem i liczy dalej, czy kończy błędem?
  - Answer: Podaje koszt tego cyklu jako nieznany, pisze wynik i kończy kodem 1 z linią `Error:`, która nazywa plik i brakujące pole — jak dziś przy repozytorium, którego nie dało się przeczytać. Zmienia to WAY-344: plik czytany z historii gita, której żadna zmiana nie poprawi, nie zatrzymuje całego liczenia.
  - Not chosen:
    - kod 2 i nic nie zapisane, jak każe WAY-344 — liczenie biegnie w nocy bez człowieka, więc sobotnia sesja nie ma żadnego wyniku, także liczb z rejestru problemów, aż ktoś poprawi skrypt
  - Source: Mariusz, 2026-11-12: „tak jak rekomendujesz”
- Według której z dwóch definicji z analiz z 12.11.2026 skrypt liczy tokeny zapisane do pamięci ponownie?
  - Answer: Według definicji z weryfikacji (`weryfikacja_usprawnienia_the_way_dane/s05_metrics.py`, wiersze 76–83): to, co poprzednie wywołanie miało w pamięci, a obecne z niej nie odczytało, najwyżej tyle, ile obecne zapisało, powyżej 2 tys. tokenów i bez skurczenia kontekstu o 30% lub więcej, które jest zwinięciem rozmowy, nie wygaśnięciem pamięci. Wartość „przed” do porównania stoi w `weryfikacja_usprawnienia_the_way_dane/miary_kontekstu.md`.
  - Not chosen:
    - definicja z syntezy (`usprawnienia_the_way_dane/15_cache_rewrites.py`, wiersze 134–137): zapis ponad przyrost kontekstu od poprzedniego wywołania — każde zwinięcie rozmowy wygląda jak wygaśnięcie pamięci, więc zmiana, która dodaje zwinięcia, wyglądałaby jak pogorszenie
  - Source: Mariusz, 2026-11-12: „z weryfikacji”

## Context

- Źródło zadania: karta działania D5 raportu o usprawnieniach procesu i sekcja 8 raportu o usprawnieniach procesu raportu o usprawnieniach procesu; wartości „przed” stoją w tabeli „Liczby do zbierania od teraz” tej sekcji.
- Audyt rozpoznaje nową serię po zmianie plików wymienionych w kryterium akceptacji (`process-audit/audit_count.py:266`, stała `TREE_PATHS`); zmiana nowych skryptów, instrukcji cyklu ani szablonu zapisu serii kosztu nie zaczyna.
- Tabelę tokenów według modelu ma każdy raport etapów w historii obu repozytoriów (130 ostatnich kopii, sprawdzone 12.11.2026), zawsze dokładnie raz.
- W obrębie jednej serii wszystkie cykle mają raport etapów tej samej formy, więc audyt nie zestawi kosztu policzonego z tabeli według modelu z kosztem policzonym z sekcji szczegółowej.
- Nowy skrypt stoi w `task-cycle/`, jak `task-cycle/cycle_stages.py`: część `task-cycle` nie może zależeć od części `process-audit` (mapa części), a cennik należy do `process-audit` — stąd liczby tokenów bez kwot.
- Bramka wypisuje dziś pod linią `== <katalog>` linię `Ran <n> tests in <s>s`, którą daje `unittest` (`gate/run_tests.py:94`); czasu katalogu w osobnej, zbiorczej formie nie podaje.
- Skrypt bramki z punktu 4 zapisuje same czasy, nie wyjście bramki: WAY-160 odrzuca trzymanie pełnego wyjścia bramki w pliku cyklu.
- Ten sam plik `gate/run_tests.py` zmienia zadanie zadanie o równoległym uruchamianiu katalogów testów (katalogi testów równolegle).
- Przechowywanie zapisów sesji Claude Code jest wydłużone do 90 dni ustawieniem z 12.11.2026.
- Skrypty, którymi policzono „przed”: katalogi `usprawnienia_the_way_dane` i `weryfikacja_usprawnienia_the_way_dane` obok raportu.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-337** — „A cycle's cost is two numbers, neither divided by a measure of the size of the task: its cost at constant prices, computed from a price list of models that carries a date, and the share of that cost spent in fix rounds […]. The share is `0.0%` only where the record says the cycle had no fix round, and unknown wherever the record and the stages cannot tie each round to the turns that served it.” Punkt 1 liczy tę samą kwotę z innej tabeli; udział rund dla starszej formy jest nieznany.
- **WAY-339** — „A new price list, or a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, starts a new series of measures. The audit compares measures only within one series, and judges a version of the process by the cycles that ran on it, never one week against another.” Zmiana: dla miar z punktu 2 i czasów bramki nową serię zaczyna tylko zmiana przyrządu, który je mierzy — skryptu z punktu 2 albo skryptu z punktu 4; zmiana instrukcji recenzenta i autora jej nie zaczyna. Seria kosztu zostaje jak jest.
- **WAY-344** — „A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs […] and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks […] and a missing field ends the script with exit code 2 and a message that names the file and the field […]. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field […].” Zmiana: plik zapisu cyklu, który polecenie liczące audytu czyta z historii gita — raport etapów, plik miar z punktu 2 i plik czasów bramki z punktu 4 — a w którym brakuje pola, daje wartości z niego nieznane, wynik zapisany i kod 1 z linią `Error:` nazywającą plik i pole, zamiast kodu 2 bez wyniku. Test brakującego pola dla każdego odczytu zostaje. Nowe skrypty z punktów 2 i 4 podlegają tej decyzji bez zmian.
- **WAY-160** — „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run […]. The gate's run is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it.” Punkt 4 zmienia, czym agent prowadzący uruchamia bramkę, nie kto ją uruchamia.
- **WAY-331** — „The audit of the process is a part of the-way of its own, `process-audit`, with a directory of its own, `process-audit/`, apart from the part of the task cycle.” Skrypty z punktów 2 i 4 działają w cyklu, więc stoją w `task-cycle/`; ich odczyt w audycie stoi w `process-audit/`.
- **WAY-341** — „The audit runs once a week, in a session of its own apart from the user's weekly review. The counting runs without a human on the night from Friday to Saturday, and a weekly task in the user's backlog starts the session.”
- **WAY-38** — „Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format.”
- **WAY-328** — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.”

## Settlements to record

Candidates: 10 shown, 8 accepted — 2026-11-12

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Miary mechanizmu liczy osobny skrypt do osobnego pliku w zapisie cyklu, nie nowe kolumny raportu etapów. | decision | decyzja Mariusza z 12.11.2026 w pierwotnym brzmieniu tego zadania („osobny skrypt i osobny plik, nie nowe kolumny raportu etapów. Powód: audyt porównuje cykle tylko w obrębie serii, a decyzja procesu mówi, że zmiana formy raportu etapów zaczyna nową serię; osobny plik omija ten spór bez zmiany decyzji”); nie wybrane, z sekcji 8 raportu o usprawnieniach: nowe kolumny w raporcie etapów — zmiana formy raportu zaczyna nową serię (WAY-339); dopisanie do WAY-339 zdania, że dodanie kolumn serii nie zaczyna — osobny plik omija spór bez zmiany decyzji | czy późniejsza zmiana może dopisać te miary jako kolumny `stages.md` |
| 2 | Cotygodniowe liczenie audytu czyta miary mechanizmu i czasy bramki z zapisów cykli i pokazuje je z medianą każdej wersji procesu i porównaniem z poprzednią wersją tej samej serii. | decision | pytanie o to, czy liczenie ma czytać nowe liczby | czy wynik audytu ma te miary porównywać, czy tylko wypisać |
| 3 | Nową serię miar mechanizmu i czasów bramki zaczyna tylko zmiana przyrządu, który je mierzy; zmiana instrukcji cyklu jej nie zaczyna. Zmienia WAY-339. | decision | pytanie o to, co zaczyna nową serię tych miar | czy zmiana instrukcji recenzenta dzieli serię tych miar, jak dzieli serię kosztu |
| 4 | Agent prowadzący cykl uruchamia bramkę produktu przez skrypt procesu, który zapisuje czas całego przebiegu i czasy katalogów do pliku w zapisie cyklu. | decision | pytanie o to, skąd zapis cyklu bierze czasy bramki | czy agent może uruchomić bramkę z pominięciem skryptu albo przepisać czasy ręcznie |
| 5 | Audyt porównuje czasy bramki tylko z przebiegów, przy których nie biegła żadna inna bramka; resztę pokazuje osobno. | decision | pytanie o to, jak porównywać czasy bramki | mediana wszystkich przebiegów albo najkrótszy przebieg wersji |
| 6 | Plik zapisu cyklu, który liczenie audytu czyta z historii gita — raport etapów, plik miar i plik czasów bramki — a w którym brakuje pola, daje wartości z niego nieznane, wynik zapisany i kod 1 z linią `Error:` nazywającą plik i pole, zamiast kodu 2 bez wyniku. Zmienia WAY-344. | decision | pytanie o raport, który nie pasuje do żadnej formy; rozszerzenie na plik miar i plik czasów bramki — Mariusz, 2026-11-12: „tak”; nie wybrane: zostawić tylko raport etapów — niedopasowany plik miar albo czasów bramki z dowolnego dawnego cyklu zatrzymuje cały cotygodniowy wynik | kod 2 bez wyniku, jak każe dziś WAY-344 |
| 7 | Ponowny zapis do pamięci podręcznej liczy się według definicji z weryfikacji: to, co poprzednie wywołanie miało w pamięci, a obecne z niej nie odczytało, najwyżej tyle, ile obecne zapisało, powyżej 2 tys. tokenów i bez skurczenia kontekstu o 30% lub więcej. | decision | pytanie o definicję ponownego zapisu | która z dwóch definicji, i czy zwinięcie rozmowy liczy się jako ponowny zapis |
| 8 | Koszt cyklu, którego raport etapów nie ma sekcji szczegółowej, liczy się z tabeli tokenów według modelu tym samym cennikiem; udział rund poprawek jest dla niego nieznany. | decision | punkt 1 *To do*; WAY-337 nie mówi, z której tabeli raportu liczy się koszt | czy następna zmiana audytu może porzucić odczyt starszej formy jako zbędny |

## Out of scope

- Wydłużenie przechowywania zapisów sesji — zrobione ustawieniem z 12.11.2026.
