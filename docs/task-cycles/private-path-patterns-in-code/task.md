---
title: "the way: sprawdzanie ścieżek prywatnych bez fałszywych trafień w kodzie i test plików śledzonych dla produktów"
status: draft
created: 2026-11-09T00:00
updated: 2026-11-10
tags: [zadanie]
related: "the project note of the process work"
---

## Po co to

- **Jak jest dziś:** the way ma skrypt `task-cycle/private_paths_check.py`, który wyszukuje w tekście ścieżki z dysku (litera dysku, katalog domowy) i linki do notatek Obsidiana w postaci `[[...]]`. Powstał do sprawdzania tekstu, który cykl zadania publikuje — zapisu cyklu i opisu PR-a — więc jego wzorce są ułożone pod prozę. Od zadania o pliku lokalizacji (WAY-320, PR #92) the way puszcza go też na każdy plik śledzony przez git, ale tylko we własnym repozytorium. Uruchomiony 2026-11-09 na plikach loop2 dał, oprócz dziewięciu prawdziwych ścieżek, 79 fałszywych trafień.
- **Kto to odczuwa:** każdy produkt na the way, który chciałby pilnować testem, żeby ścieżka z dysku nie weszła do repozytorium — dziś pierwszy jest loop2. Przez niego Mariusz: ostatnia ścieżka weszła do loop2 2026-11-06 mimo przeglądu.
- **Co jeśli nic:** produkt albo nie ma takiego testu i ścieżki wchodzą, albo pisze własny z listą wyjątków na fałszywe trafienia, która łata słabość skryptu the way i przepuszcza prawdziwą ścieżkę w plikach z listy. Zadanie loop2 o przeniesieniu ścieżek do pliku lokalizacji czeka na to zadanie, bo Mariusz nie chce dublować pracy.

# the way: sprawdzanie ścieżek prywatnych bez fałszywych trafień w kodzie i test plików śledzonych dla produktów

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skrypt `task-cycle/private_paths_check.py` the way szuka ścieżek bezwzględnych i linków do notatek wzorcem ułożonym pod prozę, więc w kodzie daje fałszywe trafienia.
- Pomiar z 2026-11-09 — skrypt z `foundations` `f238e4f` (bez zmian do `73b51db`) na każdym pliku śledzonym loop2 (`2fe922c`) — wypisał 88 miejsc: 9 prawdziwych ścieżek, 1 celowy przykład ścieżki Git Basha i 78 fałszywych trafień.
- 73 z 78 fałszywych trafień to „linki” `[[...]]`: 70 tablic w tablicy w kodzie JavaScriptu, TypeScriptu i Pythona (np. `[ [address, addressProblem(address.value)]]`), 1 klasa znaków basha `[ [:space:]]` w skrypcie bez rozszerzenia `deploy/loop2-deploy:260` i 2 zapisy slotu ze specyfikacji HTML `p.[[PromiseResult]]` w cytacie w pliku Markdown `foundations/environment_facts.md:614`.
- 5 z 78 to „ścieżki”, które są sekwencjami w napisie albo w wyrażeniu regularnym: 4 razy `s<colon>\n` (np. `f"... within {SERVE_WAIT} s<colon>\n"`) i raz `d<colon>\d\d` z `\d\d<colon>\d\d`.
- Test plików śledzonych `task-cycle/test_tracked_files_private_paths.py` pilnuje tylko repozytorium the way, z listą czterech plików, które z natury piszą przykładowe ścieżki; produkt nie ma jak go uruchomić u siebie.
- Odbiorcą jest każdy produkt na the way, który chce pilnować testem, żeby ścieżka z dysku nie weszła do jego plików; pierwszy jest loop2, którego zadanie o pliku lokalizacji czeka na to zadanie (jego pytanie 3).

### To do

1. Przy sprawdzaniu plików śledzonych skrypt szuka linków `[[...]]` tylko w plikach `.md`; w kopii zapisu cyklu i w opisie requestu szuka ich we wszystkich plikach, jak dziś (pytanie 1).
2. Skrypt nie bierze za link do notatki `[[...]]` przyklejonego z lewej do litery, cyfry, kropki albo podkreślnika (`p.[[PromiseResult]]`), w każdym sprawdzeniu (pytanie 2).
3. Skrypt nie bierze za początek dysku litery poprzedzonej backslashem (`\d\d<colon>\d\d`) ani za ścieżkę trafienia, którego cała treść po `X:` to same sekwencje `\n`, `\t` albo `\r` (`s<colon>\n`) (pytanie 3).
4. the way daje komendę w `.the-way/task-cycle/`, która sprawdza pliki śledzone repozytorium, w którym ją uruchomiono, i pomija pliki, które nazywa zdanie niezmiennika wskazanego jej argumentem (pytanie 4).
5. Test plików śledzonych the way woła tę komendę z niezmiennikiem `tracked-file-private-paths` i nie trzyma własnej kopii listy czterech plików; dalej przechodzi.
6. Instrukcja instalacji the way (`installation/README.md`) mówi, że produkt, którego repozytorium jest publiczne, dołącza to sprawdzenie, i jak: niezmiennik z listą plików z przykładowymi ścieżkami i metodą `test` oraz krótki test `test_*.py`, który woła komendę i cytuje ten niezmiennik.

### Acceptance criteria

- Reguły sprawdzenia plików śledzonych z punktów 1–3, przyłożone do plików śledzonych loop2 `2fe922c` bez pomijania żadnego pliku, wypisują dokładnie 10 miejsc: 9 prawdziwych ścieżek i przykład Git Basha `tests/deploy/deploy_script_support.py:130`.
- Prawdziwa ścieżka z dysku w napisie w kodzie (np. `"C<colon>\new\dir"` w pliku `.py`) jest dalej wypisywana.

### Questions to settle

- Pytanie 1: w jakich plikach skrypt dalej sprawdza linki `[[...]]`?
  - Answer: przy sprawdzaniu plików śledzonych — tylko w plikach `.md`; w kopii zapisu cyklu i w opisie requestu — we wszystkich plikach, jak dziś. WAY-309 zostaje bez zmian; WAY-320 i zdanie niezmiennika `tracked-file-private-paths` liczą link do notatki tylko w pliku Markdown.
  - Not chosen:
    - linki tylko w `.md` wszędzie, także w kopii zapisu i opisie requestu — link do notatki w raporcie `.txt` czy `.jsonl` kopii zapisu przechodzi, a agent cytujący dokument zadania przenosi do raportu jego linki; zmienia też WAY-309;
    - linki wszędzie poza plikami kodu rozpoznawanymi po rozszerzeniu — lista rozszerzeń do dopisywania przy każdym nowym języku produktu, a skrypt bez rozszerzenia (`deploy/loop2-deploy` z `[ [:space:]]`) dalej trafia;
    - bez zmiany — 73 fałszywe trafienia w loop2 i lista wyjątków na około 40 plików.
  - Source: Mariusz, 2026-11-09: „B” — na pytanie „w jakich plikach skrypt dalej sprawdza linki `[[...]]`?” z drogami A (tylko `.md` wszędzie), B (tylko `.md` przy plikach śledzonych, wszędzie w kopii zapisu i opisie requestu), C (wszędzie poza plikami kodu po rozszerzeniu).
- Pytanie 2: co z zapisem `p.[[PromiseResult]]` w cytacie specyfikacji w pliku Markdown loop2?
  - Answer: `[[...]]` przyklejony z lewej do litery, cyfry, kropki albo podkreślnika nie jest linkiem do notatki (`p.[[PromiseResult]]`, `a[[0]]`), w każdym sprawdzeniu, także w kopii zapisu cyklu. Przepuszczony zostaje link Obsidiana przyklejony do słowa bez spacji (`zob.[[Notatka]]`), który Obsidian renderuje jako link.
  - Not chosen:
    - loop2 wpisuje `foundations/environment_facts.md` na swoją listę pomijanych plików — każda prawdziwa ścieżka w tym rosnącym pliku fundamentu przechodzi;
    - bez zmiany — test loop2 nie przechodzi, dopóki fakt stoi w fundamencie, a cytatu nie można przepisać, bo fakt środowiskowy cytuje źródło słowo w słowo.
  - Source: Mariusz, 2026-11-09: „A” — na pytanie „co z zapisem `p.[[PromiseResult]]` w cytacie specyfikacji w pliku Markdown loop2?” z drogami A (link przyklejony do litery, cyfry, kropki albo podkreślnika nie jest linkiem) i B (plik na liście loop2).
- Pytanie 3: po czym skrypt rozpoznaje, że `s<colon>\n` i `\d\d<colon>\d\d` to nie ścieżka, i jaką prawdziwą ścieżkę przy tym przepuszcza?
  - Answer: dwiema wąskimi regułami: litera poprzedzona backslashem nie zaczyna dysku (`\d\d<colon>\d\d`), a trafienie, którego cała treść po `X:` to same sekwencje `\n`, `\t` albo `\r` (`s<colon>\n`, `s<colon>\n\n`), nie jest ścieżką. Przepuszczone zostają prawdziwe `C<colon>\n`, `C<colon>\t` i `C<colon>\r` stojące same — katalog o jednoliterowej nazwie w korzeniu dysku; `C<colon>\new\dir` i `C<colon>\n\dir` są dalej wypisywane. Tekst przyklejony do sekwencji (`"... s<colon>\nWynik"`) dalej daje fałszywe trafienie, które produkt usuwa, przepisując napis.
  - Not chosen:
    - mała litera dysku w pliku kodu nie zaczyna ścieżki — przepuszcza każdą ścieżkę pisaną małą literą, także katalog domowy `c<colon>\Users<backslash>...`, w formie, w jakiej wypisują ją niektóre narzędzia;
    - rozpoznawanie napisów i wyrażeń regularnych osobno dla każdego języka — parser na każdy język, który produkt doda, nieproporcjonalny do pięciu linii;
    - bez zmiany — loop2 przepisuje pięć napisów, a każdy przyszły komunikat w tej formie trafia znowu, albo wpisuje pliki na listę i prawdziwa ścieżka w nich przechodzi.
  - Source: Mariusz, 2026-11-09: „A” — na pytanie „po czym skrypt rozpoznaje, że `s<colon>\n` i `\d\d<colon>\d\d` to nie ścieżka, i jaką prawdziwą ścieżkę przy tym przepuszcza?” z drogami A (dwie wąskie reguły), B (mała litera dysku w kodzie), C (rozpoznawanie napisów per język).
- Pytanie 4: jak sprawdzenie plików śledzonych trafia do produktu i gdzie produkt trzyma listę plików z przykładowymi ścieżkami?
  - Answer: the way daje komendę w `.the-way/task-cycle/`, która sprawdza pliki śledzone repozytorium, w którym ją uruchomiono, a listę pominiętych plików czyta ze zdania niezmiennika produktu, który wskazuje jej argument. Produkt, który chce sprawdzenia, zapisuje taki niezmiennik z metodą `test` i krótki test `test_*.py`, który woła komendę i cytuje niezmiennik; `run_tests.py` znajduje ten test sam, a `foundation_check.py` zgłasza niezmiennik, którego żaden test nie cytuje (WAY-321). Test plików śledzonych the way woła tę samą komendę, bez własnej kopii listy. Instrukcja instalacji mówi, że produkt, którego repozytorium jest publiczne, dołącza to sprawdzenie. Słaby punkt przyjęty z tą drogą: publiczny produkt, który nie przeczyta instrukcji instalacji, nie ma sprawdzenia i nic o tym nie mówi — koszt, z powodu którego WAY-321 odrzuciła tryb dopisywany przez produkt do jego komendy testów.
  - Not chosen:
    - instalator kopiuje plik testu do produktu — kopia rozjeżdża się z the way (WAY-34 odrzuca kopie skryptów w produktach), przepisywana przy przesunięciu przypięcia poszerza obietnicę instalatora, a lista nie może stać w pliku, który instalator nadpisuje;
    - `foundation_check.py` sprawdza pliki śledzone każdego produktu zawsze, z listą z niezmiennika produktu, jeśli go ma — sprawdzenie formy fundamentu dostaje obcą robotę, wzorce trzeba przenieść do `elements-common`, a każdy produkt, także prywatny, ma po przesunięciu przypięcia czerwone testy, dopóki nie usunie albo nie wpisze swoich ścieżek;
    - bez zmiany — loop2 pisze test na funkcjach z `.the-way`, których the way nie obiecuje utrzymać, i test pęka albo zmienia to, co znajduje, przy przesunięciu przypięcia;
    - instrukcja instalacji mówi „produkt, który chce, dołącza” — publiczny produkt, który o tym nie pomyśli, zostaje bez sprawdzenia, jak loop2 przed ścieżką z 2026-11-06.
  - Source: Mariusz, 2026-11-09: „C” — na pytanie „Jak sprawdzenie plików śledzonych trafia do produktu i gdzie produkt trzyma listę plików z przykładowymi ścieżkami?”, z rekomendacją „C z listą w niezmienniku produktu i zdaniem w instrukcji instalacji ‚produkt, którego repozytorium jest publiczne, dołącza’”, po krytyce propozycji przez niezależnego agenta.
- Pytanie 5: czy zadanie czeka na własne wytyczne kodowania i testów the way, skoro repozytorium the way nie ma `guidelines/`, a WAY-215 trzyma w doprecyzowaniu zadanie piszące kod albo testy w produkcie bez wytycznych?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way, a rozjazd reguły z praktyką zostaje w zadaniu another task in the author's backlog (the-way's own guidelines).
  - Not chosen:
    - czekać na zadanie o wytycznych the way — to zadanie nie ma jeszcze kierunku, więc poprawki stałyby bez terminu, a z nimi zadanie loop2, które czeka na to zadanie.
  - Source: Mariusz, 2026-11-10: „nie czeka i przenosimy” — na pytanie, czy zadanie czeka na wytyczne the way i czy przenieść odpowiedź z pytania 6 zadania another task in the author's backlog (the batch task on the cycle, technology and decisions), tam przeniesionej z pytania 4 zadania another task in the author's backlog (the batch task on skills and guidelines): Mariusz, 2026-11-07: „nie czeka”; WAY-215 `foundations/decisions.md:6320`, `foundations` `73b51db`.

## Context

- Wzorce skryptu: `task-cycle/private_paths_check.py:56` (litera dysku) i `:63` (link `[[...]]`) na `73b51db`; opis na górze pliku mówi, co dziś uznaje za ścieżkę i za link.
- Test plików śledzonych the way: `task-cycle/test_tracked_files_private_paths.py` na `73b51db` — lista czterech plików w `:32`, funkcje `tracked_files` (`:41`) i `findings` (`:48`), test, że lista zgadza się ze zdaniem niezmiennika `tracked-file-private-paths`.
- Cykl zadania uruchamia skrypt na kopii zapisu cyklu, `docs/task-cycles/<task-slug>` (`task-cycle/skill/SKILL.md:541` na `73b51db`), i na opisie requestu; kopia zapisu trzyma nie tylko pliki `.md` — w historii the way pliki zapisów cykli to m.in. 3202 `.md`, 2898 `.txt`, 242 `.log`, 208 `.json` i 154 `.jsonl` (odczyt `git log --all` 2026-11-09).
- loop2 uruchamia już skrypty the way swoją jedną komendą testów: `scripts/test.py` w loop2 (`2fe922c`) woła `.the-way/gate/run_tests.py`, który uruchamia testy `test_*.py` śledzone przez git loop2 — bez testów the way, bo submoduł `.the-way` jest dla gita loop2 jednym wpisem (`gate/run_tests.py:65` na `73b51db`) — i `.the-way/elements/common/foundation_check.py`.
- Repozytorium loop2 jest publiczne (zadanie loop2, *Need*).
- Instrukcja instalacji mówi dziś, że instalator nie zmienia testów produktu, a produkt sam dopisuje `foundation_check.py` do swojej jednej komendy testów (`installation/README.md:71` na `73b51db`).
- Szóste fałszywe trafienie z notatki, `/c<slash>...` w `tests/deploy/deploy_script_support.py:130` loop2, to celowy przykład ścieżki Git Basha w opisie funkcji; skrypt wypisuje je słusznie, a loop2 obsłuży je swoją listą plików, jak the way swoje cztery pliki.
- Próba reguł z pytań 1–3 (link sprawdzany tylko w `.md` przy sprawdzaniu plików śledzonych, link przyklejony do litery albo kropki pominięty, sekwencje pominięte) na loop2 `2fe922c` dała 10 miejsc z kryterium akceptacji, a na the way `f238e4f` trafienia tylko w trzech plikach z jego listy czterech (próba w katalogu tymczasowym sesji, bez zmian w repozytoriach).
- Zadanie loop2, które na to czeka: „loop2: ścieżki z sekcji Backlog przenieść do pliku ~/.the-way/locations.json” w `_zadania` projektu „(P) Loop”, pytanie 3 i punkt 7 *To do*.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-309 — How does the cycle find the private paths and notes in what it publishes? (`foundations/decisions.md:9870` na `73b51db`): „[…] the orchestrator runs the-way's script that lists, with the file and the line of each, every absolute path (a drive letter, a home directory) and every note link written `[[...]]`, and corrects what it lists until it lists nothing. The script finds them by pattern, holds no list of private words and rewrites nothing. […]”
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name? (`foundations/decisions.md:10280` na `73b51db`): „[…] No file the repository tracks holds an absolute path or a note link, other than the files that the invariant `tracked-file-private-paths` names, which write example paths in order to find or to test them; a file that points to such a place names its entry in the locations file.”
  - Zmiana, którą zadanie wnosi (pytanie 1): link do notatki liczy się w pliku śledzonym tylko w pliku Markdown; ścieżka bezwzględna — w każdym pliku, jak dziś.
- WAY-16 — How are the checks of invariants run? (`foundations/decisions.md:466` na `73b51db`): „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.”
- WAY-321 — When does the check of a foundation report an invariant that reads `test` and has no test citing it? (`foundations/decisions.md:10333` na `73b51db`): „`elements/common/foundation_check.py` reports an invariant whose method reads `test` and which no line `invariant: <identifier>` in a file git tracks other than Markdown cites, in every run but the one made right after an entry is written […]. The one command that runs a product's tests runs the script without that switch (WAY-16).” Odrzucona tam droga („a separate mode of the script that a product adds to its own command of tests — […] a product that does not add it has no check and nothing says so”) to kształt drogi wybranej w pytaniu 4; zadanie przyjmuje ten koszt dla produktu, który niezmiennika nie zapisze, bo sprawdzenie nie wiąże każdego produktu.
- WAY-34 — Which version of the process does a product use? (`foundations/decisions.md:908` na `73b51db`): „A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit. […]”
- Niezmiennik `tracked-file-private-paths` (`foundations/invariants.md:86` na `73b51db`): „No file git tracks, other than `task-cycle/private_paths_check.py`, `task-cycle/test_private_paths_check.py`, `instruction-files/check_instructions.py` and `instruction-files/test_check_instructions.py`, contains an absolute path or a note link as WAY-309 names them.”
  - Zmiana, którą zadanie wnosi (pytanie 1): zdanie liczy link do notatki tylko w pliku Markdown, jak zmieniona WAY-320.

## Settlements to record

Candidates: 7 shown, 3 accepted — 2026-11-10

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Przy sprawdzaniu plików śledzonych link do notatki `[[...]]` liczy się tylko w pliku Markdown, a w kopii zapisu cyklu i w opisie requestu — w każdym pliku. Zmienia WAY-320 i niezmiennik `tracked-file-private-paths`. | decision | pytanie 1 | czy zmienić tylko WAY-320 i niezmiennik, czy też WAY-309, i czy link w raporcie `.txt` kopii zapisu dalej się liczy |
| 2 | `[[...]]` przyklejony z lewej do litery, cyfry, kropki albo podkreślnika nie jest linkiem do notatki; litera poprzedzona backslashem nie zaczyna dysku; trafienie, którego cała treść po `X:` to same sekwencje `\n`, `\t` albo `\r`, nie jest ścieżką. | decision | pytania 2 i 3 | czy zapisać te reguły z odrzuconymi drogami (mała litera dysku, rozpoznawanie napisów per język, plik na liście produktu) w decyzji, czy tylko w opisie skryptu, skąd następne zadanie nie dowie się, że te drogi już odrzucono |
| 3 | the way daje produktom komendę, która sprawdza pliki śledzone repozytorium, w którym ją uruchomiono, i pomija pliki nazwane w zdaniu niezmiennika produktu; produkt, którego repozytorium jest publiczne, dołącza ją niezmiennikiem z metodą `test` i krótkim testem `test_*.py`, który ją woła. | decision | pytanie 4 | czy kopiować test do produktu, wpiąć sprawdzenie w `foundation_check.py`, czy dać komendę; gdzie stoi lista produktu; czy sprawdzenie jest obowiązkowe; jak decyzja odnosi się do drogi odrzuconej w WAY-321 |

## Out of scope

- Jakakolwiek zmiana w loop2 — jego zadanie o pliku lokalizacji dołącza sprawdzenie i usuwa ścieżki osobno.
