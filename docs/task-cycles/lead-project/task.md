---
title: "the way: prowadzenie planu projektu — skill lead-project"
status: draft
created: 2026-10-15
updated: 2026-10-15
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]"]
---

# the way: prowadzenie planu projektu — skill lead-project

Status: ready for cycle
Project relation: independent

## Description

### Need

- Po oddaniu planu projektu (`plan-project`, krok 7) nic nie prowadzi jego zadań do stanu `ready for cycle`: każde zadanie Mariusz doprecyzowuje osobno skillem `refine-task` w rozmowie.
- Nikt nie utrzymuje stanów zadań w planie: w planie MVP `loop2` zadanie 3 `mag-w-lesie` stoi na `ready for cycle`, choć jest scalone (`loop2` PR #12).
- Mariusz chce orkiestratora, z którym rozmawia i który zleca pracę agentom, a który „dba o to, żeby stan planu był aktualny i żeby nic nie ginęło”.

### To do

1. Dodać skill `lead-project` (`project-level/lead/skill/SKILL.md`), którym orkiestrator projektu — agent, z którym rozmawia człowiek; dalej „orkiestrator” — prowadzi oddany plan projektu od zadań `to refine` do zadań przyjętych przez człowieka w stanie `ready for cycle` i utrzymuje zgodność stanów planu z rzeczywistością.
2. Orkiestrator nie uruchamia cykli zadań; cykl uruchamia człowiek — sam `implement-task` w osobnej sesji albo innym narzędziem.
3. Orkiestrator nie przeprowadza domknięcia projektu; gdy ostatnie zadanie planu jest `done`, mówi, że następne jest domknięcie, a skilla na nie jeszcze nie ma.
4. Orkiestrator nie trzyma stanu między sesjami: wszystko, czego potrzebuje, stoi w planie, w dokumentach zadań i w plikach rozmów.
5. Na początku każdej sesji orkiestrator odczytuje stan: skrypt `project-level/plan_state.py <plan> <repo produktu>` wypisuje proponowane przejścia z dowodami, a orkiestrator nanosi je z wierszem w dzienniku zmian planu:
    - `ready for cycle` → `in cycle`: któryś worktree produktu ma `.runs/task-cycles/<nazwa-zadania>/` albo w którejś gałęzi jest commit dotykający `docs/task-cycles/<nazwa-zadania>/`;
    - `in cycle` → `done`: commit z zapisem cyklu jest w głównej gałęzi produktu po pobraniu stanu zdalnego;
    - skrypt uruchamia tylko gita (WAY-38/1); gdy git nie rozstrzyga — PR scalony przez squash, zamknięty bez scalenia albo otwarty — skrypt wypisuje zadanie jako niesprawdzone, a orkiestrator sprawdza stan PR narzędziem drogi PR, którą wybrał produkt, albo pyta człowieka, gdy tego narzędzia nie ma;
    - PR zamknięty bez scalenia i ślad niezgodny z planem orkiestrator pokazuje człowiekowi i niczego nie poprawia sam.
6. Orkiestrator proponuje rundę — zadania do doprecyzowania w tej sesji, najpierw te, od których zależy najwięcej innych — a człowiek ją potwierdza albo zmienia.
7. Doprecyzowanie zadania z rundy idzie turami przez plik rozmowy `<repo produktu>/.runs/project-refinement/<nazwa-zadania>.md`; zadania rundy idą równolegle:
    - świeży agent doprecyzowujący wykonuje `refine-task` dla członka planu, wpisuje do pliku pytania, których nie rozstrzygnął z plików, i kończy turę jednym słowem: `questions`, `waits for task <n>`, `ready for approval`, `plan change` albo `obstacle`;
    - agent odpowiadający dopisuje pod każdym pytaniem odpowiedź albo pytanie do człowieka;
    - orkiestrator podaje agentom tylko ścieżkę pliku i pilnuje kolejności tur, treści między nimi nie przenosi;
    - w następnej turze świeży agent doprecyzowujący przenosi rozstrzygnięte odpowiedzi ze źródłem do `Questions to settle` dokumentu zadania.
8. Dokument zadania zmienia tylko agent doprecyzowujący; orkiestrator zmienia w nim wyłącznie linię `Status:` po przyjęciu przez człowieka.
9. Agent odpowiadający odpowiada tylko cytatem ze źródłem — definicja, plan, fundament, dokumenty innych zadań — albo faktem z kodu ze wskazaniem `plik:linia`. Na pytanie o to, jak ma być, odpowiada tylko cytatem z dokumentu, nigdy z kodu. Gdy żadne źródło nie daje odpowiedzi, zapisuje pytanie do człowieka z wariantami, rachunkiem i rekomendacją. Widzi pliki rozmów innych zadań rundy, więc to samo pytanie trafia do człowieka raz.
10. Do człowieka orkiestrator przynosi jedną paczkę z całej rundy: pytania, kandydatów na wpisy fundamentu (`Settlements to record`), umieszczenie `Human actions` i propozycje brzmienia, a po wyborze, który wejdzie do części wiążącej wpisu, pytanie przekorne (WAY-113). Do paczki dołącza listę odpowiedzi, których agent odpowiadający udzielił cytatem — pytanie, cytat, źródło — a odpowiedź skreślona przez człowieka wraca jako pytanie do niego. Odpowiedzi człowieka wpisuje do plików rozmów i zleca kolejną turę.
11. Gotowy dokument (`ready for approval`) orkiestrator pokazuje człowiekowi w całości, po jednym. Dopiero przyjęcie daje `ready for cycle` w dokumencie i w planie; plik rozmowy zostaje wtedy skasowany.
12. Stany w planie w czasie doprecyzowania: tura w toku, `questions` i `waits for task <n>` — `to refine`; paczka dla człowieka i `ready for approval` — `waiting for human`.
13. `waits for task <n>`: zadanie zostaje w stanie `to refine` z wierszem w dzienniku zmian planu; gdy odczyt stanu pokaże, że zadanie `n` jest `done`, orkiestrator proponuje je w najbliższej rundzie.
14. `plan change`: podział zadania w tym samym zakresie, nowe zadanie w zatwierdzonym zakresie, kolejność i zależności orkiestrator zleca subagentowi ze skillem `plan-project`, z wierszem w dzienniku zmian; zmiana zakresu idzie do człowieka.
15. Zmianę definicji projektu przeprowadza się przez bramkę. Samą zmianę orkiestrator nanosi sam tylko wtedy, gdy dotyczy tekstu, który już ma przed sobą, i nie wymaga czytania innych sekcji definicji ani fundamentu; inaczej zleca ją subagentowi. Krok 7 `define-project` zawsze przechodzi subagent; niezależną krytykę uruchamia orkiestrator i przekazuje jej uwagi subagentowi; zatwierdza człowiek w rozmowie z orkiestratorem; potem świeży subagent sprawdza plan od nowa (`plan-project`, krok 0). Na czas bramki żadne zadanie nie dostaje `ready for cycle`.
16. `refine-task` dostaje tryb prowadzony przez orkiestratora: agent nigdy nie pyta człowieka, każde pytanie zapisuje do pliku rozmowy i kończy turę.
17. Zadanie jest gotowe do cyklu dopiero wtedy, gdy człowiek zobaczył dokument w całości i go przyjął — dla każdego zadania, także doprecyzowanego ręcznie `refine-task` (zmiana WAY-124).
18. `Depends on` w planie projektu blokuje start cyklu, nie doprecyzowanie (zmiana WAY-144 i szablonu planu).
19. `plan-project` w kroku 7 wskazuje `lead-project` jako następny krok po oddaniu planu.

### Acceptance criteria

- Na planie MVP `loop2` odczyt stanu proponuje dla zadania 3 `mag-w-lesie` przejście do `done` z dowodem (PR #12).

## Context

- Opis orkiestratora słowami Mariusza: notatka m2l1 „krok 3, grupa 1” w [[mapa_pakietu_10x]]; różnice wobec [[szkic_poziomu_projektu]] (recenzja planu przez drugiego agenta, agent odpowiadający, przyjęcie dokumentu przez człowieka, zmiana definicji przez orkiestratora) rozstrzygnięte w sesji z 2026-10-15.
- Recenzję planu przez drugiego agenta `plan-project` już ma (krok 6, WAY-120).
- W Claude Code subagent nie uruchamia własnych subagentów, dlatego agenta odpowiadającego, krytyka bramki i subagenta zmiany planu uruchamia orkiestrator.
- Uruchamianie cykli z orkiestratora wymagałoby osobnych sesji (`implement-task` sam rozsyła subagentów) — odrzucone na rzecz odczytu stanu; dispatch Cezara (`C:\Storage\repos\open-mercato-cezar`) zostaje drogą uruchamiania poza the-way.
- Po scaleniu zadania orkiestrator nie sprawdza gotowych zadań od niego zależnych: krok 1 `implement-task` sprawdza źródła na starcie i dopasowuje zadanie (`task-cycle/skill/SKILL.md:31`).
- Pierwszym poligonem jest plan MVP `loop2`: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Loop\plan_mvp_loop2.md` — 21 zadań, 18 w stanie `to refine`.
- Katalog `.runs/` jest w `.gitignore` produktu z instalatora the-way (`installation/README.md:60`), więc plik rozmowy nie trafia do commita.

## Questions carried to cycle

- Jaki dokładny kształt ma plik rozmowy i słowa kończące turę?
- Ile nowych decyzji niosą ustalenia tego zadania i jak się dzielą?

## Human actions

none

## Decisions in play

Zderzenia — zadanie zmienia brzmienie (przed `main`: edycja w miejscu, zmiana znaczenia przyjmowana ponownie, WAY-07/1):

- WAY-124/1 — punkt 17 dokłada warunek przyjęcia całego dokumentu przez człowieka:
  > It is ready when its required outcome is stated, every known question blocking that outcome is answered, the human has accepted or rejected every candidate settlement its refinement found, every human action it places before the cycle is done (WAY-140), and implementation questions carried into the cycle are named. A project member also matches its plan item's scope, dependencies and assigned entries; any task using an approved definition checks that its approval still holds and names each projected entry, or the part of it, that its code makes true, while source-only use takes no other assignment or dependency from the plan.
- WAY-144/1 — punkt 18 zmienia, przed czym blokuje zależność; przykład zgodności w *Verification* („work on the plan takes up two tasks at once because neither depends on the other”) dotyczy odtąd startu cyklu:
  > Which tasks of a project plan can be worked on side by side follows from the tasks each depends on alone: two tasks of which neither depends on the other, directly or through other tasks, can. The plan holds no field naming the tasks a task can be worked on beside, and its order of work follows the dependencies.
- WAY-134/1 — w trybie prowadzonym tabelę kandydatów pokazuje człowiekowi orkiestrator w paczce, nie agent doprecyzowujący (punkt 10):
  > Before a task is ready for its cycle, the agent refining it shows the human a table of candidates found in the task document and the conversation that refined it, in the form WAY-115 gives with each settlement in the human's words, and the task document keeps the rows the human accepts.
- WAY-09/1 — lista zawartości `project-level/` nie obejmuje skilla prowadzenia ani skryptu odczytu stanu (punkty 1 i 5):
  > `project-level/` the templates of a project definition, a project plan and a task document, the skills that write them, the readiness check, the plan check and their tests

Odciski zmienianych decyzji cytują: `project-plan-form/1` (WAY-144), sześć niezmienników położenia plików (WAY-09), WAY-124/1 i WAY-135/1 (WAY-134); każdy dostaje nowy odcisk (WAY-31/1).

Dotykane — zadanie ich nie zmienia:

- WAY-38/1 i niezmiennik `script-subprocesses/1` — `plan_state.py` uruchamia tylko gita, a stan PR, którego git nie rozstrzyga, sprawdza orkiestrator (punkt 5; Mariusz: „na razie niech będzie A”):
  > It calls git, and the commands a product declares in its own repository — a dependency graph, a detector of breaking changes, coverage — reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.

  > No script git tracks starts a program other than git or a command the product declares in its repository.
- WAY-150/1 — orkiestrator i wszyscy jego agenci czytają fundament produktu wybiórczo:
  > The-way skills default to selective reading of the product's foundation: they use the complete part map and existing entry links to choose material for the work, read selected entries whole, and expand the reading whenever the work or an uncertain relevance needs more context.
- WAY-151/1 — wiąże subagenta zmiany planu (`plan-project`, punkt 14); orkiestrator czytający plan i agent odpowiadający czytający definicję mogą przyjąć ten sam sposób:
  > The-way's plan-project limits reading of large project definitions and existing plans to the material needed for the work, starting from complete inventories of scope items, projected entries, open questions and existing tasks and their dependencies and assignments, then reading complete source units and expanding whenever their meaning or dependencies reach further.
- WAY-145/1 — wśród naruszeń: „the breakdown answers a question from its own reading of the code”; agent odpowiadający odpowiada z kodu tylko na pytanie o to, jak jest (punkt 9):
  > Once a project definition has passed its readiness gate, the place of resolution it gives an open question is the question's first assignment, and the plan decides from then on where the question is resolved: in a task of the plan, or by an answer the human gives or the plan quotes, with its place, from the definition or the foundation. Work on the plan may move a question to another task, with an entry in the plan's log of changes giving the reason and without taking the definition through its readiness gate again, while a move that changes which task writes a projected entry into the foundation is the human's to decide.
- WAY-118/1 — punkt 15 je zachowuje:
  > A change to those sections after approval goes through the gate again before breakdown relies on it.
- WAY-113/1 — pytanie przekorne po wyborze, który wejdzie do części wiążącej wpisu, zadaje w trybie prowadzonym orkiestrator w paczce:
  > After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way.
- WAY-125/1 — „orchestrator” znaczy tu orkiestratora cyklu zadania; wpis o prowadzeniu planu nie może użyć tego słowa w drugim znaczeniu:
  > The orchestrator answers workflow questions and gives provisional stage go-aheads under the task owner's delegation, never records these as human approval, controls the return between stages, keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment of its foundation change and its return step, and brings the request to the human for review.
- WAY-142/1 — stany zadań i dziennik zmian, które pisze orkiestrator:
  > Each task stands in one row of one table of tasks, with the columns and states the plan template gives […] and a log of its changes, each with its reason, written in the language of the definition under headings, states and markers kept in English.
- WAY-147/1 — nazwa zadania, po której odczyt stanu znajduje ślady cyklu:
  > A task of the plan enters its cycle under that name, and the cycle names its record by it.
- WAY-106/1 — orkiestrator nie pisze wpisów fundamentu:
  > The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries.
- WAY-36/1 — reguła prowadzenia wiąże po scaleniu, więc jest decyzją, a nie planem pracy:
  > A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition between two states — stays in the plan of that work.
- WAY-127/1 i niezmiennik `skill-entry-points/1` — nowy `SKILL.md` dostaje punkty wejścia `the-way-lead-project`:
  > A session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`.
- WAY-10/1 i WAY-33/1 — niezależna ocena zmiany fundamentu i dwa przeszukania całego fundamentu:
  > A change to an invariant test or to the foundation is assessed by one independent agent, on a model other than its author's where one is available, which sees the diff and the files of the commit it assesses without the task's chronicle or the author's reasoning and names what of the change can be cut, or that nothing can.

  > The search runs again against the current main branch before the task branch is merged, and a change to the foundation is merged only with the record of both searches.
- Mapa części, część `project-level` (`foundations/part_map.md:96`) — odpowiedzialność nie obejmuje prowadzenia planu ani odczytu śladów cyklu; tryb awarii „an agent fills a missing human answer with a plausible settlement” (wysoki, niewykrywany) dotyczy agenta odpowiadającego.

## Settlements to record

Candidates: 10 shown, 10 accepted — 2026-10-15

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Prowadzenie oddanego planu doprowadza zadania `to refine` do zadań przyjętych przez człowieka w stanie `ready for cycle` i utrzymuje stany planu; cykli nie uruchamia i projektu nie domyka, a zadania rundy potwierdza człowiek. | decision | wybór „A z odczytem stanu będzie ok”; szkielet — „Tak” | czy `lead-project` uruchamia `implement-task` i czy przeprowadza domknięcie |
| 2 | Stany zadań w planie biorą się ze śladów cyklu zadania; skrypt odczytu stanu używa tylko gita, czego git nie rozstrzyga, sprawdza orkiestrator, a ślad niezgodny z planem idzie do człowieka. | decision | odczyt stanu — „Tak”; WAY-38 — „na razie niech będzie A” | czy stan wpisuje cykl, człowiek, czy skrypt wywołujący narzędzie PR |
| 3 | Agenci doprecyzowania „gadają po prostu przez jakiś plik tymczasowy dawany im przez orkiestratora i wywalany po doprecyzowanie zadania”; orkiestrator treści nie przenosi, dokument zadania pisze tylko agent doprecyzowujący, a rozmowa nie zostaje, bo „liczy się wynikowy efekt czyli opis zadania”. | decision | Mariusz o roli przekaźnika; tura doprecyzowania — „Tak”; pytanie przekorne o skasowanie pliku | czy orkiestrator przekazuje treść pytań i odpowiedzi; gdzie leży plik, czy trafia do commita i czy zostaje po doprecyzowaniu |
| 4 | Agent odpowiadający odpowiada cytatem ze źródłem albo faktem z kodu ze wskazaniem `plik:linia`; jak ma być — tylko z dokumentu, bo „jeśli w zadaniu albo projekcie jest ta informacja, to nie musi do mnie”; resztę zamienia w pytanie do człowieka z wariantami, rachunkiem i rekomendacją. Odpowiedzi z cytatu stoją w paczce rundy listą — pytanie, cytat, źródło — a skreślona wraca jako pytanie do człowieka. | decision | wybór B; Mariusz o pytaniach „jak ma być”; pytanie przekorne — „bierzemy listę w paczce” | czy agent odpowiadający może rozstrzygnąć pytanie własnym wnioskiem i czy człowiek widzi odpowiedzi z cytatu przed zatwierdzeniem dokumentu |
| 5 | Zadanie jest gotowe do cyklu dopiero wtedy, gdy człowiek zobaczył dokument w całości i go przyjął. | decision | propozycja zmiany WAY-124 — „Aaa, ok w tą stronę ok” | czy zadanie bez kandydatów na wpisy staje się gotowe bez człowieka |
| 6 | Zależność w planie blokuje start cyklu, nie doprecyzowanie; doprecyzowanie czeka na zadanie tylko tam, gdzie wskaże to jego pytanie. | decision | wybór C — „O, super pomysł z tym C” | czy doprecyzowanie zadania czeka na scalenie wszystkich zadań, od których zależy |
| 7 | Zmiana definicji w trakcie prowadzenia idzie przez bramkę, którą zawsze przechodzi subagent, bo orkiestrator nie wykonuje, tylko zleca; samą zmianę nanosi sam tylko wtedy, gdy dotyczy tekstu, który już ma przed sobą, i nie wymaga czytania innych sekcji definicji ani fundamentu; zatwierdza człowiek. | decision | wybór C — „C, ale najlepiej, żeby wykonania nie robił tylko zlecił”; pytanie przekorne — „bierzemy […] tę granicę” | czy orkiestrator poprawia definicję sam, czy omija bramkę i kiedy zleca |
| 8 | W prowadzeniu kandydatów na wpisy fundamentu i pytania przekorne pokazuje człowiekowi orkiestrator w paczce rundy, nie agent doprecyzowujący. | decision | tura doprecyzowania — „Tak” | kto w trybie prowadzonym pokazuje człowiekowi tabelę kandydatów |
| 9 | Po scaleniu zadania gotowych zadań zależnych nie sprawdza się w prowadzeniu; dopasowanie do zmienionych źródeł robi start cyklu zadania. | decision | „Zostawiamy cyklowi” | czy odczyt stanu ma ponownie oceniać gotowe dokumenty zadań zależnych |
| 10 | W fundamencie prowadzący plan to „project orchestrator” (orkiestrator projektu); gołe „orchestrator” zostaje przy cyklu zadania. | glossary term | materiał: WAY-125/1; Mariusz: „może faktycznie project orchestrator będzie ok” | jakim słowem wpisy o prowadzeniu nazywają prowadzącego, i czy „orchestrator” dostaje drugie znaczenie |

## Out of scope

- Rewizja [[szkic_poziomu_projektu]] o kroki 4–5 — osobne zadanie w vaulcie.
- Zawężenie niezależnej krytyki przy ponownej bramce definicji do tego, czego zmiana dotyka.
- Skill domknięcia projektu.
