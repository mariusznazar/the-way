**State: ready** — items 1 and 2 wait for your answer; items 3, 4 and 5 you only accept by merging.

## What you will see

When an agent writes a decision that derives from another decision the product's foundation does not hold yet — typically one designed in an approved project definition that no code makes true — it can now say so in the decision's relations line, in the same way an invariant already can: `TODO — <the decision, and where it is expected>`, as the last item after the relations that are known. Before, the agent could only write `none`, which is false, or leave a bare `TODO`, which the check rejected, or add partial entries for you to accept; where the code made no part of the planned decision true, the request stood blocked.

The foundation check accepts that described form. It reports as errors a bare `TODO` in the relations line, a `TODO` written right after a relation word (`derives from TODO`), and a `TODO` joined to other relations with a comma instead of ` · `. A `TODO` in the line for the entry's origin stays an error. The rule for how a planned entry enters the foundation now also says that the change that writes the entry replaces each such `TODO` that points at it with a reference to it. The request template lists the new place among the leftovers a request puts before you.

### Underneath

The check script reads the relations line the way it already reads the lines of the other fields that may hold a described `TODO`, and still checks every decision number that stands before it; the rules, the decision template and the request template say the same as the script.

## For you to decide

### Needed from you

none

### Fix or let through

1. The rule that says which leftover markers a request shows you names three places where a described `TODO` may stand; the process now has a fourth, the relations line of a decision. Nothing contradicts today: the request template lists all four, and this request was written from it. The one who feels it is whoever later compares a request with that rule and finds no case for the fourth place, so a `TODO` there may go unremarked. Fixing it in this request means adding one short clause in three places of an approved decision, which changes the wording of a decision you approved, so it needs your yes; it costs a round of correction with its review, and undoing it costs another edit. Making a task of it leaves the two lists disagreeing until that task is done and costs nothing now; undoing it, nothing. Letting it through leaves the same state with no task to end it. I recommend making a task of it, since the task document fixed that decision as unchanged and the request template already covers the fourth place. Its weak point: until the task is done, the two lists disagree and a reviewer may follow the shorter one. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)

2. The review of the whole change read the index of its selection whole (33 decisions listed in full and 123 by heading), opened 6 of the decisions listed in full and read the rest of those by their binding sentences. One decision that concerns the change — the one just named in item 1 — it read only through its reasons, not through its rejected options. Nobody feels it today: the unread part is text of an approved decision that this change does not alter. Having a fresh reviewer read the rest in this request costs a session and a short round; undoing it, nothing. Making a task of it has no object beyond what item 1 already asks. Letting it through leaves the review as it was. I recommend letting it through, since the change leaves that decision as it is. Its weak point: if something in the unread part bears on the change, it shows only when someone next edits that decision. Read it in this request, make a task of it, or let it through? (Checks, 3)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. Two small choices beyond what the task states. First, the decision template now says in one sentence that a `TODO` in a decision's relations line is no third kind of relation, because the template's list of kinds is closed at two and would otherwise contradict the new form; the task named this as a note but listed no place for it. Second, the check also reports a `TODO` written right after a relation word as an error, not only a bare one: the reviewer showed that this is the form an author writes by analogy with the other relations, and it would have passed unremarked. The alternative, reporting only the bare form, would have left that natural form through.

4. Two decisions of the log are written by this change, and you did not see their wording at the task. The rule on what a decision entry may hold now lets a decision's relations line read the described `TODO` as its last item, for any decision it derives from that the foundation does not hold yet, whether or not a project definition plans it; the bare `TODO` is an error and the origin line never reads `TODO`, and the rule's reasons and rejected ways follow, the three ways the task did not choose among them. The rule on how a planned entry enters the foundation gains one sentence: the change that writes the entry replaces each described `TODO` that points at it with a reference by its identifier. For that second rule the cycle also added a pair of examples, one that complies and one that violates, which stand word for word under it in the lower part. (Foundation entries)

5. Four tests of the foundation check now hold the sentence of the first rule by a quoted line, so that a later change to that sentence is flagged at them: they check that a bare `TODO`, a `TODO` right after a relation word and a `TODO` joined with a comma are reported, and that the described form after known relations passes. One earlier test, which required any `TODO` in the relations line to be an error, now checks the origin line only, since this change reverses the rule for the relations line on purpose. The foundation check lists no invariant for a corrected sentence. (Foundation entries)

## Cost

Counted before this request opened: working time 0:45:18 across the orchestrator and its agents, of which 0:17:24 was waiting for tools; 37.5 million tokens (26.1 million on Sonnet 5.5, 11.4 million on Opus 5.5, which did the reviews). Two review rounds each ran a fix and a review of the fix: the review of the whole change failed once (one blocking finding, fixed and passed) and the review of the return step failed once (one blocking finding, fixed and passed). The table of stages stands in the record, linked under *Course of the cycle*.

Directories of four earlier tasks still stand because the cleaning script could not tell they were no longer needed; nothing in this request waits for them and you may remove them by hand. Their names, branches and reasons stand in *Checks*.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing here waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — pozycje 1 i 2 czekają na Twoją odpowiedź; pozycje 3, 4 i 5 tylko akceptujesz przez scalenie.

## Co zobaczysz

Gdy agent pisze decyzję, która wywodzi się z innej decyzji, jeszcze nieobecnej w fundamencie produktu — zwykle zaprojektowanej w zatwierdzonej definicji projektu, której żaden kod jeszcze nie spełnia — może teraz powiedzieć o tym w linii powiązań decyzji, tak jak dziś może niezmiennik: `TODO — <the decision, and where it is expected>`, jako ostatnia pozycja po znanych powiązaniach. Wcześniej agent mógł tylko wpisać `none` (nieprawda), zostawić goły `TODO` (skrypt go odrzucał) albo dopisać wpisy częściowe do Twojej akceptacji; gdy kod nie spełniał żadnej części zaplanowanej decyzji, PR stał zablokowany.

Skrypt sprawdzający fundament przyjmuje tę opisową postać. Zgłasza jako błąd goły `TODO` w linii powiązań, `TODO` wpisany tuż po słowie powiązania (`derives from TODO`) oraz `TODO` doklejony do innych powiązań przecinkiem zamiast ` · `. `TODO` w linii pochodzenia wpisu nadal jest błędem. Reguła o wejściu zaplanowanego wpisu do fundamentu mówi teraz też, że zmiana, która ten wpis zapisuje, zastępuje każde takie `TODO`, które go wskazuje, odwołaniem do niego. Szablon opisu PR-a wymienia nowe miejsce wśród pozostałości, które PR pokazuje Tobie.

### Pod spodem

Skrypt czyta linię powiązań tak, jak czyta już linie innych pól, w których może stać opisowe `TODO`, i nadal sprawdza każdy numer decyzji stojący przed nim; reguły, szablon decyzji i szablon opisu mówią to samo co skrypt.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Reguła, która mówi, jakie pozostałości PR pokazuje Tobie, wymienia trzy miejsca, w których może stać opisowe `TODO`; proces ma teraz czwarte — linię powiązań decyzji. Dziś nic się nie wywraca: szablon opisu wymienia wszystkie cztery, a ten PR napisano z niego. Odczuje to ten, kto później porówna PR z tą regułą i nie znajdzie w niej przypadku czwartego miejsca, więc `TODO` tam może przejść niezauważone. Poprawka w tym PR-ze to jedno krótkie dopisanie w trzech miejscach zatwierdzonej decyzji, a to zmienia brzmienie decyzji, którą zatwierdziłeś, więc potrzebuje Twojego tak; kosztuje turę poprawki z jej przeglądem, cofnięcie to kolejna edycja. Zrobienie z tego zadania zostawia dwie listy rozjechane do czasu tamtego zadania i nic dziś nie kosztuje; cofnięcie — nic. Przepuszczenie zostawia ten sam stan bez zadania, które go zakończy. Rekomenduję zrobić z tego zadanie, bo dokument zadania ustalił tę decyzję jako niezmienianą, a szablon opisu już obejmuje czwarte miejsce. Słaby punkt: do czasu zadania dwie listy się różnią i recenzent może pójść za krótszą. Naprawić w tym PR-ze, zrobić z tego zadanie czy przepuścić? (Uwagi poza zakresem zadania, 1)

2. Przegląd całej zmiany przeczytał w całości indeks swojego wyboru (33 decyzje wypisane w pełni i 123 po nagłówku), otworzył w całości 6 z decyzji wypisanych w pełni, a resztę z nich przeczytał po zdaniach wiążących. Jedną decyzję, która dotyczy zmiany — tę z pozycji 1 — przeczytał tylko do uzasadnienia, bez odrzuconych dróg. Dziś nikt tego nie odczuje: nieprzeczytana część to tekst zatwierdzonej decyzji, której ta zmiana nie rusza. Świeży recenzent czytający resztę w tym PR-ze to sesja i krótka tura; cofnięcie — nic. Zadanie z tego nie ma przedmiotu poza tym, o co pyta pozycja 1. Przepuszczenie zostawia przegląd, jaki był. Rekomenduję przepuścić, bo zmiana zostawia tę decyzję bez zmian. Słaby punkt: jeśli coś w nieprzeczytanej części dotyczy zmiany, wyjdzie dopiero przy następnej edycji tej decyzji. Przeczytać w tym PR-ze, zrobić z tego zadanie czy przepuścić? (Sprawdzenia, 3)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

3. Dwa drobne wybory ponad to, co mówi zadanie. Po pierwsze, szablon decyzji mówi teraz jednym zdaniem, że `TODO` w linii powiązań decyzji nie jest trzecim rodzajem powiązania, bo zamknięta lista rodzajów w szablonie ma dwa i inaczej zaprzeczałaby nowej postaci; zadanie wskazało to jako uwagę, ale nie wskazało miejsca. Po drugie, skrypt zgłasza jako błąd także `TODO` wpisany tuż po słowie powiązania, nie tylko goły: recenzent pokazał, że tak właśnie pisze autor przez analogię do innych powiązań i taka postać przeszłaby niezauważona. Alternatywa — zgłaszać tylko postać gołą — zostawiłaby tę naturalną postać przepuszczoną.

4. Ta zmiana zapisuje dwie decyzje dziennika, których brzmienia nie widziałeś przy zadaniu. Reguła o tym, co może zawierać wpis decyzji, pozwala teraz, by linia powiązań decyzji kończyła się opisowym `TODO`, dla każdej decyzji, z której wpis się wywodzi, a której fundament jeszcze nie ma — niezależnie od tego, czy definicja projektu ją planuje; goły `TODO` jest błędem, a linia pochodzenia nigdy nie ma `TODO`; uzasadnienie i odrzucone drogi idą za tym, w tym trzy drogi niewybrane w zadaniu. Reguła o wejściu zaplanowanego wpisu do fundamentu dostaje jedno zdanie: zmiana, która ten wpis zapisuje, zastępuje każde opisowe `TODO`, które go wskazuje, odwołaniem po identyfikatorze. Do tej drugiej reguły cykl dopisał też parę przykładów — jeden zgodny i jeden naruszający — które stoją dosłownie pod nią w dolnej części. (Wpisy fundamentu)

5. Cztery testy skryptu sprawdzającego fundament trzymają teraz zdanie pierwszej reguły przez cytat w linii, więc późniejsza zmiana tego zdania zostanie wskazana przy nich: sprawdzają, że goły `TODO`, `TODO` tuż po słowie powiązania i `TODO` doklejony przecinkiem są zgłaszane, a postać opisowa po znanych powiązaniach przechodzi. Jeden wcześniejszy test, który wymagał, by każde `TODO` w linii powiązań było błędem, sprawdza teraz tylko linię pochodzenia, bo ta zmiana celowo odwraca regułę dla linii powiązań. Skrypt nie wskazuje żadnego niezmiennika ze skorygowanym zdaniem. (Wpisy fundamentu)

## Koszt

Policzony przed otwarciem PR-a: czas pracy 0:45:18 orkiestratora i jego agentów, w tym 0:17:24 czekania na narzędzia; 37,5 mln tokenów (26,1 mln na Sonnet 5.5, 11,4 mln na Opus 5.5, który robił przeglądy). Dwie rundy przeglądu miały poprawkę i przegląd poprawki: przegląd całej zmiany zakończył się raz niepowodzeniem (jedna uwaga blokująca, poprawiona i zaliczona), przegląd kroku powrotu też raz (jedna uwaga blokująca, poprawiona i zaliczona). Tabela etapów leży w zapisie cyklu, z linkiem w *Przebiegu cyklu*.

Katalogi czterech wcześniejszych zadań nadal stoją, bo skrypt czyszczący nie umiał rozpoznać, że już nie są potrzebne; nic w tym PR-ze na nie nie czeka i możesz je usunąć ręcznie. Ich nazwy, gałęzie i powody są w *Sprawdzeniach*.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy. Nic tu nie czeka na przegląd fundamentu.

</details>

## Technical changes

The change is four commits on the base `30c947f`; the first three are the author's work and its two fixes, the last two answer reviews.

1. `452f123` — the change itself. A decision's *Relations* may read `TODO — <the decision, and where it is expected>` as its last item (WAY-71; `elements/common/rules.md`; `elements/decisions/template.md`, which also says the form is no third relation type); `elements/common/foundation_check.py` takes the form (`MISSING` gains *Relations*; the numbers of the description are read as no reference; the known part is still checked line by line) and its tests; WAY-126 gains the sentence that replaces a `TODO` by its reference; `task-cycle/skill/request_template.md`, item 16, lists the new place.
2. `68d8645` — the fix of the review of the whole change: a `TODO` behind a relation type is an error in *Relations* (new pattern `TYPED_TODO`), four tests written before the fix and seen failing, the WAY-126 wording gives the reference with its type (`derives from <number>`), a test for a wrong number on the second line of the known part, and the docstring paragraph rewrapped to 100 columns. `foundation_check.py` stands at 999 lines, one under the 1000-line threshold, so the next addition there must start with a move out of it.
3. `763af69` — the return step: WAY-71's *Verification* opens with a `tests:` clause for the *Relations* part and its pair keeps the rest; two `decision:` lines in the test file.
4. `07a23b3` — the fix of the review of the return step: two more `decision:` lines, at the tests of the comma join and of the described form after known relations, so that each of the four parts the clause names has a test that holds it.

No Minor finding of the review of the whole change is left unfixed (M1, M2 and M3 were fixed with the blocking finding); the Minor findings that no fix made are below.

## Checks

1. The final gate is the CI run on the request's last head: its result is written here once it reports (the cycle runs no full gate on its own system). The agents' focused checks, all exit 0: `python -B gate/run_tests.py elements/common` 257 tests OK on the last head; `python -B gate/run_tests.py task-cycle` 534 OK, `product-guidelines` 14 OK and `agent-instructions` 37 OK, run by the author on `452f123`; `python -B elements/common/foundation_check.py` exit 0, `0 errors`, no `listed:` line, run by the orchestrator on `07a23b3` without `--skip-test-citations`. `python -B task-cycle/change_file_sizes.py` exit 0: no function or file the change touches went over a threshold of the size rule.
2. Tests failing before the change: none. The base is a merge commit with the tree of its second parent, so no gate ran on it; the list was taken from the final gate of the cycle of the merged request: its cycle record `docs/task-cycles/ci-replaces-local-final-gate/cycle.md` as added by commit `8162a28` (the gate on `cdfcf48`, exit 0, 1601 tests) and the checks of the merged request, which read `tests` and `tests-windows` green.
3. Not run: `ruff` is not installed on the system where the agents worked, so the linter's blocking rules ran in no agent's check; the CI gate runs it. The review of the whole change read 6 of the 33 decisions listed in full whole, and read WAY-287 through its reasons only (item 2 above).
4. Own-work checks. The author's: on the real decision log, with WAY-71's relations line set in turn to four values, the described form passed and each bad form was reported at its line; the fix's: the same with the forms behind a relation type, all reported with the form's message; the return step's: with a quotation altered the check rejected it, so the new `decision:` lines are read; the fix of the return step's: the same with the first quotation altered ("holds" to "keeps"), rejected, then restored.
5. The form check on this description and the check of private paths on it: written and checked before the request opened; their last runs are in the record. The checks on the copy of the record are filled in with the record's link.
6. Remarks check: `python -B task-cycle/remarks_check.py` on the original, run 1 exit 1 (2 items listed, appended to the process remarks), run 2 exit 0; the run on the copy is filled in with the record's link.
7. Directories of earlier tasks kept, with no absolute path: agent-path-to-running-product · task/agent-path-to-running-product · the branch has no merge git can see on origin/foundations; audit-answers-contradiction-after-code · task/audit-answers-contradiction-after-code · the same reason; base-check-stage-remarks · detached · the branch task/stage-remarks its name gives is not found; base-fix-minor-findings · detached · the branch task/minor-findings its name gives is not found. Working copies left by agents: none.

## Foundation entries

- WAY-71 — a decision's *Relations* may read `TODO — <the decision, and where it is expected>` as its last item for any decision the entry derives from that the foundation does not hold yet; a bare `TODO` there is an error and *Origin* never reads `TODO`. Marked `the cycle's`. Its pair of examples stands as the entry held it, with the *Relations* part now held by tests, so no pair was added.
- WAY-126 — the change that writes a projected entry replaces each descriptive `TODO` that points at it with a reference to it, in a decision's *Relations* as `derives from <number>` and in an invariant's *Derives from* as the number. Marked `the cycle's`, for the pair added to it:
  - complies, added: "a task whose code makes a projected decision true writes it into the log and replaces the `TODO` that names it with `derives from <its number>` in the *Relations* of a decision and with its number in the *Derives from* of an invariant";
  - violates, added: "a task writes a projected decision into the log and leaves a decision's *Relations* reading `TODO — <that decision, and where it is expected>`".
- Tests that hold a sentence of WAY-71 by a line `decision:`, added by this change (WAY-03, WAY-12): `test_relations_a_known_decision_then_a_missing_one_described_passes`, `test_relations_a_bare_todo_names_no_decision`, `test_relations_derives_from_todo_is_an_error` and `test_relations_a_described_todo_after_a_comma_is_no_joined_list`, all in `elements/common/test_foundation_check.py`. The test `test_relations_and_origin_take_no_todo` was cut to `test_origin_takes_no_todo`: its *Relations* half asserted the rule this task reverses.
- No topical section of the decision log is opened, no row of *Settlements to record* is written (the section reads `none`), no invariant, surface or *Violated* mark changes.

## Minor findings

The Minor findings of the review of the whole change that lay within the task (M1, M2, M3) were fixed with its blocking finding. The ones below were found later, by the review of the fix and the review of the return step, and are not fixed, as the cycle's rules give.

- N1 (review of the fix, `elements/common/foundation_check.py:170`): "`TYPED_TODO = re.compile(r"(?:derives from|narrows)[ \t]+(?=…TODO…)")` matches the types only in lower case with one space between `derives` and `from`. Scratch runs at the fix head: `- **Relations:** Derives from TODO` → `0 errors`; `- **Relations:** derives from WAY-01 · derives  from TODO` → `0 errors`. The template writes the types in lower case with one space, and the script checks the spelling of no relation type anywhere else (`Derives from WAY-01` passes too), so these values are typos the check of types would catch if one existed, not the form I1 named; that keeps it Minor. A case-insensitive match with `\s+` between the words would close it at no cost."
- N2 (review of the fix, `elements/common/test_foundation_check.py:756-757` and `:751-754`): "`test_relations_derives_from_todo_is_an_error` asserts for `derives from TODO` what `test_relations_a_bare_todo_behind_a_type_is_an_error` asserts for `narrows TODO` and `derives from TODO —`; the value could be a subtest of the latter. The testing guidelines name a duplicating test only under *Examples*, which binds nothing."
- m1 (review of the return step, the return step's report, section "For the human: WAY-287"): "WAY-287's second paragraph lets another decision add a *kind* of item 'naming the group'; WAY-71 names no group, and a descriptive `TODO` in *Relations* is not a new kind but WAY-287's own kind whose list of fields is now short by one. The conclusion — leave WAY-287 to the human, as M4 already does — stands; the argument should not be carried into the request's description as the reason the gap is harmless." The description does not carry that argument.

## Findings outside the task's scope

1. M4 (review of the whole change, `foundations/decisions.md`, the binding sentence, the *Verification* violates line and the *Rationale* of WAY-287): "WAY-287 lists three fields for the descriptive `TODO` while item 16 of the request template now lists four. Nothing contradicts — WAY-287 does not exclude the fourth field, and the orchestrator writes the request from item 16 — but a reviewer comparing a request with WAY-287's examples finds no case for a *Relations* `TODO`, and WAY-287's own *Rejected* names this very risk of an enumeration in its sentence: 'a forgotten change giving the same gap between the decision and this entry'. Leaving it costs nothing today; the fix is one clause ('or *Relations*') in three places and changes the wording of an approved decision, so it is the human's to decide." (Item 1.)
2. M5 (review of the whole change, `elements/decisions/template.md`, the table of who reads each field): "The template's table of readers does not name what now reads *Relations*. `foundation_check.py` reads the field (a decision number that names no decision, and now a bare `TODO`), the orchestrator reads it for item 16 of the request, and the writer of a projected entry reads it for WAY-126's new sentence. The row of *Based on* names `foundation_check.py`; the row of *Relations* never did, so the gap predates the change and only widens with it." A user of the process will not feel it, so it stands here only.

## Course of the cycle

- **Task and sources:** the task "the way: decision derived from a not yet written decision gets a descriptive `TODO` in *Relations*" (independent; ready for cycle; its answers given by the day advisor for you on 2026-11-14). Sources: the decision log, the decision template, the shared rules and the check script on `foundations` at `30c947f`. Two statements of the task no longer held and were reconciled with the sources: the-way now has `guidelines/` (the author followed them), and the two decisions the task lists as unchanged, WAY-32 and WAY-37, are withdrawn, their rules standing in the decision template and in the way-of-working file.
- **Process pin:** none — the-way itself.
- **Spec:** none — no open design choice (the task fixes the form and the files).
- **Route:** one author without a plan, class `same` (Sonnet 5.5): the change rewrites binding sentences of two decisions and a check's reading of a field, over three parts. Reviews on Opus 5.5.
- **Plan:** none.
- **Choices:** 3 rows in the questions table (two stale statements of the task reconciled with the sources, and your instruction to wait for the day advisor's start signal before every full gate and to run reviewers on Opus), plus the author's own choices in its reports.
- **Blocking findings left:** none.
- **Record:** the link is added with the record's commit.
