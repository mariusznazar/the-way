---
title: "the way: dziennik decyzji po przeglądzie fundamentu 2026-11-14 — uzasadnienia, ceny, brzmienia i klasa recenzji"
status: draft
created: 2026-11-15
updated: 2026-11-15
tags: [zadanie]
related: "the project's note in the author's vault"
---

# the way: dziennik decyzji po przeglądzie fundamentu 2026-11-14 — uzasadnienia, ceny, brzmienia i klasa recenzji

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/48 · https://github.com/mariusznazar/the-way/pull/79 · https://github.com/mariusznazar/the-way/pull/90 · https://github.com/mariusznazar/the-way/pull/100 · https://github.com/mariusznazar/the-way/pull/106 · https://github.com/mariusznazar/the-way/pull/109 · https://github.com/mariusznazar/the-way/pull/121 · https://github.com/mariusznazar/the-way/pull/122 · https://github.com/mariusznazar/the-way/pull/126

## Description

### Need

- Przegląd fundamentu the way z 2026-11-14 (sprawdzony commit `21ecb62`) znalazł wpisy fundamentu, których uzasadnienie, cena, odesłanie albo brzmienie przestały się zgadzać z repozytorium albo z innymi wiążącymi tekstami.
- Kto czyta te wpisy — agent cyklu, recenzent, Mariusz przy decyzji — dostaje powód, który dziś nie jest prawdziwy, odesłanie donikąd albo regułę bez odpowiedzi na swój przypadek.
- Jedna pozycja zmienia regułę, nie tylko tekst: recenzja całej zmiany i recenzja kroku powrotu biegną dziś na klasie orkiestratora, a pomiar zapisany w samej WAY-229 pokazuje, że recenzent tańszej klasy przepuszcza zmianę z blokującą wadą w 4 z 8 przebiegów.
- Mariusz zdecydował, że te sprawy idą jednym zadaniem (z całego przeglądu najwyżej ok. pięć nowych zadań).

### To do

1. WAY-229 (P1, P1a): recenzja całej zmiany i recenzja kroku powrotu biegną zawsze na najmocniejszej dostępnej klasie („the strongest class available”), nazwanej ogólnie, bez nazwy modelu i bez nazwy ustawienia narzędzia; to słowo ma w całym wpisie jedno znaczenie — to samo przy kawałku i jedynym autorze zmiany, która wymaga projektowania, i przy szczycie ponowienia. Zmiana obejmuje ostatnie zdanie wiążące (otwiera je „The fix of a slice's findings runs on the class”, ok. linii 5301), w *Verification* „the review of the whole change runs on the orchestrator's class or a stronger one” i „a review or the spec runs on a class cheaper than the orchestrator's”, w *Rationale* zdanie „the reviews of the whole change and of the return step, on the orchestrator's class, are what finds a cheaper model's error”, a w ślad za decyzją `task-cycle/skill/SKILL.md` — krok recenzji całej zmiany („a fresh reviewer that made none of it, on no class cheaper than yours (WAY-229)”, ok. linii 448) i krok 11 („a fresh reviewer on no class cheaper than yours (WAY-229) reviews its range”, ok. linii 488).
2. WAY-10 (P2): *Rationale* mówi cenę, którą Mariusz przyjął — niezależny recenzent zwykle biegnie na modelu autora albo na modelu tej samej rodziny, a skłonność modelu do faworyzowania własnych tekstów, którą mierzy fakt `llm-self-preference`, dotyczy raczej rodziny modeli niż jednego modelu, więc agent, który nie robił zmiany, usuwa wspólny kontekst autora, nie tę skłonność; recenzenta od innego dostawcy proces nie ma. Miejsce: zdanie „a model judging what it wrote favours it, so an agent that did not make the change reads it” (ok. linii 359).
3. WAY-27 i WAY-320 (P4): wyjątek WAY-27 mówi ogólnie, że miejsca, gdzie leży praca the way — zadania i reguły ich miejsca, rejestr problemów, wyniki audytu — nie są źródłem uzasadnienia, a plik, który ich potrzebuje, nazywa każde wpisem pliku lokalizacji, nigdy ścieżką; zdanie „named in the `## Backlog` section of its root `AGENTS.md` and nowhere else” i przykład zgodności idą za tym. WAY-320 dostaje klauzulę, że miejsce, które skrypt the way trzyma dla siebie pod `~/.the-way/` — dziś rejestr przebiegów bramki `~/.the-way/gate_runs` — nie potrzebuje wpisu pliku lokalizacji.
4. WAY-241 i `product-guidelines/testing/template.md` (P9): pole limitu czasu czyta `none`, gdy żaden plik konfiguracji nie trzyma limitu, tak jak pole polecenia — w zdaniu wiążącym „the field of the time limit points to the configuration file that holds it” i w linii szablonu „*Time limit* — a pointer to the configuration file that holds it, never its value (WAY-241)”.
5. WAY-287 (P11): jedno zdanie wiążące mówi, że inna decyzja może dodać rodzaj pozycji do jednej z trzech grup sekcji decyzji człowieka, nazywając grupę — tak jak zrobiły to WAY-308 (oczyszczona linia relacji) i WAY-316 (niepokazany zrzut ekranu); lista WAY-287 zostaje. Zdanie *Rejected* „A search of the log by the words "at the merge", "sees" and "merges" found no second such case” mówi wynik takiego wyszukania na dziś (WAY-308 i WAY-316 dodały po rodzaju pozycji do sekcji), a odrzucony „general item” jest zważony jeszcze raz na tej przesłance.
6. WAY-313 (P13): *Rejected* zamiast „unknown” niesie drogę, którą Mariusz rozważył i odrzucił przy ostatnim zdaniu wpisu: zadanie zmienia decyzję rzutowaną jednym wyborem, jak decyzję fundamentu — z kosztem z tamtego pytania: „definicja i plan dalej mówią starą wersję, inne zadania planu rozjeżdżają się bez sygnału, a nanoszenie zmiany na definicję i plan to większe zadanie” (Mariusz, 2026-11-08, „ale w tym przypadku a będzie ok”). `unknown` zostaje tylko dla zdania głównego, jeśli przy nim żadnej drogi nie ważono.
7. WAY-330 (P17): zdanie ceny „The price taken: until a user has a tool that fills the register, the audit has nothing to count.” mówi cenę, która dziś obowiązuje — użytkownik bez narzędzia, które wypełnia rejestr, nie ma czego liczyć, a szablon rejestru sam go nie wypełnia — bez opisu prywatnego rejestru autora.
8. Niezmiennik `repository-file-location` (P21): zdanie odsyła do mapy części zamiast do listy, której WAY-09 już nie ma — „…lies in `foundations/` or in a directory that the part map gives to a part of the process as its files (WAY-09), …” w miejsce „or in a directory WAY-09 names for a part of the process”.
9. Niezmiennik `elements-no-pending-marker` (P22): WAY-35 dostaje jedno zdanie wiążące, że szablon ani skill elementu nie niosą dopisku, że reguła czeka na decyzję; niezmiennik nazywa się `elements-pending-marker` — w nagłówku w `foundations/invariants.md`, w *Verification* WAY-35 i w komentarzu `elements/common/test_elements_pending_marker.py` (ok. linii 27), który go cytuje.
10. Niezmiennik `generated-overview` (P23): *Part* nazywa też `installation`, która w produkcie generuje pliki dla agenta (punkty wejścia skilli, definicje typów agentów, główny `CLAUDE.md`, oznaczony blok `AGENTS.md`) — „part-map · agent-instructions · installation”.
11. Fakt `openai-model-states` (P27): zdanie mówi trzy stany cyklu życia modelu z dzisiejszej strony deprecjacji OpenAI (https://developers.openai.com/api/docs/deprecations, § Overview: Active, Deprecated, Shutdown), fragmenty to cztery zdania z § Overview, kopia archiwalna to najbliższa istniejąca dla nowego tekstu albo żadna, a klauzula o „legacy” i „no longer accessible” odpada; WAY-85, jedyny wpis, który na fakcie stoi, potrzebuje tylko tego, że modele schodzą z użycia.
12. Fakt `claude-code-imports` (P28): zdanie traci „at launch” (strona https://code.claude.com/docs/en/memory, § Import additional files, mówi dziś „Imported files are expanded and loaded into context alongside the CLAUDE.md that references them.”), fragment jest dzisiejszy, a gdzie wpis zależny potrzebuje chwili ładowania głównego `CLAUDE.md`, *Source* dostaje § Choose where to put CLAUDE.md files; to samo „loads it into context at launch” znika z `instruction-files/tool_loading.md` (punkt „**`@path`** expands the imported file”, ok. linii 42). WAY-129, WAY-132, WAY-141 i niezmiennik `installation-claude-guidance` zostają sprawdzone wobec nowego zdania.
13. WAY-162 i WAY-229 — limit zdań wiążących WAY-05 (G4, #79-6; drobna poprawka 11 pliku danych): żaden akapit wiążący obu wpisów nie ma więcej niż trzy zdania, bo każda część innego pytania dostaje własny akapit, jak WAY-05 pozwala, bez zmiany treści i bez zmiany WAY-05 — w WAY-162 zdanie o poprawce samych uwag Minor (otwiera je „Where the review of the whole change leaves no blocking finding and lists Minor findings”), w WAY-229 ponowienie (otwiera je „An executor that returns `blocked`”) i klasa poprawki z recenzjami (zdanie, które zmienia *To do* 1).
14. WAY-360 i WAY-363 (G4, #109-6): *Rejected* WAY-360 nie mówi już „the same chance in the grade” o produkcie bez reguły rozmiaru, a *Rejected* WAY-363 nie mówi „as today for the form of an entry”, skoro WAY-363 daje dziś każdej uwadze o strukturze kodu w takim produkcie ocenę Minor.
15. WAY-255 (G4, #112-11; drobna poprawka 14): trzy pierwsze cytaty strony prompt-caching w *Based on* zastępują fakty o otoczeniu, tak jak szablon decyzji każe dla zachowania narzędzia, którego proces używa — w tym fakt o domyślnych pięciu minutach życia pamięci podręcznej podagenta, na którym stoi wiążące „five minutes by default”; fakty `claude-code-subagent-cache-ttl` i `claude-code-subagent-cache-ttl-credits` tej wartości nie obejmują.
16. `project-level/plan/skill/cut_tasks.md` (G5, #122-1): pierwszy powód cięcia brzmi jak w WAY-372 — „a part cannot start or finish without something outside the refinement of the task, such as access the agent lacks or another task's result” — w miejsce „outside the task, such as another task's result”.
17. `product-guidelines/styleguide/starting_rules.md` (G5, #126-8): zdanie „the styleguide of a user interface comes into being before that user interface's first screen” mówi, że skill to proponuje, a produkt wiąże tylko decyzja jego dziennika (WAY-173).
18. Powrót zatrzymanego audytu wytycznych (G5, #86-3): pliki doprecyzowania zadania (`project-level/task/skill/`) mówią, że gdy człowiek rozdzielił pracę po tym, jak audyt wytycznych kodu zatrzymał się dla audytu testów, wraca skill zatrzymanego audytu i zamyka listę przyczyn, tak jak dziś mówią tylko `product-guidelines/audit_end.md` (punkt „An audit that stopped, with no audit to follow”) i `product-guidelines/coding/hand_back.md`.
19. Drobne poprawki brzmienia — żadna nie zmienia tego, co wpis wiąże:
    1. `agent-instructions/README.md`: „on `main` as before it (WAY-07)” → „on the main branch” (ten sam plik mówi na początku, że the way nie ma `main`).
    2. WAY-90, *Rejected*: przewinąć linię „new kind of file”, która stoi sama w środku akapitu.
    3. WAY-121: przewinąć „reopens them all; one heading the”; dopisać powód pominiętego limitu lekcji, np. „— WAY-140 already leaves every effect outside the repository to a human, and reading stays with the agent”.
    4. WAY-124: przewinąć linię „are named. A”.
    5. WAY-126: przewinąć „decisions;” stojące samo w linii (dwa miejsca).
    6. WAY-140: przy tym, co „is no effect of the task” (własne katalogi robocze repozytorium poza jego katalogiem), dopisać odsyłacz do WAY-375.
    7. WAY-147, *Verification*: „keeps its cycle record under `docs/task-cycles/forest-on-hex-grid/`” → „names its record directory and its committed copy by `forest-on-hex-grid`” (zapis leży w `.runs/`, kopia jest w `docs/` jeden commit).
    8. WAY-161, *Rationale*: „and where that is outside the repository, only a human makes an effect there (WAY-140)” → „a cycle makes no effect there beyond its own record (WAY-140)” (doprecyzowanie pisze dziś linię zadania w backlogu).
    9. WAY-206: przewinąć krótkie linie.
    10. WAY-216: przewinąć „only the checks the kind”.
    11. WAY-237, *Rationale*: przykłady zgodne z szablonem testów („a duplicate of another test, a test of trivial code …”, `product-guidelines/testing/template.md`).
    12. WAY-243: przewinąć linie zostawione przez #126.
    13. WAY-320: przewinąć dwa miejsca krótkich linii.
    14. WAY-328: przewinąć „in *Scope*, neither is missing, so”.
    15. WAY-339: przewinąć dwa miejsca krótkich linii.
    16. WAY-360: przewinąć „… for the rules on failures and” / „logs.”.
    17. WAY-365: przewinąć linię 189 znaków, która niesie dwa zdania.
    18. WAY-372: przewinąć „… checkable, which a”.
    19. Mapa części, część `product-guidelines`: „…, for the shared reading…” → „…, and for the shared reading…”.
    20. Mapa części, „External context”: „the script of the gate” → „the script that runs the gate for the task cycle” (rejestr trzyma `task-cycle/gate_times.py`).
    21. Fakt `anthropic-model-states`: dwa fragmenty na dzisiejsze brzmienie strony i nowa data odczytu — „… and might be deprecated in the future.”, „… Requests to retired models fail.”.
    22. Fakt `claude-code-project-skills`: fragment o katalogu roboczym gita na dzisiejszy — „In a session running in a linked git worktree that you created with --worktree or git worktree add, Claude Code searches parent directories only up to the worktree root.” — i nowa data odczytu.
    23. WAY-44: klauzula, że pliki w korzeniu repozytorium mapa nazywa po jednym, bo korzeń nie jest katalogiem żadnej części — dziś zdanie „each naming a directory or one kind of file … rather than listing a directory's files one by one” nie obejmuje `/.gitattributes`, `/.gitignore`, `/.python-version` części `repository` ani `/AGENTS.md`, `/CLAUDE.md` części `agent-instructions`.

### Questions to settle

- P1. Na jakiej klasie modelu biegną recenzja całej zmiany i recenzja kroku powrotu?
  - Answer: zawsze na najmocniejszej dostępnej klasie; „najmocniejsza klasa” to Opus, nigdy Fable — zapisane bez nazwy modelu (WAY-229 nazywa klasy ogólnie), np. najmocniejsza klasa rodziny, na której biegnie cykl, bez furtki na Fable. Drożej; Mariusz liczy, że mniej poprawek wyrówna część kosztu, a audyt procesu pokaże koszt wersji po zmianie.
  - Not chosen:
    - (b) zapisać w *Rationale* przyjętą cenę: przy orkiestratorze na tańszej klasie recenzja przepuszcza wadę mniej więcej w połowie przebiegów — jedno zdanie, ale ochrona, na którą liczy uzasadnienie, dalej zależy od modelu sesji orkiestratora
  - Source: Mariusz, 2026-11-14, przegląd fundamentu, decyzja pod P1 w pliku danych
- P1a. Jak WAY-229 mówi „najmocniejsza klasa” tak, żeby nie objęła Fable, i czy to samo znaczenie obowiązuje tam, gdzie WAY-229 już mówi „the strongest class available” — przy kawałku i jedynym autorze zmiany wymagającej projektowania oraz przy szczycie ponowienia?
  - Answer: WAY-229 mówi „the strongest class available” w jednym znaczeniu dla recenzji, projektowania i szczytu ponowienia, bez nazwy modelu. Fable odcina nie tekst the way, tylko ustawienie sesji cyklu: sesje cykli startują z listą dozwolonych modeli bez Fable (`availableModels` podane flagą `--settings` przy starcie), a zwykłe sesje Mariusza mają Fable. Cykl uruchomiony bez tej listy bierze najmocniejszą klasę, jaką ma, także na recenzję.
  - Not chosen:
    - granica w tekście WAY-229 nazwana ogólnie — bez kryterium, które odróżnia klasy bez nazw modeli, agent odczyta ogólnik dowolnie
    - przykładowe brzmienie „najmocniejsza klasa rodziny, na której biegnie cykl” — Fable należy do tej samej rodziny co Opus, więc recenzje i kawałki projektowe trafiałyby na Fable
    - recenzja o klasę wyżej od sesji prowadzącej, najwyżej Opus — przy sesji na Haiku recenzja szłaby na Sonnecie, który w pomiarze WAY-229 przepuścił wadę w 4 z 8 przebiegów, a granicę na Fable i tak trzeba gdzieś postawić
    - lista bez Fable w ustawieniach całego konta — Fable znika ze wszystkich sesji Mariusza, a każda praca na Fable wymaga zmiany ustawień: „a co kiedy będę chciał faktycznie coś zrobić na fable?”
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „tylko w cyklach sesji, ale to by trzeba było ustawić i u doradcy w skillu i w ustawieniach herdr z których sam startuję cykle”
- P2. Co z tym, że niezależny recenzent zwykle biegnie na modelu autora?
  - Answer: zapisać cenę w *Rationale* WAY-10. Skłonność dotyczy raczej rodziny modeli niż jednego modelu, więc i inny model tej samej rodziny może ją mieć; innych dostawców Mariusz dziś nie ma, więc tak zostaje.
  - Not chosen:
    - (b) recenzent na innym modelu niż autor (zdanie wiążące WAY-10 albo WAY-229 i krok wyboru modelu) — przy autorze na najmocniejszym modelu recenzent byłby słabszy albo z innego dostawcy
  - Source: Mariusz, 2026-11-14, przegląd fundamentu, decyzja pod P2 w pliku danych
- P4. Jak poszerzyć wyjątek WAY-27 i czy rejestr bramki pod `~/.the-way/` jest miejscem pracy the way, czy własnym plikiem the way jak sam plik lokalizacji?
  - Answer (wyjątek WAY-27): reguła ogólna zamiast listy — miejsca, gdzie leży praca the way (zadania i reguły ich miejsca, rejestr problemów, wyniki audytu), nie są źródłem uzasadnienia, a plik, który ich potrzebuje, nazywa każde wpisem pliku lokalizacji, nigdy ścieżką; „and nowhere else” znika.
  - Not chosen:
    - (b) zamknięta lista miejsc z plikiem, który może każde nazwać — każde nowe miejsce wymaga zmiany WAY-27, a zapomniana zmiana daje ten sam rozjazd co dziś
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „1 a”
  - Answer (rejestr bramki): własny plik the way, jak sam plik lokalizacji — WAY-320 dostaje klauzulę, że miejsce, które skrypt the way trzyma dla siebie pod `~/.the-way/`, nie potrzebuje wpisu.
  - Not chosen:
    - (b) rejestr bramki jako wpis pliku lokalizacji — zmiana `task-cycle/gate_times.py`, jego testów i WAY-350, a skrypt bramki, który nie może zapytać człowieka, i tak potrzebuje ścieżki domyślnej przy braku wpisu
    - jeden plik z danymi wszystkich przebiegów zamiast katalogu — równoległe bramki pisałyby do jednego pliku i potrzebowałyby blokady zapisu, której układ „jeden plik na przebieg” unika
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „2 a ale nie wiem czy nie lepiej takie rzeczy po prostu do jednego zbiorczego pliku walnąć z tymi lokalizacjami?”, po rachunku: „ok”
- P11. Dopisać oba rodzaje pozycji do listy wiążącej WAY-287 czy powiedzieć raz, że inna decyzja może dodać rodzaj do grupy?
  - Answer: (b) jedno zdanie wiążące WAY-287 mówi, że inna decyzja może dodać rodzaj pozycji do jednej z trzech grup sekcji, nazywając grupę; lista WAY-287 zostaje jako podstawa, a pełny spis rodzajów trzyma szablon opisu prośby. Każdy nowy rodzaj nadal wymaga własnej decyzji, więc to nie jest odrzucona „general item”.
  - Not chosen:
    - (a) dopisać do listy wiążącej oczyszczoną linię relacji (WAY-308) i niepokazany zrzut (WAY-316) — dwa wyliczenia w długim zdaniu, a następna decyzja, która doda rodzaj, znów musi zmienić WAY-287, i zapomniana zmiana daje ten sam rozjazd
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „b”
- P22. Dopisać do WAY-35 zdanie wiążące o dopisku, że reguła czeka, czy zostawić; i czy zmienić nazwę na `elements-pending-marker`?
  - Answer: (1a) WAY-35 dostaje jedno zdanie wiążące, że szablon ani skill elementu nie niosą dopisku, że reguła czeka na decyzję; (2a) niezmiennik nazywa się `elements-pending-marker`. Wywiedzenie niezmiennika z WAY-35, wybrane przy #121 („1 a, 2 a, 3 a”, Mariusz przez doradcę dnia, 2026-11-13), zostaje.
  - Not chosen:
    - (1b) zostawić WAY-35 bez takiego zdania — powód strażnika żyje tylko w opisie prośby #121, a kto idzie od niezmiennika do WAY-35, nie znajduje uzasadnienia
    - (2b) zostawić nazwę — następny autor niezmiennika, który weźmie ten za wzór, nazwie swój wbrew szablonowi niezmienników („The identifier names what the sentence constrains, never what it demands”)
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „tak jak rekomendujesz” (rekomendacja: 1 a, 2 a)
- P23. *Part* niezmiennika `generated-overview` z trzema częściami czy zdanie, że mówi tylko o plikach repozytorium the way?
  - Answer: (a) *Part* „part-map · agent-instructions · installation” — powód WAY-52 („repository overviews have not helped”) dotyczy agenta w produkcie tak samo jak w the way.
  - Not chosen:
    - (b) zdanie, że niezmiennik mówi tylko o plikach repozytorium the way — instalator mógłby wpisać produktom przegląd katalogów i nic by tego nie zatrzymało
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „a”
- G4, #79-6. Jak WAY-162 (cztery zdania wiążące w jednym akapicie) i WAY-229 (pięć) mają się do limitu WAY-05?
  - Answer: (c) rozdzielić na akapity tak, jak WAY-05 już pozwala — osobny akapit na każdą część innego pytania; WAY-05 bez zmian.
  - Not chosen:
    - (a) połączyć zdania średnikiem do trzech — formalnie spełnia limit, ale zdanie z trzema średnikami jest tak samo długie i trudniejsze w czytaniu
    - (b) rozluźnić limit WAY-05 — dla dwóch wpisów na blisko dwieście, a WAY-05 w *Rejected* odrzuca już „a higher fixed limit — a number with no ground”
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „c”
- G5, #98-1. Czy pierwszy plik nowego rodzaju kodu w the way musi mieć wytyczne rodzaju z wierszem indeksu (WAY-216), skoro the way nie ma indeksu wytycznych kodu?
  - Answer: rozstrzyga i niesie zadanie „the way: wytyczne kodu i testów samego the way (koniec stanu przejściowego WAY-328)” — po jego scaleniu the way ma indeks rodzajów kodu, WAY-328 zostaje wycofana i WAY-216 obowiązuje the way jak każdy produkt; do scalenia odstępstwo WAY-328 obejmuje też wytyczne rodzaju. To zadanie nie zmienia w tej sprawie nic.
  - Source: dokument zadania „the way: wytyczne kodu i testów samego the way …”, *Questions to settle*, pytanie „G5, #98-1”, stan z 2026-11-15 — odpowiedź doradcy dnia w imieniu Mariusza, 2026-11-15: „1 a — to zadanie i tak usuwa przyczynę pytania; odesłanie w Z1 (…) dopisz tylko w tym dokumencie.”
- Drobne poprawki, pozycja 28 (opcjonalna). Czy WAY-44 dostaje klauzulę o plikach w korzeniu?
  - Answer: (a) tak — pliki w korzeniu repozytorium mapa nazywa po jednym, bo korzeń nie jest katalogiem żadnej części.
  - Not chosen:
    - (b) zostawić — rozjazd bez skutków, ale czytelnik WAY-44 czytający ściśle widzi mapę wbrew decyzji
  - Source: Mariusz, 2026-11-15, w rozmowie doprecyzowania — „a”

## Context

- Plik danych przeglądu: a note in the author's vault — sekcja „Fundament” → „Propozycje” (P1, P2, P4, P9, P11, P13, P17, P21, P22, P23, P27, P28), „Grupy uwag” (G4, G5) i „Drobne poprawki brzmienia”; numery pozycji drobnych poprawek w *To do* 19 różnią się od numerów w pliku danych, bo pozycje 11 i 14 pliku danych stoją w *To do* 13 i 15.
- Sprawdzony commit przeglądu: `21ecb627f885de438e2209d7ff5c137b1e1b9d83` (gałąź `foundations`); numery linii w pliku danych i podpowiedzi linii w tym dokumencie odnoszą się do niego.
- Pozycje drobnych poprawek 15, 16 i 23 pliku danych idą z innymi zadaniami: 15 z notatką do zadania „przegląd fundamentu, którego nie da się pominąć” (P12), 16 z zadaniem „the way: cykl zadania po przeglądzie fundamentu …” (P18), 23 z zadaniem „the way: mapa części …” (P6).
- Poprawka WAY-121 (*To do* 19.3) dotyka *Rationale*, które zmienia też zadanie „Uzupełnić w decyzjach the way źródła i to, czego nie biorą z przejętych praktyk”; cykl, który scali się drugi, uzgadnia tekst z pierwszym.
- P11 zmienia sekcję decyzji człowieka w opisie prośby, którą zmienia też zadanie „the way: cykl zadania po przeglądzie fundamentu …” (G2) — kolejność cykli do ustalenia.
- Droga niewybrana dla WAY-313 (*To do* 6) stoi w zamrożonym dokumencie zadania cyklu #90, commit `07cbcf8`, `docs/task-cycles/decisions-as-material-at-refinement/task.md`, pytanie 5.
- Pomiar recenzentów dla P2 (z sekcji *Cost* opisów 49 próśb #77 i #79–#126): w 30 cyklach recenzent całej zmiany biegł na tym samym modelu co autor, w 17 na innym, w 2 mieszanie; wszystkie warianty są zgodne ze zdaniami wiążącymi, bo WAY-10 wymaga innego agenta, nie innego modelu.
- Mariusz przyjął cały dokument 2026-11-15 („akceptuję z poprawką w context”). Obie czynności z *Human actions* zrobione: sesje startowane przez doradcę dnia i akcja „Implement task” panelu herdr dostają plik ustawień `the settings file of the day advisor's sessions` z `availableModels` opus, sonnet, haiku; sesja z `--model fable` biegnie na Opusie, podagent proszony o Fable — na modelu sesji.
- `Defect introduced by`: prośby, które scaliły tekst sprzeczny z wiążącym tekstem obowiązującym przy scaleniu — #48 i #79 (WAY-229 i WAY-162 ponad limit zdań WAY-05), #90 (`unknown` w *Rejected* WAY-313 wbrew szablonowi decyzji), #100 i #106 (miejsca poza wyjątkiem WAY-27, który #102 przepisał wcześniej tego samego dnia), #109 (nieaktualny powód w *Rejected* WAY-360 i WAY-363), #121 (nazwa niezmiennika wbrew szablonowi niezmienników), #122 (`cut_tasks.md` luźniej niż WAY-372), #126 (`starting_rules.md` mocniej niż WAY-173; niezmiennik `repository-file-location` po przepisaniu WAY-09). Pozostałe pozycje to nowa potrzeba, zmiana zdania Mariusza, zmiana źródła zewnętrznego albo luka.

## Questions carried to cycle

none

## Human actions

- Polecenie, którym skill doradcy dnia uruchamia sesję cyklu, dostaje listę dozwolonych modeli bez Fable (flaga `--settings` z `availableModels`), i jeden przebieg potwierdza, że podagent cyklu nie dostaje Fable — before the cycle, done
- Ustawienia herdr, z których Mariusz sam startuje cykle, dostają tę samą listę — before the cycle, done

## Decisions in play

Brzmienie zdań wiążących przy `21ecb62`; cykl czyta każdą decyzję w całości w `foundations/decisions.md` pod nagłówkiem `### WAY-NN`, z *Rationale* i *Rejected*.

**Decyzje, które zadanie zmienia wyborem Mariusza (WAY-314), ze zmianą:**

- WAY-229 — On which class of model do the executor of a slice and the one author work?
  > The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class. An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class that fails, or a retry that fails, stops the cycle. The fix of a slice's findings runs on the class of the executor whose work stands, of findings in several slices on the highest of their classes and of a planned change's finding of no slice on the orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every reviewer — the review of the whole change and the review of the return step included — work on no class cheaper than the orchestrator's.
  - Zmiana (P1, P1a): recenzja całej zmiany i recenzja kroku powrotu — zawsze na najmocniejszej dostępnej klasie, w jednym znaczeniu „the strongest class available” w całym wpisie (*To do* 1); (G4) akapity po części innego pytania (*To do* 13).
- WAY-27 — Where may this repository point for its reasoning?
  > Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the place of its tasks and the rules of that place, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else, each by an entry of the locations file of WAY-320 and never by a path.
  - Zmiana (P4): wyjątek ogólny dla miejsc, gdzie leży praca the way, bez „and nowhere else” (*To do* 3).
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?
  > A user's places on their own disk that lie outside every repository, such as the place of a product's tasks and the place of its projects, are kept in one file, `~/.the-way/locations.json`, found at that place for every user and through no environment variable: a JSON object whose keys are repository names, each holding entries by name, such as `tasks`, `projects` and `task-rules`, whose values are paths on the user's disk. No file the repository tracks holds an absolute path, or a note link in a Markdown file, other than the files that the invariant `tracked-file-private-paths` names, which write example paths in order to find or to test them; a file that points to such a place names its entry in the locations file. The copy of a task cycle's record and the description of a request are checked for a note link in every file, as WAY-309 gives.
  - Zmiana (P4): klauzula o miejscu, które skrypt the way trzyma dla siebie pod `~/.the-way/` (*To do* 3).
- WAY-287 — What does a request put before the human for a decision?
  > The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — the cycle's choices beyond the task's content, the steps skipped and the checks not run, the incomplete reading of the review of the whole change where its reviewer did not run through the rest of its selection by title or itself named a decision concerning the change as unread, and the gap was not closed on the way by that reviewer, or a fresh one, reading what stayed unread, the unfixed findings the product's user or the human working with the process will feel, the decisions of the task's own sections, in a blocked request what the cycle needs to go on, the human actions, the changed invariant tests, surfaces and *Violated* marks, the additions a change makes to a product's logging scope, a listing of the remarks check that the cycle holds wrong (WAY-295), an error of the form check that the cycle holds wrong, the pairs that give the cause of a correction after the request opened, each descriptive `TODO` in an invariant's *Rests on* or *Derives from* or in a decision's *Based on* that stands on the main branch after the change (WAY-71), and the foundation entries the human did not see at the task document — in three groups, headed *Needed from you*, *Fix or let through* and *You accept by merging*, in this order: what the request cannot go on without, an answer or an action of the human; what the cycle did not do or did not fix and can still be done in this request, which the human has done there, makes a task of or lets through; and what the cycle did within its authority, which the human accepts by merging and which waits for no separate answer. Every group stands, reading `none` where it holds no item, the items are numbered in one run through the three groups, and the section reads `none` alone where no group holds an item, which says that nothing else in the request waits for the human's yes. A blocked request keeps the same skeleton, with `blocked` in its first sentence and what the cycle needs, in plain words, and the stages it did not run because it stopped, under *Needed from you*, while each remaining finding stands with its place in the code in the lower part.
  - Zmiana (P11): zdanie, że inna decyzja może dodać rodzaj pozycji do grupy; *Rejected* na dzisiejszy wynik wyszukania (*To do* 5).
- WAY-35 — What does an element's skill hold?
  > An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them; the way of working the skills share stands once in that part, and a skill reads the rules and that way of working from there instead of restating them.
  - Zmiana (P22): zdanie, że szablon ani skill elementu nie niosą dopisku, że reguła czeka; *Verification* z nową nazwą niezmiennika (*To do* 9).
- WAY-241 — What does the recipe of a test level hold?
  > The template of the testing discipline gives a product's testing guidelines, for each level, a recipe of the same fields — what the level is for and when not to use it, where its files lie and how they are named, the name and build of a test, its doubles, its data, time and randomness, the level's exemplar test, the command and the time limit — each field that binds naming the product's decision that carries it, a field naming none standing as an example, and a field that repeats another level's reading "as in <level>". The field of the command names the gate and how it narrows to the level, a file or a test, where the gate can, and otherwise reads `none`; the field of the time limit points to the configuration file that holds it; and no recipe lists commands of the test tool of its own.
  - Zmiana (P9): pole limitu czasu czyta `none`, gdy żaden plik konfiguracji nie trzyma limitu (*To do* 4).
- WAY-44 — What assigns a file to a part?
  > Every file git tracks belongs to exactly one part of the map, by path patterns that git itself matches, each naming a directory or one kind of file — every invariant test, say — rather than listing a directory's files one by one; a file that no pattern matches, and a file that two parts claim, is an error of the check of the foundation, unless the map lists that file as left out on purpose, and so is a pattern of a part's *Files* or *Trust boundary* that matches no file git tracks. Tests belong to the part they test and generated files to the part of their generator; the files that serve the whole repository — the lockfile and the build configuration — are a part of their own; the files that serve the tests of several parts are another, which its sentence describes as such with no field of its own, and which the tests of every part may import while code that is no test may not; and the files that only direct whoever carries out its tasks — instructions for agents, skills, hooks and the configuration of agents' tools and of CI — are another. For a file that collects entries about many parts, the parts a change touches follow from the entries it adds or changes, not from the part the file itself belongs to.
  - Zmiana (pozycja 28): klauzula o plikach w korzeniu repozytorium (*To do* 19.23).
- WAY-162 — How does a code review of a task's change end when its findings block?
  > In every code review of a task's cycle — of a slice of its plan, of the whole change, of the return step's commits, of the reconciliation with the target branch and of a change made for the human's remarks on the request — the findings that block, as WAY-161 grades them, get one fix and one review of that fix, and a new Critical or Important finding in the fix itself counts as one that remains. Where a blocking finding remains after that review of the fix, no third round runs, the orchestrator does not rule on it, no further slice is made, and the cycle opens a draft request marked `blocked` that lists each remaining blocking finding with its place in the code and its reason, what the fix tried, and the time, models and tokens the cycle has used so far, from its record of stages, with the number of review rounds. Where the review of the whole change leaves no blocking finding and lists Minor findings that WAY-161 has the cycle fix, one fix takes them in and one review of that fix follows, and where that review finds a new Critical or Important finding in the fix, the cycle reverts the fix's commits with a commit of its own, so that they stay in history, runs no third round and opens the request, not blocked, on the code the review of the whole change accepted, the request listing the Minor findings the fix tried and the new finding with its grade and as the review of the fix found it. In the code reviews after the review of the whole change, and for a Minor finding that remains after a fix, the findings that do not block go unfixed to the request's lists as WAY-161 gives them.
  - Zmiana (G4): ta sama treść w akapitach po części innego pytania (*To do* 13).

**Decyzje, z którymi zadanie zestawia tekst, bez ich zmiany:**

- WAY-05 — How is a decision entry written?
  > A decision entry opens with one to three binding sentences that answer its question — in the present tense, describing a state that is to be true, concrete enough to check — and one paragraph of one to three binding sentences for each part of another question that it answers, followed by fields a script or an agent reads, then rationale and rejected options in prose, which, where the entry's author writes it rather than quotes a source, names no file, script or count — a count being how many files, tests or entries of its foundation the product holds; a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound — nor what the process's own tools do or lack today, and does not tell how the decision was reached. A field stays in the template only while someone or something reads it, and what a decision forces on later work stands in a binding sentence or a field, never in prose. An example in `elements/decisions/` names a decision of the log by its number instead of copying it.
- WAY-09 — What may enter the process repository?
  > On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository`, which the part map of the-way names with its files, the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files, the project skill entry points under `.claude/skills/` and `.agents/skills/` and the copies of the cycle's agent type definitions under `.claude/agents/`, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: an element its template and rules, examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its entries; any other directory what the sentence of its part in the part map names. The entries in `foundations/` are checked by `elements/common/foundation_check.py`.
  - Do niej odsyła poprawiony niezmiennik `repository-file-location` (*To do* 8).
- WAY-52 — What is generated from the part map for an agent?
  > Nothing is generated from the part map for an agent: an agent reads the entries of the parts its change touches, and no overview of the repository is generated for it.
  - Z niej wywodzi się niezmiennik `generated-overview` (*To do* 10).
- WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?
  > The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason. A decision of the-way on what such a template carries or what such a skill proposes binds the template and the skill, never a product's screens or code directly.
  - Z nią zgadza się poprawione zdanie `product-guidelines/styleguide/starting_rules.md` (*To do* 17).
- WAY-372 — When is a task split into several tasks?
  > A split of a task is proposed only where it makes the work better or cheaper; time does not count, so that a part is ready sooner is no reason. Whoever proposes a split names its reason, and the reasons are three: a part cannot start or finish without something outside the refinement of the task, such as access the agent lacks or another task's result; the parts change different repositories (WAY-140); or a later step of the refinement offers a separate task. A task's size alone is no reason: for it an agent says nothing of a split — no mention, no question, no recommendation — and a split the human asks for, who sees the whole document, stands without one.
  >
  > A project plan cuts its tasks by WAY-143 and by these reasons, never by a task's size alone.
  - Z nią zgadza się poprawiony pierwszy powód cięcia w `project-level/plan/skill/cut_tasks.md` (*To do* 16).

**Decyzje, w których zadanie zmienia tylko *Rationale*, *Rejected*, *Based on*, *Verification* albo łamanie linii, bez zmiany zdań wiążących:** WAY-10 (*To do* 2), WAY-90, WAY-121, WAY-124, WAY-126, WAY-140, WAY-147, WAY-161, WAY-206, WAY-216, WAY-237, WAY-243, WAY-255 (*To do* 15), WAY-313 (*To do* 6), WAY-328, WAY-330 (*To do* 7), WAY-339, WAY-360 i WAY-363 (*To do* 14), WAY-365, WAY-372 (pozycje *To do* 19).

**Wpisy, które cykl sprawdza wobec zmienionych wpisów, bez zmiany:** WAY-85 (fakty `openai-model-states` i `anthropic-model-states`), WAY-127 (fakt `claude-code-project-skills`), WAY-129, WAY-132, WAY-141 i niezmiennik `installation-claude-guidance` (fakt `claude-code-imports`), WAY-308 i WAY-316 (rodzaje pozycji, które nowe zdanie WAY-287 obejmuje), WAY-350 (rejestr bramki zostaje poza plikiem lokalizacji).

**Niezmienniki, które zadanie zmienia** (`foundations/invariants.md`):

- `repository-file-location` — „Where {merge-onto} exists, every file git tracks lies in `foundations/` or in a directory WAY-09 names for a part of the process, belongs to the `repository` or the `agent-instructions` part of the part map, or is the `README.md` at the root.” (*To do* 8)
- `elements-no-pending-marker` — „No file git tracks under `elements/` holds the text "decision pending", every run of spaces and line breaks counting as one space.” — *Derives from:* WAY-35 (*To do* 9)
- `generated-overview` — „No file generated for an agent holds an overview of the repository's directories.” — *Part:* part-map · agent-instructions (*To do* 10)

**Fakty o otoczeniu, które zadanie zmienia** (`foundations/environment_facts.md`): `openai-model-states` (*To do* 11), `claude-code-imports` (*To do* 12), `anthropic-model-states` i `claude-code-project-skills` (*To do* 19.21–22), oraz nowe fakty dla WAY-255 (*To do* 15).

## Settlements to record

Candidates: 13 shown, 11 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Recenzja całej zmiany i recenzja kroku powrotu biegną zawsze na najmocniejszej dostępnej klasie, a „the strongest class available” znaczy w WAY-229 jedno; model, którego cykle nie mają brać, odcina ustawienie sesji cyklu, nie tekst the way. | sentence of WAY-229 | *Questions to settle*, P1 i P1a | recenzent na klasie orkiestratora, jak dziś; albo nazwa modelu w tekście, albo dwa znaczenia „strongest” w jednym wpisie |
| 2 | Agent, który nie robił zmiany, zwykle biegnie na modelu autora albo jego rodziny, więc usuwa wspólny kontekst autora, nie skłonność modelu do własnych tekstów — tę cenę WAY-10 przyjmuje. | sentence of WAY-10 | *Questions to settle*, P2 | uzasadnienie dalej twierdzi, że inny agent usuwa faworyzowanie; albo wymóg recenzenta na innym modelu |
| 3 | Miejsca, gdzie leży praca the way — zadania i reguły ich miejsca, rejestr problemów, wyniki audytu — nie są źródłem uzasadnienia, a plik, który ich potrzebuje, nazywa każde wpisem pliku lokalizacji, nigdy ścieżką. | sentence of WAY-27 | *Questions to settle*, P4, odpowiedź o wyjątku | zamknięta lista miejsc z plikami, które mogą je nazwać, albo „and nowhere else” zostawione |
| 4 | Miejsce, które skrypt the way trzyma dla siebie pod `~/.the-way/`, nie potrzebuje wpisu pliku lokalizacji. | sentence of WAY-320 | *Questions to settle*, P4, odpowiedź o rejestrze bramki | rejestr bramki przeniesiony na wpis pliku lokalizacji, ze zmianą `task-cycle/gate_times.py` i WAY-350 |
| 5 | Inna decyzja może dodać rodzaj pozycji do jednej z trzech grup sekcji decyzji człowieka w opisie prośby, nazywając grupę. | sentence of WAY-287 | *Questions to settle*, P11 | oba rodzaje dopisane do listy wiążącej, a następna decyzja znów bez zmiany WAY-287 |
| 6 | Szablon ani skill elementu nie niosą dopisku, że reguła czeka na decyzję. | sentence of WAY-35 | *Questions to settle*, P22 (1a) | WAY-35 bez zdania, a powód testu strażnika tylko w opisie prośby #121 |
| 7 | Niezmiennik o dopisku „decision pending” nazywa się `elements-pending-marker`. | invariant | *Questions to settle*, P22 (2a) | nazwa `elements-no-pending-marker` zostawiona wbrew szablonowi niezmienników |
| 8 | Niezmiennik `generated-overview` obejmuje też pliki dla agenta, które instalator pisze w produkcie. | invariant | *Questions to settle*, P23 | zdanie, że niezmiennik mówi tylko o plikach the way |
| 9 | Pliki w korzeniu repozytorium mapa części nazywa po jednym, bo korzeń nie jest katalogiem żadnej części. | sentence of WAY-44 | *Questions to settle*, pozycja 28 | WAY-44 zostawiona bez klauzuli |
| 10 | Cena WAY-330 to dzisiejsza cena: użytkownik bez narzędzia, które wypełnia rejestr problemów, nie ma czego liczyć, a szablon rejestru sam go nie wypełnia — bez opisu prywatnego rejestru autora. | sentence of WAY-330 | Mariusz, 2026-11-14, przegląd fundamentu, decyzja pod P17: „droga (a) — przepisać cenę na dzisiejszą, bez opisu prywatnego rejestru autora”; droga niewybrana: (b) zostawić zdanie, bo warunkowe jest dalej prawdziwe dla każdego nowego użytkownika — czytelnik wpisu bierze audyt za narzędzie, które dziś nie ma czego liczyć | zdanie zostawione albo przepisane z opisem rejestru autora |
| 11 | Pole limitu czasu w przepisie poziomu testów czyta `none`, gdy żaden plik konfiguracji nie trzyma limitu. | sentence of WAY-241 | *To do* 4; Mariusz, 2026-11-14, przegląd fundamentu, decyzja pod P9: „do zadania Z1” | brzmienie braku pliku wymyślane w każdym produkcie, jak trzy akapity prozy w wytycznych loop2 |

## Out of scope

- P5 (fakt o widoczności loop2) i P8 (WAY-213, długość wytycznych produktu) — Mariusz zostawił bez zmian (2026-11-14).
- Sprawy przeglądu, które niosą inne zadania: cykl zadania (P10, P18–P20, G2, WAY-375), skrypty (P16, G1, G3), mapa części (P6, P26), wytyczne kodu i testów the way (WAY-328, G5 #98-1).
