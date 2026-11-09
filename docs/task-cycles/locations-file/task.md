---
title: "the way: miejsca spoza repozytorium w pliku ~/.the-way/locations.json zamiast ścieżek w plikach repozytorium"
status: draft
created: 2026-11-07T00:00
updated: 2026-11-08
tags: [zadanie]
related: "the author's project note for this process"
---

## Po co to

- **Jak jest dziś:** Skille, skrypty i instrukcje the way miejscami wskazują rzeczy, które leżą poza repozytorium — backlog w prywatnych notatkach, katalogi na dysku, pliki użytkownika. Robią to wpisaną na stałe ścieżką albo opisem w tekście. Nikt nie spisał, ile jest takich miejsc ani jakiego rodzaju. Repozytoria the-way i `loop2` są publiczne, więc każda taka ścieżka wpisana w the way publikuje się sama. Tak jest już dziś z sekcją „Backlog” w `AGENTS.md` the-way, która podaje bezwzględną ścieżkę do pliku zadań w vaulcie.
- **Kto to odczuwa:** Mariusz, gdy zmiana w the way potrzebuje miejsca na dysku i trzeba je gdzieś wpisać, nie publikując go; każdy inny użytkownik the way, który ma inny układ dysku niż Mariusz.
- **Co jeśli nic:** Każda zmiana, która potrzebuje lokalnej ścieżki, rozwiązuje to po swojemu — wpisaną ścieżką, zmienną środowiskową albo opisem — i ścieżki dalej trafiają do publicznej historii. Przy doprecyzowaniu zadania o czyszczeniu zapisów cykli (2026-11-07) ten wybór wrócił i został ominięty tylko dlatego, że lista prywatnych słów okazała się zbędna.

# the way: miejsca spoza repozytorium w pliku ~/.the-way/locations.json zamiast ścieżek w plikach repozytorium

Status: ready for cycle
Project relation: independent

## Description

### Need

- Repozytorium the-way jest publiczne, więc każda ścieżka bezwzględna wpisana w jego pliki publikuje układ dysku autora i nazwy jego prywatnych notatek.
- Spis odwołań poza repozytorium (pytanie 1, *Context*) pokazał, że kod i skille the way nie mają żadnej wpisanej prywatnej ścieżki; jedyne dwie stoją w sekcji `## Backlog` głównego `AGENTS.md` (linie 20 i 25, `foundations` `a3206c1`).
- Linia 25 tej sekcji wskazuje ścieżką bezwzględną rulebook prywatnych notatek autora, a wyjątek WAY-27 obejmuje tylko miejsce zadań repozytorium, więc niezmiennik `outbound-link-reach` jest dziś złamany.
- Nic nie sprawdza mechanicznie plików repozytorium pod kątem ścieżek: skrypt `task-cycle/private_paths_check.py` (WAY-309) czyta tylko kopię zapisu cyklu i opis requestu, a `outbound-link-reach` ma metodę `review`, więc ścieżka wpisana w skill albo skrypt przechodzi, gdy przeoczy ją review.
- Odbiorcą jest Mariusz: nie chce, by repozytorium the-way mówiło, jak wyglądają jego lokalne ścieżki, a agent dalej ma znajdować jego backlog.

### To do

1. the way ustala plik lokalizacji użytkownika `~/.the-way/locations.json`, leżący poza każdym repozytorium: obiekt JSON, którego klucze to nazwy repozytoriów, a pod każdym — pozycje po nazwie (np. `tasks`, `projects`) ze ścieżkami na dysku użytkownika (pytanie 1).
2. Sekcja `## Backlog` głównego `AGENTS.md` the-way wskazuje miejsce zadań pozycją `tasks` pod `the-way` w tym pliku, bez ścieżki bezwzględnej; gdy pliku albo pozycji brakuje, agent pyta człowieka i proponuje dopisać ją do pliku (pytanie 1).
3. Każdy skill the way, który szuka backlogu produktu w sekcji `## Backlog`, znajduje go także wtedy, gdy sekcja wskazuje pozycję pliku lokalizacji; gdy miejsca brakuje, proponuje zapisać je do pliku lokalizacji, jeśli to miejsce na dysku użytkownika poza repozytorium, a w przeciwnym razie do sekcji `## Backlog`, jak dotąd (pytania 1 i 4).
4. the way dostaje test uruchamiany przez `python -B gate/run_tests.py`, który czyta każdy plik śledzony przez git i nie przechodzi, wypisując plik i linię, gdy znajdzie ścieżkę bezwzględną (litera dysku, katalog domowy) albo link do notatki `[[...]]` — tym samym wzorcem, którym szuka ich `task-cycle/private_paths_check.py` — bez wyjątku dla sekcji `## Backlog` (pytanie 1); pomija tylko pliki z listy w samym teście, które z natury piszą przykładowe ścieżki — dziś `task-cycle/private_paths_check.py`, `task-cycle/test_private_paths_check.py`, `instruction-files/check_instructions.py` i `instruction-files/test_check_instructions.py` (pytanie 2).
5. Linia sekcji `## Backlog` w `AGENTS.md` o przestawieniu zadania na Ready zachowuje samo polecenie, a rulebook notatek autora nazywa słowami, bez ścieżki (pytanie 3).

### Questions to settle

- Pytanie 1: czy the way wprowadza jeden plik z lokalizacjami poza repozytorium, z którego wszystko, co dziś korzysta z wpisanych ścieżek, czytałoby je po nazwie pozycji?
  - Answer: tak — plik `~/.the-way/locations.json` w katalogu domowym użytkownika, w stałym miejscu, bez zmiennej środowiskowej; sekcja `## Backlog` nazywa w nim pozycję zamiast ścieżki, a test nie przepuszcza ścieżki bezwzględnej w żadnym pliku repozytorium. `~` wygląda tak samo u każdego użytkownika, więc nic o jego dysku nie mówi. Słabe punkty przyjęte z tą drogą: każdy użytkownik raz na maszynę zakłada plik (bez niego agent pyta); zmieniają się WAY-27, WAY-107, niezmiennik `outbound-link-reach` i skille czytające `## Backlog`; sesja w chmurze nie ma pliku i pyta człowieka — Mariusz z sesji w chmurze dziś nie korzysta i zostawia tę sprawę.
  - Not chosen:
    - sam test bez pliku, z wyjątkiem dla `## Backlog`, a ścieżka do pliku zadań zostaje w `AGENTS.md` — przyjęte najpierw (Mariusz, 2026-11-08: „no dobra, na razie nie ma sensu chyba tego robić, więc na razie robimy c”), odrzucone: „w repozytorium nie powinno być przecież takich ścieżek i to że są stanowi właśnie problem / nie chcę mieć w repo the way informacji o tym jak wyglądają moje lokalne ścieżki systemowe” (Mariusz, 2026-11-08);
    - `## Backlog` opisuje miejsce słowami, a ścieżka stoi w globalnych instrukcjach użytkownika — „globalne instrukcje to chyba nie jest miejsce na takie rzeczy” (Mariusz, 2026-11-08);
    - plik lokalizacji wskazany zmienną środowiskową, jak prywatna warstwa Open Mercato — koszty pliku w stałym miejscu plus zmienna do ustawienia na każdej maszynie i w każdym narzędziu, a agent w narzędziu, które jej nie widzi, nie znajduje backlogu;
    - plik lokalny w repozytorium ignorowany przez git (np. `CLAUDE.local.md`) — nie ma go w worktree, w którym biegnie cykl, a Codex nie czyta `AGENTS.local.md` (`instruction-files/tool_loading.md:30`);
    - nic nie wprowadzać, poprawić tylko linię rulebooka — ścieżka do pliku zadań zostaje w repozytorium, a następną wpisaną ścieżkę zatrzyma tylko uważne review.
  - Source: Mariusz, 2026-11-08: „C, robimy plik w ~/.the-way / nie wiem jak w takim przypadku rozwiązać sesje chmurowe, ale na razie ich nie używam, więc zostawmy to” — na pytanie „Wybierasz C, czy któraś z wcześniejszych dróg pasuje bardziej?”, przy drodze C, której słabość nazwano: sesja w chmurze nie ma pliku i zapyta.
- Pytanie 2: jak test traktuje pliki, które z natury piszą przykładowe ścieżki — skrypt wykrywania ścieżek, jego testy i skrypt sprawdzania plików instrukcji z testem?
  - Answer: test pomija pliki z listy, która stoi w samym teście; dziś są na niej cztery pliki, w których wzorzec łapie 98 wymyślonych przykładów. Słaby punkt przyjęty z tą drogą: prawdziwa ścieżka wklejona do pliku z listy przejdzie; dopisanie pliku do listy widać w zmianie.
  - Not chosen:
    - test pomija tylko linie oznaczone jako przykład — około 100 linii do oznaczenia i kod znaczników, a prawdziwa ścieżka w oznaczonej linii też przejdzie;
    - bez wyjątków, przykłady przepisane tak, żeby wzorzec ich nie łapał — 98 miejsc do przepisania, testy i opis skryptu trudniejsze do czytania, a każdy przyszły autor testu musi o tym pamiętać;
    - test pomija wszystkie pliki testów i oba skrypty — ścieżka w każdym z kilkudziesięciu testów the way przejdzie.
  - Source: Mariusz, 2026-11-08: „a” — na pytanie „Wybierasz a, b, c czy d?”, przy drodze a, której słabość nazwano: prawdziwa ścieżka w pliku z listy przejdzie.
- Pytanie 3: co zastępuje w sekcji `## Backlog` ścieżkę bezwzględną do rulebooka prywatnych notatek autora?
  - Answer: linia zachowuje samo polecenie (przestaw linię zadania na Ready, [/], i zdejmij datę), a źródło nazywa słowami, jako reguły notatek autora dla zadań agentowych, bez ścieżki; sesje autora czytają rulebook przed każdą operacją na notatkach z jego własnych instrukcji. Słaby punkt przyjęty z tą drogą: zmiana reguły w rulebooku nie przenosi się sama do `AGENTS.md` — jak już dziś, bo polecenie stoi tam przepisane.
  - Not chosen:
    - rulebook jako druga pozycja pliku lokalizacji pod `the-way` — jeszcze jedna pozycja do założenia, a plik zaczyna trzymać źródła reguł obok miejsc backlogu, wbrew pytaniu 4.
  - Source: Mariusz, 2026-11-08: „spróbujmy a” — na pytanie „Wybierasz a czy b?”, przy drodze a, której słabość nazwano: zmiana w rulebooku nie dogoni `AGENTS.md`.
- Pytanie 4: co trafia do pliku lokalizacji — tylko miejsce na dysku użytkownika poza repozytorium, czy każde miejsce backlogu?
  - Answer: tylko miejsce na dysku użytkownika poza repozytorium; katalog w repozytorium (ścieżka względna) albo adres publicznego trackera zostaje wprost w sekcji `## Backlog`, jak dziś. Słaby punkt przyjęty z tą drogą: backlog da się wskazać na dwa sposoby, a agent, który dopisuje brakujące miejsce, rozpoznaje, który pasuje.
  - Not chosen:
    - zawsze plik, a sekcja `## Backlog` tylko nazywa pozycję — każdy użytkownik każdego produktu zakłada plik także przy backlogu publicznym albo w repozytorium, a nowa osoba w zespole nie znajdzie zadań, dopóki nie wpisze ścieżki, którą wszyscy znają.
  - Source: Mariusz, 2026-11-08: „a” — na pytanie „Wybierasz a czy b?”, przy drodze a, której słabość nazwano: dwa sposoby wskazania backlogu.
- Pytanie 5: czy zadanie czeka na własne wytyczne kodowania i testów the way, skoro dopisuje test i zmienia skille w repozytorium bez `guidelines/`?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way, a brak wytycznych zostaje w osobnym zadaniu o własnych wytycznych the way. Słaby punkt przyjęty z tą drogą: test i zmiany skilli powstają bez wytycznych kodowania i testów, jak dotychczasowe skrypty the way.
  - Not chosen:
    - czekać na zadanie o wytycznych — nie ma ono jeszcze wybranego kierunku, a ścieżki autora stałyby do jego scalenia w publicznym `AGENTS.md`.
  - Source: Mariusz, 2026-11-08: „bez wytycznych” — na propozycję agenta przeniesienia odpowiedzi z zadania o czyszczeniu zapisów cykli (Mariusz, 2026-11-07: „tak”; 2026-11-06: „nadal jedziemy bez tego”).

## Context

- Spis przeszukał 269 plików śledzonych przez git na `foundations` `a3206c1` (2026-11-08): litera dysku przed `Storage`/`Users` i dowolna litera dysku przed nazwą katalogu, `~/`, `$HOME`, `USERPROFILE`, `Path.home`, `expanduser`, `os.environ` i `getenv`, słowa „vault”, „obsidian”, „private note”, „backlog”, linki `[[`, ścieżki `../`; szerszy wzorzec znalazł obie znane linie `AGENTS.md`.
- Odwołania, które nic prywatnego nie publikują: katalogi domowe narzędzi (`~/.claude`, `~/.codex`, zmienne `CLAUDE_CONFIG_DIR` i `CODEX_HOME`) w `task-cycle/cycle_stages.py:11`, `instruction-files/check_instructions.py:479` i `instruction-files/tool_loading.md` — u każdego użytkownika te same, ustalone przez Claude Code i Codex.
- Backlog produktu skille the way znajdują po nazwie sekcji, bez ścieżki: około 15 plików każe czytać `## Backlog` w `AGENTS.md` produktu, np. `project-level/task/skill/read_sources.md:17`, `foundation-review/SKILL.md:40`, `project-level/skill/first_write.md:5` (WAY-107).
- Prywatne rzeczy opisane słowami: „the author's private notes” (`AGENTS.md:22`) i „the task's note in the author's backlog” (WAY-308); program `gh` do publikacji opisu requestu (`task-cycle/skill/request_template.md:36`) nie jest lokalizacją.
- Wzorzec `task-cycle/private_paths_check.py` uruchomiony na każdym pliku śledzonym (2026-11-08, `a3206c1`) wypisuje 100 miejsc: 2 w `## Backlog` w `AGENTS.md` i 98 w czterech plikach, które opisują albo testują wykrywanie ścieżek — `task-cycle/test_private_paths_check.py` (85), `task-cycle/private_paths_check.py` (10), `instruction-files/check_instructions.py` (2), `instruction-files/test_check_instructions.py` (1).
- Open Mercato (`open-mercato/skills`, `b6d1ecb`) trzyma ustawienia zespołu w commitowanym `.ai/agentic.config.json` ze ścieżkami względnymi wobec repozytorium, a osobiste ścieżki programów i adresy usług w opcjonalnym pliku użytkownika poza repozytorium, wskazanym zmienną `OM_AGENT_HARNESS_CONFIG` (`skills/om-setup-agent-harness/SKILL.md:75-77`); lokalizacji notatek ani backlogu tam nie ma, bo ich backlogiem są publiczne zgłoszenia GitHuba.
- Ścieżki z sekcji `## Backlog` są już w publicznej historii the-way; usunięcie ich z drzewa tej historii nie zmienia.

## Questions carried to cycle

- Test sprawdza część zdania `outbound-link-reach` — ścieżki i linki do notatek — a linki do repozytoriów, których czytelnik bez logowania nie otworzy, dalej sprawdza tylko review; WAY-61 każe metodzie czytać `test` dopiero, gdy test sprawdza to, o czym jest zdanie, więc cykl wybiera, jak fundament zapisze nowe sprawdzenie, w granicach wiersza 3 *Settlements to record*.

## Human actions

- Mariusz zakłada `~/.the-way/locations.json` z pozycją `tasks` pod `the-way`, wskazującą jego plik zadań — before the cycle, done

## Decisions in play

Zadanie zmienia WAY-27, WAY-107 i niezmiennik `outbound-link-reach`: miejsce backlogu na dysku poza repozytorium nie stoi już w sekcji `## Backlog`, tylko w pliku lokalizacji, który sekcja wskazuje pozycją (pytania 1 i 4).

- WAY-27 — „Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the place of its tasks, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else.” Niezmiennik `outbound-link-reach`, który z niej wynika (metoda `review`): „No file git tracks contains a link into a repository that a reader not signed in to its host cannot open, or into a private note collection, other than a link in the `## Backlog` section of the root `AGENTS.md` to the place of the repository's tasks.”
- WAY-107 — „A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer owns. A project definition stands in the named project place; when the place is unnamed, the agent asks the human and offers to record the answer there.”
- WAY-309 — „[…] the orchestrator runs the-way's script that lists, with the file and the line of each, every absolute path (a drive letter, a home directory) and every note link written `[[...]]`, and corrects what it lists until it lists nothing. The script finds them by pattern, holds no list of private words and rewrites nothing. […]” Test z *To do* 4 szuka tym samym wzorcem w innym zbiorze plików.
- WAY-61 — „An invariant's method of checking reads `test` once a test of the product's test suite, written in the product's language and run by the command that runs the product's tests, cites it, and `review` until then, and it names no command and no script. A test checks what its invariant's sentence is about, as it stands on the commit being checked, so a test fed input made up for it is the method of a sentence about the check it exercises, never of one about the data that check reads.”
- WAY-140 — „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task. […]” Cykl tego zadania sam szuka backlogu przez sekcję `## Backlog`, którą zmienia.
- WAY-16 — „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.”

## Settlements to record

Candidates: 7 shown, 3 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Miejsce backlogu na dysku użytkownika poza repozytorium produkt wskazuje w sekcji `## Backlog` pozycją pliku lokalizacji, nigdy ścieżką bezwzględną; katalog w repozytorium albo adres publicznego trackera stoi w sekcji wprost, a gdy pliku albo pozycji brakuje, agent pyta człowieka i proponuje wpis tam, gdzie miejsce pasuje. Zmienia WAY-27 i WAY-107. | decision | pytania 1 i 4 | czy wyjątek WAY-27 dalej pozwala na ścieżkę w `## Backlog`, czy każde miejsce backlogu idzie do pliku i dokąd agent zapisuje brakujące miejsce |
| 2 | Plik lokalizacji leży w stałym miejscu `~/.the-way/locations.json`, bez zmiennej środowiskowej; jego klucze to nazwy repozytoriów, a pod każdym stoją pozycje po nazwie, np. `tasks` i `projects`. | decision | pytanie 1 | czy plik wskazuje zmienna środowiskowa, czy jest jeden na repozytorium, czy wspólny, i jak nazywa pozycje |
| 3 | Żaden plik śledzony przez git nie zawiera ścieżki bezwzględnej (litera dysku, katalog domowy) ani linku do notatki `[[...]]`, także w sekcji `## Backlog`; wyjątek mają tylko pliki z listy w teście, które z natury piszą przykładowe ścieżki. Zmienia niezmiennik `outbound-link-reach`. | invariant | pytania 1 i 2 | czy test zostawia wyjątek dla `## Backlog`, które pliki pomija i czy zostawia `outbound-link-reach` bez zmian |

## Out of scope

- Ścieżki, które już stoją w publicznej historii the-way.
- Sekcja `## Backlog` produktu `loop2`, która też podaje trzy ścieżki bezwzględne, w tym do rulebooka: to plik innego repozytorium; po domknięciu tego zadania dostaje analogiczne zadanie, które przeniesie ustalony tu sposób.
