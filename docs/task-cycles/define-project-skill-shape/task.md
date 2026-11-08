---
title: "the way, seria skilli 11/11: define-project w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok"
status: draft
created: 2026-11-06
updated: 2026-11-06
tags: [zadanie]
related: "notatka projektu w prywatnych notatkach autora"
---

# define-project w kształcie WAY-256 — obraz całości i zasady w SKILL.md, wytyczne kroków w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `define-project` the way to jeden plik `project-level/skill/SKILL.md` o 1937 słowach na `foundations` `dfd50e5`, bez żadnego pliku obok w swoim katalogu; obok katalogu leży tylko szablon definicji `project-level/definition_template.md` (3221 słów). WAY-256 każe fragment jednego kroku albo wariantu trzymać w pliku obok skilla.
- W `SKILL.md` stoją fragmenty potrzebne tylko w jednym wariancie albo na jednym kroku: „Delegated definition change and gate” (`project-level/skill/SKILL.md:25–51`, 314 słów), potrzebna tylko agentowi zleconemu przez `lead-project`; kroki 1–4 (`:73–125`, 540 słów), potrzebne tylko przy pisaniu definicji od pomysłu; krok 7 (`:145–183`, 495 słów), potrzebny dopiero przy bramce gotowości.
- Pięć z sześciu prawdziwych przebiegów skilla w `loop2` nie przechodzi kroków 1–6: cztery to tury zlecone przez `lead-project` (zmiana definicji i bramka), jedna to ponowne otwarcie wpisu zatwierdzonej definicji w sesji doprecyzowania zadania; tylko jeden przebieg pisał definicję od pomysłu.
- Agenci nieśli tekst skilla przez ok. 2,2 mln tokenów od 2026-09-01 — jedenasty wynik serii, z czego 1,2 mln w sesjach w samym repo the way (miara serii, plik rankingu serii w prywatnych notatkach autora).

### To do

1. `define-project` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a procedura kroku albo wariantu — w pliku obok w `project-level/skill/`, który ten krok albo wariant wymienia; fragment z jedną instrukcją zostaje w `SKILL.md` w miejscu odsyłacza, fragment potrzebny na niektórych krokach stoi według swojego rodzaju (WAY-256), a plik wariantu, do którego odsyła plik kroku, `SKILL.md` wymienia przy tym kroku z warunkiem, kiedy się go czyta (WAY-265).
2. Kroki zachowują numery od 0 do 7, a krok 7 numery 7.1–7.5, bo powołują się na nie inne pliki the way i zlecenia orkiestratorów; nagłówek „Delegated definition change and gate” zostaje w `SKILL.md` przy odsyłaczu do pliku trybu zleconego.
3. Przebudowa zmienia tylko katalog `project-level/skill/`; `project-level/definition_template.md` i pozostałe pliki the way zostają bez zmian (pytanie 1).
4. Request podaje tabelę oceny skilla: fragment zacytowany dosłownie z zakresem linii na `dfd50e5`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt i miejsce po przebudowie.
5. Request podaje liczby słów przed przebudową i po niej, tak jak mówi pytanie 4.
6. Request podaje jako propozycje werdykty „remove” i „reword” zmieniające treść reguły, a wśród nich powtórzenia między skillem a `project-level/lead/skill/SKILL.md` i `project-level/definition_template.md` (pytanie 1).

### Acceptance criteria

- Żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Każdy przeredagowany warunek trybu, wariantu albo odsyłacza jest porównany z bazą i nie dodaje drogi ani żadnej nie gubi, a przy każdym nowym zdaniu autor nazywa, co ono wyłącza; samo sprawdzenie obecności zdań nie wystarcza.
- Każdy odsyłacz do pliku obok nazywa swój krok albo wariant słowami, które rozpozna agent czytający `SKILL.md` po ścieżce, bez pliku wejściowego skilla.
- Plik trybu zleconego dociera do kroku 7: agent zlecony nie pyta człowieka sam, nie uruchamia krytyki z 7.3 sam i nie pisze odcisku ani statusu `approved` przed zapisaną zgodą człowieka, choć plik kroku 7 mówi o tym bez zastrzeżenia.
- Fragment potrzebny na kilku krokach dociera do każdego z nich — co najmniej: „Speak the language the human opened in” (`project-level/skill/SKILL.md:80`, krok 1) i „what the files can answer, read yourself instead of asking” (`:117`, krok 4) do każdego kroku, który pyta człowieka albo pisze definicję; „Write each answer into the definition, with its status line, before the next question” (`:106–108`) do kroków, które dalej zmieniają definicję; odesłania kroku 7.1 do kroków 4, 5 i 6 nazywają pliki tych kroków; „A change of the definition after the gate goes through the gate again” (`:182–183`) do kroku 0 i do trybu zleconego.
- Recenzent przechodzi ręcznie przez pliki dróg 1, 3a, 4 i 5 z pytania 4, od `SKILL.md` do pliku ostatniego kroku, tak jak zrobiłby to agent, wypisuje, co na każdej zostaje i co odpada, i porównuje każdy wiersz tabeli oceny z miejscem, w którym fragment naprawdę stanął.
- Opis skilla (`description`) i kod w Pythonie się nie zmieniają, więc wejścia `the-way-*` też nie.
- Liczby słów powstają po ostatniej zmianie liczonego pliku, a pomocniczy skrypt porównuje z plikami każdą podaną liczbę, także liczby w prozie requestu, nie tylko sumy z raportem.

### Questions to settle

- 1. Co oprócz tekstu `project-level/skill/SKILL.md` przebudowa może ruszyć?
  - Answer: tylko katalog `project-level/skill/` — `SKILL.md` i nowe pliki obok. `project-level/definition_template.md` się nie zmienia i dalej jest czytany w całości w kroku 0; żaden inny plik the way się nie zmienia, bo odsyłają do tego skilla tylko po numerze kroku, a numery zostają. Powtórzenia z `project-level/lead/skill/SKILL.md:202–213` i z szablonem trafiają do requestu jako propozycje.
  - Not chosen:
    - także czytanie szablonu dopiero na krokach, które go używają — tura zlecona i tak potrzebuje większości szablonu, więc zysk to kilkaset słów na turę; zmienia treść kroku 0, wbrew ustaleniu serii „przebudowa zmienia miejsce reguł, nie ich treść”, i grozi zmianą definicji bez szablonu przed oczami; w zadaniu 6 odrzucony.
    - także usunięcie powtórzeń (`project-level/skill/SKILL.md:36–45`) — ok. 100 słów mniej w turze zleconej, ale to zmiana treści, którą recenzent musiałby ocenić merytorycznie, wbrew ustaleniu serii.
    - zostawić skill jak jest — nic dziś nie kosztuje, bo WAY-256 nie wiąże fragmentów stojących bez zmian, ale seria kończy się z otwartą pozycją, a cztery z sześciu przebiegów dalej niosą kroki, których nie używają.
  - Source: Mariusz, 2026-11-06: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: największy tekst, szablon (3221 słów), zostaje bez zmian, a zysk jest skromny i zależy od tego, czy tura zlecona czyta tylko swoje kroki. Szacunek z pytania: `SKILL.md` ok. 500–600 słów; tura zlecona czytająca swoje kroki ok. 1550–1750 wobec 1937, ponowne otwarcie zatwierdzonej definicji ok. 1250–1400, definicja od pomysłu ok. 2350–2550; na sześciu zapisanych przebiegach ok. 11 600 → 10 200 słów (−12%), z szablonem ok. −3 do −5%.
- 2. Czy agent tury zleconej przez `lead-project` dostaje wprost zgodę na czytanie tylko tych kroków, których dotyczy jego zlecenie?
  - Answer: nie — bez nowego zdania; zdanie „When `lead-project` dispatches a definition edit or step 7 through a refinement conversation path, read that file and `project-level/lead/conversation_template.md` first, verify its sources and process pin, and use this same workflow with file-mediated routing (WAY-156).” (`project-level/skill/SKILL.md:27–30`) przechodzi do pliku trybu zleconego bez zmiany, pliki kroków mają nazwy, po których agent pozna swój krok, a o tym, co agent wykonuje, mówi zlecenie.
  - Not chosen:
    - jedno nowe zdanie w pliku trybu zleconego, że tura przechodzi krok 0, robi zmianę i krok 7, a pliki innych kroków czyta tylko na odesłanie z 7.1 — druga po zadaniu 8 zmiana treści w serii i nowa reguła bez decyzji, która by ją niosła; agent, którego zmiana dotyka np. zakresu (krok 4), mógłby uznać, że tego kroku czytać mu nie wolno, a nie wyłapie tego żaden skrypt.
  - Source: Mariusz, 2026-11-06: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: oszczędność zależy od tego, jak agent odczyta „this same workflow”; czytając swoje kroki niesie ok. 1550–1750 słów skilla wobec 1937, czytając wszystko ok. 2350–2550, a sprawdzi to pierwsza prawdziwa tura w `loop2`. Stan: zlecenia orkiestratorów w `loop2` wskazują wprost sekcję trybu zleconego i krok 7 (Context).
- 3. Czy krytyk z kroku 7.3 i orkiestrator `lead-project`, którzy dziś czytają `SKILL.md` tego skilla z zewnątrz, mają dostać coś w zamian za tekst kroku 7, który przejdzie do pliku obok?
  - Answer: nie — wystarczy, że nagłówek kroku 7 z odsyłaczem do pliku kroku zostaje w `SKILL.md` (To do 2), więc czytelnik, któremu zlecenie podaje „SKILL.md step 7”, trafia na odsyłacz; orkiestrator swoje obowiązki ma w `project-level/lead/skill/SKILL.md:202–219`.
  - Not chosen:
    - plik kroku 7.3 każe podać krytykowi ścieżkę pliku kroku 7 wśród reguł — domyka przypadek krytyka, któremu ktoś poda samo „SKILL.md”, ale to nowa treść, wbrew ustaleniu serii, a zlecenia orkiestratorów już wskazują krok 7.
  - Source: Mariusz, 2026-11-06: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: krytyk, któremu ktoś poda samo „SKILL.md”, bez „step 7”, zobaczy tylko obraz całości; reguły oceny wpisów i tak stoją w szablonach. Stan: zlecenie krytyka w sesji `aa33930a` (2026-10-25) podaje „Rules: .the-way\project-level\definition_template.md, .the-way\project-level\skill\SKILL.md step 7, the decision and glossary-term element templates under .the-way\elements\.”
- 4. Na jakich drogach użycia request liczy słowa przed przebudową i po niej?
  - Answer: na pięciu: (1) definicja od pomysłu przez kroki 0–7; (2) wznowienie definicji w trakcie szukania wpisów (krok 0 → 5 → 6 → 7); (3) tura zlecona przez `lead-project`, zmiana definicji i bramka, w dwóch wersjach: (a) agent czyta tryb zlecony, krok 0 i krok 7, (b) agent czyta wszystko; (4) ponowne otwarcie wpisu zatwierdzonej definicji bez trybu zleconego (krok 0 → 7); (5) definicja bez sekcji „Technology”, otwarta ponownie (krok 0 → 6 → 7). Na każdej dwie liczby: sam tekst skilla oraz suma z plikami czytanymi obok — `project-level/definition_template.md` (cały, krok 0), sekcja „How a skill asks”, sekcja „Reading the foundation” (krok 2, droga 1) i `project-level/lead/conversation_template.md` (droga 3). Pliki wywoływanych skilli (`find-foundation-entries`, `settle-technology`, `critique`, skille wpisów), sama definicja i pliki produktu są poza liczeniem. Słowa liczy skrypt jak `wc -w`, w stanie „przed” na `dfd50e5`; recenzent przechodzi ręcznie drogi 1, 3a, 4 i 5.
  - Not chosen:
    - trzy drogi (1, 3, 4) — krótszy opis, ale znikają drogi 2 i 5, a tylko one pokażą koszt pliku wariantu przy kroku 0 i odsyłaczy między krokami 5–7.
    - liczyć też pliki wywoływanych skilli — pełniejsza suma, ale `find-foundation-entries` przebudowuje zadanie 7, więc liczba zależałaby od kolejności scalenia, a te pliki w tym zadaniu się nie zmieniają.
    - jedna liczba, słowa w `SKILL.md` — najtaniej, ale pokaże ok. −70% zamiast realnych ok. −35% do +30%, a ktoś może oprzeć na tym wniosek o serii.
  - Source: Mariusz, 2026-11-06: „tak jak rekomendujesz” — na rekomendację pięciu dróg, ze słabym punktem nazwanym w pytaniu: to liczby słów w plikach, nie zachowanie agenta; liczy skrypt, a pracą agenta jest przejście czterech dróg przez recenzenta.
- 5. Kiedy i czym mierzymy niesiony tekst po scaleniu?
  - Answer: przy następnym prawdziwym użyciu skilla w `loop2`, skryptami serii z datą początkową po scaleniu, nie przy domknięciu zadania; do tego czasu główną miarą zostają słowa z requestu, a gdy użycie pójdzie w Codexie, porównanie liczy się osobno z jego zapisów.
  - Not chosen:
    - pomiar przy domknięciu — liczba mówi tylko, ile czasu minęło, a wygląda jak wynik.
  - Source: odpowiedź z zadania 8 (notatka zadania 8 serii w backlogu autora, pytanie 6): Mariusz, 2026-10-31: „Tak” — ze słabymi punktami nazwanymi tam: porównanie może długo czekać, a `skill_carry_cost.py` potrzebuje parametru daty; przeniesione też do zadania 6 (pytanie 5). Przeniesienie pokazano Mariuszowi 2026-11-06 w pytaniu 4: „tak jak rekomendujesz”.
- 6. Czy agenci cyklu czytają metody z worktree zadania, jak w poprzednich zadaniach serii?
  - Answer: tak — z worktree zadania, zwykłą drogą cyklu, bez kopii na commicie bazowym; `task-cycle/` nie wymienia `define-project`, więc przebudowa nie zmienia niczego, czym cykl pracuje.
  - Not chosen:
    - kopia the way na commicie bazowym — krok więcej na starcie, który nic nie chroni.
  - Source: odpowiedź z zadania 8 (notatka zadania 8 serii w backlogu autora, pytanie 7): Mariusz, 2026-10-31: „Tak”. Stan kodu: `task-cycle/` na `dfd50e5` nie wymienia tego skilla. Przeniesienie pokazano Mariuszowi 2026-11-06 w pytaniu 4: „tak jak rekomendujesz”.
- 7. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak wcześniejsze zadania serii; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Not chosen:
    - czekać na wytyczne samego the way — seria stoi bez żadnego zysku.
  - Source: odpowiedź z zadania 8 (notatka zadania 8 serii w backlogu autora, pytanie 8): Mariusz, 2026-10-31: „Tak”. Przeniesienie pokazano Mariuszowi 2026-11-06 w pytaniu 4: „tak jak rekomendujesz”.

## Context

- Zadanie jest jedenastym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, przebudowa zmienia miejsce reguł, nie ich treść, domknięcie zadania przestawia serię) stoją w notatce serii w prywatnych notatkach autora, sekcja „Ustalone”.
- Zadanie idzie przed zadaniami 7 (`find-foundation-entries`) i 10 (`lead-project`); zadanie 7 jest doprecyzowywane w tym samym czasie w osobnej sesji. Krok 5 tego skilla wywołuje `find-foundation-entries`, ale nie odsyła do żadnej jego sekcji, więc oba PR-y nie dotykają tych samych plików.
- Podstawą jest `foundations` po PR #76, commit `dfd50e513c09bebe9d09d74209cd28612565da83`; `project-level/skill/SKILL.md` zmienił się ostatnio w commicie `4a3ee37`.
- W zapisach Claude Code od 2026-09-01 skill przeszedł w `loop2` sześć razy: jedna definicja od pomysłu przez bramkę (`a2c2a1d6`, 2026-11-01, `/the-way-define-project`), cztery tury zlecone przez `lead-project` — zmiana definicji i bramka (`af5fae28`, 2026-10-25; `aed58d91`, 2026-10-28; `ac880376`, 2026-10-29; `ad790bb4`, 2026-11-03) — i jedno ponowne otwarcie wpisu zatwierdzonej definicji z bramką, wywołane narzędziem Skill z sesji doprecyzowania zadania (`9baf7986`, 2026-10-13).
- Orkiestratorzy `lead-project` w zleceniach tur zleconych wskazują wprost sekcję „Delegated definition change and gate” i krok 7.
- Poza przebiegami `SKILL.md` tego skilla czytali w `loop2` orkiestratorzy `lead-project` (sesje `41653e57`, `2ec66018`, `df5b6e70`, `469eeb85`) i krytyk bramki z kroku 7.3 (`aa33930a`, 2026-10-25), któremu orkiestrator podał `SKILL.md` jako regułę.
- Pozostałe zapisy z tą ścieżką — 53 w repo the way i w vaulcie oraz 4 w `loop2` (inwentaryzacja obowiązków procesu i przegląd zmiany) — to praca nad samym the way: cykle zadań, przeglądy, odchudzanie, a nie użycie skilla.
- W zapisach Codexa ścieżka skilla pada w 4 plikach `.jsonl` i 96 plikach `.jsonl.zst`; wywołanie narzędzia z tą ścieżką ma tylko jedna sesja, w repo the way (2026-10-03), a obejrzane trafienia z `loop2` to cytaty z `installation/install.py`.
- Numerów kroków tego skilla używają: `project-level/technology/start.md:8` („return to `define-project` step 5”), `project-level/lead/skill/SKILL.md:208` („`define-project` step 7 in delegated mode”), `project-level/plan/skill/existing_plan.md:9` („`define-project` step 7 again”) i zlecenia orkiestratorów („step 7.3”); nazw jego sekcji nie przytacza żaden plik the way.
- Skill wymieniają też `elements/common/projected_mode.md:4`, `:11`, `elements/common/skill/SKILL.md:82`, `project-level/plan/skill/read.md:4`, `project-level/task/skill/read_sources.md:15`, `project-level/technology/close.md:10–11`, `installation/install.py:31` i `installation/README.md:57`; `task-cycle/` go nie wymienia.
- Druga część sekcji „Delegated definition change and gate” (`project-level/skill/SKILL.md:36–45`) mówi o tym, co wolno orkiestratorowi; to samo stoi w `project-level/lead/skill/SKILL.md:202–213` i w WAY-156.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. A fragment that some steps of the skill need, not all, stands by what it is: a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did; fragments that stand unchanged are not bound by it.” — według niej przebudowuje się skill.
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.” — nie zmienia się.
- **WAY-265** — „In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file points to is named in the skill's `SKILL.md` at that step as well, with the condition under which it is read. A step's file that stands unchanged, with the variant file it points to, is not bound by it.” — nie zmienia się.
- **WAY-106** (fragment) — „The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries.” — nie zmienia się; niesie ją zdanie `project-level/skill/SKILL.md:22–23`.
- **WAY-112** (fragment) — „It writes each answer and the updated `Status:` line before the next question; work resumes from that line and, while entries are being found, from the candidate table.” — nie zmienia się; niesie ją krok 0 i krok 4.
- **WAY-118** (fragment) — „Before approval an agent searches the whole current foundation once for what the definition and its projected entries touch, linked or not, the only search of the whole foundation on the way to the gate […] A change to those sections after approval goes through the gate again before breakdown relies on it.” — nie zmienia się; niesie ją krok 7.
- **WAY-156** (fragment) — „The project orchestrator changes definition text itself only when that text is already before it and needs no reading of other definition sections or the foundation; otherwise it delegates the edit, and a subagent always performs the definition's readiness gate, with independent critique dispatched by the project orchestrator and its findings returned to that subagent, and human approval given through the project orchestrator.” — nie zmienia się; niesie ją sekcja trybu zleconego.
- **WAY-120** (fragment) — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — nie zmienia się; niesie ją krok 7.3.
- **WAY-113** (fragment) — „An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel.” — nie zmienia się; niesie ją sekcja „How a skill asks”, którą skill każe przeczytać w kroku 0.
- **WAY-111** (fragment) — „Before drafting, the agent selects and reads the current foundation under WAY-150, identifying touched parts from the proposed project's responsibilities, behaviour, flows and surfaces.” — nie zmienia się; niesie ją krok 2.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in […]” — nie zmienia się; droga sesji na samym the way.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się; droga sesji w produkcie.

## Settlements to record

Candidates: 6 shown, 0 accepted — 2026-11-06

none

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”): odhaczyć linię „seria skilli 11/11” w backlogu autora, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie następnego niescalonego zadania serii (7 albo 10) i ustawić jego linii datę dnia domknięcia.
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym cyklem (notatka serii, „Ustalone”).
- Uwagi z wcześniejszych PR-ów serii — nie przechodzą do tego zadania, poza tymi, które rozstrzygają jego pytania.
- Pozostałe skille the way — zadania 7 i 10 serii.
