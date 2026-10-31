---
title: "the way, seria skilli 5/11: maintain-testing-guidelines w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok"
status: draft
created: 2026-10-30
updated: 2026-10-31
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# maintain-testing-guidelines w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `maintain-testing-guidelines` the way to jeden plik `product-guidelines/testing/SKILL.md` o 3042 słowach na `foundations` `00c0a74`, a obok niego tylko szablon; WAY-256 każe fragment jednego kroku albo wariantu trzymać w pliku obok skilla.
- W `SKILL.md` stoją fragmenty potrzebne tylko w jednym wariancie: „Orchestrated mode” (`product-guidelines/testing/SKILL.md:82–90`), potrzebny tylko sesji prowadzonej przez `lead-project`, badania z kroku 2 (`:140–156`), potrzebne tylko przy pierwszych wytycznych bez preferencji człowieka i przy rozszerzeniu, audyt z kroku 3 (`:160–173` i `:180–183`), potrzebny tylko produktowi z testami, oraz „A new level” (`:174–179`), potrzebne tylko zadaniu, którego wynikiem jest pierwszy test poziomu.
- Krok 0 (`:92–104`) każe na wejściu przeczytać ok. 7700 słów z innych plików, dwa i pół raza tyle co sam `SKILL.md`, w tym 2835 słów, które sesja wczytała już w krokach 1 i 2 `refine-task`.
- Agenci nieśli tekst katalogu `product-guidelines/testing/` przez ok. 4,0 mln tokenów od 2026-09-01 — piąty wynik serii (miara serii, `ranking_2026-10-28.txt`).

### To do

1. `maintain-testing-guidelines` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a procedura kroku albo wariantu — w pliku obok w `product-guidelines/testing/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza (WAY-256).
2. Krok 0 przestaje kazać czytać wszystko naraz: każdy plik, który wymienia, jest czytany na kroku, który go potrzebuje, a to, co sesja przeczytała już w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz. Pozycje kroku 0 wobec tego, co czyta `refine-task` (`project-level/task/skill/read_sources.md`, `product-guidelines/reading.md`):
   - czytane już w całości, nie czytać drugi raz: `project-level/task/skill/SKILL.md` (396 słów), `project-level/task/template.md` (1739), sekcja „How a skill asks” (208) i sekcja „Reading the foundation” (492), razem 2835 słów;
   - czytane częściowo: `guidelines/` — `refine-task` czyta tylko pliki, których *Applies to* wymienia dotknięte części (`product-guidelines/reading.md:40`), więc skill czyta te pozostałe; główny `AGENTS.md` produktu — `refine-task` czyta tylko sekcję `## Backlog` (`read_sources.md:17`), więc skill czyta go w całości; fundament — dochodzą tylko pozycje dodane w kroku 0: decyzje o technologii, decyzje o narzędziu testów, poziomie, teście wzorcowym, wyłączeniu i odstępstwie od szablonu oraz granice zaufania z mapy części;
   - nieczytane przez `refine-task`, zostają na swoim kroku: `product-guidelines/template.md` (1336), `product-guidelines/testing/template.md` (3187), sekcja „Critique before collective review” (54), `elements/common/critique/SKILL.md` (322) z plikami obok (509).
3. Szablon `product-guidelines/testing/template.md` jest przeczytany przed pierwszym krokiem, który go używa, na każdej drodze, także na drodze „A new level” tam, gdzie przepis poziomu już stoi z pustym *Exemplar* (`product-guidelines/reading.md:77–78`), bo ta droga nie przechodzi przez krok 2 (`product-guidelines/testing/SKILL.md:120`). Poziom bez przepisu to rozszerzenie (WAY-251) i idzie przez krok 2.
4. `instruction-files/kind_skill.md:8–14` dostaje trzecią odpowiedź, dla fragmentu potrzebnego na niektórych krokach, w brzmieniu z pytania 2, a skill testów jest według niej przebudowany.
5. Plik wariantu, do którego odsyła plik kroku, jest wymieniony także w `SKILL.md` przy tym kroku (pytanie 3).
6. Krok 0 skilla testów i krok 0 `product-guidelines/styleguide/SKILL.md` (`:65–69`) kończą się zdaniem z pytania 4, które sesję bez kroków 1 i 2 `refine-task` odsyła najpierw do nich; to jedyna zmiana w skillu styleguide'u.
7. Request zadania podaje tabelę oceny skilla — fragment zacytowany dosłownie z zakresem linii na `00c0a74`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt, oraz osobny wiersz o wyborze z pytania 3 — i liczby słów czytanych przed przebudową i po niej, tak jak mówi pytanie 6, na sześciu drogach: pierwsze wytyczne, brak testów, człowiek bez preferencji; to samo, człowiek z preferencją; są testy, nie ma wytycznych, bez preferencji, a także rozszerzenie; odświeżenie; „A new level” z przepisem, który już stoi, bez kroku 2; tryb orkiestrowany na pierwszej z tych dróg. Słowa liczy się jak `wc -w`, w stanie „przed” na `00c0a74`; pierwsza liczba, tekst wczytany przed krokiem 4, i druga, suma do końca, obejmują pierwszy odczyt w `refine-task` (2835 słów); pliki obok krytyki (509 słów) wchodzą tam, gdzie droga do nich dochodzi. Werdykty „remove” i „reword” zmieniające treść reguły stoją w nim jako propozycje.

### Acceptance criteria

- Żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Każdy odsyłacz do pliku obok nazywa swój krok albo wariant słowami, które rozpozna agent czytający `SKILL.md` po ścieżce, bez pliku wejściowego skilla.
- Recenzent przechodzi każdą drogę ręcznie przez pliki, od `SKILL.md` do pliku ostatniego kroku, tak jak zrobiłby to agent; samo sprawdzenie, że nazwany tekst jest obecny, nie wystarcza.
- Fragment potrzebny w więcej niż jednym miejscu dociera do każdego z nich: „How to show” (`product-guidelines/testing/SKILL.md:187–194`) także do pytania o preferencje w kroku 2, a „What reaches the task document” (`:47–80`) do kroków 4 i 5, przy czym kroki 1 i 3 same mówią, co dopisują do dokumentu.
- Agent na drodze „A new level” nie czyta audytu, a agent audytu nie czyta „A new level”, gdy żadnego nowego poziomu nie ma.
- Kod w Pythonie się nie zmienia.

### Questions to settle

- 1. Co oprócz tekstu `product-guidelines/testing/SKILL.md` przebudowa może ruszyć: moment czytania plików z kroku 0, czy także `product-guidelines/testing/template.md`?
  - Answer: `SKILL.md` i moment czytania plików z kroku 0 (To do 1–3); same te pliki się nie zmieniają, także `product-guidelines/template.md`, `product-guidelines/testing/template.md` i `product-guidelines/reading.md`.
  - Not chosen:
    - zostawić skill jak jest — ok. 14 100 słów do końca skilla; skill zostaje w starym kształcie, niezgodnym z WAY-256.
    - tylko tekst `SKILL.md`, krok 0 bez zmian — ok. 13 650–14 300 słów, praktycznie bez zmiany; dochodzi 8–10 plików, a zysku nie ma.
    - także wydzielenie z szablonu części dla autora w cyklu — najwyżej 97 słów mniej; rusza plik, którego używa autor w cyklu, a nazwę sekcji „Writing the file” skill wpisuje do opisów zadań w produktach (`product-guidelines/testing/SKILL.md:53–54`).
  - Source: Mariusz, 2026-10-30: „ok C” — na drogę o szacunku ok. 11 100–11 800 słów do końca skilla (−16 do −21%) i ok. 7600–9000 przed krokiem 4 zamiast 13 600–14 100, z kosztem pokazanym w pytaniu: 8–10 plików więcej do utrzymania, łączny tekst większy o ok. 300–700 słów, szablon testów dalej czytany w całości na każdej drodze. Liczby to szacunek z liczenia słów na `00c0a74`, razem z pierwszym odczytem w `refine-task`; w zadaniu 4 końcowe liczby wyszły o ok. 700–1000 słów wyżej od szacunku.
- 2. Co robimy z fragmentem potrzebnym na dwóch albo trzech krokach, ale nie na wszystkich, skoro `instruction-files/kind_skill.md:8–14` zna tylko „każdy krok” i „jeden krok albo wariant”?
  - Answer: reguła według rodzaju fragmentu (To do 4): to, czego agent ma się trzymać przy pracy na tych krokach, zostaje w `SKILL.md`; to, do czego zagląda, stoi w pliku obok, każdy z tych kroków ten plik wymienia, a krok późniejszy każe go przeczytać, jeśli wcześniejszy tego nie zrobił. Wszystkie trzy rozwiązania z zadania 4 są z nią zgodne, więc skill styleguide'u się nie zmienia.
  - Not chosen:
    - bez reguły, każdy przypadek rozstrzyga tabela oceny — każde z sześciu kolejnych zadań rozstrzyga to od nowa, a recenzent może zablokować każdy wybór.
    - wszystko, co potrzebne na więcej niż jednym kroku, zostaje w `SKILL.md` — `SKILL.md` rośnie o ok. 400 słów, które agent nosi przez kroki, gdzie są zbędne, a układ `task_document.md` z zadania 4 przestaje się zgadzać.
  - Source: Mariusz, 2026-10-31: „C” — na proponowane brzmienie „**some steps need it, not all** — a rule of working the agent has to keep during those steps stays in `SKILL.md`; text it reads or consults, such as a procedure, a list or a template, stands in a file beside the skill, each of those steps names that file, and a step after the first has it read unless an earlier step did.”, ze słabym punktem nazwanym w pytaniu: granica między regułą pracy a tekstem do zajrzenia wymaga oceny, a fragment może być jednym i drugim; o miejscu decyduje wtedy wiersz tabeli oceny, a recenzent może się nie zgodzić. Rzeczy, na których pytanie to pokazało: szablon testów (kroki 2, 3, 4), instrukcja krytyki (2 i 4), „How to show” (2 i 4), „What reaches the task document” (pytanie podało kroki 1, 3, 4, 5; sprostowane: listy potrzebują kroki 4 i 5, a kroki 1 i 3 same mówią, co dopisują).
- 3. Czy plik kroku może odsyłać dalej do pliku wariantu, skoro `instruction-files/SKILL.md:174` mówi „one level deep”?
  - Answer: tak, jak w `refine-task`: plik kroku wskazuje plik wariantu w chwili, gdy agent go potrzebuje, a `SKILL.md` wymienia ten plik przy tym kroku (To do 5); `instruction-files/SKILL.md` się nie zmienia, a tabela oceny pokazuje ten wybór w osobnym wierszu. To wzór dla zadań 5 i 8; skill styleguide'u zostaje w układzie dwóch poziomów, dopóki ktoś nie weźmie tej uwagi z PR #60.
  - Not chosen:
    - dwa poziomy jak w zadaniu 4 — układ zostaje niezgodny z regułą; trzeba ją zmienić albo przyjąć, że recenzent zgłosi to w zadaniach 5, 8 i następnych.
    - warianty zostają w pliku kroku — każdy przebieg czyta warianty, których nie potrzebuje, np. ok. 220 słów badań przy odświeżeniu, sprzecznie z celem WAY-256.
  - Source: Mariusz, 2026-10-31: „B” — z kosztem pokazanym w pytaniu: ok. 30–45 słów więcej w `SKILL.md` i nazwa pliku w dwóch miejscach, a skill styleguide'u różni się od skilla testów. Wzór: `project-level/task/skill/SKILL.md:29–32`. Podstawa reguły: fakt `claude-skill-nested-references`; najdłuższy plik kroku w zadaniu 4 ma 42 linie, więc ryzyko częściowego odczytu jest w praktyce małe.
- 4. Co robi sesja, która otworzyła skill bezpośrednio albo wznowiła pracę i nie ma w pamięci tego, co czytał `refine-task`?
  - Answer: przechodzi najpierw przez kroki 1 i 2 `refine-task`; mówi to jedno zdanie na końcu kroku 0, w skillu testów i w `product-guidelines/styleguide/SKILL.md` (To do 6). Zadanie 8 powtórzy je dla skilla kodu.
  - Not chosen:
    - bez zdania — sesja otwarta bezpośrednio albo wznowiona pracuje bez szablonu zadania, a uwaga z PR #60 powtórzy się w zadaniach 5 i 8.
    - zdanie tylko w skillu testów — styleguide zostaje z tą samą luką, a uwaga z PR #60 dalej czeka.
    - krok 0 i tak każe przeczytać te rzeczy ponownie — wraca 2835 słów w każdym przebiegu, czyli znika większość zysku z pytania 1.
  - Source: Mariusz, 2026-10-31: „C” — na brzmienie „A session that has not read them in this conversation — it opened this skill directly, or resumed the work in a new one — goes through `refine-task` steps 1 and 2 first.”, z kosztem pokazanym w pytaniu: ok. 30 słów w każdym przebiegu i PR dotyka skilla spoza zadania, oraz ze słabym punktem: zdanie nie łapie sesji, której rozmowa została streszczona w trakcie pracy. Pytanie podało błędnie, że to nie nowe znaczenie i że nie potrzebuje wpisu do fundamentu: `product-guidelines/testing/SKILL.md:28–29` opisuje zwykłą drogę, nie to, co robi sesja otwarta bezpośrednio, a notatka serii nazywa to nową regułą; sprostowane przed przyjęciem wiersza 3 *Settlements to record*, Mariusz, 2026-10-31: „przyjmuję tak jak rekomendujesz”. Stan: oba prawdziwe przebiegi szły przez `refine-task`; wznowień w nowej rozmowie nie liczono.
- 5. Czy agent badawczy dostaje własny plik obok skilla, jak w zadaniu 9?
  - Answer: nie — jak w zadaniu 4: plik wariantu z badaniami jest dla prowadzącego, który przekazuje agentowi reguły w zleceniu; lista tego, co agent dostaje, się nie zmienia.
  - Not chosen:
    - osobny plik agenta, jak w zadaniu 9 — jeden plik i ok. 60–100 słów więcej, a nowa pozycja na liście wychodzi poza czyste przenoszenie; zysk ok. 1000 słów na agenta, tylko w przebiegu z badaniami.
  - Source: Mariusz, 2026-10-31: „A” — ze słabym punktem nazwanym w pytaniu: gdy prowadzący zapomni o regule „każde źródło to strona z wersją”, agent jej nie zobaczy, a wyłapie to dopiero krytyka raportu. Dla agenta ważne są ok. 45 słowa z `product-guidelines/testing/SKILL.md:147–150`, wobec ok. 340 słów w zadaniu 9; agent, któremu prowadzący wskaże skill, przeczyta ok. 1000 słów zamiast 3042.
- 6. Na jakich drogach użycia request liczy słowa przed przebudową i po niej?
  - Answer: na sześciu z To do 7; na każdej trzy liczby: tekst wczytany przed krokiem 4, suma do końca razem z plikiem ostatniego kroku oraz ta suma bez pierwszego odczytu w `refine-task`; plik czytany dwa razy w stanie „przed” liczy się dwa razy, a pliki produktu są poza liczeniem.
  - Not chosen:
    - jedna liczba, słowa w `SKILL.md` — pokazuje ok. −67% zamiast ok. −20%, czyli wynik zawyżony.
    - wszystkie połączenia trybów, w tym zadanie wspólne z wytycznymi kodu — dokłada drogi o tych samych plikach, a zadanie wspólne zależy od skilla kodu, który czeka na zadanie 8.
  - Source: Mariusz, 2026-10-31: „A” — ze słabym punktem nazwanym w pytaniu: to liczby słów w plikach, a nie zachowanie agenta, a droga wspólna z wytycznymi kodu nie będzie policzona. Pytanie pokazało drogę „A new level” bez warunku; sprostowane: bez kroku 2 idzie tylko poziom, którego przepis już stoi (WAY-251).
- 7. Kiedy i czym mierzymy niesiony tekst po scaleniu?
  - Answer: przy następnym prawdziwym użyciu skilla w `loop2`, skryptami serii z datą początkową po scaleniu, nie przy domknięciu zadania; gdy użycie pójdzie w Codexie, porównanie liczy się osobno z jego zapisów.
  - Not chosen:
    - pomiar przy domknięciu, jak w zadaniu 4 — liczba mówi tylko, ile czasu minęło, a wygląda jak wynik; ktoś może na niej oprzeć wniosek o przebudowie.
  - Source: Mariusz, 2026-10-31: „A” — ze słabymi punktami nazwanymi w pytaniu: porównanie może długo czekać, więc do tego czasu główną miarą zostają słowa z requestu, a `skill_carry_cost.py` ma datę początkową wpisaną na sztywno i trzeba mu dodać parametr daty. Stan: notatka serii, „Otwarte wątki / decyzje”, punkt „Porównanie kosztu po zadaniu 4 jest jeszcze puste”.
- 8. Czy procedura kroku, do którego dochodzi każdy przebieg, idzie do pliku obok?
  - Answer: tak — procedura każdego kroku idzie do pliku obok także wtedy, gdy dochodzi do niej każdy przebieg, kroki 0 i 1 włącznie, a fragment z jedną instrukcją zostaje w miejscu odsyłacza; WAY-256 się nie zmienia.
  - Not chosen:
    - zostawić obie wersje notatki serii bez rozstrzygnięcia — cykl sam wybierze jedno z dwóch źródeł, a recenzent może ocenić ten wybór według drugiego; zadania 5 i 8 trafią na to samo.
    - kroki każdego przebiegu zostają w `SKILL.md` — główny plik ok. 2250 słów i ok. 4 pliki obok, ale niezgodne z brzmieniem WAY-256 i z układem zadania 2, a przez kroki 0–3 agent ma w polu widzenia ok. 700 słów procedury rozmowy z człowiekiem.
    - odpowiedź z wyjątkiem „fragment potrzebny od pierwszego kroku zostaje w `SKILL.md`” bez zmiany WAY-256 — główny plik ok. 1000–1100 słów, ale stoi w sprzeczności z decyzją, którą recenzent cyklu czyta jako wiążącą, więc uwaga blokująca jest prawdopodobna.
    - ten sam wyjątek dopisany do WAY-256 — decyzja dostaje trzecią klauzulę dla oszczędności ok. 50 słów, PR wychodzi poza przebudowę, a granicę „pierwszego kroku” trzeba by dopiero nazwać, żeby nie cofnęła `slice.md` z zadania 1.
  - Source: odpowiedź z zadania 4 (`_zadania/zadanie_skille_the_way_4_maintain_styleguide.md`, pytanie 2): Mariusz, 2026-10-30: „wszystko zgodnie z rekomendacjami”; koszty liczone tam dla skilla styleguide'u; potwierdzone w notatce serii, „Otwarte wątki / decyzje”.
- 9. Czy agenci cyklu czytają metody z worktree zadania, jak w zadaniach 2–4 i 9?
  - Answer: tak — z worktree zadania, zwykłą drogą cyklu, bez kopii na commicie bazowym; `task-cycle/` nie wymienia `maintain-testing-guidelines`, więc przebudowa skilla nie zmienia niczego, czym cykl pracuje. Wyjątkiem jest `instruction-files/kind_skill.md` z To do 4, którym cykl ocenia skill: przed tą zmianą plik nie odpowiada na przypadek z pytania 2, więc cykl ocenia skill według brzmienia z tego pytania.
  - Not chosen:
    - kopia the way na commicie bazowym — krok więcej na starcie, który nic nie chroni.
  - Source: odpowiedź z zadania 4 (`_zadania/zadanie_skille_the_way_4_maintain_styleguide.md`, pytanie 5): Mariusz, 2026-10-30: „przyjmuję”; zdanie o `kind_skill.md` wynika z pytania 2, nie z tamtej odpowiedzi. Stan kodu: `task-cycle/` na `00c0a74` nie wymienia tego skilla.
- 10. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak wcześniejsze zadania serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Not chosen:
    - czekać na wytyczne samego the way — seria stoi.
  - Source: odpowiedź z zadania 4 (`_zadania/zadanie_skille_the_way_4_maintain_styleguide.md`, pytanie 6): Mariusz, 2026-10-30: „przyjmuję”.

## Context

- Zadanie jest piątym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię na następne) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Podstawą jest `foundations` po PR #60, commit `00c0a747272a9a179b7a855f256daff985ea2ee1`; najbliższy wzór oceny i podziału: zadanie 4 (https://github.com/mariusznazar/the-way/pull/60), z tabelą oceny w pierwszym komentarzu.
- Skill prowadził doprecyzowanie naprawdę dwa razy, oba w `loop2`: w Codexie sesja `01a16fed` z 2026-10-25 (pierwsze wytyczne testów) i w Claude Code sesja `31f32030` z 2026-10-26 (rozszerzenie o testy mutacyjne). W obu najpierw szedł `refine-task`, a nie ma sesji, która zaczęłaby od tego skilla.
- Oba przebiegi szły na tekście starszym od dzisiejszego, więc pokazują zachowanie agenta tylko częściowo.
- Liczby pochodzą z 625 zapisów Codexa (109 `.jsonl`, 516 `.jsonl.zst`), z 26 trafieniami na ścieżkę skilla, i z zapisów Claude Code, z wywołaniem Skill w jednej sesji; `command-name>/the-way-maintain-testing-guidelines` nie ma w żadnej, przy kontroli pozytywnej 41 plików dla `/the-way-refine-task`.
- `task-cycle/` nie wymienia tego skilla; wymieniają go `project-level/task/skill/guideline_findings.md:22` i `:39`, `project-level/plan/skill/SKILL.md:122`, `product-guidelines/reading.md:79`, `product-guidelines/testing/template.md:7` i `:105`, `installation/install.py:44`, `installation/README.md:57` i `:174` oraz `installation/test_testing_guidelines_installation.py:13–14` i `:103`; ten test sprawdza tylko opis skilla i zdanie wejścia.
- Agenci cyklu i tak czytali `SKILL.md` po ścieżce, w ośmiu sesjach `loop2`, także wykonawcy kawałków i planista, choć żadna metoda cyklu ich tam nie prowadzi, a zachowane zapisy cykli, niepełne, tego pliku im nie wskazują; widoczne powody to szukanie reguł o testach mutacyjnych, praca nad samymi wytycznymi testów i przegląd zmiany przypięcia.
- W pierwszym przebiegu prowadzący wskazał agentom badawczym cały `SKILL.md` i szablon (`C:\Storage\repos\loop2\.runs\testing\research-brief.md:5`), więc czterech agentów badawczych i czterech krytyków przeczytało po ok. 6200 słów; w drugim przebiegu agenci badawczy tego pliku nie czytali.
- `loop2` stoi na the way `a8dfe8a`, a wszystkie jego 40 wejść `the-way-*` mówią już, że plik czyta się na kroku, który go wymienia (commit `1d25143` w `loop2`); nowy `SKILL.md` dociera tam przez przesunięcie przypięcia.
- Liczba 4,0 mln z miary serii obejmuje każdy plik `.md` katalogu `product-guidelines/testing/`; po plikach `ranking_wytyczne_2026-10-30.txt` daje `SKILL.md` 2,4 mln i `template.md` 3,3 mln tokenów (kopia skryptu łapie ścieżki szerzej, więc suma przewyższa 4,0).
- Skrypty miary widzą tylko Claude Code, a pierwszy przebieg skilla szedł w Codexie.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. Fragments that stand unchanged are not bound by it.” — według niej przebudowuje się skill (To do 1).
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.” — nie zmienia się.
- **WAY-258** (fragment) — „No rule stands in two of its files, and no file of a kind holds a rule another kind needs” — nie zmienia się; To do 4 dokłada odpowiedź w miejscu, w pliku rodzaju „skill”.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix.” — nie zmienia się; droga sesji na samym the way.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się; droga sesji w produkcie.
- **WAY-248** (fragment) — „Before anything else, the skill `maintain-testing-guidelines` recognizes which parts of a product have tests or, before the first test, which parts the product's plan gives tests, and what the product already has for them — a test tool, levels, directories of tests, doubles, tests of invariants, or nothing — and it extends what exists rather than setting a second tool beside it.” — nie zmienia się; wiąże kolejność kroku 1, więc przenoszone czytanie nie może jej odwrócić.
- **WAY-249** (fragment) — „It researches at every extension and never at a refresh (WAY-251), and a tool the human prefers remains the one proposed, never displaced by research.” — nie zmienia się; wyznacza warunek wariantu badań.
- **WAY-250** (fragment) — „The audit the skill `maintain-testing-guidelines` makes of a product that has tests ends, for each level, with a proposed exemplar test, with one sentence of what the product gains by it, and three to five charges, each with its file and line and one sentence of its effect, and, for each trust boundary of the product's map, with whether a test of its refusal exists.” — nie zmienia się; wyznacza warunek wariantu audytu.
- **WAY-242** (fragment) — „That designation is approved in a task's refinement only where the task's required outcome is itself a test of that level, its document naming the level and that the task's first test of it becomes the exemplar, with no list of tests and no path” — nie zmienia się; wyznacza warunek drogi „A new level”.
- **WAY-247** — „One task of a product may write both its coding guidelines and its testing guidelines, the skill of each discipline leading that discipline's matters in the task's refinement.” — nie zmienia się; zdanie w „Where the skill works” zostaje.
- **WAY-120** (fragment) — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — nie zmienia się; `elements/common/critique/SKILL.md` przestaje być czytany na kroku 0, ale obie krytyki zostają.
- **WAY-154** (fragment) — „the project orchestrator hands agents only its path and routing, never relays its contents, and each refiner ends its turn as `questions`, `waits for task <n>`, `ready for approval`, `plan change` or `obstacle`.” — nie zmienia się; opisuje tryb, którego sekcja „Orchestrated mode” idzie do pliku obok.
- **WAY-172** (fragment) — „A new or changed meaning of a product's guidelines is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it” — nie zmienia się; niesie ją „Where the skill works”, gdziekolwiek stanie.

## Settlements to record

Candidates: 12 shown, 3 accepted — 2026-10-31

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Rozszerzenie WAY-256 o fragment potrzebny na niektórych krokach skilla, nie na wszystkich: to, czego agent ma się trzymać przy pracy na tych krokach, zostaje w `SKILL.md`; to, do czego zagląda, stoi w pliku obok, każdy z tych kroków ten plik wymienia, a krok późniejszy każe go przeczytać, jeśli wcześniejszy tego nie zrobił. Klauzula WAY-256 „Fragments that stand unchanged are not bound by it” obowiązuje i tutaj. | decision | pytanie 2, Mariusz, 2026-10-31: „C” | który numer decyzji cytuje trzecia odpowiedź w `kind_skill.md`, skoro dwie pierwsze cytują WAY-256 |
| 2 | W skillu przebudowywanym albo zmienianym według WAY-256 plik wariantu, do którego odsyła plik kroku, jest wymieniony także w `SKILL.md` przy tym kroku; pliki stojące bez zmian, jak w skillu styleguide'u, reguła omija. | decision | pytanie 3, Mariusz, 2026-10-31: „B” | na co powołuje się wiersz tabeli oceny o tym układzie, i czy recenzent zadania 8 ma go za wiążący |
| 3 | W skillach wytycznych produktu sesja, która nie przeszła przez kroki 1 i 2 `refine-task`, bo otworzyła skill bezpośrednio albo wznowiła pracę w nowej rozmowie, przechodzi przez nie najpierw. | decision | pytanie 4, Mariusz, 2026-10-31: „C” | na jaką decyzję powołuje się to zdanie w kroku 0, skoro reguły tych skilli cytują decyzje, i czy zadanie 8 ma je dopisać |

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 5/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie zadania 6 i ustawić linii „seria skilli 6/11” datę dnia domknięcia; do „Otwartych wątków” wchodzi też to, że porównanie niesionego tekstu czeka na następne prawdziwe użycie skilla, także w Codexie, a `skill_carry_cost.py` potrzebuje parametru daty (pytanie 7), wskazanie dla handoffu zadania 8 na odpowiedzi na pytania 3 i 4 oraz sprostowanie zdania o przypięciu `loop2` w „Otwartych wątkach”, bo `loop2` stoi już na `a8dfe8a`.
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- Treść plików, które skill każe czytać: `product-guidelines/template.md`, `product-guidelines/testing/template.md`, `product-guidelines/reading.md`, `project-level/task/skill/SKILL.md`, `project-level/task/template.md`, `elements/common/way_of_working.md`, `elements/common/critique/SKILL.md` (pytanie 1).
- `instruction-files/SKILL.md` (pytanie 3) i osobny plik agenta badawczego (pytanie 5).
- Uwagi z PR-ów #50–#52, #59 i #60 — nie przechodzą do tego zadania, poza tymi, które rozstrzygają jego pytania.
- Ewentualne scalenie plików trybu orkiestrowanego trzech skilli wytycznych — sprawa zadania 8.
- Pozostałe skille the way — zadania 6–8, 10 i 11 serii, także `maintain-coding-guidelines`, który ma ten sam układ sekcji; ze skilla styleguide'u tylko zdanie z To do 6.
