---
title: "the way: drobne poprawki z przeglądu warstwy AI i audytu procesu — źródło faktu bez kopii w archiwum, własne wyszukiwanie w kroku powrotu, miary audytu dla całej serii, fałszywe katalogi w czasach bramki"
status: accepted
created: 2026-11-21T12:00
updated: 2026-11-21
tags: [zadanie]
related: "a link to the project note of the work on the process"
---

# the way: drobne poprawki z przeglądu warstwy AI i audytu procesu — źródło faktu bez kopii w archiwum, własne wyszukiwanie w kroku powrotu, miary audytu dla całej serii, fałszywe katalogi w czasach bramki

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/106

## Description

### Need

- Szablon faktów o środowisku nie mówi, jak podać źródło publicznego stanu cudzej usługi (np. widoczności repozytorium na GitHubie), gdy strona nie ma kopii w archiwum internetu; każdy cykl zapisuje je po swojemu, a recenzent czytający szablon dosłownie może taki fakt zablokować.
- Krok powrotu porównuje z kodem wpisy, „które znalazło wyszukiwanie”, ale nie mówi, czyje to wyszukiwanie; agent kroku powrotu, który sam nie pisze wpisu, nie wie, czy ma szukać, więc niezgodność kodu ze starszą decyzją może przejść niezauważona.
- Cotygodniowy audyt procesu pokazuje miary osobno dla każdej wersji the-way; wersja zmienia się kilka razy dziennie, więc prawie każda ma jeden cykl, a dwa audyty z rzędu (14.11 i 21.11) odłożyły z tego powodu decyzję w punkcie „What each version of the process shows”.
- Skrypt mierzący czasy bramki bierze linie `== <katalog>` z wydruku padającego testu samej bramki za początek nowego katalogu, więc w nieudanych przebiegach zapisuje nieistniejące katalogi i przypisuje katalogowi, w którym test padł, cudzy czas; wynik liczenia audytu niesie przez to kilkadziesiąt wierszy szumu w *Unknown values*.

### To do

1. W `elements/environment-facts/template.md`, sekcja `## Source`, druga forma źródła — punkt zaczynający się od „a page without editions, with the closest archived copy that already exists” (około linii 109–111) — brzmienie:
   - jest: „a page without editions, with the closest archived copy that already exists and its date — never one made for the entry, since that writes to someone else's service — and the place, the passage and the date read;”
   - będzie: „a page without editions, with the closest archived copy that already exists and its date — never one made for the entry, since that writes to someone else's service; where none exists, `no archived copy exists in the Internet Archive's CDX index, checked <date>` — and the place, the passage and the date read. A service's public API address is such a page, and its answer is the passage;”
2. W `task-cycle/skill/return_step.md`, akapit zaczynający się od „It compares with the code the entries the change writes or changes” (około linii 7–8), lista porównywanych wpisów:
   - jest: „It compares with the code the entries the change writes or changes, those the task names and those the search of the foundation found, and the part map of the touched parts, …”
   - będzie: „It compares with the code the entries the change writes or changes, those the task names, those the search of the foundation found and those its own search finds — one search by the names and words the change's code adds, made even where it writes no entry — and the part map of the touched parts, …”
3. W `task-cycle/record_template.md`, sekcja `## Return step`, punkt „Foundation compared with code:” (około linii 204–206), ta sama klauzula:
   - będzie: „- Foundation compared with code: <the entries the change writes or changes, those the task names, those the search of the foundation found and those the return step's own search by the names and words the code adds found, and the part map of the touched parts, each compared with the code: what no longer matched and its correction, or none>”
4. Liczenie audytu (`process-audit/audit_count.py`) podaje dla każdej serii obraz całej serii, każdej z tym, co dziś niesie jej rodzaj, bez Q3 i bez „spada”: seria kosztu — medianę kosztu ze wszystkich jej cykli ze znanym kosztem; seria liczby uwag — odpowiedzi Q1 i Q2 ze wszystkich jej cykli; seria pomiarów mechanizmu — medianę każdego pomiaru; seria czasów bramki — medianę z jej przebiegów porównywanych, a przebiegi nieporównywane osobno (ich liczba i mediana), jak w wierszach per wersja (WAY-350). Odpowiedzi mają postać, którą daje odpowiedź na pytanie o odpowiedzi Q1–Q3 dla grupy cykli niżej. Wiersze per wersja zostają, a ich Q1 przechodzi na tę samą postać liczb cykli (`yes n · no n · unknown n`).
5. Liczenie audytu podaje wewnątrz serii porównanie „przed i po zmianie”: cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii, a o tym, czy wersja ma zmianę, rozstrzyga wersja, nigdy data — dla każdej sprawy rejestru problemów naprawionej (*Fate* `fixed`) z commitem poprawki w *Fix*, w każdej serii, w której po obu stronach poprawki stoją cykle (dla czasów bramki: przebiegi porównywane). Każda strona niesie to, co obraz serii z punktu 4, a porównanie dodaje Q3 (seria kosztu) i „spada” (pomiary mechanizmu i czasy bramki): mediana po poprawce niższa niż przed nią; seria liczby uwag daje dwie strony liczb Q1 i Q2 bez osobnego werdyktu.
6. Punkt 4 „What each version of the process shows” w `process-audit/SKILL.md` (około linii 221) pokazuje przede wszystkim obraz każdej serii i porównania „przed i po” z punktów 4–5, a wiersze per wersja za nimi.
7. `process-audit/SKILL.md` mówi wprost o ograniczeniu: seria liczby uwag zaczyna się od nowa przy każdej zmianie w `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` i `task-cycle/agent-types/the-way-stage.md` oraz przy dacie *Added* albo *Withdrawn* na liście klas rejestru (reguła „Measures are compared inside a series only”, około linii 52–61), więc porównanie „przed i po” dla uwag działa tylko dla poprawek spoza tych plików i dat; dla kosztu działa szeroko, bo jego seria zaczyna się tylko przy nowym cenniku albo zmianie skryptu pomiaru kosztu.
8. `task-cycle/gate_times.py` nie bierze za początek katalogu linii `== …`, które pochodzą z wydruku zagnieżdżonego testu (testu samej bramki, który uruchamia `gate/run_tests.py` i przy porażce drukuje jego wyjście), a katalog, w którym test padł, dostaje własny czas; test w `task-cycle/test_gate_times.py` trzyma ten przypadek.
9. Akapit o przekazaniu pracy między skillami the way (w samym the way sesja czyta plik drugiego skilla zamiast go wywoływać), który the-way#154 powtórzył w 15 plikach skilli, stoi w jednym miejscu i skille go stamtąd czytają — tak jak każe fundament dla wspólnego sposobu pracy (WAY-256 z WAY-35). Po przeniesieniu jedna sesja na the way sprawdza, że agent naprawdę idzie za tym przekazaniem: skill, który przekazuje pracę, prowadzi do przeczytania pliku drugiego skilla, a nie do wywołania go. Źródło: drobne uwagi 4 i 5 w opisie https://github.com/mariusznazar/the-way/pull/154 (punkt dopisany przez doradcę dnia po scaleniu, runda poprawek PR-a wykorzystana).

### Questions to settle

- Jak podać źródło faktu o publicznym stanie cudzej usługi, gdy strona nie ma kopii w archiwum internetu?
  - Answer: drugą formą źródła (strona bez wydań) z zapisem `no archived copy exists in the Internet Archive's CDX index, checked <date>`; publiczny adres API usługi jest taką stroną, a jego odpowiedź — cytatem; brzmienie w punkcie 1 *To do*.
  - Not chosen:
    - Poszerzyć trzecią formę (odczyt poleceniem albo API) o stan cudzej usługi bez kopii w archiwum, ze zmianą decyzji WAY-84 — kopie robione dla wpisu są zakazane, więc warunek „brak kopii” byłby prawie zawsze spełniony i odczyt otworzyłby się dla każdego publicznego API, a miał zostać dla stanu, którego czytelnik bez dostępu nie zobaczy; do tego miesza ustawienie ludzi produktu ze stanem, który ustawieniem nie jest.
    - Wpisać wyjście `gh api` w miejsce cytatu strony z dopiskiem polecenia — cytat strony to tekst, który widzi czytelnik strony; właściwą drogą jest adres publicznego API jako strona.
  - Source: Mariusz, 2026-11-21, przegląd warstwy AI, sprawa AIR-694, wybór „a”.
- Czyje wyszukiwanie fundamentu porównuje z kodem krok powrotu?
  - Answer: także własne — jedno wyszukiwanie po nazwach i słowach, które dodaje kod zmiany, robione nawet wtedy, gdy krok powrotu nie pisze żadnego wpisu; brzmienie w punktach 2–3 *To do*.
  - Not chosen:
    - Dopisać „wyszukiwania, które wymienia raport kroku fundamentu” — formularz raportu (`task-cycle/change/SKILL.md`, około linii 183) każe wymieniać tylko wyszukiwania bez wyniku albo niejasne, więc zdanie odsyłałoby do listy, której nikt nie musi prowadzić.
    - Krok powrotu porównuje tylko to, co znalazł krok fundamentu — kod pisany po kroku fundamentu (nowe polecenia, ścieżki) nie trafiłby na wpisy, które go dotyczą.
  - Source: Mariusz, 2026-11-21, przegląd warstwy AI, sprawa AIR-696, wybór „a”.
- Co pokazuje punkt 4 audytu zamiast samych wierszy per wersja?
  - Answer: obraz każdej serii (to, co niesie jej rodzaj, ze wszystkich jej cykli, bez Q3 i bez „spada”; Q3 i „spada” tylko w porównaniach dwóch grup) oraz porównanie „przed i po zmianie” wewnątrz serii — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii; reguła „Set no number of one series beside a number of another […] and no week's count beside the week before” zostaje bez zmian.
  - Not chosen:
    - Sam obraz serii, bez porównań — mówi, jak jest, ale nie daje podstawy do decyzji, czy zmiana pomogła; audyty dalej odkładałyby ją w tym miejscu.
    - Porównywanie serii z serią — wymaga zmiany reguły, która zabrania stawiać liczby jednej serii obok liczb innej, a różnicę między seriami robi częściowo zmiana narzędzia pomiaru, której nie da się oddzielić od zmiany procesu.
  - Source: Mariusz, 2026-11-21, audyt procesu i zapis zadania („obraz serii plus porównanie »przed i po zmianie« wewnątrz serii”).
- Które zmiany dostają porównanie „przed i po” wewnątrz serii?
  - Answer: każda sprawa rejestru problemów naprawiona (*Fate* `fixed`) z commitem poprawki w *Fix* — ten sam mechanizm co punkt 2 audytu („What came back after a fix”), działający bez ręcznego prowadzenia czegokolwiek; zmiana procesu bez sprawy w rejestrze nie dostaje porównania.
  - Not chosen:
    - Każde scalenie PR-a do `foundations` — dziesiątki porównań na serię, większość z jednym cyklem po jednej stronie, czyli ten sam szum, który dziś blokuje decyzję.
    - Zmiany wskazane w trakcie audytu, z ponownym uruchomieniem liczenia z podanym commitem — nowa opcja liczenia i krok w skillu, a porównanie powstaje tylko na prośbę i nie ma go w wyniku liczenia uruchamianego według harmonogramu.
    - Nowa tabela „zmiany do oceny” w rejestrze — zmiana szablonu rejestru i jego czytnika, dopisanie tabeli do rejestru ręcznie i jej ręczne prowadzenie; nie dokładana, dopóki nie wiadomo, że sprawy naprawione nie wystarczają, a dołożenie później jest tanie.
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „a — porównanie »przed i po« dostaje każda naprawiona sprawa z rejestru problemów (z commitem poprawki). To ten sam mechanizm co punkt 2 audytu, działa bez ręcznego prowadzenia czegokolwiek; d nie dokładamy, dopóki nie wiadomo, że a nie wystarcza — wycofanie tanie.”
- Jak wyglądają odpowiedzi Q1–Q3 dla grupy wielu cykli (obraz serii i każda grupa porównania „przed i po”)?
  - Answer: liczby zamiast jednego słowa, w jednej formie wszędzie: Q1 dla każdej grupy cykli — wersji, obrazu serii i każdej strony porównania „przed i po” — to liczba cykli z każdą odpowiedzią (`yes n · no n · unknown n`); Q2 to sumy odcinków planowanych i zbyt dużych z odpowiedzią z tych sum, jak dziś dla wersji; Q3 i „spada” pomiarów mechanizmu i czasów bramki stoją tylko tam, gdzie są dwie grupy — wersja wobec poprzedniej wersji serii, jak dziś, i mediana po poprawce wobec mediany przed nią; obraz serii daje medianę i liczbę cykli ze znaną wartością, bez Q3.
  - Not chosen:
    - Te same reguły co dla wersji, przyłożone do całej grupy — Q1 w każdej dłuższej serii wychodzi prawie na pewno `yes`, bo wystarczy jeden cykl, a Q3 w jednej grupie nie ma z czym porównać.
    - Liczby tylko dla obrazu serii i porównań „przed i po”, a w wierszach per wersja Q1 jak dziś — dwie postaci tej samej odpowiedzi w jednym wyniku.
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „b — liczby zamiast jednego słowa; tylko tak audyt pokazuje stan taki, jaki jest, a »spada« liczy się tam, gdzie są dwie grupy. Słaby punkt (dwie postaci Q1) usuń, zamiast go przyjmować: Q1 w wierszach per wersja też liczbami (tak · nie · nieznane), jeśli to zmienia tylko formę wyniku liczenia, a nie zapisane dane ani coś, co ten wynik czyta maszynowo”; warunek sprawdzony 2026-11-21: wynik liczenia czytają tylko `process-audit/audit_report.py` (który go pisze), `process-audit/SKILL.md` (człowiek) i `process-audit/test_audit_count.py` w the-way @ `19e5774a`, a żaden skrypt vaulta nie czyta jego kolumny Q1; żadna decyzja fundamentu nie ustala formy odpowiedzi Q1.

## Context

- Źródła punktów 1–3 *To do*: sprawy AIR-694 i AIR-696 przyjęte 2026-11-21 w przeglądzie warstwy AI (zeszyt `ai_review_ledger.md` w obszarze `(A) Claude code`, po 14 dniach w `ai_review_ledger_archive.md`).
- Źródło punktów 4–8 *To do*: audyt procesu 2026-11-21 (wynik w miejscu, które podaje klucz `audit_results` pod `the-way` w pliku lokalizacji, plik `audit-2026-11-21.md`, sprawy 4).
- Numery linii są podpowiedzią ze stanu `origin/foundations` @ `19e5774a`; brzmienia w punktach 1–3 *To do* zgadzają się z tym stanem (sprawdzone 2026-11-21).
- Wzór zapisu z punktu 1 już stoi w loop2: `foundations/environment_facts.md`, fakt `loop2-repository-visibility` (około linii 724) i widoczność repozytorium `screenshots` (około linii 814), np. „**Source:** https://api.github.com/repos/mariusznazar/loop2 (no archived copy exists in the Internet Archive's CDX index, checked 2026-11-08) § the repository object, field `visibility` — `"visibility":"public"`; read 2026-11-14”.
- Skąd sprawa z punktu 1: loop2 PR #97, zapis cyklu `serwer-odczyty-i-straznik` (`loop2@f2056ce:docs/task-cycles/serwer-odczyty-i-straznik/cycle.md`, linie 202, 203, 208); ten sam brak zgłosił cykl `przywrocic-decyzje-drogi-agenta` z 16.11.
- WAY-84 odrzuca dla ustawienia, które pokazuje tylko strona po zalogowaniu, stronę bez wydania i bez kopii w archiwum, bo nikt poza autorem nie porówna źródła z cytatem; publiczny adres API takiego problemu nie ma, bo czyta go każdy.
- Skąd sprawa z punktów 2–3: loop2 PR #96, zapis cyklu `programy-ze-starych-zapisow` (`loop2@2fe204e:docs/task-cycles/programy-ze-starych-zapisow/cycle.md`, linia 224); `elements/common/way_of_working.md` (sekcja „2. Search the foundation”) każe szukać „once the skill has settled what the entry is”, a krok powrotu, który nie pisze wpisu, takiej chwili nie ma.
- Zlecenie kroku powrotu w tamtym cyklu (`reports/return-step-handoff.md`, linia 13) już kazało szukać samemu, więc punkty 2–3 przenoszą do skilla to, co zlecenie robiło ręcznie.
- `elements/common/way_of_working.md` zostaje bez zmian.
- Porównanie „przed i po” to ten sam mechanizm co ocena poprawki w punkcie 2 audytu (`process-audit/SKILL.md`, reguła „Whether a fix works is read from the version, never from the date”, około linii 79), tylko zbiera wiele wersji naraz.
- Seria to odcinek o stałym narzędziu pomiaru (WAY-339), więc liczenie w jej obrębie nie łamie reguły porównywania tylko wewnątrz serii (`process-audit/SKILL.md`, około linii 52).
- Dziś odpowiedź Q1 dla wersji brzmi `yes`, gdy choć jeden jej cykl daje `yes`, a `no`, gdy każdy daje `no` (`process-audit/version_analysis.py`, `contradiction_of`); Q2 liczy się z sum odcinków planów wersji; Q3 porównuje medianę kosztu z poprzednią wersją tej samej serii.
- Wynik liczenia z 2026-11-21 ma 7 serii kosztu i 54 serie liczby uwag, bo serię uwag przerywa każda zmiana w katalogach recenzenta i autora.
- Przykłady fałszywych katalogów z punktu 8: `a`, `b`, `c` w przebiegach the-way i `tests/one`, `tests/two` w przebiegach loop2, a katalog `gate` z czasem 0,012 s zamiast ok. 43 s; dotyczy 12 przebiegów z 14–15.11 (wynik liczenia `count-2026-11-21.md`, sekcja *Gate runs*).
- Liczenie porównuje tylko przebiegi udane, więc porównywane mediany czasów bramki są czyste; błędne są czasy w kolumnie przebiegów nieporównywanych i wiersze szumu w *Unknown values*.
- Źródłem linii `== a`, `== b/c` itp. są testy `gate/test_run_tests.py`, które uruchamiają `gate/run_tests.py` na przykładowych katalogach i przy porażce drukują jego wyjście.
- Dziś `task-cycle/gate_times.py` bierze każdą linię zaczynającą się od `== ` za początek bloku i pierwszą linię `Ran … tests in …s` po niej za czas bloku; trzymają to testy `test_block_without_a_ran_line_gives_unknown` i `test_first_ran_line_after_its_own_block_counts` w `task-cycle/test_gate_times.py`, a zagnieżdżony wydruk ma własne linie `== …` i `Ran …`, które wyglądają tak samo jak prawdziwe.
- Poprawka z punktu 8 zaczyna nową serię czasów bramki (WAY-339), ale bieżąca seria ma jeden przebieg (stan na 2026-11-21), więc nic nie przepada.
- `Defect introduced by:` dotyczy punktu 8: `task-cycle/gate_times.py` wszedł w PR #106 (commit `54d92324`), a jego opis mówi, że czyta bloki, które otwiera `gate/run_tests.py`, czego linia z wydruku zagnieżdżonego testu nie jest; punkty 1–7 to luki i nowe potrzeby, nie defekty.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-84 — zostaje bez zmian; punkt 1 *To do* zmienia tylko szablon faktów: „The current state of a setting that people of the product change outside its repository — who can open it, a host's access rule — is an environment fact, its source the place where that state is shown, or, where no page open to a reader shows it, a reading. A choice of such a setting is a decision only where the product declares it, and that decision rests on the fact. A fact about the visibility of a repository the product links to names that one repository.”
- WAY-11 — zostaje bez zmian; punkty 2–3 *To do* dopowiadają w skillu, czyje wyszukiwanie: „A task ends with its return step before its branch is merged: an agent compares with the code the foundation entries the change writes or changes, those its task names and those the search of the foundation found, and the part map of the parts the task touched, and corrects in the same change whatever no longer matches. […]”
- WAY-33 — zostaje bez zmian: „When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches […]. The search is not repeated before the merge and leaves no record.”
- WAY-339 — dostaje zdania z wierszy 1–2 *Settlements to record*, bez zmiany tego, co już mówi; punkty 4–7 liczą w obrębie serii: „The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; […]”; poprawka z punktu 8 zaczyna nową serię czasów bramki: „a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process”.
- WAY-350 — punkty 4–5 dokładają porównania czasów bramki ponad wersją, z tym samym ograniczeniem do przebiegów porównywanych: „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.”

## Settlements to record

Candidates: 7 shown, 3 accepted — 2026-11-21

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Punkt 4 audytu pokazuje obraz każdej serii (to, co niesie jej rodzaj, ze wszystkich jej cykli, bez Q3 i bez „spada”; Q3 i „spada” tylko w porównaniach dwóch grup) oraz porównanie „przed i po zmianie” wewnątrz serii — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii. | sentence of WAY-339 | *Questions to settle*: „Co pokazuje punkt 4 audytu zamiast samych wierszy per wersja?” | czy grupowanie po wersji wewnątrz serii wiąże dalej, czy jest tylko formą tego wyniku, którą późniejsza zmiana może zastąpić porównaniem po dacie |
| 2 | Porównanie „przed i po” dostaje każda naprawiona sprawa z rejestru problemów (z commitem poprawki). | sentence of WAY-339 | *Questions to settle*: „Które zmiany dostają porównanie »przed i po« wewnątrz serii?” | po jakich zmianach liczenie rozbiera serię: po każdym scaleniu, po liście prowadzonej ręcznie czy po poprawkach z rejestru |
| 3 | Odpowiedź Q1 dla każdej grupy cykli — wersji, obrazu serii i strony porównania — to liczby cykli (tak · nie · nieznane), a Q3 i „spada” stoją tylko tam, gdzie są dwie grupy. | decision | *Questions to settle*: „Jak wyglądają odpowiedzi Q1–Q3 dla grupy wielu cykli…?” | czy Q1 grupy brzmi `yes`, gdy jeden cykl daje `yes`, jak dziś dla wersji |

## Out of scope

- Zmiana decyzji WAY-84.
- Zmiana `elements/common/way_of_working.md`.
