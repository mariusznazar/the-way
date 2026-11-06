**State: draft** — the change is reviewed and every test passes; one cycle choice waits for your yes.

## What you will see

Four small corrections to how a task cycle works, each taken from a remark that earlier cycles left in their pull requests.

1. **A cycle on the-way itself now starts from the current rules.** Before it creates its branch, the cycle fetches and, if the copy of the repository it works in stands behind the remote target branch, moves it forward and starts again from the entry point that began the cycle, so it reads the newest rules. If the copy cannot be moved forward (it holds local commits, has unsaved changes or is on another branch), the cycle stops and says so. A correction after your remarks does the same: in a copy of the target branch it moves it forward, in the request's own working copy it merges the remote target branch in, and it merges the remote branch, not the local one, in products too. The cycle's record now also sits in the task's working copy, as the instructions already said elsewhere.
2. **Foundation entries written by a change no longer go through the independent critique of a set.** The review of the change already reads them and you accept them at the merge, so the critique was a second reading that agents reported as missing.
3. **the-way no longer names a private script.** The instructions and the remarks check named the script of the nightly review, which lives outside the repository; they now say "the nightly review of cycles", the name the foundation already uses.
4. **The language check does not count quoted text.** A Polish task that quotes long English sentences used to be read as English, which opened its request as a draft with a false error. The check now leaves out text in quotation marks and lines that start with `>`. One gap follows and is accepted by the task: an English summary placed wholly in quotation marks is no longer judged.

### Underneath

Instructions of the cycle, one new decision, one decision example changed, and one small script change with three new tests; the gate passes on the final tree.

## For you to decide

1. **The new decision restarts a correction only when something came in.** Your task says a correction starts again from the entry point "in both cases". Read literally, that restarts even a correction that fetched nothing new, which would read the same paragraph again and never end. The cycle therefore wrote the restart as conditional ("where something came in") in the new decision, in the correction's instructions and, through the sentence you approved word for word, in the cycle's start. The reviewer found the first draft inconsistent on this point, and the fix brought the decision in line with the instructions. Accept the condition? (Foundation entries, 1)
2. **One sentence of the cycle's instructions still says the cycle writes only in the task's worktree.** The new start step now allows one write outside it, so a reader of the earlier sentence meets "only" before the exception. It does not change what the cycle does. Make a task of it, or merge without it? (Minor findings, 1)
3. **The reconciliation step before the request still merges the local target branch.** The correction now merges the remote one. In a cycle the local branch was brought up to date at the start, so the two differ only if the remote moved during the cycle. Make a task of it, or merge without it? (Findings outside the task's scope, 1)

## Cost

About 18 minutes of working time. The orchestrator and all agents ran on one model, Claude Sonnet 5.5, using 15.3 M tokens, of which 14.6 M were input read from cache and 0.09 M output. Review rounds: the whole change was reviewed and failed on one finding, the author fixed it once, and the same reviewer passed the fix. The return step made no commit, so it needed no review. The table of stages is in the cycle's record, linked under *Record* below.

## How to merge

Use a merge commit, not squash or rebase: the link to the cycle's record points to a commit on this branch, and it survives only when the commits are kept.

<details>
<summary>W Twoim języku</summary>

**Stan: szkic** — zmiana przeszła przegląd i wszystkie testy; jedna decyzja cyklu czeka na Twoje „tak”.

**Co zobaczysz**

Cztery drobne poprawki w tym, jak działa cykl zadania, każda wzięta z uwagi, którą wcześniejsze cykle zostawiły w swoich PR-ach.

1. **Cykl na samym the-way startuje teraz z aktualnych reguł.** Zanim założy gałąź, cykl pobiera zmiany i, jeśli kopia repozytorium, w której pracuje, stoi za zdalną gałęzią docelową, przewija ją do przodu i zaczyna od nowa od punktu wejścia, który go uruchomił, więc czyta najnowsze reguły. Gdy kopii nie da się przewinąć (ma lokalne commity, niezapisane zmiany albo stoi na innej gałęzi), cykl staje i mówi o tym. Korekta po Twoich uwagach robi to samo: w kopii gałęzi docelowej ją przewija, w osobnej kopii roboczej requestu scala do niej zdalną gałąź docelową, a w produktach scala zdalną gałąź, nie lokalną. Zapis przebiegu cyklu leży też teraz w kopii roboczej zadania, jak instrukcje mówiły już w innych miejscach.
2. **Wpisy fundamentu pisane w zmianie nie przechodzą już niezależnej krytyki zestawu.** Przegląd zmiany czyta je i tak, a Ty akceptujesz je przy scaleniu, więc krytyka była drugim czytaniem, które agenci zgłaszali jako brak.
3. **the-way nie wymienia już z nazwy prywatnego skryptu.** Instrukcje i sprawdzenie uwag nazywały skrypt nocnego przeglądu, który leży poza repozytorium; teraz mówią „nocny przegląd cykli”, nazwą, której fundament już używa.
4. **Sprawdzenie języka nie liczy tekstu w cudzysłowach.** Polskie zadanie z długimi angielskimi cytatami było czytane jako angielskie, przez co jego request otwierał się jako szkic z fałszywym błędem. Sprawdzenie pomija teraz tekst w cudzysłowach i linie zaczynające się od `>`. Wynika z tego jedna luka, którą zadanie przyjmuje: angielskie streszczenie w całości w cudzysłowie przestaje być oceniane.

*Pod spodem:* instrukcje cyklu, jedna nowa decyzja, jeden zmieniony przykład decyzji i niewielka zmiana skryptu z trzema nowymi testami; gate przechodzi na ostatecznym drzewie.

**Do Twojej decyzji**

1. **Nowa decyzja każe zaczynać korektę od nowa tylko wtedy, gdy coś przyszło.** Zadanie mówi, że korekta zaczyna od nowa od punktu wejścia „w obu przypadkach”. Czytane dosłownie, restartowałoby to także korektę, która nic nowego nie pobrała, a ta czytałaby ten sam akapit i nigdy by się nie skończyła. Cykl zapisał więc restart jako warunkowy („gdy coś przyszło”) w nowej decyzji, w instrukcji korekty i — przez zdanie, które zatwierdziłeś słowo w słowo — w starcie cyklu. Recenzent znalazł, że pierwsza wersja jest w tym miejscu niespójna, a poprawka dopasowała decyzję do instrukcji. Przyjmujesz warunek? (Wpisy fundamentu, 1)
2. **Jedno zdanie instrukcji cyklu nadal mówi, że cykl pisze tylko w worktree zadania.** Nowy krok startu dopuszcza jeden zapis poza nim, więc czytelnik wcześniejszego zdania trafia na „tylko” przed wyjątkiem. Nie zmienia to tego, co cykl robi. Robimy z tego zadanie, czy scalamy bez tego? (Drobne uwagi, 1)
3. **Krok uzgodnienia przed requestem nadal scala lokalną gałąź docelową.** Korekta scala już zdalną. W cyklu lokalna gałąź była aktualizowana na starcie, więc różnią się one tylko wtedy, gdy zdalna ruszyła w trakcie cyklu. Robimy z tego zadanie, czy scalamy bez tego? (Uwagi poza zakresem zadania, 1)

**Koszt**

Około 18 minut pracy. Prowadzący cykl i wszyscy agenci pracowali na jednym modelu, Claude Sonnet 5.5, i zużyli 15,3 mln tokenów, z tego 14,6 mln to wejście czytane z pamięci podręcznej, a 0,09 mln to wyjście. Rundy przeglądu: cała zmiana przejrzana i odrzucona z jedną uwagą, autor poprawił ją raz, a ten sam recenzent przepuścił poprawkę. Krok powrotu nie zrobił żadnego commitu, więc nie wymagał przeglądu. Tabela etapów jest w zapisie cyklu, do którego link stoi niżej w sekcji *Record*.

**Jak scalić**

Commitem scalającym, nie przez squash ani rebase: link do zapisu cyklu wskazuje commit na tej gałęzi i przetrwa tylko wtedy, gdy commity zostaną zachowane.

</details>

## Technical changes

1. **The cycle's instructions: start from the remote target branch.** `0b81978`: `task-cycle/skill/SKILL.md` step 4 gains the fetch and fast-forward sentence of the task, word for word, and step 5 says the record is created "in the task's worktree"; `task-cycle/skill/correction.md` gains a first paragraph (fetch; fast-forward in a copy of the target branch or merge the remote target branch in the request's worktree; "where something came in, start again from the entry point"), its *Reserved choice* paragraph now begins "Then read", and its merge sentence says "the remote target branch".
2. **The decision log.** `0b81978`: WAY-298 written at the end of the log (new, row 1 of the task); the *Verification* example of WAY-291 changed in place to "a correct Polish block full of English names outside quotes". `c46a0c9`, the fix: WAY-298's restart conditions made explicit in its binding sentences and *Verification*.
3. **Two small wording changes.** `f13c800`: `elements/common/way_of_working.md` gains the sentence that foundation entries a change writes are no set for the critique; `task-cycle/record_template.md` and `task-cycle/remarks_check.py` (its docstring and one comment) name "the nightly review of cycles" instead of the private script.
4. **The language check.** `7841f00`: `task-cycle/request_check.py` (`english_share`) removes text in „…”, “…” and "…" quotation marks, matched within one line, and lines that start with `>`, and its description of the measure says so; `task-cycle/test_request_check.py` gains three tests (a Polish task with long English quotations reads as not English, a block wholly in quotation marks is not judged, an unpaired quotation mark cuts only its own line).
5. **The return step changed nothing.** It compared WAY-298, the WAY-291 example, the entries of the task's *Decisions in play* and the part map with the code, found nothing that no longer matched and made no commit.

## Checks

1. **The full test run passed on the base and on the final tree.** `python -B gate/run_tests.py`: on the base `3177e10`, exit 0, 714 tests in 8 directories; on the reviewed final tree `c46a0c9`, exit 0, 717 tests in 8 directories (three new tests). `foundations` had not moved (`git fetch`, `origin/foundations` = `3177e10`), so no merge and no second run were needed. A first run of the gate on `7841f00` was stopped when the review failed, before its result was read; the run counted is the one on `c46a0c9`. No check failed or did not run.
2. **The author's own-work check showed that the language check now reads the motivating case correctly.** The author ran `english_share` on this cycle's frozen task, a Polish task with long English quotations: share 0.021 on 336 words, not English; with the quote and block-quote patterns switched off in the same process, 0.175 on 559 words. It also tried three mutations of `task-cycle/request_check.py` (block-quote stripping removed, the straight-quote alternative removed, the „…” match allowed to cross lines); each made `task-cycle/test_request_check.py` fail, and the file passed again after each was restored. The two new tests that needed the change failed first (exit 1) and passed after it (55 tests, exit 0).
3. **The focused runs of the author and the reviewers all exited 0.** `python -B elements/common/foundation_check.py` (`0 errors`), and `python -B gate/run_tests.py` for `task-cycle` (142 tests), `elements/common` (109), `agent-instructions` (18), `relation-model` (12) and `instruction-files` (104, 5 skipped by the tests).
4. **No user interface changed:** no states or screenshots apply.
5. **The form of this description was checked by the script.** `python -B task-cycle/request_check.py .runs/task-cycles/cycle-remarks-batch-3/request.md --task .runs/task-cycles/cycle-remarks-batch-3/task.md`: exit 0 on the description as first written; it reads the Polish task document and the block as Polish (`task: not English, 336 words; block: not English, 579 words`), so the false error that the opened request of the earlier cycle carried does not appear. The run after the record's link was added is named below.
6. **The remarks check listed items until they were entered.** `python -B task-cycle/remarks_check.py .runs/task-cycles/cycle-remarks-batch-3`: 3 runs; runs 1 and 2 exited 1 listing the 3 items of the author's report (the second listing stood because the orchestrator wrote the report path with backslashes that turned into control characters); run 3 exited 0, listing nothing. The cycle holds no listing wrong.

## Foundation entries

Each entry this request writes or changes, with one English sentence of its meaning. No invariant test, surface or *Violated* mark changes. No kept row was tied to an entry already stated.

1. **WAY-298 (new), row 1, with one addition marked `the cycle's`.** In the-way itself the cycle fetches and, where its checkout stands behind the remote target branch, fast-forwards it, restarts from the entry point and stops where it cannot fast-forward; a correction does the same, or in the request's worktree merges the remote target branch into it, and its merge of the target branch takes the remote branch in a product as well. The addition marked `the cycle's` is that a correction restarts only where something came in, which row 1 does not state (see *For you to decide*, 1).
2. **WAY-291 (changed in place), To do 4 of the task.** The example of a compliant case now reads that the script takes a correct Polish block "full of English names outside quotes" as English, since quoted names are no longer counted; the rule itself is unchanged.

## Minor findings

1. **A sentence before the new start step still says the cycle writes "only" in the task's worktree.** Reviewer of the whole change, `3177e10..7841f00`, finding 2, `task-cycle/skill/SKILL.md:68`: "still says "The cycle writes only in the task's worktree" while step 4 (`:116-117`) and WAY-298 (`foundations/decisions.md:9037`) say the cycle makes one change outside it. The task (Context, AIR-602) says the clause "the one change the cycle makes outside the task's worktree" removes the contradiction with line 68, and Mariusz accepted it. The author left line 68 as it stands. A reader of line 68, which comes before step 4, meets an unqualified "only"; the qualification stands 48 lines later and in the foundation. The effect is a sentence a careful agent will notice and then resolve by step 4; it does not change what the cycle does. One clause on line 68 ("except the fast-forward of step 4") would settle it."
2. **A rewritten sentence left a line of 181 characters.** Reviewer of the whole change, finding 3, `task-cycle/record_template.md:182`: "the rewritten sentence left a line of 181 characters ... was not re-wrapped after the replacement. The file has other lines over 100 (up to 123) and no script enforces the width, so no check fails; only the diff reads untidily (the wording equals the task's replacement word for word). The words are right."
3. **The entry's meaning carries a condition the task row does not state.** Reviewer of the fix, `7841f00..c46a0c9`, `foundations/decisions.md` (WAY-298): "the entry's meaning now carries a condition that row 1 of the task's *Settlements to record* does not state (the row says the correction "zaczyna od nowa od punktu wejścia" without it). The fix report names it and gives the reason (an unconditional restart never ends). The human accepts it at the merge (WAY-114), so the request's section for the human's decisions has to carry it." It stands there as item 1.

## Findings outside the task's scope

1. **Step 12 of the cycle's skill merges the local target branch while the correction merges the remote one.** Reviewer of the whole change, finding 4, `task-cycle/skill/SKILL.md:389`: "step 12 says "merge the current target branch into the task branch", while the correction now merges the remote target branch. The task changed only `correction.md:20` and the start of step 4, so step 12 is not among its items. The effect: in a cycle on the-way, the reconciliation before the request merges the local target branch, which step 4 brought up to date at the start of the cycle but which may have fallen behind the remote since; the correction merges the remote branch. The two merges of the same cycle name different branches. The author noted it. A later task can say "the remote target branch" there, as it did for the correction."

## Course of the cycle

- **Task and sources:** "the way: poprawki z uwag cykli (ai-review S7), partia 2026-11-06", an independent task, from `zadanie_the_way_poprawki_z_uwag_cykli_2026_11_06.md` in the author's notes, `Status: ready for cycle`, answers of 2026-11-06; its citations stand at `foundations` `3177e10`. It takes up four nightly-review cases (AIR-602, AIR-603, AIR-604, AIR-605).
- **Process pin:** none; the-way working on itself, the process root this worktree.
- **Spec:** none. The task leaves no open design choice: the *To do* items give the wording of each edit and row 1 of *Settlements to record* settles the new decision.
- **Route:** one author without a plan, class `same` (Sonnet 5.5): the foundation step writes a new decision with its *Rejected* and the code change has a quote-matching rule with edge cases, where a slip would change meaning silently.
- **Plan:** none.
- **Choices:** five other choices (Q1, Q2 and Q4–Q6) in the questions table of the record's `cycle.md`; Q3 stands above as item 1 of *For you to decide*.
- **Blocking findings left:** none.
- **Record:** the cycle's record is added to this branch by a commit made after the request opens, and its link by that commit's SHA is written here at once.
