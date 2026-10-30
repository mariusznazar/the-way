---
title: "the way, seria skilli 9/11: settle-technology w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok"
status: draft
created: 2026-10-30
updated: 2026-10-30
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# settle-technology w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `settle-technology` to jeden plik `project-level/technology/SKILL.md` o 2122 słowach na `foundations` `525cde1`, bez plików obok, a seria przebudowuje wszystkie skille the way do jednego kształtu; ten skill ma do niego dojść dla spójności z resztą skilli, nie dla oszczędności tokenów (pytanie 1).
- Krok 2 („Settle the open choices”, 1091 słów, 51% pliku) potrzebny jest tylko wtedy, gdy na liście wyborów zostaje wybór otwarty, a WAY-256 każe fragment jednego kroku albo wariantu trzymać w pliku obok skilla.
- W jedynym dotąd przebiegu skilla na definicji projektu prowadzący wskazał agentom badawczym ścieżkę całego skilla (`C:\Storage\repos\loop2\.runs\technology-research\brief.md:13`), choć ich pracę opisują tylko kroki 2.1–2.3, ok. 340 słów.

### To do

1. `project-level/technology/SKILL.md` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a procedura kroku albo wariantu — w pliku obok w `project-level/technology/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza (WAY-256, pytanie 7).
2. Opis pracy agenta badawczego — krok 2.1 od zdania „Each finds the options…” oraz kroki 2.2 i 2.3 — stoi w pliku obok skilla, a zdanie „Give each choice of the wave to a fresh agent…” z listą tego, co agent dostaje, zostaje u prowadzącego, razem z resztą kroku 2 w pliku obok, który czyta prowadzący; do tej listy dochodzi ścieżka pliku agenta, a request nazywa tę zmianę listy osobno.
3. Instrukcję krytyki (`elements/common/critique/SKILL.md`) prowadzący czyta dopiero na krokach 2.4 i 2.5, które jej używają, także przy wznowieniu, w którym krok 2.4 odpada, bo wszystkie raporty czytają `critique: passed`; `project-level/definition_template.md` czyta w kroku 0 w całości, jak dziś; request nazywa tę zmianę momentu czytania osobno.
4. Request zadania podaje tabelę oceny skilla — fragment zacytowany dosłownie z zakresem linii na `525cde1`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt — i liczby słów czytanych przed przebudową i po niej na pięciu drogach (słowa w plikach czytanych na danej drodze, każdy plik raz): prowadzący z nową listą bez otwartych wyborów, prowadzący z nową listą z otwartymi wyborami, prowadzący wznawiający pracę z otwartymi wyborami, prowadzący wznawiający pracę bez otwartych wyborów i agent badawczy.
5. W tych liczbach `project-level/definition_template.md`, sekcja „How a skill asks” i sekcja „Reading the foundation” z `elements/common/way_of_working.md` wchodzą raz, jako stały dodatek do dróg prowadzącego; instrukcja krytyki — `elements/common/critique/SKILL.md` i czytane przez autora `prepare.md`, `check.md`, `settle.md` — przed przebudową wlicza się do każdej drogi prowadzącego, a po niej tylko do dróg z krokiem 2; agent badawczy czyta przed przebudową cały `SKILL.md`, jak w jedynym przebiegu, a po niej swój plik, a sekcja „Technology” szablonu definicji jest stałym dodatkiem tej drogi.
6. Werdykty „remove” i „reword” zmieniające treść reguły stoją w requeście jako propozycje, a wśród nich czytanie z szablonu definicji tylko sekcji, których skill używa, z oceną według `instruction-files/judging.md` (pytanie 2).

### Acceptance criteria

- Żadna reguła nie znika ani nie zmienia znaczenia, poza zmianami z To do 2 i 3: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Każdy odsyłacz do pliku obok nazywa swój krok albo wariant słowami, które rozpozna agent, także czytający plik po ścieżce, bez pliku wejściowego skilla.
- Fragment potrzebny w więcej niż jednym miejscu dociera do każdego z nich: spojrzenie na logi, interfejs i dane deweloperskie z kroku 1 także do obu dróg wznowienia (`project-level/technology/SKILL.md:37–40`), a reguła nazwy raportu `.runs/technology/<choice>.md` także do prowadzącego (`:44–45`, `:130`).
- Agent badawczy, mając tylko swój plik i to, co daje mu prowadzący, zna każde użyte tam pojęcie i każdą regułę, która go dotyczy, także tę, że krok nie zapisuje fundamentu produktu (`project-level/technology/SKILL.md:24–25`).
- Kod w Pythonie się nie zmienia.

### Questions to settle

- 1. Czy przebudowujemy ten skill teraz, czy odkładamy zadanie do jego następnego prawdziwego użycia?
  - Answer: przebudowujemy teraz, dla spójności z resztą skilli.
  - Not chosen:
    - odłożyć zadanie do następnego prawdziwego użycia skilla — skill zostaje w starym kształcie, a seria kończy się z jedną otwartą pozycją; zysk: to użycie pokazałoby, gdzie agent się gubi.
  - Source: Mariusz, 2026-10-30: „zróbmy proszę tą zmianę dla spójności z resztą skilli” — wbrew rekomendacji odłożenia. Pytanie podało błędnie, że skill nie był ani razu uruchomiony na definicji projektu; był raz, w Codexie (Context). Powód odpowiedzi, spójność, tego nie dotyczy, a sprostowanie pokazano Mariuszowi przed akceptacją tego dokumentu.
- 2. Co oprócz tekstu `project-level/technology/SKILL.md` przebudowa może ruszyć: moment czytania plików z kroku 0, czy także zakres czytania `project-level/definition_template.md`?
  - Answer: także moment czytania: instrukcję krytyki prowadzący czyta na krokach, które jej używają, nie w kroku 0; `project-level/definition_template.md` czyta dalej w całości, a czytanie z niego tylko używanych sekcji trafia do requestu jako propozycja do osobnej decyzji.
  - Not chosen:
    - A: sam tekst `SKILL.md`, zdanie o czytaniu z kroku 0 bez zmian — prowadzący bez otwartych wyborów dalej czyta krytykę na darmo.
    - C: B i czytanie z szablonu tylko sekcji, których skill używa — ok. 800 słów mniej w każdym przebiegu, ale zmienia zakres czytania, a nie tylko miejsce reguły; prowadzący może nie znać reguły z pominiętej sekcji, a szablonu używa też `define-project`.
  - Source: Mariusz, 2026-10-30: „B” — na rekomendację B, w której wariant C „trafi do PR-a jako propozycja do osobnej decyzji”, ze słabym punktem nazwanym w pytaniu: największa część tekstu, szablon, zostaje bez zmian.
- 3. Czy agent badawczy dostaje kroki 2.1–2.3 we własnym pliku obok skilla?
  - Answer: tak — opis pracy agenta badawczego stoi w pliku obok skilla, reszta kroku 2 w pliku dla prowadzącego, a do listy tego, co prowadzący daje agentowi badawczemu, dochodzi ścieżka tego pliku.
  - Not chosen:
    - A: cały krok 2 w jednym pliku obok skilla — jeden plik mniej, ale prowadzący z otwartymi wyborami musi agentowi przepisać reguły albo wskazać plik z pracą prowadzącego, jak w jedynym przebiegu.
  - Source: Mariusz, 2026-10-30: „B” — na rekomendację B, ze słabym punktem nazwanym w pytaniu: nowa pozycja na liście wychodzi poza czyste przenoszenie, więc recenzent ocenia ją osobno, a PR ją nazywa. Pytanie podało błędnie, że skill nigdy nie działał na prawdziwej definicji; w jedynym przebiegu prowadzący wskazał agentom cały skill (`C:\Storage\repos\loop2\.runs\technology-research\brief.md:13`).
- 4. W jakich drogach użycia request liczy słowa czytane przed przebudową i po niej, i czym po scaleniu mierzymy niesiony tekst?
  - Answer: request liczy słowa na pięciu drogach z To do 4; skrypt serii `skill_carry_cost.py` uruchamiamy przy następnym prawdziwym użyciu skilla, nie przy domknięciu zadania.
  - Not chosen:
    - B: jedna liczba, słowa w `SKILL.md` przed i po — najtaniej, ale wprowadza w błąd: główny plik skurczy się mocno, choć prowadzący z otwartymi wyborami przeczyta prawie tyle samo.
  - Source: Mariusz, 2026-10-30: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: wynik w słowach to liczenie plików, a nie zachowanie agenta.
- 5. Czy agenci cyklu czytają metody z worktree zadania, bez kopii na commicie bazowym?
  - Answer: tak, z worktree zadania, zwykłą drogą cyklu; metody cyklu się nie zmieniają, a cykl nie czyta tego skilla.
  - Not chosen:
    - A: kopia na commicie bazowym — krok więcej na starcie.
  - Source: odpowiedź z zadania 3 (`_zadania/zadanie_skille_the_way_3_fundament.md`, pytanie 3): Mariusz, 2026-10-28, „jeśli uważasz, że B jest lepsze to spoko, dla mnie to żadna różnica” — na rekomendację B (worktree zadania). Stan kodu: `task-cycle/` na `525cde1` nie wymienia `settle-technology`.
- 6. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania 1–3 serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Not chosen:
    - czekanie na wytyczne samego the way — seria stoi.
  - Source: odpowiedź z zadania 3 (`_zadania/zadanie_skille_the_way_3_fundament.md`, pytanie 5): Mariusz, 2026-10-28, „tak”.
- 7. Czy procedura kroku, do którego dochodzi każdy przebieg, idzie do pliku obok, skoro notatka serii i blok przekazania zadania 3 mówią o tym co innego?
  - Answer: tak — procedura każdego kroku idzie do pliku obok także wtedy, gdy dochodzi do niej każdy przebieg, a fragment z jedną instrukcją zostaje w miejscu odsyłacza; WAY-256 się nie zmienia.
  - Not chosen:
    - zostawić obie wersje notatki serii bez rozstrzygnięcia — cykl sam wybierze jedno z dwóch źródeł, a recenzent może ocenić ten wybór według drugiego.
    - kroki każdego przebiegu zostają w `SKILL.md` — niezgodne z brzmieniem WAY-256 i z układem zadania 2.
    - odpowiedź z wyjątkiem „fragment potrzebny od pierwszego kroku zostaje w `SKILL.md`” bez zmiany WAY-256 — stoi w sprzeczności z decyzją, którą recenzent cyklu czyta jako wiążącą.
    - ten sam wyjątek dopisany do WAY-256 — decyzja dostaje trzecią klauzulę, a PR wychodzi poza przebudowę.
  - Source: odpowiedź z zadania 4 (`_zadania/zadanie_skille_the_way_4_maintain_styleguide.md`, pytanie 2): Mariusz, 2026-10-30: „wszystko zgodnie z rekomendacjami” — na drogę „WAY-256 bez zmian, kroki 0 i 1 też idą obok”, ze słabymi punktami pokazanymi w pytaniu: ok. 50 słów więcej w sumie, 1–2 pliki więcej, a tekst czytany zaraz po `SKILL.md` nic nie zyskuje na przeniesieniu.

## Context

- Zadanie jest dziewiątym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię na następne) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Podstawą jest `foundations` po PR #58, commit `525cde1dd53c474f56ea0ece289cb60e868aa90d`; wzór oceny i tabel: zadanie 3 (PR #52, https://github.com/mariusznazar/the-way/pull/52).
- Zadanie wyprzedza w kolejności serii zadania 4–8, bo tak zdecydował Mariusz; skille tych zadań nie dzielą z tym zadaniem plików.
- Zadanie 4 poprawia `instruction-files/kind_skill.md`, którego linie 11 i 13 dają dla kroku każdego przebiegu dwie sprzeczne odpowiedzi; pytanie 7 obowiązuje niezależnie od kolejności scaleń.
- Skill ma za sobą jeden prawdziwy przebieg: sesja Codexa `01a107ae` z 2026-10-04 na definicji MVP `loop2` (`C:\Users\Mariusz\.codex\sessions\2026\10\04\rollout-2026-10-04T18-10-39-01a107ae-806d-71e2-b005-c14a317d7a7f.jsonl.zst`).
- Przebieg trwał ok. 5,5 h, z ok. 45 odpowiedziami Mariusza, 35 agentami pomocniczymi i 20 wyborami (`Notes/Projects/(P) Przejście 10xDEVS/mapa_pakietu_10x.md:86`); jego raporty i krytyki leżą w `C:\Storage\repos\loop2\.runs\technology-research\`, 39 plików.
- Przebieg szedł na tekście skilla z przypięcia `2a8954e` (1335 słów), starszym od dzisiejszego, więc pokazuje zachowanie agenta tylko częściowo.
- Ocena przeszukuje więc zapisy Codexa także w plikach `.jsonl.zst`, bo starsze sesje leżą tylko w nich, a podstawą jej wierszy nie jest „not found”.
- Miara serii, ok. 2,9 mln tokenów i dziewiąty wynik (`ranking_2026-10-28.txt`), liczy tylko zapisy Claude Code, więc tego przebiegu nie obejmuje.
- W zapisach Claude Code `SKILL.md` czytało 41 agentów (liczone szerzej niż ranking, który podaje 22), wszyscy przy pracy nad zmianami the way albo w lekcjach; nie ma tam wywołania `/the-way-settle-technology`, przy 4 wywołaniach `the-way-define-project` jako kontroli pozytywnej.
- Skrypt serii `skill_carry_cost.py` liczy każdy plik `.md` katalogu `project-level/technology/`, więc pliki obok dodane w tym zadaniu też, ale nie widzi Codexa: jeśli następne użycie pójdzie w Codexie, porównanie trzeba policzyć z jego zapisów osobno.
- Poza `project-level/` i wygenerowanymi wejściami `.claude/skills/` oraz `.agents/skills/` skill nazywają tylko `installation/install.py:34`, `installation/README.md:57` i `elements/decisions/skill/projected.md:6`; `define-project` wywołuje go w kroku 6 (`project-level/skill/SKILL.md:139`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. Fragments that stand unchanged are not bound by it.” — według niej przebudowuje się skill (To do 1).
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.”
- **WAY-121** (fragment) — „Before a project definition goes through its readiness gate, a step of its own lists the technology and architecture choices the project needs — such as a language, a framework, a store of data or a place to run — and, for each, either names the decision of the foundation that already holds it or settles it as a projected decision of the definition; a project whose every choice the foundation holds thus settles nothing.” — nie zmienia się; opisuje przebieg bez otwartego wyboru.
- **WAY-122** (fragment) — „The options of each technology choice a project needs come from research of that choice against the project definition, rather than from a fixed list of bundled stacks, and the research of every choice that depends on no unsettled choice starts once the list of choices is confirmed, each in a report of its own.” — nie zmienia się.
- **WAY-123** (fragment) — „The step that settles a project's technology shows the options of each choice by their consequences for the product — what it costs, where it runs, what keeping it running takes and what changing it later costs — and the human chooses between those consequences.” — nie zmienia się.
- **WAY-137** (fragment) — „Where the options of a place to run differ in no consequence for the product and more than one of them is the simplest and cheapest, the step that settles a project's technology recommends, of those, the one an agent works with best: operated from a terminal, deployed by a script and documented in pages an agent can read.” — nie zmienia się.
- **WAY-138** (fragment) — „The step that settles a project's technology tests the option it recommends for each choice it settles, one a constraint of the definition settles included, with a devil's advocate, a pre-mortem and a search for unknown unknowns; it tests no choice a decision of the foundation holds, and no decision already written is tested afterwards.” — nie zmienia się.
- **WAY-165** (fragment) — „Of the matters of an agent's way to the running product, the logs ask where the record of what the running product does goes and how an agent reads it, and the interface asks how an agent operates the product as its user does — through a screen in a browser, a call to its API or a command in a terminal — and how it sees what the product answers.” — nie zmienia się.
- **WAY-166** — „In a choice of an agent's way to the running product, whether an agent can use an option is a consequence for the product: an option an agent cannot use stays in the comparison with that lack said as "an agent does not check the running product this way", and the recommendation passes over it.” — nie zmienia się.
- **WAY-120** (fragment) — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — nie zmienia się; obie krytyki kroku 2 zostają, zmienia się tylko moment czytania (To do 3).
- **WAY-113** (fragment) — „An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel.” — nie zmienia się; niesie ją sekcja „How a skill asks”.
- **WAY-118** (fragment) — „A change to those sections after approval goes through the gate again before breakdown relies on it.” — nie zmienia się; niesie ją zakończenie skilla.
- **WAY-150** (fragment) — „The-way skills read a product's foundation selectively […]” — nie zmienia się; niesie ją sekcja „Reading the foundation”, do której skill odsyła w kroku 0.
- **WAY-106** (fragment) — „The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries.” — nie zmienia się.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in […]” — nie zmienia się.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się.

## Settlements to record

Candidates: 6 shown, 0 accepted — 2026-10-30

none

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 9/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie następnego nieodhaczonego zadania serii i ustawić jego linii datę dnia domknięcia; do „Otwartych wątków” wchodzi też to, że porównanie skryptem `skill_carry_cost.py` czeka na następne prawdziwe użycie skilla (pytanie 4).
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- Tekst `project-level/definition_template.md` — ani jego podział, ani zmiana jego treści (pytanie 2).
- Uwagi z PR-ów #50, #51 i #52 — nie przechodzą do tego zadania.
- Pozostałe skille the way — zadania 4–8, 10 i 11 serii.
