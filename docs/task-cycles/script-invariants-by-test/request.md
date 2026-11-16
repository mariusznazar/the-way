**State: draft** — the code is finished and reviewed; the request waits only for the CI run on its last head, and nothing below waits for your answer.

## What you will see

Four rules of the process repository were checked until now only by an agent reading each change: the repository declares Python 3.14, every script is a Python file, no script imports anything outside Python's standard library or the repository's own files, and every element directory holds its template, its examples (or a pointer to them) and its skill. From now on each of the four is checked by a test that every change passes through the one command that runs all tests, so a script in another language, an import from outside the standard library or a directory missing its skill turns the run red instead of relying on a reviewer's memory. The four rules now say in their entries that a test checks them.

Three decisions you made at refinement are in the tests as you settled them. A file is taken for a possible script unless its kind is on a list of kinds known to be no script; a kind that is no script is added to the list with a reason. On an interpreter other than 3.14 the import test fails and says which two versions it found. The import test sees imports in the same reach as the existing test of imports between parts, and an import whose name cannot be worked out is reported.

### Underneath

The tests are new files in two existing places, and two sentences of the repository's part map were corrected to say what now stands there; no script and no skill changed.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. The list of file kinds that are no script holds four kinds besides the five you named, because the repository already tracks files of those kinds: the CI workflow file (accepted only under the workflows directory, so another file with the same ending is reported), the linter's configuration, and the two files that list the linter's packages. I did not find any of the four to be a script; where you do, the list is one line to change in the test.
2. The test of the Python version, of the language of scripts and of the imports stands with the other tests of the rules of the repository's own code, not beside the existing test of imports between parts, and the test of the element directories stands with the shared checks of the foundation. I chose these places because the part map lets each of them import what it needs and the decisions about the scripts already name the first place. Each can be moved with no change to what is checked.
3. The element-directories test is skipped, with the reason printed, on a copy of the repository that has no main branch, because the rule is written for a repository where one exists; it runs in CI, where the branch is set. Four small tests check that the condition is not stuck at "false".
4. Two sentences of the part map were corrected by the return step: it now names the tests of the language, version and imports of scripts under the agent-instructions part, and the element-directories test under the common checks part. Without them the map would not say where these tests stand.
5. The task cited a decision that has since been withdrawn (the guidelines of the repository's own code and tests now exist), so the tests follow those guidelines.

Changed invariant tests, in plain words: the four tests are new and cite their rules; no existing test changed or was weakened, and none of the four rules changed its sentence. A test that was wrong by the review's judgment was fixed in this request: it no longer compares against the wording of its own code's messages.

## Cost

About 36 minutes of active stages in about 33 million tokens: the author on Sonnet (three turns: the change, the fix of four Minor findings, the return step), three reviews on Opus (whole change, the fix, the return step) and the orchestrator on Sonnet. Two review rounds ran after the first review, none of them blocking. The table of stages is in the committed record, linked below.

## How to merge

Merge with a merge commit, not squash or rebase, so that the link to the cycle's record, which names a commit, stays reachable. Nothing in this request waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: wersja robocza** — kod jest gotowy i sprawdzony; żądanie czeka tylko na przebieg CI na ostatnim commicie, a nic poniżej nie czeka na Twoją odpowiedź.

## Co zobaczysz

Cztery reguły repozytorium procesu sprawdzał do tej pory tylko agent czytający każdą zmianę: repozytorium deklaruje Pythona 3.14, każdy skrypt jest plikiem Pythona, żaden skrypt nie importuje niczego spoza biblioteki standardowej Pythona ani plików samego repozytorium, a każdy katalog elementu ma szablon, przykłady (albo odesłanie do nich) i skill. Od teraz każdą z tych reguł sprawdza test, przez który przechodzi każda zmiana w jednej komendzie uruchamiającej wszystkie testy, więc skrypt w innym języku, import spoza biblioteki standardowej albo katalog bez skilla zaczerwienia przebieg, zamiast liczyć na pamięć recenzenta. Wpisy czterech reguł mówią teraz, że sprawdza je test.

Trzy decyzje, które podjąłeś przy doprecyzowaniu, są w testach tak, jak je ustaliłeś. Plik uchodzi za możliwy skrypt, jeśli jego rodzaj nie stoi na liście rodzajów, o których wiadomo, że nie są skryptem; nowy rodzaj, który nie jest skryptem, dopisuje się do listy z powodem. Na interpreterze innym niż 3.14 test importów pada i podaje obie wersje. Test importów widzi importy w tym samym zasięgu co istniejący test importów między częściami, a import, którego nazwy nie da się wyliczyć, zgłasza.

### Pod spodem

Testy to nowe pliki w dwóch istniejących miejscach, a dwa zdania mapy części repozytorium poprawiono tak, by mówiły, co tam teraz stoi; żaden skrypt ani skill się nie zmienił.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Popraw albo przepuść

brak

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

1. Lista rodzajów plików, które nie są skryptem, ma cztery rodzaje oprócz pięciu, które wskazałeś, bo repozytorium już śledzi pliki takich rodzajów: plik workflow CI (przyjmowany tylko w katalogu workflows, więc inny plik z tym samym rozszerzeniem jest zgłaszany), konfigurację lintera i dwa pliki z listą pakietów lintera. Żadnego z czterech nie uznałem za skrypt; jeśli uważasz inaczej, to jedna linia do zmiany w teście.
2. Test wersji Pythona, języka skryptów i importów stoi razem z innymi testami reguł własnego kodu repozytorium, a nie obok istniejącego testu importów między częściami, a test katalogów elementów — ze wspólnymi sprawdzeniami fundamentu. Wybrałem te miejsca, bo mapa części pozwala każdemu z nich importować to, czego potrzebuje, a decyzje o skryptach już nazywają pierwsze z nich. Każdy da się przenieść bez zmiany tego, co jest sprawdzane.
3. Test katalogów elementów jest pomijany, z podanym powodem, w kopii repozytorium bez gałęzi głównej, bo reguła jest napisana dla repozytorium, w którym ona istnieje; w CI, gdzie gałąź jest ustawiona, test działa. Cztery małe testy sprawdzają, że warunek nie tkwi na „fałsz”.
4. Krok zwrotny poprawił dwa zdania mapy części: nazywa teraz testy języka, wersji i importów skryptów przy części agent-instructions, a test katalogów elementów przy części wspólnych sprawdzeń. Bez nich mapa nie mówiłaby, gdzie te testy stoją.
5. Zadanie powoływało się na decyzję, która została już wycofana (wytyczne własnego kodu i testów repozytorium już istnieją), więc testy idą za tymi wytycznymi.

Zmienione testy niezmienników, prostymi słowami: cztery testy są nowe i powołują się na swoje reguły; żaden istniejący test się nie zmienił ani nie osłabł, a żadna z czterech reguł nie zmieniła swojego zdania. Test, który recenzent ocenił jako błędny, poprawiono w tym żądaniu: nie porównuje już z brzmieniem komunikatów własnego kodu.

## Koszt

Około 36 minut aktywnych etapów, około 33 mln tokenów: autor na Sonnecie (trzy tury: zmiana, poprawka czterech drobnych uwag, krok zwrotny), trzy przeglądy na Opusie (cała zmiana, poprawka, krok zwrotny) oraz orkiestrator na Sonnecie. Po pierwszym przeglądzie odbyły się dwie rundy, żadna nie blokująca. Tabela etapów jest w zatwierdzonym zapisie, podlinkowanym niżej.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase, żeby link do zapisu cyklu, który wskazuje commit, pozostał osiągalny. Nic w tym żądaniu nie czeka na przegląd fundamentu.

</details>

## Technical changes

- `4bc1667c` — the change: tests of the four invariants and `Method: test` in the four entries of `foundations/invariants.md` (nothing else of them changed). `python-version-declared`: `.python-version` is tracked, holds one line, and the line is `3.14` or `3.14.<patch>`. `script-language`: every tracked file is `.py`, `.md`, or of a listed kind that is no script, else reported. `script-imports`: reuses `imports` of `elements/part-map/test_cross_part_imports.py` (the same reach as `cross-part-imports`), runs only on the declared interpreter and fails naming both versions otherwise. `element-directory-contents`: for each directory under `elements/` but `common`, a template, `examples.md` or a pointer, and `skill/SKILL.md`.
- `540aed04` — the fix of the four Minor findings of the review of the whole change: the kind `.yml` is accepted only under `.github/workflows/`; no expected value comes from the wording of the code's own messages and each test value names its source; the file of the three script tests moved from `elements/part-map/` to `agent-instructions/test_script_invariants.py`; a missing `.python-version` is refused with a message that names it.
- `3043e760` — the return step: two sentences of `foundations/part_map.md` (`agent-instructions`, `elements-common`).
- New tests, by name: `agent-instructions/test_script_invariants.py` — `PythonVersionDeclared.test_the_repository_declares_python_3_14_in_python_version`, `ScriptLanguage.test_every_file_git_tracks_is_a_python_file_or_of_a_kind_that_is_no_script`, `ScriptImports.test_no_python_file_git_tracks_imports_a_module_outside_the_standard_library` (the three that cite the invariants) and ten unit tests of their functions; `elements/common/test_element_directory_contents.py` — `ElementDirectoryContents.test_every_element_directory_holds_a_template_examples_or_a_pointer_and_a_skill` (cites `element-directory-contents`) and twelve unit tests.

## Checks

- Final gate: the CI run on this request's last head; its result is added here when the run ends (pending when this description was first written).
- The list of failing checks before the change, taken from the merged request https://github.com/mariusznazar/the-way/pull/145, since the base `604907c8` is a merge commit with the tree of its second parent and no gate ran on it: none (every check of that request's one CI run passed).
- Focused checks by the author, reviewers and orchestrator (each with the command and exit 0): `python -B gate/run_tests.py elements/part-map` (40 tests), `agent-instructions` (50 tests, 2 expected failures of the invariants marked violated), `elements/common` (270 tests); `python -B elements/common/foundation_check.py` without `--skip-test-citations` on the finished change: exit 0, `0 errors`, no `listed:` line; Ruff 0.17.1 with `--ignore-noqa` on the two new files: exit 0.
- Each of the four tests was seen failing once and passing after, by the author and again by a reviewer in a working copy: `.python-version` as `3.13`; a tracked `build_tool.sh`; a tracked file with `import yaml`, an `import_module` of an environment variable and an `exec` of an import, and a run on Python 3.12 (a message naming both versions); an element directory without its skill and one whose template has no pointer. After the fix the reviewer repeated the break of the narrowed `.yml` kind (a root file `tools_deploy.yml` is reported), of Python 3.12 and of a missing `.python-version`.
- Own-work check (WAY-164): the author named as most likely missed the reach of `script-imports` equal to that of `cross-part-imports`, and checked it with a tracked file holding `importlib.import_module("yaml")` and `importlib.import_module(os.environ["M"])`: both reported. No walk through a running product was made: the change adds tests and four words of the foundation and alters nothing a user sees.
- The full gate was not run on the cycle's own system: CI runs on this request and is the final gate (WAY-160). No wait for a start signal was needed.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, 19 merges, `reminder: no`. `python -B task-cycle/private_paths_check.py`, `request_check.py`, the image check and the remarks check on the description and the copy of the record: results added with the record's link.
- No working copy of an agent stays; the author's outputs of focused runs stand in the ignored directory of the task's worktree. No directory of an earlier task stays.

## Foundation entries

- `python-version-declared`, `script-language`, `script-imports`, `element-directory-contents` (invariants): each now reads `Method: test`; no sentence changed. Carried by item 5 of the task's *To do*, not a row of *Settlements to record*. Each is cited by a test of this change by a line `invariant: <identifier>` (WAY-03).
- Part map, `agent-instructions` and `elements-common` (`the cycle's`, written by the return step): the first now says the part answers for the tests of the rules every script keeps — its language, the Python version it runs on and the modules it imports; the second says it answers for the test that every element directory holds its template, its examples or a pointer, and its skill.
- Rows 1–3 of *Settlements to record* went to the code of the tests (lists `SUFFIXES`, `NAMES` and `PLACES` with a reason at each kind; `wrong_interpreter`; `outside_imports` over `imports` of the cross-part test), so no entry was written for them.
- No decision, glossary term, environment fact or topical section was written. The task named a decision that the log lists as withdrawn; WAY-379 and WAY-392 stand in its place.

## Minor findings

Minor findings of the review of the return step, within the task, not fixed (WAY-161):

1. `foundations/part_map.md:166-168` — "the colon makes the three tests the whole list of 'the rules every script of the-way keeps'. […] The same part holds the tests of two more rules of the-way's own scripts: `agent-instructions/test_linter_invariant.py` […] and `agent-instructions/test_size_invariant.py`. The new sentence leaves them unnamed, and the sentence before this change did not name them either. […] A reader who asks which part answers for the linter's or the size test does not find it named here." The reviewer offers two fixes: "the tests of three rules every script of the-way keeps: …", or a sentence naming the tests of the rules of the-way's own code with these three as examples.
2. `foundations/part_map.md:166-168` with WAY-44 — "the test of a `repository` invariant now stands, by the map, in `agent-instructions`, and the tension with 'Tests belong to the part they test' is neither resolved nor raised. […] `repository` cannot hold a test either way. […] There is a precedent: `ruff-blocking-rules`, whose *Part* includes `repository`, is tested in `agent-instructions` too. Consequence today: none for any verdict or any selection of decisions." The cheapest form, the reviewer says, is one clause in the questions table or in WAY-44.

The one new Minor finding of the review of the fix (the docstring of `agent-instructions/test_script_invariants.py` said the map's description of `agent-instructions` covers tests of the-way's own code rules) is answered by the return step's sentence; the reviewer of the return step names it as asked for. The four Minor findings of the review of the whole change were fixed (`540aed04`).

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task: tests for four invariants held until now by review; its three settlements (the list of kinds, the refusal on another interpreter, the reach of the import test) were accepted on 2026-11-14. The task states the base of an earlier commit; on this base two things differed, a decision it names is withdrawn and git tracks four more kinds of file than it lists (both in the questions table, Q1 and Q2).
- **Process pin:** not applicable; this is the process repository itself, base `604907c8`.
- **Spec:** none: the task leaves no open design choice.
- **Route:** one author without a plan, class `same` (Sonnet), because the import test reuses the reader of a 1188-line test and each of the four tests had to be seen failing. Reviews on Opus.
- **Plan:** none.
- **Choices:** 3 recorded in the questions table (Q1 withdrawn decision, Q2 four more kinds, Q3 partial reads carried to the reviewer) and 6 of the author (the condition of the element test, the form of a pointer, which directories are elements, the form of `.python-version`, the comparison of versions, the source of expected values) — see the record.
- **Blocking findings left:** none.
- **Record:** pending the commit that adds it.
