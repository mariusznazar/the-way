---
title: "the way: kiedy podział zadania ma sens, a kiedy tylko dokłada pracy"
status: draft
created: 2026-11-12T19:30
updated: 2026-11-13
tags: [zadanie]
related: "the project note of the process work"
---

# the way: kiedy podział zadania ma sens, a kiedy tylko dokłada pracy

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Według relacji Mariusza agent przy doprecyzowaniu większego zadania proponuje podzielić je na kilka i dokłada rekomendację podziału, choć podział nie przyspiesza realizacji, nie obniża jej kosztu ani nie poprawia wyniku.
- Rekomendację uzasadnia korzyściami, które dla Mariusza nic nie znaczą, np. że część będzie gotowa szybciej.
- Mariusz traci przy każdym doprecyzowaniu większego zadania turę rozmowy na odpieranie podziału albo przyjmuje podział, który czyni całość wolniejszą i droższą.
- Każdy przyjęty podział bez korzyści to drugi pełny cykl: osobny przegląd, osobne pełne testy, osobna prośba o scalenie.
- Nigdzie nie jest zapisane, kiedy podział faktycznie się opłaca; zadanie ma to ustalić, nie wprowadzić reguły „nigdy nie dzielimy”.
- Jak często to się zdarza, nie jest ustalone.

### To do

1. Akapit o jednym zadaniu w `project-level/task/skill/read_sources.md` (akapit zaczynający się od „Check that this is one task”, około linii 28) pozwala agentowi wskazać podział tylko z trzech powodów, każdy nazwany przy propozycji: część nie może ruszyć albo się skończyć bez czegoś spoza doprecyzowania (dostępu, którego agent nie ma, wyniku innego zadania); części zadania zmieniają różne repozytoria, a cykl pisze tylko w repozytorium produktu; późniejszy krok tej instrukcji sam proponuje osobne zadanie (pytanie 2).
2. Ten sam akapit mówi, że przy samym rozmiarze zadania agent nic nie mówi o podziale: ani wzmianki, ani pytania, ani rekomendacji (pytanie 3).
3. Decyzja WAY-13 traci zdanie, że rozmiar zadania „otherwise serves only as a signal to split it”; w jego miejscu stoi, że poza przygotowaniem i wykonaniem zmiany rozmiar niczego nie rozstrzyga (pytanie 3).
4. Krok o umiejętności wdrożenia w `project-level/task/skill/resolve_gaps.md` (zdanie „offer the human to split it into a task of its own”, około linii 63) dodaje do *To do* punkt na brakującą pracę i nie proponuje jej wydzielenia (pytanie 4).
5. Punkt tego kroku zaczynający się od „Where the product has no deployment skill at all, ask before offering the split” (około linii 85) przestaje zakładać ofertę podziału: agent zadaje jego pytania, zanim człowiek sam wydzieli tę pracę, tak żeby wydzielone zadanie niosło odpowiedź albo odmowę (pytanie 6).
6. Wzmianka „deployment-work splits” znika z listy spraw idących do człowieka w `project-level/task/skill/orchestrated_mode.md` (około linii 15) (pytanie 4).
7. Podział projektu na zadania w `project-level/plan/skill/cut_tasks.md` traci zdanie „A large task is split” (około linii 4); zadania tnie się według WAY-143 i powodów z punktu 1 (pytanie 5).

### Questions to settle

- 1. Który sprawdzian obowiązuje: podział ma sens, gdy realizacja będzie szybsza, tańsza i lepsza naraz, gdy wystarczy jedno z trzech, czy gdy będzie lepsza albo tańsza, a czas się nie liczy?
  - Answer: podział ma sens, gdy realizacja będzie dzięki niemu lepsza albo tańsza; sam czas się nie liczy, więc „część będzie gotowa szybciej” podziału nie uzasadnia.
  - Not chosen:
    - wszystkie trzy naraz — przechodzi praktycznie tylko podział tam, gdzie jedno zadanie i tak nie przejdzie przez jeden cykl, a odpada nawet „lepiej” okupione drugim cyklem.
    - wystarczy jedno z trzech — przechodzi „dwa cykle równolegle skończą się szybciej”, choć drożej, czyli dokładnie te argumenty, które Mariusz odrzuca.
  - Source: doradca dnia, odpowiedź Mariusza, 2026-11-13, „1 c — lepiej albo taniej, a sam czas się nie liczy”.
- 2. Z jakich powodów agent sam proponuje podział zadania?
  - Answer: tylko z dzisiejszych dwóch — część nie może ruszyć albo się skończyć bez czegoś spoza doprecyzowania, albo późniejszy krok instrukcji sam proponuje podział — i, nazwanego wprost, trzeciego: części zadania zmieniają różne repozytoria, bo cykl pisze tylko w repozytorium produktu; nic więcej.
  - Not chosen:
    - dodatkowo część ryzykowna obok niezależnej — ryzyko obsługuje już przegląd nastawiony na nie i decyzja człowieka przy prośbie o scalenie, a podział daje tylko to, że część niezależna scali się bez czekania, czyli „szybciej”.
    - dodatkowo prośba o scalenie za duża na sensowny przegląd — przy doprecyzowaniu agent zna rozmiar zadania, nie przyszłej zmiany, więc to sam rozmiar w przebraniu.
    - ogólny sprawdzian zamiast listy: agent proponuje, gdy nazwie konkretnie, co będzie lepsze albo tańsze — agent łatwo dorabia wiarygodne „lepiej”, a to jest dzisiejszy problem.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13, „2 a, 3 a (zgoda na zmianę zdania w WAY-13), 4 a, 5 a”.
- 3. Co agent robi, gdy zadanie jest po prostu duże: nic nie mówi, wspomina jednym zdaniem bez pytania, czy pyta jak dziś?
  - Answer: nic nie mówi; Mariusz widzi cały dokument przy akceptacji i może sam poprosić o podział. Zdanie WAY-13 „otherwise serves only as a signal to split it” zmienia się tak, że rozmiar poza przygotowaniem i wykonaniem zmiany niczego nie rozstrzyga — na tę zmianę decyzji jest zgoda.
  - Not chosen:
    - jedno zdanie bez pytania i bez rekomendacji — wzmianka dalej kusi agenta do pytania, więc instrukcja musiałaby pytania wprost zabraniać.
    - jak dziś — pytanie wraca przy każdym większym zadaniu.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13, „2 a, 3 a (zgoda na zmianę zdania w WAY-13), 4 a, 5 a”.
- 4. Czy krok o umiejętności wdrożenia dalej proponuje wydzielenie brakującej pracy do osobnego zadania?
  - Answer: nie; agent dodaje punkt do *To do*, a człowiek może wydzielić tę pracę sam, jak WAY-139 już mówi („or the human splits that work into a task of its own”). Znika wzmianka „deployment-work splits” w trybie z orkiestratorem; co dzieje się z punktem „ask before offering the split”, rozstrzyga pytanie 6.
  - Not chosen:
    - zostawić ofertę — pytanie o podział wraca przy każdym zadaniu wdrożeniowym, a wydzielenie to drugi cykl, na który zadanie wdrożeniowe i tak musi czekać.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13, „2 a, 3 a (zgoda na zmianę zdania w WAY-13), 4 a, 5 a”.
- 5. Czy podział projektu na zadania przestaje dzielić zadanie z powodu samego rozmiaru?
  - Answer: tak, w tym zadaniu; z podziału projektu znika zdanie „A large task is split”, a zadania tnie się według WAY-143 i powodów z pytania 2.
  - Not chosen:
    - poza zakresem — reguła zostaje i rozjazd między doprecyzowaniem a podziałem projektu też.
    - osobne zadanie — osobne doprecyzowanie i osobny cykl.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13, „2 a, 3 a (zgoda na zmianę zdania w WAY-13), 4 a, 5 a”.
- 6. Gdy produkt nie ma umiejętności wdrożenia wcale, a agent już nie proponuje wydzielenia jej napisania: czy punkt „ask before offering the split” znika, czy zostaje z pytaniami zadawanymi, zanim człowiek sam wydzieli tę pracę?
  - Answer: zostaje w zmienionym brzmieniu: agent zadaje te pytania, zanim człowiek sam wydzieli tę pracę, więc wydzielone zadanie niesie odpowiedź albo odmowę.
  - Not chosen:
    - punkt znika — gdy człowiek sam wydzieli napisanie umiejętności, pytania o czas życia logów i o awarie mogą nie paść nigdzie, a wyjdzie to dopiero przy pierwszym wdrożeniu, które z niej skorzysta.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13, „6 b”.

## Context

- Dzisiejszą regułę o jednym zadaniu wprowadził commit eac1751 („split the refinement's one-task check by default”).
- Cykl sam dzieli dużą zmianę: plan zadania tnie ją na kawałki, a każdy kawałek robi osobny agent (`task-cycle/plan/SKILL.md`); zmiana jednego autora, która okaże się za duża, wraca do planowania (`task-cycle/skill/SKILL.md`, akapit zaczynający się od „A one-author change that proves too large”).
- Cykl pisze tylko w repozytorium produktu (`task-cycle/skill/SKILL.md`, akapit zaczynający się od „The cycle writes only in the task's worktree”).
- Wspólny sposób pytania (`elements/common/way_of_working.md`, „How a skill asks”) każe pytanie o decyzję podać z wariantami, ich kosztem i rekomendacją.
- Przypadek, z którego to wyszło: the note of the task on the review of the whole change, pytanie 1, z odpowiedzią Mariusza z 2026-11-12: „ja chcę je po prostu zrobić, nie ma znaczenia czas i że zajmie więcej; rozdzielenie miałoby dla mnie sens tylko wtedy kiedy spowodowałoby, że realizacja będzie szybsza, tańsza i lepsza”.
- Po zmianie z punktu 4 późniejszym krokiem doprecyzowania, który sam proponuje osobne zadanie, zostaje brak wytycznych dyscypliny: instrukcja proponuje wtedy zadanie wstępne, na które to zadanie czeka (`project-level/task/skill/guideline_findings.md`, „Missing discipline guidelines”).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-13 — What sets the weight of a task's process? Zdanie o rozmiarze: „A task's size may lighten how its change is prepared and made — its plan and the number of agents making it — never the outcome it has to reach or the checks run on the finished change, and otherwise serves only as a signal to split it; only a human sets a task to return knowledge instead of a change, which merges nothing.” Zmiana, którą robi to zadanie (pytanie 3, wariant a): fragment „and otherwise serves only as a signal to split it” zastępuje stwierdzenie, że poza tym rozmiar niczego nie rozstrzyga.
- WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one? Zdanie o podziale: „When a task's outcome deploys the product or changes how or where it runs, the-way's skill `refine-task` checks, while it refines the task, that the product has a deployment skill covering every item of the list, and where it has none or an item is missing, the task gains an item of its To do for that work or the human splits that work into a task of its own.”
- WAY-143 — What does a task of a project plan end with? „A task of a project plan ends with something that can be checked in the running product, never with a layer of the product put in place; a preparatory task stands in the plan only where a task of the plan depends on it, the task it opens the way for. A technical element enters the plan with the first task that uses it, or with a preparatory task that task depends on.”
- WAY-113 — How does an agent of the-way ask a human decision? Działa przez „How a skill asks” w `elements/common/way_of_working.md`: „A question of decision — a choice that settles something in a file — gives the ways open, what each costs, and a recommendation.”

## Settlements to record

Candidates: 7 shown, 6 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Podział zadania ma sens, gdy realizacja będzie dzięki niemu lepsza albo tańsza; sam czas się nie liczy, więc „część będzie gotowa szybciej” podziału nie uzasadnia. | decision | pytanie 1 | jakie uzasadnienie reguły podziału wpisać i czy podział dający tylko wcześniejsze scalenie części przechodzi |
| 2 | Agent sam proponuje podział zadania tylko wtedy, gdy część nie może ruszyć albo się skończyć bez czegoś spoza doprecyzowania, gdy części zmieniają różne repozytoria albo gdy późniejszy krok instrukcji sam proponuje osobne zadanie, i nazywa ten powód. | decision | pytanie 2 | czy część ryzykowna obok niezależnej albo za duża prośba o scalenie też uzasadnia propozycję podziału |
| 3 | Przy samym rozmiarze zadania agent nic nie mówi o podziale, a rozmiar poza przygotowaniem i wykonaniem zmiany niczego nie rozstrzyga; zmienia WAY-13. | decision | pytanie 3 | czy zostawić w instrukcji jednozdaniową wzmiankę o rozmiarze i czy zmienić WAY-13 |
| 4 | Krok o umiejętności wdrożenia dodaje brakującą pracę do *To do* i nie proponuje jej wydzielenia; człowiek może wydzielić ją sam. | decision | pytanie 4 | czy krok wdrożeniowy dalej proponuje osobne zadanie na umiejętność wdrożenia |
| 5 | Gdy produkt nie ma umiejętności wdrożenia wcale, agent zadaje pytania o czas życia zapisu logów i o awarie, zanim człowiek sam wydzieli jej napisanie, więc wydzielone zadanie niesie odpowiedź albo odmowę. | decision | pytanie 6 | czy usunąć punkt „ask before offering the split”, zostawiając wydzielone zadanie bez tych pytań |
| 6 | Podział projektu na zadania nie dzieli zadania z powodu samego rozmiaru; zadania tnie się według WAY-143 i powodów z wiersza 2. | decision | pytanie 5 | czy zostawić w podziale projektu zdanie „A large task is split” |

## Out of scope

none
