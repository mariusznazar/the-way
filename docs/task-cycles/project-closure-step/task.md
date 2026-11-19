---
title: "the way: krok zamykania projektu po ostatnim zrobionym zadaniu planu — co sprawdzić, co zapisać i dokąd przenieść zadania wycofane"
status: draft
created: 2026-11-19T08:09
updated: 2026-11-19
tags: [zadanie]
related: "the project note in the author's private notes"
---

# the way: krok zamykania projektu po ostatnim zrobionym zadaniu planu — co sprawdzić, co zapisać i dokąd przenieść zadania wycofane

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Gdy w projekcie prowadzonym przez the-way ostatnie zadanie planu jest zrobione, skill prowadzący plan mówi człowiekowi, że następne jest zamknięcie projektu i że skilla zamknięcia nie ma, i staje (`project-level/lead/skill/SKILL.md`, krok „1. Reconcile progress”, punkt zaczynający się od „If the last task is `done`”).
- Zamknięcie robi się dziś ręcznie, bez wzoru, a linia `Status:` planu zna tylko `draft` i `handed over YYYY-MM-DD` (`project-level/plan/template.md`, sekcja „The header”).
- Odczuwa to Mariusz na końcu każdego projektu produktu prowadzonego przez the-way: przy MVP2 `loop2` agent szukał wzoru zamknięcia i go nie znalazł.
- Bez zmiany projekty zostają formalnie otwarte, plan może pokazywać zrobione zadanie jako czekające na cykl, a zadanie wycofane z projektu nie ma nowego miejsca i może przepaść — wszystkie trzy rzeczy zdarzyły się w `loop2`.

### To do

1. Skill prowadzący plan (`project-level/lead/skill/SKILL.md`) dostaje krok zamknięcia projektu, opisany w osobnym pliku obok skilla, czytanym dopiero wtedy, gdy krok przychodzi; punkt kroku 1 zaczynający się od „If the last task is `done`” zamiast zatrzymania odsyła do tego pliku, a opis skilla (pole `description`) i jego wstęp przestają wyłączać zamknięcie projektu.
2. Zamknięcie zaczyna się dopiero wtedy, gdy uzgodnienie stanów z dowodów (krok 1 skilla) zostawia każdy wiersz planu w stanie `done`, `done — goal delivered in task <n>` albo `dropped — approved by human`; gdy jakiś wiersz stoi w innym stanie, `in cycle` i `ready for cycle` w tym, zamknięcie się nie zaczyna, a agent mówi człowiekowi, który wiersz i w jakim stanie je wstrzymuje.
3. Każdemu zadaniu wycofanemu człowiek wybiera przy zamknięciu jedno z trzech miejsc, a zamknięcie samo zapisuje przeniesienie:
   - następny projekt — w miejscu projektów produktu (sekcja `## Backlog` w `AGENTS.md` produktu) zamknięcie dopisuje sekcję o zadaniu do notatki następnego projektu, którą wskaże człowiek, a gdy takiej notatki nie ma, zakłada nowy plik; gdy sekcja o tym zadaniu już tam stoi, uzupełnia ją zamiast dopisywać drugą;
   - samodzielne zadanie — w miejscu zadań zamknięcie zakłada dokument zadania w stanie `refining`, w pełnym układzie `project-level/task/template.md`, z `Project relation: source only: <definicja>`; istniejąca linia zadania zostaje, a zamknięcie zmienia w niej tylko to, na co pozwalają reguły miejsca zadań, nową linię według `project-level/task_line.md` zakłada tylko wtedy, gdy zadanie żadnej nie ma;
   - porzucone na zawsze — z powodem podanym przez człowieka, zapisanym we wpisie zamknięcia.
   Z zadaniem idzie wszystko, co plan do niego przypiął: jego cel, otwarte pytania planu wskazujące to zadanie (`— plan: task <n>`) i wpisy z sekcji „Projected entries”, które realizują albo piszą tylko zadania wycofane, z zapisem, czy taki wpis jest w fundamencie produktu: zamknięcie szuka go w fundamencie na wskazanym commicie po pytaniu wpisu, które plan trzyma dosłownie, i pisze „brak w fundamencie na commicie <commit>” albo wskazuje znaleziony wpis, także częściowy, zapisany przez inne zadanie (WAY-126), a niepewne trafienie stawia w podglądzie przed zapisem jako pytanie do człowieka; sekcja albo dokument na nowym miejscu podaje te rzeczy i odsyła do wpisu zamknięcia w dzienniku zamkniętego planu.
4. Zamknięcie dopisuje do dziennika zmian planu jeden wpis zamknięcia, który podaje: osobno liczbę zadań `done`, zadań `done — goal delivered in task <n>` i zadań wycofanych, każde zadanie wycofane z jego nowym miejscem, pozycje „In scope” definicji, których nie dostarczyło żadne zadanie zrobione ani dostarczone w innym zadaniu, oraz wpisy przewidywane, których zadanie wycofane nie zapisało, z wynikiem sprawdzenia fundamentu z punktu 3.
5. Plan zamknięty ma w linii `Status:` stan `closed YYYY-MM-DD`, ustawiany przez zamknięcie obok wpisu zamknięcia; szablon planu (`project-level/plan/template.md`, sekcja „The header”) go podaje, `project-level/plan_check.py` go przyjmuje i zgłasza plan zamknięty, w którym jakiś wiersz stoi w stanie innym niż `done`, `done — goal delivered in task <n>` albo `dropped — approved by human`, albo wiersz `done — goal delivered in task <n>` wskazuje zadanie n wycofane, a `project-level/plan_state.py` na planie zamkniętym mówi wprost, że plan jest zamknięty, zamiast zgłaszać błąd braku stanu `handed over`, a skill prowadzący na takim planie mówi to człowiekowi i staje.
6. Zamknięcie najpierw pokazuje człowiekowi całość — treść wpisu zamknięcia, zmianę `Status:` na `closed YYYY-MM-DD` i pełny tekst każdego przeniesienia — i zapisuje cokolwiek dopiero po jego akceptacji.
7. Plik kroku zamknięcia mówi, że zamknięcie nie zmienia definicji projektu, a rozjazd między definicją a tym, co dostarczono, opisuje tylko wpis zamknięcia w planie.

### Questions to settle

- Co zamknięcie projektu ma robić?
  - Answer: Lista czynności z ręcznych zamknięć MVP1 i MVP2 `loop2` zostaje cała (A — uzupełnienie stanów zadań z dowodów, B — sprawdzenie, że każde zadanie jest zrobione, dostarczone w innym albo wycofane, C — nowe miejsce dla każdego zadania wycofanego zapisane w dzienniku planu, D — oznaczenie planu jako zamkniętego, E — definicja projektu nietknięta), nic w niej nie jest zbędne. Dochodzą dwie czynności: F — z zadaniem wycofanym idzie wszystko, co plan do niego przypiął (otwarte pytania planu wskazujące to zadanie i wpisy przewidywane, które tylko ono realizuje albo pisze; zamknięcie zapisuje, że wpis fundamentu nie powstał, i przenosi go z pytaniem tam, dokąd poszło zadanie); G — wpis zamknięcia wymienia pozycje „In scope” definicji, których żadne zadanie zrobione nie dostarczyło, „żeby zamknięty plan nie udawał, że cały zakres jest zrobiony”. Warunek wstępny przy B: żaden wiersz nie stoi w `in cycle` ani `ready for cycle`, a gdy stoi, zamknięcie się nie zaczyna.
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „Lista A–E zostaje, nic zbędnego. Brakuje dwóch rzeczy, obie wynikają z tego samego, co prawie zgubiło samouczek” — przykład z MVP2 `loop2`: pytanie „Jaka jest dokładna treść podpowiedzi samouczka i ile samouczek kosztuje?” (plan: task 26) i wpis „(new) — How does the game teach a new player?” (Realized by 26, Written by 26), pozycja „In scope” 30.
- Gdzie w procesie mieszka zamknięcie projektu?
  - Answer: Krok w skillu prowadzącym plan, opisany w osobnym pliku obok skilla — skill ma już dowody stanów i sam wykrywa ostatnie zadanie zrobione, a zmianę tanio odwrócić.
  - Not chosen:
    - osobny skill zamknięcia — nowy punkt wejścia, opis i synchronizacja z produktami, a skill prowadzący i tak musiałby go wskazać; wróci, gdy zamknięcie urośnie o przegląd fundamentu albo retrospektywę projektu
    - tylko nowy status planu i wpis w dzienniku — nie pilnuje uzupełnienia stanów ani zadań wycofanych, a brak tego prawie zgubił samouczek MVP2
    - nic nie zmieniać — projekty zostają formalnie otwarte, a zadania wycofane tylko w dzienniku
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „a) — krok w skillu prowadzącym, w osobnym pliku obok skilla.”
- Dokąd może pójść zadanie wycofane przy zamknięciu, kto wybiera miejsce i czy zamknięcie samo je tam zapisuje?
  - Answer: Trzy miejsca — następny projekt (notatka w miejscu projektów), samodzielne zadanie (linia i dokument w miejscu zadań), porzucone na zawsze z powodem; człowiek wybiera, zamknięcie samo zapisuje przeniesienie. Gdy w miejscu projektów istnieje już notatka następnego projektu, zamknięcie dopisuje do niej sekcję o zadaniu wycofanym zamiast zakładać nowy plik; nowy plik tylko wtedy, gdy takiej notatki nie ma. Brak szablonu notatki jest przyjęty; forma sekcji: cel zadania, pytania planu, wpis fundamentu, który nie powstał, odsyłacz do wpisu w dzienniku zamkniętego planu.
  - Not chosen:
    - te same trzy miejsca, ale zamknięcie zapisuje w planie tylko, dokąd zadanie poszło, a treść przenosi człowiek — przeniesienie pytania i wpisu znów zależy od pamięci człowieka, czyli od tego, co prawie zgubiło samouczek
    - tylko dwa miejsca: samodzielne zadanie albo porzucone — rozjeżdża się z praktyką z MVP2, a definicja następnego projektu musiałaby sama szukać takich zadań w miejscu zadań, inaczej powstaje dubel
    - jak dziś, tylko wpis w dzienniku bez wymaganego miejsca — zadanie wycofane może przepaść
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „3 a — trzy miejsca, człowiek wybiera, zamknięcie samo zapisuje przeniesienie. To dokładnie to, co Mariusz zrobił przy MVP2 (samouczek → zakres_projektu_2_loop2.md), więc a) utrwala jego praktykę zamiast ją zmieniać.”
- Czy plan zamknięty dostaje nowy stan w linii `Status:`?
  - Answer: Tak — `closed YYYY-MM-DD`, z kontrolą w `plan_check.py`, że każdy wiersz zamkniętego planu jest `done`, dostarczony w innym zadaniu albo `dropped`, i z `plan_state.py` mówiącym wprost „plan zamknięty”; wpis zamknięcia w dzienniku zostaje obok nowego stanu. Zmienia WAY-142.
  - Not chosen:
    - bez nowego stanu, znacznikiem zamknięcia jest sam wpis w dzienniku — nagłówek planu dalej wygląda na otwarty, a skill prowadzący przy każdej sesji wracałby do planu i musiałby rozpoznawać zamknięcie po tekście wpisu, co jest kruche
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „4 a — nowy stan `closed RRRR-MM-DD` w linii Status: […] Rozpoznawanie zamknięcia po tekście wpisu w dzienniku to krucha droga, a skill prowadzący wracałby do tego planu przy każdej sesji.”
- Czy zamknięcie zapisuje cokolwiek dopiero po akceptacji człowieka?
  - Answer: Tak — najpierw pokazuje całość (wpis zamknięcia, zmianę `Status:`, pełny tekst każdego przeniesienia), zapisuje po akceptacji człowieka; zamknięcie pisze w notatkach, które człowiek prowadzi sam, a dodatkowa tura to zwykle jedno „tak”.
  - Not chosen:
    - wybór miejsc dla zadań wycofanych jako zgoda, zapis od razu — tekst dopisany do notatki następnego projektu albo nowy dokument zadania trafia bez przejrzenia, a zły trzeba poprawiać ręcznie w dwóch miejscach
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „5 a — najpierw pokazuje całość (wpis zamknięcia, zmianę Status:, pełny tekst każdego przeniesienia), zapisuje po akceptacji człowieka.”
- Skąd zamknięcie wie, że wpis fundamentu zadania wycofanego nie powstał?
  - Answer: Zamknięcie sprawdza fundament produktu na konkretnym commicie i pisze „brak w fundamencie na commicie X” albo wskazuje znaleziony wpis (także częściowy, zapisany przez inne zadanie według WAY-126). Szuka po pytaniu wpisu: nagłówki wpisów fundamentu to pytania, a plan trzyma pytanie dosłownie, więc to pewniejsze niż brzmienie zdania. Niepewne trafienie idzie do podglądu przed zapisem jako pytanie do człowieka.
  - Not chosen:
    - wystarczy tabela planu: piszące zadanie wycofane, więc wpisu nie ma — nic nie kosztuje, ale może fałszywie ogłosić brak wpisu, który inne zadanie zapisało (WAY-126)
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „6 a — zamknięcie sprawdza fundament produktu na konkretnym commicie i pisze „brak w fundamencie na commicie X” albo wskazuje znaleziony wpis”
- Jak wygląda zadanie wycofane, które staje się samodzielnym zadaniem?
  - Answer: Pełny układ szablonu zadania i `Project relation: source only: <definicja>`; istniejąca linia zadania zostaje (zamknięcie zmienia w niej tylko to, na co pozwalają reguły miejsca zadań), nowa linia tylko, gdy zadanie żadnej nie ma. Ta sama zasada „bez dubla” dla sekcji w notatce następnego projektu: gdy sekcja o tym zadaniu już tam stoi, zamknięcie ją uzupełnia, nie dopisuje drugiej.
  - Not chosen:
    - `Project relation: independent` — zadanie zrywa związek z definicją, a pytanie i wpis wchodzą jako zwykły tekst, nie jako przejęte ustalenia definicji
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „7 a — pełny układ szablonu i `Project relation: source only: <definicja>`; istniejąca linia zadania zostaje […], nowa linia tylko, gdy zadanie żadnej nie ma.”
- Czy kontrola planu zgłasza plan zamknięty, w którym wiersz `done — goal delivered in task <n>` wskazuje zadanie n wycofane?
  - Answer: Tak, tylko w planie zamkniętym; to kontrola, którą skrypt może zrobić, więc według WAY-146 nie zostaje dla krytyki.
  - Not chosen:
    - nie — zamknięty plan może twierdzić, że cel dostarczyło zadanie, którego nigdy nie zrobiono
  - Source: doradca dnia (sesja w imieniu Mariusza), 2026-11-19: „8 a — tylko w planie zamkniętym; to kontrola, którą skrypt może zrobić, więc wg WAY-146 nie zostaje dla krytyki.”

## Context

- Ręczne zamknięcia `loop2` z 2026-11-19 są materiałem wyjściowym, nie przyjętym wzorcem: plan MVP2 (w prywatnych notatkach autora, sekcja `## Change log`, trzy wpisy z 2026-11-19 — wycofanie samouczka, uzupełnienie stanu zadania 22, zamknięcie projektu), plan MVP1 (w prywatnych notatkach autora, ostatni wpis dziennika) i przeniesienie samouczka do zakresu następnego projektu (w prywatnych notatkach autora, sekcja „Samouczek z MVP2”).
- W obu wpisach zamknięcia linia `Status:` planu została `handed over`, bo szablon planu nie zna stanu zamknięcia.
- Linię `Status:` planu czytają dwa skrypty: `project-level/plan_check.py` (wzorzec `STATUS`, przyjmuje tylko `draft` i `handed over YYYY-MM-DD`) i `project-level/plan_state.py` (funkcja sprawdzająca nagłówek planu, komunikat „plan must have one handed-over Status line”), więc nowy stan zmienia oba i ich testy.
- Folder-note projektu w vaulcie i odhaczanie linii zadań w Obsidianie to konwencja Mariusza, nie the-way; the-way zna tylko miejsca projektów i zadań z sekcji `## Backlog` produktu i reguły miejsca zadań (WAY-107).
- Vaultowa procedura domknięcia całego projektu `(P)` (w prywatnych notatkach autora, sekcja „Cykl życia projektu: archiwizacja”) dotyczy końca całego obszaru w vaulcie, nie zamknięcia planu wewnątrz żywego produktu.
- Zapis sesji, w której zadanie powstało (plik lokalny poza repo, wygasa około 2027-02-17): plik zapisu sesji w katalogu użytkownika, poza repozytorium.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-142 — What does the breakdown of a project write, and in what form?: „The breakdown of a project writes its plan as one document beside the approved definition, whose header names the definition and the fingerprint the definition's approval record holds, and whose `Status:` line says whether the plan is still a draft or has been handed to the human.” (pierwsze zdanie) — zadanie zmienia to zdanie: linia `Status:` mówi też, że plan został zamknięty (`closed YYYY-MM-DD`), co ustawia krok zamknięcia skilla prowadzącego, gdy każde zadanie jest zrobione, dostarczone w innym albo wycofane (odpowiedź na pytanie o nowy stan w *Questions to settle*).
- WAY-145 — Who sets where an open question of an approved project definition is resolved?: „Once a project definition has passed its readiness approval, the place of resolution it gives an open question is the question's first assignment, and the plan decides from then on where the question is resolved: in a task of the plan, or by an answer the human gives or the plan quotes, with its place, from the definition or the foundation.” — przeniesienie pytania zadania wycofanego przy zamknięciu nie zmienia jego linii w sekcji „Open questions” planu; dokąd poszło, mówi wpis zamknięcia.
- WAY-146 — What checks a project plan before it is handed over?: „A check a script can make is never left to the critique.” — z tego zdania kontrola stanów wierszy planu zamkniętego trafia do `plan_check.py`.
- WAY-118 — What makes a project definition ready for breakdown?: „A change to those sections after approval goes through the readiness approval again before breakdown relies on it.”
- WAY-153 — What evidence supports a task state in a project plan?: „The project orchestrator applies supported transitions with a reason and evidence in the plan's log, resolves outcomes Git cannot establish through the product's chosen PR tool or asks the human when that tool is absent, and brings a closed-unmerged PR or a trace conflicting with the plan to the human without automatically correcting the plan.”
- WAY-107 — Where does a product tell the project level where its backlog stands?: „A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md` […]. How a task's line is handled […] is taken from the rules of the task place itself, never from text written at the product or in the-way's skills”

## Settlements to record

Candidates: 9 shown, 6 accepted — 2026-11-19

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zamknięcie projektu jest krokiem skilla prowadzącego plan, opisanym w osobnym pliku obok skilla, a nie osobnym skillem; wróci do osobnego skilla, gdy zamknięcie urośnie o przegląd fundamentu albo retrospektywę projektu. | decision | pytanie „Gdzie w procesie mieszka zamknięcie projektu?” (jego *Not chosen*) | czy zapisać, dlaczego zamknięcie nie jest osobnym skillem — bez wpisu następna zmiana skilla prowadzącego może je wydzielić, nie znając kosztu |
| 2 | Każdemu zadaniu wycofanemu człowiek wybiera przy zamknięciu jedno z trzech miejsc — następny projekt (sekcja w istniejącej notatce następnego projektu w miejscu projektów, nowy plik tylko gdy jej nie ma), samodzielne zadanie w miejscu zadań albo porzucone z powodem — a zamknięcie samo zapisuje przeniesienie razem z celem zadania, pytaniami planu i wpisem fundamentu, którego zadanie nie zapisało. | decision | pytanie „Dokąd może pójść zadanie wycofane przy zamknięciu…” (jego *Not chosen*) | czy zamknięcie przenosi treść samo, czy tylko zapisuje w planie, dokąd zadanie poszło, i czy zakłada nowy plik, gdy notatka następnego projektu już jest |
| 3 | Zamknięcie najpierw pokazuje człowiekowi całość — wpis zamknięcia, zmianę `Status:` i pełny tekst każdego przeniesienia — i zapisuje cokolwiek dopiero po jego akceptacji. | decision | pytanie „Czy zamknięcie zapisuje cokolwiek dopiero po akceptacji człowieka?” (jego *Not chosen*) | czy wybór miejsc przez człowieka wystarcza jako zgoda na zapis |
| 4 | Kontrola planu zgłasza plan zamknięty, w którym jakiś wiersz stoi w stanie innym niż `done`, `done — goal delivered in task <n>` albo `dropped — approved by human`, albo wiersz `done — goal delivered in task <n>` wskazuje zadanie n wycofane. | invariant | pytania „Czy plan zamknięty dostaje nowy stan w linii `Status:`?” („z kontrolą w `plan_check.py`, że każdy wiersz zamkniętego planu jest done, dostarczony w innym zadaniu albo dropped”) i „Czy kontrola planu zgłasza plan zamknięty, w którym wiersz `done — goal delivered in task <n>` wskazuje zadanie n wycofane?” (ich *Not chosen*) | czy dopisać zdanie do niezmiennika `project-plan-form` albo `project-plan-check`, czy zostawić nową kontrolę bez niezmiennika i testu, który go cytuje |
| 5 | Zamknięcie sprawdza, czy wpis przewidywany zadania wycofanego jest w fundamencie produktu, szukając go po pytaniu wpisu na konkretnym commicie, i pisze „brak w fundamencie na commicie X” albo wskazuje znaleziony wpis, także częściowy, a niepewne trafienie stawia człowiekowi jako pytanie w podglądzie. | decision | pytanie „Skąd zamknięcie wie, że wpis fundamentu zadania wycofanego nie powstał?” (jego *Not chosen*) | czy wnioskować brak wpisu z samej tabeli planu |
| 6 | Zadanie wycofane, które staje się samodzielnym zadaniem, dostaje dokument w pełnym układzie szablonu z `Project relation: source only: <definicja>`, a zamknięcie nie dubluje ani jego istniejącej linii w miejscu zadań, ani sekcji o nim w notatce następnego projektu. | decision | pytanie „Jak wygląda zadanie wycofane, które staje się samodzielnym zadaniem?” (jego *Not chosen*) | czy nowe zadanie jest `independent`, czy `source only`, i czy zakłada drugą linię albo drugą sekcję |

## Out of scope

- Plany MVP1 i MVP2 `loop2` w vaulcie i definicja MVP2 `loop2` zostają nietknięte — to zamknięty materiał przykładowy.
- Przesunięcie przypiętej wersji the-way w `loop2`; produkty dostają zmianę dopiero przy takim przesunięciu.
