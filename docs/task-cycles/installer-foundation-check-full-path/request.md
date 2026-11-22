**State: draft** — the code is finished and reviewed; the record of the cycle and the result of the CI run on the last head, which is the final gate, are still being added.

## What you will see

The text that the installer writes into the agent instructions of every product now names the script that checks the foundation by its full path in one more sentence, the way the two sentences next to it already did. Before, that sentence gave the bare name of the script, and the check of instruction files took the name for a path to a file that does not exist and reported a warning. Now it reports none on that file. A product that moves to the new version of the process therefore starts with no warning on its main agent instructions, and the review of its first change no longer blocks on a warning that nobody in the product could fix, since the installer would overwrite a manual correction at the next move.

A new test builds a product by a full installation, before any skill has run in it, runs the product's own check of instruction files on it and fails if that check reports a warning or an error on the main agent instructions. It also fails if the installation stops leaving the working directory of the skills in the product's ignore file, which is what keeps the warning about that directory away. The rule is written down as a rule of the foundation, so that a later change to the text cannot bring a warning back unnoticed.

### Underneath

The change to the code is one sentence of the text the installer writes and the line of the test that expects the same text; the rest is one rule of the foundation, the one test that holds it, a link from the decision it derives from, and a line in the installer's description of its tests.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. Two choices of the cycle beyond the task's words, both for the new rule and its test. The test also fails on an error of the check on the main agent instructions, not only on a warning, since an error stops a product's one command and is the same break in a worse form; the sentence of the rule still says only "warning", so the test is a little stricter than its sentence. And the rule covers only the main agent instructions that the installation created: a product that already had its own text in that file keeps it, and nothing the installer does can keep that text free of warnings. The other ways were to name errors in the rule, which goes beyond what the task's settlement says and might need your answer, and to leave the rule's reach unsaid, which a reader could take for a promise the installer cannot keep.
2. The decision that makes a warning of the check of instruction files a blocking finding now names the new rule in the list of its checks, and introduces its pair of examples as covering what no rule and no test holds. Its binding sentences are unchanged. The reviewer of the whole change held that the foundation requires this link whenever a rule derives from a decision, and it fixed it in this request; the other way, leaving the decision as it was, would have left whoever reads it unaware that a test now holds part of it.
3. Changed tests that hold a rule, in plain words: the existing test of the installer's whole block of agent instructions now expects the new sentence, and so does nothing else; and the new test holds the new rule. The check of the foundation lists no rule whose sentence was reworded while its test stayed as it was.

## Cost

The cycle's working time so far was 44 minutes, 29 of them waiting for tools. One author on Claude Sonnet 5.5 made the change, the fix of one blocking finding and two Minor findings, and the return step; one reviewer on Claude Opus 5.5, as you asked, reviewed the whole change, which failed with one blocking finding, and then the fix, which passed; a fresh reviewer on Claude Opus 5.5 reviewed the return step, which passed. Tokens in all: 24.1 million (15.2 million on Claude Sonnet 5.5, 8.9 million on Claude Opus 5.5). Table of stages: https://github.com/mariusznazar/the-way/tree/RECORDSHA/docs/task-cycles/installer-foundation-check-full-path/stages.md.

## How to merge

Merge with a merge commit, not a squash or a rebase, so that the link to the record of the cycle, which points at one commit by its identifier, stays reachable.

<details>
<summary>Po polsku</summary>

**Stan: wersja robocza** — kod jest gotowy i sprawdzony; zapis cyklu i wynik przebiegu CI na ostatniej głowie, który jest końcową bramką, są jeszcze dopisywane.

## Co zobaczysz

Tekst, który instalator wpisuje do instrukcji agentów każdego produktu, w jeszcze jednym zdaniu podaje teraz skrypt sprawdzający fundament pełną ścieżką, tak jak robiły to już dwa sąsiednie zdania. Wcześniej to zdanie podawało samą nazwę skryptu, a sprawdzarka plików instrukcji brała nazwę za ścieżkę do pliku, którego nie ma, i zgłaszała ostrzeżenie. Teraz na tym pliku nie zgłasza żadnego. Produkt, który przechodzi na nową wersję procesu, zaczyna więc bez ostrzeżenia na głównych instrukcjach agentów, a przegląd jego pierwszej zmiany nie blokuje się na ostrzeżeniu, którego nikt w produkcie nie mógł naprawić, bo instalator nadpisałby ręczną poprawkę przy następnym przepięciu.

Nowy test buduje produkt pełną instalacją, zanim uruchomił się w nim jakikolwiek skill, puszcza na nim własną sprawdzarkę plików instrukcji i kończy się porażką, gdy sprawdzarka zgłosi ostrzeżenie albo błąd na głównych instrukcjach agentów. Kończy się też porażką, gdy instalacja przestanie zostawiać w pliku ignorowanych katalog roboczy skilli, który trzyma z daleka ostrzeżenie o tym katalogu. Reguła jest zapisana jako reguła fundamentu, żeby późniejsza zmiana tekstu nie przywróciła ostrzeżenia po cichu.

### Pod spodem

Zmiana w kodzie to jedno zdanie tekstu, który zapisuje instalator, i linia testu oczekująca tego samego tekstu; reszta to jedna reguła fundamentu, jeden test, który ją trzyma, odsyłacz z decyzji, z której reguła wynika, i linia w opisie testów instalatora.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Do poprawy albo przepuszczenia

brak

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, napisz którą.

1. Dwa wybory cyklu poza słowami zadania, oba dla nowej reguły i jej testu. Test kończy się porażką także na błędzie sprawdzarki na głównych instrukcjach agentów, nie tylko na ostrzeżeniu, bo błąd zatrzymuje jedno polecenie produktu i jest tym samym złamaniem w gorszej postaci; zdanie reguły mówi dalej tylko „ostrzeżenie”, więc test jest trochę ostrzejszy od swojego zdania. Reguła obejmuje też tylko te główne instrukcje agentów, które utworzyła instalacja: produkt, który miał już w tym pliku własny tekst, go zachowuje i nic, co robi instalator, nie utrzyma tego tekstu wolnego od ostrzeżeń. Inne drogi to nazwanie błędów w regule, co wykracza poza ustalenie zadania i mogłoby wymagać Twojej odpowiedzi, oraz zostawienie zasięgu reguły niewypowiedzianego, co czytelnik mógłby wziąć za obietnicę, której instalator nie utrzyma.
2. Decyzja, która robi z ostrzeżenia sprawdzarki plików instrukcji uwagę blokującą, nazywa teraz nową regułę na liście swoich sprawdzeń, a swoją parę przykładów przedstawia jako obejmującą to, czego nie trzyma żadna reguła ani test. Jej zdania wiążące się nie zmieniły. Recenzent całej zmiany uznał, że fundament wymaga tego odsyłacza, ilekroć reguła wynika z decyzji, i poprawiono to w tym zgłoszeniu; inna droga, zostawienie decyzji bez zmiany, nie dałaby czytającemu ją wiedzy, że część decyzji trzyma teraz test.
3. Zmienione testy trzymające regułę, prostymi słowami: istniejący test całego bloku instrukcji agentów instalatora oczekuje teraz nowego zdania i nic poza tym; a nowy test trzyma nową regułę. Sprawdzenie fundamentu nie wypisuje żadnej reguły, której zdanie przeformułowano, a test został bez zmian.

## Koszt

Dotychczasowy czas pracy cyklu to 44 minuty, w tym 29 minut czekania na narzędzia. Jeden autor na Claude Sonnet 5.5 zrobił zmianę, poprawkę jednej uwagi blokującej i dwóch uwag Minor oraz krok zwrotny; jeden recenzent na Claude Opus 5.5, tak jak prosiłeś, przejrzał całą zmianę, która nie przeszła z jedną uwagą blokującą, a potem poprawkę, która przeszła; świeży recenzent na Claude Opus 5.5 przejrzał krok zwrotny, który przeszedł. Tokenów łącznie: 24,1 miliona (15,2 miliona na Claude Sonnet 5.5, 8,9 miliona na Claude Opus 5.5). Tabela etapów: https://github.com/mariusznazar/the-way/tree/RECORDSHA/docs/task-cycles/installer-foundation-check-full-path/stages.md.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase'em, żeby link do zapisu cyklu, wskazujący jeden commit po identyfikatorze, pozostał osiągalny.

</details>

## Technical changes

- `1c222ce2` — the sentence of the block that `installation/install.py` (`product_guidance`) writes into the product's `AGENTS.md`, which begins "Until the part map has its first parts", now names `{SUBMODULE}/elements/common/foundation_check.py` in backticks, as the two sentences beside it name it; the expected `BLOCK` of `installation/test_install.py` follows it. The new test `InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning` builds a product by a full `--apply` installation (as the other tests of that class do), asserts that the product has no `.runs/`, runs the product's own `.the-way/instruction-files/check_instructions.py` on its root and asserts that the last line counts the findings and that no `WARN` line stands on `AGENTS.md`; it cites `invariant: installation-agents-md-warnings`. The new invariant stands in `foundations/invariants.md`, after `installation-paths-through-links`.
- `674c93fe` — fix 1 of the review of the whole change: WAY-418's *Verification* gains `invariants: installation-agents-md-warnings.` and its pair of examples is introduced as covering the part no invariant and no test holds; the test also matches `ERROR` lines on `AGENTS.md`; the invariant's sentence ends "that the run created".
- `325af473` — the return step: the list of what the installer's tests hold in `installation/README.md` ("Check the installer") names the new test.
- Not changed, as the task's question 1 binds: the sentence about `.runs/`; the full installation leaves `.runs/` in the product's `.gitignore`, so the check gives that path only a note.

## Checks

1. Final gate: the CI run on this request's last head, which is the final gate; the cycle ran no full gate on its own system, since CI runs on a request into `foundations`. Its result: pending — to be written once the run on the last head ends.
2. Failing before the change: none. The base `fad52af3` is a merge commit with the tree of its second parent (`ca36198c6e50d6faf0c9930c7c985ef20b1fd42c` both), so no gate ran on the base; the list was taken from the *Checks* of the merged request https://github.com/mariusznazar/the-way/pull/157 (the CI run https://github.com/mariusznazar/the-way/actions/runs/45028155620 on `d48d080d`, first attempt: `tests` and `tests-windows` passed) and from `docs/task-cycles/poprawki-z-przegladu-cykli-22-11/cycle.md` at `ede55664`.
3. The author's focused checks: the new test fails before the fix of the sentence (exit 1, `WARN  dead-path AGENTS.md:10 \`foundation_check.py\` does not exist`) and passes after; `python -B gate/run_tests.py installation` exit 0 (74 tests, twice: after the first commit and after the fix); `python -B gate/run_tests.py instruction-files` exit 0 (122 tests, 5 skipped for POSIX); `python -B elements/common/foundation_check.py` exit 0, `0 errors`, with no `listed:` line; `python -B instruction-files/check_instructions.py .` on the head: `0 error, 0 warn, 5 info`; Ruff format and lint of the two Python files exit 0. The orchestrator ran the foundation check on the finished change: exit 0, `0 errors`.
4. The reviewers' own runs: the review of the whole change ran mutations of the new test against the head: the old sentence (red, exit 1), a full path to a file the commit lacks (red), an installation that leaves `.runs/` out of the ignore file (red, `.runs/` warning), an `@` import with a full stop in the block (passed the first version of the test, exit 0 — the Minor finding the fix took); the review of the fix repeated the three and the last turns the test red (exit 1); a full installation into an empty repository gave `0 error, 0 warn, 3 info` over the whole product; the size test passed on the base and the head. The review of the return step ran the foundation check, the instruction check and the two tests that read the README, exit 0 each.
5. Own-work checks: the author named the requirement most likely not met, question 1 of the task (the warning on `.runs/` must go in the product after a full installation), and checked it by a mutation of `ignore_change` that leaves `.runs/` out of the ignore file: the new test failed with `WARN  dead-path AGENTS.md:8 \`.runs/\` does not exist`; the mutation was restored before the commit.
6. Walk through the running product (WAY-406): the author judged and said in its report that the change is no change of behaviour a user sees in a running product — it alters the text of one block that the installer writes, no screen, answer or command — so no walk and no case marked unchecked stand for it; the foundation also settles no way to run the-way as a running product. The new test is itself a full installation followed by the product's own check, which the review of the whole change repeated by hand into an empty repository (`0 error, 0 warn, 3 info` over the whole product).
7. Not run: the full gate on the cycle's own system (CI is the final gate); `python -B gate/run_tests.py installation` was run by the author after the first commit and after the fix, not by a reviewer (the reviewers ran the five and the two tests the change reaches) and not after the return step's one-line Markdown change.
8. The review of the whole change read 5 decisions of its index whole (WAY-418, WAY-16, WAY-392, WAY-393, WAY-394), with WAY-12, WAY-17 and WAY-30 whole as reaches beyond it, and the index of its whole selection (34 decisions in full, 27 by heading); it read WAY-395 in its first lines only, its binding fields standing in the testing guidelines read whole, and did not open WAY-385, whose size rule it checked by the size test; it named none of the unread as bearing on the change. It read the guideline for the kind of script `install.py` is (repository changer) whole, which the author had not opened for the reason that the change edits one literal.
9. The form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/installer-foundation-check-full-path/request.md --task .runs/task-cycles/installer-foundation-check-full-path/task.md` and `python -B task-cycle/private_paths_check.py .runs/task-cycles/installer-foundation-check-full-path/request.md` — last runs to be written when the description is final.
10. Working copies left: none; directories of earlier tasks kept: none.

## Foundation entries

- `installation-agents-md-warnings` — `row 2`, new, at the end of the entries of the part `installation` in `foundations/invariants.md`; Method `test`, Derives from WAY-418, Part `installation · instruction-files`, Violated `no`: in a product made by a full run of the installation command, before any skill of the-way has run in it, the script that checks instruction files, run on the product's root, reports no warning on the root `AGENTS.md` that the run created.
- WAY-418 — `the cycle's`, *Verification* edited in place, no binding sentence changed: it names `installation-agents-md-warnings` after `invariants:` and introduces its pair of examples as covering the part no invariant and no test holds; the pair stands word for word as before.
- Row 1 of *Settlements to record* (the sentence of the block) is no entry: it went to `product_guidance` in `installation/install.py` and to the `BLOCK` constant of the test that pins the text.
- Invariant tests changed (WAY-03): `InstallTest.test_preview_apply_rerun_and_preserve_foundation`, which cites `invariant: installation-claude-guidance`, expects the changed block (the `BLOCK` constant); `InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`, new, cites `invariant: installation-agents-md-warnings`.

## Minor findings

- Review of the fix, Minor 4, within the task, not fixed: `installation/test_install.py:453-458` against `foundations/invariants.md:336` — "The sentence of `installation-agents-md-warnings` says the checker "reports no warning". The test that cites it now also fails on a line `ERROR … AGENTS.md:`. So a block that draws an error and no warning makes the test, and through it the invariant's result, read `fail` (WAY-08: "The status of an invariant with a test comes from running that test"), although its sentence holds." The reviewer: "The consequence is small, and I do not grade it higher." It left to the cycle to name errors in the sentence (which widens row 2 and may need the human) or to accept a test stricter than its sentence; the cycle left it, and judged that the product's user and the person working with the process will not feel it, since the extra assertion fails only on a real defect.
- Review of the return step, Minor, within the task, not fixed: `installation/README.md:287-288` — the new line says the root `AGENTS.md` draws "no warning" from the instruction check while the test also refuses errors; "the same gap as the known Minor on the invariant, now in a second place, so whoever fixes the invariant's sentence should fix this line too."

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task document in the author's backlog, `Status: ready for cycle`, relation independent; the target branch `foundations` at `fad52af3`; the task's two settlement rows and two answered questions as accepted on 2026-11-22.
- **Process pin:** none — the-way is the top-level repository, the process is the checkout's own.
- **Spec:** none — the task settles the wording of the sentence, the rule and the way the test builds its product; no open design choice, no reserved choice.
- **Route:** one author without a plan, on the class of the orchestrator (`same`), because the author writes a foundation entry and a test that builds a product by a full installation and runs another script on it, which takes design decisions of its own; the review of the whole change failed once with one blocking finding (WAY-418's *Verification* did not name the new rule; marked as contradicting WAY-12) and two Minor findings within the task, fixed in one fix that passed its review.
- **Plan:** none.
- **Choices:** 2 other choices of the orchestrator in the questions table (the reviewers' class `opus`, as you asked; leaving WAY-418 unchanged, later withdrawn by the review's finding), and the author's recorded choices in its reports (the record, RECORDSHA).
- **Blocking findings left:** none.
- **Record:** https://github.com/mariusznazar/the-way/tree/RECORDSHA/docs/task-cycles/installer-foundation-check-full-path
