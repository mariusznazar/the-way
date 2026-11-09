---
title: "the way: zadanie zbiorcze z uwag PR-ów — cykl zadania, krok technologii, brzmienie decyzji"
status: draft
created: 2026-11-08
updated: 2026-11-09
tags: [zadanie]
related: "the project note of the process"
---

# the way: zadanie zbiorcze z uwag PR-ów — cykl zadania, krok technologii, brzmienie decyzji

Status: ready for cycle
Project relation: independent

## Description

### Need

- Pierwszy przegląd fundamentu the way (2026-11-06/07) znalazł w opisach scalonych PR-ów 35 niezałatanych uwag o cyklu zadania, kroku technologii, brzmieniu decyzji, README i dwóch narzędziach; wszystkie dalej stoją na `foundations` `a3206c1` (sprawdzone 2026-11-08).
- Agent cyklu albo kroku technologii dostaje w tych tekstach reguły sprzeczne ze sobą albo z decyzjami, odesłania bez celu i zdania, które mówią więcej niż źródło; Mariusz dostaje z tego powtórzone pytania (wykreślona sprawa wraca), PR bez świeżych zmian gałęzi docelowej, test, który pada bez winy zmiany, i skrypt uwag, który po cichu pomija raporty.
- Przegląd warstwy AI z 2026-11-09 dołożył dwie sprawy: agent doprecyzowania zadania rekomenduje podział bez potrzeby, a Mariusz go cofa — w ostatnim tygodniu kilka razy (AIR-618, punkt 30); opis pozycji w skrypcie uwag przeczy jego kodowi (AIR-617, punkt 8).
- Odbiorcą jest agent cyklu zadania i kroku technologii w produkcie, który używa the way (dziś `loop2`), i w samym the way, oraz Mariusz, który odpowiada na ich pytania i scala PR-y.

### To do

Cykl zadania (`task-cycle/`):

1. Poprawka po uwagach człowieka, scalając gałąź docelową, robi przy tym to, co krok 12: gdzie scalenie zmienia zrecenzowany kod, świeży recenzent recenzuje scalenie, a sprawdzenia, których scalenie dotyka, biegną znowu (theway#022-1; `skill/correction.md:26-27` wobec `skill/SKILL.md:415-417`).
2. Uzgodnienie przed otwarciem PR-a w kroku 12 scala zdalną gałąź docelową, jak poprawka (`correction.md:26`) i jak uzasadnia WAY-298 (theway#076-4; `skill/SKILL.md:416`).
3. Zdanie „The cycle writes only in the task's worktree” wymienia jedyny wyjątek, przewinięcie gałęzi docelowej z kroku 4 (theway#076-2; `skill/SKILL.md:68` wobec `:116-117` i WAY-298).
4. Skill wykonawcy kawałka (`task-cycle/change/`) mówi, że gdy zakresy linii w zleceniu różnią się od zakresów z planu, obowiązują bieżące (theway#039-3; reguła dla prowadzącego stoi w `skill/planning.md:36-37`).
5. Druga droga sprawdzeń bazy — osobna kopia bazy pod `.runs/` — mówi, że w produkcie trzeba w tej kopii przed sprawdzeniami zainstalować zależności i wypełnić `.the-way`, bo inaczej sprawdzenia padają z tego powodu, a nie na bazie (theway#061-2; `skill/SKILL.md:125-127`).
6. W szablonie opisu PR-a (`skill/request_template.md`):
   - punkt *Questions* wskazuje plik `skill/foundation_step.md`, który mówi, na jakie pytania krok fundamentu pozwala (theway#050-3; `:165`);
   - punkt o dopisaniach do listy tego, co produkt loguje, mówi, gdzie ich szukać: w zmianie reguły zakresu logowania produktu w diffie (theway#074-3; `:219-221`).
7. Odczyt stanu planu (`project-level/plan_state.py`) pokazuje zadanie, którego cykl skończył się zablokowanym szkicem PR-a otwartym po zapisie (`skill/blocked_finding.md`, `skill/reserved_return.md`), jako zablokowane, a nie jako zadanie bez PR-a; zapis cyklu na obu drogach ma w *Request URL and status* brzmienie, które skrypt rozpoznaje (theway#071-17; `blocked_finding.md:10-14`, `reserved_return.md:56`, `plan_state.py:27`, `:146-158`).
8. Skrypt uwag (`remarks_check.py`) czyta raporty po nazwie tak, jak ustalił ai-review (AIR-607; theway#074, #075, #079, #080), a jego opis pozycji sekcji mówi to, co robi kod (AIR-617):
   - czyta wszystkie pliki `.md` z `reports/`, których nazwa nie zawiera `handoff` ani `findings`; docstring: „The reports are the `.md` files of `reports/` whose name holds neither `handoff` nor `findings`, read in the order of their names; a handoff, a findings file and a log are not read.” (`:12-13`, `:318`);
   - test `test_only_files_whose_name_ends_in_report_are_read` (`test_remarks_check.py:362`) sprawdza, że `review_whole.md` i `report-planner.md` są czytane, a `01-author-handoff.md`, `handoff_author.md`, `slice-1-findings.md`, `notes.txt` i `gate.log` nie;
   - `skill/SKILL.md:140` mówi, że zlecenie stoi w pliku `reports/`, którego nazwa zawiera `handoff`; `:474` dopisuje „, a file whose name holds neither `handoff` nor `findings`”;
   - opis pozycji sekcji w docstringu (`:26-27`) mówi to, co robi kod (`:165-168`) — akapit pod listą też jest pozycją (AIR-617; the-way PR #85, `define-project-skill-shape/cycle.md:174`): „The items of a section are its list items, each with the lines that continue it and its sub-items, and its paragraphs, a paragraph after a list included, so that nothing written in the section goes unread.”
9. Test instalatora `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink` nie pada, gdy w trakcie pełnego przebiegu testów ktoś zrobi commit w repozytorium the-way (theway#070-12; `installation/test_install.py:39`, `:145-149`, `:216`, `:228`).

Krok technologii (`project-level/technology/`):

10. Krok, pokazując listę do potwierdzenia (`list.md:31-32`), mówi, że sprawy logów, interfejsu, danych deweloperskich i powiadamiania o awarii nie da się z niej wykreślić; człowiek, którego sprawa nie dotyczy, odpowiada na nią jak na każdy wybór, a ta odpowiedź ją rozstrzyga, więc przy wznowieniu nie wraca jako otwarta (pytanie 1; theway#024-1 = theway#065-12; `start.md:15-16`, `running_product.md:34-35`).
11. Przebieg przy zadaniu przerwany między zapisaniem notatki a zapisaniem jej pozycji, wznowiony, listuje wybór z tej notatki, zamiast zamknąć się bez niego (theway#063-9; `task_run.md:27-29`, `:37`).
12. Odszukanie decyzji rzutowanej przy wznowieniu (`start.md:22-26`), kończąc pozycję `— projected`, usuwa linię zagnieżdżoną pod nią, jak robi to `settle.md` (podkrok 7) (theway#065-1).
13. Spojrzenie na powiadamianie o awarii (`failure_notice.md:13-15`) szuka też decyzji rzutowanej tej definicji i daje wtedy `— projected`, jak `list.md:21-22`, zamiast `— open` (theway#065-4).
14. Jeden z dwóch plików `settle.md` — kroku technologii albo krytyki (`elements/common/critique/settle.md`) — dostaje inną nazwę, tak że agent kroku technologii, czytając w krytyce „the author reads `settle.md` beside this skill”, nie otworzy swojego pliku (theway#059-3; `elements/common/critique/SKILL.md:37`).
15. Gdy żadna opcja sprawy dostępu agenta do działającego produktu nie pozwala agentowi jej użyć, krok poleca opcję według pozostałych skutków i mówi wprost jednym zdaniem, że żadna opcja nie pozwala agentowi sprawdzić działającego produktu tą drogą, więc to sprawdzenie zostaje przy człowieku; WAY-166 i plik kroku mówią to samo (pytanie 2; theway#024-5).
16. WAY-139 wiąże pozycję skilla wdrożenia „how to read the logs” z decyzją o logach tak jak pozycje o życiu zapisu i o awarii: gdy decyzja fundamentu albo zatwierdzonej definicji, którą zadanie niesie, na to odpowiada, doprecyzowanie ją cytuje, a zadanie dostaje punkt, który przepisuje odpowiedź do skilla; bez takiej decyzji pozycja idzie jak dziś. `project-level/task/skill/resolve_gaps.md` mówi to samo (pytanie 3; theway#024-9; WAY-165 „how an agent reads it”).

Brzmienie decyzji (`foundations/decisions.md`):

17. WAY-165:
    - zdanie o danych deweloperskich nie czyta się jak zamknięta para dwóch opcji: dane stawiane od zera i trwałe środowisko testowe są przykładami, żadna nie jest wykluczona, a opcje daje badanie (WAY-122), jak mówi już uzasadnienie („neither is ruled out”); to samo zdanie w `project-level/definition_template.md:182-184` (theway#024-2);
    - zastrzeżenie „holds the choice like any decision, which opens only on the human's word” dotyczy decyzji fundamentu; decyzji rzutowanej zatwierdzonej definicji żaden przebieg nie otwiera, jak mówią WAY-267 i `task_run.md:58-59` (theway#065-10);
    - zdanie o wpisie, który odpowiada na część sprawy, nie powołuje się na WAY-270, bo WAY-270 o tym nie mówi; relacja „derives from WAY-270” zostaje tylko tam, gdzie inne zdanie WAY-165 na niej stoi (theway#065-3).
18. Przykład zgodności WAY-166 rekomenduje wyjście kontenera serwera „kept in a store that outlives a redeployment”, jak przykład WAY-165 (theway#065-14).
19. Zdanie WAY-128 o punktach wejścia skilli wymienia też WAY-259 (theway#051-1).
20. *Verification* WAY-292 mówi, że skrypt formy zgłasza powtórzony blok przy zadaniu po angielsku tam, gdzie umie odczytać dokument zadania jako angielski, jak zdanie wiążące (theway#071-14).
21. *Verification* WAY-05 ma dwie pary `complies`/`violates` zamiast jednej pary z dwoma niezwiązanymi przykładami po średniku (theway#072-1).
22. WAY-293: *Rationale* podaje powód bez opisu tego, co dziś robi albo czego nie ma szablon opisu PR-a, czego zabrania WAY-05 (theway#072-2); odrzucony wariant „no change, which withdraws the rule” mówi, że brak zmiany zostawia krok powrotu bez pierwszeństwa (theway#072-3).
23. Lista WAY-287 wymienia też listing skryptu uwag uznany za błędny i błąd skryptu formy uznany za błędny, które WAY-295 i WAY-291 już wstawiają do sekcji decyzji człowieka (theway#074-4; `request_template.md:214`, `:54`).
24. WAY-148 żąda linii wyniku sprawdzeń od każdego etapu, który uruchamia test albo inne sprawdzenie, bez zawężenia „of the product”, więc zwrot planisty z wynikiem skryptu rozmiaru (`task-cycle/plan/SKILL.md:201-203`) jest z nią zgodny (pytanie 5; theway#072-6).

Szablon zadania, find-foundation-entries, README, pliki instrukcji, mapa części:

25. Szablon zadania mówi, że trwałe wykluczenie, na którym opiera się dalsza praca, należy do decyzji, jak `project-level/task/skill/SKILL.md:51` (theway#041-2; `project-level/task/template.md:203-204`).
26. Krok 2 find-foundation-entries wyłącza kandydata, którego wpis z kroku 1 już ustala, zanim tabela zostanie zapisana i pokazana (theway#032-6; `elements/common/skill/build_table.md:12-15` po `:3`; pokazanie tabeli w `task_variant.md:31` i `definition_variant.md:27-28`).
27. README:
    - zdanie o `product-guidelines/` mówi o szablonie i skillu dla każdej dyscypliny, dla której the-way daje szablon, jak WAY-09 (theway#025-29; `README.md:115-116`);
    - zdania o źródłach (`README.md:48-49`, `:75`) obejmują też odczyt stanu hosta, który ludzie produktu uruchamiają, jak WAY-80 (theway#047-2).
28. Skill plików instrukcji (`instruction-files/SKILL.md`):
    - „How to write a single rule” mówi, że rzeczy nazywa się słowami czytelników produktu, co dziś stoi tylko w trybie pisania (`writing.md:14`) (theway#049-2);
    - zdanie o nadmiarze wyróżnień mówi tyle, co źródło — ostrożnie i o Claude, nie stanowczo o każdym modelu (theway#049-5; `:230-231`).
29. Mapa części dopisuje `installation` do *Depends on* części `task-cycle`, bo skill cyklu przy przesuwaniu przypięcia odsyła do `installation/README.md` (pytanie 4; theway#050-9; `task-cycle/skill/SKILL.md:41-43`, `foundations/part_map.md:98-99`).
30. Krok czytania źródeł przy doprecyzowaniu zadania zaczyna od jednego zadania i dzieli je tylko z nazwanego powodu (AIR-618 — Mariusz w kilku sesjach cofał rekomendowany podział; `project-level/task/skill/read_sources.md:23`): zdanie „Check that this is one task. If it joins independent outcomes, identify the split.” → „Check that this is one task. Keep one task by default: each split adds a full cycle. Identify a split only where a part cannot start or finish without something outside this refinement — access the agent lacks, another task's result — or where a later step of this skill offers one, and name that reason; a task's size alone (WAY-13) you name as a signal and leave the split to the human.”

### Questions to settle

- Pytanie 1: co dzieje się ze sprawą logów, interfejsu, danych deweloperskich albo powiadamiania o awarii, którą człowiek wykreślił z listy wyborów technologii?
  - Answer: tych czterech spraw nie da się wykreślić; człowiek, którego sprawa nie dotyczy, odpowiada na nią jak na każdy wybór (np. „narzędzie nie ma logów, agent czyta wyjście konsoli”), a odpowiedź ją rozstrzyga. Słaby punkt przyjęty z tą drogą: przy produkcie, którego sprawa nie dotyczy, człowiek pisze jedno zdanie odpowiedzi zamiast skreślenia.
  - Not chosen:
    - wykreślona sprawa zostaje na liście z nowym oznaczeniem `— struck` — nowe oznaczenie w trzech szablonach i w sprawdzeniu gotowości, a sprawa stoi rozstrzygnięta bez odpowiedzi, wbrew WAY-165, i agent cyklu zgaduje, skąd czyta logi.
    - zostawić jak jest — przy każdym wznowieniu człowiek wykreśla to samo i dwa razy ogląda listę.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; `project-level/technology/list.md:31-32`, `start.md:13-16`, `running_product.md:17-20`, `foundations` `a3206c1`.
- Pytanie 2: co rekomenduje krok technologii, gdy żadna opcja sprawy dostępu agenta do działającego produktu nie pozwala agentowi jej użyć?
  - Answer: krok poleca opcję według pozostałych skutków i mówi wprost jednym zdaniem, że żadna opcja nie pozwala agentowi sprawdzić działającego produktu tą drogą, więc to sprawdzenie zostaje przy człowieku. Słaby punkt przyjęty z tą drogą: krok nie szuka drugi raz opcji, której agent mógłby użyć; brak wychodzi przed wyborem i odpowiada na niego człowiek.
  - Not chosen:
    - krok najpierw szuka dalej opcji, której agent może użyć (np. wysyłanie logów do miejsca, które agent czyta), i dopiero bez wyniku idzie drogą a — dłuższe badanie przy każdej takiej sprawie, często dodatkowa usługa do opłacenia, a WAY-122 i tak każe szukać opcji badaniem.
    - krok nie poleca nic — wyjątek od WAY-113, człowiek odpowiada bez podpowiedzi.
    - zostawić jak jest — przypadek wychodzi przy pierwszym produkcie z takim hostingiem i każdy agent rozwiąże go inaczej.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-166 `foundations/decisions.md:4697-4700`, `foundations` `a3206c1`.
- Pytanie 3: które miejsce odpowiada, jak czytać logi wdrożonego produktu — skill wdrożenia (WAY-139) czy decyzja o logach (WAY-165)?
  - Answer: decyzja o logach; WAY-139 wiąże pozycję „how to read the logs” z decyzją fundamentu albo zatwierdzonej definicji tak jak pozycje o życiu zapisu i o awarii, a skill powtarza jej odpowiedź; bez takiej decyzji pozycja idzie jak dziś, jako punkt *To do*. Słaby punkt przyjęty z tą drogą: skill dalej powtarza tekst decyzji, więc zmiana decyzji wymaga przepisania go do skilla.
  - Not chosen:
    - skill mówi, jak logi czyta człowiek, a decyzja, jak czyta je agent — dalej dwie odpowiedzi, zwykle takie same, więc mogą się rozjechać.
    - zostawić jak jest — rozjazd wychodzi dopiero, gdy agent trafi na dwa różne przepisy.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-139 `foundations/decisions.md:3642-3652`, WAY-165 `:4636-4638`, `foundations` `a3206c1`.
- Pytanie 4: czy cykl zadania może zależeć od instalatora?
  - Answer: tak; mapa części dopisuje `installation` do zależności `task-cycle`, a przepis przesunięcia przypięcia zostaje w `installation/README.md`. Słaby punkt przyjęty z tą drogą: `task-cycle` i `installation` zależą od siebie nawzajem, jak już `product-guidelines` i `installation`.
  - Not chosen:
    - skill cyklu sam opisuje przesunięcie przypięcia — ten sam przepis w dwóch miejscach, które rozjadą się przy następnej zmianie instalatora.
    - zostawić mapę i zapisać rozjazd jako znany — mapa dalej nie mówi prawdy, a każdy krok powrotu zgłosi to od nowa.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; `foundations/part_map.md:98-99`, `task-cycle\skill\SKILL.md:41-43`, `foundations` `a3206c1`.
- Pytanie 5: czy planista oddaje w zwrocie wynik sprawdzeń?
  - Answer: tak; WAY-148 traci zawężenie „of the product” i linię wyniku podaje każdy etap, który uruchamia test albo inne sprawdzenie; skill planisty zostaje. Słaby punkt przyjęty z tą drogą: zmienia się brzmienie przyjętej decyzji, a etap, który niczego nie uruchamia, dalej tej linii nie podaje.
  - Not chosen:
    - skill planisty traci linię wyniku — prowadzący dowiaduje się o niesprawdzonej ścieżce skryptu rozmiaru tylko z pełnego raportu, którego przy zwykłym przejściu nie czyta.
    - zostawić jak jest — o linii decyduje to, czy agent czyta skill czy decyzję, a recenzent porównujący z decyzją znów to zgłosi.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-148 `foundations/decisions.md:4001-4004`, `task-cycle\plan\SKILL.md:186-188`, `:201-203`, `foundations` `a3206c1`.
- Pytanie 6: czy zadanie czeka na własne wytyczne kodowania i testów the way, skoro repozytorium the-way nie ma `guidelines/`, a WAY-215 trzyma zadanie piszące kod albo testy w produkcie bez wytycznych w doprecyzowaniu?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way, a rozjazd reguły z praktyką zostaje w zadaniu the note on the-way's own guidelines.
  - Not chosen:
    - czekać na zadanie o wytycznych the way — to zadanie nie ma jeszcze kierunku, więc poprawki stałyby bez terminu.
  - Source: odpowiedź przeniesiona z pytania 4 zadania the sibling task note on the guidelines skills: Mariusz, 2026-11-07: „nie czeka”; WAY-215 `foundations/decisions.md`, `foundations` `f447bb6`.

## Context

- Zadanie zbiera drobne poprawki w jedno zadanie zamiast osobnych, jak Mariusz ustalił dla uwag z przeglądu (zadanie przeglądu fundamentu, pytanie 12); to druga połowa uwag the way, pierwsza to the sibling task note on the guidelines skills.
- Źródło uwag: `a document in the author's private notes`, sekcja „Zadanie 7 (the way): zbiorcze — cykl, krok technologii, brzmienie decyzji” — przy każdej uwadze słowa recenzenta, miejsce i stan sprawdzony 2026-11-06 na `foundations` `e0a71f4`.
- Wszystkie 35 uwag sprawdzono ponownie 2026-11-08 na `foundations` `a3206c1` (77 commitów później): każda stoi; theway#032-6 przeniosła się z `elements/common/skill/SKILL.md` do `build_table.md` i plików wariantów, z tą samą kolejnością. Numery linii w *To do* są z `a3206c1`; punkt 30 i ostatni podpunkt punktu 8 — z `f218b55`; cykl szuka miejsca po treści.
- Dwa zadania, po których plik źródłowy kazał sprawdzić theway#032-6 i theway#076-4 (przebudowa find-foundation-entries, zlecenie przeglądu scalenia), są scalone; obie uwagi dalej stoją.
- README nie wiąże niczego (WAY-09, `foundations/part_map.md`, „Files left out on purpose”), więc punkt 27 nie zmienia gwarancji ani decyzji.
- Punkty 17–23 zmieniają brzmienie przyjętych decyzji tylko tam, gdzie inny wiążący tekst albo uzasadnienie tej samej decyzji już mówi to, co poprawka; przyjęcie całego dokumentu jest zgodą na te zmiany (WAY-30).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Cytaty z `foundations/decisions.md`, `foundations` `a3206c1`; numer linii to nagłówek decyzji.

- WAY-05 — How is a decision entry written? (`:124`): „[…] rationale and rejected options in prose, which, where the entry's author writes it rather than quotes a source, names no file, script or count […] nor what the process's own tools do or lack today, and does not tell how the decision was reached.” Podstawa punktów 21 i 22.
- WAY-09 — What may enter the process repository? (`:219`): „[…] `product-guidelines/` the template that the guidelines of every product share, for each discipline of work whose guidelines the-way gives a template of, that template with the skill that leads the work on them […].” Podstawa punktu 27.
- WAY-13 — What sets the weight of a task's process? (`:400`, `f218b55`): „[…] and otherwise serves only as a signal to split it […]”. Punkt 30: rozmiar zostaje sygnałem, który agent nazywa, a podział rozstrzyga człowiek.
- WAY-80 — What is an environment fact's source? (`:1810`): „A state of a host the product's people run, which no page shows and only those with access to the host can read, has for its source a reading: the command, the host it ran on and the tool with its version, its output word for word or the lines of it the sentence rests on, and the date run.” Podstawa punktu 27.
- WAY-113 — How does an agent of the-way ask a human decision? (`:2533`) — pytanie o decyzję daje drogi, ich koszt i rekomendację (`elements/common/way_of_working.md`, „How a skill asks”). Podstawa odpowiedzi na pytanie 2.
- WAY-121 — Where does a project settle the technology it needs? (`:2759`): „[…] where the project brings behaviour a user sees in the running product, the step looks at three matters of an agent's way to the running product — its logs, its interface and its development data — and lists as a choice of its own each matter that no decision of the foundation settles for that behaviour […].” Zmienia się według pytania 1 (punkt 10).
- WAY-128 — What may a line of an instruction file that a tool loads into every session hold, and where does any other rule stand? (`:3134`): „[…] the lines of process skills and their entry points answer to WAY-35, WAY-127 and WAY-256 instead.” Zadanie dopisuje WAY-259 (punkt 19).
- WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one? (`:3640`): „[…] how to read the logs; how long the record lives, between deployments too; and how a human learns of a failure. […] For the two items on the record's life and on a failure, the check quotes the answer a decision of the foundation or an approved definition the task carries already gives, and the task gains the item that writes it into the skill […].” Zmienia się według pytania 3 (punkt 16).
- WAY-148 — How do task-cycle stages pass their work to the orchestrator? (`:3999`): „[…] its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check of the product, and the report's path […].” Zmienia się według pytania 5 (punkt 24).
- WAY-165 — What must an answer to each matter of an agent's way to the running product settle? (`:4634`): „[…] Data set up from scratch and a dedicated test environment that persists are both options of that choice, and an entry, a decision of the foundation or a projected decision of a definition, that leaves part of what a matter asks unanswered does not settle that matter at a project definition, while in a run at a task (WAY-267) it holds the choice like any decision, which opens only on the human's word.” *Rationale:* „[…] so it settles nothing at a definition, whether its answer is good or not (WAY-270) […] so neither is ruled out and the step weighs them by their consequences (WAY-123).” Punkty 17 i 18.
- WAY-166 — How does whether an agent can use an option weigh in a choice of its way to the running product? (`:4695`): „[…] an option an agent cannot use stays in the comparison with that lack said as "an agent does not check the running product this way", and the recommendation passes over it.” Zmienia się według pytania 2 (punkt 15) i w przykładzie zgodności (punkt 18).
- WAY-259 — What does an installed skill entry point tell an agent to read from the pinned the-way? (`:7700`): „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full.” Punkt 19.
- WAY-267 — How does the step that settles technology run outside a project definition? (`:7922`): „[…] a human may run it for any choice save one a projected decision of an approved definition settles, which no run reopens, and a choice a decision of the foundation holds opens only on the human's word, the result then being a change of that decision.” Podstawa punktu 17 (zastrzeżenie o decyzji rzutowanej).
- WAY-270 — When does the step that settles technology ask how a human learns of a failure of the running product? (`:8114`): „[…] lists how a human learns of a failure of the running product as a choice of its own, answered by a tool that collects failures, an alert or a deliberate absence, even where its answer adds nothing to run, pay for or back up; in a run at a task (WAY-267) it enters the list only where the note touches it. No definition has to hold this choice, the readiness gate does not check it […].” Przy pytaniu 1 człowiek, którego ta sprawa nie dotyczy, wybiera zamierzony brak, który WAY-270 zawsze stawia w porównaniu.
- WAY-287 — What does a request put before the human for a decision? (`:8803`): „The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — […] the additions a change makes to a product's logging scope, and the foundation entries the human did not see at the task document — and its `none` says that nothing else in the request waits for the human's yes.” Punkt 23.
- WAY-291 — What does the cycle do with an error of the form check that it holds wrong? (`:8957`): „[…] the request opens, or stays, a draft whose section for the human's decisions names the error and the cycle's reason […].” Podstawa punktu 23.
- WAY-292 — What does the collapsed block of a request's description hold where the task document is in English? (`:8990`): „[…] and the form check, wherever it reads the task document as English, holds the block to `none`.” Punkt 20.
- WAY-293 — What prevails where a task or its spec excludes the entry for a choice? (`:9015`): „Where a task or its spec explicitly excludes an entry in the foundation for a choice, that exclusion prevails over the rule that a choice binding after the merge is written into the foundation […].” Punkt 22.
- WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give? (`:9056`): „[…] the orchestrator runs the-way's script that lists each item other than `none` under **Searches not found or unclear** in the record's stage reports that the record's process remarks do not hold word for word […].” Podstawa punktu 8.
- WAY-295 — What does the cycle do with a listing of the remarks check that it holds wrong? (`:9096`): „[…] the orchestrator enters the case in the record's process remarks as a case of the script, not as an item of its stage, and names it in the request's section for the human's decisions.” Podstawa punktu 23.
- WAY-298 — How does a cycle on the-way itself start from the current rules? (`:9191`): „[…] and the merge of the target branch it makes takes the remote branch, in a product as well. The fast-forward is the one change the cycle makes outside the task's worktree.” Podstawa punktów 2 i 3.
- WAY-306 — What does the review of the merge of the target branch ask? (`:9496`): „Where merging the current target branch into the task branch changes the code the cycle reviewed, the dispatch of the fresh reviewer of the merge asks whether the two sides, the task branch and what the merge brought in, still hold together […].” Podstawa punktu 1.

## Settlements to record

Candidates: 8 shown, 5 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Sprawy logów, interfejsu, danych deweloperskich i powiadamiania o awarii nie da się wykreślić z listy wyborów technologii; człowiek, którego sprawa nie dotyczy, odpowiada na nią jak na każdy wybór, a odpowiedź ją rozstrzyga. | decision | pytanie 1 | czy zapisać zakaz wykreślania w decyzji (WAY-121, WAY-165) z odrzuconymi drogami, czy tylko w `list.md` |
| 2 | Gdy żadna opcja sprawy dostępu agenta do działającego produktu nie pozwala agentowi jej użyć, krok poleca opcję według pozostałych skutków i mówi jednym zdaniem, że to sprawdzenie zostaje przy człowieku. | decision | pytanie 2 | czy dopisać przypadek do WAY-166, czy tylko do pliku kroku; co polecić, gdy nie ma czego polecić |
| 3 | Pozycję skilla wdrożenia „how to read the logs” wiąże się z decyzją o logach tak jak pozycje o życiu zapisu i o awarii; skill powtarza jej odpowiedź. | decision | pytanie 3 | czy zmienić WAY-139, czy tylko `resolve_gaps.md` |
| 4 | Linię wyniku sprawdzeń w krótkim zwrocie podaje każdy etap cyklu, który uruchamia test albo inne sprawdzenie, nie tylko etap, który sprawdza produkt. | decision | pytanie 5 | czy zmienić WAY-148, czy usunąć linię ze skilla planisty |
| 5 | Raportami etapu, które czyta skrypt uwag, są pliki `.md` z `reports/`, których nazwa nie zawiera `handoff` ani `findings`. | decision | punkt 8 *To do*; ai-review 2026-11-07, po krytyce, sprawdzone na sześciu kopiach zapisów cykli; Mariusz, 2026-11-08: „tak jak rekomendujesz” — na rekomendację agenta, by przyjąć wiersz, bo *Rejected* decyzji zachowa odrzucone drogi; nie wybrane: kod wyjścia 2 przy zerze raportów — nie łapie przypadku, gdy skrypt czyta część raportów, i przeczy `task-cycle/skill/SKILL.md:486` („Exit 2 is no listing: fix the call, or the file that could not be read”, `a3206c1`); linia `not read:` w wyniku skryptu — wygląda jak pozycja do dopisania | czy dopisać regułę nazw do WAY-294, czy zostawić ją w skillu i docstringu skryptu |

## Out of scope

- Uwagi o skillach wytycznych — zadanie 6 tego samego przeglądu (the sibling task note on the guidelines skills).
- Uwagi z dopisków pliku źródłowego (lead-project, wybory technologii tekstem, sprawdzanie przed scaleniem, twarda blokada, słowo „gate”) i z listy „Zostawić” — należą do innych zadań albo zostają.
