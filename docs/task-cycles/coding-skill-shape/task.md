---
title: "the way, seria skilli 8/11: maintain-coding-guidelines w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok"
status: draft
created: 2026-10-31
updated: 2026-10-31
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# maintain-coding-guidelines w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `maintain-coding-guidelines` the way to jeden plik `product-guidelines/coding/SKILL.md` o 3396 słowach na `foundations` `f86fd71`, a obok niego tylko szablon; WAY-256 każe fragment jednego kroku albo wariantu trzymać w pliku obok skilla.
- W `SKILL.md` stoją fragmenty potrzebne tylko w jednym wariancie: „Orchestrated mode” (`product-guidelines/coding/SKILL.md:90–99`), potrzebny tylko sesji prowadzonej przez `lead-project`, badania z kroku 2 (`:150–162`), potrzebne tylko przy pierwszych wytycznych bez preferencji człowieka i przy rozszerzeniu, próbny przebieg i audyt rodzajów kodu z kroku 3 (`:171–196`), potrzebne tylko produktowi z kodem, oraz „A new kind” (`:197–199`), potrzebne tylko zadaniu, które tworzy pierwszy plik rodzaju kodu.
- Krok 0 (`:101–112`) każe na wejściu przeczytać ok. 7200 słów z innych plików, dwa razy tyle co sam `SKILL.md`, w tym 3391 słów, które sesja wczytała już w krokach 1 i 2 `refine-task`.
- Agenci nieśli tekst katalogu `product-guidelines/coding/` przez ok. 3,2 mln tokenów od 2026-09-01 — ósmy wynik serii, z czego 2,3 mln w sesjach w samym repo the way, a nie w produktach (miara serii, `ranking_2026-10-28.txt`).

### To do

1. `maintain-coding-guidelines` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a procedura kroku albo wariantu — w pliku obok w `product-guidelines/coding/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza, a fragment potrzebny na niektórych krokach stoi według swojego rodzaju (WAY-256).
2. Krok 0 przestaje kazać czytać wszystko naraz: każdy plik, który wymienia, jest czytany na kroku, który go potrzebuje, a to, co sesja przeczytała już w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz. Pozycje kroku 0 wobec tego, co czyta `refine-task` (`project-level/task/skill/read_sources.md`, `product-guidelines/reading.md`):
   - czytane już w całości, nie czytać drugi raz: `project-level/task/skill/SKILL.md` (463 słowa), `project-level/task/template.md` (2228), sekcja „How a skill asks” (208) i sekcja „Reading the foundation” (492), razem 3391 słów;
   - czytane częściowo: `guidelines/` — `refine-task` czyta tylko pliki, których *Applies to* wymienia dotknięte części (`product-guidelines/reading.md:40`), więc skill czyta te pozostałe; główny `AGENTS.md` produktu — `refine-task` czyta tylko sekcję `## Backlog` (`read_sources.md:17`), więc skill czyta go w całości; fundament — dochodzą tylko pozycje dodane w kroku 0: decyzje o technologii produktu i każda decyzja, która przyjmuje stałe sprawdzenie, zestaw reguł albo wzorzec albo od nich odstępuje;
   - nieczytane przez `refine-task`, zostają na swoim kroku: `product-guidelines/template.md` (1336), `product-guidelines/coding/template.md` (2112), sekcja „Critique before collective review” (54), `elements/common/critique/SKILL.md` (322) z plikami obok (509).
3. Szablon `product-guidelines/coding/template.md` jest przeczytany przed pierwszym krokiem, który go używa, na każdej drodze: na kroku 2, na kroku 3 przy `trial_run.md` albo `kinds.md`, jeśli krok 2 tego nie zrobił, a na kroku 4, jeśli nie zrobił tego żaden wcześniejszy krok, co obejmuje drogę „A new kind”.
4. Plik wariantu, do którego odsyła plik kroku, jest wymieniony także w `SKILL.md` przy tym kroku, z warunkiem, kiedy się go czyta (WAY-265).
5. Krok 0 kończy się zdaniem, które sesję bez kroków 1 i 2 `refine-task` odsyła najpierw do nich (WAY-266), w brzmieniu z `product-guidelines/testing/SKILL.md:79–81`.
6. Request zadania podaje tabelę oceny skilla: fragment zacytowany dosłownie z zakresem linii na `f86fd71`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt i miejsce po przebudowie.
7. Request podaje liczby słów przed przebudową i po niej, tak jak mówi pytanie 4.
8. Request podaje jako propozycje werdykty „remove” i „reword” zmieniające treść reguły, poza To do 9–13; wśród nich jest sprzeczność drogi „A new kind” z `product-guidelines/coding/SKILL.md:223–224`, `:269` i pozycjami *To do* z `:63–69`, które na tej drodze nadal mówią o wszystkich stałych sprawdzeniach, a cykl jej nie naprawia.
9. Lista trybów w kroku 1 (`product-guidelines/coding/SKILL.md:124–130`) dostaje piąty tryb: rodzaj kodu, którego pliki produkt już ma, bez wiersza w indeksie `guidelines/coding.md`, gdy ten plik stoi, a zadanie go nie odświeża ani nie rozszerza; idzie przez „Kinds” z kroku 3 tylko dla tego rodzaju, bez kroku 2 i bez próbnego przebiegu (pytanie 3), a przy połączeniu z innym trybem wygrywa tryb szerszy.
10. Na tej drodze kroki 4 i 5 rozstrzygają i sprawdzają tylko to, co dotyczy tego rodzaju: identyfikator, wzorzec, status jego plików i reguły sprawdzane skryptem z ich niezmiennikami, a *To do* zadania dostaje plik `guidelines/coding-<kind>.md` z wierszem indeksu.
11. Reguła z To do 10 stoi w `SKILL.md`, bo agent trzyma się jej na krokach 3–5 (WAY-256).
12. Próbny przebieg i audyt rodzajów stoją w osobnych plikach obok skilla, `trial_run.md` i `kinds.md`; droga jednego rodzaju to porównanie z WAY-200, nie audyt z WAY-201, i tak nazywa ją `kinds.md` przy zdaniu „the audit covers every one of them” (`:187–188`).
13. Fundament zmieniają dwie edycje w miejscu: WAY-216 z wierszy 1 i 2 *Settlements to record* i WAY-266 z wiersza 3; żaden nowy wpis nie powstaje.

### Acceptance criteria

- Poza To do 9–13 żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Agent na drodze jednego rodzaju czyta `kinds.md`, a nie czyta `starting_set.md`, `research.md` ani `trial_run.md`; agent pierwszych wytycznych, rozszerzenia i odświeżenia czyta `trial_run.md` i `kinds.md` tak, jak dziś krok 3.
- Każdy przeredagowany warunek trybu albo odsyłacza jest porównany z bazą i nie dodaje drogi ani żadnej nie gubi; samo sprawdzenie obecności zdań nie wystarcza. Odsyłacz do kroku 2 wymienia wszystkie warunki z `product-guidelines/coding/SKILL.md:141`, także „before the first code”, a „for code that has no coding guidelines yet” nie czyta się tam jako rodzaju bez własnego pliku.
- Każdy odsyłacz do pliku obok nazywa swój krok albo wariant słowami, które rozpozna agent czytający `SKILL.md` po ścieżce, bez pliku wejściowego skilla.
- Recenzent przechodzi każdą drogę ręcznie przez pliki, od `SKILL.md` do pliku ostatniego kroku, tak jak zrobiłby to agent, i porównuje każdy wiersz tabeli oceny z miejscem, w którym fragment naprawdę stanął.
- Fragment potrzebny w więcej niż jednym miejscu dociera do każdego z nich: „How to show” (`:206–215`) także do pytania o preferencje w kroku 2, „What reaches the task document” (`:47–88`) do kroków 4 i 5, przy czym kroki 1 i 3 same mówią, co dopisują do dokumentu, „Extend what exists” (`:131–133`) i zdanie o wyborze znalezionym w plikach produktu (`:200–202`) do każdej drogi, także „A new kind”.
- Reguła o zaleceniach dokumentacji lintera dla produktu bez kodu (`:163–165`) dociera także na drogę z preferencją człowieka, na której nie ma badań.
- Zdanie o odświeżeniu bez badań (`:149–150`) stoi w `starting_set.md`, nie w `research.md`.
- Agent na drodze „A new kind” nie czyta `trial_run.md` ani `kinds.md`.
- Fragment `:197–199` to jedna instrukcja, więc zostaje w `SKILL.md` przy kroku 3 (WAY-256), a jego warunek nie zależy od nagłówka „Where the product has code:” (`:169`), bo pierwszy plik rodzaju może powstać też w produkcie bez kodu (WAY-200, WAY-209).
- „Where the skill works” z tabelą i akapitem o znaczeniach (`:24–45`) zostaje w `SKILL.md`, bo tam sięgają po nie agenci cyklu.
- Opis skilla (`description`) i kod w Pythonie się nie zmieniają, więc wejścia `the-way-*` też nie.
- Liczby słów powstają po ostatniej zmianie liczonego pliku, a pomocniczy skrypt porównuje każdą podaną liczbę z plikiem, nie tylko sumy z raportem.

### Questions to settle

- 1. Co oprócz tekstu `product-guidelines/coding/SKILL.md` przebudowa może ruszyć: moment czytania plików z kroku 0, czy także `product-guidelines/coding/template.md`?
  - Answer: `SKILL.md` i moment czytania plików z kroku 0 (To do 1–3); same te pliki się nie zmieniają, także `product-guidelines/template.md`, `product-guidelines/coding/template.md` i `product-guidelines/reading.md`.
  - Not chosen:
    - zostawić skill jak jest — ok. 14 500 słów do końca skilla; skill kodu zostaje jako jedyny z trzech skilli wytycznych w starym kształcie, a każdy przebieg czyta wszystko.
    - tylko tekst `SKILL.md`, krok 0 bez zmian — ok. 14 500–14 900 słów; dochodzi ok. 10 plików, a zysku nie ma, bo krok 0 i tak czyta to samo.
    - także wydzielenie z szablonu części dla autora w cyklu — najwyżej 88 słów mniej; rusza plik, którego używa autor w cyklu, a nazwę sekcji „Writing the files” skill wpisuje do opisów zadań w produktach (`product-guidelines/coding/SKILL.md:55`).
  - Source: Mariusz, 2026-10-31: „C” — na drogę o szacunku ok. 10 600–11 300 słów do końca skilla (−22 do −27%) i ok. 5100–8800 przed krokiem 4 zamiast 14 000–14 500, z kosztem pokazanym w pytaniu: ok. 10 plików więcej do utrzymania, łączny tekst większy o ok. 400 słów, szablon kodu dalej czytany w całości; ze słabym punktem nazwanym w pytaniu: oszczędność zależy od tego, czy agent sięgnie po plik na właściwym kroku. Liczby to szacunek z liczenia słów na `f86fd71`, razem z pierwszym odczytem w `refine-task`.
- 2. Czy trzy pliki trybu orkiestrowanego (styleguide, testy, kod) scalamy w jeden, skoro notatka serii odłożyła tę sprawę do zadania 8?
  - Answer: nie — skill kodu dostaje własny `product-guidelines/coding/orchestrated_mode.md`, a pliki styleguide'u i testów się nie zmieniają; wątek scalania zamyka się w notatce serii przy domknięciu tego zadania.
  - Not chosen:
    - jeden wspólny plik w `product-guidelines/` — każde zdanie różni się między dyscyplinami, więc plik staje się tabelą, a agent czyta też to, co dotyczy innych dyscyplin (ok. 60 słów więcej); PR rusza odsyłacze w skillach styleguide'u i testów, poza tym zadaniem, i przestaje być czystym przeniesieniem.
  - Source: Mariusz, 2026-10-31: „A” — ze słabym punktem nazwanym w pytaniu: gdy `lead-project` zmieni sposób prowadzenia, ktoś musi pamiętać o trzech plikach, a nic tego nie pilnuje. Różnice: `product-guidelines/styleguide/orchestrated_mode.md:3–9`, `product-guidelines/testing/orchestrated_mode.md:3–9`, `product-guidelines/coding/SKILL.md:92–99` na `f86fd71`.
- 3. Co z drogą, której lista trybów w kroku 1 nie wymienia: wzorzec rodzaju kodu, którego pliki w produkcie już są, bez nowego pliku tego rodzaju?
  - Answer: skill dostaje piąty tryb razem ze zmianą WAY-216 (To do 9–13): porównanie plików jednego rodzaju bez wpisu w indeksie wytycznych, bez kroku 2 i bez próbnego przebiegu. To wyjątek od ustalenia serii „Przebudowa zmienia miejsce reguł, nie ich treść”, tylko dla tego trybu. Zmiana wzorca, który już stoi (WAY-199), do trybu nie wchodzi.
  - Not chosen:
    - zostawić cztery tryby i opisać lukę w PR jako propozycję — agent na tej drodze dalej improwizuje i może zrobić pełny audyt; późniejsza naprawa to osobne zadanie: jedno zdanie w trybach i rozdzielenie `audit.md` na dwa pliki.
  - Source: Mariusz, 2026-10-31: „B”, potwierdzone po sprostowaniu kosztu: „Zostaję przy B” — na drogę z pokazanym kosztem: krok fundamentu i przeszukanie całego fundamentu w cyklu, zmiana znaczenia decyzji przyjmowana przy scaleniu, jeden plik więcej, skill kodu rozstrzyga ten przypadek inaczej niż skill testów poziom bez przepisu (`product-guidelines/testing/recognize.md:23`). Pierwsze pytanie zaniżyło koszt: mówiło o ok. 30 słowach w skillu, a sam tryb złamałby WAY-211 („The skill researches at every extension and never at a refresh (WAY-251).”, `foundations/decisions.md:5735`). Podstawa trybu: `product-guidelines/reading.md:83–85`, `project-level/task/skill/guideline_findings.md:33–35`; stan: w przeszukanych zapisach żadna sesja nie szła tą drogą, więc tryb nie ma za sobą prawdziwego przypadku.
- 4. Na jakich drogach użycia request liczy słowa przed przebudową i po niej?
  - Answer: na siedmiu: (1) brak kodu, człowiek bez preferencji; (2) brak kodu, człowiek z preferencją; (3) jest kod, nie ma wytycznych, bez preferencji, a także rozszerzenie; (4) odświeżenie; (5) „A new kind”, gdy wytyczne już stoją; (6) jeden rodzaj, którego pliki już są, z To do 9–13; (7) tryb orkiestrowany na drodze 1. Na każdej trzy liczby: tekst wczytany przed krokiem 4, suma do końca razem z plikiem ostatniego kroku oraz ta suma bez pierwszego odczytu w `refine-task` (3391 słów). Słowa liczy się jak `wc -w`, w stanie „przed” na `f86fd71`; plik czytany dwa razy w stanie „przed” liczy się dwa razy, pliki obok krytyki (509 słów) wchodzą tam, gdzie droga do nich dochodzi, a pliki produktu są poza liczeniem.
  - Not chosen:
    - siedem dróg i ósma, zadanie wspólne z wytycznymi testów (WAY-247) — czyta te same pliki co droga 1 i droga 1 testów, tylko wspólne pliki liczą się raz, więc nic nowego nie pokazuje, a dokłada pracę liczenia.
    - jedna liczba, słowa w `SKILL.md` — pokazuje ok. −62% zamiast ok. −25%, czyli wynik zawyżony; ktoś może na nim oprzeć wniosek o całej serii.
  - Source: Mariusz, 2026-10-31: „A” — ze słabym punktem nazwanym w pytaniu: to liczby słów w plikach, a nie zachowanie agenta, a droga wspólna, realna przy nowych produktach, zostaje niepoliczona.
- 5. Czy agent badawczy dostaje własny plik obok skilla, jak w zadaniu 9?
  - Answer: nie — jak w zadaniach 4 i 5: plik wariantu z badaniami jest dla prowadzącego, który przekazuje agentowi reguły w zleceniu; lista tego, co agent dostaje, się nie zmienia.
  - Not chosen:
    - osobny plik agenta, jak w zadaniu 9 — jeden plik i ok. 60–100 słów więcej.
  - Source: Mariusz, 2026-10-31: „Tak” — ze słabym punktem nazwanym w pytaniu: gdy prowadzący zapomni o regule „każde źródło to strona z wersją”, agent jej nie zobaczy, a wyłapie to dopiero krytyka. W pierwszym przebiegu prowadzący wskazał agentom krok 2 `SKILL.md` i szablon kodu (`C:\Storage\repos\loop2\.runs\coding\research-brief.md:7`).
- 6. Kiedy i czym mierzymy niesiony tekst po scaleniu?
  - Answer: przy następnym prawdziwym użyciu skilla w `loop2`, skryptami serii z datą początkową po scaleniu, nie przy domknięciu zadania; do tego czasu główną miarą zostają słowa z requestu, a gdy użycie pójdzie w Codexie, porównanie liczy się osobno z jego zapisów.
  - Not chosen:
    - pomiar przy domknięciu — liczba mówi tylko, ile czasu minęło, a wygląda jak wynik.
  - Source: Mariusz, 2026-10-31: „Tak” — ze słabymi punktami nazwanymi w pytaniu: porównanie może długo czekać, a `skill_carry_cost.py` potrzebuje parametru daty.
- 7. Czy agenci cyklu czytają metody z worktree zadania, jak w zadaniach 2–5 i 9?
  - Answer: tak — z worktree zadania, zwykłą drogą cyklu, bez kopii na commicie bazowym; `task-cycle/` nie wymienia `maintain-coding-guidelines`, więc przebudowa nie zmienia niczego, czym cykl pracuje.
  - Not chosen:
    - kopia the way na commicie bazowym — krok więcej na starcie, który nic nie chroni.
  - Source: Mariusz, 2026-10-31: „Tak”. Stan kodu: `task-cycle/` na `f86fd71` nie wymienia tego skilla.
- 8. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak wcześniejsze zadania serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Not chosen:
    - czekać na wytyczne samego the way — seria stoi bez żadnego zysku.
  - Source: Mariusz, 2026-10-31: „Tak”.

## Context

- Zadanie jest ósmym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Mariusz wziął to zadanie przed zadaniami 6 i 7: wywołanie `/the-way-refine-task` z nazwą tego skilla, 2026-10-31.
- Podstawą jest `foundations` po PR #63, commit `f86fd71f3cb72a9eb1620c388af44bbd1198fb4a`; najbliższy wzór oceny i podziału: zadanie 5 (https://github.com/mariusznazar/the-way/pull/62), z tabelą oceny w pierwszym komentarzu.
- W dostępnych zapisach skill prowadził doprecyzowanie raz: 2026-10-19 i 2026-10-20 w `loop2`, droga „jest kod, nie ma wytycznych, człowiek bez preferencji”, z trzema raportami badań, próbnymi przebiegami i audytem; zapis: `C:\Storage\repos\loop2\.runs\coding\reading-record.md`.
- W tym przebiegu prowadzący kazał agentom badawczym przeczytać krok 2 `SKILL.md` i szablon kodu (`C:\Storage\repos\loop2\.runs\coding\research-brief.md:7`).
- W zapisach Claude Code nikt nie wywołał tego skilla poleceniem ani narzędziem Skill: 0 trafień, przy kontroli pozytywnej 250 wywołań innych skilli `the-way-*` i 42 plikach z `/the-way-refine-task`.
- Po pierwszym przebiegu plik czytali narzędziem Read tylko agenci cykli: planiści, wykonawcy kawałków, agenci kroku powrotu i recenzenci w `konta-graczy-i-logowanie`, `potwierdzenie-adresu`, `zapis-stanu-na-serwerze` i `reset-hasla`.
- W `reset-hasla` powoływali się na `SKILL.md:37-41` (`C:\Storage\repos\loop2-wt\reset-hasla\.runs\task-cycles\reset-hasla\plan.md:543`), `:44-45` (`…\reports\36-return-review-report.md:107`) i `:30-45` (tamże, `:175`): tabelę, kto co pisze, i zdanie, że użycie znaczenia niesionego przez decyzję nie wymaga zgody.
- `loop2` ma na `main` (`4ed8fcd`) 11 plików rodzajów: 4 z pierwszego przebiegu (`a98222d`) i 7 z późniejszych zadań funkcjonalnych (np. commity `1c335f3`, `483f5dc`); w przeszukanych zapisach nie ma sesji doprecyzowania, która przeszłaby drogę „A new kind” tym skillem.
- Zapisów Codexa `.jsonl.zst` nie przeszukiwałem, więc sesji pierwszego przebiegu w nich nie widziałem; opis tego przebiegu pochodzi z `reading-record.md`.
- `task-cycle/` nie wymienia tego skilla; wymieniają go `project-level/task/skill/guideline_findings.md:21` i `:32`, `project-level/plan/skill/SKILL.md:121`, `product-guidelines/reading.md:84`, `product-guidelines/coding/template.md:114`, `installation/install.py:43`, `installation/README.md:57` i `:174` oraz `installation/test_coding_guidelines_installation.py:13–14` i `:103`; ten test sprawdza tylko opis skilla i zdanie wejścia.
- Wiersze 1 i 2 *Settlements to record* przyjęto w brzmieniu końca WAY-216: „Where files of the kind already exist, refinement records that discrepancy and routes exemplar selection through the comparison WAY-200 gives existing code, rather than treating the next file as the first. Neither a kind's first file nor that comparison alone makes a task an extension under WAY-251 or takes research of the standing checks; the comparison covers that kind alone, takes no trial run of a linter's set and is no audit under WAY-201.”; cały wpis ma wtedy trzy zdania wiążące, czyli tyle, ile dopuszcza WAY-05.
- WAY-266 dotyczy po wierszu 3 każdego skilla wytycznych, bez wyjątku; WAY-265 zostaje bez zmian, bo jego drugie zdanie dalej obejmuje skill styleguide'u.
- Słowa pierwszego odczytu są wyższe niż w zadaniu 5 (3391 wobec 2835), bo od tamtej pory szablon zadania urósł o 489 słów, a `project-level/task/skill/SKILL.md` o 67; liczb z zadań 4, 5 i 9 nie da się wprost porównać z tymi.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. A fragment that some steps of the skill need, not all, stands by what it is: a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did; fragments that stand unchanged are not bound by it.” — według niej przebudowuje się skill (To do 1).
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.” — nie zmienia się.
- **WAY-265** — „In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file points to is named in the skill's `SKILL.md` at that step as well, with the condition under which it is read. A step's file that stands unchanged, with the variant file it points to, is not bound by it.” — wiąże To do 4.
- **WAY-266** — „In a skill that leads a product's guidelines matters, a session that has not read steps 1 and 2 of `refine-task` in the conversation, because it opened the skill directly or resumed the work in a new conversation, goes through those steps before the skill's first step. Skills of guidelines whose text stands unchanged are not bound by it until they are rebuilt.” — wiąże To do 5; drugie zdanie znika w miejscu (wiersz 3 *Settlements to record*).
- **WAY-216** — „A task that creates the first file of a kind of code whose row the general coding index lacks gains in *To do* the designation of that kind's exemplar under WAY-200 and its kind guidelines with their index row, without waiting for a separate exemplar task. Where files of the kind already exist, refinement records that discrepancy and routes exemplar selection through the comparison WAY-200 gives existing code, rather than treating the next file as the first.” — zmienia się w miejscu (pytanie 3, wiersze 1 i 2 *Settlements to record*).
- **WAY-200** (fragment) — „Where it already holds files of that kind, the skill `maintain-coding-guidelines` judges every one of them, compares them and proposes the exemplar from that comparison, with the status `copy` or `do not copy` of every other file, and the human approves the decision that designates it.” — nie zmienia się; wyznacza treść `kinds.md`.
- **WAY-199** (fragment) — „Designating another file as the exemplar of a kind of code and changing a rule a script checks from that exemplar are changes of the product's decisions, approved as WAY-172 gives a changed meaning, while an edit of the exemplar that keeps those rules takes no approval.” — nie zmienia się; ta droga nie wchodzi do piątego trybu.
- **WAY-201** — „The audit the skill `maintain-coding-guidelines` makes of a product that has code ends with a proposed exemplar for each kind of code the product holds files of, each with one sentence of what the product gains by it, and with the files of that kind marked `do not copy`, each with the file and line of the place that breaks a rule.” — nie zmienia się; wyznacza warunek audytu.
- **WAY-202** (fragment) — „They bind a product from the task that writes its coding guidelines, which is complete only once it holds, for each of the three standing checks, a decision of the product's log adopting it or departing from it with the reason.” — nie zmienia się; dlatego piąty tryb stoi tylko tam, gdzie ogólny plik wytycznych już jest.
- **WAY-204** (fragment) — „The skill `maintain-coding-guidelines` proposes which rules of a linter's set block and which stand among the examples from a trial run of the set on the product's code, each report of which an agent that wrote none of that code judges by whether it leads to a change of code worth making, whether it is technically right or not, and a rule with one report that leads to no such change goes among the examples; for a product with no code it proposes as blocking the rules the tool's documentation marks as recommended.” — nie zmienia się; wyznacza warunek `trial_run.md`.
- **WAY-209** — „The skill `maintain-coding-guidelines` proposes that, in a product with no code, the general file of its coding guidelines, with its standing checks, comes into being before the first task that writes the product's code, and that the file of a kind of code comes into being with the task that creates the first file of that kind.” — nie zmienia się; niesie go droga „A new kind”.
- **WAY-210** (fragment) — „Before anything else, the skill `maintain-coding-guidelines` recognizes which parts of a product hold code and what the product already has for them — a linter, a formatter, an audit of dependencies, kinds of code that already have files, or nothing — and whether it has coding guidelines, and it extends what exists rather than setting a second tool beside it.” — nie zmienia się; wiąże kolejność kroku 1, więc przenoszone czytanie nie może jej odwrócić.
- **WAY-211** (fragment) — „A tool the human prefers remains the one proposed, never displaced by research. The skill researches at every extension and never at a refresh (WAY-251).” — nie zmienia się; wyznacza warunek wariantu badań, a zmiana WAY-216 mówi, czego nie liczy się jako rozszerzenia.
- **WAY-251** — „For the skills `maintain-coding-guidelines`, `maintain-styleguide` and `maintain-testing-guidelines`, a refresh updates or corrects accepted guidelines within the scope they already cover, including adapting them to a new version of a tool the product already uses. An extension covers something new, and its research checks whether to use what the product already has or something else, with the human's preferred tool remaining the proposal.” — brzmienie się nie zmienia; WAY-216 dostaje relację `narrows WAY-251` dla swoich dwóch przypadków.
- **WAY-247** — „One task of a product may write both its coding guidelines and its testing guidelines, the skill of each discipline leading that discipline's matters in the task's refinement.” — nie zmienia się; zdanie w „Where the skill works” zostaje.
- **WAY-174** (fragment) — „The coding-guidelines skill asks for decisions, never for single rules, so that the human adopts a linter's set of rules whole.” — nie zmienia się; niesie go „How to show”.
- **WAY-268** (fragment) — „and the tools the skills of guidelines choose stay on those skills' routes” — nie zmienia się; „New tools” zostaje na drodze tego skilla.
- **WAY-120** (fragment) — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — nie zmienia się; krytyki zostają, zmienia się tylko moment czytania `elements/common/critique/SKILL.md`.
- **WAY-154** (fragment) — „the project orchestrator hands agents only its path and routing, never relays its contents, and each refiner ends its turn as `questions`, `waits for task <n>`, `ready for approval`, `plan change` or `obstacle`.” — nie zmienia się; opisuje tryb, którego sekcja idzie do pliku obok.
- **WAY-172** (fragment) — „A new or changed meaning of a product's guidelines is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it” — nie zmienia się; niesie ją „Where the skill works”.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix.” — nie zmienia się; droga sesji na samym the way.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się; droga sesji w produkcie.

## Settlements to record

Candidates: 8 shown, 3 accepted — 2026-10-31

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Koniec WAY-216, edycja w miejscu: porównanie plików rodzaju bez wpisu w indeksie obejmuje tylko ten rodzaj, samo nie czyni zadania rozszerzeniem według WAY-251, nie wymaga badań stałych sprawdzeń ani próbnego przebiegu zestawu lintera i nie jest audytem z WAY-201; WAY-216 dostaje relację `narrows WAY-251`. | decision | pytanie 3, Mariusz, 2026-10-31: „Zostaję przy B”; pozostałe drogi w *Not chosen* tego pytania; brzmienie: Mariusz, 2026-10-31: „ok” — odrzucone brzmienie „Neither task is an extension under WAY-251, and neither takes research of the standing checks” zdejmowało badania także z zadania, które jest rozszerzeniem z innego powodu, wbrew WAY-211 | na jaką decyzję powołuje się piąty tryb, skoro bez niej łamie WAY-211, i czy WAY-216 zawęża WAY-251 |
| 2 | Pierwszy plik rodzaju sam też nie czyni zadania rozszerzeniem według WAY-251 i sam nie wymaga badań stałych sprawdzeń; stoi w tym samym zdaniu WAY-216 co wiersz 1. | decision | Mariusz, 2026-10-31: „Tak, przyjmuję” — na propozycję opartą na `product-guidelines/coding/SKILL.md:128`, z pokazanym kosztem: kilka słów więcej w decyzji; bez wiersza każde zadanie tworzące pierwszy plik rodzaju mogłoby ściągać badania wszystkich stałych sprawdzeń; brzmienie: „ok”, jak w wierszu 1 | czy droga „A new kind” bierze badania, skoro po wierszu 1 tylko drugi przypadek byłby wprost wyjęty spod rozszerzenia |
| 3 | Z WAY-266 znika ostatnie zdanie („Skills of guidelines whose text stands unchanged are not bound by it until they are rebuilt.”), edycja w miejscu, bo po tym zadaniu wszystkie trzy skille wytycznych mają zdanie z kroku 0. | decision | Mariusz, 2026-10-31: „Tak, przyjmuję” — na propozycję opartą na `foundations/decisions.md:7631–7632` i opisie PR #62: „Bez drugiego skill kodu naruszałby wpis od dnia scalenia, a zadanie 8 i tak dopisze mu to zdanie.”; droga pokazana i niewybrana: zostawić zdanie — nic się nie psuje, ale decyzja niesie martwy wyjątek | czy zostawić wyjątek, który po scaleniu nikogo nie dotyczy |

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 8/11” w `_tasks_active.md` i zaktualizować w notatce serii „Otwarte wątki / decyzje”. Zadanie 9 jest już zrobione, a następne zostaje zadanie 6, więc „Handoff dla AI” dalej prowadzi do zadania 6; dopisuje się do niego tylko wnioski z tego zadania, a dat linii 6/11 i 7/11 się nie zmienia (Mariusz, 2026-10-31: „Tak”). Do „Otwartych wątków” wchodzi też zamknięcie sprawy scalenia plików trybu orkiestrowanego (pytanie 2) i to, że porównanie niesionego tekstu czeka na następne prawdziwe użycie skilla (pytanie 6).
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- Uwagi z PR-ów #50–#52, #59, #60 i #62 — nie przechodzą do tego zadania, poza tymi, które rozstrzygają jego pytania.
- Pozostałe skille the way — zadania 6, 7, 10 i 11 serii.
