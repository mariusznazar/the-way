---
title: "the way: zadanie zbiorcze z uwag cykli — nazwy plików raportów, fałszywe pozycje w skrypcie uwag"
status: draft
created: 2026-11-12T10:40
updated: 2026-11-12
tags: [zadanie]
related: "the author's note of the project of the process work"
---

# the way: zadanie zbiorcze z uwag cykli — nazwy plików raportów, fałszywe pozycje w skrypcie uwag

Status: ready for cycle
Project relation: independent

## Description

### Need

- W cyklu zadania the-way każdy agent etapu zapisuje swój pełny raport do pliku w `reports/`, a prowadzący cykl czyta z niego tylko wybrane części (WAY-148).
- Gdy nazwa pliku raportu zaczyna się od `report`, `summary`, `findings` albo `analysis` (bez względu na wielkość liter), Claude Code odmawia subagentowi zapisu z komunikatem „Subagents should return findings as text, not write report files. Include this content in your final response instead.”
- Agent oddaje wtedy cały raport w odpowiedzi, a prowadzący zapisuje go sam i ładuje przy tym całość do swojego kontekstu — dokładnie to, czego WAY-148 ma unikać.
- Skrypt `task-cycle/remarks_check.py`, który przed zapisaniem rekordu cyklu sprawdza, czy pozycje sekcji **Searches not found or unclear** z raportów trafiły do uwag procesowych (WAY-294), zgłasza czasem pozycje, które pozycjami nie są: poziomą kreskę `---` oddzielającą części raportu i dalszy ciąg zdania, którego druga linia zaczyna się od pogrubionej nazwy sekcji.
- Kto to odczuwa: prowadzący cykl, któremu pełne raporty zapychają kontekst, a fałszywe zgłoszenia skryptu musi z dowodem odrzucać (WAY-295); Mariusz, do którego obie rzeczy wracają jako uwagi w przeglądzie warstwy AI i punkty w opisie PR-a do rozstrzygnięcia.
- Co jeśli nic: nic nie przepada — cykle radzą sobie obejściem, a skrypt myli się głośno, nie po cichu; zostaje koszt raportu w całości w kontekście prowadzącego co kilka cykli i kwadransa na każde fałszywe zgłoszenie.

### To do

1. W `task-cycle/skill/SKILL.md`, zaraz po zdaniu „Write each dispatch's full handoff to a file in `reports/` whose name holds `handoff`; …(WAY-148).”, stoi reguła nazw plików raportów (pytanie 2):

   > Begin each report file's name with the stage or the agent's role, the word `report` after it if at all (`author-report.md`, not `report-author.md`): Claude Code refuses a subagent's write of a file whose name starts with `report`, `summary`, `findings` or `analysis`, answering that subagents should return findings as text.
2. W `task-cycle/remarks_check.py` linia sekcji, która jest samą poziomą kreską (`---`, `***`, `___`, także ze spacjami między znakami, jak `- - -` albo `* * *`), nie jest pozycją — tak jak dziś nie jest nią podnagłówek; w opisie skryptu „a sub-heading is no item” zmienia się na „a sub-heading and a thematic break are no items”.
3. W `task-cycle/remarks_check.py` pogrubiona etykieta `**Searches not found or unclear**` otwiera sekcję tylko na początku akapitu albo punktu listy: na początku pliku, po pustej linii, po nagłówku, po kresce, po linii, która sama zaczyna się od pogrubienia, albo na linii ze znacznikiem listy; w opisie skryptu „at the start of a line or of a list item” zmienia się na „at the start of a paragraph, of a list item, or after a line opening with another bold label”.
4. Raport bez sekcji **Searches not found or unclear** nadal nie daje żadnej pozycji i nie kończy skryptu błędem, jak dziś; WAY-294 zapisuje to jako wyjątek od WAY-344 (pytanie 1).
5. W `task-cycle/test_remarks_check.py` cztery przypadki: kreska po sekcji z nagłówkiem nie jest pozycją; etykieta na drugiej linii akapitu nie otwiera sekcji; dwie etykiety w kolejnych liniach bez pustej linii między nimi są obie czytane; raport bez sekcji nie daje pozycji, a skrypt kończy się kodem 0.

### Questions to settle

- Pytanie 1. WAY-344 każe skryptowi, którego sposób czytania pliku zmiana przerabia, kończyć się kodem 2 z komunikatem, gdy w pliku brak potrzebnego pola; punkty 2 i 3 przerabiają to, jak skrypt uwag znajduje sekcję w raporcie i dzieli ją na pozycje. Czy raport bez sekcji **Searches not found or unclear** ma od tej zmiany kończyć skrypt kodem 2, czy nadal nie dawać żadnej pozycji?
  - Answer: Nadal nie daje żadnej pozycji, a wyjątek od WAY-344 stoi w WAY-294, decyzji o tym skrypcie (WAY-30 nie pozwala, by wyjątek żył tylko w zadaniu). Raport etapu, który zgubił sekcję, przechodzi przez skrypt bez błędu; łapie go prowadzący, który z reguły skilla cyklu zwraca taki raport agentowi do naprawy (`task-cycle/skill/SKILL.md:213-216`).
  - Not chosen:
    - Zastosować WAY-344 wprost: raport bez sekcji kończy skrypt kodem 2, z testem — od 2026-11-05 w 10 z 50 cykli w `reports/` leżały pliki prowadzącego bez sekcji i każdy taki cykl stanąłby przy zapisie rekordu; raport zwracający `questions` legalnie nie ma sekcji; zadanie urosłoby o regułę nazywania plików pomocniczych i zmianę definicji raportu w WAY-294.
    - Uznać, że zmiana nie przerabia czytania raportów, i niczego nie dopisywać — recenzent porówna zmianę z przykładem z samej WAY-344 („a change that reworks how a script reads the section headings of a report brings every field of that report under the check”) i najpewniej zgłosi naruszenie.
  - Source: Mariusz, 2026-11-12, „A”, na pytanie z drogami A (wyjątek w WAY-294), B (WAY-344 wprost), C (nic nie dopisywać).
- Pytanie 2. Jak brzmi reguła nazw plików raportów, skoro blokada Claude Code obejmuje nie tylko nazwy od `report`, ale też od `summary`, `findings` i `analysis`?
  - Answer: Reguła mówi, od czego nazwę zacząć — od etapu albo roli agenta, ze słowem `report` dalej, jeśli w ogóle — a sprawdzone słowa podaje jako powód; brzmienie w punkcie 1 *To do*. Chroni też przed słowami, których nie sprawdzono, kosztem nieco ciaśniejszej reguły dla prowadzącego.
  - Not chosen:
    - Zdanie z notatki rozszerzone o listę czterech słów — działa dla sprawdzonych, ale gdy Claude Code blokuje jeszcze inne słowo, prowadzący trafi na tę samą odmowę bez ostrzeżenia.
    - Zdanie z notatki bez zmian (tylko `report`) — prowadzący, który nazwie raport `findings-review.md` albo `summary-…`, wróci do obejścia.
  - Source: Mariusz, 2026-11-12, „A”, na pytanie z drogami A (od czego zacząć nazwę), B (lista czterech słów), C (zdanie z notatki).

## Context

- Źródło: sprawy AIR-633 (nazwy plików) i AIR-635 (skrypt uwag) z przeglądu warstwy AI 2026-11-12, w wersjach poprawionych po krytyce w tej samej sesji; rekordy AIR-633 i AIR-635 w zeszycie przeglądu niosą propozycje nocnego skanu sprzed krytyki i nie są wersją obowiązującą.
- Według przeglądu warstwy AI z 2026-11-12 od 5 listopada zdarzyło się to w 7 z 58 cykli; wszystkie 67 prób zapisu pliku z nazwą od `report` odrzucono, wszystkie 758 z `report` dalej w nazwie przyjęto.
- Blokadę sprawdzono 2026-11-12 subagentem Claude Code 2.1.322 (Windows 11, komputer Mariusza) zapisującym narzędziem Write pliki o jedenastu nazwach: odrzucone `report-author.md`, `report.md`, `Report-x.md`, `reports-x.md`, `reporting.md`, `summary-author.md`, `findings-author.md`, `analysis-author.md`; zapisane `author-report.md`, `review-author.md`, `notes-author.md`.
- Pliki z `findings` w nazwie zapisuje w cyklu prowadzący, nie subagent, więc blokada ich nie dotyczy.
- Nocny skan proponował regułę obejścia (prowadzący zapisuje raport za agenta i odnotowuje to w pierwszej linii); odpadła, bo zostawia przyczynę, a pierwsza linia raportu recenzji niesie wynik `PASS`/`FAIL`, z którego skill cyklu go czyta.
- Kreskę rozważano też jako koniec sekcji; wybrano „nie jest pozycją”, bo niczego nie ucina, gdyby po kresce stał jeszcze tekst sekcji.
- Wyjątek „po linii zaczynającej się od pogrubienia” w punkcie 3 jest potrzebny, bo raporty stawiają czasem dwie etykiety pod rząd bez pustej linii (`**Unread material:** none`, a zaraz pod nią `**Searches not found or unclear:** …`).
- Przegląd 972 różnych raportów cykli na dysku (the-way i loop2, 2026-11-12): etykieta poza nagłówkiem stoi w 19 miejscach — 13 po pustej linii, 2 na linii ze znacznikiem listy, 2 po linii z inną etykietą, 1 w środku akapitu, 1 jako dalszy ciąg punktu listy; reguła punktu 3 otwiera sekcję w 17 pierwszych i nie otwiera w 2 ostatnich, które są dziś fałszywymi zgłoszeniami.
- Ten sam przegląd: wśród 1385 pozycji, które skrypt dziś czyta, jedna jest samą kreską.
- Ten sam przegląd, cykle od 2026-11-05: 24 z 524 plików `.md` w `reports/` (w 10 z 50 cykli) nie mają sekcji — w większości pliki prowadzącego (uwagi człowieka do korekty, liczby słów, oceny, wyciągi z dokumentacji, podsumowanie bramki), raz raport etapu (`slice-11-report.md` w loop2).
- Raport zwracający `questions` może nie mieć sekcji (`task-cycle/skill/SKILL.md:213-216`), a raport etapu bez niej prowadzący i tak zwraca agentowi do naprawy.
- Miejsca w kodzie: dzielenie sekcji na pozycje — `split_items` (`task-cycle/remarks_check.py:149`), koniec sekcji etykiety — `label_end` (`:186`), znajdowanie etykiety — `section_items` (`:205`), opis skryptu — `:1-48`; numery linii z the-way `origin/foundations` @ 55afa8e.
- Reguła nazw plików raportów stoi tylko w skillu cyklu, z powodem w samym zdaniu, bez decyzji i bez faktu o środowisku: to obejście zachowania narzędzia w jednym kroku prowadzącego, jak sposób czekania na agenta, którego decyzję WAY-157 wycofano jako krok skilla niewiążący innej pracy (Mariusz, 2026-11-12, skreślając te dwa wiersze z kandydatów: „tak, skreślamy 2 i 3”).
- Wytyczne kodu i testów: the-way odstępuje od wytycznych produktu dla własnego kodu i testów (WAY-328), więc zadanie na nie nie czeka.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-148** — „Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. […]” Punkt 1 przywraca to, czego ta decyzja wymaga, gdy Claude Code odmawia zapisu.
- **WAY-260** — „Every task-cycle stage's report states each thing the agent looked for and did not find, or found unclear, wherever it arose, or `none`; it keeps this separate from the report's account of each reach beyond the dispatch. The orchestrator copies every such item other than `none` word for word, with the stage name and full report path, into the cycle record's *Process remarks on the-way*, without combining repeated items.”
- **WAY-294** — „Before every commit that adds the cycle record to the product's repository, the orchestrator runs the-way's script that lists each item other than `none` under **Searches not found or unclear** in the record's stage reports — the `.md` files of the cycle's `reports/` directory whose name holds neither `handoff` nor `findings` — that the record's process remarks do not hold word for word, appends each listed item word for word with its stage name and full report path, and runs the script again until it lists nothing. […] The script only lists, and an item that two reports give is listed again until the remarks hold it twice.” Zmiana, którą niesie zadanie: decyzja zyskuje zdanie, że raport bez sekcji nie daje żadnej pozycji i nie kończy skryptu błędem, jako zawężenie WAY-344 z jego powodem — w `reports/` leżą też pliki prowadzącego bez sekcji, a raport etapu bez niej prowadzący zwraca agentowi (pytanie 1). Jej *Verification* podaje też jako przykład raportu nazwę `report-planner.md`, której punkt 1 zabrania; przykład brzmi `planner-report.md`, przy tym samym znaczeniu.
- **WAY-295** — „Where the orchestrator of a cycle holds a listing of the remarks check of WAY-294 to be an error of the script, with evidence it can name, the record is archived all the same and the script is not changed in that cycle […]” To zadanie jest tą osobną zmianą skryptu, poza cyklem, który błąd spotkał.
- **WAY-344** — „A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs […] and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks — every field of that file, no other file and no other part of the script — and a missing field ends the script with exit code 2 and a message that names the file and the field […]. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field […].” Zmiana, którą niesie zadanie: czytanie raportów przez skrypt uwag zostaje zawężone wyjątkiem zapisanym w WAY-294 — raport bez sekcji nie daje pozycji (pytanie 1).

## Settlements to record

Candidates: 4 shown, 1 accepted — 2026-11-12

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Skrypt uwag czyta raport bez sekcji **Searches not found or unclear** jako niedający żadnej pozycji i nie kończy się wtedy błędem; ten wyjątek od WAY-344 stoi w WAY-294. | decision (zmienia WAY-294, zawęża WAY-344) | Pytanie 1 | czy raport bez sekcji kończy skrypt kodem 2, jak każe WAY-344, czy daje zero pozycji |

## Out of scope

- Kolejność sekcji **Unread material** i **Searches not found or unclear** w raportach — to zadanie jej nie rusza; autor i recenzent zalecili czekać na pierwszy prawdziwy przypadek.
- Czytanie przez skrypt pliku `cycle.md` — zmiana przerabia tylko czytanie raportów.
