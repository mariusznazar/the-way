---
title: "the way: przegląd całej zmiany — pytanie o strukturę kodu, stopień uwag o formie wpisu, podstawa reguły o klasie recenzenta"
status: draft
created: 2026-11-12T17:54
updated: 2026-11-12
tags: [zadanie]
related: "the project note of the process work (a private note)"
---

## Po co to

- **Jak jest dziś:** Przegląd całej zmiany nie pyta o strukturę kodu, więc funkcje rosną niezauważone — w grze jedna ma 456 linii, druga 781. Ta sama uwaga recenzenta o formie wpisu fundamentu raz blokuje scalenie, raz jest drobna: w eksperymencie z recenzentami była blokująca w 9 przebiegach i drobna w 8, a sześć przebiegów odrzuciło zmianę wyłącznie za formę. Reguła „recenzent nie na tańszym modelu niż agent prowadzący” obowiązuje, ale nie ma zapisanej podstawy.
- **Kto to odczuwa:** Ja, gdy runda poprawek idzie za samą formę wpisu, i gdy przy rozmowie o kosztach wraca pomysł tańszego recenzenta. Kod gry, który rośnie w kilku miejscach bez pytania, czy to dobre miejsce.
- **Co jeśli nic:** Werdykt przeglądu dalej zależy od losu: każde odrzucenie za samą formę to runda poprawek i ponowna recenzja. Rozrost funkcji wychodzi dopiero w osobnej analizie. Regułę o recenzencie trzeba będzie sprawdzać od zera przy następnej rozmowie o kosztach.

# the way: przegląd całej zmiany — pytanie o strukturę kodu, stopień uwag o formie wpisu, podstawa reguły o klasie recenzenta

Status: ready for cycle
Project relation: independent

## Description

### Need

- Przegląd całej zmiany — jedyny przegląd, który przed otwarciem prośby o scalenie czyta całą zmianę zadania — nie pyta o strukturę kodu, więc funkcje rosną niezauważone: w grze jedna ma 456 linii, druga 781 (wg notatki tego zadania).
- Recenzent czyta różnicę, a różnica pokazuje dodane linie, nie rozmiar funkcji ani pliku, do których trafiły.
- Ta sama uwaga recenzenta o formie wpisu fundamentu raz blokuje scalenie, raz jest drobna: w eksperymencie z recenzentami była blokująca w 9 przebiegach i drobna w 8, a sześć przebiegów odrzuciło zmianę wyłącznie za formę (wg raportu z eksperymentu).
- Instrukcja recenzenta ustala stopień dla rozjazdu wpisu z kodem (`task-cycle/review/SKILL.md:117-120`, WAY-263) i dla brakującego hasła słownika (`:121-125`, WAY-297), a o odstępstwie wpisu od formy szablonu nie mówi nic.
- Reguła „recenzent nie na tańszej klasie modelu niż agent prowadzący” (WAY-229) obowiązuje, ale jej uzasadnienie nie podaje żadnego pomiaru.
- Odbiorcą jest Mariusz: runda poprawek idzie za samą formę wpisu, a przy rozmowie o kosztach wraca pomysł tańszego recenzenta; oraz kod produktu, który rośnie w kilku miejscach bez pytania, czy to dobre miejsce.

### To do

1. `task-cycle/review/whole_change.md` dostaje punkt: recenzent całej zmiany ocenia, co zmiana zostawia w strukturze kodu — wzrost funkcji albo pliku, kod, który po zmianie nie ma użytkownika, nazwę, która przestała być prawdą.
2. Recenzent całej zmiany ma do tego punktu liczby: skrypt the way w `task-cycle/`, z testami, podaje dla zakresu commitów liczbę linii każdego zmienionego pliku przed zmianą i po niej; funkcje i pliki ponad progiem podaje test reguły rozmiaru produktu (To do 3), który recenzent uruchamia na stanie sprzed zmiany i po niej.
3. `product-guidelines/coding/template.md` dostaje wymaganą regułę rozmiaru funkcji i pliku (pytanie 4): osobną regułę z własnym niezmiennikiem i własnym testem, poza zestawem reguł lintera, którego test przy niepowodzeniu wymienia każdą funkcję i plik ponad progiem z ich rozmiarem; `product-guidelines/coding/settle.md` dostaje pytanie o progi, zadawane po próbie na istniejącym kodzie produktu, i o wyjątki zapisane w decyzji; produkt, który ma już wytyczne, dostaje regułę rozszerzeniem wytycznych, jak reguły o awariach i logach (WAY-278).
4. `task-cycle/review/SKILL.md`, sekcja 3, mówi, że znalezisko o strukturze kodu poniżej progu z wytycznych produktu jest drobne, a jego zakres ocenia recenzent jak każdej uwagi; dziennik decyzji dostaje o tym decyzję (przez `record-decision`), która zawęża WAY-161 tak jak WAY-297.
5. Plan zadania (`task-cycle/plan/SKILL.md`) każe, gdy kawałek dopisuje do funkcji albo pliku ponad progiem z wytycznych produktu, zacząć od kawałka, który wydziela część tej funkcji albo pliku bez zmiany zachowania, i zapisać to w tabeli wyborów planu; instrukcja autora zmiany bez planu (`task-cycle/change/SKILL.md`) każe w takim przypadku zrobić wydzielenie pierwszym commitem (pytanie 6).
6. `task-cycle/review/SKILL.md`, sekcja 3, mówi, że uwaga, iż wpis fundamentu odstępuje od formy szablonu, gdy treść wpisu zgadza się z kodem, jest drobna, chyba że recenzent wskaże zdanie, które czytelnik przez to odstępstwo odczyta źle (pytanie 2); dziennik decyzji dostaje o tym decyzję (przez `record-decision`), która zawęża WAY-161 tak jak WAY-297.
7. WAY-229 (przez `record-decision`), bez zmiany zdań wiążących:
   - w *Rationale* wynik pomiaru z jego warunkami: na czterech scalonych zmianach jednego produktu (959–1740 dodanych linii każda), po dwa przebiegi każdego wariantu na każdej zmianie, czyli 8 przebiegów na wariant; recenzenci czytali kod i uruchamiali własne skrypty, ale nie mogli uruchomić testów produktu, i pracowali na instrukcji recenzenta nowszej niż recenzowane zmiany; recenzent tańszej klasy (Sonnet 5.5) wystawił PASS w 4 z 8 przebiegów, za każdym razem zmianie, w której pierwotna recenzja znalazła wadę blokującą, później naprawioną, a recenzent klasy agenta prowadzącego (Opus 5.5), czytający raport autora, w 1 z 8;
   - w *Rejected* wariant „dwa przebiegi recenzenta tańszej klasy zamiast jednego przebiegu klasy agenta prowadzącego” z wynikiem: oba przebiegi razem złapały 5 z 14 błędów wzorcowych, tyle co jeden przebieg klasy agenta prowadzącego (5 i 6), i nie poprawiły werdyktu — zmianie z trzema wadami blokującymi oba wystawiły PASS.
8. WAY-164 (przez `record-decision`), bez zmiany zdań wiążących, dostaje w *Rejected* wariant „recenzja bez raportu autora” z wynikiem: recenzent klasy agenta prowadzącego bez raportu autora złapał 4 i 3 z 14 błędów wzorcowych, z raportem 5 i 6, i zużył więcej tokenów (112,47 mln wobec 90,20 mln w ośmiu przebiegach); warunki pomiaru nie są powtarzane, tylko odesłane jednym zdaniem do WAY-229 (pytanie 7).

### Questions to settle

- 1. Czy to jedno zadanie, czy dwa: struktura kodu (To do 1–5) osobno od stopnia uwag o formie i podstawy reguły o klasie recenzenta (To do 6–8)?
  - Answer: jedno zadanie.
  - Not chosen:
    - dwa zadania — „w przypadku podziału będzie wolniejsza, droższa i prawdopodobnie bez wpływu na jakość”; podział miałby sens tylko wtedy, gdy realizacja byłaby szybsza, tańsza i lepsza.
  - Source: Mariusz, 2026-11-12, „ja chcę je po prostu zrobić, nie ma znaczenia czas i że zajmie więcej; rozdzielenie miałoby dla mnie sens tylko wtedy kiedy spowodowałoby, że realizacja będzie szybsza, tańsza i lepsza”.
- 2. Jaki stopień ma uwaga recenzenta, że wpis fundamentu odstępuje od formy szablonu, gdy treść wpisu zgadza się z kodem?
  - Answer: drobna, chyba że recenzent wskaże zdanie, które czytelnik przez to odstępstwo odczyta źle; z takim zdaniem uwaga ma stopień jak każda inna — ten sam wzór co dla brakującego hasła słownika (WAY-297). Rozjazd treści wpisu z kodem zostaje ważny (WAY-263).
  - Not chosen:
    - zawsze drobna — odstępstwo od formy, przez które czytelnik zrozumie wpis źle (np. reguła wiążąca w uzasadnieniu zamiast w zdaniu wiążącym), też nie blokuje, a w przeglądach po przeglądzie całej zmiany nie jest poprawiane.
    - zawsze ważna, czyli blokuje — każde odstępstwo od formy to FAIL i runda poprawek, a nieudana poprawka daje prośbę zablokowaną za samą formę (WAY-162); w eksperymencie dotyczyłoby 6 z 32 przebiegów.
  - Source: Mariusz, 2026-11-12, „B” (wariant „drobna, chyba że recenzent wskaże zdanie, które czytelnik odczyta źle” z pytania z trzema wariantami).
- 3. Czy znaleziska o strukturze są domyślnie poza zakresem zadania — co zmienia regułę WAY-161, według której o zakresie rozstrzyga recenzent przy każdej uwadze — i co dokładnie znaczy „blokują po przekroczeniu progu”?
  - Answer: znalezisko o strukturze kodu poniżej progu z wytycznych produktu jest zawsze drobne, tak jak uwaga o brakującym haśle słownika (WAY-297); zakres ocenia recenzent jak dziś (WAY-161), więc pozostałość zostawiona przez samą zmianę idzie do poprawki uwag drobnych, a przebudowa kodu sprzed zmiany na listę w prośbie. Przekroczenie progu zatrzymuje test reguły rozmiaru, a gdy jej niezmiennik jest oznaczony jako naruszony — recenzja (WAY-51).
  - Not chosen:
    - recenzent ocenia znaleziska o strukturze jak każde inne — uwaga o strukturze może zablokować zmianę i dać rundę poprawek, z tą samą losowością stopnia co dziś przy formie wpisu.
    - znaleziska o strukturze zawsze poza zakresem zadania, na listę w prośbie i do przeglądu fundamentu (zdanie z notatki tego zadania) — kod bez użytkownika i nieprawdziwą nazwę, które zostawiła sama zmiana, sprząta dopiero osobne zadanie po przeglądzie fundamentu, pełnym cyklem.
  - Source: Mariusz, 2026-11-12, „ok niech będzie C” (wariant „zawsze drobna, chyba że przekracza próg” z pytania z trzema wariantami, przy którym przytoczono zdanie notatki „znaleziska o strukturze są domyślnie poza zakresem zadania”).
- 4. Czy reguła rozmiaru funkcji i pliku jest w szablonie wytycznych kodowania wymagana (produkt przyjmuje ją albo odstępuje od niej decyzją z powodem), czy tylko proponowana, i jak trafia do produktu, który ma już wytyczne?
  - Answer: wymagana. Produkt przy pisaniu wytycznych ustala progi po próbie na własnym kodzie, a funkcje, których dzielić nie warto, dostają wyjątek zapisany w decyzji; reguła ma własny niezmiennik i test (osobny przebieg narzędzia z samymi regułami rozmiaru, poza zestawem reguł lintera); gdy kod już przekracza próg, niezmiennik jest oznaczony jako naruszony do czasu sprzątania (WAY-51); produkt, który ma już wytyczne, dostaje regułę zwykłym rozszerzeniem wytycznych, jak reguły o awariach i logach (WAY-278).
  - Not chosen:
    - reguła proponowana jako „dalsza reguła” produktu, bez decyzji o odstępstwie — produkt bez reguły nie ma progu, więc blokowanie po progu i zmiana w planie zadania nic tam nie robią; WAY-202 odrzuca ten wariant dla linterów: „a skill that only proposes the checks leaves it so for as long as nobody takes the proposal up”.
    - bez reguły w szablonie, samo pytanie o strukturę w przeglądzie — nic nie blokuje, a ocena struktury zależy od recenzenta, z tą samą losowością co dziś przy uwagach o formie.
  - Source: Mariusz, 2026-11-12, „jestem za A” (wariant „reguła wymagana” z pytania z trzema wariantami).
- 5. Gdzie stoi polecenie produktu, które podaje rozmiary funkcji: reguły procesu nie pozwalają dziś wytycznym nazywać polecenia narzędzia obok bramki (WAY-16), a jedyny wyjątek ma własną decyzję (WAY-254).
  - Answer: nigdzie — produkt nie ma osobnego polecenia. Recenzent całej zmiany uruchamia test reguły rozmiaru jako zwykły test pakietu produktu, na stanie sprzed zmiany i po niej; szablon wymaga, żeby ten test przy niepowodzeniu wymieniał każdą funkcję i plik ponad progiem z ich rozmiarem; rozmiary plików przed zmianą i po niej podaje skrypt the way (To do 2). WAY-16 zostaje bez zmiany.
  - Not chosen:
    - polecenie produktu w regule rozmiaru, które dla plików zmiany wypisuje rozmiar każdej funkcji, uruchamiane przez orkiestratora przed przeglądem całej zmiany — nowa decyzja z drugim wyjątkiem od WAY-16, drugie polecenie w każdym produkcie i krok orkiestratora w każdym cyklu, za liczbę o funkcjach poniżej progu, które według progu są w porządku.
  - Source: Mariusz, 2026-11-12, „ok B” (wariant „bez polecenia produktu” z pytania z dwoma wariantami).
- 6. Co robi plan, gdy zmiana dopisuje do miejsca ponad progiem: odsyła do specyfikacji (zmienia WAY-135) czy zaczyna od kawałka „zrób miejsce” (wydzielenie bez zmiany zachowania)?
  - Answer: zaczyna od kawałka „zrób miejsce”: plan zaczyna od kawałka, który wydziela część funkcji albo pliku ponad progiem bez zmiany zachowania, a dopiero następny kawałek dopisuje nową funkcję; autor zmiany bez planu robi to samo pierwszym commitem. To wybór, jak zrobić zmianę, zapisywany w tabeli wyborów planu; WAY-135 zostaje bez zmiany.
  - Not chosen:
    - otwarty wybór projektowy, czyli specyfikacja przed kodem — dwa dodatkowe etapy (projektant i recenzent specyfikacji) przy każdym takim dopisaniu i zmiana WAY-135, której uzasadnienie wiąże specyfikację z wpisem fundamentu projektowanym przez agenta.
    - bez zmiany w planie — gdy niezmiennik reguły rozmiaru nie jest naruszony, przekroczenie wychodzi dopiero w bramce po napisaniu kodu; gdy jest naruszony, dopisanie do funkcji jeszcze nieposprzątanej nie zatrzymuje ani test, ani recenzja (WAY-51 pilnuje tylko plików posprzątanych i nowych).
  - Source: Mariusz, 2026-11-12, „B” (wariant „najpierw zrób miejsce” z pytania z trzema wariantami).
- 7. W której decyzji zapisać odrzucony wariant „recenzja bez raportu autora”: w WAY-229 (klasa modelu) czy w WAY-164 (to ona ustala, że przegląd czyta raport autora)?
  - Answer: w WAY-164, z jednym zdaniem odsyłającym do warunków pomiaru opisanych w WAY-229 zamiast ich powtórki.
  - Not chosen:
    - w WAY-229, razem z resztą wyników eksperymentu — WAY-229 odpowiada na pytanie o klasę modelu, a „bez raportu autora” nie jest odpowiedzią na nie; kto zechce zabrać recenzentowi raport, zajrzy do decyzji o raporcie i wyniku tam nie znajdzie.
  - Source: Mariusz, 2026-11-12, „B” (wariant „w WAY-164” z pytania z dwoma wariantami).

## Context

- Źródła, wszystkie w prywatnych notatkach Mariusza: tabela działań w prywatnym raporcie o usprawnieniach procesu, wiersz D11, i tabela konfliktów w tym samym prywatnym raporcie; karty karta D2 prywatnego raportu o architekturze gry, karta D3 tego raportu i karta D8 tego raportu raportu o architekturze gry; karty karta D2 prywatnego raportu o eksperymencie z recenzentami i karta D3 tego raportu raportu o eksperymencie z recenzentami.
- Karty sprawdzone z dziennikiem decyzji procesu na `foundations` @ `2292f33`, 2026-11-12; wynik w pozycjach niżej.
- Odczyt fundamentu przy doprecyzowaniu nie był pełny: *Scope* 196 z 304 decyzji nazywa części, których dotyka zadanie (`task-cycle`, `product-guidelines`), a w całości przeczytane zostały 47 z nich, wybrane po tytułach i wyszukiwaniu słów; kolizję z pozostałymi znajduje przeszukanie całego fundamentu, które cykl robi przy zapisie każdego wiersza (WAY-33).
- Uwaga drobna w zakresie zadania, którą wymienia przegląd całej zmiany, i tak jest poprawiana przed otwarciem prośby — jedną poprawką i jednym jej przeglądem (WAY-161), więc stopień „drobna” nie usuwa rundy poprawek w tym przeglądzie.
- Stopień „drobna” zmienia trzy rzeczy: werdykt (PASS zamiast FAIL); skutek nieudanej poprawki — poprawka samych uwag drobnych jest cofana, a prośba otwiera się niezablokowana, zamiast prośby zablokowanej (WAY-162); oraz los uwagi w późniejszych przeglądach (kroku zwrotnego, uzgodnienia z gałęzią docelową, poprawki po uwagach człowieka) — tam uwaga drobna nie jest poprawiana i idzie na listę w prośbie.
- Skrypt sprawdzający fundament (`elements/common/foundation_check.py`) zgłasza brak pola i słowo, którego pole nie przyjmuje; pozostałe reguły formy z szablonów — na przykład zakaz dokumentu zadania w polu *Origin* (`elements/decisions/template.md`, sekcja „Origin”) — ocenia tylko recenzent.
- Przegląd fundamentu czyta każdą niepoprawioną uwagę z opisów scalonych próśb, także uwagi poza zakresem zadania (WAY-303), więc droga „lista w prośbie → przegląd fundamentu” już istnieje.
- Reguła zestawu lintera blokuje tylko wtedy, gdy każde jej zgłoszenie prowadzi do zmiany kodu wartej zrobienia (WAY-203); dziennik dwa razy odrzucił próg liczbowy jako regułę: udział mutacji wykrytych przez testy („a number to chase”, WAY-252) i próg słów albo linii skilla („a count says nothing of whether a step needs a fragment”, WAY-256).
- Uzasadnienie decyzji może podać pomiar z tym, co mierzono i w jakich warunkach (WAY-05), ale nie wskazuje źródła, którego czytelnik repozytorium nie otworzy (WAY-27); raport z eksperymentu leży w prywatnych notatkach, więc wynik opisuje się we wpisie, a *Origin* zostaje `none`.
- Modele w eksperymencie: Opus 5.5, Sonnet 5.5 i Fable 5.2 (wg pliku z tokenami w danych eksperymentu).
- the way odstępuje od własnych wytycznych kodowania i testów (WAY-328), więc nowy skrypt i jego testy na nie nie czekają.
- Wzór skryptu: `task-cycle/slice_size.py` z testami w `task-cycle/test_slice_size.py`.
- Zadanie „the way: przegląd fundamentu, którego nie da się pominąć” dodaje do przeglądu fundamentu część o strukturze kodu i korzysta z liczb, które daje to zadanie.

## Questions carried to cycle

- Kto uruchamia skrypt rozmiarów plików z To do 2: orkiestrator, który dołącza wynik do zlecenia przeglądu całej zmiany, czy sam recenzent.
- Gdzie wśród reguł wymaganych szablonu wytycznych kodowania stoi reguła rozmiaru i jak brzmi niezmiennik, który szablon dla niej proponuje.

## Human actions

none

## Decisions in play

- **WAY-229 — On which class of model do the executor of a slice and the one author work?** Zadanie zmienia *Rationale* i *Rejected* (To do 7); zdania wiążące zostają.
  > … while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every reviewer — the review of the whole change and the review of the return step included — work on no class cheaper than the orchestrator's.
- **WAY-164 — What does the author of a change check of its own work before review?** Zadanie dopisuje do *Rejected* wariant „recenzja bez raportu autora” z wynikiem (To do 8); zdania wiążące zostają.
  > The review that judges the work — a slice's own review where it has one, otherwise the review of the whole change — reads that report, and the request lists what each such check showed among its test evidence.
- **WAY-161 — Which findings of the review of the whole change are fixed, and how does the request carry the rest?** Bez zmiany treści; wiersze 1 i 2 *Settlements to record* zawężają go, tak jak WAY-297.
  > In the review of the whole change on either route, a finding blocks when the reviewer grades it Critical or Important and has not itself marked it as outside the task's scope, and a Minor finding that the review lists and the reviewer has not marked so is fixed before the request opens — in the fix that runs for the blocking findings or, where none blocks, in one fix of its own that WAY-162 bounds.
- **WAY-297 — How does a reviewer grade a finding about a missing glossary entry or a missing qualifier?** Bez zmiany; wzór dla wierszy 1 i 2.
  > A reviewer grades as Minor a finding that a word needs a glossary entry, or that a word of the process lacks the qualifier WAY-104 gives it in a product's foundation, unless the finding cites a sentence the files hold that a reader would read wrongly for lack of it; a finding that cites such a sentence is graded as any other.
- **WAY-263 — Which foundation mismatches are Important findings?** Bez zmiany; wiersz 2 dotyczy tylko formy przy treści zgodnej z kodem.
  > A reviewer grades as Important a finding that a change departs from a foundation entry it writes or changes: the change's files do what the entry forbids, fail to do what it requires, or restate it differently, including more broadly or without a qualification.
- **WAY-51 — What does the main branch hold where the product does not meet an invariant?** Bez zmiany; wiersz 5 zamyka przed kodem lukę dla pliku jeszcze nieposprzątanego.
  > While an invariant is marked violated, no second invariant compares the product with its state on `{fork-point}`, and the review of each change to the files of the parts the invariant names keeps a cleaned file or a new one from breaking it again until the mark is cleared.
- **WAY-135 — When does a task's cycle write a spec?** Bez zmiany (pytanie 6).
  > A task's cycle writes a spec, reviewed by an agent other than its author, before implementation and any plan where the task leaves an open design choice and nowhere else, and an invariant whose sentence a row of the task's *Settlements to record* or a projected entry of its sources gives leaves none.
- **WAY-16 — How are the checks of invariants run?** Bez zmiany (pytanie 5).
  > One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.
- **WAY-271 — Which rules on failures and logs does the template of the coding discipline require?** Bez zmiany; wzór dla wiersza 3.
  > The template of the coding discipline requires six rules on failures and logs in the general file of a product's coding guidelines, after the rules of its standing checks, each under a heading of its own …
- **WAY-278 — How do the rules on failures and logs reach a product that has coding guidelines?** Bez zmiany; wiersz 3 bierze tę samą drogę.
  > The rules on failures and logs reach a product that has coding guidelines by an ordinary extension, with no route of their own. A refresh that finds them missing proposes them: the human's yes makes the task an extension, and the human's no is a departure with its reason.
- **WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?** Bez zmiany.
  > A rule names an invariant only where a cheap test of the product's suite checks the rule on a convention of the product's code; a rule no such test can check names none, and the review of each change the rule reaches compares the change with it.
- **WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?** Bez zmiany.
  > The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason.
- **WAY-203 — Which rules of a linter's set block a change of a product's code?** Bez zmiany; reguła rozmiaru stoi poza zestawem reguł lintera.
  > A rule of a linter's set stands among the rules that block a change in the product's decision adopting the set, and so is checked by the invariant of the one rule of the product's coding guidelines on its linter, only where every report it gives on the product's code leads to a change of code worth making …
- **WAY-05 — How is a decision entry written?** Bez zmiany; ogranicza, jak wynik pomiaru stoi w uzasadnieniu WAY-229 i WAY-164.
  > … a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound …
- **WAY-27 — Where may this repository point for its reasoning?** Bez zmiany; raport z eksperymentu nie jest wskazywany, wynik opisuje się we wpisie.
  > Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.
- **WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?** Bez zmiany; nowy skrypt i jego testy nie czekają na wytyczne.
  > The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.

## Settlements to record

Candidates: 8 shown, 6 accepted — 2026-11-12

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Znalezisko o strukturze kodu poniżej progu z wytycznych produktu jest drobne, a jego zakres ocenia recenzent jak każdej uwagi. | decision | pytanie 3 | czy uwaga o strukturze w zakresie zadania może zablokować zmianę |
| 2 | Uwaga, że wpis fundamentu odstępuje od formy szablonu przy treści zgodnej z kodem, jest drobna, chyba że recenzent wskaże zdanie, które czytelnik przez to odstępstwo odczyta źle. | decision | pytanie 2 | jaki stopień dać uwadze o formie i czy zmiana z taką uwagą dostaje FAIL |
| 3 | Szablon wytycznych kodowania wymaga reguły rozmiaru funkcji i pliku z własnym niezmiennikiem i testem, poza zestawem reguł lintera; produkt ustala progi po próbie na swoim kodzie i wyjątki w decyzji albo odstępuje od reguły decyzją z powodem, a produkt z wytycznymi dostaje ją rozszerzeniem. | decision | pytanie 4 | czy reguła rozmiaru jest wymagana, czy tylko proponowana, i jak trafia do produktu, który ma już wytyczne |
| 4 | Test reguły rozmiaru przy niepowodzeniu wymienia każdą funkcję i plik ponad progiem z ich rozmiarem, recenzent całej zmiany uruchamia go na stanie sprzed zmiany i po niej, a produkt nie ma osobnego polecenia liczącego rozmiary funkcji. | decision | pytanie 5 | czy dopisać do wytycznych polecenie produktu obok bramki, wbrew WAY-16 |
| 5 | Gdy zmiana dopisuje do funkcji albo pliku ponad progiem, plan zaczyna od kawałka, który wydziela jej część bez zmiany zachowania, a autor zmiany bez planu robi to pierwszym commitem. | decision | pytanie 6 | czy taki przypadek odsyłać do specyfikacji, czy pisać kod od razu |
| 6 | Recenzent całej zmiany ocenia, co zmiana zostawia w strukturze kodu — wzrost funkcji albo pliku, kod bez użytkownika, nazwę, która przestała być prawdą — z liczbami linii każdego zmienionego pliku przed zmianą i po niej. | decision | notatka tego zadania przed doprecyzowaniem, „Co zmienić”, punkt 1 („Recenzent dostaje liczby (rozmiary funkcji i plików dotkniętych zmianą) i pytanie o strukturę”); To do 1–2; Mariusz, 2026-11-12, „przyjmuję zgodnie z rekomendacją” | czy przegląd całej zmiany w ogóle pyta o strukturę i co obejmuje to pytanie |

## Out of scope

- Przyjęcie reguły rozmiaru i ustalenie progów w grze — osobne zadanie w backlogu gry.
- Część o strukturze kodu w przeglądzie fundamentu — zadanie „the way: przegląd fundamentu, którego nie da się pominąć”.
- Zdania wiążące WAY-229: reguła o klasie recenzenta zostaje bez zmiany.
