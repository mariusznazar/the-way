**State: blocked** — waits for your action outside the repository: setting the check as required in the branch rules (item 1)

## What you will see

Every pull request into `foundations` now gets its tests run automatically on GitHub, on Linux, with the one command of the-way's tests. Until now only a person or the agent of a cycle ran them, on a Windows machine, and five tests that need Linux (links, loops of links, a named pipe) never ran anywhere. Three tests of the instruction-file checker failed on Linux; they were faults of the tests, not of the checker, and are fixed. The first run of this very request is the proof that those five tests now run instead of being skipped.

The agent that leads a cycle now waits for that run on its own request, treats a red run like a failed final test run (a fix and a review of it), and writes the result into the request's description, so that a request reaches you with the result of the run. This holds for corrections after your remarks too. A request the cycle leaves blocked for unfinished code is not waited for.

For products that use the-way: the block of instructions the installer writes into a product now says that the one command also runs the instruction-file checker (a script error stops the tests, a warning does not), that it runs in CI on every merge request, and that its result is a check the repository requires with the owner allowed to bypass it. A short description tells a product's owner what its CI file must hold: the one command on every merge request, the-way at the commit the product pinned and never the latest, the history the foundation check needs, and the required check. The installer puts no CI file into a product; the product writes its own. The skill that proposes the coding guidelines now also proposes turning on the repository service's alerts about vulnerable libraries (on GitHub, Dependabot alerts), which is the signal for a library the product already uses; a human turns them on.

### Underneath

The rules about these things now stand in the foundation (the decisions on the one command of tests, on the audit of dependencies and on the cycle's final test run), with three facts about GitHub's own behaviour written down with their sources.

## For you to decide

### Needed from you

1. Set the check of this request, named `tests`, as required before a merge in the branch rules of `foundations`, with you, the repository's owner, allowed to bypass it. GitHub lets you choose only a check that has already run once, and the run on this request is the first, so the rule can be set now. Without it the check only shows its result and blocks nothing, so a red request can be merged by oversight; with it, a broken CI can still be bypassed by you. Nothing in this request changes any setting on GitHub, since that is an effect outside the repository that only you make.

### Fix or let through

2. One decision (the one that says the one command also runs in CI and that its result is a required check with a bypass for the owner) rests on a setting of GitHub that nobody has read yet: the branch rule does not exist today, so no reading of it can be written down. The decision is marked with an open gap that says so. If you leave it, nothing breaks; the decision stays true and the gap stays marked until someone reads the rule once you have set it. Closing it in this request would cost one more correction round after item 1 and a review of it; making a task of it costs a small task later; letting it through leaves the marked gap on the main branch. I recommend making a task, since the reading can only be done after your action. Close it in this request, make a task of it, or let it through?
3. Two things the reviewers named as outside this task. First, two tests of the checker that removes finished working directories fail when the tests run as the root user (the root user can write where the test makes a file unwritable); the CI runner is not root and you do not run them as root, so you will not feel it unless someone runs the tests as root in a container. Second, a pull request that edits the CI file can replace the run with one that always passes, so the required check protects against mistakes, not against a change that edits the CI itself; this is how GitHub's required checks work for any repository, and the only guard is your review of every merge. Fixing them in this request would cost a correction round and a review each; I recommend letting the first through and making a task of the second only if you want a rule that the CI file is changed only by you. Fix them in this request, make a task of it, or let them through? (Findings outside the task's scope, 1 and 2)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

4. A request that the cycle leaves blocked for unfinished code (a review finding that remained, a slice that failed twice, a technology choice only you make) is not waited for: its code is not finished, so a red run is expected and the result stands on the request's page for you to read. A request that waits only for your actions, like this one, is waited for, because you need the run to have happened. The other way, waiting for every request, would stop the cycle on a failure it already knows.
5. The block the installer writes now also tells an agent what to do in a product that has not yet written its CI file (loop2, until its own task): run the one command on its own, as the block already says for the two checks. The task asked only for the sentence that CI runs the command; without the fallback the block would say something false in such a product.
6. The description for products also says that the CI job needs Python at the version the-way declares, which the task did not list; without it the job fails in every product that pins the-way.
7. Foundation entries you did not see at the task, written by the cycle: the decision on the one command of tests now binds what the installer promises a product and rests on the pin of the-way; the decision that lists what the repository holds names the CI file among the files of the instructions part; the cycle's final-test-run decision now says that the wait for CI covers corrections and not requests blocked for unfinished code; the part map gives the CI configuration folder to the instructions part; and three facts about GitHub (the alerts of vulnerable libraries, the required status check, the bypass list of a branch rule) are written with the address of GitHub's page, the date read and the passages. (Foundation entries)

## Cost

About 2 hours of working time in one session (of which about 1 hour 20 minutes was waiting for tools), 99.3 million tokens, almost all of them cached input (74.7 million on Sonnet, 24.6 million on Opus). One review of the whole change that failed on three blocking findings and four minor ones, one fix, one review of the fix that passed, a return step and a review of it that passed, and the full test run once on the final tree (7 minutes). The table of stages is in the committed record, linked at the end.

Directories of earlier tasks still stand because the cleaning script could not tell they were no longer needed; nothing in this request waits for them and you may remove them by hand (their names are under Checks).

## How to merge

First do item 1, then mark the request ready and merge it with a merge that keeps the commits, since the link to the record survives only then. Squash or rebase would lose that link.

The foundation has waited for a review through 49 merges since the review of 2026-11-06. The review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**State: blocked** — czeka na Twoją czynność poza repozytorium: ustawienie sprawdzenia jako wymaganego w regułach gałęzi (pozycja 1)

## Co zobaczysz

Każda prośba o scalenie do `foundations` dostaje teraz automatycznie uruchomione testy na GitHubie, na Linuksie, jednym poleceniem testów the way. Dotąd uruchamiał je tylko człowiek albo agent cyklu na maszynie z Windowsem, a pięć testów wymagających Linuksa (dowiązania, pętle dowiązań, nazwany potok) nie biegło nigdzie. Trzy testy sprawdzania plików instrukcji padały na Linuksie; były to błędy testów, nie skryptu, i są poprawione. Pierwszy przebieg na tej prośbie jest dowodem, że tych pięć testów teraz biegnie zamiast być pominiętych.

Agent prowadzący cykl czeka teraz na ten przebieg na własnej prośbie, czerwony traktuje jak nieudaną końcową bramkę (poprawka i jej recenzja) i wpisuje wynik do opisu, więc prośba trafia do Ciebie z wynikiem przebiegu. Dotyczy to też poprawek po Twoich uwagach. Na prośbę, którą cykl zostawia zablokowaną z niedokończonym kodem, nie czeka.

Dla produktów używających the way: blok instrukcji wpisywany przez instalator do produktu mówi teraz, że jedno polecenie uruchamia też sprawdzanie plików instrukcji (błąd skryptu zatrzymuje testy, ostrzeżenie nie), że biegnie w CI na każdej prośbie o scalenie i że jego wynik jest sprawdzeniem wymaganym przez repozytorium z prawem obejścia dla właściciela. Krótki opis mówi właścicielowi produktu, co ma zawierać jego plik CI: jedno polecenie na każdej prośbie, the way na commicie przypiętym przez produkt (nigdy najnowszym), historię potrzebną do sprawdzania fundamentu i wymagane sprawdzenie. Instalator nie wkłada produktowi pliku CI; produkt pisze go sam. Skill proponujący wytyczne kodowania proponuje też włączenie alertów serwisu o lukach w bibliotekach (na GitHubie alerty Dependabota), które są sygnałem o bibliotece już używanej; włącza je człowiek.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

1. Ustaw sprawdzenie tej prośby, o nazwie `tests`, jako wymagane przed scaleniem w regułach gałęzi `foundations`, z Twoim prawem obejścia jako właściciela repozytorium. GitHub pozwala wybrać tylko sprawdzenie, które już raz się uruchomiło, a przebieg na tej prośbie jest pierwszy, więc regułę można ustawić już teraz. Bez niej sprawdzenie tylko pokazuje wynik i niczego nie blokuje, więc czerwoną prośbę da się scalić przez przeoczenie; z nią uszkodzone CI nadal możesz obejść. Ta prośba niczego nie zmienia w ustawieniach GitHuba, bo to skutek poza repozytorium, który robisz tylko Ty.

### Popraw albo przepuść

2. Jedna decyzja (ta, która mówi, że jedno polecenie testów biegnie też w CI, a jego wynik jest wymaganym sprawdzeniem z obejściem dla właściciela) opiera się na ustawieniu GitHuba, którego nikt jeszcze nie odczytał: reguły gałęzi dziś nie ma, więc nie da się zapisać jej odczytu. Decyzja ma oznaczoną otwartą lukę, która to mówi. Gdy ją zostawisz, nic się nie psuje; decyzja pozostaje prawdziwa, a luka oznaczona, dopóki ktoś nie odczyta reguły po jej ustawieniu przez Ciebie. Domknięcie w tej prośbie kosztuje jeszcze jedną rundę poprawek po pozycji 1 i jej recenzję; zadanie na później kosztuje małe zadanie; przepuszczenie zostawia oznaczoną lukę na głównej gałęzi. Rekomenduję zadanie, bo odczyt da się zrobić dopiero po Twojej czynności. Domknąć w tej prośbie, zrobić z tego zadanie, czy przepuścić?
3. Dwie rzeczy, które recenzenci uznali za spoza tego zadania. Po pierwsze, dwa testy skryptu usuwającego zakończone katalogi robocze padają, gdy testy biegną jako root (root może pisać tam, gdzie test czyni plik niezapisywalnym); runner CI nie jest rootem i Ty nie uruchamiasz ich jako root, więc nie poczujesz tego, chyba że ktoś uruchomi testy jako root w kontenerze. Po drugie, prośba o scalenie, która zmienia plik CI, może podmienić przebieg na taki, który zawsze przechodzi, więc wymagane sprawdzenie chroni przed pomyłką, nie przed zmianą, która sama edytuje CI; tak działają wymagane sprawdzenia GitHuba w każdym repozytorium, a jedyną ochroną jest Twój przegląd każdego scalenia. Poprawa obu w tej prośbie kosztuje rundę poprawek i recenzję każdej; rekomenduję przepuścić pierwszą i zrobić zadanie z drugiej tylko wtedy, gdy chcesz reguły, że plik CI zmienia tylko Ty. Poprawić w tej prośbie, zrobić z tego zadanie, czy przepuścić? (Uwagi spoza zakresu zadania, 1 i 2)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

4. Na prośbę, którą cykl zostawia zablokowaną z niedokończonym kodem (uwaga recenzji, która została, plasterek, który dwa razy zawiódł, wybór technologii, który należy do Ciebie), nie czeka się: kod nie jest skończony, więc czerwony przebieg jest oczekiwany, a wynik stoi na stronie prośby do Twojego odczytu. Na prośbę czekającą tylko na Twoje czynności, jak ta, się czeka, bo potrzebujesz, żeby przebieg się odbył. Drugi sposób, czekanie na każdą prośbę, zatrzymałby cykl na awarii, którą już zna.
5. Blok pisany przez instalator mówi teraz też agentowi, co robić w produkcie, który nie napisał jeszcze pliku CI (loop2, do własnego zadania): uruchomić jedno polecenie samodzielnie, jak blok już mówi przy dwóch sprawdzeniach. Zadanie prosiło tylko o zdanie, że CI uruchamia polecenie; bez zastępstwa blok mówiłby w takim produkcie coś nieprawdziwego.
6. Opis dla produktów mówi też, że zadanie CI potrzebuje Pythona w wersji, którą deklaruje the way, czego zadanie nie wymieniało; bez tego zadanie CI pada w każdym produkcie przypinającym the way.
7. Wpisy fundamentu, których nie widziałeś przy zadaniu, zapisane przez cykl: decyzja o jednym poleceniu testów wiąże teraz to, co instalator obiecuje produktowi, i opiera się na przypięciu the way; decyzja o tym, co zawiera repozytorium, wymienia plik CI wśród plików części instrukcji; decyzja o końcowym przebiegu testów mówi teraz, że czekanie na CI obejmuje poprawki, a nie obejmuje próśb zablokowanych z niedokończonym kodem; mapa części daje katalog konfiguracji CI części instrukcji; trzy fakty o GitHubie (alerty o lukach w bibliotekach, wymagane sprawdzenie stanu, lista obejścia reguły gałęzi) są zapisane z adresem strony GitHuba, datą odczytu i cytatami. (Wpisy fundamentu)

## Koszt

Około 2 godzin pracy w jednej sesji (w tym około 1 godziny 20 minut czekania na narzędzia), 99,3 mln tokenów, prawie wszystkie jako wejście z pamięci podręcznej (74,7 mln na Sonnet, 24,6 mln na Opus). Jedna recenzja całości, która nie przeszła z trzema uwagami blokującymi i czterema drobnymi, jedna poprawka, jedna recenzja poprawki, która przeszła, krok powrotu i jego recenzja, które przeszły, oraz jeden pełny przebieg testów na końcowym drzewie (7 minut). Tabela etapów jest w zatwierdzonym rekordzie, z linkiem na końcu.

Katalogi wcześniejszych zadań nadal stoją, bo skrypt sprzątający nie mógł stwierdzić, że nie są już potrzebne; nic w tej prośbie na nie nie czeka i możesz je usunąć ręcznie (ich nazwy są w Sprawdzeniach).

## Jak scalić

Najpierw zrób pozycję 1, potem oznacz prośbę jako gotową i scal ją scaleniem zachowującym commity, bo link do rekordu przeżywa tylko wtedy. Squash albo rebase straciłby ten link.

Fundament czeka na przegląd przez 49 scaleń od przeglądu z 2026-11-06. Przeglądem jest skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium; nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

The change adds a CI workflow, makes the products' description and the installer's block say what is now true, widens three decisions of the foundation and adds three facts, and fixes three tests that failed on Linux. It does not touch the checker's own code (`instruction-files/check_instructions.py`), which was right on Linux. The commits, oldest first: `7217667`, `ff45403` (the description for products in `installation/README.md`; the installer's paragraph in `installation/install.py` with its two tests in `installation/test_install.py`); `80e9eca`, `7c301ce`, `ddcbfc2` (`instruction-files/test_check_instructions.py`: a Windows network path judged under a patched platform, the guard of the macOS shapes, one test split in two); `66121c8` (`.github/workflows/tests.yml`, the part map line, `agent-instructions/README.md`); `3410e33`, `345b6bd` (the decision log: WAY-16, WAY-206, WAY-160, WAY-09); `a5abe37` (`product-guidelines/coding/settle.md`, step 12 of `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`, `task-cycle/record_template.md`); `7d027c6` (root `README.md`); the fix of the review (`21777bd`: environment facts and the decisions; `827f716`: the installer's block, its tests, the README; `23f08e9`: `task-cycle/skill/SKILL.md`, `correction.md`, `blocked_finding.md`, `reserved_return.md`, the two templates, `agent-instructions/README.md`); the return step `b344595` (one clause in `installation/README.md`). The workflow runs `python -B gate/run_tests.py` on `ubuntu-latest` on `pull_request` into `foundations`, with the Python version of `.python-version`, the whole history and `origin/HEAD` set to `foundations` so that the foundation check compares with the fork point, read-only token, no secret, both actions pinned at commit SHAs; its job and workflow are named `tests`.

## Checks

- The gate, `python -B task-cycle/gate_times.py --output .runs/task-cycles/ci-on-merge-requests/gate_times.md -- python -B gate/run_tests.py`, on the final tree `b344595`: exit 0, 1376 tests in 10 directories, every directory passed, 423 s, no other run at the same time.
- Before the change, no test failed: the list was taken from the final gate of the earlier cycle (`docs/task-cycles/decision-log-second-round/cycle.md` of commit `cfd275c`, run 2: exit 0, 1374 tests, every directory passed), since the base is a merge whose tree equals that of its second parent.
- The foundation check, `python -B elements/common/foundation_check.py`: exit 0, `0 errors`, no `listed:` line.
- CI on this request: the run on the last head, its link and its conclusion by check, will be written here after the request is pushed; at the moment of writing it has not run.
- Linux: the author ran ten test directories one by one in a Linux container (`python:3.14`, non-root user), all exit 0, and the five tests Windows skips each ran and passed; the reviewer repeated `instruction-files`, `elements/common`, `installation`, `agent-instructions`, `task-cycle` and the foundation check in a clone made like GitHub's checkout of a pull request, all exit 0. The author's own-work check on the acceptance criterion showed that all five run on Linux; it does not show the run on a GitHub runner, which the first CI run of this request does.
- Failed and passed again: none. Two tests of `task-cycle/test_remove_merged_worktrees.py` fail as root in a container and pass as a non-root user (Findings outside the task's scope, 1).
- Own-work checks of the author: the acceptance criterion, as above; none unrun.
- The form check and the check of private paths on this description, and the three checks on the record's copy: written below after the last runs.
- Working copies an agent could not remove: none. The `python:3.14` Docker image the author pulled stays on the machine.
- Directories of earlier tasks that the cleaning script kept: `agent-path-to-running-product` (branch `task/agent-path-to-running-product`: the branch has no merge git can see on `origin/foundations`: not merged, merged by squash or rebase, or its request open or closed); `base-check-stage-remarks` (detached: the branch `task/stage-remarks` its name gives is not found); `base-fix-minor-findings` (detached: the branch `task/minor-findings` its name gives is not found).

## Foundation entries

- WAY-16 (rows 1 and 2): the one command of tests also runs in CI on every merge request, from the product's own CI file with `.the-way` at the pinned commit, and its result is a required check with a bypass for the owner. Its *Scope*, *Relations*, *Verification*, *Rationale* and *Rejected* carry it, and its *Based on* holds the open `TODO` for a reading of the branch rule (marked `row 1`, `row 2`; the entry's other changes `the cycle's`).
- WAY-206 (row 4): a vulnerability found in a library the product already holds gets its signal from the alerts of the repository's service, which the skill proposes and a human turns on; the audit of a change and the sentence that the template carries no audit of the whole tree stay.
- WAY-160 (row 6): the orchestrator waits for the CI result on the open request before it is marked ready, treats red as a failed gate and puts the result into the description; widened by the cycle to corrections and exempted for a request left blocked for unfinished code (`the cycle's`).
- WAY-09 (`the cycle's`): the list of what the repository holds names the CI configuration among the files of the instructions part.
- Part map (`the cycle's`): `agent-instructions` gains `.github/workflows/**`.
- Environment facts (`the cycle's`): `github-dependabot-alerts`, `github-required-status-checks`, `github-ruleset-bypass`.
- Row 3 stands as the comment of the CI workflow; row 5 as the installer's block. No invariant is written or changed and no invariant test altered; no *Violated* mark is set or cleared; no surface changes.

## Minor findings

none

## Findings outside the task's scope

1. `task-cycle/test_remove_merged_worktrees.py`, two tests that fail where the user is root (reviewer's words: "outside the task — the fault is in the tests' handling of a held file under root, the CI runner is not root, and no file of this change touches them or what they test"). The author's account: `hold_a_file` makes a directory unwritable with `chmod`, root ignores it, the removal succeeds, and `holder()` in the `finally` raises `FileNotFoundError` on the removed path before the test can skip.
2. What a pull request that edits `.github/workflows/tests.yml` can do to its own required check (reviewer's words: "it can replace the run with one that passes, and a request from a branch of the same repository can raise the token's `permissions` in its own copy of the workflow. Both are properties of GitHub's `pull_request` event for any required check, not of this workflow; the-way's answer is the review of every change (WAY-10) and the owner's merge, which no file of this task can add to. Outside the task.").

## Course of the cycle

- **Task and sources:** make the tests of every pull request run automatically in CI and give products a signal about new vulnerabilities in the libraries they already use; independent task, from the author's task note of 2026-11-14 with its six settled answers.
- **Process pin:** none (the-way itself); the checkout was brought to `21ecb62` at the start.
- **Spec:** none; no open design choice stood.
- **Route:** one author without a plan, class same as the orchestrator, because the change is a set of short text edits and one workflow file that one agent holds; a review of the whole change by an agent on a stronger model, one fix, a review of the fix, the return step and its review.
- **Plan:** none.
- **Choices:** 9 other choices of the cycle, rows Q0 and Q3–Q10 of *Questions and autonomous choices* in the record (the exemption of blocked requests from the wait, the part of the CI file, the place of the description, the fork point of the foundation check in CI, the pinned actions and the job's settings, the installer's fallback, the place of the wait in the cycle, the Linux test fixes, the Python line and the removed claim); the link is the record's, below.
- **Blocking findings left:** none.
- **Record:** pending the commit that adds it.
