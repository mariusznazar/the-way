---
title: "the way: poprawki z uwag cykli (ai-review S7), partia 2026-11-06"
status: draft
created: 2026-11-06T11:00
updated: 2026-11-06
tags: [the-way, zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Cztery poprawki the way z uwag cykli (AIR-602–605): cykl na the-way rusza z aktualnej gałęzi, wpisy zmiany bez krytyki zestawu, bez nazwy prywatnego skryptu, język zadania liczony bez cytatów

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykle zadań prowadzone według the-way zostawiają w PR-ach uwagi o miejscach, w których reguły procesu nie pasowały do sytuacji; nocny przegląd ai-review zbiera je jako sprawy, a 2026-11-06 Mariusz przyjął cztery: AIR-602, AIR-603, AIR-604 i AIR-605.
- Cykl puszczony z nieaktualnej kopii repozytorium idzie po cichu według starych reguł, więc poprawka procesu scalona wieczorem potrafi nie zadziałać w cyklu puszczonym zaraz po niej.
- PR-y polskich zadań na the-way otwierają się jako szkice z fałszywym błędem sprawdzenia, który Mariusz musi ocenić przy scaleniu.
- Agenci i recenzenci cykli zgłaszają jako brak krytykę zestawu, której nie musieli robić.
- Bez zmiany te same uwagi wracają w zapisach kolejnych cykli.

### To do

Numery linii odpowiadają stanowi `origin/foundations` @ `3177e10`.

1. **(AIR-602) Cykl na samym the-way rusza z aktualnej wersji zdalnej gałęzi.** Zmiany w `task-cycle/skill/SKILL.md`:
   - w kroku 4, przed „Create a task branch from the current target branch…” (`:116`):
     > In the-way itself, first bring the checkout the session works in up to the remote target branch, the one change the cycle makes outside the task's worktree: fetch, and where it stands behind, fast-forward it when it is on that branch with a clean tree and no local commits, then start again from the entry point that started the cycle; where it cannot fast-forward, stop and say so.
   - w kroku 5 (`:125-126`) zdanie „Create the ignored record `.runs/task-cycles/<task-slug>/cycle.md`” dostaje dopisek „in the task's worktree”; reszta skilla już tak mówi (`:41`, `:68`, `:121`).
   - korekta po uwagach do PR-a też rusza z aktualnej wersji zdalnej gałęzi (`task-cycle/skill/correction.md`): na samym the-way, przed sprawdzeniem pola *Reserved choice* (`:6`, „Before anything else…”, przeformułowane), korekta pobiera zmiany, a potem — gdy sesja pracuje w kopii gałęzi docelowej, przewija ją jak krok 4 skilla cyklu albo staje; gdy pracuje w worktree requestu, scala do niego zdalną gałąź docelową — i w obu przypadkach zaczyna od nowa od punktu wejścia, który ją uruchomił;
   - w `correction.md:20` „First merge, never rebase, the current target branch” → „…the remote target branch”; zmiana obejmuje też produkty, bo `correction.md` jest wspólny.
2. **(AIR-603) Wpisy fundamentu pisane w zmianie nie przechodzą krytyki zestawu.** W `elements/common/way_of_working.md`, po „(WAY-120).” (`:16`):
   > Foundation entries a change writes are no such set: the review of the change reads them, and the human accepts them at the readiness gate, with the task document or at the merge (WAY-10, WAY-114).
3. **(AIR-604) the-way nie wymienia z nazwy skryptu z prywatnych notatek** (WAY-27):
   - `task-cycle/record_template.md:181-182`: „`cycle_remarks_digest.py` of the nightly review and `task-cycle/remarks_check.py` cut the block…” → „The nightly review of cycles and `task-cycle/remarks_check.py` cut the block…”;
   - `task-cycle/remarks_check.py:31-32`: „that open as `cycle_remarks_digest.py`, which the nightly review of cycles runs, cuts them:” → „that open as the nightly review of cycles cuts them:”;
   - `task-cycle/remarks_check.py:34`: „as that script cuts them” → „as that review cuts them”;
   - `task-cycle/remarks_check.py:70` (komentarz): „as `cycle_remarks_digest.py` has them.” → „as the nightly review of cycles has them.”
4. **(AIR-605) Sprawdzenie języka nie liczy tekstu w cudzysłowach.**
   - `task-cycle/request_check.py`, `english_share` (`:262-269`): przed liczeniem usuwać tekst w cudzysłowach („…”, “…”, "…"), dopasowywany w obrębie jednej linii, żeby niesparowany znak nie wyciął reszty tekstu, oraz linie zaczynające się od `>`;
   - opis miary (`:31-33`): dopisać „quoted text” do listy tego, czego się nie liczy;
   - `task-cycle/test_request_check.py`: polskie zadanie z długimi angielskimi cytatami daje `not English`; blok w całości w cudzysłowie daje `not judged` (znana luka: angielskie streszczenie w cudzysłowie przestaje być oceniane);
   - WAY-291, *Verification* (`foundations/decisions.md:8810`): przykład zgodny „the script reads a correct Polish block full of quoted English names as English” → „…full of English names outside quotes as English”.

### Questions to settle

- Jak cykl na samym the-way ma uniknąć pracy według reguł z nieaktualnej kopii repozytorium?
  - Answer: cykl sam pobiera zmiany — fetch i przewinięcie do przodu, gdy kopia stoi na gałęzi docelowej, czysta i bez lokalnych commitów, potem ponowne czytanie skilla; w przeciwnym razie cykl staje.
  - Not chosen:
    - Skill każe czytać skill i pliki, które nazywa, z commitu bazowego zadania — przeczy WAY-127, według którego sesja czyta skill z katalogu, w którym pracuje, bo zmianę skilla sprawdza się skillem z własnej gałęzi; do tego każdy plik to dodatkowe polecenie gita, a agent może z wygody sięgnąć po kopię już zmienioną przez autora.
    - Bez zmiany w the-way: `git pull` w głównej kopii przed każdym cyklem na the-way, jako nawyk albo hook startu sesji — chroni przed starymi regułami, ale nie rozstrzyga miejsca zapisu przebiegu.
  - Source: Mariusz, 2026-11-06, sesja ai-review — `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md`, AIR-602, *Historia*: „Mariusz zmienił wariant — cykl sam pobiera zmiany (fetch + fast-forward przy czystej kopii na gałęzi docelowej, potem ponowne czytanie skilla; inaczej staje)”; drogi nie wybrane: tamże, *Propozycja* i *Rachunek*.
- Czy punkt wejścia `.claude/skills/the-way-implement-task/SKILL.md` (i jego bliźniak w `.agents/skills/`) też trzeba przeczytać od nowa po pobraniu zmian, skoro pobrane commity mogą go zmienić?
  - Answer: tak — zdanie z *To do* 1 każe po przewinięciu zacząć od nowa od punktu wejścia, który uruchomił cykl, zamiast czytać od nowa sam skill; punkt wejścia i tak każe przeczytać skill w całości.
  - Not chosen:
    - Czytać od nowa sam skill — gdy pobrane commity zmienią punkt wejścia, cykl idzie po cichu według jego starej wersji; od 2026-10-08 punkt wejścia zmieniał się 15 razy, ostatnio (`8e5115a`) właśnie w sposobie czytania plików.
  - Source: Mariusz, 2026-11-06: „tak”, na pytanie z rekomendacją „then start again from the entry point that started the cycle”.
- Czy pobieranie zmian obejmuje też korektę po uwagach do PR-a, która idzie przez `task-cycle/skill/correction.md` i kroku 4 nie przechodzi?
  - Answer: tak — korekta na samym the-way pobiera zmiany; gdy sesja pracuje w kopii gałęzi docelowej, przewija ją albo staje, gdy w worktree requestu, scala do niego zdalną gałąź docelową; potem zaczyna od nowa od punktu wejścia. Korekta scala zawsze zdalną gałąź docelową, także w produktach.
  - Not chosen:
    - Tylko nowy cykl — korekta po uwagach dalej może iść według starych reguł i scalić starą wersję gałęzi docelowej, niewidocznie aż do kolejnej uwagi z cyklu.
    - Przewijanie w korekcie jak w kroku 4, tylko na gałęzi docelowej — korekta uruchomiona w worktree requestu, na gałęzi zadania, stawałaby na starcie.
    - „Remote target branch” tylko w zdaniu „In the-way itself…” — produkty zostają przy niejasnym „current target branch”, które może znaczyć nieaktualną gałąź lokalną.
  - Source: Mariusz, 2026-11-06: „tak”, na pytanie zakotwiczone w jego zdaniu z notatki zadania „poprawka procesu scalona wieczorem potrafi nie zadziałać w cyklu puszczonym zaraz po niej”; brzmienie z dwoma przypadkami: Mariusz, 2026-11-06: „myślę, że tak”, na `Proposal:` z tym brzmieniem.
- Czy to zadanie czeka na własne wytyczne kodowania i testów the way, skoro the way nie ma katalogu `guidelines/`, a zadanie zmienia skrypty i ich testy (WAY-215)?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak zadanie [[zadanie_the_way_pozne_etapy_w_uwagach_rekordu]], a rozjazd reguły z praktyką zostaje w zadaniu [[wlasne_wytyczne_the_way]].
  - Not chosen:
    - Czekać na zadanie o własnych wytycznych the way — wszystkie cztery poprawki, także trzy bez kodu, czekają, a do tego czasu każde polskie zadanie na the-way daje szkic PR-a z fałszywym błędem.
    - Wydzielić punkt 4 i tylko jego zostawić czekającym — dwa zadania i dwa cykle zamiast jednego, fałszywy błąd i tak zostaje do czasu wytycznych.
  - Source: Mariusz, 2026-11-06: „nie czeka”, na pytanie z trzema drogami i rekomendacją „nie czeka, jak poprzednio”.

## Context

- Źródło: sprawy AIR-602–605 z przeglądu warstwy AI, 2026-11-06, w `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md` (po 14 dniach od zamknięcia przechodzą do `ai_review_ledger_archive.md` w tym samym katalogu).
- Każda z czterech spraw to drobna poprawka, dlatego idą jednym zadaniem.
- AIR-602: w PR #73 główna kopia stała 5 commitów za `origin/foundations`, w tym za poprawką samego skilla cyklu; prowadzący sam zauważył różnicę i przeczytał skill drugi raz z worktree.
- AIR-602: w PR #72 narzędzie przeniosło sesję do worktree zadania, a prowadzący zostawił zapis przebiegu w `.runs/` głównej kopii, „jak w poprzednich cyklach”.
- AIR-602: przy doprecyzowaniu tego zadania główna kopia the-way stała na `2692e05`, 8 commitów za `origin/foundations` (`3177e10`); wśród nich zmiany `task-cycle/request_check.py`, `task-cycle/record_template.md` i `elements/common/way_of_working.md`.
- AIR-602: dopisek „the one change the cycle makes outside the task's worktree” w zdaniu z *To do* 1 zdejmuje sprzeczność z `task-cycle/skill/SKILL.md:68` („The cycle writes only in the task's worktree…”); Mariusz przyjął go 2026-11-06: „tak”.
- AIR-603: zwolnienie stoi dziś w `elements/common/critique/SKILL.md:20-22` i w zdaniu wiążącym WAY-120 („the diff of a change to an invariant test or to the foundation does not (WAY-10)”), ale agent otwiera `critique/SKILL.md` dopiero przy uruchamianiu krytyki; skutek: 4 uwagi w 2 cyklach (loop2 PR #57, the-way PR #73).
- AIR-603: do loop2 poprawka dotrze dopiero po przesunięciu jego przypięcia the-way.
- AIR-604: „the nightly review of cycles” to nazwa, której fundament już używa (`foundations/decisions.md:8925`, `:8960`); Mariusz przyjął ją 2026-11-06: „ok”, w miejsce „a review of the remarks outside the repository”, które dodałoby drugą nazwę tej samej rzeczy.
- AIR-604: nazwę `cycle_remarks_digest.py` (skrypt nocnego przeglądu, leżący poza repozytorium) wpisał commit `2a4847e`.
- AIR-605: skrypt uznał polskie zadanie z PR #72 za angielskie, bo liczył zacytowane w nim angielskie zdania — udział angielskich słów 0,224 na 854 słowa przy progu 0,2, a po wycięciu cytatów 0,015 na 406 słów.
- AIR-605: `english_share` mierzy zarówno zadanie, jak i zwinięty blok opisu PR-a (`request_check.py:272-276`), więc wycinanie cytatów działa na oba.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Brzmienia z `foundations/decisions.md` na `origin/foundations` @ `3177e10`.

- **WAY-127 — How does a session working on the-way itself reach the-way's skills?** (`:3015`; *To do* 1): „A session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`. An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix. No global link reaches a skill of the-way other than one to `instruction-files/`, whose skill, judging a repository that pins the-way, follows that repository's pinned copy instead, and the-way is not installed in itself.”
- **WAY-140 — How does a task change something outside the product's repository?** (`:3647`; *To do* 1, zdanie skilla `:68` powołuje się na nią): „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task. […]”
- **WAY-10 — Who assesses a change to an invariant test or to the foundation?** (`:294`; *To do* 2): „A change to an invariant test or to the foundation has no assessment of its own, in a product as in the-way itself: an agent that did not make the change reviews the whole change, its foundation entries and invariant tests included, against its task and the foundation, and a human reads the section of the request's description for the human's decisions and accepts the change by merging the request.”
- **WAY-114 — What does a human accept of an entry, and when?** (`:2513`; *To do* 2): „A human accepts the meaning of a foundation entry while its wording is the agent's: the meaning of a projected entry at the readiness gate, shown as one sentence in the human's language with the entry beside it; that of an entry written whole from an accepted row of a task's *Settlements to record* with the task document, the row being the human's own settlement; and that of every other entry at the merge of the change that holds it, […]. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.”
- **WAY-120 — How does the-way critique an agent's proposal?** (`:2678`; *To do* 2): „An agent may invoke critique for any proposal without waiting for the human to express doubt; a completed set for collective human review goes through it, and the diff of a change to an invariant test or to the foundation does not (WAY-10). An independent critique gives one fresh agent the full proposal or set, its sources and applicable rules without the author's defense; the author checks each observation and gives one explicit verdict. For a collectively reviewed set the critic checks form, fidelity to source and contradictions across entries before presentation.”
- **WAY-27 — Where may this repository point for its reasoning?** (`:678`; *To do* 3): „Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the place of its tasks, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else.”
- **WAY-296 — In what form does the cycle record hold its process remarks?** (`:8970`; *To do* 3, opis formy w `record_template.md` i `remarks_check.py`): „The cycle record holds its process remarks in the one form its template gives, which the check of WAY-294 reads, and in no section or file of their own.”
- **WAY-290 — How is the form of a request's description checked?** (`:8770`; *To do* 4): „Before a request opens, the cycle runs the-way's script that checks the form of the request's description — the order and level of its headings, content or `none` in each section, and the collapsed block in the task document's language — and corrects the description until the script reports no error. The script judges no content.”
- **WAY-291 — What does the cycle do with an error of the form check that it holds wrong?** (`:8798`; *To do* 4 zmienia przykład zgodny w jej *Verification*): „Where the orchestrator of a cycle holds an error the form check reports wrong, with evidence it can name, it does not change the description to silence the error — it never empties the collapsed block and never puts it into English — and the request opens, or stays, a draft whose section for the human's decisions names the error and the cycle's reason, while its checks name the check as failed; a request blocked for another cause stays blocked.”
- **WAY-292 — What does the collapsed block of a request's description hold where the task document is in English?** (`:8831`; *To do* 4 zmienia miarę języka, na której stoi): „Where the task document of a request is in English, the collapsed block of the request's description holds `none` in place of a second English copy of the top part, and the form check, wherever it reads the task document as English, holds the block to `none`.”

## Settlements to record

Candidates: 6 shown, 1 accepted — 2026-11-06

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Cykl na samym the-way, zanim założy gałąź zadania, pobiera zmiany i przewija do przodu kopię, w której pracuje sesja — jedyna zmiana cyklu poza worktree zadania — gdy stoi ona na gałęzi docelowej, czysta i bez lokalnych commitów, po czym zaczyna od nowa od punktu wejścia, który go uruchomił; gdy przewinąć się nie da, cykl staje. Korekta po uwagach do PR-a robi to samo, a gdy sesja pracuje w worktree requestu, scala do niego zdalną gałąź docelową i zaczyna od nowa od punktu wejścia. | decision | *Questions to settle*, pytania 1, 2 i 3 (drogi nie wybrane stoją pod nimi); dopisek o jedynej zmianie poza worktree: *Context*, Mariusz 2026-11-06 „tak” | czy regułę zapisać tylko w skillu cyklu, czy jako decyzję, i co wpisać w jej *Rejected* (czytanie z commitu bazowego, nawyk `git pull`) |

## Out of scope

- Przesunięcie przypięcia the-way w loop2.
- Skrypt nocnego przeglądu (`cycle_remarks_digest.py`) zostaje bez zmian.
