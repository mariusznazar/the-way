---
title: Wyłapywać zbyt duże zadania przed oddaniem planu projektu Mariuszowi
status: draft
created: 2026-10-25T16:00
updated: 2026-11-14
tags: [zadanie]
related: "notatka projektu procesu pracy nad produktem"
---

# Wyłapywać zbyt duże zadania przed oddaniem planu projektu Mariuszowi

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- W planie pierwszej wersji gry loop2 jedno zadanie („konta-graczy-i-logowanie”) zebrało zakładanie kont, logowanie, blokowanie kont, potwierdzanie adresu, reset hasła i wysyłkę poczty — osiem z czternastu pytań otwartych definicji projektu.
- Ani skrypt sprawdzający plan, ani niezależna krytyka planu nie wskazały jego wielkości; Mariusz zauważył ją sam przy oddaniu planu i uruchomił poprawkę, w której agent podzielił zadanie na cztery, każde kończące się czymś sprawdzalnym na serwerze testowym.
- Krok cięcia planu na zadania mówi tylko „A large task is split; its size chooses nothing else (WAY-13)” i nie podaje, po czym poznać duże zadanie.
- Polecenie dla krytyka planu wymienia cztery rzeczy do oceny i wielkości zadania wśród nich nie ma; decyzja WAY-146 wylicza te same cztery.
- Skrypt sprawdzający plan (`project-level/plan_check.py`) sprawdza formę i strukturę planu, a nie to, ile pracy skupia jedno zadanie.
- Co jeśli nic: przy kolejnym planie wychwycenie zbyt dużego zadania nadal spada na Mariusza; źródła dokumentują jeden taki przypadek, już poprawiony w loop2, i nie ustalono, czy spowodował opóźnienie albo błąd w produkcie.

### To do

1. Krok cięcia planu na zadania (`project-level/plan/skill/cut_tasks.md`, punkt zaczynający się od „Cut the definition's In scope into tasks”) podaje, po czym autor planu rozpoznaje zadanie do podziału: zadanie jest za duże, gdy jego cel łączy dwa albo więcej efektów, z których każdy da się osobno sprawdzić w działającym produkcie i scalić przed pozostałymi; sygnałem do przyjrzenia się jest zadanie, które zbiera wyraźnie więcej pytań otwartych definicji, wpisów rzutowanych albo pozycji In scope niż pozostałe zadania planu. Kryterium nie ma progu liczbowego.
2. Polecenie dla krytyka planu (`project-level/plan/skill/critique_plan.md`, zdanie zaczynające się od „Ask it to judge, besides what that skill checks”) prosi także o ocenę wielkości każdego zadania według kryterium z punktu 1.
3. Zadanie, które krytyk wskaże jako za duże, idzie do człowieka jako pytanie przed oddaniem planu, z podziałem i z wariantem „zostawić”; autor planu nie dzieli go sam z powodu wielkości. Krok krytyki (`project-level/plan/skill/critique_plan.md`, punkt zaczynający się od „Verify each observation”, który dziś odsyła do człowieka poprawkę zmieniającą odpowiedź człowieka albo zadanie zapisujące wpis) mówi to wprost.
4. Decyzja WAY-146 zmieniona w miejscu (WAY-07): jej zdanie wiążące wymienia ocenę wielkości zadania według kryterium z punktu 1 wśród tego, co ocenia krytyka planu, i mówi, że podział z powodu wielkości rozstrzyga człowiek; *Verification* dostaje przykład zgodności i naruszenia opisany słowami, bez odsyłania do prywatnych notatek (WAY-27); *Rejected* dostaje oba warianty nie wybrane pod pytaniem 2.

### Acceptance criteria

- Kryterium z punktu 1, przyłożone do dawnego celu zadania o kontach w loop2 (konta, logowanie, blokada konta, potwierdzenie adresu, reset hasła i poczta; osiem z czternastu pytań definicji), wskazuje je jako za duże, a przyłożone do zadania o jednym sprawdzalnym efekcie, takiego jak „właściciel blokuje konto gracza, a zablokowany gracz traci sesję i nie może się zalogować”, nie wskazuje.

### Questions to settle

- Czy pomiar z dopisku z 12.11.2026 (rozmiar dokumentu zadania i rozmiar scalonej zmiany zestawione z liczbą problemów w cyklu) wchodzi w to zadanie?
  - Answer: Nie — zadanie zmienia tylko instrukcję planu projektu; dopisek zostaje w *Context* jako tło.
  - Not chosen:
    - pomiar teraz, przed ustaleniem kryterium — około godziny pracy agenta na skrypty od nowa, a rozmiar dokumentu zadania i scalonej zmiany powstaje dopiero po planie, więc nie da progu, którego autor planu mógłby użyć
    - zadanie zwracające tylko wiedzę (sam pomiar), zmiana instrukcji odłożona — problem planu zostaje otwarty co najmniej o jeden cykl dłużej
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a”
- Po czym autor i krytyk planu rozpoznają zadanie wymagające podziału?
  - Answer: Ocena agenta bez liczby: zadanie jest za duże, gdy jego cel łączy dwa albo więcej efektów, z których każdy da się osobno sprawdzić w działającym produkcie i scalić przed pozostałymi; sygnałem do przyjrzenia się jest zadanie zbierające wyraźnie więcej pytań definicji, wpisów rzutowanych albo pozycji In scope niż reszta planu. Stosuje ją autor przy cięciu i krytyk przy ocenie.
  - Not chosen:
    - próg liczbowy w `plan_check.py` (np. zadanie z ponad jedną trzecią pytań definicji jest błędem) — próg z jednego przypadku; zadanie o kontach już po podziale miało 5 z 14 pytań (36%), więc taki próg zatrzymałby i je; skrypt musi przejść bez uwag przed oddaniem planu, więc każdy fałszywy alarm wymusza podział (pełny cykl) albo mechanizm wyjątków, a WAY-13 czyni wielkość tylko sygnałem do podziału
    - skrypt wypisuje przy każdym zadaniu same liczby, bez progu, a ocenia krytyk — nowy rodzaj wyjścia skryptu, który dziś wypisuje tylko błędy, z testami; zysk mały, bo krytyk i tak czyta cały plan
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 a”
- Co dzieje się z zadaniem, które krytyk wskaże jako za duże?
  - Answer: Każdy podział z powodu wielkości idzie do człowieka jako pytanie przed oddaniem planu, z wariantem „zostawić”; o dopłacie za dodatkowy cykl decyduje człowiek.
  - Not chosen:
    - jak każda uwaga krytyki: autor planu ocenia ją i sam dzieli zadanie, a do człowieka idzie tylko podział zmieniający zadanie zapisujące wpis — agent może podzielić za drobno, a każdy zbędny podział to cykl, który człowiek widzi dopiero w oddanym planie
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 b”

## Context

- Pierwotne brzmienie zadania: „the way: sprawdzanie wielkości zadania na poziomie planu projektu — skill `plan-project` mówi „duże zadanie się dzieli” (WAY-13), ale nie sprawdza tego ani `plan_check.py`, ani krytyka planu; w planie MVP `loop2` zadanie 15 wchłonęło konta, logowanie, blokadę, potwierdzenie adresu, reset hasła i pocztę (8 z 14 pytań definicji)”.
- Dowód przypadku: wiersz „Pionowe plasterki zamiast warstw” (sekcja m2l1) w notatka autora z mapą pakietu kursu — krytyk wielkości nie ocenił, podział po korekcie Mariusza; wpis dziennika zmian z 2026-10-11 w notatka autora z planem MVP gry loop2 („zadanie 15 konta-graczy-i-logowanie podzielone na zadanie 15 …, 19 blokada-konta, 20 potwierdzenie-adresu … i 21 reset-hasla”).
- Podział nastąpił w tym samym dniu, w którym plan powstał, więc historia notatek nie trzyma wersji planu sprzed podziału; liczba „8 z 14” pochodzi z mapy i z wpisu dziennika zmian planu.
- Po podziale zadanie 15 nadal trzymało 5 z 14 pytań definicji, a przy jego doprecyzowaniu 2026-10-25 z zadania wydzielono jeszcze zadanie 22 „szyfrowana-droga-do-serwera” (wpis dziennika zmian planu z tego dnia).
- Przy doprecyzowaniu pojedynczego zadania the way już ma regułę o wielkości: „Keep one task by default: each split adds a full cycle” i „a task's size alone (WAY-13) you name as a signal and leave the split to the human” (`project-level/task/skill/read_sources.md`).
- Dopisek z 12.11.2026 (analizy na Fable, sprawa 10 w notatka autora z rozstrzygnięciami): zestawić rozmiar dokumentu zadania i rozmiar scalonej zmiany z liczbą problemów w cyklu — rejestr problemów audytu ma ocenę wsteczną cykli od 29.10.2026, skrypty pomiaru trzeba napisać od nowa; mediana scalanej zmiany w grze to 1430 linii, 62 z 81 zmian ma ponad 150 linii (D8 i K4 w notatka autora z praktykami z kursu o AI).
- Karta K4 tego samego raportu sama zaznacza, że rozmiar zmiany oceniany przez jedną recenzję to inna sprawa niż wielkość pracy w zadaniu planu.
- Rachunek z notatka autora o usprawnieniach the way (sekcja 3): 22 z 58 cykli gry dodały ponad 3000 linii i dały 61% kosztu; mediana takiego cyklu to 80,5 USD i 4:47 h pracy agentów.
- Pomiar z zadania notatka autora o mierze rozmiaru przy wyborze drogi cyklu: koszt na zmienioną linię spada z rozmiarem zmiany na obu drogach cyklu, więc podział zadania sam w sobie nie obniża kosztu — każde nowe zadanie to pełny cykl.
- the way nie ma wytycznych kodowania ani testowania dla własnego kodu (WAY-328), więc zadanie nie czeka na wytyczne.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-13 — What sets the weight of a task's process?** „A task's size may lighten how its change is prepared and made — its plan and the number of agents making it — never the outcome it has to reach or the checks run on the finished change, and otherwise serves only as a signal to split it; only a human sets a task to return knowledge instead of a change, which merges nothing.” Zadanie jej nie zmienia.
- **WAY-143 — What does a task of a project plan end with?** „A task of a project plan ends with something that can be checked in the running product, never with a layer of the product put in place; a preparatory task stands in the plan only where a task of the plan depends on it, the task it opens the way for.” Zadanie jej nie zmienia.
- **WAY-146 — What checks a project plan before it is handed over?** „The plan's independent critique then judges, against the definition, what no script tells apart: whether each task that is not preparatory ends with something checkable in the running product, whether each technical element enters with the first task that uses it, whether each question stands where the definition puts it or the log of changes gives its move, and whether a quoted answer settles its question. A check a script can make is never left to the critique.” Zadanie ją zmienia (punkt 4).
- **WAY-120 — How does the-way critique an agent's proposal?** „An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict.” Zadanie jej nie zmienia.

## Settlements to record

Candidates: 3 shown, 2 accepted — 2026-11-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zadanie planu projektu jest za duże, gdy jego cel łączy dwa albo więcej efektów, z których każdy da się osobno sprawdzić w działającym produkcie i scalić przed pozostałymi, a skupienie pytań definicji, wpisów rzutowanych albo pozycji In scope jest tylko sygnałem do przyjrzenia się — bez progu liczbowego w skrypcie (zmienia WAY-146). | decision | pytanie 2 pod *Questions to settle* (wybór Mariusza przez doradcę dnia) | czy wielkość ocenia skrypt progiem, czy krytyk, i po czym — oraz czy *Rejected* WAY-146 dostaje próg i same liczby |
| 2 | Podział zadania planu z powodu wielkości rozstrzyga człowiek, przed oddaniem planu, z wariantem „zostawić”; autor planu nie dzieli zadania sam tylko dlatego, że jest duże (zmienia WAY-146). | decision | pytanie 3 pod *Questions to settle* (wybór Mariusza przez doradcę dnia) | czy autor dzieli zadanie sam po uwadze krytyka, czy pyta człowieka |

## Out of scope

- Pomiar z dopisku z 12.11.2026 (rozmiar dokumentu zadania i scalonej zmiany wobec liczby problemów w cyklu) — poza tym zadaniem (pytanie 1).
- Zmiana `project-level/plan_check.py` — kryterium nie ma części dla skryptu (pytanie 2).
