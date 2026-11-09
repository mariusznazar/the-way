**State: ready** — the change is complete, was reviewed by agents that did not make it, and the full tests pass; two questions wait for your yes below.

## What you will see

- The rule for how a product's own rule says it is kept now matches what the cycles already do. A rule may say "kept by a test" from the moment it is written, when the test that keeps it is written later in the same change. Before, the foundation said to write "kept by review" until the test existed, and agents wrote "test" at once and had to settle the contradiction themselves.
- A new automatic check closes the gap this opens. Whenever the script that checks the foundation runs, it now reports every rule that says "kept by a test" while no test mentions it, naming the rule and the line. A forgotten test can no longer leave a false "test" in the foundation without a signal; the tests that run all of a product's checks fail on it.
- One run is exempt: the run an agent makes right after writing a foundation entry. It passes a switch that skips this one report, because the test of a rule written in the same change may not exist yet. The instructions for writing an entry now tell the agent to pass it. An agent that forgets the switch sees an error and may turn the rule back to "kept by review", which is the safe direction.
- The foundation of the-way itself now states this as a rule of its own, and the one test that already runs the check on the-way's own foundation now mentions it. On today's foundation the check passes: all 19 rules that say "kept by a test" have a test.

### Underneath

The check reuses the way the script already finds the lines in which tests name a rule (comment lines in tracked files other than Markdown), so no second way of listing files was added. Two one-clause edits keep the overview of the repository and the installation guide true to the new behaviour.

## For you to decide

1. The task left a few choices to the cycle, and another answer would change what you or an agent meets. The switch is named `--skip-test-citations`. The way the task rejected (a sentence in the planning skill that turns "review" into "test" in a later slice) is recorded among the ways the decision on the method did not take. Two sentences were added outside the task's list, one in the overview of the repository and one in the installation guide, so that both still describe the script truly. Accept?
2. The new rule that every "test" rule is mentioned by a test derives from the decision on the check and also from the decision on the method; the task left the derivation to the cycle. The one test that runs the check on the-way's own foundation now carries a mention of the new rule (an invariant test altered), and the check command gains an optional switch while keeping its path, argument and exit codes (a surface altered). Accept?

## Cost

About 30 minutes of working time in 11 stages, plus the waits for the two full test runs: 19.5 million tokens (14.4 million on claude-sonnet-5-5, 5.1 million on claude-opus-5-5), mostly cached input. Review rounds: 1 on the whole change (passed, with 3 Minor findings that were fixed in one fix) and 1 on that fix (passed). The table of stages is in the committed record.

## How to merge

Use a merge that keeps the commits, because the link to the record survives only then. The branch has 3 commits on top of the target branch, and the target branch has not moved.

<details>
<summary>W języku zadania (polski)</summary>

**Stan: gotowe** — zmiana jest kompletna, przejrzana przez agentów, którzy jej nie pisali, a pełne testy przechodzą; poniżej czekają dwa pytania o Twoje „tak”.

## Co zobaczysz

- Reguła o tym, jak reguła produktu mówi, czym jest pilnowana, zgadza się teraz z tym, co robią cykle. Reguła może mówić „pilnuje test” od chwili zapisania, gdy test, który ją pilnuje, powstaje później w tej samej zmianie. Wcześniej fundament kazał pisać „pilnuje przegląd”, dopóki testu nie ma, a agenci pisali od razu „test” i musieli sami rozstrzygać sprzeczność.
- Nowe sprawdzenie automatyczne zamyka lukę, którą to otwiera. Za każdym razem, gdy działa skrypt sprawdzający fundament, zgłasza teraz każdą regułę, która mówi „pilnuje test”, choć żaden test jej nie wymienia, i podaje regułę oraz linię. Zapomniany test nie zostawi już w fundamencie fałszywego „test” bez sygnału; testy uruchamiające wszystkie sprawdzenia produktu na tym padają.
- Jedno uruchomienie jest wyjęte spod tego: to, które agent robi zaraz po zapisaniu wpisu fundamentu. Przekazuje przełącznik pomijający to jedno zgłoszenie, bo test reguły zapisanej w tej samej zmianie może jeszcze nie istnieć. Instrukcja zapisu wpisu każe teraz agentowi go przekazać. Agent, który o nim zapomni, zobaczy błąd i może cofnąć regułę na „pilnuje przegląd”, co jest kierunkiem bezpiecznym.
- Fundament the-way sam mówi to teraz jako własną regułę, a jedyny test, który już uruchamia sprawdzenie na własnym fundamencie the-way, ją wymienia. Na dzisiejszym fundamencie sprawdzenie przechodzi: wszystkie 19 reguł „pilnuje test” ma test.

### Pod spodem

Sprawdzenie korzysta ze sposobu, w jaki skrypt już znajduje linie, w których testy nazywają regułę (linie komentarza w plikach śledzonych innych niż Markdown), więc nie doszedł drugi sposób listowania plików. Dwie poprawki po jednej klauzuli utrzymują zgodność przeglądu repozytorium i instrukcji instalacji z nowym zachowaniem.

## Do rozstrzygnięcia

1. Zadanie zostawiło cyklowi kilka wyborów, a inna odpowiedź zmieniłaby to, co spotkasz Ty albo agent. Przełącznik nazywa się `--skip-test-citations`. Droga, którą zadanie odrzuciło (zdanie w skillu planu, które zamienia „przegląd” na „test” w późniejszym kawałku), jest zapisana wśród dróg, których decyzja o metodzie nie wybrała. Dwa zdania dodano poza listą zadania, jedno w przeglądzie repozytorium i jedno w instrukcji instalacji, żeby oba nadal prawdziwie opisywały skrypt. Przyjąć?
2. Nowa reguła, że każdą regułę „test” wymienia jakiś test, wynika z decyzji o sprawdzeniu, a także z decyzji o metodzie; wyprowadzenie zadanie zostawiło cyklowi. Jedyny test, który uruchamia sprawdzenie na fundamencie the-way, niesie teraz wzmiankę o nowej regule (zmieniony test niezmiennika), a polecenie sprawdzania zyskuje opcjonalny przełącznik, zachowując ścieżkę, argument i kody wyjścia (zmieniona powierzchnia). Przyjąć?

## Koszt

Około 30 minut czasu pracy w 11 etapach, plus oczekiwanie na dwa pełne przebiegi testów: 19,5 mln tokenów (14,4 mln na claude-sonnet-5-5, 5,1 mln na claude-opus-5-5), głównie wejście z pamięci podręcznej. Rundy przeglądu: 1 dla całej zmiany (przeszła, z 3 drobnymi uwagami poprawionymi jedną poprawką) i 1 dla tej poprawki (przeszła). Tabela etapów jest w zatwierdzonym zapisie.

## Jak scalić

Użyj scalenia, które zachowuje commity, bo link do zapisu przeżywa tylko wtedy. Gałąź ma 3 commity ponad gałęzią docelową, a gałąź docelowa się nie ruszyła.

</details>

## Technical changes

The change makes a rule's method judged on the finished change, adds the check that keeps it honest, and writes the three foundation entries the task carried.

- Commit `9d499d0`: the foundation entries. `foundations/decisions.md`: WAY-61 gains the sentence "The method is held on the finished change: an invariant whose test a later slice of the same change writes may read `test` from its writing on.", with its complies example, violates example and rationale made to agree, and the rejected way of question 1 in its *Rejected*; new WAY-321 for the check and its switch. `foundations/invariants.md`: new invariant `test-method-citation`.
- Commit `e3fcc20`: the check. `elements/common/foundation_check.py` gains `check_test_citations` and the switch `--skip-test-citations` (an unknown switch or two roots print the usage line and exit 2); `elements/common/test_foundation_check.py` gains eight tests and the citing line of the new invariant in `test_the_way_foundation_passes`; `elements/common/way_of_working.md` step 4.3 passes the switch; `elements/invariants/template.md` says the new rule instead of "An invariant whose test is not written yet reads `review` (WAY-61).". One clause each in `README.md` and `installation/README.md`.
- Commit `7c3161a`: the fix of the review's three Minor findings — the rationale of WAY-61 reworded ("may read `test`"), the new invariant also derives from WAY-61 (and WAY-61's *Verification* names it), one docstring line shortened.

The part map is unchanged: `foundation-check-command` keeps its path, its argument and its exit codes; the switch is optional. The three places the task's question 4 keeps unchanged are unchanged.

## Checks

- The gate, `python -B gate/run_tests.py`, on the final tree (head `7c3161a`, which the return step did not change): exit 0, 834 tests in 9 directories, every directory passed. On the base (`46bba35`): exit 0, 826 tests; no check failed on the base. No check failed or did not run.
- The new check, the author's failing run: the eight new tests before the code, `python -B gate/run_tests.py elements/common`, exit 1 (8 failures, on assertions); after the script and before the entries, exit 1 with the one failure `test_the_way_foundation_passes` (`test-method-citation names no invariant`); passing: exit 0, 117 tests. With the citing line of the new invariant removed for a moment, the same test failed on the real foundation (exit 1, the error at the *Method* line of the invariant). The reviewer repeated this in a scratch copy with another invariant's citing line deleted: exit 1 without the switch, exit 0 with it.
- Own-work check: the author named the requirement "reports on tracked non-Markdown files only, like the existing citation check" and covered it with tests for a Markdown citation, an untracked file and a tracked file; a further test shows the switch skips no other error. Left untested by the author: a citing line of the form with a fingerprint is counted through the existing pattern, not by a separate test. The fix: `foundation_check.py` exit 0 after it.
- `python -B elements/common/foundation_check.py`: exit 0, 0 errors (also with `--skip-test-citations .`).
- No user interface is touched; no screenshot applies.
- Reconciliation with the target branch: `origin/foundations` is still the base commit, so no merge and no review of a merge. The return step changed nothing, so it has no review of its own.
- Count of merges since the last review of the foundation: `python -B task-cycle/review_reminder.py origin/foundations`: 15 merges, threshold 30, `reminder: no`.
- Form check of this description: pending.
- Check of private paths on this description: pending.
- Checks on the copy of the record: pending.

## Foundation entries

- WAY-61 (edited, `row 1`): an invariant's method is judged on the finished change, so an invariant whose test a later slice of the same change writes may read `test` from the moment it is written.
- WAY-321 (new, `row 2`): the foundation check reports every invariant that reads `test` and that no test cites, in every run, and only the run made right after writing an entry skips that report with a switch.
- Invariant `test-method-citation` (new, `row 3`, method `test`; derives from WAY-61 and WAY-321, part `every`): every invariant whose method is `test` is cited by a comment line `invariant: <its identifier>` in a file git tracks other than a Markdown file. Its test is `test_the_way_foundation_passes`, an existing invariant test that now carries the citation (an invariant test altered, WAY-03); no surface of the part map is altered and no *Violated* mark is set or cleared. WAY-321 names the invariant in its *Verification*.

No entry is marked `the cycle's`.

## Minor findings

none

## Findings outside the task's scope

None of a reviewer. The return step reported two open points, left unchanged, for you to make tasks of if you want them:

1. WAY-61's *Scope* does not name `task-cycle`, though its new sentence speaks of a later slice of a change; a change to the cycle's planning text finds WAY-61 only through the search of the foundation.
2. On a planned route, a slice that writes a `test` invariant before the slice that writes its test would fail the focused check `test_the_way_foundation_passes` between the two slices (`task-cycle/plan/SKILL.md:169-172` makes the slice run the tests of the invariants it reaches). The task records this as context and carries no item for it; the one-author route of this task has no such moment.

## Course of the cycle

- **Task and sources:** an independent task (`Status: ready for cycle`): let a product's rule read `test` while its test is written later in the same change, and have an automatic check keep it; sources: the task's questions 1–4 and rows 1–3, the foundation at `46bba35`.
- **Process pin:** this checkout, the base commit `46bba35`; the cycle did not move the pin.
- **Spec:** none — the task leaves no open design choice; the name of the switch, the place of the rejected way and the derivation of the new invariant were how-to choices of the author.
- **Route:** one author without a plan (one agent could hold it); class `same` as the orchestrator, because the change touches three parts and rewords an approved decision; resumed for the fix and the return step.
- **Plan:** none.
- **Choices:** 6 other choices of the cycle, in the author's report and the record: the switch name; the rejected way kept in *Rejected* of WAY-61; the check as a decision of its own (WAY-321); the invariant deriving from both decisions after the fix; the error placed at the *Method* line of the invariant; the two README clauses.
- **Blocking findings left:** none.
- **Record:** pending
