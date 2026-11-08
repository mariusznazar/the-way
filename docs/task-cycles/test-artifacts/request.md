**State: ready** — nothing blocks the merge; three items below wait for your answer.

## What you will see

When a task changes a screen, the screenshots that the author or the reviewer shows you now stand in the description of the pull request as pictures. They come from a place that the product itself settles, outside the product's repository. No image file goes into the product's history any more, not even in the copy of the cycle's record that a commit adds to the pull request. The process names no place: the rule comes from the-way, the place from the product. The screenshots are evidence for the moment you accept the change, so a product may clear its place after a long time; pictures in old pull requests then stop showing.

When a product has settled no place for screenshots, the agent still looks at the screen, but the description shows no picture. It says so among the points for you to decide, with the reason, and the cycle does not stop. Only screenshots reach the description: the agent describes motion in words, and logs and command results stay in the cycle's reports.

The agent's way to the running product, which a product's foundation settles, must now let two cycles in separate worktrees check at once without a shared browser, and the agent closes the browser it opened. When a project is defined, the step that settles technology looks at a fourth matter beside logs, interface and development data: where the screenshots lie and how the description shows them.

Before a copy of the cycle's record is committed, a new check lists every file in it that is an image. The cycle removes the file from the copy and runs the check again, and the copy goes into a commit only when the check lists nothing.

### Underneath

The change is rules in the foundation (four new decisions, four edited ones and two new invariants), a new check script with its test, and wording in the cycle's skill, the description template, the review and change skills and the documents of the technology step.

## For you to decide

1. The new check recognizes an image by the end of the file name only (png, jpg, jpeg, gif, webp, bmp, tif, tiff, ico, svg, avif, heic). It does not catch an image saved under another name or none, an image written into a text as base64, or an image inside an archive, and it lists a text file merely named like an image. The task does not say how to recognize an image. Recommendation: accept; a file signature would need facts from outside standards and one more source to keep, and the cases it adds are rare in a cycle's record. Accept, or make a task of recognizing by content? (Technical changes, 3)
2. The condition that two cycles check at once without a shared browser stands in the rules for the way to the running product. The step that settles technology is not told to test it, so a product could settle an interface option that shares one browser and the first cycle would show it. An earlier version of this change made the step keep such an option in the comparison with the lack said; the review found that this weakens your condition into a choice between consequences, and it was removed. Recommendation: leave it until a product meets it, then make a task of it. Leave it, or make a task of it now? (Foundation entries)
3. Three entries were written beyond the rows of the task, for consistency (the entries listed under "the cycle's" in the Foundation entries): the fourth matter now says what it asks of a product, so that the step can tell when the place is settled; and two counts in the rules for the technology step now read "four", with one word changed in a rejected option so that "a fourth matter" no longer reads as a missing one. None changes a meaning you accepted. Accept?

## Cost

About 42 minutes of working time by the table of stages (the wait for you is not counted). The models were Sonnet 5.5 for the orchestrator, the author and the review of the return step, and Opus 5.5 for the review of the whole change and the review of its fix. 32.4 million tokens in all, 30.9 million of them read from cache and 0.17 million written as output. Three code reviews ran. The first, of the whole change, returned three blocking findings, which one fix removed, together with four of its Minor findings; the review of that fix and the review of the return step passed. The table of stages is in the committed record, linked under **Course of the cycle**.

## How to merge

Merge with a merge commit that keeps the commits; the link to the record survives only then. The record is added and removed in two commits at the end of the branch, so the changed files show only the change.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — nic nie blokuje scalenia; trzy punkty poniżej czekają na Twoją odpowiedź.

### Co zobaczysz

Gdy zadanie zmienia ekran, zrzuty, które autor albo recenzent pokazuje Tobie, stoją teraz w opisie pull requesta jako obrazki. Pochodzą z miejsca, które ustala sam produkt, poza repozytorium produktu. Żaden plik obrazu nie trafia już do historii produktu, także w kopii zapisu cyklu, którą commit dodaje do pull requesta. Proces nie wskazuje miejsca: regułę daje the-way, miejsce — produkt. Zrzuty są dowodem na chwilę, w której akceptujesz zmianę, więc produkt może po długim czasie wyczyścić swoje miejsce; obrazki w starych pull requestach przestaną się wtedy wyświetlać.

Gdy produkt nie ustalił miejsca na zrzuty, agent nadal ogląda ekran, ale opis nie pokazuje obrazka. Mówi o tym wśród punktów do Twojej decyzji, z powodem, a cykl się nie zatrzymuje. Do opisu trafiają tylko zrzuty ekranu: ruch agent opisuje słowami, a logi i wyniki poleceń zostają w raportach cyklu.

Droga agenta do działającego produktu, którą ustala fundament produktu, musi teraz pozwalać dwóm cyklom w osobnych worktree sprawdzać naraz bez wspólnej przeglądarki, a agent zamyka przeglądarkę, którą otworzył. Przy definiowaniu projektu krok, który ustala technologię, patrzy na czwartą sprawę obok logów, interfejsu i danych deweloperskich: gdzie leżą zrzuty i jak opis je pokazuje.

Przed commitem kopii zapisu cyklu nowe sprawdzenie wypisuje każdy plik w niej, który jest obrazem. Cykl usuwa plik z kopii i uruchamia sprawdzenie jeszcze raz, a kopia trafia do commita dopiero, gdy sprawdzenie nic nie wypisze.

#### Pod spodem

Zmiana to reguły w fundamencie (cztery nowe decyzje, cztery poprawione i dwa nowe niezmienniki), nowy skrypt sprawdzający z testem oraz brzmienie w skillu cyklu, szablonie opisu, skillach przeglądu i zmiany oraz dokumentach kroku technologii.

### Do rozstrzygnięcia

1. Nowe sprawdzenie rozpoznaje obraz tylko po końcówce nazwy pliku (png, jpg, jpeg, gif, webp, bmp, tif, tiff, ico, svg, avif, heic). Nie wychwyci obrazu zapisanego pod inną nazwą albo bez rozszerzenia, obrazu wpisanego w tekst jako base64 ani obrazu w archiwum, a wypisze plik tekstowy, który tylko nazywa się jak obraz. Zadanie nie mówi, jak rozpoznać obraz. Rekomendacja: przyjąć; sygnatura pliku wymagałaby faktów ze standardów zewnętrznych i jednego źródła więcej do utrzymania, a przypadki, które by dołożyła, zdarzają się w zapisie cyklu rzadko. Przyjąć, czy zrobić zadanie o rozpoznawaniu po zawartości? (Technical changes, 3)
2. Warunek, że dwa cykle sprawdzają naraz bez wspólnej przeglądarki, stoi w regułach o drodze do działającego produktu. Krok ustalający technologię nie ma polecenia, żeby go sprawdzić, więc produkt mógłby ustalić opcję interfejsu ze wspólną przeglądarką i dopiero pierwszy cykl by to pokazał. Wcześniejsza wersja tej zmiany kazała krokowi zostawiać taką opcję w porównaniu z nazwanym brakiem; przegląd uznał, że to osłabia Twój warunek do wyboru między skutkami, i fragment usunięto. Rekomendacja: zostawić, dopóki produkt na to nie trafi, wtedy zrobić zadanie. Zostawić, czy zrobić zadanie teraz? (Foundation entries)
3. Trzy wpisy powstały poza wierszami zadania, dla spójności (wpisy oznaczone „the cycle's” w Foundation entries): czwarta sprawa mówi teraz, czego wymaga od produktu, żeby krok umiał poznać, że miejsce jest ustalone; dwie liczby w regułach kroku technologii brzmią teraz „cztery”, a w jednej odrzuconej opcji zmieniono jedno słowo, żeby „czwarta sprawa” nie czytała się jak brakująca. Żaden nie zmienia znaczenia, które przyjąłeś. Przyjąć?

### Koszt

Około 42 minut pracy według tabeli etapów (czekanie na Ciebie nie jest liczone). Modele: Sonnet 5.5 dla orkiestratora, autora i przeglądu kroku powrotnego, Opus 5.5 dla przeglądu całej zmiany i przeglądu jej poprawki. Łącznie 32,4 mln tokenów, z czego 30,9 mln odczytanych z pamięci podręcznej i 0,17 mln wyniku. Przeszły trzy przeglądy kodu. Pierwszy, całej zmiany, zwrócił trzy uwagi blokujące, które usunęła jedna poprawka razem z czterema uwagami Minor; przegląd poprawki i przegląd kroku powrotnego przeszły. Tabela etapów jest w zatwierdzonym zapisie przebiegu, z odnośnikiem w „Course of the cycle”.

### Jak scalić

Scal commitem scalającym, który zachowuje commity; odnośnik do zapisu przeżywa tylko wtedy. Zapis jest dodany i usunięty dwoma commitami na końcu brancha, więc zmienione pliki pokazują tylko zmianę.

</details>

## Technical changes

The change is four commits and a record pair. Each paragraph says what a reader sees; the places follow.

1. Commit `dd84fba`, the foundation: new decisions WAY-316 to WAY-319 and the invariant `record-copy-image-check` (`foundations/decisions.md`, `foundations/invariants.md`); WAY-121 edited in place from three matters to four; the glossary line for the way to the running product was widened here and reverted in the fix (see 4).
2. Commit `d0d3ce6`, the skills and the script: step 5 of "The record before it is committed" in `task-cycle/skill/SKILL.md` runs the new check; *What you will see*, item 13 of *For you to decide* and *Checks* in `task-cycle/skill/request_template.md`; the screenshot rules in `task-cycle/change/ui_check.md`, `task-cycle/record_template.md` and `task-cycle/review/SKILL.md`; the fourth matter in `project-level/definition_template.md` and `project-level/technology/{list,research,running_product,start,task_run}.md`.
3. The check script is `task-cycle/image_files_check.py` with `task-cycle/test_image_files_check.py` (13 tests): a script of its own, not an extension of the private-paths check, because that one is bound to paths and note links and counts an image as a binary file; it recognizes an image by the end of the file name only, never opens a file, takes a directory or one file, and exits 0 (nothing listed), 1 (listed) or 2 (wrong argument).
4. Commit `ef0195e`, the fix for the review of the whole change: the glossary change reverted (so the term keeps one meaning and the case of no place for screenshots stays apart from the case of no way to the running product); sentence 2 of WAY-319 and its sentence in `project-level/technology/research.md` removed; the invariant `record-copy-image-files` added; the four Minor findings fixed (the list of matters in WAY-267, long lines, the wording of a rejected option of WAY-316, the reviewer's screenshot in `task-cycle/review/SKILL.md`).
5. Commit `25dd4ba`, the return step: a docstring of `task-cycle/image_files_check.py` now says that the private-paths check skips a file with a NUL byte near its start, not every image (an SVG is text).
6. Not done, on purpose: no change in a product repository (the place for screenshots in the first product is a task of that product); the task about a method of testing in the running product keeps its scope.

## Checks

- The gate, `python -B gate/run_tests.py`, run by the orchestrator on the final tree (`25dd4ba`): exit 0, 817 tests in 9 directories, every directory passed. The same command on `ef0195e`, the tree the review of the fix passed: exit 0, 817 tests. On the base `f218b55`, before the change: exit 0, 804 tests. No check failed on the base, and nothing failed or did not run in the gate.
- The invariant `record-copy-image-check` was seen failing before the script and passing after: `python -B -m unittest discover -s task-cycle -p "test_image_files_check.py"` exit 1 against a stub, then exit 0 with 13 tests; `python -B gate/run_tests.py task-cycle`: exit 0, 200 tests. The invariant `record-copy-image-files` is read by review (no test).
- Own-work check of the author: a run of the script on a throwaway record with a real photo under an upper-case extension listed it and exited 1, the same record without it exited 0, a missing directory exited 2; a grep for "three matters" and the lists of the three matters found the places that were corrected, and a later grep after the fix found no list of three left.
- Focused checks of the author and the reviewers, each exit 0: `python -B elements/common/foundation_check.py` (0 errors), `python -B gate/run_tests.py` for `task-cycle` (200), `project-level` (271), `elements/common` (109) and `agent-instructions` (18), and `python -B agent-instructions/skill_entry_points.py` (entry points current).
- No user-interface state or screenshot applies: the change alters no screen.
- The part of each changed file: `decisions`, `invariants`, `project-level` and `task-cycle` — the parts the task names; no file belongs to a part outside them.
- Form check, `python -B task-cycle/request_check.py docs/task-cycles/test-artifacts/request.md --task docs/task-cycles/test-artifacts/task.md`: run after every edit of this description (last run and exit code written when the description is published).
- Check of private paths, `python -B task-cycle/private_paths_check.py`, image check, `python -B task-cycle/image_files_check.py`, and process remarks check, `python -B task-cycle/remarks_check.py`: last runs on the copy of the record and on the original written when the record is committed.

## Foundation entries

Entries written whole from the accepted rows of the task (marked `row <n>`):

- WAY-316 (`row 1`, `row 2`, new): screenshots that the author or the reviewer shows the human stand in the description as images from a place the product's foundation settles outside the product's repository, never in the repository's history, the record's copy included; they are evidence for the moment of acceptance and the product may clear the place later.
- WAY-317 (`row 3`, new): where the foundation settles no place for screenshots, the author inspects the screenshot, the description shows none and says so, with the reason, among the human's decisions, and the cycle does not stop; a case different from WAY-219.
- WAY-318 (`row 5`, new): of the artifacts of a change's check only screenshots reach the description; motion is described in words and text traces stay in the reports.
- WAY-319 (`row 6`, new): the way to the running product that a product's foundation settles for its interface lets two cycles in separate worktrees check at once without a shared browser, and the agent closes the browser it opened.
- WAY-121 (`row 4`, edited): the step that settles technology looks at four matters of an agent's way to the running product — logs, interface, development data and the place of the screenshots.
- `record-copy-image-check` (`row 7`, new invariant, method test): the script that checks a record's copy lists each file whose name ends in an image extension of its list and exits 1 when it lists any, 0 when none.
- `record-copy-image-files` (`row 7`, new invariant, method review): no commit of a change adds a file below `docs/task-cycles/` whose name ends in an image extension of the check's list.

Entries the human did not see at the task document (marked `the cycle's`, for item 3 of *For you to decide*):

- WAY-165 (`the cycle's`, edited): the place of the screenshots, as the fourth matter, asks where the screenshot files lie outside the product's repository and how the description shows each as an image.
- WAY-267 and WAY-270 (`the cycle's`, wording): a count ("three" to "four") and the list of matters in a *violates* example are kept consistent with four matters; in WAY-270's *Rejected* "a fourth matter" now reads "a further matter".

No kept row tied to an entry already stated. The invariant test of `record-copy-image-check` is new; no surface and no *Violated* mark changed.

## Minor findings

The three notes of the review of the fix (`PASS ef0195e`), in the reviewer's words; none blocks, none was fixed. The Minor findings of the review of the whole change were all fixed.

1. `foundations/glossary.md:9` against `foundations/decisions.md` WAY-121: with the definition back to "the means through which an agent checks", WAY-121 counts the place of the screenshots among "four matters of an agent's way to the running product", though a place for evidence shown to the human is not quite a means of checking; WAY-270's *Rejected* uses exactly this fit ("the family's definition stops fitting, since the matter does not speak of an agent checking behaviour") to keep the failure notice out. No sentence the files hold is read wrongly for it, since the place is where the screenshots of the agent's check lie. The author names the cost in the fix report.
2. `foundations/invariants.md:330`: because of "Where {merge-onto} exists", `record-copy-image-files` binds nothing in the-way until it has a main branch (the same holds for `return-step-record`), and for a product's repository the rule stands in WAY-316's "file of a screenshot" and in step 5 of `task-cycle/skill/SKILL.md` ("checked for image files, which no copy holds"). Step 5 still runs on every copy, so no image passes unchecked in practice.
3. `task-cycle/review/SKILL.md:89-90`: "where the foundation settles none, keep none" does not say, as `ui_check.md` does for the author, that the reviewer's report states that no place is settled, so the request can tell the human (WAY-317). Today no reviewer step requires a screenshot.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task: screenshots of a changed screen reach the description spoiled by no file in the product's history; sources — the frozen task document of the record and the-way's `foundations` at `f218b55`.
- **Process pin:** not applicable — the-way itself, the base `f218b55`; the gate on it: exit 0, 804 tests.
- **Spec:** none written; the task leaves no open design choice, its nine questions settle the shape and rows 1–7 are accepted; the form of the check script was the author's to make.
- **Route:** one author without a plan, class `same`: a change that is mostly text across four parts plus one small script; the review of the whole change (`FAIL`, three Important findings), one fix, the review of the fix (`PASS`), the return step (one docstring) and its review (`PASS`).
- **Plan:** none.
- **Choices:** 6 other choices of the cycle (Q3–Q8 of the questions table), see the questions table of the committed record.
- **Blocking findings left:** none.
- **Record:** the commit that adds the record is written here when it exists.
