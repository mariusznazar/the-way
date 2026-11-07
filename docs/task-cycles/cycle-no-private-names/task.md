---
title: "the way: cykl zadania nie publikuje prywatnych nazw w publicznej historii"
status: draft
created: 2026-11-01T12:00
updated: 2026-11-07
tags: [zadanie]
related: "the project note in the author's backlog"
---

## Po co to

- **Jak jest dziś:** Repozytorium the way jest publiczne, a cykl zadania przy otwieraniu requestu zapisuje cały swój zapis pracy, razem z kopią dokumentu zadania, w commicie, który po scaleniu zostaje w historii. Kopia z ostatniego zadania (PR #65) ma 8 linii z nazwą produktu i 1 ze ścieżką do vaulta.
- **Kto to odczuwa:** Mariusz — nazwy produktów, układ katalogów i ścieżki do prywatnych notatek stają się publiczne przy każdym zadaniu, choć nikt tego nie wybrał.
- **Co jeśli nic:** Każde kolejne zadanie dokłada swoje nazwy do publicznej historii. Czyszczenie pojedynczych dokumentów zależy od tego, czy ktoś o tym pamięta.

# the way: cykl zadania nie publikuje prywatnych nazw w publicznej historii

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykl zadania przy otwieraniu requestu kopiuje cały katalog zapisu pracy — zapis cyklu, kopię dokumentu zadania, przekazania i raporty etapów, tabelę kosztów — do `docs/task-cycles/<task-slug>/`, commituje kopię i zaraz potem jej usunięcie (`task-cycle/skill/SKILL.md:430-432`, `foundations` `52889bc`); commit z kopią po scaleniu zostaje w historii repozytorium.
- Oba repozytoria, w których dziś biegną cykle the way — the-way i `loop2` — są publiczne (`gh repo view`, 2026-11-07: `PUBLIC` dla obu).
- Prywatne ścieżki niesie nie tylko kopia dokumentu zadania: szablon zapisu każe wpisać w pierwszej linii bezwzględną ścieżkę źródła zadania (`task-cycle/record_template.md:3`, „Task source: <absolute path and approval date or source commit>”), a przekazania, raporty i uwagi procesowe podają bezwzględne ścieżki worktree na dysku Mariusza.
- Skala: 55 z 56 commitów z kopią zapisu w the-way i 58 z 58 w `loop2` zawiera ścieżkę do vaulta albo do katalogu użytkownika (przeszukanie `git grep` każdego commitu, który dodał pliki pod `docs/task-cycles/`, po nazwie katalogu vaulta i po początku ścieżki katalogu użytkownika, 2026-11-07).
- Zapis PR #65 (commit `93930e9`) niesie ścieżki do vaulta w zapisie cyklu, w kopii zadania i w przekazaniu projektanta, a w kopii zadania 7 linii z nazwą gałęzi i tagu prywatnej pracy w repozytorium `loop2`.
- Odbiorcą jest Mariusz: każdy cykl publikuje bez jego wyboru układ jego dysku, tytuły i ścieżki jego prywatnych notatek i nazwy jego prywatnych prac.

### To do

1. Przed każdym commitem, który dodaje zapis cyklu do repozytorium — kopią przy requeście, jej powtórzeniem w poprawce po review i kopią requestu zablokowanego z każdego powodu — orkiestrator czyści kopię: ścieżki bezwzględne zamienia na względne wobec repozytorium, a ścieżki i tytuły prywatnych notatek na opis tego, czym są; linia `Project relation:` kopii zadania zostaje bez zmian, bo po niej czytnik stanu planu wiąże zapis z zadaniem planu (pytanie 1).
2. the way dostaje skrypt, który przed każdym takim commitem sprawdza kopię zapisu, a przed każdą publikacją opisu requestu — opis, i wypisuje z miejscem każdą ścieżkę bezwzględną (litera dysku, katalog domowy) i każdy link do notatki w postaci `[[...]]`; orkiestrator poprawia to, co skrypt wypisał, i uruchamia go znowu, aż nic nie wypisze (pytania 2 i 3).

### Acceptance criteria

- Zapis cyklu tego zadania, w commicie, który go dodaje, i opis jego requestu przechodzą skrypt z punktu 2 z gałęzi zadania (pytanie 5).

### Questions to settle

- Pytanie 1: którą drogą cykl przestaje publikować prywatne nazwy — nie commituje zapisu wcale, commituje go oczyszczonego, czy rozróżnia repozytoria publiczne i prywatne?
  - Answer: cykl dalej commituje zapis, ale oczyszczony, w każdym repozytorium: przed commitem zamienia w kopii ścieżki bezwzględne na względne wobec repozytorium, a prywatne notatki opisuje zamiast wskazywać ich ścieżkę, a skrypt sprawdza kopię przed commitem. Wszyscy czterej czytelnicy zapisu z *Context* działają dalej. Słaby punkt przyjęty z tą drogą: jeden krok i jedno sprawdzenie więcej w każdym cyklu; opublikowana kopia zadania różni się od dokumentu w notatkach; skrypt rozpoznaje ścieżki po wzorcu, ale nazw prywatnych prac bez listy nie rozpozna (pytanie 2).
  - Not chosen:
    - cykl nie commituje zapisu wcale, zapis zostaje na dysku — czytnik stanu planu traci dowód wejścia w cykl i zrobienia (do przepisania jego kod, WAY-153 z inwariantem `project-plan-state-evidence` i szablon planu), nocny przegląd uwag musiałby czytać katalogi znikające z worktree, a link do zapisu w requeście znika;
    - oczyszczanie tylko w repozytoriach publicznych — dziś oba są publiczne, więc to samo co droga wybrana plus druga ścieżka, której żaden cykl nie przećwiczy; widoczność repozytorium zna tylko serwis, nie git, więc pytałby o nią agent, a jedna pomyłka publikuje wszystko.
  - Source: Mariusz, 2026-11-07: „b” — na pytanie „Którą drogę wybierasz: a, b czy c?”, przy drodze b, której słabość nazwano: nazw bez listy skrypt nie rozpozna.
- Pytanie 2: co jest „prywatne” — czego opublikowany zapis nie może zawierać i po czym sprawdzenie to pozna?
  - Answer: sprawdzenie łapie po wzorcu ścieżki bezwzględne (litera dysku, katalog domowy) i linki do notatek w postaci `[[...]]`, bez listy prywatnych słów. Powód: przeszukanie wszystkich 114 commitów z zapisem w the-way i `loop2` (2026-11-07) pokazało, że prawie wszystko, co wycieka, to ścieżki vaulta, nazwy katalogów worktree na dysku i tytuły notatek w linkach, które łapie wzorzec; poza ścieżkami zostają głównie nazwa kursu i numery jego lekcji, które fundament the-way już celowo podaje (`foundations/decisions.md`, 5 wystąpień na `foundations` `52889bc`), i numery spraw z prywatnego zeszytu przeglądu, które nic nie zdradzają. Słaby punkt przyjęty z tą drogą: naprawdę prywatna nazwa w zwykłym tekście przejdzie; listę można dodać osobnym zadaniem, gdy taka nazwa się pojawi.
  - Not chosen:
    - wzorce i lista prywatnych słów w pliku w katalogu domowym — przyjęte najpierw (Mariusz, 2026-11-07: „b”), odrzucone po przeszukaniu historii: na liście prawie nie byłoby czego wpisać, a kosztowałaby plik do pamiętania, działanie człowieka przed cyklem i kod, który dziś prawie nic nie złapie;
    - wzorce i lista w notatkach, której miejsce the way zna tylko przez zmienną środowiskową — koszty jak wyżej plus zmienna do ustawienia na każdej maszynie, a bez niej skrypt sprawdza same wzorce;
    - wzorce i ocena orkiestratora, który sam zamienia to, co uzna za prywatne — dodatkowe czytanie całego zapisu w każdym cyklu, pominięcie przechodzi po cichu, a nazwy publicznego i prywatnego repozytorium wyglądają w tekście tak samo.
  - Source: Mariusz, 2026-11-07: „ale w tym przypadku chyba faktycznie będzie wzorzec - a” — na pytanie „zostawiamy listę prywatnych słów czy z niej rezygnujemy?”, przy drodze a, której słabość nazwano: prywatna nazwa w zwykłym tekście przejdzie.
- Pytanie 3: czy reguła obejmuje też to, co cykl publikuje poza zapisem — opis requestu i wiadomości commitów?
  - Answer: obejmuje opis requestu, bez wiadomości commitów: sprawdzenie z pytania 2 przechodzi też opis przed każdą jego publikacją, także po dopisaniu linku do zapisu. Słaby punkt przyjęty z tą drogą: wiadomości commitów zostają bez sprawdzenia; dziś żadna wiadomość commitu the-way nie niesie prywatnej ścieżki.
  - Not chosen:
    - zapis, opis i wiadomości commitów gałęzi zadania przed pushem — znalezisko w wiadomości każe agentowi przepisać historię gałęzi przed pierwszym pushem, krok ryzykowny i płacony w każdym cyklu za problem, który dotąd nie wystąpił;
    - tylko zapis — opis requestu dalej może wyciec jak w PR #51, choć leży w katalogu, który sprawdzenie i tak czyta.
  - Source: Mariusz, 2026-11-07: „a” — na pytanie „Którą drogę wybierasz: a, b czy c?”, przy drodze a, której słabość nazwano: wiadomości commitów zostają bez sprawdzenia.
- Pytanie 4: czy zadanie czeka na własne wytyczne kodowania i testów the way, skoro cykl może zmienić skrypt (np. dopisać sprawdzenie zapisu) w repozytorium bez `guidelines/`?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way, a rozjazd reguły z praktyką zostaje w osobnym zadaniu o własnych wytycznych the way. Słaby punkt przyjęty z tą drogą: skrypt powstaje bez wytycznych kodowania i testów, jak dotychczasowe skrypty the way.
  - Not chosen:
    - czekać na zadanie o wytycznych — to zadanie nie ma jeszcze wybranego kierunku, a wycieki trwałyby do jego scalenia.
  - Source: Mariusz, 2026-11-07: „tak” — na propozycję agenta powtarzającą jego odpowiedź z doprecyzowania zadania o przeglądzie fundamentu („nadal jedziemy bez tego”, 2026-11-06).
- Pytanie 5: czy zapis cyklu tego zadania już przechodzi nowe sprawdzenie?
  - Answer: tak — orkiestrator przed commitem zapisu uruchamia skrypt z gałęzi zadania i czyści własny zapis, bo cykl zaczyna od reguł sprzed zmiany i bez tego opublikowałby ścieżkę dokumentu zadania i ścieżki worktree jak dotąd.
  - Source: Mariusz, 2026-11-07: „tak” — na propozycję agenta.

## Context

- Zapis w commicie czyta dziś czterech odbiorców: Mariusz przez link w requeście, po SHA commita, który dodaje zapis (`task-cycle/skill/SKILL.md:434-435`); czytnik stanu planu projektu, który z commita z zapisem dowodzi, że zadanie planu weszło w cykl, a z zapisu osiągalnego z gałęzi głównej — że jest zrobione, i czyta przy tym linię `Project relation:` kopii zadania (`project-level/plan_state.py:338-399`, WAY-153, inwariant `project-plan-state-evidence`); kolumna *Document* planu, która po zakończeniu zadania linkuje kopię zadania w tym commicie (`project-level/plan/template.md:88`); nocny przegląd uwag procesowych w prywatnych notatkach Mariusza, który wyszukuje commity z zapisem osiągalne z gałęzi głównej każdego repozytorium i czyta z nich uwagi.
- Opis requestu każe scalać tak, żeby commity przetrwały, „since the link to the record survives only then” (`task-cycle/skill/request_template.md:208`).
- Opisy requestów niosą prywatne ścieżki rzadko: z 40 ostatnich PR-ów the-way jeden (#51) podaje bezwzględne ścieżki worktree w kotwicach uwag; wiadomości commitów the-way żadnej (przeszukanie 2026-11-07).
- Szablon zapisu już każe usuwać z raportów sekrety i dane osobowe (`task-cycle/record_template.md:84`), o nazwach i ścieżkach prywatnych nie mówi nic.
- Fundament już traktuje repozytoria jako publiczne: WAY-288 pisze opis requestu po angielsku, bo „the repositories are public”, a WAY-301 nie pozwala, by opis tagu przeglądu podawał tytuły z prywatnych notatek.
- Ten dokument zadania sam trafi do zapisu swojego cyklu, więc podaje pliki the-way ścieżką względną, a prywatnych notatek nie wskazuje ścieżką.

## Questions carried to cycle

- Uwagi procesowe trzymają pozycje raportów słowo w słowo, a sprawdzenie WAY-294 porównuje je przed tym samym commitem; czyszczenie raportów i uwag musi dać w obu te same słowa — kolejność obu kroków wybiera cykl.

## Human actions

none

## Decisions in play

- WAY-27 — „Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the place of its tasks, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else.” Inwariant `outbound-link-reach`, który z niej wynika: „No file git tracks contains a link into a repository that a reader not signed in to its host cannot open, or into a private note collection, other than a link in the `## Backlog` section of the root `AGENTS.md` to the place of the repository's tasks.” Plik zapisu w commicie, który go dodaje, jest plikiem, który git śledzi.
- WAY-153 — „At each leading session's start a reader using git alone proposes plan state transitions only from evidence that ties a cycle trace to the plan's task, establishes the product's integration ref without guessing, changes no plan or task document and reports what it cannot establish.” Inwariant `project-plan-state-evidence`: czytnik proponuje przejście do in cycle „only from the task's working cycle directory in a worktree git lists or a commit of its archived cycle directory, and a move to done only from a cycle record reachable in the product's freshly fetched integration history, each tied to the task by its recorded provenance”. Oczyszczona kopia zachowuje tę provenance (punkt 1 *To do*).
- WAY-294 — „Before every commit that adds the cycle record to the product's repository, the orchestrator runs the-way's script that lists each item other than `none` under **Searches not found or unclear** in the record's stage reports that the record's process remarks do not hold word for word, appends each listed item word for word with its stage name and full report path, and runs the script again until it lists nothing. The commits that add the record are its copy for a request, the repetition of that copy in a correction after review, and the copy of a request blocked for any cause.” Nowe sprawdzenie biegnie przed tymi samymi commitami; uwagi podają dziś pełną ścieżkę raportu.
- WAY-288 — „A request's description is written in English, and its top part stands a second time, in the language of the task document, in a collapsed block of the description.” Blok po polsku jest częścią opisu, więc sprawdzenie z pytania 3 go obejmuje.

## Settlements to record

Candidates: 3 shown, 2 accepted — 2026-11-07

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Cykl w każdym repozytorium, publicznym i prywatnym, commituje zapis i publikuje opis requestu tylko oczyszczone: ścieżki bezwzględne zamienione na względne wobec repozytorium, prywatne notatki opisane zamiast wskazane; wiadomości commitów zostają bez sprawdzenia. | decision | pytania 1 i 3 | czy reguła dotyczy tylko repozytoriów publicznych i czy obejmuje opis requestu oraz wiadomości commitów |
| 2 | Przed każdym commitem z zapisem i przed każdą publikacją opisu skrypt wypisuje po wzorcu ścieżki bezwzględne i linki `[[...]]`, bez listy prywatnych słów. | decision | pytanie 2 | czy prywatne nazwy łapie wzorzec, lista czy ocena agenta |

## Out of scope

- To, co już stoi w historii the-way i `loop2`: usunięcie tego wymaga przepisania publicznej historii.
