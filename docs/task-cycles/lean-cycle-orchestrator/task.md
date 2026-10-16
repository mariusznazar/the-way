---
title: "the way: odchudzić orkiestratora cyklu zadania — mniej kroków i mniejszy kontekst"
status: draft
created: 2026-10-16
updated: 2026-10-16
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]"]
---

# the way: odchudzić orkiestratora cyklu zadania — mniej kroków i mniejszy kontekst

Status: ready for cycle
Project relation: independent

## Description

### Need

- Orkiestrator cyklu `implement-task` zużywa 48–68% tokenów małego cyklu i 29–43% dużego.
- Każdy jego krok czyta od nowa cały jego kontekst, który rośnie przez cały cykl: w cyklu PR #17 od 33 tys. do 310 tys. tokenów, średnio 179 tys., przez 159 kroków.
- Mariusz chce obniżyć koszt i czas wykonywania zadań.

### To do

1. Orkiestrator czeka na zakończenie agenta jednym oczekiwaniem tak długim, jak pozwala narzędzie, bez wielokrotnego sprawdzania i bez usypiania się między sprawdzeniami.
2. Orkiestrator nie wczytuje do swojego kontekstu tego, co czyta i sprawdza agent etapu; przy zwykłym przejściu między etapami opiera się na krótkim zwrocie agenta, zapisie cyklu, ścieżkach i commitach, a pełny raport czyta tylko w przypadkach, które WAY-148 już wymienia.
3. Pełną różnicę w kodzie plasterka czyta recenzent; orkiestrator widzi listę zmienionych plików z liczbą zmienionych linii i werdykt recenzenta.
4. Orkiestrator nie uruchamia ponownie testów plasterka; opiera się na poleceniu i kodzie wyjścia z raportu wykonawcy, a raport bez nich jest niepełny i wraca do agenta.
5. Pełną bramkę na gotowej zmianie orkiestrator uruchamia sam; pełny wynik idzie do pliku w `reports/`, a do kontekstu orkiestratora tylko kod wyjścia, podsumowanie, linie błędów, ostrzeżenia i wyniki `unchecked`.
6. Orkiestrator czyta w całości tylko metody, które prowadzi sam — skill cyklu, `subagent-driven-development`, `requesting-code-review`; metody prowadzone przez agenta etapu (`brainstorming`, `test-driven-development`, `plan-task`, skille zapisu wpisów fundamentu) czyta agent, a orkiestrator zna ich granice z kroku cyklu.

### Questions to settle

- Pytanie 1: Czy orkiestrator dalej sam czyta pełną różnicę w kodzie każdego plasterka (krok 10 skilla cyklu: „After each slice, run its focused checks, review its diff and resolve findings”), obok recenzenta, który czyta ją w całości?
  - Answer: Nie; pełną różnicę czyta recenzent, orkiestrator widzi listę zmienionych plików z liczbą linii i werdykt recenzenta. Ryzyko: orkiestrator nie złapie tego, co przeoczy recenzent; zostają niezależna ocena i przegląd człowieka przy scaleniu.
  - Source: Mariusz, 2026-10-16, „1. zmieńmy”.
- Pytanie 2a: Czy orkiestrator uruchamia ponownie testy każdego plasterka (krok 10: „After each slice, run its focused checks”), które uruchomił już wykonawca, a zwykle także recenzent?
  - Answer: Nie; wystarcza polecenie i kod wyjścia z raportu wykonawcy z pełnym wynikiem w pliku w `reports/`; brak ich czyni raport niepełnym. Całość sprawdza raz pełna bramka na końcu.
  - Source: Mariusz, 2026-10-16, „tak, przyjmuję 2a i 2b”.
- Pytanie 2b: Czy pełny wynik bramki na gotowej zmianie ma trafiać do kontekstu orkiestratora?
  - Answer: Nie; orkiestrator uruchamia bramkę sam, pełny wynik idzie do pliku w `reports/`, a do kontekstu kod wyjścia, podsumowanie, linie błędów, ostrzeżenia i wyniki `unchecked`.
  - Source: Mariusz, 2026-10-16, „tak, przyjmuję 2a i 2b”.
- Czego dotyczy zdanie skilla cyklu „a summary is not proof of a missing check”?
  - Answer: Streszczenia od agenta przy naprawie niepełnego raportu — zdanie „testy przeszły” nie zastępuje sprawdzenia, którego w raporcie brakuje; nie każe orkiestratorowi uruchamiać testów ponownie.
  - Source: `task-cycle/skill/SKILL.md` w `foundations` @ dc43305, akapit po „Read authoritative sources and relevant report evidence”; Mariusz, 2026-10-16.
- Pytanie 3: Czy orkiestrator czyta w całości metody, które prowadzi agent etapu, a nie on sam (skill cyklu, krok 3: „Read each skill and its linked files when its stage begins”)?
  - Answer: Nie; czyta w całości tylko metody, które prowadzi sam (skill cyklu, `subagent-driven-development`, `requesting-code-review`), a metody agentów czyta agent.
  - Source: Mariusz, 2026-10-16, „3. zdecydowanie to zmieniamy”.
- Które dźwignie wchodzą do zadania?
  - Answer: Czekanie bez wielokrotnego sprawdzania i niewczytywanie przez orkiestratora tego, co sprawdził agent etapu; świeży orkiestrator na granicy etapów zostaje na osobne zadanie.
  - Source: Mariusz, 2026-10-16, „ok, zróbmy faktycznie 1 i 2”.

## Context

### Kolejność

- Cykl tego zadania startuje po scaleniu [[jeden_autor_malej_zmiany]] — oba zmieniają `task-cycle/skill/SKILL.md`, a liczba kroków orkiestratora zależy od drogi jednego autora; opis zadania na scalenie nie czeka.

### Pomiar kroków orkiestratora (2026-10-16)

- Pomiar z zapisów sesji czterech małych cykli: PR #17, PR #15, PR #18 (Codex) i PR #14 (Claude Code); kategorie przypisane po treści poleceń, w Codeksie przybliżone, bo jedno wywołanie łączy kilka poleceń.
- Czekanie na agentów i wiadomości do nich to 15–40% kroków orkiestratora; w Codeksie orkiestrator sprawdza agenta wielokrotnie (PR #17: 37 oczekiwań na 7 agentów; PR #18: dodatkowo 21 poleceń uśpienia).
- Do kontekstu orkiestratora wchodzi przez cykl 110–276 tys. tokenów wyników poleceń.
- Czytanie tekstów procesu — skille, szablony, metody Superpowers, README, fundament — to 30–55% tego, co wchodzi do kontekstu; kontekst dochodzi do ok. 100 tys. już w rozpoznaniu.
- Czytanie raportów agentów i zapisu cyklu to 12–31%.
- Wyniki gita, różnice w kodzie i wyniki testów to reszta, 10–47%.

## Questions carried to cycle

- Jak w Codeksie i w Claude Code zrealizować czekanie na agenta jednym oczekiwaniem — którymi narzędziami i przy jakich limitach czasu.

## Human actions

none

## Decisions in play

- WAY-148/1 — kontrakt przekazania pracy; zwykłe przejście na krótkim zwrocie już w nim stoi, zadanie dokłada, czego orkiestrator nie czyta i nie powtarza:
  > Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, stage status, paths, commits, a concise check result and every unresolved concern affecting the next dispatch. The orchestrator records the event and relevant choices before dependent dispatch and reads authoritative sources and relevant report evidence before deciding a question, settling a finding, accepting a foundation meaning or verifying disputed or incomplete evidence; routine progression uses the short return, record, source paths and commits without requiring prior conversational history. A missing or incomplete report is repaired before dependent work proceeds, and this transfer contract preserves required whole-source reads, check and review duties and the independent assessor's filtered inputs (WAY-10), reusing a borrowed method's existing brief and report rather than duplicating them.
- WAY-125/1 — obowiązki orkiestratora przy przyjętych metodach Superpowers; zadanie nie zmienia, które metody przyjęto, tylko kto czyta ich tekst:
  > The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec, test-first implementation, subagent execution with independent task and final code reviews, and preparing a pull or merge request, only for a ready task run through `implement-task`. The orchestrator answers workflow questions and gives provisional stage go-aheads under the task owner's delegation, never records these as human approval, controls the return between stages, keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment of its foundation change and its return step, and brings the request to the human for review. Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request; a different Superpowers version requires a reviewed change to the-way before use.
- WAY-16/1 — jedno polecenie bramki dla agenta, człowieka i scalenia; zadanie zmienia tylko, gdzie trafia jego wynik:
  > The gate takes its checks from the methods of checking written in the entries, never from a list written by hand, and one command runs the checks a change calls for together with the product's own tests it calls for — the same command for an agent, for a human and for whatever runs it when a change is merged.
- WAY-63/1 — wyniki bramki; podsumowanie w kontekście orkiestratora musi nieść `error`, `fail` i `unchecked`:
  > An invariant's result on the commit being checked is `pass`, `fail`, `unchecked` for a reason on the template's closed list, or `error` otherwise. The gate reports a result for at least every invariant the change reaches and every invariant a critical flow names, and its command exits non-zero when a result it reports is `error`, a listed invariant's is `pass`, an unlisted invariant's or a fact's is `fail`, or a run records a failure for no entry, and zero otherwise.
- WAY-136/1 — orkiestrator zapisuje rozstrzygnięcie o równoległej pracy; decyzję zmienia [[jeden_autor_malej_zmiany]], cykl tego zadania bierze jej brzmienie po scaleniu.

## Settlements to record

Candidates: 5 shown, 5 accepted — 2026-10-16

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Orkiestrator czeka na zakończenie agenta jednym oczekiwaniem, bez wielokrotnego sprawdzania i usypiania się. | decision | Mariusz, 2026-10-16, „ok, zróbmy faktycznie 1 i 2”; To do 1 | Czy odpytywać agenta w krótkich odstępach, jak dziś w Codeksie. |
| 2 | Pełną różnicę w kodzie plasterka czyta recenzent; orkiestrator widzi listę zmienionych plików z liczbą linii i werdykt recenzenta. | decision | Pytanie 1; To do 3 | Czy orkiestrator ma dalej sam przeglądać różnicę każdego plasterka. |
| 3 | Orkiestrator nie uruchamia ponownie testów plasterka; opiera się na poleceniu i kodzie wyjścia z raportu wykonawcy. | decision | Pytanie 2a; To do 4 | Czy po każdym plasterku uruchamiać jego testy po raz kolejny. |
| 4 | Pełny wynik bramki idzie do pliku; do kontekstu orkiestratora trafia kod wyjścia, podsumowanie, linie błędów, ostrzeżenia i wyniki `unchecked`. | decision | Pytanie 2b; To do 5 | Czy wczytywać cały wynik bramki do kontekstu orkiestratora. |
| 5 | Orkiestrator czyta w całości tylko metody, które prowadzi sam; metody prowadzone przez agenta etapu czyta agent. | decision | Pytanie 3; To do 6 | Czy orkiestrator ma czytać `brainstorming`, `test-driven-development`, `plan-task` i skille zapisu wpisów przed etapem agenta. |

## Out of scope

- Świeży orkiestrator na granicy etapów (nowa sesja czytająca tylko zapis cyklu) — osobne zadanie, gdy będzie wiadomo, ile zostaje po tym i czy da się to zrobić w Claude Code.
- Droga jednego autora dla zmiany, którą obejmie jeden agent: [[jeden_autor_malej_zmiany]].
