---
title: Katalogi robocze zadań the way znikają po scaleniu PR-a, a zaległe są posprzątane
status: draft
created: 2026-11-14T02:55
updated: 2026-11-14
tags: [zadanie]
related: "the process project's note"
---

# Katalogi robocze zadań the way znikają po scaleniu PR-a, a zaległe są posprzątane

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Cykl zadania zostawia katalog roboczy zadania (worktree: osobny katalog z kopią repozytorium na gałęzi zadania) „do poprawek po przeglądzie”, a po scaleniu PR-a nikt go nie usuwa.
- Skill cyklu mówi tylko „Keep the worktree for corrections.” i nie mówi, kiedy katalog przestaje być potrzebny.
- Katalogi zajmują dysk, zaśmiecają listę gita (`git worktree list`) i Mariusz musi je sprzątać ręcznie, nie wiedząc, który jeszcze jest potrzebny do poprawek.
- Reguła z zadania o kopiach roboczych agentów („resztki znikają razem z katalogiem zadania”) nie działa, dopóki nikt katalogu zadania nie usuwa.

### To do

1. Dodać do the way skrypt, który domyślnie tylko wypisuje worktree repozytorium z decyzją „usunę / zostawiam” i powodem, a katalogi usuwa dopiero z przełącznikiem `--apply`.
2. Skrypt uznaje katalog za zbędny tylko wtedy, gdy spełnione jest wszystko naraz: drzewo jest czyste (brak zmian w śledzonych plikach i brak nowych niezignorowanych plików; pliki ignorowane nie liczą się), wszystkie commity katalogu są na zdalnym repozytorium, gałąź katalogu jest scalona, a katalog należy do cyklu, czyli leży na gałęzi zadania albo jest odłączoną kopią bazy pod `.runs/`.
3. Gałąź jest scalona tylko wtedy, gdy jej czubek jest drugim rodzicem commita scalającego na gałęzi docelowej ze zdalnego repozytorium; sprawdza się to samym gitem, bez zapytania do hosta. Skrypt sam odświeża refy zdalnego przed oceną.
4. Kopie bazy `base-check-*` zagnieżdżone w katalogu zadania znikają razem z nim, a luźne skrypt usuwa tylko wtedy, gdy ich nazwa wskazuje zadanie ze scaloną gałęzią.
5. Skrypt rusza tylko checkouty, które git tego repozytorium sam wymienia w `git worktree list`; nigdy kopii głównej, katalogu, w którym sam jest uruchomiony, ani odłączonych katalogów spoza cyklu (m.in. `the-way-global`, `the-way-fullrun`, kopii w schowkach sesji), i nigdy nie usuwa gałęzi, ani lokalnych, ani zdalnych.
6. Wszystko, czego skrypt nie usuwa — z niezacommitowanymi zmianami, z otwartym PR-em, niescalone, bez PR-a, z PR-em zamkniętym bez scalenia, ze scaleniem niewykrywalnym gitem (squash, rebase) — skrypt wypisuje z powodem; przy każdym katalogu do usunięcia wypisuje też jego ignorowane ścieżki poza `.runs/`, pomijając znane cache.
7. W skillu cyklu, w kroku 4, na starcie nowego cyklu (przy tworzeniu gałęzi zadania), dodać uruchomienie skryptu z `--apply` i dopisać je do wyjątków w akapicie „The cycle writes only in the task's worktree”; poprawka po przeglądzie (correction) skryptu nie uruchamia.
8. Cykl przenosi do zapisu cyklu i do opisu PR-a listę katalogów należących do cyklu, które zostały z powodem do ludzkiej decyzji (nie obce odłączone), tą drogą, którą WAY-373 prowadzi pozostałości po agentach. Lista podaje nazwę katalogu, jego gałąź i powód, bez ścieżki bezwzględnej, i czeka w pamięci cyklu do powstania zapisu cyklu w kroku 5.
9. Zdanie „Keep the worktree for corrections.” zostaje, z dopowiedzeniem, że katalog leży do scalenia gałęzi zadania, a usuwa go skrypt z punktu 1.

### Questions to settle

- Kto i kiedy usuwa katalog roboczy zadania po scaleniu PR-a?
  - Answer: skrypt w the way wypisuje worktree repozytorium i z `--apply` usuwa zbędne; cykl uruchamia go na starcie następnego cyklu, w kroku 4 przy tworzeniu gałęzi zadania. Działa w każdym produkcie przypiętym do the way. Opcja zmienia decyzję WAY-298: zdanie „The fast-forward is the one change the cycle makes to a checkout outside the task's worktree.” przestaje być prawdziwe. Katalog `<a directory beside the repository>/the-way-global` (cel dowiązania skilla `maintain-instruction-files`) skrypt zawsze pomija.
  - Not chosen:
    - sam skrypt, bez wpisu w cyklu, uruchamiany przez Mariusza albo doradcę dnia przy scaleniu — kto nie ma doradcy, nie sprząta, a lista rośnie jak dziś.
    - sama reguła w skillu, bez skryptu — każdy cykl ocenia „zbędny” po swojemu i nie ma jednego dry-runu dla jednorazowego sprzątania.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „a” oraz uwaga „<a directory beside the repository>/the-way-global jest celem dowiązania skilla maintain-instruction-files i nie może zostać usunięty”; zgoda na zmianę WAY-298: odpowiedź „tak, oba zapisy” na pytanie 3 przeglądu.
- Który katalog jest zbędny, a który zostaje i trafia na listę dla Mariusza?
  - Answer: skrypt usuwa katalog tylko wtedy, gdy spełnione jest wszystko naraz: drzewo czyste; wszystkie commity katalogu są na zdalnym repozytorium; gałąź katalogu jest scalona do gałęzi docelowej (sprawdzenie samym gitem); katalog należy do cyklu, czyli leży na gałęzi zadania albo jest odłączoną kopią bazy pod `.runs/`. Pozostałe odłączone katalogi skrypt pomija. Wszystko, czego nie usuwa — z niezacommitowanymi zmianami, z otwartym PR-em, niescalone, bez PR-a, z PR-em zamkniętym bez scalenia — trafia na listę dla Mariusza do ręcznej decyzji. Kopie bazy `base-check-*`: zagnieżdżone w katalogu zadania znikają razem z nim, luźne skrypt usuwa tylko wtedy, gdy ich nazwa wskazuje zadanie ze scaloną gałęzią.
  - Not chosen:
    - zamknięcie PR-a bez scalenia jako powód usunięcia — wymaga zapytania do hosta (`gh`), a cykl działa też z innymi hostami niż GitHub; w the way dotyczy to jednego katalogu, w `loop2` żadnego.
    - skrypt usuwa każdą czystą, odłączoną kopię bazy pod `.runs/` — może usunąć kopię trwającego równolegle cyklu.
    - skrypt nie rusza kopii bazy — 8 luźnych kopii w kopii głównej the way zostaje do ręcznego sprzątania.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedzi „tak” i „a” na pytania o definicję „zbędny” i o kopie bazy.
- Co znaczy „gałąź scalona”?
  - Answer: czubek gałęzi jest drugim rodzicem commita scalającego na gałęzi docelowej ze zdalnego repozytorium. Gałąź scalona squashem albo rebase'em nie jest rozpoznana i trafia na listę z powodem „scalenie niewykrywalne gitem”.
  - Not chosen:
    - samo „czubek gałęzi jest przodkiem gałęzi docelowej” — gałąź założona przed chwilą przez równoległy cykl, jeszcze bez commitów, wskazuje czubek gałęzi docelowej i przeszłaby jako „scalona”, więc automat usunąłby katalog cyklu, który dopiero ruszył.
    - dodatkowo wiek katalogu (np. starszy niż doba) — heurystyka na czasie, myli się przy dłuższej pracy.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „a” na pytanie 2 przeglądu.
- Kto robi jednorazowe sprzątnięcie zaległych katalogów w the way i `loop2` i kiedy?
  - Answer: zadanie dostarcza skrypt; przy PR-ze zadania, przed jego scaleniem, Mariusz w każdym z dwóch repozytoriów uruchamia skrypt z gałęzi zadania najpierw jako dry-run, przegląda listę „usunę / zostawiam i dlaczego” i dopiero po akceptacji uruchamia z `--apply`; usunięcia nie da się cofnąć. To ruch ludzki ustawiony „w cyklu”, bo korzysta z kodu, który cykl pisze, i dotyczy katalogów poza repozytorium (WAY-140). Dzięki temu pierwszy cykl po scaleniu zastaje niewiele do usunięcia.
  - Not chosen:
    - posprzątać teraz ręcznymi poleceniami gita, poza zadaniem — bez przetestowanego skryptu i bez jednej definicji „zbędny”; katalogi wracałyby, bo nic ich nie pilnuje.
    - pierwszy start cyklu po scaleniu robi to sam — pierwsze, największe usunięcie (ponad 100 katalogów) bez wglądu Mariusza w listę i bez cofnięcia.
    - dry-run i `--apply` po scaleniu — pierwszy cykl po scaleniu mógłby uruchomić `--apply` przed Mariuszem.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „a” na pytanie 3 („skasowania nie da się cofnąć”) i odpowiedź „a” na pytanie 1 przeglądu („dry-run i --apply robi Mariusz przy PR-ze, przed scaleniem”).
- Gdzie ląduje lista „zostaje, do decyzji Mariusza” i co zawiera?
  - Answer: w zapisie cyklu i w opisie PR-a, tą samą drogą co pozostałości po agentach (WAY-373); zawiera tylko katalogi należące do cyklu, które zostały z powodem do ludzkiej decyzji, każdy jako nazwa katalogu, gałąź i powód, bez ścieżki bezwzględnej, i czeka w pamięci cyklu do powstania zapisu cyklu. Obce odłączone katalogi widać tylko w wydruku skryptu.
  - Not chosen:
    - tylko w zapisie cyklu — zapis leży w ignorowanym `.runs/` i znika razem z katalogiem zadania.
    - tylko wypisana przez skrypt na konsolę — lista przepada, gdy cykl nie pokaże jej dalej.
    - obce odłączone katalogi też w opisie PR-a — wracałyby w każdym PR-ze, a opis PR-a nie przechodzi kontroli ścieżek prywatnych ze ścieżką bezwzględną.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „a” na pytanie 4 oraz „tak” na pytanie 4 przeglądu.
- Czy automat może usuwać katalogi leżące poza katalogiem repozytorium (`the-way-wt`, `loop2-wt`) bez człowieka?
  - Answer: tak, o ile git tego repozytorium sam je wymienia w `git worktree list`; to stan repozytorium, a nie serwer, DNS, klucz ani konto zewnętrzne z WAY-140.
  - Not chosen:
    - tylko katalogi pod katalogiem repozytorium — katalogi w `the-way-wt` i `loop2-wt` zostają do ręcznego sprzątania.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „tak, oba zapisy” na pytanie 3 przeglądu.
- Czy usunięcie katalogu może zgubić pliki ignorowane poza `.runs/`?
  - Answer: tak, to akceptowane: pliki ignorowane nie liczą się do „czyste”, a dry-run pokazuje przy każdym katalogu do usunięcia jego ignorowane ścieżki poza `.runs/` (z pominięciem znanych cache), żeby Mariusz zobaczył np. `.claude/settings.local.json` przed `--apply`.
  - Not chosen:
    - ignorowane pliki liczą się jako niezacommitowane — zablokowałoby to prawie wszystkie katalogi `loop2` (`node_modules`, `dist`).
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „tak” na pytanie 5 przeglądu.

## Context

- Zlecił doradca dnia w imieniu Mariusza 2026-11-14 przy doprecyzowaniu zadania blokady zapisu poza katalogiem zadania, które tego samego dnia porzucono (decyzja Mariusza), więc katalog zadania zostaje worktree głównej kopii.
- Mariusz 2026-11-14: robimy.
- Odczyt the way z 2026-11-14 (`git worktree list`, klasyfikacja po `gh pr list` i `git branch --merged`, nic nie usunięto) dał 94 wpisy: kopia główna 1, katalogi zadań `task/*` ze scalonym PR-em i czystym drzewem 78, katalog zadania z zamkniętym niescalonym PR-em 1, odłączone kopie bazy `base-check-*` pod `.runs/` 11 (8 luźnych, 3 zagnieżdżone), odłączone poza `.runs/` 2 (`the-way-fullrun`, `the-way-global`), katalog w schowku sesji z niezacommitowanymi zmianami 1; otwartych PR-ów nie było, a od odczytu doszedł kolejny scalony PR (#123).
- Odczyt `loop2` z tego samego dnia dał 57 wpisów: kopia główna 1, scalone czyste 42, scalone z niezacommitowanymi zmianami 4, z otwartym PR-em 2, bez PR-a niescalone 4, odłączone 4.
- Liczby pochodzą z dysku autora i nie dają się sprawdzić ze źródeł repozytorium, więc cykl liczy je na nowo.
- `the-way-global` jest celem dowiązania (junction) `~\.claude\skills\maintain-instruction-files`, więc jego usunięcie zepsułoby ten skill.
- Poza `.runs/` odczyt znalazł ignorowane pliki: w the way `.superpowers` (5 katalogów) i cache testów, w `loop2` `node_modules` (52), `dist` (50), cache narzędzi i raz `.claude/settings.local.json`.
- Zapis scalonego zadania jest w historii gita, bo krok 12 skilla cyklu kopiuje go do `docs/task-cycles/<task-slug>/`, commituje i usuwa, a opis PR-a linkuje go po SHA commita.
- Kod i test w części `task-cycle` objęte są odstępstwem WAY-328, więc zadanie nie czeka na wytyczne kodowania ani testowania the way.
- Ruch zadania planu do „done” opiera się na scalonej historii zintegrowanej gałęzi (WAY-153, niezmiennik `project-plan-state-evidence`), więc usunięcie katalogu po scaleniu nie odbiera tego dowodu.
- Powiązane: the note of the task about the agents' work copies, scalone jako WAY-373, którego ostatni krok „resztki znikają razem z katalogiem zadania” zależy od tego zadania.
- Powiązane: zadanie w `(A) Claude code` o sprzątaniu schowków sesji `%TEMP%\claude`, bo katalogi zadań w schowkach leżą na styku obu zadań.
- Miejsca do zmiany w `task-cycle/skill/SKILL.md`: akapit zaczynający się „The cycle writes only in the task's worktree”, krok 4 (akapit „In the-way itself, first bring the checkout”) i zdanie „Keep the worktree for corrections.” kończące krok 12.

## Questions carried to cycle

- Nazwa i miejsce skryptu w `task-cycle/` oraz to, jak odróżnia gałąź zadania od innej (prefiks `task/` nie wystarcza: gałąź `s7-cycle-remarks` jest scalona i go nie ma).
- Kolejność usuwania zagnieżdżonych katalogów, katalog zablokowany przez inny proces (Windows) i katalogi, których rejestracja w gicie jest zepsuta.
- Dokładna reguła „nazwa wskazuje zadanie ze scaloną gałęzią” dla luźnych kopii bazy `base-check-*` i `base-fix-*`.
- Które ignorowane ścieżki są „znanymi cache” pomijanymi w wydruku.

## Human actions

- Jednorazowe sprzątnięcie zaległych katalogów w the way i `loop2`: Mariusz przy PR-ze zadania, przed jego scaleniem, uruchamia skrypt z gałęzi zadania jako dry-run, przegląda listę, po akceptacji uruchamia z `--apply`, w każdym z dwóch repozytoriów (katalogi `the-way-wt` i `loop2-wt` leżą poza repozytorium) — in the cycle

## Decisions in play

- WAY-298 — How does a cycle on the-way itself start from the current rules?: „The fast-forward is the one change the cycle makes to a checkout outside the task's worktree.” Zadanie zmienia to zdanie: na starcie nowego cyklu cykl uruchamia też skrypt, który usuwa zbędne katalogi robocze zadań, więc fast-forward przestaje być jedyną zmianą poza katalogiem zadania. Wybór drogi „skrypt uruchamiany na starcie cyklu” i odpowiedź „tak” na pytanie o tę zmianę to zgoda na nią (WAY-314).
- WAY-373 — Where does an agent of a task cycle make a working copy to check something, and what happens to it?: „where a removal fails, the agent finishes and names the remainder with its path in the report, and the cycle carries it to its record and to the description of the request, where the human sees it, and goes on.” Zadanie nie zmienia tej decyzji; lista katalogów, których skrypt nie usunął, idzie tą samą drogą, bez ścieżki bezwzględnej.
- WAY-140 — How does a task change something outside the product's repository?: „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it […]” Jednorazowe sprzątnięcie jest takim ruchem ludzkim, ustawionym w cyklu; usuwanie przez automat checkoutów wymienianych przez `git worktree list` zadanie uznaje za stan repozytorium, nie za taki skutek.
- WAY-153 — What evidence supports a task state in a project plan?: „[…] brings a closed-unmerged PR or a trace conflicting with the plan to the human without automatically correcting the plan.” Katalog z PR-em zamkniętym bez scalenia zostaje na liście dla człowieka, tak jak tu.
- WAY-269 — How does a task leave a cycle that met a reserved choice, and how does it come back?: „For a task of a project plan, on the human's word, the project orchestrator removes by name that one cycle's worktree or working directory, its local branch, its branch on the host and that branch's remote-tracking ref […]” Zadanie tego nie zmienia: katalog niescalonego, zwróconego cyklu zostaje, bo jego gałąź nie jest scalona.

## Settlements to record

Candidates: 7 shown, 6 accepted — 2026-11-14

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Na starcie nowego cyklu cykl uruchamia skrypt usuwający zbędne katalogi robocze zadań repozytorium; to zmiana poza katalogiem zadania obok fast-forwardu. | sentence of WAY-298 | pytanie „Kto i kiedy usuwa katalog roboczy zadania po scaleniu PR-a?” (wybór człowieka; drogi niewybrane pod pytaniem) | czy sprzątanie robi sam cykl, kiedy, i czy zdanie „fast-forward to jedyna zmiana poza katalogiem zadania” nadal obowiązuje |
| 2 | Skrypt usuwa katalog tylko wtedy, gdy drzewo jest czyste, wszystkie commity są na zdalnym, gałąź jest scalona (czubek jest drugim rodzicem commita scalającego na gałęzi docelowej, sprawdzone samym gitem) i katalog należy do cyklu; reszta, z katalogiem zamkniętego niescalonego PR-a włącznie, zostaje na liście dla człowieka. | decision | pytania „Który katalog jest zbędny…” i „Co znaczy „gałąź scalona”?” (wybór człowieka; drogi niewybrane pod pytaniami) | czy zamknięty PR, czubek będący przodkiem albo każda czysta odłączona kopia wystarcza do usunięcia i czy sprawdza się host |
| 3 | Lista katalogów cyklu, których skrypt nie usunął, idzie do zapisu cyklu i do opisu PR-a drogą WAY-373, jako nazwa, gałąź i powód, bez ścieżki bezwzględnej. | skill or instruction file: task-cycle/skill/SKILL.md | pytanie „Gdzie ląduje lista…” (wybór człowieka; drogi niewybrane pod pytaniem) | czy lista trafia tylko na konsolę albo tylko do zapisu cyklu, ze ścieżkami, które kontrola ścieżek prywatnych odrzuci |
| 4 | Skrypt usuwa same katalogi i nie usuwa gałęzi, ani lokalnych, ani zdalnych. | decision | doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „przyjąć” na pytanie o wiersz 4 (wiersz wyprowadzony z materiału; skasowanie gałęzi ewentualnie osobnym zadaniem) | czy po usunięciu katalogu cykl kasuje też gałąź zadania, jak robi to orkiestrator w WAY-269 na słowo człowieka |
| 5 | Skrypt usuwa tylko checkouty, które git tego repozytorium wymienia w `git worktree list`, także poza katalogiem repozytorium, a to nie jest skutek poza repozytorium w rozumieniu WAY-140. | decision | pytanie „Czy automat może usuwać katalogi leżące poza katalogiem repozytorium…” (odpowiedź „tak, oba zapisy”) | czy automat może usuwać katalogi poza repozytorium bez człowieka i które |
| 6 | Pliki ignorowane poza `.runs/` nie liczą się do „czyste”, a dry-run pokazuje je przy każdym katalogu do usunięcia. | decision | pytanie „Czy usunięcie katalogu może zgubić pliki ignorowane poza `.runs/`?” (wybór człowieka; droga niewybrana pod pytaniem) | czy ignorowane pliki blokują usunięcie, jak `node_modules` w `loop2`, i czy skrypt je pokazuje |

## Out of scope

- Sprzątanie schowków sesji `%TEMP%\claude` (osobne zadanie w `(A) Claude code`).
