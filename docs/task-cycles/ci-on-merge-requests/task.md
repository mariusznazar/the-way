---
title: Automatycznie sprawdzać zmiany przed scaleniem i wykrywać nowe luki w używanych bibliotekach
status: draft
created: 2026-10-25T16:00
updated: 2026-11-14
tags: [zadanie]
related: "the project note of the process work in the author's notes"
---

# Automatycznie sprawdzać zmiany przed scaleniem i wykrywać nowe luki w używanych bibliotekach

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Testy przed scaleniem uruchamia dziś tylko człowiek albo agent cyklu na własnej maszynie; ani the way, ani loop2 nie mają automatu, który uruchamia jedno polecenie testów na prośbie o scalenie.
- Mariusz scala prośby, nie widząc wyniku testów policzonego poza maszyną, na której zmianę zrobiono; agent prowadzący cykl sam uruchamia bramkę i sam podaje jej wynik.
- Testy wymagające Linuksa nie biegną nigdzie: pięć testów sprawdzania plików instrukcji (dowiązania, pętle dowiązań, FIFO) pomija się na Windowsie Mariusza, a recenzenci zgłosili to w ośmiu PR-ach the way.
- Luka odkryta w bibliotece, której produkt już używa, nie daje sygnału: audyt zmiany (WAY-206) sprawdza tylko wersje, które zmiana wnosi.
- Przegląd fundamentu loop2 z 2026-11-06 znalazł na `main` (`5694146`) `body-parser` 2.3.0 z podatnością wysokiej wagi (GHSA-27r3-jxmh-p828 — serwer da się położyć spreparowanym, skompresowanym żądaniem) i `qs` 6.16.0 z podatnością średniej wagi; audyt zmian ich nie zgłosił, a alerty Dependabota w loop2 były wtedy wyłączone.

### To do

1. Fundament the way mówi, że jedno polecenie testów produktu biegnie w CI na każdej prośbie o scalenie, z `.the-way` na commicie przypiętym przez produkt, a jego wynik jest wymaganym sprawdzeniem przed scaleniem, z prawem obejścia dla właściciela repozytorium; plik konfiguracji CI pisze produkt sam (wiersze 1 i 2 tabeli ustaleń).
2. the way ma opis tego, co plik konfiguracji CI produktu musi zawierać: uruchomienie jednego polecenia testów na każdej prośbie o scalenie; pobranie `.the-way` na commicie, który produkt przypiął, nigdy najnowszego the way (WAY-34); historię gita, której potrzebuje `foundation_check.py` do porównania z commitem, od którego gałąź odeszła; ustawienie wyniku jako wymaganego sprawdzenia z prawem obejścia dla właściciela.
3. Blok, który instalator wpisuje do `AGENTS.md` produktu (`installation/install.py`, funkcja `product_guidance`, akapit zaczynający się od „Before a merge, run every test of this repository with its one command”), mówi, że jedno polecenie testów uruchamia też `check_instructions.py`, przy czym błąd skryptu zatrzymuje testy, a ostrzeżenie nie; że to polecenie biegnie w CI na każdej prośbie o scalenie; i wskazuje opis z punktu 2.
4. Repozytorium the way ma plik konfiguracji GitHub Actions, który na każdej prośbie o scalenie do `foundations` uruchamia na Linuksie `python -B gate/run_tests.py`. Testy, które na Linuksie padną, cykl poprawia, o ile poprawka mieści się w zakresie zadania; większą wydziela jako uwagę w opisie prośby o scalenie.
5. Skill `maintain-coding-guidelines` przy audycie zależności proponuje produktowi włączenie alertów serwisu, na którym leży repozytorium, o lukach w bibliotekach (na GitHubie alertów Dependabota) jako sygnału o luce w bibliotece już używanej; włącza je człowiek. Miejsce: `product-guidelines/coding/settle.md`, punkt zaczynający się od „for the audit of dependencies, that a vulnerability found in a dependency the product already holds gives no signal”, ok. linii 123, i miejsce, w którym skill proponuje audyt zależności.
6. WAY-206 mówi, że sygnał o luce w bibliotece już używanej dają alerty serwisu, na którym leży repozytorium (wiersz 4 tabeli ustaleń).
7. Instrukcja cyklu zadania (`task-cycle/skill/SKILL.md`, sekcja „Request and handoff”, ok. linii 515) każe prowadzącemu, gdy na otwartej prośbie biegnie CI, czekać na jego wynik; czerwony wynik traktuje jak nieudaną końcową bramkę — poprawka i jej recenzja — a wynik CI trafia do opisu prośby (wiersz 6 tabeli ustaleń).

### Acceptance criteria

- Przebieg CI na prośbie o scalenie tego zadania uruchamia pięć testów `instruction-files/test_check_instructions.py`, które na Windowsie są pomijane (dowiązania, pętle dowiązań, FIFO), zamiast je pominąć.

### Questions to settle

- Co the way dostarcza produktom, żeby ich jedno polecenie testów biegło automatycznie na każdej prośbie o scalenie, i czy konfiguracja CI loop2 należy do tego zadania?
  - Answer: the way zapisuje zasadę i mówi produktowi, jak ją spełnić: decyzję, że jedno polecenie testów produktu biegnie w CI na każdej prośbie o scalenie, z `.the-way` na przypiętym commicie (WAY-34); zdanie o tym w bloku, który instalator wpisuje do `AGENTS.md` produktu; krótki opis tego, co plik konfiguracji CI produktu musi zawierać. Plik konfiguracji CI loop2 pisze osobne zadanie w backlogu loop2 (inne repozytorium), które czeka na to zadanie.
  - Not chosen:
    - instalator sam wkłada do produktu gotowy plik konfiguracji CI — instalator nie zna środowiska produktu, więc plik i tak trzeba poprawiać ręcznie; po poprawce instalator nadpisze zmiany produktu albo przestanie plikiem zarządzać; zmienia się obietnica instalatora wobec produktów, która dziś wymienia, których plików dotyka
    - the way niczego produktom nie daje, loop2 robi CI sam — zasada żyje tylko w loop2, następny produkt zaczyna od zera, a instalator dalej mówi tylko „uruchom testy przed scaleniem”
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 — a. Zadanie na plik CI w loop2 dopisz jako osobną linię w backlogu Loop według system_zadan.md (zadanie agentowe, z zależnością ⛔ od tego zadania).”
- Czy the way dostaje własne CI, które uruchamia `python -B gate/run_tests.py` na każdej prośbie o scalenie do `foundations`, na Linuksie?
  - Answer: Tak, na Linuksie. Testy, które na Linuksie od razu padną, poprawia ten cykl, o ile poprawka mieści się w zakresie zadania; większą poprawkę cykl wydziela jako uwagę w opisie prośby o scalenie.
  - Not chosen:
    - na Linuksie i na Windowsie — dwa przebiegi na każdą prośbę, a ścieżki Windowsa sprawdza już lokalna bramka cyklu
    - bez własnego CI, tylko lokalna bramka — testy wymagające Linuksa nie biegną nigdzie, a the way każe produktom coś, czego sam nie robi
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 — a, własne CI the way na Linuksie. Jeśli testy linuksowe od razu padną, ich poprawka zostaje w tym cyklu, o ile mieści się w zakresie; większą wydziel jako uwagę w opisie PR-a.”
- Czy wynik CI blokuje scalenie (wymagane sprawdzenie w regułach gałęzi), czy tylko się pokazuje?
  - Answer: Wynik CI jest wymaganym sprawdzeniem: prośby o scalenie nie da się scalić, dopóki sprawdzenie nie przejdzie, a właściciel repozytorium ma prawo obejścia. Dotyczy gałęzi `foundations` the way i zasady, którą the way zapisuje dla produktów.
  - Not chosen:
    - wymagane sprawdzenie bez prawa obejścia — awaria CI blokuje każde scalenie, dopóki Mariusz nie wyłączy reguły, a jako właściciel i tak może to zrobić, więc różnica to tylko więcej klikania
    - wynik tylko widoczny, nic nie blokuje — czerwoną prośbę da się scalić przez przeoczenie; „ładny dashboard niczego nie blokuje; blokuje dopiero wymagany check”
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 — a, wymagane sprawdzenie z prawem obejścia dla właściciela; ustawienie reguły na GitHubie jako ruch Mariusza w cyklu.”
- Czym produkt dostaje sygnał o nowej luce w bibliotece, której już używa, gdzie ten sygnał trafia i kto na niego reaguje?
  - Answer: Alertami serwisu, na którym leży repozytorium (na GitHubie alerty Dependabota): skill `maintain-coding-guidelines` proponuje ich włączenie, a włącza je Mariusz w ustawieniach repozytorium. Sygnał trafia do właściciela repozytorium, a reakcją jest zadanie podbicia biblioteki w backlogu produktu. WAY-206 zapisuje te alerty jako źródło sygnału o luce w bibliotece już używanej.
  - Not chosen:
    - codzienny przebieg CI z narzędziem audytu produktu na całym zestawie bibliotek — drugi plik konfiguracji w każdym produkcie i codzienne przebiegi, mocniejsza zmiana WAY-206, a zysk to tylko spójność progu wagi z audytem zmiany
    - nic, ograniczenie zostaje na stałe i WAY-206 zapisuje je jako przyjęte — przy wyłączonych alertach powtórzy się luka wysokiej wagi na `main` bez żadnego sygnału, jak z `body-parser`
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „4 — a, alerty serwisu (Dependabot), skill wytycznych proponuje ich włączenie, włącza Mariusz; WAY-206 zapisuje to jako źródło sygnału o luce w już używanej bibliotece.”
- Czy do tego zadania należy dopisanie `check_instructions.py` do jednego polecenia testów, które instalator opisuje produktowi (karta D6 z analiz 12.11)?
  - Answer: Tak. Zdanie instalatora o jednym poleceniu testów mówi, że polecenie uruchamia też `check_instructions.py`; błąd skryptu zatrzymuje testy, ostrzeżenie nie. loop2 dopisuje wywołanie w swoim zadaniu o CI.
  - Not chosen:
    - osobne zadanie — osobny cykl dla jednego zdania w tym samym bloku instalatora
    - nie robić — martwa ścieżka albo powtórzona reguła w plikach instrukcji wyjdzie dopiero przy ręcznym przeglądzie
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „5 — a.”
- Co cykl zadania robi z wynikiem CI na prośbie o scalenie, którą otworzył?
  - Answer: Po otwarciu prośby cykl czeka na wynik CI na niej; czerwony traktuje jak nieudaną końcową bramkę (poprawka i jej recenzja), a wynik wpisuje do opisu prośby. Mariusz dostaje prośbę dopiero z wynikiem CI.
  - Not chosen:
    - cykl bez zmian, wynik CI Mariusz widzi przy prośbie — błąd widoczny tylko na Linuksie trafia do Mariusza i wraca jako runda poprawek
    - CI zastępuje końcową bramkę cyklu — błędy widoczne tylko na Windowsie przestają być łapane, cykl staje przy awarii GitHuba; największa zmiana z trzech
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „6 — b, cykl czeka na wynik CI na swojej prośbie, czerwony traktuje jak nieudaną końcową bramkę, wynik wpisuje do opisu.”

## Context

- Ani the way, ani loop2 nie mają ochrony gałęzi: GitHub API dla `foundations` the way i `main` loop2 odpowiada „Branch not protected” (odczyt 2026-11-14).
- Oba repozytoria są publiczne (`gh repo view`, odczyt 2026-11-14), więc reguły gałęzi i GitHub Actions są dostępne bez płatnego planu; zastrzeżenie z lekcji 17 kursu AI Tech Leaders o prywatnym repozytorium na koncie osobistym tu nie zachodzi.
- loop2 ma dwa workflow: `.github/workflows/deploy.yml` (wdrożenie po wypchnięciu na `main`) i `.github/workflows/check-address.yml` (co pięć minut sprawdza publiczny adres; porażka powiadamia właściciela przez GitHub) — żaden nie uruchamia testów.
- Jedno polecenie testów loop2 to `npm test`, czyli `python -B scripts/test.py`: budowa, testy Node, skrypt bramki the way i `foundation_check.py`; nie uruchamia `check_instructions.py` (`scripts/test.py`, funkcja `main`).
- the way nie ma katalogu `.github/` ani żadnej konfiguracji CI; nie ma też zależności spoza biblioteki standardowej Pythona (git nie śledzi żadnego pliku `requirements*`, `pyproject.toml` ani `package.json`).
- Alerty Dependabota: w loop2 włączone (API `vulnerability-alerts` odpowiada 204), w the way wyłączone (404); odczyt 2026-11-14.
- Pełna bramka the way trwa ok. 16 minut przy `--jobs 1` i krócej domyślnie, gdy katalogi biegną naraz (`agent-instructions/README.md`, sekcja „Check the change”); zadanie o krótszej bramce scalono 2026-11-13 (PR #111).
- Niezmiennik `ci-checking-commands` the way już zakłada CI: „No CI configuration git tracks runs a checking command other than `python -B gate/run_tests.py`.” (`foundations/invariants.md`).
- Instalator pisze produktowi w bloku `AGENTS.md` (`installation/install.py`, funkcja `product_guidance`, zdanie „Before a merge, run every test of this repository with its one command”): przed scaleniem uruchomić wszystkie testy jednym poleceniem i zgłosić, co padło i co zostało niesprawdzone; o automatycznym uruchamianiu nie mówi nic.
- Okresowy audyt całości zależności wydzielono z zadania o wytycznych kodowania (jego pytanie 13); tamten opis zadania nie istnieje już w vaulcie (szukano 2026-11-14), ustalenie zostało w pierwotnym brzmieniu tego zadania: „obejmuje też audyt całości zależności produktu uruchamiany z zegara, bo luka odkryta w zależności, którą produkt już ma, nie daje dziś sygnału, dopóki nikt jej nie ruszy”.
- Przy odchudzaniu the way wycięto zegar, czyli polecenie uruchamiane niezależnie od zmian (`odchudzanie_radykalne_dane/obowiazki_1_3_4_6.md`, ok. linii 322); WAY-206 przyjmowała brak sygnału o luce w bibliotece już używanej tylko do czasu zegara, a po jego wycięciu ograniczenie zostało na stałe bez rozstrzygnięcia.
- Analizy z 12.11.2026 (sprawa 10 w `analizy_na_fable_dane/rozstrzygniecia_mariusza.md`) dokładają: lista bramek z kursu Mega.DEV (formatowanie, linter, typy, audyt zależności, testy, skrypty własne; cały zestaw ponownie po każdej poprawce — `praktyki_z_kursu_mega_dev_cz2.md`); zasada z lekcji 02 AI Tech Leaders „nie scalać bez zielonych sprawdzeń” i z lekcji 14 „ładny dashboard niczego nie blokuje; blokuje dopiero wymagany check” (`praktyki_z_kursu_ai_tech_leaders.md`, `praktyki_z_kursu_ai_tech_leaders_cz2.md`, sekcja U4); cztery wiersze rejestru problemów, w których agent pracował na Windowsie albo sam podawał wynik (brak `logrotate`, brak Linuksa dwa razy, kod wyjścia `tail` zamiast testów).

## Questions carried to cycle

none

## Human actions

- Ustawić na GitHubie, w regułach gałęzi `foundations` repozytorium the way, sprawdzenie CI tego zadania jako wymagane przed scaleniem, z prawem obejścia dla właściciela repozytorium; GitHub pozwala wybrać tylko sprawdzenie, które już raz się uruchomiło — in the cycle

## Decisions in play

- **WAY-16** — „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.” Zadanie dopisuje do niej zdania wierszy 1 i 2 tabeli ustaleń: polecenie biegnie w CI na każdej prośbie o scalenie, z `.the-way` na przypiętym commicie, plik CI pisze produkt sam, a wynik jest wymaganym sprawdzeniem z prawem obejścia dla właściciela.
- **WAY-206** — „The skill `maintain-coding-guidelines` proposes an audit of dependencies that checks a change and fails it only where a version of a dependency that the change brings in against `{fork-point}` has a known vulnerability, as the advisory database named by the product's decision adopting the audit gives it when the check runs, of at least the severity that decision sets, every severity being among the ways the skill offers. The template of the coding discipline carries no audit of the whole tree of a product's dependencies.” Jej *Verification* podaje jako naruszenie „the template carries an audit of the whole tree of dependencies run every day”, a *Rationale* nazywa słabością: „A vulnerability found in a dependency the product already holds gives no signal while no change brings in a version of it.” Zadanie zmienia ją wierszem 4 tabeli ustaleń: sygnał o luce w bibliotece już używanej dają alerty serwisu, na którym leży repozytorium, które skill proponuje włączyć; audyt zmiany i zdanie, że szablon nie niesie audytu całego zestawu bibliotek, zostają.
- **WAY-34** — „A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit.” Jej *Verification* podaje jako zgodne niezmiennik produktu „CI runs only that commit's scripts”, a jako naruszenie „a product's CI fetches the latest the-way on every run”.
- **WAY-160** — „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed.” Zadanie dopisuje do niej zdanie wiersza 6 tabeli ustaleń: gdy na prośbie biegnie CI, prowadzący czeka na jego wynik, czerwony traktuje jak nieudaną końcową bramkę, a wynik wpisuje do opisu prośby.
- **WAY-133** — „Where a rule of an instruction file has to hold every time, the skill of `instruction-files` proposes a mechanism that keeps it without the agent choosing to — a CI check, a linter, a check of a step's output, or a local git hook where the rule guards against slips rather than against an agent that can turn the hook off — and a change to the-way's repository instruction files adds such a rule only with its mechanism.”

## Settlements to record

Candidates: 6 shown, 6 accepted — 2026-11-14

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Jedno polecenie testów produktu biegnie w CI na każdej prośbie o scalenie, z `.the-way` na przypiętym commicie; plik konfiguracji CI pisze produkt sam według opisu the way, a instalator go nie wkłada. | sentence of WAY-16 | Questions to settle — pytanie „Co the way dostarcza produktom…” (wybór Mariusza; *Not chosen* tam) | czy instalator ma wkładać do produktu gotowy plik CI i gdzie w fundamencie stoi zasada uruchamiania polecenia w CI |
| 2 | Wynik CI jest wymaganym sprawdzeniem przed scaleniem, z prawem obejścia dla właściciela repozytorium. | sentence of WAY-16 | Questions to settle — pytanie „Czy wynik CI blokuje scalenie…” (wybór Mariusza; *Not chosen* tam) | czy CI ma tylko pokazywać wynik, czy blokować scalenie, i czy z obejściem |
| 3 | CI the way biegnie na Linuksie, bo testy wymagające POSIX nie biegną na Windowsie Mariusza; Windows sprawdza lokalna bramka cyklu. | data or code: plik konfiguracji CI the way, komentarz przy wyborze systemu | Questions to settle — pytanie „Czy the way dostaje własne CI…” (wybór Mariusza; *Not chosen* tam) | system, na którym biegnie CI the way — sam Windows albo Linux i Windows naraz |
| 4 | Sygnałem o luce w bibliotece, której produkt już używa, są alerty serwisu, na którym leży repozytorium (na GitHubie alerty Dependabota); skill wytycznych kodowania proponuje ich włączenie, a włącza je człowiek. | sentence of WAY-206 | Questions to settle — pytanie „Czym produkt dostaje sygnał…” (wybór Mariusza; *Not chosen* tam) | czy WAY-206 dalej uznaje brak sygnału za stałą słabość, czy szablon wytycznych proponuje codzienny audyt całości |
| 5 | Jedno polecenie testów produktu uruchamia też `check_instructions.py`; błąd skryptu zatrzymuje testy, ostrzeżenie nie. | skill or instruction file: blok instalatora w `AGENTS.md` produktu (`installation/install.py`) | Questions to settle — pytanie „Czy do tego zadania należy dopisanie `check_instructions.py`…” (wybór Mariusza; *Not chosen* tam) | czy ostrzeżenia skryptu też mają zatrzymywać testy |
| 6 | Cykl czeka na wynik CI na swojej prośbie o scalenie, czerwony traktuje jak nieudaną końcową bramkę, a wynik wpisuje do opisu prośby. | sentence of WAY-160 | Questions to settle — pytanie „Co cykl zadania robi z wynikiem CI…” (wybór Mariusza; *Not chosen* tam) | czy cykl oddaje prośbę od razu, czeka na CI, czy zastępuje nim końcową bramkę |

## Out of scope

- Plik konfiguracji CI loop2, dopisanie `check_instructions.py` do `scripts/test.py` loop2 i ustawienie wymaganego sprawdzenia na `main` loop2 — osobne zadanie w backlogu Loop, które czeka na to zadanie.
