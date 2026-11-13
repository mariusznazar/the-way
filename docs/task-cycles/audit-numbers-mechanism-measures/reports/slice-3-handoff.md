# Handoff — slice 3

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator.
Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`. The slice's base is the current HEAD, `036d24a`
(`git rev-parse HEAD`); the task's base is `2292f334d5499f45b68b00c477cd76a2effd7537`. The-way is the top-level
repository (no product, no `.the-way`). Class of model of this executor: `cheaper`.

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
- your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/slice-3-report.md`

Answers of the start of the cycle: trust boundary yes (this change adds a reader of session records and changes
`process-audit/audit_count.py`, the trust boundary of `process-audit`: crafted input at every reading must be
survived — missing fields, malformed lines, bars and control characters in text that reaches a cell, huge files);
irreversible operation no. Checks failing on the base: none (the whole gate passed on the base). The foundation
check `python -B elements/common/foundation_check.py --skip-test-citations` is NOT yours to fix beyond this slice's files.

The slice, copied word for word from the plan:

### Slice 3 — The script that runs the gate and records its times

- **Goal:** the script `task-cycle/gate_times.py` and its tests exist. The script uses the standard library alone and
  imports no file of the-way. It starts a gate, relays its output, and appends what the run took to a file.
  *Command.* `python -B task-cycle/gate_times.py --output PATH [--registry DIR] -- COMMAND [ARG ...]`:
  COMMAND is the gate the product declares, given by the orchestrator as an argument vector and run with no
  shell in the current directory, its error output joined to its output. Everything the command prints is
  passed on to stdout unchanged and as it comes; the script keeps no copy of it beyond the lines it reads for the
  times. The exit code is the command's own. The script's own failures — no command, no `--output`, an
  output that cannot be appended, a command that cannot be started — end with a first line beginning
  `Error: gate_times.py:` on stderr and exit code 2, and are all found before the command is started where
  they can be; an exit code of 2 that comes with no such line is the gate's own.
  *The times.* The total is the wall time of the run, in seconds to three decimals. The output is read as
  `gate/run_tests.py` writes it: a line `== <directory>` opens a block, and the first line `Ran <n> test(s) in
  <seconds>s` after it, before the next `== ` line, gives that directory's time, kept as printed. No
  order of the directories is assumed, and text before the first `== ` line belongs to no directory. A
  block that holds no such line gives its directory the time `unknown`, never zero. This reading takes a
  stream, not a file; the unknown time is its protection against a missing field (WAY-344).
  *Runs at the same time.* The count of the other gate runs by this script going on at the same time on the
  machine is kept in a directory, default `~/.the-way/gate_runs/` (`--registry DIR` names another, as the
  tests do). Each run makes there an empty file named with its start and a random token, written as
  `<start in milliseconds since the epoch>_running_<token>.run`, and on its end renames it to
  `<start>_<end>_<token>.run`; the registry holds names and no content. At the run's end, the others are the
  entries other than its own whose interval met the run's interval: an entry with an end counts where it
  started before this run ended and ended after this run started; one still running counts where it
  started before this run ended and no more than six hours ago. Entries that ended more than a day ago, and
  running entries more than six hours old, are deleted when a run starts; a file whose name has another form is
  left alone and counted for nothing. Where the directory cannot be made or listed, the run goes on, `Warning:`
  is written to stderr, and the count is `unknown`, never zero.
  *The file* is Markdown, UTF-8, LF line ends. Where the file is missing or empty the script writes first
  the heading `# Gate runs of the cycle`, a line saying that each row is one run by this script and times
  are seconds, and the header row of a table with the columns `Started (UTC)`, `Exit code`, `Total seconds`,
  `Other gate runs at the same time`, `Directory` and `Directory seconds`; every run then appends rows to
  that table, one row for each directory it printed, the first five cells repeated in each, or one row
  with `—` in the last two cells where it printed none. `Started (UTC)` is `YYYY-MM-DD HH:MM:SS.mmm`, so
  that rows of one run share it; `Other gate runs at the same time` is a whole number or `unknown`;
  the `Directory` cell is written on one line with each bar replaced; `Directory seconds` is the time as
  printed or `unknown`.
  *Tests* (`task-cycle/test_gate_times.py`, written first, on commands that are Python one-liners printing
  made-up gate output, never the real gate): the rows for a made-up run with the directories out of
  alphabetical order; a block with no `Ran` line giving `unknown`; text before the first block; a run
  with no block giving the one row with `—`; the exit code passed on; the output passed on unchanged;
  the heading and the table header written once over two runs; the count of others for a registry made in the test
  with entries running, ended inside the run, ended before it, stale and named in another form; an unusable
  registry giving `unknown` with the gate still run; the default registry under the home directory of the
  process, with the home set to a temporary directory in the test's environment; the script's text importing no module of
  the repository and starting no program other than the command.
- **Change:** `task-cycle/gate_times.py` · `task-cycle/test_gate_times.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:35-35` To do, item 4 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:57-68` Questions to settle, the source of the times and the runs at the same time · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:87-89` Context · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:4651-4689` WAY-160 · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:126-135` script-subprocesses · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:93-102` task-cycle · `foundations/part_map.md:124-132` gate · `foundations/part_map.md:188-194` test-runner-command · `foundations/glossary.md:67-72` gate · Foundation entries rows 4, 5 and the part-map row · `gate/run_tests.py`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` fails on the base before the script exists and passes after; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit; `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"`
- **Depends on:** Foundation entries rows 4, 5 and the part-map row

Passages of the task and the plan its *Read* names, copied word for word:

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:35-35` To do, item 4

4. Agent prowadzący cykl uruchamia bramkę produktu przez nowy skrypt w `task-cycle/`, przy każdym przebiegu, ten na stanie wyjściowym też. Skrypt uruchamia bramkę, którą produkt deklaruje, mierzy czas całego przebiegu, wyciąga z jej wyjścia czas każdego katalogu testów, który wypisał program uruchamiający testy procesu (linia `== <katalog>` i czas z `unittest`), bez zakładania ich kolejności, i dopisuje przebieg do pliku w katalogu zapisu cyklu, razem z liczbą innych przebiegów bramki uruchomionych tym skryptem, które biegły w tym samym czasie na tej maszynie. Instrukcja cyklu i szablon zapisu cyklu wymieniają ten skrypt i ten plik.

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:57-68` Questions to settle, the source of the times and the runs at the same time

- Skąd zapis cyklu bierze czas każdego katalogu testów w przebiegu bramki?
  - Answer: Ze skryptu, przez który agent prowadzący uruchamia bramkę: mierzy czas całego przebiegu, wyciąga z wyjścia czasy katalogów wypisane przez program uruchamiający testy procesu i zapisuje je do pliku w katalogu zapisu cyklu. Budowanie i testy Node gry zostają w czasie całości.
  - Not chosen:
    - agent prowadzący przepisuje czasy z wyjścia do zapisu cyklu — przepisane liczby bywają błędne, audyt czytałby tabelę pisaną ręcznie, a zmiana nawyku agenta zmienia przyrząd bez śladu w plikach
    - program uruchamiający testy procesu (`gate/run_tests.py`) sam zapisuje czasy do pliku — dziś z założenia nie zostawia śladu przebiegu, w grze nie objąłby budowania ani Node i zderzyłby się z zadaniem o równoległych katalogach
  - Source: Mariusz, 2026-11-12: „skrypt”
- Jak audyt porównuje czasy bramki między wersjami procesu, skoro ten sam przebieg trwa 15–16 minut na wolnej maszynie i 23–40 minut przy kilku sesjach obok?
  - Answer: Skrypt bramki zapisuje przy każdym przebiegu, ile innych bramek uruchomionych tym skryptem biegło w tym samym czasie; audyt porównuje medianę przebiegów, przy których nie biegła żadna inna, a resztę pokazuje osobno. Innego obciążenia maszyny ta liczba nie widzi, a wersja, w której każda bramka miała towarzystwo, nie dostaje porównania.
  - Not chosen:
    - najkrótszy przebieg każdej wersji — wersja z większą liczbą cykli ma więcej szans na szybki przebieg i wypada lepiej, a jeden szczęśliwy przebieg wyznacza wynik
    - mediana jak dla pozostałych miar — przy dzisiejszym rozrzucie porównanie mówi głównie o obciążeniu maszyny
  - Source: Mariusz, 2026-11-12: „tak jak rekomendujesz”

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:87-89` Context

- Bramka wypisuje dziś pod linią `== <katalog>` linię `Ran <n> tests in <s>s`, którą daje `unittest` (`gate/run_tests.py:94`); czasu katalogu w osobnej, zbiorczej formie nie podaje.
- Skrypt bramki z punktu 4 zapisuje same czasy, nie wyjście bramki: WAY-160 odrzuca trzymanie pełnego wyjścia bramki w pliku cyklu.
- Ten sam plik `gate/run_tests.py` zmienia zadanie zadanie o równoległym uruchamianiu katalogów testów (katalogi testów równolegle).

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

- `foundations/decisions.md:4651-4689` WAY-160
- `foundations/decisions.md:11336-11431` WAY-344
- `foundations/decisions.md:10868-10917` WAY-328
- `foundations/decisions.md:1026-1051` WAY-38
- `foundations/invariants.md:116-125` script-imports
- `foundations/invariants.md:126-135` script-subprocesses
- `foundations/invariants.md:328-337` cross-part-imports
- `foundations/invariants.md:86-95` tracked-file-private-paths
- `foundations/part_map.md:93-103` task-cycle
- `foundations/part_map.md:125-133` gate
- `foundations/part_map.md:189-195` test-runner-command
- `foundations/glossary.md:67-72` gate
- `foundations/decisions.md:11549-11581` WAY-349 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11582-11608` WAY-350 (written by the foundation-entries agent of this change)

Files and ranges of code or tests to read (as its *Read* names them; read each as far as you need):

- `gate/run_tests.py`

Foundation entries of this change already written (commit `a030dbf`): WAY-347 to WAY-352, WAY-339 and WAY-344 changed
in place, and the trust boundary of `task-cycle` in `foundations/part_map.md` naming `task-cycle/cycle_measures.py`.

Notes from the orchestrator (binding where they differ from nothing in your section): (1) the default registry is under the user's home directory; `Path.home()` reads `USERPROFILE` on Windows and `HOME` elsewhere, so the test of the default registry sets both in the test's environment. (2) Slice 1's script `task-cycle/cycle_measures.py` is a worked example of the module layout, the `Error:` handling and tests of this part's scripts; read it as a pattern, not as a dependency — `gate_times.py` imports no file of the-way. (3) Write each test before the code it covers. (4) Nothing in this slice runs the real gate: tests use Python one-liners that print made-up gate output.

Return as `make-change` gives for a slice: status, commits (the slice's range from its base to its head), a one-line
check result naming what failed or did not run, the report path; in the report: each check with its command and exit
code, the own-work check, **Unread material** and **Searches not found or unclear** (each `none` where none), every
reach beyond this handoff, and the choices you made.
