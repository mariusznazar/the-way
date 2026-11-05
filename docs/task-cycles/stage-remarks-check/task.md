---
title: "the way: braki zgłoszone przez etapy, które pracują pod koniec cyklu, trafiają do zapisu cyklu tak jak braki z wcześniejszych etapów"
status: draft
created: 2026-11-05T21:08
updated: 2026-11-05
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Skrypt the way sprawdza przed każdym zapisaniem archiwum cyklu, że każda pozycja „Searches not found or unclear” z raportów etapów stoi w uwagach procesowych zapisu cyklu

Status: ready for cycle
Project relation: independent

## Description

### Need

- Od WAY-260 raport każdego etapu cyklu zadania ma sekcję **Searches not found or unclear**, a orkiestrator przepisuje każdą jej pozycję poza `none` słowo w słowo do *Process remarks on the-way* zapisu cyklu (`task-cycle/skill/SKILL.md:71-72` na `61c72fb`).
- Nocny przegląd cykli (`ai-review`) robi sprawy usprawnień the way tylko z uwag zapisanych w zapisie cyklu; raportów etapów nie czyta nikt, więc pozycja, której orkiestrator nie przepisał, nie staje się sprawą i Mariusz, usprawniając the way, jej nie zobaczy.
- Według pomiaru Mariusza z 5.11 pozycji brakuje w 4 z 7 sprawdzonych cykli `loop2`; liczone skryptem z grubsza, dokładne liczby nie są ustalone.
- W trzech archiwach sprawdzonych przy doprecyzowaniu brakuje pozycji z etapów, które pracowały po otwarciu requestu: uzgodnienia z nowym `main` i jego recenzji w `reset-hasla` oraz korekty 2 w `kopia-bazy` (Context).
- Brakuje też pozycji z etapów, które pracowały przed wypełnieniem uwag: kroku powrotu w `plomyk` i poprawki kawałka 6 w `kopia-bazy`; obie pozycje stoją w sekcji obok wierszy mówiących „none” (Context).

### To do

1. The way dostaje skrypt, który dla katalogu zapisu cyklu czyta sekcję **Searches not found or unclear** każdego raportu w `reports/` — w obu formach, w jakich raporty ją dziś mają: nagłówek `## Searches not found or unclear` albo pogrubiona etykieta w wierszu — i wymienia każdą pozycję poza `none`, której uwagi procesowe zapisu nie zawierają słowo w słowo, ze ścieżką jej raportu; czy skrypt sam wpisuje te pozycje do bloku uwag, wybiera cykl.
2. Orkiestrator uruchamia skrypt przed każdym commitem, który dodaje zapis cyklu do `docs/task-cycles/<task-slug>/` — w kroku 12, w jego powtórce przy korekcie po uwagach człowieka (`task-cycle/skill/correction.md`) i w wariantach zablokowanego requestu — dopisuje do uwag każdą pozycję, którą skrypt wymienił, słowo w słowo, z nazwą etapu i pełną ścieżką raportu, i uruchamia skrypt ponownie, aż nie wymieni żadnej. Zgłoszenie, które orkiestrator uważa za błąd skryptu, nie zatrzymuje archiwum i nie jest poprawiane w skrypcie w tym cyklu: orkiestrator zapisuje archiwum, wpisuje przypadek do uwag procesowych i stawia go w opisie requestu w części do decyzji człowieka, tak jak przy `task-cycle/request_check.py`.
3. Szablon zapisu cyklu (`task-cycle/record_template.md`) ustala jedną formę bloku uwag procesowych, którą czyta skrypt z punktu 1; zapis cyklu trzyma uwagi tylko w tej formie, nie w osobnej sekcji ani w osobnym pliku.

### Acceptance criteria

- Blok uwag w ustalonej formie stoi tam, skąd wycina go `cycle_remarks_digest.py` — w punkcie zaczynającym się od „Process remarks” albo w wierszach wciętych pod nim głębiej niż jego znacznik listy.
- Uruchomiony na zapisach `plomyk` (`loop2@31ac651`), `reset-hasla` (`loop2@b311814`) i `kopia-bazy` (`loop2@d79c8e4`) skrypt wymienia jako brakującą każdą z pozycji opisanych w *Context*: kroku powrotu w `plomyk`, uzgodnienia i jego recenzji w `reset-hasla`, poprawki kawałka 6 i korekty 2 w `kopia-bazy`.

### Questions to settle

- Jak cykl ma zapewnić, że do uwag procesowych trafia każda pozycja każdego raportu — także z etapów po otwarciu requestu i także pozycja stojąca obok wierszy „none”?
  - Answer: skrypt the way uruchamiany przed każdym zapisaniem archiwum zapisu cyklu wyciąga pozycje sekcji **Searches not found or unclear** z każdego raportu w `reports/` i zgłasza te, których brakuje w uwagach; czy skrypt tylko zgłasza, czy sam wypisuje blok, wybiera cykl.
  - Not chosen:
    - Orkiestrator dopisuje pozycje do uwag zaraz po każdym raporcie, korekta też — kilka zdań w skillu cyklu i w `correction.md`, ale nie zamyka braków pozycji stojących obok wierszy „none”, które powstały, gdy orkiestrator miał raport przed sobą.
    - Obowiązkowe przejście orkiestratora przez wszystkie raporty przed każdym zapisaniem archiwum, z regułą, że pomija się tylko sekcję, która w całości brzmi `none` — kilka zdań, zamyka obie przyczyny, ale dalej opiera się na uważnym czytaniu przez model, które już zawiodło (38 raportów w `reset-hasla`).
  - Source: Mariusz, 2026-11-05: „C”, na pytanie z trzema drogami; słabe punkty nazwane przy C: nowy skrypt z testami i dłuższy cykl, rozpoznanie sekcji w dwóch formach raportów, stała forma bloku uwag, dosłowne „poza `none`” — wiersze typu „A source outside the product…: none found.” trafią do uwag i nocny przegląd dostanie więcej szumu.
- Czy w tym samym zadaniu ujednolicić formę bloku uwag w zapisie cyklu (dziś: punkt listy z wcięciami w `plomyk`, sekcja `## Process remarks` w `kopia-bazy` i `plan-wyprawy`, osobny plik `process-remarks.md` w `petla-zarobkowa`)?
  - Answer: tak — skrypt z odpowiedzi wyżej potrzebuje jednej formy bloku.
  - Source: Mariusz, 2026-11-05: „C”, przy którym pytanie postawiono z kosztem „potrzebuje stałej formy bloku uwag, więc drugie pytanie (ujednolicenie formy) rozstrzyga się samo na »tak«”.
- Czy to zadanie czeka na własne wytyczne kodowania i testów the way, skoro w the way nie ma katalogu `guidelines/`, a zadanie dodaje skrypt z testami (WAY-215)?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak zadanie o schemacie opisu PR-a (the way #71), a rozjazd reguły z praktyką zostaje w zadaniu [[wlasne_wytyczne_the_way]].
  - Not chosen:
    - Czekać na zadanie o własnych wytycznych the way — skrypt powstaje dopiero po wytycznych, a do tego czasu pozycje z końca cyklu dalej giną.
  - Source: Mariusz, 2026-11-05: „wszystko zgodnie z rekomendacjami”, na pytanie z rekomendacją „to samo co przy #71”.
- Co robi orkiestrator, gdy skrypt zgłasza brak, który orkiestrator uważa za błąd skryptu?
  - Answer: tak jak przy `task-cycle/request_check.py` — nie poprawia skryptu w cyklu, zapisuje archiwum, wpisuje przypadek do uwag procesowych i stawia go w opisie requestu w części do decyzji człowieka.
  - Not chosen:
    - Bez osobnej reguły — orkiestrator utknie, bo skrypt nie przestanie zgłaszać, albo sam uzna zgłoszenie za błędne i po cichu wróci odczyt przez model.
  - Source: Mariusz, 2026-11-05: „wszystko zgodnie z rekomendacjami”, na `Proposal:` z tym brzmieniem.
- Czy sprawdzić skrypt na zapisach z prawdziwymi brakami?
  - Answer: tak — kryterium akceptacji z trzema archiwami `loop2`, czytanymi przez `git show`.
  - Not chosen:
    - Bez tego kryterium — testy skryptu mogą stać tylko na spreparowanych przykładach i nie złapać formy, w jakiej agenci naprawdę piszą raporty, np. „None unresolved. Unclear: …”.
  - Source: Mariusz, 2026-11-05: „wszystko zgodnie z rekomendacjami”, na `Proposal:` z tym kryterium.

## Context

- Źródło zadania: lekcja Mega.DEV s01e03, krok 4 — `Notes/Projects/(P) Przejście Mega.DEV/mapa_pakietu_mega_dev.md`, Notatki, wpisy „krok 4: luka” i „krok 4: forma bloku uwag”; zadanie, które wprowadziło WAY-260: [[zadanie_raport_etapu_gdzie_sie_zgubilem]].
- `plomyk` (`loop2@31ac651:docs/task-cycles/plomyk/`): raport kroku powrotu `reports/06-return-step-report.md:81` niesie „Unclear: whether D-175's last sentence (…) needs code today”, trzy wiersze wyżej kończą się na „none”/„none found”; w `cycle.md` tego zdania nie ma. W tabeli zdarzeń krok powrotu (wiersz 58) stoi przed uzgodnieniem i `stages` (wiersze 59-60), czyli przed krokiem 12, w którym orkiestrator pisze *Request handoff* z uwagami — z archiwum nie wynika, czy orkiestrator wypełnił uwagi wcześniej, czy pozycję przeoczył.
- `reset-hasla` (`loop2@b311814`): uzgodnienie z `main` przed działaniem człowieka H1 (wybór A8, request już otwarty) — raporty `reports/37-reconciliation-report.md` i `reports/38-reconciliation-review-report.md` mają po dwie pozycje; żadnej nie ma w `cycle.md`.
- `kopia-bazy` (`loop2@d79c8e4`): `reports/slice-6-fix-report.md` — „None unresolved. Unclear: `rsync` availability on a new host is not stated by any source…” — nie ma w `cycle.md`, choć raport był już w pierwszym archiwum `67620ff`; `reports/correction-2-report.md` — „Head `e69034c` named in the handoff was the head at start…” — nie ma, a pozycje `correction-2-fix-review-report.md` są.
- Korekta po uwagach człowieka (`task-cycle/skill/correction.md`) powtarza parę commitów zapisu z kroku 12, ale nie mówi nic o uwagach procesowych; uzgodnienie z `main` po otwarciu requestu nie ma w skillu cyklu osobnego miejsca.
- Pole uwag stoi w szablonie zapisu w sekcji *Request handoff* (`task-cycle/record_template.md:171-172` na `61c72fb`), którą orkiestrator wypełnia przy requeście.
- Nocny przegląd mimo różnej formy bloku policzył uwagi ze wszystkich cykli, więc dziś nic przez formę nie ginie; skryptu `cycle_remarks_digest.py` ani sesji `/ai-review-cycles` to zadanie nie zmienia.
- Zasad WAY-260 zadanie nie zmienia: wszystkie etapy, słowo w słowo, bez łączenia powtórzeń — ustalenia Mariusza z 29.10.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-260 — What does each task-cycle stage report about what it could not find or understand?** (`foundations/decisions.md:7535`): „Every task-cycle stage's report states each thing the agent looked for and did not find, or found unclear, wherever it arose, or `none`; it keeps this separate from the report's account of each reach beyond the dispatch. The orchestrator copies every such item other than `none` word for word, with the stage name and full report path, into the cycle record's *Process remarks on the-way*, without combining repeated items.”
- **WAY-148 — How do task-cycle stages pass their work to the orchestrator?** (`foundations/decisions.md:3886`): „Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report.”
- **WAY-38 — In what are the scripts of the-way written?** (`foundations/decisions.md`): „Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.”
- **WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move?** (`foundations/decisions.md`): „The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and the declared version moves when the version in use leaves bugfix support, never because a newer version comes out.”
- **WAY-290 — How is the form of a request's description checked?** (`foundations/decisions.md`): „Before a request opens, the cycle runs the-way's script that checks the form of the request's description — the order and level of its headings, content or `none` in each section, and the collapsed block in the task document's language — and corrects the description until the script reports no error. The script judges no content.”
- **WAY-291 — What does the cycle do with an error of the form check that it holds wrong?** (`foundations/decisions.md`): „Where the orchestrator of a cycle holds an error the form check reports wrong, with evidence it can name, it does not change the description to silence the error — it never empties the collapsed block and never puts it into English — and the request opens, or stays, a draft whose section for the human's decisions names the error and the cycle's reason, while its checks name the check as failed; a request blocked for another cause stays blocked.”

## Settlements to record

Candidates: 6 shown, 3 accepted — 2026-11-05

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Przed każdym commitem, który dodaje zapis cyklu do `docs/task-cycles/<task-slug>/` — w kroku 12, w jego powtórce przy korekcie i w wariantach zablokowanego requestu — orkiestrator uruchamia skrypt the way, który wymienia każdą pozycję **Searches not found or unclear** poza `none` z raportów w `reports/`, której brakuje w uwagach procesowych zapisu, dopisuje każdą i uruchamia skrypt ponownie, aż nie wymieni żadnej. | decision | *Questions to settle*, pytanie 1 (drogi nie wybrane stoją pod nim); *To do* 2 | czy skrypt jest obowiązkowy przy każdym zapisaniu archiwum, czy tylko w kroku 12, bez powtórki przy korekcie po uwagach człowieka |
| 2 | Zgłoszenie skryptu, które orkiestrator uważa za błąd skryptu, nie zatrzymuje archiwum i nie jest poprawiane w skrypcie w tym cyklu: orkiestrator zapisuje archiwum, wpisuje przypadek do uwag procesowych i stawia go w opisie requestu w części do decyzji człowieka, tak jak przy `task-cycle/request_check.py`. | decision | *Questions to settle*, pytanie 4; pytanie przeciw odpowiedzi, zakotwiczone w notatce zadania („Nikt tego nie zauważy, bo nocny przegląd czyta tylko zapis cyklu…”) — czy reguła trzyma, skoro pozycja błędnie uznana za błąd skryptu trafia do uwag tylko jako przypadek skryptu i do opisu requestu: Mariusz, 2026-11-05: „myslę, że tak”; nie wybrane: pozycja wskazana przez skrypt trafia do uwag jako pozycja etapu niezależnie od oceny orkiestratora | czy przy wątpliwym zgłoszeniu zatrzymać zapis archiwum, poprawić skrypt w bieżącym cyklu, czy pominąć zgłoszenie bez śladu |
| 3 | Zapis cyklu trzyma uwagi procesowe w jednej formie, którą ustala szablon zapisu i czyta skrypt z wiersza 1, nie w osobnej sekcji ani w osobnym pliku. | decision | *Questions to settle*, pytanie 2; pytanie przeciw odpowiedzi, zakotwiczone w notatce zadania („Nocny przegląd mimo to policzył uwagi ze wszystkich, więc dziś nic przez to nie ginie”) — czy ujednolicenie trzyma, skoro jedynym jego powodem jest skrypt, a zapisy już zarchiwizowane zostają w dawnej formie: Mariusz, 2026-11-05: „myslę, że tak” | czy dopuścić dalej osobną sekcję `## Process remarks` albo plik `process-remarks.md` obok formy z szablonu |

## Out of scope

- Skrypt `cycle_remarks_digest.py` i sesja `/ai-review-cycles` zostają bez zmian (handoff zadania, ustalenie Mariusza).
