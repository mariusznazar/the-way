# Handoff — slice 5

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator.
Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`. The slice's base is the current HEAD, `8a8f636`
(`git rev-parse HEAD`); the task's base is `2292f334d5499f45b68b00c477cd76a2effd7537`. The-way is the top-level
repository (no product, no `.the-way`). Class of model of this executor: `same`.

Method: `make-change`, in its variant "a slice, or the retry of a slice". Read whole `task-cycle/change/SKILL.md`,
and a file it names (`task-cycle/change/slice.md` included) only when the step or variant that names it comes.
Boundary: this slice only, its commits on the task branch (git add by path, never `-A`), then return. Do not run
the product's gate (`gate/run_tests.py`); run the slice's own focused checks named in its section, each with its
command and exit code in your report. Write each test before the code it covers where the slice changes behaviour.
Another slice's files you do not touch.

Paths:
- frozen task: `.runs/task-cycles/audit-numbers-mechanism-measures/task.md`
- plan: `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md` (you need not open it: your section is below)
- spec: none
- your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/slice-5-report.md`

Answers of the start of the cycle: trust boundary yes (this change adds a reader of session records and changes
`process-audit/audit_count.py`, the trust boundary of `process-audit`: crafted input at every reading must be
survived — missing fields, malformed lines, bars and control characters in text that reaches a cell, huge files);
irreversible operation no. Checks failing on the base: none (the whole gate passed on the base). The foundation
check `python -B elements/common/foundation_check.py --skip-test-citations` is NOT yours to fix beyond this slice's files.

The slice, copied word for word from the plan:

### Slice 5 — The count reads the cost from either form of the stage report, and ends with exit code 1 on a missing field

- **Goal:** `process-audit/audit_count.py` gives a cycle's cost from the section `Stages: start, waiting for tools and
  tokens by model` where `stages.md` has it, as before, and from the table of tokens by model where it has not;
  and a field a form needs that `stages.md` lacks gives the cost of that cycle unknown, the result written
  and exit code 1 with an `Error:` line naming the file and the field. The series of the cost stay as they
  are: `TREE_PATHS` is not edited, and no other condition of a series changes.
  *Forms.* The newer form is known by the heading of the section and read as it is read today. The older form
  is known by its table: the table whose header row's first cell is `Model`, the columns of which are `Model`,
  `Total tokens`, `Input`, `Cached input` and `Output`, found exactly once; found twice, the cost is unknown with
  a reason and no `Error:`. Its rows are priced by the price list as the rows of the newer form are: the input
  less its cached input at the *Input* price, the cached input at the *Cached input* price, the output at the
  *Output* price; a model the list gives no price for, a model `unknown`, a cached input above its input, or a
  token count that is no number leave the cost unknown with a reason. The older form's share of the
  cost in fix rounds is `unknown` with a reason that the form gives no turns; the number of fix rounds is still
  read from the record where the record gives it, as for the newer form. A cycle in the older form is never
  put beside one of the newer form: the series' rule is as it is.
  *Missing fields* (WAY-344 as the row 6 settles it; the whole reading of `stages.md` is reworked, so every
  field of the file is under the check): a field is missing where the form the file's own signs name needs
  it and the file has no such name. The newer form needs the columns `#`, `Stage`, `Start`, `Waiting for tools`,
  `Model`, `Input`, `Cached input` and `Output` in the table of its section — a heading with no table at all misses the
  table — and `Files named` is never a missing field: the section without it is the earlier form of the section, and the
  share is unknown as today. The older form needs the columns `Input`, `Cached input` and `Output` of its table, `Model`
  being its sign. A file with neither the heading nor a table with first cell `Model` misses the section and the table, and
  the `Error:` line names both. The times: a file that has neither the line `- Working time without waiting for tools:`
  nor the line `- Waiting for tools:` is an earlier form, read as today with those two values unknown and no `Error:`;
  a file that has one of them misses the other. A form that has every field but in another order, or with another
  column beside them, misses none and is refused with a reason as today. Each missing field puts a line in the result's
  *Unknown values* and one `Error: repository `<key>`: cycle `<folder>`: the file `stages.md` of the copy lacks the field
  `<field>`` on stderr after the result is written; text from the records is cut and escaped as the command does for every
  other reason; the exit code is 1, joining the cases that give it now. The module's docstring and the lines of the
  result that describe the cost are brought to this.
  *Tests* (`process-audit/test_audit_count.py`, the new ones in the class `Cost`, in `Times` or in a class whose name holds `StagesForms`): the tests that give the cost of an earlier form as unknown are changed to
  what the row 8 settles; new tests: the older form priced by hand at a test price list; its share unknown with the reason;
  its rounds read from the record; a model with no price; the newer and the older form of one version
  not put in one comparison — the series of the cost unchanged, with a test that a change of
  `task-cycle/cycle_measures.py` or `task-cycle/gate_times.py` between two versions does not split the series of the cost
  while a change of `task-cycle/cycle_stages.py` still does; and for each reading of `stages.md`
  — the newer form's table, the older form's table, the two time lines — one test that gives the file without a field and
  asserts exit code 1, the result written with the cost unknown, and the `Error:` line naming the file and the field.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:27-27` To do, item 1 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:39-42` Acceptance criteria · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:69-73` Questions to settle, the report that fits neither form · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:84-86` Context · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:11125-11165` WAY-337 · `foundations/decisions.md:11193-11217` WAY-339 · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10990-11013` WAY-331 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:114-123` process-audit · `foundations/part_map.md:231-239` External context · Foundation entries rows 6, 8 · `foundations/decisions.md:11166-11192` WAY-338 · `foundations/decisions.md:11294-11319` WAY-343 · `task-cycle/cycle_stages.py:858-954` the stage report · `process-audit/price_list.md`
- **Model:** same — a rework of the reading rules of a 2200-line file at a trust boundary, where the rules interlock
- **Risk:** trust boundary — `process-audit/audit_count.py`, which reads the copies of the cycles' records from git history, untrusted input
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k Times -k StagesForms -k ProcessVersions` — the new tests fail on the base and pass after; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` once at the end of the slice; `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py` shows no changed line in the assignment of `TREE_PATHS`; `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` exits 0; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Foundation entries rows 6, 8

Passages of the task and the plan its *Read* names, copied word for word:

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:27-27` To do, item 1

1. Polecenie liczące audytu (`process-audit/audit_count.py`) podaje koszt cyklu także wtedy, gdy raport etapów nie ma sekcji `Stages: start, waiting for tools and tokens by model`: liczy go z tabeli tokenów według modelu (nagłówek `| Model | Total tokens | Input | Cached input | Output |`), tym samym cennikiem i wzorem co dziś — wejście bez części odczytanej z pamięci po cenie wejścia, część odczytana z pamięci po cenie odczytu, wyjście po cenie wyjścia. Starszą formę rozpoznaje po jej własnych znakach, osobną ścieżką odczytu. Udział rund poprawek zostaje dla takiego cyklu nieznany, z podanym powodem. Raport etapów, w którym brakuje pola potrzebnego którejkolwiek z obu form, daje koszt tego cyklu nieznany; polecenie zapisuje wynik i kończy kodem 1 z linią `Error:`, która nazywa plik i brakujące pole.

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:39-42` Acceptance criteria

### Acceptance criteria

- Zmiana nie dotyka pliku `task-cycle/cycle_stages.py` ani katalogów `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` i `task-cycle/spec`: każda zmiana w nich zaczyna w audycie nową serię miar, a osobny skrypt i osobny plik wybrano po to, żeby jej nie zaczynać.
- Wynik liczenia dzieli dawne cykle na te same serie kosztu co przed zmianą: dodanie skryptu miar i jego pliku nie zaczyna nowej serii kosztu.

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:69-73` Questions to settle, the report that fits neither form

- Co robi liczenie audytu, gdy raport etapów dawnego cyklu nie pasuje ani do nowszej, ani do starszej formy: podaje koszt jako nieznany z powodem i liczy dalej, czy kończy błędem?
  - Answer: Podaje koszt tego cyklu jako nieznany, pisze wynik i kończy kodem 1 z linią `Error:`, która nazywa plik i brakujące pole — jak dziś przy repozytorium, którego nie dało się przeczytać. Zmienia to WAY-344: plik czytany z historii gita, której żadna zmiana nie poprawi, nie zatrzymuje całego liczenia.
  - Not chosen:
    - kod 2 i nic nie zapisane, jak każe WAY-344 — liczenie biegnie w nocy bez człowieka, więc sobotnia sesja nie ma żadnego wyniku, także liczb z rejestru problemów, aż ktoś poprawi skrypt
  - Source: Mariusz, 2026-11-12: „tak jak rekomendujesz”

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:84-86` Context

- Tabelę tokenów według modelu ma każdy raport etapów w historii obu repozytoriów (130 ostatnich kopii, sprawdzone 12.11.2026), zawsze dokładnie raz.
- W obrębie jednej serii wszystkie cykle mają raport etapów tej samej formy, więc audyt nie zestawi kosztu policzonego z tabeli według modelu z kosztem policzonym z sekcji szczegółowej.
- Nowy skrypt stoi w `task-cycle/`, jak `task-cycle/cycle_stages.py`: część `task-cycle` nie może zależeć od części `process-audit` (mapa części), a cennik należy do `process-audit` — stąd liczby tokenów bez kwot.

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record

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

Foundation entries of its *Read*, by identifier with the current range in the worktree (read each whole; the
current ranges hold where they differ from the plan's):

- `foundations/decisions.md:11125-11165` WAY-337
- `foundations/decisions.md:11193-11233` WAY-339
- `foundations/decisions.md:11336-11431` WAY-344
- `foundations/decisions.md:10990-11013` WAY-331
- `foundations/decisions.md:10868-10917` WAY-328
- `foundations/decisions.md:1026-1051` WAY-38
- `foundations/invariants.md:116-125` script-imports
- `foundations/invariants.md:328-337` cross-part-imports
- `foundations/invariants.md:86-95` tracked-file-private-paths
- `foundations/part_map.md:115-124` process-audit
- `foundations/part_map.md:232-240` External context
- `foundations/decisions.md:11336-11431` WAY-344 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11640-11710` WAY-352 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11166-11192` WAY-338
- `foundations/decisions.md:11310-11335` WAY-343

Files and ranges of code or tests to read (as its *Read* names them; read each as far as you need):

- `task-cycle/cycle_stages.py:858-954` the stage report
- `process-audit/price_list.md`

Foundation entries of this change already written (commit `a030dbf`): WAY-347 to WAY-352, WAY-339 and WAY-344 changed
in place, and the trust boundary of `task-cycle` in `foundations/part_map.md` naming `task-cycle/cycle_measures.py`.

Notes from the orchestrator: (1) `process-audit/audit_count.py` is the module this slice reworks; read it whole before changing it (it is long: read the parts the slice's section names and every function they call, and name in your report what you did not read). (2) The new measures script and gate script are committed (`task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`); this slice reads neither — only `stages.md`. (3) `task-cycle/test_cycle_stages.py` and `task-cycle/cycle_stages.py` stay unchanged: the plan's check `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` must exit 0. (4) Write each new test before the code it covers; the failing run goes in your report. (5) `TREE_PATHS` is not edited. (6) Reading of `stages.md` is reworked by this slice, so by WAY-344 every field of the file's readings is under the check you write, as the slice's section says.

Return as `make-change` gives for a slice: status, commits (the slice's range from its base to its head), a one-line
check result naming what failed or did not run, the report path; in the report: each check with its command and exit
code, the own-work check, **Unread material** and **Searches not found or unclear** (each `none` where none), every
reach beyond this handoff, and the choices you made.
