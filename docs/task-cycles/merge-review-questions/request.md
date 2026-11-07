**State: ready** — the change is complete and checked; one choice of the cycle waits for your yes below.

## What you will see

Three small changes to how the process works, all in the cycle's own instructions:

- When the cycle merges the newest main branch into a task branch just before opening the request, and that merge changes the code under review, the agent who reviews the merge is now told what to look for: whether the task's change and what just arrived on the main branch still fit together. The agent leading the cycle also names the decisions and rules that arrived with the merge and concern the parts the task touches, so the reviewer does not have to find them.
- At the end of a task, an agent that finds a word used against its entry in the glossary now simply corrects the use. Before, the instructions sent such a case to the tool that writes glossary entries, which does not handle it.
- When the review of a design spec fails, the version that was reviewed is now kept next to the spec under its own name, and whoever reviews the corrected spec compares the two versions instead of recalling the old one.

Two rules behind the first and third change are written into the log of decisions.

### Underneath

Five instruction files of the cycle changed by a few lines each, and the log of decisions gained two entries, one for each of the two rules; the instruction file of the reviewer of the whole change stays as it was.

## For you to decide

1. The reviewer of the whole change noted that the cycle's own instruction for a failed spec does not say that the path of the kept copy goes into the dispatch to the reviewer of the corrected spec; only the reviewer's own instruction says it. Closing that would have meant adding words to the sentence you fixed word for word, so the cycle left that sentence as you wrote it and made the new decision say only what both instructions say. The risk: a cycle that reads only its own instruction may forget to hand over the copy's path, and the reviewer would then compare from memory as before. Accept this, or make a task of it? (Choices, 1)

## Cost

About 12 minutes of working time in one orchestrator session and its three subagent turns, all on one model (Claude Sonnet 5.5), 10.85 million tokens in all, almost all of them cached input; two code-review rounds (the whole change, then the fix of its two minor findings). The table of stages is in the committed record, linked under *Record* below.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then.

<details>
<summary>Po polsku</summary>

**Stan: gotowe** — zmiana jest skończona i sprawdzona; poniżej czeka na Twoje „tak” jeden wybór cyklu.

## Co zobaczysz

Trzy drobne zmiany w tym, jak działa proces; wszystkie w instrukcjach samego cyklu:

- Gdy cykl tuż przed otwarciem PR-a dociąga do gałęzi zadania najnowszą gałąź główną, a to scalenie zmienia przeglądany kod, agent przeglądający scalenie dostaje teraz wskazówkę, czego szukać: czy zmiana zadania i to, co właśnie weszło na gałąź główną, nadal do siebie pasują. Agent prowadzący cykl nazywa też decyzje i reguły, które przyszły ze scaleniem i dotyczą części ruszanych przez zadanie, więc recenzent nie musi ich sam szukać.
- Na końcu zadania agent, który znajdzie słowo użyte wbrew jego wpisowi w słowniku, po prostu poprawia użycie. Wcześniej instrukcja odsyłała taki przypadek do narzędzia zapisującego wpisy słownika, które go nie obsługuje.
- Gdy przegląd specu kończy się odrzuceniem, przejrzana wersja zostaje obok specu pod własną nazwą, a ten, kto przegląda poprawiony spec, porównuje obie wersje zamiast przypominać sobie starą.

Dwie reguły stojące za pierwszą i trzecią zmianą trafiły do dziennika decyzji.

### Pod spodem

Pięć plików instrukcji cyklu zmieniło się o kilka linii każdy, a dziennik decyzji dostał dwa wpisy, po jednym na każdą z dwóch reguł; plik instrukcji recenzenta całej zmiany został bez zmian.

## Do rozstrzygnięcia

1. Recenzent całej zmiany zauważył, że własna instrukcja cyklu dla odrzuconego specu nie mówi, że ścieżka zachowanej kopii idzie do zlecenia dla recenzenta poprawionego specu; mówi to tylko instrukcja samego recenzenta. Domknięcie tego wymagałoby dopisania słów do zdania, które ustaliłeś co do słowa, więc cykl zostawił to zdanie tak, jak je napisałeś, a nową decyzję sformułował tak, by mówiła tylko to, co mówią obie instrukcje. Ryzyko: cykl czytający tylko własną instrukcję może zapomnieć o przekazaniu ścieżki kopii, a recenzent znów porównywałby z pamięci. Przyjąć to, czy zrobić z tego zadanie? (Choices, 1)

## Koszt

Około 12 minut pracy w jednej sesji prowadzącego i trzech turach podagentów, wszystko na jednym modelu (Claude Sonnet 5.5), łącznie 10,85 mln tokenów, prawie wszystkie to wejście z pamięci podręcznej; dwie rundy przeglądu kodu (całej zmiany, potem poprawki jej dwóch drobnych uwag). Tabela etapów jest w zatwierdzonym zapisie, linkowanym niżej w *Record*.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przeżywa tylko wtedy.

</details>

## Technical changes

Three commits: the foundation entries first, then the text that cites them, then the fix.

- `5932216` adds two decisions to the log, `foundations/decisions.md`: one on what the review of the merge of the target branch asks, one on keeping a failed spec as `spec-reviewed.md`.
- `3601aba` changes five instruction files with the exact wording of the task's four items: step 12 in `task-cycle/skill/SKILL.md` (the merge review's dispatch asks whether the two sides still hold together and names the entries the merge brought in), `task-cycle/skill/return_step.md` (a term used against its entry takes the use corrected and no entry), `task-cycle/skill/spec_review.md` (the failed spec is kept as `spec-reviewed.md` and the revision is reviewed against it), `task-cycle/spec/SKILL.md` (the dispatch of the spec reviewer may carry that copy) and `task-cycle/spec/review.md` (the reviewer of a revision compares with the spec as reviewed). `task-cycle/review/SKILL.md` is unchanged, as the task requires.
- `a5d6d5f` is the fix for the two Minor findings of the review of the whole change: the *Rationale* of both new decisions no longer names a count of files or what the checks lack, and the *Verification* examples of the spec decision say only what the instruction files say (8 insertions, 10 deletions, all in the two new entries).

## Checks

- The gate, `python -B gate/run_tests.py`, ran on the reviewed change `a5d6d5f` in the task's worktree: exit code 0, 765 tests in 9 directories, every directory passed. The same gate on the base `52889bc` also exited 0, so no check was failing before. Nothing failed or did not run.
- Own-work checks: the author's script confirmed all six quoted sentences of the task's items 1–4 are in their files word for word (six of six); the fixer checked that the fix stayed within the *Rationale* and *Verification* texts and touched no binding sentence, *Scope*, *Relations* or *Rejected*.
- Focused checks by the agents: `python -B elements/common/foundation_check.py` gave 0 errors (exit 0), `python -B gate/run_tests.py task-cycle` passed 151 tests (exit 0), and `python -B gate/run_tests.py elements/common` passed 109 tests (exit 0).
- The user interface is not touched, so there are no states or screenshots.
- The target branch had not moved since the branch was made, so there was no merge to review and the final tree is the one the gate checked.
- Review reminder: `python -B task-cycle/review_reminder.py origin/foundations` printed `reminder: no` (3 merges since the tag `foundation-review/2026-11-06`, threshold 30).
- Remarks check: `python -B task-cycle/remarks_check.py .runs/task-cycles/merge-review-questions`, 2 runs, the last exit 0 after 8 items from the stage reports were copied into the process remarks.
- Form check: written after this commit.
- Parts of the change, recovered through the part map: `task-cycle` (the five instruction files) and the decisions file; no check's file belongs to another part.

## Foundation entries

- WAY-306 (`row 1`): where merging the target branch changes the reviewed code, the dispatch of the merge review asks whether the two sides still hold together and names, by identifier, the foundation entries the merge brought in that bear on the parts the change touches, chosen by the orchestrator.
- WAY-307 (`row 2`): where the review of a spec fails, the spec as reviewed stays beside it as `spec-reviewed.md`, and the reviewer of the revision compares the revision with it.
- No row was tied to an entry already stated: the search of the whole foundation found neither settlement stated; both were written as new decisions rather than additions to WAY-162, WAY-135 or WAY-150. The change to the return step needs no entry (task: no entry needed; WAY-11 is unchanged and the instruction file is brought into line with it). No invariant test, surface or *Violated* mark is altered.

## Minor findings

none

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task: the order for the merge review asks whether both sides still hold together and names the entries the merge brought in, the return step stops sending a term used against its entry to the glossary tool, and a failed spec is kept for its revision's review; source: the task document (`task.md` in the record, settlements accepted 2026-11-06), the base `52889bc` of `foundations`.
- **Process pin:** none; this is the-way itself. The task was written at `dfd50e5`, the checkout was fast-forwarded to `52889bc`, and the four edited targets and the step-12 sentence were unchanged since (the step moved from lines 389-391 to 415-420 only by earlier additions).
- **Spec:** none; the task gives the exact wording of every change and both rows of *Settlements to record* settle their entries.
- **Route:** one author without a plan (class `same`, Claude Sonnet 5.5, because the foundation step writes two decisions into a long log and searches the whole foundation); no discarded attempt.
- **Plan:** none.
- **Choices:** 1 (the handling of the Minor finding about the path of the kept copy, see *For you to decide*, 1); the other 2 rows of the questions table are answered by binding sources; the questions table is in `cycle.md` of the record.
- **Blocking findings left:** none.
- **Record:** written after this commit.
