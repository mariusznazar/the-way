---
title: "the way: dopisanie do zakresu logowania produktu trafia do sekcji decyzji PR-a"
status: draft
created: 2026-11-05T18:19
updated: 2026-11-05
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: dopisanie do zakresu logowania produktu trafia do sekcji decyzji PR-a

Status: ready for cycle
Project relation: independent

## Description

### Need

- Decyzja WAY-274 pozwala agentowi dopisać do listy tego, co produkt loguje (identyfikatory i zdarzenia biznesowe) pozycję w tej samej zmianie, która ją wnosi, i zakłada, że Mariusz zobaczy to przy scaleniu.
- Od zmiany WAY-10 Mariusz czyta przy scaleniu tylko sekcję „For you to decide” opisu PR-a, a jej lista pozycji w szablonie nie ma pozycji o logowaniu.
- Lista logowania stoi w wytycznych produktu, które są poza fundamentem, więc nie obejmuje jej też pozycja o wpisach do fundamentu.
- Dopisanie stoi więc tylko w diffie i w dolnej części opisu, do której Mariusz nie zagląda, i przechodzi bez jego wiedzy.
- Odczuwa to Mariusz przy scalaniu PR-ów produktu (np. loop2); zwykle to drobiazg, ale decyzja pozwala na takie dopisania pod warunkiem, że człowiek je widzi.
- Skrypt `task-cycle/request_check.py`, który sprawdza układ opisu PR-a przed jego otwarciem, ma dwie luki (uwagi M-1 i M-2 z przeglądu całej zmiany w cyklu PR-a #71).
- M-1: plik opisu zapisany przez PowerShell zaczyna się niewidocznym znacznikiem UTF-8 (BOM); skrypt go nie zdejmuje i zgłasza, że pierwsza linia nie podaje stanu PR-a, choć na oko wygląda poprawnie.
- M-1 odczuwa prowadzący cykl, a przez niego Mariusz: błąd wygląda na fałszywy, więc PR może się otworzyć jako szkic bez powodu.
- M-2: nagłówek-wypełniacz `## <…>` z szablonu, przepisany do opisu razem z `none` pod spodem, przechodzi sprawdzenie, więc w PR-ze pojawia się sekcja zatytułowana `<…>`.
- Luki skryptu najwyżej kosztują dodatkową turę.

### To do

1. W `task-cycle/skill/request_template.md` lista pozycji sekcji „For you to decide” dostaje na końcu nową pozycję o dopisaniach do zakresu logowania produktu: każdą pozycję, którą zmiana dopisuje do listy tego, co produkt loguje, prostymi słowami (co to jest i którą linię logu niesie), z pytaniem „Accept it?”. W PR-ze, który niczego nie dopisuje, tej pozycji nie ma. Numery dotychczasowych pozycji się nie zmieniają.
2. W WAY-274 nic się nie zmienia. W WAY-287 (`foundations/decisions.md`) lista rodzajów rzeczy, które sekcja zbiera, dostaje rodzaj „dopisania do zakresu logowania produktu”.
3. Opis zapisany z niewidocznym znacznikiem UTF-8 na początku pliku przechodzi sprawdzenie stanu tak samo jak ten sam opis bez znacznika.
4. Opis, który zachowuje nagłówek-wypełniacz `## <…>` ze szkieletu szablonu, nie przechodzi sprawdzenia; komunikat mówi, żeby pominąć nagłówek albo wpisać w jego miejsce nagłówek własnej sekcji zadania.
5. Zdanie szkieletu w `task-cycle/skill/request_template.md:101-104` mówi wprost, że nagłówek pomija się, gdy zadanie nie ma własnych sekcji.

### Questions to settle

- Którą drogą sprawić, żeby dopisanie do logowania było widoczne przy scaleniu: (A) nowa pozycja w szablonie z dopiskiem w WAY-287 i WAY-274 bez zmian, (B) zmiana WAY-274 tak, żeby nie liczył na widok człowieka przy scaleniu, czy (C) zostawić jak jest?
  - Answer: A. Pozycja pojawia się tylko w PR-ze, który coś dopisuje do logowania, w rodzaju „Accept it?”; scalenie PR-a jest akceptacją. Dopisek w WAY-287 potrzebuje zgody Mariusza, bo zmienia zatwierdzoną decyzję, i ta zgoda jest zawarta w tej odpowiedzi.
  - Not chosen:
    - B. Zmiana WAY-274 tak, żeby nie liczył na widok człowieka — wraca opcja, którą WAY-274 sam odrzucił w *Rejected* („the principle alone”: lista niewidziana, nowe pozycje wchodzą bez człowieka), i zmienia znaczenie przyjętej decyzji.
    - C. Zostawić jak jest — dopisania do logów dalej wchodzą bez wiedzy Mariusza, a decyzja opisuje mechanizm, którego nie ma; recenzent porównujący zmianę z WAY-274 uzna jej „complies” za spełnione.
    - Ogólna pozycja na wszystko, co jakaś decyzja każe człowiekowi zobaczyć przy scaleniu — przeszukanie dziennika nie znalazło drugiego takiego przypadku, a taka pozycja zachęcałaby do zrzucania do sekcji wszystkiego, choć jej `none` ma znaczyć „można scalić” (WAY-287).
  - Source: Mariusz, 2026-11-05: „A”, na pytanie, czy idziemy drogą A razem z dopiskiem w WAY-287. Cytaty i miejsca: `foundations/decisions.md:8120-8121` (WAY-274), `:291-293` (WAY-10), `:8608-8616` (WAY-287), `task-cycle/skill/request_template.md:147-189` — stan `foundations` @ 61c72fb.
- Czy zgoda na dane wskazujące osobę (WAY-274) dociera do sekcji decyzji i czy zadanie ma to zmieniać?
  - Answer: Zostaje na ogólnej drodze, bez zmian w tym zadaniu. Zgodę uzyskuje się przed kodem (WAY-172), cykl otwiera wtedy zablokowany szkic PR-a, a jego wariant „An impossible task” stawia brakującą zgodę w sekcji decyzji jako „permission”. Ryzykiem jest agent, który nie rozpozna, że dopisanie wskazuje osobę; WAY-274 nazywa je wśród swoich słabych punktów.
  - Not chosen:
    - Osobny wariant „zgoda na dane wskazujące osobę” w tabeli wariantów szablonu opisu PR-a — daje agentowi punkt zaczepienia, ale to druga zmiana w szablonie i w WAY-287, bez dowodu, że ogólna droga zawodzi.
  - Source: Mariusz, 2026-11-05: „tak”, na pytanie, czy zostawiamy zgodę na ogólnej drodze, bez zmian w tym zadaniu. Miejsca: `product-guidelines/coding/template.md:213-215`, `foundations/decisions.md:4801-4808` (WAY-172), `task-cycle/skill/SKILL.md:21-23`, `task-cycle/skill/request_template.md:250` (wariant „An impossible task”) — stan `foundations` @ 61c72fb.
- Jak zamknąć lukę M-2: odrzucać nagłówek-wypełniacz w skrypcie, przeredagować zdanie szablonu (`request_template.md:101-104`) na „pomiń nagłówek, gdy zadanie nie ma własnych sekcji”, czy jedno i drugie?
  - Answer: Jedno i drugie: zdanie szablonu usuwa przyczynę, a skrypt łapie błąd, gdy agent mimo to przepisze nagłówek. Odrzucenie literału `<…>` sprawdza formę, nie treść, więc skrypt dalej nie ocenia treści (WAY-290).
  - Not chosen:
    - Tylko skrypt — zdanie szablonu dalej wprowadza w błąd, a agent traci turę na poprawkę.
    - Tylko szablon — nic nie łapie błędu, gdy agent mimo to przepisze nagłówek, a WAY-290 daje na to skrypt.
  - Source: Mariusz, 2026-11-05: „c - oba”.

## Context

- Źródło: uwagi M-1, M-2 i M-3 z przeglądu całej zmiany w cyklu PR-a #71 oraz raport autora tej zmiany; zapis cyklu stoi w the way na commicie `a8bd8b6`, w `docs/task-cycles/pr-description-schema/reports/whole-review.md` (M-3 także w `reports/author.md`).
- Numery linii zgadzają się ze stanem `foundations` @ 61c72fb: `task-cycle/skill/request_template.md:101-104` (nagłówek-wypełniacz) i `:147-189` (lista pozycji), `task-cycle/request_check.py:317` (sprawdzenie pierwszej linii), `:363-368` (własne sekcje zadania) i `:460-465` (odczyt pliku).
- Luki M-1 i M-2 są potwierdzone odczytem kodu na tym stanie, bez uruchamiania skryptu; recenzent PR-a #71 zgłosił je po próbnym uruchomieniu.
- Przeszukanie dziennika decyzji po frazach „at the merge”, „sees” i „merges” nie znalazło drugiej decyzji, która liczyłaby na widok człowieka przy scaleniu bez miejsca w sekcji: WAY-03, WAY-49 i WAY-51 mają pozycję o zmienionych testach niezmienników, WAY-114, WAY-99 i WAY-126 pozycję o wpisach do fundamentu, WAY-161 i WAY-289 pozycję o niepoprawionych uwagach; to wyszukiwanie po słowach, nie dowód.
- Samo the way nie ma własnych wytycznych kodowania i testów ani decyzji, która by od nich odchodziła; zadanie idzie dalej jak dotychczasowe zadania the way, bez czekania na nie (Mariusz, 2026-11-05: „tak jak dotychczas”), a sprawę prowadzi osobne zadanie [[wlasne_wytyczne_the_way]].
- Wytyczne produktu stoją poza fundamentem (`foundations/decisions.md:4791`); lista logowania stoi w regule `### Logging scope` ich szablonu (`product-guidelines/coding/template.md:209-215`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-274: „The principle of a product's logging scope stands in the product's decision on the rules on failures and logs, and the list of today of the identifiers and business events it logs, at adoption from what the product has in its code or in its plan, stands in a rule of its guidelines, as the product's promise and no inventory of its code. An agent adds an item that fits the principle, any identifier of a thing included, in the change that brings it, and the human sees it at the merge. Whatever points to a person, an email, a name, a telephone number, a home address and an IP address among them, takes the human's consent, and the number the product gives a user is settled by the human when the list is accepted and takes that consent if added later.”
- WAY-287: „The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — the cycle's choices beyond the task's content, the steps skipped and the checks not run, the unfixed findings the product's user or the human working with the process will feel, the decisions of the task's own sections, in a blocked request what the cycle needs to go on, the human actions, the changed invariant tests, surfaces and *Violated* marks, and the foundation entries the human did not see at the task document — and its `none` says that nothing else in the request waits for the human's yes.” To do 2 dopisuje do tej listy jeden rodzaj.
- WAY-10: „a human reads the section of the request's description for the human's decisions and accepts the change by merging the request.”
- WAY-286: „a section with no content reads `none` rather than being left out.”
- WAY-290: „Before a request opens, the cycle runs the-way's script that checks the form of the request's description — the order and level of its headings, content or `none` in each section, and the collapsed block in the task document's language — and corrects the description until the script reports no error. The script judges no content.”

## Settlements to record

Candidates: 5 shown, 1 accepted — 2026-11-05

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Dopisanie do zakresu logowania produktu stoi w sekcji „For you to decide” opisu PR-a jako pozycja do akceptacji, a WAY-274 zostaje bez zmian. | decision | *Questions to settle*, pytanie 1 (drogi niewybrane pod nim) | czy przy dopisku do WAY-287 zapisać drogi B i C w jego *Rejected*, które dziś brzmi `unknown`, i czy przy okazji poprawić zdanie WAY-274 |

## Out of scope

- Osobny wariant szablonu opisu PR-a dla zgody na dane wskazujące osobę: ogólna droga przez zablokowany szkic PR-a istnieje i nic nie wskazuje, że zawodzi.
