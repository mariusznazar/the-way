**State: ready** — corrected for your answers to two items and to one question of the cycle; nothing below waits for your answer

## What you will see

Every pull request into `foundations` now gets its tests run automatically on GitHub, on Linux, with the one command of tests. Until now only a person or the agent of a cycle ran them, on a Windows machine, and five tests that need Linux (links, loops of links, a named pipe) never ran anywhere. Three tests of the instruction-file checker failed on Linux; they were faults of the tests, not of the checker, and are fixed. The run of this request on its first head finished and passed, and it is the proof that those five tests now run instead of being skipped.

The agent that leads a cycle now waits for that run on its own request, treats a red run like a failed final test run (a fix and a review of it), and writes the result into the request's description, so that a request reaches you with the result of the run. This holds for corrections after your remarks too. One exception came with the new rules of the target branch and is written here: a red run caused by a test outside the task's scope that passes when run again does not stop the cycle; the request names that test and the task that fixes it. A request the cycle leaves blocked for unfinished code is not waited for.

For products that use the-way: the block of instructions the installer writes into a product now says that the one command also runs the instruction-file checker (a script error stops the tests, a warning does not), that it runs in CI on every merge request, and that its result is a check the repository requires with the owner allowed to bypass it. A short description tells a product's owner what its CI file must hold: the one command on every merge request, the-way at the commit the product pinned and never the latest, the history the foundation check needs, and the required check. The installer puts no CI file into a product; the product writes its own. The skill that proposes the coding guidelines now also proposes turning on the repository service's alerts about vulnerable libraries (on GitHub, Dependabot alerts), which is the signal for a library the product already uses; a human turns them on.

Since your answers: you set the branch rule on GitHub, and the cycle read it back (it exists, requires the check `tests`, and the repository's admin role may bypass it) and wrote the reading down as a fact in the foundation, so the decision that rests on the rule has no open gap. You also allowed two dependencies the change brought in, for the installer part on the instruction-file checker's part and for the part that holds the CI file on the part that holds the Python version file, and the cycle wrote them in the map of parts. The task's branch was merged twice with newer commits of `foundations`, and both merges were reviewed.

### Underneath

The rules about these things stand in the foundation (the decisions on the one command of tests, on the audit of dependencies and on the cycle's final test run), with four facts about GitHub: three about its own behaviour and one reading of this repository's branch rule.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. A request that the cycle leaves blocked for unfinished code (a review finding that remained, a slice that failed twice, a technology choice only you make) is not waited for: its code is not finished, so a red run is expected and the result stands on the request's page for you to read. A request that waits only for your actions is waited for, because you need the run to have happened; so is this one, now that its blocking item is settled. The other way, waiting for every request, would stop the cycle on a failure it already knows.
2. The block the installer writes now also tells an agent what to do in a product that has not yet written its CI file: run the one command on its own, as the block already says for the two checks. The task asked only for the sentence that CI runs the command; without the fallback the block would say something false in such a product.
3. The description for products also says that the CI job needs Python at the version the-way declares, which the task did not list; without it the job fails in every product that pins the-way.
4. The rule that a red CI run is a failed final test run has one exception, which I wrote in the four places that state it so that they agree with the target branch's rule about flaky tests: a test outside the task's scope that fails and passes when run again does not stop the cycle, and the request names it with the task that fixes it. Without it, a flaky test that runs only in CI would have to be fixed outside the task or rerun until green, which the rules forbid.
5. Foundation entries you did not see at the task, written by the cycle: the decision on the one command of tests now binds what the installer promises a product and rests on the pin of the-way and on the reading of the branch rule; the decision that lists what the repository holds names the CI file among the files of the instructions part; the cycle's final-test-run decision now says that the wait for CI covers corrections, does not cover requests blocked for unfinished code, and leaves a flaky test outside the task's scope to the rule for such tests; the part map gives the CI configuration folder to the instructions part, lets the installer part depend on the instruction-file checker's part, and lets the part that holds the CI file depend on the part that holds the Python version file (the last two are your answers); and four facts about GitHub (the alerts of vulnerable libraries, the required status check, the bypass list of a branch rule, and the reading of this repository's branch rule on 2026-11-15, which shows the rule's name, its target, the required check `tests` and its bypass). (Foundation entries)
6. The cause of the corrections: the first answered your answer to an item of this request (closing the open gap on the branch rule), and the cycle judged that the task did not require what the answer asked to change, since the foundation allowed the gap while the rule did not exist and the task asked for no reading; the second answered your answer to the blocking item and to one question of the cycle (allowing the two dependencies), and the cycle judged that the task and the foundation required what they asked to change, since the task itself asked for the instruction-file checker to be named in the installer's text and the map of parts must allow every dependency the code holds.

## Cost

About 3 hours 10 minutes of working time across the two sessions (of which about 1 hour 47 minutes was waiting for tools), 178.8 million tokens, almost all of them cached input (133.7 million on Sonnet, 45.1 million on Opus). The first cycle: one review of the whole change that failed on three blocking findings and four minor ones, one fix, one review of the fix that passed, a return step with its review, and a full test run (7 minutes). The corrections: two merges with the target branch, each reviewed (the first failed on two blocking findings, one fixed and one settled by your answer), the fact written for your first answer with a review that passed, the two dependencies you allowed with their reviews that passed, the return step run twice (the first time it asked one question, which you answered), and two more full test runs, the last on the final code (14 minutes, with two other runs at the same time). The table of stages is in the committed record, linked at the end.

Directories of earlier tasks still stand because the cleaning script could not tell they were no longer needed; nothing in this request waits for them and you may remove them by hand (their names are under Checks).

## How to merge

Merge it with a merge that keeps the commits, since the link to the record survives only then. Squash or rebase would lose that link.

<details>
<summary>Po polsku</summary>

**State: ready** — poprawiona dla Twoich odpowiedzi do dwóch pozycji i do jednego pytania cyklu; nic poniżej nie czeka na Twoją odpowiedź

## Co zobaczysz

Każda prośba o scalenie do `foundations` dostaje teraz automatycznie uruchomione testy na GitHubie, na Linuksie, jednym poleceniem testów. Dotąd uruchamiał je tylko człowiek albo agent cyklu na maszynie z Windowsem, a pięć testów wymagających Linuksa (dowiązania, pętle dowiązań, nazwany potok) nie biegło nigdzie. Trzy testy sprawdzania plików instrukcji padały na Linuksie; były to błędy testów, nie skryptu, i są poprawione. Przebieg na pierwszym commicie tej prośby zakończył się powodzeniem i jest dowodem, że tych pięć testów teraz biegnie zamiast być pominiętych.

Agent prowadzący cykl czeka teraz na ten przebieg na własnej prośbie, czerwony traktuje jak nieudany końcowy przebieg testów (poprawka i jej recenzja) i wpisuje wynik do opisu, więc prośba trafia do Ciebie z wynikiem przebiegu. Dotyczy to też poprawek po Twoich uwagach. Jeden wyjątek przyszedł z nowymi regułami gałęzi docelowej i jest tu zapisany: czerwony przebieg spowodowany testem spoza zakresu zadania, który po powtórzeniu przechodzi, nie zatrzymuje cyklu; prośba wymienia ten test i zadanie, które go naprawia. Na prośbę, którą cykl zostawia zablokowaną z niedokończonym kodem, nie czeka.

Dla produktów używających the way: blok instrukcji wpisywany przez instalator do produktu mówi teraz, że jedno polecenie uruchamia też sprawdzanie plików instrukcji (błąd skryptu zatrzymuje testy, ostrzeżenie nie), że biegnie w CI na każdej prośbie o scalenie i że jego wynik jest sprawdzeniem wymaganym przez repozytorium z prawem obejścia dla właściciela. Krótki opis mówi właścicielowi produktu, co ma zawierać jego plik CI: jedno polecenie na każdej prośbie, the way na commicie przypiętym przez produkt (nigdy najnowszym), historię potrzebną do sprawdzania fundamentu i wymagane sprawdzenie. Instalator nie wkłada produktowi pliku CI; produkt pisze go sam. Skill proponujący wytyczne kodowania proponuje też włączenie alertów serwisu o lukach w bibliotekach (na GitHubie alerty Dependabota), które są sygnałem o bibliotece już używanej; włącza je człowiek.

Od Twoich odpowiedzi: ustawiłeś regułę gałęzi na GitHubie, a cykl odczytał ją z powrotem (istnieje, wymaga sprawdzenia `tests`, a rola administratora repozytorium może ją obejść) i zapisał odczyt jako fakt w fundamencie, więc decyzja, która na tej regule się opiera, nie ma otwartej luki. Dopuściłeś też dwie zależności, które przyniosła ta zmiana: część instalatora od części sprawdzającej pliki instrukcji oraz część z plikiem CI od części z plikiem wersji Pythona, a cykl zapisał je w mapie części. Gałąź zadania została dwukrotnie scalona z nowszymi commitami `foundations` i oba scalenia przeszły recenzję.

### Pod spodem

Reguły o tych sprawach stoją w fundamencie (decyzje o jednym poleceniu testów, o audycie zależności i o końcowym przebiegu testów w cyklu), razem z czterema faktami o GitHubie: trzema o jego własnym zachowaniu i jednym odczytem reguły gałęzi tego repozytorium.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Popraw albo przepuść

none

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

1. Na prośbę, którą cykl zostawia zablokowaną z niedokończonym kodem (uwaga recenzji, która została, plasterek, który dwa razy zawiódł, wybór technologii, który należy do Ciebie), nie czeka się: kod nie jest skończony, więc czerwony przebieg jest oczekiwany, a wynik stoi na stronie prośby do Twojego odczytu. Na prośbę czekającą tylko na Twoje czynności się czeka, bo potrzebujesz, żeby przebieg się odbył; na tę też, skoro pozycja blokująca jest rozstrzygnięta. Drugi sposób, czekanie na każdą prośbę, zatrzymałby cykl na awarii, którą już zna.
2. Blok pisany przez instalator mówi teraz też agentowi, co robić w produkcie, który nie napisał jeszcze pliku CI: uruchomić jedno polecenie samodzielnie, jak blok już mówi przy dwóch sprawdzeniach. Zadanie prosiło tylko o zdanie, że CI uruchamia polecenie; bez zastępstwa blok mówiłby w takim produkcie coś nieprawdziwego.
3. Opis dla produktów mówi też, że zadanie CI potrzebuje Pythona w wersji, którą deklaruje the way, czego zadanie nie wymieniało; bez tego zadanie CI pada w każdym produkcie przypinającym the way.
4. Reguła, że czerwony przebieg CI jest nieudanym końcowym przebiegiem testów, ma jeden wyjątek, który zapisałem w czterech miejscach, które ją podają, żeby zgadzały się z regułą gałęzi docelowej o niestabilnych testach: test spoza zakresu zadania, który pada i po powtórzeniu przechodzi, nie zatrzymuje cyklu, a prośba wymienia go razem z zadaniem, które go naprawia. Bez tego niestabilny test, który biegnie tylko w CI, trzeba by naprawiać poza zadaniem albo powtarzać do skutku, czego reguły zabraniają.
5. Wpisy fundamentu, których nie widziałeś przy zadaniu, zapisane przez cykl: decyzja o jednym poleceniu testów wiąże teraz to, co instalator obiecuje produktowi, i opiera się na przypięciu the way oraz na odczycie reguły gałęzi; decyzja o tym, co zawiera repozytorium, wymienia plik CI wśród plików części instrukcji; decyzja o końcowym przebiegu testów mówi teraz, że czekanie na CI obejmuje poprawki, nie obejmuje próśb zablokowanych z niedokończonym kodem i zostawia niestabilny test spoza zakresu zadania regule dla takich testów; mapa części daje katalog konfiguracji CI części instrukcji, pozwala części instalatora zależeć od części sprawdzającej pliki instrukcji i pozwala części z plikiem CI zależeć od części z plikiem wersji Pythona (dwa ostatnie to Twoje odpowiedzi); oraz cztery fakty o GitHubie (alerty o lukach w bibliotekach, wymagane sprawdzenie stanu, lista obejścia reguły gałęzi oraz odczyt reguły gałęzi tego repozytorium z 2026-11-15, który pokazuje nazwę reguły, jej cel, wymagane sprawdzenie `tests` i jej obejście). (Wpisy fundamentu)
6. Przyczyna poprawek: pierwsza odpowiedziała na Twoją odpowiedź do pozycji tej prośby (domknięcie otwartej luki w regule gałęzi), a cykl uznał, że zadanie nie wymagało tego, co odpowiedź kazała zmienić, bo fundament dopuszczał lukę, dopóki reguły nie było, a zadanie nie prosiło o odczyt; druga odpowiedziała na Twoją odpowiedź do pozycji blokującej i do jednego pytania cyklu (dopuszczenie dwóch zależności), a cykl uznał, że zadanie i fundament wymagały tego, co kazały zmienić, bo samo zadanie prosiło, żeby sprawdzanie plików instrukcji było nazwane w tekście instalatora, a mapa części musi dopuszczać każdą zależność, którą ma kod.

## Koszt

Około 3 godzin 10 minut pracy w dwóch sesjach (w tym około 1 godziny 47 minut czekania na narzędzia), 178,8 mln tokenów, prawie wszystkie jako wejście z pamięci podręcznej (133,7 mln na Sonnet, 45,1 mln na Opus). Pierwszy cykl: jedna recenzja całości, która nie przeszła z trzema uwagami blokującymi i czterema drobnymi, jedna poprawka, jedna recenzja poprawki, która przeszła, krok powrotu z recenzją i pełny przebieg testów (7 minut). Poprawki: dwa scalenia z gałęzią docelową, każde zrecenzowane (pierwsze nie przeszło z dwiema uwagami blokującymi, jedną naprawioną i jedną rozstrzygniętą Twoją odpowiedzią), fakt zapisany dla Twojej pierwszej odpowiedzi z recenzją, która przeszła, dwie zależności, które dopuściłeś, z recenzjami, które przeszły, krok powrotu uruchomiony dwa razy (za pierwszym razem zadał jedno pytanie, na które odpowiedziałeś) oraz dwa kolejne pełne przebiegi testów, ostatni na ostatecznym kodzie (14 minut, przy dwóch innych przebiegach równolegle). Tabela etapów jest w zatwierdzonym rekordzie, z linkiem na końcu.

Katalogi wcześniejszych zadań nadal stoją, bo skrypt sprzątający nie mógł stwierdzić, że nie są już potrzebne; nic w tej prośbie na nie nie czeka i możesz je usunąć ręcznie (ich nazwy są w Sprawdzeniach).

## Jak scalić

Scal ją scaleniem zachowującym commity, bo link do rekordu przeżywa tylko wtedy. Squash albo rebase straciłby ten link.

</details>

## Technical changes

The change adds a CI workflow, makes the products' description and the installer's block say what is now true, widens three decisions of the foundation and adds four facts, and fixes three tests that failed on Linux. It does not touch the checker's own code (`instruction-files/check_instructions.py`), which was right on Linux. The commits of the first cycle, oldest first: `7217667`, `ff45403` (the description for products in `installation/README.md`; the installer's paragraph in `installation/install.py` with its two tests in `installation/test_install.py`); `80e9eca`, `7c301ce`, `ddcbfc2` (`instruction-files/test_check_instructions.py`: a Windows network path judged under a patched platform, the guard of the macOS shapes, one test split in two); `66121c8` (`.github/workflows/tests.yml`, the part map line, `agent-instructions/README.md`); `3410e33`, `345b6bd` (the decision log: WAY-16, WAY-206, WAY-160, WAY-09); `a5abe37` (`product-guidelines/coding/settle.md`, step 12 of `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`, `task-cycle/record_template.md`); `7d027c6` (root `README.md`); the fix of the review (`21777bd`: environment facts and the decisions; `827f716`: the installer's block, its tests, the README; `23f08e9`: `task-cycle/skill/SKILL.md`, `correction.md`, `blocked_finding.md`, `reserved_return.md`, the two templates, `agent-instructions/README.md`); the return step `b344595` (one clause in `installation/README.md`). The workflow runs `python -B gate/run_tests.py` on `ubuntu-latest` on `pull_request` into `foundations`, with the Python version of `.python-version`, the whole history and `origin/HEAD` set to `foundations` so that the foundation check compares with the fork point, read-only token, no secret, both actions pinned at commit SHAs; its job and workflow are named `tests`.

The corrections, oldest first: `3eacbc1` merges `origin/foundations` (`7f5c5a5`, 44 newer commits; two conflicts, `agent-instructions/README.md` with both paragraphs kept and `foundations/decisions.md`, the target's log divided into 28 sections taken whole and the four entries the branch had changed re-applied by hand); `7d00a48` adds the fact `foundations-branch-ruleset` to `foundations/environment_facts.md` and names it in the *Based on* of WAY-16 in place of the open `TODO`; `dcb1a19` makes the CI rule defer to WAY-261 for a flaky test outside the task's scope (WAY-160 and its *Verification*, step 12 of `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`, `agent-instructions/README.md`) and added an invariant that `2e83447` removed again on your answer, so the net change of the pair is the CI rule only; `2e83447` adds `instruction-files` to the *Depends on* of `installation` in `foundations/part_map.md`; `cde07dd` merges `origin/foundations` again (`9cbc6b2`, 39 newer commits, no conflict); `0e3cb2a` adds `repository` to the *Depends on* of `agent-instructions` in `foundations/part_map.md`.

## Checks

- The gate, `python -B task-cycle/gate_times.py --output .runs/task-cycles/ci-on-merge-requests/gate_times.md -- python -B gate/run_tests.py`, on the final tree `0e3cb2a`: exit 0, 1563 tests in 11 directories, every directory passed, 843 s, two other gate runs at the same time. Earlier runs: on `dcb1a19` exit 0, 1459 tests, 449 s; on the final tree of the first cycle `b344595` exit 0, 1376 tests, 423 s.
- Before the change, no test failed: the list was taken from the final gate of the earlier cycle (`docs/task-cycles/decision-log-second-round/cycle.md` of commit `cfd275c`, run 2: exit 0, 1374 tests in 10 directories, every directory passed), since the base is a merge whose tree equals that of its second parent.
- The foundation check, `python -B elements/common/foundation_check.py`, without `--skip-test-citations`, on `0e3cb2a`: exit 0, `0 errors`, no `listed:` line.
- CI on this request: pending, filled in with the run on the last head.
- The branch rule, read by the author of the correction and again by its reviewer on 2026-11-15, `gh api repos/mariusznazar/the-way/rulesets/27308872` (read only): the output matched the quoted output character for character.
- Linux: the author of the first cycle ran ten test directories one by one in a Linux container (`python:3.14`, non-root user), all exit 0, and the five tests Windows skips each ran and passed; the reviewer repeated six checks in a clone made like GitHub's checkout of a pull request, all exit 0. The first CI run of this request shows the run on a GitHub runner (the acceptance criterion): the check `tests` succeeded in 54 s with 1376 tests in 10 directories, and `instruction-files` ended `OK (skipped=10)`, the ten skipped tests being the ones that look up network paths only on Windows.
- Reviews of the corrections, each with the focused checks exit 0: the review of the first merge (`FAIL`, two blocking findings), the review of the fact written for your first answer (`PASS`), the review of the fix (`FAIL` on the one finding that your answer then settled), the review of correction 2 (`PASS`), the second merge (`PASS`), the second part of correction 2 (`PASS`). The return step ran after correction 1 (nothing changed), after correction 2 (one question, answered by you) and on the final code (nothing changed, no commit); the author's own run of the `installation` tests in the last one was stopped by its time limit (exit 124, no verdict), and the gate above covers that directory.
- Failed and passed again: none. Two tests of `task-cycle/test_remove_merged_worktrees.py` fail as root in a container and pass as a non-root user (Findings outside the task's scope, 1).
- Own-work checks of the authors: the acceptance criterion, as above; the author of the fix: the five places of the CI rule read side by side after the change, and a search that no other text says a red CI result is always fixed; none unrun.
- The process remarks check, `python -B task-cycle/remarks_check.py .runs/task-cycles/ci-on-merge-requests`: on the original, in the first cycle exit 1 listing 11 items and then 0 (2 runs); in correction 1 exit 1 listing 8 items and then 0 (2 runs); in correction 2 exit 1 listing 7 items and then 0 (2 runs). The checks on the copy of the record and on this description: filled in with the record's link.
- Working copies an agent could not remove: none. The `python:3.14` Docker image the author pulled stays on the machine.
- Directories of earlier tasks that the cleaning script kept (from the first cycle's start; the script does not run in a correction): `agent-path-to-running-product` (branch `task/agent-path-to-running-product`: the branch has no merge git can see on `origin/foundations`: not merged, merged by squash or rebase, or its request open or closed); `base-check-stage-remarks` (detached: the branch `task/stage-remarks` its name gives is not found); `base-fix-minor-findings` (detached: the branch `task/minor-findings` its name gives is not found).

## Foundation entries

- WAY-16 (rows 1 and 2): the one command of tests also runs in CI on every merge request, from the product's own CI file with `.the-way` at the pinned commit, and its result is a required check with a bypass for the owner. Its *Scope*, *Relations*, *Verification*, *Rationale* and *Rejected* carry it; its *Based on* names `github-required-status-checks`, `github-ruleset-bypass` and, since correction 1, `foundations-branch-ruleset` in place of the open `TODO` (`the cycle's`, by your answer to item 2 of the earlier description).
- `foundations-branch-ruleset` (`the cycle's`, by your answer): the repository `mariusznazar/the-way` has an active ruleset `foundations_tests` that targets `refs/heads/foundations`, requires the status check `tests` of the integration 15368 without requiring the branch to be up to date, has one bypass actor (a repository role, id 5, mode `always`), and the account `mariusznazar`, which holds the permission `admin`, is reported able to bypass it always; its source is a reading of two read-only `gh api` calls of 2026-11-15, quoted word for word.
- WAY-206 (row 4): a vulnerability found in a library the product already holds gets its signal from the alerts of the repository's service, which the skill proposes and a human turns on; the audit of a change and the sentence that the template carries no audit of the whole tree stay.
- WAY-160 (row 6): the orchestrator waits for the CI result on the open request before it is marked ready, treats red as a failed gate and puts the result into the description; widened by the cycle to corrections and exempted for a request left blocked for unfinished code (`the cycle's`); it also leaves a check outside the task's scope that passes when run again to WAY-261 (`the cycle's`).
- WAY-09 (`the cycle's`): the list of what the repository holds names the CI configuration among the files of the instructions part.
- Part map (`the cycle's`): `agent-instructions` gains `.github/workflows/**`; its *Depends on* gains `repository` (your answer to the question of the return step, comment of 2026-11-15); the *Depends on* of `installation` gains `instruction-files` (your answer to the blocking item, comment of 2026-11-15, citing settlement 5 of the task).
- Environment facts (`the cycle's`): `github-dependabot-alerts`, `github-required-status-checks`, `github-ruleset-bypass`, and `foundations-branch-ruleset` above.
- Row 3 stands as the comment of the CI workflow; row 5 as the installer's block. No invariant is written or changed and no invariant test altered; no *Violated* mark is set or cleared (an invariant the cycle wrote for the reach of `installation` and marked violated was removed again on your answer, and it never reached the target branch); no surface changes.

## Minor findings

1. From the review of correction 1, M1, `foundations/environment_facts.md` (the new fact, its sentence and *Source*): "The quoted reading does not show the account that `current_user_can_bypass` describes, which is the link from the fact to "the owner of the repository may bypass it" in WAY-16." The reviewer found the sentence true and the gap in whether the source can be checked again; adding `gh api user --jq .login` as a third line of the reading would show the link.
2. From the review of correction 1, M2, `foundations/environment_facts.md` (the new fact, its sentence): "Nothing in the foundation shows that the integration 15368 is GitHub Actions, the source of the `tests` job in `.github/workflows/tests.yml`." Optional; `gh api apps/github-actions --jq '{id, slug}'` printed `{"id":15368,"slug":"github-actions"}`.
3. From the review of correction 1, M3, `foundations/environment_facts.md` (the new fact, its *Source*): "The first command reads fields the sentence does not rest on." The filter keeps the rules `deletion` and `non_fast_forward`, and the second command keeps `role_name`; no secret, so the only effect is that a change to those rules would make the quote stale.
4. From the review of the fix, A, `agent-instructions/README.md`, `task-cycle/skill/SKILL.md` (step 12), `foundations/decisions.md` (WAY-160): "Three edited lines run past the width of the paragraphs around them." The paragraphs were not rewrapped after the insertion; cosmetic, with no effect on any reader.

The earlier Minor finding of the review of the first merge ("Two further reaches of the change, under the same definition, that no *Depends on* allows": the CI file's read of `/.python-version` and the README's mentions of the workflow file and of `.the-way/.python-version`) is settled by your answer to the question of the return step: the CI file's reach is allowed in the map, and the README's mentions are no dependency.

## Findings outside the task's scope

You let both of these through in your answer and asked for no task.

1. `task-cycle/test_remove_merged_worktrees.py`, two tests that fail where the user is root (reviewer's words: "outside the task — the fault is in the tests' handling of a held file under root, the CI runner is not root, and no file of this change touches them or what they test"). The author's account: `hold_a_file` makes a directory unwritable with `chmod`, root ignores it, the removal succeeds, and `holder()` in the `finally` raises `FileNotFoundError` on the removed path before the test can skip.
2. What a pull request that edits `.github/workflows/tests.yml` can do to its own required check (reviewer's words: "it can replace the run with one that passes, and a request from a branch of the same repository can raise the token's `permissions` in its own copy of the workflow. Both are properties of GitHub's `pull_request` event for any required check, not of this workflow; the-way's answer is the review of every change (WAY-10) and the owner's merge, which no file of this task can add to. Outside the task.").

## Course of the cycle

- **Task and sources:** make the tests of every pull request run automatically in CI and give products a signal about new vulnerabilities in the libraries they already use; independent task, from the author's task note of 2026-11-14 with its six settled answers.
- **Process pin:** none (the-way itself); the checkout was brought to `21ecb62` at the start of the first cycle, found up to date with `7f5c5a5` at the start of correction 1, and merged with `9cbc6b2` during correction 2.
- **Spec:** none; no open design choice stood.
- **Route:** one author without a plan, class same as the orchestrator, because the change is a set of short text edits and one workflow file that one agent holds; a review of the whole change by an agent on a stronger model, one fix, a review of the fix, the return step and its review. The corrections: the author of the corrections on the same route, a fresh agent (the first author's session was gone) and then resumed, reviews by agents on a stronger model, and one fix of the review of the first merge.
- **Plan:** none.
- **Choices:** 11 other choices of the cycle, rows Q0 and Q3–Q10 of the first cycle and Q11 and Q12 of the corrections in *Questions and autonomous choices* of the record (the exemption of blocked requests from the wait, the part of the CI file, the place of the description, the fork point of the foundation check in CI, the pinned actions and the job's settings, the installer's fallback, the place of the wait in the cycle, the Linux test fixes, the Python line and the removed claim; the CI rule's exception for a flaky test; the route for the reach of the installer part, which a reviewer held wrong and which you settled by your answer); the link is the record's, below.
- **Blocking findings left:** none. The one that remained after the review of the fix (the invariant the cycle wrote for the reach of the installer part, which a reviewer held wrong) was settled by your answer (a): the invariant was removed and the dependency allowed in the map (`2e83447`, review `PASS`).
- **Corrections:** correction 1, your answer of 2026-11-15 to item 2 of the earlier description, remarks in the record's `reports/correction-1-remarks.md`; correction 2, your answer of 2026-11-15 to the blocking item and your answer to the question of its return step, remarks in `reports/correction-2-remarks.md`; no reset base (no attempt was discarded).
- **Record:** pending.
