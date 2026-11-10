**State: ready** — the change is complete and tested; two questions and one listing of a check wait for you below.

## What you will see

When an agent of a task cycle says that something it was told to read stayed unread, the person leading the cycle now has a rule for what to do, and you see it in the request instead of finding out later.

- **Every report has a section about unread material.** The agents that write a spec, a plan, the change itself or a review each end their report with a section called "Unread material": what of the material they were given stayed unread or was read only in part, or `none`. For the reviewer of the whole change it covers the material it chose itself, and it says how many decisions it read whole and how many only by title. The section is separate from "Searches not found or unclear", so it does not reach the process remarks.
- **The leader of the cycle reads that section in every report**, also when the report says `done` or `PASS`. A report without it goes back to the agent, as a report without the other section does. When the section names a gap, the leader decides before acting on the status: resume the agent to read it, pass the gap to the next agent able to judge it, or record a choice saying why it bears on nothing the agent judged. A decision read only by title, as the rule below allows, is no gap.
- **The reviewer of the whole change may now skim.** It reads whole the decisions of its selection that concern the topic of the change, runs through the rest by title and opens every one whose title points to a bearing on the change. Everyone else still reads what the handoff names, whole. The rule that said the whole log is not read no longer contradicts what reviewers do.
- **The request tells you when that review read too little.** Only when the reviewer did not run through the rest of its selection by title, or itself said that a decision concerning the change stayed unread, and nobody read it afterwards, this list gains one item, such as "The review of the whole change read 40 of 151 selected decisions whole; merge anyway?". Here it does not apply: the reviewer read 45 of 162 whole, ran through the other 117 by title and named none as unread that bears on the change.

### Underneath

Two new decisions and two edited ones in the foundation, the matching sentences in the skill of the cycle's leader, the five stage methods, the request template and the way of working, and one test of the remarks check. One author made the change without a plan; two reviews and a fix followed.

## For you to decide

1. Three choices of the cycle beyond the task's words. The new item for an incomplete reading stands last in this list of items, not beside the skipped steps, because putting it earlier would renumber the items that other files refer to by number. The task's fourth row was written as an addition to the existing decision on what the request puts before you, not as a new decision, because that decision is the list the row extends. The new section is called "Unread material" and stands before "Searches not found or unclear" in every report; the task gave it no name. Accept these three choices? (Course of the cycle, Choices)
2. Foundation entries you did not see at the task. The decision on what the request puts before you gained a clause: a gap counts as closed on the way only when the reviewer, or a fresh one, read what stayed unread, and a choice of the leader that it bears on nothing does not close it for the request. The decision on the new section gained two clauses: a decision read by title under the new rule is no gap and shows only in the counts, and a report that returns questions is not sent back for the section. Accept? (Foundation entries, 5 and 6)
3. The check that compares the reports with the process remarks listed two lines that the cycle holds are no items: a horizontal rule that follows the last item of a report's section, and the second line of a wrapped sentence in a finding that mentions the name of the section. The script is not changed in this cycle. Merge as it stands? (Checks, last item)

## Cost

About 30 minutes of working time in the session (orchestrator turns and subagent turns together), five turns of two subagents, two review rounds (the whole change, and the fix of its five Minor findings), with 31.7 million tokens in all, all on Sonnet. The table of stages is in the committed record.

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record of the cycle points to a commit that survives only then. Nothing else in this request waits for a review of the foundation.

<details>
<summary>Po polsku</summary>

**Stan: gotowe** — zmiana jest kompletna i przetestowana; poniżej czekają na Ciebie dwa pytania i jedno zestawienie sprawdzenia.

## Co zobaczysz

Gdy agent cyklu zadania mówi, że coś, co kazano mu przeczytać, zostało nieprzeczytane, prowadzący cykl ma teraz regułę, co z tym zrobić, a Ty widzisz to w PR-ze, zamiast dowiadywać się później.

- **Każdy raport ma dział o materiale nieprzeczytanym.** Agenci piszący specyfikację, plan, samą zmianę i przegląd kończą raport działem „Unread material”: co z przekazanego im materiału zostało nieprzeczytane albo przeczytane tylko w części, albo `none`. U recenzenta całej zmiany dział dotyczy materiału, który wybrał sam, i podaje, ile decyzji przeczytał w całości, a ile tylko po tytule. Dział jest osobny od „Searches not found or unclear”, więc nie trafia do uwag o procesie.
- **Prowadzący cykl czyta ten dział w każdym raporcie**, także gdy raport mówi `done` albo `PASS`. Raport bez niego wraca do agenta, tak jak raport bez drugiego działu. Gdy dział wskazuje lukę, prowadzący przed działaniem na statusie decyzuje: wznawia agenta, żeby doczytał, przenosi lukę do następnego agenta, który może ją ocenić, albo zapisuje wybór z powodem, dla którego luka nie dotyczy niczego, co agent ocenił. Decyzja przeczytana tylko po tytule, jak pozwala poniższa reguła, nie jest luką.
- **Recenzent całej zmiany może teraz przesiewać.** Czyta w całości decyzje swojego wyboru, które dotyczą tematu zmiany, resztę przegląda po tytułach i otwiera każdą, której tytuł wskazuje na związek ze zmianą. Pozostali agenci dalej czytają w całości to, co wskazuje im zlecenie. Reguła mówiąca, że całego dziennika się nie czyta, nie przeczy już temu, co recenzenci robią.
- **PR mówi Ci, gdy ten przegląd przeczytał za mało.** Tylko gdy recenzent nie przejrzał reszty swojego wyboru po tytułach albo sam przyznał, że decyzja dotycząca zmiany została nieprzeczytana, i nikt jej potem nie przeczytał, ta lista dostaje jedną pozycję, np. „Przegląd całej zmiany przeczytał w całości 40 ze 151 wybranych decyzji; scalić mimo to?”. Tu to nie dotyczy: recenzent przeczytał w całości 45 ze 162, resztę 117 przejrzał po tytułach i żadnej nie wskazał jako nieprzeczytanej, a dotyczącej zmiany.

### Pod spodem

Dwie nowe decyzje i dwie zmienione w fundamencie, odpowiadające im zdania w skillu prowadzącego cykl, w pięciu metodach etapów, w szablonie opisu PR-a i w sposobie pracy oraz jeden test sprawdzenia uwag. Zmianę zrobił jeden autor bez planu; potem były dwa przeglądy i jedna poprawka.

## Do rozstrzygnięcia

1. Trzy wybory cyklu poza słowami zadania. Nowa pozycja o niepełnej lekturze stoi na końcu tej listy, a nie obok pominiętych kroków, bo wstawienie jej wcześniej przenumerowałoby pozycje, do których inne pliki odwołują się numerem. Czwarty wiersz zadania zapisano jako uzupełnienie istniejącej decyzji o tym, co PR stawia przed Tobą, a nie jako nową decyzję, bo ta decyzja jest listą, którą wiersz rozszerza. Nowy dział nazwano „Unread material” i stoi przed „Searches not found or unclear” w każdym raporcie; zadanie nie dało mu nazwy. Przyjmujesz te trzy wybory? (Przebieg cyklu, Wybory)
2. Wpisy fundamentu, których nie widziałeś przy zadaniu. Decyzja o tym, co PR stawia przed Tobą, dostała klauzulę: luka jest zamknięta po drodze tylko wtedy, gdy recenzent albo świeży przeczytał to, co zostało nieprzeczytane, a wybór prowadzącego, że luka nie dotyczy niczego, nie zamyka jej dla PR-a. Decyzja o nowym dziale dostała dwie klauzule: decyzja przeczytana po tytule wedle nowej reguły nie jest luką i widać ją tylko w liczbach, a raport zwracający pytania nie wraca po ten dział. Przyjmujesz? (Wpisy fundamentu, 5 i 6)
3. Sprawdzenie porównujące raporty z uwagami o procesie wypisało dwie linie, które cykl uważa za błędne: poziomą kreskę po ostatniej pozycji działu raportu i drugą linię zawiniętego zdania w uwadze, które wspomina nazwę działu. Skrypt nie jest zmieniany w tym cyklu. Scalić tak, jak jest? (Sprawdzenia, ostatnia pozycja)

## Koszt

Około 30 minut czasu pracy w sesji (tury orkiestratora i subagentów razem), pięć tur dwóch subagentów, dwie rundy przeglądu (całość zmiany i poprawka jej pięciu drobnych uwag), łącznie 31,7 mln tokenów, wszystkie Sonnet. Tabela etapów jest w zatwierdzonym zapisie cyklu.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase’em: link do zapisu cyklu wskazuje commit, który przeżywa tylko wtedy. Nic więcej w tym PR-ze nie czeka na przegląd fundamentu.

</details>

## Technical changes

1. **Foundation** (`foundations/decisions.md`, commit `ca376a0`, wording fixed in `613f100`): WAY-325 and WAY-326 are new; WAY-150 and WAY-287 are edited in place. See *Foundation entries*.
2. **The orchestrator's skill** (`task-cycle/skill/SKILL.md`, `afa4343`, `613f100`): the task's sentence stands word for word after "add what it found to the handoffs that follow."; the paragraph of what a report holds, the line of what is read in every report, the repair rule and the mechanical check of a slice's executor carry the **Unread material** section; a sentence says a decision read by title is no gap. The places that speak of **Searches not found or unclear** only for the process remarks (the copy into the remarks, the process remarks check) are unchanged on purpose.
3. **The five stage methods** (`task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/plan/SKILL.md`, `task-cycle/spec/design.md`, `task-cycle/spec/review.md`, `afa4343`): each report lists **Unread material** before **Searches not found or unclear**; the reviewer's section carries the counts. `task-cycle/review/SKILL.md` section "Read" and `elements/common/way_of_working.md` step 2 of "Reading the foundation" carry the title screening of decisions for the reviewer of the whole change only; "The whole log is not read." became "The log beyond the decisions found is not read."
4. **The request template** (`task-cycle/skill/request_template.md`, `afa4343`): item 14 of *For you to decide* for an incomplete reading by the review of the whole change.
5. **A test** (`task-cycle/test_remarks_check.py`, `afa4343`, `613f100`): characterization tests that record how `task-cycle/remarks_check.py` reads **Unread material** placed before and after a bold-label **Searches not found or unclear** section. The script is unchanged.
6. **What the change leaves open.** If an agent writes **Unread material** as a bullet after a **Searches not found or unclear** label that is no list item, the script lists the bullet as an item of the other section and a line reaches the process remarks; the methods put the new section first, so a report that follows them is safe. A guidelines file the reviewer read in part goes to the section but not to the request item, which speaks of decisions, as the task words it. Nothing guards the order of the two sections mechanically; the leader's repair rule is the only guard.

## Checks

- Full gate on the base `02c3d47`: `python -B gate/run_tests.py`, exit 0, 861 tests in 9 directories; nothing failed on the base.
- Full gate on the reviewed head `afa4343`: exit 0, 863 tests. Full gate on the final tree (head `613f100`, in the task worktree): exit 0, 864 tests in 9 directories. The target branch had no new commit since the base, so no merge was made. No check failed and passed again.
- Focused checks of the author after each stage: `python -B gate/run_tests.py task-cycle` (235 tests), `elements/common` (117), `agent-instructions` (18), `instruction-files` (104), and `python -B elements/common/foundation_check.py` (0 errors, also with `--skip-test-citations`): all exit 0. The reviewer repeated the focused runs and the foundation check, exit 0 each.
- Own-work checks: the author compared every place that lists a report's sections with `grep` for both section names and found no listing place missed; after the fix it compared the quoted sentence with the text of the task, unchanged. The reviewer checked the sentence as a substring of the file and searched the dropped sentence of the older note: absent. The characterization tests passed on their first run and were not seen failing.
- No user interface changed, so there are no screenshot states.
- Form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/unread-material/request.md --task .runs/task-cycles/unread-material/task.md`, last run: pending.
- Check of private paths: on this description `python -B task-cycle/private_paths_check.py .runs/task-cycles/unread-material/request.md`, last run: pending; on the copy of the record and the image check on the copy: pending.
- Remarks check: `python -B task-cycle/remarks_check.py .runs/task-cycles/unread-material` on the original, last run exit 1 (4 runs): 8 items of the reports were appended to the process remarks word for word, and two lines remained listed that the cycle holds wrong — the line `---` that follows the last item of the **Searches not found or unclear** section of the author's report, and the line of the whole-change review's report that begins `as a bold label outside a list and then **Unread material** as a list item`, the second line of a wrapped sentence that mentions the section's name. Neither is an item of an agent's section, so neither was appended as an item; the case stands in the record's process remarks as an entry of the orchestrator.

## Foundation entries

1. WAY-325, `row 1`: when a report says that something its handoff names stayed unread or was read in part, the leader of the cycle decides before acting on its status — resume the agent, carry the gap to the next agent able to judge it, or record an autonomous choice with the reason it bears on nothing the agent judged. New; no existing entry stated it.
2. WAY-326, `row 2`: every stage report holds a section **Unread material** for what the handoff names (for the reviewer of the whole change: its own selection) that stayed unread or was read in part, or `none`, apart from the account of WAY-260; the leader reads it in every report whatever the status, and a report without it returns to its agent. New.
3. WAY-150, `row 3`, edited in place: the reviewer of the whole change reads whole the decisions of its selection that concern the topic of the change, skims the rest by title, opens every one whose title points to a bearing on the change and states in its report how many it read whole and how many by title only; every other agent reads what its handoff names whole. Its *Rejected* gained the three ways not chosen of the task's third question.
4. WAY-287, `row 4`, edited in place: the request's section for the human's decisions holds the incomplete reading of the review of the whole change, with "merge anyway?", only where the reviewer did not run through the rest of its selection by title or itself named a decision concerning the change as unread and the gap was not closed on the way. Its *Rejected* gained the two ways not chosen of the task's second question. Kept as an edit of the entry that holds the list, not a third new entry (Q2 of the record).
5. WAY-287, one clause added, `the cycle's` (fix of the Minor findings): the gap is closed on the way only by the reviewer, or a fresh one, reading what stayed unread; the leader's choice that it bears on nothing does not close it for the request.
6. WAY-326, two clauses added, `the cycle's` (fix of the Minor findings): a decision the reviewer of the whole change read by title as WAY-150 gives is no gap and stands in the section only in the counts; a report that returns `questions` is not returned for the section.
No invariant, no environment fact, no glossary term, no part-map entry and no *Violated* mark was written, changed, set or cleared. No invariant test was altered.

## Minor findings

1. `task-cycle/test_remarks_check.py:156-170` asserts the leak of **Unread material** into the Searches items as expected behaviour. If the script is later improved (the author's proposal in the first review: end the section at a bold label named `Unread material`), the test must be turned round, and the comment says only "recorded behaviour, not a wish". Suggested, only when the script is next touched: change the script and the test together. It blocks nothing, and the first review accepted the test as one of its two fixes (review of the fix of the Minor findings, `reports/review_fix_report.md`; new in the fix; not fixed because a Minor finding of a fix review goes to this list).

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task: what the leader of a task cycle does when an agent did not read the material it was pointed to — the sentence for the leader, the section in the five stage reports, the item in the request, and the title screening for the reviewer of the whole change (four points of *To do*, four answered questions, four settlements to record), stated on `foundations` `a3206c1` and reconciled against `02c3d47`, where the places the task names had moved; the outcome the task requires could still be established.
- **Process pin:** none; the cycle ran on the-way's own checkout.
- **Spec:** none; no open design choice (the name of the section and the wording of the sentences are choices of how to make what the task settles).
- **Route:** one author without a plan, class `same`, because the change touches the skill, five methods, a template, the way of working and four decisions across three parts. No attempt was discarded. The author was resumed twice, for the fix of the Minor findings and the return step; the return step committed nothing and had no review. The author's own reading was partial (65 of 160 decisions whole, 94 by title, no glossary entries); the cycle carried that gap to the reviewer of the whole change, who selected its own foundation, read the glossary whole and found no contradiction beyond its five Minor findings.
- **Plan:** none.
- **Choices:** 5 other choices, in the questions table of the record.
- **Blocking findings left:** none.
- **Record:** the link is added once the record is committed.
