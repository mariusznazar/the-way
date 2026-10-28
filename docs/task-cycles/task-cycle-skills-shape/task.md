---
title: "the way, seria skilli 1/11: pięć skilli cyklu zadania w kształcie WAY-256, ze zmianą WAY-125"
status: draft
created: 2026-10-28
updated: 2026-10-28
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Pięć skilli cyklu zadania w kształcie WAY-256, ze zmianą WAY-125 i wyjątkiem dla fragmentu z jedną instrukcją

Status: ready for cycle
Project relation: independent

## Description

### Need

- Pięć skilli cyklu zadania the way — `implement-task` (`task-cycle/skill/SKILL.md`, 6605 słów), `plan-task` (`task-cycle/plan/SKILL.md`, 2178), `review-change` (`task-cycle/review/SKILL.md`, 1860), `make-change` (`task-cycle/change/SKILL.md`, 1777) i `write-spec` (`task-cycle/spec/SKILL.md`, 1066) — trzyma w `SKILL.md` także fragmenty potrzebne tylko na jednym kroku albo w jednym wariancie, choć WAY-256 każe takie fragmenty trzymać w plikach obok (stan na `foundations` `cf11541`).
- Agenci nieśli tekst tych pięciu skilli przez ok. 83,5 mln tokenów od 2026-09-01, najwięcej ze wszystkich skilli the way; sam skill orkiestratora `implement-task` — 61,1 mln (miara serii, `ranking_2026-10-28.txt`).
- WAY-125 każe dziś agentowi etapu czytać na starcie swoją metodę i wszystko, co ona wymienia, więc w skillach etapów przeniesienie fragmentu do pliku obok niczego nie zmienia — agent i tak wczyta go od razu.
- Pliki wejściowe skilli `the-way-*` każą czytać skill „and the files it names” bez słowa o tym, kiedy, więc orkiestrator, który dochodzi do `implement-task` przez taki plik, może wczytać na starcie wszystkie pliki obok.
- WAY-256 nie mówi, co z fragmentem, który jest jedną instrukcją: przeniesiony do pliku obok zostawiłby w `SKILL.md` odsyłacz, który też jest instrukcją — liczba instrukcji naraz nie spada, a plików do utrzymania przybywa.

### To do

1. WAY-125 mówi, że agent etapu czyta `SKILL.md` swojej metody w całości, a plik obok dopiero wtedy, gdy przychodzi krok albo wariant, który ten plik wymienia; `implement-task` przestaje kazać agentom etapów czytać na starcie wszystko, co metoda wymienia (dziś krok 3 sekcji „Inputs and authority” i treść zleceń).
2. WAY-256 i `instruction-files/kind_skill.md` mówią, że fragment kroku albo wariantu, który jest jedną instrukcją, zostaje w `SKILL.md` w miejscu, w którym stałby odsyłacz do niego.
3. Pliki wejściowe `the-way-*` każą czytać plik wymieniony przez skill z tego samego repo albo worktree, gdy przychodzi krok, który go wymienia — nie wszystkie naraz na starcie; zmienia się zdanie, które je generuje (`agent-instructions/skill_entry_points.py:175`), jego test, a pliki wejściowe wszystkich skilli są wygenerowane na nowo poleceniem `python -B agent-instructions/skill_entry_points.py --write`.
4. Każdy z pięciu skilli cyklu jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a fragment potrzebny tylko na jednym kroku albo w jednym wariancie — w pliku obok, który ten krok wymienia.
5. `make-change` dostaje układ z przykładu (`przyklad_make_change.md`, sekcja „Po przebudowie”), z wierszami 5, 9 i 22 jego tabeli jako fragmentami z jedną instrukcją, które zostają w `SKILL.md`.
6. Request zadania podaje przy każdym z pięciu skilli tabelę jego oceny — fragment, kiedy jest potrzebny i czy agent rozpozna ten moment, werdykt — i to, ile słów czyta każdy agent w każdym wariancie przed przebudową i po niej; werdykty „remove” i „reword” zmieniające treść reguły stoją w nim jako propozycje.
7. Agenci cyklu tego zadania czytają metody etapów z kopii the way na commicie bazowym w ignorowanym `.runs/` worktree, nie z gałęzi zadania.

### Acceptance criteria

- Kod w Pythonie zmienia się tylko w zdaniu, które generator wejść wkleja do plików wejściowych, i w asercji jego testu na to zdanie (punkt 3).
- Żadna reguła pięciu skilli nie znika ani nie zmienia znaczenia, poza tym, co zmieniają punkty 1–3: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.

### Questions to settle

- Czy zadanie zmienia też zdanie wejść `the-way-*` „read the files it names under the same root”, które agent może wziąć za polecenie wczytania na starcie wszystkich plików obok?
  - Answer: tak — w tym zadaniu, razem ze zmianą WAY-125: to ta sama reguła („plik obok czytasz na jego kroku”) w drugim miejscu, przez które agent dochodzi do skilla; obejmuje wejścia wszystkich skilli the way, także przebudowanego już `maintain-instruction-files`.
  - Source: Mariusz, 2026-10-28: „A” — wybór spośród: A — zmienić zdanie w tym zadaniu (słaby punkt: zadanie dotyka kodu w Pythonie, generatora i jego testu `agent-instructions/test_skill_entry_points.py:53`, a PR rośnie o 42 wygenerowane pliki różniące się jedną linią); B — zostawić (orkiestrator może wczytać na starcie wszystkie pliki obok `implement-task`, a zmierzony cykl na `loop2` nie odróżni zawodu przebudowy od tego zdania); C — osobne małe zadanie przed tym. Brzmienie dziś, np. `.claude/skills/the-way-make-change/SKILL.md:13` na `cf11541`: „Read `task-cycle/change/SKILL.md` there in full and follow it, and read the files it names under the same root, never a copy in another checkout or worktree.” Orkiestrator `implement-task` dochodzi do skilla przez to wejście; agenci etapów — przez zlecenie orkiestratora (punkt 1).
- Czy zadanie, które przez punkt 3 zmienia kod w Pythonie, czeka na wytyczne kodowania samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak dotychczasowe zadania the way z kodem; wybór wytycznych jest pusty, a sprawa wytycznych samego the way zostaje w swoim zadaniu, `wlasne_wytyczne_the_way.md`.
  - Source: Mariusz, 2026-10-28: „A” — wybór spośród: A — droga z README, wybór wytycznych pusty (słaby punkt: reguła WAY-215 i praktyka dalej się rozjeżdżają); B — czekać na rozstrzygnięcie `wlasne_wytyczne_the_way.md` (seria stoi). Brzmienie `product-guidelines/reading.md` na `cf11541`: „code work in a product with no `guidelines/coding.md` […] lacks discipline guidelines”; zmiana w kodzie dotyczy tylko tekstu, który generator wkleja do plików wejściowych, i asercji testu na ten tekst.
- Kto projektuje układ każdego z pięciu skilli po przebudowie i gdzie Mariusz widzi tabele ocen przed scaleniem?
  - Answer: cykl — ocenia każdy skill skillem `the-way-maintain-instruction-files` i rozkłada fragmenty sam, z przykładem `make-change` jako wzorem; `make-change` idzie według przykładu; Mariusz widzi tabele ocen i liczby czytanych słów w requeście. Cykl nie pisze kodu poza zdaniem generatora wejść i jego testem, żeby nowy kod nie wrócił jako brak wytycznych w połowie cyklu.
  - Source: Mariusz, 2026-10-28: „no dobrze, ale jeśli pójdziemy w B - tak by było ok”, a po wyjaśnieniu, że wytyczne wróciłyby tylko przy nowym kodzie, na propozycję „B z dopiskiem (i)”: „ok” — wybór spośród: A — tabele i układy wszystkich czterech skilli w doprecyzowaniu (słaby punkt: kilka godzin sesji, opis zadania staje się projektem wykonania wbrew `project-level/task/skill/SKILL.md:239`); B — projektuje cykl, tabele w requeście (słaby punkt: niezgoda z układem wraca dopiero korektą dużego PR-a); C — w doprecyzowaniu tylko `implement-task`; dopisek (i) — cykl nie pisze kodu poza generatorem, skrypt sprawdzający odsyłacze poza zakresem — przeciw (ii) — cykl może dopisać taki skrypt (nowy kod bez wytycznych). Kontakt cyklu z człowiekiem: `task-cycle/skill/SKILL.md:16` na `cf11541`: „The cycle has one ordinary human contact: the request.”; zatrzymanie przy nowym kodzie: `product-guidelines/reading.md`, sekcja „Hand the findings back”: „one that changes what the task needs stops the cycle, which opens a blocked draft request showing it”.
- Z której wersji metod etapów korzysta cykl, który te metody przebudowuje — z gałęzi zadania czy z commitu bazowego?
  - Answer: z commitu bazowego — orkiestrator robi w ignorowanym `.runs/` worktree kopię the way na commicie bazowym, a każde zlecenie podaje ścieżkę metody w tej kopii; nowy układ sprawdza zmierzony cykl na `loop2`, nie ten cykl.
  - Source: Mariusz, 2026-10-28: „A” — wybór spośród: A — metody z kopii commitu bazowego (słaby punkt: krok więcej na starcie, odstępstwo od cyklu zadania A, nowy układ niewypróbowany w tym cyklu); B — metody z worktree zadania (wada przebudowy osłabia przegląd tej samej przebudowy, kolejne kawałki pracują w stanach pośrednich). Zlecenie autora w zadaniu A, `docs/task-cycles/instruction-files-router/reports/author-handoff.md` na `8eec20a`: „read `task-cycle/change/SKILL.md` of this worktree whole, with every file it names”.
- Czy przebudowa tylko przenosi treść i dopisuje odsyłacze, czy może też usuwać albo zmieniać treść reguł?
  - Answer: cykl wykonuje sam tylko werdykty „keep” i „move” oraz przeredagowania, które nie zmieniają znaczenia — zdanie odsyłacza, wiersz tabeli wariantów, fragment z jedną instrukcją w miejscu odsyłacza; werdykty „remove” i „reword” zmieniające treść reguły idą do requestu jako propozycje, bez zmiany w plikach.
  - Source: Mariusz, 2026-10-28: „A” — wybór spośród: A — cykl wykonuje tylko przeniesienia i przeredagowania bez zmiany znaczenia, reszta jako propozycje w requeście (słaby punkt: znalezione zbędne reguły czekają na osobną zmianę); B — cykl wykonuje wszystkie werdykty (dwa rodzaje zmian w jednym PR-ze, pomiar na `loop2` nie odróżni zysku z kształtu od zysku z usuniętej treści). `instruction-files/judging.md:28` na `cf11541`: „The table is a batch of decisions; edit nothing until it is accepted.”; `agent-instructions/README.md`, sekcja „Make the change”: poprawka, która zmieniałaby znaczenie przyjętej decyzji ponad to, co ustala zadanie, idzie do Mariusza, zanim zmiana pójdzie dalej.

## Context

- Zadanie jest pierwszym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, zmiana WAY-125, wyjątek dla jednej instrukcji) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Pięć skilli idzie jednym zadaniem, bo orkiestrator w zleceniach nazywa pliki etapów, a osobne PR-y dawałyby stany pośrednie (notatka serii; Mariusz, 2026-10-28, „wariant 2”).
- Wzór oceny i układu: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/przyklad_make_change.md` — tabela 22 fragmentów `make-change` na `cf11541` i układ po przebudowie (`SKILL.md` z tabelą wariantów na początku kroku 1, obok `slice.md`, `fix.md`, `ui_check.md`); zysk w `make-change` ok. 15%, bo warianty różnią się kilkoma liniami.
- Miara serii: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/skill_carry_cost.py`, wynik `ranking_2026-10-28.txt` obok; liczy rozmiar tekstu skilla w tokenach razy liczba wywołań modelu, które ten tekst niosły, z zapisów sesji Claude Code od 2026-09-01; po scaleniu ten sam skrypt na zapisach od dnia scalenia daje porównanie.
- Nowe zdanie plików wejściowych musi dalej spełniać niezmiennik `skill-entry-points` (`foundations/invariants.md`), który wymaga, żeby tekst wejścia prowadził sesję do `SKILL.md` w checkoucie albo worktree, w którym pracuje; nie mówi nic o tym, kiedy czytać pliki obok, więc się nie zmienia.

## Questions carried to cycle

- Gdzie po przebudowie stoją krok fundamentu i krok powrotu, które dziś zlecenie wskazuje jako akapit `implement-task` czytany w całości (`task-cycle/skill/SKILL.md:131–133` na `cf11541`): w `SKILL.md` czy w pliku obok, który zlecenie wymienia.
- Czy szablon zapisu cyklu `task-cycle/record_template.md` (1901 słów), który orkiestrator czyta na kroku zakładania zapisu (`task-cycle/skill/SKILL.md:120`), jest oceniany razem z `implement-task`; miara serii go nie liczy, bo liczy tylko `SKILL.md`.

## Human actions

none

## Decisions in play

- **WAY-125** — „The task cycle `implement-task` uses the-way's own methods: `write-spec` for a spec and its review, `plan-task` for a plan, `make-change` for each change an author, a slice's executor or a fix makes, and `review-change` for each code review; the orchestrator conducts the cycle and its loop of slices itself. Each agent reads the method of its stage, and what it names, whole, while the orchestrator reads no method it does not conduct.” — zmienia się (wiersz 1).
- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. Fragments that stand unchanged are not bound by it.” — dostaje wyjątek (wiersz 3).
- **WAY-127** (fragment) — „An entry point reads its skill and the files it names from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix.” — zmienia się (wiersz 2).
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.”
- **WAY-35** — „An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them; the way of working the skills share stands once in that part, and a skill reads the rules and that way of working from there instead of restating them.”
- **WAY-148** (fragment) — „The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files”.
- **WAY-150** (fragment) — „every other agent of the cycle reads what its handoff names and reaches for what is missing selectively”.

## Settlements to record

Candidates: 8 shown, 3 accepted — 2026-10-28

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Agent etapu czyta `SKILL.md` swojej metody w całości, a plik obok skilla dopiero na kroku albo w wariancie, który ten plik wymienia (zmiana WAY-125). | decision | To do 1; notatka serii, „Ustalone” (Mariusz, 2026-10-28, „dopiszmy”; ryzyko przegapionego momentu nazwane tam); przyjęte przez Mariusza 2026-10-28: „tak, przyjmuję” | czy zlecenia dalej każą czytać „what it names, whole”, przez co przeniesienie fragmentów w skillach etapów nic nie daje |
| 2 | Plik wejściowy skilla the way każe czytać plik, który skill wymienia, z tego samego repo albo worktree, gdy przychodzi krok, który go wymienia — nie wszystkie na starcie (zmiana WAY-127). | decision | To do 3; Questions to settle — pytanie o zdanie plików wejściowych (Mariusz, 2026-10-28, „A”); przyjęte przez Mariusza 2026-10-28: „tak, przyjmuję” | czy zmieniać tylko tekst generatora, zostawiając WAY-127 ze zdaniem „reads its skill and the files it names” bez słowa o tym, kiedy |
| 3 | Fragment kroku albo wariantu, który jest jedną instrukcją, zostaje w `SKILL.md` w miejscu, gdzie stałby odsyłacz do niego, bo odsyłacz też jest instrukcją (wyjątek w WAY-256). | decision | To do 2; notatka serii, „Ustalone” (Mariusz, 2026-10-28, „dopiszmy ten wyjątek”; ryzyko furtki i granica „jedna instrukcja przeciw jednemu odsyłaczowi” nazwane tam); przyjęte przez Mariusza 2026-10-28: „tak, przyjmuję” | czy przenosić do pliku obok także jednozdaniowe wiersze wariantów, jak wiersze 5, 9 i 22 przykładu `make-change` |

## Out of scope

- Zmierzony cykl na `loop2` po scaleniu — krok 4 lekcji s01e02 w mapie Mega.DEV; `loop2` przesuwa przypięcie the way tylko przed nim (notatka serii, „Ustalone”).
- Przestawienie nośnika wierszy E16 i E17 sekcji s01e02 w `Notes/Projects/(P) Przejście Mega.DEV/mapa_pakietu_mega_dev.md` na numer WAY-125 — krok po scaleniu, nie cykl tego zadania.
- Pozostałe skille the way — zadania 2–11 serii.
- Skrypt albo test, który sprawdza, że każdy plik obok skilla jest wymieniony w którymś jego kroku — osobny pomysł na własne zadanie; w tym zadaniu pilnuje tego recenzent i tabele ocen w requeście (Mariusz, 2026-10-28).
