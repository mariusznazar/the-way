---
title: "the way, seria skilli 7/11: find-foundation-entries w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków i wariantów w plikach obok"
status: draft
created: 2026-11-06
updated: 2026-11-06
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# find-foundation-entries w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków i wariantów w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `find-foundation-entries` the way to jeden plik `elements/common/skill/SKILL.md` o 1584 słowach na `foundations` `dfd50e5`, bez pliku obok w swoim katalogu; WAY-256 każe fragment jednego kroku albo wariantu trzymać w pliku obok skilla.
- Skill ma dwa warianty, które wyznacza wołający: wpisy rzutowane definicji projektu (`define-project`, krok 5) i wiersze *Settlements to record* zadania (`refine-task`, krok 5, także w trybie orkiestrowanym i po skillach wytycznych, które oddają pracę do `refine-task`). Różnice stoją przy krokach 1, 2, 4 i 5; krok 3 jest wspólny.
- Tylko definicji projektu służy ok. 600 słów: wartości wołającego (`elements/common/skill/SKILL.md:24–28`), sekcja szablonu definicji i `projected_mode.md` w kroku 1 (`:41–46`), linie definicji i tabela robocza w definicji w kroku 2 (`:60–63`, `:72–74`), krok 4 (`:102–125`) i zamknięcie definicji (`:129–133`).
- Tylko zadaniu służy ok. 420 słów: wartości wołającego (`:30–34`), sekcja szablonu zadania w kroku 1 (`:43–44`, `:55–56`), tabela zadania w kroku 2 (`:75–81`), akapit zamiast kroku 4 (`:93–101`) i zamknięcie zadania (`:134–138`).
- W zapisach Claude Code od 2026-09-01 skill szedł w wariancie zadania w ok. 107 zapisach, a w wariancie definicji raz, więc niemal każdy agent niesie tekst definicji, którego nie użyje.
- Agenci nieśli tekst katalogu `elements/common/skill/` przez ok. 3,5 mln tokenów od 2026-09-01 — siódmy wynik serii, z czego 2,0 mln w sesjach w samym repo the way (miara serii, `ranking_2026-10-28.txt`).

### To do

1. `find-foundation-entries` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a procedura kroku albo wariantu — w pliku obok w `elements/common/skill/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza (WAY-256).
2. Wspólna procedura kroku 1 i kroku 2 stoi w dwóch plikach kroków, a tekst każdego wariantu — definicji projektu i zadania — w jednym pliku tego wariantu, który `SKILL.md` wymienia przy każdym kroku, którego wariant dotyczy, z warunkiem, kiedy się go czyta, i który agent czyta raz, na kroku 1; krok 3 zostaje w `SKILL.md` (pytanie 1).
3. Request podaje tabelę oceny skilla: fragment zacytowany dosłownie z zakresem linii na `dfd50e5`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt i miejsce po przebudowie.
4. Request podaje liczby słów przed przebudową i po niej, tak jak mówi pytanie 4.
5. Request podaje jako propozycje werdykty „remove” i „reword” zmieniające treść reguły, a wśród nich czytanie w wariancie zadania tylko trzech sekcji `elements/common/way_of_working.md` — krytyki zestawu propozycji, sposobu pytania i czytania fundamentu — zamiast całego pliku (pytanie 3).
6. Poza `elements/common/skill/` nic się nie zmienia: wołający skilla, `elements/common/projected_mode.md` i `elements/common/way_of_working.md` zostają, jak są (pytanie 3).

### Acceptance criteria

- Żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Każdy przeredagowany warunek wariantu albo odsyłacza jest porównany z bazą i nie dodaje drogi ani żadnej nie gubi, a przy każdym nowym zdaniu autor nazywa, co ono wyłącza; samo sprawdzenie obecności zdań nie wystarcza.
- Wariant zadania zachowuje to, co dziś bierze z punktu definicji przez „show it whole as above” (`elements/common/skill/SKILL.md:80–81` wobec `:72–74`): proponowane wiersze zaczynają jako `waiting`, wiersze bez konkretnego skutku dla następnego czytelnika jako `rejected`, a tabela jest pokazana cała, z kolumną źródła i następnego czytelnika i z powodem przy każdym odrzuconym wierszu.
- Każdy odsyłacz do pliku obok mówi, czy agent ma plik tylko przeczytać, czy wykonać jego krok, i nazywa krok albo wariant słowami, które rozpozna agent czytający `SKILL.md` po ścieżce, bez pliku wejściowego skilla.
- Agent przysłany przez wołającego rozpozna swój wariant w `SKILL.md` po słowach, którymi wołający go nazywa: „task mode” (`project-level/task/skill/orchestrated_mode.md:17`, `product-guidelines/coding/hand_back.md:24`, `product-guidelines/styleguide/hand_back.md:11`, `product-guidelines/testing/hand_back.md:16`), wiersze *Settlements to record* (`project-level/task/skill/find_settlements.md:4–7`) i wpisy rzutowane do „Projected foundation changes” (`project-level/skill/SKILL.md:129–131`).
- Recenzent przechodzi ręcznie przez obie drogi — wariant zadania i wariant definicji — od `SKILL.md` do pliku ostatniego kroku, tak jak zrobiłby to agent, wypisuje, co na każdej zostaje i co odpada, i porównuje każdy wiersz tabeli oceny z miejscem, w którym fragment naprawdę stanął.
- Opis skilla (`description`) i kod w Pythonie się nie zmieniają, więc wejścia `the-way-*` też nie.
- Liczby słów powstają po ostatniej zmianie liczonego pliku, a pomocniczy skrypt porównuje z plikami każdą liczbę podaną w requeście, także w prozie, nie tylko sumy z raportem.

### Questions to settle

- 1. Jak rozłożyć skill na pliki obok, skoro każde użycie idzie jednym wariantem od początku do końca?
  - Answer: pliki kroków na wspólną procedurę kroku 1 i kroku 2 oraz jeden plik na wariant (definicja projektu, zadanie), wymieniony w `SKILL.md` przy każdym kroku, którego dotyczy, i czytany raz, na kroku 1; krok 3 jako jedna instrukcja zostaje w `SKILL.md`; razem cztery pliki obok.
  - Not chosen:
    - plik na każdy krok w każdym wariancie, ok. 10 plików — ten sam tekst na drodze i ok. 75–100 słów więcej na zdania otwierające; agent nie widzi kroków 4–5 przed czasem, ale dziesięć plików do utrzymania przy skillu o 1584 słowach.
    - tylko dwa pliki wariantów, wspólna część kroków 1 i 2 zostaje w `SKILL.md` — najtańszy w słowach (zadanie ok. 1190, −25%; definicja ok. 1380, −13%), ale wyjątek od ustalenia serii, że procedura każdego kroku idzie do pliku obok także wtedy, gdy dochodzi do niej każdy przebieg, odrzuconego w zadaniu 4 dla pierwszego kroku; recenzent zgłosi niezgodność z WAY-256.
    - zostawić jak jest — nic nie kosztuje, ale skill zostaje niezgodny z WAY-256, seria kończy się z otwartą pozycją, a agent zadania dalej niesie ok. 600 słów tekstu definicji.
  - Source: Mariusz, 2026-11-06: „A” — na rekomendację A, z szacunkiem: zadanie 1584 → ok. 1300–1450 słów (−8 do −18%), definicja 1584 → ok. 1500–1650 (−5 do +4%), suma plików +370–550 słów; ze słabym punktem nazwanym w pytaniu: agent wariantu definicji ma procedurę kroku 4 (ok. 290 słów) w kontekście od kroku 1, a ten wariant zdarza się raz na ok. 100 użyć.
- 2. Czy w wariancie zadania krok 1 czyta sekcję „Projected foundation changes” szablonu definicji, skoro zdanie `elements/common/skill/SKILL.md:41–44` pozwala czytać „for a task” jako „zamiast” albo „dodatkowo”?
  - Answer: nie — polecenie czytania sekcji szablonu definicji trafia do pliku wariantu definicji, a plik wariantu zadania wymienia tylko sekcję *Settlements to record* szablonu zadania; stany wierszy, których zadanie używa, stoją w samym skillu (`:37`, `:134–136`).
  - Not chosen:
    - oba warianty czytają sekcję definicji — bezpieczne wobec dosłownego czytania, ale 674 słowa na każdym użyciu zadania (droga ok. +45%) za tekst, którego zadanie nie używa: tabelę roboczą w definicji, stan `written`, nagłówki wpisów rzutowanych.
    - zostawić zdanie dwuznaczne — pliku nie da się przypisać, autor rozstrzygnie po swojemu, a recenzent zgłosi to tak czy inaczej.
  - Source: Mariusz, 2026-11-06: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: recenzent czytający bazę dosłownie jako „dodatkowo” uzna to za zmianę znaczenia, a chroni przed tym ta odpowiedź i kryterium akceptacji o nazwaniu, co nowe zdanie wyłącza. Stan: w zapisach Claude Code po sekcję definicji sięgnęło 5 ze 107 sesji wariantu zadania.
- 3. Co oprócz `elements/common/skill/` przebudowa może zmienić?
  - Answer: nic — wołający, `elements/common/projected_mode.md` i `elements/common/way_of_working.md` zostają bez zmian; czytanie w wariancie zadania tylko trzech sekcji `way_of_working.md` (ok. 800 z 1752 słów) trafia do requestu jako propozycja.
  - Not chosen:
    - węższe czytanie `way_of_working.md` w wariancie zadania już w tym PR-ze — do ok. 950 słów mniej w sesjach, które nie miały tego pliku w kontekście, ale drugi po zadaniu 8 wyjątek od ustalenia serii, recenzent ocenia treść, nie tylko miejsce, a pomiar po scaleniu pokazuje skutek dwóch zmian naraz.
    - granica nienazwana — autor sam decyduje, czy dotknąć wołających, a recenzent ocenia bez punktu odniesienia.
  - Source: Mariusz, 2026-11-06: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: największa pojedyncza oszczędność czeka na osobną decyzję. Stan: żaden plik spoza skilla nie odsyła do jego sekcji ani kroku; `projected_mode.md` czytają też skille elementów w trybie rzutowanym; `way_of_working.md` w całości przed skillem przeczytało 47 ze 107 sesji wariantu zadania, a 22 wcale.
- 4. Na jakich drogach request liczy słowa przed przebudową i po niej?
  - Answer: na dwóch — wariant zadania i wariant definicji, bo nowe szukanie, wznowienie z tabeli roboczej i tryb orkiestrowany w `refine-task` czytają w jednym wariancie ten sam tekst skilla. Na każdej drodze: (1) sam tekst skilla; (2) suma z plikami czytanymi obok — `elements/common/way_of_working.md`, sekcja szablonu zadania albo definicji, `elements/common/projected_mode.md` w wariancie definicji; (3) w wariancie zadania ta sama suma bez tego, co krok 1 `refine-task` przeczytał wcześniej: cały szablon zadania oraz sekcje „How a skill asks” i „Reading the foundation” `way_of_working.md`. Odsyłacz „Read <plik>” liczy się jako przeczytanie i wykonanie. Słowa liczy skrypt jak `wc -w`, w stanie „przed” na `dfd50e5`; dokument źródłowy, definicja i pliki produktu są poza liczeniem.
  - Not chosen:
    - jedna liczba na drogę, sam tekst skilla — krótszy opis, ale znika to, że `way_of_working.md` waży więcej niż cały skill, i wynik wygląda lepiej, niż agent go odczuje.
    - drogi bez ustalenia — autor wybiera je sam; w zadaniu 6 dało to dwie liczby za dobre, które wyłapał dopiero recenzent.
  - Source: Mariusz, 2026-11-06: „tak” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: to liczby słów w plikach, a nie zachowanie agenta.
- 5. Kiedy i czym mierzymy niesiony tekst po scaleniu?
  - Answer: przy następnym prawdziwym użyciu skilla w `loop2`, skryptami serii z datą początkową po scaleniu, nie przy domknięciu zadania; do tego czasu główną miarą zostają słowa z requestu, a gdy użycie pójdzie w Codexie, porównanie liczy się osobno z jego zapisów.
  - Not chosen:
    - pomiar przy domknięciu — liczba mówi tylko, ile czasu minęło, a wygląda jak wynik.
  - Source: odpowiedź z zadania 8 (`_zadania/zadanie_skille_the_way_8_maintain_coding_guidelines.md`, pytanie 6): Mariusz, 2026-10-31: „Tak” — ze słabymi punktami nazwanymi tam: porównanie może długo czekać, a `skill_carry_cost.py` potrzebuje parametru daty. Przeniesienie pokazano Mariuszowi 2026-11-06 w pytaniu 4, z dopiskiem, że wariant definicji szedł od 2026-09-01 raz, więc jego porównanie może czekać szczególnie długo; Mariusz, 2026-11-06: „tak”.
- 6. Czy agenci cyklu czytają metody z worktree zadania, jak w poprzednich zadaniach serii?
  - Answer: tak — z worktree zadania, zwykłą drogą cyklu, bez kopii na commicie bazowym; `task-cycle/` nie wymienia `find-foundation-entries`, więc przebudowa nie zmienia niczego, czym cykl pracuje.
  - Not chosen:
    - kopia the way na commicie bazowym — krok więcej na starcie, który nic nie chroni.
  - Source: odpowiedź z zadania 8 (`_zadania/zadanie_skille_the_way_8_maintain_coding_guidelines.md`, pytanie 7): Mariusz, 2026-10-31: „Tak”. Stan kodu: `task-cycle/` na `dfd50e5` nie wymienia tego skilla. Przeniesienie pokazano Mariuszowi 2026-11-06 w pytaniu 4; Mariusz, 2026-11-06: „tak”.
- 7. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak wcześniejsze zadania serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Not chosen:
    - czekać na wytyczne samego the way — seria stoi bez żadnego zysku.
  - Source: odpowiedź z zadania 8 (`_zadania/zadanie_skille_the_way_8_maintain_coding_guidelines.md`, pytanie 8): Mariusz, 2026-10-31: „Tak”. Stan: na `dfd50e5` the way nie ma katalogu `guidelines/`. Przeniesienie pokazano Mariuszowi 2026-11-06 w pytaniu 4; Mariusz, 2026-11-06: „tak”.

## Context

- Zadanie jest siódmym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, procedura każdego kroku idzie do pliku obok także wtedy, gdy dochodzi do niej każdy przebieg, domknięcie zadania przestawia serię) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcje „Ustalone” i „Otwarte wątki / decyzje”.
- Podstawą jest `foundations` po PR #76, commit `dfd50e513c09bebe9d09d74209cd28612565da83`; `elements/common/skill/SKILL.md` zmienił się ostatnio w `1267e73` (2026-10-29) i od PR #69 stoi bez zmian.
- Zapisy Claude Code od 2026-09-01 (sesje i subagenci) dają 188 zapisów, w których agent sięgnął po ścieżkę skilla, w tym 133 pełne odczyty (Read bez zakresu, `cat` albo narzędzie Skill); w ok. 107 z nich sesja szła przez `refine-task`, a jedyne użycie wariantu definicji to `define-project` w `loop2` 2026-11-01 (`a2c2a1d6`), z wywołaniami `record-decision`, `record-invariant`, `record-glossary-term`, `record-environment-fact` i `update-part-map`.
- Pozostałe pełne odczyty to praca nad samym the way (cykle zmieniające ten skill albo jego wołających) i trzech agentów kroku fundamentu cykli w `loop2` (`1d1a68d6`, `eb9f59e0`, `b53bd467`), którzy otworzyli skill sami, choć `task-cycle/` go nie wymienia.
- W wariancie zadania sesja przed skillem przeczytała już cały szablon zadania w 89 ze 107 zapisów, `way_of_working.md` w całości w 47, w części albo poleceniem powłoki w kolejnych, a w 22 wcale; po skillu sekcję szablonu definicji czytało 5 zapisów, a `projected_mode.md` jeden.
- Pliki, które skill każe czytać obok siebie: `elements/common/way_of_working.md` w całości, 1752 słowa, w obu wariantach; sekcja „Projected foundation changes” szablonu definicji, `project-level/definition_template.md:260–348`, 674 słowa; sekcja *Settlements to record* szablonu zadania z jej regułą, `project-level/task/template.md`, 424 słowa; `elements/common/projected_mode.md`, 419 słów, w wariancie definicji.
- Zdanie kroku 1 (`elements/common/skill/SKILL.md:41–44`) nie mówi jednoznacznie, czy w wariancie zadania sekcja szablonu definicji jest czytana obok sekcji szablonu zadania, czy zamiast niej.
- Żaden plik spoza skilla nie odsyła do jego sekcji ani kroku; wołający wymieniają skill w całości: `project-level/skill/SKILL.md:129`, `project-level/task/skill/find_settlements.md:4`, `project-level/task/skill/orchestrated_mode.md:17`, `product-guidelines/coding/hand_back.md:24`, `product-guidelines/styleguide/hand_back.md:11`, `product-guidelines/testing/hand_back.md:16`, `task_document.md` tych trzech katalogów, `project-level/task/template.md:183`, `project-level/definition_template.md:265` i `elements/common/projected_mode.md:4`, `:26`.
- `installation/install.py:30` przypisuje nazwie skilla ścieżkę `elements/common/skill/SKILL.md`; żaden test nie wymienia tego pliku z nazwy, a `task-cycle/` nie wymienia skilla.
- W zapisach Codexa (78 plików `.jsonl`, 547 `.jsonl.zst`) ścieżka skilla pada w 80, przy kontroli pozytywnej 128 plikach ze ścieżką `project-level/task/skill`; żaden z tych 80 nie jest sesją w `loop2`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. A fragment that some steps of the skill need, not all, stands by what it is: a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did; fragments that stand unchanged are not bound by it.” — według niej przebudowuje się skill.
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.” — nie zmienia się.
- **WAY-265** — „In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file points to is named in the skill's `SKILL.md` at that step as well, with the condition under which it is read. A step's file that stands unchanged, with the variant file it points to, is not bound by it.” — nie zmienia się.
- **WAY-35** (fragment) — „An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them” — nie zmienia się; reguły wpisów zostają w szablonach elementów.
- **WAY-115** (fragment) — „The agent reads the project's sources in full and selects and reads the product's foundation under WAY-150, then shows the human a complete candidate table with each proposed settlement, its kind, its source and the concrete choice or action the next reader would otherwise have to guess; a row without such a consequence is shown as rejected. The human accepts or rejects rows before they are handed to the skills of their kinds, and each accepted row is recorded as it is worked through.” — nie zmienia się; niesie wspólny kształt tabeli obu wariantów.
- **WAY-134** (fragment) — „Before a task is ready for its cycle, the human sees a table of candidates found in the task document and the conversation that refined it, in the form WAY-115 gives with each settlement in the human's words, and the task document keeps the rows the human accepts […] A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on, and a settlement that a current entry the refinement reads for the parts the task touches, or a projected entry the task carries, already states is no candidate.” — nie zmienia się; niesie wariant zadania.
- **WAY-117** (fragment) — „The skill of each entry's kind writes its whole proposal under the definition's `Projected foundation changes` […] without searching the whole foundation for the entry: the readiness gate searches it once for the whole definition (WAY-118).” — nie zmienia się; niesie wariant definicji.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in” — nie zmienia się; droga sesji na samym the way.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się; droga sesji w produkcie.

## Settlements to record

Candidates: 11 shown, 0 accepted — 2026-11-06

none

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 7/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie zadania 10 (`lead-project`), bo zadania 8 i 9 są już scalone, i ustawić linii „seria skilli 10/11” datę dnia domknięcia.
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- Uwagi z PR-ów #50–#52, #59, #60, #62, #64 i #69 — nie przechodzą do tego zadania, poza tymi, które rozstrzygają jego pytania.
- Pozostałe skille the way — zadania 10 i 11 serii.
