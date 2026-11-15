---
title: "the way: jak agent czyta dziennik decyzji — generowany spis zamiast tytułów, podział dziennika na tematy, pomiar przed i po"
status: draft
created: 2026-11-12T23:10
updated: 2026-11-14
tags: [zadanie]
related: "the author's project note on the process of working on a product"
---

## Po co to

- **Jak jest dziś:** Reguła procesu każe agentowi przeczytać w całości każdą decyzję, która dotyczy części produktu ruszanej przez zadanie. W grze sama część „widok w przeglądarce” to 263 wpisy, więc reguły nie da się wykonać: w czterech ostatnich sprawdzonych cyklach agent sprawdzający całą zmianę przeczytał w całości 22–48 decyzji z 80–331, a resztę zna z tytułu i sam zapisuje to jako odstępstwo. Dziennik nie ma podziału na tematy, więc wybór „po części produktu” zwraca 70–85% dziennika.
- **Kto to odczuwa:** Agent sprawdzający całą zmianę przed scaleniem — zmiana sprzeczna z decyzją, której nie przeczytał, przechodzi niezauważona. Agenci piszący zmianę, którzy dostają albo za dużo do czytania, albo czytają wybiórczo.
- **Co jeśli nic:** Z każdym zadaniem dziennik rośnie, a odsetek decyzji znanych tylko z tytułu się powiększa.

# the way: jak agent czyta dziennik decyzji — generowany spis zamiast tytułów, podział dziennika na tematy, pomiar przed i po

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Reguła czytania fundamentu (`elements/common/way_of_working.md`, „Reading the foundation”, krok 2; WAY-150) każe czytać w całości każdą decyzję, której *Scope* nazywa część dotkniętą pracą; tylko recenzent całej zmiany może resztę wyboru przejrzeć po tytułach.
- W produkcie gry wybór po części zwraca 70–85% dziennika (część `browser-view` to 263 z 373 wpisów), więc reguły nie da się wykonać: w siedmiu sprawdzonych cyklach recenzent całej zmiany przeczytał w całości 10–60 decyzji z 80–331, a resztę znał z tytułu (raport o dzienniku decyzji, ustalenie 4).
- W dzienniku the way ten sam wybór dla części, których dotyka to zadanie (`elements-common`, `decisions`, `task-cycle`, `gate`), zwraca 191 z 331 decyzji, ok. 600 KB (policzone na `foundations` `f4af75d`).
- Zdania wiążące — część wpisu, która mówi, co obowiązuje — to ok. 22% bajtów dziennika w obu produktach; resztę stanowią pola, uzasadnienie i warianty odrzucone, potrzebne temu, kto decyzję zmienia albo jej przeczy.
- Zmiana testu, który linią `decision:` pilnuje zdania decyzji, nie prowadzi dziś autora ani recenzenta do tej decyzji: reguła wyboru dodaje niezmienniki cytowane przez zmieniany test, a decyzji pilnowanych przez niego nie (uwaga recenzenta w prośbie #120 the way).
- Odbiorcą jest agent sprawdzający całą zmianę, który zna dziś większość decyzji tylko z tytułu, i agenci piszący zmianę, którzy dostają za dużo do czytania albo czytają wybiórczo.

### To do

1. Spis decyzji: skrypt the way, z testami, wypisuje do pliku, który wskaże agent, spis wybranych decyzji dziennika produktu — dla każdej decyzji jej numer, pytanie z nagłówka, zdania wiążące i *Scope*. Zdania wiążące to każdy akapit przed pierwszym polem wpisu, nie tylko pierwszy, bo wpis ma osobny akapit na każdą dołączoną część pytania (WAY-05). Wybór podaje się częściami produktu, a w dzienniku z sekcjami tematycznymi także sekcjami (punkt 7). Spis nie jest plikiem repozytorium i nie ma czego w nim odświeżać ani pilnować bramką (pytanie 1). Skrypt działa na dzienniku każdego produktu — w produkcie z przypiętej kopii the way — z sekcjami i bez nich.
2. Reguła czytania (`elements/common/way_of_working.md`, „Reading the foundation”, krok 2) i WAY-150 (przez `record-decision`): agent tworzy skryptem z punktu 1 spis swojego wyboru i go czyta; w całości otwiera tylko te decyzje, które praca zmienia, którym przeczy albo na których pytanie proponuje inną odpowiedź — tę ostatnią razem z wariantami odrzuconymi — te nazwane w zadaniu albo w źródle pracy i te, których zdania wiążące zostawiają otwarte, co praca ma zrobić.
3. Do wyboru dochodzi każda decyzja, której zdanie zmieniany test pilnuje linią `decision:`, i jest czytana w całości.
4. Recenzent całej zmiany czyta spis wszystkich wybranych decyzji i podaje w raporcie, ile z nich przeczytał w całości; przeglądanie decyzji po tytułach jako główna lektura znika z reguły i z każdego miejsca the way, które je dziś opisuje (instrukcja recenzenta, sekcja **Unread material** raportu i WAY-326, szablon opisu prośby o scalenie). Zostaje tylko przegląd po pytaniach decyzji spoza sekcji tematów pracy z punktu 7.
5. Dziennik decyzji the way (`foundations/decisions.md`) dostaje 20–30 sekcji tematycznych po kilkanaście wpisów, każdą z nagłówkiem i jednym zdaniem, co obejmuje: numery wpisów bez zmian, treść każdego wpisu bajt w bajt ta sama, co potwierdza skrypt porównujący wpisy przed podziałem i po nim. Listę sekcji i przydział wpisów proponuje cykl; opis prośby o scalenie pokazuje listę sekcji z liczbą wpisów i zdaniem opisu każdej oraz wynik skryptu porównującego, a Mariusz przyjmuje listę przy scaleniu (pytanie 3).
6. Szablon decyzji (`elements/decisions/template.md`, sekcja „Where entries go”, punkt, który otwiera „A product keeps all its decisions in one log”) i WAY-18 (przez `record-decision`): dziennik może mieć sekcje tematyczne; nowy wpis staje na końcu sekcji swojego tematu, a gdy żadna sekcja nie pasuje, autor zakłada nową sekcję na końcu dziennika i opis prośby o scalenie ją wymienia (pytanie 3).
7. Wybór po temacie (`elements/common/way_of_working.md`, „Reading the foundation”, i WAY-150 przez `record-decision`): w dzienniku z sekcjami agent wybiera z listy sekcji (nagłówek i zdanie opisu) sekcje tematów pracy i czyta spis ich decyzji; do tego czyta pytania — same nagłówki — decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, i otwiera te, których pytanie wskazuje na związek z pracą (pytanie 2). W dzienniku bez sekcji — jak dziennik gry do jego podziału w projekcie Loop — wybór zostaje po częściach produktu, a spis zastępuje lekturę w całości tak jak w punkcie 2.
8. Pomiar przed i po: `task-cycle/cycle_measures.py` liczy dla każdego agenta cyklu, ile bajtów dziennika decyzji i spisu weszło do jego kontekstu i ile razy, a WAY-347 (przez `record-decision`) dostaje ten pomiar. „Przed”: cykl tego zadania uruchamia rozszerzony skrypt na zapisach sesji ostatniego cyklu gry i ostatniego cyklu the way sprzed zmiany i podaje liczby w opisie prośby o scalenie; „po” przychodzi w pomiarach każdego następnego cyklu (pytanie 4).

### Acceptance criteria

- Opis prośby o scalenie wypisuje wprost, przy WAY-150, WAY-18 i WAY-21, który wariant albo powód, wcześniej przez tę decyzję odrzucony, zmiana przyjmuje — przy WAY-150 spis decyzji („a separate maintained index”), przy WAY-18 kolejność wpisów według tematu zamiast kolejności zapisania, przy WAY-21 wybór po temacie („topics — cannot be derived from a change”) — tak, żeby Mariusz przyjął te odwrócenia świadomie przy scaleniu.

### Questions to settle

- 0. Jak agent ma czytać dziennik decyzji?
  - Answer: generowany spis (numer, pytanie, zdania wiążące, części produktu) i reguła czytania z brzmienia 7h raportu.
  - Not chosen:
    - zostawić — reguła „czytaj w całości” dalej jest łamana w każdym cyklu, recenzent zna 85% decyzji z tytułu; z każdym zadaniem gorzej
    - fizyczne rozdzielenie dziennika na dwa pliki (zdania wiążące osobno, uzasadnienia osobno pod tym samym numerem) — Mariusz: „odłożone, do rozważenia, gdyby spis nie wystarczył”; koszt wg raportu: jednorazowa zmiana każdego wpisu, skryptu kontroli i wszystkich skilli elementów
  - Source: Mariusz, 2026-11-12, `the author's private note of decisions on the analyses of the process`, „Sprawa 9”, decyzja 1: „wariant A — generowany spis (numer, pytanie, zdania wiążące, części) i reguła czytania z brzmienia 7h; rozdzielenie dziennika na dwa pliki odłożone, do rozważenia, gdyby spis nie wystarczył. Świadomy koszt: ok. 54 tys. zamiast 31 tys. tokenów na agenta sprawdzającego, dopóki nie ma podziału na tematy.”
- 1. Gdzie stoi spis i jak zostaje aktualny?
  - Answer: bez pliku — agent uruchamia skrypt z częściami produktu (po podziale także z tematami) i dostaje do pliku roboczego spis dokładnie swojego wyboru; spis nigdy nie jest nieświeży, nie ma czego pilnować bramką ani scalać, a wyszukiwanie decyzji po częściach robi skrypt. Odpada zdanie z wcześniejszego kierunku „Bramka testów zgłasza spis nieświeży”.
  - Not chosen:
    - plik w repozytorium, odświeżany skryptem po każdej zmianie dziennika, bramka zgłasza nieświeży — każda zmiana decyzji musi pamiętać o odświeżeniu; dwie równoległe gałęzie dopisujące decyzję kłócą się przy scalaniu także o plik spisu; w produkcie nieświeży spis musiałby zgłaszać skrypt kontroli fundamentu, a instalator zakładać plik
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 b”
- 2. Jak agent wybiera decyzje w dzienniku podzielonym na tematy?
  - Answer: tematy plus zabezpieczenie — spis decyzji z sekcji tematów pracy, do tego same pytania decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, i otwarcie tych, których pytanie wskazuje na związek; dla tego zadania to ok. 16 KB nagłówków, ok. 4 tys. tokenów więcej.
  - Not chosen:
    - tylko tematy — najtańsze, ale decyzja z innego tematu, która rządzi dotkniętą częścią, przepada bez śladu
    - tematy dla wszystkich poza recenzentem całej zmiany, który czyta spis całego wyboru po częściach — recenzent nic nie zyskuje na podziale (dla tego zadania ok. 33 tys. tokenów spisu)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 b”
- 3. Jak drobne są sekcje dziennika the way i kto przyjmuje ich listę?
  - Answer: 20–30 drobnych tematów; listę sekcji i przydział wpisów proponuje cykl, Mariusz przyjmuje je przy scaleniu z opisu prośby, który pokazuje listę sekcji z liczbą wpisów i zdaniem opisu. Nowy wpis, do którego żadna sekcja nie pasuje, zakłada nową sekcję na końcu dziennika, a opis prośby ją wymienia.
  - Not chosen:
    - sześć obszarów z notatki zadania AIR-518 — prawie pokrywają się z częściami produktu, sekcja „cykl zadania” miałaby ok. 100 wpisów, więc podział niewiele daje ponad wybór po częściach
    - drobne tematy z listą ustaloną w doprecyzowaniu — dłuższe doprecyzowanie, w zamian brak niespodzianek przy scaleniu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 b (z Twoją propozycją: nowa sekcja na końcu dziennika, wymieniona w opisie prośby)”
- 4. Jak mierzyć, ile dziennika wchodzi do kontekstu agentów przed zmianą i po niej?
  - Answer: rozszerzyć `task-cycle/cycle_measures.py` o liczbę bajtów dziennika i spisu, które weszły do kontekstu każdego agenta, i liczbę takich odczytów; „przed” z zapisów ostatniego cyklu gry i ostatniego cyklu the way, w opisie prośby; „po” w pomiarach każdego następnego cyklu. Koszt: zmiana skryptu zaczyna nową serię pomiarów w audycie procesu; rozpoznanie odczytu dziennika jest przybliżone.
  - Not chosen:
    - jednorazowy pomiar osobnym agentem poza cyklem, teraz i za kilka cykli — druga połowa wymaga osobnego zadania z przypomnieniem, a w procesie nic nie zostaje
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „4 a”

## Context

- Kierunek Mariusz wybrał 2026-11-12 przy przeglądzie raportu o dzienniku decyzji (`the author's private report on slimming the decision log`, „Decyzje dla Mariusza”, decyzja 1, i karty D2, D3, D7).
- Brzmienie 7h raportu, od którego warto zacząć punkt 2: „Read the index line of each decision found — its question, binding sentences and *Scope*. Read whole each decision the work changes, goes against or proposes another answer to, each one the task names, and each whose binding sentences leave open what the work has to do. The reviewer of the whole change reads the index of every decision found and states how many it read whole.”
- Podział dziennika the way na tematy przeszedł tu z zadania AIR-518 („Ułatwić rozumienie i znajdowanie zasad the way…”, jego punkt 3), które zostaje z punktami 1 i 2.
- Dziennik gry dzieli się w zadaniu porządków dziennika gry w projekcie Loop, po wyprowadzeniu z niego wpisów, które decyzjami nie są.
- Punkt 3 przyszedł z zadania zbiorczego „the way: drobne poprawki po PR-ach #117–#121” (pozycja 3, sprawa 3), które go tu przekazało; cytat recenzenta: „WAY-150's selection does not take in the decision a test holds by a line `decision:` … A reviewer or author altering such a test is not led to the decision whose sentence it holds, except through the line itself”.
- Zadanie o przeglądzie całej zmiany, z którym wcześniejsza notatka kazała to zgrać, jest scalone (the way, prośba #109) i nie zmieniło reguły czytania decyzji.
- Rachunek raportu dla gry (ustalenie 4, „bajty przez cztery”, nie tokenizer): dziś recenzent czyta ok. 31 tys. tokenów i zna ok. 15% zdań wiążących; sam spis — ok. 54 tys. i 100%; spis po podziale na tematy — 10–13 tys. i 100% w tematach zadania; założenie „3–5 tematów na zadanie” jest autora raportu, nie pomiar.
- `task-cycle/cycle_measures.py` liczy już z zapisów sesji Claude Code i Codex, jak agenci jednego cyklu używają kontekstu, a cykl uruchamia go w każdym przebiegu; jego zmiana zaczyna nową serię tych pomiarów w audycie procesu (`process-audit/SKILL.md`, punkt „Measures are compared inside a series only”).
- Miejsca, które dziś opisują lekturę po tytułach: `elements/common/way_of_working.md` („Reading the foundation”, krok 2), `task-cycle/review/SKILL.md` (punkt „For the review of the whole change” i sekcja **Unread material**), `task-cycle/skill/SKILL.md` (zdanie „A decision the reviewer of the whole change read by title”), `task-cycle/skill/request_template.md` (akapit o tym, ile recenzent przeczytał w całości).
- Szablon decyzji mówi dziś w „Where entries go”: „the log has no topical sections, and a new entry goes at its end (WAY-18)”.
- Cały dokument przyjął doradca dnia w imieniu Mariusza, 2026-11-14.

## Questions carried to cycle

- Jak skrypt pomiarów rozpoznaje, że wywołanie narzędzia wprowadziło do kontekstu dziennik decyzji albo spis (odczyt pliku, wyszukiwanie, polecenie powłoki, skrypt spisu).
- Skąd cykl bierze sesje ostatniego cyklu gry i ostatniego cyklu the way do pomiaru „przed”.

## Human actions

none

## Decisions in play

- **WAY-150 — How do the-way skills choose which product foundation material to read?** Zmiana: agent czyta spis swojego wyboru zamiast decyzji w całości, a w całości otwiera tylko te, które praca rusza; w dzienniku z sekcjami wybiera po temacie z przeglądem pytań decyzji spoza tematów; do wyboru dochodzą decyzje pilnowane linią `decision:` zmienianego testu; recenzent całej zmiany podaje, ile decyzji przeczytał w całości. Wariant odrzucony „a separate maintained index — a second account can drift without resolving semantic relevance” zostaje przyjęty w postaci spisu tworzonego na żądanie, który się nie rozjeżdża (*To do* 1–4, 7; pytania 0–2).
  > The-way skills read a product's foundation selectively: whoever selects names the parts the work touches […]; finds by a touched part's identifier the decisions whose *Scope* names it and the invariants whose *Part* names it or `every`, and adds the invariants a test the work alters cites, the decisions the task's *Decisions in play* or the work's source names […]; and reads each selected entry whole, […] save that the reviewer of the whole change reads whole the decisions of its selection that concern the change's topic, skims the rest of the decisions of its selection by title and opens every one whose title points to a bearing on the change, and states in its report how many decisions it read whole and how many by title only. […]
- **WAY-18 — How is a product's decision log kept?** Zmiana: wpisy stoją w sekcjach tematycznych, nowy wpis na końcu sekcji swojego tematu albo w nowej sekcji na końcu dziennika, zamiast w kolejności zapisania; zdanie „with no view generated from it” zostaje prawdziwe, bo spis nie jest plikiem (*To do* 5, 6; pytania 1, 3).
  > A product keeps all its decisions in one log, whatever they are about. The log holds one entry for each decision in force, in the order the entries were written, and says what binds today with no view generated from it. A link between entries is written at one end only; the one exception is a decision's invariants, which its *Verification* names while each of them names the decision in *Derives from*.
- **WAY-21 — What is a decision's scope?** Zmiana w uzasadnieniu i wariantach odrzuconych: wybór po temacie, które dziś odrzucają („Topics cannot be derived from changed files”; „topics — cannot be derived from a change”), staje obok wyboru po *Scope*, który zostaje zabezpieczeniem; zdanie wiążące bez zmiany (*To do* 7; pytanie 2).
  > A decision's scope names the parts of the product it governs, taken from the part map, and never file paths, so that the decisions governing a change are found from the files it touches through the part map's rule for assigning files.
- **WAY-326 — What does a task-cycle stage report about the material its handoff names that stayed unread?** Zmiana: liczby recenzenta całej zmiany mówią, ile decyzji wyboru przeczytał w całości, a decyzja znana ze spisu nie jest luką (*To do* 4).
  > […] the section of the reviewer of the whole change also holds the counts WAY-150 gives. […] A decision the reviewer of the whole change read by title as WAY-150 gives is no gap and stands in the section only in the counts.
- **WAY-347 — How are the measures of how a cycle's agents use context and the prompt cache counted?** Zmiana: do pomiarów dochodzi liczba bajtów dziennika decyzji i spisu w kontekście każdego agenta i liczba takich odczytów (*To do* 8; pytanie 4).
  > The measures of how a cycle's agents use the context and the prompt cache of the model — the number of model calls, the size of each call's context, the tokens written to the cache and the tokens written to it again — are counted by a script of their own into a file of their own in the cycle's record, and are never columns of the stage report.
- **WAY-05 — How is a decision entry written?** Bez zmiany; mówi, co jest zdaniami wiążącymi, które bierze spis (*To do* 1).
  > A decision entry opens with one to three binding sentences that answer its question […] and one paragraph of one to three binding sentences for each part of another question that it answers, followed by fields a script or an agent reads, then rationale and rejected options in prose […]
- **WAY-12 — How is a decision checked?** i **WAY-02 — How does whatever depends on an entry refer to it?** Bez zmiany; wprowadzają linię `decision:`, po której punkt 3 znajduje decyzję zmienianego testu.
  > A test that holds a sentence of a decision carries beside it a line `decision:` that gives the number of the decision and the start of that sentence […] (WAY-12)
- **WAY-52 — What is generated from the part map for an agent?** Bez zmiany; dotyczy mapy części, nie dziennika; jego powód („a derived file to keep in step”) spis tworzony na żądanie omija.
  > Nothing is generated from the part map for an agent: an agent reads the entries of the parts its change touches, and no overview of the repository is generated for it.
- **WAY-33 — What does the author of a foundation change search for?** Bez zmiany; przeszukanie całego fundamentu przez autora wpisu zostaje obok wyboru lektury i czyta znalezione wpisy w całości.
  > When a change writes a foundation entry or changes its binding part, its author, once the entry is settled, searches the whole foundation once for the entries the change touches […]

## Settlements to record

Candidates: 9 shown, 7 accepted — 2026-11-14

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Agent czyta spis swojego wyboru decyzji, a w całości otwiera tylko te, które praca zmienia, którym przeczy albo na których pytanie proponuje inną odpowiedź (z wariantami odrzuconymi), te nazwane w zadaniu albo w źródle pracy i te, których zdania wiążące zostawiają otwarte, co praca ma zrobić; recenzent całej zmiany czyta spis całego wyboru i podaje, ile przeczytał w całości. | sentence of WAY-150 | pytanie 0 | czy dalej czytać decyzje w całości, a recenzent po tytułach |
| 2 | Spis nie jest plikiem repozytorium: skrypt the way wypisuje na żądanie spis wybranych decyzji — numer, pytanie, zdania wiążące, *Scope*. | sentence of WAY-150 | pytanie 1 | plik spisu w repozytorium z testem świeżości w bramce |
| 3 | W dzienniku z sekcjami tematycznymi agent wybiera sekcje tematów pracy i czyta spis ich decyzji, a pytania decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, przegląda i otwiera te, które wskazują na związek. | sentence of WAY-150 | pytanie 2 | wybór wyłącznie po temacie, bez zabezpieczenia |
| 4 | Dziennik decyzji ma sekcje tematyczne bez zmiany numerów; nowy wpis staje na końcu sekcji swojego tematu, a gdy żadna nie pasuje, w nowej sekcji na końcu dziennika, którą opis prośby o scalenie wymienia. | sentence of WAY-18 | pytanie 3 | gdzie postawić nowy wpis i czy autor może założyć sekcję |
| 5 | Decyzja, której zdanie zmieniany test pilnuje linią `decision:`, wchodzi do wyboru lektury i jest czytana w całości. | sentence of WAY-150 | *To do* 3; *Context*, uwaga recenzenta prośby #120; przyjęte: doradca dnia w imieniu Mariusza, 2026-11-14 | czy zmiana testu z linią `decision:` prowadzi do lektury tej decyzji |
| 6 | W dzienniku bez sekcji tematycznych wybór zostaje po częściach produktu, a spis zastępuje lekturę decyzji w całości. | sentence of WAY-150 | *To do* 7; przyjęte: doradca dnia w imieniu Mariusza, 2026-11-14 | czy w dzienniku gry, do jego podziału, dalej czytać decyzje w całości |
| 7 | Pomiary kontekstu cyklu liczą dla każdego agenta, ile bajtów dziennika decyzji i spisu weszło do jego kontekstu i ile razy. | sentence of WAY-347 | pytanie 4 | jednorazowy pomiar poza procesem |

## Out of scope

- Podział dziennika decyzji gry na tematy — zadanie porządków dziennika gry w projekcie Loop.
- Rozdzielenie dziennika na dwa pliki (zdania wiążące osobno, uzasadnienia osobno) — odłożone przez Mariusza 2026-11-12, do rozważenia, gdyby spis nie wystarczył.
- Ocena „wybór zostaje / treść do szablonu” wpisów dziennika the way — zadanie AIR-518.
