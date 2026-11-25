---
title: "the way: rekomendacja w pytaniu o decyzję nie daje mniej niż cel zadania ani niż wzorzec, z którym cel każe się porównać"
status: draft
created: 2026-11-25T21:30
updated: 2026-11-25
tags: [zadanie]
related: "the project note in the author's backlog"
---

## Po co to

- **Jak jest dziś:** agent doprecyzowania zadania, który zadaje Mariuszowi pytanie z wariantami, poleca czasem wariant tańszy, który robi mniej, niż każe cel zadania w planie — choć cel mówi wprost „co najmniej tak dobry jak w starym Loopie”. Reguła procesu o tym, jak skill pyta, każe dać rekomendację z jej słabym punktem, ale nie mówi, że rekomendacja nie może schodzić poniżej celu.
- **Kto to odczuwa:** Mariusz przy każdej partii pytań w doprecyzowaniu; musi wyłapać taką rekomendację sam i odrzucić ją, a prowadzący projekt poprawia kolejne rekomendacje ręcznie, bo agenci doprecyzowania jego uwag nie widzą.
- **Co jeśli nic:** błąd wraca w każdym zadaniu o wyglądzie albo o grze „jak w starym Loopie” — 25 listopada w jednej rundzie wrócił w trzech zadaniach — a gdy Mariusz go przeoczy, do cyklu idzie zadanie, które z góry da mniej, niż obiecał plan.

# the way: rekomendacja w pytaniu o decyzję nie daje mniej niż cel zadania ani niż wzorzec, z którym cel każe się porównać

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Reguła „How a skill asks” w `elements/common/way_of_working.md` i decyzja WAY-113 każą przy pytaniu o decyzję dać rekomendację z jej słabym punktem, ale nie mówią, że polecany wariant nie może dawać mniej, niż cel, który materiał stawia pracy.
- Według relacji z rundy doprecyzowania loop2 z 2026-11-25 agenci doprecyzowania polecali warianty, które dają mniej niż cel zadania w planie porównujący wynik ze starym Loopem, w trzech zadaniach jednej rundy (szczegóły w *Context*); Mariusz musi takie rekomendacje wyłapywać sam.
- Reguła należy do procesu, nie do produktu: „How a skill asks” czyta każdy skill the way, który pyta człowieka, a cel porównujący wynik ze wzorcem może mieć zadanie każdego produktu.

### To do

1. Punkt reguły „How a skill asks” o pytaniu o decyzję w `elements/common/way_of_working.md` (ten, który zaczyna się od „A question of decision — a choice that settles something in a file —”) mówi, że polecany wariant nie daje mniej niż cel, który materiał stawia pracy — cel zadania w planie, potrzeba w dokumencie zadania, cel i miara sukcesu definicji projektu — a gdy cel porównuje wynik ze wzorcem, daje co najmniej to, co wzorzec, cecha po cesze (pytanie 1).
2. Ten sam punkt mówi, że wariant, który daje mniej niż cel, stoi wśród wariantów z tym, czego mu do celu brakuje, w swojej linii, ale nigdy nie jest polecany; gdy żaden wariant nie osiąga celu, pytanie nie ma wariantu polecanego i mówi to wprost; gdy agent uważa, że cel nie jest wart swojego kosztu — także wtedy, gdy żaden wariant go nie osiąga — stawia osobne pytanie o decyzję, czy zmienić cel, które rozstrzyga się tam, gdzie stoi cel: plan u jego właściciela, definicję przez jej zatwierdzenie gotowości (WAY-118), cel zadania niezależnego u człowieka w tym samym doprecyzowaniu (pytania 2 i 4).
3. `elements/common/critique/prepare.md`, w akapicie, który zaczyna się od „Give the fresh agent the complete proposal or set”, mówi, że gdy propozycja albo zestaw zawiera pytanie o decyzję do człowieka, wśród reguł podanych krytykowi zawsze stoi „How a skill asks” z `elements/common/way_of_working.md`; `elements/common/critique/check.md` nie dostaje własnej kopii tej reguły (pytanie 3).

### Questions to settle

- 1. Czy reguła obejmuje każdy cel, który materiał stawia pracy, czy tylko cel porównujący wynik z jawnym wzorcem („co najmniej tak … jak X”)?
  - Answer: każdy cel, który materiał stawia pracy: cel zadania w planie, potrzeba w dokumencie zadania, cel i miara sukcesu w definicji projektu; gdy cel porównuje wynik ze wzorcem, „nie mniej” znaczy co najmniej to, co daje wzorzec, sprawdzane cecha po cesze.
  - Not chosen:
    - tylko cel z jawnym wzorcem — łatwy do sprawdzenia, ale wariant, który po prostu nie spełnia celu bez wzorca, dalej może być polecony; Mariusz mówił ogólnie: „polecanie wariantu, który nie spełnia celu, to ten sam błąd z wzorcem i bez”
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „1 a — Mariusz mówił ogólnie: cel był jasny, ma być tak samo albo lepiej; polecanie wariantu, który nie spełnia celu, to ten sam błąd z wzorcem i bez.”
- 2. Co z wariantem tańszym, który daje mniej niż cel — czy może być polecany, gdy jego słaby punkt mówi to wprost?
  - Answer: nigdy jako polecany; stoi wśród wariantów, a jego linia mówi, czego mu brakuje do celu; gdy agent uważa, że cel nie jest wart swojego kosztu, mówi to osobno, jako propozycję zmiany celu, którą rozstrzyga się tam, gdzie stoi cel — plan u jego właściciela, definicję przez jej zatwierdzenie gotowości (WAY-118), cel zadania niezależnego u człowieka w tym samym doprecyzowaniu.
  - Not chosen:
    - polecany, gdy jego słaby punkt mówi wprost, że schodzi poniżej celu, i dlaczego — to w praktyce dzisiejsza reguła słabego punktu, pod którą stały już wszystkie cztery przypadki z 25.11
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „2 a.”
- 3. Czy oprócz reguły dopisać punkt do sprawdzenia, które robi niezależny krytyk zestawu (`elements/common/critique/check.md`)?
  - Answer: nie dopisywać punktu do listy krytyka, tylko naprawić jego wejście: tam, gdzie the way wysyła krytyka na zestaw z pytaniami o decyzję, reguła „How a skill asks” jest zawsze podawana jako reguła do sprawdzenia — w jednym miejscu, bez drugiej kopii treści. Tym miejscem jest `elements/common/critique/prepare.md`: każde wysłanie krytyka w the way idzie przez `elements/common/critique/SKILL.md`, który każe przy wysłaniu przeczytać `prepare.md`, a ten mówi dziś tylko „the full relevant sources and applicable rules”, więc niczego nie wymusza.
  - Not chosen:
    - bez zmian, bo krytyk dostaje „applicable rules” i sprawdza „each item against its required form” — krytyk widzi regułę tylko wtedy, gdy wysyłający poda mu `way_of_working.md`, a nic tego nie wymusza; to dokładnie cichy brak z 25.11, gdy krytyk widział regułę tylko dlatego, że prowadzący pamiętał
    - jedno zdanie w `elements/common/critique/check.md` o sprawdzeniu rekomendacji względem celu — druga kopia reguły wbrew WAY-35, czytana przy każdej krytyce, także bez pytań
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „3 — ani a, ani b: słaby punkt a to dokładnie cichy brak, który wyszedł 25.11 (krytyk widział regułę tylko dlatego, że prowadzący pamiętał), a b kopiuje regułę wbrew WAY-35. Napraw wejście krytyka, nie jego listę: tam, gdzie the way wysyła krytyka na zestaw z pytaniami o decyzję, regułę How a skill asks podaje się zawsze jako regułę do sprawdzenia — jedno miejsce, bez drugiej kopii treści.”; fakt: `elements/common/critique/SKILL.md` @ 07aa55df („When invoking a critique, read `prepare.md` beside this skill”), `elements/common/critique/prepare.md` @ 07aa55df („Give the fresh agent the complete proposal or set, its intended moment of use, the full relevant sources and applicable rules”); wysłania krytyka na zestaw z pytaniami do człowieka: `project-level/lead/skill/SKILL.md` krok 4 (ok. :141), `project-level/technology/settle.md` krok 4 i 5 (ok. :21, :45), `product-guidelines/*/settle.md` „Critique”, `project-level/skill/readiness_approval.md` (ok. :31) — każde przez `elements/common/critique/SKILL.md`
- 4. Co robi agent, gdy żaden wariant nie osiąga celu, i w jakiej formie stawia propozycję zmiany celu?
  - Answer: pytanie nie ma wtedy wariantu polecanego i mówi to wprost; propozycja zmiany celu — także wtedy, gdy żaden wariant celu nie osiąga — jest osobnym pytaniem o decyzję, czy zmienić cel, rozstrzyganym tam, gdzie stoi cel.
  - Not chosen:
    - zostawić punkt 2 *To do* bez tego dopowiedzenia — cykl sam rozstrzygnąłby oba przypadki bez Mariusza, a agent bez wariantu osiągającego cel dostałby dwa sprzeczne zdania („nigdy nie jest polecany” i „pytanie o decyzję daje rekomendację”)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „A — a (dopisać brzmienie: bez wariantu polecanego, gdy nic nie osiąga celu, i osobne pytanie o decyzję o zmianie celu — usuwa sprzeczność dwóch zdań, koszt dwa zdania).”; fakt: `elements/common/way_of_working.md:28` @ 07aa55df („A question of decision — a choice that settles something in a file — gives the ways open, what each costs, […] and a recommendation with its weak point”)

## Context

- Słowa Mariusza, 2026-11-25, odpowiedź na pytanie, co z katalogu map starego Loopa ma mieć ekran Mapy (loop2, zadanie 3; cel zadania w planie: „co najmniej tak czytelny jak w starym Loopie”; agent polecał „rdzeń katalogu” bez szukajki i trzech widoków): „1a - nie rozumiem rekomendacji kiedy cel był jasny, ma być tak samo albo lepiej, rekomendacja jest, żeby nie robić rzeczy, czyli żeby było gorzej”.
- Nawroty w tej samej rundzie loop2, 2026-11-25, każdy poprawiony ręcznie przez prowadzącego projekt przed pokazaniem Mariuszowi: zadanie 18 (paski parametrów) — agent polecał brak koloru paska przy ogniu, brak pulsowania alarmu, sam pasek bez objaśnień po kliknięciu i bez znacznika ciosu, choć stary Loop ma to wszystko; zadanie 8 (wyposażenie postaci) — agent polecał, żeby po zużyciu broni ręka zostawała pusta do końca przejścia, choć w starym Loopie kolejny cios brał następną sztukę z plecaka.
- Prowadzący projekt dopisywał po odpowiedzi Mariusza do notatek dla agentów doprecyzowania zdanie „recommendations never below the old Loop or the plan goal”, a niezależny krytyk rundy sprawdzał je jako osobny punkt; działało tylko w tej rundzie i tylko dlatego, że prowadzący pamiętał.
- Odrzucone przed doprecyzowaniem: wpis w pamięci prowadzącego projekt — rekomendacje piszą agenci doprecyzowania, którzy tej pamięci nie czytają; reguła tylko w loop2 — błąd nie zależy od produktu.
- Ta myśl nie stoi dziś w the way innymi słowami: ani w `elements/common/way_of_working.md`, ani w `elements/common/critique/check.md`, ani w żadnym innym pliku `.md` the way z regułą o rekomendacji (przeszukanie słów „recommend”, „goal”, „at least as” @ 07aa55df).
- Słaby punkt rekomendacji wszedł do WAY-113 w commicie a14b07f6 (2026-11-15); wszystkie cztery przypadki z 25.11 stały już pod tą regułą, więc sam słaby punkt ich nie łapie.
- Reguły „poleć najprostszy i najtańszy wariant” (WAY-123, `project-level/definition_template.md`, `project-level/technology/settle.md`, `product-guidelines/*/new_tools.md`) działają tylko tam, gdzie między wariantami nie zostaje różnica ze skutkiem dla produktu, więc nie kolidują z regułą tego zadania.
- Pierwszy akapit zdań wiążących WAY-113 ma dziś trzy zdania, a cała część wiążąca ok. 310 słów; `elements/common/foundation_check.py` zgłasza w decyzji, którą zmiana zmienia, akapit ponad trzy zdania albo 300 słów i część wiążącą ponad 600 słów.
- Krytyk zestawu w rundzie projektu dostaje „its sources and applicable rules” (`project-level/lead/skill/SKILL.md`, krok 4, ok. :141) i sprawdza „each item against its required form” (`elements/common/critique/check.md`, ostatni akapit).
- Decyzja WAY-120 mówi ogólnie, że krytyk dostaje „its sources and applicable rules”; reguła z punktu 3 *To do* dopowiada w skillu krytyki, która reguła zawsze do nich należy, i tamtego zdania nie zmienia.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-113 — How does an agent of the-way ask a human decision? — „An agent asks in plain conversation text, with no separate question panel: a question of assessment stays open, and a decision question gives the available ways, the cost of each, a recommendation and the weak point of the way recommended. The cost of a way includes the cost of undoing it later, written as one word where it is nil; the weak point is the strongest argument against the way recommended, anchored in the material where the material gives one, and for a shortcut, where another way would be right were cost no matter, it names that way and says why it is not recommended. […]” (`foundations/decisions.md` @ 07aa55df). Zmiana, którą zadanie wnosi: zdania wiążące i *Verification* mówią, że polecany wariant nie daje mniej niż cel, który materiał stawia pracy, a przy celu ze wzorcem co najmniej to, co wzorzec; wariant poniżej celu stoi z tym, czego mu brakuje, nigdy jako polecany; gdy żaden wariant nie osiąga celu, pytanie nie ma wariantu polecanego; uwaga, że cel nie jest wart kosztu, idzie jako osobne pytanie o decyzję o zmianie celu (pytania 1, 2 i 4; wiersz 1 *Settlements to record*).
- WAY-120 — How does the-way critique an agent's proposal? — „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” (`foundations/decisions.md` @ 07aa55df). Zadanie jej nie zmienia; punkt 3 *To do* stoi w skillu krytyki pod nią.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-25

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Polecany wariant w pytaniu o decyzję nie daje mniej niż cel, który materiał stawia pracy — przy celu ze wzorcem co najmniej to, co wzorzec, cecha po cesze; wariant poniżej celu stoi z tym, czego mu brakuje, nigdy jako polecany; gdy żaden wariant nie osiąga celu, pytanie nie ma wariantu polecanego; uwaga, że cel nie jest wart kosztu, idzie jako osobne pytanie o decyzję o zmianie celu tam, gdzie cel stoi. | sentence of WAY-113 | Questions to settle, pytania 1, 2 i 4 | czy zmienić samą regułę w `way_of_working.md`, czy też WAY-113 i jej *Verification*; czy reguła obejmuje tylko cele ze wzorcem; co robi pytanie, gdy żaden wariant nie osiąga celu |
| 2 | Tam, gdzie the way wysyła krytyka na zestaw z pytaniami o decyzję do człowieka, reguła „How a skill asks” zawsze stoi wśród reguł podanych krytykowi — w jednym miejscu, `elements/common/critique/prepare.md`, bez kopii jej treści. | skill or instruction file: `elements/common/critique/prepare.md` | Questions to settle, pytanie 3; przyjęte przez doradcę dnia w imieniu Mariusza, 2026-11-25: „Wiersz 2 tabeli ustaleń […] — przyjmuję.” | czy dopisać punkt do `check.md`, czy zmienić wejście krytyka; czy wymóg zapisać w każdym miejscu, które wysyła krytyka, czy raz |

## Out of scope

- Dokumenty zadań loop2 i jego plan — zadanie ich nie zmienia.
