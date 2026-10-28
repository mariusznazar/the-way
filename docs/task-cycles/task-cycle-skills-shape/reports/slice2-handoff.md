# Handoff — Slice 2, task `task-cycle-skills-shape`

You are the executor of one slice of a planned change in a the-way task cycle. The person who
requested this cycle has delegated intermediate choices to the orchestrator; send questions to the
orchestrator in your report, never to the human.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`.
- Slice 2's base: `746da1b620074ea42d26adc4bd6557710ecc8609`. Class of model: `cheaper`.
- **Method:** `make-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/change/SKILL.md`; every file of the process it names (the-way's
  skills, templates, `elements/common/way_of_working.md`, scripts) is read from
  `.runs/the-way-base/` as well. The task requires every agent of this cycle to read the methods of
  its stage from that copy at the base commit (its To do 7), because the task rebuilds them. The
  foundation (`foundations/`), the files you change and the tests are the worktree's.
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/slice2-report.md`.

## Answers of the orchestrator's start

- Trust boundary: no. Irreversible operation: no. No spec was written; the route is planned
  slices. Guidelines: none — the-way has no `guidelines/` (the task settles it).
- The foundation entries of the plan (rows 1–3: changes of WAY-125, WAY-127 and WAY-256) are
  written in commit `40f0fd3`; read them in the worktree at the ranges below.

## Note from the orchestrator

- WAY-127 as changed in `40f0fd3` (range below) gives the wording to follow: "An entry point reads
  its skill, and each file the skill names when the step that names that file comes rather than all
  of them at the start, from the checkout or worktree the session works in".
- The test `test_the_tracked_entry_points_are_what_the_generator_produces` failing on the 36 paths
  of Slices 3–6 after your slice is the plan's expected state, not a failing check of your slice:
  report it by test name with the paths' count.
- To write your six entry points from the generator's own `produce(discover(ROOT))`, a one-off
  in-process call (e.g. `python -B -c ...` importing the module) is how the plan means it; commit
  no script.

## Your section of the plan

Copied word for word from `.runs/task-cycles/task-cycle-skills-shape/plan.md`:

> ### Slice 2 — The entry points' sentence on the files a skill names
>
> - **Goal:** the sentence the generator writes into every entry point
>   (`agent-instructions/skill_entry_points.py:175-176`, "read the files it names under the same root,
>   never a copy in another checkout or worktree") says that a file the skill names is read from the
>   same root when the step or variant that names it comes, not all of them at the start, and never
>   from a copy in another checkout or worktree (*Foundation entries* row 2; task, *To do* 3 and
>   *Questions to settle* 1). The assertion of its test on that sentence
>   (`agent-instructions/test_skill_entry_points.py:52-56`, in `DECISION_ENTRY`) holds the new
>   sentence; it is changed first and seen failing. The sentence keeps the skill's path in backticks
>   and every phrase `gate/test_skills_reach_the_way_sessions.py:32-38` requires, since that test may
>   not change (acceptance criterion 1). `AGENTS.md:9-11` ("each reads its skill and the files it
>   names from the checkout or worktree the session works in") is reworded to the same rule, which
>   the search of row 2 finds; it stays one sentence of the same section. The entry points of
>   `critique`, `define-project` and `find-foundation-entries`, in both tools, are written from the
>   generator's own `produce(discover(ROOT))`, run in process for those six paths only — never by
>   hand and never by `--write`. No other Python changes.
> - **Change:** `agent-instructions/skill_entry_points.py` ·
>   `agent-instructions/test_skill_entry_points.py` · `AGENTS.md` ·
>   `.claude/skills/the-way-critique/SKILL.md` · `.agents/skills/the-way-critique/SKILL.md` ·
>   `.claude/skills/the-way-define-project/SKILL.md` · `.agents/skills/the-way-define-project/SKILL.md` ·
>   `.claude/skills/the-way-find-foundation-entries/SKILL.md` ·
>   `.agents/skills/the-way-find-foundation-entries/SKILL.md`
> - **Read:** `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:42-44` Questions to settle (the first) ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:58-64` Context ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
>   Foundation entries row 2 (WAY-127 as the foundation step changes it) ·
>   `foundations/decisions.md:1059-1093` WAY-44 · `foundations/decisions.md:2963-3011` WAY-128 ·
>   `foundations/decisions.md:3012-3034` WAY-129 · `foundations/invariants.md:241-250`
>   skill-entry-points · `foundations/invariants.md:56-65` derived-file-content ·
>   `foundations/invariants.md:251-260` instruction-file-imports · `foundations/invariants.md:76-85`
>   outbound-link-reach · `gate/test_skills_reach_the_way_sessions.py:1-60`
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** with the assertion changed and the generator not yet,
>   `python -B -m unittest discover -s agent-instructions -p "test_skill_entry_points.py" -k EntryPointText -k Writing`
>   exits 1 on `test_text_is_the_written_out_form`; after the generator's change it exits 0.
>   `python -B agent-instructions/skill_entry_points.py` prints `would change` for exactly the 36
>   paths of Slices 3–6 and nothing else. `python -B gate/run_tests.py gate` exits 0.
>   `python -B gate/run_tests.py agent-instructions` fails only in
>   `test_the_tracked_entry_points_are_what_the_generator_produces` (invariant
>   derived-file-content), on those 36 paths, until Slice 6 — an expected state recorded by test
>   name, not a failing check of this slice. `git diff <base>..HEAD -- "*.py"` shows only the sentence
>   and the assertion. `python -B instruction-files/check_instructions.py .` reports 0 errors.
>   `git diff --check` prints nothing.
> - **Depends on:** Foundation entries row 2

## Current ranges of the foundation entries your *Read* names

Where they differ from the plan's ranges, these hold (the foundation step moved them):

- `foundations/decisions.md:2918-2983` WAY-127
- `foundations/decisions.md:1059-1093` WAY-44
- `foundations/decisions.md:2984-3032` WAY-128
- `foundations/decisions.md:3033-3055` WAY-129
- `foundations/invariants.md:241-250` skill-entry-points
- `foundations/invariants.md:56-65` derived-file-content
- `foundations/invariants.md:251-260` instruction-file-imports
- `foundations/invariants.md:76-85` outbound-link-reach

## Passages your *Read* names, copied word for word

### `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33`

```text
### To do

1. WAY-125 mówi, że agent etapu czyta `SKILL.md` swojej metody w całości, a plik obok dopiero wtedy, gdy przychodzi krok albo wariant, który ten plik wymienia; `implement-task` przestaje kazać agentom etapów czytać na starcie wszystko, co metoda wymienia (dziś krok 3 sekcji „Inputs and authority” i treść zleceń).
2. WAY-256 i `instruction-files/kind_skill.md` mówią, że fragment kroku albo wariantu, który jest jedną instrukcją, zostaje w `SKILL.md` w miejscu, w którym stałby odsyłacz do niego.
3. Pliki wejściowe `the-way-*` każą czytać plik wymieniony przez skill z tego samego repo albo worktree, gdy przychodzi krok, który go wymienia — nie wszystkie naraz na starcie; zmienia się zdanie, które je generuje (`agent-instructions/skill_entry_points.py:175`), jego test, a pliki wejściowe wszystkich skilli są wygenerowane na nowo poleceniem `python -B agent-instructions/skill_entry_points.py --write`.
4. Każdy z pięciu skilli cyklu jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, i przebudowany według tej oceny: w `SKILL.md` obraz całości, zasady wspólne dla kroków i odsyłacze, a fragment potrzebny tylko na jednym kroku albo w jednym wariancie — w pliku obok, który ten krok wymienia.
5. `make-change` dostaje układ z przykładu (`przyklad_make_change.md`, sekcja „Po przebudowie”), z wierszami 5, 9 i 22 jego tabeli jako fragmentami z jedną instrukcją, które zostają w `SKILL.md`.
6. Request zadania podaje przy każdym z pięciu skilli tabelę jego oceny — fragment, kiedy jest potrzebny i czy agent rozpozna ten moment, werdykt — i to, ile słów czyta każdy agent w każdym wariancie przed przebudową i po niej; werdykty „remove” i „reword” zmieniające treść reguły stoją w nim jako propozycje.
7. Agenci cyklu tego zadania czytają metody etapów z kopii the way na commicie bazowym w ignorowanym `.runs/` worktree, nie z gałęzi zadania.
```

### `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38`

```text
### Acceptance criteria

- Kod w Pythonie zmienia się tylko w zdaniu, które generator wejść wkleja do plików wejściowych, i w asercji jego testu na to zdanie (punkt 3).
- Żadna reguła pięciu skilli nie znika ani nie zmienia znaczenia, poza tym, co zmieniają punkty 1–3: każdy fragment stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
```

### `.runs/task-cycles/task-cycle-skills-shape/task.md:42-44`

```text
- Czy zadanie zmienia też zdanie wejść `the-way-*` „read the files it names under the same root”, które agent może wziąć za polecenie wczytania na starcie wszystkich plików obok?
  - Answer: tak — w tym zadaniu, razem ze zmianą WAY-125: to ta sama reguła („plik obok czytasz na jego kroku”) w drugim miejscu, przez które agent dochodzi do skilla; obejmuje wejścia wszystkich skilli the way, także przebudowanego już `maintain-instruction-files`.
  - Source: Mariusz, 2026-10-28: „A” — wybór spośród: A — zmienić zdanie w tym zadaniu (słaby punkt: zadanie dotyka kodu w Pythonie, generatora i jego testu `agent-instructions/test_skill_entry_points.py:53`, a PR rośnie o 42 wygenerowane pliki różniące się jedną linią); B — zostawić (orkiestrator może wczytać na starcie wszystkie pliki obok `implement-task`, a zmierzony cykl na `loop2` nie odróżni zawodu przebudowy od tego zdania); C — osobne małe zadanie przed tym. Brzmienie dziś, np. `.claude/skills/the-way-make-change/SKILL.md:13` na `cf11541`: „Read `task-cycle/change/SKILL.md` there in full and follow it, and read the files it names under the same root, never a copy in another checkout or worktree.” Orkiestrator `implement-task` dochodzi do skilla przez to wejście; agenci etapów — przez zlecenie orkiestratora (punkt 1).
```

### `.runs/task-cycles/task-cycle-skills-shape/task.md:58-64`

```text
## Context

- Zadanie jest pierwszym z jedenastu zadań serii przebudowy skilli the way; ustalenia wspólne serii (kolejność, miara, podział na PR-y, zmiana WAY-125, wyjątek dla jednej instrukcji) stoją w `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_skille_the_way_po_kolei_wedlug_kryterium.md`, sekcja „Ustalone”.
- Pięć skilli idzie jednym zadaniem, bo orkiestrator w zleceniach nazywa pliki etapów, a osobne PR-y dawałyby stany pośrednie (notatka serii; Mariusz, 2026-10-28, „wariant 2”).
- Wzór oceny i układu: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/przyklad_make_change.md` — tabela 22 fragmentów `make-change` na `cf11541` i układ po przebudowie (`SKILL.md` z tabelą wariantów na początku kroku 1, obok `slice.md`, `fix.md`, `ui_check.md`); zysk w `make-change` ok. 15%, bo warianty różnią się kilkoma liniami.
- Miara serii: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/skill_carry_cost.py`, wynik `ranking_2026-10-28.txt` obok; liczy rozmiar tekstu skilla w tokenach razy liczba wywołań modelu, które ten tekst niosły, z zapisów sesji Claude Code od 2026-09-01; po scaleniu ten sam skrypt na zapisach od dnia scalenia daje porównanie.
- Nowe zdanie plików wejściowych musi dalej spełniać niezmiennik `skill-entry-points` (`foundations/invariants.md`), który wymaga, żeby tekst wejścia prowadził sesję do `SKILL.md` w checkoucie albo worktree, w którym pracuje; nie mówi nic o tym, kiedy czytać pliki obok, więc się nie zmienia.
```

### `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93`

```text
## Settlements to record

Candidates: 8 shown, 3 accepted — 2026-10-28

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Agent etapu czyta `SKILL.md` swojej metody w całości, a plik obok skilla dopiero na kroku albo w wariancie, który ten plik wymienia (zmiana WAY-125). | decision | To do 1; notatka serii, „Ustalone” (Mariusz, 2026-10-28, „dopiszmy”; ryzyko przegapionego momentu nazwane tam); przyjęte przez Mariusza 2026-10-28: „tak, przyjmuję” | czy zlecenia dalej każą czytać „what it names, whole”, przez co przeniesienie fragmentów w skillach etapów nic nie daje |
| 2 | Plik wejściowy skilla the way każe czytać plik, który skill wymienia, z tego samego repo albo worktree, gdy przychodzi krok, który go wymienia — nie wszystkie na starcie (zmiana WAY-127). | decision | To do 3; Questions to settle — pytanie o zdanie plików wejściowych (Mariusz, 2026-10-28, „A”); przyjęte przez Mariusza 2026-10-28: „tak, przyjmuję” | czy zmieniać tylko tekst generatora, zostawiając WAY-127 ze zdaniem „reads its skill and the files it names” bez słowa o tym, kiedy |
| 3 | Fragment kroku albo wariantu, który jest jedną instrukcją, zostaje w `SKILL.md` w miejscu, gdzie stałby odsyłacz do niego, bo odsyłacz też jest instrukcją (wyjątek w WAY-256). | decision | To do 2; notatka serii, „Ustalone” (Mariusz, 2026-10-28, „dopiszmy ten wyjątek”; ryzyko furtki i granica „jedna instrukcja przeciw jednemu odsyłaczowi” nazwane tam); przyjęte przez Mariusza 2026-10-28: „tak, przyjmuję” | czy przenosić do pliku obok także jednozdaniowe wiersze wariantów, jak wiersze 5, 9 i 22 przykładu `make-change` |
```

## Your boundary

Make your slice only, commit it on the task branch, keep the worktree clean, and return. Run your
slice's *Checks* and report each with its command and exit code. Do not run `gate/run_tests.py` as a
whole; that run is the orchestrator's (a directory argument is a focused check and allowed). Return
your status (`done`, `done with concerns`, `questions`, `returned` or `blocked`), your commits, a
one-line check result naming what failed or did not run, and your report's path.
