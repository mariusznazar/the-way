---
title: "the way: zadanie zbiorcze z uwag PR-ów — skille wytycznych kodu, testów i styleguide'u"
status: draft
created: 2026-11-07
updated: 2026-11-07
tags: [zadanie]
related: "the author's project note on the process of work on a product"
---

# the way: zadanie zbiorcze z uwag PR-ów — skille wytycznych kodu, testów i styleguide'u

Status: ready for cycle
Project relation: independent

## Description

### Need

- Pierwszy przegląd fundamentu the way (2026-11-06/07) znalazł w opisach scalonych PR-ów 26 niezałatanych uwag o skillach wytycznych kodu, testów i styleguide'u, ich szablonach i wspólnym audycie, które dalej stoją.
- Agent prowadzący z Mariuszem doprecyzowanie wytycznych produktu dostaje w tych tekstach reguły sprzeczne między sobą albo z decyzjami the way, odesłania do złego kroku i pytania w złym miejscu rozmowy; skutek: zgaduje, pyta Mariusza o rzeczy już ustalone albo przepuszcza sprawę, której żaden skill nie domyka.
- Odbiorcą jest agent doprecyzowania i cyklu w produkcie, który używa the way (dziś `loop2`), oraz Mariusz, który odpowiada na pytania tych skilli.

### To do

Skill styleguide'u (`product-guidelines/styleguide/`):

1. Zdanie skilla o tym, że nowe znaczenie dociera do kodu „only through the task document”, mówi też o drugiej drodze, którą daje WAY-172: zatwierdzeniu przy zablokowanym szkicu requestu, gdy dokument zadania znaczenia nie ustala (theway#025-23; `SKILL.md:39`).
2. Audyt ekranów sam sprawdza, co widać bez danych, prosto z linku i po odświeżeniu, zamiast pytać o to człowieka przy każdym ekranie (theway#025-28; `audit.md:10`).
3. Skill styleguide'u i skill kodu wskazują `research.md`, `new_tools.md` i `staged_cleaning.md` wprost z kroku w `SKILL.md`, jeden poziom w głąb, a nie przez inny plik obok skilla (theway#060-2; `styleguide/starting_rules.md:9-10`, `styleguide/settle.md:6-7`, `:37-38`, `coding/SKILL.md:108`; zasada: `instruction-files/SKILL.md:174`).

Skill wytycznych kodu (`product-guidelines/coding/`):

4. Rozmowa o stałych sprawdzeniach ustala z człowiekiem także wersję narzędzia każdego z nich, bo dokument zadania każe autorowi zainstalować narzędzie „at the version … the task settles” (theway#026-1; `settle.md:16-25` wobec `task_document.md:11-13`).
5. Gdy człowiek wybierze inne narzędzie albo inny zestaw reguł niż ten, który przeszedł próbne uruchomienie, podział reguł na blokujące i przykłady opiera się na próbnym uruchomieniu wybranego zestawu, bo WAY-204 wywodzi podział z próby „of the set” (theway#026-20; `trial_run.md:5-14`, `settle.md`).
6. Na drodze „A new kind” w produkcie z wytycznymi kodu skill rozstrzyga i sprawdza tylko te stałe sprawdzenia, których nowy rodzaj kodu dotyka, a nie każde od nowa; nowy rodzaj w języku, którego żadne stałe sprawdzenie produktu nie czyta, robi z zadania rozszerzenie wytycznych (WAY-251), z researchem i próbnym uruchomieniem (theway#064-1; `settle.md:17-18`, `hand_back.md:3-4`, `task_document.md:11`; rekomendacja autora cyklu PR #64; WAY-216: pierwszy plik rodzaju „takes no … research of the standing checks”; Mariusz, 2026-11-07, pytanie kontrolne do wiersza 5 *Settlements to record*).
7. Sprawdzenie odświeżenia w kroku 1 nazywa wymagane nagłówki reguł o awariach i logach i mówi, że stoją w `template.md` skilla, a krok 1 `SKILL.md` każe ten plik przeczytać (theway#066-1; `recognize.md:27-32`, `SKILL.md:97-99`).
8. Produkt, którego wytyczne kodu mają przy regule o awariach i logach nagłówek z `none —`, nie dostaje pytania o te reguły od nowa także przy rozszerzeniu i przy pierwszych wytycznych — tak jak dziś przy odświeżeniu (theway#066-2; `settle.md:31`, `hand_back.md:9` wobec `recognize.md:28` i WAY-278).
9. W szablonie kodu (`template.md`):
   - reguła `### Identifiers in log lines` nie niesie uzasadnienia („since that handler usually does not know what the case was”), bo ten sam szablon i WAY-168 mówią, że reguła uzasadnienia nie niesie (theway#066-3; `:200` wobec `:182-183`);
   - przy `### Logging scope` dopisanie identyfikatora, który wskazuje osobę, wymaga zgody człowieka i nie jest nową decyzją produktu, jak mówi WAY-274 („The list stands in a rule, so adding an item changes no decision”) i jak mówi to sam szablon w drodze 1 odstępstw (theway#066-5; `:213-215` wobec `:246-248`);
   - linia `Personal data: none — <PREFIX-NN>` drogi 2 odstępstw jest polem reguły `### Secrets and personal data`, które dodaje szablon kodu, więc zostaje po angielsku jako nazwa pola według WAY-171, bez zmiany tej decyzji (theway#066-4; `:250-256`; pytanie 2);
   - wiersz tabeli odstępstw dla `### Secrets and personal data` w całości wymienia wśród tego, co odpada, także zawężenie `### Identifiers in log lines`, które WAY-276 dziś daje (theway#066-8; `:273`);
   - reguły, które zostają po odstępstwie od `### Recording a failure`, zachowują znaczenie każdego słowa, które z niej biorą — awarii i spodziewanej odmowy przy `### Hiding a failure` — a wiersz tabeli odstępstw mówi to wprost zamiast „nothing else” (theway#066-6; `:275`; Mariusz, 2026-11-07, propozycja A).

Skill wytycznych testów (`product-guidelines/testing/`):

10. `new_level.md` mówi, że droga nowego poziomu dokłada wzorzec do przepisu poziomu, który już stoi z pustym *Exemplar*, zgodnie z `recognize.md:21-23` i `product-guidelines/reading.md:78`; poziom bez przepisu jest rozszerzeniem (WAY-251) (theway#062-2; `new_level.md:3-4`).
11. Wskazanie kroku 2 w `SKILL.md` wymienia też produkt bez testów, któremu `recognize.md:18-19` ten krok daje (theway#062-3; `SKILL.md:90-91`).
12. Zdanie „A choice found in the product's tests is a proposal, never a rule” dociera na każdą drogę produktu, który ma testy, droga nowego poziomu włącznie (theway#062-4; dziś tylko `audit.md:21`).
13. W zadaniu, które rozszerza wytyczne testów i zarazem robi pierwszy test poziomu ze stojącym przepisem, „no step 2” dotyczy tylko tego poziomu, a rozszerzenie dalej idzie przez krok 2 (theway#062-7; `recognize.md:21-25`).
14. WAY-240 mówi, że przy nazwach poziomów testów ma pierwszeństwo przed WAY-95: poziom nazwany w produkcie inaczej niż w branży, także węziej, zawsze dostaje hasło słownika; `settle.md:8-10` i `template.md:110-113` skilla testów mówią to samo (theway#075-3; pytanie 1).

Wspólne czytanie wytycznych i wspólny audyt (`product-guidelines/`, `project-level/task/skill/`):

15. Doprecyzowanie zadania, którego wymaganym wynikiem jest pierwszy test poziomu, którego wytyczne testów jeszcze nie nazywają, kieruje to zadanie do `maintain-testing-guidelines` jako rozszerzenie wytycznych (WAY-251), a nie przepuszcza go do cyklu (theway#042-2; `product-guidelines/reading.md:77-82`, `project-level/task/skill/guideline_findings.md:38-42`).
16. `guideline_findings.md` odsyła po zasady zapisu zadania w backlogu do `read_sources.md`, a nie do „step 1's document conventions”, bo agent czyta ten plik też z kroku 5 skilla wytycznych, którego krok 1 to `recognize.md` (theway#070-2; `guideline_findings.md:14`, `:51-52`).
17. We wspólnym zadaniu wytycznych kodu i testów audyt, który sprawdza, czy ma się zatrzymać, bierze z kroku 1 drugiego skilla tylko jego tryb, więc pytanie o reguły awarii i logów nie trafia do człowieka w środku audytu testów (theway#070-3; `product-guidelines/audit_end.md:52`, `testing/SKILL.md:99-101`, `coding/recognize.md:27-32`).
18. We wspólnym zadaniu wytycznych kodu i testów, gdy po zatrzymaniu jednego audytu drugi audyt w tym zadaniu już nie ruszy, bo człowiek rozdzielił pracę, skill zatrzymanego audytu wraca i domyka listę przyczyn tak, jak audyt, który biegnie ostatni — numer, czołówka, sprawdzenie (theway#070-1; `product-guidelines/audit_end.md:57-59`, `coding/hand_back.md:18-22`, `testing/hand_back.md:10-14`; Mariusz, 2026-11-07, propozycja B).
19. We wspólnym zadaniu wytycznych kodu i testów skill, którego audyt się skończył, oddaje pracę do kroku 3 `refine-task`, a nie do kroku 4, dopóki skill drugiej dyscypliny nie poprowadził swoich spraw — także wtedy, gdy druga dyscyplina nie ma audytu (droga jednego rodzaju kodu, nowy poziom testów) (theway#070-8; `coding/hand_back.md:18-24`, `testing/hand_back.md:10-16`, `product-guidelines/audit_end.md:52-56`; Mariusz, 2026-11-07, propozycja C).

Skill plików instrukcji (`instruction-files/`):

20. `judging.md` mówi, że fragment, który przy ocenie idzie w kilka miejsc, dostaje w tabeli wiersz na każdą część, każdy z jednym z czterech werdyktów, i że każda propozycja dodania albo zmiany reguły stoi w tabeli we własnym wierszu (theway#062-6, #064-3, #069-10; pytanie 3).

### Questions to settle

- Pytanie 1: która reguła wygrywa przy poziomie testów nazwanym w produkcie węziej niż w branży — WAY-240 (taki poziom zawsze dostaje hasło słownika) czy WAY-95 (węższe znaczenie dostaje hasło tylko tam, gdzie zdanie da się przeczytać źle)?
  - Answer: WAY-240 wygrywa przy nazwach poziomów testów, a WAY-240 dostaje zdanie o pierwszeństwie przed WAY-95. Słaby punkt przyjęty z tą drogą: słownik dostaje hasło dla każdego takiego poziomu, także gdy żadne zdanie nie myli czytelnika; w zamian każdy poziom ma jedną definicję, bo WAY-240 odrzuca definicję poziomu w tabeli poziomów („each level defined in the guidelines' own table — a second definition beside the glossary, and the two drift apart”).
  - Not chosen:
    - WAY-240 zawężona do reguły WAY-95 — agent ocenia przy każdym poziomie, czy zdanie myli; poziom bez hasła zostaje bez żadnej definicji, a spór o „integration”, dla którego WAY-240 powstała, wraca.
    - zostawić jak jest — pierwszy cykl piszący wytyczne testów trafia na dwie reguły bez pierwszeństwa (WAY-25), co kosztuje blokującą uwagę i rundę poprawek.
  - Source: Mariusz, 2026-11-07: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-240 `foundations/decisions.md:6962`, WAY-95 `:2051`, `foundations` `f447bb6`.
- Pytanie 2: w jakim języku stoi etykieta `Personal data:` w wytycznych kodu pisanych po polsku — szablon kodu każe zostawić ją po angielsku, a WAY-171 zamyka listę tego, co zostaje po angielsku, i tej etykiety na niej nie ma (theway#066-4; `coding/template.md:254-255` wobec WAY-171)?
  - Answer: szablon kodu nazywa `Personal data` polem reguły `### Secrets and personal data`, które sam dodaje (WAY-171 pozwala szablonowi dyscypliny dodawać „at the places that template names”), a nazwy pól zostają po angielsku według WAY-171; decyzja się nie zmienia. Słaby punkt przyjęty z tą drogą: jedna reguła ma pole, którego inne nie mają, i to pole pojawia się tylko przy odstępstwie.
  - Not chosen:
    - WAY-171 dopisuje tę linię do listy tego, co zostaje po angielsku — decyzja o formie wszystkich plików wytycznych dostaje wyjątek dla jednej etykiety jednego szablonu, a każda następna taka etykieta znów ją zmienia.
    - etykieta idzie za językiem produktu, a szablon usuwa swoje zdanie — recenzent nie porówna linii z szablonem dosłownie, musi ją rozpoznać po znaczeniu.
    - zostawić jak jest — pierwszy produkt, który odejdzie od zakazu i pisze wytyczne po polsku, dostaje dwie sprzeczne reguły, a dwa cykle mogą rozstrzygnąć to różnie.
  - Source: Mariusz, 2026-11-07: „b” — na drogę b przedstawioną w rozmowie doprecyzowania; `product-guidelines/coding/template.md:254`, WAY-171 `foundations/decisions.md:4884`, `foundations` `f447bb6`; fraza `Personal data` występuje w repozytorium tylko w szablonie kodu (grep, 2026-11-07).
- Pytanie 3: czy zadanie poprawia `instruction-files/judging.md`, skoro oceny w trzech kolejnych przebudowach skilli (PR #62, #64, #69) odeszły od formatu, który ten plik daje?
  - Answer: tak — `judging.md` dostaje dwie rzeczy, których brakuje: fragment idący w kilka miejsc ma wiersz na każdą część z jednym z czterech werdyktów, a każda propozycja dodania albo zmiany reguły stoi w tabeli we własnym wierszu; kolejności sekcji, którą plik już podaje wprost, zadanie nie rusza. Słaby punkt przyjęty z tą drogą: dwa zdania więcej w pliku czytanym przy każdej ocenie, a odejście od kolejności zostaje bez zmiany.
  - Not chosen:
    - zostawić — raporty ocen są tymczasowe, ale kolejne przebudowy skilli (seria 10/11) najpewniej powtórzą te same odchyłki, a recenzent znów zgłosi je jako uwagi.
    - skrypt sprawdzający kształt oceny — łapie też kolejność, ale to nowy skrypt z testami dla raportu, który żyje jeden cykl.
  - Source: Mariusz, 2026-11-07: „b” — na drogę b przedstawioną w rozmowie doprecyzowania; `instruction-files/judging.md:11-26`, `foundations` `f447bb6`; raporty ocen w historii gita: `15b041a:docs/task-cycles/testing-skill-shape/reports/assessment.md` i `e0c2141:docs/task-cycles/coding-skill-shape/reports/assessment.md` (sprzeczności przed tabelą, werdykt `SPLIT`, sekcja „Proposals (not applied)”), `c5eb5fc:docs/task-cycles/plan-project-skill-shape/reports/assessment.md` (sekcja „Proposals that change the meaning of a rule (not applied)”).
- Pytanie 4: czy zadanie czeka na własne wytyczne kodowania i testów the way, skoro repozytorium the-way nie ma `guidelines/`, a WAY-215 trzyma zadanie piszące kod albo testy w produkcie bez wytycznych w doprecyzowaniu?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way, a rozjazd reguły z praktyką zostaje w zadaniu the task note on the-way's own guidelines in the author's backlog.
  - Not chosen:
    - czekać na zadanie o wytycznych the way — to zadanie nie ma jeszcze kierunku, więc poprawki stałyby bez terminu, a agenci w `loop2` dalej czytaliby sprzeczne teksty.
  - Source: Mariusz, 2026-11-07: „nie czeka” — na propozycję agenta powtarzającą odpowiedź z `the note of the task on the review of the foundation, in the author's backlog:93` (Mariusz, 2026-11-06: „nadal jedziemy bez tego”); WAY-215 `foundations/decisions.md:6102`, `foundations` `f447bb6`.

## Context

- Zadanie zbiera drobne poprawki w jedno zadanie zamiast osobnych, jak Mariusz ustalił dla uwag z przeglądu (zadanie przeglądu fundamentu, pytanie 12).
- Źródło uwag: `the author's note with the remarks from the pull requests of the review`, sekcja „Zadanie 6 (the way): zbiorcze — skille wytycznych” — przy każdej uwadze słowa recenzenta, miejsce i stan sprawdzony 2026-11-06 na `foundations` `e0a71f4`.
- Katalogi `product-guidelines/`, `project-level/task/` i `instruction-files/` nie zmieniły się od `e0a71f4` do `f447bb6` (`git diff --stat`, 2026-11-07), więc stan z pliku źródłowego dalej obowiązuje; numery linii przesuwają się z każdą zmianą — cykl szuka miejsca po treści.
- Trzy uwagi oceniono w przeglądzie jako „nic” (theway#062-6, #064-3, #069-10): dotyczą raportów ocen, które zostały tylko w historii gita (`15b041a`, `e0c2141`, `c5eb5fc`); krytyka przeglądu zauważyła, że to ten sam rodzaj odejścia od formatu oceny w trzech kolejnych cyklach — kolejność sekcji, werdykt `SPLIT` spoza czterech, propozycje bez własnych wierszy — stąd pytanie 3.
- Repozytorium the-way nie ma własnych wytycznych kodowania ani testów; czy ich potrzebuje, rozstrzyga osobne zadanie the task note on the-way's own guidelines in the author's backlog (pytanie 4).
- Uwagi theway#062-2 i #064-1 przegląd oznaczył jako wymagające zgody człowieka; punkty 10 i 6 *To do* opierają się na tekstach i decyzjach, które już stoją (`recognize.md`, `reading.md`, WAY-216), a przyjęcie całego dokumentu jest tą zgodą.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Cytaty z `foundations/decisions.md`, `foundations` `f447bb6`; numer linii to nagłówek decyzji.

- WAY-95 — Which words take a glossary entry? (`:2051`): „A word takes a glossary entry when it means, in the product, something other than a reader who knows the product's field takes it to mean; a word the product uses more narrowly than the field takes an entry only where a reader who takes the field's meaning would read a sentence of the product's English files wrongly.” Przy nazwach poziomów testów ustępuje WAY-240 (pytanie 1).
- WAY-240 — How do a product's testing guidelines name its test levels? (`:6962`): „The template of the testing discipline requires that a product's testing guidelines name its test levels, each with the product's decision that sets it, and that a level whose name means in the product something other than in the field, "integration" above all, is a term of the product's glossary, defined by the resources a test of that level may touch, such as files, the network or a browser.” Zadanie dopisuje jej pierwszeństwo przed WAY-95 (punkt 14 *To do*).
- WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it? (`:4770`): „A binding rule of a product's guidelines names by identifier the decision of the product's log that carries its choice and says what to do and how, and may give a use that follows it and one that breaks it, each in one line, while its reasons and rejected options stand in that decision alone […].” Podstawa punktu 9 (reguła bez uzasadnienia).
- WAY-171 — What form does a file of a product's guidelines take? (`:4884`): „Every file of a product's guidelines holds […] the sections `## When to read`, `## Rules`, `## Examples` and `## Where in code`, with what the template of its discipline adds at the places that template names […]. The headings, header lines, field names, values of closed lists and the marker `none —` stay in English while the rest of the text is in the language the product writes its guidelines in.” Podstawa odpowiedzi na pytanie 2.
- WAY-172 — How is a new or changed meaning of a product's guidelines approved? (`:4928`): „A new or changed meaning of a product's guidelines is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it, as WAY-30 has a change to a decision approved, or, where that document does not settle it, at a blocked draft request on whose branch the cycle proposes the decision.” Podstawa punktu 1.
- WAY-204 — How are the rules of a linter's set split between the rules that block and the examples? (`:5669`): „The skill `maintain-coding-guidelines` proposes which rules of a linter's set block and which stand among the examples from a trial run of the set on the product's code […]. The human approves that split in the product's decision adopting the set […].” Podstawa punktu 5.
- WAY-215 — What happens to a task that needs missing discipline guidelines? (`:6102`): „Unless a departure under WAY-217 applies, a task changing a user interface with no styleguide, writing code in a product with no general coding guidelines or writing or changing a test in a product with no testing guidelines […] stays in refinement as `waiting for human` with a *Questions to settle* question awaiting the merge of a separate guidelines task […].” Pytanie 4.
- WAY-216 — What does refinement assign to a task creating an unindexed kind of code? (`:6146`): „Neither a kind's first file nor that comparison alone makes a task an extension under WAY-251 or takes research of the standing checks; the comparison covers that kind alone, takes no trial run of a linter's set and is no audit under WAY-201.” Podstawa punktu 6.
- WAY-242 — How is the exemplar test of a level designated? (`:7039`): „That designation is approved in a task's refinement only where the task's required outcome is itself a test of that level, its document naming the level and that the task's first test of it becomes the exemplar, with no list of tests and no path […]. Until a decision designates it, the field of the exemplar in the level's recipe stands empty […].” Podstawa punktów 10 i 15.
- WAY-247 — May one task write a product's coding and testing guidelines together? (`:7205`): „One task of a product may write both its coding guidelines and its testing guidelines, the skill of each discipline leading that discipline's matters in the task's refinement.” Podstawa punktów 17–19.
- WAY-251 — What distinguishes a refresh from an extension of guidelines? (`:7332`): „[…] a refresh updates or corrects accepted guidelines within the scope they already cover […]. An extension covers something new […].” Podstawa punktów 10, 13 i 15.
- WAY-256 — Where does a fragment of a skill stand? (`:7503`): „[…] that only one step or one variant of the skill needs stands in a file beside the skill that the step names […].” Podstawa punktu 3, razem z zasadą `instruction-files/SKILL.md:174` („A step of a route points directly and one level deep”).
- WAY-272 — What counts as a failure, and where is it written? (`:8172`): „The template of the coding discipline holds that a failure is a situation in which the product did not do what it was asked to do or what it was to do on its own, for a reason other than an expected refusal […].” Podstawa punktu 9 (odstępstwo od `### Recording a failure`).
- WAY-274 — Where does a product's logging scope stand, and who adds to it? (`:8244`): „An agent adds an item that fits the principle, any identifier of a thing included, in the change that brings it, and the human sees it at the merge. Whatever points to a person, an email, a name, a telephone number, a home address and an IP address among them, takes the human's consent […].” *Rationale:* „The list stands in a rule, so adding an item changes no decision (WAY-30) […].” Podstawa punktu 9 (zgoda zamiast nowej decyzji).
- WAY-276 — What do a product's logs not hold? (`:8331`): „[…] an identifier on that list that is a secret stays out of a line, this rule prevailing over WAY-275.” Podstawa punktu 9 (wiersz `### Secrets and personal data`).
- WAY-278 — How do the rules on failures and logs reach a product that has coding guidelines? (`:8409`): „A refresh that finds them missing proposes them: the human's yes makes the task an extension, and the human's no is a departure with its reason.” Podstawa punktu 8.
- WAY-282 — In what order do the causes of an audit of the skills of guidelines stand? (`:8560`): „A task joining a product's coding and testing guidelines has one list and one order, made at the end of the audit that runs last […].” Podstawa punktu 18.

## Settlements to record

Candidates: 9 shown, 5 accepted — 2026-11-07

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Przy nazwach poziomów testów WAY-240 ma pierwszeństwo przed WAY-95: poziom nazwany w produkcie inaczej niż w branży, także węziej, zawsze dostaje hasło słownika. | decision | pytanie 1 | czy zawęzić WAY-240 do reguły WAY-95, czy tylko poprawić szablon testów bez zapisu pierwszeństwa |
| 2 | Linia `Personal data: none — <PREFIX-NN>` przy odstępstwie od zakazu danych osobowych jest polem reguły `### Secrets and personal data`, które dodaje szablon kodu, i jako nazwa pola zostaje po angielsku. | decision | pytanie 2; pytanie kontrolne 2026-11-07 (anchor: WAY-171 „each rule of `## Rules` stands under a heading of its own with the fields *Decision*, *Invariant*, *Good* and *Bad*” obok „with what the template of its discipline adds at the places that template names”): Mariusz, „tak” — na rekomendację agenta, by wybór został, bo WAY-171 sama pozwala szablonowi dyscypliny dodawać; nie wybrane: etykieta na liście WAY-171 — decyzja o formie wszystkich wytycznych dostaje wyjątek dla jednej linii jednego szablonu | czy wybór zapisać w decyzji (z odrzuconymi drogami), czy tylko w szablonie; czy dopisać etykietę do listy WAY-171 |
| 3 | W ocenie plików instrukcji fragment, który idzie w kilka miejsc, dostaje wiersz na każdą część z jednym z czterech werdyktów, a każda propozycja dodania albo zmiany reguły stoi w tabeli we własnym wierszu. | decision | pytanie 3 | czy zmienić decyzję o tabeli oceny (WAY-257), czy tylko `judging.md` |
| 4 | We wspólnym zadaniu wytycznych kodu i testów, gdy drugi audyt w tym zadaniu już nie ruszy, bo człowiek rozdzielił pracę, listę przyczyn domyka zatrzymany audyt, tak jak audyt, który biegnie ostatni. | decision | punkt 18 *To do*; Mariusz, 2026-11-07, propozycja B: „przyjmuję zgodnie z propozycjami”; pytanie kontrolne 2026-11-07 (anchor: WAY-282 „A task joining a product's coding and testing guidelines has one list and one order, made at the end of the audit that runs last”): Mariusz, „tak” — na rekomendację agenta, by wybór został, bo po rozdzieleniu nie ma wspólnego zadania, a utrata scalania przyczyn obu dyscyplin jest ceną rozdzielenia; nie wybrane: lista czeka na audyt w drugim zadaniu — przyczyny jednego zadania wędrują do innego, a pierwsze idzie do cyklu z listą bez kolejności | czy WAY-282 zmienia się o ten przypadek |
| 5 | Na drodze nowego rodzaju kodu w produkcie z wytycznymi kodu skill rozstrzyga i sprawdza tylko te stałe sprawdzenia, których nowy rodzaj dotyka; rodzaj w języku, którego żadne stałe sprawdzenie produktu nie czyta, robi z zadania rozszerzenie wytycznych (WAY-251). | decision | punkt 6 *To do* (rekomendacja autora PR #64); pytanie kontrolne 2026-11-07 (anchor: WAY-202 „They bind a product from the task that writes its coding guidelines, which is complete only once it holds, for each of the three standing checks, a decision of the product's log adopting it or departing from it”): Mariusz, „tak” — na wariant c agenta, zmieniający obie strony; nie wybrane: tylko sprawdzenia, których rodzaj dotyka, bez wyjątku dla nowego języka — narzędzie wybierane na drodze bez researchu narzędzi (WAY-216); żadnych stałych sprawdzeń, jak WAY-216 czytany dosłownie — skrypt w nowym języku wchodzi bez lintera | czy nowy rodzaj rozstrzyga od nowa wszystkie trzy stałe sprawdzenia, jak czytany wprost WAY-202, i co z rodzajem w nowym języku |

## Out of scope

- Uwagi o cyklu zadania, kroku technologii, brzmieniu decyzji i README — zadanie 7 tego samego przeglądu.
- Uwagi z listy „Zostawić” pliku źródłowego.
