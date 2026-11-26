---
title: "the way: poprawki przyczyn z przeglądu warstwy AI 26.11 — model przeglądu w cyklu startowanym na słabszym modelu i lista testów „spodziewanie czerwonych” między kawałkami"
status: draft
created: 2026-11-26T13:27
updated: 2026-11-26
tags: [zadanie]
related: "the project's note in the author's notes"
---

# the way: poprawki przyczyn z przeglądu warstwy AI 26.11 — model przeglądu w cyklu startowanym na słabszym modelu i lista testów „spodziewanie czerwonych” między kawałkami

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Przegląd całej zmiany i przegląd kroku powrotu w cyklu the way mają iść na najmocniejszym modelu, na jaki pozwalają ustawienia sesji (WAY-229).
- Gdy sesję cyklu uruchomiono z listą dozwolonych modeli podaną przy starcie (`--settings <plik>`), prowadzący cykl tej listy nie widzi, uznaje, że wolno wszystko, prosi o model wyłączony, a Claude Code bez błędu daje podagentowi model sesji — przegląd idzie na słabszym modelu, a zapis cyklu podpisuje go nazwą z prośby.
- Odczuwa to Mariusz: dostaje PR po przeglądzie słabszym, niż zakłada proces, i dowiaduje się o tym tylko wtedy, gdy sam zauważy.
- Wykonawca kolejnego kawałka planu dostaje listę testów, które „mają prawo” padać na jego bazie; listę układa planista bez uruchamiania testów, a prowadzący ma ją przebudować dla każdego kawałka.
- Gdy lista nie odpowiada gałęzi, wykonawcy tracą kroki na wyjaśnianie rozjazdu, a za listą może się schować prawdziwy błąd kawałka, który wyjdzie dopiero w pełnych testach na końcu cyklu.

### To do

1. W każdym cyklu, przed pierwszym zleceniem najmocniejszej klasy, prowadzący ustala próbnym wywołaniem model, który sesja naprawdę daje: zleca małemu agentowi pracę na modelu-kandydacie i z zapisu sesji (`task-cycle/cycle_stages.py`) odczytuje, na którym modelu ten agent faktycznie pracował. Pierwszym kandydatem jest model podany przy starcie cyklu, a bez niego najmocniejszy model, jaki oferuje narzędzie uruchamiania agentów; gdy agent dostał zastępstwo, prowadzący próbuje następnego modelu w dół. Wszystkie zlecenia najmocniejszej klasy w cyklu idą na ustalony model, a zapis cyklu podaje próby i ich wynik.
2. Zapis cyklu podaje przy każdym agencie model, na którym ten faktycznie pracował, odczytany z zapisu sesji (`task-cycle/cycle_stages.py`), a nie nazwę modelu, o który prowadzący prosił; gdzie te dwa się różnią, wiersz podaje oba.
3. Wykonawca kawałka rozstrzyga, czy padający test jest błędem jego kawałka, pomiarem na bazie kawałka: test, który pada także na bazie (przed zmianą kawałka), nie jest błędem kawałka, poza testem z *Checks* kawałka-właściciela (punkt 5); test, który na bazie przechodzi, a po zmianie pada, jest błędem kawałka, chyba że *Goal* tego samego kawałka zapowiada, że kawałek zostawia go czerwonym, i wskazuje kawałek, który go naprawi. Wykonawca uruchamia na bazie tylko testy, które mu padły, i jego raport podaje przy każdym z nich wynik na bazie.
4. Zlecenie kawałka nie niesie już listy testów, które plan zostawia czerwone na jego bazie, a prowadzący przestaje ją układać; ten sam pomiar na bazie zastępuje porównanie z tą listą w sprawdzeniu raportu wykonawcy i w regule ponowienia kawałka na mocniejszym modelu. Zostaje reguła, że test padający bez kawałka-właściciela dostaje właściciela edycją planu przed zleceniem następnego kawałka.
5. Plan, zapowiadając w *Goal* kawałka test, który ten kawałek zostawia czerwony, wpisuje ten sam test do *Checks* kawałka, który ma go naprawić; test z *Checks* kawałka-właściciela, który po jego zmianie dalej pada, jest nieudanym sprawdzeniem tego kawałka, choć padał też na jego bazie.

### Questions to settle

- Skąd prowadzący cyklu bierze najmocniejszy dozwolony model, gdy nie widzi listy dozwolonych modeli?
  - Answer: próbnym wywołaniem w każdym cyklu, przed pierwszym zleceniem najmocniejszej klasy; model podany przy starcie cyklu jest pierwszym kandydatem próby, nie przyjmowanym na wiarę; przy zastępstwie prowadzący próbuje następnego modelu w dół, a ustalony model obowiązuje dla wszystkich zleceń najmocniejszej klasy w cyklu.
  - Not chosen:
    - próbne wywołanie tylko wtedy, gdy przy starcie nikt modelu nie podał, a model podany przyjmowany na wiarę — rzadko ćwiczona ścieżka psuje się niezauważona i nie łapie modelu podanego przy starcie, który przestał być dozwolony (powód Mariusza)
    - prośba o model sesji, który na pewno jest dostępny — nie osiąga celu WAY-229: cykl startowany na Sonnecie dostaje przegląd na Sonnecie, a w pomiarze WAY-229 przegląd tańszej klasy przepuścił wadliwą zmianę w 4 z 8 prób
    - prośba o najmocniejszy model i zapis faktycznego modelu bez próby — nie osiąga celu WAY-229: przegląd dalej bywa słabszy, tylko jawnie, a o powtórce decyduje człowiek przy PR
    - cykl bez modelu podanego przy starcie zatrzymuje się i prosi o model — każde ręczne uruchomienie cyklu bez listy w ustawieniach zatrzymałoby się tak samo, bo prowadzący nie odróżni listy nieobecnej od niewidocznej; tura człowieka przy każdym takim starcie
    - `CLAUDE_CODE_SUBAGENT_MODEL=opus` w ustawieniach sesji cyklu — przeniosłoby na Opusa każdego podagenta wołanego bez nazwy modelu (w cyklach na Sonnecie od 15.11 było ich 57, ok. 1 mld tokenów), bo definicje w `task-cycle/agent-types/` nie mają pola `model`; wykonawcy klasy „same” chodziliby na Opusie, a zapis cyklu podawałby klasę sesji (notatka zadania, 2026-11-26)
    - sprawdzanie modelu po przeglądzie i ponowny przegląd — leczy skutek i dokłada prowadzącemu kroki; Mariusz: „trzeba rozwiązać przyczynę, nie skutek” (notatka zadania, 2026-11-26)
  - Source: Mariusz przez doradcę dnia (mandat 14:13), 2026-11-26: „pytanie 1 — a, ze zmianą: próbne wywołanie biegnie w każdym cyklu, nie tylko gdy przy starcie nikt modelu nie podał. Model podany przy starcie jest wtedy pierwszym kandydatem próby, nie przyjmowanym na wiarę. Powód: usuwa słaby punkt, który sam wskazałeś (rzadko ćwiczona ścieżka psuje się niezauważona) — jedna ścieżka w każdym cyklu, a koszt kilkudziesięciu tysięcy tokenów jest pomijalny wobec setek milionów cyklu. Próba łapie też przypadek, gdy model podany przy starcie przestał być dozwolony.”
- Po czym wykonawca kawałka poznaje, że padający test nie jest błędem jego kawałka, i co zostaje z listy testów, którą dziś układa planista?
  - Answer: pomiar na bazie kawałka zamiast listy: test padający także na bazie nie jest błędem kawałka; test, który na bazie przechodzi, a po zmianie pada, jest błędem kawałka, chyba że *Goal* tego samego kawałka zapowiada go jako zostawiony czerwony, jak pozwala WAY-136; lista w zleceniach znika.
  - Not chosen:
    - jak wyżej, ale z listą z planu w zleceniach jako podpowiedzią — prowadzący dalej układa listę, czyli ogniwo, które zawiodło; lista może kłamać, a wykonawca, który zobaczy na niej swój test, może go nie uruchomić na bazie
    - samo kryterium bazy, bez wyjątku zapowiedzi w *Goal* — kawałek, który z planu ma zostawić test czerwony, dostaje powtórkę na mocniejszym modelu, a planista musi sklejać kawałki, których nie da się zrobić osobno; cofa uzasadnienie WAY-136
    - zostawienie reguły z dopisanym zdaniem „buduj listę od nowa dla każdego kawałka, nie kopiuj jej” — znowu tekst dla prowadzącego, którego ta sama przyczyna już raz ominęła (notatka zadania, 2026-11-26)
    - dopisanie do `task-cycle/skill/planning.md` czterech warunków, kiedy test trafia na listę — dokłada tekst do reguły, której przy tej awarii nikt nie stosował; warunek „nieuruchomione” byłby spełniony prawie zawsze (notatka zadania, 2026-11-26)
  - Source: Mariusz przez doradcę dnia (mandat 14:13), 2026-11-26: „pytanie 2 — a. Pomiar na bazie zamiast zgadywanej listy, z wyjątkiem WAY-136 zapowiedzianym we własnym Goal kawałka; ten wyjątek trzyma właściciel testu i bramka końcowa, więc słaby punkt (za szeroka zapowiedź) ma wąski zasięg. b zostawia ogniwo, które zawiodło; c cofa uzasadnienie WAY-136; d odrzucone w notatce.”
- Co z testem, który wcześniejszy kawałek zostawia czerwony, gdy kawałek mający go naprawić też go nie naprawi?
  - Answer: planista, zapowiadając czerwony test w *Goal* kawałka, który go psuje, wpisuje ten sam test do *Checks* kawałka, który ma go naprawić; test, który po tym kawałku dalej pada, jest jego nieudanym sprawdzeniem i kawałek dostaje ponowienie na mocniejszym modelu jak przy każdym nieudanym sprawdzeniu.
  - Not chosen:
    - zostawić to bramce końcowej, bez zmiany tekstu — niedokończona naprawa wychodzi dopiero po wszystkich kawałkach, bez wskazania kawałka, który zawiódł, a koszt poprawki rośnie z każdym kawałkiem zbudowanym na czerwonym teście
  - Source: Mariusz przez doradcę dnia (mandat 14:13), 2026-11-26: „pytanie 3 — a. Obowiązek stoi w sekcji kawałka, który naprawia, a błąd wychodzi w kawałku, który go zrobił (przyczyna u źródła); b przesuwa wykrycie na koniec cyklu, gdy koszt rośnie z każdym kawałkiem.”

## Context

- Źródło: sprawy AIR-739 i AIR-740 z przeglądu warstwy AI 26.11 (zeszyt `Notes/Areas/(A) Claude code/ai_review_ledger.md`, po 14 dniach `ai_review_ledger_archive.md`); fakty potrzebne do zadania stoją niżej.
- Reguła najmocniejszej klasy stoi w `task-cycle/skill/SKILL.md` w trzech miejscach: krok 9, podkrok 2 trasy z planem („on the class of model the slice's *Model* sets (WAY-229)”, ok. linii 463), akapit „Then the review of the whole change: a fresh reviewer that made none of it, on the strongest class available” (ok. linii 523) i krok 11 („Take the return step”, ok. linii 590); oraz w decyzji WAY-229 w `foundations/decisions.md`.
- Doradca dnia uruchamia cykle z `--settings <the settings file of the day advisor> --model sonnet`; plik ma `availableModels: ["opus","sonnet","haiku"]`.
- W zapisie rozmowy cyklu z 25.11 (`370390df-cbe0-4508-a11e-262c25bed673`) prowadzący szukał listy w `~/.claude/settings.json` i `.claude/settings*.json`, nie znalazł jej i zapisał: „Step 9 asks for the strongest the session's settings allow, from `availableModels`; the session's settings list none” — po czym poprosił o `fable`.
- Dokumentacja Claude Code (https://code.claude.com/docs/en/sub-agents.md, „When an allowlist blocks a subagent model”, czytane 2026-11-26): „the subagent runs on the first of these that applies: 1. For a blocked family alias, the newest permitted version in that family […] 2. The model in `CLAUDE_CODE_SUBAGENT_MODEL`, if you set it […] 3. The main conversation's model”; ostrzeżenie o zastępstwie widzi tylko człowiek w sesji interaktywnej, a strony nie podają zmiennej, polecenia ani ustawienia, z którego sesja odczyta listę dozwolonych modeli.
- Skala: od 15.11 w sesjach cykli na Sonnecie 9 próśb o `fable` poszło na Sonnecie (3 razy 15.11, 6 razy 25.11; około 257 mln tokenów); 19–20.11 sesje bez listy dostawały Fable poprawnie.
- the-way PR #160: przegląd całej zmiany, poprawka i przegląd poprawki poszły na Sonnecie, co wyszło dopiero w tabeli etapów z `cycle_stages.py`, więc całą rundę powtórzono na `opus` (`git -C <the the-way checkout> show 9b94b3f4:docs/task-cycles/recommendation-not-below-goal/cycle.md`, wiersze tabeli 19:04–19:26).
- loop2 PR #177: przeglądy podpisane w zapisie cyklu jako `fable`, wykryte dopiero uwagą do PR-a (`git -C <the loop2 checkout> show 3f48f79:docs/task-cycles/katalog-map/cycle.md`).
- Po stronie doradcy już naniesione 26.11: `the day advisor's script that lists the allowed models` wypisuje `STRONGEST <model>`, a `the day advisor's skill file` dopisuje do polecenia startowego cyklu „— najmocniejszy model dozwolony w tej sesji: <STRONGEST>”.
- The way już dziś honoruje model podany przy starcie, choć żadna reguła tego nie mówi — w zapisie `370390df`: „The reviewers run with `model: opus`, as the human who started the cycle asked in the entry point's arguments”.
- Reguła listy testów padających między kawałkami (AIR-708, the-way PR #157, commity `b7d99dfa` i `041d11f5`, 22.11) stoi w trzech plikach: `task-cycle/plan/SKILL.md`, punkt zaczynający się „A slice may leave tests of the product failing” (ok. linii 189); `task-cycle/skill/planning.md`, sekcja „A slice's handoff”, akapit „The handoff of each later slice also lists the tests the plan leaves failing” (ok. linii 39); `task-cycle/change/slice.md`, sekcja „Read”, punkt „The dispatch lists the tests the plan leaves failing at your slice's base” (ok. linii 14); oraz w `task-cycle/skill/SKILL.md`, krok 9, podkroki 3 i 4 trasy z planem („the failures its report names against those the plan lists”, „a listed test that fails as the plan says is none (WAY-136)”).
- loop2 PR #177 (cykl `katalog-map`, 25.11): blok listy jest identyczny we wszystkich 12 zleceniach wykonawców, także kawałka 1, który nie powinien mieć żadnej listy; blok mówi „they begin to fail after Slice 3” i „14 known citation errors”; wykonawcy 3, 8 i 9 zastali wymienione testy zielone, wykonawca 8 zastał 12 błędów zamiast 14, wykonawca 12 — zero; wykonawca 11 zgłosił to w raporcie i nikt tego nie odebrał; planista ułożył listę bez uruchomienia testów. Kopia zapisu: `a copy of that cycle's record kept in the author's notes`.
- Wykonawcy już dziś sami uruchamiali padający test na bazie kawałka („at base it passed (50 of 50)”, `cycle.md` tego cyklu, ok. linii 212).
- Pełny zapis sesji przeglądu, w której sprawy powstały (wygasa ok. 2027-02-24, 1,9 MB, nie czytać surowego): `the transcript of the review session in the author's session store`; tekst z niego daje `python "<the author's session-extraction script>" --session 7b2b3869-b91d-4b5b-8c5a-049b30467810 --format text --out <katalog roboczy>/zapis_sesji.txt`.
- Żaden test the way nie trzyma obecnego brzmienia tych reguł (przeszukane `*.py` po `availableModels`, `leaves failing`, `fails as expected`, `strongest class`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-229 — On which class of model do the executor of a slice and the one author work? (`foundations/decisions.md`, ok. linii 6577): „or the strongest class available, which is the strongest of the models that the session's settings allow, which the orchestrator takes from the list of allowed models (in Claude Code the setting `availableModels`; where the session has no such list, every model it offers) and never from the name of the strongest model of the family”. Zmiana, którą niesie zadanie (odpowiedź na pytanie 1): najmocniejszą dostępną klasę prowadzący ustala w każdym cyklu próbnym wywołaniem, z modelem podanym przy starcie jako pierwszym kandydatem i odczytem faktycznego modelu z zapisu sesji, zamiast brać ją z listy `availableModels` albo, bez listy, ze wszystkich modeli, jakie sesja oferuje.
- WAY-136 — When does a task's change need a plan, and who makes and reviews it? (`foundations/decisions.md`, ok. linii 6374): „A slice of a plan may leave tests of the product failing that a later slice of the same plan makes pass, where its *Goal* names each such test file and the slice that makes it pass, and the failure of a test so named is no failing check of the slice that meets it.” Zmiana, którą niesie zadanie (odpowiedź na pytanie 2): test padający także na bazie kawałka nie jest nieudanym sprawdzeniem tego kawałka, a test, który na bazie przechodzi i pada po zmianie, jest nim, chyba że *Goal* tego samego kawałka go zapowiada; zapowiedź z *Goal* wcześniejszego kawałka nie rozstrzyga już o kawałku późniejszym; test zapowiedziany jako czerwony stoi też w *Checks* kawałka, który ma go naprawić, i jego porażka po tym kawałku jest nieudanym sprawdzeniem tego kawałka (odpowiedź na pytanie 3). Zmienia się też *Verification* tej decyzji („the executor of a later slice reports the test as failing as expected, not as a failing check of its slice”; „the executor of a slice takes a test that the plan lists as failing for a failing check of its slice and is retried for it”).
- WAY-227 — Where does the human meet a task cycle's work? (`foundations/decisions.md`): „The orchestrator of a task cycle answers the agents' questions and gives provisional go-aheads under the task owner's delegation, never recording these as human approval, and brings the request to the human, the cycle's first point of human review.” Bez zmiany; z niej wynika, że próbne wywołanie modelu nie pyta człowieka w trakcie cyklu.

## Settlements to record

Candidates: 5 shown, 3 accepted — 2026-11-26

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Próbne wywołanie biegnie w każdym cyklu; model podany przy starcie jest pierwszym kandydatem próby, nie przyjmowanym na wiarę. | sentence of WAY-229 | *Questions to settle*, pytanie o najmocniejszy dozwolony model (jego *Not chosen*) | czy model podany przy starcie przyjąć bez próby i czy brak widocznej listy `availableModels` znaczy, że wolno każdy model |
| 2 | Pomiar na bazie zamiast zgadywanej listy, z wyjątkiem WAY-136 zapowiedzianym we własnym *Goal* kawałka. | sentence of WAY-136 | *Questions to settle*, pytanie o padający test kawałka (jego *Not chosen*) | czy test zapowiedziany w *Goal* wcześniejszego kawałka dalej zwalnia wykonawcę późniejszego kawałka z pomiaru na bazie, czy w ogóle zostawić kawałkowi prawo do zapowiedzianego czerwonego testu |
| 3 | Obowiązek naprawy zapowiedzianego czerwonego testu stoi w sekcji kawałka, który naprawia, a błąd wychodzi w kawałku, który go zrobił. | sentence of WAY-136 | *Questions to settle*, pytanie o test, którego kawałek-właściciel nie naprawi (jego *Not chosen*) | czy kawałek-właściciel ma zapowiedziany test w *Checks*, czy niedokończona naprawa przechodzi pomiar na bazie i wychodzi dopiero w bramce końcowej |

## Out of scope

- Zmiany doradcy dnia w `the day advisor's skill directory` — weszły 26.11 i działają niezależnie od the way.
