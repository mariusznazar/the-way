---
title: Doprecyzowanie zadania pyta o słowo, które da się zrozumieć na dwa sposoby, zanim agent wybierze sam
status: draft
created: 2026-10-25T16:00
updated: 2026-11-14
tags: [zadanie]
related: "the note of the project of the process of work on a product"
---

# Doprecyzowanie zadania pyta o słowo, które da się zrozumieć na dwa sposoby, zanim agent wybierze sam

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Gdy opis zadania używa słowa, które da się rozumieć na dwa sposoby, a różnica zmienia wymagany wynik, doprecyzowanie zadania nie ma kroku, który o to pyta.
- Krok „Resolve the gaps” skilla doprecyzowania pyta o brakujące i sprzeczne odpowiedzi, nie o słowa, które da się rozumieć dwojako.
- Rozjazd wychodzi dziś przypadkiem — przy krytyce wpisów fundamentu albo dopiero przy poprawce po PR — i wymaga cofnięcia się do wcześniejszych ustaleń.
- W zadaniu „Mag w lesie” w loop2 zdarzyło się to dwa razy: „widok” (rysunek planszy czy wszystkie ekrany przeglądarki) i „restart” (ponowne przejście mapy czy restart kontenera).
- Przy „widoku” Mariusz musiał otworzyć na nowo zatwierdzoną definicję projektu i jeszcze raz przejść kontrolę gotowości; przy „restarcie” rozjazd poprawiano po złożeniu PR, z osobnym przeglądem miejsc użycia słowa.
- Według rachunku programu usprawnień z 14 wierszy rejestru problemów, które kosztowały czas Mariusza, 8 to niejasność zadania rozstrzygnięta przez agenta.
- Bez zmiany słowo o dwóch znaczeniach może przejść do kodu i ujawnić się dopiero przy przeglądzie PR albo wcale.

### To do

1. Krok „Resolve the gaps” w `project-level/task/skill/resolve_gaps.md` dostaje sprawdzenie: agent szuka w dokumencie zadania i w zdaniach źródeł, na których zadanie opiera wymagany wynik — przytoczonych decyzjach fundamentu i zdaniach zatwierdzonej definicji projektu — słów, które dopuszczają różne wymagane zachowania, a których nie rozstrzyga zatwierdzone źródło: definicja projektu, wpis fundamentu, w tym wpis słownika pojęć, albo odpowiedź człowieka (pytania 1 i 4).
2. Przypadek liczy się tylko wtedy, gdy oba odczyty dopuszcza zdanie, które stoi w dokumencie zadania albo w źródle z punktu 1, i oba dają różny, obserwowalny wynik w zakresie zadania; odczyt, którego zdanie nie dopuszcza, i scenariusz spoza zakresu zadania się nie liczą (pytanie 2).
3. Dla takiego przypadku agent pokazuje krótki przykład z zakresu zadania („przy odczycie A dzieje się X, przy odczycie B — Y”) i pyta, który odczyt obowiązuje, jako pytanie o decyzję według „How a skill asks”; odpowiedź staje pod *Questions to settle*.
4. Sprawdzenie nie ma obowiązku znaleźć niejasności ani pokazać określonej liczby przypadków; gdy agent nic nie znajdzie, nic o sprawdzeniu nie mówi (pytanie 3).
5. Sekcja „## 3. Resolve the gaps” w `project-level/task/skill/SKILL.md` wymienia to sprawdzenie obok pytań i wyborów.

### Questions to settle

- 1. Które słowa agent sprawdza: tylko z dokumentu zadania, także ze zdań źródeł, na których zadanie opiera wymagany wynik, czy z całej definicji projektu i fundamentu?
  - Answer: słowa z dokumentu zadania i ze zdań źródeł, na których zadanie opiera wymagany wynik — przytoczonych decyzji fundamentu i zdań zatwierdzonej definicji projektu; niejasność w definicji wraca do definicji i jej bramki gotowości, jak dziś daje krok „Resolve the gaps”.
  - Not chosen:
    - tylko słowa z dokumentu zadania — przypadek „widoku” by przeszedł, bo stał w decyzji D-03 definicji, nie w opisie zadania; to połowa znanych przypadków.
    - cała definicja projektu i fundament — rytuał i zachęta do szukania przypadków spoza zadania, czyli tego, przed czym chroni przyjęta granica.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „1 b, 2 a, 3 a, 4 a, 5 a”.
- 2. Jaka granica chroni przed wymyślaniem przypadków na siłę?
  - Answer: przypadek pokazuje się tylko wtedy, gdy oba odczyty dopuszcza zdanie, które stoi w dokumencie zadania albo w źródle z pytania 1, i oba dają różny, obserwowalny wynik w zakresie zadania; odczyt, którego zdanie nie dopuszcza, i scenariusz spoza zakresu się nie liczą. To ta sama granica, którą ma mieć próba spisu decyzji (pytanie 5).
  - Not chosen:
    - sama zasada „bez obowiązku i bez liczby”, reszta na ocenę agenta — najkrócej, ale agent łatwo dorabia wiarygodne przypadki brzegowe; najsłabsza ochrona.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „1 b, 2 a, 3 a, 4 a, 5 a”.
- 3. Co agent mówi, gdy nie znajdzie słowa o dwóch odczytach?
  - Answer: nic; skuteczność widać w rejestrze problemów audytu (wiersze niejasności rozstrzygniętej przez agenta), nie w rozmowie.
  - Not chosen:
    - jedno zdanie „nie znalazłem słowa o dwóch odczytach zmieniających wynik” — widać, że sprawdzenie zaszło, ale z czasem robi się z tego rytuał i pokusa dopisania „ale może…”, czyli wymyślania przypadków tylnymi drzwiami.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „1 b, 2 a, 3 a, 4 a, 5 a”.
- 4. Jak sprawdzenie ma się do słownika pojęć w fundamencie produktu?
  - Answer: wpis słownika rozstrzyga odczyt i wtedy agent nie pyta — słowa procesu w słowniku the-way, słowa produktu w słowniku produktu; znaczenie rozstrzygnięte przez Mariusza, którego czytelnik dziedziny by nie nadał, trafia jako kandydat „glossary term” do *Settlements to record* dzisiejszą drogą WAY-95; w słowniku nic się nie zmienia.
  - Not chosen:
    - każde rozstrzygnięte znaczenie jako kandydat do słownika — słownik rósłby o słowa, których nikt nie myli; sprzeczne z WAY-95 i wymagałoby jej zmiany.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „1 b, 2 a, 3 a, 4 a, 5 a”.
- 5. Co z próbą spisu decyzji z oznaczeniem źródła (karta D8), która celuje w tę samą klasę problemów?
  - Answer: zostaje poza tym zadaniem jako osobne zadanie w backlogu projektu, ze wspólną granicą z pytania 2; to zadanie nie czeka na jej wynik.
  - Not chosen:
    - wstrzymać to zadanie do wyniku próby i zrobić jeden krok — jeden spójny krok zamiast dwóch, ale wdrożenie opóźnia się o co najmniej dwa doprecyzowania.
    - zrobić próbę teraz na tym dokumencie — wynik skażony, bo próba mierzy, ile „zgaduję” Mariusz rozstrzygnąłby inaczej, a odpowiadał za niego doradca dnia.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „1 b, 2 a, 3 a, 4 a, 5 a. Próbę D8 załóż jako [>] z datą 📅 2026-11-14.”

## Context

- Pomysł pochodzi z kursu 10xDEVS, lekcja m2l2, skill `10x-plan` krok 1.1.4: przed planowaniem sonduje się terminy, których prośba nie definiuje („top N”, „najnowszy”, „aktywny”), najmniejszym przypadkiem, w którym dwa odczyty dają różny wynik.
- Werdykt „przejmuję” i przyjęty zakres w słowach Mariusza stoją w the author's map of the 10xDEVS package, sekcja „m2l2”, wiersz „Sondowanie terminów, których prośba nie definiuje”: „agent sprawdza różne wymagane zachowania dopuszczone przez opis i nierozstrzygnięte w zatwierdzonych ustaleniach. Gdy różnica wpływa na wymagany wynik zadania, pokazuje krótki przypadek w jego zakresie i pyta o rozstrzygnięcie. Bez obowiązku znalezienia niejasności lub określonej liczby przypadków; Mariusz zaakceptował ten zakres z ochroną przed wymyślaniem przypadków brzegowych na siłę”.
- Przy „widoku” rozjazd dotyczył decyzji D-03 definicji projektu loop2, nie samego opisu zadania; zmianę zatwierdzonej definicji krok „Resolve the gaps” już dziś kieruje do definicji i jej bramki gotowości (WAY-118).
- Granica z pytania 2 bierze wzór z testu WAY-99, który rozpoznaje słowo o dwóch znaczeniach po zdaniu stojącym w plikach, nie po zdaniu wymyślonym na potrzeby testu.
- Rachunek „8 z 14” pochodzi z sekcji 3 the author's note on the improvements of the-way; w rejestrze problemów większość tych wierszy to zadanie milczące o czymś („the task did not say…”), a nie słowo o dwóch odczytach — tę szerszą klasę bada próba spisu decyzji (karta D8 w the author's note on practices from a course for AI tech leaders), przyjęta jako dopisek do tego zadania 12.11.2026.
- W trybie z orkiestratorem projektu każde pytanie doprecyzowania idzie przez plik rozmowy (`project-level/task/skill/orchestrated_mode.md`), więc nowe pytanie trafia tam bez osobnej zmiany.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-100 — When does a method or practice borrowed from elsewhere bind a product? „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness to a method or practice no decision has adopted, it asks a human before treating it as a rule.” Sprawdzenie pochodzi z kursu 10xDEVS, więc wiąże dopiero przez decyzję z wiersza 1 *Settlements to record*.
- WAY-113 — How does an agent of the-way ask a human decision? „An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel.”
- WAY-95 — Which words take a glossary entry? „A word takes a glossary entry when it means, in the product, something other than a reader who knows the product's field takes it to mean; a word the product uses more narrowly than the field takes an entry only where a reader who takes the field's meaning would read a sentence of the product's English files wrongly.”
- WAY-99 — How does one word keep one meaning in the foundation? „Two uses of a word in the English text of the files git tracks carry two meanings when a sentence those files hold is true in the meaning of one use and false in the meaning of the other, whichever of the two the sentence uses, and a sentence made up for the test does not count; […]”
- WAY-118 — What makes a project definition ready for breakdown? „A change to those sections after approval goes through the gate again before breakdown relies on it.”

## Settlements to record

Candidates: 2 shown, 1 accepted — 2026-11-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Doprecyzowanie zadania przejmuje z kursu 10xDEVS (m2l2, `10x-plan`) sondowanie słów: gdy zdanie dokumentu zadania albo źródła, na którym zadanie opiera wymagany wynik, dopuszcza dwa odczyty dające różny obserwowalny wynik w zakresie zadania, a nie rozstrzyga ich zatwierdzone źródło ani wpis słownika, agent pokazuje przypadek i pyta, który odczyt obowiązuje — bez obowiązku znalezienia niejasności, bez liczby przypadków i bez słowa, gdy nic nie znajdzie. | decision | pytania 1–4 (wybór człowieka) i werdykt „przejmuję” w the author's map of the 10xDEVS package, wiersz „Sondowanie terminów…” | jak szeroko sięga sprawdzenie, czy zdanie o przypadku musi stać w źródle i co agent mówi przy braku niejasności, a także czy w ogóle pisać decyzję o przejęciu praktyki |

## Out of scope

- Próba spisu decyzji z oznaczeniem źródła (karta D8) — osobne zadanie w backlogu projektu.
