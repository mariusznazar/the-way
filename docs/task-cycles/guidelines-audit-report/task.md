---
title: "the way: audyt w skillach wytycznych podaje wagę każdego ustalenia i kolejność naprawy"
status: draft
created: 2026-10-29T23:55
updated: 2026-11-01
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: audyt w skillach wytycznych podaje wagę każdego ustalenia i kolejność naprawy

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skille wytycznych the way — dla kodu, ekranów i testów — przy zakładaniu, odświeżaniu i rozszerzaniu wytycznych produktu przeglądają jego istniejący kod, ekrany albo testy i kończą ten audyt ustaleniami z plikiem i linią.
- Ustalenia nie mają wagi ani wspólnej przyczyny, więc nie wiadomo, które naprawić najpierw ani które pochodzą z jednego źródła.
- Audyt ekranów i audyt testów kończą się trzema do pięciu zarzutami, a nic nie mówi, według czego agent je wybiera (`product-guidelines/styleguide/audit.md:14`, `product-guidelines/testing/audit.md:10`, `foundations` `2f51e6c`).
- Audyt kodu nie ma limitu i przy każdym pliku `do not copy` podaje miejsce, ale nie skutek (`product-guidelines/coding/kinds.md:15-16`, tamże).
- Mariusz zgłasza, że sam ocenia, co jest pilne, a agent, który planuje naprawy, układa je bez podstawy.
- Mariusz zgłasza, że przy krótkiej liście nic złego się nie dzieje, a przy długiej rośnie ryzyko, że pierwsze w kolejce będą drobiazgi, a krytyczne ustalenie utonie w środku.

### To do

1. Audyt w skillach `maintain-coding-guidelines`, `maintain-styleguide` i `maintain-testing-guidelines` daje wagę każdej przyczynie, także takiej, która powstała z jednego ustalenia, na skali z opisem, co znaczy każdy stopień, mierzoną skutkiem dla użytkownika albo właściciela produktu, nie wielkością naruszenia; skalę z pytania 2 opisuje raz plik wspólny dla trzech skilli.
2. Audyt scala ustalenia w przyczyny: kilka naruszeń z jednego źródła to jedna przyczyna i jedna naprawa, a każde ustalenie należy do jednej przyczyny; spis przyczyn obejmuje też granicę zaufania bez testu odmowy i reguły lintera łamane z jednego powodu, opisane skutkiem, z liczbą plików, bez nazw reguł (pytanie 5).
3. Przyczyna niesie miejsca, w których zachodzi: plik i linię, przy regułach lintera liczbę plików, a przy granicy zaufania jej nazwę; kategorie audytu ekranów z WAY-187 zostają przy przyczynie.
4. Audyt kończy się kolejnością naprawy: od przyczyn krytycznych w dół, a przy równym stopniu pierwsza stoi naprawa, po której znika najwięcej problemu za najmniejszą pracę (pytanie 7).
5. Każda przyczyna, która trafia na górę listy, jest sprawdzona: prowadzący audyt wraca do miejsc, które wskazuje, i sprawdza, czy opisany skutek naprawdę zachodzi; to, co się nie potwierdzi, obniża albo wycofuje, a przy każdej sprawdzonej przyczynie zapisuje, że ją sprawdził; czego nie da się zobaczyć bez działającego produktu, zostaje oznaczone jako niesprawdzone (`product-guidelines/styleguide/audit.md:11-13`) (pytanie 6).
6. Audyt daje człowiekowi do decyzji górę listy, czyli początek kolejności: trzy do pięciu przyczyn na cały audyt, zawsze z wszystkimi krytycznymi, a gdy krytycznych jest ponad pięć, wchodzą wszystkie i nic więcej, gdy zaś przyczyn jest mniej niż trzy, wchodzą wszystkie; pełny spis, z wagą i miejscem w kolejności, stoi niżej w dokumencie zadania, a zadanie łączące kod i testy ma jedną listę i jedną kolejność (pytania 1 i 7).
7. Agent proponuje, które przyczyny z góry listy wchodzą do zadania, a które są odkładane, człowiek o tym decyduje, a przy odłożeniu przyczyny krytycznej agent pyta dodatkowo, czy założyć na nią osobne zadanie w backlogu; zgodę zamienia w zadanie tą drogą, którą `refine-task` daje zadaniu wstępnemu (`project-level/task/skill/guideline_findings.md:12-17`), więc przy zadaniu z planu projektu przez `plan change` (pytanie 3); przyczyny spod góry listy są odkładane razem, z powodem „poza górą listy”, chyba że człowiek weźmie którąś do zadania (pytanie 7).
8. Pliki `task_document.md` trzech skilli mówią, co z tego audytu trafia do dokumentu zadania: wagi, przyczyny z miejscami, kolejność i odłożone przyczyny.

### Questions to settle

- Pytanie 1: co ma się stać z limitem trzech do pięciu zarzutów, gdy audyt dostaje wagę i scalanie w przyczyny, skoro audyt kodu limitu nie ma, a zadanie mówi o wadze każdego ustalenia?
  - Answer: pełny spis zostaje w dokumencie, a limit obejmuje tylko to, co człowiek dostaje do decyzji: audyt ocenia i scala wszystko, człowiek dostaje na górze trzy do pięciu przyczyn na cały audyt, nie na poziom testów, zawsze z wszystkimi przyczynami najwyższego stopnia, a reszta stoi niżej w dokumencie zadania, z wagą i miejscem w kolejności; lista `do not copy` audytu kodu zostaje osobno, bo mówi następnemu agentowi, czego nie kopiować.
  - Not chosen:
    - twardy limit, który liczy przyczyny, a reszta to jedna linia: ile ich jest i jaki mają najwyższy stopień — najkrótsza i najtańsza droga, ale waga obejmuje tylko to, co się zmieściło, a treść reszty przepada, więc kolejność naprawy jest niepełna
    - bez limitu, człowiek rozstrzyga wszystkie przyczyny po kolei — nic nie ginie, ale wraca lista za długa, żeby ją zważyć, nawet po scaleniu, co WAY-250 odrzuciła
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: lżejsze przyczyny stoją w dokumencie, którego po zadaniu nikt nie otworzy; `product-guidelines/styleguide/audit.md:14`, `product-guidelines/testing/audit.md:10`, `product-guidelines/coding/kinds.md:15`, WAY-250, `foundations/decisions.md:7175`, `foundations` `2f51e6c`.
- Pytanie 2: jedna skala wagi dla trzech skilli czy własna dla każdej dyscypliny, i ile ma stopni?
  - Answer: jedna skala o czterech stopniach, opisana raz, w pliku wspólnym dla trzech skilli, z przykładem z każdej dyscypliny; stopień zależy od tego, co jest stawką, a nie od tego, ile miejsc łamie regułę:
    - krytyczna — realna sytuacja w działającym produkcie kończy się utratą danych albo pieniędzy, dostępem do cudzych danych albo niedziałaniem głównej rzeczy, po którą przychodzi użytkownik; tu należy też szkoda, o której nikt by się nie dowiedział;
    - wysoka — użytkownik nie kończy ważnej czynności albo dostaje nieprawdziwą informację; tu należy też problem, który właściciel widzi, ale nie potrafi ustalić jego przyczyny;
    - średnia — użytkownik da radę to obejść albo szkoda przychodzi z czasem: kolejne pliki kopiują zły wzorzec, a naprawa drożeje;
    - niska — dziś nie odczuwa tego ani użytkownik, ani właściciel.
  - Przykłady do pliku wspólnego: kod — endpoint czyta dane z żądania bez sprawdzenia i pozwala sięgnąć po cudze zamówienie, więc krytyczna, nawet jeśli to jeden plik; testy — test płatności przechodzi niezależnie od tego, co policzy kod, więc krytyczna, bo błąd dojdzie do klienta i nikt tego nie zauważy; ekrany — przycisk kasowania wygląda jak zwykły przycisk, więc wysoka, a czterdzieści źle wpisanych odstępów to niska.
  - Not chosen:
    - własna skala dla każdej dyscypliny — lepiej oddaje różnice między dyscyplinami, ale to trzy teksty do utrzymania, a gdy kod i testy są w jednym zadaniu, ich stopni nie da się porównać, więc wspólna kolejność naprawy nie ma podstawy
    - skala przeglądu zmiany (Critical, Important, Minor), bez nowych słów — nic nowego do nauczenia, ale tamta skala ocenia, czy zmianie można ufać, a nie skutek dla użytkownika, a stopień w audycie sugerowałby blokadę, której tu nie ma
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 i tekst stopni przedstawione w rozmowie doprecyzowania, ze wskazanym słabym punktem: tekst jest ogólny, więc to agent ocenia, jak poważna byłaby szkoda, a ekrany rzadko sięgną stopnia krytycznego, więc góra listy będzie częściej z kodu i testów; `task-cycle/review/SKILL.md:99-101`, `foundations` `2f51e6c`.
- Pytanie 3: czy waga rozstrzyga, co idzie do zadania, a co jest odkładane, czy tylko porządkuje listę?
  - Answer: waga proponuje, człowiek rozstrzyga: agent proponuje, które przyczyny z góry listy wchodzą do zadania, a które są odkładane, i pokazuje to razem z wagami; decyzja należy do człowieka, a przy odłożeniu przyczyny krytycznej agent pyta dodatkowo, czy założyć na nią osobne zadanie w backlogu.
  - Not chosen:
    - waga rozstrzyga sama: wszystko krytyczne wchodzi do zadania, reszta jest odkładana — mniej do rozstrzygania, ale naprawa krytycznej przyczyny bywa duża, więc zadanie o wytycznych puchnie, a tego WAY-205 chciała uniknąć
    - waga tylko porządkuje listę, a człowiek odkłada sam, bez dodatkowego pytania — najmniej zmian w skillach, ale odłożona krytyczna kończy tak samo jak dziś, a problem z początku zadania wraca, tylko później
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: człowiek może odpowiedzieć „nie” i krytyczna dalej zostanie w dokumencie, a nic nie zmusi do powrotu; `product-guidelines/testing/audit.md:13`, `product-guidelines/styleguide/audit.md:16`, `product-guidelines/coding/task_document.md:43`, WAY-205, `foundations/decisions.md:5598`, `foundations` `2f51e6c`.
- Pytanie 4: czy zmiana ma wejść przed przebudową tych trzech skilli, czy po niej?
  - Answer: po niej, i to już jest stan repozytorium: przebudowy skilli ekranów, testów i kodu są scalone, więc zmiana wchodzi raz.
  - Source: `foundations` `2f51e6c`, commity `802b56d` (PR #60), `d024d56` (PR #62), `097123e` (PR #64).
- Pytanie 5: które wyniki audytu wchodzą do spisu przyczyn i na skalę, skoro audyt testów mówi też o granicach zaufania, a audyt kodu liczy pliki łamiące reguły lintera?
  - Answer: oba wyniki wchodzą do spisu: granica zaufania bez testu odmowy to przyczyna z wagą, a reguły lintera łamane z jednego powodu to jedna przyczyna opisana skutkiem, z liczbą plików, bez nazw reguł; to, co te wyniki uruchamiają dziś, zostaje bez zmian; ponowne formatowanie kodu nie jest ustaleniem, bo to jednorazowa czynność.
  - Not chosen:
    - tylko granice zaufania, a linter zostaje liczbą obok — krótszy spis, ale kolejność naprawy nie widzi najszerszego długu w kodzie, czyli miejsca, gdzie jedna naprawa często zamyka najwięcej
    - żaden z nich, na skalę idą tylko zarzuty i `do not copy` — najmniej zmian, ale góra listy może pominąć brak testu na granicy zaufania
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: drobne reguły lintera mogą rozdmuchać dolną część spisu, choć na górę listy nie trafią; `product-guidelines/testing/audit.md:15`, `product-guidelines/coding/trial_run.md:17`, WAY-201, `foundations/decisions.md:5404`, `foundations` `2f51e6c`.
- Pytanie 6: co znaczy „prowadzący audyt sprawdza sam w kodzie” i które ustalenia to obejmuje, skoro audyt the way prowadzi jeden agent, bez agentów pomocniczych?
  - Answer: powrót do kodu z konkretnym zadaniem: dla wszystkich przyczyn z góry listy, a więc i wszystkich krytycznych, prowadzący audyt wraca do wskazanych linii i przechodzi drogę od wejścia do szkody, sprawdzając, czy to, co opisuje, naprawdę tak zachodzi; to, co się nie potwierdzi, obniża albo wycofuje, a przy każdej sprawdzonej przyczynie zapisuje, że ją sprawdził; dzieje się to tak samo, gdyby audyt robił agent pomocniczy.
  - Not chosen:
    - sprawdza świeży agent, jak przy próbnym przebiegu lintera — prawdziwa niezależność, ale to zmienia „sam” z pierwotnego zadania, dokłada jednego agenta do każdego audytu, a krytyka i tak idzie po nim
    - sprawdzenie tylko wtedy, gdy audyt robiły agenty pomocnicze, dosłownie jak w kursie — dziś nic nie kosztuje, bo reguła w ogóle nie zadziała, a zdanie z zadania zostaje bez skutku
  - Source: Mariusz, 2026-11-01: „wziąłbym 1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: autor dalej sprawdza własny wniosek, a niezależność daje dopiero krytyka świeżego agenta; `product-guidelines/coding/settle.md:96`, `product-guidelines/coding/trial_run.md:11`, `foundations` `2f51e6c`.
  - Doprecyzowane po krytyce: „droga od wejścia do szkody” pasuje do kodu, a nie do ekranów i testów, więc To do 5 mówi: sprawdza, czy opisany skutek naprawdę zachodzi.
- Pytanie 7: jak ułożona jest kolejność naprawy, skoro „ile problemu znika na jednostkę pracy” dosłownie pozwala taniej przyczynie niskiej wyprzedzić drogą krytyczną, i czym wypełnia się góra listy?
  - Answer: najpierw stopień, w obrębie stopnia zysk na jednostkę pracy: kolejność idzie od przyczyn krytycznych w dół, a przy równym stopniu pierwsza stoi naprawa, po której znika najwięcej problemu za najmniejszą pracę; góra listy to początek tej kolejności: wszystkie krytyczne, dopełnione do trzech do pięciu, a gdy krytycznych jest ponad pięć, wchodzą wszystkie i nic więcej, gdy zaś przyczyn jest mniej niż trzy, wchodzą wszystkie; przyczyny spod góry są odkładane razem, z powodem „poza górą listy”, chyba że człowiek weźmie którąś do zadania; zadanie łączące kod i testy ma jedną listę i jedną kolejność.
  - Not chosen:
    - dosłownie zysk na jednostkę pracy, bez względu na stopień — najszybciej ubywa problemów w sumie, ale wraca obawa o drobiazgi w kolejce, a agent musiałby przeliczać stopnie na liczby, czego skala nie daje
    - krytyczne pierwsze, cała reszta dosłownie według zysku — kolejność pozostaje prosta u góry, a niżej liczy się zysk, ale tania niska może wyprzedzić wysoką, która blokuje użytkownikowi ważną czynność
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: tania naprawa usuwająca trzydzieści niskich problemów czeka za drogą krytyczną; notatka zadania, sekcje „Po co to” i „Co zmienić”.
- Pytanie 8: czy audyt staje się osobnym skillem uruchamianym okresowo?
  - Answer: nie: wagę, scalanie i kolejność audyt przejmuje ze skilla audytu obserwowalności z kursu, a dalej biegnie w skillach wytycznych.
  - Not chosen:
    - audyt jako osobny skill uruchamiany okresowo — logowanie ma trzymać wytyczna na kodzie dotykanym w zmianie, a przegląd całości robi audyt przy rozszerzeniu wytycznych
  - Source: Mariusz, notatka zadania z 2026-10-30, sekcja „Co zmienić”: „Mariusz przejął z niego wagę, scalanie i kolejność (wiersz 15 mapy), a odrzucił sam audyt jako osobny skill uruchamiany okresowo: logowanie ma trzymać wytyczna na kodzie dotykanym w zmianie, a przegląd całości robi audyt przy rozszerzeniu wytycznych.”
- Pytanie 9: gdzie stoi odłożony cykliczny przegląd wszystkich wytycznych z warunkiem powrotu, skoro decyzja the way nie może nieść warunku swojego przeglądu (WAY-24)?
  - Answer: bez wpisu do fundamentu: odłożenie z warunkiem powrotu stoi w backlogu, jako otwarty wątek zadania o przeglądzie zasad produktu, gdzie rozstrzyga się też, czy wyzwalacz obejmuje wytyczne.
  - Not chosen:
    - decyzja bez warunku powrotu: audyt biegnie tylko przy założeniu, odświeżeniu i rozszerzeniu — reguła jest wyraźna, ale dubluje odrzucenie z pytania 8 i wymaga zmiany decyzji, gdy tamto zadanie wprowadzi przegląd, a powód z pierwotnego zadania i tak odpada
    - tylko w tym dokumencie, w sekcji z kontekstem — nic nie trzeba dopisywać, ale po zamknięciu zadania nikt do tego nie wróci
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: warunek dalej może nigdy nie zadziałać, a przypomnienie działa tylko wtedy, gdy ktoś weźmie tamto zadanie; WAY-24, `foundations/decisions.md:595`, WAY-26, `foundations/decisions.md:643`, `elements/decisions/template.md:53-55`, `task-cycle/review/SKILL.md:57`, `foundations` `2f51e6c`.

## Context

- Audyt dalej biegnie przy założeniu, odświeżeniu i rozszerzeniu wytycznych.
- Porównanie jednego rodzaju kodu i pierwszy test nowego poziomu nie są audytem, więc nie dostają tego zakończenia (WAY-216; `product-guidelines/testing/SKILL.md:98`).
- Audyty leżą dziś w `product-guidelines/coding/kinds.md` z `trial_run.md`, `product-guidelines/styleguide/audit.md` i `product-guidelines/testing/audit.md`, a to, co z nich trafia do dokumentu zadania, w `task_document.md` obok każdego z nich (`foundations` `2f51e6c`).
- Skala i kolejność stoją w tym dokumencie w całości, a decyzja the way opisuje przejęty wzór własnymi słowami (WAY-27), więc cykl nie potrzebuje skilla z kursu.

## Questions carried to cycle

- Jakimi angielskimi słowami skala nazywa cztery stopnie, skoro nazwy muszą różnić się od Critical, Important i Minor przeglądu zmiany, żeby jedno słowo nie miało w the way dwóch znaczeń (pytanie 2).
- Jak audyt pokazuje koszt naprawy, na którym stoi kolejność z To do 4, tak żeby człowiek widział, skąd ta kolejność.
- Jakimi angielskimi słowami skille nazywają ustalenie audytu i przyczynę, skoro przegląd zmiany używa już słowa „finding”, a audyty ekranów i testów słowa „charge”.
- Czy ustalenia z *Settlements to record* wchodzą jako jedna nowa decyzja wspólna dla trzech skilli, która zawęża WAY-187, WAY-201 i WAY-250, czy jako zmiany tych decyzji, skoro decyzja mieści się w jednym do trzech zdań wiążących (`elements/decisions/template.md:25`).

## Human actions

none

## Decisions in play

Wybór: decyzje z *Scope* `product-guidelines` według „Reading the foundation”, wyszukanie słów „audit”, „charge” i „finding” w fundamencie i w `product-guidelines/`, oraz wpisy, do których te decyzje prowadzą, na `foundations` `2f51e6c`.

- WAY-187 — „ends with three to five charges, each with its file and line and one sentence of its effect on the user, in four categories: a missing design token, a missing shared component, accidental architecture, and a meaning, one colour carrying several.” Odpowiedź na pytanie 1 zmienia to brzmienie; koszt zmiany Mariusz przyjął przy tym pytaniu (WAY-30).
- WAY-201 — „ends with a proposed exemplar for each kind of code the product holds files of, each with one sentence of what the product gains by it, and with the files of that kind marked `do not copy`, each with the file and line of the place that breaks a rule.” Zostaje, a audyt dostaje spis przyczyn; zmiana jak przy WAY-187. Naruszeniem jest tam audyt, który „ends with the linter's reports listed by the names of their rules”, stąd brzmienie pytania 5.
- WAY-250 — „ends, for each level, with a proposed exemplar test, with one sentence of what the product gains by it, and three to five charges, each with its file and line and one sentence of its effect, and, for each trust boundary of the product's map, with whether a test of its refusal exists.” Limit na poziom testów przechodzi na cały audyt; zmiana jak przy WAY-187. *Rejected*: „every fault the audit found listed — a list too long to weigh.” Pełny spis z pytania 1 nie jest listą do ważenia, bo człowiek waży górę listy, ale *Rejected* trzeba przepisać razem ze zmianą.
- WAY-200 — „the skill `maintain-coding-guidelines` judges every one of them, compares them and proposes the exemplar from that comparison, with the status `copy` or `do not copy` of every other file”. Bez zmian: lista `do not copy` zostaje osobno.
- WAY-216 — „the comparison covers that kind alone, takes no trial run of a linter's set and is no audit under WAY-201.” Porównanie jednego rodzaju kodu nie jest więc audytem i nie dostaje tego zakończenia.
- WAY-204 — „The skill `maintain-coding-guidelines` proposes which rules of a linter's set block and which stand among the examples from a trial run of the set on the product's code”. Bez zmian: spis przyczyn korzysta z tego przebiegu.
- WAY-205 — „the skill `maintain-coding-guidelines` proposes the linter's invariant over the whole of that code, marked violated until the code is cleaned (WAY-51).” Bez zmian (pytanie 5). *Rejected*: „the whole of the code cleaned in the task that brings a linter — that task grows into cleaning the whole product.” Niesie granicę z pytania 3.
- WAY-51 — „an invariant is marked violated only by a change of the foundation that a human accepts, never by a step of implementation.” Bez zmian.
- WAY-235 — „a boundary that does not refuse today has that invariant marked violated as WAY-51 gives it”. Bez zmian: przyczyna z pytania 5 stoi obok tego niezmiennika.
- WAY-174 — „put to the human every choice they settle for a product's guidelines, a choice they recommend included, and show each in plain words”. Tak agent pokazuje przyczyny i propozycję z pytania 3.
- WAY-173 — „A decision of the-way on what such a template carries or what such a skill proposes binds the template and the skill, never a product's screens or code directly.” Skala wiąże więc skille, nie kod produktu.
- WAY-251 — „a refresh updates or corrects accepted guidelines within the scope they already cover”; „An extension covers something new”. Audyt biegnie przy nich jak dotąd.
- WAY-120 — „a completed set for collective human review goes through it”. Niezależność, której sprawdzenie z pytania 6 nie daje.
- WAY-161 — „a finding blocks when the reviewer grades it Critical or Important and has not itself marked it as outside the task's scope”; *Rejected*: „a second scale beside the grade”. Tamto odrzucenie dotyczy przeglądu zmiany; skala audytu mierzy co innego (pytanie 2) i nosi inne nazwy.
- WAY-256 — „text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did”. Dotyczy jednego skilla; plik wspólny trzech skilli ma wzór w `product-guidelines/reading.md`.
- WAY-100 — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” Niesie wiersz 1 poniżej.
- WAY-27 — „every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.” Decyzja opisuje przejęty wzór własnymi słowami.
- WAY-247 — „One task of a product may write both its coding guidelines and its testing guidelines, the skill of each discipline leading that discipline's matters in the task's refinement.” Przy takim zadaniu obowiązuje wspólna kolejność z pytania 2.
- WAY-24 — „A decision names no date or condition for its review, the log holds no record of a review, and the review of the foundation against the product is a task of the product's backlog.” Dotyczy pytania 9.
- WAY-26 — „What the product does not do only because no work has brought it yet is no non-goal: where later work builds on it, a decision states what the product does today.” Dotyczy pytania 9.
- WAY-30 — „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made”. Tak wchodzą zmiany WAY-187, WAY-201 i WAY-250.

## Settlements to record

Candidates: 8 shown, 6 accepted — 2026-11-01

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Audyt w trzech skillach wytycznych daje wagę każdej przyczynie na jednej skali czterech stopni, opisanej raz w pliku wspólnym, mierzonej skutkiem dla użytkownika albo właściciela produktu, nie wielkością naruszenia, a stopień zależy od tego, co jest stawką, nie od tego, ile miejsc łamie regułę; wagę, scalanie i kolejność the way przejmuje ze skilla audytu obserwowalności z kursu 10xDEVS, lekcja m3l5, a sam audyt nie staje się osobnym skillem. | decision | To do 1; pytania 2 i 8 (*Not chosen* obu niesie odrzucone drogi) | czy każdy skill ma własną skalę, czy czterdzieści drobnych naruszeń waży więcej niż jedno groźne i czy decyzja nazywa, co przejmuje (WAY-100) |
| 2 | Audyt scala ustalenia w przyczyny: kilka naruszeń z jednego źródła to jedna przyczyna i jedna naprawa, a przyczyna niesie miejsca, w których zachodzi; spis obejmuje też granicę zaufania bez testu odmowy i reguły lintera łamane z jednego powodu, opisane skutkiem, z liczbą plików, bez nazw reguł, a ponowne formatowanie kodu nie jest ustaleniem. | decision | To do 2 i 3; pytanie 5 | czy brak testu odmowy i wyniki lintera stoją poza spisem i czy przyczyna traci plik i linię |
| 3 | Audyt kończy się kolejnością naprawy: od przyczyn krytycznych w dół, a przy równym stopniu pierwsza stoi naprawa, po której znika najwięcej problemu za najmniejszą pracę; zadanie łączące kod i testy ma jedną listę i jedną kolejność. | decision | To do 4 i 6; pytanie 7 | czy tania przyczyna niska może wyprzedzić drogą krytyczną |
| 4 | Pełny spis zostaje w dokumencie zadania, a człowiek dostaje do decyzji górę listy, czyli początek kolejności: trzy do pięciu przyczyn na cały audyt, zawsze z wszystkimi krytycznymi, a gdy krytycznych jest ponad pięć, wszystkie i nic więcej, gdy zaś przyczyn jest mniej niż trzy, wszystkie; lista `do not copy` zostaje osobno. | decision | To do 6; pytania 1 i 7; zmienia WAY-187, WAY-201 i WAY-250 | czy limit dalej odcina ustalenia, czy obowiązuje na poziom testów i co robić przy sześciu krytycznych |
| 5 | Waga proponuje, człowiek rozstrzyga, które przyczyny z góry listy wchodzą do zadania; przy odłożeniu przyczyny krytycznej agent pyta dodatkowo, czy założyć na nią osobne zadanie w backlogu, a przyczyny spod góry są odkładane razem, z powodem „poza górą listy”, chyba że człowiek weźmie którąś do zadania. | decision | To do 7; pytania 3 i 7 | czy krytyczne wchodzą do zadania z automatu, czy odłożona krytyczna zostawia ślad i kto odkłada przyczyny spod góry |
| 6 | Każda przyczyna z góry listy, zanim trafi do człowieka, jest sprawdzona: prowadzący audyt wraca do miejsc, które wskazuje, i sprawdza, czy opisany skutek naprawdę zachodzi; to, co się nie potwierdzi, obniża albo wycofuje, a przy każdej sprawdzonej przyczynie zapisuje, że ją sprawdził. | decision | To do 5; pytanie 6 | czy przy jednym agencie sprawdzenie w ogóle się odbywa i co znaczy |

## Out of scope

- Zastosowanie nowego zakończenia audytu w konkretnym produkcie.
- Cykliczny przegląd wszystkich wytycznych na całym kodzie (pytanie 9).
