# Handoff — the agent of the plan's Foundation entries (stage: foundation step, `make-change`)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. A question that needs
the human comes back as status `blocked`, as `task-cycle/skill/foundation_step.md` gives.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`,
  branch `task/weekly-process-audit`, HEAD and base of this stage `e3825a82386a61930a86f8517fc0c5f422fc2833`
  (this is also slice 1's base; slice 1's range starts there so its review covers your entries).
- The product is the-way itself: methods live in the worktree.

## Stage and boundary

You are **the agent of the plan's *Foundation entries***: not the one author, not a slice's executor.
You write the foundation entries below and nothing else: no code, no part-map entry (Slice 1 writes
it with the first file of the directory), no template, no skill. Commit them on the task branch.
Write each through the skill of its element: the decisions through the project skill
`the-way-record-decision` (its `SKILL.md` in the worktree's `.claude/skills/the-way-record-decision/`
points to the file under `elements/decisions/`). Read, whole, in this order of need:
- `task-cycle/change/SKILL.md` (the method `make-change`; you take no row of its table: your stage is
  the plan's *Foundation entries*, and you keep from it the rules of reading, committing and the report
  that apply to writing entries);
- `task-cycle/skill/foundation_step.md` (what the foundation step writes and what you keep in your
  report: for each entry one sentence of its meaning in English and one in Polish, the task document's
  language, marked `row <n>`, `projected` or `the cycle's`).
The decision log is written in English (WAY-72).

## Inputs

- Frozen task (whole): `.runs/task-cycles/weekly-process-audit/task.md`.
- Plan, its *Foundation entries* (copied below word for word) — the plan file is
  `.runs/task-cycles/weekly-process-audit/plan.md`, for your reference only; read nothing else of it.
- No spec.

### The plan's *Foundation entries*, word for word

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Row 1 — the-way gives the template of the register of problems; the audit reads the register a locations entry names; the user's own tool fills it and the user adapts the template | decision | *Settlements to record* row 1 | Slice 1 · Slice 5 · Slice 7 |
| Row 2 — the audit is a part of its own with its own directory, apart from the task cycle | decision | *Settlements to record* row 2 | Slice 1 · Slice 7 |
| Row 3 — the audit's results lie in the user's place outside every repository, named by a locations entry | decision | *Settlements to record* row 3 | Slice 3 · Slice 7 |
| Row 4 — four levels of weight, and a list of classes the template starts and the audit widens | decision | *Settlements to record* row 4 | Slice 1 · Slice 5 · Slice 6 |
| Row 5 — the audit counts problems, not remarks: one problem reported by several stages is one | decision | *Settlements to record* row 5 | Slice 1 · Slice 5 |
| Row 6 — whether a fix works is settled by the cycles whose the-way version holds it, not by a date | decision | *Settlements to record* row 6 | Slice 5 |
| Row 7 — how often an issue comes back is material for the human to weigh; the audit sets no priority from it | decision | *Settlements to record* row 7 | Slice 5 · Slice 7 |
| Row 8 — a cycle's cost is its cost at constant prices from a dated price list and the share of fix rounds in it, with no denominator of task size | decision | *Settlements to record* row 8 | Slice 2 · Slice 4 · Slice 6 |
| Row 9 — a cycle's time is the agents' working time without the wait for the human, and apart the wait for tools | decision | *Settlements to record* row 9 | Slice 2 · Slice 3 |
| Row 10 — a new price list, or a change of a stage report's form, of the list of classes or of the reviewer's instructions, starts a new series; measures compare within a series and a process version | decision | *Settlements to record* row 10 | Slice 4 · Slice 6 · Slice 7 |
| Row 11 — the audit replays no frozen earlier tasks on an old and a new process version | decision | *Settlements to record* row 11 | Slice 7 |
| Row 12 — the audit runs weekly, apart from the weekly review; the counting runs unattended on the night from Friday to Saturday, and a weekly backlog task starts the session | decision | *Settlements to record* row 12 | Slice 3 · Slice 7 |
| WAY-09 changed — the list of the repository's directories gains the audit part's directory, and the sentence of what a directory must hold gains what that one holds | decision | *To do* item 1 | Slice 1 |
| WAY-38 changed — its *Scope* gains `process-audit`, whose command is a script of the-way | decision | *To do* items 1 and 3, through WAY-21 | Slice 3 |
| WAY-89 changed — its *Scope* gains `process-audit` | decision | *To do* items 1 and 3, through WAY-21 | Slice 3 |
| WAY-320 changed — its *Scope* gains `process-audit`, whose skill and command read the locations file | decision | *To do* item 6, through WAY-21 | Slice 3 · Slice 5 · Slice 7 |

The rows and the changes name the part `process-audit`, whose part-map entry Slice 1 writes with the
first file of its directory (`task-cycle/plan/SKILL.md`: a change to the part map for a file the
change adds belongs to the slice that adds the file). Until Slice 1 is made,
`python -B elements/common/foundation_check.py --skip-test-citations` reports the references to that
part, and only those; after Slice 1 it reports nothing.

### The task's *Settlements to record*, word for word

## Settlements to record

Candidates: 13 shown, 12 accepted — 2026-11-11

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | the way określa szablon rejestru problemów, audyt czyta rejestr wskazany wpisem w pliku lokalizacji użytkownika, a wypełnia go narzędzie użytkownika, który dostosowuje szablon do siebie | decision | Questions to settle: „Skąd audyt bierze klasę i wagę…” | czy audyt sam czyta zapisy cykli i sam nadaje klasę i wagę |
| 2 | Audyt jest własną częścią the way z własnym katalogiem, osobno od cyklu zadania | decision | Questions to settle: „Gdzie w repozytorium the way stoi audyt?” | czy położyć audyt w `task-cycle/` |
| 3 | Wyniki audytu leżą w miejscu użytkownika poza repozytoriami, wskazanym wpisem w pliku lokalizacji | decision | Questions to settle: „Gdzie leżą wyniki audytu?” | czy zapisywać wyniki w repozytorium the way |
| 4 | Każdy problem ma wagę w czterech poziomach (brak problemu, Minor, Important, Critical) i klasę z listy, którą szablon zaczyna, a audyt poszerza | decision | Mariusz, 2026-11-11: „tak” na cztery poziomy i listę startową klas poprawianą w audycie | skala wagi (np. pięć poziomów) i zamknięta lista klas |
| 5 | Audyt liczy problemy, nie uwagi: ten sam problem zgłoszony przez kilka etapów cyklu to jeden problem | decision | Mariusz, 2026-11-11: „to są zwyczajnie problemy wpuszczone bez poprawki”; próbka: jeden brak zgłoszony przez trzy etapy | czy liczyć każdą uwagę osobno |
| 6 | O tym, czy poprawka działa, rozstrzygają cykle, których wersja the way ją zawiera, a nie data | decision | Context: pytania audytu; zapis cyklu niesie *Process pin* | porównanie przed i po dacie wdrożenia poprawki |
| 7 | Częstość powrotów sprawy jest materiałem do ważenia przez człowieka; audyt nie nadaje z niej priorytetu | decision | Mariusz, 2026-11-11: „czy to, że coś jest częste oznacza, że automatycznie rośnie priorytet? nie, więc to trzeba zważyć zawsze” | ranking spraw według liczby powrotów |
| 8 | Koszt cyklu to koszt w stałych cenach według cennika z datą i udział rund poprawek w koszcie, bez mianownika wielkości zadania | decision | Mariusz, 2026-11-11: „Koszt mierzymy tymi dwiema liczbami bez mianownika.” | suma tokenów albo koszt na zmienioną linię |
| 9 | Czas cyklu to czas pracy agentów bez czekania na człowieka i osobno czas czekania na narzędzia | decision | Mariusz, 2026-11-11: „miałem na myśli głównie czas pracy agentów, ale pewnie do pary można dorzucić też czas kiedy agent czekał na skrypty - oczekiwania na mnie nie wliczałbym” | czas od startu do scalenia |
| 10 | Nowy cennik oraz zmiana formatu raportu etapu, listy klas albo instrukcji recenzenta zaczynają nową serię; miary porównuje się w obrębie serii i wersji procesu, nie tydzień do tygodnia | decision | rozmowa 2026-11-11: wzrost uwag po WAY-260; Mariusz przyjął ocenę na cyklach wersji procesu | porównanie tydzień do tygodnia przez zmianę formatu |
| 11 | Audyt nie odtwarza zamrożonych dawnych zadań na starej i nowej wersji procesu | decision | Mariusz, 2026-11-11: „tak, zestaw zamrożonych zadań skreślamy” | dołożenie zestawu kontrolnego zadań |
| 12 | Audyt odbywa się raz w tygodniu, osobno od przeglądu tygodnia; liczenie biegnie bez człowieka w nocy z piątku na sobotę, a sesję wyzwala cotygodniowe zadanie w backlogu | decision | Mariusz, 2026-11-11: „wolałbym dedykowane zadanie pod audyt, nie mieszałbym tego z przeglądem tygodnia”; „liczenie automatyczne przed sobotą, spoko” | audyt w przeglądzie tygodnia albo na żądanie |

### The decision the task changes, as the task's *Decisions in play* quotes it

- WAY-09 — What may enter the process repository? Zadanie zmienia ją: lista katalogów repozytorium zyskuje katalog części audytu, a zdanie o tym, co katalog musi zawierać, zyskuje jego zawartość. Brzmienie dziś: „On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository` — `elements/<element>/` for each foundation element, `elements/common/` for what the elements share, `relation-model/`, `gate/`, `installation/`, `agent-instructions/`, `instruction-files/`, `project-level/`, `product-guidelines/`, `foundation-review/` and `task-cycle/` — the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files and the project skill entry points under `.claude/skills/` and `.agents/skills/`, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: (…) `foundation-review/` the skill that reviews a product's foundation against the product, with the files it names; `task-cycle/` what the design of the task cycle sets.”

## Notes of the orchestrator

- Row 10's "series" and rows 4–6 use words of the task's language. Write the decision in plain English
  and tie to the glossary as the element's skill gives; do not invent a name for a mechanism the code
  of later slices has not made.
- The slices after yours write the template, the command and the skill. Decisions describe what holds,
  not how a script computes it; leave the register's field names, the command's output shape and the
  keys of the locations file to the slices, except where a row names them.
- For WAY-38, WAY-89 and WAY-320: only their *Scope* gains `process-audit`, as the plan's table gives,
  through the decisions' skill (WAY-07: an existing decision is edited in place).
- `elements/common/foundation_check.py` will report the references to the part `process-audit` until
  Slice 1 writes its part-map entry; that is expected and only that. Run
  `python -B elements/common/foundation_check.py --skip-test-citations` after your commits and report
  its output: it must list only references to `process-audit`.
- Foundation reading: select as `elements/common/way_of_working.md` "Reading the foundation" and the
  skill of the element give. The decisions most likely to bear on your entries: WAY-09, WAY-103,
  WAY-140, WAY-320, WAY-260, WAY-296, WAY-135, WAY-134. Name every reach beyond what you were given.

## Report

- Path: `docs/task-cycles/weekly-process-audit/reports\foundation_entries_report.md`
- Return: status (`done`, `done with concerns`, `questions`, `blocked`), your commits, a one-line check
  result naming what failed or did not run, the report path; questions and concerns; each reach beyond
  this handoff; **Unread material** (what this handoff names that stayed unread or was read in part,
  or `none`); **Searches not found or unclear** (or `none`); and the own-work check `make-change`
  requires.
