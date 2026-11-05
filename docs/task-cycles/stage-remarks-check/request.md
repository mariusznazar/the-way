**State: ready** — the change is reviewed and every test passes; three items below wait for your yes.

## What you will see

A task cycle can no longer lose a remark that one of its stages made about the process. Before the cycle's record is archived, a small script now compares what every stage said it could not find or understand with the process remarks stored in the record, and lists each item the remarks do not hold word for word. The one who runs the cycle adds every listed item exactly as the stage wrote it, with the stage name and the full path of its report, and runs the script again until it lists nothing. The check is repeated before every archive of a record: when the request opens, when a correction after your remarks archives the record again, and when a request opens blocked.

The remarks now stand in one fixed form in the record: one item that opens with "Process remarks on the-way", and the entries indented under it, one for each item of each stage report. It is the form the nightly review already cuts out, so nothing in the review changes. The record template says so, and the record keeps no separate section or file for the remarks.

I ran the script on three real archives from your other repository. It lists the items you described: the return step in the first one, the reconciliation with the main branch and its review in the second, and the last fix of a slice and the second correction in the third. It lists seven, six and eight items that the three records lack. One count differs from your task: the task says two reports of the second archive hold two items each, the script finds three each, and all of them are real and missing from the record. As you chose, a line like "none found" with more text after it counts as an item, so the nightly review will see some more noise.

If the one who runs the cycle holds a listing to be an error of the script, the script is not changed in that cycle and the archive is written all the same. The case goes into the remarks and into this section of the request, so that you decide on it.

### Underneath

One new script with its tests and edits to the cycle's instructions and to the record template; the three decisions you accepted with the task are written in the decision log.

## For you to decide

1. **A listing held wrong does not turn the request into a draft.** You wrote that this case should be handled "as with the form check". When the form check reports an error that the cycle holds wrong, the request stays a draft. The author kept the request in the state it has for its other causes, because your task names three steps (write the archive, enter the case in the remarks, show it here) and no draft state. A request marked ready can therefore carry this kind of item, and its first line says whether something waits. Accept this, or make such a request a draft as for the form check? (Minor findings, 2)
2. **The record template names the nightly review's script.** To explain why the remarks have exactly this form, the template names the script of the nightly review, which lives in your private notes outside this repository. Nothing in the repository checks it, and the new script keeps its own copy of the way that script cuts the block, so a later change of the nightly script would not be noticed here. Keep this mention, or take it out? (Technical changes, 3)
3. **A short item can be hidden by a longer remark.** The script holds an item to be present when its words stand anywhere inside the remarks, so a short item such as "none found." would pass if a longer remark of another report contains it. Your own archives hold short items, for example "Otherwise none." in seven reports. Such an item is not listed, so it would not reach the nightly review, which is the loss this task fights. Make a task of it? (Minor findings, 1)

## Cost

About 28 minutes of working time. The orchestrator and all agents ran on one model, Claude Sonnet 5.5, with 21.7 M tokens in all, of which 20.8 M were input read from cache and 0.16 M output. Review rounds: the whole change was reviewed once and passed; no fix was needed. The return step made no commit, so it needed no review. The table of stages: https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/stage-remarks-check/stages.md

## How to merge

Use a merge commit, not squash or rebase: the link to the cycle's record points to a commit on this branch, and it survives only when the commits are kept.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — zmiana jest przejrzana i wszystkie testy przechodzą; na Twoje tak czekają trzy punkty poniżej.

**Co zobaczysz**

Cykl zadania nie może już zgubić uwagi, którą któryś jego etap zgłosił o procesie. Przed zarchiwizowaniem zapisu cyklu mały skrypt porównuje teraz to, czego każdy etap nie znalazł albo nie zrozumiał, z uwagami procesowymi zapisanymi w rekordzie i wypisuje każdą pozycję, której uwagi nie zawierają słowo w słowo. Prowadzący cykl dopisuje każdą wypisaną pozycję dokładnie tak, jak napisał ją etap, z nazwą etapu i pełną ścieżką jego raportu, i uruchamia skrypt ponownie, aż nic nie zostanie wypisane. Sprawdzenie powtarza się przed każdym zarchiwizowaniem zapisu: przy otwarciu requestu, przy korekcie po Twoich uwagach, która archiwizuje zapis jeszcze raz, i przy requeście otwieranym jako zablokowany.

Uwagi stoją teraz w zapisie w jednej stałej formie: jeden punkt zaczynający się od „Process remarks on the-way” i wpisy wcięte pod nim, po jednym na każdą pozycję każdego raportu etapu. To forma, którą nocny przegląd już wycina, więc w przeglądzie nic się nie zmienia. Mówi o tym szablon zapisu, a zapis nie ma osobnej sekcji ani pliku na uwagi.

Uruchomiłem skrypt na trzech prawdziwych archiwach z Twojego drugiego repozytorium. Wypisuje pozycje, które opisałeś: krok powrotu w pierwszym, uzgodnienie z główną gałęzią i jego recenzję w drugim, ostatnią poprawkę kawałka i drugą korektę w trzecim. W tych trzech zapisach brakuje odpowiednio siedmiu, sześciu i ośmiu pozycji. Jedna liczba różni się od Twojego zadania: zadanie mówi, że dwa raporty drugiego archiwum mają po dwie pozycje, a skrypt znajduje po trzy, i wszystkie są prawdziwe i brakuje ich w zapisie. Tak jak wybrałeś, wiersz w rodzaju „none found” z dalszym tekstem liczy się jako pozycja, więc nocny przegląd zobaczy trochę więcej szumu.

Jeśli prowadzący cykl uzna wypisaną pozycję za błąd skryptu, skryptu nie poprawia się w tym cyklu, a archiwum i tak jest zapisywane. Przypadek trafia do uwag i do tej części requestu, żebyś o nim zdecydował.

*Pod spodem:* jeden nowy skrypt z testami oraz zmiany w instrukcjach cyklu i w szablonie zapisu; trzy decyzje, które przyjąłeś razem z zadaniem, są zapisane w dzienniku decyzji.

**Do Twojej decyzji**

1. **Wypisana pozycja uznana za błąd skryptu nie zamienia requestu w szkic.** Napisałeś, że ten przypadek ma przebiegać „tak jak przy sprawdzeniu układu”. Gdy sprawdzenie układu zgłasza błąd, który cykl uważa za fałszywy, request zostaje szkicem. Autor zostawił request w stanie, jaki ma z innych powodów, bo Twoje zadanie wymienia trzy kroki (zapisać archiwum, wpisać przypadek do uwag, pokazać go tutaj) i nie mówi o szkicu. Request oznaczony jako gotowy może więc nieść taki punkt, a jego pierwsza linia mówi, czy coś czeka. Przyjmujesz to, czy taki request ma być szkicem jak przy sprawdzeniu układu? (Drobne uwagi, 2)
2. **Szablon zapisu wymienia skrypt nocnego przeglądu.** Żeby wyjaśnić, skąd taka forma uwag, szablon wymienia skrypt nocnego przeglądu, który leży w Twoich prywatnych notatkach poza tym repozytorium. Nic w repozytorium go nie sprawdza, a nowy skrypt ma własną kopię sposobu, w jaki tamten skrypt wycina blok, więc późniejszej zmiany skryptu nocnego tu nie zauważymy. Zostawiamy tę wzmiankę, czy ją usuwamy? (Zmiany techniczne, 3)
3. **Krótką pozycję może przykryć dłuższa uwaga.** Skrypt uznaje pozycję za obecną, gdy jej słowa stoją gdziekolwiek w uwagach, więc krótka pozycja w rodzaju „none found.” przeszłaby, gdyby zawierała ją dłuższa uwaga innego raportu. Twoje archiwa mają krótkie pozycje, na przykład „Otherwise none.” w siedmiu raportach. Taka pozycja nie zostałaby wypisana, więc nie trafiłaby do nocnego przeglądu, a to jest dokładnie strata, z którą to zadanie walczy. Robimy z tego zadanie? (Drobne uwagi, 1)

**Koszt**

Około 28 minut pracy. Prowadzący cykl i wszyscy agenci pracowali na jednym modelu, Claude Sonnet 5.5, i zużyli łącznie 21,7 mln tokenów, z tego 20,8 mln to wejście czytane z pamięci podręcznej, a 0,16 mln to wyjście. Rundy przeglądu: cała zmiana przejrzana raz i przeszła, bez poprawki. Krok powrotu nie zrobił żadnego commitu, więc nie wymagał przeglądu. Tabela etapów: https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/stage-remarks-check/stages.md

**Jak scalić**

Commitem scalającym, nie przez squash ani rebase: link do zapisu cyklu wskazuje commit na tej gałęzi i przetrwa tylko wtedy, gdy commity zostaną zachowane.

</details>

## Technical changes

1. **The cycle gets a script that lists what the remarks lack.** `2a4847e`: `task-cycle/remarks_check.py` (new, standard library only) reads `reports/*report.md` of a record in name order, takes the **Searches not found or unclear** section in both forms (a heading of any level, or a bold label with its colon inside, outside or absent, at a line start or as a list item), splits it into items, drops the items that read `none`, and lists each other item that the record's process remarks do not hold word for word, as `<report path>: <item>` plus a last line `checked: …`. It only lists and writes nothing; exit 0 nothing missing, 1 something listed, 2 a call it cannot serve. `task-cycle/test_remarks_check.py` (new, 137 tests in `task-cycle` after it): fixtures stand in the test file, written first against a stub; they cover both forms, the `none` readings, repeated items, the block the digest cuts and the template's form.
2. **The cycle's instructions call the script before every archive.** `2a4847e`: `task-cycle/skill/SKILL.md` gains "The process remarks check" (run, append each listed item word for word with the stage name and the full report path, run again until exit 0, record the run under *Verification*; and "A listing you hold wrong": script not changed, archive written, case in the remarks and in *For you to decide*, check named in *Checks*); step 12 runs it after `cycle_stages.py` and before the description is written, and step 9 sub-step 4 (a slice failed twice) points to it. `task-cycle/skill/correction.md`, `blocked_finding.md` and `reserved_return.md` each point to it before the commit that adds the record. `task-cycle/skill/request_template.md` gains item 10 of *For you to decide*, a mention under *Checks* and a variant row.
3. **The record template fixes one form of the remarks.** `2a4847e`: `task-cycle/record_template.md`: the block is the list item `- Process remarks on the-way: …` with one entry `- <stage name>, <full report path>: <item>` indented under it, and an `<the orchestrator>: …` entry for the orchestrator's own remarks; it is the last item of the record. The template names `cycle_remarks_digest.py` of the nightly review in the paragraph that says why (the second item of *For you to decide*).
4. **Three decisions are written.** `5e90498`: WAY-294, WAY-295, WAY-296 at the end of `foundations/decisions.md`, from rows 1–3 of the task (see *Foundation entries*). The return step compared them, the entries the task names and the part map with the code and changed nothing.

## Checks

1. **The full test run passed on the base and on the tree that goes into this request.** `python -B gate/run_tests.py`: on the base `b96cfff`, exit 0, 667 tests in 8 directories; on the reviewed change `5e90498`, which is also the final tree, exit 0, 712 tests in 8 directories. The return step made no commit and `origin/foundations` had not moved from `b96cfff` (`git fetch`), so no merge and no second run were needed. No check failed on the base or on the change; the 5 tests skipped in `instruction-files` skip themselves, as on the base.
2. **The foundation check and the focused runs exited 0.** `python -B elements/common/foundation_check.py`: exit 0, `0 errors`, by the author and by the reviewer. `python -B gate/run_tests.py task-cycle`: exit 0, 137 tests, by the author, the reviewer and the return step.
3. **The script found what the task describes in the three real archives.** The archives were read with `git show` from the other repository and never checked out. `python -B task-cycle/remarks_check.py <extract>`: exit 1 on each; summary lines `plomyk@31ac651`: 3 reports, 13 items other than `none`, 7 not in the process remarks; `reset-hasla@b311814`: 38 reports, 84 items, 6 missing; `kopia-bazy@d79c8e4`: 41 reports, 129 items, 8 missing. They include the return step of `plomyk`, reports 37 and 38 of `reset-hasla` (three items each, the task says two), and the last fix of slice 6 and the second correction of `kopia-bazy`. The script also lists three items of `plomyk` that stand in the record as a second entry the nightly digest does not cut, and in `kopia-bazy` three entries that begin `none. …` or `none for the code; …`, by the literal rule "other than `none`". The first archive of `kopia-bazy` (`67620ff`) lists 5 items.
4. **Own-work checks.** The author named as the requirement most likely unmet that the script finds every item of the real reports in the forms agents write. It counted the items of four extracts a second way: every report has the section, the 13 reports with no item all read `none`, and the counts agree except five reports whose extra items a bullet count cannot see (`none. Note: …`, a trailing paragraph); it also showed that a byte-order mark hides a first-line section, which the author fixed and covered with a test. The reviewer imported the real digest script read-only and compared the blocks it cuts with the script's on `cycle.md` of the three archives and on the record template: equal in all four. Four mutations of the script run by the reviewer (remarks taken as the whole `cycle.md`, the `none` test as `startswith`, exit code always 0, block cut to its first line) were each caught by the tests; the author's mutations were caught but one: dropping the sort of the report names, which cannot be observed on Windows.
5. **No user interface changed:** no states or screenshots apply.
6. **The form of the process remarks of this cycle was checked by the script.** `python -B task-cycle/remarks_check.py .runs/task-cycles/stage-remarks-check`: the first run exit 1 with 10 items listed, all appended; the last run exit 0, `checked: 3 reports, 10 items other than none, 0 not in the process remarks`. No listing was held wrong.
7. **The form of this description was checked by the script.** `python -B task-cycle/request_check.py .runs/task-cycles/stage-remarks-check/request.md --task .runs/task-cycles/stage-remarks-check/task.md`: exit 0, 1 run before the record's link was added.

## Foundation entries

Each entry this request writes, with one English sentence of its meaning. No invariant test, surface or *Violated* mark changes. No kept row was tied to an entry already stated. No entry is marked `the cycle's`: all three come from rows of the task.

1. **WAY-294 (new), row 1.** Before every commit that adds a cycle's record to its archive, the orchestrator runs the-way's script that lists each item other than `none` of the stage reports that the record's process remarks lack, appends each listed item and runs the script again until it lists nothing.
2. **WAY-295 (new), row 2.** A listing the orchestrator holds to be an error of the script neither stops the archive nor changes the script in that cycle: the archive is written, and the case goes into the process remarks and into the request's section for the human's decisions, narrowing WAY-294.
3. **WAY-296 (new), row 3.** The process remarks of a record stand in the one form the record template gives and the script reads, not in a section or a file of their own.

## Minor findings

1. **The match is a substring match over all remark blocks, so a short item can be masked by longer text of another entry.** M1 of the whole-change review, at `5e90498`, `task-cycle/remarks_check.py:315` and `:328` (`remarks.count(item)`), `:330`: "The remarks are one joined string and an item is "held" when it occurs anywhere in it as a substring, with no boundary at the start or end of an entry. An item of one report that is a substring of another entry's text counts as held. Evidence (scratch record, outside the worktree): `cycle.md` holds one entry `stage a, <path>: A source outside the product: none found.`; report a gives that item, report b gives the bare item `none found.`; `python -B task-cycle/remarks_check.py <record>` prints `checked: 2 reports, 2 items other than none, 0 not in the process remarks`, exit 0, although no entry for report b exists. In the real archives there are short items (`reset-hasla`: eight items below 60 characters, e.g. `Otherwise none.` in seven reports), so the case can occur. Why it matters: a missing item hides, which is the failure the task fights; but it needs a short item, the task asks for "word for word inside the block" (a containment reading), and the repeat count already covers identical items. Not blocking. A fix, if wanted, is to require the item to stand at the end of an entry line (after `: ` or at a line start) in new-form records."
2. **A listing held wrong leaves the request state unchanged, where the task's row 2 says "as with `request_check.py`".** M2, at `5e90498`, `task-cycle/skill/SKILL.md` ("A listing you hold wrong") and `task-cycle/skill/request_template.md` (variant row "A remarks listing held wrong"): "WAY-291, which row 2 points to, makes the request a draft whose human-decision section names the error. The change copies the rest of that rule (script not changed, archive written, case in the remarks, item in *For you to decide* with "Merge as it stands?", *Checks* names the check) but keeps the request's state "unchanged", as the author's report states and gives the cost of. The task's words for the rule (row 2 and *To do* 2) name the three steps the change does and no draft state, so this is within the task; it is a choice the human may want to see. Equality with row 2 otherwise holds (see Checks of the task below)."
3. **The script prints a non-printable character as an escape, but the orchestrator is told to copy the printed item word for word.** M3, at `5e90498`, `task-cycle/remarks_check.py:85-87` and `:347` (`display()`): "A report item with a character that `str.isprintable` rejects and `str.split` does not treat as whitespace (for example U+200B) is printed as an escape (`​`); the copy would not match the original and the script would list it again for ever. Whitespace-like characters (NBSP included) are collapsed to a space first, so the real archives are not affected (I saw no such character in the listed items of the three archives, but did not scan every item). Rare; the held-wrong rule is the way out."

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** "the way: braki zgłoszone przez etapy, które pracują pod koniec cyklu, trafiają do zapisu cyklu tak jak braki z wcześniejszych etapów", an independent task, from `zadanie_the_way_pozne_etapy_w_uwagach_rekordu.md` in the author's notes, `Status: ready for cycle`, settlements accepted 2026-11-05; its citations stand at `foundations` `61c72fb`, and the branch starts from `origin/foundations` `b96cfff`, five commits later (pull request 72 touched the cycle's skill and the record template, and the script and the edits sit on top of it). It reads the three archives `31ac651`, `b311814` and `d79c8e4` of the other repository.
- **Process pin:** none; the-way working on itself, the process root this worktree.
- **Spec:** none. The task leaves no open design choice: *To do* and rows 1–3 of *Settlements to record* fix the check, the order of its run, the rule for a listing held wrong and the single form of the remarks; how the script reads and matches is a choice of how to make what the task settles.
- **Route:** one author without a plan, class `same` (Sonnet 5.5): the change writes decision entries and reads report forms found in real archives, so it is more than ordinary implementation.
- **Plan:** none.
- **Choices:** twelve other choices (Q1–Q8 and Q10–Q13) in the questions table of the record's `cycle.md`; Q9 stands above as item 1 of *For you to decide*.
- **Blocking findings left:** none.
- **Record:** the cycle's record at the commit that adds it, `RECORD_SHA`: https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/stage-remarks-check (`cycle.md` for the log, `reports/` for the handoffs and reports).
