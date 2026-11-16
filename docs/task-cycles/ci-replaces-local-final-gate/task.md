---
title: CI na prośbie o scalenie zastępuje końcową pełną bramkę testów, którą cykl uruchamia lokalnie
status: draft
created: 2026-11-14T18:05
updated: 2026-11-15
tags: [zadanie]
related: "the project's note in the author's backlog"
---

# CI na prośbie o scalenie zastępuje końcową pełną bramkę testów, którą cykl uruchamia lokalnie

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Przed każdą prośbą o scalenie agent prowadzący cykl uruchamia pełne testy produktu na komputerze Mariusza (WAY-160), a potem czeka na te same testy w CI na tej prośbie — testy biegną dwa razy, a komputer jest zajęty przez czas lokalnego przebiegu.
- Mariusz, 2026-11-14: „jeśli PR powstanie, a bramka cyklu z pełnym npm test poleci w githubie, to wilk syty i owca cała”.

### To do

1. WAY-160 i instrukcja cyklu (`task-cycle/skill/SKILL.md`, kroki 10 i 12) mówią: gdy na prośbie o scalenie z gotowym kodem biegnie CI, końcową bramką cyklu jest przebieg CI na commicie wypchniętym ostatnio, a cykl nie uruchamia pełnej bramki lokalnie ani na końcu, ani po scaleniu z gałęzią docelową; czerwony wynik CI jest nieudaną bramką (poprawka, jej recenzja, czekanie na przebieg na nowym commicie), z wyjątkiem, który daje WAY-261. Przebieg na kodzie wyjściowym (krok 4) i przebieg po przesunięciu przypiętej wersji the way (krok 2) zostają lokalne. Gdy na prośbie CI nie biegnie, cykl uruchamia bramkę lokalnie jak dziś.
2. Gdy przebieg CI nie da wyniku w ciągu 30 minut od wypchnięcia commita — nie wystartuje, stoi w kolejce albo GitHub nie odpowiada — cykl uruchamia pełną bramkę lokalnie, tak jak dziś, a opis prośby mówi, że CI nie odpowiedziało i bramka biegła lokalnie.
3. CI the way (`.github/workflows/tests.yml`) uruchamia `python -B gate/run_tests.py` na Linuksie i na Windowsie, a oba przebiegi są wymaganymi sprawdzeniami przed scaleniem do `foundations`; plik CI i `agent-instructions/README.md` (sekcje „Check the change” i „Integrate into `foundations`”) przestają mówić, że Windows sprawdza lokalna bramka cyklu.
4. Opis pliku CI produktu (`installation/README.md`, sekcja „Run the one command in CI”) mówi, że CI produktu biegnie na każdym systemie, na którym produkt działa, bo wynik CI zastępuje końcową bramkę cyklu.
5. *Verification* zapisu cyklu mówi wprost, że końcowa bramka biegła w CI, a audyt procesu, gdy zapis cyklu nie ma `gate_times.md`, podaje jako możliwą przyczynę obok cyklu wcześniejszego i zepsutego pomiaru także końcową bramkę w CI, odsyłając do *Verification* zapisu (`process-audit/SKILL.md`, zdanie zaczynające się od „A copy with no `mechanism_measures.md` or `gate_times.md` is an earlier cycle or one whose measuring script failed”, i komunikaty o tym samym w `process-audit/audit_count.py`, funkcja czytająca plik z kopii zapisu i wiersz „Gate times of version”); czasy bramki porównuje dalej tylko z przebiegów lokalnych.

### Acceptance criteria

- Przebieg CI na prośbie o scalenie tego zadania uruchamia na Windowsie 32 testy, które na Linuksie są pomijane (21 testów instalatora z junctions, 10 testów sprawdzania plików instrukcji ze ścieżkami sieciowymi, 1 test z junctions), zamiast je pominąć.

### Questions to settle

- Czy zadanie kończy się raportem, czy od razu zmienia proces?
  - Answer: Od razu zmienia proces: WAY-160, instrukcję cyklu, opis bramki i w razie potrzeby plik CI.
  - Not chosen:
    - samo sprawdzenie zakończone raportem, zmiana w osobnym zadaniu — dwa cykle zamiast jednego, a zysk później
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 a”.
- Czy Windows trzeba sprawdzać, skoro lokalna bramka przestaje biec na końcu cyklu?
  - Answer: Tak: CI the way biegnie na Linuksie i na Windowsie naraz (repozytorium publiczne, więc przebieg na Windowsie nic nie kosztuje); prośba czeka na wolniejszy z dwóch przebiegów. Produkt sprawdza w CI systemy, na których działa (loop2: Linux).
  - Not chosen:
    - sam Linuks — 32 testy windowsowe nie biegną nigdzie, a błąd instalatora przy junctions na Windowsie Mariusza wyjdzie dopiero w użyciu
    - Linuks w CI, a lokalnie tylko katalogi z testami windowsowymi (instalator, sprawdzanie plików instrukcji) — czas tego przebiegu niezmierzony, część obciążenia komputera zostaje
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „2 a […] Repo the-way jest publiczne (sprawdzone), więc przebieg na Windowsie nic nie kosztuje.”
- Co cykl robi, gdy GitHub nie odpowiada albo CI stoi w kolejce?
  - Answer: Czeka do 30 minut od wypchnięcia commita, potem uruchamia pełną bramkę lokalnie i zapisuje w opisie prośby, że CI nie odpowiedziało; cykl nigdy nie staje z powodu GitHuba.
  - Not chosen:
    - cykl staje, prośba czeka zablokowana, aż CI odpowie, a Mariusz wznawia cykl — awaria GitHuba zatrzymuje pracę, czyli dokładnie powód, dla którego WAY-160 ten wariant odrzuciła
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „3 a (limit 30 min od wypchnięcia)”.
- Które przebiegi pełnej bramki przechodzą do CI?
  - Answer: Przebieg końcowy i jego powtórka po scaleniu z gałęzią docelową. Przebieg na kodzie wyjściowym i przebieg po przesunięciu przypiętej wersji the way zostają lokalne — prośby wtedy jeszcze nie ma, a oba zdarzają się rzadko.
  - Not chosen:
    - wszystkie przebiegi — cykl musiałby wypychać gałąź i otwierać roboczą prośbę już na starcie; większa zmiana dla rzadkich przypadków
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „4 a”.
- Co audyt procesu robi z czasami bramki, gdy cykl z CI nie ma już lokalnego przebiegu końcowego?
  - Answer: Pomiar zostaje tylko dla przebiegów lokalnych (awaryjnych, na kodzie wyjściowym, po przesunięciu przypiętej wersji the way); audyt i zapis cyklu mówią wprost, że końcowa bramka biegła w CI i lokalnego czasu nie ma. Czas przebiegu CI widać na stronie GitHuba.
  - Not chosen:
    - cykl pobiera z GitHuba czasy przebiegów CI (Linuks i Windows osobno) do tego samego pliku, a audyt porównuje je jako osobną serię — nowy kod czytający GitHuba, zmiana formatu pliku z czasami i skryptu audytu oraz zmiana WAY-350; wyraźnie większy cykl
    - pomiar czasów bramki znika z audytu całkiem — usunięcie kodu i decyzji, strata także czasów przebiegów lokalnych
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „5 a”.
- Kiedy w regule gałęzi `foundations` przybywa wymagane sprawdzenie na Windowsie?
  - Answer: W trakcie cyklu: cykl zostawia prośbę jako roboczą i zablokowaną z tym krokiem, a Mariusz ustawia regułę przy prośbie.
  - Not chosen:
    - przed cyklem — niewykonalne, bo GitHub pozwala wybrać tylko sprawdzenie, które już raz się uruchomiło, a przebieg na Windowsie pierwszy raz uruchomi się na prośbie tego zadania
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „6 a (regułę ustawia Mariusz przy prośbie, jako Human action)”.

## Context

- WAY-160 odrzuciła CI w miejsce lokalnej bramki z dwóch powodów: błędy widoczne tylko na Windowsie przestałyby być łapane, a awaria GitHuba zatrzymałaby cykl; to zadanie odpowiada na oba (pytania „Czy Windows trzeba sprawdzać…” i „Co cykl robi, gdy GitHub nie odpowiada…”).
- Lokalna pełna bramka the way trwa ok. 16 minut przy `--jobs 1` i krócej domyślnie (`agent-instructions/README.md`, sekcja „Check the change”), a obok innych sesji 23–40 minut (uzasadnienie WAY-350).
- CI na Linuksie przy PR #127: cztery przebiegi, trzy udane po 0,9–1,2 minuty, jeden anulowany; przebieg 43710999530 objął 1563 testy w 11 katalogach i pominął 32 testy windowsowe (`gh run list`, `gh run view --log`, odczyt 2026-11-15).
- Czas przebiegu the way na windowsowej maszynie GitHuba jest nieznany; pierwszy przebieg w cyklu go pokaże.
- Reguła gałęzi `foundations_tests` wymaga dziś jednego sprawdzenia o nazwie `tests`, z prawem obejścia dla właściciela (fakt `foundations-branch-ruleset` w `foundations/environment_facts.md`); komentarz w pliku CI mówi, że nazwa joba zostaje, bo reguła ją nazywa. GitHub pozwala wybrać jako wymagane tylko sprawdzenie, które raz już się uruchomiło.
- Cykl uruchamia pełną bramkę w czterech miejscach `task-cycle/skill/SKILL.md`: krok 2 (po przesunięciu przypiętej wersji the way), krok 4 (na kodzie wyjściowym, pomijany, gdy baza jest scaleniem gałęzi poprzedniego cyklu), krok 10 (końcowy) i krok 12 (powtórka po scaleniu z gałęzią docelową, a potem czekanie na CI).
- Każdy przebieg bramki idzie przez `task-cycle/gate_times.py`, który zapisuje czasy do `gate_times.md` w zapisie cyklu; audyt procesu porównuje je między wersjami procesu (WAY-350, `process-audit/SKILL.md`), a zapis cyklu bez `gate_times.md` uznaje dziś za cykl wcześniejszy albo taki, w którym skrypt pomiaru zawiódł.
- Komunikaty audytu o brakującym `gate_times.md` sprawdzają testy w `process-audit/test_audit_count.py`, a zdanie WAY-160 cytuje `task-cycle/test_request_check.py`.
- Prośba zablokowana na niedokończonym kodzie nie czeka na CI (WAY-160, `task-cycle/skill/blocked_finding.md`, `task-cycle/skill/reserved_return.md`), więc bramka biegnie dla niej lokalnie jak dziś.
- Agenci cyklu już dziś uruchamiają lokalnie testy tego, co zmienili; zadanie dotyczy tylko pełnej serii.
- Zadanie o CI (scalone 2026-11-15, PR #127) zostawiło lokalną bramkę na prośbę Mariusza, żeby nie przesuwać terminu zgłoszenia projektu loop2 na kurs AI Tech Leaders (28.11.2026); loop2 dostanie tę zmianę dopiero po przesunięciu przypiętej wersji the way.
- Mariusz chciał tę zmianę po zgłoszeniu projektu loop2 28.11.2026 (zadanie loop2 o CI przy prośbie o scalenie, `the loop2 task's note in the author's backlog`, sekcja „Out of scope”): cykl tego zadania rusza dopiero po scaleniu tamtego zadania loop2, żeby przesunięcie przypiętej wersji the way w loop2 nie wniosło tej zmiany przed 28.11.

## Questions carried to cycle

none

## Human actions

- Dodać w regule gałęzi `foundations_tests` repozytorium the way sprawdzenie CI na Windowsie jako wymagane przed scaleniem, z prawem obejścia dla właściciela (i poprawić nazwę wymaganego sprawdzenia na Linuksie, jeśli zmieni się wraz z plikiem CI) — in the cycle

## Decisions in play

- **WAY-160** — „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed. […] Where CI runs on a request whose code is finished — one open for review, or one that waits only for human actions in the cycle — the orchestrator waits for the result of the run on each head it pushes to it, a correction's included, treats a red result as a failed gate […]” Jej *Rejected* podaje: „the CI result in place of the cycle's final gate — an error visible only on the cycle's own system is no longer caught, and the cycle stops where the host of the repository fails.” Zadanie zmienia ją punktami 1 i 2 *To do*: przebieg CI na prośbie z gotowym kodem jest końcową bramką cyklu, a lokalny przebieg końcowy biegnie tylko wtedy, gdy CI na prośbie nie biegnie albo nie da wyniku w 30 minut.
- **WAY-16** — „In CI that command runs on every merge request, with `.the-way` at the commit the product pins (WAY-34), from a file of CI configuration that the product writes itself by the description the-way gives, and the installer writes none. The result of that run is a check the repository requires before a merge, and the owner of the repository may bypass it.” Zadanie dokłada do opisu, według którego produkt pisze plik CI, systemy, na których CI biegnie (punkt 4 *To do*).
- **WAY-261** — „The red result of the first run of the gate on the final tree stays the result of the gate, also where the check that failed is one outside the task's scope that passes when run again; the cycle does not stop for it, and the request names that check and the task that fixes it, or proposes that task where none exists.” Wyjątek z punktu 1 *To do* zostaje bez zmian.
- **WAY-350** — „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.” Zdanie decyzji zostaje bez zmian: porównanie dalej obejmuje tylko przebiegi lokalne, których będzie mniej; zmienia się opis cyklu bez pliku z czasami w audycie (punkt 5 *To do*).

## Settlements to record

Candidates: 7 shown, 6 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy na prośbie o scalenie z gotowym kodem biegnie CI, jego wynik na ostatnio wypchniętym commicie jest końcową bramką cyklu: cykl nie uruchamia pełnej bramki lokalnie ani na końcu, ani po scaleniu z gałęzią docelową, a przebieg na kodzie wyjściowym i po przesunięciu przypiętej wersji the way zostaje lokalny. | sentence of WAY-160 | Questions to settle — pytania „Czy zadanie kończy się raportem…” i „Które przebiegi pełnej bramki przechodzą do CI?” (wybór Mariusza; *Not chosen* tam) | czy CI zastępuje tylko przebieg końcowy, czy też przebieg na kodzie wyjściowym i po przesunięciu wersji, i czy cykl dalej uruchamia bramkę lokalnie przed otwarciem prośby |
| 2 | Gdy na prośbie CI nie biegnie, cykl uruchamia pełną bramkę lokalnie, tak jak dziś. | sentence of WAY-160 | To do, punkt 1, ostatnie zdanie; wiersz wyprowadzony przez agenta, przyjęty przez doradcę dnia w imieniu Mariusza, 2026-11-15: „1 a” | czy produkt bez pliku CI, jak dziś loop2, zostaje bez końcowej bramki |
| 3 | Gdy CI nie da wyniku w ciągu 30 minut od wypchnięcia commita, cykl uruchamia pełną bramkę lokalnie, a opis prośby mówi, że CI nie odpowiedziało i bramka biegła lokalnie. | sentence of WAY-160 | Questions to settle — pytanie „Co cykl robi, gdy GitHub nie odpowiada…” (wybór Mariusza; *Not chosen* tam) | jak długo czekać na CI i czy cykl staje, czy idzie dalej bez CI |
| 4 | CI the way biegnie na Linuksie i na Windowsie, bo jego wynik zastępuje końcową bramkę cyklu, a 32 testy biegną tylko na Windowsie. | data or code: `.github/workflows/tests.yml`, komentarz przy wyborze systemów | Questions to settle — pytanie „Czy Windows trzeba sprawdzać…” (wybór Mariusza; *Not chosen* tam) | czy CI the way zostaje na samym Linuksie |
| 5 | CI produktu biegnie na każdym systemie, na którym produkt działa, bo jego wynik zastępuje końcową bramkę cyklu. | sentence of WAY-16 | Questions to settle — pytanie „Czy Windows trzeba sprawdzać…”, drugie zdanie odpowiedzi (wybór Mariusza; *Not chosen* tam) | na jakich systemach produkt ma uruchamiać CI według opisu w `installation/README.md` |
| 6 | Pomiar czasów bramki zostaje tylko dla przebiegów lokalnych, a audyt przy zapisie cyklu bez pliku z czasami podaje końcową bramkę w CI jako trzecią możliwą przyczynę obok cyklu wcześniejszego i zepsutego pomiaru. | skill or instruction file: `process-audit/SKILL.md` | Questions to settle — pytanie „Co audyt procesu robi z czasami bramki…” (wybór Mariusza; *Not chosen* tam) | czy pobierać czasy CI z GitHuba do `gate_times.md`, czy zostawić fałszywe „pomiar się zepsuł” |

## Out of scope

- Plik CI loop2 — loop2 pisze go we własnym zadaniu i bierze nowy opis z `installation/README.md` przy przesunięciu przypiętej wersji the way.
- Windows w loop2 — po przejęciu tej zmiany loop2 traci lokalną bramkę na Windowsie, a jego CI biegnie tylko na Linuksie (zadanie loop2 o CI przy prośbie o scalenie, ustalenie 3: „ścieżki Windowsa sprawdza lokalna bramka”); loop2 rozstrzyga to we własnym zadaniu przy przesunięciu przypiętej wersji the way po tej zmianie.
