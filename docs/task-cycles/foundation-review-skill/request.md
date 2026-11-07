**State: ready** — the change is finished and checked; eleven points below wait for your yes, one of them an action only you can do.

## What you will see

The process gets a way to review the whole foundation of a repository, and a reminder that it is time. The way to review is a new skill, started by you in a session in one repository. It reads the whole foundation, not a list of conditions: it compares facts about the environment with their sources, and the weak points, prices and accepted risks that the decisions name with the state of the product today, running a missing check where that is cheap and by reading alone. It also checks every remark that the requests merged since the last review left unfixed, including the ones a request asked you about at the merge (but not one whose answer is written down). It then lists proposals, hands the whole set to the critique skill, and goes through them with you one at a time, remarks in groups; a proposal you accept becomes a task in the backlog, small ones go into collective tasks, and the review itself changes nothing in the foundation or the code. At the end it puts a tag on the checked commit, and pushes it only on your yes.

The reminder works like this: at the end of every cycle the orchestrator counts the merges to the main branch since the last review tag (from the start of the history where there is no tag). From 30 merges the description of the request says that the foundation waits for a review, with the count, the last tag and the command; it blocks nothing, and the number is the same for every product. This request carries no reminder: the count is 1, since the first review tagged the commit just before. The decision about review in the log now says that the review is a run of the skill that the reminder asks for, not a task of the backlog.

### Underneath

A new part of the repository, with its own directory, holds the skill; a small script with a test does the counting, so the 30 and the two git commands stand in one place; six new decisions and three changed ones carry the rules.

## For you to decide

1. The task asks you to move the "carrier" of row L7 in your list of articles to the number of the decision that carries the reminder. That decision is the one listed first under *Foundation entries* as the reminder's. You do it when you merge, since the number is known only now; the request stays open for review meanwhile, and the cycle changes nothing outside the repository. Done at the merge? (Foundation entries, 2)
2. The task says the review keeps its remark lists in one data file but not where, and that accepted proposals become tasks but not how. The skill keeps the file in the product's private task area, named with the date of the review, not in the repository, which may be public; it makes a task as an entry plus a task document in the state "refining", or hands you the text where it cannot write there. Accept? (Technical changes, 2)
3. The task says the skill puts a tag, but not whether pushing needs your say. The skill pushes the tag only after your yes, and puts it only when you have decided every proposal and group, so a half review leaves no tag. The tag marks the commit read at the start of the session. Accept? (Technical changes, 2)
4. The task gives the start of the first review of one product as a date. The skill has no date: the first review of a repository starts after the request you name, and the decision says so. This widens what the task stated for one product. Accept? (Technical changes, 2)
5. The skill lives in a new part of the repository, and the counting is a script with a test, not text left to the orchestrator. The cost if wrong is one rename of a directory and a part. Accept? (Technical changes, 1)
6. The list of directories the repository may hold now names the new directory, and the part map lets the installer depend on the new part, since the installer names the skill by its path and now installs it into products. You had not seen these changes. Accept? (Foundation entries, 8 and 10)
7. The sentences of the foundation that called the review of the foundation a task of the backlog now say it is a place where a moved source is found, in the decision about environment facts and in the template that repeats it. You had not seen these changes. Accept? (Foundation entries, 9)
8. A repository cloned without its tags would read "no tag" and count from the start of its history, so a false reminder could appear. The cycle's text says "after a fetch" but not "with tags". Make a task of it? (Minor findings, 3)
9. The correction after your remarks and the two blocked variants of the description do not tell the orchestrator to count again, so a corrected request may lose the reminder or keep a stale one. Make a task of it? (Minor findings, 7)
10. In a product that squashes or rebases its merges there is no merge commit to count, so its reminder would never appear. The task fixed the two git commands, so this was not changed. Make a task of it? (Findings outside the task's scope, 2)
11. A change to the-way made by hand, without a cycle, gets no reminder, since the decision binds the end of a cycle and the hand-made route is silent on it. Make a task of it? (Findings outside the task's scope, 3)

## Cost

About 41 minutes of working time, one model (Sonnet 5.5), 36.8 million tokens, two reviews: one of the whole change, which found one problem, and one of the fix; [the table of stages](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/foundation-review-skill/stages.md).

## How to merge

Merge with a merge commit, not a squash or a rebase, so that the link to the record of the cycle keeps working.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — zmiana jest skończona i sprawdzona; na twoje „tak” czeka jedenaście punktów niżej, w tym jedno działanie, które możesz wykonać tylko ty.

## Co zobaczysz

Proces dostaje sposób na przegląd całego fundamentu repozytorium i przypomnienie, że pora. Przegląd to nowy skill, który uruchamiasz w sesji w jednym repozytorium. Czyta cały fundament, a nie listę warunków: fakty o środowisku porównuje z ich źródłami, a słabe punkty, ceny i przyjęte ryzyka z uzasadnień decyzji z dzisiejszym stanem produktu, uruchamiając brakujące sprawdzenie tam, gdzie jest tanie i samym odczytem. Sprawdza też każdą uwagę, którą scalone od ostatniego przeglądu requesty zostawiły niepoprawioną, także tę, o którą request pytał cię przy scaleniu (ale nie tę, której odpowiedź jest zapisana). Potem spisuje propozycje, oddaje cały zestaw do krytyki i prowadzi cię przez nie po jednej, a uwagi grupami; propozycja, którą przyjmiesz, staje się zadaniem w backlogu, drobne trafiają do zadań zbiorczych, a sam przegląd niczego w fundamencie ani w kodzie nie zmienia. Na koniec stawia tag na sprawdzonym commicie i wypycha go dopiero na twoje „tak”.

Przypomnienie działa tak: na końcu każdego cyklu orkiestrator liczy scalenia do gałęzi głównej od ostatniego tagu przeglądu (od początku historii, gdy tagu nie ma). Od 30 scaleń opis requestu mówi, że fundament czeka na przegląd, i podaje liczbę, ostatni tag i komendę; niczego to nie blokuje, a liczba jest taka sama dla każdego produktu. Ten request przypomnienia nie niesie: liczba to 1, bo pierwszy przegląd oznaczył tagiem commit tuż przed nim. Decyzja o przeglądzie w dzienniku mówi teraz, że przegląd to uruchomienie skilla, o które prosi przypomnienie, a nie zadanie backlogu.

### Pod spodem

Skill trzyma nowa część repozytorium z własnym katalogiem; liczy mały skrypt z testem, więc 30 i dwie komendy gita stoją w jednym miejscu; reguły niosą sześć nowych decyzji i trzy zmienione.

## Do twojej decyzji

1. Zadanie prosi, byś przestawił „nośnik” wiersza L7 na liście artykułów na numer decyzji, która niesie przypomnienie. To decyzja podana jako pierwsza w sekcji *Foundation entries* jako ta od przypomnienia. Robisz to przy scaleniu, bo numer jest znany dopiero teraz; request do tego czasu czeka na przegląd, a cykl niczego poza repozytorium nie zmienia. Zrobione przy scaleniu? (Foundation entries, 2)
2. Zadanie mówi, że przegląd trzyma listy uwag w jednym pliku danych, ale nie gdzie, i że przyjęte propozycje stają się zadaniami, ale nie jak. Skill trzyma plik w prywatnym obszarze zadań produktu, nazwany datą przeglądu, a nie w repozytorium, które bywa publiczne; zadanie zakłada jako wpis i dokument zadania w stanie „doprecyzowanie” albo podaje ci tekst, gdy nie może tam pisać. Akceptujesz? (Technical changes, 2)
3. Zadanie mówi, że skill stawia tag, ale nie czy wypchnięcie wymaga twojego słowa. Skill wypycha tag dopiero po twoim „tak” i stawia go tylko wtedy, gdy rozstrzygnąłeś każdą propozycję i grupę, więc przegląd urwany w połowie tagu nie zostawia. Tag oznacza commit odczytany na początku sesji. Akceptujesz? (Technical changes, 2)
4. Zadanie podaje początek pierwszego przeglądu jednego produktu jako datę. Skill daty nie ma: pierwszy przegląd repozytorium zaczyna się po requeście, który wskażesz, i mówi to decyzja. To poszerza to, co zadanie ustaliło dla jednego produktu. Akceptujesz? (Technical changes, 2)
5. Skill leży w nowej części repozytorium, a liczenie to skrypt z testem, a nie tekst zostawiony orkiestratorowi. Koszt pomyłki to jedna zmiana nazwy katalogu i części. Akceptujesz? (Technical changes, 1)
6. Lista katalogów, które repozytorium może zawierać, wymienia teraz nowy katalog, a mapa części pozwala instalatorowi zależeć od nowej części, bo instalator wskazuje skill ścieżką i instaluje go teraz w produktach. Tych zmian nie widziałeś. Akceptujesz? (Foundation entries, 8 i 10)
7. Zdania fundamentu, które nazywały przegląd fundamentu zadaniem backlogu, mówią teraz, że to miejsce, w którym znajduje się przesunięte źródło — w decyzji o faktach o środowisku i w szablonie, który ją powtarza. Tych zmian nie widziałeś. Akceptujesz? (Foundation entries, 9)
8. Repozytorium sklonowane bez tagów przeczyta „brak tagu” i policzy od początku historii, więc może pokazać fałszywe przypomnienie. Tekst cyklu mówi „po pobraniu” (fetch), ale nie „z tagami”. Zrobić z tego zadanie? (Minor findings, 3)
9. Korekta po twoich uwagach i dwa warianty zablokowanego opisu nie każą orkiestratorowi liczyć jeszcze raz, więc poprawiony request może stracić przypomnienie albo zachować nieaktualne. Zrobić z tego zadanie? (Minor findings, 7)
10. W produkcie, który scala przez squash albo rebase, nie ma commitu scalającego do policzenia, więc jego przypomnienie nigdy by się nie pojawiło. Zadanie ustaliło dwie komendy gita, więc tego nie zmieniono. Zrobić z tego zadanie? (Findings outside the task's scope, 2)
11. Zmiana w the-way zrobiona ręcznie, bez cyklu, nie dostaje przypomnienia, bo decyzja wiąże koniec cyklu, a ścieżka ręczna o tym milczy. Zrobić z tego zadanie? (Findings outside the task's scope, 3)

## Koszt

Około 41 minut pracy, jeden model (Sonnet 5.5), 36,8 miliona tokenów, dwa przeglądy: jeden całej zmiany, który znalazł jeden problem, i jeden poprawki; [tabela etapów](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/foundation-review-skill/stages.md).

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase’em, żeby link do zapisu cyklu dalej działał.

</details>

## Technical changes

1. The merge-count script and its test (commit `46ae3b9`): `task-cycle/review_reminder.py` takes the branch, finds the nearest `foundation-review/*` tag reachable from it (none counts from the start of history), counts `git rev-list --merges --first-parent` since the tag, compares with 30 and prints `tag`, `merges`, `threshold` and `reminder`. `task-cycle/test_review_reminder.py` builds histories and holds nine cases, among them that a merge of the main branch into a task branch does not count and that the reminder starts at 30, not 29. The author saw the tests fail on a stub, restored `--first-parent` and `>=` after trying them as mutations, and the tests caught both.
2. The skill and the choices of its text (commit `dcf04d2`): `foundation-review/SKILL.md` with four files read at the step that needs each (`weak_points.md`, `remarks.md`, `proposals.md`, `with_the_human.md`), the installer line `installation/install.py` so that products get the skill (21 skills, 42 entry points), the regenerated entry points under `.claude/skills/` and `.agents/skills/`, and `README.md`. Choices the task did not settle, all in the author's report: the data file's place and name, how a task is made in a backlog, the push of the tag on a yes and no tag for an unfinished review, the checked commit being the tip read at the start, the first review starting after the request you name.
3. The reminder in the cycle (commit `0ef44b0`): step 13 of `task-cycle/skill/SKILL.md` runs the count after a fetch, and the end of *How to merge* in `task-cycle/skill/request_template.md` carries the reminder where the count reads `reminder: yes`. `task-cycle/request_check.py` needed no change.
4. The decisions and the part (commit `45d294f`): WAY-24 rewritten; WAY-300 to WAY-305 added; WAY-09 and WAY-82 changed; part `foundation-review` in `foundations/part_map.md`; the sentence in `elements/environment-facts/template.md`. Three installation tests moved their expected count of entry points from 40 to 42 (commit `02ca017`), the assertion kept. After the review, the tag message was made to read the same in WAY-301, the skill and `weak_points.md` (commit `34a206f`).
5. Not changed: `elements/common/migrate_foundation.py:436` still names "the task of the periodic review of the foundation" in a message of the migration of the old form; the author left it as text of a one-off migration.

## Checks

- The full gate, `python -B gate/run_tests.py`, on the final tree `34a206f`: exit 0, 765 tests in 9 directories, every directory passed (the base `86cc21e`: exit 0, 756 tests; nine tests are new). No check failed or did not run on it.
- One check failed in a cycle run and passed again: `python -B gate/run_tests.py installation`, run by the author on the first commits, failed once (3 tests held 40 entry points, the product now gets 42), failed in 1 run and passed in 2 (the author's rerun after the fix in `02ca017`, and the final gate); the file belongs to the part `installation`, which the change touches.
- `python -B elements/common/foundation_check.py`: exit 0, 0 errors, run by the author, the reviewer, and again by the author after the fix.
- `python -B task-cycle/review_reminder.py origin/foundations` on the final tree: exit 0, `tag: foundation-review/2026-11-06`, `merges: 1`, `threshold: 30`, `reminder: no`.
- Own-work check of the author: the requirement that every place which restates the review of the foundation says it is a run of the skill, not a backlog task; a search for the old wording and for "backlog" beside it showed no leftover but the two places named under *Technical changes*, 5, and a sample description with the reminder passed the form check. After the fix: a search for "entries checked" and "entries and remarks" found nothing left. What was not checked: that a human following the skill gets what its text describes, as the skill has not been run on a repository.
- User-interface states and screenshots: not applicable, no screen changes.
- The form check, `python -B task-cycle/request_check.py docs/task-cycles/foundation-review-skill/request.md --task docs/task-cycles/foundation-review-skill/frozen_task.md`: last run exit 0, `form holds`, after 3 runs (the first and the second after the record's links were set)
- The remarks check, `python -B task-cycle/remarks_check.py .runs/task-cycles/foundation-review-skill`: last run exit 0 and nothing listed, after 2 runs (the first listed 11 items, now in the record's process remarks; the reports of the two reviewers are named `review_*.md`, not `*report.md`, so the script does not read them and their items were copied by hand)

## Foundation entries

1. `WAY-24` (changed), `row 1`: the review of the foundation against the product is a run of the skill that a human starts in a session when a request's reminder asks for it, not a task of the backlog; its *Rejected* gains the ways the task keeps, and row 1 is tied to this entry, which writes no second one.
2. `WAY-300`, `row 2`: at the end of every cycle the orchestrator counts the merges since the last review tag, and from 30 merges the request's description reminds the human, without blocking anything; the number is one for every product and a repository with no tag counts from the start of its history. This is the decision whose number row L7 of the list of articles takes (*For you to decide*, 1).
3. `WAY-301`, `row 3`: the last review is marked by an annotated tag on the checked commit, put also when nothing changed, with a message of the number of items checked and no title of a task or of a private note.
4. `WAY-302`, `row 4`: a review goes analysis, proposals, critique of the whole set, then one proposal at a time with the human and remarks in groups; accepted proposals become backlog tasks, small ones collective tasks, and the review changes nothing in the foundation or code.
5. `WAY-303`, `row 5`: the review checks every unfixed remark of its own repository's requests merged since the last tag, the question put to the human at the merge included, and raises again none whose answer is written down.
6. `WAY-304`, `row 6`: one skill serves every product and a review is made per repository; the review of the-way reads a product's requests only for evidence about the-way's decisions, and a repository's first review starts after the request the human names.
7. `WAY-305`, `row 7`: the review compares the weak points, prices, gaps and accepted risks named in decisions' rationales with the product's state today and runs the missing check where it is cheap and by reading alone.
8. `WAY-09` (changed), `the cycle's`: the directory of the new part `foundation-review/` is named among the directories the repository may hold.
9. `WAY-82` (its rationale) and the sentence of `elements/environment-facts/template.md` that repeats it, `the cycle's`: the review of the foundation is named as a place where a moved source is found, without calling it a backlog task.
10. The part map (`foundations/part_map.md`): new part `foundation-review`, and `installation` gains it in *Depends on*, `the cycle's`: a new part answers for the review of a foundation; the installer, which names its skill by path, may depend on it.

Row 1 is tied to the entry already stated (`WAY-24`), as the foundation step gives. No invariant test, surface or *Violated* mark is changed, and no invariant, environment fact or glossary entry is written: no row or decision sets such a rule, no decision cites an outside source in *Based on*, and no word is used in another meaning than its ordinary one.

## Minor findings

The Minor findings of the review of the whole change, in the reviewer's words, each with its place; none was fixed, and the review of the fix named no new one.

1. `foundation-review/SKILL.md` step 1, `git rev-list --merges --first-parent <tag>..<main branch>` and the no-tag form `... <main branch>`: the task's *Context* says that in the-way the main branch is spelled `foundations --` because a directory has the same name. The skill drops that. Evidence: in this worktree `git rev-list --merges --first-parent --count foundations` printed "ambiguous argument ... Use '--' to separate paths from revisions" (exit 128), while `... origin/foundations` printed 86 and `... foundation-review/2026-11-06..foundations` printed 1. Only a bare name with no range is ambiguous, so in the-way (which has a tag) it bites only a review with no tag, but the skill is the one place a future agent reads. Say `origin/<main branch>` or add `--`. (`task-cycle/review_reminder.py` is not affected: the cycle passes `origin/<target branch>`.)
2. `task-cycle/test_review_reminder.py`, `test_a_branch_name_that_looks_like_an_option_is_an_error` does not reach the guard it names. The argument `--output=x` is rejected by argparse ("the following arguments are required: BRANCH"), so the `branch.startswith("-")` guard in `review_reminder.count` is never executed by the test: deleting the guard would leave the test green. Evidence: `python -B task-cycle/review_reminder.py --output=x` printed `Error: the following arguments are required: BRANCH`, exit 2; with `-- -x` it printed `Error: '-x' is no branch name`, exit 2 (the guard). The script's behaviour is right; the protection is untested. A test that passes `main`-less `["--", "-x"]` would cover it.
3. `task-cycle/review_reminder.py`, `last_review_tag`: any non-zero exit of `git describe` is read as "no tag", not only "No names found". The count then runs from the start of history and can read `reminder: yes` falsely (for instance in a clone where tags are not fetched). `rev-parse` before it covers a bad branch, so the exposure is a repository whose tags are missing; the cycle step 13 says "after a fetch" but not "with tags". Say so in step 13 or tell the two cases apart.
4. `foundations/decisions.md`, WAY-300 *Rejected*: "running into the daily scan" names a routine of the human that no foundation entry defines, in a file a public repository can hold. A reader of the decision cannot read it; the other outside reference in that sentence ("an outside harness") is anonymised. Say "the human's existing daily review" with a clause, or drop the phrase.
5. `foundations/decisions.md`, WAY-24 *Verification* "violates": "the review is set as a task of the product's backlog with a date" is narrower than the binding sentence ("no task of the product's backlog"), so a task with no date reads as complying. And WAY-302 *Verification* "complies" says "the remarks about one guide gather into one collective task", where no guide is defined. Both are wording of a test line for a reviewer; neither changes what the entry binds.
6. `foundation-review/remarks.md`, "Which remarks": "A remark about the process itself, taken from a cycle's record, is not read: another review collects those." The task excludes these remarks (question 11, category B) because the human's nightly review of the AI layer collects them. In a generic skill for any product the sentence asserts a collector that a product may not have, and nothing in the foundation names it. Say the kind is out of this review's reading and leave it there.
7. Reminder in the cycle's other request variants: `task-cycle/skill/request_template.md` says "Where the count of `SKILL.md` step 13 reads `reminder: yes`" and step 13 says the request "the cycle writes or rewrites gets it while the count stands", but `task-cycle/skill/correction.md` (the rewrite for the human's remarks) does not tell the orchestrator to count again, and the variants table of the template for a blocked or reserved request gives *How to merge* as "do not merge, close" without saying whether the reminder still ends it. `reserved_return.md` and `blocked_finding.md` send the writer through "step 13", which includes the count, so a diligent orchestrator gets there; the correction path and the blocked variants are left to inference. WAY-300 says "each request the cycle writes". I judged it Minor because step 13 is named from each path but the correction path does not recount.

## Findings outside the task's scope

The reviewer marked no finding as outside the task's scope. These are the points it set aside as not judged, from its "Declined to judge" section:

1. Set aside by the reviewer of the whole change ("Declined to judge"): "The skill has never been run on a repository; whether a human following it gets what the text describes cannot be settled by reading. Outside the task's reach to settle before a first run." The reviewer names no place in the code.
2. Set aside by the reviewer of the whole change ("Declined to judge"): "A product that squashes or rebases its merges reads 0 merges and gets no reminder (the author's report, "Searches"). The task's *Context* fixes the two git commands and the request template already names the limitation for the merge; the skill tells such a product to read the host's list for the review itself. Outside the task." The reviewer names no place in the code.
3. Set aside by the reviewer of the whole change ("Declined to judge"): "A change to the-way made under `agent-instructions/README.md` with no cycle gets no reminder, since WAY-300 and the task bind "the end of every cycle". The README sends that writer to the template but not to the count. Outside the task; a decision for the human whether the README should say so." The reviewer names no place in the code.
4. Set aside by the reviewer of the whole change ("Declined to judge"): "The wording of WAY-300's rationale on the review intervals (the numbers come from the task's question 2 and I did not recompute them from the history of git)." The reviewer names no place in the code.
5. Set aside by the reviewer of the whole change ("Declined to judge"): "The 42 regenerated entry points under `.claude/skills/` and `.agents/skills/` (44 files): generated; I checked the generator's `--check` mode and the new entry point whole, and read one regenerated sibling's diff (one added name in its list)." The reviewer names no place in the code.

No check whose file belongs to a part outside the task's parts failed in a cycle run and passed again.

## Course of the cycle

- **Task and sources:** a skill for the review of a repository's foundation and of the unfixed remarks of its requests, with a reminder after 30 merges; an independent task, `Status: ready for cycle` (the document updated 2026-11-07). Sources: `foundations` at `86cc21e`; the first review's data file and the list of predictions in the author's private notes, read for form only.
- **Process pin:** not applicable; this is the-way itself, so the checkout is the process. The gate on the base `86cc21e`: exit 0, 756 tests.
- **Spec:** none; the task leaves no open design choice, since it settles the skill, the tag, the threshold, the place of the reminder and rows 1 to 7; what is left is how to make them (the author's choices below).
- **Route:** one author without a plan, on the class `same` as the orchestrator, because the change crosses many parts and has to take decisions of its own about a skill's shape. The fix and the return step were made by the same author, resumed; the return step made no commit. The cycle ran the product's gate once, on the final tree after the return step, not before and again after, since the return step could change the tree.
- **Plan:** none.
- **Choices:** 12 beyond the task's content, in [the questions table of the record](https://github.com/mariusznazar/the-way/blob/RECORD_SHA/docs/task-cycles/foundation-review-skill/cycle.md#questions-and-autonomous-choices): the author's nine choices and three of the orchestrator, among them that this request is marked ready although the task places one human action in the cycle, since that action can only be done at the merge.
- **Blocking findings left:** none; the one blocking finding of the review of the whole change was fixed and the fix reviewed `PASS`.
- **Record:** [the committed record](https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/foundation-review-skill), by the SHA of the commit that adds it.
