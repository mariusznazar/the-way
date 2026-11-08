---
title: "the way: przy doprecyzowaniu decyzje fundamentu opisują stan obecny, wiążą dopiero przy implementacji"
status: draft
created: 2026-11-08T14:45
updated: 2026-11-08
tags: [zadanie]
related: "the author's note of the process project"
---

## Po co to

- **Jak jest dziś:** w the way decyzja zapisana w fundamencie produktu trzyma wybór także w trakcie doprecyzowania zadania albo projektu. Zmiana jednej decyzji przechodzi tam przez cztery osobne zgody człowieka, każdą z innej reguły: (1) krok wyboru technologii przy zadaniu otwiera decyzję dopiero „na słowo człowieka”; (2) po wyborze pada „pytanie przeciw odpowiedzi”, gdy człowiek odpowiedział własnymi słowami; (3) każdy wiersz ustaleń do zapisania w fundamencie, także ten, który niesie tę samą zmianę, człowiek przyjmuje osobno; (4) na końcu akceptuje cały dokument. W sesji 2026-11-08 nad zadaniem loop2 „skąd wiem o awarii” zmianę jednej decyzji gry (D-347) Mariusz potwierdzał trzy razy, do tego doszło pytanie przeciw odpowiedzi o Lokiego.
- **Kto to odczuwa:** Mariusz przy każdym doprecyzowaniu, które dotyka istniejącej decyzji. Jego słowa: „reguły i decyzje nie są po to, żeby ograniczać tylko opisywać stan obecny” i „gdzieś jest spierdolone coś mocno jeśli decyzje wiążą tak mocno że ich zmiana wymaga 50 potwierdzeń”.
- **Co jeśli nic:** każde doprecyzowanie zmieniające decyzję powtarza tę samą drogę. Rozmowa się wydłuża, a potwierdzenia przestają być czytane, czyli tracą to, czemu miały służyć.

# the way: przy doprecyzowaniu decyzje fundamentu są materiałem, wiążą dopiero w cyklu zadania

Status: ready for cycle
Project relation: independent

## Description

### Need

- Problem, który zadanie naprawia, słowami Mariusza (2026-11-08): „opór agenta przy proponowaniu opcji, które są lepsze, ale zmieniają dotychczas podjęte decyzje podczas rozważania zmian w ramach refinementu zadania”.
- Przy doprecyzowaniu — w definicji projektu, w doprecyzowaniu zadania i w kroku wyboru technologii — decyzja fundamentu produktu działa dziś jak zamek: agent nie może zaproponować jej zmiany jako jednej z opcji, a gdy zmiana jednak pada, przechodzi przez kilka osobnych zgód człowieka, każdą z innej reguły (miejsca w *Context*).
- Według relacji Mariusza z sesji 2026-11-08 nad zadaniem loop2 „skąd wiem o awarii” zmianę jednej decyzji gry (D-347) potwierdzał trzy razy, a do tego doszło pytanie przeciw odpowiedzi o Lokiego, zadane po luźnej uwadze („zastanawia mnie Loki”).
- Zasada Mariusza (2026-11-08): „decyzje wiążą, ale przy implementacji, a nie przy refinowaniu projektów czy zadań gdzie z założenia wszystko się może zmienić”; oraz „reguły i decyzje nie są po to, żeby ograniczać tylko opisywać stan obecny”.
- Odbiorcą jest człowiek, który doprecyzowuje zadanie albo projekt produktu używającego the way (dziś Mariusz w loop2 i w samym the way), oraz agent doprecyzowania, który dziś nie może pokazać zmiany decyzji jako zwykłej opcji.
- Bez zmiany każde doprecyzowanie, które zmienia decyzję, powtarza tę drogę: rozmowa się wydłuża, a potwierdzenia przestają być czytane.

### To do

1. Krok wyboru technologii, przy zadaniu i przy definicji projektu: agent może sam pokazać jako otwarty wybór, który trzyma decyzja fundamentu, gdy widzi powód, by ją zmienić; obecna odpowiedź decyzji stoi w porównaniu jako jedna z opcji, opcja zmieniająca decyzję mówi to w swoim wierszu, a wybór człowieka jest jedyną zgodą na zmianę — bez osobnego „słowa człowieka” przed porównaniem i bez powrotu do zmiany przy akceptacji dokumentu (pytanie 1) (`project-level/technology/task_run.md`, sekcja „List”; `running_product.md`, „The agent opens no decision of the foundation on its own”; `list.md`, punkt „find what settles it”).
2. Doprecyzowanie zadania i definicja projektu: agent pokazuje opcję, która zmienia decyzję fundamentu, tak samo jak każdą inną — z nazwaną decyzją, którą zmienia, i z rekomendacją, także gdy poleca ją zamiast obecnej decyzji; wybór człowieka jest zgodą na zmianę. Dokument zadania niesie wtedy zmianę tej decyzji, jak WAY-30 już pozwala, a cykl zapisuje ją razem z kodem; w definicji zmiana staje się rzutowaną zmianą decyzji. Zamiast tego dziś: „route that change to its own process” (`project-level/task/skill/resolve_gaps.md`, akapit „If two answers conflict”) i konflikt, przy którym człowiek wybiera „change the task or reopen the upstream settlement” (`project-level/task/skill/carry_foundation.md`, ostatni akapit). Decyzja rzutowana zatwierdzonej definicji zostaje poza tym punktem (pytanie 5).
3. Przy doprecyzowaniu pytanie przeciw odpowiedzi pada tylko wtedy, gdy odpowiedź przeczy zacytowanemu zdaniu, które człowiek sam wcześniej wypowiedział; w cyklu zadania i przy zapisie wpisów fundamentu zostaje jak dziś (pytanie 2; `elements/common/way_of_working.md`, „How a skill asks”; `elements/common/skill/task_variant.md`, „Step 4”; `project-level/technology/settle.md`, podkrok 6 „Choose”; w definicji projektu ruch „collision — […] the material against the conversation” z `elements/common/skill/definition_variant.md`, „Step 4”, zostaje tylko dla dwóch zdań człowieka; pytania o to, czego wpis potrzebuje, a źródło nie daje, zostają).
4. Wiersz *Settlements to record*, który powtarza wybór dokonany przez człowieka między pokazanymi opcjami — także wynik kroku wyboru technologii — wchodzi do tabeli już przyjęty, oznaczony, z możliwością skreślenia; człowiek tnie tylko wiersze wyprowadzone przez agenta (pytanie 3; `elements/common/skill/SKILL.md`, krok 3 „The human cuts”; `elements/common/skill/task_variant.md`, „Step 2” i „Step 4”; `project-level/task/skill/find_settlements.md`, akapit o „settled technology question”).
5. Decyzje the way mówią to samo co punkty 1–4 i 6: WAY-165 i WAY-267 bez zastrzeżenia „opens only on the human's word” (z uzasadnieniem i *Verification*), WAY-113 według pytania 2, a WAY-115, WAY-124 i WAY-134 według pytania 3 — wiersz powtarzający wybór człowieka liczy się jako przyjęty, dopóki człowiek go nie skreśli.
6. W cyklu zadania wiązanie zostaje: agent cyklu nie odchodzi od decyzji sam, tylko wraca z pytaniem, jak mówi WAY-30. Granicą jest start cyklu zadania (`implement-task`), z pisaniem specu w cyklu włącznie; decyzje the way i pliki z punktów 1–4 mówią, że ich luźniejsze reguły obowiązują tylko przed tą granicą (pytanie 4).

### Acceptance criteria

- Agent doprecyzowania, który widzi wariant lepszy od obecnej decyzji fundamentu, pokazuje go w porównaniu i może go polecić, bez wcześniejszego pytania o pozwolenie na otwarcie decyzji; żaden plik skilla ani decyzja the way nie każe mu traktować decyzji jako granicy opcji przed startem cyklu.
- W doprecyzowaniu, które zmienia jedną decyzję fundamentu, człowiek wyraża zgodę na tę zmianę raz; żaden krok nie pyta go o nią ponownie przed akceptacją całego dokumentu.

### Questions to settle

- Pytanie 1: która zgoda człowieka jest zgodą na zmianę decyzji przy doprecyzowaniu — wybór opcji w tabeli porównania czy akceptacja całego dokumentu (WAY-124)?
  - Answer: wybór opcji w tabeli porównania. Opcja, która zmienia decyzję, mówi to w swoim wierszu (np. „zmienia D-347: …”); akceptacja całego dokumentu zostaje, jak dla każdego zadania (WAY-124), ale nie pyta o tę zmianę drugi raz. Słaby punkt przyjęty z tą drogą: zmiana przeoczona przy wyborze stoi potem w *Decisions in play*, ale nikt nie pyta o nią osobno.
  - Not chosen:
    - zgodą jest akceptacja dokumentu, wybór w tabeli wstępny, a zmiana decyzji osobnym punktem przy akceptacji — druga zgoda na to samo; skutki widać przy wyborze, a zgodę daje się później
  - Source: Mariusz, 2026-11-08, „a” (droga (a) w rozmowie doprecyzowania)
- Pytanie 2: co z pytaniem przeciw odpowiedzi (WAY-113) przy doprecyzowaniu — znika przy zmianie decyzji, czy zostaje tylko wtedy, gdy odpowiedź przeczy zdaniu, które człowiek sam wcześniej wypowiedział?
  - Answer: przy doprecyzowaniu (definicja projektu, doprecyzowanie zadania, krok wyboru technologii) pytanie przeciw odpowiedzi pada tylko wtedy, gdy odpowiedź przeczy zdaniu, które człowiek sam wcześniej wypowiedział, z tym zdaniem zacytowanym; nie pada przy zmianie decyzji ani po luźnej uwadze. W cyklu zadania i przy zapisie wpisów fundamentu reguła WAY-113 zostaje jak dziś. Słaby punkt przyjęty z tą drogą: odpowiedź sprzeczna z materiałem (np. PRD, notatką) przechodzi bez pytania.
  - Not chosen:
    - pytanie znika przy doprecyzowaniu całkiem — sprzeczność z własnym wcześniejszym zdaniem człowieka też przechodzi niezauważona
    - pytanie znika tylko przy zmianie decyzji, poza tym jak dziś — luźna uwaga („zastanawia mnie Loki”) dalej dostaje pytanie
  - Source: Mariusz, 2026-11-08, „a” (droga (a) w rozmowie doprecyzowania)
- Pytanie 3: wiersze ustaleń, które powtarzają wybór już dokonany przez człowieka — wchodzą same, z możliwością skreślenia, czy człowiek przyjmuje je osobno jak dziś?
  - Answer: wiersz, który powtarza wybór dokonany przez człowieka między pokazanymi opcjami, wchodzi do tabeli już przyjęty, oznaczony, z możliwością skreślenia; człowiek przyjmuje albo odrzuca tylko wiersze, które agent wyprowadził sam — z materiału albo z luźnych słów człowieka. Słaby punkt przyjęty z tą drogą: wiersz jest streszczeniem agenta, którego człowiek nie czytał przy wyborze; złe streszczenie łapie tylko lektura tabeli przy akceptacji dokumentu.
  - Not chosen:
    - jak dziś, każdy wiersz przyjmowany osobno — druga zgoda na to samo
    - takie wiersze nie trafiają do tabeli, cykl pisze decyzję wprost z odpowiedzi pod pytaniem — znika odsiew wyborów, które nie wiążą po scaleniu (kolumna „co cykl by zgadł”), cykl sam ocenia, który wybór wpisać, a WAY-134 wymaga mocniejszej przebudowy
  - Source: Mariusz, 2026-11-08, „a” (droga (a) w rozmowie doprecyzowania)
- Pytanie 4: gdzie zaczyna się „implementacja”, od której decyzja wiąże — od startu cyklu zadania (`implement-task`), z pisaniem specu w cyklu włącznie?
  - Answer: decyzja wiąże od startu cyklu zadania (`implement-task`), z pisaniem specu w cyklu włącznie; w cyklu nic się nie zmienia — agent nie odchodzi od decyzji sam, a sprzeczność wraca do człowieka, jak mówi WAY-30. Słaby punkt przyjęty z tą drogą: autor specu, który widzi lepszy wariant niż decyzja, nie idzie nim sam — kosztuje to jeden obieg przez człowieka.
  - Not chosen:
    - wiązanie dopiero od pisania kodu, spec w cyklu traktuje decyzję jako materiał, zgoda przy PR-ze — zmiana decyzji dociera do człowieka w PR-ze z kodem już na niej stojącym, a cykl przestaje iść bez człowieka od startu do PR-a
  - Source: Mariusz, 2026-11-08, „a” (droga (a) w rozmowie doprecyzowania)
- Pytanie 5: czy zasada obejmuje też decyzję rzutowaną zatwierdzonej definicji projektu, której dziś „no run reopens” (WAY-267), a zmiana wymaga ponownej bramki gotowości (WAY-118)?
  - Answer: nie obejmuje; zmiana decyzji rzutowanej zatwierdzonej definicji idzie przez definicję i ponowną bramkę gotowości, jak dziś (WAY-118, WAY-267). Słaby punkt przyjęty z tą drogą: zmiana takiej decyzji przy zadaniu przerywa zadanie i kosztuje powrót do definicji — jedną zgodę przy bramce.
  - Not chosen:
    - zadanie zmienia decyzję rzutowaną jednym wyborem, jak decyzję fundamentu — definicja i plan dalej mówią starą wersję, inne zadania planu rozjeżdżają się bez sygnału, a nanoszenie zmiany na definicję i plan to większe zadanie
  - Source: Mariusz, 2026-11-08, „ale w tym przypadku a będzie ok” (droga (a) w rozmowie doprecyzowania)

## Context

- Źródło zadania: sesja loop2 2026-11-08, lokalny zapis `the local transcript of the session that started the task` (wygasa ok. 2026-12-08).
- Ta sama zasada stoi w globalnych instrukcjach Mariusza, sekcja „Decyzja zapisana w dokumencie jest materiałem, nie ścianą” (`the author's private global instruction file`).
- Miejsca, które niosą wiązanie przy doprecyzowaniu, sprawdzone na `foundations` `a3206c1`:
  - `project-level/technology/task_run.md:50-56` — „A choice a decision of the foundation holds opens only on the human's word […] An agent never opens one. […] A note that refinement derived from a reserved choice is not that word”;
  - `project-level/technology/running_product.md:38-40` — „The agent opens no decision of the foundation on its own here”;
  - `project-level/technology/list.md:19-25` — wybór, który trzyma decyzja, stoi `— held by` i nie wchodzi do porównania;
  - `project-level/task/skill/resolve_gaps.md:10-14` — „If the answer changes the approved project definition or a current foundation decision, route that change to its own process”; wyjątek tylko dla wyboru otwartego krokiem technologii;
  - `project-level/task/skill/carry_foundation.md:13-17` — „The human chooses whether to change the task or reopen the upstream settlement”;
  - `elements/common/way_of_working.md:29-35` — pytanie przeciw odpowiedzi, także dla odpowiedzi własnymi słowami;
  - `elements/common/skill/SKILL.md:47-50` (krok 3, „The human cuts”) i `elements/common/skill/task_variant.md:36-44` — człowiek przyjmuje każdy wiersz, a wiersz z wyborem dostaje jeszcze pytanie przeciw odpowiedzi;
  - `project-level/task/skill/find_settlements.md:24-30` — wiersz z wyniku kroku technologii jest „always shown as a candidate”.
- WAY-30 już dziś pozwala, by dokument zadania niósł zmianę decyzji przyjmowaną razem z nim; sprzeczna z tym jest reguła `resolve_gaps.md:10-11`, która każe kierować taką zmianę osobną drogą.
- Żaden test the way nie sprawdza brzmienia tych miejsc (przeszukanie plików `test_*.py` pod kątem „human's word”, „opens no decision”, „question against”, `a3206c1`); zmiana dotyczy tylko plików Markdown, więc brak własnych wytycznych kodowania i testów the way jej nie dotyczy.
- Zadanie zbiorcze the note of the sibling task in the author's backlog (`ready for cycle`), punkt 17, przeredagowuje to samo zastrzeżenie WAY-165 („holds the choice like any decision, which opens only on the human's word”); cykl, który pójdzie drugi, zastanie brzmienie po pierwszym.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Cytaty z `foundations\decisions.md`, `foundations` `a3206c1`; numer linii to nagłówek decyzji.

- WAY-14 — Who accepts a decision? (`:440`): „A decision, and every change to it, binds once a human accepts it, never an agent. In the-way, that human is Mariusz.” Zostaje: zgoda dalej jest człowieka, zmienia się tylko, ile razy pada.
- WAY-30 — What happens when a change contradicts a decision? (`:806`): „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made; […] When a contradiction shows only during implementation, the agent stops, quotes the decision by its number, and either brings the change into line, drops the change, or proposes on the task branch an edit of the decision, a new wording or a narrowing, and the code that needs it waits for that human.” Podstawa punktów 2 i 6.
- WAY-113 — How does an agent of the-way ask a human decision? (`:2533`): „After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way.” Zmienia się według pytania 2.
- WAY-115 — How are foundation entries found in a project's source? (`:2612`): „The human accepts or rejects rows before they are handed to the skills of their kinds, and each accepted row is recorded as it is worked through.” Zmienia się według pytania 3.
- WAY-118 — What makes a project definition ready for breakdown? (`:2695`): „A change to those sections after approval goes through the gate again before breakdown relies on it.” Dotyczy pytania 5.
- WAY-124 — When is a task ready for its cycle? (`:2939`): „It is ready when the human has seen and accepted its complete document, […] the human has accepted or rejected every candidate settlement its refinement found […].” Dotyczy pytań 1 i 3.
- WAY-134 — How does a task carry what its refinement settles for the foundation? (`:3338`): „Before a task is ready for its cycle, the human sees a table of candidates found in the task document and the conversation that refined it, […] and the task document keeps the rows the human accepts […].” Zmienia się według pytania 3.
- WAY-165 — What must an answer to each matter of an agent's way to the running product settle? (`:4634`): „[…] while in a run at a task (WAY-267) it holds the choice like any decision, which opens only on the human's word.” *Verification*, violates: „an agent opens, in a run at a task, a logs decision silent on the record's life with no word of the human”. Zmienia się w punkcie 5.
- WAY-267 — How does the step that settles technology run outside a project definition? (`:7922`): „[…] and a choice a decision of the foundation holds opens only on the human's word, the result then being a change of that decision.” *Rationale:* „Opening a choice a decision holds takes the human's word because a change of a decision is the human's (WAY-14, WAY-30), and going through the step gives that change research and a critique, at the price that a decision held is no longer final and a hurried run could reach further ones.” *Verification*, violates: „an agent opens a choice a decision holds on its own”. Zmienia się w punkcie 5.

## Settlements to record

Candidates: 6 shown, 5 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Przy doprecyzowaniu projektu albo zadania decyzja fundamentu opisuje stan obecny i jest materiałem do rewizji: agent proponuje opcję lepszą od niej, także ją polecając, bez pytania o pozwolenie; decyzje wiążą przy implementacji. | decision | *Need*, słowa Mariusza 2026-11-08: „decyzje wiążą, ale przy implementacji, a nie przy refinowaniu projektów czy zadań gdzie z założenia wszystko się może zmienić” i „opór agenta przy proponowaniu opcji, które są lepsze, ale zmieniają dotychczas podjęte decyzje”; wiersz przyjęty 2026-11-08: „przyjmuję zgodnie z rekomendacją” | czy wpisać zasadę jako jedną ogólną decyzję dla definicji, zadania i kroku technologii, czy tylko poprawić zastrzeżenia WAY-165 i WAY-267; czy agent może zmianę decyzji polecać, czy tylko dopuścić |
| 2 | Zgodą na zmianę decyzji przy doprecyzowaniu jest wybór opcji, która mówi w swoim wierszu, jaką decyzję zmienia; akceptacja dokumentu nie pyta o tę zmianę drugi raz. | decision | pytanie 1 | czy zmiana decyzji stoi przy akceptacji dokumentu osobnym punktem do zatwierdzenia |
| 3 | Przy doprecyzowaniu pytanie przeciw odpowiedzi pada tylko wtedy, gdy odpowiedź przeczy zacytowanemu zdaniu, które człowiek sam wcześniej wypowiedział; w cyklu i przy zapisie wpisów fundamentu zostaje jak dziś. | decision | pytanie 2 | czy pytanie znika przy doprecyzowaniu całkiem, tylko przy zmianie decyzji, czy zawęża się do sprzeczności z własnymi zdaniami człowieka; czy dotyczy też definicji |
| 4 | Wiersz ustaleń, który powtarza wybór człowieka między pokazanymi opcjami, wchodzi do tabeli przyjęty, z możliwością skreślenia; człowiek tnie tylko wiersze wyprowadzone przez agenta. | decision | pytanie 3 | czy taki wiersz czeka na przyjęcie, wchodzi sam, czy znika z tabeli |
| 5 | Decyzja wiąże od startu cyklu zadania, z pisaniem specu w cyklu włącznie. | decision | pytanie 4 | czy spec w cyklu może traktować decyzję jako materiał |

## Out of scope

none
