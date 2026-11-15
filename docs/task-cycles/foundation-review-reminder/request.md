**State: ready** — one item of *Fix or let through* waits for your answer: a rule that was tried only in this repository; what you only accept by merging waits for nothing.

## What you will see

The reminder that tells you the foundation waits for a review changes. It now comes at 60 merges since the last review instead of 30. From that point the cycle reads your backlog: where no open line of the review of this repository stands, the request asks you to add one and says what its name must hold (the name of the review skill and the name of the repository); where one stands, the request only points to it and no longer urges. The cycle never adds or changes a line of your backlog. Below the threshold a request says nothing about a review.

The script that counts the merges no longer takes a failure of git for "no review tag yet". It used to count from the start of the history when git failed, which could make the reminder appear falsely; now it ends with an error message, the cycle writes no reminder, and the failed count is listed among the checks that did not run.

When you run the review of the foundation, it now also finds every entry of the decision log that is no decision — rules that belong to the guidelines, single texts and numbers, descriptions of a missing feature, parts of one question under separate numbers — sorts them into groups by the place each goes to, with the number of entries in each group, and puts the groups before you. You choose which whole groups go into the task this time; the rest wait for the next review.

### Underneath

The number 60 now stands in the script that counts, with its test and the reason for it beside it, so the decision about the reminder says "from the script's threshold" and holds no number.

## For you to decide

### Needed from you

none

### Fix or let through

1. The rule that tells the cycle which name an open review line must hold — the last part of the address of the repository's `origin` remote, or the name of the main checkout's folder where it has none — was tried only in this repository, where it gives `the-way`. It was not tried in a product that carries the process inside it as a submodule, where the address that counts is the product's and not the process's. If the rule picks a wrong name there, the first reminder in that product, after 60 merges, keeps asking you to add a review line that already stands. Trying it now costs a session in such a product and a round of review; making a task of it leaves the rule untried until a product reaches the threshold; letting it through accepts that. I recommend letting it through: the sentence the cycle writes always states the name it expects, so a wrong name shows in the request itself, and the repair is one sentence. Try it in this request, make a task of it, or let it through? (Checks, 8)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. Your task did not say what the cycle does when the counting script fails. The cycle records the error message, writes no reminder, since it would have to state a count it does not know, and lists the failed count among the checks that did not run in this section of the request, so that you see it. The other way, saying nothing, would leave each cycle to invent its own reaction, in the one case where the reminder must not be missed.
3. One sentence beyond the task: when the review of the foundation ends, it tells you to mark an open review line done. Without it, a line left open after a review makes every later reminder only point to that line and never ask again. The reviewer of the whole change found the sentence beyond the task, harmless and closing a real gap; it writes nothing to your backlog. The other way was to leave this to the setup of your daily advisor, which lies outside this repository, so the gap would stay for every other user.
4. Your task says the review line's name holds "the name of the repository" but not where the name comes from. The cycle took the last part of the address of the repository's `origin` remote, or the name of the main checkout's folder where there is no such remote. It did not take the name from the backlog section of the instruction file, which names nothing for a product whose backlog is a folder or a public tracker, and it did not take the folder of the working copy of the task, which differs for each task.
5. The comment beside the number 60 says a review comes every 2 to 10 weeks in the-way, where your task's note said 2.5 to 10. The cycle followed the arithmetic: 60 merges at 26 a week is 2.3 weeks, and the pace figures of the note give no 2.5. The other figures of the note hold: about 10 days at the pace of 6 to 14 November, and 3 to 15 weeks in the product.
6. The cycle made two changes in the reminder decision that no row of your task carried: it now links to the decisions on where a product's backlog is read from and on who writes outside the repository, since it rests on both, and its checking part now names the tests that hold the count and the threshold, in place of two examples that those tests already check. In the review decision, the rejected ways lost the wording that described its earlier text, and no longer reject the review line that a human adds.
7. Five tests of the counting script now carry a comment line saying which sentence of the reminder decision each holds. No test code and no invariant changed; the foundation check lists no sentence for a corrected invariant.

## Cost

The cycle ran 30 minutes of working time, 7 minutes of it waiting for tools, and used 33.6 million tokens in all, 32.8 million of them cached input, all on one model (Sonnet 5.5): one author in three turns (the change, the fix, the return step) and three reviews (the whole change, its fix, the return step). The full gate ran once, 5 minutes 27 seconds, on the signal of your daily advisor. The table of stages is in the committed record.

One file of an agent's check stayed in the ignored working directory of the task, the reviewer's list of decisions; nothing waits for it, and it goes when the task's directory goes. Directories of four earlier tasks still stand, because the script that tidies them could not tell they were no longer needed; nothing in this request waits for them, and you may remove them by hand.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then.

<details>
<summary>W Twoim języku (po polsku)</summary>

**Stan: gotowe** — jeden punkt z *Popraw albo przepuść* czeka na Twoją odpowiedź: reguła sprawdzona tylko w tym repozytorium; to, co tylko akceptujesz przez scalenie, na nic nie czeka.

## Co zobaczysz

Zmienia się przypomnienie, że fundament czeka na przegląd. Teraz pojawia się przy 60 scaleniach od ostatniego przeglądu zamiast przy 30. Od tego progu cykl czyta Twój backlog: gdy nie stoi w nim otwarta linia przeglądu tego repozytorium, prośba prosi Cię o jej dodanie i mówi, co ma stać w jej nazwie (nazwa skilla przeglądu i nazwa repozytorium); gdy linia stoi, prośba tylko na nią wskazuje i już nie ponagla. Cykl nigdy nie dodaje ani nie zmienia linii Twojego backlogu. Poniżej progu prośba nie mówi nic o przeglądzie.

Skrypt liczący scalenia nie bierze już błędu gita za „jeszcze nie ma znacznika przeglądu”. Dawniej przy błędzie gita liczył od początku historii, co mogło fałszywie wywołać przypomnienie; teraz kończy się komunikatem o błędzie, cykl nie pisze przypomnienia, a nieudane liczenie trafia na listę sprawdzeń, które się nie odbyły.

Gdy prowadzisz przegląd fundamentu, znajduje on teraz także wszystkie wpisy dziennika decyzji, które decyzjami nie są — reguły, które należą do wytycznych, pojedyncze teksty i liczby, opisy braku funkcji, części jednego pytania pod osobnymi numerami — układa je w grupy według miejsca, do którego każdy idzie, z liczbą wpisów w każdej, i przedstawia Ci grupy. Ty wybierasz, które całe grupy wchodzą w zadanie tym razem; reszta czeka do następnego przeglądu.

### Pod spodem

Liczba 60 stoi teraz w skrypcie liczącym, z testem i powodem przy wartości, więc decyzja o przypomnieniu mówi „od progu skryptu” i nie trzyma żadnej liczby.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Popraw albo przepuść

1. Reguła, która mówi cyklowi, jaką nazwę ma mieć otwarta linia przeglądu — ostatnia część adresu zdalnego repozytorium `origin` albo nazwa katalogu głównego checkoutu, gdy zdalnego nie ma — została sprawdzona tylko w tym repozytorium, gdzie daje `the-way`. Nie sprawdzono jej w produkcie, który ma proces w środku jako podmoduł, gdzie liczy się adres produktu, nie procesu. Jeśli reguła wybierze tam złą nazwę, pierwsze przypomnienie w tym produkcie, po 60 scaleniach, będzie dalej prosić o dodanie linii przeglądu, która już stoi. Sprawdzenie teraz kosztuje sesję w takim produkcie i rundę przeglądu; zrobienie z tego zadania zostawia regułę niesprawdzoną, aż produkt dojdzie do progu; przepuszczenie przyjmuje to ryzyko. Rekomenduję przepuścić: zdanie, które pisze cykl, zawsze podaje nazwę, jakiej oczekuje, więc zła nazwa widać w samej prośbie, a poprawka to jedno zdanie. Sprawdzić w tej prośbie, zrobić z tego zadanie czy przepuścić? (Checks, 8)

### Akceptujesz przez scalenie

Scalenie akceptuje te punkty; jeśli któryś Ci nie odpowiada, powiedz który.

2. Zadanie nie mówiło, co robi cykl, gdy skrypt liczący zawiedzie. Cykl zapisuje komunikat o błędzie, nie pisze przypomnienia, bo musiałby podać liczbę, której nie zna, i wpisuje nieudane liczenie na listę sprawdzeń, które się nie odbyły, w tej sekcji prośby, żebyś to zobaczył. Druga droga, milczenie, zostawiłaby każdemu cyklowi wymyślenie własnej reakcji, w jedynym przypadku, w którym przypomnienia nie wolno przeoczyć.
3. Jedno zdanie ponad zadanie: gdy przegląd fundamentu się kończy, mówi Ci, żebyś oznaczył otwartą linię przeglądu jako zrobioną. Bez niego linia zostawiona otwarta po przeglądzie sprawia, że każde kolejne przypomnienie tylko na nią wskazuje i nigdy już nie prosi. Recenzent całej zmiany uznał to zdanie za wykraczające poza zadanie, nieszkodliwe i domykające realną lukę; nic nie zapisuje w Twoim backlogu. Druga droga: zostawić to ustawieniu Twojego doradcy dnia, które leży poza tym repozytorium, więc luka zostałaby dla każdego innego użytkownika.
4. Zadanie mówi, że nazwa linii przeglądu zawiera „nazwę repozytorium”, ale nie mówi, skąd ją brać. Cykl wziął ostatnią część adresu zdalnego `origin` repozytorium albo nazwę katalogu głównego checkoutu, gdy zdalnego nie ma. Nie wziął nazwy z sekcji backlogu w pliku instrukcji, która nie nazywa niczego dla produktu z backlogiem w katalogu albo w publicznym trackerze, ani katalogu kopii roboczej zadania, który jest inny dla każdego zadania.
5. Komentarz przy liczbie 60 mówi, że przegląd wypada co 2 do 10 tygodni w the-way, a notatka zadania mówiła 2,5 do 10. Cykl poszedł za arytmetyką: 60 scaleń przy 26 tygodniowo to 2,3 tygodnia, a liczby tempa z notatki nie dają 2,5. Pozostałe liczby notatki się zgadzają: około 10 dni przy tempie z 6–14 listopada i 3 do 15 tygodni w produkcie.
6. Cykl zrobił dwie zmiany w decyzji o przypomnieniu, których nie niósł żaden wiersz zadania: łączy się ona teraz z decyzjami o tym, skąd czyta się backlog produktu i kto zapisuje poza repozytorium, bo na obu stoi, a jej część sprawdzająca nazywa teraz testy, które trzymają liczenie i próg, zamiast dwóch przykładów, które te testy już sprawdzają. W decyzji o przeglądzie odrzucone drogi straciły sformułowanie opisujące jej wcześniejszy tekst i nie odrzucają już linii przeglądu, którą dodaje człowiek.
7. Pięć testów skryptu liczącego nosi teraz linię komentarza mówiącą, które zdanie decyzji o przypomnieniu każdy trzyma. Kod testów ani żaden niezmiennik się nie zmienił; sprawdzenie fundamentu nie wypisuje żadnego zdania dla poprawionego niezmiennika.

## Koszt

Cykl pracował 30 minut, z czego 7 minut czekał na narzędzia, i zużył łącznie 33,6 mln tokenów, z czego 32,8 mln z pamięci podręcznej, wszystko na jednym modelu (Sonnet 5.5): jeden autor w trzech turach (zmiana, poprawka, krok zwrotny) i trzy przeglądy (całej zmiany, jej poprawki, kroku zwrotnego). Pełna bramka przeszła raz, w 5 minut 27 sekund, na sygnał Twojego doradcy dnia. Tabela etapów jest w zatwierdzonym zapisie.

Jeden plik sprawdzenia agenta został w ignorowanym katalogu roboczym zadania, spis decyzji recenzenta; nic na niego nie czeka i zniknie razem z katalogiem zadania. Katalogi czterech wcześniejszych zadań nadal stoją, bo skrypt, który je sprząta, nie potrafił poznać, że przestały być potrzebne; nic w tej prośbie na nie nie czeka i możesz je usunąć ręcznie.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przetrwa tylko wtedy.

</details>

## Technical changes

1. The counting script (`f96ddd2`): `THRESHOLD = 60` in `task-cycle/review_reminder.py` with a comment holding the rhythm for 60 merges and the price taken, and a failure of git now ends the script with exit code 2 and an `Error:` line. The script first lists the review tags the branch contains (`git tag --list --merged`): an empty list with exit 0 is no tag, a non-zero exit is an error, and a failure of `git describe` where a tag is listed is an error too. It reads no message of git, which git translates. `task-cycle/test_review_reminder.py` holds the boundary at 59 and 60 merges, the restart of the count after a tag, and the two error cases, with a stub for the one failing git command.
2. The cycle's step 13, the template of the description, the root `README.md` and the files of `foundation-review/` (`c0ba78b`): step 13 reads the backlog from the threshold on, finds the open review line by the skill's name and the repository's name, writes the reminder in its two forms (ask for the line, or point to it) and says that below the threshold nothing is written; `request_template.md` gives the forms; `foundation-review/SKILL.md`, `weak_points.md`, `proposals.md` and `with_the_human.md` give the review its grouping of the entries of the log that are no decisions, by the five questions "Where it goes" of the decisions template, and the human's choice of whole groups; the number 30 left `SKILL.md` and `README.md`.
3. The two decisions (`b7ec371`): the reminder decision and the review decision in `foundations/decisions.md`, as the task's rows 1, 2 and 5 give; its *Verification* example, *Rationale* and *Rejected* are changed as the task's point 5 gives.
4. The fix of the five Minor findings of the review of the whole change (`9638c91`, `31f7507`): one boundary in `weak_points.md` for a rule that ends with its own change; the rejected ways of the two decisions without the history of their earlier text; the repository's name taken from the `origin` remote; the failed count placed in the section for the human's decisions; two overlong lines rewrapped.
5. The return step (`e5ae875`): the reminder decision's *Verification* now begins with a `tests:` clause and its pair of examples keeps only the part no test holds, and five tests carry `decision:` lines. It found nothing else to correct. Nothing was reverted.

## Checks

1. Gate on the final tree `e5ae875`, run on the signal `start` of the day's advisor: `python -B task-cycle/gate_times.py --output docs/task-cycles/foundation-review-reminder/gate_times.md -- python -B gate/run_tests.py` exits 0: 1445 tests in 10 directories, 326.8 s, 0 other gate runs at the same time; every directory passed. The target branch had not moved from `ff88ca3`, so no reconciliation ran.
2. Tests failing before the change: none. The base is a merge commit whose tree equals that of its second parent, so no gate ran on it; the list was taken from the final gate of the merged cycle, `docs/task-cycles/decision-log-reading-index/cycle.md` of commit `f6bc252`, *Verification*: exit 0, 1443 tests in 10 directories, every directory passed. A timing test of the gate, `test_by_default_every_directory_runs_at_the_same_time`, is known to be flaky; it did not fail in this cycle.
3. `python -B elements/common/foundation_check.py`, without skipping the test citations: exit 0, `0 errors`, no `listed:` line. The return step also altered one quotation of a new `decision:` line on purpose and got `4 errors`, so the check reads the new lines; the text was restored.
4. `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `tag: foundation-review/2026-11-15`, `merges: 1`, `threshold: 60`, `reminder: no`; so this request carries no reminder.
5. Focused checks, each exit 0 in its last run: `python -B task-cycle/test_review_reminder.py` (11 tests), `python -B gate/run_tests.py task-cycle` (480 tests), `python -B gate/run_tests.py elements/common` (232 tests), `python -B gate/run_tests.py agent-instructions` (25 tests, by the reviewer). The new tests were seen failing first: 3 failures with exit 1 against the old code, each for the expected reason, then exit 0.
6. Own-work checks: the author's weakest points were the exit 2 for a git error with a real absence of tags still read as none, and the three texts of the two forms of the reminder; both were tried (the script on the real history agrees with `git describe` and `git rev-list` by hand, and the error tests answer in Polish so that no English message can pass them). The one thing the author could not make fail for real was `git describe` failing where the tag list works; the error tests use a stub. The review of the whole change judged the rhythm "2 to 10 weeks" right.
7. `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` on this cycle's orchestrator session: both exit 0.
8. Unchecked: (a) the rule for the repository's name in a product that has the process as a submodule; (b) that the task place's own definition of an open line agrees with what step 13 assumes, since the file with those rules lies outside the repository and no reviewer opened it; (c) a request that carries either form of the new reminder, since this request is below the threshold and the first one after 60 merges will be the first. The form check reads the template's skeleton, not these two forms. The reviewers of the whole change and of its fix named (a), (b) and (c) as unverified.
9. Process remarks check: `python -B task-cycle/remarks_check.py docs/task-cycles/foundation-review-reminder` on the original, 2 runs: exit 1 listing 10 items, which were appended word for word to the process remarks, then exit 0. On the copy: COPYREMARKS.
10. Form check of this description: `python -B task-cycle/request_check.py docs/task-cycles/foundation-review-reminder/request.md --task docs/task-cycles/foundation-review-reminder/task.md`, exit 0, FORMRUNS.
11. Private paths in the description: `python -B task-cycle/private_paths_check.py docs/task-cycles/foundation-review-reminder/request.md`, exit 0, PPRUNS.
12. Checks on the copy of the record: COPYCHECKS
13. Working copies left: the reviewer of the return step left its list of decisions, `.runs/review-return/index.md`, a file and no checkout; it goes with the task's directory.
14. Directories of earlier tasks kept by the script of the start: `agent-path-to-running-product` (branch `task/agent-path-to-running-product`; its branch has no merge git can see on the target branch), `ci-on-merge-requests` (branch `task/ci-on-merge-requests`; same reason), `base-check-stage-remarks` (detached; the branch `task/stage-remarks` its name gives is not found) and `base-fix-minor-findings` (detached; the branch `task/minor-findings` its name gives is not found).

## Foundation entries

1. The review decision (`row 2`): the review of the foundation stays a run of its skill in a session with a human; a task of the product's backlog may stand for that run, and a human adds it, never a cycle.
2. The reminder decision, from the threshold of the script on (`row 1`, `row 5`): the orchestrator reads the product's backlog for an open line whose name holds the skill's name and the repository's name; where there is no such line or the backlog cannot be read the reminder asks the human to add the task of the review, otherwise it points to the line without urging; the cycle adds or changes no line; the threshold stands in the reminder script and is one number for every product, which no product sets for itself.
3. The reminder decision's checking part and its links (`the cycle's`): its *Verification* names in words the tests that hold the count since the nearest review tag, the threshold and its single value, and keeps a pair of examples only for the cycle's and the request's part; its *Relations* now also say it derives from the decision on where a product's backlog is read from and the one on who writes outside the repository.
4. Row 3 went to the skill files of `foundation-review/` and row 4 to the script and its test; no entry of the log is written for either.
5. Five tests of `task-cycle/test_review_reminder.py` carry a line `decision: WAY-300 "…"`, added by the return step; no test code changed, no invariant, surface or *Violated* mark changed. The log opens no topical section.

## Minor findings

1. Minor finding 1 of the review of the fix of the whole change's Minor findings, `foundations/decisions.md`, the reminder decision's *Rejected*: "the line 'later review needs a new one, since the old stays on a done line; no reading of the backlog, the sentence always asking for the' — 127 columns, left over by the author's rewrap commit `31f7507` (the report claims the lines of WAY-24 and WAY-300 were rewrapped); the line 'identifier the-way computes for the review's line, in the field of identifier …' is 101 columns. Besides this, the second paragraph of WAY-300 now has a short ragged line ('(WAY-107). Where no such line stands, or') after the edit. Polish; no check reads it; the finding 5 repair was for the other two files and holds. Within the task." The return step rewrapped the ragged paragraph of the binding sentences; the lines of *Rejected* stand as they were.
2. The review of the return step, `foundations/decisions.md:6818-6819`, the reminder decision's *Verification*, the violating example: "the example 'the count starts at the merge of the review's own change' still describes a part the tests hold. What: the clause `tests:` says the tests hold 'the count of merges to the main branch since the nearest review tag, from the start of the history where none stands'. The tests `test_only_the_merges_after_the_nearest_review_tag_count` and `test_without_a_tag_every_merge_since_the_start_of_history_counts` check where the count starts, and a count that started at some merge of the review's own change instead of the tag would fail the first. WAY-12 and `task-cycle/skill/return_step.md` keep the pair 'only for the part no test holds'. Why it matters little: the example overlaps what the tests hold and contradicts nothing, so an agent that compares a change with it is told the same as the test says. Graded Minor for that reason. Evidence: the diff of the commit removes only the complying example on merges of the main branch into task branches, and leaves this one. Whether the example is held depends on reading it as the count's start (script) and not as a rule of the cycle's wording; I could not settle that from the entry, so I name it and leave the choice to the orchestrator." Within the task. Neither Minor finding will be felt by the user or by the human working with the process, so neither is among the items to decide.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** make the review of the foundation hard to skip — a reminder at 60 merges that reads the backlog for the review line and asks for it, a script that tells a missing tag from an error of git, and a batch of the log's entries that are no decisions at each review; independent task; the foundation of `foundations` at `ff88ca3`, the task document as it stood on 2026-11-15, with its five accepted rows.
- **Process pin:** none; the-way itself, on `foundations` `ff88ca3`; no gate was run on the base (a merge with its second parent's tree), the list of failing tests came from the earlier cycle's final gate.
- **Spec:** none; the task left no open design choice, since its questions 1 to 6 and rows 1 to 5 settle the shape; how the script tells a missing tag from an error of git was a choice of how to make what the task settles.
- **Route:** one author without a plan, class `same` as the orchestrator's, since the change reaches three parts (decisions, the task cycle and the foundation review) and rewords two decisions and several skill texts that must agree with each other; one fix round for five Minor findings, and a return step with its review.
- **Plan:** none.
- **Choices:** 7 questions and autonomous choices, among them the wait for the day's advisor before the full gate, the open end of four decisions the author read in part, the source of the repository's name and the two additions of the author; the questions table is in the committed record.
- **Blocking findings left:** none; the review of the whole change, the review of its fix and the review of the return step all passed.
- **Record:** LINK
