**State: ready** — one item waits for your answer: whether the audit of the process gets a new series of gate times (a task, or let through); the rest you only accept by merging.

## What you will see

The command that runs every test of a repository now starts all test directories at the same time, each in a process of its own, instead of one after another. Each directory's report appears whole, under its own heading line, when that directory ends, so reports no longer mix, and the last line still counts the tests and names the directories that failed. Two new options exist: one limits how many directories run at once (the value 1 runs them one after another, as before) and one lists the slowest tests with their times. A product that cannot run its tests side by side, such as one whose tests use Docker and fail under load, writes the limit into its own gate command; nothing else in the command changes, and without the options the output looks as before. The game's own gate is not changed here; that is a separate task of the game's repository.

The cycle's first step also changes. When the state a cycle starts from is a merge commit whose files are exactly the files of the branch that was merged, the cycle no longer runs the whole gate on that state: it takes the list of tests that were already failing from the final gate of the cycle that made the merged branch, red or not, writes into its record where it took them from, and goes on. In any other case it runs the gate on the starting state as before. When the cycle's own final gate then fails on a test that is not on that list, the cycle runs the failing tests on the starting state to tell a fault of the change from a fault already there, and writes the result into its record. This saves one full run of the gate in most cycles: 99 of the last 111 merged branches of this repository started from such a state.

The final gate of this change took 11 minutes 37 seconds on this machine and passed, 1238 tests in 10 directories. That is one run beside other work, not a controlled measurement, and it is not the 15 to 16 minutes against 23 to 24 that the task estimated for the game; the-way's own gate was already short, and one directory (the audit's tests) now takes nearly the whole run, so the gain here is small.

### Underneath

The runner starts one process per directory in a pool and prints each finished report in one piece; the cycle's instructions, its record template and the description template speak of a run on the starting state only where the cycle makes one; the decision log gains two decisions and one existing decision is changed by one sentence.

## For you to decide

### Needed from you

none

### Fix or let through

1. From now on every directory of the gate runs while the others run, so the time a record shows for one directory is its time under that load, and the time of the whole run falls. The weekly audit of the process starts a new series of gate times only when the script that measures them changes, and this task leaves that script untouched, as it asks. So the next audits will put runs of the two kinds into one series: the median of the whole run will fall, the medians of single directories will rise, and the audit will compare them as if one version of the process were faster or slower than another. Ways: do it in this request — change the audit's rule or the script so that a new series begins, which costs a fix round with its review and touches the script the task keeps as it is; make a task of it — the audits mix the two kinds of runs until that task is done, and whoever reads them has to remember it; let it through — accept the mixed series, which ends in effect once the runs of the new kind outnumber the old ones. I recommend making a task of it, because the change to the audit is outside this task and the mixing is harmless for a few weeks if the audit's reader knows of it. Do it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. When no limit is given, the gate starts every directory at once, not as many as the machine has processors. On this repository that is ten processes at once; in a product with more directories more, and the memory of the machine is shared between them (the task names that cost). A processor-count default would make the same gate take different times on two machines. The price: a product on a small machine writes the limit into its command.
3. A directory's report now appears when its process ends, also when the limit is 1, so a run no longer shows lines as they are printed; a directory that hangs shows nothing until it is killed. The task asks for whole reports without mixing, which a live view cannot give while directories run together; I chose whole reports over a prefix on each line, which the task does not ask for.
4. Where the merged branch added its copy of the cycle's record more than once (a correction repeats it), the cycle's first step takes the last copy, because the last copy holds the last final gate. The task says only "the final gate of that cycle"; the reviewer judged that this follows its direction and does not go beyond it.
5. One existing decision about how the gate is run through the measuring script is changed by one sentence and its check: the run on the starting state goes through the script when the cycle makes it, and the check requires that run only in such a cycle. The task asks for this and your answer "1 a" accepted it; it stays here because it changes a decision you saw before the cycle wrote it.

## Cost

Working time of the cycle's agents across the orchestrator's session: 57 minutes 37 seconds, of which 29 minutes 53 seconds waiting for tools. Models: the orchestrator, the author and the reviewer all Claude Sonnet 5.5 (the author on the orchestrator's class, because the change reaches two parts and writes decisions); about 41.2 million tokens (39.7 million of them cached input, 197 thousand output). Review rounds: the review of the whole change passed with five Minor findings within the task; one fix and one review of it, passed with two new Minor findings; in the same turn the reviewer read the decisions it had left unread, nothing changed. The gate ran twice, on the base (22 minutes 37 seconds, with the author's checks beside it) and on the final tree (11 minutes 37 seconds). The table of stages is in the committed record, linked under Record.

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record survives only when the commits are kept. The foundation has waited for a review through 33 merges since its last tag; the review is the skill `the-way-review-foundation`, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: gotowa** — jedna pozycja czeka na Twoją odpowiedź: czy audyt procesu dostaje nową serię czasów bramki (zadanie, czy przepuścić); resztę tylko przyjmujesz przez scalenie.

## Co zobaczysz

Polecenie, które uruchamia wszystkie testy repozytorium, startuje teraz wszystkie katalogi testów jednocześnie, każdy w osobnym procesie, zamiast jeden po drugim. Raport każdego katalogu pojawia się w całości, pod jego własną linią nagłówka, gdy ten katalog się skończy, więc raporty już się nie mieszają, a ostatnia linia nadal liczy testy i nazywa katalogi, które padły. Są dwie nowe opcje: jedna ogranicza, ile katalogów biegnie naraz (wartość 1 uruchamia je po kolei, jak dotąd), druga wypisuje najwolniejsze testy z ich czasem. Produkt, który nie może uruchamiać swoich testów obok siebie, na przykład taki, którego testy z Dockerem padają pod obciążeniem, wpisuje limit do własnego polecenia bramki; nic innego w poleceniu się nie zmienia, a bez opcji wynik wygląda jak dawniej. Bramka gry nie jest tu zmieniana; to osobne zadanie repozytorium gry.

Zmienia się też pierwszy krok cyklu. Gdy stan, z którego cykl startuje, jest commitem scalenia, którego pliki są dokładnie plikami scalonej gałęzi, cykl nie uruchamia już na nim całej bramki: bierze listę testów, które już padały, z końcowej bramki cyklu, który zrobił scaloną gałąź, czerwonej albo nie, wpisuje do swojego zapisu, skąd ją wziął, i idzie dalej. W każdym innym przypadku uruchamia bramkę na stanie wyjściowym jak dotąd. Gdy końcowa bramka cyklu pada potem na teście spoza tej listy, cykl uruchamia padające testy na stanie wyjściowym, żeby odróżnić błąd zmiany od błędu zastanego, i wpisuje wynik do zapisu. To oszczędza jeden pełny przebieg bramki w większości cykli: 99 z ostatnich 111 scalonych gałęzi tego repozytorium startowało z takiego stanu.

Końcowa bramka tej zmiany trwała na tej maszynie 11 minut 37 sekund i przeszła, 1238 testów w 10 katalogach. To jeden przebieg obok innej pracy, nie pomiar kontrolowany, i nie jest to 15–16 minut zamiast 23–24, które zadanie szacowało dla gry; bramka the way była już krótka, a jeden katalog (testy audytu) zajmuje teraz prawie cały przebieg, więc zysk tu jest mały.

### Pod spodem

Skrypt uruchamia po jednym procesie na katalog w puli i wypisuje każdy skończony raport w jednym kawałku; instrukcja cyklu, szablon zapisu i szablon opisu prośby mówią o przebiegu na stanie wyjściowym tylko tam, gdzie cykl go robi; dziennik decyzji zyskuje dwie decyzje, a jedna istniejąca zmienia się jednym zdaniem.

## Do twojej decyzji

### Wymagane od Ciebie

none

### Do poprawienia albo przepuszczenia

1. Od teraz każdy katalog bramki biegnie, gdy biegną pozostałe, więc czas, który zapis pokazuje dla jednego katalogu, jest jego czasem pod takim obciążeniem, a czas całego przebiegu spada. Cotygodniowy audyt procesu zaczyna nową serię czasów bramki tylko wtedy, gdy zmieni się skrypt, który je mierzy, a to zadanie zostawia ten skrypt bez zmian, tak jak każe. Następne audyty wrzucą więc przebiegi obu rodzajów do jednej serii: mediana całego przebiegu spadnie, mediany pojedynczych katalogów wzrosną, a audyt porówna je tak, jakby jedna wersja procesu była szybsza albo wolniejsza od drugiej. Warianty: zrobić to w tej prośbie — zmienić regułę audytu albo skrypt tak, żeby zaczęła się nowa seria, co kosztuje rundę poprawki z jej przeglądem i dotyka skryptu, który zadanie zostawia; zrobić z tego zadanie — audyty mieszają oba rodzaje przebiegów, aż zadanie będzie zrobione, i czytający musi o tym pamiętać; przepuścić — przyjąć mieszaną serię, która traci znaczenie, gdy przebiegów nowego rodzaju będzie więcej niż starych. Polecam zrobić z tego zadanie, bo zmiana audytu wykracza poza to zadanie, a mieszanie jest nieszkodliwe przez kilka tygodni, jeśli czytający audyt o nim wie. Zrobić to w tej prośbie, zrobić z tego zadanie, czy przepuścić? (Findings outside the task's scope, 1)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Gdy nie podano limitu, bramka startuje wszystkie katalogi naraz, a nie tyle, ile maszyna ma procesorów. W tym repozytorium to dziesięć procesów naraz; w produkcie z większą liczbą katalogów więcej, a pamięć maszyny jest dzielona między nimi (zadanie nazywa ten koszt). Domyślna liczba z liczby procesorów sprawiłaby, że ta sama bramka trwa różnie na dwóch maszynach. Cena: produkt na małej maszynie wpisuje limit do swojego polecenia.
3. Raport katalogu pojawia się teraz, gdy jego proces się kończy, także przy limicie 1, więc przebieg nie pokazuje już linii w miarę ich drukowania; katalog, który się zawiesi, nie pokazuje nic, dopóki nie zostanie zabity. Zadanie prosi o raporty w całości bez mieszania, czego widok na żywo nie da, gdy katalogi biegną razem; wybrałem całe raporty zamiast przedrostka przy każdej linii, o który zadanie nie prosi.
4. Gdy scalona gałąź dodała kopię zapisu cyklu więcej niż raz (poprawka ją powtarza), pierwszy krok cyklu bierze ostatnią kopię, bo ona niesie ostatnią końcową bramkę. Zadanie mówi tylko „końcowa bramka tamtego cyklu”; recenzent uznał, że to idzie w jego kierunku i go nie przekracza.
5. Jedna istniejąca decyzja o tym, jak bramka jest uruchamiana przez skrypt pomiarowy, zmienia się jednym zdaniem i swoim sprawdzeniem: przebieg na stanie wyjściowym idzie przez skrypt, gdy cykl go robi, a sprawdzenie wymaga tego przebiegu tylko w takim cyklu. Zadanie o to prosi, a Twoja odpowiedź „1 a” to przyjęła; stoi tu, bo zmienia decyzję, którą widziałeś przed napisaniem jej przez cykl.

## Koszt

Czas pracy agentów cyklu w sesji orkiestratora: 57 minut 37 sekund, z czego 29 minut 53 sekundy to oczekiwanie na narzędzia. Modele: orkiestrator, autor i recenzent Claude Sonnet 5.5 (autor na klasie orkiestratora, bo zmiana dotyka dwóch części i pisze decyzje); około 41,2 mln tokenów (39,7 mln z nich to wejście z pamięci podręcznej, 197 tys. wyjście). Rundy przeglądu: przegląd całej zmiany zakończył się wynikiem PASS z pięcioma uwagami Minor w zakresie zadania; jedna poprawka i jeden jej przegląd, PASS z dwiema nowymi uwagami Minor; w tej samej turze recenzent doczytał decyzje, których wcześniej nie przeczytał, nic się nie zmieniło. Bramka biegła dwa razy, na bazie (22 minuty 37 sekund, z kontrolami autora obok) i na końcowym drzewie (11 minut 37 sekund). Tabela etapów jest w zatwierdzonym zapisie, do którego link stoi w sekcji Record.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase: link do zapisu przetrwa tylko przy zachowanych commitach. Fundament czeka na przegląd po 33 scaleniach od ostatniego tagu; przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium, a nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

1. Commit `a6807f1` — `gate/run_tests.py` and `gate/test_run_tests.py`: without a directory the runner starts the directories in a pool (`--jobs N` at most N at once, default all, a wrong value exits 2 with a message; `--slowest N` passes `durations=N` to `unittest`, exit 2 with a message where `unittest` has none) and prints each directory's whole report, under its `== <directory>` line, when its process ends; the last line and the exit codes are as before. `task-cycle/test_gate_times.py` gains a test that feeds `gate_times.py` the runner's output; `gate_times.py` is not changed. The runner's docstring is brought up to date.
2. Commit `9bea9a1` — the decision log: WAY-366 (the gate runs directories in parallel by default, an option limits the number, a product writes it into its gate command) and WAY-367 (the cycle skips the gate on a starting state that is a merge commit with the tree of the merged branch's head, takes the list of failing tests from that cycle's final gate, runs the failing tests on the starting state when the final gate fails outside the list), and WAY-349 changed in place by one sentence and its *Verification*.
3. Commit `264703f` — `task-cycle/skill/SKILL.md` step 4 (the check in git, the list taken from the earlier cycle's record, the fall back to running the gate, item 5's run of the failing tests), step 2 and step 10 (a run on the starting state only where step 4 requires it), `task-cycle/record_template.md` (*Verification* names the list's source), `task-cycle/skill/request_template.md` (the checks failing on the base, from its run or from the list) and `agent-instructions/README.md` (the options and the time of a full run: "about 16 minutes with `--jobs 1`, and less by default").
4. Commit `9282e6f` — the fix of the five Minor findings of the review of the whole change: queued directories are cancelled on an interrupt with a test that fails without it, the sentence on the creation of `gate_times.md` in `task-cycle/record_template.md` names step 10's run where step 4 skips its own, step 4 names the path as the merged branch's copy and gives the `git log` that finds it, the rendezvous tests wait 120 s instead of 30 s, and uneven line wraps are redone without changing a word.
5. The return step compared the three decisions, those the task names, WAY-350 and WAY-63 and the part-map entries `gate`, `task-cycle` and `test-runner-command` with the repository, found nothing that no longer matched and committed nothing.

## Checks

- The gate on the final tree: `python -B task-cycle/gate_times.py --output docs/task-cycles/gate-parallel-directories/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1238 tests in 10 directories, every directory passed, 697 seconds in one run. On the base the same command exited 0 with 1221 tests in 1357 seconds, beside the author's focused checks. No check failed or did not run, and none failed and passed again in the cycle. Not measured: the memory of a full parallel run (the run passed, the machine holds 32 GB), the option `--slowest` on a real Python older than 3.12 (none on this machine; the product's Python is 3.14), and a real Ctrl-C at a console; the interrupt is tested by simulation.
- Own-work check of the author: the new tests failed on the base runner first (8 of 33) and pass on the new one; the runner's output with `--jobs 1` compared with the base runner's on a temporary repository of four directories, `diff` exit 0 after one blank-line fix; `python -B elements/common/foundation_check.py` exit 0 (0 errors). The reviewers repeated the focused checks on both heads, ran mutations of the runner that the new tests detect, and ran the interrupt test 55 times without a failure, 30 of them under heavy load.
- The state of user-interface screens: not applicable, the change touches no screen.
- The rule of item 4 tried on this repository: the base `f749cfc` has a tree equal to the tree of the merged branch's head, and the earlier cycle's record is found with the `git log` of step 4 (the copy of the cycle `close-decision-pending-templates`, final gate exit 0, 1221 tests). The cycle ran the gate on the base nevertheless, as the rule was not yet in force.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `merges: 33`, `threshold: 30`, `reminder: yes`.
- `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` for the orchestrator's session: both exit 0.
- On the copy of the record and on this description: written and checked after this description was first published (see the edit that adds the record's link).

## Foundation entries

- WAY-366, row 1: the gate runs the directories of tests in parallel by default, prints each directory's report whole when it ends, and an option limits the number at once, 1 running them one after another, which a product writes into its one gate command.
- WAY-367, row 2: the cycle skips the gate on its starting state when that is a merge commit whose tree equals that of the merged branch's head, takes the failing tests from the final gate of that branch's cycle from its record in git history and records the source; otherwise it runs the gate there; when its final gate fails on a test outside the list it runs the failing tests on the starting state, for diagnosis only. The author's text says "most of the time" where the task's reasons say "two thirds"; the reviewer judged it faithful.
- WAY-349, `the cycle's` (it is no row; the task's *Decisions in play* carries it): the run on the starting state goes through the script in a cycle that makes it, and *Verification* asks for that run only in such a cycle.

No invariant, environment fact, glossary entry or part-map entry is written, and no invariant test, surface or *Violated* mark is changed.

## Minor findings

1. Review of the fix. `gate/run_tests.py:124-151` — "only an interrupt cancels the queue; an exception of a worker does not." If `run_directory` raises (a failure to start the process, say), the error shows only after every queued directory ended; in a scratch run the error appeared after 9.1 seconds and the three other directories ran silently. The reviewer: "A rare failure (Python cannot start a child), and the same class as the first finding, so Minor. A `finally`/`except BaseException` that cancels the queue would cover both cases. Not covered by a test."
2. Review of the fix. `gate/test_run_tests.py`, the interrupt test — "imports the runner with `runpy.run_path` and reaches `loaded['concurrent'].futures`". The reviewer: "A change of that import (`from concurrent.futures import ...`) would break the test with a `KeyError`, not with a message about the interrupt. Minor, and no effect today."

## Findings outside the task's scope

1. Review of the whole change. The audit reads the gate times as one series across this change (`process-audit/SKILL.md` lines 57–60). The reviewer: "After this change each directory's own `Ran ... in <s>s` is its time under the load of the directories beside it, and the time of the whole run falls, so one median of the version before and one of the version after hold runs of two kinds: the per-directory medians rise, the run median falls, and the audit would compare them. WAY-350's count of 'other gate runs' counts runs of the script, not the directories inside one run, so it does not separate them." Judged to reach the human working with the process: item 1 of *Fix or let through*.

## Course of the cycle

- **Task and sources:** an independent task from the author's backlog, ready for cycle: the gate runs its test directories in parallel with a limit and a list of the slowest tests, and the cycle skips the gate on a starting state that repeats the earlier cycle's final gate. Sources: the task's *Questions to settle*, the answers of 2026-11-12 and 2026-11-13, the decisions in play; the-way at `f749cfc` of `foundations`.
- **Process pin:** none; the-way itself, base `f749cfc` of `foundations`; the gate on the base exited 0 with 1221 tests.
- **Spec:** none written; no open design choice.
- **Route:** one author without a plan, class `same` (Sonnet) because the change reaches two parts and writes decisions; review of the whole change by a fresh reviewer on Sonnet (`PASS`, five Minor findings within the task); one fix and one review of it (`PASS`, two new Minor findings); the same reviewer read the decisions it had named unread (`PASS`, nothing changed); return step with nothing to correct.
- **Plan:** none on this route.
- **Choices:** 3 choices of the cycle beyond the questions answered by a binding source (the record's questions table, Q2 to Q4; items 2 to 4 above).
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds it, written after the commit.
