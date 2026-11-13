---
title: "the way: jedną zmianą zamknąć dopiski „decision pending” w szablonach — 19 cytatem albo zwykłym tekstem, sześć reguł poprawionych, nagłówek „Draft” usunięty"
status: draft
created: 2026-11-13T10:30
updated: 2026-11-13
tags: [zadanie]
related: "przegląd projektu w prywatnych notatkach autora"
---

## Po co to

- **Jak jest dziś:** W szablonach the way — plikach, które mówią agentowi, jak pisać wpisy fundamentu produktu (niezmienniki, fakty o otoczeniu, słownik, mapę części) — stoją 32 dopiski `TODO — decision pending` przy regułach, którym kiedyś brakowało decyzji. Zasadę, że każda reguła szablonu musi cytować decyzję, zniesiono 21.10.2026, ale dopiski zostały. Kilka reguł przy nich przeczy dziennikowi decyzji albo innym zdaniom tego samego pliku, a nagłówek „Draft” w szablonie niezmienników mówi, że reguły bez cytowanej decyzji nie wiążą i że szablon nie trafia na gałąź główną.
- **Kto to odczuwa:** Agenci, którzy piszą wpisy fundamentu w loop2 i w the way — czytają sprzeczne zdania, a część reguł jako niewiążące; rejestr problemów audytu ma trzy drobne uwagi, że agenci rozstrzygali takie miejsca sami. Ja — przy wydaniu the way na gałąź główną, które stoi, dopóki szablony mają dopiski i nagłówek „Draft”.
- **Co jeśli nic:** Dziś nic się nie psuje — w zapisach rozmów nie ma ani jednej mojej skargi z tego powodu. Sprzeczności zostają w szablonach, a wydanie dalej stoi.

# the way: jedną zmianą zamknąć dopiski „decision pending” w szablonach — 19 cytatem albo zwykłym tekstem, sześć reguł poprawionych, nagłówek „Draft” usunięty

Status: ready for cycle
Project relation: independent

## Description

### Need

- W siedmiu plikach `elements/` the way stoją 32 linie `TODO — decision pending: …` (stan na `6814c6f`, gałąź `foundations`).
- Agent piszący wpis fundamentu czyta taki dopisek jako „ta reguła nie wiąże” i rozstrzyga sam; rejestr problemów audytu ma o tym trzy drobne uwagi.
- Część reguł przy dopiskach przeczy dziennikowi decyzji the way albo innemu zdaniu tego samego pliku, np. krok 4.1 w `elements/common/way_of_working.md` każe dawać każdemu pytaniu proponowaną odpowiedź, a WAY-113 każe zostawić pytanie o ocenę otwarte.
- Nagłówek „Draft” w `elements/invariants/template.md` mówi, że reguła bez cytowanej decyzji nie wiąże i że szablon nie trafia na gałąź główną — to jedna z rzeczy, które dziś wstrzymują wydanie the way na `main`.
- Odbiorcą są agenci piszący wpisy fundamentu w produktach i w samym the way, i Mariusz przy wydaniu the way na `main`.

### To do

1. Dziewiętnaście spraw S1–S19 z raportu (23 linie dopisków) zamknięte bez zmiany sensu reguły: w sprawach S1–S12 dopisek zastępuje numer istniejącej decyzji, w sprawach S13–S19 dopisek znika, a reguła zostaje zwykłym tekstem szablonu. Numery linii — stan na `6814c6f`:

   | Sprawa | Dopisek | Czym zamknąć |
   |---|---|---|
   | S1 | `elements/environment-facts/template.md:183`, `elements/glossary/template.md:104`, `elements/invariants/template.md:181`, `elements/part-map/template.md:171` | WAY-05 |
   | S2 | `elements/invariants/template.md:33` | WAY-64 |
   | S3 | `elements/invariants/template.md:71` | WAY-61 |
   | S4 | `elements/invariants/template.md:107` | WAY-44 |
   | S5 | `elements/invariants/template.md:159` | WAY-62 i WAY-22; końcówka „it belongs to the foundation of the product whose commits decide it” wypada |
   | S6 | `elements/environment-facts/template.md:59` | WAY-73 |
   | S7 | `elements/environment-facts/template.md:68` | WAY-90 i WAY-73 |
   | S8 | `elements/part-map/template.md:20` | WAY-48, WAY-44 i WAY-41 — każda przy swojej liście |
   | S9 | `elements/part-map/template.md:150` | WAY-48 |
   | S10 | `elements/invariants/skill/decide_entry.md:12` | WAY-22 i WAY-29 |
   | S11 | `elements/common/missing_element_file.md:11` | WAY-44, obok cytowanej już WAY-28 |
   | S12 | `elements/common/way_of_working.md:133` | WAY-71 przy zakazie `none`; „najpierw zapytaj” zostaje zwykłym tekstem |
   | S13 | `elements/common/way_of_working.md:130` | zwykły tekst |
   | S14 | `elements/common/way_of_working.md:160` | zwykły tekst |
   | S15 | `elements/common/missing_element_file.md:5` | zwykły tekst |
   | S16 | `elements/environment-facts/template.md:25`, `elements/invariants/template.md:29` | zwykły tekst |
   | S17 | `elements/environment-facts/template.md:124` | zwykły tekst |
   | S18 | `elements/environment-facts/template.md:175` | zwykły tekst |
   | S19 | `elements/environment-facts/template.md:86` | zwykły tekst |

   Każdy cytat jest sprawdzony w `foundations/decisions.md` przed wpisaniem; przy S4, S5, S7, S10 i S11 raport ma średnią pewność, więc przegląd zmiany potwierdza cytat albo zamienia go na zwykły tekst.
2. Krok 4.1 w `elements/common/way_of_working.md` brzmi: „Ask in one round about everything still open, as »How a skill asks« gives it (WAY-113): a value the source does not give, with where to look for it and never the value itself; a choice, with the ways open, what each costs and a recommendation; a question of assessment, open.” Dopisek przy nim znika.
3. Punkt o pytaniu o decyzję w sekcji „How a skill asks” tego samego pliku brzmi: „A question of decision — a choice that settles something in a file — gives the ways open, what each costs, and a recommendation.” — odsyłacz do kroku 4.1 wypada.
4. W `elements/environment-facts/template.md` zdanie o zdaniu faktu traci słowa „in the present tense” i dopisek; zostaje „The sentence states what is true of the world today, and nothing it says is an invariant (WAY-76).”
5. W `elements/environment-facts/template.md` końcówka „and finding it is a task” z dopiskiem zastąpiona odesłaniem do WAY-71: wpis, który stałby na brakującym fakcie, dostaje `TODO — …`, a zmiana, która go zostawia, stawia to przed człowiekiem.
6. W `elements/environment-facts/template.md` zdanie „Moving the product to another release is a decision's to make.” usunięte razem z dopiskiem, bez zdania w zamian.
7. W `elements/part-map/template.md` reguła `Files: none` („A part whose tool does not exist yet holds no files …”) zostaje bez zmian jako zwykły tekst; znika tylko dopisek.
8. Nagłówek „Draft” (cytat blokowy na początku `elements/invariants/template.md`, razem z jego dopiskiem) usunięty.
9. W `elements/glossary/template.md` zdanie z dopiskiem o słowie, które produkt pokazuje w innym języku, zastąpione zwykłym zdaniem opartym na WAY-72 i WAY-99: wpis słownika trzyma termin angielski, a słowo pokazywane użytkownikom w innym języku zostaje w plikach produktu.

### Questions to settle

- Co zamyka dopisek „decision pending” (sprawa S0 raportu)?
  - Answer: (a) jedna z trzech dróg — cytat istniejącej decyzji, pozostawienie reguły jako zwykłego tekstu szablonu albo, tylko przy prawdziwym wyborze, zmiana dziennika; sprawy S1–S19 są jedną partią w wariantach rekomendowanych przez raport.
  - Not chosen:
    - (b) każdy dopisek dostaje decyzję albo reguła wypada, jak ustalono w odchudzaniu — zapis sprzed zniesienia zasady cytowania 21.10.2026.
    - (c) usunąć same dopiski bez sprawdzania — sprzeczności zostają w szablonach.
  - Source: Mariusz, 2026-11-12 — `otwarte_decyzje_the_way.md`, akapit pod tabelą „Tabela do wyboru”: „Decyzja Mariusza z 2026-11-12: w sprawie S0 wariant (a).”
- S20 — krok 4.1 każe zadawać pytania jednego wpisu w jednej rundzie, każde z proponowaną odpowiedzią.
  - Answer: przeredagować krok 4.1 i punkt sekcji „How a skill asks”, który do niego odsyła; trzy rodzaje pytań: brakująca wartość — gdzie szukać, nigdy sama wartość; wybór — warianty, koszt, rekomendacja; ocena — otwarte (brzmienie w punktach 2 i 3 *To do*).
  - Not chosen:
    - zostawić brzmienie i usunąć sam dopisek — sprzeczność z WAY-113 i WAY-114 zostaje, agent ma dwie instrukcje naraz.
    - usunąć także „jedną rundę” — człowiek dostaje pytania pojedynczo, każde przerywa mu pracę osobno.
  - Source: Mariusz, 2026-11-13 — `rozstrzygniecia_mariusza.md`, „Sprawa 3”: „S20: przeredagować krok 4.1 **i** linie 27–29 `way_of_working.md` (sekcja „How a skill asks” odsyłała z powrotem do 4.1); trzy rodzaje pytań: brakująca wartość — gdzie szukać, nigdy sama wartość; wybór — warianty, koszt, rekomendacja; ocena — otwarte.”
- S21 — zdanie faktu ma być w czasie teraźniejszym.
  - Answer: usunąć same słowa „in the present tense”; „what is true of the world today” zostaje.
  - Not chosen:
    - wyciąć też „today” (propozycja agenta) — Mariusz: „chroni przed przewidywaniem zapisanym jako fakt”.
    - zostawić w całości jako zwykły tekst — regułę łamią własne przykłady elementu, co uczy agentów, że reguły można łamać.
    - nowa decyzja i przepisanie faktów z badań na czas teraźniejszy — brzmi sztucznie i przeczy WAY-85.
  - Source: Mariusz, 2026-11-13 — „Sprawa 3”: „S21: jak w raporcie (usunąć „in the present tense”); propozycja agenta, by wyciąć też „today”, nieprzyjęta — chroni przed przewidywaniem zapisanym jako fakt.”
- S22 — „finding it is a task” przy fakcie bez źródła.
  - Answer: zastąpić odesłaniem do WAY-71.
  - Not chosen:
    - zostawić jako zwykły tekst — dalej nie wiadomo, kto zadanie zakłada.
    - usunąć końcówkę — agent nie wie, co zrobić z luką.
  - Source: Mariusz, 2026-11-13 — „Sprawa 3”: „S22: jak w raporcie.”
- S23 — „Moving the product to another release is a decision's to make.”
  - Answer: zdanie usunąć, nie przerabiać.
  - Not chosen:
    - przeredagować na „przejście jest zmianą produktu, nie faktu” (rekomendacja raportu) — przeczy `elements/environment-facts/template.md:143-144`, gdzie fakt zmienia się, gdy nowsze wydanie, na którym stoi produkt, mówi co innego.
    - zostawić jako zwykły tekst — agenci mogą czytać to jako nakaz pisania decyzji przy każdej aktualizacji zależności.
    - nowa decyzja uogólniająca WAY-89 na produkty — realny koszt w każdym cyklu z aktualizacją.
  - Source: Mariusz, 2026-11-13 — „Sprawa 3”: „S23: **zdanie usunąć**, nie przerabiać — wariant (a) raportu („zmiana produktu, nie faktu”) przeczy `environment-facts\template.md:143-144`.”
- S24 — reguła `Files: none` dla części, której narzędzie jeszcze nie istnieje.
  - Answer: reguła zostaje jako zwykły tekst, znika tylko dopisek.
  - Not chosen:
    - usunąć regułę (rekomendacja raportu, z powodu sprzeczności z WAY-01) — skrypt sprawdzający fundament odrzuca wzorzec plików bez trafienia, a wpisy fundamentu powstają w cyklu przed kodem, więc nowa część, której pliki przyjdą później w tej samej zmianie, nie miałaby innej drogi.
    - nowa decyzja z wyjątkiem od WAY-01 — brak przypadku, który by jej potrzebował.
  - Source: Mariusz, 2026-11-13 — „Sprawa 3”: „S24: **odwrócone — wariant (b)**, reguła `Files: none` zostaje jako zwykły tekst: skrypt odrzuca wzorzec bez trafienia (`foundation_check.py:62`), a wpisy fundamentu powstają przed kodem.”
- S25 — nagłówek „Draft” szablonu niezmienników.
  - Answer: usunąć w tej zmianie, bez czekania na drugie zadanie.
  - Not chosen:
    - zostawić do dnia wydania — agent czytający szablon dalej dowiaduje się, że połowa reguł nie wiąże.
    - nowa decyzja — sprzeczna z WAY-36.
  - Source: Mariusz, 2026-11-13 — „Sprawa 3”: „S25: nagłówek „Draft” usunąć **od razu** w zmianie z D2, bez czekania na D4 (precedens: szablon faktów, `f2c3186`, 29.09).”
- S27 — jak w słowniku stoi słowo, które produkt pokazuje w innym języku.
  - Answer: wariant (a) bez zmiany dziennika — zdanie w szablonie słownika jako zwykły tekst oparty na WAY-72 i WAY-99: wpis trzyma termin angielski, słowo pokazywane w innym języku zostaje w plikach produktu.
  - Not chosen:
    - (a) z dopiskiem do WAY-99 — zmiana dziennika; słownik loop2 od 39 wpisów działa bez niej.
    - (b) słowo w cudzysłowie w definicji — kopia napisu z interfejsu rozjedzie się z nim po pierwszej zmianie tekstu, a nic tego nie wykryje.
    - (c) nowe pole *Shown as* — pole wymaga czytelnika i mechanizmu, który je utrzymuje (WAY-05, WAY-04), a takiego nie ma.
  - Source: Mariusz, 2026-11-13 — „Sprawa 3”: „S27: wariant (a) bez zmiany dziennika — zdanie w szablonie słownika jako tekst własny (WAY-72, WAY-99); sprawa przeszła z D4 do zmiany z D2.”

## Context

- Raport, z którego zadanie wyszło: raport w prywatnych notatkach autora (otwarte decyzje the way) — sprawy S1–S19 z cytatami decyzji (sekcje U3 i U4), S20–S25 z cytatami obu stron sprzeczności (U5), S27 (U6); stan repozytorium raportu `55afa8e`.
- Decyzje Mariusza z 12 i 13.11.2026: plik rozstrzygnięć w prywatnych notatkach autora, sekcja „Sprawa 3”; tam też to, co zmieniła krytyka propozycji.
- Pełny zapis sesji, w której zadanie powstało (wygasa ok. 2027-02-11, ok. 1,5 MB — przeszukiwać po konkretach): zapis sesji w prywatnym katalogu autora.
- Na `6814c6f` wszystkie 32 linie dopisków stoją w tych samych miejscach co na `55afa8e`, a cytowane w raporcie zdania dziennika — pod tymi samymi numerami linii.
- Reguła szablonu nie potrzebuje cytowanej decyzji: WAY-05, *Rejected* (`foundations/decisions.md:160`) — „a rule of the template changed only with a decision citing its number — the template is the-way's own text, changed and reviewed like any other change to it”; to samo WAY-35, *Rejected* (`:974`).
- Precedens zwykłego tekstu: dwie reguły szablonu decyzji stoją bez dopisku i bez cytatu (`elements/decisions/template.md:106` i `:110`).
- Precedens usunięcia nagłówka „Draft”: commit `f2c3186` (2026-09-29) usunął go z szablonu faktów, w którym zostało wtedy 16 dopisków.
- Żaden test ani skrypt the way nie czyta dopisków „decision pending” ani zdań, które zadanie zmienia (wyszukanie w plikach `*.py`).
- `elements/common/foundation_check.py:62` zgłasza błąd przy wzorcu pliku części, który nie trafia w żaden plik śledzony przez git — na tym stoi decyzja S24.
- Raport uznał regułę `Files: none` za sprzeczną z WAY-01 (`foundations/decisions.md:9` i `:33`); Mariusz zostawił ją po krytyce, z powodem zapisanym przy S24.
- Po zmianie zostają dwa dopiski: S26 (`elements/environment-facts/template.md:138`, źródło ustawienia czytanego po zalogowaniu w cudzej usłudze) i S28 (`elements/invariants/template.md:94`, wpis wskazuje miejsce swojego warunku); oba zamyka zadanie z prywatnego backlogu autora o odczycie ustawienia w cudzej usłudze i o warunku niezmiennika.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-05 (`foundations/decisions.md:132-133`): „A field stays in the template only while someone or something reads it” — cytat dla S1.
- WAY-22 (`:595-597`): „A rule that records a choice is a decision, and what of it a commit can make false is written as an invariant derived from it” — cytat dla S5 i S10.
- WAY-29 (`:793`): opcje odtworzonej decyzji są „quoted from a source, given by a human who knows them, or written as `unknown`” — cytat dla S10.
- WAY-36 (`:979-982`): „A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition between two states — stays in the plan of that work” — dlatego nagłówek „Draft” nie dostaje decyzji (S25).
- WAY-41 (`:1079-1083`): identyfikator mapy części, który zostaje po podziale, scaleniu albo usunięciu wpisu, „stays in the map as a withdrawn identifier” — cytat dla S8.
- WAY-44 (`:1126`, `:1129`): „Every file git tracks belongs to exactly one part of the map”; „unless the map lists that file as left out on purpose” — cytat dla S4, S8, S11.
- WAY-48 (`:1205`): „An exchange with the external context records its direction and marks what comes in as untrusted” — cytat dla S8 i S9.
- WAY-61 (`:1480`): metoda `test` oznacza „a test of the product's test suite, written in the product's language” — cytat dla S3.
- WAY-62 (`:1529`): „An invariant entry names the parts of the part map where a change can make its sentence false, or `every`” — cytat dla S5.
- WAY-64 (`:1601-1602`): „an entry taking in a clause of another keeps its identifier, and the other is split” — cytat dla S2.
- WAY-71 (`:1688-1694`, `:1711-1712`): „The main branch holds `TODO` only where an entry stands on something the product's foundation does not hold yet … a change that leaves one there puts it before the human”; przykład naruszenia: „a decision reads `Based on: none` where its source says nothing of what it rests on” — cytat dla S12 i S22.
- WAY-72 (`:1739-1740`): „A product's foundation is written in English, whatever language the product shows the people who use it and whatever language its team speaks.” — podstawa zdania S27.
- WAY-73 (`:1763`): fakt w *Rests on* to ten, którego warunek trzyma zdanie niezmiennika, „and no other fact” — cytat dla S6 i S7.
- WAY-90 (`:2053`): wpisem faktu staje się cytat, „that, once it stopped being true, would call the decision into question” — cytat dla S7.
- WAY-99 (`:2233-2235`): „A file of a product in another language uses its words in the meaning they have in that language, and the rules of the glossary do not reach it.” — podstawa zdania S27.
- WAY-113 (`:2630-2631`): „a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open” — podstawa kroku 4.1 (S20).
- WAY-114 (`:2692-2693`): „Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision” — dzisiejszy krok 4.1 mu przeczy (S20).

## Settlements to record

Candidates: 3 shown, 0 accepted — 2026-11-13

none

## Out of scope

- Dziennik decyzji (`foundations/decisions.md`) się nie zmienia.
- Dopiski S26 (`elements/environment-facts/template.md:138`) i S28 (`elements/invariants/template.md:94`) zostają — zamyka je zadanie z prywatnego backlogu autora o odczycie ustawienia w cudzej usłudze i o warunku niezmiennika, razem z testem, że dopiski nie wracają.
- Sens reguł w sprawach S1–S19 się nie zmienia; poza końcówką S5 przy tych sprawach zmienia się tylko dopisek.
