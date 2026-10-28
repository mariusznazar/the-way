# Handoff — Slice 9, task `task-cycle-skills-shape`

You are the executor of one slice of a planned change in a the-way task cycle. The person who
requested this cycle has delegated intermediate choices to the orchestrator; send questions to the
orchestrator in your report, never to the human.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`.
- Slice 9's base: `bf75d1cc3f59ab3144dc362b4932f3658e71d7fe`. Class of model: `strongest`.
- **Method:** `make-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/change/SKILL.md`; every file of the process it names (the-way's
  skills, templates, `elements/common/way_of_working.md`, scripts) is read from
  `.runs/the-way-base/` as well. The task requires every agent of this cycle to read the methods of
  its stage from that copy at the base commit (its To do 7), because the task rebuilds them. The
  foundation (`foundations/`), the files you change and the tests are the worktree's.
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/slice9-report.md`.

## Answers of the orchestrator's start

- Trust boundary: no. Irreversible operation: no. No spec was written; the route is planned
  slices. Guidelines: none — the-way has no `guidelines/` (the task settles it).
- The foundation entries of the plan (rows 1–3: changes of WAY-125, WAY-127 and WAY-256) are
  written in commit `40f0fd3`; read them in the worktree at the ranges below.

## Notes from the orchestrator

- WAY-125 as changed in `40f0fd3` reads: "Each agent reads the `SKILL.md` of its stage's method
  whole, and a file the method names, one beside that `SKILL.md` included, only when the step or
  variant that names the file comes". It reaches every file a method names, not only one beside
  `SKILL.md` (the cycle's choice C19, from the task's To do 1). Judge each fragment against it.
- WAY-256 as changed in `40f0fd3` bounds the one-instruction exception to a fragment "which would
  otherwise stand in a file beside the skill"; `instruction-files/kind_skill.md` in the worktree
  states it since Slice 1 (`746da1b`). You judge with the base copy's `maintain-instruction-files`
  and apply that exception (plan, *Common to the rebuild slices*, point 1).
- Words read before and after (report, point 7c): count the words of the files each variant's
  agent reads from the skill's directory — before, `SKILL.md` at `cf11541`; after, `SKILL.md` plus
  the files beside it its variant's steps name.
- The rebuild changes where text stands, not what it says. Where you are unsure whether a move
  changes a rule's meaning, keep the text in place and name the doubt in the report.
- Slice 7 (`9b776fe`) rebuilt `make-change` already: `task-cycle/change/SKILL.md` opens step 1 with
  a table of variants and names `slice.md`, `fix.md` and `ui_check.md`. Its executor found that a
  table of variants plus pointer rows cost about 150 words in `SKILL.md`, so a variant that still
  reads its file beside the skill can read more than before; weigh that cost per fragment as
  WAY-256 and the one-instruction exception give.
- Slice 8 (`bf75d1c`) rebuilt `write-spec` with a pointer at each step that needs its file
  (`design.md`, `review.md`) rather than a table of variants, since each variant there is a whole
  step. Choose whichever form fits `plan-task`'s variants and name why.
- The foundation step's search noted `task-cycle/plan/SKILL.md:116` and `:170` ("*Read* is the
  whole reading of the slice's agent"): make sure the rebuilt text cannot be read as forbidding a
  slice's agent the files its method's steps name — without changing that rule's meaning; a doubt
  goes to the report.

## Your section of the plan

Copied word for word from `.runs/task-cycles/task-cycle-skills-shape/plan.md`:

> ### Slice 9 — `plan-task` judged and rebuilt
>
> - **Goal:** `task-cycle/plan/` is judged and rebuilt as "Common to the rebuild slices" gives. Its
>   agent is the planner: of a first plan, of a plan after a reviewed spec, after a one-author attempt
>   proved too large, and after a slice proved too large (`task-cycle/plan/SKILL.md:21-27`, `:186-196`).
>   The form of the plan in step 3 stays in `SKILL.md` word for word: `task-cycle/slice_size.py:10`
>   names `task-cycle/plan/SKILL.md` as its place, and acceptance criterion 1 leaves that script as it
>   is.
> - **Change:** `task-cycle/plan/SKILL.md`, and each file beside it in task-cycle/plan/ that the
>   judgment creates, named by the executor
> - **Read:** `.runs/task-cycles/task-cycle-skills-shape/plan.md:26-87` Common to the rebuild slices ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:25-33` To do ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:35-38` Acceptance criteria ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:48-50` Questions to settle (the third) ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:54-56` Questions to settle (the fifth) ·
>   `.runs/task-cycles/task-cycle-skills-shape/task.md:85-93` Settlements to record ·
>   `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md` ·
>   `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-63` Ustalone (Wzór;
>   Przebudowa zmienia miejsce reguł) · Foundation entries row 1 (WAY-125 as the foundation step
>   changes it) · Foundation entries row 3 (WAY-256 as the foundation step changes it) ·
>   `foundations/decisions.md:7273-7297` WAY-257 · `foundations/decisions.md:3012-3034` WAY-129 ·
>   `foundations/decisions.md:3273-3349` WAY-136 · `foundations/decisions.md:3766-3825` WAY-148 ·
>   `foundations/decisions.md:3826-3885` WAY-150 · `foundations/decisions.md:6172-6249` WAY-229 ·
>   `foundations/invariants.md:76-85` outbound-link-reach ·
>   `.runs/the-way-base/instruction-files/SKILL.md` ·
>   `.runs/the-way-base/instruction-files/judging.md` ·
>   `.runs/the-way-base/instruction-files/kind_skill.md` ·
>   `.runs/the-way-base/instruction-files/tool_loading.md` · `task-cycle/slice_size.py:1-45` ·
>   `task-cycle/skill/SKILL.md:128-196` Inputs and authority, handoffs and returns ·
>   `task-cycle/skill/SKILL.md:198-255` Design and execution choice
> - **Model:** strongest — each verdict judges whether an agent of the cycle recognises the moment a
>   fragment is for, and a wrong "move" switches a rule off without a sign (WAY-128), which the
>   sentence comparison cannot catch: design judgment over the skill's layout.
> - **Risk:** none
> - **Checks:** the checks of "Common to the rebuild slices", point 8, with `<dir>` = `plan`; and
>   `git diff cf11541 -- task-cycle/plan/SKILL.md` shows no line changed inside the fenced form of
>   step 3.
> - **Depends on:** Foundation entries row 1 · Foundation entries row 3 · Slice 6

## Current ranges of the foundation entries your *Read* names

Where they differ from the plan's ranges, these hold (the foundation step moved them):

- `foundations/decisions.md:2837-2875` WAY-125
- `foundations/decisions.md:7246-7304` WAY-256
- `foundations/decisions.md:7305-7329` WAY-257
- `foundations/decisions.md:3033-3055` WAY-129
- `foundations/decisions.md:3294-3370` WAY-136
- `foundations/decisions.md:3787-3846` WAY-148
- `foundations/decisions.md:3847-3906` WAY-150
- `foundations/decisions.md:6193-6270` WAY-229
- `foundations/invariants.md:76-85` outbound-link-reach

## Passages your *Read* names, copied word for word

### `.runs/task-cycles/task-cycle-skills-shape/plan.md:26-87`

```text
## Common to the rebuild slices

This section binds Slices 7–11; each of them names it in its *Read*. Each of those slices judges
one skill of the task cycle and rebuilds it by that judgment (task, *To do* 4).

1. **Method.** `maintain-instruction-files` of the base copy,
   `.runs/the-way-base/instruction-files/SKILL.md`, in the mode judge, for the kind skill — with
   `judging.md`, `kind_skill.md` and `tool_loading.md` of that copy as it names them — never the
   worktree's `instruction-files/`, which Slice 1 changes. Apply it with the exception of
   *Foundation entries* row 3: a fragment of one step or one variant that is one instruction stays in
   `SKILL.md` where its pointer would stand; the bound is one instruction against one pointer.
2. **What step 1 of that method asks of the repository as a whole is settled here, not asked.** The
   tools are Claude Code and Codex (`AGENTS.md:9-10`). Configuration settings and where sessions
   start are not read: the judgment is of one skill, which its agent loads from its handoff or, for
   `implement-task`, through its entry point. Session records are not searched: the ground of each
   row is the decision or the step of the cycle the fragment carries, as the example's column
   "Podstawa" gives it. A "remove" or "reword" proposal names the condition of "When to remove a
   rule" (`judging.md`) it rests on and says that no session records were searched.
3. **Who reads the skill and in which variants** comes from the skill's own text and from the
   places of `task-cycle/skill/SKILL.md` that dispatch it, which the slice's *Read* names.
4. **The table's acceptance is given by the task in advance** (*Questions to settle* 3 and 5), in
   place of the acceptance `judging.md` waits for: carry out without waiting the verdicts "keep" and
   "move" and the rewordings that change no meaning — a pointer's sentence, a row of a table of
   variants, a fragment of one instruction in place of its pointer. A "remove" or "reword" that
   changes a rule's content is a proposal in the report, with no edit.
5. **Layout.** `SKILL.md` keeps its frontmatter unchanged, the picture of the whole, the rules of
   working that hold across its steps and the pointers. A fragment that only one step or one variant
   needs goes to a file beside `SKILL.md`, in the skill's own directory, which that step or variant
   names by its path in backticks with the condition under which to read it (WAY-129), one level
   deep: no file beside the skill points to another. The names of those files are the executor's,
   each named in the report. A skill whose judgment moves nothing stays as it is, its table showing
   why.
6. **Text.** Every sentence of the skill at the base stands after the rebuild, word for word, in
   `SKILL.md` or in a file beside it, except the rewordings of point 4 and what the slice's *Goal*
   changes (acceptance criterion 2). No link into a private note collection enters the skill
   (invariant `outbound-link-reach`): the task's sources are private notes, and none of their paths
   goes into the-way. No script, test or other code is written (task, *Questions to settle* 3;
   *Out of scope*).
7. **Report**, besides what `make-change` asks: (a) the table in the form `judging.md` gives, one row
   per fragment — the fragment with `file:line` at the base, when an agent needs it and whether it
   recognises that moment (WAY-257), the verdict, the reason and the ground; (b) the "remove" and
   "reword" proposals apart, with no edit; (c) for each agent that reads the skill and each variant
   it works in, the words it reads before the rebuild and after it, counted with `wc -w` over the
   files that variant reads, the commands given; (d) the sentence comparison of the checks below,
   each line it prints accounted for; (e) the contradictions found between the skill and the places
   of `task-cycle/skill/SKILL.md` it read, or that none were found.
8. **Checks common to these slices**, with `<dir>` the skill's directory under `task-cycle/` and the
   outputs kept under `.runs/task-cycles/task-cycle-skills-shape/reports/`:
   - the sentence comparison (acceptance criterion 2):
     `git show cf11541:task-cycle/<dir>/SKILL.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > <slice>-before.txt`,
     the same pipeline over `cat task-cycle/<dir>/*.md` into `<slice>-after.txt`, then
     `comm -3 <slice>-before.txt <slice>-after.txt`; every line it prints is accounted for in the
     report by a row of the table (a rewording that changes no meaning, a pointer, a row of the table
     of variants) or by the slice's *Goal*;
   - for each file beside the skill, `grep -n '<file>' task-cycle/<dir>/SKILL.md` shows it named at
     the step or variant that needs it, and `ls task-cycle/<dir>/` shows every file `SKILL.md`
     names beside it;
   - `git diff cf11541 -- task-cycle/<dir>/SKILL.md` leaves lines 1–4, the frontmatter, unchanged,
     and `python -B agent-instructions/skill_entry_points.py` prints `entry points are current` with
     exit code 0;
   - `grep -rn -E "Storage|The Brain|_zadania|Notes/" task-cycle/<dir>/` prints nothing;
   - `python -B gate/run_tests.py task-cycle` exits 0, and `git diff --check` prints nothing.
```

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

### `.runs/task-cycles/task-cycle-skills-shape/task.md:48-50`

```text
- Kto projektuje układ każdego z pięciu skilli po przebudowie i gdzie Mariusz widzi tabele ocen przed scaleniem?
  - Answer: cykl — ocenia każdy skill skillem `the-way-maintain-instruction-files` i rozkłada fragmenty sam, z przykładem `make-change` jako wzorem; `make-change` idzie według przykładu; Mariusz widzi tabele ocen i liczby czytanych słów w requeście. Cykl nie pisze kodu poza zdaniem generatora wejść i jego testem, żeby nowy kod nie wrócił jako brak wytycznych w połowie cyklu.
  - Source: Mariusz, 2026-10-28: „no dobrze, ale jeśli pójdziemy w B - tak by było ok”, a po wyjaśnieniu, że wytyczne wróciłyby tylko przy nowym kodzie, na propozycję „B z dopiskiem (i)”: „ok” — wybór spośród: A — tabele i układy wszystkich czterech skilli w doprecyzowaniu (słaby punkt: kilka godzin sesji, opis zadania staje się projektem wykonania wbrew `project-level/task/skill/SKILL.md:239`); B — projektuje cykl, tabele w requeście (słaby punkt: niezgoda z układem wraca dopiero korektą dużego PR-a); C — w doprecyzowaniu tylko `implement-task`; dopisek (i) — cykl nie pisze kodu poza generatorem, skrypt sprawdzający odsyłacze poza zakresem — przeciw (ii) — cykl może dopisać taki skrypt (nowy kod bez wytycznych). Kontakt cyklu z człowiekiem: `task-cycle/skill/SKILL.md:16` na `cf11541`: „The cycle has one ordinary human contact: the request.”; zatrzymanie przy nowym kodzie: `product-guidelines/reading.md`, sekcja „Hand the findings back”: „one that changes what the task needs stops the cycle, which opens a blocked draft request showing it”.
```

### `.runs/task-cycles/task-cycle-skills-shape/task.md:54-56`

```text
- Czy przebudowa tylko przenosi treść i dopisuje odsyłacze, czy może też usuwać albo zmieniać treść reguł?
  - Answer: cykl wykonuje sam tylko werdykty „keep” i „move” oraz przeredagowania, które nie zmieniają znaczenia — zdanie odsyłacza, wiersz tabeli wariantów, fragment z jedną instrukcją w miejscu odsyłacza; werdykty „remove” i „reword” zmieniające treść reguły idą do requestu jako propozycje, bez zmiany w plikach.
  - Source: Mariusz, 2026-10-28: „A” — wybór spośród: A — cykl wykonuje tylko przeniesienia i przeredagowania bez zmiany znaczenia, reszta jako propozycje w requeście (słaby punkt: znalezione zbędne reguły czekają na osobną zmianę); B — cykl wykonuje wszystkie werdykty (dwa rodzaje zmian w jednym PR-ze, pomiar na `loop2` nie odróżni zysku z kształtu od zysku z usuniętej treści). `instruction-files/judging.md:28` na `cf11541`: „The table is a batch of decisions; edit nothing until it is accepted.”; `agent-instructions/README.md`, sekcja „Make the change”: poprawka, która zmieniałaby znaczenie przyjętej decyzji ponad to, co ustala zadanie, idzie do Mariusza, zanim zmiana pójdzie dalej.
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

### `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md:61-63`

```text
- **Wzór: przykład `make-change`, z wyjątkiem dla fragmentu z jedną instrukcją.** Tabela ocen i układ po przebudowie: `Notes/Projects/(P) Proces pracy nad produktem/skille_po_kolei_dane/przyklad_make_change.md` — w `SKILL.md` obraz całości, tabela wariantów na początku kroku 1, część wspólna; obok `slice.md`, `fix.md`, `ui_check.md`. Fragment wariantu albo kroku, który jest jedną instrukcją, zostaje w `SKILL.md` w miejscu, gdzie stałby odsyłacz do niego: odsyłacz też jest instrukcją, więc plik obok nie zmniejszyłby liczby instrukcji naraz, a dołożyłby plik do utrzymania. Wyjątek dochodzi do WAY-256 i do `instruction-files/kind_skill.md` w zadaniu 1, razem ze zmianą WAY-125. Ryzyko: „to tylko jedna instrukcja” jako furtka do zostawiania wszystkiego; granica jest policzalna — jedna instrukcja przeciw jednemu odsyłaczowi. Przykład pokazał też, że w `make-change` zysk jest mały (ok. 15%, z 12 do ok. 10 mln tokenów w mierze serii), bo warianty różnią się kilkoma liniami; duży zysk leży w `implement-task`. Źródło: Mariusz, 2026-10-28, „dopiszmy ten wyjątek”.

- **Przebudowa zmienia miejsce reguł, nie ich treść.** Cykl każdego zadania serii wykonuje sam tylko werdykty „keep” i „move” oraz przeredagowania, które nie zmieniają znaczenia — zdanie odsyłacza, wiersz tabeli wariantów, fragment z jedną instrukcją w miejscu odsyłacza; werdykty „remove” i „reword” zmieniające treść reguły idą do requestu jako propozycje. Powód: PR serii ma być do przejrzenia jako przebudowa („nic nie zginęło, nic nie zmieniło sensu”), a pomiar ma pokazać skutek samego kształtu, nie usuniętej treści. Koszt: znalezione zbędne reguły czekają na osobną zmianę. Odrzucone: cykl wykonuje wszystkie werdykty. Źródło: Mariusz, 2026-10-28, „A” w doprecyzowaniu zadania 1 (`_zadania/zadanie_skille_the_way_1_cykl_zadania.md`) i „tak, przyjmuję” na dopisanie tego do serii.
```

## Your boundary

Make your slice only, commit it on the task branch, keep the worktree clean, and return. Run your
slice's *Checks* and report each with its command and exit code. Do not run `gate/run_tests.py` as a
whole; that run is the orchestrator's (a directory argument is a focused check and allowed). Return
your status (`done`, `done with concerns`, `questions`, `returned` or `blocked`), your commits, a
one-line check result naming what failed or did not run, and your report's path.
