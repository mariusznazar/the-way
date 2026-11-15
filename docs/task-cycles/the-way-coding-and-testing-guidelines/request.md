**State: ready** — two items in "Fix or let through" wait for your answer; everything else is accepted by merging.

## What you will see

The-way now holds its own coding guidelines and testing guidelines, in a new directory of the repository, and the two lines that tell an agent when to read them stand in the root instruction file. Until now the-way's own code and tests were exempt from the guidelines every product gets, with no time limit; that exemption is withdrawn. The coding guidelines name a linter (Ruff 0.17.1, pinned by version and by the checksum of every wheel), say that the-way keeps no automatic formatter and no audit of dependencies and why, cap a function at 80 lines and a script file at 1000, and describe six kinds of scripts (checks, measuring reports, generators, scripts that change the repository, scripts that run one command, shared modules), each with a model file and a rule that a test holds. The testing guidelines describe five levels of tests with a model test for each, where an expected value may come from, and what the-way deliberately does not test.

How the work changes: Ruff must be installed once, by the steps in the README, into a local environment in the main checkout; the gate is red without it, and CI now installs it before the tests. The gate gained two tests that fail on purpose and are marked as expected failures — one for the places where the code still breaks a blocking rule of the linter (25 places remain), one for the functions and files still over the size cap (11 functions and 3 script files). They turn into ordinary failing tests the day someone cleans the last place, which is the signal to remove the mark. The scripts that read a Codex session now stop with an error that names the file and the field when a token count or an identifier is missing, instead of reporting a cost that is too low; six scripts at the edge of the repository got a written rule that a test cites; and about twenty places in tests were cleaned of the faults the audit named (expected values taken from the code they check, a real clock, the user's own git configuration).

### Underneath

Forty entries of the foundation were written or changed by the task (decisions, invariants, glossary terms, environment facts, one part-map line each for the new files); the gate ran once on the final state and passed (1596 tests in 11 directories).

## For you to decide

### Needed from you

none

### Fix or let through

1. The review of the whole change and the review of the return step were asked to run on the strongest model, but the record of the run shows them on the same model as the rest of the work, so the strongest class was not applied. If that review missed something, whoever works with the new guidelines meets it on a later task. Running the review again with a stronger model costs a session of about forty minutes and one more round of review; undoing it costs nothing. Making a task of it costs a later session; undoing it, nothing. Letting it through costs nothing now, and a missed flaw costs a correction later. I recommend letting it through, since that review found four blocking problems that were all fixed and the check of the fix found none new. Its weak point: a review by the same class can share the blind spots of the work it reviews. Run it again with a stronger model, make a task of it, or let it through?
2. A few small things were found and not fixed, none of which a user of the process will meet often: a time written with the letter Z in place of the separator is now accepted by the script that measures cycles; a line of a Claude Code session that is valid JSON but not an object is skipped, while the same line in a Codex session stops the run with an error; three decisions keep examples that repeat what a test already holds; one decision says time is given "as the option does" where the tests replace the clock instead; no test compares the installer's list of skills with the list written in its test; a new script that copies the one script allowed to overwrite a named report file inherits that (Minor findings, 1–7). Fixing them now costs a round of review; undoing it, nothing. Making one task of them costs a later session, and leaving them costs nothing today; they would show up as a reviewer's remark when someone next changes those scripts. I recommend letting them through, since each is rare or only about wording. Its weak point: they are seven separate remarks and nothing collects them once this request is merged. Fix them in this request, make one task of them, or let them through?

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The task said ten parts of the-way hold Python; at the time of the work there were eleven, because a test of the guidelines' references was added after the task was written. The linter, the size test and both guidelines read all eleven. The one sentence on where that eleventh part's complexity lies, which the task did not settle, says "in computation" — my proposal, which only decides where a mutation tool could run one day. The other way was to leave that file unread by both checks.
4. The three words for kinds of tests became "files test", "git test" and "repository test", not the bare "files", "git" and "repository" the task wrote, because bare "git" and "repository" would turn every use of those common words in the foundation into a possible second meaning. Renaming back is a small edit.
5. The rule that a script which changes the repository changes nothing without being told now excepts the report file the human names with an option: one script opens that file for writing before it checks whether it was told to act, so a human who names a tracked file loses it. The review of the whole change found the rule said "never" while the script did it; I narrowed the rule (and the decision that restates it) rather than mark it violated or change the script, which the task did not ask for. Marking it violated would have meant an expected failure for a case no one meets by accident.
6. Two rules stand as known violations, with their tests marked as expected failures: the linter's blocking rules (25 places remain, 17 of the places the audit named were cleaned) and the size cap (the task counted 2 script files over 1000 lines, a third has grown over since). The gate stays green; the review of each later change to the cleaned files is what keeps them from breaking again (Foundation entries).
7. The test that checks the-way's foundation inside the gate now keeps only the findings of two invariants (references to parts and the citation of tests), because it failed in a clone whose main branch has another name. So an ordinary error of the foundation, such as a number that names no decision, no longer turns the gate red; the cycle's own step still runs the whole check. That is what the task asked for, and the README says it.
8. Some sentences of the new decisions go beyond a row of the task, so that an agent following them has what it needs: the rule that a part which gains Python code is added to the scope of two decisions; the rule that a new dependency other than the linter ends the departure from the dependency audit; the way back to a formatter; how the end-to-end level is described; and the rule of each kind written beside its model file. Other small choices stand in the questions table of the record: the guidelines leave out the template's rows on property tests, on doubles of other services and on smoke tests, because no test level of the-way has them; the two kinds with nothing a test checks have no rule; the command-runner rule is tested on one script only, since the gate runner wraps no single command; the task's answer that the reviewer checks tests in the head follows the decision it cites, which says the author does (Technical changes; Foundation entries).

## Cost

About five hours of working time across 95 stages (two hours of it waiting for tools), 263 million tokens (212 million on Sonnet 5.5, 51 million on Haiku 5.5), seven reviews of slices (one of them of a fix), two reviews of the whole change (one of its fix, after a first reviewer stopped by accident) and one of the return step, two fixes after a failed review (slice 4 and the whole change), one full run of the gate (332 seconds). The table of stages is in the committed record: the committed record, linked by its commit in the next edit of this description/stages.md.

## How to merge

Merge so that the commits are kept (the repository's own pull requests are merged as "Merge pull request"), since the link to the record survives only then.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — dwie pozycje w „Do poprawy albo przepuszczenia” czekają na Twoją odpowiedź; reszta jest przyjmowana przez scalenie.

## Co zobaczysz

The way ma teraz własne wytyczne kodu i wytyczne testów, w nowym katalogu repozytorium, a w głównym pliku instrukcji stoją dwie linie mówiące agentowi, kiedy je czytać. Dotąd kod i testy samego the way były zwolnione z wytycznych, które dostaje każdy produkt, bez limitu czasu; to zwolnienie jest wycofane. Wytyczne kodu wskazują linter (Ruff 0.17.1, przypięty wersją i sumą kontrolną każdego koła), mówią, że the way nie ma automatycznego formatera ani audytu zależności i dlaczego, ograniczają funkcję do 80 linii, a plik skryptu do 1000, i opisują sześć rodzajów skryptów (kontrole, raporty pomiarowe, generatory, skrypty zmieniające repozytorium, skrypty uruchamiające jedno polecenie, moduły współdzielone), każdy ze wzorcowym plikiem i regułą pilnowaną testem. Wytyczne testów opisują pięć poziomów testów ze wzorcowym testem każdego, skąd może pochodzić wartość oczekiwana i czego the way świadomie nie testuje.

Jak zmienia się praca: Ruff trzeba raz zainstalować, według kroków z README, do lokalnego środowiska w głównym checkoucie; bez niego bramka jest czerwona, a CI instaluje go teraz przed testami. Bramka dostała dwa testy, które padają celowo i są oznaczone jako oczekiwane porażki: jeden dla miejsc, w których kod nadal łamie zatrzymującą regułę lintera (zostaje 25 miejsc), drugi dla funkcji i plików nadal ponad limitem (11 funkcji i 3 pliki skryptów). Zamienią się w zwykłe padające testy w dniu, gdy ktoś posprząta ostatnie miejsce, i to będzie znak, żeby zdjąć oznaczenie. Skrypty czytające sesję Codexa kończą się teraz błędem z nazwą pliku i pola, gdy brakuje liczby tokenów albo identyfikatora, zamiast podawać koszt za niski; sześć skryptów na brzegu repozytorium ma zapisaną regułę odmowy, którą cytuje test; około dwudziestu miejsc w testach poprawiono z wad, które wskazał audyt (wartości oczekiwane brane z kodu, który sprawdzają, prawdziwy zegar, własna konfiguracja gita użytkownika).

### Pod spodem

Zadanie napisało albo zmieniło czterdzieści kilka wpisów fundamentu (decyzje, niezmienniki, hasła słownika, fakty środowiska, po jednej linii mapy części dla nowych plików); bramka biegła raz na końcowym stanie i przeszła (1596 testów w 11 katalogach).

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Do poprawy albo przepuszczenia

1. Przegląd całości zmiany i przegląd kroku powrotu miały biec na najsilniejszym modelu, ale zapis przebiegu pokazuje je na tym samym modelu co reszta pracy, więc najsilniejsza klasa nie została zastosowana. Jeśli ten przegląd coś przeoczył, ktoś pracujący z nowymi wytycznymi trafi na to w późniejszym zadaniu. Ponowny przegląd na silniejszym modelu kosztuje sesję około czterdziestu minut i jeszcze jedną rundę przeglądu; cofnięcie nic nie kosztuje. Zadanie na to kosztuje późniejszą sesję; cofnięcie nic. Przepuszczenie nic dziś nie kosztuje, a przeoczona wada kosztuje później poprawkę. Rekomenduję przepuścić, bo ten przegląd znalazł cztery blokujące problemy, wszystkie naprawione, a sprawdzenie poprawki nie znalazło nowych. Słaby punkt: przegląd tej samej klasy może mieć te same ślepe punkty co przeglądana praca. Powtórzyć na silniejszym modelu, zrobić z tego zadanie czy przepuścić?
2. Znaleziono i nie naprawiono kilka drobiazgów, z których żadnego użytkownik procesu nie spotka często: czas z literą Z w miejscu separatora jest teraz przyjmowany przez skrypt mierzący cykle; linia sesji Claude Code, która jest poprawnym JSON-em, ale nie obiektem, jest pomijana, a ta sama linia w sesji Codexa zatrzymuje przebieg błędem; trzy decyzje zachowują przykłady powtarzające to, co już trzyma test; jedna decyzja mówi, że czas podaje się „jak robi to opcja”, a testy podmieniają zegar; żaden test nie porównuje listy skilli instalatora z listą zapisaną w jego teście; nowy skrypt kopiujący jedyny skrypt, który może nadpisać wskazany plik raportu, odziedziczy to (Drobne uwagi, 1–7). Poprawa teraz kosztuje rundę przeglądu; cofnięcie nic. Jedno zadanie na nie kosztuje późniejszą sesję, a zostawienie nic dziś nie kosztuje; pojawią się jako uwaga recenzenta, gdy ktoś zmieni te skrypty. Rekomenduję przepuścić, bo każdy jest rzadki albo dotyczy tylko brzmienia. Słaby punkt: to siedem osobnych uwag i nic ich nie zbiera po scaleniu. Poprawić w tym requeście, zrobić jedno zadanie czy przepuścić?

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

3. Zadanie mówiło o dziesięciu częściach the way z Pythonem; w chwili pracy było ich jedenaście, bo test odwołań wytycznych dodano po napisaniu zadania. Linter, test rozmiaru i oba pliki wytycznych obejmują wszystkie jedenaście. Jedno zdanie o tym, gdzie leży złożoność tej jedenastej części, którego zadanie nie rozstrzygało, mówi „w obliczeniach” — to moja propozycja, która decyduje tylko o tym, gdzie kiedyś mógłby działać narzędzie testów mutacyjnych. Druga droga to zostawić ten plik nieczytany przez obie kontrole.
4. Trzy hasła dla rodzajów testów nazywają się „files test”, „git test” i „repository test”, a nie gołe „files”, „git” i „repository”, jak napisało zadanie, bo gołe „git” i „repository” zamieniłyby każde użycie tych zwykłych słów w fundamencie w możliwe drugie znaczenie. Powrót do starych nazw to mała zmiana.
5. Reguła, że skrypt zmieniający repozytorium nic nie zmienia bez polecenia, ma teraz wyjątek na plik raportu, który człowiek wskazuje opcją: jeden skrypt otwiera ten plik do zapisu, zanim sprawdzi, czy kazano mu działać, więc człowiek, który wskaże plik śledzony, go traci. Przegląd całości znalazł, że reguła mówi „nigdy”, a skrypt to robi; zawęziłem regułę (i decyzję, która ją powtarza), zamiast oznaczać ją jako naruszoną albo zmieniać skrypt, czego zadanie nie żądało. Oznaczenie jako naruszona oznaczałoby oczekiwaną porażkę dla przypadku, na który nikt nie trafia przypadkiem.
6. Dwie reguły stoją jako znane naruszenia, z testami oznaczonymi jako oczekiwane porażki: reguły zatrzymujące lintera (zostaje 25 miejsc, 17 miejsc z audytu poprawiono) i limit rozmiaru (zadanie liczyło 2 pliki skryptów ponad 1000 linii, trzeci urósł od tamtej pory). Bramka zostaje zielona; przed ponownym złamaniem chroni je przegląd każdej późniejszej zmiany posprzątanych plików (Wpisy fundamentu).
7. Test sprawdzający fundament the way w bramce trzyma teraz tylko znaleziska dwóch niezmienników (odwołania do części i cytowanie testów), bo padał w klonie, którego główna gałąź nazywa się inaczej. Zwykły błąd fundamentu, jak numer niewskazujący żadnej decyzji, nie zaczerwieni więc bramki; krok cyklu dalej uruchamia całą kontrolę. Tego chciało zadanie, a README to mówi.
8. Niektóre zdania nowych decyzji wychodzą poza wiersz zadania, żeby agent idący za nimi miał to, czego potrzebuje: reguła, że część zyskująca kod Pythona wchodzi do zakresu dwóch decyzji; reguła, że nowa zależność inna niż linter kończy odstępstwo od audytu zależności; droga powrotna do formatera; opis poziomu end-to-end; reguła każdego rodzaju zapisana obok jego wzorca. Inne drobne wybory stoją w tabeli pytań rekordu: wytyczne pomijają wiersze szablonu o testach własności, atrapach cudzych usług i smoke testach, bo żaden poziom testów the way ich nie ma; dwa rodzaje bez niczego, co sprawdza test, nie mają reguły; regułę skryptu uruchamiającego polecenie testuje się na jednym skrypcie, bo uruchamiacz bramki nie owija jednego polecenia; odpowiedź zadania, że testy mutuje w głowie recenzent, idzie za decyzją, którą cytuje i która mówi, że autor (Zmiany techniczne; Wpisy fundamentu).

## Koszt

Około pięciu godzin czasu pracy w 95 etapach (dwie z nich to czekanie na narzędzia), 263 miliony tokenów (212 milionów na Sonnet 5.5, 51 milionów na Haiku 5.5), siedem przeglądów plastrów (jeden z nich poprawki), dwa przeglądy całości zmiany (jeden jej poprawki, po tym jak pierwszy recenzent został przypadkiem zatrzymany) i jeden przegląd kroku powrotu, dwie poprawki po nieudanym przeglądzie (plaster 4 i cała zmiana), jedno pełne uruchomienie bramki (332 sekundy). Tabela etapów jest w zatwierdzonym rekordzie: the committed record, linked by its commit in the next edit of this description/stages.md.

## Jak scalić

Scal tak, by commity zostały (pull requesty tego repozytorium scala się jako „Merge pull request”), bo link do rekordu przeżywa tylko wtedy.

</details>

## Technical changes

The change is 41 commits (the foundation entries first, then one slice after another, the fix of the whole-change review and the return step), 38 files, +3083 −259 lines.

- Foundation entries (`foundations/decisions.md`, `invariants.md`, `glossary.md`, `environment_facts.md`): the new section of the decision log, the changed and withdrawn decisions and the new invariants, listed under *Foundation entries*.
- Linter (`ruff.toml`, `requirements-quality.in`, `requirements-quality.txt`, `README.md`, `.github/workflows/tests.yml`, `foundations/part_map.md`): the pinned linter with a `select` of 389 rules, the sums of 17 wheels, the installation steps, and a CI step that installs it.
- Guidelines (`guidelines/coding.md`, six `guidelines/coding-<kind>.md`, `guidelines/testing.md`) and two pointer lines in `AGENTS.md`; the part map lists `guidelines/**` under `agent-instructions`.
- Tests of the new invariants: `agent-instructions/test_linter_invariant.py` and `test_size_invariant.py` (each an expected failure plus an ordinary test that fails if the tool cannot run or the counting is wrong), the rules of kinds in the test files of the generators, the repository changers, `task-cycle/gate_times.py` and `relation-model/fingerprint.py`, and the citation of an invariant above six existing tests of a refusal at the boundary.
- Fixes named by the audit: the expected values written out in the tests of the readiness check, the installer and the foundation check (causes 1, 2, 5, 23); a missing token count or identifier in a Codex session ends `task-cycle/cycle_stages.py` with exit code 2 (cause 3); fixed clocks and event waits in the tests of the gate and of `gate_times.py` (cause 4); a repository built in a temporary directory and git without the user's configuration in the audit tests (causes 6, 7); a missing field of a skill ends `skill_entry_points.py` with exit code 2 (cause 17); the lint places of four files (causes 26, 27, 30, 33).
- The fix of the review of the whole change (7 commits, `be9b44d..f0482d0`) and the return step (`3cf54a5`): two tests that read a file the import check could not work out, a race in the order test of the gate, wording of two invariants, the narrowing of the repository changers' rule, and twelve Minor findings.

## Checks

- Gate: `python -B task-cycle/gate_times.py --output … -- python -B gate/run_tests.py` on `3cf54a5` (Windows, after the day advisor's start signal): exit 0, 1596 tests in 11 directories, every directory passed, 332 s. The run on the base was not made: the base is a merge commit whose tree equals that of the merged branch, so the list of tests failing before the change was taken from the final gate of that cycle, commit `8636f9e`, `docs/task-cycles/decisions-log-after-foundation-review`: one failure there, `gate/test_run_tests.py` `DirectoriesAtOnce.test_by_default_every_directory_runs_at_the_same_time` (a flaky test that failed on its base too).
- The flaky test of the gate (`DirectoriesAtOnce`, two tests of that class): in this cycle the final gate passed it; focused runs failed it about 5 times in 40 at the base and at the head alike. It lies outside the task, and the task that fixes it already exists: the task about small corrections after pull requests 93 and 117–121 (its item on the random failure of the gate's test).
- Own-work checks: each slice's report names its failing run before and passing run after, with command and exit code; the reviews reran their checks. The foundation check without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line. Ruff (`--ignore-noqa`, ten parts plus the eleventh): 43 reports at the base, 25 at the head, none new.
- Not run on this machine: the POSIX path of the installation steps and of the CI step, and the real signal test of `gate_times.py` (skipped on Windows); CI runs them on Linux: the run on the request is waited for after the record is committed and its result is written here.
- Forms: form check of this description: run before publishing, see the record; check of private paths on the description and on the record's copy: run before publishing, see the record; image check: run on the copy of the record before it is committed; remarks check: run on the original (2 runs, last exit 0, 0 listed).
- Working copies left: none. Directories of earlier tasks kept (the script of the start left them): `agent-path-to-running-product` (branch `task/agent-path-to-running-product`, no merge git can see on the target branch), `base-check-stage-remarks` (detached, its branch `task/stage-remarks` not found), `base-fix-minor-findings` (detached, its branch `task/minor-findings` not found).

## Foundation entries

The new topical section of the decision log: "The-way's own coding and testing guidelines" — what the-way adopts of the templates of the coding and the testing discipline for its own code and tests, where it departs from them, the kinds of its code and the levels of its tests, and the exemplar of each. Rows 16 and 17 of the task's settlements (the two rules of the whole of the code) went to the guidelines, not to an entry. Violated marks set: `ruff-blocking-rules` and `function-and-file-size` (both `Violated: yes`, their tests expected failures); no mark cleared; the sentence of `script-subprocesses` changed and the tests of the invariants that cite each other were checked (`0 errors`, no `listed:` line). No entry is marked `the cycle's` as a whole; the sentences that go beyond a row are item 8 above. WAY-328 is withdrawn (successors WAY-379 and WAY-392); WAY-09, WAY-38, WAY-344 and WAY-363 changed as the rows say, and WAY-389 was narrowed together with its invariant (item 5).

- WAY-379 (decision), `row 1`: The-way adopts the template of the coding discipline for its own code in the parts that hold Python, and departs from it only by a decision that gives the reason.
- WAY-380 (decision), `row 3`: Ruff 0.17.1 checks the-way's code with the default set of that version, no preview, `py314`; 389 rules block, 18 stand among the examples, a comment cannot turn a rule off, and disabling a rule for the whole of the-way changes the decision.
- WAY-381 (decision), `row 4`: The version is pinned by `required-version` and by the requirements files with the SHA-256 of every wheel, Ruff stands in `.runs/quality-venv` installed as the README says, and CI gains only an installation step.
- WAY-382 (decision), `row 11`: The-way's code has no automatic formatter (`### Formatter` reads `none — WAY-382`); one enters later by a decision and one reformatting of the whole code.
- WAY-383 (decision), `row 12`: The-way departs from the audit of dependencies because its code imports nothing outside the standard library and its one declared dependency is the linter in the pinned version.
- WAY-384 (decision), `row 13`: The-way departs from all six rules on failures and logs because its scripts write no logs and report a failure by an exit code and a line `Error:`.
- WAY-385 (decision), `row 14`: A function of a script has at most 80 lines with its nested functions, a script file at most 1000; tests outside, no exceptions, counted by an `ast` test apart from the linter.
- WAY-386 (decision), `row 18`: `task-cycle/tracked_private_paths_check.py` is the exemplar of the kind `check`; no rule of the kind that a test checks.
- WAY-387 (decision), `row 18`: `task-cycle/cycle_measures.py` is the exemplar of the kind `measuring-report`; no rule that a test checks.
- WAY-388 (decision), `row 18`: `agent-instructions/skill_entry_points.py` is the exemplar of the kind `generator`; without `--write` a generator changes no file.
- WAY-389 (decision), `row 18`: `task-cycle/remove_merged_worktrees.py` is the exemplar of the kind `repository-changer`; without `--apply` or where the confirmation is declined nothing changes.
- WAY-390 (decision), `row 18`: `task-cycle/gate_times.py` is the exemplar of the kind `command-runner`; a script that wraps one command ends with that command's exit code unchanged.
- WAY-391 (decision), `row 18`: `relation-model/fingerprint.py` is the exemplar of the kind `shared-module`; importing a file of the kind runs nothing.
- WAY-392 (decision), `row 2`: The-way adopts the template of the testing discipline for its own tests, departs from the field *Time limit* and from mutation testing, and takes `### AI in tests` with no tool decision.
- WAY-393 (decision), `row 20`: The-way's tests stand at five levels: unit, files test, git test, repository test, e2e.
- WAY-394 (decision), `row 25`: A test takes its expected value from the-way's foundation, glossary, the templates and skills the script carries out, or the description at the head of the script.
- WAY-395 (decision), `row 26`: The fields *Purpose*, *Files*, *Doubles*, *Data*, *Time and randomness*, *Exemplar* and *Command* of a recipe bind; *Time limit* reads `none — WAY-395`.
- WAY-396 (decision), `row 27`: `relation-model/test_fingerprint.py::Fingerprint.test_a_tab_is_kept` is the exemplar of the level unit.
- WAY-397 (decision), `row 27`: `task-cycle/test_cycle_measures.py::RewriteEdgesTest.test_a_rewrite_of_2000_tokens_is_not_counted` is the exemplar of the files test.
- WAY-398 (decision), `row 27`: `project-level/test_plan_state_invariant.py::PlanStateEvidence.test_fresh_remote_record_composes_both_transitions` is the exemplar of the git test.
- WAY-399 (decision), `row 27`: `elements/common/test_elements_pending_marker.py::TrackedFilesUnderElementsTest.test_no_tracked_file_under_elements_holds_the_pending_marker` is the exemplar of the repository test.
- WAY-400 (decision), `row 27`: `process-audit/test_audit_count.py::Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` is the exemplar of the e2e level, once git runs there without the user's configuration.
- WAY-401 (decision), `row 28`: The-way does not test automatically what an agent does when it follows a skill; it returns to it when an error of an agent's behaviour repeats that the audit does not catch before the merge.
- WAY-402 (decision), `row 29`: The-way adopts no mutation tool (the author mutates in their head); a tool returns when a missing assertion lets an error through after the merge in a part whose complexity lies in computation.
- WAY-09 (change of a decision), `row 31`: The repository also holds the directory `guidelines/` with the-way's own guidelines, which the map gives to `agent-instructions`.
- WAY-328 (withdrawal of a decision), `row 32`: WAY-328 is withdrawn (the list of withdrawn numbers holds it, successors WAY-379 · WAY-392).
- WAY-344 (change of a decision), `row 33`: The sentence of its *Rationale* and the item of its *Rejected* that named WAY-328 speak of the state after the guidelines of the-way.
- WAY-363 (change of a decision), `row 34`: The example in its *Verification* names a script of a product with no coding guidelines.
- WAY-38 (change of a decision), `row 9`: A second paragraph: a test of a standing check runs the tool the check pins from the environment the repository declares (and a sentence of the *Rationale*).
- `script-subprocesses` (change of an invariant), `row 10`: The sentence allows, in a test of a standing check, the pinned tool of that check run from the environment the repository declares.
- `ruff-blocking-rules` (invariant), `row 6`: No file of the parts of WAY-379 breaks a blocking rule of WAY-380 under the pinned Ruff with `--ignore-noqa`; `Violated: yes`; rests on `ruff-default-rules`.
- `function-and-file-size` (invariant), `row 15`: No function and no script file of those parts is longer than WAY-385 allows; `Violated: yes`.
- `generator-writes-only-with-write` (invariant), `row 19`: Without `--write` the two generators change no file of their repository.
- `repository-changer-acts-only-when-told` (invariant), `row 19`: Without `--apply`, or with the confirmation declined, the three repository changers change no tracked file and no working directory.
- `command-runner-passes-exit-code` (invariant), `row 19`: `task-cycle/gate_times.py` ends with the exit code of its command unchanged, 128 plus the signal where a signal kills it.
- `shared-module-import-runs-nothing` (invariant), `row 19`: Importing `relation-model/fingerprint.py` in a new process with closed input ends with 0 and writes and reads nothing.
- `readiness-check-refuses-non-utf-8` (invariant), `row 30`: The readiness check refuses a file that is not UTF-8 with exit 2 and a message.
- `cycle-stages-refuses-crafted-names` (invariant), `row 30`: Crafted names neither split a row of the stages report nor enter its column of files.
- `cycle-measures-refuses-nested-line` (invariant), `row 30`: A line nested too deeply ends the script with exit 2, a line `Error:` naming file and line, and no result.
- `gate-times-refuses-impossible-entry` (invariant), `row 30`: A registry entry with an impossible time is deleted and counts as no run.
- `audit-count-refuses-record-links` (invariant), `row 30`: The count of the audit follows no symbolic link that leaves the record and gives the values as unknown.
- `check-instructions-refuses-outside-links` (invariant), `row 30`: A file link out of the repository is neither read nor listed, and is reported as not read.
- `files test` (glossary term), `row 21`: A files test works on files in a temporary directory and the process of a Python interpreter, and uses no git.
- `git test` (glossary term), `row 22`: A git test works on git repositories it builds in a temporary directory.
- `repository test` (glossary term), `row 23`: A repository test works on the real checkout of the-way and checks a property of the repository itself.
- `ruff-default-rules` (environment fact), `row 7`: The default set of Ruff 0.17.1 holds the 407 rules that `DEFAULT_SELECTORS` names at the tag 0.17.1 (the 407 are written out in the sentence).
- `ruff-required-version` (environment fact), `row 8`: Ruff ends with an error where the version it runs does not meet the requirement `required-version` sets.

## Minor findings

Minor findings that no fix made, each with its place and the reviewer's words (the twelve Minor findings of the review of the whole change that lay within the task were fixed and passed the review of the fix):

1. Review of the fix of the whole change, `agent-instructions/test_linter_invariant.py:68-74` and `agent-instructions/test_size_invariant.py:76-84`: "the same coverage test and the same tuple `PARTS` stand twice, so a new part must be added in two files; the finding asked for 'each of the two tests or one shared helper', so this meets it, at the cost the fix report names."
2. Review of the fix of the whole change, `guidelines/coding-repository-changer.md`: "`elements/common/migrate_foundation.py` is `copy` while its `--report` can overwrite a tracked file the human names; the invariant now allows it, but a new script that copies it inherits that writing. It is what the narrowed invariant says; mention only."
3. Review of the return step, `foundations/decisions.md` (the pairs of examples of the decisions on the linter and on the four kinds of scripts): "Pairs of examples in WAY-380 and WAY-388 to WAY-391 repeat what an invariant holds. The template allows a pair only for the part no invariant and no test checks."
4. Review of the return step: "WAY-395 says tests give time 'as the option `--today` gives it'. `gate_times.py` has no such option, and its tests replace the clock function instead."
5. Review of slice 5, `task-cycle/cycle_measures.py` (the read of a time): "`2026-10-06Z09:00:00` is now read as a naive time (taken as UTC). It was refused before. The old code already accepted other separator characters such as `x`, and the task's Fix prescribes this expression"; and "`2026-10-06Z` (a date with a `Z` and no time) was read before and is now refused. It is also Minor. Neither form comes from a real session writer."
6. Fix of the whole-change review, `task-cycle/cycle_stages.py` (the reading of a Claude Code session): the fixer reports that a line which is JSON but no object is skipped there, while the Codex half now ends with exit code 2 and a message naming the rollout and the line; no reviewer judged the Claude Code half, which was not reworked.
7. Executor of slice 3, `installation/test_install.py`: no test compares the installer's list of skills with the list written out in the test, so a skill added to the installer passes silently; the executor recommended a small separate slice, which the plan does not hold.

No fix was reverted.

## Findings outside the task's scope

- The time with `Z` in the separator position (`task-cycle/cycle_measures.py`, the read of a time): the reviewer marked it outside the task; see item 5 of *Minor findings*; whether to make a task of it is part of item 2.
- The flaky test of the gate (`gate/test_run_tests.py`, `DirectoriesAtOnce`): marked outside the task by the review of the whole change, "failed in 2 of 4 runs of the `gate` directory at the head and 0 of 2 at the base"; it can turn a gate run red. It failed in no full run of this cycle. The task that fixes it already exists (see *Checks*); no new task is proposed.

## Course of the cycle

- **Task and sources:** one independent task, "the way: coding and testing guidelines of the-way itself (end of the transitional state)", ready for the cycle, approved 2026-11-15; sources: the foundation at `2d59321`, the task's 26 answers and 34 settlement rows, the audit's causes 1–34.
- **Process pin:** none — the-way itself; the cycle ran from its own checkout at `2d59321`.
- **Spec:** none; the task left no open design choice.
- **Route:** planned slices, since the change spans eleven parts and was more than one agent can hold.
- **Plan:** 23 slices and 40 foundation entries, the plan's size report fit every slice; slice 9 was made after slice 17, because its check needed the tests the slices 11–17 add. The record's `plan.md` holds it.
- **Choices:** 15 autonomous choices and rulings beside the task, in the questions table of the record: the committed record, linked by its commit in the next edit of this description/cycle.md.
- **Blocking findings left:** none. Two reviews failed — the review of slice 4 (the other fields of a Codex session) and the review of the whole change (four findings, including a red import check and a rule that a script broke) — and each one fix was reviewed and passed.
- **Record:** the committed record, linked by its commit in the next edit of this description
