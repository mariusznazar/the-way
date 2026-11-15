---
title: "the way: drobne poprawki po PR-ach #93 i #117–#121 — losowa porażka testu bramki, przewodnik wdrożeniowy w kroku listy WAY-139, stare reguły po zmianie dziennika decyzji, identyfikator decyzji w zdaniu niezmiennika, kontrola fundamentu między kawałkami planu"
status: draft
created: 2026-11-14T11:55
updated: 2026-11-15
tags: [zadanie]
related: "the author's project note of the process"
---

# the way: drobne poprawki po PR-ach #93 i #117–#121 — losowa porażka testu bramki, przewodnik wdrożeniowy w kroku listy WAY-139, stare reguły po zmianie dziennika decyzji, identyfikator decyzji w zdaniu niezmiennika, kontrola fundamentu między kawałkami planu

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/93 · https://github.com/mariusznazar/the-way/pull/111 · https://github.com/mariusznazar/the-way/pull/120

## Description

### Need

- Cztery scalone zmiany the way z 14.11.2026 (PR-y #117, #119, #120 i #121) i zmiana z PR #93 zostawiły poza swoim zakresem drobiazgi; zadanie robi je jednym cyklem.
- Test bramki `test_by_default_every_directory_runs_at_the_same_time` (`gate/test_run_tests.py`) raz na cztery przebiegi w cyklu PR #117 nie przeszedł bez winy zmiany; każda taka porażka zatrzymuje cykl na powtórce bramki (~15 min) i opisie w PR-ze.
- Przyczyna jest ustalona: procesy testowe dopisują swoje linie `start <nazwa>` do jednego wspólnego pliku `timeline.log` (`open(LOG, 'a')`), a na Windows równoczesne dopisanie do jednego pliku gubi linie.
- Krok sprawdzający listę WAY-139 (`project-level/task/skill/resolve_gaps.md`) nie kieruje do przewodnika po pisaniu skilla wdrożeniowego produktu (`project-level/task/deployment_skill_guide.md`) punktów, które wpisują do skilla odpowiedź o logach, o czasie życia zapisu albo o awarii, choć części 6–8 przewodnika dotyczą właśnie tych trzech spraw.
- Trzy szablony wytycznych mówią jeszcze regułę sprzed zmiany WAY-172 w PR #120 (każdy nierozstrzygnięty wybór zatrzymuje cykl na zablokowanej prośbie), więc agent piszący wytyczne z szablonu może stanąć na regule, która tylko mówi, jak pisać.
- Skrypt kontroli fundamentu pomija bez słowa niezmiennik, któremu w kopii bazowej brakowało pola *Method* albo *Part*, choć WAY-344 każe skryptowi sprawdzającemu formę wypisać brak pola; recenzent nie dowiaduje się wtedy, że zmienione zdanie takiego niezmiennika nie zostało porównane.
- Szablon decyzji nie mówi, co wpisać w *Rejected* decyzji, którą cykl zapisał z własnego wyboru (oznaczenie `the cycle's`), więc trzy cykle z 11.11 wpisały w to pole trzy różne rzeczy.
- Szablon niezmienników mówi, że powiązania stoją poza zdaniem niezmiennika (reguła wycofanej WAY-56), a WAY-60 i ten sam szablon każą w pewnych przypadkach wpisać identyfikator decyzji w samo zdanie; żadne zdanie nie mówi, czemu to nie kolizja, więc recenzent, który przeczyta najpierw tę regułę szablonu, może odrzucić poprawną formę.
- Szablon dokumentu zadania nie ma statusu dla zadania, z którego człowiek zrezygnował, więc taki dokument zostaje z `Status: refining` i następna sesja może wziąć go za zadanie w toku.
- Skill planu każe w *Checks* kawałka uruchamiać testy każdego niezmiennika, do którego kawałek sięga, czego planujący nie robią; reguła wymaga drogiego wariantu, który rozstrzygnięcie AIR-515 odrzuciło, a recenzent czytający ją dosłownie może zakwestionować każdy plan.
- Na drodze z planem kawałek, który zapisuje niezmiennik z metodą `test`, gdy jego test pisze dopiero późniejszy kawałek (na co pozwala WAY-61), uruchamia w swoich *Checks* test kontroli fundamentu (`test_the_way_foundation_passes` w `elements/common/test_foundation_check.py`), a ten pada, bo niezmiennika nie cytuje jeszcze żaden test; wykonawca dostaje czerwony wynik dla stanu, na który decyzja pozwala, i może zablokować kawałek albo cofnąć metodę na `review`.
- *Scope* WAY-61 nie wymienia części `task-cycle`, choć jej zdanie o kawałkach planu stosuje skill planu, więc agent zmieniający ten skill nie wybierze jej do lektury i może przepisać zdanie *Checks* wbrew niej.
- Cykl dopisuje do decyzji z wiersza albo do zaprojektowanego wpisu część, której wiersz ani wpis nie dają — parę przykładów „complies / violates” albo pole, które zaprojektowany wpis zostawił `TODO` — i nie wiadomo, czy to wpis „niesiony w całości”; w the way PR #103 agenci rozważali, czy wolno im dopisać parę, i pokazali ją człowiekowi, a w loop2 PR #79 krok fundamentu wypełnił *Relations* i *Verification* decyzji D-362 bez słowa w opisie PR-a, więc Mariusz przyjął scaleniem przykłady, którymi agenci mierzą każdą późniejszą zmianę, nie widząc ich (AIR-661).

### To do

1. Moduł próbny testów równoległego uruchamiania katalogów (funkcja `timed_module` w `gate/test_run_tests.py`, około linii 38) zapisuje start i koniec każdego testu tak, że równoczesne zapisy kilku procesów nie gubią linii; dotyczy to każdego testu klasy `DirectoriesAtOnce`, który z niego korzysta.
2. Test `test_by_default_every_directory_runs_at_the_same_time` dalej nie przechodzi, gdy katalogi biegną jeden po drugim, a jego limit oczekiwania zostaje 120 sekund.
3. — odpadł: WAY-09 nie trzyma już spisu tego, co leży w `project-level/` (PR #126 przeniósł go do zdania części w mapie części), a przewodnik w tym zdaniu mapy wpisuje zadanie the author's task note on the dependency line of the part map; numer zostaje, bo pozostałe punkty odwołują się do numerów.
4. — przeniesiony do zadania the author's task note on the dependency line of the part map (zob. *Context*); numer zostaje, bo pozostałe punkty odwołują się do numerów.
5. Krok sprawdzenia listy w `project-level/task/skill/resolve_gaps.md` (akapit zaczynający się „The list holds three items the check handles apart”, około linii 90) kieruje do przewodnika także punkt *To do*, który wpisuje do skilla odpowiedź dla jednej z trzech pozycji: jak czytać logi, jak długo żyje zapis i skąd człowiek dowiaduje się o awarii.
6. Zdanie wiążące WAY-139 mówi to samo co krok z punktu 5, a jej *Verification* i *Rationale* zgadzają się ze zmianą; WAY-139 zmienia się w miejscu (WAY-07).
7. W trzech szablonach wytycznych zdanie o wyborze, którego zadanie nie rozstrzygnęło, zatrzymuje cykl tylko dla wyboru niosącego realny koszt, jak mówi WAY-172: `product-guidelines/coding/template.md` („A choice the task did not settle is a question that stops the cycle at a blocked draft request, never a rule or a row (WAY-172).”, około linii 354), `product-guidelines/styleguide/template.md` („A meaning the task did not settle is a question that stops the cycle at a blocked draft request, never a row of `## Roles` (WAY-172).”, około linii 188) i `product-guidelines/testing/template.md` („A choice the task did not settle is a question that stops the cycle at a blocked draft request, never a rule, a row or a field (WAY-172).”, około linii 274).
8. Skrypt `elements/common/foundation_check.py`, w wypisaniu niezmienników `test`, których zdanie zmiana przeredagowała (funkcja `list_invariants`, której opis kończy się „An invariant the base lacks, or lacking *Method* or *Part* at either state, is left out. The listing is no error.”), dla niezmiennika, któremu w kopii bazowej brakuje *Method* albo *Part*, wypisuje jedną linię `listed:` z nazwą niezmiennika i brakującym polem, bez zmiany kodu wyjścia; test `test_reworded_invariant_lacking_method_or_part_at_base_adds_no_listing` w `elements/common/test_foundation_check.py` sprawdza tę linię.
9. WAY-344 dostaje zdanie, że brak pola w kopii pliku z commita bazowego skrypt kontroli fundamentu wypisuje linią `listed:`, bez błędu i bez zmiany kodu wyjścia; WAY-344 zmienia się w miejscu (WAY-07).
10. Szablon decyzji `elements/decisions/template.md` dostaje po punkcie WAY-134 (tym, który zaczyna się „The *Rejected* of a decision written from a row of a task's *Settlements to record*”) punkt: „The *Rejected* of a decision marked `the cycle's` takes `unknown`, unless a statement of the human names the ways weighed — then those ways, or `none considered` where the human said so.”
11. W `task-cycle/skill/foundation_step.md` zdanie kończące się „as the decisions' template gives (WAY-134)” dostaje dopisek: „, and an entry marked `the cycle's` takes it as that template gives for such an entry”.
12. WAY-60 (`foundations/decisions.md`, „Where may a condition that decides an invariant stand…”) i punkt szablonu niezmienników `elements/invariants/template.md`, który zaczyna się „A condition that decides whether a commit makes the sentence true” i kończy „and otherwise in the sentence (WAY-60)” (około linii 82), dostają klauzulę: identyfikator decyzji wpisany w zdanie niezmiennika, bo ta decyzja trzyma jego warunek, jest częścią warunku, a nie powiązaniem, którego wymaga WAY-17; gdy takie powiązanie się należy, stoi obok zdania, w swoim polu, jak mówi punkt szablonu „The sentence is the binding part; the method, the links, *Part* and *Violated* stand outside it.”, który zostaje bez zmian. WAY-60 zmienia się w miejscu (WAY-07).
13. Szablon dokumentu zadania (`project-level/task/template.md`, zdanie „`Status:` reads `refining`, `waiting for human`, or `ready for cycle`.”, około linii 97) ma czwartą wartość, `dropped — approved by human`, dla zadania, z którego człowiek zrezygnował — to samo słowo co stan wiersza w szablonie planu projektu (`project-level/plan/template.md`, tabela pod „The states (WAY-142)”).
14. W skillu planu (`task-cycle/plan/SKILL.md`, punkt *Checks*, zdanie „They are the slice's focused checks — its tests and those of the code and invariants it reaches”, około linii 173) *Checks* kawałka uruchamiają testy niezmienników, które zmiana kawałka może uczynić fałszywymi, wybrane przez planującego, a nie testy każdego niezmiennika, do którego kawałek sięga; punkt *Read* (wszystkie niezmienniki, do których kawałek sięga, WAY-62) zostaje bez zmian, a zdanie uzasadnienia WAY-160 „while the focused checks of the code and invariants a slice reaches find what it breaks there” zgadza się z nowym brzmieniem *Checks*.
15. *Scope* WAY-61 (`foundations/decisions.md`, „How is an invariant's method of checking written?”, linia „- **Scope:** invariants, gate, decisions, part-map, elements-common”) wymienia też `task-cycle`; WAY-61 zmienia się w miejscu (WAY-07).
16. W skillu planu (`task-cycle/plan/SKILL.md`, punkt *Checks*, ten sam co w punkcie 14) stoi zdanie: kawałek, który zapisuje niezmiennik z metodą `test`, gdy jego test pisze późniejszy kawałek tej samej zmiany (WAY-61), uruchamia w *Checks* kontrolę fundamentu `elements/common/foundation_check.py` z przełącznikiem `--skip-test-citations` zamiast testu albo polecenia, które uruchamia ją bez przełącznika (w the way `test_the_way_foundation_passes`), jak w przykładzie zgodności WAY-321 „the run right after an invariant that reads `test` is written, whose test a later slice of the same change writes, passes the switch and reports nothing”.
17. W `task-cycle/skill/foundation_step.md` po „the last for an entry no row and no projected entry carries whole” stoi dopisek: „; a part the writer adds that its row or projected entry does not give — a pair of examples, a field the projected entry left `TODO` — makes the entry `the cycle's`, save a pair kept only until a test of the same change holds the sentence”. Powiązanie (*Relations*) dopisane do wpisu z wiersza wpisu nie zmienia w `the cycle's` (WAY-114, *Rejected*: ściana tekstu u góry opisu PR-a).
18. W `elements/decisions/skill/SKILL.md`, krok „## 3. Draft”, punkt *Verification*, po „where the human gives one or accepts one you propose” stoi dopisek: „ — in a task's cycle the human accepts it at the merge, the entry marked as `task-cycle/skill/foundation_step.md` gives (WAY-114)”.
19. (dodatek przy okazji, 2026-11-15) Reguła początku cytatu linii `decision:` w szablonie decyzji (`elements/decisions/template.md`, sekcja `## Verification`, „the first word after a full stop and a space”, około wiersza 230) i jej sprawdzenie w `elements/common/foundation_check.py` nie uznają kropki ze spacją wewnątrz cudzysłowu („…” albo "…") za koniec zdania wiążącego; test w `elements/common/test_foundation_check.py` sprawdza zdanie, które cytuje napis z dwoma zdaniami. Przykłady i źródło: the author's task note on the binding sentence and the full stop in a quotation (D-216, D-222, D-345 loop2; uwagi agentów PR-a loop2#133). Linii `decision:` w testach loop2 punkt nie rusza.
20. (dodatek przy okazji, 2026-11-15) WAY-229 i dwa kroki skilla cyklu, które go powtarzają (`task-cycle/skill/SKILL.md`: krok przeglądu całej zmiany i krok 11), mówią, że przegląd całej zmiany i przegląd kroku powrotu biegną na najmocniejszej klasie modelu **spośród dozwolonych w ustawieniach sesji**: orkiestrator bierze ją z listy dozwolonych modeli (ustawienie `availableModels`), nie z nazwy najmocniejszego modelu rodziny. Powód: sesje cykli startują z ustawieniami, które wyłączają Fable; cykl wytycznych kodu (15.11) zlecił recenzenta z `model: fable`, a podagent proszący o model spoza listy dostaje model sesji — przegląd poszedł na Sonnecie zamiast na Opusie (zapis rozmowy sesji `the session record that item 20 of the task names (a Claude Code session record of the author's, outside the repository)`: zlecenie `"model":"fable"`, odpowiedzi recenzenta `claude-sonnet-5-5`). Do czasu tej zmiany doradca dnia dopisuje w poleceniu startu każdego wdrożenia, że najmocniejszy dozwolony model to Opus.

### Acceptance criteria

- Opis PR-a podaje przyczynę porażki testu bramki z pozycji 1 (utrata linii przy równoczesnym dopisywaniu do jednego pliku na Windows) zamiast „nieudany przebieg na zajętej maszynie”, jak mówił opis PR #117.

### Questions to settle

- Czy po naprawie modułu próbnego zjawisko utraty linii dostaje stały test?
  - Answer: nie; naprawa tylko w module próbnym, bez stałego testu samej utraty linii, bo to zachowanie Windows, nie kodu the way.
  - Not chosen:
    - naprawa plus stały test, który odtwarza utratę linii przy dopisywaniu — pilnuje, żeby nikt nie wrócił do wspólnego pliku, ale to losowy, kilkusekundowy test w bramce, który sprawdza system operacyjny.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „1 a”.
- Czy krok sprawdzenia listy i zdanie wiążące WAY-139 kierują do przewodnika także punkty, które wpisują do skilla odpowiedź dla trzech osobno obsługiwanych pozycji listy?
  - Answer: tak; krok w `resolve_gaps.md` i zdanie WAY-139 zmieniane w miejscu, z *Verification* i *Rationale* zgodnymi ze zmianą.
  - Not chosen:
    - zmienić tylko dwa opisy katalogu (WAY-09 i mapa części), punktów nie ruszać — agent uzupełniający skill dla jednej z trzech pozycji może nie trafić do przewodnika; to pominięte wskazanie, nie błędna instrukcja.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „2 a”.
- Co z trzema szablonami wytycznych, które mówią, że każdy wybór nierozstrzygnięty przez zadanie zatrzymuje cykl?
  - Answer: dopisać w trzech zdaniach ograniczenie do wyboru z realnym kosztem, zgodnie z WAY-172.
  - Not chosen:
    - zostawić zdania i pokazywać nakładanie się w opisie PR-a przy każdym zadaniu wytycznych — agent piszący wytyczne z szablonu może stanąć na drobnej regule; jedna zbędna runda z Mariuszem za każdym razem.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „3 a”.
- Co robi skrypt kontroli fundamentu z niezmiennikiem, któremu w kopii bazowej brakuje *Method* albo *Part*?
  - Answer: wypisuje jedną linię `listed:` z nazwą niezmiennika i brakującym polem, bez zmiany kodu wyjścia, a WAY-344 dostaje zdanie, że brak pola w kopii bazowej idzie właśnie tak; linia wskazuje przypadek, który wypisanie ma łapać: zdanie mogło się zmienić bez porównania.
  - Not chosen:
    - dalej pomijać i dopisać do WAY-344 wyjątek dla kopii bazowej — zmieniony niezmiennik z luką w bazie przechodzi niezauważony.
    - nic nie robić, jak w PR #120 — rozjazd kodu z WAY-344 zostaje i wróci przy następnym przeglądzie.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „4 a”.
- Co wpisać w *Rejected* decyzji zapisanej przez cykl z własnego wyboru (oznaczenie `the cycle's`)?
  - Answer: `unknown`, chyba że wypowiedź człowieka nazywa rozważone drogi — wtedy te drogi, albo `none considered`, gdy człowiek tak powiedział; dwa zdania z punktów 10 i 11 *To do*.
  - Not chosen:
    - wariant z tabeli pytań cyklu (kolumna *Alternative rejected* z *Cost if wrong*) — odwraca granicę WAY-134 (pole mówi, co rozważył człowiek; „a way the writer derives … never enters it”), a *Cost if wrong* to koszt pomyłki wybranej odpowiedzi, nie powód odrzucenia drogi.
  - Source: Mariusz, 2026-11-14, rozstrzygnięcie sprawy AIR-650 (ai-review), przeniesione z notatki the author's task note on three matters after the change of the decision log (sprawa 4).
- Gdzie stoi klauzula, że identyfikator decyzji w zdaniu niezmiennika nie koliduje z WAY-56, i czym ją uzasadnić?
  - Answer: w WAY-60 i w punkcie szablonu niezmienników, który odsyła do WAY-60; uzasadnienie: identyfikator w zdaniu mówi, gdzie leży warunek, i nie jest powiązaniem z WAY-17, a powiązanie, gdy się należy, stoi obok zdania w swoim polu — tak jak w niezmienniku `tracked-file-private-paths`, który ma „as WAY-309 and WAY-323 name them” w zdaniu i te same numery w *Derives from*.
  - Not chosen:
    - to samo miejsce z uzasadnieniem „decyzja spoza dziennika produktu nie jest jego wpisem (WAY-58)” — nie pokrywa przykładu z samego the way, gdzie decyzje są z własnego dziennika, więc recenzent może uznać `tracked-file-private-paths` za kolizję.
    - klauzula w WAY-56 — zawęża zasięg zatwierdzonej decyzji.
    - nic nie dopisywać — pierwszy recenzent, który przeczyta najpierw WAY-56, może odrzucić poprawną formę; runda poprawki w cudzym zadaniu.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „5 a”.
- Jakie słowo wpisuje się w `Status:` dokumentu zadania, z którego człowiek zrezygnował?
  - Answer: a — `dropped — approved by human`, to samo słowo co w planie projektu.
  - Not chosen:
    - b) `dropped` — krótkie, ale inne niż w planie; przy zadaniu z planu dwa miejsca mówią to samo różnymi słowami i ktoś musi pamiętać, że to jedno.
    - c) `rejected` — inne niż w planie i myli się z odrzuceniem PR-a albo propozycji.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „punkt 13 — a („dropped — approved by human”, to samo słowo co w planie projektu)”.
- Czy reguła skilla planu ma wymagać w *Read* i *Checks* kawałka wszystkich niezmienników jego części, czy tylko tych, których dotyczy zmiana kawałka?
  - Answer: a — *Read* bez zmian, według WAY-62 (wszystkie niezmienniki, do których kawałek sięga); *Checks* tylko testy niezmienników, które zmiana kawałka może zepsuć; zgodne z rozstrzygnięciem AIR-515.
  - Not chosen:
    - b) w *Read* i *Checks* tylko niezmienniki, których dotyczy zmiana kawałka, ze zmianą zdania wiążącego WAY-62 — krótsze przekazanie (około 150 linii na kawałek), ale agent może nie zobaczyć niezmiennika z `every` i go złamać; łapie to dopiero recenzja albo bramka, z rundą poprawki.
    - c) praktyka dociąga do reguły: planujący wpisuje wszystkie, orkiestrator pilnuje — *Checks* każdego kawałka zbliżają się do pełnej bramki, wbrew rozstrzygnięciu AIR-515 i odrzuceniu „the gate after every slice” w WAY-160.
    - zostawić bez zmian — reguła dalej wymaga tego, czego nikt nie robi, a recenzent czytający ją dosłownie może zakwestionować każdy plan.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „punkt 14 — a (Read bez zmian wg WAY-62, Checks tylko testy niezmienników, które zmiana kawałka może zepsuć; zgodne z AIR-515)”.
- Co uruchamia w *Checks* kawałek planu, który zapisuje niezmiennik z metodą `test`, gdy jego test pisze dopiero późniejszy kawałek?
  - Answer: a — kontrolę fundamentu z przełącznikiem `--skip-test-citations` zamiast testu, który uruchamia ją bez przełącznika; zdanie w punkcie *Checks* skilla planu, oparte na przykładzie zgodności WAY-321, która zostaje bez zmian.
  - Not chosen:
    - b) taki kawałek nie wpisuje do *Checks* testu, który uruchamia kontrolę bez przełącznika, bo kontrola z przełącznikiem przeszła przy zapisie wpisu (`elements/common/way_of_working.md`, krok 4.3) — zmiany fundamentu zrobione później w tym samym kawałku czekają na sprawdzenie do bramki przed PR-em.
    - c) bez zdania, tylko nowe brzmienie *Checks* z punktu 14 — planujący dalej może wybrać ten test, bo `test-method-citation` ma *Part* `every`; czerwony wynik między kawałkami zostaje i kończy się rundą wyjaśnień albo cofnięciem metody na `review`.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, odpowiedź „1 a — zdanie w Checks skilla planu: kawałek, który dopisuje niezmiennik z metodą test pisany dopiero przez późniejszy kawałek, uruchamia kontrolę fundamentu z --skip-test-citations; oprzyj się na przykładzie zgodności WAY-321”.
- Kolejność cyklu tego zadania i zadania „the way: skrypty po przeglądzie fundamentu — brakujące pole, kontrole tekstów i ich testy, liczenie audytu”, które zmienia ten sam plik `elements/common/foundation_check.py` i to samo zdanie WAY-344.
  - Answer: bez zależności; cykl, który scala się drugi, odświeża gałąź i godzi oba zdania WAY-344 i obie zmiany `foundation_check.py`.
  - Not chosen:
    - jedno zadanie czeka na drugie — dzień albo więcej przestoju za konflikt w kilku liniach jednego zdania i jednej funkcji.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15 (jak przy pytaniu 6: za rekomendacją); przeniesione z the author's task note on the scripts after the foundation review, pytanie 9.
- Czy część, którą cykl dopisuje do wpisu z wiersza albo do zaprojektowanego wpisu, trafia przed człowieka?
  - Answer: tak, para przykładów i pole, które zaprojektowany wpis zostawił `TODO` — wpis dostaje oznaczenie `the cycle's` (*To do* 17), a skill decyzji mówi, że w cyklu człowiek przyjmuje taką parę przy scaleniu (*To do* 18); powiązania nie, a para trzymana tylko do testu tej samej zmiany też nie.
  - Not chosen:
    - b) każda dopisana część, także powiązanie, przed człowiekiem — cykl dopisuje powiązania niemal zawsze, więc góra opisu PR-a staje się ścianą tekstu, drogą, którą WAY-114 odrzuciła.
    - zakazać cyklowi dopisywania przykładów, których nie ma w zadaniu — decyzji bez testu nic nie trzyma, sprawdzenie fundamentu zatrzymuje cykl i każdy taki przypadek kończy się pytaniem w zablokowanym szkicu PR-a.
    - zostawić bez zmian — przykłady wchodzą raz z wiedzą człowieka, raz bez niej.
  - Source: Mariusz w `/ai-review`, 2026-11-15 (AIR-661): „c” (dołączyć do tego zadania).

## Context

- Zadanie składa cztery notatki, które zostały w `_zadania/` z pełnym materiałem: the author's task note on the gate test of three directories at once (pozycja 1, z PR #117), the author's task note on the deployment guide in the descriptions of parts (pozycja 2, z PR #119), the author's task note on three matters after the change of the decision log (pozycja 3, z PR #120 i AIR-650) i the author's task note on the identifier in an invariant's sentence (pozycja 4, z PR #121).
- Nieudany przebieg bramki: `git show 73c5437fc9e097490af28a8160b6a6f2cdbd8381:docs/task-cycles/installer-junction-refusal/final-gate-2-failed.log` — katalogi `a` i `c` padły po 120 s z „did not meet the others”, a `b` przeszedł w 0,115 s, czyli w pliku zginęła linia `start b`.
- Próba odtworzenia przy doprecyzowaniu (2026-11-14, Python 3.14.3, Windows 11): trzy procesy startujące w tej samej chwili dopisują po jednej linii do jednego pliku przez `open(..., 'a')`; w 196 próbach na 200 w pliku brakowało jednej albo dwóch linii; w prawdziwym teście procesy startują w odstępach, więc kolizja jest rzadka.
- Moduł próbny i wspólny plik `timeline.log` weszły w PR #111 (commit `a6807f1`), razem z równoległym uruchamianiem katalogów bramki.
- Kod i testy w częściach `gate` i `elements-common` objęte są odstępstwem WAY-328, więc zadanie nie czeka na wytyczne kodowania ani testowania the way.
- Opis PR #117 przedstawia porażkę jako „nieudany przebieg na zajętej maszynie, przyczyna nieustalona” (https://github.com/mariusznazar/the-way/pull/117, sekcje „Fix or let through” punkt 2 i „Findings outside the task's scope” punkt 2).
- Przewodnik ma części „## 6. How to read the logs”, „## 7. How long the record lives, between deployments too” i „## 8. How a human learns of a failure”; jego treści i miejsca zadanie nie zmienia, a decyzję o zadaniu zamiast poprawki w PR podjął Mariusz w https://github.com/mariusznazar/the-way/pull/119#issuecomment-6872066189, punkt 1.
- Pominięcie niezmiennika bez pola w bazie to wybór D9 specu cyklu PR #120 (https://github.com/mariusznazar/the-way/blob/07a2ba5ef5a9c4c0b97722f0d982544603f798a6/docs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md); WAY-344 stała w fundamencie od 2026-11-12, przed scaleniem PR #120.
- Uwagi recenzenta do pozycji 3 (m3, m4, o1) w oryginalnym brzmieniu: https://github.com/mariusznazar/the-way/blob/07a2ba5ef5a9c4c0b97722f0d982544603f798a6/docs/task-cycles/co-trafia-do-dziennika-decyzji/reports/unread-review-report.md
- Uwaga M1 do pozycji 4 w pełnym brzmieniu: `git show a2a8d88:docs/task-cycles/service-reading-and-invariant-condition/reports/correction-1-review-report.md`, sekcja „Minor, within the task”.
- `agent-instructions/README.md`, sekcja „The form of the foundation”, opisuje wypisanie niezmienników, których zdanie zmiana przeredagowała; krok powrotu cyklu porówna ją ze zmianą z punktu 8.
- Pozycje 13 i 14 dopisał doradca dnia 2026-11-14 za zgodą Mariusza (uwagi sesji cyklu the way z nocy 13–14.11, zapisane w pliku stanu doradcy z 13.11, wpis 02:10): zadanie AIR-515 po rezygnacji zostało ze „Status: refining”, bo szablon nie ma wartości dla zadania odrzuconego; planujący wybierają kilka niezmienników części, choć reguła z WAY-62 każe wpisać wszystkie. Po scaleniu sprawdzanie zgodności notatek z liniami zadań w vaulcie (`scripts/agent_tasks_check.js` i `system_zadan.md`, sekcja „Zadania agentowe”) musi rozpoznawać dokładnie wartość `dropped — approved by human` — to zmiana poza repozytorium the way, którą robi doradca dnia albo Mariusz.
- Rozjazd reguły z praktyką przy pozycji 14, plan cyklu PR #120 (`git show 07a2ba5:docs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`): w kopii bazowej 17 z 34 niezmienników ma *Part* `every`, więc każdy kawałek sięga co najmniej 17 z nich; *Read* kawałka 1 wymienia 5 niezmienników, kawałka 7 żadnego, a *Checks* uruchamiają testy jednego do trzech katalogów.
- Testy niezmienników z *Part* `every` leżą co najmniej w katalogach `agent-instructions`, `elements/common`, `elements/part-map`, `gate` i `task-cycle`, więc uruchamianie ich po każdym kawałku zbliża się do pełnej bramki.
- Rozstrzygnięcie AIR-515 z 14.11.2026 (po kawałku planu nie dokładamy testów, bramka przed PR-em łapie zepsuty test, audyt liczy kolejne przypadki) stoi w notatce audytu procesu, `audyt_usprawniania_procesu.md`, punkt „Testy psujące się po kawałku planu”.
- Sprawa 3 pozycji 3 (reguła lektury WAY-150 nie prowadzi do decyzji pilnowanej linią `decision:` zmienianego testu) jest przekazana zadaniu the author's task note on how an agent reads the decision log, gdzie stoi jako jego punkt 3 *To do*.
- Przegląd fundamentu 2026-11-14 (grupa G6) dopisał do zadania dwie uwagi recenzenta PR #93 spoza zakresu tamtego zadania: #93-5 (czerwona kontrola fundamentu między kawałkami planu; *To do* 16) i #93-4 (*Scope* WAY-61; *To do* 15); decyzja Mariusza 2026-11-14 w pliku danych przeglądu, pod tabelą G6.
- Uwaga #93-5 w oryginalnym brzmieniu: „On a planned route, a slice that writes a `test` invariant before the slice that writes its test would fail the focused check `test_the_way_foundation_passes` between the two slices” (opis PR #93, sekcja „Findings outside the task's scope”, punkt 2).
- Test `test_the_way_foundation_passes` uruchamia `elements/common/foundation_check.py` na fundamencie the way bez przełącznika `--skip-test-citations` i cytuje niezmienniki `map-reference-target` i `test-method-citation`; przełącznik pomija tylko zgłoszenie niezmiennika `test`, którego nie cytuje żaden test (WAY-321).
- *Defect introduced by*: #93 — zdanie WAY-61 o niezmienniku, którego test pisze późniejszy kawałek (commit `9d499d0`), weszło przy zdaniu *Checks* skilla planu sprzed tej zmiany (`9131d0d`), bez *Scope* `task-cycle`.
- WAY-56 jest wycofana (`foundations/decisions.md`, tabela „Withdrawn identifiers”): jej reguła stoi w szablonie niezmienników, więc klauzula z *To do* 12 idzie do WAY-60 i do szablonu; pytanie o miejsce klauzuli zostaje w brzmieniu sprzed wycofania.
- Zadanie o skryptach po przeglądzie fundamentu zmienia WAY-344 kodem do reguły i dwoma wąskimi wyjątkami (poziomy tabel rejestru, wpis `repository`), bez wyjątku dla kopii bazowej, więc zdanie z *To do* 9 nie koliduje z jego wyborem.
- Dawny punkt 4 *To do* (przewodnik wdrożeniowy w zdaniu części `project-level` mapy) przeszedł 2026-11-15 do zadania the author's task note on the dependency line of the part map, które przepisuje to zdanie w całości (decyzja doradcy dnia w imieniu Mariusza, odpowiedź „5 a”).
- Plik danych przeglądu fundamentu 2026-11-14: `the data file of the foundation review of 2026-11-14 in the author's notes`, sekcja „Grupy uwag”, G6.

## Questions carried to cycle

- Technika naprawy modułu próbnego (np. osobny plik na proces albo jawna blokada przy zapisie) i to, jak testy, które sprawdzają kolejność linii (`--jobs 1`, limit zadań), dalej ją widzą.
- Brzmienie klauzuli w WAY-60 i w szablonie niezmienników, zdania w WAY-344 oraz poprawionego zdania WAY-139 z jej *Verification* i *Rationale*.

## Human actions

none

## Decisions in play

- WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one?: „[…] the task gains an item of its To do for that work or the human splits that work into a task of its own, and that item and that task point to the guide, which an agent reads only when it writes or completes a deployment skill; for the items on how to read the logs, on the record's life and on a failure, the check quotes the answer a decision of the foundation or an approved definition the task carries already gives, and the task gains the item that writes it into the skill […]” Zadanie zmienia to zdanie: punkt, który wpisuje odpowiedź do skilla dla jednej z trzech pozycji, też wskazuje przewodnik; wybór drogi „2 a” to zgoda na zmianę (WAY-314).
- WAY-172 — How is a new or changed meaning of a product's guidelines approved?: „A new or changed meaning of a product's guidelines that carries a choice with a real cost is a decision of the product's log, new or changed, […] A new or changed rule that only says how to write code, tests or the look of the product, with no decision, is accepted by the human as a row of the task's table of settlements before the code that uses it, or, where the cycle found the rule itself, at the merge from the request's description […]” Zadanie nie zmienia decyzji; doprowadza do zgodności z nią trzy szablony wytycznych.
- WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?: „The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them […]” Bez zmiany.
- WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?: „[…] except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit […]” Zadanie zmienia decyzję: brak pola w kopii pliku z commita bazowego skrypt kontroli fundamentu wypisuje linią `listed:`, bez błędu i bez zmiany kodu wyjścia; wybór drogi „4 a” to zgoda na zmianę (WAY-314).
- WAY-134 — How does a task carry what its refinement settles for the foundation?: „[…] and gives a decision written from a row as its rejected options only the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown` […]” Bez zmiany; szablon decyzji dostaje odpowiednik tej reguły dla decyzji oznaczonej `the cycle's`.
- WAY-60 — Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities?: „An invariant whose condition stands outside its sentence names by identifier the entry or the decision that holds the condition, in a field where the template gives one and otherwise in its sentence.” Zadanie dopisuje klauzulę, że tak wpisany identyfikator jest częścią warunku, nie powiązaniem z WAY-17; wybór drogi „5 a” to zgoda na zmianę (WAY-314).
- WAY-17 — Which links between foundation entries are mandatory?: „Every link of the chain fact → decision → invariant → test is written in the entry that depends on the other, and none is optional […]” Bez zmiany.
- WAY-61 — How is an invariant's method of checking written?: „The method is held on the finished change: an invariant whose test a later slice of the same change writes may read `test` from its writing on.” — **Scope:** invariants, gate, decisions, part-map, elements-common. Część wiążąca bez zmiany; zadanie dopisuje `task-cycle` do *Scope* (punkt 15 *To do*), jak postanowił Mariusz przy przeglądzie fundamentu 2026-11-14.
- WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it?: „`elements/common/foundation_check.py` reports an invariant whose method reads `test` and which no line `invariant: <identifier>` in a file git tracks other than Markdown cites, in every run but the one made right after an entry is written, which passes the switch `--skip-test-citations` and so skips this report and no other.” Bez zmiany; punkt 16 *To do* opiera się na jej przykładzie zgodności „the run right after an invariant that reads `test` is written, whose test a later slice of the same change writes, passes the switch and reports nothing”.
- WAY-62 — What does an invariant entry name in the part map?: „[…] and the agent making the change reads every invariant it reaches.” Bez zmiany; *Read* kawałka dalej wymienia każdy niezmiennik, do którego kawałek sięga.
- WAY-160 — How does the task-cycle orchestrator run the finished change's gate?: „[…] neither a plan's *Checks* nor a handoff names a run of it.” Część wiążąca bez zmiany; zdanie uzasadnienia o „focused checks of the code and invariants a slice reaches” zgadza się z nowym brzmieniem *Checks* (punkt 14 *To do*).
- WAY-142 — What does the breakdown of a project write, and in what form?: „Each task stands in one row of one table of tasks, with the columns and states the plan template gives […]” Bez zmiany; punkt 13 bierze słowo `dropped — approved by human` ze stanów tego szablonu.
- WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?: „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217 […]” Bez zmiany.

## Settlements to record

Candidates: 11 shown, 9 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Punkt *To do*, który wpisuje do skilla wdrożeniowego odpowiedź o czytaniu logów, o czasie życia zapisu albo o awarii, też wskazuje przewodnik po pisaniu skilla wdrożeniowego. | sentence of WAY-139 | pytanie „Czy krok sprawdzenia listy i zdanie wiążące WAY-139 kierują do przewodnika także punkty…” (wybór człowieka; droga niewybrana pod pytaniem) | czy zmienić tylko krok w `resolve_gaps.md`, a WAY-139 zostawić, czy odwrotnie |
| 2 | Wybór nierozstrzygnięty przez zadanie zatrzymuje cykl na zablokowanej prośbie tylko wtedy, gdy niesie realny koszt; reguła, która tylko mówi, jak pisać, idzie drogą WAY-172. | skill or instruction file: product-guidelines/coding/template.md, product-guidelines/styleguide/template.md, product-guidelines/testing/template.md | pytanie „Co z trzema szablonami wytycznych…” (wybór człowieka; droga niewybrana pod pytaniem) | czy zostawić zdania szablonów i pokazać nakładanie się tylko w opisie PR-a |
| 3 | Brak *Method* albo *Part* w kopii bazowej niezmiennika skrypt kontroli fundamentu wypisuje jedną linią `listed:` z nazwą niezmiennika i polem, bez błędu i bez zmiany kodu wyjścia. | sentence of WAY-344 | pytanie „Co robi skrypt kontroli fundamentu z niezmiennikiem, któremu w kopii bazowej brakuje…” (wybór człowieka; drogi niewybrane pod pytaniem) | czy brak pola w bazie pominąć z wyjątkiem w WAY-344, zgłosić błędem z kodem 1, czy wypisać linią |
| 4 | *Rejected* decyzji oznaczonej `the cycle's` dostaje `unknown`, chyba że wypowiedź człowieka nazywa rozważone drogi — wtedy te drogi, albo `none considered`, gdy człowiek tak powiedział. | skill or instruction file: elements/decisions/template.md, task-cycle/skill/foundation_step.md | pytanie „Co wpisać w *Rejected* decyzji zapisanej przez cykl z własnego wyboru…” (wybór Mariusza w AIR-650; droga niewybrana pod pytaniem) | czy wpisać wariant z tabeli pytań cyklu, `none considered` czy `unknown` |
| 5 | Identyfikator decyzji wpisany w zdanie niezmiennika, bo ta decyzja trzyma jego warunek, jest częścią warunku, a nie powiązaniem z WAY-17; powiązanie, gdy się należy, stoi obok zdania w swoim polu. | sentence of WAY-60 | pytanie „Gdzie stoi klauzula, że identyfikator decyzji w zdaniu niezmiennika nie koliduje z WAY-56…” (wybór człowieka; drogi niewybrane pod pytaniem) | czy klauzulę oprzeć na „decyzja spoza dziennika produktu nie jest jego wpisem” i czy postawić ją w WAY-56 |
| 6 | *Read* kawałka planu zostaje według WAY-62, a jego *Checks* uruchamiają tylko testy niezmienników, które zmiana kawałka może zepsuć. | skill or instruction file: task-cycle/plan/SKILL.md | pytanie „Czy reguła skilla planu ma wymagać w *Read* i *Checks* kawałka wszystkich niezmienników jego części…” (wybór człowieka; drogi niewybrane pod pytaniem) | czy wpisywać do *Checks* testy każdego niezmiennika, do którego kawałek sięga, czy zawęzić także *Read* i zmienić WAY-62 |
| 7 | Dokument zadania, z którego człowiek zrezygnował, ma `Status: dropped — approved by human`, to samo słowo co w planie projektu. | skill or instruction file: project-level/task/template.md | pytanie „Jakie słowo wpisuje się w `Status:` dokumentu zadania, z którego człowiek zrezygnował?” (wybór człowieka; drogi niewybrane pod pytaniem) | czy wpisać `dropped`, `rejected` czy słowo z planu projektu |
| 8 | Kawałek planu, który zapisuje niezmiennik z metodą `test`, gdy jego test pisze późniejszy kawałek, uruchamia w *Checks* kontrolę fundamentu z przełącznikiem `--skip-test-citations` zamiast testu, który uruchamia ją bez przełącznika. | skill or instruction file: task-cycle/plan/SKILL.md | pytanie „Co uruchamia w *Checks* kawałek planu, który zapisuje niezmiennik z metodą `test`…” (wybór człowieka; drogi niewybrane pod pytaniem) | czy wpisać do *Checks* `test_the_way_foundation_passes`, pominąć go, czy uruchomić kontrolę z przełącznikiem |
| 9 | Para przykładów albo pole po `TODO`, które cykl dopisuje do wpisu z wiersza albo do zaprojektowanego wpisu, czyni wpis `the cycle's` i trafia przed człowieka przy scaleniu; powiązanie i para trzymana tylko do testu tej samej zmiany — nie. | skill or instruction file: task-cycle/skill/foundation_step.md, elements/decisions/skill/SKILL.md | pytanie „Czy część, którą cykl dopisuje do wpisu z wiersza…” (wybór Mariusza w AIR-661; drogi niewybrane pod pytaniem) | czy dopisaną parę pokazać człowiekowi, czy wpis z wiersza zostaje „z wiersza” mimo dopisku |

## Out of scope

- Sprawa 3 pozycji 3 (lektura decyzji pilnowanej linią `decision:` zmienianego testu) — należy do zadania „jak agent czyta dziennik decyzji”.
- Pozostałe uwagi Minor z PR #120 (m1, m2, m5, M12, M15, N2 i długa linia w WAY-168).
- Uwagi M2 i O1 recenzji korekty z PR #121.
- Treść i miejsce przewodnika po skillu wdrożeniowym oraz skill wdrożeniowy loop2.
