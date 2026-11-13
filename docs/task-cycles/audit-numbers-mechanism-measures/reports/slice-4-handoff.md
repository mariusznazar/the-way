# Handoff — slice 4

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator.
Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`. The slice's base is the current HEAD, `7916a21`
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
- your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/slice-4-report.md`

Answers of the start of the cycle: trust boundary yes (this change adds a reader of session records and changes
`process-audit/audit_count.py`, the trust boundary of `process-audit`: crafted input at every reading must be
survived — missing fields, malformed lines, bars and control characters in text that reaches a cell, huge files);
irreversible operation no. Checks failing on the base: none (the whole gate passed on the base). The foundation
check `python -B elements/common/foundation_check.py --skip-test-citations` is NOT yours to fix beyond this slice's files.

The slice, copied word for word from the plan:

### Slice 4 — The cycle's instruction and record template name the two scripts and their files

- **Goal:** the instruction of the cycle and the record template say that the cycle runs the gate through
  `task-cycle/gate_times.py` and writes the measures with `task-cycle/cycle_measures.py`, and name the two files. In
  `task-cycle/skill/SKILL.md`: every run of the product's gate — step 2's run on the commit that moved the
  pin, step 4's run of the checks on the base, step 10's run, and the reruns of steps 9 and 12 that step 10
  governs — goes through `gate_times.py`, with `--output .runs/task-cycles/<task-slug>/gate_times.md` and the
  product's declared gate command after `--`; the orchestrator records that command and the script's exit
  code, which is the gate's, as before; WAY-160 stands: the run is the orchestrator's alone and no handoff
  or plan names it. Step 4 runs before step 5 names `<task-slug>`: the instruction settles that the name is
  known to the base run (the naming moved before it, or the run's file the one step 5 names), and the file
  lies in the cycle's record directory, which the script makes if it is absent and which the instruction names by a path that
  reaches the worktree's record directory from where the gate runs, since step 4's run may stand in a separate checkout of the base. The base-state run is
  named as one of the runs. Where step 12 runs `task-cycle/cycle_stages.py`, the next command is
  `task-cycle/cycle_measures.py` with `--output .runs/task-cycles/<task-slug>/mechanism_measures.md`,
  naming the same sessions, in the same step; the places that run `cycle_stages.py` — step 9 sub-step 4's
  stop, `task-cycle/skill/blocked_finding.md` and `task-cycle/skill/reserved_return.md` — name the new
  command beside it. The sentence that the cycle writes nothing outside the task's worktree gains the one
  exception: the script's registry of running gates, a directory of empty files under the user's
  `~/.the-way/`, which holds no content of the cycle. `The record before it is committed` stays as it is:
  it copies the whole record directory, and the two files go with it; the instruction says so where it
  names `stages.md`. In `task-cycle/record_template.md`, the sentence that lists the files of the
  record's directory gains `mechanism_measures.md` and `gate_times.md`, each with the step that creates it.
  No word of `task-cycle/cycle_stages.py`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` or
  `task-cycle/spec` changes. The description of the skill `implement-task` is unchanged, so the skill's entry points are not
  regenerated.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/skill/blocked_finding.md` · `task-cycle/skill/reserved_return.md` · `task-cycle/record_template.md`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:34-35` To do, items 3 and 4 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times · `foundations/decisions.md:4651-4689` WAY-160 · `foundations/decisions.md:4198-4265` WAY-148 · `foundations/decisions.md:10023-10088` WAY-308 · `foundations/decisions.md:10089-10139` WAY-309 · `foundations/part_map.md:93-102` task-cycle · `instruction-files/kind_skill.md` · `instruction-files/changing.md` · Foundation entries rows 1, 4
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B instruction-files/check_instructions.py .` exits as it does on the base and lists no finding on the four files that it did not list there; `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"`; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Slice 1 · Slice 3

Passages of the task and the plan its *Read* names, copied word for word:

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:34-35` To do, items 3 and 4

3. Instrukcja cyklu (`task-cycle/skill/SKILL.md`) i szablon zapisu cyklu (`task-cycle/record_template.md`) wymieniają ten plik i krok, który go tworzy; plik trafia do kopii zapisu cyklu w repozytorium razem z resztą katalogu.
4. Agent prowadzący cykl uruchamia bramkę produktu przez nowy skrypt w `task-cycle/`, przy każdym przebiegu, ten na stanie wyjściowym też. Skrypt uruchamia bramkę, którą produkt deklaruje, mierzy czas całego przebiegu, wyciąga z jej wyjścia czas każdego katalogu testów, który wypisał program uruchamiający testy procesu (linia `== <katalog>` i czas z `unittest`), bez zakładania ich kolejności, i dopisuje przebieg do pliku w katalogu zapisu cyklu, razem z liczbą innych przebiegów bramki uruchomionych tym skryptem, które biegły w tym samym czasie na tej maszynie. Instrukcja cyklu i szablon zapisu cyklu wymieniają ten skrypt i ten plik.

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

- `foundations/decisions.md:4651-4689` WAY-160
- `foundations/decisions.md:4198-4265` WAY-148
- `foundations/decisions.md:10023-10088` WAY-308
- `foundations/decisions.md:10089-10139` WAY-309
- `foundations/part_map.md:93-103` task-cycle
- `foundations/decisions.md:11494-11518` WAY-347 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11549-11581` WAY-349 (written by the foundation-entries agent of this change)

Files and ranges of code or tests to read (as its *Read* names them; read each as far as you need):

- `instruction-files/kind_skill.md`
- `instruction-files/changing.md`

Foundation entries of this change already written (commit `a030dbf`): WAY-347 to WAY-352, WAY-339 and WAY-344 changed
in place, and the trust boundary of `task-cycle` in `foundations/part_map.md` naming `task-cycle/cycle_measures.py`.

Notes from the orchestrator: (1) The two scripts exist now: `task-cycle/cycle_measures.py` (slices 1–2, reviewed) and `task-cycle/gate_times.py` (slice 3). Where the plan's passages for slices 1 and 3 above and the committed scripts differ in a command-line form or a file's form, the scripts hold: read the docstring at the head of each (`python -B task-cycle/gate_times.py --output PATH [--registry DIR] -- COMMAND [ARG ...]`; `python -B task-cycle/cycle_measures.py [SESSION ...] [--output PATH] [--codex-home DIR] [--claude-home DIR]`) and `python -B task-cycle/cycle_measures.py --help` is not needed. (2) `gate_times.py` creates its `--output` file's directory and an empty `--output` file before it starts the command (to prove it can append), so the file exists from the first run on. (3) A trailing detail the instruction must say for the base run: the run's `--output` path must reach the worktree's record directory, `.runs/task-cycles/<task-slug>/gate_times.md` in the worktree, from wherever the gate runs — in the-way itself step 4's base run stands in a separate checkout under the worktree's `.runs/`, so name the path as absolute-from-the-worktree-root expressed relative to the checkout where it runs only if you can make it correct, otherwise have the orchestrator name the slug before step 4 and give the path of the worktree's record directory by the same words the instruction already uses for it. (4) The product's declared gate command: where the instruction names a command, name the-way's as `python -B gate/run_tests.py` and say a product passes the command its own rules declare after `--`; the gate's output is still passed through unchanged. (5) Do not edit the entry points; the skill's description is unchanged.

Return as `make-change` gives for a slice: status, commits (the slice's range from its base to its head), a one-line
check result naming what failed or did not run, the report path; in the report: each check with its command and exit
code, the own-work check, **Unread material** and **Searches not found or unclear** (each `none` where none), every
reach beyond this handoff, and the choices you made.
