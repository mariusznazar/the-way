---
title: Doprecyzowanie zadania kończy się spisem decyzji, które dokument zostawia wykonawcy, sprawdzonym krytyką — człowiek widzi tylko sprawy otwarte
status: draft
created: 2026-11-14
updated: 2026-11-14
tags: [zadanie]
related: the project note of the author's backlog
---

# Doprecyzowanie zadania kończy się spisem decyzji, które dokument zostawia wykonawcy, sprawdzonym krytyką — człowiek widzi tylko sprawy otwarte

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Agent wykonujący zadanie the way często trafia na sprawę, o której dokument zadania milczy albo mówi niejednoznacznie, i rozstrzyga ją sam; według rachunku programu usprawnień z 14 wierszy rejestru problemów, które kosztowały czas Mariusza, 8 to niejasność zadania rozstrzygnięta przez agenta.
- Doprecyzowanie zadania pyta dziś o brakujące i sprzeczne odpowiedzi oraz o słowo, które da się zrozumieć na dwa sposoby (WAY-374), ale nie ma kroku, który sprawdza dokument pod kątem decyzji, jakie wykonawca musiałby podjąć sam.
- Próba z 14.11.2026 na dwóch przyjętych dokumentach zadań the way pokazała, że świeży agent czytający sam dokument i wpisy fundamentu z jego *Decisions in play* wypisuje takie decyzje: 14 na dokument, w tym 9 i 12 zgadnięć.
- Surowa lista zgadnięć była dla Mariusza nieczytelna: przejrzał ją w 5 minut i nie umiał jej ocenić; dopiero krytyka agenta z dostępem do repozytorium, opisana prostym językiem, dała mu sprawy do rozstrzygnięcia — 7 z nich rozstrzygnął, a 5 z tych 7 dało dopisek do dokumentu zadania.
- Odbiorcą jest Mariusz, który przyjmuje dokument zadania i rozstrzyga sprawy otwarte, oraz agent wykonujący zadanie w cyklu, który dostaje dokument bez tych luk.

### To do

1. Krok „Review and hand off” (`project-level/task/skill/final_review.md`, akapit, który zaczyna się od „When the draft is complete, show it whole.”) dostaje przed pokazaniem kompletnego dokumentu człowiekowi krok „spis decyzji”: agent doprecyzowania uruchamia go, gdy dokument ma niepustą sekcję *Decisions in play* albo zadanie zmienia skill lub plik instrukcji; przy innych zadaniach go pomija (pytanie 1).
2. Pierwszy agent spisu: agent doprecyzowania uruchamia świeżego agenta klasy tańszej od swojej, nazwanej ogólnie, nie nazwą modelu (pytanie 3). Agent dostaje wyłącznie kompletny dokument zadania i pełne brzmienie wpisów fundamentu z jego *Decisions in play*, bez rozmowy doprecyzowania. Wypisuje decyzje, które wykonawca musiałby podjąć, a które dokument i wpisy zostawiają bez odpowiedzi albo rozstrzygają tylko w części, i przy każdej zaznacza, skąd zna odpowiedź: zapisana (gdzie i jakim zdaniem), widoczna tylko z pliku, który dokument wskazuje jako wzór, albo zgadywana — z odpowiedzią, jaką by przyjął.
3. Granica spisu jest ta sama co sprawdzania słów (WAY-374): decyzja liczy się tylko wtedy, gdy wynika ze zdania, które naprawdę stoi w dokumencie zadania albo we wskazanym wpisie fundamentu, i gdy różne rozstrzygnięcia dają różny, zauważalny wynik w zakresie zadania; scenariusz spoza zakresu się nie liczy. Spis nie ma obowiązku znaleźć decyzji ani podać liczby; sprawy, o które sprawdzanie słów już zapytało albo które stoją w *Questions to settle*, nie wracają.
4. Drugi agent, krytyka: agent doprecyzowania uruchamia świeżego agenta tej samej klasy, z dostępem do odczytu repozytorium, które zadanie zmienia, na wzór krytyki z WAY-120. Dostaje dokument, wpisy fundamentu i listę pierwszego agenta i przy każdym zgadnięciu ustala: czy odpowiedź jest już rozstrzygnięta w repozytorium albo w dokumencie (z cytatem i ścieżką), czy odpowiedź przyjęta przez pierwszego agenta zgadza się z tym, co repozytorium mówi, co by się zmieniło w plikach, które zadanie zmienia, gdyby odpowiedź była inna, i werdykt: najpewniej trafiona, najpewniej błędna albo naprawdę otwarta. Pisze prostym językiem; czego nie sprawdził, nazywa niesprawdzonym.
5. Agent doprecyzowania sprawdza cytaty krytyki przy każdej sprawie, którą pokaże, i daje jej jeden jawny werdykt (WAY-120). Człowiekowi pokazuje tylko sprawy naprawdę otwarte i luki samego dokumentu, najwyżej około czterech, najważniejsze pierwsze, każdą prostym językiem, jak WAY-113 każe pytać o decyzję (drogi, koszt, rekomendacja). Pełna lista i krytyka zostają w pliku w ignorowanym katalogu `.runs/` produktu, którego ścieżkę agent podaje człowiekowi. Gdy żadna sprawa nie jest otwarta, agent nic o kroku nie mówi (pytanie 2).
6. Odpowiedzi człowieka stają pod *Questions to settle* z jego słowami jako źródłem i drogami niewybranymi, jak przy każdym pytaniu; to, co zmieniają w *Decisions in play* i *Settlements to record*, wchodzi do dokumentu tak jak przy reszcie doprecyzowania (kroki 4 i 5 przepisu).
7. W doprecyzowaniu z orkiestratorem (`project-level/task/skill/orchestrated_mode.md`, akapit „Use `find-foundation-entries` in task mode […]. Start no child agent.”) agent doprecyzowania nie uruchamia żadnego agenta: zapisuje oba kroki jako *Child-work request* w swojej turze, tak jak prośbę o przebieg kroku rozstrzygającego technologię, a orkiestrator je uruchamia i przynosi listę oraz krytykę; sprawy dla człowieka agent wpisuje do tury jako materiał dla człowieka.
8. Sekcja „## 6. Review and hand off” w `project-level/task/skill/SKILL.md` wymienia krok jednym zdaniem obok sprawdzenia kompletnego dokumentu.

### Questions to settle

- Kiedy agent doprecyzowania uruchamia spis decyzji?
  - Answer: tylko gdy dokument ma niepustą sekcję *Decisions in play* albo zadanie zmienia skill lub plik instrukcji; przy innych zadaniach krok jest pominięty.
  - Not chosen:
    - przy każdym doprecyzowaniu zadania the way — jeden przebieg dwóch agentów kosztował w próbie około 200–250 tysięcy tokenów i 3–5 minut; przy drobnych zadaniach (zmiana nazwy, drobna poprawka) koszt przewyższa zysk
    - tylko na prośbę Mariusza — zależy od tego, czy o tym pamięta, a luki dalej zamyka agent w trakcie wykonania
  - Source: Mariusz, 2026-11-14: „1b”
- Co widzi człowiek po spisie i krytyce?
  - Answer: tylko sprawy otwarte i luki dokumentu, najwyżej około czterech, prostym językiem, każda z kosztem dróg i rekomendacją; pełna lista zostaje w pliku.
  - Not chosen:
    - pełna lista zgadnięć — surowa lista zajęła Mariuszowi 5 minut i nie dała się ocenić; krytyka mogła uznać sprawę za trafioną, choć agent się mylił, dlatego pełna lista zostaje w pliku, a agent doprecyzowania sprawdza cytaty krytyki
  - Source: Mariusz, 2026-11-14: „2a”
- Na jakiej klasie modelu pracują oba agenty?
  - Answer: na tej samej klasie, tańszej od klasy agenta doprecyzowania (w próbie model sonnet), nazwanej w dokumencie ogólnie.
  - Not chosen:
    - mocniejszy model — kilka razy droższy bez dowodu, że jest potrzebny: w próbie krytyka na tańszej klasie znalazła m.in. wpis, który naruszał WAY-90, i lukę w szablonie opisu PR-a, a wyrywkowo sprawdzone cytaty zgadzały się z repozytorium
  - Source: Mariusz, 2026-11-14: „3a”

## Context

- Pomysł pochodzi z karty D8 („Wypróbować na dwóch zadaniach spis decyzji z oznaczeniem źródła”) w the author's notes on the AI Tech Leaders course; rachunek „8 z 14” pochodzi z sekcji 3 `the author's note on the improvements of the-way`.
- Próba z 14.11.2026 dała na dwóch dokumentach: pierwszy 14 pozycji (5 zapisanych, 9 zgadnięć), drugi 14 (1 zapisana, 1 z kodu, 12 zgadnięć); krytyka ustaliła, że 5 z 9 zgadnięć pierwszego dokumentu było już rozstrzygniętych w repozytorium; Mariusz rozstrzygnął 7 spraw, z których 5 dało dopisek do dokumentu zadania. Jeden przebieg dwóch agentów kosztował około 200–250 tysięcy tokenów i 3–5 minut.
- Miejsce kroku: `final_review.md`, a nie `resolve_gaps.md`, bo pierwszy agent czyta kompletny dokument z *Decisions in play*, a te powstają w kroku 4 przepisu, po kroku „Resolve the gaps”. Plik `resolve_gaps.md` zmienia równocześnie inne zadanie w innym akapicie (lista przewodnika wdrożeniowego), więc rozdzielenie unika kolizji.
- Granica z punktu 3 i zasada milczenia, gdy nic nie znaleziono, pochodzą z WAY-374 (zadanie, którego cykl scalił PR #124).
- Krok przejmuje praktykę z kursu AI Tech Leaders, więc wiąże dopiero przez decyzję z wiersza 1 *Settlements to record* (WAY-100).
- Pokrewne, ale osobne: zadanie „Pokazywać najmocniejszy argument przeciw propozycji agenta przed jej zatwierdzeniem” dotyczy propozycji agenta w pytaniu o decyzję (WAY-113), nie sprawdzania dokumentu zadania.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-374** — „At its step that resolves the gaps, the refinement of a task looks in the task document and in the sentences of the sources its required result rests on […] for a word that allows two different required behaviours […]. A reading no sentence allows and a case outside the task's scope raise no question, the check owes no finding and no number of cases, and where the agent finds none it says nothing of the check.” — wzór granicy i milczenia przy braku znaleziska; spis idzie po tym sprawdzeniu i nie powtarza jego pytań.
- **WAY-120** — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” — wzór dla drugiego agenta; agent doprecyzowania sprawdza cytaty krytyki.
- **WAY-113** — „An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel.” — tak agent pokazuje człowiekowi sprawy otwarte.
- **WAY-229** — „The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model […]” — decyzja nie dotyczy agentów doprecyzowania; zadanie nazywa ich klasę w ten sam sposób, ogólnie.
- **WAY-100** — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” — spis pochodzi z kursu, więc wiąże przez decyzję z wiersza 1.
- **WAY-134** — „[…] where the human chose among ways shown, each way not chosen, under the answer to its question or, for a choice made outside the task's questions, in the source of the row it settles […]” — tak odpowiedzi z tego kroku stają w dokumencie.
- **WAY-124** — „It is ready when the human has seen and accepted its complete document, its required outcome is stated, every known question blocking that outcome is answered […]” — spis biegnie przed pokazaniem kompletnego dokumentu do akceptacji.
- **WAY-154** — „Project refinement resumes from the plan, task documents and one ignored conversation file per task at `.runs/project-refinement/<task-name>.md`, through which fresh parallel refiners, the answering agent and the project orchestrator take serialized turns on each file […]” — w doprecyzowaniu z orkiestratorem agenty uruchamia orkiestrator, nie doprecyzowujący (punkt 7).

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-14

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Doprecyzowanie zadania przejmuje z kursu AI Tech Leaders (karta D8) spis decyzji, które dokument zostawia wykonawcy: przed pokazaniem kompletnego dokumentu człowiekowi dwaj świeży agenci tej samej, tańszej klasy wypisują takie decyzje i sprawdzają je w repozytorium, gdy dokument ma niepustą sekcję *Decisions in play* albo zadanie zmienia skill lub plik instrukcji, żeby luki zamykał człowiek przed cyklem, a nie agent w jego trakcie. | decision | pytania 1 i 3 (wybór człowieka; *Not chosen* tam) i wynik próby z 14.11.2026 w *Context* | czy pisać decyzję o przejęciu praktyki (WAY-100), przy jakich zadaniach krok biegnie i na jakiej klasie modelu |
| 2 | Po spisie i krytyce człowiek widzi tylko sprawy otwarte i luki dokumentu, najwyżej około czterech, każdą z kosztem dróg i rekomendacją; pełna lista zostaje w pliku, a agent doprecyzowania sprawdza cytaty krytyki, zanim pokaże sprawę. | decision | pytanie 2 (wybór człowieka; *Not chosen* tam); WAY-120 | czy człowiek dostaje pełną listę zgadnięć i czy agent doprecyzowania pokazuje obserwacje krytyki bez sprawdzenia |

## Out of scope

- Sprawdzanie słowa o dwóch znaczeniach (WAY-374) w `resolve_gaps.md` — zostaje bez zmian.
- Zasada „najmocniejszy argument przeciw propozycji” (WAY-113) — osobne zadanie.
