---
title: "the way: własne typy podagentów dla etapów cyklu — lżejszy start agenta i godzinna pamięć podręczna autora"
status: draft
created: 2026-11-12T22:00
updated: 2026-11-13
tags: [zadanie]
related: "the project note in the author's private notes"
---

## Po co to

- **Jak jest dziś:** Każdy agent, którego cykl zadania uruchamia do jednego etapu (pisanie zmiany, przegląd, krok zwrotny), zaczyna z bagażem 36,7 tys. tokenów, zanim przeczyta pierwszy plik. Największą częścią tego bagażu jest lista wszystkich skilli, moich prywatnych i tych z procesu, a korzysta z niej mniej więcej co dziesiąty agent. Osobno: agent piszący zmianę jest wznawiany po każdym przeglądzie, a ponieważ jego pamięć podręczna żyje 5 minut, po każdej takiej przerwie płaci za zapisanie całego kontekstu od nowa.
- **Kto to odczuwa:** Ja, w koszcie każdego cyklu w grze i w procesie. Agent cyklu, który widzi na liście mój prywatny skill o tej samej nazwie co skill procesu i może wziąć jeden za drugi.
- **Co jeśli nic:** Koszt zostaje, jaki jest, i rośnie z każdym skillem, który dopiszę, bo lista jest wspólna dla wszystkich sesji. Szacunek zysku: ok. 4,5% kosztu cyklu z lżejszego startu oraz ok. 0,9% kosztu cykli gry i 3,6% cykli procesu z godzinnej pamięci autora. Jakości to nie zagraża ani w jedną, ani w drugą stronę.

# the way: własne typy podagentów dla etapów cyklu — lżejszy start agenta i godzinna pamięć podręczna autora

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Każdy podagent, którego cykl zadania uruchamia do jednego etapu, zaczyna od ok. 36,7 tys. tokenów, zanim przeczyta pierwszy plik, a największą częścią tego startu jest lista wszystkich skilli sesji: prywatnych skilli użytkownika i skilli procesu (wg sondy z 2026-11-12).
- Z narzędzia skilli korzysta mało który agent cyklu: w grze 72 z 625 podagentów cykli, w the way 4 z 252 (wg tej samej sondy).
- Na tej liście agent cyklu widzi obok skilla procesu prywatny skill użytkownika o tej samej nazwie bez przedrostka i może wziąć jeden za drugi; plik instrukcji the way ostrzega przed tym: „a personal skill of the same name without the prefix … is not the-way's” (`AGENTS.md`, sekcja „Skills”).
- Jeden autor — agent, który sam robi zmianę bez planu — jest wznawiany do poprawki po przeglądzie i do kroku zwrotnego (`task-cycle/skill/SKILL.md`, krok 9, „Keep it for the fix and the return step”), a jego pamięć podręczna żyje 5 minut (WAY-255), więc po dłuższej przerwie zapisuje cały kontekst od nowa.
- Odbiorcą jest Mariusz, który płaci za każdy cykl gry i procesu: szacunek zysku to ok. 4,5% kosztu cyklu z lżejszego startu oraz ok. 0,9% kosztu cykli gry i 3,6% cykli procesu z godzinnej pamięci jednego autora (wg notatki z wynikami sond, sekcje 2 i 3).

### To do

1. the way ma definicje dwóch własnych typów podagentów Claude Code dla etapów cyklu, każdą z własną treścią — co najmniej dwoma zdaniami o tym, czym typ jest — i obie z każdym narzędziem sesji poza narzędziem skilli (pytanie 3):
   - typ etapów;
   - typ jednego autora: jak typ etapów i godzinna pamięć podręczna (`cacheTtl: 1h` w mapie `experimental`).
2. Instalator wstawia te definicje z przypiętego commita the way do `.claude/agents/` produktu, a z plików, które tam zastaje, przepisuje i usuwa tylko własne, tak jak wejścia skilli; plan instalacji pokazuje je przed potwierdzeniem.
3. Sesja pracująca nad samym the way ma te same definicje w śledzonym przez git katalogu `.claude/agents/` repozytorium, tak jak ma wejścia skilli (WAY-127), więc cykle procesu też z nich korzystają.
4. Instrukcja cyklu (`task-cycle/skill/SKILL.md`) zleca w Claude Code każdy etap typem z punktu 1: jednego autora — typem jednego autora, każdy inny etap — typem etapów; gdy sesja typu nie ma — inna uprząż niż Claude Code (pytanie 4), sesja uruchomiona, zanim powstał katalog `.claude/agents/` — zleca etap tak jak dziś i zapisuje to w zapisie cyklu.
5. Każdą metodę, którą agent etapu stosuje, zlecenie i metody etapów wskazują ścieżką pliku w przypiętym the way, nie nazwą skilla do wywołania — także skill elementu fundamentu, przez który agent pisze wpis („Each is written through the pinned skill of its element” w `task-cycle/skill/foundation_step.md`; „through `record-glossary-term`” w `task-cycle/skill/return_step.md`; „Where you write a foundation entry through an element's skill” w `task-cycle/change/SKILL.md`), i skille, które wskazuje metoda planisty („each skill named below is the project skill of that name with the `the-way-` prefix” w `task-cycle/plan/SKILL.md`).
6. WAY-255 (przez `record-decision`) dostaje wyjątek: pamięć podręczna jednego autora żyje godzinę; odrzucenie „a longer cache lifetime for every agent” zostaje, z rachunkiem według rodzaju agenta (pytanie 2).

### Acceptance criteria

- Agent typu z punktu 1 startuje bez listy skilli — cykl sprawdza to jedną sondą na wersji Claude Code, której używa, i podaje jej wynik w opisie prośby (pytanie 3).

### Questions to settle

- 1. Czy typ startuje bez plików instrukcji (`omitClaudeMd: true`)?
  - Answer: nie; pliki instrukcji zostają. Wróci jako osobna decyzja, jeśli zlecenia etapów zaczną same wskazywać plik instrukcji produktu.
  - Not chosen:
    - start bez plików instrukcji — start spada do 10,5 tys. tokenów, ale agent traci naraz globalny plik instrukcji użytkownika (reguły gita, skryptów, prywatności) i plik instrukcji produktu; samego pliku produktu zostawić się nie da.
  - Source: notatka tego zadania przed doprecyzowaniem, sekcja „Otwarte wątki / decyzje”, Mariusz, 2026-11-12, „Na dziś ustalone: pliki instrukcji zostają. Wróci jako osobna decyzja, jeśli zlecenia etapów zaczną same wskazywać plik instrukcji produktu.”
- 2. Który agent cyklu dostaje godzinną pamięć podręczną?
  - Answer: tylko jeden autor; pozostałe typy zostają przy pamięci pięciominutowej.
  - Source: notatka tego zadania przed doprecyzowaniem, sekcja „Co zmienić”, Mariusz, 2026-11-12, „Drugi, dla agenta piszącego zmianę, ma dodatkowo godzinną pamięć podręczną”; karta D26 raportu o usprawnieniach procesu, „Dać jednemu autorowi godzinną pamięć podręczną”, z rachunkiem według rodzaju agenta (Context).
- 3. Ile typów i z jakimi narzędziami?
  - Answer: dwa typy, oba z każdym narzędziem sesji poza narzędziem skilli: typ etapów i ten sam z godzinną pamięcią dla jednego autora; narzędzia przeglądarki ma każdy agent, który ma je w sesji, a cykl potwierdza jedną sondą, że przy tej drodze lista skilli znika.
  - Not chosen:
    - trzy typy, jak w notatce zadania, z wąską listą narzędzi i trzecim typem z narzędziami przeglądarki wpisanymi z nazwy — the way wpisuje do swojego pliku nazwy narzędzi prywatnej wtyczki Playwright, a w produkcie bez niej typ nie ma czym sprawdzić interfejsu; orkiestrator rozstrzyga przy każdym zleceniu, czy etap ogląda interfejs; jeden autor zmiany w interfejsie potrzebuje czwartego typu.
    - dwa wąskie typy, a etapy z interfejsem zwykłym podagentem jak dziś — cykl zmiany w interfejsie nie ma ani lżejszego startu, ani godzinnej pamięci autora; orkiestrator i tak wybiera typ dla każdego etapu.
  - Source: Mariusz przez doradcę dnia, 2026-11-13, „1 b (dwa typy z każdym narzędziem sesji poza narzędziem skilli; cykl potwierdza jedną sondą, że lista skilli znika)”.
- 4. Czy zadanie obejmuje Codexa?
  - Answer: nie; tylko Claude Code, a w Codexie cykl zleca etapy tak jak dziś.
  - Not chosen:
    - także Codex, z typami w `.codex/agents/` — lista wyłączonych skilli rośnie z każdym skillem i trzeba jej pilnować w procesie, a zysku nie pokazała żadna sonda.
  - Source: Mariusz przez doradcę dnia, 2026-11-13, „2 a (tylko Claude Code)”.

## Context

- Źródła, wszystkie w prywatnych notatkach Mariusza: wyniki sondy startu (a private note) i wyniki sondy pamięci (a private note); cztery definicje typów użyte w sondzie, w folderze `pomiary_i_sondy_przed_zmianami_procesu_dane/sonda_startu_i_pamieci/definicje_podagentow/`; karty D4 (a private note) i D26 (a private note) raportu o usprawnieniach procesu.
- Sonda startu: Claude Code 2.1.322, model Sonnet 5.5, kopia gry; start podagenta bez narzędzia skilli spadł z 36 711 do 21 759 tokenów, bo lista skilli (29 896 znaków) zniknęła w całości, definicje narzędzi zmalały z 31 547 znaków (13 narzędzi) do 22 639 (9), a pliki instrukcji (23 658 znaków) zostały.
- Typ z pustą treścią startuje z promptem systemowym 1 722 znaków zamiast 3 158 — nie dziedziczy domyślnego opisu zwykłego podagenta.
- Sonda pamięci: podagent z `cacheTtl: 1h`, wznowiony po 6,9 minuty w żywej sesji, odczytał z pamięci 10 470 tokenów i zapisał 123; kontrolny z pamięcią pięciominutową zapisał całość od nowa (4 786).
- Po ponownym uruchomieniu sesji (`claude -p --resume`) godzinna pamięć nie pomogła: agent zapisał cały kontekst od nowa po stawce 2,0 zamiast 1,25 ceny wejścia, wg jednej próby dwa razy; rachunek zysku tego nie obejmuje.
- Rachunek według rodzaju agenta, na zapisach sesji: godzina dla wszystkich podagentów to +4,7% kosztu cykli gry i −1,4% cykli procesu; tylko dla jednego autora −1,2% w grze i −4,3% w procesie; dla wykonawcy kawałka +1,6% w grze, dla recenzenta całej zmiany +0,4% w grze i +1,0% w procesie. Po korekcie w notatce z wynikami sond: −0,9% gry i −3,6% procesu, a gdy autor nie jest wznawiany, dopłata 0,7% i 2,2%.
- Narzędzia skilli używało 72 z 625 podagentów cykli gry, najczęściej do skilli samego procesu (`the-way-make-change` 30, `the-way-record-decision` 13, `the-way-review-change` 13, skille pozostałych elementów fundamentu 21) i do prywatnego skilla pracy z przeglądarką (`playwright-mcp`, 8); od 6 listopada 13 z 254. Narzędzi przeglądarki użyło 33 z 625.
- Instrukcja cyklu już każe wskazać w zleceniu metodę etapu ścieżką jej `SKILL.md` („the method of the stage by the path of its `SKILL.md` in the pinned the-way”, `task-cycle/skill/SKILL.md`, akapit, który zaczyna się od „Write each dispatch's full handoff”), ale krok 3 tej instrukcji nazywa metody etapów „each a project skill with the `the-way-` prefix”.
- Dokumentacja Claude Code, odczyt 2026-11-13, https://code.claude.com/docs/en/sub-agents.md: typy projektu leżą w `.claude/agents/`; „To prevent a subagent from invoking skills entirely, omit `Skill` from the `tools` list or add it to `disallowedTools`” — że przy tym znika lista skilli, pokazała tylko sonda, i tylko dla drogi przez `tools`, stąd sonda w kryteriach akceptacji.
- Typ z każdym narzędziem sesji poza narzędziem skilli ma start większy o ok. 2 tys. tokenów niż typ z wąską listą narzędzi sondy (szacunek z tabeli definicji narzędzi, niezmierzony), czyli zysk ok. 37% startu zamiast 41%.
- Żaden z typów nie ma narzędzia skilli, więc agent etapu traci prywatny skill `playwright-mcp`.
- Ta sama strona: `experimental.cacheTtl` wymaga wersji 2.1.248, a Claude Code „ignores `1h` while your Claude subscription is using usage credits” — przy dopłatach ponad plan agent wraca do pamięci pięciominutowej; ustawienie użytkownika `subagentPromptCacheTtl` ma pierwszeństwo przed polem definicji.
- Ta sama strona: parametr modelu podany przy wywołaniu ma pierwszeństwo przed polem `model` definicji i obowiązuje też po wznowieniu, więc klasa modelu ustawiana przy zleceniu (WAY-229) działa dalej.
- Ta sama strona: „Hooks from settings files, managed policy settings, and plugins all apply inside subagents, so a `PreToolUse` hook in `settings.json` also runs before every tool a subagent uses” — hook sprawdzający polecenia powłoki obejmuje podagenta własnego typu.
- Ta sama strona: Claude Code śledzi zmiany w `.claude/agents/` bez restartu, ale tylko w katalogu, który istniał przy starcie sesji: „after creating a scope's first agent file in a new `agents` directory, restart to load it”; pole, którego nie zna, pomija bez błędu.
- Codex (https://learn.chatgpt.com/codex/agent-configuration/subagents, odczyt 2026-11-13) ma własne typy agentów w `.codex/agents/*.toml`, bez listy narzędzi, z wyłączaniem pojedynczych skilli po ścieżce; zapisy sesji, z których liczono zysk, nie mają sesji Codexa.
- Skrypt miar cyklu (`task-cycle/cycle_measures.py`) liczy osobno zapis do pamięci na godzinę („Cache written, 1 hour”), więc miary pierwszego cyklu po scaleniu pokażą, czy zapisy jednego autora idą na godzinę.
- Wpis w mapie części o poleceniu instalacji (`installation-command`) wymienia każdy plik, który instalator przepisuje albo usuwa; nowe pliki w `.claude/agents/` ten wpis zmieniają.
- Wyniki sond i rachunek opisuje się we wpisach fundamentu, a nie wskazuje (WAY-27), z tym, co mierzono, i w jakich warunkach (WAY-05).

## Questions carried to cycle

- Gdzie w the way stoją definicje typów jako jedno źródło dla instalatora i dla `.claude/agents/` samego the way, i czy kopie the way generuje skrypt `agent-instructions`, tak jak wejścia skilli, ze sprawdzającym je testem.
- Nazwy typów i brzmienie treści każdego z nich.

## Human actions

none

## Decisions in play

- **WAY-255 — How does an agent of a task's cycle wait for a command that runs long?** Zadanie dopisuje wyjątek dla jednego autora (To do 6).
  > … in Claude Code a subagent's cache lives five minutes by default, so each wait stays under about four. …
  > *Rejected:* … a longer cache lifetime for every agent — it raises the price of each step to spare the few that wait.
- **WAY-125 — Which methods does the autonomous task cycle use?** Bez zmiany; To do 5 ją realizuje także dla skilli elementów.
  > Each agent reads the `SKILL.md` of its stage's method whole, and a file the method names, one beside that `SKILL.md` included, only when the step or variant that names the file comes, while the orchestrator reads no method it does not conduct.
- **WAY-148 — How do task-cycle stages pass their work to the orchestrator?** Bez zmiany; zlecenie dalej idzie plikiem.
  > The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files …
- **WAY-127 — How does a session working on the-way itself reach the-way's skills?** Bez zmiany; wzór dla To do 3.
  > A session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`.
- **WAY-34 — Which version of the process does a product use?** Bez zmiany; definicje typów w produkcie pochodzą z przypiętego commita.
  > A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit.
- **WAY-229 — On which class of model do the executor of a slice and the one author work?** Bez zmiany; klasę ustawia się dalej przy zleceniu.
  > The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class.
- **WAY-347 — How are the measures of how a cycle's agents use context and the prompt cache counted?** Bez zmiany.
  > The measures of how a cycle's agents use the context and the prompt cache of the model — the number of model calls, the size of each call's context, the tokens written to the cache and the tokens written to it again — are counted by a script of their own into a file of their own in the cycle's record …
- **WAY-05 — How is a decision entry written?** Bez zmiany; ogranicza, jak wynik sondy stoi w uzasadnieniu.
  > … a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound …
- **WAY-27 — Where may this repository point for its reasoning?** Bez zmiany; notatka z wynikami sond nie jest wskazywana.
  > Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.

## Settlements to record

Candidates: 3 shown, 3 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Etapy cyklu w Claude Code idą dwoma własnymi typami podagentów z każdym narzędziem sesji poza narzędziem skilli — typem etapów i typem jednego autora z godzinną pamięcią podręczną — więc każdą metodę agent etapu dostaje ścieżką pliku. | decision | pytanie 3 | ile typów zdefiniować, z jakimi narzędziami, i czy agent etapu może jeszcze wywołać skill |
| 2 | Typy podagentów cyklu startują z plikami instrukcji, bez `omitClaudeMd`. | decision | pytanie 1 | czy wyłączyć pliki instrukcji dla dodatkowych 11 tys. tokenów startu |
| 3 | W innej uprzęży niż Claude Code cykl zleca etapy tak jak dziś; the way nie daje Codexowi własnych typów agentów. | decision | pytanie 4 | czy pisać typy dla Codexa w `.codex/agents/` |

## Out of scope

- Sesja cyklu uruchamiana bez ustawień użytkownika i osobny katalog konfiguracji (drogi 1 i 2 z sondy startu) — dotyczą ustawień agentów Mariusza, nie procesu.
- Podagenci, których uruchamiają skille poza cyklem zadania — prowadzenie projektu, krytyka, przegląd fundamentu.
- Odczyt miar pierwszego cyklu po scaleniu, który pokaże godzinną pamięć jednego autora na pełnym cyklu.
