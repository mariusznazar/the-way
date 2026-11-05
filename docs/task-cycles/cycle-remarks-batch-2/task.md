---
title: "the way: poprawki z uwag cykli (ai-review S7), partia 2026-11-05"
status: draft
created: 2026-11-05T11:53
updated: 2026-11-05
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]"]
---

# the way: poprawki z uwag cykli (ai-review S7), partia 2026-11-05

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykle zadań prowadzone według the-way zostawiają w PR-ach uwagi o miejscach, w których reguły procesu nie pasowały do sytuacji, a nocny przegląd ai-review zbiera je jako sprawy; Mariusz przyjął cztery z nich do naniesienia w sesji z 2026-11-05: AIR-585, AIR-586, AIR-587 i AIR-592.
- Odbiorcą są agenci i recenzenci kolejnych cykli, którzy przy każdej takiej luce rozstrzygają sami i każdy trochę inaczej, oraz Mariusz, który czyta w PR-ach drobne uwagi o rzeczach, których nie miał jak rozstrzygnąć wcześniej.
- Bez tej zmiany nic nie psuje się od razu: cykle dalej osądzają te miejsca same, a te same wątpliwości wracają w zapisach kolejnych cykli.

### To do

1. (AIR-585) Gdy zadanie albo jego spec wprost wykluczają wpis w fundamencie dla wyboru, to wykluczenie wygrywa z regułą kroku powrotu, a wybór zostaje wierszem tabeli pytań w zapisie cyklu; bez wykluczenia reguła kroku powrotu działa jak dziś. Zmiana idzie w dwa miejsca: `task-cycle/skill/return_step.md:13`, po „(WAY-36).”: „Where the task or its spec explicitly excludes an entry for a choice, that exclusion prevails over the rule for a choice that binds after the merge: the choice stays a row of the questions table.”, oraz `task-cycle/record_template.md:99`, gdzie „(WAY-36);” zastępuje „(WAY-36), unless the task or its spec excludes the entry, as `task-cycle/skill/return_step.md` gives;”. Kandydat wycięty z *Settlements to record* wykluczeniem nie jest.
2. (AIR-586) Decyzja WAY-05 dopuszcza w uzasadnieniu i odrzuconych wariantach wynik pomiaru, na którym opiera się wybór, i podaje powód zakazu; ta sama zmiana wchodzi do zdania wiążącego WAY-05, do szablonu decyzji, do uzasadnienia i do *Verification* WAY-05:
   - zdanie wiążące WAY-05 (`foundations/decisions.md:128-130`), po „names no file, script or count”: „— a count being how many files, tests or entries of its foundation the product holds; a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound —”;
   - `elements/decisions/template.md:53-55`: ten sam fragment w tym samym miejscu;
   - *Rationale* WAY-05, nowe zdanie na końcu: „The prose gives only what a reader needs to understand the choice: the history of the product or of the decision — what the product held, how the choice was reached — is information the reader does not need, while a measurement the choice rests on is a reason for the choice.”;
   - *Verification* WAY-05, nowa para: „complies: a rationale gives '12 loops fit in a save with the longest program, 16 and 19 with shorter ones'; violates: a rationale gives 'at most 12 loops' with no conditions, or how many entries the log held when the decision was taken.”
3. (AIR-592) Raport etapu bez sekcji **Searches not found or unclear** (WAY-260), a raport `make-change` także bez opisu sprawdzenia własnej pracy (WAY-164), wraca do agenta do poprawki przed dalszą pracą — tak samo jak dziś raport ze sprawdzeniem bez polecenia albo kodu wyjścia; `none` jest odpowiedzią, brak sekcji nie jest. Dotyczy to obu miejsc `task-cycle/skill/SKILL.md`, które dziś mówią o poprawce tylko dla sprawdzenia bez polecenia albo kodu wyjścia: reguły ogólnej (`:187-189`) i reguły sprawdzenia mechanicznego raportu wykonawcy kawałka (`:283-289`), gdzie każda inna niezgodność „goes as information … and does not return it”. Raport pośredni `questions` nie wraca za brak **Searches not found or unclear**, a raport `make-change` bez kodu (`returned`, `reserved`) nie wraca za brak opisu sprawdzenia własnej pracy. Sprawdzenie mechaniczne raportu wykonawcy sprawdza obie sekcje. Brzmienie: po „(WAY-159).” w `:189` nowe zdanie „A report that lacks its **Searches not found or unclear** (WAY-260), save one returning `questions`, or a `make-change` report of `done` or `done with concerns` without its own-work check (WAY-164), returns to its agent for repair the same way (WAY-148); `none` is an answer, a missing section is not.”, a fragment w `:286-289` po zmianie: „…and, for slice 1, the plan's *Foundation entries*, and each check of the report with its command and exit code, its **Searches not found or unclear** and its own-work check. Uncommitted work returns to the executor to commit, and a check without its command or exit code, or a report missing either section, returns the report for repair (WAY-148, WAY-159, WAY-164, WAY-260); any other mismatch goes as information to the review that judges the slice and does not return it.”
4. (AIR-587) Recenzent oddaje prowadzącemu cykl pierwszą linię raportu, liczby uwag (blokujących, drobnych i poza zakresem), jednolinijkowy wynik sprawdzeń z tym, co padło albo się nie uruchomiło, i ścieżkę raportu — tak, jak WAY-148 każe każdemu agentowi cyklu; zmiana dotyczy `task-cycle/review/SKILL.md:140-141`, które dostaje brzmienie: „Return to the orchestrator only the first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result naming what failed or did not run, and the report path (WAY-148).” Ta sama zmiana obejmuje etap specu, który nie uruchamia testu ani innego sprawdzenia produktu:
   - zdanie wiążące WAY-148 (`foundations/decisions.md:3888-3890`), po „a one-line check result naming what failed or did not run”: „, where the stage runs a test or another check of the product,”;
   - `task-cycle/spec/SKILL.md:51` dostaje brzmienie „The designer returns its status, the spec path and its report path, and the reviewer its report's first line and its report path (WAY-148); neither runs a test or another check of the product, so neither returns a check result.”;
   - `task-cycle/skill/SKILL.md:178`, po „…naming what failed or did not run”: wtrącenie „(an agent of `write-spec` runs no test or other check of the product and returns no check result)”;
   - `task-cycle/spec/review.md:26`: „…to its own path and returns its first line and that path.”

### Questions to settle

- Pytanie 1 (AIR-585): czy wybór zapisany w tekście skilla albo szablonu, który zmiana pisze, dostaje wpis w fundamencie, i co wygrywa w kroku powrotu, gdy zadanie albo spec mówią „bez wpisu”?
  - Answer: wykluczenie wpisu w zadaniu albo specu wygrywa z regułą kroku powrotu, a wybór zostaje wierszem tabeli pytań; bez wykluczenia reguła zostaje jak dziś (droga B).
  - Not chosen:
    - Wyjątek dla każdego wyboru zapisanego w tekście skilla albo szablonu, bez wpisu, chyba że zadanie lub spec o niego proszą (droga A, szkic z zeszytu) — powody i odrzucone warianty giną ze specem, późniejsza zmiana przerobi regułę bez sprzeczności z żadnym wpisem, a wyjątek idzie wbrew WAY-22 i WAY-18 (koszt podany w pytaniu).
    - Bez zmiany (droga C) — dalej drobne uwagi w PR-ach i rozważania na dwóch etapach cyklu, bez szkody dla produktu (koszt podany w pytaniu).
  - Source: Mariusz, 2026-11-05: „B” — na drogi A/B/C przedstawione w rozmowie doprecyzowania; stan the-way `61c72fb`: `task-cycle/skill/return_step.md:12-13`, `task-cycle/record_template.md:98-99`, `foundations/decisions.md:571` (WAY-22), `:498` (WAY-18).
  - Pytanie kontrolne: czy B trzyma się wobec ceny zapisanej w pierwotnej notatce zadania — „powody odrzucenia innych wariantów takiego wyboru giną razem ze specem, a późniejsza zmiana może przerobić regułę bez sprzeczności z żadnym wpisem — zmianę tekstu skilla i tak widzę przy scaleniu” — skoro spec, który wyklucza wpis, pisze agent, a Mariusz widzi taki wybór dopiero przy scaleniu, w „For you to decide” opisu PR-a (`task-cycle/skill/request_template.md:162-172`)? Trzyma się. Mariusz, 2026-11-05: „ok”.
  - Krytyka przed przyjęciem dokumentu pokazała, że B też idzie wbrew WAY-22 („A rule that records a choice is a decision”) i WAY-18 („A product keeps all its decisions in one log”), tylko w węższym obszarze, a kolizja bez zapisanego pierwszeństwa zatrzymuje pracę (`elements/decisions/template.md:163-167`, WAY-25). Odpowiedź: B zostaje, a decyzja z wiersza 1 zawęża WAY-22 i WAY-18 (`narrows`) w obszarze wyborów, które zadanie albo spec wprost wykluczają (droga a). Not chosen: wykluczać może tylko zadanie, nie spec (droga b) — w przypadku takim jak PR #70 cykl pisze decyzję dla każdego takiego wyboru i dziennik rośnie; wycofanie punktu 1 (droga c) — dalej drobne uwagi w PR-ach, bez szkody. Mariusz, 2026-11-05: „ok a”.
- Pytanie 2 (AIR-586): po co WAY-05 zabrania w uzasadnieniu podawania liczb (`names no file, script or count`)?
  - Answer: zakaz chroni przed zapisywaniem historii i kronik w decyzjach, czyli przed informacjami, których czytelnik decyzji nie potrzebuje — nie przed tym, że treść się starzeje.
  - Source: Mariusz, 2026-11-05: „wpis miał chronić przed zapisywaniem historii i kronik w decyzjach” — na pytanie o ocenę, bez wariantów; i przy pytaniu kontrolnym do pytania 3: „w nie zapisywaniu historii nie chodzi o starzenie się, tylko o niepotrzebne informacje”. Uzasadnienie WAY-05 (`foundations/decisions.md:143-145` @ `61c72fb`) tego powodu nie podaje.
- Pytanie 3 (AIR-586): czy zmieniać zdanie wiążące WAY-05 i szablon decyzji, żeby wynik pomiaru, na którym opiera się wybór, mógł stać w uzasadnieniu — a jeśli tak, w jakim brzmieniu?
  - Answer: wyjątek dla pomiaru w zdaniu wiążącym WAY-05 i w szablonie, powód zakazu dopisany do uzasadnienia WAY-05 i para przykładów w *Verification*, w brzmieniu z To do 2 (droga A+).
  - Not chosen:
    - Sam wyjątek, bez powodu w uzasadnieniu (droga A, szkic z zeszytu) — zasięg zakazu dalej trzeba zgadywać przy każdym przypadku, którego wyjątek nie nazywa (koszt podany w pytaniu).
    - Sam powód w uzasadnieniu, bez zmiany zdania wiążącego (droga B) — WAY-05 nie pozwala, by to, co wiąże późniejszą pracę, stało w samej prozie, więc zdanie wiążące dalej zakazywałoby pomiaru, a uzasadnienie by mu przeczyło (koszt podany w pytaniu).
    - Bez zmiany — jedne pomiary zostają we wpisach, inne wypadają, a recenzenci zgłaszają drobne uwagi; szkody dla produktu dotąd nie było (koszt podany w pytaniu).
    - Rozciągnięcie zakazu na pomiary (wariant z zeszytu) — wpisy przestałyby się starzeć, ale zniknąłby jedyny ślad tego, dlaczego wybrano dany wariant, bo spec nie przetrwa scalenia (koszt podany w zeszycie, AIR-586).
  - Source: Mariusz, 2026-11-05: „przyjmuję A+ z propozycjami” — na drogi A+/A/B/bez zmiany i tekst propozycji przedstawione w rozmowie doprecyzowania; zgoda na zmianę WAY-05 w tym dokumencie (WAY-30).
  - Pytanie kontrolne: czy wyjątek dla pomiaru trzyma się wobec celu „nie zapisywać historii i kronik w decyzjach”, skoro pomiar starzeje się z każdą zmianą produktu, jak w loop2 PR #47 („było „około 10”, mieści się 12”, AIR-586)? Trzyma się: zakaz odcina informacje niepotrzebne czytelnikowi, a pomiar, na którym opiera się wybór, jest mu potrzebny; zdanie do *Rationale* przepisane z powodu „starzenia się” na powód „niepotrzebnych informacji”. Mariusz, 2026-11-05: „w nie zapisywaniu historii nie chodzi o starzenie się, tylko o niepotrzebne informacje”; nowe brzmienie zdania do *Rationale*: „tak”.
  - Po krytyce przed przyjęciem dokumentu: przykład zgodny „12 loops fit a 64 KB save” nie mówił, przy jakim programie zmierzono — wada, którą zgłosił recenzent w loop2 PR #47 („„at most” trzyma się tylko dla jednego programu; przy krótszych wychodzi 16 i 19”, `ai_review_ledger.md:140`) — a „64 KB” nie ma źródła; „at what size” zastąpione przez „under which conditions”, „entries the product holds” przez „entries of its foundation the product holds”, a przykład wzięty z liczb zeszytu. Mariusz, 2026-11-05: „przyjmuję”.
- Pytanie 4 (AIR-587): czy poprawka zwrotu recenzenta obejmuje też projektanta i recenzenta specu, których zwrot `task-cycle/spec/SKILL.md:51` opisuje jako „their paths, and nothing more”?
  - Answer: tak — etap specu dołączony do punktu 4, w brzmieniu z To do 4 (droga A).
  - Not chosen:
    - Osobne zadanie na etap specu (droga B) — niejasność wraca w kolejnych cyklach, dopóki tamto zadanie nie przejdzie własnego cyklu, a to więcej pracy niż dwa zdania tutaj (koszt podany w pytaniu).
    - Etap specu bez zmiany (droga C) — recenzent specu dalej sam decyduje, co oddać; szkody nie ma, bo pełny raport leży w pliku (koszt podany w pytaniu).
  - Source: Mariusz, 2026-11-05: „A” — na drogi A/B/C i tekst propozycji przedstawione w rozmowie doprecyzowania; stan the-way `61c72fb`: `task-cycle/spec/SKILL.md:51`, `task-cycle/skill/SKILL.md:177-178`, `task-cycle/spec/review.md:26`, `task-cycle/spec/design.md:60-65` i `:73`; przypadek recenzenta specu w loop2 PR #47 (AIR-587).
  - Pytanie kontrolne: czy zdanie „neither runs a check” trzyma się wobec `task-cycle/spec/design.md:60` i `:70` — „Before you return, read the spec again for four things and fix what you find” … „the result of the four checks”? Nie w tym brzmieniu: projektant ma „checks”, tylko nie polecenia, więc zdanie i wtrącenie zawężone do poleceń („runs a command”, „runs no command”). Mariusz, 2026-11-05: „ok” — na zawężenie zaproponowane w rozmowie.
  - Po krytyce przed przyjęciem dokumentu: „runs a command” też jest nieprawdą — projektant czyta kod (`task-cycle/spec/SKILL.md:26`), a WAY-148 (`foundations/decisions.md:3888-3890`) daje wynik sprawdzeń każdemu etapowi; zamiast wyjątku w skillu WAY-148 zmienia się w miejscu („where the stage runs a test or another check of the product”), zdanie zawężone do testu albo innego sprawdzenia produktu, a projektant oddaje też ścieżkę specu, recenzent w `spec/review.md:26` także ścieżkę raportu. Mariusz, 2026-11-05: „przyjmuję” — także zgoda na zmianę WAY-148 w tym dokumencie (WAY-30).

## Context

- Każda z tych spraw to jedno albo dwa zdania w skillu, szablonie albo decyzji the-way, a osobny cykl i osobny PR na każdą kosztuje więcej niż sama zmiana, więc idą jednym zadaniem, tak jak sprawy AIR-476–481 (zamknięte zadanie `poprawki_z_uwag_cykli_s7.md`, PR #29 w the-way).
- Źródło: wpisy AIR-585, AIR-586, AIR-587 i AIR-592 w `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md`; każdy ma tam cytaty z zapisów cykli, diagnozę i rachunek.
- Numery wierszy w zeszycie są ze stanu `f45ca40`; w tym dokumencie sprawdzono je na czubku `origin/foundations` @ `61c72fb` (2026-11-05), po scaleniu PR #71 (`pr-description-schema`).
- Po PR #71 przesunęły się wiersze w `foundations/decisions.md` (WAY-60 stoi teraz w `:1371-1378`, WAY-148 w `:3886-3904`); `task-cycle/skill/return_step.md:13`, `task-cycle/record_template.md:99`, `task-cycle/review/SKILL.md:140-141`, `task-cycle/skill/SKILL.md:287-289`, `foundations/decisions.md:126-133` i `elements/decisions/template.md:53-56` stoją pod tymi samymi numerami, a reguła o poprawce raportu stoi w `task-cycle/skill/SKILL.md:187-189` (nie `:186-188`).
- Zadanie `zadanie_the_way_staly_schemat_pr`, które zmieniało te same pliki (`task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`), jest zrobione (PR #71), więc kolejność dwóch cykli nie jest już ograniczeniem.
- Związek treściowy z tamtym zadaniem trzyma się: nowy `task-cycle/skill/request_template.md:155-159` wylicza „a missing own-work check (WAY-164)” wśród niewykonanych sprawdzeń, a bierze je z raportów etapów — raport bez opisu sprawdzenia własnej pracy zostawia tę sekcję bez informacji.
- Punkt 1: wykluczenie wpisu w specu pisze agent, ale wybór, który spec tak zostawia, i tak trafia do opisu PR-a w „For you to decide”, gdy zmienia „what the human meets when working with the process” — `task-cycle/skill/request_template.md:162-172` każe go szukać w „the spec's *Decisions*”; Mariusz widzi więc przy scaleniu sam wybór, ale żadna sekcja opisu PR-a nie mówi, że wybór nie dostał wpisu.
- Punkt 2: żaden wpis w `foundations/` nie niesie odcisku WAY-05 (`WAY-05@…`), a brzmienie „names no file, script or count” stoi tylko w `foundations/decisions.md:129` i `elements/decisions/template.md:54` — grep po całym repozytorium nie trafia w żaden skrypt ani test, więc zakaz pilnuje recenzja, nie narzędzie.
- Punkt 2: pięć wpisów powołuje się na WAY-05 w uzasadnieniu (`decisions.md:524`, `:1285`, `:1619`, `:1637`, `:1905`) i żaden nie opiera się na zakazie liczb; WAY-72 (`:1637`) mówi ogólnie o „words the rules of form keep out (WAY-05, WAY-60)” i zakazu liczb nie cytuje.
- Punkt 4: zeszyt podaje, że prowadzący wpisuje liczby uwag do zapisu cyklu (`cycle.md:51` w kopii the-way@1754f38); `task-cycle/skill/SKILL.md:324` do decyzji o przejściu dalej używa pierwszej linii recenzji.
- Części dotknięte zmianą (według `foundations/part_map.md`): `decisions` (punkt 2: `foundations/decisions.md`, `elements/decisions/template.md`; punkt 4: `foundations/decisions.md`) i `task-cycle` (punkty 1, 3, 4).
- Wytyczne produktu: zmiana dotyka wyłącznie instrukcji w Markdownie — ani interfejsu, ani kodu, ani testów w rozumieniu `product-guidelines/reading.md`; the-way nie ma katalogu `guidelines/`, więc wybór wytycznych jest pusty i nie ma braku do zgłoszenia.
- Opis żadnego skilla się nie zmienia, więc punktów wejścia (`agent-instructions/skill_entry_points.py`) nie trzeba generować na nowo.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-36 (`foundations/decisions.md:916`): „A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition between two states — stays in the plan of that work, or in the choices of its cycle record where no plan is written.” — punkt 1.
- WAY-22 (`foundations/decisions.md:571`): „A rule that records a choice is a decision, and what of it a commit can make false is written as an invariant derived from it; a rule with no choice behind it is an invariant alone.” — punkt 1.
- WAY-18 (`foundations/decisions.md:498`): „A product keeps all its decisions in one log, whatever they are about.” — punkt 1; wiersz 1 *Settlements to record* zawęża WAY-22 i WAY-18 (WAY-25: „the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails”).
- WAY-35 (`foundations/decisions.md:891`): „An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them…” — punkt 1.
- WAY-05 (`foundations/decisions.md:124`): „A decision entry opens with one to three binding sentences — in the present tense, describing a state that is to be true, concrete enough to check — followed by fields a script or an agent reads, then rationale and rejected options in prose, which, where the entry's author writes it rather than quotes a source, names no file, script or count, nor what the process's own tools do or lack today, and does not tell how the decision was reached.” — punkt 2.
- WAY-30 (`foundations/decisions.md:762`): „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made…” — punkty 2 i 4: zmiany WAY-05 i WAY-148 wymagają tej zgody.
- WAY-60 (`foundations/decisions.md:1371`): „A sentence bounding or equating a quantity measured while the product runs names its bound or tolerance, statistic and population.” — punkt 2, kierunek zgodny z propozycją.
- WAY-148 (`foundations/decisions.md:3886`): „…its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, and the report's path…” oraz „…a missing or incomplete report is repaired before dependent work proceeds…” — punkty 3 i 4; punkt 4 zmienia zdanie wiążące WAY-148 (To do 4, wiersz 3), za zgodą w tym dokumencie (WAY-30); żaden wpis nie niesie jej odcisku.
- WAY-159 (`foundations/decisions.md:4232`): „A report missing the command or the exit code of a check it ran is incomplete, and a claim that tests passed does not repair it…” — punkt 3.
- WAY-164 (`foundations/decisions.md:4441`): „…states in its report which requirement, which check and what the check showed.” — punkt 3.
- WAY-260 (`foundations/decisions.md:7535`): „Every task-cycle stage's report states each thing the agent looked for and did not find, or found unclear, wherever it arose, or `none`…” — punkt 3.

## Settlements to record

Candidates: 5 shown, 3 accepted — 2026-11-05

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy zadanie albo jego spec wprost wykluczają wpis w fundamencie dla wyboru, to wykluczenie wygrywa z regułą kroku powrotu, a wybór zostaje wierszem tabeli pytań w zapisie cyklu; ta decyzja zawęża WAY-22 i WAY-18 (`narrows`) w obszarze wyborów, które zadanie albo spec wprost wykluczają. | decision | odpowiedź na pytanie 1 z pytaniem kontrolnym i odpowiedzią po krytyce; To do 1 | czy cykl zapisuje to pierwszeństwo jako decyzję, która zawęża WAY-22 i WAY-18, czy zostawia je wyłącznie w tekście `return_step.md` i `record_template.md` i zatrzymuje się na kolizji bez zapisanego pierwszeństwa (WAY-25) |
| 2 | Uzasadnienie decyzji może podać pomiar, na którym opiera się wybór, z tym, co zmierzono i w jakich warunkach, nigdy jako ogólną granicę; zakaz liczb chroni przed zapisywaniem w decyzjach historii i kronik, czyli informacji, których czytelnik nie potrzebuje — zmiana WAY-05 w brzmieniu z To do 2. | decision | odpowiedzi na pytania 2 i 3 z pytaniem kontrolnym; To do 2 | czy krok fundamentu zatrzymuje cykl pytaniem o zmianę sensu WAY-05 i skąd bierze powód zakazu do *Rationale* — z odpowiedzi Mariusza czy z własnego domysłu o starzeniu się |
| 3 | Etap, który nie uruchamia testu ani innego sprawdzenia produktu — projektant i recenzent specu — nie oddaje prowadzącemu wyniku sprawdzeń; to zmiana WAY-148 w miejscu, w brzmieniu z To do 4. | decision | odpowiedź na pytanie 4 z pytaniem kontrolnym i odpowiedzią po krytyce; To do 4 | czy cykl zmienia WAY-148, czy zostawia skill specu w sprzeczności z jej zdaniem wiążącym, które wymienia wynik sprawdzeń przy każdym etapie |

## Out of scope

- Usunięcie liczb uwag z wiadomości recenzenta do prowadzącego — byłoby osobną zmianą (punkt 4).
