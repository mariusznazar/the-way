# Handoff — Slice 1, task `task-cycle-skills-shape`

You are the executor of one slice of a planned change in a the-way task cycle. The person who
requested this cycle has delegated intermediate choices to the orchestrator; send questions to the
orchestrator in your report, never to the human.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`.
- Slice 1's base: `40f0fd357deadc3818cfc77cf251c2a983db687f`. Class of model: `cheaper`.
- **Method:** `make-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/change/SKILL.md`; every file of the process it names (the-way's
  skills, templates, `elements/common/way_of_working.md`, scripts) is read from
  `.runs/the-way-base/` as well. The task requires every agent of this cycle to read the methods of
  its stage from that copy at the base commit (its To do 7), because the task rebuilds them. The
  foundation (`foundations/`), the files you change and the tests are the worktree's.
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/slice1-report.md`.

## Answers of the orchestrator's start

- Trust boundary: no. Irreversible operation: no. No spec was written; the route is planned
  slices. Guidelines: none — the-way has no `guidelines/` (the task settles it).
- The foundation entries of the plan (rows 1–3: changes of WAY-125, WAY-127 and WAY-256) are
  written in commit `40f0fd3`; read them in the worktree at the ranges below.

## Note from the foundation step

WAY-256 as changed in `40f0fd3` bounds the exception to a fragment "which would otherwise stand in a
file beside the skill" — so that it does not reach the rules WAY-35 places in an element's template.
`kind_skill.md` states the exception within that bound and cites WAY-256.

## Your section of the plan

Copied word for word from `.runs/task-cycles/task-cycle-skills-shape/plan.md`:

> ### Slice 1 — The exception for a one-instruction fragment in the file of skills
>
> - **Goal:** `instruction-files/kind_skill.md`, in its section "Where a fragment of a skill stands",
>   says that a fragment only one step or one variant needs, which is one instruction, stays in
>   `SKILL.md` where its pointer would stand, since the pointer is an instruction too — the exception
>   *Foundation entries* row 3 adds to WAY-256 — citing WAY-256. The rule stands in that file alone
>   (WAY-258): `instruction-files/SKILL.md` and the other files of that skill do not change. Process
>   prose; no test asserts it.
> - **Change:** `instruction-files/kind_skill.md`
> - **Read:** `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
>   `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-61` Ustalone (Wzór) ·
>   Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
>   `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:7298-7331` WAY-258 ·
>   `instruction-files/SKILL.md:97-151` Where a rule stands
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** `git diff --stat <base>..HEAD` names `instruction-files/kind_skill.md` alone;
>   `grep -n "WAY-256" instruction-files/*.md` shows the exception in `kind_skill.md` only;
>   `python -B instruction-files/check_instructions.py .` reports 0 errors;
>   `python -B gate/run_tests.py instruction-files` exits 0; `git diff --check` prints nothing.
> - **Depends on:** Foundation entries row 3

## Current ranges of the foundation entries your *Read* names

Where they differ from the plan's ranges, these hold (the foundation step moved them):

- `foundations/decisions.md:7246-7304` WAY-256
- `foundations/decisions.md:7305-7329` WAY-257
- `foundations/decisions.md:7330-7410` WAY-258

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

### `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-61`

```text
- **Wzór: przykład `make-change`, z wyjątkiem dla fragmentu z jedną instrukcją.** Tabela ocen i układ po przebudowie: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/przyklad_make_change.md` — w `SKILL.md` obraz całości, tabela wariantów na początku kroku 1, część wspólna; obok `slice.md`, `fix.md`, `ui_check.md`. Fragment wariantu albo kroku, który jest jedną instrukcją, zostaje w `SKILL.md` w miejscu, gdzie stałby odsyłacz do niego: odsyłacz też jest instrukcją, więc plik obok nie zmniejszyłby liczby instrukcji naraz, a dołożyłby plik do utrzymania. Wyjątek dochodzi do WAY-256 i do `instruction-files/kind_skill.md` w zadaniu 1, razem ze zmianą WAY-125. Ryzyko: „to tylko jedna instrukcja” jako furtka do zostawiania wszystkiego; granica jest policzalna — jedna instrukcja przeciw jednemu odsyłaczowi. Przykład pokazał też, że w `make-change` zysk jest mały (ok. 15%, z 12 do ok. 10 mln tokenów w mierze serii), bo warianty różnią się kilkoma liniami; duży zysk leży w `implement-task`. Źródło: Mariusz, 2026-10-28, „dopiszmy ten wyjątek”.
```

## Your boundary

Make your slice only, commit it on the task branch, keep the worktree clean, and return. Run your
slice's *Checks* and report each with its command and exit code. Do not run `gate/run_tests.py` as a
whole; that run is the orchestrator's (a directory argument is a focused check and allowed). Return
your status (`done`, `done with concerns`, `questions`, `returned` or `blocked`), your commits, a
one-line check result naming what failed or did not run, and your report's path.
