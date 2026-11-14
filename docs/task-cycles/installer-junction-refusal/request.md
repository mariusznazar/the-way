**State: ready** — three items in "Fix or let through" ask for your answer; merging lets them through, and nothing else waits for you.

## What you will see

The command that installs the process in a product no longer writes or deletes through a Windows junction (a folder shortcut that the file system shows as an ordinary folder). Before, a product whose settings folder for agents was a junction to a folder elsewhere got the process files written into that other folder, and the command ended with success and no warning; a junction at the folder of an outdated skill entry would have made it delete a file outside the product. Now the command stops before writing anything, says the path is not a regular folder, and ends with a failure code, the same as for a symbolic link. A junction at the place where the process is attached to the product is refused too, and outdated entries behind a junction are left alone. Three new tests make a junction and show that nothing is written or deleted, in the product or where the junction leads; they run on Windows and are skipped elsewhere. The foundation gets a new rule that says all this, and one new environment fact that it stands on.

### Underneath

The installer's check of folders on the way to a file now asks Python's own junction test next to the symbolic link test, at every place that looks at a folder; the checks of single files stay as they were, since a junction is never a file.

## For you to decide

### Needed from you

none

### Fix or let through

1. One kind of junction still goes through: if the folder where git keeps the data of the attached process (inside the product's own git folder) is a junction, git itself writes the data to where the junction leads, and the installer ends with success. Who feels it: someone who keeps git's data outside the product on purpose, by a junction they made; git does not carry junctions to a clone, so only the owner of that one copy. The new rule no longer claims more than the installer's own code does, so nothing it says is false. Ways: do it in this request — add a check before git runs, a test and a changed rule; it costs a round of correction with a review, and it widens the task, which asked about the files the installer writes itself; make a task of it — the hole stays until someone does it; let it through — nothing today, and the rare case stays silent. I recommend letting it through, since the task itself called this kind of junction rare and the installer's own writes are covered. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)
2. A test of the command that runs every test failed once on a busy machine. The test checks that three trial directories run at the same time, and waits 120 seconds for them to meet; on the run that overlapped with another test run of this cycle they did not meet, and on the rerun with the machine idle it passed, as it did on the base and on the first run of this change's final code. The cause is not proven. Whoever runs the whole test command on a loaded machine may see it fail and have to rerun it. Ways: do it in this request — find the cause in a test the change does not touch; it costs a correction round with a review and is outside the task; make a task of it — someone measures it on a busy machine; let it through — nothing now, and a rerun may be needed again. I recommend making a task, since one failure with an unproven cause is too little to fix here and too much to forget. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 2)
3. The review of the whole change read 10 of the 22 decisions selected for the installer whole and went through the other 12 by their titles; besides, it named eight decisions about how an invariant is written as unread, and read the template that holds their rules instead. Who feels it: whoever later reads the new rule and trusts that every decision about its form was checked. Another reviewer reading those decisions costs a session and a review; letting it through costs nothing today, and the reviewer of the fix judged the rule against the same template. I recommend letting it through, since the template carries their rules and the fix review passed the entry. Have a fresh reviewer read them in this request, make a task of it, or let it through? (Course of the cycle, Choices)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

4. The new rule says the installer "with its own code" neither writes nor deletes through a link. The first wording said it for every path of the product, and the review found that git's own writes under the product's git folder break it; the cycle took the review's cheaper way and narrowed the wording, and did not add a check of the git folder, which would have widened the task. The rule still means what the task's row said: refuse before writing, and delete nothing through a symbolic link or a junction. Where the installer meets a link at an outdated entry it skips that entry and goes on, as it already did for a symbolic link, and refuses only on the way to a file it writes.
5. The cycle wrote one fact the task did not name: in Python 3.14 the call the installer uses, `Path.is_junction`, is true for a junction and only Windows has junctions. It is quoted from Python's documentation and the new rule rests on it; a first version quoted the neighbouring call and was corrected in the return step.
6. Changed tests that guard rules: the rule's three new tests and one more new test of the scans for outdated entries now carry its name, and two older tests of the installer, which check that nothing is deleted or written through a symbolic link, now carry it too, since the new rule covers symbolic links as well. No surface of the installer changed, and the new rule reads "violated: no".

## Cost

About 1 hour 12 minutes of working time, 23 minutes of it without waiting for tools; 33.1 million tokens, all on one model class (Sonnet 5.5), 32.1 million of them cached input and 0.18 million output. Review rounds: the whole change failed once and passed after its one fix; the return step and the fix of a failed test run each had one review and passed. The whole test command ran four times: on the base, twice on the final code with a failure each time that the cycle explains below, and once more with a pass. The table of stages is in the record linked under Course of the cycle.

## How to merge

Merge with a merge commit that keeps the commits; the link to the record of the cycle survives only then. The foundation has waited for a review through 39 merges since the last review (the tag foundation-review/2026-11-06; the reminder starts at 30). The review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>In your language</summary>

**Stan: ready** — trzy punkty w „Napraw albo przepuść” czekają na twoją odpowiedź; scalenie przepuszcza je, a nic innego na ciebie nie czeka.

## Co zobaczysz

Polecenie, które instaluje proces w produkcie, nie zapisuje już ani nie usuwa niczego przez junction Windows (skrót do folderu, który system plików pokazuje jak zwykły folder). Wcześniej produkt, w którym folder ustawień agentów był junction do folderu gdzie indziej, dostawał pliki procesu zapisane w tamtym folderze, a polecenie kończyło się sukcesem bez ostrzeżenia; junction w folderze przestarzałego wejścia skilla mogło sprawić, że polecenie usunie plik poza produktem. Teraz polecenie zatrzymuje się przed zapisem czegokolwiek, mówi że ścieżka nie jest zwykłym folderem i kończy się kodem błędu, tak samo jak przy dowiązaniu symbolicznym. Junction w miejscu, gdzie proces jest podpięty do produktu, też jest odrzucane, a przestarzałe wpisy za junction zostają nietknięte. Trzy nowe testy zakładają junction i pokazują, że nic nie jest zapisane ani usunięte, ani w produkcie, ani tam, dokąd junction prowadzi; na Windows działają, gdzie indziej są pomijane. Fundament dostaje nową regułę, która to mówi, i jeden nowy fakt środowiskowy, na którym stoi.

### Pod spodem

Sprawdzenie folderów na drodze do pliku pyta teraz obok dowiązania symbolicznego także o junction, własnym testem Pythona, w każdym miejscu, które patrzy na folder; sprawdzenia pojedynczych plików zostały, bo junction nigdy nie jest plikiem.

## Do rozstrzygnięcia

### Potrzebne od ciebie

none

### Napraw albo przepuść

1. Jeden rodzaj junction nadal przechodzi: jeśli folder, w którym git trzyma dane podpiętego procesu (w środku własnego folderu gita produktu), jest junction, sam git zapisuje dane tam, dokąd junction prowadzi, a instalator kończy się sukcesem. Odczuje to ten, kto celowo trzyma dane gita poza produktem przez junction, który sam założył; git nie przenosi junction do klonu, więc dotyczy to tylko właściciela tej jednej kopii. Nowa reguła nie twierdzi już więcej niż kod instalatora, więc nic, co mówi, nie jest fałszem. Drogi: zrobić to w tym żądaniu — dodać sprawdzenie przed uruchomieniem gita, test i zmienioną regułę; kosztuje turę poprawki z przeglądem i rozszerza zadanie, które pytało o pliki zapisywane przez sam instalator; zrobić z tego zadanie — dziura zostaje, dopóki ktoś tego nie zrobi; przepuścić — dziś nic, a rzadki przypadek zostaje ciche. Polecam przepuścić, bo samo zadanie nazwało ten rodzaj junction rzadkim, a własne zapisy instalatora są pokryte. Naprawić w tym żądaniu, zrobić zadanie czy przepuścić? (Findings outside the task's scope, 1)
2. Test polecenia, które uruchamia wszystkie testy, raz nie przeszedł na zajętej maszynie. Test sprawdza, że trzy próbne katalogi biegną w tym samym czasie, i czeka 120 sekund, aż się spotkają; w przebiegu nałożonym na inny przebieg testów tego cyklu nie spotkały się, a po powtórzeniu na wolnej maszynie test przeszedł, tak jak na bazie i w pierwszym przebiegu końcowego kodu tej zmiany. Przyczyna nie jest ustalona. Kto uruchamia całe polecenie na obciążonej maszynie, może zobaczyć błąd i musieć powtórzyć przebieg. Drogi: zrobić to w tym żądaniu — znaleźć przyczynę w teście, którego zmiana nie dotyka; kosztuje turę poprawki z przeglądem i jest poza zadaniem; zrobić z tego zadanie — ktoś zmierzy to na zajętej maszynie; przepuścić — dziś nic, a powtórzenie może znów być potrzebne. Polecam zrobić zadanie, bo jeden błąd o nieustalonej przyczynie to za mało, żeby naprawiać tutaj, i za dużo, żeby zapomnieć. Naprawić w tym żądaniu, zrobić zadanie czy przepuścić? (Findings outside the task's scope, 2)
3. Przegląd całej zmiany przeczytał w całości 10 z 22 decyzji wybranych dla instalatora, a pozostałe 12 przejrzał po tytułach; poza tym wskazał osiem decyzji o tym, jak pisze się niezmiennik, jako nieprzeczytane i przeczytał zamiast nich szablon, który niesie ich reguły. Odczuje to ten, kto później czyta nową regułę i ufa, że każdą decyzję o jej formie sprawdzono. Drugi recenzent czytający te decyzje kosztuje sesję i przegląd; przepuszczenie nic dziś nie kosztuje, a recenzent poprawki ocenił regułę wobec tego samego szablonu. Polecam przepuścić, bo szablon niesie ich reguły, a przegląd poprawki zaakceptował wpis. Czy świeży recenzent ma je przeczytać w tym żądaniu, zrobić zadanie czy przepuścić? (Course of the cycle, Choices)

### Akceptujesz przez scalenie

Scalenie akceptuje te punkty; jeśli któryś ci nie odpowiada, powiedz który.

4. Nowa reguła mówi, że instalator „własnym kodem” nie zapisuje ani nie usuwa niczego przez dowiązanie. Pierwsze brzmienie mówiło to o każdej ścieżce produktu, a przegląd znalazł, że zapisy samego gita w folderze gita produktu je łamią; cykl wziął tańszą drogę z przeglądu i zawęził brzmienie, a nie dodał sprawdzenia folderu gita, co rozszerzyłoby zadanie. Reguła nadal znaczy to, co wiersz zadania: odmowa przed zapisem i nic usuniętego przez dowiązanie symboliczne ani junction. Gdy instalator trafia na dowiązanie przy przestarzałym wpisie, pomija ten wpis i idzie dalej, jak już robił przy dowiązaniu symbolicznym, a odmawia tylko na drodze do pliku, który zapisuje.
5. Cykl zapisał jeden fakt, którego zadanie nie nazwało: w Pythonie 3.14 wywołanie, którego używa instalator, `Path.is_junction`, jest prawdziwe dla junction, a junction ma tylko Windows. Fakt jest zacytowany z dokumentacji Pythona, a nowa reguła na nim stoi; pierwsza wersja cytowała sąsiednie wywołanie i została poprawiona w kroku powrotnym.
6. Zmienione testy, które pilnują reguł: trzy nowe testy reguły i jeszcze jeden nowy test przeszukiwania przestarzałych wpisów noszą teraz jej nazwę, a dwa starsze testy instalatora, które sprawdzają, że nic nie jest usuwane ani zapisywane przez dowiązanie symboliczne, też ją noszą, bo nowa reguła obejmuje i dowiązania symboliczne. Żadna powierzchnia instalatora się nie zmieniła, a nowa reguła ma „naruszona: nie”.

## Koszt

Około 1 godziny 12 minut czasu pracy, z czego 23 minuty bez czekania na narzędzia; 33,1 mln tokenów, wszystkie na jednej klasie modelu (Sonnet 5.5), z tego 32,1 mln to wejście z pamięci podręcznej, a 0,18 mln wyjście. Tury przeglądu: cała zmiana nie przeszła raz i przeszła po jednej poprawce; krok powrotny i poprawka nieudanego przebiegu testów miały po jednym przeglądzie i przeszły. Całe polecenie testów biegło cztery razy: na bazie, dwa razy na końcowym kodzie z błędem w każdym, który cykl wyjaśnia niżej, i jeszcze raz z wynikiem pozytywnym. Tabela etapów jest w rekordzie podlinkowanym w sekcji Course of the cycle.

## Jak scalić

Scal z commitem scalającym, który zachowuje commity; link do rekordu cyklu przetrwa tylko wtedy. Fundament czeka na przegląd od 39 scaleń od ostatniego przeglądu (tag foundation-review/2026-11-06; przypomnienie zaczyna się od 30). Przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium; nic w tym żądaniu na niego nie czeka.

</details>

## Technical changes

The change makes the installer treat a Windows junction as it treats a symbolic link, then guards that with tests and a rule. By commit:

- `54ed53c` — `installation/install.py`: one helper, `is_link`, a symbolic link or a junction, used at each place that looks at a folder: the folders on the way to every file the installer writes (`check_parents`: foundation files, skill entry points, agent type definitions), the folder of the agent definitions, the `skills` folders and the folder of each skill entry in the scan for outdated entries, and the folder of the attached process in `plan`. The checks of single files (`read_text_file`, `owned_entry_point`, `owned_agent_definition`, the foundation file check, the `.gitmodules` check) stay `is_symlink`, since a junction is never a file. Three tests in `installation/test_install.py` (junction on the way to a written file, junction at the folder of an outdated entry, junction at the attached process) that make a junction with the standard library's `_winapi.CreateJunction`, as `instruction-files/test_check_instructions.py` does; a sentence in `installation/README.md`; the two older symbolic-link tests of `installation/test_agent_types_installation.py` cite the new rule.
- `474df77` — the new rule in `foundations/invariants.md`.
- `62ec7c1` — fix for the review's Minor findings: a new test that calls the two scans for outdated entries directly with a junction at their folders; the test found that the scan of skill entries never looked at the `.claude` and `.agents` folders themselves, and `install.py` now does (a run never reaches it, since the check on the way to a written file refuses earlier); README wording corrected.
- `ee6126c` — fix for the blocking finding: the rule narrowed to the installer's own code; the environment fact written in `foundations/environment_facts.md`.
- `e899494` — return step: the fact now quotes `Path.is_junction`, the call the installer makes.
- `a6ddd8c` — fix of the first failed run of the whole test command: the helper of the new tests assigned a second value to `self.product`, so the check of imports between parts could not read two older runs; the helper no longer assigns it and the module-level `make_writable` serves both.

## Checks

- The whole test command, `python -B task-cycle/gate_times.py --output .runs/task-cycles/installer-junction-refusal/gate_times.md -- python -B gate/run_tests.py`: on the base `6fa755c` exit 0, 1267 tests in 10 directories. On `e899494`: exit 1, 1271 tests, `elements/part-map` failed (`test_the_way_imports_only_from_allowed_parts`, the change's fault, fixed in `a6ddd8c`; `python -B gate/run_tests.py elements/part-map` on `a6ddd8c` exit 0, 39 tests). On `a6ddd8c`, run while the review of the fix ran tests on the same machine: exit 1, 1274 tests, `gate` failed (`test_by_default_every_directory_runs_at_the_same_time`); on `a6ddd8c`, machine idle: exit 0, 1271 tests in 10 directories, every directory passed. That test failed in 1 of the 4 cycle runs it ran in and passed in 3; its file is `gate/test_run_tests.py`, a part outside the task's parts, so it stands under the findings outside the scope.
- The new rule's tests seen failing once: `python -B -m unittest installation.test_install -k junction -k stale_entry` on the unchanged installer, exit 1, 18 failing subtests; after the fix, exit 0, 3 tests, none skipped on Windows (the task's acceptance criterion). The new scan test: failing on a mutation of the checks (4 failures) and on the one-line change reverted (1 failure), passing after (`python -B -m unittest installation.test_install -k scan_for_stale`). `python -B gate/run_tests.py installation`: exit 0, 60 tests, on `ee6126c`.
- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`, on the head after each commit.
- Own-work checks: the author's, the weakest requirement being that a junction is recognised at every folder level — a listing of every `is_symlink` before and after and one crafted case per place found one more place in the fix round and fixed it; the reviewers' own checks: mutations of two of the three sites each caught by its test, crafted junctions at ten places (a junction at the git data folder went through, which is finding 1 of the outside-scope list), the quotation of the new fact against the live page and its archived copy, `shutil.rmtree` of Python 3.14.3 removing a junction without following it.
- The form check, the check of private paths on this description, the process remarks check and the image check on the copy of the record: written and checked after this commit.

## Foundation entries

- `installation-paths-through-links` — row 1: the installer's own code neither writes nor deletes anything through a symbolic link or a Windows junction that stands in a path of a product, and refuses before writing where such a link stands on the path of a file it writes or is the attached process. Method test, rests on `python-junction-detection`, part `installation`, violated no.
- `python-junction-detection` — the cycle's: in Python 3.14, `Path.is_junction` returns true if the path points to a junction and false for any other type of file, and only Windows supports junctions (Python documentation, pathlib page, archived 2026-10-21).
- Invariant tests changed or added: the new rule is cited by `test_rejects_a_junction_on_the_path_of_a_file_it_writes_without_touching_the_target`, `test_deletes_nothing_through_a_junction_at_the_folder_of_a_stale_entry_point`, `test_rejects_a_junction_at_the_submodule_directory` and `test_the_scan_for_stale_files_does_not_enter_a_junction_at_their_directory` in `installation/test_install.py`, and now also by `test_a_symlink_in_the_way_stops_the_run_and_its_target_is_not_touched` and `test_a_symlink_named_like_an_own_definition_of_a_gone_type_is_not_deleted` in `installation/test_agent_types_installation.py`. Surfaces altered: none. *Violated* marks set or cleared: none (the new rule is written as `no`).

## Minor findings

1. Review of the whole change, finding 6 — `installation/test_install.py`: "`python -B task-cycle/change_file_sizes.py 6fa755c 474df77` (exit 0): `installation/install.py` 675 to 681 (+6), `installation/test_install.py` 713 to 807 (+94), `installation/test_agent_types_installation.py` 332 to 334, `installation/README.md` 250 to 257, `foundations/invariants.md` 356 to 366. The-way holds none of the product guidelines (WAY-328), so there is no threshold test to run; my numbers and the diff are the material. Nothing grew past a point I would name: `test_install.py` was already the largest file of its part and the three new tests and three helpers are the growth. `is_link` has five users and no dead code was added besides the three unprotected guards of finding 2. The names are true." No fix was asked or made.
2. Review of the fix, note A — `foundations/invariants.md:303`: "'with its own code' leaves the hole in place and says it in few words. A junction at `.git/modules` is still written through by git with exit 0; the sentence no longer promises otherwise, but a reader of the entry alone does not learn that git's writes under `.git` are outside it (the part map and README say nothing either). The human sees it in the author's report; a one-clause note in `installation/README.md` ('git's own writes under `.git` are not checked') would put it where an installer user reads. Out of the findings file; Minor; not required." The return step judged the README clause a new statement of a limitation and did not make it.
3. Review of the fix, note C — `reports/author-fix-report.md` (a report, not code): "Author report +41 versus the diff's +37." Nothing in the code to change.

## Findings outside the task's scope

1. Review of the whole change, finding 7, Minor, out of scope — place: `installation/install.py` (the call of `git submodule add`): "Same evidence as finding 1 (case B). Outside the task: the task's items are about paths of files the installer writes, `.the-way` and stale entries; a junction at `.git/modules` is made by someone who keeps git's data elsewhere. If the human wants the installer to refuse it, it is a new task. Grade: Minor, out of scope (and it becomes in scope only if finding 1 is fixed by adding the check rather than by narrowing the sentence)."
2. A check whose file belongs to a part outside the task's parts failed in a cycle run and passed again: `gate/test_run_tests.py`, `test_by_default_every_directory_runs_at_the_same_time` (part `gate`); failed in 1 of the 4 cycle runs it ran in, passed in 3; the rerun with the machine idle passed. No reviewer marked it; it comes from the cycle's own runs.

## Course of the cycle

- **Task and sources:** the task "the way: the installer refuses to write through a Windows junction in a product's agent settings folder", independent, from the author's task document, status ready for cycle, frozen as `task.md` in the record; sources: the review of an earlier request of the-way (the finding that started it) and the answers recorded in the task to questions 1 and 2.
- **Process pin:** the-way itself, base `6fa755c` of `foundations`; the gate on the base: exit 0, 1267 tests.
- **Spec:** none — the task settles the rule and the means.
- **Route:** one author without a plan: the change fits one agent; class `same` (a trust boundary and a foundation entry across two parts); a discarded attempt: none.
- **Plan:** none on this route.
- **Choices:** 6 other choices, in the questions table of the record.
- **Blocking findings left:** none; the one blocking finding of the review of the whole change (the rule broader than the code) was fixed and the fix passed its review.
- **Record:** pending, linked by the SHA of the commit that adds it.
