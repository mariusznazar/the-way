# Handoff — slice 1

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator.
Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`. The slice's base is the current HEAD, `a030dbf`
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
- your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/slice-1-report.md`

Answers of the start of the cycle: trust boundary yes (this change adds a reader of session records and changes
`process-audit/audit_count.py`, the trust boundary of `process-audit`: crafted input at every reading must be
survived — missing fields, malformed lines, bars and control characters in text that reaches a cell, huge files);
irreversible operation no. Checks failing on the base: none (the whole gate passed on the base). The foundation
check `python -B elements/common/foundation_check.py --skip-test-citations` is NOT yours to fix beyond this slice's files.

The slice, copied word for word from the plan:

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

Passages of the task and the plan its *Read* names, copied word for word:

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:28-33` To do, item 2

2. Nowy skrypt w `task-cycle/`, uruchamiany przy zamknięciu cyklu w tym samym kroku, w którym powstaje raport etapów, liczy z zapisów sesji cyklu i zapisuje do osobnego pliku w katalogu zapisu cyklu same liczby tokenów i wywołań, bez kwot:
   - liczbę wywołań modelu — w całym cyklu, osobno agenta prowadzącego cykl i każdego podagenta;
   - kontekst wywołania (wejście, odczyt z pamięci i zapis do pamięci razem) — dla każdego agenta w pierwszym, środkowym i ostatnim wywołaniu; dla cyklu średnią, osobno średnią agenta prowadzącego, oraz udział kontekstu przypadający na wywołania ponad 200 tys. tokenów;
   - tokeny zapisane do pamięci podręcznej, osobno z czasem życia 5 minut i godziny, dla każdego agenta;
   - tokeny zapisane do pamięci ponownie i liczbę wywołań z takim zapisem, osobno dla agenta prowadzącego i dla podagentów: w wywołaniu agenta po pierwszym ponownie zapisane jest to, co poprzednie wywołanie miało w pamięci (odczyt i zapis do pamięci), a obecne z niej nie odczytało, najwyżej tyle, ile obecne zapisało; liczy się tylko powyżej 2 tys. tokenów i tylko wtedy, gdy kontekst nie skurczył się o 30% lub więcej względem poprzedniego wywołania;
   - dla agenta Codexa zapis do pamięci i ponowny zapis są nieznane, nie zero: jego zapis sesji podaje tylko część wejścia odczytaną z pamięci.

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:74-78` Questions to settle, the definition of the tokens written again

- Według której z dwóch definicji z analiz z 12.11.2026 skrypt liczy tokeny zapisane do pamięci ponownie?
  - Answer: Według definicji z weryfikacji (`weryfikacja_usprawnienia_the_way_dane/s05_metrics.py`, wiersze 76–83): to, co poprzednie wywołanie miało w pamięci, a obecne z niej nie odczytało, najwyżej tyle, ile obecne zapisało, powyżej 2 tys. tokenów i bez skurczenia kontekstu o 30% lub więcej, które jest zwinięciem rozmowy, nie wygaśnięciem pamięci. Wartość „przed” do porównania stoi w `weryfikacja_usprawnienia_the_way_dane/miary_kontekstu.md`.
  - Not chosen:
    - definicja z syntezy (`usprawnienia_the_way_dane/15_cache_rewrites.py`, wiersze 134–137): zapis ponad przyrost kontekstu od poprzedniego wywołania — każde zwinięcie rozmowy wygląda jak wygaśnięcie pamięci, więc zmiana, która dodaje zwinięcia, wyglądałaby jak pogorszenie
  - Source: Mariusz, 2026-11-12: „z weryfikacji”

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

- `foundations/decisions.md:11336-11431` WAY-344
- `foundations/decisions.md:10868-10917` WAY-328
- `foundations/decisions.md:1026-1051` WAY-38
- `foundations/invariants.md:106-115` script-language
- `foundations/invariants.md:116-125` script-imports
- `foundations/invariants.md:126-135` script-subprocesses
- `foundations/invariants.md:328-337` cross-part-imports
- `foundations/invariants.md:86-95` tracked-file-private-paths
- `foundations/part_map.md:93-103` task-cycle
- `foundations/part_map.md:232-240` External context
- `foundations/decisions.md:11494-11518` WAY-347 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11609-11639` WAY-351 (written by the foundation-entries agent of this change)

Files and ranges of code or tests to read (as its *Read* names them; read each as far as you need):

- `task-cycle/cycle_stages.py`
- `task-cycle/test_cycle_stages.py:1-30`
- `task-cycle/test_cycle_stages.py:225-247`

Foundation entries of this change already written (commit `a030dbf`): WAY-347 to WAY-352, WAY-339 and WAY-344 changed
in place, and the trust boundary of `task-cycle` in `foundations/part_map.md` naming `task-cycle/cycle_measures.py`.

Return as `make-change` gives for a slice: status, commits (the slice's range from its base to its head), a one-line
check result naming what failed or did not run, the report path; in the report: each check with its command and exit
code, the own-work check, **Unread material** and **Searches not found or unclear** (each `none` where none), every
reach beyond this handoff, and the choices you made.
