**State: ready** — corrected for your remarks; two items below wait for your yes

## What you will see

From now on the cycle of a task no longer publishes the layout of your disk, the titles of your private notes or the names of your worktrees in the repository's history. Before the record of the cycle is committed, the cycle rewrites its copy: every path on your disk becomes a path inside the repository, and every private note is described instead of pointed to. A new check script lists, by pattern, each path that starts at a drive letter or a home directory and each note link written in double square brackets. The cycle fixes what the script lists and runs it again, until it lists nothing. The same check runs on the description of every request before it is published, the Polish block included. Commit messages are not checked, and neither is a private name written as plain words.

Your decision on the first version of this request is carried out. The new rule had made one exception: two lines of the record, the ones that tell the plan reader which plan a task belongs to, were to stay as they are even when the check listed them. You chose to drop it. Now a line the check lists is cleaned like any other, and nothing the check lists is ever committed. When that happens, the request says so in its list of questions to you, because the plan reader may then report a conflict for that task. In this cycle the check never listed such a line, so there is no such question below.

### Underneath

The rule is written down as two decisions in the foundation, and the cycle's own steps, the record template and the request template are changed to follow them. The check is a small standard-library script with its own tests. Three tests also pin what the reader of a project plan's state does with a cleaned copy.

## For you to decide

1. A choice the cycle made beyond the task's words. A cleaned copy of a task's record can no longer be tied by the plan reader to its plan row before a human links the frozen copy in that row. For a task that belongs to a project plan the reader then reports the copy as unchecked and proposes no move to done until the link is made. It stops short and does not guess, and an independent task is not affected. Teaching the reader another way to anchor a cleaned copy is a task of its own. Accept it as it stands, or make a task of the reader?
2. Foundation entries the cycle added beyond the task's rows, each one a rule you have not seen before. The second decision says that the second run of the remarks check, on the cleaned copy, narrows the first decision about that check, and that the cleaning is one rewriting of every text file of the copy, so a report and the remarks stay word for word the same. The first decision says that the request tells you when a relation line had to be cleaned. Accept them?

## Cost

@@TIME@@ of work in total across the whole cycle, on one model, claude-sonnet-5-5, with @@TOKENS@@ million tokens counted. Four reviews of the code and one of the return step, two fixes and one correction after your decision. The table of stages is linked in the lower part, under the record.

## How to merge

Merge with a merge commit, which keeps the commits. The link to the record survives only then. The branch merges into the integration branch of the-way; nothing else waits for the merge.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — poprawione po Twoich uwagach; dwie rzeczy poniżej czekają na Twoje tak

## Co zobaczysz

Od teraz cykl zadania nie publikuje w historii repozytorium układu Twojego dysku, tytułów Twoich prywatnych notatek ani nazw Twoich worktree. Zanim zapis cyklu trafi do commita, cykl przepisuje jego kopię: każda ścieżka z Twojego dysku staje się ścieżką wewnątrz repozytorium, a każda prywatna notatka jest opisana zamiast wskazana. Nowy skrypt sprawdzający wypisuje po wzorcu każdą ścieżkę zaczynającą się od litery dysku albo katalogu domowego i każdy link do notatki w podwójnych nawiasach kwadratowych. Cykl poprawia to, co skrypt wypisał, i uruchamia go znowu, aż nic nie wypisze. To samo sprawdzenie przechodzi opis każdego requestu przed publikacją, razem z blokiem po polsku. Wiadomości commitów nie są sprawdzane, nie jest też sprawdzana prywatna nazwa wpisana zwykłymi słowami.

Twoja decyzja z pierwszej wersji requestu jest wykonana. Nowa reguła miała jeden wyjątek: dwie linie zapisu, te, po których czytnik planu poznaje, do jakiego planu należy zadanie, miały zostać bez zmian, nawet gdy sprawdzenie je wypisze. Wybrałeś, żeby go usunąć. Teraz linia, którą sprawdzenie wypisze, jest czyszczona jak każda inna i nic, co sprawdzenie wypisze, nigdy nie trafia do commita. Gdy to się zdarzy, request mówi o tym na liście pytań do Ciebie, bo czytnik planu może wtedy zgłosić konflikt dla tego zadania. W tym cyklu sprawdzenie nigdy takiej linii nie wypisało, więc takiego pytania poniżej nie ma.

### Pod spodem

Reguła jest zapisana jako dwie decyzje w fundamencie, a kroki cyklu, szablon zapisu i szablon requestu są zmienione zgodnie z nimi. Sprawdzenie to mały skrypt na bibliotece standardowej, z własnymi testami. Trzy testy utrwalają też, co robi czytnik stanu planu projektu z oczyszczoną kopią.

## Do Twojej decyzji

1. Wybór, który cykl zrobił poza słowami zadania. Czytnik planu nie umie już powiązać oczyszczonej kopii zapisu zadania z jego wierszem w planie, zanim człowiek podlinkuje w tym wierszu zamrożoną kopię. Dla zadania należącego do planu projektu czytnik zgłasza wtedy kopię jako niesprawdzoną i nie proponuje przejścia na gotowe, dopóki link nie powstanie. Zatrzymuje się i nie zgaduje, a zadanie niezależne nie jest dotknięte. Nauczenie czytnika innego sposobu powiązania oczyszczonej kopii to osobne zadanie. Przyjąć tak, jak jest, czy zrobić z czytnika zadanie?
2. Wpisy fundamentu, które cykl dodał poza wierszami zadania, każdy to reguła, której jeszcze nie widziałeś. Druga decyzja mówi, że drugi przebieg sprawdzenia uwag na oczyszczonej kopii zawęża pierwszą decyzję o tym sprawdzeniu, i że czyszczenie to jedno przepisanie wszystkich plików tekstowych kopii, więc raport i uwagi pozostają słowo w słowo takie same. Pierwsza decyzja mówi, że request informuje Cię, gdy trzeba było oczyścić linię powiązania z planem. Akceptujesz?

## Koszt

@@TIME@@ pracy w całym cyklu, na jednym modelu, claude-sonnet-5-5, policzone @@TOKENS@@ mln tokenów. Cztery przeglądy kodu i jeden przegląd kroku powrotu, dwie poprawki i jedna poprawka po Twojej decyzji. Tabela etapów jest w dolnej części, pod zapisem.

## Jak scalić

Scal przez merge commit, który zachowuje commity. Link do zapisu przeżywa tylko wtedy. Gałąź scala się do gałęzi integracyjnej the-way; nic innego nie czeka na scalenie.

</details>

## Technical changes

The change keeps the private paths and note titles of the author out of what a cycle publishes. In plain words: a cycle cleans the copy of its record before committing it and runs a pattern check on the copy and on every description, and the files below carry that.

- `c8fe9f6`: `task-cycle/private_paths_check.py` and `task-cycle/test_private_paths_check.py`. The script takes a directory or a file and lists as `<file>:<line>: <kind>: <text>` each Windows drive path, each home directory (Windows, Linux, macOS), the POSIX form of a drive (`/c/`, `/mnt/c/`, `/cygdrive/c/`) and each note link in double square brackets. It writes nothing and holds no list of words. Exit 0 nothing listed, 1 listed, 2 call error.
- `4643660`: the cycle's rules. `task-cycle/skill/SKILL.md` gets the new section "The record before it is committed" with the sequence (remarks check on the original, copy, one cleaning of every file, the new script on the copy, remarks check on the copy), and steps 9.4, 12 and 13 point to it. `task-cycle/skill/correction.md`, `blocked_finding.md` and `reserved_return.md` point to it. `task-cycle/skill/request_template.md` gets the check of the description and its place under *Checks*. `task-cycle/record_template.md` stops asking for the repository's path and says the copy is cleaned. `agent-instructions/README.md` gets the command for a change made without a cycle.
- `b6d93e8`: `foundations/decisions.md` gains the two decisions listed below.
- `d745246`: the fix of the first review. The script reads UTF-16 files that start with a byte order mark, no longer lists a web address with a drive-like segment, and lists file addresses. `project-level/test_plan_state.py` gains three tests that pin what the plan reader does with a cleaned copy: an unfinished plan task's copy is unchecked until the copy is linked, the same copy is read once it is linked, and a cleaned `Task relation:` line makes the reader report a conflict.
- `4deb195`: the decisions, the record template, the section of `SKILL.md` and the request template say exactly what the plan reader loses.
- `a5ea36f`: the correction for your decision. The exception for a listed `Task relation:` or `Project relation:` line is dropped in `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` and the first decision. `task-cycle/skill/request_template.md` gains item 12 of *For you to decide*, which tells the human that such a line was cleaned and that the plan reader may report a conflict. One comment in `project-level/test_plan_state.py` changed; the tests did not.
- `b241bb0`: the return step. The first decision now holds in its binding paragraph the request's item for a cleaned relation line, and the second holds the order of the two checks and the single rewriting of the copy.

The plan reader (`project-level/plan_state.py`) and its invariants are not changed.

## Checks

- Full gate `python -B gate/run_tests.py` on `b241bb0`, the final tree, after the correction and the return step: @@GATE@@.
- Earlier full gate on `4deb195`, before the correction: exit code 0, "804 tests in 9 directories; every directory passed". Base gate on `ad44b84`, before any change: exit code 0, 765 tests in 9 directories, every directory passed; no check was failing on the base.
- Focused checks of the author and the reviewers, each with exit code 0: `python -B gate/run_tests.py task-cycle` (187 tests), `python -B gate/run_tests.py project-level` (271 tests), `python -B gate/run_tests.py agent-instructions` (18 tests), `python -B elements/common/foundation_check.py` (0 errors).
- Not run: the author's mutation runs were not repeated by a reviewer. The merge of the target branch needed no run: it stands at the same commit as the base, so nothing came in.
- Own-work checks: the author ran the script over the tracked text of the repository (hits only in `instruction-files/` code, a drive root inside a regular expression), over the frozen task (one hit, the front-matter link), and the whole sequence on a made-up record (exit 0 on the cleaned copy, 1 on the uncleaned original). After the fix, the author checked that the places that describe the plan reader agree with what its three tests assert, and mutated the first test to see it fail. After the correction, a search outside the record found no text that still says a listed line is committed.
- Form check of this description: `python -B task-cycle/request_check.py <description> --task <frozen task>`, @@FORM@@.
- Check of private paths on this description: `python -B task-cycle/private_paths_check.py <description>`, @@PRIV@@.
- Check of private paths on the copy of the record, committed as `@@COPYSHA@@`: `python -B task-cycle/private_paths_check.py docs/task-cycles/cycle-no-private-names` exit code 0 ("checked: @@NFILES@@ files, 0 listed", after one rewriting of the copy and, for a real directory name in two files, one more), and the remarks check on the original and on the copy, exit code 0 each (@@NREPORTS@@ reports, @@NITEMS@@ items, all in the remarks). The first copy of this record, committed for the first version of this request, passed both checks the same way.
- The change touches no user interface.

## Foundation entries

- WAY-308, `row 1`: a task cycle commits its record and publishes the description of its request only cleaned, in every repository, public or private: absolute paths become relative to the repository, private notes are described, and the lines `Task relation:` of the record and `Project relation:` of the task copy stay as they are unless the check lists them, in which case they are cleaned like any other; commit messages are not cleaned. Its binding paragraph also says the request tells the human when a relation line had to be cleaned (`the cycle's`, return step).
- WAY-309, `row 2`: a pattern script lists absolute paths and note links before each commit of the copy and each publication of the description, the cycle corrects what it lists until it lists nothing, and no list of private words exists. It also narrows WAY-294 (`the cycle's`, found by the review): the second run of the remarks check, on the cleaned copy, appends nothing. Its binding paragraph holds the order of the two checks and the single rewriting of every text file of the copy (`the cycle's`, return step).

No invariant test, no surface and no *Violated* mark changed.

## Minor findings

Minor findings that no fix made:

- N2, `task-cycle/private_paths_check.py`, the drive pattern: "a drive letter after any slash is now excluded, so `/C:/Work/x` (a Windows path in a URL path, as some tools print it) is no longer listed as a drive path; only a home directory behind it is still caught. Not listed in my checks: `/C:/Work/x` alone. Narrow; within the task."
- N3, `task-cycle/private_paths_check.py`, `check_file`: "a UTF-16 file that fails to decode raises an error that says "as UTF-8". Cosmetic. Within the task."
- M1, `foundations/decisions.md`, WAY-309, from the review of the return step: "the Verification of WAY-309 has no case that violates the order of the two checks or the single rewriting. The files match the entry, so this is polish."

No Minor finding is felt by a user or by you, so none is put under *For you to decide*.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** independent task; a cycle record is published without the author's private paths and note titles. The task document was accepted on 2026-11-07, its citations stand at `foundations` `52889bc`, the cycle base is `foundations` `ad44b84`, and `foundations` has not moved since.
- **Process pin:** not applicable, the-way works on itself here.
- **Spec:** none. The task's rows settle what the cycle does; the script's name, call and patterns were choices of how to make it.
- **Route:** one author without a plan, class same as the orchestrator's: a script with tests, the same step added to six places of the cycle and two decisions bind one another, and nothing called for division. No discarded attempt.
- **Plan:** none.
- **Choices:** 3 other choices (the order of the cleaning and the remarks check, the `Task source:` line kept absolute in the working record and described in the committed copy, and the answer to the first review's finding), questions table in the record.
- **Correction:** the request first opened blocked: after the review of the fix, one finding remained (the exception for a listed relation line). Your answer, in the session on 2026-11-07: "Poprawimy zatem tak jak proponujesz" (drop the exception). No reset: the correction `a5ea36f` was added on the branch (range `acbcb15..a5ea36f`), reviewed (`PASS a5ea36f`), followed by the return step `b241bb0` (`PASS b241bb0`) and the gate on the final tree. Cost across all sessions of the orchestrator: one session.
- **Blocking findings left:** none. The one that remained, N1 of the review of the first fix, is fixed by the correction.
- **Record:** [record of the cycle](@@TREE@@), by the SHA of the commit that adds it; [table of stages](@@STAGES@@).

https://claude.ai/code/session_01GQhooaBqva1kjAzReLoCHk
