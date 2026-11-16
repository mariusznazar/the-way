---
title: Dać agentom the way metodę testowania w działającym produkcie tego, czego nie łapią testy automatyczne
status: draft
created: 2026-10-25T16:00
updated: 2026-11-15
tags: [zadanie]
related: "the author's project note on the process"
---

# Dać agentom the way metodę testowania w działającym produkcie tego, czego nie łapią testy automatyczne

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Agent, który robi zmianę w cyklu zadania produktu, sprawdza swoją pracę testami automatycznymi, a przy zmianie ekranu ogląda jeszcze stany komponentów i zrzut ekranu działającego produktu (`task-cycle/change/ui_check.md`).
- Żaden krok cyklu nie każe agentowi ustalić, czego testy zmiany nie obejmują w zachowaniu, które użytkownik widzi w działającym produkcie, zaplanować sprawdzenie tego zakresu, przeprowadzić je i wydać werdykt.
- Odczuwa to Mariusz jako recenzent PR-a produktu (np. `loop2`): o tym, czy zachowanie spoza testów zostało sprawdzone i jak, decyduje dziś agent sam.
- Dziś ryzyko jest hipotetyczne: w źródłach nie ma przypadku, w którym brak takiego sprawdzenia przepuścił błąd. Pojawi się przy zmianie, którą użytkownik widzi w działającym produkcie, a której nie sprawdza żaden test ani zrzut ekranu.
- Metoda stoi na drodze agenta do działającego produktu, a reguły the way kierują tę drogę i miejsce zrzutów ekranu w dwa miejsca naraz: WAY-121, WAY-165, WAY-316 i WAY-319 — do fundamentu produktu, pytanie 1 szablonu decyzji („Is it an instruction for how an agent works?”) — do skilla. loop2 poszedł za szablonem i 2026-11-14 przeniósł je do skilla, więc jego cykl, idąc dosłownie za the way, nie pokaże zrzutu, choć miejsce istnieje.
- Krok technologii nie niesie warunku WAY-319 o dwóch cyklach bez wspólnej przeglądarki, więc nowy produkt dowie się o konflikcie z błędów pierwszych równoległych cykli.

### To do

1. Dodać w `task-cycle/` obok skilla autora (`task-cycle/change/SKILL.md`) plik z metodą sprawdzenia w działającym produkcie, na wzór `task-cycle/change/ui_check.md`, i wskazać go w sekcji „## 3. Check your own work” tego skilla tak, jak dziś wskazane jest „Before you finish a change that alters what a screen shows, read `ui_check.md`”: autor zmiany bez planu i wykonawca części planu czytają plik, gdy ich praca zmienia zachowanie, które użytkownik widzi w działającym produkcie — ekran, odpowiedź API, polecenie w terminalu, dane, które produkt pokazuje. Poprawka po recenzji (`task-cycle/change/fix.md`) pliku nie czyta: punkt w tej sekcji wymienia czytających wprost, bo dziś punkt o `ui_check.md` nie ogranicza się do żadnego wariantu. Metoda prowadzi przez:
   - przygotowanie: zadanie (dla części — fragmenty zadania z jej zlecenia), zmiana, droga agenta do działającego produktu, którą ustala fundament produktu, i sprawdzenie, czy produkt działa, zanim cokolwiek zostanie uznane za niedostępne;
   - co zmiana zmienia dla użytkownika i jakiego kodu wspólnego z innymi ścieżkami dotyka;
   - zakres: wymagania zadania zestawione z tym, co już pokrywają testy zmiany;
   - plan przypadków ułożony według wymagań zadania, nie według samego kodu, z kolumną „czym sprawdzam” wypełnianą drogą produktu, w kolejności warunków wstępnych i budowy stanu, z ostatnią pozycją „rozpoznanie poboczne” na to, co agent zauważy po drodze;
   - wykonanie przypadek po przypadku: przypadek, który wypadł źle, nie przerywa przejścia, a plan rozszerza się tylko na twardy sygnał z przebiegu (błąd w logach na niesprawdzanej ścieżce, rozjazd między odpowiedzią API a ekranem, nieoczekiwany zapis);
   - werdykt dla każdego przypadku osobno, z nazwaniem warstwy, gdy to ona rozstrzyga („API liczy dobrze, ekran rysuje źle”), poprzedzony krokiem „czego nie sprawdziłem” z powodem przy każdej pozycji;
   - porównanie dwóch pomiarów nazywa, co z czym i kiedy porównano, zanim różnica zostanie nazwana regresją; pomiary nieporównywalne dają werdykt „nie wiem”.
2. Zapisać w tym pliku zasady przejścia:
   - przejście nie uruchamia w działającym produkcie skutku poza nim, który kosztuje albo którego nie da się cofnąć (prawdziwy mail, płatność, płatne API), chyba że produkt ustala dla niego atrapę; inaczej przypadek zostaje niesprawdzony, z powodem;
   - gdzie przypadek da się sprawdzić odczytem stanu strony albo odpowiedzi API, werdykt opiera się na tym odczycie, a zrzut ekranu służy człowiekowi;
   - werdykt bierze pod uwagę wszystko, co użytkownik widzi na ekranie — okienka i komunikaty też — nie tylko sprawdzany element;
   - gdy droga do produktu albo przeglądarka nie działa, agent zapisuje to ograniczenie i podaje dowód z warstwy, którą faktycznie sprawdził, zamiast uznać przypadek za sprawdzony;
   - przypadek niesprawdzony z braku narzędzia nazywa narzędzie, którego zabrakło;
   - gdy fundament produktu nie ustala drogi do działającego produktu, sprawdzenie jest niewykonane z tym powodem, a cykl się nie zatrzymuje; autor mimo to układa plan przypadków według wymagań zadania, nie wykonuje go i oznacza każdy przypadek jako niesprawdzony z tym powodem, żeby opis PR-a miał listę i kroki do ręcznego sprawdzenia;
   - przypadek, który wypadł źle, autor poprawia przed recenzją, a poprawka dostaje test na najniższym poziomie, który ten błąd łapie; każda niezgodność z zadaniem jest błędem do poprawienia, nie uwagą na marginesie;
   - błąd poza zakresem zadania autor zgłasza w raporcie zamiast go poprawiać.
3. Raport autora i wykonawcy części (`task-cycle/change/SKILL.md`, sekcja „## 6. Commit and report”) podaje przy takiej zmianie: plan przypadków, werdykt każdego, gdzie sprawdzono (system, przeglądarka, adres), co wypadło źle, co poprawiono i jakim testem, czego nie sprawdzono i dlaczego, błędy poza zakresem zadania — albo że zmiana nie zmienia zachowania widocznego dla użytkownika.
4. Recenzja (`task-cycle/review/SKILL.md`, punkt otwierany „The author's own-work check”) czyta raport przejścia: czy ocena, że zmiana zmienia albo nie zmienia zachowania widocznego dla użytkownika, się zgadza, czy przypadki wynikają z wymagań zadania i czy każdy przypadek niesprawdzony ma powód.
5. Opis PR-a (`task-cycle/skill/request_template.md`): przypadek przejścia, którego autor nie sprawdził, stoi w pozycji **4.** *Skipped steps and unrun checks* z powodem, a gdy da się go sprawdzić ręcznie, z krokami; błąd spoza zakresu zadania znaleziony przy przejściu trafia do sekcji dla decyzji człowieka jako sprawa do rozstrzygnięcia (zrobić z niego zadanie czy puścić). Przy zmianie ekranu, gdy fundament nie ustala drogi do działającego produktu, zrzut ekranu „niesprawdzony” (`task-cycle/change/ui_check.md`) i przejście „niewykonane” z tej samej przyczyny stoją w opisie PR-a jako jedna pozycja, nie dwie; `task-cycle/change/ui_check.md` zostaje bez zmian.
6. W `elements/decisions/template.md`, w punkcie **Where it goes:**, przy pytaniu 1 („Is it an instruction for how an agent works?”), zapisać, że odpowiedź na sprawę drogi agenta do działającego produktu — logi, interfejs, dane deweloperskie, miejsce zrzutów — jest decyzją produktu, choć mówi agentowi, jak pracować, a skill produktu może trzymać kroki obsługi i powołuje się na tę decyzję; to samo zdanie dostaje WAY-121.
7. W haśle „agent's way to the running product” słownika the way (`foundations/glossary.md`) dopisać, że droga to także środek, którym agent pokazuje człowiekowi, co zobaczył.
8. W `project-level/technology/research.md`, punkt „3. **Consequences.**”, przy wyborze interfejsu: dla każdej opcji podać, czy dwa cykle zadania w osobnych worktree produktu mogą sprawdzać naraz bez wspólnej przeglądarki; opcja, która nie może, zostaje w porównaniu z tym brakiem. WAY-319 dostaje zdanie, że warunek dociera do produktu przez krok technologii.

### Questions to settle

- Kto przeprowadza sprawdzenie w działającym produkcie i w którym miejscu cyklu zadania?
  - Answer: autor zmiany, po napisaniu kodu, przed recenzją. Metoda stoi w pliku obok skilla autora (jak `task-cycle/change/ui_check.md`), czytanym tylko przy zmianie zachowania, które użytkownik widzi w działającym produkcie; plan, wyniki i „czego nie sprawdziłem” idą do raportu autora, który czyta recenzent. Warunek powrotu: gdy audyt procesu pokaże błąd przepuszczony przez autora przy takim sprawdzeniu, sprawdzenie przechodzi do osobnego etapu cyklu z nowym agentem i nowym skillem.
  - Not chosen:
    - recenzent całej zmiany jako dodatkowy krok przeglądu — recenzent dziś tylko czyta, musiałby uruchamiać produkt i budować stan danych, najdroższy etap rośnie, a każdy zły wynik to runda poprawki i ponowna recenzja
    - osobny etap cyklu z nowym agentem i nowym skillem — jeden agent więcej przy każdej zmianie widocznej dla użytkownika, nowy etap w skrypcie etapów, w liczbach audytu, w typach agentów i w szablonie PR-a; największa zmiana the way z trzech
    - nic nie zmieniać — zachowanie spoza ekranu dalej nie jest sprawdzane w działającym produkcie, a PR nie mówi, czego nie sprawdzono
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a — krok autora, z warunkiem powrotu na c, gdy audyt pokaże błąd przepuszczony przez autora”
- Przy jakich zmianach sprawdzenie jest wymagane i co robi agent, gdy fundament produktu nie ustala drogi do działającego produktu?
  - Answer: przy każdej zmianie zachowania, które użytkownik widzi w działającym produkcie — ekran, odpowiedź API, polecenie w terminalu, dane, które produkt pokazuje; ocenia to autor i podaje w raporcie, recenzent sprawdza tę ocenę. Gdy fundament produktu nie ustala drogi do działającego produktu, autor oznacza sprawdzenie jako niewykonane z tym powodem w raporcie i w PR-ze, a cykl się nie zatrzymuje; plan przypadków mimo to powstaje, a każdy jego przypadek jest oznaczony jako niesprawdzony z tym powodem. Zrzut ekranu niesprawdzony z tej samej przyczyny stoi w PR-ze razem z przejściem, jako jedna pozycja. Poprawka po recenzji przejścia nie powtarza.
  - Not chosen:
    - tylko przy zmianie ekranu — taniej, ale zostaje luka, o którą chodzi w zadaniu: API, terminal, przepływy
    - przy każdej zmianie, także czysto wewnętrznej — koszt bez zysku: przy przebudowie kodu bez zmiany zachowania przejście nic nie znajdzie
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2a”; plan przy braku drogi, scalenie zrzutu z przejściem i brak przejścia przy poprawce — Mariusz osobiście, 2026-11-14: „1b”, „3a”, „2a”
- Kto sprawdza zmianę robioną według planu w kilku częściach?
  - Answer: każdy wykonawca części, która zmienia zachowanie widoczne dla użytkownika, sprawdza swoją część na tle fragmentów zadania, które dostał — tak jak przy zrzucie ekranu (`task-cycle/change/ui_check.md`) i sprawdzeniu własnej pracy (WAY-164); stan pośredni widać w raporcie, który czyta recenzent całej zmiany.
  - Not chosen:
    - tylko wykonawca ostatniej części sprawdza całą zmianę — ten agent zna tylko swoją część i ma limit lektury, więc musiałby doczytać całe zadanie
    - w zmianach robionych częściami bez sprawdzenia — największe zmiany zostają bez niego
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3a”
- Kto zatwierdza plan sprawdzenia i skąd biorą się przypadki do wypróbowania?
  - Answer: nikt przed sprawdzeniem. Autor układa przypadki według wymagań zadania, nie samego kodu, z ostatnią pozycją „rozpoznanie poboczne”; plan i wyniki trafiają do raportu, który czyta recenzent, a człowiek widzi w PR-ze, czego nie sprawdzono (WAY-227).
  - Not chosen:
    - doprecyzowanie zadania zapisuje w dokumencie konkretne wejścia do wypróbowania podane przez człowieka — każde doprecyzowanie zadania widocznego dla użytkownika dostaje jedno pytanie więcej, a WAY-238 trzeba by doprecyzować, że taka lista nie jest planem testów; ma sens dopiero, gdy okaże się, że autor gubi warianty znane tylko człowiekowi
    - cykl zatrzymuje się na zatwierdzenie planu przez człowieka — sprzeczne z WAY-227 i z WAY-140 (żadnych pauz w środku cyklu)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „4a”
- Co dzieje się z przypadkiem, który wypadł źle?
  - Answer: autor poprawia go przed recenzją, a poprawka dostaje test na najniższym poziomie, który ten błąd łapie; raport mówi, co wypadło źle, co poprawiono i jakim testem; każda niezgodność z zadaniem jest błędem do poprawienia, nie uwagą na marginesie. Błąd poza zakresem zadania autor zgłasza, a trafia on do PR-a jako sprawa dla człowieka (zrobić zadanie czy puścić). Zły przypadek nie przerywa przejścia; diagnoza idzie na koniec.
  - Not chosen:
    - autor tylko zgłasza w raporcie, o poprawce decyduje recenzent — zawsze dodatkowa runda poprawki i ponownej recenzji
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „5a”
- W jakiej kolejności stoją przypadki planu?
  - Answer: według warunków wstępnych i budowy stanu, jak w `test-run`; sprawdzenie własnej pracy (WAY-164) zostaje osobno i bez zmian.
  - Not chosen:
    - najpierw przypadek, który najpewniej padnie — reguła odrzucona dla `test-run` w wierszu L2, bo zderza się z kolejnością wynikającą ze stanu i pcha do spekulacji przy drobnych zmianach
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „6a”
- Które pozycje dopisku z 12.11.2026 wchodzą do tego zadania?
  - Answer: wchodzą: podstawione płatne wywołania razem z blokadą działań nie do cofnięcia (przejście nie uruchamia skutku poza produktem, który kosztuje albo którego nie da się cofnąć, chyba że produkt ustala atrapę; inaczej przypadek niesprawdzony z powodem); wiedza o zachowaniach zależnych od platformy jako jedno zdanie raportu — gdzie sprawdzono; pomiar w kodzie zamiast samego odczytu zrzutu przez model; „nie dało się sprawdzić → nowe polecenie narzędzia” w wersji okrojonej — przypadek niesprawdzony nazywa narzędzie, którego zabrakło, a zadanie na narzędzie zakłada człowiek; zapis ograniczenia i dowód z warstwy faktycznie sprawdzonej, gdy przeglądarka nie działa; werdykt czyta wszystko, co użytkownik widzi na ekranie. Już są w the way: własne konto i katalog roboczy na instancję (WAY-373, WAY-319, WAY-165), gotowe stany startowe (WAY-165), przegląd i sprzątanie skryptów agentów (WAY-373). Poza zadaniem: limit jednoczesnych instancji, pole „jak to sprawdzić” w mapie części. Lista wejść do wypróbowania w zleceniu — rozstrzygnięta w pytaniu o plan.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „7 jak w tabeli”
- Co z `test-run` przechodzi do the way jako metoda, a co zostaje przy narzędziach VOX?
  - Answer: przechodzi metoda — przygotowanie (zadanie, zmiana, droga produktu, czy produkt działa), co się zmieniło dla użytkownika i jaki kod wspólny zmiana zahacza, zakres z wymagań zadania wobec tego, co pokrywają testy, plan przypadków z kolumną „czym” wypełnianą drogą produktu i pozycją „rozpoznanie poboczne”, rozszerzanie planu tylko na twardy sygnał, werdykt dla każdego przypadku z nazwaniem warstwy, krok „czego nie sprawdziłem”, sprawdzenie, czy pomiary są z tego samego świata, zanim różnica stanie się regresją. Zostaje przy VOX: Jira, Bruno, Playwright MCP, OpenSearch (zastępuje je droga ustalona przez produkt), zapis przebiegu w `~/.vox/test-runs/` (zastępują go raporty cyklu, `task-cycle/skill/request_template.md`), kolumna „Kto: Ty” i tryb interaktywny, pauza na plan, domykacze (`/report-bug`, aktualizacja e2e, dokumenty repo), pytanie do człowieka „czy ten objaw jest znany”, sprzątanie (WAY-373).
  - Not chosen:
    - cały `test-run` z trybem interaktywnym, do użycia także poza cyklem — sprzeczne z odpowiedzią na pierwsze pytanie (krok autora, nie osobny skill)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „8a”
- Czy droga agenta do działającego produktu i miejsce zrzutów ekranu muszą stać w fundamencie produktu, czy mogą stać w skillu produktu? (przegląd fundamentu 2026-11-14, P14: loop2 wycofał 2026-11-14 decyzje D-254, D-357, D-358 i D-359 — Playwright jako droga do gry, publiczne repozytorium na zrzuty, wypychanie zrzutu kontem właściciela, Playwright MCP tylko z sesji w worktree cyklu — jako „instruction to the agent, not a decision of the product” i przeniósł je do skilla `loop2-play`; WAY-121, WAY-165, WAY-316, WAY-319 i `ui_check.md` każą szukać drogi i miejsca w fundamencie)
  - Answer: muszą stać w fundamencie produktu, a the way dopisuje zdanie, które to mówi: odpowiedź na sprawę drogi agenta do działającego produktu (logi, interfejs, dane deweloperskie, miejsce zrzutów) jest decyzją produktu, choć mówi agentowi, jak pracować; skill produktu może trzymać kroki obsługi i powołuje się na tę decyzję. loop2 przywraca D-254, D-357, D-358 i D-359 w osobnym zadaniu.
  - Not chosen:
    - mogą stać w skillu — krok technologii musiałby szukać ich także w skillach; zmiana WAY-121, WAY-165, WAY-316, WAY-319, `ui_check.md`, szablonu opisu PR-a, skilla recenzji, `running_product.md`, `research.md` i słownika, około dziesięciu plików więcej; wybory z kosztem (Playwright zamiast innej drogi, publiczne repozytorium na zrzuty) tracą uzasadnienie i odrzucone opcje, bo skill daje regule jedno zdanie powodu; przegląd fundamentu nie czyta skilli
    - muszą stać w fundamencie, a the way niczego nie dopisuje, tylko loop2 przywraca decyzje — następny produkt zastosuje pytanie 1 szablonu decyzji tak samo jak loop2 i znowu je wycofa
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 c, 2 a, 3 a”
- Co z uwagą #91-4: słownik nazywa drogę agenta do działającego produktu „the means through which an agent checks”, a WAY-121 liczy do jej spraw miejsce zrzutów, które niczego nie sprawdza?
  - Answer: dopisać do hasła słownika, że droga agenta do działającego produktu to także środek, którym agent pokazuje człowiekowi, co zobaczył.
  - Not chosen:
    - zostawić — dziś nic się nie psuje, ale definicja i WAY-121 dalej się rozjeżdżają, a czytelnik słownika uzna, że miejsce zrzutów nie należy do drogi
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 c, 2 a, 3 a”
- Jak warunek WAY-319 (dwa cykle sprawdzają produkt naraz bez wspólnej przeglądarki) ma docierać do produktu, skoro krok technologii (`project-level/technology/research.md`, punkt „Consequences”) go nie niesie, a *Rationale* WAY-319 mówi, że dociera przed konfliktem? (przegląd fundamentu 2026-11-14, P15, uwaga #91-2)
  - Answer: krok technologii, porównując opcje interfejsu, podaje dla każdej, czy dwa cykle zadania w osobnych worktree produktu mogą sprawdzać naraz bez wspólnej przeglądarki; opcja, która nie może, zostaje w porównaniu z tym brakiem, tak jak WAY-166 robi z opcją, której agent nie umie użyć; WAY-319 mówi, że warunek dociera do produktu przez ten krok.
  - Not chosen:
    - przepisać *Rationale* WAY-319, że warunek dociera do produktu dopiero przy sprawdzeniu autora — jedno zdanie, ale produkt dalej dowiaduje się o konflikcie z błędów pierwszych dwóch równoległych cykli (WAY-319 liczy 13 takich błędów)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 c, 2 a, 3 a”

## Context

- Pierwotne brzmienie zadania: „the way: skill do testowania zakresu, którego nie pokrywają skrypty, na wzór `test-run` (grunt, zakres, plan testu, wykonanie, werdykt) — dziś cykl zadania mówi tylko „zachowanie widoczne sprawdź też w uruchomionym produkcie”; źródło: lekcja „Towards Autonomous Product Development”, wiersz L2 w the author's private note with the map of articles”.
- Zdanie „zachowanie widoczne sprawdź też w uruchomionym produkcie” nie stoi już w skillach cyklu; jego miejsce zajmuje sprawdzenie stanów i zrzutu ekranu przy zmianie interfejsu (`task-cycle/change/ui_check.md`).
- Źródło zadania: notatka z kroku 3 (grupa 2) w `the author's private note with the map of articles`, pod tabelą: „`the-way` potrzebuje skilla do pisania testów i skilla do testowania zakresu poza skryptami (na wzór `test-run`)”.
- Wiersz L2 tej mapy: do the way przejęto sprawdzenie własnej pracy przez autora (WAY-164); dla warsztatu odrzucono regułę „najpierw przypadek, który padnie”, bo `test-run` już stawia pomiar kontrolny, a reguła „zderzyłaby się z kolejnością planu mającą realne powody (warunki wstępne, budowa stanu, konta współdzielone) i pchała do spekulacji na drobnych zmianach”.
- Wiersz A1 tej mapy wiąże krok technologii z tym zadaniem: droga agenta do działającego produktu (WAY-121, WAY-165) jest warunkiem takiego sprawdzenia.
- Skill-wzór: `the skill `test-run` of a team repository, which is not in this repository` (zespołowe repozytorium VOX).
- Szablon opisu PR-a już mówi o „the reports of the walk through the running product” (`task-cycle/skill/request_template.md`, pozycja **8.** *Unfixed findings the user or the human will feel*), choć przed tym zadaniem żaden etap cyklu takiego przejścia nie robił.
- Gdzie leżą ślady sprawdzenia, rozstrzygnęło zadanie o artefaktach testów (rozmowa 2026-11-08): do opisu PR-a trafiają tylko zrzuty ekranu spoza historii repo produktu, a ślady tekstowe zostają w raportach zapisu cyklu (WAY-316; reguła o śladach tekstowych stoi dziś w `task-cycle/skill/request_template.md`, akapit otwierany „Where a change alters what a screen shows”).
- Reguła sprawdzenia stanów i zrzutu ekranu przy zmianie interfejsu stoi dziś w `task-cycle/change/ui_check.md` (dawna WAY-219, wycofana): „Changing a user interface, check the states of the affected components that the applicable styleguide requires, and inspect a screenshot of the running product by the route its foundation settles; where it settles none, check the states in code and mark the screenshot unchecked with that reason.” Wzór dla przejścia: kto, kiedy, co przy braku drogi.
- Dopisek z 12.11.2026, przyjęty przez Mariusza jako materiał do tego zadania (sprawa 10 w `the author's private note with the human's rulings`): lista „laboratorium agenta” z kursu Mega.DEV (D21 i sekcja dopisków w `the author's private note on the practices of the first course`) i trzy rzeczy z kursu AI Tech Leaders (sekcja U4 w `the author's private note on the practices of the second course`); co z nich weszło, mówi odpowiedź pod pytaniem o dopisek.
- Przejęte praktyki wiążą the way tylko przez decyzję, która nazywa, co przejęto, gdzie obowiązuje i dlaczego (WAY-100): z `test-run` metoda wymieniona pod pytaniem o `test-run`, z kursów pozycje wymienione pod pytaniem o dopisek.
- Wytyczne kodu i testów: the way odchodzi od nich dla własnego kodu i testów (WAY-328), więc zadanie na nie nie czeka.
- Zadanie doradca dnia doprecyzował w imieniu Mariusza 2026-11-14 i przyjął dokument z góry, „o ile nie dojdzie nic nowego”.
- Przegląd fundamentu 2026-11-14 włączył do tego zadania propozycje P14 (z uwagą #91-4) i P15 (uwaga #91-2); ich pytania stoją pod *Questions to settle*. Plik danych przeglądu fundamentu 2026-11-14: `the author's private data file of the foundation review`, sekcja „Fundament” → „Propozycje”, P14 i P15.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-164** — „Before its work goes to review, the author of a one-author change names the requirement of the task, and the executor of each slice the requirement of its slice read against the passages of the task its handoff gives, that its work most likely does not meet, writes a check that would catch that, and states in its report which requirement, which check and what the check showed. The review that judges the work — a slice's own review where it has one, otherwise the review of the whole change — reads that report, and the request lists what each such check showed among its test evidence.” Zadanie zostawia ją bez zmian; przejście stoi obok niej.
- **WAY-121** — „As an exception to that rule, where the project brings behaviour a user sees in the running product, the step looks at four matters of an agent's way to the running product — its logs, its interface, its development data and the place of its screenshots — and lists as a choice of its own each matter that no decision of the foundation settles for that behaviour […]”. Przejście korzysta z tej drogi. Zadanie zmienia ją wariantem wybranym w pytaniu o miejsce drogi i zrzutów (c): dochodzi zdanie, że odpowiedź na sprawę drogi agenta do działającego produktu jest decyzją produktu, choć mówi agentowi, jak pracować, a skill produktu może trzymać kroki obsługi i powołuje się na tę decyzję.
- **WAY-165** — „[…] the interface asks how an agent operates the product as its user does — through a screen in a browser, a call to its API or a command in a terminal — and how it sees what the product answers. The development data asks where the data comes from on which an agent checks the product's behaviour outside production, and how an agent brings that data to the state a check needs […]”.
- **WAY-227** — „The orchestrator of a task cycle answers the agents' questions and gives provisional go-aheads under the task owner's delegation, never recording these as human approval, and brings the request to the human, the cycle's first point of human review.” Dlatego plan przejścia nie czeka na człowieka.
- **WAY-238** — „The author of a change chooses, in the task's cycle, which behaviour gets a permanent test and at which level, naming the break each test catches, and the review checks the choice against the product's testing guidelines, while a task's refinement holds no plan of tests.” Zadanie zostawia ją bez zmian: doprecyzowanie nie dostaje listy wejść do wypróbowania.
- **WAY-239** — „The template of the testing discipline requires the rule that a bug which only a high-level test or a human caught also gets a test at the lowest level that catches it.” Ta sama zasada obowiązuje poprawkę przypadku, który wypadł źle.
- **WAY-13** — „[…] an operation that cannot be undone is only prepared, and a human performs it after deciding at the request.”
- **WAY-140** — „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent […]”.
- **WAY-287** — „The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — the cycle's choices beyond the task's content, the steps skipped and the checks not run, […]”.
- **WAY-316** — „Where a change alters what a screen shows, the screenshots that its author or reviewer shows the human are embedded as images in the description of the request, from a place that the foundation of the product settles outside the product's repository; the-way names no place.” oraz akapit drugi (dawna WAY-317, wycofana): „Where a change alters what a screen shows and the foundation of the product settles no place for screenshots, the author inspects the screenshot as the author's check of a user-interface change gives and the request shows none: the section of its description for the human's decisions says that no screenshot is shown and why, and the cycle does not stop. A screenshot left unchecked for want of a settled way to the running product is reported as that check gives and needs no second item.”
- **WAY-166** — „In a choice of an agent's way to the running product, whether an agent can use an option is a consequence for the product: an option an agent cannot use stays in the comparison with that lack said as "an agent does not check the running product this way", and the recommendation passes over it. […]” Wzór dla warunku dwóch cykli w kroku technologii.
- **WAY-319** — „The way to the running product that the foundation of a product settles for its interface lets two task cycles working in separate worktrees of the product check at the same time without a browser they share, and an agent closes the browser it opened when its check ends.” oraz z *Rationale*: „Stated once for every way, the condition reaches a product before it meets the conflict.” Zadanie zmienia ją wariantem wybranym w pytaniu o warunek dwóch cykli (a): dochodzi zdanie, że warunek dociera do produktu przez krok technologii, który przy wyborze interfejsu podaje dla każdej opcji, czy dwa cykle mogą sprawdzać naraz.
- **WAY-373** — „An agent of a task cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own under the ignored `.runs/` directory of the task's worktree, never in the system's temporary directory, in a session's scratch directory or in the main checkout of the repository. […]”
- **WAY-125** — „Each agent reads the `SKILL.md` of its stage's method whole, and a file the method names, one beside that `SKILL.md` included, only when the step or variant that names the file comes, while the orchestrator reads no method it does not conduct.”
- **WAY-256** — „A fragment of a skill […] that only one variant of the skill needs, or only one step that some uses of the skill pass by, stands in a file beside the skill that the step names […]”. Dlatego metoda stoi w pliku obok skilla autora.
- **WAY-293** — „In the log of the-way, a rule that stands in one skill or template of the-way stands there with one sentence of its reason. It is an entry of the log only where it carries a choice with a real cost, one for which someone could reasonably propose the rejected way, and the skill or template then names that decision.” Pytanie 1 szablonu decyzji w logu the way; zadanie go nie zmienia — zdanie z *To do* 6 dotyczy logu produktu, w którym pytanie 1 brzmi bez tego zastrzeżenia, a *Rejected* WAY-293 już mówi, że w logu produktu powody i odrzucone drogi takiego wyboru ginęłyby ze skillem.
- **WAY-100** — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.”

## Settlements to record

Candidates: 11 shown, 11 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zachowanie widoczne w działającym produkcie, którego nie obejmują testy, sprawdza autor zmiany po kodzie, przed recenzją, a recenzent czyta jego raport; gdy audyt procesu pokaże błąd przepuszczony przez autora przy takim sprawdzeniu, sprawdzenie przechodzi do osobnego etapu cyklu z nowym agentem; poprawka po recenzji przejścia nie powtarza. | decision | wybór człowieka: pytanie „Kto przeprowadza sprawdzenie w działającym produkcie i w którym miejscu cyklu zadania?”; Mariusz osobiście, 2026-11-14: „2a” | czy przejście robi autor, recenzent czy nowy etap, kiedy do tego wrócić, i czy poprawka po recenzji też je robi |
| 2 | Sprawdzenie jest obowiązkowe przy każdej zmianie zachowania, które użytkownik widzi w działającym produkcie — ekran, odpowiedź API, polecenie w terminalu, pokazywane dane — a bez drogi do działającego produktu ustalonej w fundamencie jest niewykonane z tym powodem w raporcie i w PR-ze, bez zatrzymania cyklu; plan przypadków mimo to powstaje, z każdym przypadkiem oznaczonym jako niesprawdzony z tym powodem, a zrzut ekranu niesprawdzony z tej samej przyczyny stoi w PR-ze razem z przejściem jako jedna pozycja. | decision | wybór człowieka: pytanie „Przy jakich zmianach sprawdzenie jest wymagane…”; Mariusz osobiście, 2026-11-14: „1b”, „3a” | czy przejście obejmuje tylko ekran, czy brak drogi zatrzymuje cykl, czy plan powstaje bez drogi do produktu, i czy zrzut i przejście niesprawdzone z tej samej przyczyny to jedna pozycja czy dwie |
| 3 | W zmianie robionej według planu każdy wykonawca części zmieniającej zachowanie widoczne dla użytkownika sprawdza swoją część na tle fragmentów zadania, które dostał. | decision | wybór człowieka: pytanie „Kto sprawdza zmianę robioną według planu w kilku częściach?” | czy sprawdza każda część, ostatnia część, czy żadna |
| 4 | Plan przejścia nie czeka na zatwierdzenie: autor układa przypadki według wymagań zadania, a człowiek widzi w PR-ze, czego nie sprawdzono; doprecyzowanie zadania nie zapisuje listy wejść do wypróbowania. | decision | wybór człowieka: pytanie „Kto zatwierdza plan sprawdzenia…” | czy zatrzymać cykl na plan, i czy dopisać listę wejść do dokumentu zadania |
| 5 | Przypadek, który wypadł źle, autor poprawia przed recenzją z testem na najniższym poziomie, który ten błąd łapie, a błąd poza zakresem zadania zgłasza do PR-a jako sprawę dla człowieka. | decision | wybór człowieka: pytanie „Co dzieje się z przypadkiem, który wypadł źle?” | czy autor poprawia sam, czy oddaje recenzentowi, i czy poprawka dostaje test |
| 6 | Przypadki planu stoją w kolejności warunków wstępnych i budowy stanu, nie „najpierw ten, który padnie”, bo ta reguła zderza się z kolejnością wynikającą ze stanu. | skill or instruction file: plik metody obok `task-cycle/change/SKILL.md` | wybór człowieka: pytanie „W jakiej kolejności stoją przypadki planu?” | regułę kolejności przejętą z WAY-164 albo z Limena |
| 7 | Z dopisku z 12.11.2026 metoda przejmuje blokadę skutków płatnych i nie do cofnięcia, zapis, gdzie sprawdzono, werdykt z odczytu stanu zamiast samego zrzutu, nazwanie brakującego narzędzia, dowód z warstwy faktycznie sprawdzonej i odczyt całego ekranu. | skill or instruction file: plik metody obok `task-cycle/change/SKILL.md` | wybór człowieka: pytanie „Które pozycje dopisku z 12.11.2026 wchodzą do tego zadania?” | które pozycje kursów wejść do metody |
| 8 | Z `test-run` metoda przejmuje kroki przygotowania, zakresu, planu z „rozpoznaniem pobocznym”, wykonania i werdyktu dla każdego przypadku z krokiem „czego nie sprawdziłem”, a zostawia przy VOX narzędzia, zapis przebiegu, tryb interaktywny, pauzę na plan i domykacze. | skill or instruction file: plik metody obok `task-cycle/change/SKILL.md` | wybór człowieka: pytanie „Co z `test-run` przechodzi do the way…” | co z `test-run` przenieść, a co zostawić |
| 9 | Droga agenta do działającego produktu i miejsce zrzutów ekranu to decyzje produktu, choć mówią agentowi, jak pracować; skill produktu może trzymać kroki obsługi i powołuje się na te decyzje. | sentence of WAY-121 | wybór człowieka: pytanie „Czy droga agenta do działającego produktu i miejsce zrzutów ekranu muszą stać w fundamencie produktu…”; doradca dnia w imieniu Mariusza, 2026-11-15: „1 c” | czy szukać drogi i miejsca zrzutów w skillu produktu, czy tylko w fundamencie, i czy pytanie 1 szablonu decyzji kieruje je do skilla |
| 10 | Droga agenta do działającego produktu to środek, którym agent sprawdza zachowanie widoczne dla użytkownika i pokazuje człowiekowi, co zobaczył. | glossary term | wybór człowieka: pytanie „Co z uwagą #91-4…”; doradca dnia w imieniu Mariusza, 2026-11-15: „2 a” | czy miejsce zrzutów należy do drogi agenta, skoro słownik mówi tylko o sprawdzaniu |
| 11 | Warunek dwóch cykli sprawdzających naraz bez wspólnej przeglądarki dociera do produktu przez krok technologii, który podaje go przy każdej opcji interfejsu, a opcja, która go nie spełnia, zostaje w porównaniu z tym brakiem. | sentence of WAY-319 | wybór człowieka: pytanie „Jak warunek WAY-319…”; doradca dnia w imieniu Mariusza, 2026-11-15: „3 a” | czy krok technologii odrzuca opcję z jedną przeglądarką, pokazuje ją z brakiem, czy w ogóle nie pyta o ten warunek |

## Out of scope

- Gdzie leżą zrzuty ekranu i ślady sprawdzenia — rozstrzygnięte w WAY-316 i w `task-cycle/skill/request_template.md`.
- Zmiana skilla `test-run` w repozytorium `vox-ai-tools`.
- Limit jednoczesnych instancji agentów.
- Pole „jak to sprawdzić” przy części produktu w mapie części.
- Przywrócenie D-254, D-357, D-358 i D-359 w loop2 — osobne zadanie loop2 w backlogu projektu Loop, czekające na to zadanie.
