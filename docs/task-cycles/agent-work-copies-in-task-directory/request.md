**State: ready** — one item waits for your answer (item 1, how much of the foundation the review read whole); the full tests are green on the final tree.

## What you will see

The work with the process changes in one respect, all of it instructions and one new decision; no product code changes.

- Every agent of a task cycle that needs a copy to check something — a copy of the code at some commit, a clone, a script, a screenshot, an input prepared for a test — now makes it in a folder of its own inside the task's ignored working directory, named after the agent's role. It never makes it in the system's temporary folder, in a session's scratch folder or in the main copy of the repository. Before the agent returns, it deletes its copy, keeps with its report only what the report needs, and says in the report where the copy stood and that it was deleted.
- If a deletion fails, the agent still finishes and names what stayed, with its path. The cycle writes it into its record and shows it to you in the description of the request, under *Cost* and *Checks*, and goes on: a copy you can delete with one command does not stop a cycle.
- The orchestrator's own checkouts (of the base, and of the process at a pinned version) follow the same rule, and the orchestrator now reads, in each agent's report, the line about its copies, as it already reads the line about material the agent did not read.

### Underneath

Only instruction files, two templates and the decision log change. The agents of this cycle worked while the rule was being written; the author slipped against it twice (a test-output file and an empty file in the system's temporary folder, both deleted at once), and no agent left a copy behind (Checks, 5).

## For you to decide

### Needed from you

none

### Fix or let through

1. The review of the whole change did not read every decision that bears on it as a whole: of 137 decisions about the task cycle it read 31 whole and ran through 106 by title, and it named six that it read by title only — how an author searches the foundation after writing an entry, what a human accepts by merging, from which folder a session reads its skills, how the cycle chooses the material an agent reads, how findings are graded and fixed, and how long an agent waits for a long command. If this change clashed with one of them, you would meet it only when you read the request. Having a fresh reviewer read those six whole costs one more agent turn, a few minutes and about as many tokens as the review of the fix (1.5 million), and a round of correction if it finds something; letting it through costs nothing today, and the risk is a wording that clashes with one of the six. I recommend letting it through: the change adds one rule about where an agent's copies stand, the six decisions concern other matters, and both reviews read the decisions that touch the places it edits. Have a fresh reviewer read them in this request, make a task of it, or let it through? (Course of the cycle, Record)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. Two things the task left to the cycle. The folder of each agent is named after its role (for example the author, the planner, a numbered executor, the reviewer of the whole change, with a counter where a stage runs twice) and stands directly in the task's working directory, so two agents of one cycle never share a name; I did not number every agent or add one more level of folders, since that makes no name less ambiguous. A screenshot that the browser tool saves by itself under its session's folder is moved by the agent into its own folder and the original deleted, rather than told where to save: the author could not confirm that either tool of Claude Code and Codex accepts a place inside the agent's folder, and a file the agent cannot move or delete is a remainder like any other.
3. A copy that could not be deleted shows in the description as one plain sentence under *Cost* and the path under *Checks*, and in the record as its own item, and not as an item of this section. The review first found the item here and found that the list of what this section holds is closed to what waits for your yes. The rule also says that such a remainder goes when the task's directory goes; the removal of task directories after a merge is another task, parked, so until it is done you delete a remainder by hand.

## Cost

About 37 minutes of working time in the stages, plus 13 minutes for the full test run, and about 28 million tokens, all on one model family, across the session of the cycle; one fix round (the review of the whole change failed once, on a sentence in the rule that reached more than the task asked, the fix passed its review). Table of stages: the committed record, `stages.md`.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation has waited for a review through 45 merges since the last review, tagged 2026-11-06; the review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — jedna pozycja czeka na Twoją odpowiedź (pozycja 1, ile fundamentu przegląd przeczytał w całości); pełne testy są zielone na końcowym drzewie.

## Co zobaczysz

Praca z procesem zmienia się w jednym miejscu; wszystko to instrukcje i jedna nowa decyzja, kod produktu się nie zmienia.

- Każdy agent cyklu zadania, który potrzebuje kopii do sprawdzenia czegoś — kopii kodu na jakimś commicie, klonu, skryptu, zrzutu ekranu, wejścia przygotowanego dla testu — robi ją teraz we własnym katalogu w ignorowanym katalogu roboczym zadania, nazwanym od roli agenta. Nigdy nie robi jej w katalogu tymczasowym systemu, w schowku sesji ani w głównej kopii repozytorium. Zanim agent odda wynik, usuwa swoją kopię, przy raporcie zostawia tylko to, czego raport potrzebuje, i w raporcie podaje, gdzie kopia stała i że została usunięta.
- Gdy usunięcie się nie uda, agent mimo to kończy pracę i wymienia pozostałość z jej ścieżką. Cykl zapisuje ją w swoim zapisie i pokazuje Ci w opisie PR-a, w *Koszcie* i w *Sprawdzeniach*, i idzie dalej: kopia, którą usuwasz jednym poleceniem, nie zatrzymuje cyklu.
- Własne kopie orkiestratora (bazy i procesu w przypiętej wersji) podlegają tej samej regule, a orkiestrator czyta teraz w raporcie każdego agenta wiersz o jego kopiach, tak jak czyta już wiersz o materiale, którego agent nie przeczytał.

### Pod spodem

Zmieniają się tylko instrukcje, dwa szablony i dziennik decyzji. Agenci tego cyklu pracowali, gdy reguła dopiero powstawała; autor dwa razy się o nią potknął (plik z wynikiem testów i pusty plik w katalogu tymczasowym systemu, oba od razu usunięte), a żaden agent nie zostawił kopii (Sprawdzenia, 5).

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Przegląd całej zmiany nie przeczytał w całości każdej decyzji, która jej dotyczy: ze 137 decyzji o cyklu zadania 31 przeczytał w całości, a 106 przejrzał po tytułach, i sam wymienił sześć, które znał tylko z tytułów — jak autor szuka w fundamencie po zapisaniu wpisu, co człowiek akceptuje przez scalenie, z jakiego katalogu sesja czyta umiejętności, jak cykl wybiera materiał, który czyta agent, jak ocenia się i poprawia uwagi oraz jak długo agent czeka na długie polecenie. Gdyby ta zmiana kłóciła się z którąś z nich, zobaczyłbyś to dopiero przy czytaniu PR-a. Przeczytanie tych sześciu w całości przez świeżego recenzenta kosztuje jeszcze jedną turę agenta, kilka minut i tyle tokenów co przegląd poprawki (1,5 miliona), oraz rundę poprawek, jeśli coś znajdzie; przepuszczenie nic dziś nie kosztuje, a ryzyko to brzmienie, które koliduje z jedną z sześciu. Polecam przepuścić: zmiana dodaje jedną regułę o tym, gdzie stoją kopie agenta, tych sześć decyzji dotyczy innych spraw, a oba przeglądy czytały decyzje dotyczące miejsc, które zmiana edytuje. Mam kazać świeżemu recenzentowi przeczytać je w tym PR-ze, zrobić z tego zadanie, czy przepuścić? (Przebieg cyklu, Zapis)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Dwie rzeczy, które zadanie zostawiło cyklowi. Katalog każdego agenta nazywa się od jego roli (na przykład autor, planista, ponumerowany wykonawca, recenzent całej zmiany, z licznikiem tam, gdzie etap biegnie dwa razy) i stoi wprost w katalogu roboczym zadania, więc dwaj agenci jednego cyklu nigdy nie dzielą nazwy; nie numerowałem każdego agenta ani nie dodawałem kolejnego poziomu katalogów, bo to żadnej nazwy nie robi mniej dwuznaczną. Zrzut ekranu, który narzędzie przeglądarki zapisuje samo w katalogu swojej sesji, agent przenosi do własnego katalogu i usuwa oryginał, zamiast podawać narzędziu miejsce zapisu: autor nie mógł potwierdzić, że któreś z narzędzi Claude Code i Codexa przyjmuje miejsce wewnątrz katalogu agenta, a plik, którego agent nie może przenieść ani usunąć, jest pozostałością jak każda inna.
3. Kopia, której nie udało się usunąć, pokazuje się w opisie jako jedno zwykłe zdanie w *Koszcie* i ścieżka w *Sprawdzeniach*, a w zapisie jako osobny punkt, nie jako pozycja tej sekcji. Przegląd najpierw znalazł tę pozycję tutaj i stwierdził, że lista tego, co ta sekcja zawiera, jest zamknięta do tego, co czeka na Twoje „tak”. Reguła mówi też, że taka pozostałość znika razem z katalogiem zadania; usuwanie katalogów zadań po scaleniu to inne zadanie, zaparkowane, więc do czasu jego wykonania pozostałość usuwasz ręcznie.

## Cost / Koszt

Około 37 minut pracy w etapach, plus 13 minut pełnego przebiegu testów, i około 28 milionów tokenów, wszystko na jednej rodzinie modeli, w sesji cyklu; jedna runda poprawek (przegląd całej zmiany raz dał wynik negatywny z powodu zdania w regule, które sięgało dalej, niż prosiło zadanie, poprawka przeszła swój przegląd). Tabela etapów: zapis w commicie, `stages.md`.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przeżywa tylko wtedy. Fundament czeka na przegląd przez 45 scaleń od ostatniego przeglądu, oznaczonego 2026-11-06; przegląd to umiejętność `the-way-review-foundation`, uruchamiana w sesji w tym repozytorium; nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

The change writes one rule — an agent of a task cycle makes each working copy in a directory of its own under the ignored directory of the task's worktree, removes it before it returns, and names a remainder in its report — and carries it through the places that made a copy without saying where.

- `5f01235` — adds WAY-373 ("Where does an agent of a task cycle make a working copy to check something, and what happens to it?"); adds the section "Working copies" to `task-cycle/skill/SKILL.md` and has the handoff paragraph give each agent its directory and copy the first paragraph of that section; moves the orchestrator's own clone of the process to a directory of its own (step 2) and its checkout of the base to another (step 4); adds the rule's line to the reviewer's, the planner's and the author's methods (`task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`), to the instruction on the screenshot an author inspects (`task-cycle/change/ui_check.md`), the item *Working copies left* to the record template and a sentence to the description template.
- `a300ee6` — the fix of the review of the whole change: narrows the sentence on files a tool writes by itself to the screenshot a screenshot tool saves, and says in the rule and in WAY-373 that the files a product's own tools and tests make are no working copy of the agent (finding I-1); moves the leftover copy out of the section for the human's decisions to *Cost* and *Checks* of the description (M-1); has the orchestrator read the line on working copies of each report when the agent returns (M-2); rewraps the paragraphs the change edited (M-3).
- The return step changed nothing: no commit.

## Checks

1. The gate, `python -B task-cycle/gate_times.py --output .runs/task-cycles/agent-work-copies-in-task-directory/gate_times.md -- python -B gate/run_tests.py`, on `a300ee6`, the final tree (`origin/foundations` had not moved, so no merge): exit 0; 1328 tests in 10 directories, 791.7 s, every directory passed. The list of tests failing before the change was taken from the final gate of the merged branch of the previous cycle (`docs/task-cycles/split-only-for-gain/cycle.md` in commit `06be7bb`, its run 2 on `50548bf`): none failing, 1328 tests; no gate ran on the base. That cycle's run 1 failed once on a flaky test of the test runner (class `DirectoriesAtOnce` in `gate/test_run_tests.py`), which fails on the base too; it did not fail in this cycle's run.
2. `python -B elements/common/foundation_check.py` on `a300ee6`, without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line. The focused runs of the author and the reviewers: `gate/run_tests.py` for `task-cycle` (394 tests), `agent-instructions` (25), `instruction-files` (104, 5 skipped by the tests) and `elements/common` (201), each exit 0.
3. Own-work checks: the author's, `grep -rn -i "separate worktree\|separate checkout\|scratch run\|scratch worktree" task-cycle --include=*.md`, exit 0, two lines, both now with a directory; the fix's, `grep -rn "kind 18\|writes by itself outside" task-cycle foundations/decisions.md`, exit 1 (no match, as wanted), and the clause "no working copy of the agent" present in the rule and in the decision. What they cannot show: whether an agent given the rule removes its copy and reports it; the next cycle shows that.
4. Not run: no review of the return step (it made no commit); no run of the two generators of `AGENTS.md` and of skill entry points (no agent type's definition and no skill's description changed); no test was written, since the change is instruction text and one decision, whose pair of examples an agent compares a change with. The reviewer's Unread material is judged in item 1.
5. Working copies: each agent reported where its copy stood and that it was removed — the reviewer's worktree of the head under its own directory, twice, the author's directory for test output, and none for the return step — and no remainder was named. The author's three slips against the rule it was writing (test output in the system's temporary folder in the first round, an empty file there in the fix) were deleted by the author and listed in its reports.
6. The form check, `python -B task-cycle/request_check.py .runs/task-cycles/agent-work-copies-in-task-directory/request.md --task .runs/task-cycles/agent-work-copies-in-task-directory/task.md`, and the check of private paths on this description: written and checked after this commit. The remarks check, the check of private paths and the check of image files on the copy of the record: filled in when the record's link is added.

## Foundation entries

1. WAY-373 (`row 1`) — an agent of a task cycle makes each working copy to check something in a directory of its own under the ignored `.runs/` of the task's worktree, removes it before it returns and says in its report where it stood and that it was removed; a failed removal is named with its path, carried to the record and to the description of the request, and stops nothing.

No invariant, its test or its surface changes and no *Violated* mark is set; the foundation check lists nothing.

## Minor findings

Minor findings that no fix made, from the review of the fix of the whole change (`PASS a300ee62676e5812141c86852357d32e54e3b068`), in the reviewer's words:

1. `task-cycle/plan/SKILL.md:180-183`: "leaves a short last line ("moves. The move is a choice of how to make the") before an unreflowed line, as the reflow stopped one line early; polish only, blocks nothing, lies within the task."

The three Minor findings of the review of the whole change (the place of the leftover item in the description, the orchestrator not told how it learns of a remainder, ragged wrapping) were fixed in `a300ee6` and the review of the fix found them fixed.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** agents of a task cycle make working copies in a directory of their own under the task's ignored working directory, remove them before they return and name what they could not remove; independent task, no project; sources: the task document (released to the cycle on 2026-11-14) and the foundation at `671f470`.
- **Process pin:** this checkout of the-way is the repository changed; base `671f470` of `foundations`; no pin moved; the gate on the final tree is in Checks, 1.
- **Spec:** none; no open design choice at the start (the two questions the task carried to the cycle are choices of how to make what the task settles).
- **Route:** one author without a plan, class `same` (the change writes a decision entry and keeps one rule consistent across several instruction files, where wording is the whole product), a fix and a review of the fix after one `FAIL`, the return step found nothing; the review of the whole change read 31 of 137 decisions whole and ran through the rest by title, six it names as read by title only (item 1).
- **Plan:** none.
- **Choices:** 5 other choices of the cycle beyond the items above: the class of the author, and four on what to do with the unread material of the author's, the fix reviewer's and the whole-change reviewer's reports and with the reviewer's last Minor note, in the questions table of the record.
- **Blocking findings left:** none.
- **Record:** written when the record's link is added.
