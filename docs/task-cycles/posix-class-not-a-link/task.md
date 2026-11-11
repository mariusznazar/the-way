---
title: "the way: kontrola ścieżek prywatnych nie ma zgłaszać klasy znaków POSIX w podwójnych nawiasach jako linku do notatki"
status: draft
created: 2026-11-11T21:00
updated: 2026-11-11
tags: [zadanie]
related: "the project note of the author's backlog"
---

# the way: kontrola ścieżek prywatnych nie ma zgłaszać klasy znaków POSIX w podwójnych nawiasach jako linku do notatki

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skrypt `task-cycle/private_paths_check.py` zgłasza jako link do notatki każdy tekst `[[...]]`, który ma literę lub cyfrę, z wyjątkami, które daje WAY-323; klasa znaków POSIX zapisana w podwójnych nawiasach (`[[:space:]]`, `[[:alpha:]]`) wśród tych wyjątków nie stoi.
- Sprawdzone 2026-11-11 na `e1726b7`: próbka Markdown z wierszem `grep -v -E "^[[:space:]]*#" "$file"` i z `[[:alpha:]]` daje te dwa teksty na liście obok prawdziwych linków `[ [Notatka] ]` i `[ [(P) Loop] ]`, a `[^[:space:]]` (jeden nawias przed klasą) nie.
- Klasa stoi w poleceniach powłoki zapisanych w plikach Markdown: kontrola uruchomiona w loop2 (przypięcie `e3825a8`, gałąź zadania o miejscach z dysku) zgłasza 12 takich trafień, wszystkie to ta klasa i nic innego.

### To do

1. Przestać zgłaszać jako link do notatki klasę znaków POSIX zapisaną w podwójnych nawiasach, `[ [:nazwa:] ]`, we wszystkich sprawdzeniach, w których skrypt szuka linku (kopia zapisu cyklu, opis requestu, pliki śledzone).
    - nazwy, które wyjątek obejmuje: `alnum`, `alpha`, `blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`
    - tekst `[[:` z inną nazwą w środku jest dalej zgłaszany
2. Dalej zgłaszać każdy prawdziwy link do notatki i każdą ścieżkę, także w wierszu, w którym stoi taka klasa.

### Questions to settle

- Pytanie 1: jak wąski ma być wyjątek dla `[[:...:]]`?
  - Answer: tylko nazwy klas POSIX (`alnum`, `alpha`, `blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`) zapisane jako `[ [:nazwa:] ]`; prawdziwy link do notatki dalej jest zgłaszany.
  - Not chosen:
    - każdy tekst `[[:...:]]` — jedna reguła bez listy nazw, ale przepuści link do notatki zatytułowanej `:coś:`;
    - każdy `[ [`, po którym nie stoi litera ani cyfra — ucina też prawdziwe linki, np. `[[(P) Loop] ]`, które w vaulcie istnieją.
  - Source: Mariusz, 2026-11-11: „A” — na pytanie „Którą ścieżkę wybierasz: A, B czy inną?”; koszt lewej strony A (lista dwunastu nazw do utrzymania, nowa klasa w powłoce wymaga dopisania) podany w pytaniu.
- Pytanie 2: czy wyjątek obowiązuje wszędzie, gdzie skrypt sprawdza link (kopia zapisu cyklu, opis requestu, pliki śledzone), czy tylko w kontroli plików śledzonych?
  - Answer: wyjątek stoi we wspólnej liście wzorców skryptu, więc obowiązuje wszędzie, gdzie skrypt sprawdza link: w kopii zapisu cyklu, w opisie requestu i w plikach śledzonych.
  - Not chosen:
    - wyjątek tylko w kontroli plików śledzonych — dwa zestawy reguł do pilnowania i opisywania osobno, a cykl, który cytuje takie polecenie, dalej przepisuje je słowami w kopii zapisu, jak w cyklu loop2.
  - Source: Mariusz, 2026-11-11: „X” — na pytanie „Którą ścieżkę wybierasz: X, Y czy inną?”.
- Pytanie 3: czy zadanie, które zmienia skrypt i jego test w the way, czeka na wytyczne kodowania i testów the way?
  - Answer: nie — PR #98 jest scalony, a WAY-328 zapisuje odejście the way od własnych wytycznych kodowania i testów w części `task-cycle` (oraz w pozostałych częściach mapy), więc zadanie na wytyczne nie czeka.
  - Source: `foundations/decisions.md:10759` na `e1726b7` (WAY-328, *Scope* zawiera `task-cycle`); Mariusz, 2026-11-11: „98 zostało zmergowane”; wcześniej, na `5b20e75`, w the way nie było `guidelines/` ani decyzji o odejściu.

## Context

- Źródło: request https://github.com/mariusznazar/loop2/pull/76 (zablokowany draft) i zapis cyklu zadania „miejsca z dysku Mariusza z plików repozytorium do pliku lokalizacji” w commicie `89b2fb4` repozytorium loop2, `docs/task-cycles/lokalizacje-poza-repozytorium/`.
- Skutek w loop2: nowy test plików śledzonych, który bierze kontrolę z the way, jest czerwony na tych 12 liniach, więc loop2 oznaczyło swój niezmiennik `Violated: yes`, a test jako oczekiwane niepowodzenie; request czeka na decyzję (PR #76 w loop2).
- Zadanie loop2 zabrania własnych wyjątków dla fałszywych trafień i zabrania przesuwania przypięcia, więc poprawka musi wyjść z the way.
- Trafienia w loop2 stoją w `.claude/skills/loop2-deploy/references/backup_and_restore.md` i jego kopii `.agents/skills/loop2-deploy/references/backup_and_restore.md` (linie 211 i 224 w każdej) oraz w `foundations/environment_facts.md` (linie 39 i 52), który cytuje skrypt wdrożeniowy słowo w słowo, więc cytatu nie da się przeredagować.
- Poprzednia zmiana tych samych wzorców: PR #95 the way (`task/private-path-patterns-in-code`, commit `287a027`), z WAY-323 i WAY-324.
- Uzasadnienie WAY-323 liczy „a character class of the shell” wśród 78 tekstów, które próba z 2026-11-09 uznała za fałszywe trafienia; po regule „link tylko w pliku Markdown” klasa w kodzie przestała być zgłaszana, a w Markdownie reguła jej nie obejmuje.
- Kontrola czyta też kopię zapisu cyklu i opis requestu; w cyklu loop2 klasa w cytowanym poleceniu musiała być przepisana słowami w kopii zapisu, żeby kontrola przeszła.
- Dalej po stronie loop2, poza tym zadaniem: przesunięcie przypięcia `.the-way`, zdjęcie oczekiwanego niepowodzenia z testu i `Violated: no` na niezmienniku `tracked-file-private-paths`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-323 — „The script of WAY-309 takes no `[[...]]` for a note link when its first bracket stands against a letter, a digit, a dot or an underscore on its left, and no letter for the start of a drive when a backslash stands before it. It takes no text for an absolute path when all that follows the drive letter and its colon is escape sequences of a newline, a tab or a carriage return (`\n`, `\t`, `\r`), so a message ending in a letter, a colon and such a sequence is not listed; a path written with a real name, a Git Bash path, a link after a space or a mark and a text stuck to such a sequence stay listed.” (`foundations/decisions.md:10549` na `e1726b7`) — zadanie dopisuje do niego wyjątek dla klasy znaków POSIX, dwanaście nazw, wspólny dla wszystkich sprawdzeń linku (pytania 1 i 2).
- WAY-328 — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.” (`foundations/decisions.md:10759` na `e1726b7`) — zadanie zmienia skrypt i test w części `task-cycle`, którą ta decyzja obejmuje; zmiany w niej nie robi.

## Settlements to record

Candidates: 1 shown, 1 accepted — 2026-11-11

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Skrypt kontroli ścieżek prywatnych nie zgłasza jako linku do notatki klasy znaków POSIX zapisanej `[ [:nazwa:] ]` z dwunastu nazw (`alnum`, `alpha`, `blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`), a wyjątek stoi we wspólnej liście wzorców, więc obowiązuje w kopii zapisu cyklu, w opisie requestu i w plikach śledzonych; każdy inny `[[...]]` z literą lub cyfrą dalej jest zgłaszany. | decision | pytania 1 i 2 (wybór człowieka między pokazanymi drogami; zmienia WAY-323) | czy wyjątek obejmuje dwanaście nazw, czy każdy tekst `[[:...:]]`, i czy stoi we wspólnej liście wzorców, czy tylko w kontroli plików śledzonych |

## Out of scope

- Przesunięcie przypięcia `.the-way` w loop2 i zdjęcie oczekiwanego niepowodzenia z testu loop2.
