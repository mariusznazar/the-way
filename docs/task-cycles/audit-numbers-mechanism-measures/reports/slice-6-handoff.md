# Handoff — slice 6

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator.
Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`. The slice's base is the current HEAD, `0e75a4b`
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
- your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/slice-6-report.md`

Answers of the start of the cycle: trust boundary yes (this change adds a reader of session records and changes
`process-audit/audit_count.py`, the trust boundary of `process-audit`: crafted input at every reading must be
survived — missing fields, malformed lines, bars and control characters in text that reaches a cell, huge files);
irreversible operation no. Checks failing on the base: none (the whole gate passed on the base). The foundation
check `python -B elements/common/foundation_check.py --skip-test-citations` is NOT yours to fix beyond this slice's files.

The slice, copied word for word from the plan:

### Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values

- **Goal:** `process-audit/audit_count.py` reads, from the last copy of each cycle, the files `mechanism_measures.md` and
  `gate_times.md` as the plan's Slice 1 and Slice 3 give their form, keeps the values on the cycle, and writes two sections of
  the result, `## Mechanism measures` and `## Gate runs`, after `## Cost` and before `## Process versions`. No series, median or comparison
  is made here (Slice 7).
  *Reading.* A copy with no such file gives its values unknown with the reason that the copy holds none, an earlier form,
  and no `Error:`. A file that is there is read by its labels: in `mechanism_measures.md` each line label of the form, found
  once, and the table `## Agents` is no needed field; in `gate_times.md` the six columns of the table's header row. A
  needed field the file lacks — a label never written, a column absent — gives every value of that file unknown, the result
  written, and exit code 1 with an `Error:` line that names the file of the copy and the field, joining Slice 5's mechanism
  (the row 6 of the settlements). A label written twice, a value that is not what its label gives, or a row of the table with
  the wrong number of cells is no missing field: the value, or the run, is unknown with a reason in *Unknown values*, and the
  count goes on. `unknown` written by the script is read as unknown. Work and size are bounded as the other readings are: a
  file over the limit already used for the copy's files is not read; at most a fixed number of runs per file and of
  directories per run are read, and the rest give unknown with that reason; every text from a file reaches the result
  as the cells of the result are written, one line, bars escaped, and cut.
  *Sections.* `## Mechanism measures`: one row per cycle with the columns `Repository`, `Record` and one for each cycle-level
  line of the file, named as its label, `unknown` where it is unknown; the per-agent table stays in the file. `## Gate runs`: one
  row per run — `Repository`, `Record`, `Started (UTC)`, `Exit code`, `Total seconds`, `Other gate runs at the same time` and
  `Directories`, a cell listing each directory with its seconds. A cycle with no run has no row there. A line before each
  table says which script writes the file and that `unknown` is never zero.
  *Tests* (`process-audit/test_audit_count.py`, in classes whose names hold `Measures`): a cycle with both files read against values worked out by hand; a copy
  without them; the last copy read where a later copy differs; for each of the two readings one test that gives the file
  without a field and asserts exit code 1, the result written, that cycle's values `unknown` and the `Error:` line naming the
  file and the field; a doubled label and a malformed value giving unknown with no `Error:`; a crafted file — bars, control
  characters, very many runs and directories — breaking no cell and costing bounded work.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:36-36` To do, item 5 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:46-51` Questions to settle, whether the count reads the new numbers · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:63-68` Questions to settle, the gate times between versions · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:114-123` process-audit · `foundations/part_map.md:231-239` External context · Foundation entries rows 2, 6 · `foundations/decisions.md:11166-11192` WAY-338 · `foundations/decisions.md:11294-11319` WAY-343
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py`, which reads the copies of the cycles' records from git history, untrusted input
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Measures` — the new tests fail before the slice and pass after; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` once at the end of the slice; `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py` shows no changed line in the assignment of `TREE_PATHS`; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Slice 5 · Slice 1 · Slice 3 · Foundation entries rows 2, 6

Passages of the task and the plan its *Read* names, copied word for word:

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:36-36` To do, item 5

5. Polecenie liczące audytu czyta plik miar z punktu 2 i czasy bramki z punktu 4 każdego cyklu i pokazuje je w osobnej sekcji wyniku: wartości każdego cyklu, a dla każdej wersji procesu medianę każdej miary i odpowiedź, czy spada względem poprzedniej wersji tej samej serii, jak dziś dla kosztu. Dla czasów bramki mediana i porównanie biorą tylko przebiegi, przy których nie biegła żadna inna bramka; pozostałe przebiegi wynik pokazuje osobno. Nową serię tych miar zaczyna tylko zmiana przyrządu, który je mierzy: skryptu z punktu 2 albo skryptu z punktu 4. Plik miar albo czasów bramki, w którym brakuje pola, daje wartości z niego nieznane; polecenie zapisuje wynik i kończy kodem 1 z linią `Error:`, która nazywa plik i brakujące pole.

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:46-51` Questions to settle, whether the count reads the new numbers

- Czy cotygodniowe liczenie audytu ma czytać nowe liczby (plik miar z punktu 2 i czasy bramki z punktu 4) i pokazywać je w swoim wyniku, czy to zadanie tylko zaczyna je zbierać w zapisach cykli?
  - Answer: Czyta je i pokazuje razem z medianami każdej wersji procesu i porównaniem z poprzednią wersją tej samej serii (wariant pełny).
  - Not chosen:
    - tylko zbierać w zapisach cykli — liczby leżą w katalogach cykli, do których sesja audytu nie zagląda, a porównanie „przed i po” trzeba robić ręcznie
    - czytać i pokazywać wartości każdego cyklu, bez median i porównań wersji — „sam na oko to nic nie porównam sensownie”
  - Source: Mariusz, 2026-11-12: „wolę wariant pełny, bo sam na oko to nic nie porównam sensownie”

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:63-68` Questions to settle, the gate times between versions

- Jak audyt porównuje czasy bramki między wersjami procesu, skoro ten sam przebieg trwa 15–16 minut na wolnej maszynie i 23–40 minut przy kilku sesjach obok?
  - Answer: Skrypt bramki zapisuje przy każdym przebiegu, ile innych bramek uruchomionych tym skryptem biegło w tym samym czasie; audyt porównuje medianę przebiegów, przy których nie biegła żadna inna, a resztę pokazuje osobno. Innego obciążenia maszyny ta liczba nie widzi, a wersja, w której każda bramka miała towarzystwo, nie dostaje porównania.
  - Not chosen:
    - najkrótszy przebieg każdej wersji — wersja z większą liczbą cykli ma więcej szans na szybki przebieg i wypada lepiej, a jeden szczęśliwy przebieg wyznacza wynik
    - mediana jak dla pozostałych miar — przy dzisiejszym rozrzucie porównanie mówi głównie o obciążeniu maszyny
  - Source: Mariusz, 2026-11-12: „tak jak rekomendujesz”

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

#### `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions

### Slice 1 — The measures script, for Claude Code sessions

- **Goal:** the script `task-cycle/cycle_measures.py` and its tests exist, and for the sessions of Claude Code
  they write the file of the cycle's mechanism measures. The script stands on its own: it imports no
  file of the-way, `task-cycle/cycle_stages.py` included, so that the script is the one instrument of
  these measures; it uses the standard library alone.
  *Command.* `python -B task-cycle/cycle_measures.py [SESSION ...] [--output PATH] [--codex-home DIR]
  [--claude-home DIR]`: SESSION, the two homes and the default of the session running the command are
  taken as `task-cycle/cycle_stages.py` takes them (a transcript path or a session id; the homes from
  `CODEX_HOME` and `CLAUDE_CONFIG_DIR`, else `~/.codex` and `~/.claude`; without SESSION, the session
  named in `CLAUDE_CODE_SESSION_ID` or `CODEX_SESSION_ID`, with an error where both or neither is set).
  The text goes to PATH, its directory made if it is absent, or to stdout. Exit code 0 when the
  file is written; 2 with `Error: <message>` on stderr and nothing written, for every failure: a
  session that cannot be found or read, a line that is not JSON, a needed field that is missing.
  *What is read.* The transcript of each session given — an orchestrator's — and each
  `<transcript without .jsonl>/subagents/agent-<id>.jsonl` beside it. An agent is one transcript; a
  subagent that another subagent started is an agent of its own. A subagent is named
  `<description> (<agentType>)` from its `agent-<id>.meta.json`, and by its id where the file or those
  keys are missing: the name is a label and no field the script needs. A call is a model response of
  an agent: a Claude Code response is written over several lines sharing the `id` of its message, so
  each id counts once, from the line with the most `output_tokens`; a response whose model is
  `<synthetic>` is no call. The calls of an agent are in the order of their time. A call's needed
  fields are `message.usage.input_tokens`, `.cache_read_input_tokens`, `.cache_creation_input_tokens`,
  `.output_tokens` and `.cache_creation.ephemeral_5m_input_tokens` and `.ephemeral_1h_input_tokens`;
  where one is missing — never read as zero — the script ends with exit code 2 and an `Error:` line
  that names the transcript file and the field.
  *Measures.* The context of a call is its `input_tokens`, its cache read and its cache write
  together. The middle call of n calls is the one at zero-based position (n-1)//2. A cache write again
  is counted per agent over each two consecutive calls, the earlier P and the later C: what P held in
  the cache (its read and its write) and C did not read, at most what C wrote — that is
  min(max(0, P.read + P.write - C.read), C.write) — and it counts only where it is above 2000 tokens
  and where C's context is not 30% or more below P's context (C's context times 10 is not at most P's
  context times 7); a call that passes both is a call with a cache write again. Means are rounded
  half up to a whole token; a share to one decimal, half up; where nothing can be averaged the value is
  `unknown`, never zero.
  *The file* is Markdown, UTF-8, LF line ends, the same bytes for the same input. It opens with the
  heading `# Measures of the cycle run`, then the lines below, each exactly once, in this order, then
  a table under the heading `## Agents`. Values are whole numbers with no separator, a share is
  `<n.n>%`, and a value that cannot be given is `unknown`.
  - `- Calls in all: ` (all agents) · `- Calls of the orchestrator: ` · `- Calls of subagents: `
  - `- Mean context per call: ` (all calls) · `- Mean context per call of the orchestrator: `
  - `- Share of the context in calls above 200000 tokens: ` — the context of the calls with a
    context above 200000 tokens over the context of all calls, all agents
  - `- Context of the orchestrator's first call: ` · `- Context of the orchestrator's middle call: ` ·
    `- Context of the orchestrator's last call: ` — the calls of the orchestrator's sessions taken
    together in the order of their time
  - `- Cache written, 5 minutes: ` · `- Cache written, 1 hour: ` — the sums over all agents
  - `- Cache written again by the orchestrator: ` · `- Calls of the orchestrator with a cache write
    again: ` · `- Cache written again by subagents: ` · `- Calls of subagents with a cache write
    again: ` — each summed over the agents it names, the rewrite taken within one transcript
  The table `## Agents` has the columns `Agent`, `Tool`, `Calls`, `First call`, `Middle call`,
  `Last call`, `Cache written, 5 minutes`, `Cache written, 1 hour`, `Cache written again` and `Calls with
  a cache write again`: one row per agent, the contexts of its first, middle and last call, the
  orchestrator's session as `orchestrator <session id>`, the tool `Claude Code`. A cell of the agent's
  name is text from a transcript: written on one line with each bar replaced.
  *Tests* (`task-cycle/test_cycle_measures.py`, written first, on small transcripts made in the test and
  the form `task-cycle/test_cycle_stages.py` gives, with no absolute path in any text): each line of the
  file against figures worked out by hand for a small cycle; the rewrite's four edges (the threshold
  of 2000, the shrink of exactly 30%, the minimum with the write, the first call of an agent counting
  no rewrite); a response over several lines counting once; a synthetic response skipped; a nested
  subagent as an agent of its own; the share above 200000; the first, middle and last call; the
  same bytes on a second run; the script's text importing no module of the repository. For the
  reading of a transcript, one test that gives a response without one of its needed fields —
  `cache_creation` — and asserts exit code 2 with an `Error:` line naming the transcript file and the
  field, and nothing written (WAY-344).
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:28-33` To do, item 2 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:74-78` Questions to settle, the definition of the tokens written again · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:106-115` script-language · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:126-135` script-subprocesses · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:93-102` task-cycle · `foundations/part_map.md:231-239` External context · Foundation entries rows 1, 7 and the part-map row · `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py:1-30` · `task-cycle/test_cycle_stages.py:225-247`
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`, which reads session transcripts, untrusted input by the part map's External context
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` fails on the base before the script exists and passes after; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit; `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"`; `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` exits 0
- **Depends on:** Foundation entries rows 1, 7 and the part-map row

#### `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times

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

Foundation entries of its *Read*, by identifier with the current range in the worktree (read each whole; the
current ranges hold where they differ from the plan's):

- `foundations/decisions.md:11336-11431` WAY-344
- `foundations/decisions.md:10868-10917` WAY-328
- `foundations/decisions.md:1026-1051` WAY-38
- `foundations/invariants.md:86-95` tracked-file-private-paths
- `foundations/part_map.md:115-124` process-audit
- `foundations/part_map.md:232-240` External context
- `foundations/decisions.md:11519-11548` WAY-348 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11336-11431` WAY-344 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11166-11192` WAY-338
- `foundations/decisions.md:11310-11335` WAY-343

Files and ranges of code or tests to read (as its *Read* names them; read each as far as you need):



Foundation entries of this change already written (commit `a030dbf`): WAY-347 to WAY-352, WAY-339 and WAY-344 changed
in place, and the trust boundary of `task-cycle` in `foundations/part_map.md` naming `task-cycle/cycle_measures.py`.

Notes from the orchestrator: (1) The writers exist now: `task-cycle/cycle_measures.py` (the file `mechanism_measures.md`, lines 410-430 write its labels and the `## Agents` heading) and `task-cycle/gate_times.py` (`gate_times.md`, heading, note and table header at its lines 61-70). Build your test fixtures from the labels and columns they actually write; the plan passages above state the same forms, and the scripts hold where they differ. Do not import either script into `process-audit` (the part may depend on `task-cycle` as the map allows, but the audit reads the written files from git history, never runs the scripts). (2) Slice 5 reworked the reading of `stages.md` in the same file (commit `0e75a4b`): read its new helpers for how a missing field gives exit 1 with an `Error:` line and the result written, and follow the same mechanism for the two new files; do not rework slice 5's code. (3) Write each new test before the code it covers; the failing run goes in your report. (4) `TREE_PATHS` and the cost series stay as they are; `task-cycle/cycle_stages.py`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` stay untouched. (5) The whole `process-audit/test_audit_count.py` takes about 3 minutes; run it in the background once at the end of the slice. (6) `process-audit/SKILL.md` is slice 8's, not yours.

Return as `make-change` gives for a slice: status, commits (the slice's range from its base to its head), a one-line
check result naming what failed or did not run, the report path; in the report: each check with its command and exit
code, the own-work check, **Unread material** and **Searches not found or unclear** (each `none` where none), every
reach beyond this handoff, and the choices you made.
