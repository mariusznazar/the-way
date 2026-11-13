---
title: "the way: miara błędów znalezionych po scaleniu — linia w nagłówku każdego zadania, klasy w rejestrze, przyczyna każdej poprawki po otwarciu prośby"
status: draft
created: 2026-11-12T17:54
updated: 2026-11-12
tags: [zadanie]
related: "the project note of the process"
---

# Miara błędów znalezionych po scaleniu: linia w nagłówku każdego zadania i nazwana przyczyna każdej poprawki po otwarciu prośby

Status: ready for cycle
Project relation: independent

## Description

### Need

- Żadna liczba nie mówi dziś, co przegląd zmiany przepuszcza.
- Rejestr problemów audytu procesu powstaje z raportów cyklu, a błąd, który przeszedł, nie stoi w raportach cyklu, który go wprowadził: wychodzi później, jako zadanie naprawcze albo uwaga Mariusza z gry.
- Nic nie łączy dziś takiej poprawki ze zmianą, która błąd wprowadziła.
- 22 z 57 cykli gry (39%) ma poprawkę po otwarciu prośby i jej przyczyna nie jest nigdzie nazwana, więc nie wiadomo, ile z tych poprawek to błąd przepuszczony przez przegląd, a ile zmiana zdania.
- Odczuwa to Mariusz przy każdej decyzji „taniej” (tańszy model, krótszy przegląd, krótsze wytyczne) oraz audyt procesu, który ma mierzyć „lepiej”, a mierzy tylko to, co cykl sam zgłosił.
- Na tę miarę czekają trzy rzeczy odłożone 12.11.2026: skrócenie wytycznych testów, pomiar modeli etapami i scalanie bez człowieka; miara potrzebuje co najmniej dwóch tygodni danych, zanim da się na niej oprzeć.

### To do

1. Szablon dokumentu zadania (`project-level/task/template.md`) dostaje w nagłówku, pod `Project relation:`, linię `Defect introduced by:` w postaci, którą podaje odpowiedź na pytanie „Jaką postać ma pole…”, z regułą zadania naprawczego z odpowiedzi na pytanie „Które zadanie jest naprawcze…”; skill doprecyzowania zadania każe ją wypełnić w każdym zadaniu. Dokument zadania napisany przed tą linią nie ma jej, a brak linii znaczy „nie oceniano”, nie `none`. Zmianę, która weszła bez prośby, linia nazywa adresem commita.
2. Szablon zapisu cyklu (`task-cycle/record_template.md`) dostaje pozycję z jedną linią na każdą poprawkę po otwarciu prośby — pary źródło · rodzaj i plik uwag w `reports/`, jak podaje odpowiedź na pytanie „Jakie przyczyny ma zamknięta lista…” — a skill poprawki (`task-cycle/skill/correction.md`) każe agentowi prowadzącemu cykl ją dopisać i zapisać uwagi człowieka słowo w słowo do pliku w `reports/`, także gdy przyszły w rozmowie albo dotyczą tylko odświeżenia gałęzi docelowej. Źródło `item <n>` podaje numer rodzaju pozycji z szablonu opisu prośby (np. `item 8` — niepoprawione znaleziska, które człowiek odczuje), nie numer pozycji w danym opisie.
3. Opis prośby po poprawce (`task-cycle/skill/request_template.md`, wariant poprawki) pokazuje pary tej poprawki jednym zdaniem jako pozycję nowego rodzaju w grupie *You accept by merging*; po poprawce sekcja decyzji człowieka nie czyta więc samego `none`.
4. Szablon rejestru problemów (`process-audit/problem_register.md`) dostaje dwie klasy na liście startowej i zdania o kolumnach *Record* i *Stages* dla wiersza po scaleniu, jak podaje odpowiedź na pytanie „Czy szablon rejestru w the way…”, oraz dla wiersza `defect-found-at-request`: *Record* to kopia zapisu, która niesie linię tej poprawki, a *Stages* czyta `at the request`.

### Questions to settle

- Gdzie zapisywać błąd znaleziony po scaleniu?
  - Answer: w obu miejscach — pole w dokumencie zadania naprawczego (która zmiana wprowadziła błąd) jest źródłem, a nowa klasa w rejestrze problemów audytu je liczy.
  - Not chosen:
    - samo pole w dokumencie zadania naprawczego — niczego nie liczy
    - sama nowa klasa w rejestrze, wypełniana przez nocny przegląd — wymaga zgadywania przez nocny przegląd
  - Source: decyzja Mariusza z 2026-11-12 nad pytaniem R6 raportu o usprawnieniach procesu (sekcja 7 tego raportu), zapisana w notatce z rozstrzygnięciami autora: „R6 (gdzie zapisywać błąd znaleziony po scaleniu): wariant (c)”
- Które zadanie jest naprawcze, czyli co liczy się jako błąd znaleziony po scaleniu?
  - Answer: wąsko — naprawcze jest zadanie, które usuwa wadę wobec tego, czego w chwili scalenia wymagało zadanie tamtej zmiany albo fundament, albo regresję, czyli zepsucie czegoś, co działało, a czego zadanie tamtej zmiany nie kazało zmieniać. Nie liczą się nowa potrzeba, zmiana zdania, luka samego zadania (czegoś nie przewidziało) ani konserwacja, np. aktualizacja zależności.
  - Not chosen:
    - szeroko: każde zadanie, które poprawia coś, co scalona zmiana zrobiła źle albo czego nie przewidziała — tania ocena, ale liczba miesza to, co przepuścił przegląd, z tym, czego nie przewidziało doprecyzowanie, więc nie odpowie, czy np. tańszy model przeglądu przepuszcza więcej
    - szeroko, z rodzajem w polu („wada wobec wymagań” albo „luka zadania”) — jedna ocena więcej przy każdym takim zadaniu, druga klasa w rejestrze i drugi wynik do czytania, a na miarę luk zadań dziś nic nie czeka
  - Source: Mariusz, 2026-11-12: „no chyba może być a”
- Jaką postać ma pole: gdzie stoi w dokumencie, czym nazywa zmianę (prośba, commit), co wpisuje zadanie naprawiające kilka błędów z różnych zmian i co, gdy zmiany nie da się ustalić?
  - Answer: linia nagłówka `Defect introduced by:` pod `Project relation:` w każdym zadaniu; czyta `none` w zadaniu, które nie jest naprawcze, adres prośby o scalenie, która wprowadziła błąd, a przy kilku błędach z różnych zmian kilka adresów rozdzielonych ` · `, albo `unknown — <dlaczego nie da się ustalić>`. Zmianę nazywa prośba, nie commit. Ustala ją agent doprecyzowujący zadanie, z historii linii, które poprawka zmienia, i ze zgłoszenia człowieka; nie cykl.
  - Not chosen:
    - linia nagłówka tylko w zadaniu naprawczym — zapomniane pole wygląda tak samo jak zadanie nienaprawcze, więc błąd znika z miary bez śladu
    - pozycja w sekcji *Context* — swobodny tekst, nocny przegląd musiałby rozpoznawać pole w treści, a brak pola jest tak samo niewidoczny
    - commit zamiast prośby — trzeba szukać prośby od commita, a commit nie powie, że zmiana nie przeszła przez prośbę
  - Source: Mariusz, 2026-11-12: „a”, na propozycję postaci pola pokazaną w rozmowie
- Gdzie agent prowadzący cykl zapisuje przyczynę poprawki po otwarciu prośby: w tytule commita kolejnej kopii zapisu cyklu czy w samym zapisie cyklu?
  - Answer: w zapisie cyklu — jedna linia na każdą poprawkę po otwarciu prośby, z przyczyną z listy i odnośnikiem do tego, co poprawkę wywołało (uwagi człowieka, pozycja opisu prośby, ponowne scalenie gałęzi docelowej).
  - Not chosen:
    - tytuł commita, który dodaje kolejną kopię zapisu — nic go nie sprawdza (wiadomości commitów nie są sprawdzane), zderza się z regułami commitów produktu, a przyczyna stoi poza zapisem, który czyta nocny przegląd
    - oba miejsca — dwa zapisy, które mogą się rozjechać, a drugi nic nie dodaje
  - Source: Mariusz, 2026-11-12: „b”
- Jakie przyczyny ma zamknięta lista i co robi agent, gdy żadna nie pasuje?
  - Answer: linia poprawki wymienia raz każdą parę **źródło · rodzaj**, z plikiem uwag w `reports/` zapisu. Źródło jest odczytem: `item <n>` — odpowiedź na pozycję *For you to decide* o tym numerze; `remark` — uwaga człowieka spoza pozycji; `target-branch` — poprawka, która istnieje tylko dla odświeżenia gałęzi docelowej na prośbę człowieka. Rodzaj jest osądem agenta prowadzącego cykl jednym testem w dokumentach: `defect` — to, co poprawka zmienia, wymagało zatwierdzone zadanie albo fundament, albo to regresja (to samo kryterium co przy zadaniu naprawczym); `not-required` — nie było wymagane; `none` — tylko przy `target-branch`. Opis prośby po poprawce pokazuje te pary jednym zdaniem w grupie *You accept by merging*, żeby człowiek widział ocenę agenta przy scalaniu. Z par wychodzą dwie liczby: wada przepuszczona przez przegląd (`remark · defect`) i wada widziana przez cykl i zostawiona (`item · defect`).
  - Not chosen:
    - pięć przyczyn: `defect-missed`, `requirement-changed`, `task-gap`, `raised-by-cycle`, `target-branch`, osądzanych przez agenta — miesza „kto podniósł” z „co było nie tak”; na 20 prawdziwych poprawkach 15 to wyłącznie `raised-by-cycle`, pod którym chowają się prawdziwe wady (plik hasła z dwoma znacznikami kodowania przechodzi start serwera — cykl to wystawił, człowiek kazał poprawić), więc wada przepuszczona przez przegląd wyszłaby bliska zeru; `target-branch` „bez uwag człowieka” nie zachodzi, bo każda poprawka zaczyna się od scalenia gałęzi docelowej
    - trzy przyczyny bez podziału uwag człowieka (uwaga, pozycja wystawiona przez cykl, gałąź docelowa) — tanie i sprawdzalne, ale nie oddziela przepuszczonej wady od zmiany zdania
  - Source: Mariusz, 2026-11-12: „tak”, na nowy kształt pokazany w rozmowie po krytyce listy pięciu przyczyn (drugi agent rozpisał 20 poprawek: 14 w `loop2`, 6 w the way)
- Czy szablon rejestru w the way (`process-audit/problem_register.md`) dostaje zdanie o tym, jak zapisać wiersz problemu znalezionego po scaleniu, i klasę na liście startowej?
  - Answer: tak. Lista startowa klas dostaje `defect-found-at-request` (wada przepuszczona przez przegląd, znaleziona przez człowieka przed scaleniem — para `remark · defect`) i `defect-found-after-merge` (wada znaleziona przez zadanie naprawcze po scaleniu — linia `Defect introduced by:`); para `item · defect` idzie do istniejącej klasy `known-problem-left`. Opis kolumn dostaje zdanie dla wiersza po scaleniu: *Record* to commit ostatniej kopii zapisu cyklu, który błąd wprowadził, a *Stages* czyta `after the merge`. Polecenie liczące się nie zmienia.
  - Not chosen:
    - szablon bez zmian, wszystko w narzędziu użytkownika — szablon dalej mówi, że każdy problem pochodzi z raportu etapu, nocny przegląd odchodzi od opisu, który ma go prowadzić, a pole w zadaniach the way zostaje bez drogi do liczenia dla każdego poza autorem
  - Source: Mariusz, 2026-11-12: „a”

## Context

- Karty źródłowe: tabela działań w raporcie o usprawnieniach procesu, wiersz D9; D2 w raporcie o kursie 10xDEVS; D3 w drugim raporcie o kursie AI Tech Leaders; tabela działań raportu o eksperymencie z recenzentami, wiersz D5.
- Rejestr problemów i nocny przegląd zapisów cykli, który go wypełnia, są narzędziami Mariusza poza repozytorium procesu (WAY-330); cykl tego zadania ich nie zmienia.
- Nową klasę rejestru dodaje sesja audytu na „tak” Mariusza (WAY-333), a data jej dodania zaczyna nową serię miar (WAY-339).
- Rejestr ma 1306 wierszy z 83 cykli w 15 klasach i żadna klasa nie oznacza błędu znalezionego po scaleniu; najbliższa, `defect-found-by-review`, obejmuje wady złapane przez przegląd przed scaleniem (stan z 2026-11-12).
- Tabela klas rejestru wymienia 7 klas, a wiersze używają 15, bo nocna sesja, gdy żadna klasa nie pasuje, wpisuje nową nazwę zamiast najbliższej; liczenie audytu odrzuca te 126 wierszy do czasu, aż sesja audytu postawi klasy przed Mariuszem (wynik liczenia z 2026-11-12, sekcja *Unknown values*; skill nocnej sesji, sekcja „Problem w rejestrze”).
- Cykl trzyma zamrożoną kopię dokumentu zadania w katalogu zapisu (`task-cycle/skill/SKILL.md:131` @ 2292f33), a kopia zapisu w repozytorium ją niesie — w praktyce jako `docs/task-cycles/<slug>/task.md` (commit `90f4002` the way); nazwy pliku skill nie ustala.
- Szablon rejestru opisuje dziś kolumnę *Stages* jako etapy cyklu, które problem zgłosiły, a *Record* jako commit kopii zapisu z raportem, w którym problem stoi (`process-audit/problem_register.md:114-119` @ 2292f33); problemu znalezionego po scaleniu żaden etap tamtego cyklu nie zgłosił.
- Zapis cyklu jest według swojego szablonu jedynym dziennikiem cyklu (`task-cycle/record_template.md:98` @ 2292f33); tytułów commitów, które dodają kopię zapisu, skill cyklu nie ustala, a gra pisze je inaczej niż the way.
- Poprawka po otwarciu prośby ma dziś w skillu cyklu trzy wejścia: uwagi człowieka, odpowiedź „zrób to w tej prośbie” na pozycję, którą cykl sam wystawił jako niezrobioną, i decyzja człowieka przy zablokowanej prośbie (`task-cycle/skill/correction.md:26`, `:41-43`, `:48-65` @ 2292f33); każda poprawka zaczyna się od scalenia zdalnej gałęzi docelowej (`:27`).
- Skill poprawki każe zapisać uwagi jako nowe zdarzenia zapisu (`task-cycle/skill/correction.md:33` @ 2292f33); cykle gry trzymają je dodatkowo w pliku w `reports/` (np. `correction-1-remarks.md` w zapisie zadania `martwe-odsylacze-origin`), a ostatni cykl the way (`problem-cost-in-register`, commit `90f4002`) takiego pliku nie ma.
- Skrypty the way czytają nagłówek dokumentu zadania po nazwie pola (`project-level/plan_state.py:322` @ 2292f33 czyta `Project relation`), więc dodatkowa linia nagłówka nie zmienia tego, co czytają.
- Eksperyment z recenzentami znalazł w czterech zmianach gry trzy błędy przeoczone przez recenzję i zostawił skrypt, który wskazuje kandydatów: `a one-off script in the author's notes` (wynik obok, w jego pliku wyniku: 33 commity naprawcze gry, które usuwają linie z wcześniej scalonych próśb). Po odjęciu zadań porządkowych, poprawek testów i zmian z nowych wymagań został jeden czysty przypadek błędu wykrytego po scaleniu, prośba #34 gry (sekcja 10 raportu o eksperymencie z recenzentami).

## Questions carried to cycle

- Numer nowego rodzaju pozycji w szablonie opisu prośby i miejsce nowej pozycji w szablonie zapisu cyklu (przed uwagami procesowymi, które są ostatnią pozycją).

## Human actions

- Dodać w swojej kopii rejestru problemów klasy `defect-found-at-request` i `defect-found-after-merge`, przy prośbie — in the cycle
- Nauczyć nocny przegląd zapisów cykli (skill nocnej sesji i jej playbook) czytać linię `Defect introduced by:` z zamrożonego dokumentu zadania w zapisie i linie poprawek po otwarciu prośby, i pisać z nich wiersze rejestru tak, jak podaje szablon — in the cycle

## Decisions in play

- WAY-330 — Where does the audit of the process get the class, weight and cost of an occurrence of each problem, and the tie of a problem to the fix meant to remove it? — „The-way gives a template of a register of problems, which holds for each problem the cycle it comes from, its class, its weight, the cost of its occurrence, the issue it belongs to — the one matter that like problems of several cycles make — and that issue's fate, the fix of an implemented issue included. A user's own tool fills the register and the user adapts the template to their own needs; the audit reads the register that an entry of the user's locations file names and gives no problem a class, a weight or a cost of an occurrence itself.”
- WAY-333 — How is a problem that the audit counts graded and classed? — „Each problem the audit counts has a weight on a scale of four levels — no problem, Minor, Important and Critical — and a class from a list that the template of the register starts and the audit widens. Minor, Important and Critical are the grades of the review of a cycle (WAY-161), and no problem is the level below them.”
- WAY-339 — When do the measures of the audit stop being comparable? — „A new price list, or a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, starts a new series of measures. The audit compares measures only within one series, and judges a version of the process by the cycles that ran on it, never one week against another.”
- WAY-287 — What does a request put before the human for a decision? — „The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — […] — in three groups, headed *Needed from you*, *Fix or let through* and *You accept by merging*, in this order: […] and what the cycle did within its authority, which the human accepts by merging and which waits for no separate answer.”
  - Zmiana, którą wprowadza zadanie: wyliczenie tego, co sekcja trzyma, dostaje pary źródło · rodzaj poprawki po otwarciu prośby, w grupie *You accept by merging* (odpowiedź na pytanie „Jakie przyczyny ma zamknięta lista…”).
- WAY-296 — In what form does the cycle record hold its process remarks? — „The cycle record holds its process remarks in the one form its template gives, which the check of WAY-294 reads, and in no section or file of their own.” Szablon zapisu stawia uwagi procesowe jako ostatnią pozycję zapisu (`task-cycle/record_template.md:194-197` @ 2292f33), więc pozycja poprawek stoi przed nimi.
- WAY-289 — Which things the cycle left unfixed or undone does a request put before the human for a decision? — „Writing a request's description, the orchestrator of the cycle judges each unfixed finding […] and restates each that will be felt, in plain words, in the section for the human's decisions, under *Fix or let through*, as one question with the answers to fix it in this request, to make a task of it or to let it through […]. The answer to fix it runs a correction with one fix and one review of that fix; the same answer is offered for a step or a check the cycle skipped, a proposal of the task's own sections not applied and an incomplete reading of the review of the whole change […].” Źródło `item <n>` linii poprawki liczy odpowiedzi na te pozycje.
- WAY-335 — What decides whether a fix of the process works? — „Whether a fix works is decided by the cycles that ran on a version of the-way that holds the fix, compared with the cycles that ran on a version without it, and never by the date on which the fix was made.” Wiersz po scaleniu wskazuje w *Record* cykl, który błąd wprowadził, więc liczy się pod wersją procesu, na której ten cykl przeszedł przegląd.

## Settlements to record

Candidates: 13 shown, 11 accepted — 2026-11-12

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Błąd znaleziony po scaleniu zapisuje się w dwóch miejscach: pole w dokumencie zadania naprawczego mówi, która zmiana go wprowadziła, i jest źródłem, a klasa w rejestrze problemów go liczy. | decision | *Questions to settle*: „Gdzie zapisywać błąd znaleziony po scaleniu?” | czy pole w zadaniu wystarczy, czy liczenie zostaje samemu rejestrowi |
| 2 | Zadanie naprawcze usuwa wadę wobec tego, czego w chwili scalenia wymagało zadanie tamtej zmiany albo fundament, albo regresję; nowa potrzeba, zmiana zdania, luka zadania i konserwacja nie są błędem znalezionym po scaleniu. | decision | *Questions to settle*: „Które zadanie jest naprawcze…” | które zadania dostają w polu adres prośby |
| 3 | Każde zadanie ma w nagłówku linię `Defect introduced by:` — `none`, adresy próśb, które wprowadziły błąd, albo `unknown` z powodem — i ustala ją agent doprecyzowujący zadanie, nie cykl. | decision | *Questions to settle*: „Jaką postać ma pole…” | gdzie stoi pole, czy zwykłe zadanie je ma, czym nazywa zmianę, kto je wypełnia |
| 4 | Przyczyna poprawki po otwarciu prośby stoi w zapisie cyklu, jedną linią na poprawkę, a nie w tytule commita. | decision | *Questions to settle*: „Gdzie agent prowadzący cykl zapisuje przyczynę…” | tytuł commita czy zapis, i w jakiej postaci |
| 5 | Linia poprawki wymienia pary źródło · rodzaj: źródło `item <n>`, `remark` albo `target-branch` jest odczytem, rodzaj `defect` albo `not-required` (`none` przy `target-branch`) jest osądem agenta jednym testem „czy było wymagane”, a opis prośby pokazuje te pary w grupie *You accept by merging*. | decision | *Questions to settle*: „Jakie przyczyny ma zamknięta lista…” | wartości listy, kto je ocenia, czy człowiek widzi ocenę |
| 6 | Szablon rejestru zaczyna listę klas także od `defect-found-at-request` i `defect-found-after-merge`, para `item · defect` idzie do `known-problem-left`, a wiersz po scaleniu ma w *Record* ostatnią kopię zapisu cyklu, który błąd wprowadził, i `after the merge` w *Stages*. | decision | *Questions to settle*: „Czy szablon rejestru w the way…” | nazwy klas, który commit wpisać w *Record* wiersza po scaleniu |
| 7 | Dokument zadania napisany przed linią `Defect introduced by:` nie ma jej, a brak linii znaczy „nie oceniano”, nie `none`. | decision | *To do* 1 | jak nocny przegląd czyta zamrożone kopie zadań sprzed zmiany: jako `none` czy jako brak oceny |
| 8 | Zmianę, która weszła bez prośby, linia `Defect introduced by:` nazywa adresem commita. | decision | *To do* 1 | co wpisać, gdy błąd wprowadził commit spoza prośby: `unknown` czy commit |
| 9 | Poprawka po otwarciu prośby zapisuje uwagi człowieka słowo w słowo do pliku w `reports/` zapisu, także gdy przyszły w rozmowie, a linia poprawki go wskazuje. | decision | *To do* 2 | czy uwagi zostają tylko zdarzeniem zapisu, czy plikiem, na który może wskazać linia |
| 10 | Źródło `item <n>` podaje numer rodzaju pozycji z szablonu opisu prośby, nie numer pozycji w danym opisie. | decision | *To do* 2 | który numer wpisać |
| 11 | Wiersz `defect-found-at-request` ma w *Record* kopię zapisu, która niesie linię tej poprawki, a w *Stages* `at the request`. | decision | *To do* 4 | który commit i jaki etap wpisać w wierszu wady znalezionej przy prośbie |

## Out of scope

- Wsteczne wpisanie do rejestru przypadków sprzed tej zmiany — trzech błędów przeoczonych przez recenzję, znalezionych w eksperymencie z recenzentami, i prośby #34 gry, wskazanej przez skrypt — robota narzędzia Mariusza poza cyklem.
- Ten jednorazowy skrypt zostaje narzędziem jednorazowym w notatkach i nie wchodzi do the way: na 33 kandydatów dał jeden czysty przypadek, więc każdy wymaga osądu, a audyt nie nadaje problemom klasy sam (WAY-330).
