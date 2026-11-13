**State: ready** — nothing waits for your answer; the three items in the last group you only accept by merging.

## What you will see

The weekly audit of the process now starts a new series of gate times whenever the command that runs every test of the-way changes between two versions of the process, just as it already did when the script that records the gate times changed. The audit's text says which of the two changed as the reason of the split. The series of the cost and of how the agents use context and the prompt cache are not split by it. The rule stands the same in the audit's instructions and in the decision that answers when the audit's measures stop being comparable, which gained the new case.

For you this means that from the next count, the runs of the gate from before the parallel directories (the previous merged request) and the runs after it stand in two series, so the weekly comparison no longer mixes a whole-run time that fell with directory times that rose. The audit counts again from the history of git at each count, so the cycles that ran after the previous request and before this merge are sorted into the new series as well.

The final gate of this change passed: 1267 tests in 10 directories, 12 minutes 27 seconds on this machine, with one other gate running at the same time.

### Underneath

The function that splits the series of one instrument now takes a list of files instead of one file, a new name holds the test runner, the audit's printed explanation, its instructions and the decision say the same, and two tests were added that fail on the old code.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. The decision about when the audit's measures stop being comparable now lists the part that holds the test runner among the parts it concerns. The task did not say so, but the decision now governs a change in a file of that part, and without it whoever checks a change of that part against the decisions would not find this one. The price: one more part named in the decision; a decision that lists a part is checked against every change of that part.
2. The audit's reason for a split names the file that changed, and both files where both changed in the same version. The task asks that the audit gives the change as the reason; I chose the name of the file over one fixed sentence, because you read this line to know what to remember about the two sides of a split. The price: the line is longer and holds two names in the rare version that changes both.
3. The merge of the target branch that came in while the cycle ran (the request about the agent types of the cycle) was not reviewed by a separate reviewer: it merged cleanly, it changed no file of the audit or of the test runner and none of the decisions this change edits, and the foundation check and the whole gate passed on the merged tree. The price: if the new decisions about agent types collide in meaning with the edited decision, nobody looked for it beyond those checks.

## Cost

Working time of the orchestrator's turns and the agents' turns: 32 minutes 44 seconds, of which 18 minutes 37 seconds waiting for tools; the two gate runs (10 and 12 minutes) ran beside, in the background. Models: the orchestrator and the three reviews on Claude Sonnet 5.5, the author on Claude Haiku 5.5 (the cheaper class, since the change is ordinary implementation); about 20.6 million tokens (19.7 million of them cached input, 124 thousand output). Review rounds: the review of the whole change failed once (one blocking finding, four Minor), one fix and one review of it passed, and the return step's commit was reviewed and passed. The table of stages is linked under *Record* below.

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record survives only when the commits are kept. The foundation has waited for a review through 35 merges since its last tag; the review is the skill `the-way-review-foundation`, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: gotowa** — nic nie czeka na Twoją odpowiedź; trzy pozycje w ostatniej grupie tylko przyjmujesz przez scalenie.

## Co zobaczysz

Cotygodniowy audyt procesu zaczyna teraz nową serię czasów bramki za każdym razem, gdy polecenie uruchamiające wszystkie testy the way zmieni się między dwiema wersjami procesu, tak jak dotąd robił to przy zmianie skryptu, który te czasy zapisuje. Tekst audytu podaje, który z dwóch plików się zmienił, jako powód podziału. Serie kosztu i tego, jak agenci używają kontekstu i pamięci podręcznej promptów, nie są przez to dzielone. Reguła stoi tak samo w instrukcji audytu i w decyzji odpowiadającej, kiedy miary audytu przestają być porównywalne, która dostała nowy przypadek.

Dla Ciebie znaczy to, że od następnego liczenia przebiegi bramki sprzed równoległych katalogów (poprzednia scalona prośba) i przebiegi po nich stoją w dwóch seriach, więc cotygodniowe porównanie nie miesza już czasu całego przebiegu, który spadł, z czasami katalogów, które wzrosły. Audyt przy każdym liczeniu wylicza serie od nowa z historii gita, więc cykle, które przebiegły po poprzedniej prośbie, a przed tym scaleniem, też trafią do nowej serii.

Końcowa bramka tej zmiany przeszła: 1267 testów w 10 katalogach, 12 minut 27 sekund na tej maszynie, przy jednej innej bramce działającej w tym samym czasie.

### Pod spodem

Funkcja dzieląca serie jednego przyrządu bierze teraz listę plików zamiast jednego pliku, nowa nazwa trzyma skrypt testów, wypisywane objaśnienie audytu, jego instrukcja i decyzja mówią to samo, a dodano dwa testy, które na starym kodzie padają.

## Do twojej decyzji

### Wymagane od Ciebie

none

### Do poprawienia albo przepuszczenia

none

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

1. Decyzja o tym, kiedy miary audytu przestają być porównywalne, wymienia teraz wśród części, których dotyczy, część z skryptem testów. Zadanie tego nie mówiło, ale decyzja rządzi teraz zmianą w pliku tej części, a bez tego ten, kto sprawdza zmianę tej części z decyzjami, by jej nie znalazł. Cena: jedna część więcej w decyzji; decyzję wymieniającą część sprawdza się przy każdej zmianie tej części.
2. Powód podziału w audycie podaje nazwę pliku, który się zmienił, a w rzadkiej wersji, która zmienia oba pliki, oba. Zadanie prosi, żeby audyt podał zmianę jako powód; wybrałem nazwę pliku zamiast jednego stałego zdania, bo tę linię czytasz, żeby wiedzieć, co zapamiętać o obu stronach podziału. Cena: linia jest dłuższa i trzyma dwie nazwy w rzadkiej wersji zmieniającej oba pliki.
3. Scalenie gałęzi docelowej, które weszło w trakcie cyklu (prośba o typy agentów cyklu), nie miało osobnej recenzji: weszło czysto, nie zmieniło żadnego pliku audytu ani skryptu testów i żadnej z decyzji, które ta zmiana edytuje, a kontrola fundamentu i cała bramka przeszły na scalonym drzewie. Cena: jeśli nowe decyzje o typach agentów kolidują znaczeniem z edytowaną decyzją, nikt tego nie szukał poza tymi kontrolami.

## Koszt

Czas pracy tur orkiestratora i agentów: 32 minuty 44 sekundy, z czego 18 minut 37 sekund to oczekiwanie na narzędzia; dwa przebiegi bramki (10 i 12 minut) biegły obok, w tle. Modele: orkiestrator i trzy recenzje Claude Sonnet 5.5, autor Claude Haiku 5.5 (klasa tańsza, bo zmiana to zwykła implementacja); około 20,6 mln tokenów (19,7 mln z nich to wejście z pamięci podręcznej, 124 tys. wyjście). Rundy przeglądu: przegląd całej zmiany nie przeszedł raz (jedna uwaga blokująca, cztery Minor), jedna poprawka i jej przegląd przeszły, a commit kroku powrotnego został przejrzany i przeszedł. Tabela etapów jest podlinkowana pod *Record* niżej.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase: link do zapisu przetrwa tylko przy zachowanych commitach. Fundament czeka na przegląd po 35 scaleniach od ostatniego tagu; przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium, a nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

1. Commit `909fcb9` — `process-audit/audit_count.py`: new constant `GATE_TEST_RUNNER = "gate/run_tests.py"` and the tuple `GATE_SCRIPTS`; `instrument_series` takes a tuple of files, one `git diff --quiet` over all of them decides a split, and the reason names the files that changed; the mechanism measures still split on `task-cycle/cycle_measures.py` alone; the text of *Measure versions* and the module docstring say the same. `process-audit/test_audit_count.py`: two new tests (a runner change starts a gate series only; the reason names the changed files and a runner change splits no mechanism series) that failed on the old code, and the price-list test passes tuples. `process-audit/SKILL.md`: the paragraph *Measures are compared inside a series only* says the same. `foundations/decisions.md`: WAY-339 changed in place.
2. Commit `b8dc239` — the fix of the review's findings, in WAY-339 only: the correct *violates* bullet about a change of the script that records the gate times is restored beside the new test-runner bullet; the runner is named "of the process" (not "of the gate") in the binding sentence, *Verification* and *Rationale*; *Rejected* no longer speaks of this change being merged; the last *Rationale* sentence gives the task's reason that the test runner is part of the measurement.
3. Commit `5b87cb1` — the return step re-wrapped the *Rejected* paragraph of WAY-339 to the width of the entry after the fix; the word-level diff is empty.
4. Merge `1f7dab2` — the target branch at `f04f046` (the agent types of the cycle, WAY-368 to WAY-370) merged in, no conflict.

## Checks

- The gate on the merged final tree: `python -B task-cycle/gate_times.py --output docs/task-cycles/gate-series-on-test-runner/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1267 tests in 10 directories, every directory passed, 747 seconds, with one other gate running at the same time (WAY-350 shows such a run apart). The same command on the tree before the merge (`5b87cb1`): exit 0, 1240 tests, 610 seconds. No check failed or did not run, and none failed and passed again.
- Base: the starting state `715ae20` is a merge commit with the same tree as its second parent, so no gate ran on it; the list of tests failing before the change, none, was taken from the final gate of the cycle `gate-parallel-directories` (exit 0, 1238 tests), from its record at commit `575f286`, file `docs/task-cycles/gate-parallel-directories/cycle.md`.
- Own-work check of the author: the two new tests failed on the old code (the medians of the gate series; an `IndexError` on the missing reason) and pass now; `python -B gate/run_tests.py process-audit` exit 0, 182 tests; `python -B elements/common/foundation_check.py` exit 0, 0 errors. The reviewer repeated the focused checks, ran `python -B task-cycle/change_file_sizes.py 715ae20 909fcb9` (exit 0) and a scratch run showing that `git diff --quiet` over a history without `gate/run_tests.py` exits 0 (no spurious split) and exits 1 where the file is added.
- The state of user-interface screens: not applicable, the change touches no screen.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `merges: 35`, `threshold: 30`, `reminder: yes`.
- `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` for the orchestrator's session: both exit 0.
- On the copy of the record and on this description: written and checked after this description was first published (see the edit that adds the record's link).

## Foundation entries

- WAY-339, row 1: a change of the test runner of the process (`gate/run_tests.py`) starts a new series of the audit's gate times, as a change of the script that records them does, because the test runner is part of the measurement; it splits no series of the cost or of the use of context and cache; its *Scope* now also names the part `gate`, the one choice of the cycle that goes beyond the row (item 1 of *You accept by merging*), and its *Rejected* records the two ways the task did not choose, a mark on each run and no split, with their costs.

No invariant, environment fact, glossary entry or part-map entry is written, and no invariant test, surface or *Violated* mark is changed.

## Minor findings

1. Review of the whole change. Structure (`process-audit/audit_count.py`, `process-audit/test_audit_count.py`). The reviewer: "`process-audit/audit_count.py` is 2983 lines and `test_audit_count.py` 3186; the change adds 11 and 58 lines. The-way has no coding guidelines and no rule of size (WAY-328), so there is no threshold test to run. The functions the diff reaches (`instrument_series`, `measure_versions`, `measure_versions_lines`) grew by a few lines each; `instrument_series` is about 20 lines. No code without a user (the constant `GATE_SCRIPT` still has users; `GATE_SCRIPTS` is used once). No name has stopped being true. Nothing to grade above Minor; noted for completeness, no change asked." Nothing was changed; the files are long and grew by a little.

The other three Minor findings of that review and the Minor finding of the review of the fix (unwrapped lines of *Rejected*) were fixed in `b8dc239` and `5b87cb1`.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task from the author's backlog, ready for cycle: the weekly audit starts a new series of gate times also at a change of the test runner, and the rule and the decision say the same. Sources: the task's *Questions to settle* (answer of 2026-11-13, "1 a"), its *Decisions in play* and the one row of *Settlements to record*; the-way at `715ae20` of `foundations`.
- **Process pin:** none; the-way itself, base `715ae20` of `foundations`; no gate ran on the base (the list of failing tests, none, taken from the earlier cycle's final gate, see *Checks*).
- **Spec:** none written; no open design choice.
- **Route:** one author without a plan, class `cheaper` (Claude Haiku 5.5), because the change is ordinary implementation; review of the whole change by a fresh reviewer on Sonnet (`FAIL`, one blocking and four Minor findings within the task); one fix and one review of it by the same reviewer (`PASS`, one new Minor finding); the reviewer read in a second turn the invariants and the glossary its own selection had left unread (no new finding); the return step committed a re-wrap (`PASS`, no finding).
- **Plan:** none on this route.
- **Choices:** 3 choices of the cycle beyond the questions answered by a binding source (the record's questions table holds the one about the merge, Q2; items 1 to 3 of *You accept by merging*).
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds it, written after the commit.
