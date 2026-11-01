---
title: "the way, seria skilli 6/11: plan-project w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok"
status: draft
created: 2026-11-01
updated: 2026-11-01
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# plan-project w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `plan-project` the way to jeden plik `project-level/plan/skill/SKILL.md` o 2344 słowach na `foundations` `2f51e6c`, a obok niego stoi tylko szablon planu `project-level/plan/template.md` (1881 słów); WAY-256 każe fragment jednego kroku albo wariantu trzymać w pliku obok skilla.
- W `SKILL.md` stoją fragmenty potrzebne tylko w jednym wariancie: „Delegated work while leading a plan” (`project-level/plan/skill/SKILL.md:23–46`), potrzebna tylko agentowi zleconemu przez `lead-project`, praca na istniejącym planie (`:52–61`) oraz zadania wytycznych (`:115–127`), potrzebne tylko wtedy, gdy odczyt wytycznych coś znalazł.
- Sekcja „Reading the definition and plan” (`:79–106`) stoi między krokami 1 i 2, choć czytają ją krok 0 i krok 1, a poza skillem odsyła do niej `project-level/lead/skill/SKILL.md:30–32`.
- Agenci nieśli tekst katalogu `project-level/plan/` przez ok. 3,7 mln tokenów od 2026-09-01 — szósty wynik serii, z czego 0,5 mln w sesjach w samym repo the way (miara serii, `ranking_2026-10-28.txt`).

### To do

1. `plan-project` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a procedura kroku albo wariantu — w pliku obok w `project-level/plan/skill/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza, a fragment potrzebny na niektórych krokach stoi według swojego rodzaju (WAY-256).
2. Kroki zachowują numery od 0 do 7, a nagłówek „Delegated work while leading a plan” zostaje w `SKILL.md` przy odsyłaczu do pliku trybu zleconego, którego zdanie „follow this workflow with these routing differences” się nie zmienia (pytanie 1).
3. Sekcja „Reading the definition and plan” stoi w pliku obok, wymienionym przez kroki 0 i 1, a jej zdania o tym, że oryginały są nadrzędne i każde sprawdzenie idzie na całych plikach (`project-level/plan/skill/SKILL.md:81–83`), zostają w `SKILL.md`, bo agent trzyma się ich przy każdym uruchomieniu sprawdzenia, także na krokach 5–7.
4. Zdanie w `project-level/lead/skill/SKILL.md:30–31` wskazuje ten plik zamiast sekcji `SKILL.md`; to jedyna zmiana w tym skillu (pytanie 2).
5. Praca na istniejącym planie (`:52–61`) stoi w pliku obok, który wskazuje też plik kroku 1 (pytanie 3).
6. Zadania wytycznych z kroku 2 (`:115–127`) stoją w pliku wariantu, do którego odsyła plik kroku 2 i który `SKILL.md` wymienia przy tym kroku, z warunkiem, kiedy się go czyta (WAY-265).
7. Request podaje tabelę oceny skilla: fragment zacytowany dosłownie z zakresem linii na `2f51e6c`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt i miejsce po przebudowie.
8. Request podaje liczby słów przed przebudową i po niej, tak jak mówi pytanie 4.
9. Request podaje jako propozycje werdykty „remove” i „reword” zmieniające treść reguły, a wśród nich powtórzenia między skillem a `project-level/plan/template.md` (pytanie 2).

### Acceptance criteria

- Poza To do 4 i 5 żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Każdy przeredagowany warunek trybu, wariantu albo odsyłacza jest porównany z bazą i nie dodaje drogi ani żadnej nie gubi, a przy każdym nowym zdaniu autor nazywa, co ono wyłącza; samo sprawdzenie obecności zdań nie wystarcza.
- Warunek pliku zadań wytycznych obejmuje wszystko z `project-level/plan/skill/SKILL.md:115–127`: brakujące wytyczne, pierwszy plik rodzaju, istniejący rodzaj bez wpisu w indeksie, pierwszy test poziomu i rozszerzenie istniejących wytycznych.
- Każdy odsyłacz do pliku obok nazywa swój krok albo wariant słowami, które rozpozna agent czytający `SKILL.md` po ścieżce, bez pliku wejściowego skilla.
- Recenzent przechodzi ręcznie przez pliki drogi 2, 3, 4, 5 i 7 z pytania 4, od `SKILL.md` do pliku ostatniego kroku, tak jak zrobiłby to agent, wypisuje, co na każdej zostaje i co odpada, i porównuje każdy wiersz tabeli oceny z miejscem, w którym fragment naprawdę stanął.
- Fragment potrzebny w więcej niż jednym miejscu dociera do każdego z nich: zdania o pytaniu do człowieka w kroku 5 z kroków 2–4 (`:125`, `:135`, `:142–143`, `:160–163`) do pliku kroku 5, wynik `plan_check.py` o dwóch zadaniach realizujących jeden wpis (`:59–61`) do plików kroków 3 i 7, a zdanie „A new complete breakdown processes every scope item, projected entry and exact question” (`:105–106`) do kroków 2–4.
- Plik trybu zleconego dociera do kroków 5–7: agent zlecony nie pyta człowieka sam ani nie uruchamia krytyki sam, choć pliki tych kroków mówią o tym bez zastrzeżenia.
- Opis skilla (`description`) i kod w Pythonie się nie zmieniają, więc wejścia `the-way-*` też nie.
- Liczby słów powstają po ostatniej zmianie liczonego pliku, a pomocniczy skrypt porównuje każdą podaną liczbę z plikiem, nie tylko sumy z raportem.

### Questions to settle

- 1. Czy agent w wąskiej turze zleconej przez `lead-project` dostaje wprost zgodę na czytanie tylko tych kroków, których dotyczy jego zlecenie?
  - Answer: nie — bez nowego zdania; zdanie „follow this workflow with these routing differences” (`project-level/plan/skill/SKILL.md:27`) przechodzi do pliku trybu zleconego bez zmiany, pliki kroków mają nazwy, po których agent pozna swój krok, a o tym, co agent wykonuje, mówi zlecenie.
  - Not chosen:
    - jedno nowe zdanie w pliku trybu zleconego, że tura wykonuje tylko kroki, których dotyczy jej zlecenie — drugi po zadaniu 8 wyjątek od ustalenia „Przebudowa zmienia miejsce reguł, nie ich treść” i nowa reguła bez decyzji, która by ją niosła; agent, który dzieli zadanie i pominie krok o przypisaniu wpisów fundamentu, może przeoczyć, że ta zmiana wymaga zgody człowieka, a `plan_check.py` tego nie wyłapie.
  - Source: Mariusz, 2026-11-01: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: oszczędność zależy od tego, jak agent odczyta zdanie o całym przebiegu; jeśli przeczyta wszystko, zapłaci ok. 450–900 słów więcej niż dziś, a sprawdzi to pierwszy prawdziwy przebieg. Szacunek samego tekstu skilla: wąska tura czytająca swoje kroki ok. 1650–1850 słów wobec 2344, czytająca wszystko ok. 2800–3250, nowe rozbicie ok. 2300–2900. Pytanie zaniżyło pierwszą liczbę, bo nie liczyło pliku kroku 1, który dochodzi przez pytanie 3: wąska tura czytająca swoje kroki to ok. 1800–2000 słów; sprostowanie pokazano Mariuszowi 2026-11-01 przed jego odpowiedzią na pytanie 3 i nie zmienia ono porównania obu dróg.
- 2. Co oprócz tekstu `project-level/plan/skill/SKILL.md` przebudowa może ruszyć?
  - Answer: jedno zdanie w `project-level/lead/skill/SKILL.md:30–31`, które odsyła do sekcji „Reading the definition and plan”: po przebudowie wskazuje plik obok skilla, do którego sekcja przejdzie. `project-level/plan/template.md` się nie zmienia i dalej jest czytany w całości w kroku 0; powtórzenia między nim a skillem trafiają do requestu jako propozycje.
  - Not chosen:
    - zostawić skill jak jest — nic nie kosztuje, ale skill zostaje niezgodny z WAY-256, seria kończy się z otwartą pozycją, a zyski z pytania 1 przepadają.
    - tylko `SKILL.md`, sekcja o czytaniu zostaje w nim — `lead-project` bez zmian, ale główny plik jest o ok. 300 słów dłuższy, niezgodnie z WAY-256, więc recenzent zapewne to zgłosi.
    - także czytanie szablonu dopiero na krokach, które go używają — oszczędza 1881 słów tylko przy samym oddaniu planu (1 z 14 użyć) i gdy definicja nie przejdzie sprawdzenia; kosztuje dopisek przy ok. 5 odsyłaczach, razem ok. 60–75 słów, i ryzyko, że agent pisze plan bez szablonu.
    - także usunięcie powtórzeń między szablonem a skillem — to nie jest już przenoszenie, tylko zmiana pliku czytanego przez `lead-project` i `refine-task`, poza ustaleniem serii; zysk to kilkaset słów, ale recenzent musiałby ocenić treść, a nie tylko miejsce.
  - Source: Mariusz, 2026-11-01: „B” — na rekomendację B, ze słabymi punktami nazwanymi w pytaniu: PR dotyka skilla, którego przebudowa jest w zadaniu 10, a największy tekst, szablon, zostaje bez zmian.
- 3. Czy agent pracujący na istniejącym planie dostaje po przebudowie krok 1, skoro `project-level/plan/skill/SKILL.md:54–55` każe szkicowi iść od pierwszego kroku, którego sekcje są niedokończone, a krok 1 nie zostawia w planie żadnej sekcji?
  - Answer: tak — plik pracy na istniejącym planie wskazuje plik kroku 1, a sesja, która go jeszcze nie czytała, czyta go, zanim pójdzie dalej.
  - Not chosen:
    - bez odsyłacza, dosłownie według zdania o szkicu — oszczędza ok. 170 słów, ale po cichu wyłącza to, co dziś robią wszystkie sesje; agent zmienia plan bez fundamentu w głowie, a jedyną ochroną zostaje `plan_check.py`, który wykryje zmianę definicji, ale nie zderzenie z decyzją.
  - Source: Mariusz, 2026-11-01: „A” — na rekomendację A, z kosztem ok. 170 słów na każdej drodze z istniejącym planem i ze słabym punktem nazwanym w pytaniu: to nowy odsyłacz, którego w bazie nie ma, więc recenzent musi sprawdzić, że nie dodaje drogi, a jedynie zachowuje to, co agent widział. Stan: w 14 sesjach z Context `readiness_check.py` uruchomiono w każdej, a do `foundations/` produktu sięgnięto w 11. Odsyłacz nie dostaje wiersza *Settlements to record*: stoi już w WAY-256 („a step after the first having that file read unless an earlier step did”, a uzasadnienie dodaje „a session that skipped the earlier step reads the file there”) i w WAY-150, więc zdanie w skillu powołuje się na nie, a tabela oceny podaje powód; Mariusz, 2026-11-01: „tak jak rekomendujesz” — ze słabym punktem nazwanym przy cięciu: praca na istniejącym planie nie ma osobnej decyzji, więc ktoś mógłby to zdanie usunąć, nie wiedząc, po co stoi.
- 4. Na jakich drogach użycia request liczy słowa przed przebudową i po niej?
  - Answer: na siedmiu: (1) nowe rozbicie, gdy odczyt wytycznych nic nie znalazł; (2) nowe rozbicie z plikiem zadań wytycznych; (3) wznowienie szkicu od kroku 5; (4) korekta człowieka do oddanego planu, np. podział zadania; (5) wąska tura zlecona z jedną zmianą, w dwóch wersjach: agent czyta swoje kroki albo wszystko; (6) tura samego oddania planu; (7) ponowne sprawdzenie po bramce definicji. Na każdej dwie liczby: sam tekst skilla oraz suma z plikami czytanymi obok, czyli `project-level/plan/template.md`, sekcjami `elements/common/way_of_working.md`, `project-level/lead/conversation_template.md`, `product-guidelines/reading.md` i plikami krytyki, tam, gdzie droga do nich dochodzi. Dokument definicji, plan i pliki produktu są poza liczeniem. Słowa liczy skrypt jak `wc -w`, w stanie „przed” na `2f51e6c`.
  - Not chosen:
    - trzy drogi (1, 5 i 7) — krótszy opis, ale znika pierwszy plan nowego produktu i korekta człowieka, a tylko one pokażą koszt pliku wytycznych i pliku pracy na istniejącym planie.
    - jedna liczba, słowa w `SKILL.md` — najtaniej, ale pokaże ok. −70% zamiast realnych −15 do +25%, a ktoś może oprzeć na tym wniosek o serii.
  - Source: Mariusz, 2026-11-01: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: to liczby słów w plikach, a nie zachowanie agenta. Do tej odpowiedzi Mariusz spytał, czy liczy to agent, czy skrypt, bo agentowo to spory nakład; odpowiedź: liczy skrypt, a pracą agenta jest przejście dróg przez recenzenta, zawężone w kryteriach akceptacji do pięciu dróg.
- 5. Kiedy i czym mierzymy niesiony tekst po scaleniu?
  - Answer: przy następnym prawdziwym użyciu skilla w `loop2`, skryptami serii z datą początkową po scaleniu, nie przy domknięciu zadania; do tego czasu główną miarą zostają słowa z requestu, a gdy użycie pójdzie w Codexie, porównanie liczy się osobno z jego zapisów.
  - Not chosen:
    - pomiar przy domknięciu — liczba mówi tylko, ile czasu minęło, a wygląda jak wynik.
  - Source: odpowiedź z zadania 8 (`_zadania/zadanie_skille_the_way_8_maintain_coding_guidelines.md`, pytanie 6): Mariusz, 2026-10-31: „Tak” — ze słabymi punktami nazwanymi tam: porównanie może długo czekać, a `skill_carry_cost.py` potrzebuje parametru daty. Przeniesienie pokazano Mariuszowi 2026-11-01 w pytaniu 4.
- 6. Czy agenci cyklu czytają metody z worktree zadania, jak w poprzednich zadaniach serii?
  - Answer: tak — z worktree zadania, zwykłą drogą cyklu, bez kopii na commicie bazowym; `task-cycle/` nie wymienia `plan-project`, więc przebudowa nie zmienia niczego, czym cykl pracuje.
  - Not chosen:
    - kopia the way na commicie bazowym — krok więcej na starcie, który nic nie chroni.
  - Source: odpowiedź z zadania 8 (`_zadania/zadanie_skille_the_way_8_maintain_coding_guidelines.md`, pytanie 7): Mariusz, 2026-10-31: „Tak”. Stan kodu: `task-cycle/` na `2f51e6c` nie wymienia tego skilla. Przeniesienie pokazano Mariuszowi 2026-11-01 w pytaniu 4.
- 7. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak wcześniejsze zadania serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Not chosen:
    - czekać na wytyczne samego the way — seria stoi bez żadnego zysku.
  - Source: odpowiedź z zadania 8 (`_zadania/zadanie_skille_the_way_8_maintain_coding_guidelines.md`, pytanie 8): Mariusz, 2026-10-31: „Tak”. Przeniesienie pokazano Mariuszowi 2026-11-01 w pytaniu 4.

## Context

- Zadanie jest szóstym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Podstawą jest `foundations` po PR #66, commit `2f51e6c31f5911ac8a0292a80a4f599bd4bd0092`; między PR #64 a tym commitem `project-level/plan/` się nie zmienił.
- W zapisach Claude Code skill wywołano narzędziem Skill w 14 sesjach, wszystkie w `loop2`, od 2026-10-11 do 2026-10-30: jedno nowe rozbicie (`01246b80`), jedna korekta człowieka do oddanego planu (`b813b629`), jedno ponowne sprawdzenie w sesji doprecyzowania zadania (`9baf7986`) i 11 tur agentów zleconych przez `lead-project`.
- Tych 11 tur to wąska praca, każda nazwana w zleceniu: zastosowanie żądanej zmiany planu (4), przygotowanie propozycji bez edycji planu (1), rozliczenie krytyki (1), wpisanie odpowiedzi człowieka (2), samo oddanie planu (1), ponowne sprawdzenie po bramce definicji (2).
- Żadna z tych 14 sesji nie sięgnęła do katalogu `guidelines/` produktu, choć w `loop2` on istnieje, a krok 1 każe czytać wytyczne dotkniętych części.
- W poleceniach `command-name>/the-way-plan-project` nie ma poza tą sesją żadnej, przy kontroli pozytywnej 98 wystąpieniach `/the-way-refine-task`; ludzie uruchamiali skill przez wklejony opis albo przez `lead-project`.
- W zapisach Codexa (625 plików, `.jsonl` i `.jsonl.zst`) ścieżka skilla pada w 61, przy kontroli pozytywnej 143 plikach ze ścieżką `project-level/task/skill`; pięć z nich to sesje w `loop2`, a w żadnej z tych pięciu narzędzie nie czyta tego pliku. Pozostałe to praca nad samym the way albo notatkami.
- Numerów kroków używają inne pliki: `project-level/lead/skill/SKILL.md:214` i `project-level/skill/SKILL.md:49` („step 0”) oraz WAY-156 („plan-project step 0”).
- Nazwę sekcji „Delegated work while leading a plan” powtarzają w zleceniach orkiestratorzy `lead-project` (wszystkie 11 zleceń), choć `lead-project` jej nie nazywa.
- Krok 0 nie ma pozycji przeczytanych wcześniej, jak skille wytycznych po `refine-task`: agent tury zleconej i sesja nowego rozbicia startują od zera, a krytykę autor czyta dopiero na kroku 6; odczyt do pominięcia zdarza się tylko w sesji, która przyszła z innego skilla, np. „How a skill asks” (208 słów).
- `task-cycle/` nie wymienia tego skilla; wymieniają go `installation/install.py:32`, `installation/README.md:57`, `product-guidelines/reading.md:90`, `project-level/lead/skill/SKILL.md:31`, `:193`, `:214`, `project-level/skill/SKILL.md:49`, `:179` i `project-level/task/skill/project_plan_task.md:8`; żaden test nie wymienia go z nazwy.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. A fragment that some steps of the skill need, not all, stands by what it is: a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did; fragments that stand unchanged are not bound by it.” — według niej przebudowuje się skill.
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.” — nie zmienia się.
- **WAY-265** — „In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file points to is named in the skill's `SKILL.md` at that step as well, with the condition under which it is read. A step's file that stands unchanged, with the variant file it points to, is not bound by it.” — nie zmienia się.
- **WAY-151** — „The-way's plan-project limits reading of large project definitions and existing plans to the material needed for the work, starting from complete inventories of scope items, projected entries, open questions and existing tasks and their dependencies and assignments, then reading complete source units and expanding whenever their meaning or dependencies reach further. A new breakdown covers every scope item, projected entry and open question, and a resumed change reads all units its dependencies or meaning reach, with the original whole documents remaining the inputs to the existing readiness and plan checks. The plan's one independent critique reads the complete plan and every source unit needed for its whole semantic judgment under WAY-146, independently of the author's selection.” — nie zmienia się.
- **WAY-156** — „An in-scope task split, new task, order or dependency change is delegated to a plan-project agent and logged with its reason, while a scope change goes to the human, as does a reassignment of the task writing a projected entry (WAY-145). The project orchestrator changes definition text itself only when that text is already before it and needs no reading of other definition sections or the foundation; otherwise it delegates the edit, and a subagent always performs the definition's readiness gate, with independent critique dispatched by the project orchestrator and its findings returned to that subagent, and human approval given through the project orchestrator. A fresh subagent then checks the plan again through plan-project step 0, and no task gains ready for cycle while that definition gate remains open.” — nie zmienia się; wiąże numer kroku 0.
- **WAY-145** (fragment) — „Work on the plan may move a question to another task, with an entry in the plan's log of changes giving the reason and without taking the definition through its readiness gate again, while a move that changes which task writes a projected entry into the foundation is the human's to decide. A question that arises only in the breakdown goes to the human before the plan is handed over.” — nie zmienia się.
- **WAY-146** (fragment) — „A check a script can make is never left to the critique.” — nie zmienia się.
- **WAY-143** (fragment) — „A task of a project plan ends with something that can be checked in the running product, never with a layer of the product put in place” — nie zmienia się.
- **WAY-218** (fragment) — „The skill `plan-project` uses the same reading of product guidelines as refinement and the task cycle, and places a task for a missing styleguide, general coding guidelines or testing guidelines before the tasks that need it, with those tasks depending on it, reusing an adequate task the plan already holds” — nie zmienia się.
- **WAY-230** (fragment) — „Two tasks of a project plan that realize the same projected entry go one after the other: one depends on the other, directly or through other tasks, unless an item of the plan's change log lets the two go side by side on that entry and gives the reason, and the breakdown shows each such item to the human when it hands the plan over.” — nie zmienia się.
- **WAY-120** (fragment) — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — nie zmienia się.
- **WAY-113** (fragment) — „An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel.” — nie zmienia się; niesie ją sekcja „How a skill asks”.
- **WAY-150** (fragment) — „The-way skills read a product's foundation selectively […]” — nie zmienia się; niesie ją sekcja „Reading the foundation”, do której skill odsyła w kroku 1.
- **WAY-106** (fragment) — „The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries.” — nie zmienia się.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix.” — nie zmienia się; droga sesji na samym the way.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się; droga sesji w produkcie.

## Settlements to record

Candidates: 6 shown, 0 accepted — 2026-11-01

none

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 6/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie zadania 7 (`find-foundation-entries`) i ustawić linii „seria skilli 7/11” datę dnia domknięcia.
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- Uwagi z PR-ów #50–#52, #59, #60, #62 i #64 — nie przechodzą do tego zadania, poza tymi, które rozstrzygają jego pytania.
- Pozostałe skille the way — zadania 7, 10 i 11 serii.
