**State: ready** — the change is complete and tested; four items below wait for your yes.

## What you will see

This one task gathers 30 small corrections that the first review of the foundation found in the descriptions of merged requests. After the merge the agent that runs a task cycle, and the agent that settles technology for a project, get texts that no longer contradict each other or the recorded decisions.

- **The task cycle.** A correction made after your remarks now merges the target branch the way the first pass does: if the merge changes reviewed code, a fresh reviewer looks at it and the affected checks run again. The sentence about what the cycle may write outside its worktree names its real exceptions. The base-check copy of a product gets its dependencies installed. The rules for handoff files and for the request template say which file answers which question.
- **A stuck cycle is visible.** When a cycle ends in a blocked draft request, the report of the plan's state now shows the task as blocked instead of as a task with no request.
- **The remarks script reads every report.** It reads every report file in the cycle's folder except handoffs and findings files, so no stage's remarks can be skipped by a file name. The installer test no longer fails when someone commits while the full tests run.
- **The technology step.** A matter about logs, the interface, development data, the place of screenshots or how a human learns of a failure can no longer be struck from the list. A person to whom it does not apply answers it in one sentence, and the answer settles it, so it does not come back when the step is resumed. The step also resumes an interrupted run correctly, and says plainly that no option lets an agent check the running product when none does.
- **Refining a task.** The step that reads the sources now starts from one task and splits it only for a named reason, which ends the recommended splits you kept undoing. The reading of how to read the logs of a deployed product is tied to the decision about logs.
- **The recorded decisions and the guides.** Several decisions read more clearly or agree with each other. The process's overview page, the guide to instruction files and the map of the parts say what the process now does.

### Underneath

The change is eleven small slices plus twelve edits to the recorded decisions. One slice changed a script at a trust boundary, which got a review of its own.

## For you to decide

1. The cycle made two choices beyond the task's words. (a) The rule that these matters cannot be struck from the technology list also covers the place of the screenshots, a fifth matter that the foundation holds and the task did not name; the alternative was a rule on four of five matters of one listed group. Accept? (b) A blocked draft request is shown in the report of the plan's state by one extra line, not by a new state; a new state would change what that report promises to its readers. Accept? (Technical changes, 3; Foundation entries, 1)
2. The cycle corrected two sentences of recorded decisions that the task cited and did not open: the sentence that says what the cycle may change outside its worktree now says "to a checkout", so that it agrees with the account of the request in the backlog that the skill and two other decisions allow; and the example answer in the new decision about struck matters now names how long the record lives, which the decision about logs requires. Accept both? (Foundation entries, 12 and 13)
3. The task said the merge before a request opens takes the remote target branch "as a recorded decision justifies". That decision names only the merge made when a correction is applied; the skill states the rule and the decision's reason applies to it. The cycle left the decision as it is. Leave it, or add one clause to the decision? (Technical changes, 1)
4. Two other installer test files read the current commit in the same fragile way as the one fixed here, so a commit made during a full test run can break them. The reviewers marked this outside the task. Fix it in this request, or make a task of it? (Findings outside the task's scope, 1)

## Cost

About 1 h 49 min of working time (orchestrator and subagent turns together), 19 subagent turns by 18 subagents and three review rounds, with 79.6 million tokens in all, of which 56.0 million were Sonnet, 13.1 million Opus and 10.5 million Haiku. The table of stages is in the committed record (link added with the record).

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record of the cycle points to a commit that survives only then. Nothing else in this request waits for a review of the foundation.

<details>
<summary>Po polsku</summary>

**Stan: gotowe** — zmiana jest kompletna i przetestowana; cztery punkty poniżej czekają na Twoje „tak”.

## Co zobaczysz

To jedno zadanie zbiera 30 drobnych poprawek, które pierwszy przegląd fundamentu znalazł w opisach scalonych PR-ów. Po scaleniu agent prowadzący cykl zadania i agent rozstrzygający technologię dla projektu dostają teksty, które nie przeczą już sobie ani zapisanym decyzjom.

- **Cykl zadania.** Poprawka po Twoich uwagach scala teraz gałąź docelową tak jak pierwszy przebieg: jeśli scalenie zmienia zrecenzowany kod, świeży recenzent je ogląda, a dotknięte sprawdzenia biegną znowu. Zdanie o tym, co cykl może zapisać poza swoim worktree, nazywa jego prawdziwe wyjątki. Kopia bazy do sprawdzeń w produkcie dostaje zainstalowane zależności. Reguły o plikach zleceń i o szablonie opisu PR-a mówią, który plik odpowiada na które pytanie.
- **Zablokowany cykl jest widać.** Gdy cykl kończy się zablokowanym szkicem PR-a, odczyt stanu planu pokazuje zadanie jako zablokowane, a nie jako zadanie bez PR-a.
- **Skrypt uwag czyta wszystkie raporty.** Czyta każdy plik raportu w folderze cyklu poza zleceniami i plikami uwag, więc żadna nazwa pliku nie pozwoli pominąć uwag etapu. Test instalatora nie pada, gdy ktoś zrobi commit w trakcie pełnego przebiegu testów.
- **Krok technologii.** Sprawy logów, interfejsu, danych deweloperskich, miejsca zrzutów ekranu i powiadamiania o awarii nie da się już wykreślić z listy. Osoba, której sprawa nie dotyczy, odpowiada jednym zdaniem, a odpowiedź ją rozstrzyga i nie wraca przy wznowieniu. Krok poprawnie wznawia przerwany przebieg i mówi wprost, że żadna opcja nie pozwala agentowi sprawdzić działającego produktu, gdy tak jest.
- **Doprecyzowanie zadania.** Krok czytania źródeł zaczyna od jednego zadania i dzieli je tylko z nazwanego powodu, co kończy rekomendowane podziały, które cofałeś. Czytanie logów wdrożonego produktu jest powiązane z decyzją o logach.
- **Zapisane decyzje i przewodniki.** Kilka decyzji czyta się jaśniej albo zgadza się ze sobą. Strona przeglądowa procesu, przewodnik po plikach instrukcji i mapa części mówią to, co proces robi teraz.

### Pod spodem

Zmiana to jedenaście małych kawałków i dwanaście poprawek zapisanych decyzji. Jeden kawałek zmienił skrypt na granicy zaufania i dostał własną recenzję.

## Do rozstrzygnięcia

1. Cykl dokonał dwóch wyborów poza słowami zadania. (a) Reguła, że tych spraw nie da się wykreślić z listy technologii, obejmuje też miejsce zrzutów ekranu, piątą sprawę, którą fundament ma, a zadanie jej nie nazwało; alternatywą była reguła o czterech z pięciu spraw jednej wymienionej grupy. Akceptujesz? (b) Zablokowany szkic PR-a jest pokazany w odczycie stanu planu jedną dodatkową linią, a nie nowym stanem; nowy stan zmieniłby to, co ten odczyt obiecuje czytelnikom. Akceptujesz? (Zmiany techniczne, 3; Wpisy fundamentu, 1)
2. Cykl poprawił dwa zdania zapisanych decyzji, które zadanie przytaczało i nie otwierało: zdanie o tym, co cykl może zmienić poza swoim worktree, mówi teraz „w kopii roboczej” (to a checkout), żeby zgadzało się z zapisem o PR-ze w backlogu, który dopuszczają skill i dwie inne decyzje; a przykładowa odpowiedź w nowej decyzji o wykreślonych sprawach podaje teraz, jak długo żyje zapis, czego wymaga decyzja o logach. Akceptujesz obie? (Wpisy fundamentu, 12 i 13)
3. Zadanie mówiło, że scalenie przed otwarciem PR-a bierze zdalną gałąź docelową „jak uzasadnia zapisana decyzja”. Ta decyzja wymienia tylko scalenie robione przy poprawce; regułę podaje skill, a powód decyzji jej dotyczy. Cykl zostawił decyzję bez zmian. Zostawić, czy dopisać do decyzji jedną klauzulę? (Zmiany techniczne, 1)
4. Dwa inne pliki testów instalatora czytają bieżący commit tak samo kruchą metodą jak ten naprawiony tutaj, więc commit zrobiony w trakcie pełnego przebiegu może je zepsuć. Recenzenci uznali to za sprawę poza zadaniem. Naprawić w tym PR-ze, czy zrobić z tego zadanie? (Uwagi poza zakresem zadania, 1)

## Koszt

Około 1 h 49 min czasu pracy (tury orkiestratora i subagentów razem), 19 tur 18 subagentów i trzy rundy recenzji, łącznie 79,6 mln tokenów, z czego 56,0 mln Sonnet, 13,1 mln Opus i 10,5 mln Haiku. Tabela etapów jest w zatwierdzonym zapisie cyklu (link dochodzi razem z zapisem).

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase’em: link do zapisu cyklu wskazuje commit, który przeżywa tylko wtedy. Nic więcej w tym PR-ze nie czeka na przegląd fundamentu.

</details>

## Technical changes

1. **Task cycle rules** (`task-cycle/skill/SKILL.md`, `correction.md`): a correction merges the remote target branch and has the merge reviewed and the affected checks run again where it changes reviewed code (items 1–2); the sentence on writes outside the worktree names the fast-forward and the backlog account as its exceptions, and step 4 calls the fast-forward the one change to a checkout (items 3, Minor 4 of the review); step 4's base-check copy gets its dependencies installed and `.the-way` populated in a product (item 5). Step 12 and the correction already merged the remote branch in text; the decision log names that only for a correction (see item 3 of *For you to decide*). Commits `361c9fb`, `75fe0e3`.
2. **Slice executor and request template** (`task-cycle/change/slice.md`, `task-cycle/skill/request_template.md`): current ranges of the dispatch hold; the *Questions* item points to `task-cycle/skill/foundation_step.md`; the logging-scope item says where to find the additions (items 4, 6). Commit `7b04db0`.
3. **Plan-state reader** (`project-level/plan_state.py`, `project-level/test_plan_state.py`, `task-cycle/skill/blocked_finding.md`, `reserved_return.md`): a record whose *Request URL and status* line reads exactly `blocked draft, opened on this commit` makes the reader print one fixed-words evidence line; both flows write that wording (item 7). Trust boundary: the line is built from fixed words, the record's text only compared, bytes split on `\n` only, and the limit that the wording inside a fenced block is also read stands in the docstring. Commits `8b5662d`, `4fbe357`. A user of the reader sees one new evidence line; the plan item itself keeps its state.
4. **Remarks script** (`task-cycle/remarks_check.py`, `test_remarks_check.py`, `SKILL.md`): reads every `.md` file of `reports/` whose name holds neither `handoff` nor `findings`; the docstring's description of an item is true to the code; tests for the name rule and for a paragraph after a list (item 8, row 5). Commit `491f048`, rename of the old test in `75fe0e3`.
5. **Installer test** (`installation/test_install.py`): installs from a clone taken in `setUp` with the working tree's `install.py` copied in, so a concurrent commit changes neither the installed nor the expected commit, and an uncommitted edit of the installer is still under test (item 9). Commits `815294c`, `4515b4d`.
6. **Technology step** (`project-level/technology/*.md`, `project-level/definition_template.md`): no-strike rule with a three-part example, resume of an interrupted task run, `— projected` clears the nested line, the failure notice also looks for a projected decision, no option an agent can use (items 10–13, 15, 17 first point). Commits `f3bf7b6`, `66d36cd`.
7. **Smaller edits**: the critique's file renamed to `settle_review.md` and the step 2 order of `build_table.md` (items 14, 26; `22c626c`); the refine-task logs item, the lasting-exclusion sentence in the task template and the one-task default (items 16, 25, 30; `eac1751`); README (item 27; `da8c818`); the instruction-files skill's names rule and cautious emphasis sentence, with `writing.md` pointing to it (item 28; `fcb701e`, `75fe0e3`); `task-cycle` depends on `installation` in the part map (item 29; `6349019`); "of the product" dropped from `task-cycle/spec/SKILL.md` and `SKILL.md` where it restated what the log of checks no longer says (item 24; `75fe0e3`).

## Checks

- Full gate on the base `f238e4f`: `python -B gate/run_tests.py`, exit 0, 834 tests in 9 directories; nothing failed on the base.
- Full gate on the reviewed head `75fe0e3`: exit 0, 840 tests in 9 directories. Full gate on the final tree (head `5b3eb46`, run in the worktree): exit 0, 840 tests in 9 directories. The target branch had no new commit, so no merge was made.
- Focused checks after each slice and after the fix: all exited 0 (foundation check, the directory tests of `task-cycle`, `project-level`, `installation`, `instruction-files`, `elements/part-map`, `elements/common`, `agent-instructions`, the skill entry points without `--write`, `git diff --check`). No check failed and passed again.
- Own-work checks: each author and executor reported one and the reviewers confirmed them; the new tests (the blocked-draft line, the lone carriage return, the name rule, the paragraph after a list) failed before their change and pass after.
- No user interface changed, so there are no screenshot states.
- Form check of this description: COMMANDS_PENDING.
- Check of private paths on this description and on the copy of the record: COMMANDS_PENDING. Image check on the copy: COMMANDS_PENDING.
- Remarks check: run on the original in `.runs/` twice (the first listed 45 items, the second exit 0), and on the cleaned copy: COMMANDS_PENDING.

## Foundation entries

1. WAY-322, `row 1`: a matter of an agent's way to the running product that the technology step lists, and the matter of how a human learns of a failure, cannot be struck from the list; the human answers like any choice and the answer settles it. A new decision; it also covers the place of the screenshots (beyond the row's four, see item 1 of *For you to decide*).
2. WAY-166, `row 2` and `task item 18`: where no option can be used by an agent, the step recommends by the other consequences and says in one sentence that the check stays with the human; the example of compliance keeps the container's output in a store that outlives a redeployment.
3. WAY-139, `row 3`: its item "how to read the logs" is tied to the logs decision as the items on the record's life and on a failure are.
4. WAY-148, `row 4` and `task item 24`: every stage that runs a test or another check gives the check-result line, not only a stage that checks the product.
5. WAY-294, `row 5`: the reports the remarks script reads are the `.md` files of `reports/` whose name holds neither `handoff` nor `findings`.
6. WAY-165, `task item 17`: data set up from scratch and a dedicated test environment are examples, none ruled out; the reservation about opening a decision only on the human's word was already gone at the base; the sentence on a partial entry no longer cites WAY-270.
7. WAY-128, `task item 19`: the sentence on process skills and entry points names WAY-259 too.
8. WAY-292, `task item 20`: the form check reports the repeated block wherever it reads the task document as English.
9. WAY-05, `task item 21`: *Verification* in two pairs of `complies` and `violates`.
10. WAY-293, `task item 22`: *Rationale* without a description of what the request template does today; the rejected way says that no change leaves the return step without a precedence.
11. WAY-287, `task item 23`: the list names also a remarks-check listing and a form-check error held wrong.
12. WAY-298, `the cycle's` (return step): the fast-forward is the one change the cycle makes to a checkout outside the task's worktree.
13. WAY-322 *Rationale*, `the cycle's` (return step): the example answer names how long the record lives.
14. Part map, `task item 29`: `task-cycle` depends on `installation`.
No invariant test was added or changed, no *Violated* mark was set or cleared. The surface of the plan-state command gains one evidence line for a blocked draft record.

## Minor findings

1. `task-cycle/skill/SKILL.md:119` is 110 characters, past the file's usual wrap of about 100 (review of the fix, new in the fix; cosmetic).
2. The return step noted other lines past that wrap: `project-level/task/skill/read_sources.md:23` (the sentence the task gives word for word), `task-cycle/skill/request_template.md:171` and `project-level/definition_template.md:185-186`; the checks do not mind.
3. The review of the return step: the edit of the cycle-rules decision belongs among the entries the human did not see; it stands in item 2 of *For you to decide*.

## Findings outside the task's scope

1. `installation/test_coding_guidelines_installation.py:32` and `installation/test_lead_installation.py:32` read `self.commit` from the live repository's head in `setUp` and install from the live repository, the pattern the fixed test had; a commit made during a full run can break them (whole-change review, Minor outside the task; not run by the reviewer).

## Course of the cycle

- **Task and sources:** an independent task gathering 30 corrections from the first foundation review (items 1–30, five settlements to record, six answered questions), stated on `foundations` `a3206c1` and `f218b55`; the cycle worked on `f238e4f`, 46 commits later, and found each place by content; items 17 (second point), 25 (as worded) and 27 (first point) were already met at the base, and item 25 was reworded anyway as its sentence lacked the lasting-exclusion condition.
- **Process pin:** none; the cycle ran on the-way's own checkout.
- **Spec:** none; no open design choice.
- **Route:** planned slices, because the change spans about fifteen parts and a script at a trust boundary. No attempt was discarded.
- **Plan:** `plan.md` in the record, 11 slices and 12 foundation entries.
- **Choices:** 14 other choices, in the questions table of the record.
- **Blocking findings left:** none; two blocking findings of the review of the whole change were fixed and the fix passed its review.
- **Record:** RECORD_LINK_PENDING.
