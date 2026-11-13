# Handoff — slice 2

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator.
Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`. The slice's base is the current HEAD, `dae0de6`
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
- your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/slice-2-report.md`

Answers of the start of the cycle: trust boundary yes (this change adds a reader of session records and changes
`process-audit/audit_count.py`, the trust boundary of `process-audit`: crafted input at every reading must be
survived — missing fields, malformed lines, bars and control characters in text that reaches a cell, huge files);
irreversible operation no. Checks failing on the base: none (the whole gate passed on the base). The foundation
check `python -B elements/common/foundation_check.py --skip-test-citations` is NOT yours to fix beyond this slice's files.

The slice, copied word for word from the plan:

### Slice 2 — The measures script, for Codex sessions

- **Goal:** `task-cycle/cycle_measures.py` also reads Codex sessions, and its tests cover them. A session
  whose first line is a `session_meta` is a Codex orchestrator's rollout; a rollout that names a
  `parent_thread_id` is not given as a session. Its subagents are found as `task-cycle/cycle_stages.py` finds
  them: rollouts under `<codex home>/sessions` whose `session_meta` names the orchestrator's id, or the id
  of a subagent already found, as `parent_thread_id`; a subagent's name is its `agent_path`, else its
  `agent_nickname`, else its id. A forked subagent's rollout repeats its parent's history, so an agent's
  calls are only the `token_usage_record` entries whose `payload.thread_id` is the agent's own id, in the order
  of their time; the usage is read from `payload.usage`. The context of a Codex call is its
  `input_tokens`, which already holds the part read from the cache. Codex's record of a session gives no write to
  the cache, so for an agent of Codex the cache written (5 minutes and 1 hour), the cache written again
  and the calls with a cache write again are `unknown`, never zero; the first, middle and last call, the calls and
  the means are given. In the lines of the file, a value summed over agents is `unknown` where any
  agent it sums has it unknown: the lines of the cache written, and the orchestrator's or the
  subagents' lines of the cache written again. The table `## Agents` gives the tool `Codex` and `unknown` in those
  cells. A Codex call's needed fields are `payload.usage.input_tokens` and the `payload.thread_id` of the
  entry, and a rollout's `session_meta` needs `payload.id`; where one is missing, exit code 2 and an
  `Error:` line naming the rollout file and the field. Sessions of both tools may be named together; a
  cycle's measures then sum over both. Tests: a Codex orchestrator with two subagents, one of them
  forked and repeating history; the `unknown` cells and lines; a mixed Claude Code and Codex cycle; and, for the
  reading of a rollout, one test that gives a token usage entry without `input_tokens` and asserts exit code 2
  with an `Error:` line naming the file and the field (WAY-344).
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:28-33` To do, item 2 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:93-102` task-cycle · `foundations/part_map.md:231-239` External context · Foundation entries rows 1, 7 and the part-map row · `task-cycle/cycle_stages.py:274-470` the Codex reading · `task-cycle/cycle_stages.py:619-642` finding and reading a session · `task-cycle/test_cycle_stages.py:32-125` the Codex fixtures
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`, which reads session transcripts, untrusted input by the part map's External context
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` — the Codex tests fail before the slice and pass after; `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"`
- **Depends on:** Slice 1

Passages of the task and the plan its *Read* names, copied word for word:

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:28-33` To do, item 2

2. Nowy skrypt w `task-cycle/`, uruchamiany przy zamknięciu cyklu w tym samym kroku, w którym powstaje raport etapów, liczy z zapisów sesji cyklu i zapisuje do osobnego pliku w katalogu zapisu cyklu same liczby tokenów i wywołań, bez kwot:
   - liczbę wywołań modelu — w całym cyklu, osobno agenta prowadzącego cykl i każdego podagenta;
   - kontekst wywołania (wejście, odczyt z pamięci i zapis do pamięci razem) — dla każdego agenta w pierwszym, środkowym i ostatnim wywołaniu; dla cyklu średnią, osobno średnią agenta prowadzącego, oraz udział kontekstu przypadający na wywołania ponad 200 tys. tokenów;
   - tokeny zapisane do pamięci podręcznej, osobno z czasem życia 5 minut i godziny, dla każdego agenta;
   - tokeny zapisane do pamięci ponownie i liczbę wywołań z takim zapisem, osobno dla agenta prowadzącego i dla podagentów: w wywołaniu agenta po pierwszym ponownie zapisane jest to, co poprzednie wywołanie miało w pamięci (odczyt i zapis do pamięci), a obecne z niej nie odczytało, najwyżej tyle, ile obecne zapisało; liczy się tylko powyżej 2 tys. tokenów i tylko wtedy, gdy kontekst nie skurczył się o 30% lub więcej względem poprzedniego wywołania;
   - dla agenta Codexa zapis do pamięci i ponowny zapis są nieznane, nie zero: jego zapis sesji podaje tylko część wejścia odczytaną z pamięci.

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
- `foundations/invariants.md:116-125` script-imports
- `foundations/invariants.md:328-337` cross-part-imports
- `foundations/invariants.md:86-95` tracked-file-private-paths
- `foundations/part_map.md:93-103` task-cycle
- `foundations/part_map.md:232-240` External context
- `foundations/decisions.md:11494-11518` WAY-347 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11609-11639` WAY-351 (written by the foundation-entries agent of this change)

Files and ranges of code or tests to read (as its *Read* names them; read each as far as you need):

- `task-cycle/cycle_stages.py:274-470` the Codex reading
- `task-cycle/cycle_stages.py:619-642` finding and reading a session
- `task-cycle/test_cycle_stages.py:32-125` the Codex fixtures

Foundation entries of this change already written (commit `a030dbf`): WAY-347 to WAY-352, WAY-339 and WAY-344 changed
in place, and the trust boundary of `task-cycle` in `foundations/part_map.md` naming `task-cycle/cycle_measures.py`.

What slice 1 left (commits `f0a3829` and the fix `dae0de6`, reviewed PASS): `task-cycle/cycle_measures.py` reads Claude Code sessions and refuses a Codex rollout with exit 2 and `Error:` — this slice relaxes that refusal. Binding rulings from slice 1's review, which apply to your Codex reading too: the script must end with exit 2 and an `Error:` naming file, line and field for a missing or unreadable field it looks for data by (the time of a Codex entry used for ordering included — treat `timestamp` and `thread_id` as needed fields), for a JSON line that cannot be parsed, *including* a `ValueError` or `RecursionError` from `json.loads` on a deeply nested line or a number of more than 4300 digits (catch them, name the file and line), and a usage value that is no non-negative whole number. Reuse the helpers slice 1 wrote for those; read `task-cycle/cycle_measures.py` whole before changing it.

Return as `make-change` gives for a slice: status, commits (the slice's range from its base to its head), a one-line
check result naming what failed or did not run, the report path; in the report: each check with its command and exit
code, the own-work check, **Unread material** and **Searches not found or unclear** (each `none` where none), every
reach beyond this handoff, and the choices you made.
