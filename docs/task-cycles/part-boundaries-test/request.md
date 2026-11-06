**State: draft** — the change is reviewed and every test passes; four items wait for your yes.

## What you will see

The part map already says, for each part, which other parts it may depend on, but nothing checked that the code keeps to it: only the agent of the return step could notice an import across a boundary, and in loop2 one went unnoticed through many merges. This change makes keeping to those allowed dependencies a duty of every product, carried by one invariant with a test, and gives the-way its own such test as the example.

1. **A new rule for products.** Every product whose parts import code from other parts has one invariant with a test in its own suite: a file imports only from its own part, from the parts its part may depend on, from a part of test helpers when the importing file is a test, and from a part that an accepted dependency, written as an invariant "part X does not depend on Y" marked violated, says X depends on today. A product sets it up in the change that brings a second part holding code into its map; a product that already has such parts does it in a task of its own (for loop2, the separate loop2 task). Each accepted dependency stays its own whole entry, accepted by a human, not a list of known violations, and the shared test keeps guarding every other boundary.
2. **A part for shared test helpers.** Files that serve the tests of several parts form a part of their own, which its sentence describes as such, with no new field in the map. The tests of every part may import from it; code that is not a test may not. The part-map template now says this, and an approved decision on how files belong to parts was extended for it, as you agreed when the task was refined.
3. **the-way checks itself.** A new test reads the part map and every Python file's imports, those through a directory added to Python's search path included, and fails on an import the map does not allow. On today's tree it passes: the one import across parts, from the project-level scripts to the fingerprint script, is allowed. Tests on small repositories made for them show it failing on a forbidden import, seeing an import through the search path, and letting each of the two exceptions pass. The invariant's entry is now one of the examples of how an invariant is written.

This task writes code and a test in the-way, which has no coding or testing guidelines of its own yet; you decided at refinement that it does not wait for them.

### Underneath

One new decision, one decision extended in place, one new invariant, the part-map template and one example line, and a new test directory of 13 tests; the full test run passes on the final tree.

## For you to decide

1. **Running another part's script does not count as an import.** The task left this question to the cycle. The cycle read the new invariant as covering only import statements, those through Python's search path included, and not one file running another as a script or as a new process; today two files do that, each within its own part, so either answer gives the same result now. If you want such runs counted, the invariant's sentence and the test need widening. Accept the narrower reading?
2. **The part map's sentence for the part that holds the map's rules now also names the new test.** The cycle wrote this because the test lives in that part; you did not see it at the task document. Accept? (Foundation entries, 4)
3. **A new invariant test is added.** The test of the new invariant is a new file in a new test directory; no existing invariant test, surface or violated mark changes. Accept? (Foundation entries, 3)
4. **The test can still miss some ways of importing.** The reviewer found that an import the test cannot match to any file is ignored without a word, so an import that only works because another file put a directory on the search path passes unseen; and seven forms of import the test claims to handle have no test of their own, so breaking the test's handling of any of them leaves every test green. Nothing on today's tree uses them, but the test is meant to be the guard that tells you when a boundary breaks, and products will copy it. Make a task of it? (Minor findings, 1 and 2)

## Cost

About 48 minutes of working time. The orchestrator and all agents ran on one model, Claude Opus 5.5, using 29.1 M tokens, of which 27.9 M were input read from cache and 0.17 M output. Review rounds: the whole change was reviewed and failed on one finding, the author fixed it once, and the same reviewer passed the fix. The return step made no commit, so it needed no review. The table of stages is in the cycle's record, linked under *Record* below.

## How to merge

Use a merge commit, not squash or rebase: the link to the cycle's record points to a commit on this branch, and it survives only when the commits are kept.

<details>
<summary>W Twoim języku</summary>

**Stan: szkic** — zmiana przeszła przegląd i wszystkie testy; cztery sprawy czekają na Twoje „tak”.

**Co zobaczysz**

Mapa części mówi już przy każdej części, od których innych części wolno jej zależeć, ale nic nie sprawdzało, czy kod się tego trzyma: import zza granicy mógł zauważyć tylko agent kroku zwrotnego, a w loop2 jeden taki przeszedł niezauważony przez wiele scaleń. Ta zmiana czyni pilnowanie dozwolonych zależności obowiązkiem każdego produktu, niesionym przez jeden niezmiennik z testem, i daje the way własny taki test jako przykład.

1. **Nowa reguła dla produktów.** Każdy produkt, którego części importują kod z innych części, ma jeden niezmiennik z testem we własnym zestawie testów: plik importuje tylko z własnej części, z części, od których jego części wolno zależeć, z części pomocników testów, gdy sam jest testem, i z części, od której — według zaakceptowanej zależności zapisanej jako niezmiennik „część X nie zależy od Y” oznaczony jako naruszony — X dziś zależy. Produkt zakłada go w zmianie, która wprowadza do mapy drugą część z kodem; produkt, który już ma takie części, robi to osobnym zadaniem (dla loop2 — osobne zadanie loop2). Każda zaakceptowana zależność zostaje osobnym, pełnym wpisem, który zaakceptował człowiek, a nie listą znanych naruszeń, a wspólny test pilnuje dalej wszystkich pozostałych granic.
2. **Część na wspólne pomocniki testów.** Pliki, które obsługują testy kilku części, tworzą osobną część, którą tak opisuje jej zdanie, bez nowego pola w mapie. Testy każdej części mogą z niej importować; kod, który nie jest testem — nie. Mówi to teraz szablon mapy części, a zatwierdzona decyzja o tym, do której części należy plik, została o to uzupełniona, na co zgodziłeś się przy doprecyzowaniu zadania.
3. **the way sprawdza sam siebie.** Nowy test czyta mapę części i importy każdego pliku Pythona, także te przez katalog dopisany do ścieżki wyszukiwania Pythona, i nie przechodzi na imporcie, którego mapa nie dopuszcza. Na dzisiejszym drzewie przechodzi: jedyny import między częściami, ze skryptów poziomu projektu do skryptu odcisku tekstu, jest dozwolony. Testy na małych, specjalnie przygotowanych repozytoriach pokazują, że nie przechodzi na zakazanym imporcie, widzi import przez ścieżkę wyszukiwania i przepuszcza każdy z dwóch wyjątków. Wpis tego niezmiennika jest teraz jednym z przykładów, jak pisać niezmiennik.

To zadanie pisze kod i test w the way, które nie ma jeszcze własnych wytycznych kodowania ani testów; przy doprecyzowaniu zdecydowałeś, że na nie nie czeka.

*Pod spodem:* jedna nowa decyzja, jedna decyzja uzupełniona w miejscu, jeden nowy niezmiennik, szablon mapy części i jedna linia przykładu oraz nowy katalog testów z 13 testami; pełny przebieg testów przechodzi na ostatecznym drzewie.

**Do Twojej decyzji**

1. **Uruchomienie skryptu innej części nie liczy się jako import.** Zadanie zostawiło to pytanie cyklowi. Cykl odczytał nowy niezmiennik jako obejmujący tylko instrukcje importu, także przez ścieżkę wyszukiwania Pythona, a nie uruchomienie przez jeden plik drugiego jako skryptu albo nowego procesu; dziś robią to dwa pliki, każdy w obrębie własnej części, więc obie odpowiedzi dają dziś ten sam wynik. Jeśli chcesz, żeby takie uruchomienia się liczyły, trzeba poszerzyć zdanie niezmiennika i test. Przyjmujesz węższy odczyt?
2. **Zdanie mapy części dla części, która trzyma reguły mapy, wymienia teraz także nowy test.** Cykl dopisał to, bo test leży w tej części; nie widziałeś tego w dokumencie zadania. Przyjmujesz? (Wpisy fundamentu, 4)
3. **Dochodzi nowy test niezmiennika.** Test nowego niezmiennika to nowy plik w nowym katalogu testów; żaden istniejący test niezmiennika, żadna powierzchnia ani żadne oznaczenie naruszenia się nie zmienia. Przyjmujesz? (Wpisy fundamentu, 3)
4. **Test może jeszcze przegapić niektóre sposoby importu.** Recenzent znalazł, że import, którego test nie umie dopasować do żadnego pliku, jest pomijany bez słowa, więc import, który działa tylko dlatego, że inny plik dopisał katalog do ścieżki wyszukiwania, przechodzi niezauważony; a siedem form importu, które test deklaruje, nie ma własnego testu, więc zepsucie obsługi którejkolwiek z nich zostawia wszystkie testy zielone. Na dzisiejszym drzewie nic ich nie używa, ale test ma być strażnikiem, który mówi, że granica pękła, a produkty będą go kopiować. Robimy z tego zadanie? (Drobne uwagi, 1 i 2)

**Koszt**

Około 48 minut pracy. Prowadzący cykl i wszyscy agenci pracowali na jednym modelu, Claude Opus 5.5, i zużyli 29,1 mln tokenów, z tego 27,9 mln to wejście czytane z pamięci podręcznej, a 0,17 mln to wyjście. Rundy przeglądu: cała zmiana przejrzana i odrzucona z jedną uwagą, autor poprawił ją raz, a ten sam recenzent przepuścił poprawkę. Krok zwrotny nie zrobił żadnego commitu, więc nie wymagał przeglądu. Tabela etapów jest w zapisie cyklu, do którego link stoi niżej w sekcji *Record*.

**Jak scalić**

Commitem scalającym, nie przez squash ani rebase: link do zapisu cyklu wskazuje commit na tej gałęzi i przetrwa tylko wtedy, gdy commity zostaną zachowane.

</details>

## Technical changes

1. **The decision log.** `e7947e8`: WAY-299 written at the end of the log (new, row 1 of the task): the duty of one invariant of allowed dependencies with its test, when it is set up, its two exceptions, and why a marked "does not depend on" invariant is no list of known violations; its *Rejected* carries the ways the task did not choose (a general script of the-way, leaving it to the return step, a recommendation of the template, no change, one invariant per part, WAY-51 alone). WAY-44 extended in place (row 2): the files serving the tests of several parts are a part of their own; its *Verification* now names `cross-part-imports` and gains one complies and one violates example; its *Rationale* and its *Rejected* item "tests as a part of their own" say why a helper part is consistent with tests belonging to what they test.
2. **The invariant and its test.** `e7947e8`: `cross-part-imports` in `foundations/invariants.md` (*Method* test, *Rests on* `git-path-patterns`, *Derives from* WAY-299 · WAY-44, *Part* every, *Violated* no); `elements/part-map/test_cross_part_imports.py`, a new test directory: it assigns tracked files to parts by `git check-attr`, reads imports with `ast` (so imports inside string literals are not counted), evaluates directories added to `sys.path` (`insert`, `append`, `extend`, assignment, `+=`; `os.path` calls, `Path` and `/`, `__file__`, names bound once, `os.getcwd()` as the root), fails on an addition it cannot evaluate and on a Python file no part or two parts claim, and lets pass a test's import of a part named in `TEST_HELPER_PARTS` (empty in the-way) and an import X → Y that a marked "The part `X` does not depend on `Y`." invariant covers. One test runs on the-way's tree and cites the invariant; twelve run on repositories made in a temporary directory. `fbea390`, the fix: the invariant's sentence gives the direction of the marked exception (X the importing part, Y the imported one), and a fixture shows a marked invariant of the other direction lets nothing pass.
3. **The part-map template and the examples.** `b4a5509`: `elements/part-map/template.md` — "Allowed dependencies" states the duty and its two exceptions, when the invariant is set up, that the product's task settles how a test file is recognised, and names `cross-part-imports` as the-way's own; the paragraph on an accepted dependency stays and points to it; "Assigning files" gains the bullet on a part of test helpers; the fields table names the test as a reader of *Files* and *Depends on*. `e7947e8`: `elements/invariants/examples.md` gains the example line; `foundations/part_map.md` — the sentence of `part-map` names the test.
4. **The return step changed nothing.** It compared the entries written, the task's *Decisions in play*, the entries the search found and the map entries of the touched parts with the code at `fbea390`, found nothing that no longer matched and made no commit.

## Checks

1. **The full test run passed on the base and on the final tree.** `python -B gate/run_tests.py`: on the base `dfd50e5`, exit 0, 717 tests in 8 directories; on `b4a5509`, exit 0, 729 tests in 9 directories; on the reviewed final tree `fbea390`, exit 0, 730 tests in 9 directories. `foundations` had not moved (`git fetch`, `origin/foundations` = `dfd50e5`), so no merge and no further run were needed. No check failed or did not run.
2. **The author's own-work check showed that the test sees imports through `sys.path` on the real tree, rather than passing because it sees nothing.** A listing of every edge the checker resolves on the-way: 38 Python files, 20 edges, two across parts, both allowed (`project-level/readiness_check.py:46` → `relation-model/fingerprint.py` through `os.path.join(HERE, "..", "relation-model")`; the test → `elements/common/foundation_check.py`), no problems. With `relation-model` removed from `project-level`'s *Depends on*, `python -B gate/run_tests.py elements/part-map` exited 1; restored, exit 0. Five mutations of the checker (search directories dropped, either exception removed, problems discarded, string constants not evaluated) each exited 1; after the fix, accepting either direction exited 1. The author also checked the *Rejected* of WAY-299 and the additions to WAY-44 item by item against the task's *Not chosen*.
3. **The focused runs of the author and the reviewer all exited 0.** `python -B elements/common/foundation_check.py` (`0 errors`), and `python -B gate/run_tests.py` for `elements/part-map` (13 tests), `elements/common` (109), `agent-instructions` (18), `gate` (20), `project-level` (268) and `relation-model` (12).
4. **No user interface changed:** no states or screenshots apply.
5. **The form of this description was checked by the script.** `python -B task-cycle/request_check.py .runs/task-cycles/part-boundaries-test/request.md --task .runs/task-cycles/part-boundaries-test/task.md`: its runs before the request opened are named in the record; the run after the record's link was added is named below.
6. **The remarks check listed items until they were entered.** `python -B task-cycle/remarks_check.py .runs/task-cycles/part-boundaries-test`: 2 runs; run 1 exited 1 listing 17 items of five reports; run 2 exited 0, listing nothing. The cycle holds no listing wrong.

## Foundation entries

Each entry this request writes or changes, with one English sentence of its meaning. No surface and no *Violated* mark changes. No kept row was tied to an entry already stated.

1. **WAY-299 (new), row 1.** Every product whose parts import code from other parts holds one invariant with a test, under which a file imports only its own part, the parts its *Depends on* names, a part of test helpers when it is a test, and a part that a marked "X does not depend on Y" invariant says X depends on; it is set up when a second such part enters the map, or by a task of its own in a product that already has them, and each such marked invariant is a whole entry a human accepted, not a list of known violations.
2. **WAY-44 (changed in place), row 2.** The files that serve the tests of several parts form a part of their own, described by its sentence with no new field, from which the tests of every part may import and code that is not a test may not.
3. **`cross-part-imports` (new), row 3, with a new invariant test.** No Python file git tracks imports, by an import statement and through `sys.path` as well, a file of another part that its own part's *Depends on* does not name, unless a test imports a part of test helpers or a marked invariant "the part X does not depend on Y" covers the import from X to Y. Its test is the new file `elements/part-map/test_cross_part_imports.py`.
4. **The sentence of the part `part-map` (changed), `the cycle's`.** The part that answers for the part map now also answers for the test that holds the-way's imports to the dependencies the map allows (see *For you to decide*, 2).

## Minor findings

1. **An import the test cannot match to a file is ignored in silence.** Reviewer of the whole change, `dfd50e5..b4a5509`, finding M1, `elements/part-map/test_cross_part_imports.py:216-225` (`resolve`) and the docstring at :7-8: "a name that resolves to no file the check can see is dropped in silence, so an import that reaches another part through a directory another file put on `sys.path` passes unseen. … on today's tree every import resolves to the standard library or to a file the check sees … Cheap fix that matches the test's own principle ("a check that quietly sees less would pass", docstring :10-11): report as a problem an absolute import whose first name is neither in `sys.stdlib_module_names` nor resolved."
2. **Seven forms the test claims to handle have no fixture.** Reviewer of the whole change, finding M2, `elements/part-map/test_cross_part_imports.py:174-175` (`extend`), :183-184 (`sys.path = […]`, `+=`), :238-242 (relative imports), :219 (`__init__.py`), :227-229 (dotted prefixes), :213 (own directory), :98-104 (a marked sentence wrapped over lines): "several branches the author's report and docstring claim have no fixture, and mutating them leaves the whole file green. … the test on the-way's tree uses none of these forms, so the fixtures are the only evidence the checker sees them … A fixture per claimed form would close it."
3. **A Python file left out of the map on purpose would fail the test.** Reviewer of the whole change, finding M3, `elements/part-map/test_cross_part_imports.py:81-87` (`parts`), against `elements/common/foundation_check.py:530` and `:556-559`: "a Python file the map lists under "Files left out on purpose" fails the test, though WAY-44 and `foundation_check` allow it. … the copy of the pattern extraction (the author's concern 1) already diverges … Loud, not silent, and no such file exists today — hence Minor."
4. **Two lines of prose are wrapped untidily.** Reviewer of the whole change, finding M4: "`elements/part-map/template.md:97` is 122 characters, where the surrounding paragraph wraps at 100 (the other lines over 100 in the file are table rows). `foundations/decisions.md:1083` — the re-wrap of WAY-44 leaves the short line "another. For a file that" before the old line continues."

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** "the way: produkt pilnuje dozwolonych zależności między częściami niezmiennikiem z testem", an independent task, from `zadanie_the_way_test_granic_czesci.md` in the author's notes, `Status: ready for cycle`, answers of 2026-11-06; its citations stand at `foundations` `3177e10`, all found unchanged at the base `dfd50e5`. It departs from WAY-215 (no coding or testing guidelines of the-way yet) by Mariusz's decision under its *Questions to settle*.
- **Process pin:** none; the-way working on itself, the process root this worktree.
- **Spec:** none. The rows of *Settlements to record* settle the decision, the change to WAY-44 and the invariant's sentence, *To do* 3 what its test reads; the one question carried to the cycle was answered from them (*For you to decide*, 1).
- **Route:** one author without a plan, class `same` (Opus 5.5): the change spans three parts, writes a new decision whose *Rejected* must match the task's *Not chosen*, edits an approved decision in place, and adds a static reader of imports whose silent misses would let the invariant pass while saying nothing.
- **Plan:** none.
- **Choices:** eight other choices (Q2–Q9) in the questions table of the record's `cycle.md`; Q1 stands above as item 1 of *For you to decide*, Q10 as item 2.
- **Blocking findings left:** none.
- **Record:** the cycle's record is added to this branch by a commit made after the request opens, and its link by that commit's SHA is written here at once.
