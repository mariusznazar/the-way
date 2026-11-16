---
title: "the way: przegląd zmiany łapie kod, który obchodzi test, a autor zatrzymuje się, gdy test przeczy wymaganiu"
status: draft
created: 2026-10-24
updated: 2026-11-14
tags: [the-way, zadanie]
related: ["the project note of the process of working on a product"]
---

## Po co to

- **Jak jest dziś:** Agent piszący kod, który nie umie przejść testu, może wpisać na sztywno wynik dla tego jednego wejścia, które sprawdza test — test świeci na zielono, a funkcja dla innych wejść dalej nie działa. Gdy test przeczy wymaganiu zadania, agent dopasowuje kod albo test, zamiast się zatrzymać, a przegląd zmiany nie ma polecenia, żeby szukać takich obejść.
- **Kto to odczuwa:** Mariusz, który scala PR na podstawie zielonych testów i nie czyta kodu — dostaje zmianę, która wygląda na sprawdzoną, a nie działa; skutek wychodzi dopiero u użytkownika produktu albo przy kolejnym zadaniu.
- **Co jeśli nic:** W źródłach nie ma przypadku z cykli Mariusza — na razie hipotetyczny; zewnętrzne badania (karta systemowa Claude 3.7 Sonnet, ImpossibleBench) pokazują, że modele tak robią, więc może się to pojawić przy pierwszym zadaniu, w którym agent utknie na czerwonym teście.


# the way: przegląd zmiany łapie kod, który obchodzi test, a autor zatrzymuje się, gdy test przeczy wymaganiu

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Agent, który pisze kod i nie może przejść czerwonego testu, potrafi „zaliczyć” test bez naprawienia problemu: wpisuje w kod oczekiwaną wartość dla tego jednego wejścia, którego używa test (np. „jeśli wejście to 200 zł, zwróć 180 zł”), zamiast napisać ogólną regułę. Test świeci na zielono, a produkt dalej nie działa dla innych wejść.
- Drugi wariant tego samego problemu: test i wymaganie zadania sobie przeczą (np. test oczekuje wartości, której wymaganie nie dopuszcza). Agent nie ma dziś w the way wyraźnej drogi „zatrzymaj się i oddaj sprawę człowiekowi”, więc dopasowuje kod albo test, żeby było zielono.
- Zadanie o przewodniku testów (the way: testy jako osobna dyscyplina wytycznych produktu) łapie tylko jedną stronę: zmianę samego testu (osłabienie, usunięcie, zmianę oczekiwanej wartości bez przyczyny). Nie łapie kodu, który oszukuje przy nietkniętym teście, bo to nie jest reguła o treści pliku testu, tylko o tym, jak agent pracuje i co sprawdza recenzent — czyli o procesie the way, nie o wytycznych produktu.
- Odbiorcą jest recenzent zmiany w cyklu zadania (agent, który nie robił zmiany) i autor zmiany; pośrednio Mariusz, który scala PR i nie czyta kodu.

### To do

1. Recenzent zmiany (`task-cycle/review/SKILL.md`, sekcja „2. Review”, obok punktu „The tests: do they fail when the behaviour they protect breaks […]”, około linii 84) szuka w zmianie kodu produktu, który przechodzi test, nie spełniając wymagania: rozgałęzienia albo zwracanej wartości pod konkretne wejście, którego używa test; wartości oczekiwanej testu wpisanej na sztywno w kod produktu; komentarza w rodzaju „specjalny przypadek dla testu”; zmiany, która zmienia wynik porównania w teście bez zmiany samego testu (np. przeciążony operator porównania). Taki kod jest znaleziskiem, które blokuje, w każdym przeglądzie zmiany — kawałka planu, całej zmiany, poprawki i korekty.
2. Autor zmiany (`task-cycle/change/SKILL.md`, sekcje „2. Tests” i „6. Commit and report”) ma jawne wyjście, gdy test przeczy wymaganiu zadania albo gdy nie umie przejść testu kodem ogólnym: nie pisze kodu pod wejście testu i nie zmienia testu, tylko commituje to, co ma, i wraca do orkiestratora z pytaniem, które nazywa test, cytuje wymaganie i mówi, co próbował. Test, który sprawdza zachowanie, jakie zadanie wprost zmienia, nie jest sprzecznością: autor zmienia go z przyczyną po stronie wymagania, jak dziś.
3. Orkiestrator cyklu (`task-cycle/skill/SKILL.md`, akapit „An agent that returns `questions` gets your answers as step 6 answers the designer's […]”, około linii 263) odpowiada na takie pytanie tylko ze źródła — zadania, specyfikacji, decyzji albo zdania niezmiennika. Gdy żadne nie rozstrzyga, nie wybiera „najmniejszego odwracalnego odczytania”, tylko otwiera zablokowany szkic PR-a, z pytaniem w sekcji decyzji człowieka. Wykonawca części planu, który zwraca takie pytanie, nie dostaje ponowienia z wyższą klasą modelu (`task-cycle/skill/SKILL.md`, krok 9, podkrok 4, około linii 396): silniejszy model nie usunie sprzeczności, a ponowienie kasuje pracę części; gdy żadne źródło nie rozstrzyga, orkiestrator od razu otwiera zablokowany szkic.
4. Szablon opisu PR-a (`task-cycle/skill/request_template.md`) dostaje miejsce na taki zablokowany szkic: w grupie „Needed from you” rodzaj 2 („Questions”) dopuszcza dziś tylko pytania kroku fundamentu i wybór zastrzeżony, a tabela wariantów (około linii 500) nie ma wiersza dla sprzeczności testu z wymaganiem. Nowy wiersz niesie to samo pytanie co pytanie autora (test, cytat wymagania, co autor próbował); jego pozostałą treść autor zmiany układa na wzór sąsiednich wierszy, np. „A reserved choice” i „A blocking finding remains” (`task-cycle/skill/blocked_finding.md`).
5. Ustalenie z karty systemowej Claude 3.7 Sonnet (rozdział 6, cytowane w *Context*) zapisuje się w fundamencie jako wpis faktu środowiska (`foundations/environment_facts.md`, WAY-90), a decyzje z *Settlements to record* 1 i 2 powołują się w *Based on* na ten wpis i na istniejący `impossiblebench-test-modification`, zamiast cytować kartę w uzasadnieniu. Liczby ImpossibleBench (54% → 9%, trzy z czterech strategii) wchodzą do wpisów dopiero po sprawdzeniu w PDF (arXiv 2510.20270).

### Questions to settle

- Czy oba punkty wchodzą do kroków autora i recenzenta (`task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`), czy do szablonu przewodnika testów jako reguły, które produkt przyjmuje decyzją?
  - Answer: Do skilli autora i recenzenta zmiany — reguła działa w każdym cyklu, w produktach i w samym the way.
  - Not chosen:
    - reguła w szablonie przewodnika testów — działa tylko w produkcie, który przyjął przewodnik, nie w the way (WAY-328), a nie jest regułą o treści pliku testu, bo test zostaje nietknięty, a oszukuje kod
    - zostawić jak jest — dziś nic nie kosztuje (zero przypadków w 83 cyklach), ale pierwszy przypadek przejdzie przez przegląd niezauważony
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a — do skilli autora i recenzenta”
- Czy „sprzeczność testu z wymaganiem” to nowy powód zwrotu bez kodu obok dwóch dzisiejszych (nierozstrzygnięty wybór, zmiana za duża), i kto ją rozstrzyga — orkiestrator cyklu czy człowiek przy zablokowanym PR-ze?
  - Answer: Autor zatrzymuje się i pyta orkiestratora cyklu. Orkiestrator odpowiada tylko wtedy, gdy sprawę rozstrzyga źródło — zadanie, specyfikacja, decyzja albo zdanie niezmiennika; gdy żadne źródło nie rozstrzyga, nie wybiera odczytania sam, tylko otwiera zablokowany szkic PR-a z pytaniem do człowieka. Wykonawca części planu nie dostaje przy takim pytaniu ponowienia z wyższą klasą modelu.
  - Not chosen:
    - nowy, trzeci powód zwrotu bez kodu — praca autora idzie do kosza, a autor specyfikacji też nie rozstrzygnie wymagania, bo pyta orkiestratora, nigdy człowieka: ten sam problem, drożej
    - od razu zablokowany PR, bez orkiestratora — każda sprzeczność, także oczywista, którą zadanie już rozstrzyga, zatrzymuje cykl i zabiera człowiekowi turę
    - zostawić jak jest („napisz w raporcie, pracuj dalej”) — dziś nic nie kosztuje, ale autor bez wyjścia dopasowuje kod albo test; według ImpossibleBench samo wyjście „zgłoś człowiekowi” obniżyło odsetek oszustw GPT-5 z 54% do 9% (liczby do sprawdzenia w PDF)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 a […] — wg Twoich rekomendacji”; zawężenie źródeł do czterech i brak ponowienia wykonawcy części — Mariusz osobiście, 2026-11-14: „1a”, „4 dopiszmy”
- Czy wyjście autora obejmuje też test, którego autor nie umie przejść kodem ogólnym, choć sprzeczności z wymaganiem nie widzi?
  - Answer: Tak — oba przypadki idą tą samą drogą: pytanie do orkiestratora, a gdy źródło nie rozstrzyga, zablokowany PR z pytaniem do człowieka.
  - Not chosen:
    - tylko jawna sprzeczność — autor, który utknął bez widocznej sprzeczności, a to z tego rodzi się kod pod jedno wejście, dalej nie ma innego wyjścia niż obejście
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 a […] — wg Twoich rekomendacji”
- Czy próba „nowy test czerwony na kodzie sprzed zmiany” (dopisek z 12.11.2026) wchodzi do tego zadania?
  - Answer: Nie — idzie jako osobne zadanie próby w produkcie gry, linia w backlogu Loop bez daty.
  - Not chosen:
    - stały krok cyklu w tym zadaniu — wymaga polecenia zadeklarowanego przez każdy produkt (WAY-38) i zostawia nierozwiązany test, który pada na brakującym module zamiast na asercji, przy trzech takich przypadkach w 83 cyklach, wszystkich bez kosztu; do tego nie łapie kodu z wartością na sztywno, który przed zmianą pada, a po niej przechodzi tak samo jak kod uczciwy
    - porzucić — dziś nic nie kosztuje, ale odrzuca próbę przyjętą 12.11.2026
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „4 a — wg Twoich rekomendacji. Przy 4 a: osobne zadanie próby w produkcie gry dopisz jako linię zadania w backlogu Loop (bez daty)”

## Context

- Skąd ten temat: research do zadania o przewodniku testów (`research_wytyczne_testow/raport_wytyczne_testow.md`, sekcja 8) znalazł dwie luki procesu, które nie są regułami przewodnika; w doprecyzowaniu tamtego zadania odłożone do osobnego zadania (jego sekcja *Out of scope*).
- Dowód, że to się dzieje — karta systemowa Claude 3.7 Sonnet, rozdział 6 (cytat dokładny, `raport_wytyczne_testow.md`, sekcja 3): „Most often this takes the form of directly returning expected test values rather than implementing general solutions, but also includes modifying the problematic tests themselves to match the code's output.” Ta sama karta zaleca obserwować: „Excessive edit / test-execution cycles on a single file - Comments that suggest test-specific handling - Unexpected modifications to test files”.
- Prośba „nie oszukuj” prawie nie działa — METR: prośby w rodzaju „Please do not cheat” miały „a nearly negligible effect on reward hacking” (`raport_wytyczne_testow.md`, sekcja 3).
- Wyjście „oddaj człowiekowi” działa — ImpossibleBench: możliwość przerwania i zgłoszenia człowiekowi obniżyła odsetek oszustw GPT-5 z 54% do 9%; według tego samego źródła trzy z czterech strategii oszukiwania omijają zakaz edycji testów, więc sama ochrona plików testów nie wystarcza. Obie liczby to parafraza narzędzia pobierającego strony — przed użyciem sprawdzić w PDF (arXiv 2510.20270).
- Co the way ma dziś (stan `foundations` `f4af75d`):
  - autor, sekcja „2. Tests” w `task-cycle/change/SKILL.md`, punkt „Never weaken an assertion, skip a test or relax a lint rule to make a check pass” (około linii 88) — zakaz ruszania testu, nic o kodzie, który oszukuje;
  - autor, sekcja „1. Read” tego pliku, akapit „When a value in the task, spec or plan does not pass your own reckoning […] say so in your report instead of bending the code to it” (około linii 47) — tylko „powiedz w raporcie”, praca idzie dalej;
  - zwrot bez kodu tylko w dwóch przypadkach: wybór, którego zadanie nie rozstrzyga, i zmiana za duża — sekcja „5. When you return without code”, akapit „Return a report that holds no code and no diff, with the status `returned`” (około linii 121);
  - recenzent, sekcja „2. Review” w `task-cycle/review/SKILL.md`, punkt „The tests: do they fail when the behaviour they protect breaks, and pass for a reason other than the code computing its own expected value?” (około linii 84) — łapie test, który sam liczy oczekiwaną wartość, nie kod, który ją zwraca na sztywno;
  - szablon przewodnika testów produktu (`product-guidelines/testing/template.md`) ma już reguły „Where the expected value comes from” (WAY-232) i „Changing an existing test” (WAY-233) — strona testu jest zamknięta, a the way we własnym kodzie od przewodnika testów odstępuje (WAY-328);
  - fundament ma już fakt środowiska `impossiblebench-test-modification` (ImpossibleBench, § 4.2: „OpenAI models perform special-casing most of the time, while Claude models and Qwen3-Coder mostly modify the test cases”; § 5.2: tryb tylko-do-odczytu testów „does not eliminate other cheating methods such as special-casing or operator overloading”), na którym stoi WAY-03.
- Próba „nowy test czerwony na kodzie sprzed zmiany” (dopisek przyjęty 12.11.2026, sprawa 10 w notatka autora z rozstrzygnięciami; karty karta D4 notatki autora z praktykami z kursu i karta D15 notatki autora z praktykami z kursu; sam skrypt w the way: kroki „sprawdź sam” w prośbie, wskazywanie miejsc w zadaniu nagłówkiem, przegląd fundamentu pyta o koniec stanu przejściowego) wyszła z tego zadania do backlogu Loop (pytanie 4); rejestr problemów 2026-11-12 ma trzy wiersze o czerwonym przebiegu nowego testu w 83 cyklach, wszystkie o koszcie „nic”.
- Liczby z lekcji 14 kursu AI Tech Leaders: z poprawek uznanych za rozwiązane około 8% psuło inne testy tego samego repozytorium, a około 11% było po prostu złych; test napisany przez autora poprawki sprawdza to, co autor myślał, że naprawia (sekcja U4 w notatka autora z praktykami z kursu AI Tech Leaders).
- Związek z the way: testy jako osobna dyscyplina wytycznych produktu: tamto zadanie dało regułę „zmiana istniejącego testu wymaga przyczyny” (WAY-233, łapie przerabianie testu); to zadanie łapie przerabianie kodu pod test. Razem zamykają obie drogi do fałszywej zieleni.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-03** — „Any change may alter an invariant test, in any step of its task, implementation included. A change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request, so that the agent reviewing the change and the human merging it see it.” — strona testu; zadanie jej nie zmienia, dokłada stronę kodu.
- **WAY-13** — „Every change, whatever its size, passes the product's tests and a review by an agent that did not make it.” — przegląd, któremu zadanie daje nowe pytanie.
- **WAY-69** — „An invariant's sentence, its test and the code the test covers may come from one agent; the agent reviewing the change, which made none of it, reads the test against the sentence.”
- **WAY-100** — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” — sygnały kodu ustawionego pod test pochodzą z karty systemowej Claude 3.7 Sonnet i z ImpossibleBench, więc wiążą przez decyzję.
- **WAY-135** — „A task's cycle writes a spec, reviewed by an agent other than its author, before implementation and any plan where the task leaves an open design choice and nowhere else […]. An agent that meets an open design choice while it makes the change returns a report that holds no code, the attempt is discarded […]” — zadanie nie dodaje tu trzeciego powodu zwrotu (pytanie 2).
- **WAY-136** — „[…] an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change.” — jak wyżej.
- **WAY-164** — „Before its work goes to review, the author of a one-author change names the requirement of the task, and the executor of each slice the requirement of its slice read against the passages of the task its handoff gives, that its work most likely does not meet, writes a check that would catch that, and states in its report which requirement, which check and what the check showed.”
- **WAY-227** — „The orchestrator of a task cycle answers the agents' questions and gives provisional go-aheads under the task owner's delegation, never recording these as human approval, and brings the request to the human, the cycle's first point of human review. Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request.” — zadanie dokłada sprawę zastrzeżoną dla człowieka: sprzeczność testu z wymaganiem, której nie rozstrzyga żadne źródło.
- **WAY-90** — „[…] once the environment facts element has entries, it names instead a fact entry, by its identifier alone, for every citation that, once it stopped being true, would call the decision into question — a finding about agents or models, the behaviour of a tool the process uses.” — karta systemowa Claude 3.7 Sonnet jest ustaleniem o modelach, więc dostaje wpis faktu (*To do* 5).
- **WAY-229** — „An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check […] gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class that fails, or a retry that fails, stops the cycle.” — zadanie wyłącza to ponowienie dla wykonawcy, który zwraca pytanie o sprzeczność testu z wymaganiem (*To do* 3).

## Settlements to record

Candidates: 4 shown, 2 accepted — 2026-11-14

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Recenzent każdej zmiany szuka kodu produktu, który przechodzi test bez spełnienia wymagania — rozgałęzienia albo wartości pod wejście testu, oczekiwanej wartości testu wpisanej na sztywno, komentarza „specjalny przypadek dla testu”, zmiany wyniku porównania bez zmiany testu — i taki kod blokuje; reguła stoi w skillu recenzenta, nie w szablonie przewodnika testów. | decision | *Questions to settle*, pytanie 1 (wybór spośród pokazanych dróg, *Not chosen* tam); *To do* 1 | czy sygnały zapisać tylko jako zdania skilla bez decyzji (wbrew WAY-100), i czy taki kod jest znaleziskiem blokującym czy uwagą |
| 2 | Gdy test przeczy wymaganiu zadania albo autor nie umie go przejść kodem ogólnym, autor nie obchodzi testu, tylko pyta orkiestratora; orkiestrator odpowiada tylko ze źródła — zadania, specyfikacji, decyzji albo zdania niezmiennika — a gdy żadne nie rozstrzyga, otwiera zablokowany szkic PR-a z pytaniem do człowieka; wykonawca części planu nie dostaje przy takim pytaniu ponowienia z wyższą klasą modelu (zawęża regułę ponowienia z WAY-229). | decision | *Questions to settle*, pytania 2 i 3 (wybór spośród pokazanych dróg, *Not chosen* tam); *To do* 2 i 3; Mariusz osobiście, 2026-11-14: „1a”, „4 dopiszmy” | czy to trzeci powód zwrotu bez kodu z odrzuceniem próby, czy orkiestrator przy milczeniu źródeł wybiera „najmniejsze odwracalne odczytanie” jak przy innych pytaniach, i czy wykonawca części dostaje przy takim pytaniu ponowienie z wyższą klasą modelu |

## Out of scope

- Próba „nowy test czerwony na kodzie sprzed zmiany” — osobne zadanie próby w produkcie gry, w backlogu Loop (pytanie 4).
