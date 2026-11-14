**State: ready** — one item waits for your answer (item 1), and the full tests ended red on a test that also fails on the unchanged branch (see Checks).

## What you will see

The work with the process changes in four places, all of them instructions and decisions; no product code changes.

- When an agent refines a larger task, it no longer mentions splitting it, asks whether to split it or recommends a split because the task is large. It proposes a split only for one of three reasons, and names the reason: a part cannot start or finish without something outside the refinement (access the agent lacks, another task's result); the parts change different repositories; or a later step of the refinement itself offers a separate task. A split only makes sense when it makes the work better or cheaper; "a part will be ready sooner" is no reason. You still see the whole document at acceptance and can ask for a split yourself.
- When a task's outcome deploys a product and the product lacks a skill for deploying it, the refinement adds that missing work to the task's list and no longer offers to split it off; you can still split it off yourself. Where the product has no deployment skill at all, the agent asks its questions (how long the logs live, how you learn of a failure) before you split that work off, so the new task carries your answer or refusal.
- When a project is cut into tasks, a task is cut by the same rules; the size of a task alone is no reason to cut it. The independent critique of a project plan no longer judges whether a task is "too large" and no longer sends you a split question for that (item 2).
- The decision log gets one new entry that answers "when is a task split", and the entry on what sets the weight of a task's process no longer calls size a signal to split.

### Underneath

Only the instruction files for refining a task and cutting a project into tasks, and the decision log, change. The full tests ended red on one test of the test runner that fails on the unchanged branch as well (Checks, 1).

## For you to decide

### Needed from you

none

### Fix or let through

1. The review of the whole change read 13 of the roughly 130 decisions it selected whole and went through the rest by title, and it named nine decisions that bear on the change and stayed unread (how you accept an entry, how an agent asks a question, how tasks of a plan are named and what the breakdown writes, how missing guidelines are handled). If one of them holds a rule that the new wording contradicts, the person working with the process would meet two rules that say different things, and nobody has seen it yet. A search of the whole log for the words of the split, made by the author and by the reviewer, found no such rule. Reading them in this request costs a session of a fresh reviewer and a round of review; merging as it is costs nothing now, and a contradiction, if there is one, shows up the first time an agent refines a task that touches it. I recommend letting it through, since the search of the whole log found nothing and the nine are about other matters. Read them in this request, make a task of it, or let it through?

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The independent critique of a project plan no longer judges a task's size. The task asked to remove from the cutting of a project into tasks the sentence that splits a large task, but the day before this cycle another change had added to the same place a test: a task is "too large" when its goal joins two or more effects that can each be checked alone and merged before the others, and the critique then asks you to split it. That test is the reason you rejected in your answers ("the independent part merges without waiting", that is, sooner), so it contradicted the rule this task writes. The cycle removed the test and the critique's question from the decision on the plan's check, from the critique's instructions, from the plan template and from the cutting instructions, and with them the signal "clearly more open questions, projected entries or items in scope than the rest of the plan", which pointed only to that test. The rest of the plan's check is as before. The other way was to keep the test as a fourth reason to split, which reopens your answer that lists three reasons, or to leave both and write which prevails, which leaves the wording in four files. If you want the plan's critique to keep judging size, say so: the part of the last commit about the plan's critique is reverted and the test is named a fourth reason (Foundation entries, 3).
3. The sentence that stood in the cutting instructions was no longer "A large task is split", as the task said, but "A task too large is put to the human to split, and its size chooses nothing else"; the cycle replaced that sentence with the rule that a task of a plan is cut by the rule for the end of a task and by the same three reasons, and that size alone is no reason. The other way was to delete the sentence without a replacement, which leaves the plan's author without a statement of when to cut.
4. One new entry in the decision log carries four of your settlements (when a split makes sense, the three reasons, the silence on size, and the plan's cut) instead of one entry for each, because they answer one question; the sentence "the human sees the whole document and may ask for a split" comes from your answer on silence and is in the entry and in the refinement instructions. The other way was separate entries for each settlement, which spreads one rule over three places to change. The entry's rule binds the one who proposes a split and leaves a split you ask for outside it.
5. Your settlements on the deployment-work check are written only as lines of the instruction for that check, with no new entry, and the existing entry on deployment skills stands beside them, since it names the human's own split. That entry does not itself say that the refinement offers no split or that the questions come before your split, so the instruction line is their only home; a later edit of that instruction could drop them unnoticed. The other way was a sentence in that entry, which the cycle did not take because the task named it as staying as it is.

## Cost

About 56 minutes of working time and 21 million tokens, all on one model family; one fix round (the review of the whole change failed once on the clash described in item 2, the fix passed its review). Table of stages: <the committed record's stages table, linked by the SHA of the commit that adds it>.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation has waited for a review through 43 merges since the last review, tagged 2026-11-06; the review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — jedna pozycja czeka na Twoją odpowiedź (pozycja 1), a pełne testy skończyły się na czerwono na teście, który pada też na niezmienionej gałęzi (zob. Sprawdzenia, 1).

## Co zobaczysz

Praca z procesem zmienia się w czterech miejscach; wszystko to instrukcje i decyzje, kod produktu się nie zmienia.

- Gdy agent doprecyzowuje większe zadanie, nie wspomina już o podziale, nie pyta, czy dzielić, i nie rekomenduje podziału dlatego, że zadanie jest duże. Podział proponuje tylko z jednego z trzech powodów i ten powód nazywa: część nie może ruszyć albo się skończyć bez czegoś spoza doprecyzowania (dostępu, którego agent nie ma, wyniku innego zadania); części zmieniają różne repozytoria; albo późniejszy krok doprecyzowania sam proponuje osobne zadanie. Podział ma sens tylko wtedy, gdy realizacja będzie lepsza albo tańsza; „część będzie gotowa szybciej” podziału nie uzasadnia. Cały dokument nadal widzisz przy akceptacji i możesz sam poprosić o podział.
- Gdy wynik zadania wdraża produkt, a produkt nie ma umiejętności wdrożenia, doprecyzowanie dodaje tę brakującą pracę do listy zadania i nie oferuje już jej wydzielenia; nadal możesz ją wydzielić sam. Gdy produkt nie ma umiejętności wdrożenia wcale, agent zadaje swoje pytania (jak długo żyją logi, jak dowiadujesz się o awarii), zanim sam wydzielisz tę pracę, więc nowe zadanie niesie Twoją odpowiedź albo odmowę.
- Przy podziale projektu na zadania zadanie tnie się według tych samych reguł; sam rozmiar zadania nie jest powodem cięcia. Niezależna krytyka planu projektu nie ocenia już, czy zadanie jest „za duże”, i nie przysyła Ci z tego powodu pytania o podział (pozycja 2).
- W dzienniku decyzji pojawia się jeden nowy wpis odpowiadający na pytanie „kiedy zadanie się dzieli”, a wpis o tym, co ustala ciężar procesu zadania, nie nazywa już rozmiaru sygnałem do podziału.

### Pod spodem

Zmieniają się tylko instrukcje doprecyzowania zadania i podziału projektu na zadania oraz dziennik decyzji. Pełne testy skończyły się na czerwono na jednym teście programu uruchamiającego testy, który pada również na niezmienionej gałęzi (Sprawdzenia, 1).

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Przegląd całej zmiany przeczytał w całości 13 z około 130 wybranych decyzji, a resztę przejrzał po tytułach; nazwał dziewięć decyzji dotyczących zmiany, które zostały nieprzeczytane (jak przyjmujesz wpis, jak agent zadaje pytanie, jak nazywa się zadania planu i co zapisuje podział projektu, jak obsługuje się brakujące wytyczne). Jeśli któraś z nich zawiera regułę, której nowe brzmienie przeczy, osoba pracująca z procesem trafi na dwie reguły mówiące co innego, a nikt tego jeszcze nie widział. Przeszukanie całego dziennika po słowach podziału, zrobione przez autora i recenzenta, takiej reguły nie znalazło. Przeczytanie ich w tej prośbie kosztuje sesję świeżego recenzenta i rundę przeglądu; scalenie bez tego nie kosztuje nic teraz, a sprzeczność, jeśli jest, wyjdzie przy pierwszym doprecyzowaniu zadania, którego ona dotyczy. Rekomenduję przepuścić, bo przeszukanie całego dziennika nic nie znalazło, a te dziewięć dotyczy innych spraw. Przeczytać je w tej prośbie, zrobić z tego zadanie, czy przepuścić?

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Niezależna krytyka planu projektu nie ocenia już rozmiaru zadania. Zadanie prosiło o usunięcie z podziału projektu na zadania zdania, które dzieli duże zadanie, ale dzień przed tym cyklem inna zmiana dodała w to samo miejsce test: zadanie jest „za duże”, gdy jego cel łączy co najmniej dwa efekty, z których każdy da się sprawdzić osobno i scalić przed pozostałymi, a krytyka prosi wtedy Ciebie o podział. Ten test to powód, który odrzuciłeś w swoich odpowiedziach („część niezależna scali się bez czekania”, czyli szybciej), więc przeczył regule, którą to zadanie zapisuje. Cykl usunął test i pytanie krytyki z decyzji o sprawdzaniu planu, z instrukcji krytyki, z szablonu planu i z instrukcji cięcia, a razem z nimi sygnał „wyraźnie więcej otwartych pytań, wpisów do zapisania albo punktów zakresu niż reszta planu”, który wskazywał tylko na ten test. Reszta sprawdzania planu jest taka jak była. Druga droga to zostawić test jako czwarty powód podziału, co otwiera Twoją odpowiedź wymieniającą trzy powody, albo zostawić oba i zapisać, który przeważa, co zostawia to brzmienie w czterech plikach. Jeśli chcesz, żeby krytyka planu dalej oceniała rozmiar, powiedz: część ostatniego commita dotyczącą krytyki planu cofnie się i test zostanie nazwany czwartym powodem (Wpisy fundamentu, 3). Przytoczenie z Twojej odpowiedzi na pytanie 5: „tak, w tym zadaniu; z podziału projektu znika zdanie »A large task is split«, a zadania tnie się według [reguły o końcu zadania] i powodów z pytania 2”; odrzucone tam: „poza zakresem — reguła zostaje i rozjazd między doprecyzowaniem a podziałem projektu też”; wiersz 6: „Podział projektu na zadania nie dzieli zadania z powodu samego rozmiaru; zadania tnie się według [reguły o końcu zadania] i powodów z wiersza 2.”
3. W instrukcji cięcia stało już nie „A large task is split”, jak mówiło zadanie, tylko „A task too large is put to the human to split, and its size chooses nothing else”; cykl zastąpił to zdanie regułą, że zadanie planu tnie się według reguły o końcu zadania i tych samych trzech powodów, a sam rozmiar nie jest powodem. Druga droga to skasować zdanie bez zastępstwa, co zostawia autora planu bez wskazania, kiedy ciąć.
4. Jeden nowy wpis dziennika decyzji niesie cztery Twoje ustalenia (kiedy podział ma sens, trzy powody, milczenie przy rozmiarze i cięcie planu) zamiast osobnego wpisu na każde, bo odpowiadają na jedno pytanie; zdanie „człowiek widzi cały dokument i może poprosić o podział” pochodzi z Twojej odpowiedzi o milczeniu i stoi we wpisie oraz w instrukcji doprecyzowania. Druga droga to osobne wpisy, co rozprasza jedną regułę na trzy miejsca zmian. Reguła wpisu wiąże tego, kto proponuje podział, a podział, o który prosisz Ty, zostaje poza nią.
5. Twoje ustalenia o sprawdzeniu pracy wdrożeniowej są zapisane tylko jako linie instrukcji tego sprawdzenia, bez nowego wpisu, a obok stoi dotychczasowy wpis o umiejętnościach wdrożenia, który nazywa podział robiony przez człowieka. Ten wpis sam nie mówi, że doprecyzowanie nie oferuje podziału ani że pytania padają przed Twoim podziałem, więc linia instrukcji jest ich jedynym domem; późniejsza zmiana tej instrukcji mogłaby je po cichu zgubić. Druga droga to zdanie w tym wpisie, czego cykl nie wziął, bo zadanie kazało go zostawić bez zmian.

## Cost / Koszt

Około 56 minut pracy i 21 milionów tokenów, wszystko na jednej rodzinie modeli; jedna runda poprawek (przegląd całej zmiany raz dał wynik negatywny z powodu starcia opisanego w pozycji 2, poprawka przeszła swój przegląd). Tabela etapów: <tabela etapów zapisu cyklu, linkowana przez SHA commita, który go dodaje>.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przeżywa tylko wtedy. Fundament czeka na przegląd przez 43 scalenia od ostatniego przeglądu, oznaczonego 2026-11-06; przegląd to umiejętność `the-way-review-foundation`, uruchamiana w sesji w tym repozytorium; nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

The change makes one rule — a task is split only for a reason that makes the work better or cheaper, and size alone is no reason — and carries it through the places that held the old rule. Everything is prose of instruction files and entries of the decision log; no code.

- `4e09369` — adds WAY-372 ("When is a task split into several tasks?"), edits WAY-13 in place so that size no longer "serves only as a signal to split", and edits four instruction files: `project-level/task/skill/read_sources.md` (the three reasons, the silence on size), `project-level/task/skill/resolve_gaps.md` (no offer of a split for deployment work, the questions before the human's split), `project-level/task/skill/orchestrated_mode.md` (the mention of deployment-work splits is gone) and `project-level/plan/skill/cut_tasks.md` (the plan's cut by the same rule). If it is wrong, an agent refining a task would again offer or withhold a split from the wrong rule; the instruction files and the entry say the same thing, which the return step compared.
- `edf1699` — the fix of the review of the whole change: removes the plan critique's judgment of a task's size from WAY-146, `project-level/plan/skill/critique_plan.md`, `project-level/plan/template.md` and `project-level/plan/skill/cut_tasks.md`; binds WAY-372's rule to the proposer of a split; puts the reason of different repositories on a link to WAY-140; replaces a duplicated sentence in WAY-13's rationale by a pointer to WAY-372. If the removal is unwanted, the plan's critique goes back to asking you for splits that the refinement's rule says size alone does not justify (item 2).
- The return step changed nothing: no commit.

## Checks

1. The gate, `python -B task-cycle/gate_times.py --output .runs/task-cycles/split-only-for-gain/gate_times.md -- python -B gate/run_tests.py` on `edf1699`, the final tree: exit 1; 1330 tests in 10 directories, 881 s; failed: the directory `gate`, one test, `test_run_tests.DirectoriesAtOnce.test_each_report_stands_whole_under_its_own_line_in_the_order_directories_end`, which waits 120 s for the directories to run at the same time and reports "did not meet the others"; the other nine directories passed. Not rerun to make the gate pass (WAY-243). Run in diagnosis only, the directory `gate` alone: on the worktree at `edf1699` it failed in another test of the same class, and alternately in a checkout of the base `0b77f5a` and a checkout of `edf1699` each passed (27.8 s, 29.3 s base; 30.0 s change) and failed (146.7 s base; 147.4 s change) in turn: a fault already on the base, not of the change. The earlier cycle's list took the final gate of the merged branch as green with one test of this class named flaky; the failing test here is a different one of the same class. This is the gate's failure to report: nothing of the change touches the runner or its tests.
2. `python -B elements/common/foundation_check.py` on `edf1699` without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line. The author's focused runs after the fix: `gate/run_tests.py` on `agent-instructions` (25), `instruction-files` (104, 5 skipped by the tests), `elements/common` (201), `project-level` (275), each exit 0; the reviewer of the fix ran `project-level` again: 275 OK (a first run killed at its 110-second limit showed one `F` that it could not read; the full run of the gate passed all of `project-level`).
3. Own-work checks: the author's first report — every wording of the old rule gone from the whole worktree (grep, exit 1 with no match); the author's fix report — no wording of the plan critique's size test remains (grep and a whole reading of WAY-146, `foundation_check.py` exit 0).
4. The form check, `python -B task-cycle/request_check.py .runs/task-cycles/split-only-for-gain/request.md --task .runs/task-cycles/split-only-for-gain/task.md`, and the check of private paths, `python -B task-cycle/private_paths_check.py .runs/task-cycles/split-only-for-gain/request.md`, on this description: <filled after the runs>. The remarks check, the private-paths check and the image check on the copy of the record: <filled by the edit that adds the record's link>.
5. Not run: no review of the return step (it made no commit); no reconciliation with the target branch (it had not moved since the base).

## Foundation entries

1. WAY-372 (`row 1`, `row 2`, `row 6`, and the silence half of `row 3`) — a split of a task is proposed only where it makes the work better or cheaper (time does not count), with one of three named reasons; an agent says nothing of a split for size alone; a split the human asks for stands without a reason; a project plan cuts its tasks by WAY-143 and these reasons. Relations: derives from WAY-13, WAY-140, WAY-143.
2. WAY-13 (`row 3`, edited in place) — a task's size may lighten how its change is prepared and made, and outside that it decides nothing; a split for size alone has no reason of its own (WAY-372).
3. WAY-146 (`the cycle's`, edited in place) — before a project plan is handed over a script checks its form and structure, and the independent critique judges only whether an end is checkable, whether a technical element enters early, whether a question stands where the definition puts it and whether a quoted answer settles it; no judgment of a task's size is made. It carries the accepted answer to question 5 and row 6 of the task, and changes the meaning of WAY-146 beyond the task's own *Decisions in play* (item 2).
4. Rows 4 and 5 of *Settlements to record* are written as lines of `project-level/task/skill/resolve_gaps.md` (`:62-64` and `:85-87`) with no entry of their own; WAY-139 stands beside them as the entry that holds the human's own split, not as the entry that states them (item 5).

No invariant, its test or its surface changes and no *Violated* mark is set; the foundation check lists nothing.

## Minor findings

Minor findings that no fix made, from the review of the fix of the whole change (`PASS edf1699`), in the reviewer's words:

- `project-level/plan/skill/critique_plan.md:19`, 126 columns: "The fix joined two lines ("...goes back to the human. If an independent critic cannot run, say so and wait;") without rewrapping the paragraph; the file was within 100 columns at `4e09369`. No rule of the-way fixes a width, so only polish."
- `foundations/decisions.md`, WAY-372 *Rationale*, around "one change. Naming the reason makes the proposal checkable, which a" / "bare "better" is not,": "the edit left one short line in the middle of the paragraph. Polish."
- `foundations/decisions.md`, WAY-146 *Verification*, "complies": "now has a single example, and WAY-146's binding sentence names four judgments of the critique with no pair on the "whether a quoted answer settles its question" judgment. That was already so at `4e09369` (the lost example only covered size); no change needed."

Finding 4 of the review of the whole change asked for the wording of this request: rows 4 and 5 are named in item 5 and in *Foundation entries*, 4, as lines of a skill with WAY-139 beside them; no file needed a change for it.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the refinement and the plan stop proposing a split of a task for its size or for a part being ready sooner, and name when a split pays; independent task, no project; sources: the approved task document (approved 2026-11-13) and the foundation at `0b77f5a`; the plan critique's size test, merged on 2026-11-14 after the task was approved, was reconciled by the choice in item 2.
- **Process pin:** this checkout of the-way is the repository changed; base `0b77f5a` of `foundations`; no pin moved; the gate on the final tree is in Checks, 1.
- **Spec:** none; no open design choice at the start.
- **Route:** one author without a plan, class `same`, because six decision entries under the decisions' schema, a search of the whole foundation and a collision with a decision merged hours before need judgment a cheaper class could miss; a fix and a review of the fix after one `FAIL`; the return step found nothing.
- **Plan:** none.
- **Choices:** 15 choices of the cycle beyond the rows and items: 3 autonomous choices of the orchestrator (the sentence in the cutting instructions, the paragraph of the refinement instructions as it stood, the removal of the plan critique's size test), in the questions table of the record, and 12 of the author (8 in its first report and 4 in its fix report).
- **Blocking findings left:** none.
- **Record:** <the committed record, linked by the SHA of the commit that adds it>.
