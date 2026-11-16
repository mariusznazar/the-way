**State: ready** — corrected for your remarks; nothing waits for your answer, and the items below you only accept by merging.

## What you will see

When an agent writes a decision that derives from another decision the product's foundation does not hold yet — typically one designed in an approved project definition that no code makes true — it can now say so in the decision's relations line, in the same way an invariant already can: `TODO — <the decision, and where it is expected>`, as the last item after the relations that are known. Before, the agent could only write `none`, which is false, or leave a bare `TODO`, which the check rejected, or add partial entries for you to accept; where the code made no part of the planned decision true, the request stood blocked.

The foundation check accepts that described form. It reports as errors a bare `TODO` in the relations line, a `TODO` written right after a relation word (`derives from TODO`), and a `TODO` joined to other relations with a comma instead of ` · `. A `TODO` in the line for the entry's origin stays an error. The rule for how a planned entry enters the foundation now also says that the change that writes the entry replaces each such `TODO` that points at it with a reference to it. The request template lists the new place among the leftovers a request puts before you, and, at your remark, so does the rule that says which leftovers a request shows you, which had listed three places and now lists four.

One more fact is corrected at your remark: the rule of the repository that guards the branch now requires two checks, `tests` and `tests-windows`, and the record of that fact now says so.

### Underneath

The check script reads the relations line the way it already reads the lines of the other fields that may hold a described `TODO`, and still checks every decision number that stands before it; the rules, the decision template and the request template say the same as the script.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. Two small choices beyond what the task states. First, the decision template now says in one sentence that a `TODO` in a decision's relations line is no third kind of relation, because the template's list of kinds is closed at two and would otherwise contradict the new form; the task named this as a note but listed no place for it. Second, the check also reports a `TODO` written right after a relation word as an error, not only a bare one: the reviewer showed that this is the form an author writes by analogy with the other relations, and it would have passed unremarked. The alternative, reporting only the bare form, would have left that natural form through.

2. Two decisions of the log are written by this change, and you did not see their wording at the task. The rule on what a decision entry may hold now lets a decision's relations line end with the described `TODO`, for any decision it derives from that the foundation does not hold yet, whether or not a project definition plans it; the bare `TODO` is an error and the origin line never reads `TODO`, and the rule's reasons and rejected ways follow, the three ways the task did not choose among them. The rule on how a planned entry enters the foundation gains one sentence: the change that writes the entry replaces each described `TODO` that points at it with a reference by its identifier. For that second rule the cycle also added a pair of examples, one that complies and one that violates, which stand word for word under it in the lower part. (Foundation entries)

3. Two more entries were changed at your remarks. The rule that says which leftover markers a request shows you now names a decision's relations line as the fourth place where a described `TODO` may stand, in its binding sentence, its violating line and its reasons, and nothing else of it changed. The record of the repository's branch rule now says the rule requires the two checks `tests` and `tests-windows`, as it read on 2026-11-16, with the output of the two read commands quoted as its source. (Foundation entries)

4. Four tests of the foundation check now hold the sentence of the first rule by a quoted line, so that a later change to that sentence is flagged at them: they check that a bare `TODO`, a `TODO` right after a relation word and a `TODO` joined with a comma are reported, and that the described form after known relations passes. One earlier test, which required any `TODO` in the relations line to be an error, now checks the origin line only, since this change reverses the rule for the relations line on purpose. The foundation check lists no invariant for a corrected sentence. (Foundation entries)

5. This correction answered your answer to one item of this request and one remark of yours outside any item, and the cycle judged that neither the task nor the foundation required what they asked to change: you asked for the fourth place to be added to the rule on leftover markers, which the task had fixed as unchanged, and for the branch rule's record to be brought up to what the owner set today.

## Cost

Counted before this corrected request was published: working time 1:15:44 across the orchestrator and its agents, of which 0:38:17 was waiting for tools (the wait for the CI run is in it); 57.7 million tokens (44.6 million on Sonnet 5.5, 13.1 million on Opus 5.5, which did the reviews). Two review rounds each ran a fix and a review of the fix: the review of the whole change failed once (one blocking finding, fixed and passed) and the review of the return step failed once (one blocking finding, fixed and passed); the review of the correction passed at once. The table of stages stands in the record, linked under *Course of the cycle*.

Directories of four earlier tasks still stand because the cleaning script could not tell they were no longer needed; nothing in this request waits for them and you may remove them by hand. Their names, branches and reasons stand in *Checks*.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing here waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — poprawione według Twoich uwag; nic nie czeka na Twoją odpowiedź, a pozycje poniżej tylko akceptujesz przez scalenie.

## Co zobaczysz

Gdy agent pisze decyzję, która wywodzi się z innej decyzji, jeszcze nieobecnej w fundamencie produktu — zwykle zaprojektowanej w zatwierdzonej definicji projektu, której żaden kod jeszcze nie spełnia — może teraz powiedzieć o tym w linii powiązań decyzji, tak jak dziś może niezmiennik: `TODO — <the decision, and where it is expected>`, jako ostatnia pozycja po znanych powiązaniach. Wcześniej agent mógł tylko wpisać `none` (nieprawda), zostawić goły `TODO` (skrypt go odrzucał) albo dopisać wpisy częściowe do Twojej akceptacji; gdy kod nie spełniał żadnej części zaplanowanej decyzji, PR stał zablokowany.

Skrypt sprawdzający fundament przyjmuje tę opisową postać. Zgłasza jako błąd goły `TODO` w linii powiązań, `TODO` wpisany tuż po słowie powiązania (`derives from TODO`) oraz `TODO` doklejony do innych powiązań przecinkiem zamiast ` · `. `TODO` w linii pochodzenia wpisu nadal jest błędem. Reguła o wejściu zaplanowanego wpisu do fundamentu mówi teraz też, że zmiana, która ten wpis zapisuje, zastępuje każde takie `TODO`, które go wskazuje, odwołaniem do niego. Szablon opisu PR-a wymienia nowe miejsce wśród pozostałości, które PR pokazuje Tobie, i — na Twoją uwagę — robi to także reguła mówiąca, jakie pozostałości PR pokazuje; wymieniała trzy miejsca, teraz wymienia cztery.

Poprawiony jest też jeden fakt: reguła repozytorium chroniąca gałąź wymaga teraz dwóch sprawdzeń, `tests` i `tests-windows`, i zapis tego faktu mówi to samo.

### Pod spodem

Skrypt czyta linię powiązań tak, jak czyta już linie innych pól, w których może stać opisowe `TODO`, i nadal sprawdza każdy numer decyzji stojący przed nim; reguły, szablon decyzji i szablon opisu mówią to samo co skrypt.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

none

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

1. Dwa drobne wybory ponad to, co mówi zadanie. Po pierwsze, szablon decyzji mówi teraz jednym zdaniem, że `TODO` w linii powiązań decyzji nie jest trzecim rodzajem powiązania, bo zamknięta lista rodzajów w szablonie ma dwa i inaczej zaprzeczałaby nowej postaci; zadanie wskazało to jako uwagę, ale nie wskazało miejsca. Po drugie, skrypt zgłasza jako błąd także `TODO` wpisany tuż po słowie powiązania, nie tylko goły: recenzent pokazał, że tak właśnie pisze autor przez analogię do innych powiązań i taka postać przeszłaby niezauważona. Alternatywa — zgłaszać tylko postać gołą — zostawiłaby tę naturalną postać przepuszczoną.

2. Ta zmiana zapisuje dwie decyzje dziennika, których brzmienia nie widziałeś przy zadaniu. Reguła o tym, co może zawierać wpis decyzji, pozwala teraz, by linia powiązań decyzji kończyła się opisowym `TODO`, dla każdej decyzji, z której wpis się wywodzi, a której fundament jeszcze nie ma — niezależnie od tego, czy definicja projektu ją planuje; goły `TODO` jest błędem, a linia pochodzenia nigdy nie ma `TODO`; uzasadnienie i odrzucone drogi idą za tym, w tym trzy drogi niewybrane w zadaniu. Reguła o wejściu zaplanowanego wpisu do fundamentu dostaje jedno zdanie: zmiana, która ten wpis zapisuje, zastępuje każde opisowe `TODO`, które go wskazuje, odwołaniem po identyfikatorze. Do tej drugiej reguły cykl dopisał też parę przykładów — jeden zgodny i jeden naruszający — które stoją dosłownie pod nią w dolnej części. (Wpisy fundamentu)

3. Na Twoje uwagi zmieniono jeszcze dwa wpisy. Reguła mówiąca, jakie pozostałości PR pokazuje Tobie, wymienia teraz linię powiązań decyzji jako czwarte miejsce, w którym może stać opisowe `TODO` — w zdaniu wiążącym, w linii naruszenia i w uzasadnieniu — i nic poza tym się w niej nie zmieniło. Zapis reguły chroniącej gałąź repozytorium mówi teraz, że reguła wymaga dwóch sprawdzeń, `tests` i `tests-windows`, tak jak odczytano ją 2026-11-16, a wynik dwóch poleceń odczytu jest w nim zacytowany jako źródło. (Wpisy fundamentu)

4. Cztery testy skryptu sprawdzającego fundament trzymają teraz zdanie pierwszej reguły przez cytat w linii, więc późniejsza zmiana tego zdania zostanie wskazana przy nich: sprawdzają, że goły `TODO`, `TODO` tuż po słowie powiązania i `TODO` doklejony przecinkiem są zgłaszane, a postać opisowa po znanych powiązaniach przechodzi. Jeden wcześniejszy test, który wymagał, by każde `TODO` w linii powiązań było błędem, sprawdza teraz tylko linię pochodzenia, bo ta zmiana celowo odwraca regułę dla linii powiązań. Skrypt nie wskazuje żadnego niezmiennika ze skorygowanym zdaniem. (Wpisy fundamentu)

5. Ta poprawka odpowiedziała na Twoją odpowiedź do jednej pozycji tego PR-a i na jedną Twoją uwagę poza pozycjami, a cykl uznał, że ani zadanie, ani fundament nie wymagały tego, o co prosiły: poprosiłeś o dopisanie czwartego miejsca do reguły o pozostałościach, którą zadanie ustaliło jako niezmienianą, i o doprowadzenie zapisu reguły gałęzi do tego, co właściciel ustawił dziś.

## Koszt

Policzony przed opublikowaniem tego poprawionego PR-a: czas pracy 1:15:44 orkiestratora i jego agentów, w tym 0:38:17 czekania na narzędzia (jest w nim czekanie na CI); 57,7 mln tokenów (44,6 mln na Sonnet 5.5, 13,1 mln na Opus 5.5, który robił przeglądy). Dwie rundy przeglądu miały poprawkę i przegląd poprawki: przegląd całej zmiany zakończył się raz niepowodzeniem (jedna uwaga blokująca, poprawiona i zaliczona), przegląd kroku powrotu też raz (jedna uwaga blokująca, poprawiona i zaliczona); przegląd korekty zaliczył od razu. Tabela etapów leży w zapisie cyklu, z linkiem w *Przebiegu cyklu*.

Katalogi czterech wcześniejszych zadań nadal stoją, bo skrypt czyszczący nie umiał rozpoznać, że już nie są potrzebne; nic w tym PR-ze na nie nie czeka i możesz je usunąć ręcznie. Ich nazwy, gałęzie i powody są w *Sprawdzeniach*.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy. Nic tu nie czeka na przegląd fundamentu.

</details>

## Technical changes

The change is five commits on the base `30c947f`: the first three are the author's work and its two fixes, the next two answer reviews, the last is the correction.

1. `452f123` — the change itself. A decision's *Relations* may read `TODO — <the decision, and where it is expected>` as its last item (WAY-71; `elements/common/rules.md`; `elements/decisions/template.md`, which also says the form is no third relation type); `elements/common/foundation_check.py` takes the form (`MISSING` gains *Relations*; the numbers of the description are read as no reference; the known part is still checked line by line) and its tests; WAY-126 gains the sentence that replaces a `TODO` by its reference; `task-cycle/skill/request_template.md`, item 16, lists the new place.
2. `68d8645` — the fix of the review of the whole change: a `TODO` behind a relation type is an error in *Relations* (new pattern `TYPED_TODO`), four tests written before the fix and seen failing, the WAY-126 wording gives the reference with its type (`derives from <number>`), a test for a wrong number on the second line of the known part, and the docstring paragraph rewrapped to 100 columns. `foundation_check.py` stands at 999 lines, one under the 1000-line threshold, so the next addition there must start with a move out of it.
3. `763af69` — the return step: WAY-71's *Verification* opens with a `tests:` clause for the *Relations* part and its pair keeps the rest; two `decision:` lines in the test file.
4. `07a23b3` — the fix of the review of the return step: two more `decision:` lines, at the tests of the comma join and of the described form after known relations, so that each of the four parts the clause names has a test that holds it.
5. `000a7639` — correction 1, for your remarks: WAY-287 names a decision's *Relations* in the three places that listed the other fields (its binding sentence, its violating line and its *Rationale*); the environment fact `foundations-branch-ruleset` is corrected to the two required checks. The decision about CI (WAY-16) names no single check and stays as it was; the files that name the checks (`agent-instructions/README.md`, `installation/README.md`, the CI workflow) already agree with two.

No Minor finding of the review of the whole change is left unfixed (M1, M2 and M3 were fixed with the blocking finding); the Minor findings that no fix made are below.

## Checks

1. The final gate is the CI run on the request's last head: its result is written here once it reports (the cycle runs no full gate on its own system). The agents' focused checks, all exit 0: `python -B gate/run_tests.py elements/common` 257 tests OK on the last head; `python -B gate/run_tests.py task-cycle` 534 OK (author, on `452f123`, and again by the correction's author on `000a7639`), `product-guidelines` 14 OK and `agent-instructions` 37 OK (author, on `452f123`); `python -B elements/common/foundation_check.py` exit 0, `0 errors`, no `listed:` line, run by the orchestrator on `000a7639` without `--skip-test-citations`. `python -B task-cycle/change_file_sizes.py` exit 0 in the reviews of the first change: no function or file the change touches went over a threshold of the size rule.
2. Tests failing before the change: none. The base is a merge commit with the tree of its second parent, so no gate ran on it; the list was taken from the final gate of the cycle of the merged request: its cycle record `docs/task-cycles/ci-replaces-local-final-gate/cycle.md` as added by commit `8162a28` (the gate on `cdfcf48`, exit 0, 1601 tests) and the checks of the merged request, which read `tests` and `tests-windows` green.
3. Not run: `ruff` is not installed on the system where the agents worked, so the linter's blocking rules ran in no agent's check; the CI gate runs it. The review of the whole change read 6 of the 33 decisions listed in full whole and read the decision on leftover markers through its reasons only; at your remark the review of the correction read that decision whole, its rejected options included, and read the CI decision whole, and found nothing in the part not read before that bears on the change.
4. Own-work checks. The author's: on the real decision log, with WAY-71's relations line set in turn to four values, the described form passed and each bad form was reported at its line; the fix's: the same with the forms behind a relation type, all reported with the form's message; the return step's: with a quotation altered the check rejected it, so the new `decision:` lines are read; the fix of the return step's: the same with the first quotation altered ("holds" to "keeps"), rejected, then restored; the correction's: the two `gh api` read commands the environment fact holds were run again (GET only, nothing written on the host), the quoted output compared with a fresh run, both match; the reviewer of the correction ran the same two commands and found the quotation matching character for character.
5. The form check on this description (`python -B task-cycle/request_check.py … --task …`) and the check of private paths on it (`python -B task-cycle/private_paths_check.py …`): checked before the corrected description was published, results below with the record's link.
6. Remarks check: `python -B task-cycle/remarks_check.py` on the original, exit 0 after the items were appended (4 runs in all across the cycle and the correction).
7. Directories of earlier tasks kept, with no absolute path: agent-path-to-running-product · task/agent-path-to-running-product · the branch has no merge git can see on origin/foundations; audit-answers-contradiction-after-code · task/audit-answers-contradiction-after-code · the same reason; base-check-stage-remarks · detached · the branch task/stage-remarks its name gives is not found; base-fix-minor-findings · detached · the branch task/minor-findings its name gives is not found. Working copies left by agents: none.

## Foundation entries

- WAY-71 — a decision's *Relations* may read `TODO — <the decision, and where it is expected>` as its last item for any decision the entry derives from that the foundation does not hold yet; a bare `TODO` there is an error and *Origin* never reads `TODO`. Marked `the cycle's`. Its pair of examples stands as the entry held it, with the *Relations* part now held by tests, so no pair was added.
- WAY-126 — the change that writes a projected entry replaces each descriptive `TODO` that points at it with a reference to it, in a decision's *Relations* as `derives from <number>` and in an invariant's *Derives from* as the number. Marked `the cycle's`, for the pair added to it:
  - complies, added: "a task whose code makes a projected decision true writes it into the log and replaces the `TODO` that names it with `derives from <its number>` in the *Relations* of a decision and with its number in the *Derives from* of an invariant";
  - violates, added: "a task writes a projected decision into the log and leaves a decision's *Relations* reading `TODO — <that decision, and where it is expected>`".
- WAY-287 (changed at your remark) — the request's section for your decisions also lists a descriptive `TODO` in a decision's *Relations* among the gaps the merge leaves. Marked `the cycle's`; no pair was added.
- `foundations-branch-ruleset` (environment fact, changed at your remark) — the rule `foundations_tests` on `foundations` requires two checks, `tests` and `tests-windows`, as read on 2026-11-16. Marked `the cycle's`.
- Tests that hold a sentence of WAY-71 by a line `decision:`, added by this change (WAY-03, WAY-12): `test_relations_a_known_decision_then_a_missing_one_described_passes`, `test_relations_a_bare_todo_names_no_decision`, `test_relations_derives_from_todo_is_an_error` and `test_relations_a_described_todo_after_a_comma_is_no_joined_list`, all in `elements/common/test_foundation_check.py`. The test `test_relations_and_origin_take_no_todo` was cut to `test_origin_takes_no_todo`: its *Relations* half asserted the rule this task reverses.
- No topical section of the decision log is opened, no row of *Settlements to record* is written (the section reads `none`), no invariant, surface or *Violated* mark changes.

## Minor findings

The Minor findings of the review of the whole change that lay within the task (M1, M2, M3) were fixed with its blocking finding. The ones below were found later, by the review of the fix, the review of the return step and the review of the correction, and are not fixed, as the cycle's rules give.

- N1 (review of the fix, `elements/common/foundation_check.py:170`): "`TYPED_TODO = re.compile(r"(?:derives from|narrows)[ \t]+(?=…TODO…)")` matches the types only in lower case with one space between `derives` and `from`. Scratch runs at the fix head: `- **Relations:** Derives from TODO` → `0 errors`; `- **Relations:** derives from WAY-01 · derives  from TODO` → `0 errors`. The template writes the types in lower case with one space, and the script checks the spelling of no relation type anywhere else (`Derives from WAY-01` passes too), so these values are typos the check of types would catch if one existed, not the form I1 named; that keeps it Minor. A case-insensitive match with `\s+` between the words would close it at no cost."
- N2 (review of the fix, `elements/common/test_foundation_check.py:756-757` and `:751-754`): "`test_relations_derives_from_todo_is_an_error` asserts for `derives from TODO` what `test_relations_a_bare_todo_behind_a_type_is_an_error` asserts for `narrows TODO` and `derives from TODO —`; the value could be a subtest of the latter. The testing guidelines name a duplicating test only under *Examples*, which binds nothing."
- m1 (review of the return step, the return step's report, section "For the human: WAY-287"): "WAY-287's second paragraph lets another decision add a *kind* of item 'naming the group'; WAY-71 names no group, and a descriptive `TODO` in *Relations* is not a new kind but WAY-287's own kind whose list of fields is now short by one. The conclusion — leave WAY-287 to the human, as M4 already does — stands; the argument should not be carried into the request's description as the reason the gap is harmless." The description does not carry that argument, and the list of fields of that decision is now whole (correction 1).
- m-a (review of the correction, `foundations/decisions.md:7047-7054`): "WAY-287's *complies* list still gives no example of a *Relations* `TODO` (outside what the remark asked; not blocking). The complies examples name an invariant's `Rests on: TODO — …`, a decision's `Based on: TODO — …` and an invariant's `Derives from: TODO — …`, but no decision reading `Relations: TODO — <the decision, and where it is expected>`. The binding sentence (`:7006-7008`), the *violates* line (`:7064-7067`) and the *Rationale* (`:7082-7086`) now name *Relations*, so no sentence a reader follows excludes the fourth field; M4 itself noted that a reviewer comparing a request with WAY-287's examples finds no such case. Remark 1 named the binding sentence, the *Verification* lines and the *Rationale* 'as M4 names them', and M4's places are the violates line, not the complies examples, so the author kept to the remark. One more example clause would close it; leaving it costs nothing today."
- m-b (review of the correction, `foundations/decisions.md:7008` and `:7084`): "Two reflowed lines of WAY-287 run wider than the paragraph (style). `foundations/decisions.md:7008` (119 characters) and `:7084` (117); the paragraph wraps at about 100. The entry already held a 121-character line (`:7074`) and a 103-character one before the change, and no check covers width in the log, so this is style only."

## Findings outside the task's scope

1. M5 (review of the whole change, `elements/decisions/template.md`, the table of who reads each field): "The template's table of readers does not name what now reads *Relations*. `foundation_check.py` reads the field (a decision number that names no decision, and now a bare `TODO`), the orchestrator reads it for item 16 of the request, and the writer of a projected entry reads it for WAY-126's new sentence. The row of *Based on* names `foundation_check.py`; the row of *Relations* never did, so the gap predates the change and only widens with it." You let it through with no task. (M4, the list of fields in the decision on leftover markers, is fixed by correction 1.)

## Course of the cycle

- **Task and sources:** the task "the way: decision derived from a not yet written decision gets a descriptive `TODO` in *Relations*" (independent; ready for cycle; its answers given by the day advisor for you on 2026-11-14). Sources: the decision log, the decision template, the shared rules and the check script on `foundations` at `30c947f`. Two statements of the task no longer held and were reconciled with the sources: the-way now has `guidelines/` (the author followed them), and the two decisions the task lists as unchanged, WAY-32 and WAY-37, are withdrawn, their rules standing in the decision template and in the way-of-working file.
- **Process pin:** none — the-way itself.
- **Spec:** none — no open design choice (the task fixes the form and the files).
- **Route:** one author without a plan, class `same` (Sonnet 5.5): the change rewrites binding sentences of two decisions and a check's reading of a field, over three parts. Reviews on Opus 5.5. Correction 1: your remarks (`reports/correction-1-remarks.md`; the target branch had not moved, so no merge), made by the resumed author, reviewed by a fresh reviewer on Opus 5.5 that read the decision on leftover markers whole, then the return step, which committed nothing.
- **Plan:** none.
- **Choices:** 5 rows in the questions table (two stale statements of the task reconciled with the sources, your instruction to wait for the day advisor's start signal before every full gate and to run reviewers on Opus, the correction's extra entry done as you asked, and the return step of the correction as a separate turn), plus the author's own choices in its reports.
- **Blocking findings left:** none.
- **Record:** RECORD_LINK
