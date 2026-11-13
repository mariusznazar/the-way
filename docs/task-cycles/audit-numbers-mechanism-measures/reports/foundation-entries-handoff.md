# Handoff — the plan's foundation entries

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the
orchestrator. Your questions go to the orchestrator, never to the human; no answer of the
orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`; base commit `2292f334d5499f45b68b00c477cd76a2effd7537`
(this is also slice 1's base). The-way is the top-level repository: no product, no `.the-way`.

Stage: the plan's *Foundation entries*, written before any slice. Variant: none of the rows of
`make-change`'s table — your stage is the foundation step. Read whole `task-cycle/change/SKILL.md`
(the method `make-change`; read a file it names only when the step or variant that names it comes) and
`task-cycle/skill/foundation_step.md`, and the skill of each element when you write an entry of it:
`the-way-record-decision` for decisions and `the-way-update-part-map` for the part map — their `SKILL.md`
in `.claude/skills/` of the worktree, and the files each names when its step comes.

Boundary: write the foundation entries below and nothing else — no code, no test, no instruction file
other than what the entries' own searches (WAY-33) require. Commit on the task branch with git add by
path. Do not run the product's gate. Report path:
`.runs/task-cycles/audit-numbers-mechanism-measures/reports/foundation-entries-report.md`.

Paths:
- frozen task: `.runs/task-cycles/audit-numbers-mechanism-measures/task.md` (read whole)
- plan: its section *Foundation entries* is copied below; the plan's slices say what the code will do
  (`.runs/task-cycles/audit-numbers-mechanism-measures/plan.md`; read the slices only as far as an entry's
  wording needs it — the entries state decisions, not code)
- the answers of the start: trust boundary yes (a new script reads session records; `process-audit/audit_count.py`
  is the boundary of `process-audit`); irreversible operation no; no spec; planned route.

Foundation selection (read each whole, by identifier, in `foundations/`): the *Decisions in play* of the
task are copied below; the decisions whose *Scope* names `process-audit` (WAY-09 WAY-38 WAY-89 WAY-320
WAY-328 WAY-330 WAY-331 WAY-332 WAY-333 WAY-334 WAY-335 WAY-336 WAY-337 WAY-338 WAY-339 WAY-340 WAY-341
WAY-342 WAY-343 WAY-344 WAY-345 WAY-346); of `task-cycle`: WAY-147 WAY-148 WAY-158 WAY-159 WAY-160 WAY-229
WAY-260 WAY-294 WAY-296 WAY-308 WAY-309 WAY-316 WAY-325 WAY-326 WAY-331 WAY-337 WAY-338 WAY-343; WAY-140;
the part-map entries `task-cycle`, `process-audit`, `gate` and the External context; the glossary. Rows 3 and
6 change WAY-339 and WAY-344 in place (WAY-07: edit an existing decision in place).

The task's *Decisions in play* (copied word for word from the frozen task):

## Decisions in play

- **WAY-337** — „A cycle's cost is two numbers, neither divided by a measure of the size of the task: its cost at constant prices, computed from a price list of models that carries a date, and the share of that cost spent in fix rounds […]. The share is `0.0%` only where the record says the cycle had no fix round, and unknown wherever the record and the stages cannot tie each round to the turns that served it.” Punkt 1 liczy tę samą kwotę z innej tabeli; udział rund dla starszej formy jest nieznany.
- **WAY-339** — „A new price list, or a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, starts a new series of measures. The audit compares measures only within one series, and judges a version of the process by the cycles that ran on it, never one week against another.” Zmiana: dla miar z punktu 2 i czasów bramki nową serię zaczyna tylko zmiana przyrządu, który je mierzy — skryptu z punktu 2 albo skryptu z punktu 4; zmiana instrukcji recenzenta i autora jej nie zaczyna. Seria kosztu zostaje jak jest.
- **WAY-344** — „A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs […] and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. The rule binds a script that a change adds and, in a script that a change changes, the whole reading of each file whose way of reading the change reworks […] and a missing field ends the script with exit code 2 and a message that names the file and the field […]. Each reading of a file that the rule covers has one test that gives the file without one of the fields it needs and asserts the failure that names that field […].” Zmiana: plik zapisu cyklu, który polecenie liczące audytu czyta z historii gita — raport etapów, plik miar z punktu 2 i plik czasów bramki z punktu 4 — a w którym brakuje pola, daje wartości z niego nieznane, wynik zapisany i kod 1 z linią `Error:` nazywającą plik i pole, zamiast kodu 2 bez wyniku. Test brakującego pola dla każdego odczytu zostaje. Nowe skrypty z punktów 2 i 4 podlegają tej decyzji bez zmian.
- **WAY-160** — „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run […]. The gate's run is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it.” Punkt 4 zmienia, czym agent prowadzący uruchamia bramkę, nie kto ją uruchamia.
- **WAY-331** — „The audit of the process is a part of the-way of its own, `process-audit`, with a directory of its own, `process-audit/`, apart from the part of the task cycle.” Skrypty z punktów 2 i 4 działają w cyklu, więc stoją w `task-cycle/`; ich odczyt w audycie stoi w `process-audit/`.
- **WAY-341** — „The audit runs once a week, in a session of its own apart from the user's weekly review. The counting runs without a human on the night from Friday to Saturday, and a weekly task in the user's backlog starts the session.”
- **WAY-38** — „Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format.”
- **WAY-328** — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.”


The rows of *Settlements to record* (copied word for word from the frozen task, lines 114-125):

Candidates: 10 shown, 8 accepted — 2026-11-12

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Miary mechanizmu liczy osobny skrypt do osobnego pliku w zapisie cyklu, nie nowe kolumny raportu etapów. | decision | decyzja Mariusza z 12.11.2026 w pierwotnym brzmieniu tego zadania („osobny skrypt i osobny plik, nie nowe kolumny raportu etapów. Powód: audyt porównuje cykle tylko w obrębie serii, a decyzja procesu mówi, że zmiana formy raportu etapów zaczyna nową serię; osobny plik omija ten spór bez zmiany decyzji”); nie wybrane, z sekcji 8 raportu o usprawnieniach: nowe kolumny w raporcie etapów — zmiana formy raportu zaczyna nową serię (WAY-339); dopisanie do WAY-339 zdania, że dodanie kolumn serii nie zaczyna — osobny plik omija spór bez zmiany decyzji | czy późniejsza zmiana może dopisać te miary jako kolumny `stages.md` |
| 2 | Cotygodniowe liczenie audytu czyta miary mechanizmu i czasy bramki z zapisów cykli i pokazuje je z medianą każdej wersji procesu i porównaniem z poprzednią wersją tej samej serii. | decision | pytanie o to, czy liczenie ma czytać nowe liczby | czy wynik audytu ma te miary porównywać, czy tylko wypisać |
| 3 | Nową serię miar mechanizmu i czasów bramki zaczyna tylko zmiana przyrządu, który je mierzy; zmiana instrukcji cyklu jej nie zaczyna. Zmienia WAY-339. | decision | pytanie o to, co zaczyna nową serię tych miar | czy zmiana instrukcji recenzenta dzieli serię tych miar, jak dzieli serię kosztu |
| 4 | Agent prowadzący cykl uruchamia bramkę produktu przez skrypt procesu, który zapisuje czas całego przebiegu i czasy katalogów do pliku w zapisie cyklu. | decision | pytanie o to, skąd zapis cyklu bierze czasy bramki | czy agent może uruchomić bramkę z pominięciem skryptu albo przepisać czasy ręcznie |
| 5 | Audyt porównuje czasy bramki tylko z przebiegów, przy których nie biegła żadna inna bramka; resztę pokazuje osobno. | decision | pytanie o to, jak porównywać czasy bramki | mediana wszystkich przebiegów albo najkrótszy przebieg wersji |
| 6 | Plik zapisu cyklu, który liczenie audytu czyta z historii gita — raport etapów, plik miar i plik czasów bramki — a w którym brakuje pola, daje wartości z niego nieznane, wynik zapisany i kod 1 z linią `Error:` nazywającą plik i pole, zamiast kodu 2 bez wyniku. Zmienia WAY-344. | decision | pytanie o raport, który nie pasuje do żadnej formy; rozszerzenie na plik miar i plik czasów bramki — Mariusz, 2026-11-12: „tak”; nie wybrane: zostawić tylko raport etapów — niedopasowany plik miar albo czasów bramki z dowolnego dawnego cyklu zatrzymuje cały cotygodniowy wynik | kod 2 bez wyniku, jak każe dziś WAY-344 |
| 7 | Ponowny zapis do pamięci podręcznej liczy się według definicji z weryfikacji: to, co poprzednie wywołanie miało w pamięci, a obecne z niej nie odczytało, najwyżej tyle, ile obecne zapisało, powyżej 2 tys. tokenów i bez skurczenia kontekstu o 30% lub więcej. | decision | pytanie o definicję ponownego zapisu | która z dwóch definicji, i czy zwinięcie rozmowy liczy się jako ponowny zapis |
| 8 | Koszt cyklu, którego raport etapów nie ma sekcji szczegółowej, liczy się z tabeli tokenów według modelu tym samym cennikiem; udział rund poprawek jest dla niego nieznany. | decision | punkt 1 *To do*; WAY-337 nie mówi, z której tabeli raportu liczy się koszt | czy następna zmiana audytu może porzucić odczyt starszej formy jako zbędny |

The plan's *Foundation entries* (copied word for word from `plan.md`):

## Foundation entries

The plan names the entries; the agent of the entries words them by `task-cycle/skill/foundation_step.md`
and the skill of the element. Each row of *Settlements to record* of the task is a row here by its
number.

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Row 1 — the mechanism measures are counted by a script of their own into a file of their own, never as new columns of the stage report | new decision | Settlement row 1 | Slice 1 · Slice 2 · Slice 6 |
| Row 2 — the weekly count reads the mechanism measures and the gate times of the cycles' copies and shows them with the median of each version of the process and the comparison with the previous version of the same series | new decision | Settlement row 2 | Slice 6 · Slice 7 · Slice 8 |
| Row 3 — only a change of the instrument that measures them starts a new series of the mechanism measures and of the gate times; WAY-339 changed in place, the series of the cost staying as it is | change of WAY-339 in place | Settlement row 3 | Slice 7 |
| Row 4 — the orchestrator runs the product's gate through a script of the process that records the time of the run and of each test directory into a file of the cycle's record | new decision | Settlement row 4 | Slice 3 · Slice 4 |
| Row 5 — the audit compares gate times only over runs during which no other gate run by the script was going, and shows the rest apart | new decision | Settlement row 5 | Slice 3 · Slice 7 |
| Row 6 — a file of a cycle's copy that the count reads from git history and that lacks a field gives its values unknown, the result is written and the count ends with exit code 1 and an `Error:` line naming file and field; WAY-344 changed in place | change of WAY-344 in place | Settlement row 6 | Slice 5 · Slice 6 |
| Row 7 — the tokens written again to the prompt cache are counted by the definition of the verification | new decision | Settlement row 7 | Slice 1 · Slice 2 |
| Row 8 — the cost of a cycle whose stage report has no detailed section is counted from the table of tokens by model at the same price list, and the share of the fix rounds is unknown for it | new decision | Settlement row 8 | Slice 5 |
| Part map — the entry `task-cycle`: the trust boundary gains `task-cycle/cycle_measures.py`; the part's two new scripts and their two files named where the entry's text calls for it | part-map change | the cycle's answer on the trust boundary; the new scripts | Slice 1 · Slice 2 · Slice 3 |

No invariant is written or changed: none of the eight rows is an invariant, and the change reaches no
invariant that its tests cite.


Part-map row: the entry `task-cycle` gains `task-cycle/cycle_measures.py` as a trust boundary (the line now names
`task-cycle/cycle_stages.py`); the part's two new scripts, `task-cycle/cycle_measures.py` and
`task-cycle/gate_times.py`, are inside `task-cycle/**` already. `gate_times.py` is NOT a trust boundary (the
orchestrator's choice, recorded). Where the entry's text needs a sentence on the two scripts, add it; the part's
*Depends on* stays as is unless the map's rules need otherwise.

For the writer's attention (orchestrator's reading, to be checked against the code the slices will write):
- row 4's decision binds the orchestrator to run the product's gate through `task-cycle/gate_times.py`, which writes
  the times to a file in the cycle's record directory; WAY-160 stays: the run is the orchestrator's alone.
- row 5 rests on the count of other gate runs by the script, kept in empty files under `~/.the-way/gate_runs/`; the
  registry lies outside the repository and WAY-140 names no such effect — state it in the entry only as far as the
  row's meaning needs it; the file names are code, not decision.
- the rewrite definition in row 7 is spelled out in the task document's *Questions to settle*; do not read the
  author's notes outside the repository.

Return as `foundation_step.md` and `make-change` give: status, commits, a one-line check result (the check of the
foundation `python -B elements/common/foundation_check.py --skip-test-citations` run as the way of working
gives), the report path; in the report, for each entry one sentence of its meaning in English and one in the
task document's language, and its mark (`row <n>`, `projected` or `the cycle's`); **Unread material** and
**Searches not found or unclear** (each `none` where none); any question for the orchestrator.
