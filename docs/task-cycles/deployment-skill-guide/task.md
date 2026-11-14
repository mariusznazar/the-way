---
title: Pokazać na przykładzie loop2, jak przygotować instrukcję wdrażania kolejnego produktu
status: draft
created: 2026-10-25T16:00
updated: 2026-11-14
tags: [zadanie]
related: "the project note of the process"
---

# Pokazać na przykładzie loop2, jak przygotować instrukcję wdrażania kolejnego produktu

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Decyzja WAY-139 wymienia, co musi objąć skill wdrożeniowy produktu (instrukcja wdrażania dla agenta), a krok doprecyzowania zadania sprawdza tę listę, gdy zadanie wdraża produkt albo zmienia, jak lub gdzie działa — ale the way nie pokazuje nigdzie, jak taki skill może wyglądać, kiedy agent po niego sięga i jak odpowiedzieć na każdą pozycję listy.
- Gdy sprawdzenie dodaje zadaniu punkt „napisać albo uzupełnić skill wdrożeniowy”, agent tego punktu ma do dyspozycji samą listę; jedyny gotowy skill, `loop2-deploy`, opisuje konkretny serwer (Mikrus), tunel Cloudflare i konkretne polecenia, więc kto bierze go za wzór, sam musi oddzielać to, co ogólne, od tego, co właściwe loop2.
- Co jeśli nic: kolejny produkt dostanie skill wdrożeniowy napisany z samej listy albo przez przepisanie loop2; nie ustalono, żeby brak wzoru spowodował już błąd lub zatrzymał wdrożenie — trudność jest na razie przewidywana, nie zaobserwowana.

### To do

1. Nowy plik przewodnika po pisaniu skilla wdrożeniowego produktu w `project-level/task/`, obok kroku, który sprawdza listę WAY-139 (nazwę pliku wybiera cykl).
2. Krok sprawdzenia (`project-level/task/skill/resolve_gaps.md`, akapit zaczynający się od „When the task's outcome deploys the product or changes how or where it runs”) mówi, że punkt *To do*, który dodaje zadaniu, oraz zadanie wydzielone na tę pracę wskazują przewodnik; agent czyta przewodnik tylko wtedy, gdy pisze albo uzupełnia skill wdrożeniowy, a doprecyzowanie innych zadań go nie czyta.
3. Przewodnik ma po jednej części na każdą z siedmiu pozycji listy WAY-139: podgląd wdrożeń; gdzie leżą sekrety i jak się je wymienia; cofnięcie wdrożenia z liczbą kroków i skutkami dla danych; co robi agent, a co człowiek; jak czytać logi; jak długo żyje zapis logów, także między wdrożeniami; skąd człowiek dowiaduje się o awarii. Do tego część o tym, do czego skill służy i kiedy agent po niego sięga (opis skilla, po którym sesja go znajduje).
4. Każda część podaje pytania, na które produkt odpowiada, i krótki fragment pokazujący, jak odpowiedział loop2; to, co właściwe loop2 — serwer Mikrus, ustawienia Cloudflare, konkretne polecenia, ścieżki i parametry wdrożenia — jest we fragmencie oznaczone jako właściwe temu produktowi.
5. Fragmenty pochodzą z jednego commitu loop2, a przewodnik linkuje skill loop2 w tym commicie na GitHubie pełnym SHA; publiczny adres gry i adres pocztowy nadawcy z domeny Mariusza są we fragmentach zastąpione przykładowymi w domenie `example.com`.
6. Przewodnik mówi wprost, że niczego nie wiąże: wiążąca zostaje lista w WAY-139 i sprawdzenie w kroku doprecyzowania zadania; właściwy skill pisze i trzyma produkt, a przewodnik nie jest gotowym skillem dla żadnego rodzaju serwera.
7. Decyzja WAY-139 zmieniona w miejscu (WAY-07): jej zdanie wiążące mówi, że the way trzyma obok listy przewodnik po pisaniu skilla wdrożeniowego, z loop2 jako pierwszym przykładem, który niczego nie wiąże, a wskazuje go sprawdzenie listy; *Rejected* dostaje warianty nie wybrane pod pytaniami 1 i 2.

### Questions to settle

- 1\. Gdzie w the way leży przewodnik i jak agent piszący skill wdrożeniowy do niego trafia?
  - Answer: Osobny plik obok kroku doprecyzowania zadania, który sprawdza listę WAY-139; krok wskazuje przewodnik w punkcie *To do* „napisać albo uzupełnić skill”, który dodaje zadaniu, więc agent czyta go tylko wtedy, gdy pisze skill. Zmienia zdanie wiążące WAY-139 („The-way holds no skill of a product, only the list […]”).
  - Not chosen:
    - treść przewodnika wpisana wprost do kroku sprawdzenia — kilkadziesiąt linii czyta każde doprecyzowanie każdego zadania, także tych, które nic nie wdrażają, a wiążąca reguła miesza się z przykładem
    - osobny katalog, nowa część the way — zmiana WAY-09 i mapy części, bez zysku dla czytelnika, bo do pliku i tak prowadzi tylko krok sprawdzenia
    - nic nie robić — zostaje lista i samodzielne przerabianie loop2; dziś nic nie kosztuje, płaci pierwszy kolejny wdrażany produkt
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a”
- 2\. Jak przewodnik pokazuje loop2?
  - Answer: Szkielet z jedną częścią na każdą pozycję listy i jedną na opis skilla; w każdej pytania i krótki fragment, jak odpowiedział loop2, z oznaczeniem tego, co właściwe loop2; link do skilla loop2 w konkretnym commicie. We fragmentach nie ma adresu gry ani adresu pocztowego Mariusza — zastępuje je przykład w domenie `example.com`.
  - Not chosen:
    - cały skill loop2 skopiowany z komentarzami — około 470 linii, do publicznego the way trafiają adres gry i adres pocztowy w domenie Mariusza, cała kopia się starzeje
    - sam szkielet z pytaniami i linkiem, bez fragmentów — czytelnik i tak musi otworzyć loop2 i sam oddzielać ogólne od szczególnego, więc zostaje dzisiejsza trudność
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 a — we fragmentach bez adresu gry i adresu pocztowego Mariusza (zastąp przykładem typu example.com); link do commitu loop2 zostaje”

## Context

- Pierwotne brzmienie zadania: „Dodać do the-way szablon skilla wdrożeniowego produktu obok listy z WAY-139 — jak taki skill może wyglądać, jak działa i do czego służy; pisać po scaleniu zadania „serwer-testowy” loop2, ze skillem wdrożeniowym loop2 jako pierwszym przykładem, oddzielając to, co ogólne, od specyfiki Mikrusa i Cloudflare”.
- Warunek „po scaleniu zadania serwer-testowy” jest spełniony: gałąź `main` loop2 zawiera scalenie PR #11, a skill `.claude/skills/loop2-deploy/SKILL.md` wraz z katalogiem `references/` jest na `main` (stan 2026-11-14, `main` na `6ab6a32b`).
- Zadanie czekało na rozmowę o tym, jak agent dochodzi do działającego produktu; loop2 zapisało to w skillu `loop2-play`, więc zadanie nie czeka i zachowuje zakres (rozmowa 2026-11-08).
- Lista WAY-139 ma dziś siedem pozycji; wcześniejsze brzmienie tej notatki wymieniało pięć, bez życia zapisu logów i powiadomienia o awarii.
- Krok sprawdzenia obsługuje osobno trzy pozycje listy (odczyt logów, życie zapisu, powiadomienie o awarii): skill powtarza odpowiedź decyzji produktu o logach, a odmowę człowieka zapisuje jako pokrycie pozycji; przewodnik pokazuje oba przypadki.
- Skill loop2 ma około 470 linii i trzy pliki w `references/` (ustawienie i sekrety, awarie i cofanie, kopie zapasowe).
- Oba repozytoria, the way i loop2, są publiczne; the way cytuje już loop2 linkiem do pliku w konkretnym commicie (`foundations/environment_facts.md`, wpis ze źródłem `github.com/mariusznazar/loop2/blob/9c0dfc8…`).
- Zadanie samo niczego nie wdraża ani nie zmienia, jak czy gdzie działa produkt, więc sprawdzenie listy WAY-139 go nie obejmuje.
- the way nie ma wytycznych kodowania ani testowania dla własnego kodu (WAY-328), a zadanie zmienia pliki instrukcji, nie interfejs; nie czeka na wytyczne.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-139 — What does the-way hold for the skill that deploys a product, and which step checks that a product has one?** „The-way holds no skill of a product, only the list of what a product's deployment skill covers: a preview of deployments; where the secrets lie and how they are rotated; rollback, with its number of steps and what happens to the data; what the agent does and what the human does; how to read the logs; how long the record lives, between deployments too; and how a human learns of a failure.” *Rejected* odrzuca m.in. „a deployment skill carried by the-way — what to run and where differs for every product” i „the list in a template alone — nothing binds the refinement to check it”. Zadanie ją zmienia (punkt 7): obok listy the way trzyma przewodnik, z loop2 jako pierwszym przykładem, który niczego nie wiąże i który wskazuje sprawdzenie listy; lista zostaje w zdaniu wiążącym decyzji.
- **WAY-140 — How does a task change something outside the product's repository?** „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent […]” Przewodnik w części „co robi agent, a co człowiek” nie może jej przeczyć. Zadanie jej nie zmienia.
- **WAY-165 — What must an answer to each matter of an agent's way to the running product settle?** „[…] the logs ask where the record of what the running product does goes, how long that record lives, between deployments too, and how an agent reads it […]” WAY-139 każe skillowi powtarzać odpowiedź decyzji produktu o logach. Zadanie jej nie zmienia.
- **WAY-270 — When does the step that settles technology ask how a human learns of a failure of the running product?** „[…] lists how a human learns of a failure of the running product as a choice of its own, answered by a tool that collects failures, an alert or a deliberate absence […]” Przewodnik pokazuje świadomy brak powiadomienia jako pełnoprawną odpowiedź. Zadanie jej nie zmienia.
- **WAY-09 — What may enter the process repository?** Wymienia, co musi trzymać katalog każdej części, m.in. `project-level/` „the templates of a project definition, a project plan and a task document, the skills that write them […]”. Zadanie jej nie zmienia: przewodnik staje w `project-level/` obok kroku, który go wskazuje.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Obok listy WAY-139 the way trzyma przewodnik po pisaniu skilla wdrożeniowego produktu, z loop2 jako pierwszym przykładem; leży obok kroku sprawdzenia, który wskazuje go w punkcie „napisać albo uzupełnić skill”, i niczego nie wiąże (zmienia WAY-139). | decision | pytanie 1 pod *Questions to settle* (wybór Mariusza przez doradcę dnia) | gdzie położyć przewodnik, czy wpisać go do kroku sprawdzenia i jak przeredagować „only the list” w WAY-139 |
| 2 | Przewodnik pokazuje loop2 fragmentami z jednego commitu, z linkiem do tego commitu i z oznaczeniem tego, co właściwe loop2, bez adresu gry i adresu pocztowego Mariusza, zastąpionych przykładem w domenie `example.com` (zmienia WAY-139). | decision | pytanie 2 pod *Questions to settle* (wybór Mariusza przez doradcę dnia) | czy kopiować cały skill loop2, czy trzymać przewodnik w zgodzie z kolejnymi zmianami loop2 i czy przenosić prawdziwe adresy |

## Out of scope

- Zmiana skilla wdrożeniowego loop2 — zadanie tylko go cytuje.
