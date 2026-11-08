**State: ready** — corrected for your remarks; nothing blocks the merge, and one item below waits for your answer.

## What you will see

When you refine a task or a project, a decision that the foundation already holds stops acting as a lock. The agent shows an option that changes such a decision the same way as any other option: it names the decision the option would change, gives its recommendation (also when it recommends the change), and asks no permission first. Your choice of that option is the one consent to the change; accepting the whole document afterwards does not ask about it again.

The challenge question after your answer is now asked at refinement only when your answer contradicts a sentence you said earlier yourself, and the question quotes that sentence. A loose remark or a change of a decision no longer draws one.

A row of the candidate table that only repeats a choice you made between options shown to you enters the table already accepted and marked. You strike it if you disagree; you cut only the rows the agent derived itself.

Nothing changes once a task's cycle starts: from its start, the spec written inside the cycle included, the agent of the cycle does not depart from a decision and comes back with the question. A decision projected by an approved project definition stays outside this; changing it still goes through the definition and its readiness gate.

### Underneath

The change is wording in the skills of refinement and in the foundation's log of decisions: three new decisions and eight edited ones. No script and no test changed.

## For you to decide

1. The step of a project definition that restates your words and asks whether their consequence holds, and the anchor "from the material" it may use, can still draw a question after your answer for the entries written during a definition's refinement; the task narrowed only the contradiction move, so the change left this one as it was. Recommendation: leave it unless it draws questions you do not want in practice. Leave it, or make a task of it? (Technical changes, 5)

## Cost

About 46 minutes of working time in all, the correction included. Every stage ran on one model, Sonnet 5.5: 47.6 million tokens in total, almost all of them read from cache (45.4 million), 0.23 million written as output. Three code reviews ran, of the whole change, of its fix and of the correction, and none found a blocking problem; one correction ran after your remarks. The table of stages is in the committed record, linked under **Course of the cycle**.

## How to merge

Merge with a merge commit that keeps the commits; the link to the record survives only then. The record is added and removed in two commits at the end of the branch, so the changed files show only the change.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — poprawione według Twoich uwag; nic nie blokuje scalenia, a jeden punkt poniżej czeka na Twoją odpowiedź.

### Co zobaczysz

Gdy doprecyzowujesz zadanie albo projekt, decyzja, którą fundament już trzyma, przestaje działać jak zamek. Agent pokazuje opcję zmieniającą taką decyzję tak samo jak każdą inną: nazywa decyzję, którą opcja zmieniłaby, daje rekomendację (także gdy poleca zmianę) i nie pyta wcześniej o pozwolenie. Twój wybór tej opcji jest jedyną zgodą na zmianę; akceptacja całego dokumentu potem o nią nie pyta drugi raz.

Pytanie przeciw odpowiedzi pada teraz przy doprecyzowaniu tylko wtedy, gdy Twoja odpowiedź przeczy zdaniu, które sam wcześniej wypowiedziałeś, a pytanie to zdanie cytuje. Luźna uwaga ani zmiana decyzji go już nie wywołują.

Wiersz tabeli kandydatów, który tylko powtarza wybór dokonany przez Ciebie między pokazanymi opcjami, wchodzi do tabeli już przyjęty i oznaczony. Skreślasz go, jeśli się nie zgadzasz; tniesz tylko wiersze, które agent wyprowadził sam.

Gdy cykl zadania się zaczyna, nic się nie zmienia: od jego startu, z pisaniem specu w cyklu włącznie, agent cyklu nie odchodzi od decyzji i wraca z pytaniem. Decyzja rzutowana zatwierdzonej definicji projektu zostaje poza tą zmianą; jej zmiana nadal idzie przez definicję i jej bramkę gotowości.

#### Pod spodem

Zmiana to brzmienie w skillach doprecyzowania i w dzienniku decyzji fundamentu: trzy nowe decyzje i osiem poprawionych. Żaden skrypt ani test się nie zmienił.

### Do rozstrzygnięcia

1. Krok definicji projektu, który powtarza Twoje słowa i pyta, czy ich skutek też obowiązuje, oraz kotwica „z materiału”, której może użyć, mogą jeszcze po Twojej odpowiedzi wywołać pytanie przy wpisach zapisywanych w trakcie doprecyzowania definicji; zadanie zawęziło tylko ruch ze sprzecznością, więc zmiana zostawiła ten bez zmian. Rekomendacja: zostawić, dopóki w praktyce nie wywoła pytań, których nie chcesz. Zostawić, czy zrobić z tego zadanie? (Technical changes, 5)

### Koszt

łącznie ok. 46 minut pracy, z korektą. Wszystkie etapy poszły na jednym modelu, Sonnet 5.5: 47,6 mln tokenów, prawie wszystkie odczytane z pamięci podręcznej (45,4 mln), 0,23 mln wyniku. Przeszły trzy przeglądy kodu, całej zmiany, jej poprawki i korekty, żaden nie znalazł problemu blokującego; po Twoich uwagach przeszła jedna korekta. Tabela etapów jest w zatwierdzonym zapisie przebiegu, z odnośnikiem w „Course of the cycle”.

### Jak scalić

Scal commitem scalającym, który zachowuje commity; odnośnik do zapisu przeżywa tylko wtedy. Zapis jest dodany i usunięty dwoma commitami na końcu brancha, więc zmienione pliki pokazują tylko zmianę.

</details>

## Technical changes

The change reaches three parts in two groups of commits, then a fix. Item 1 of each paragraph says what a reader sees; the places follow.

- Commit `8316d28`, the log of decisions (`foundations/decisions.md`): three new decisions and edits of eight; see **Foundation entries**.
- Commit `3cf2a09`, 18 files of the skills and templates: `project-level/technology/` (the list, the choice step, the run at a task, the running-product matters), `project-level/task/skill/` (resolve gaps, carry foundation, find settlements, orchestrated mode) and `project-level/task/template.md`, `project-level/definition_template.md`, `project-level/lead/`, `elements/common/way_of_working.md` and `elements/common/skill/` (the table of candidates, both variants). They carry the same rules as the decisions and say that the looser rules hold only before the cycle starts.
- Commit `d496942`, the fix for the four Minor findings of the review of the whole change (7 files, +56/-45): the definition-start question framed as no consent (`project-level/skill/read_foundation.md`, decision WAY-111), the narrow question at a definition's entry writing (WAY-113 and `elements/common/way_of_working.md`), the step "may open" a silent held decision (WAY-165, `project-level/technology/task_run.md`), and line wrapping. Its review passed.
- Commit `c8bf864`, the correction for your remark on the explanation of WAY-113 (`foundations/decisions.md`, +13/-9): its *Rationale* now says that the full question stays where an entry is written outside a refinement and in a cycle, and that the entries written during a refinement, such as the projected entries of a definition, follow the rule of the refinement; its *Verification* names a project definition and the entries written during it. The binding sentence you accepted is untouched. The return step repeated for it changed nothing. Its review passed.
- Left unchanged and put before you (**For you to decide**, 1): `elements/common/skill/definition_variant.md`, step 4, item 1, the "implication" move and the anchor "from the human's words or from the material", which the task does not name for narrowing.
- Not an edit of this request: a sibling task (`ready for cycle` in the backlog) rewords the same sentence of WAY-165. Whichever of the two merges second will find the wording of the first; the conflict, if any, is textual.

## Checks

- The gate, `python -B gate/run_tests.py`, run by the orchestrator on the final tree after the correction (`c8bf864`, the tree the request contains): exit 0, 804 tests in 9 directories, every directory passed. The same command on the tree before the correction (`d496942`): exit 0, 804 tests; on the base `354d37d`, before the change: exit 0, 804 tests. No check failed on the base. Nothing failed or did not run in the gate.
- Own-work checks: the author's check of the two acceptance criteria — a grep over the skills, templates and decisions for the old reservations, and a walk of one decision change through the files in the order an agent meets them — showed no old reservation left and one place that still asked at a definition's start (fixed in `d496942`). The reviewer repeated the grep and the walk. For the correction, the author's search for the same stale wording in other files found none, and the reviewer confirmed it.
- Focused checks of the author and the reviewers, each exit 0: `python -B elements/common/foundation_check.py` (0 errors, last run on `c8bf864`), `python -B gate/run_tests.py` for `elements/common`, `project-level`, `task-cycle`, `agent-instructions` and `installation`, and `python -B agent-instructions/skill_entry_points.py` (entry points current).
- Form check, `python -B task-cycle/request_check.py docs/task-cycles/decisions-as-material-at-refinement/request.md --task docs/task-cycles/decisions-as-material-at-refinement/task.md`: run after every edit of this description, the last exit 0.
- Check of private paths, `python -B task-cycle/private_paths_check.py`: on this description run after every edit, the last exit 0; on the copy of the record, `docs/task-cycles/decisions-as-material-at-refinement`, run on the copy of this correction, exit 0 (see **Course of the cycle** for the commit; the earlier copy of the first run needed a wider cleaning rule once).
- Process remarks check, `python -B task-cycle/remarks_check.py`: on the original in `.runs/`, the last run exit 0 with 11 items in the process remarks of the record (10 from the first run, 1 from the correction's return step); on the copy of the record, exit 0, 0 items not in the remarks.
- No test was written: the change is Markdown, and no test of the-way reads the wording of these places.
- No user-interface state or screenshot applies.
- The part of each changed file: `project-level`, `elements-common` and `decisions` — the parts the task names; no file belongs to a part outside them.

## Foundation entries

Entries written whole from the accepted rows of the task (marked `row <n>`):

- WAY-313 (`row 1`, new): while a project definition or a task is refined, a decision of the foundation is material for revision, not a limit; a projected decision of an approved definition is outside.
- WAY-314 (`row 2`, new): the option that changes a decision names it in its line, and the human's choice of that option is the one consent.
- WAY-315 (`row 5`, new): a decision binds from the start of a task's cycle, the spec included; in the cycle no agent departs from a decision on its own.
- WAY-113 (`row 3`, edited): at refinement the question against an answer is asked only where the answer contradicts a quoted earlier sentence of the human; in the cycle and where an entry is written outside a refinement it stays as before. The correction made its *Rationale* and *Verification* say the same as its binding sentence, entries written during a refinement included.
- WAY-115, WAY-124, WAY-134 (`row 4`, edited): a row repeating a choice the human made between ways shown enters the table accepted and marked, stays unless the human strikes it, and counts as accepted for readiness.
- WAY-165, WAY-267 (`row 1`, edited): the reservation "opens only on the human's word" is gone; the step may open a choice a decision holds when it sees a reason to change it, and the human's choice is the consent.

Entries the human did not see at the task document (marked `the cycle's`; accepted by the human on this request in the correction's conversation):

- WAY-138 (`the cycle's`, wording): a choice the step opened over a decision is no longer held, so its recommended option is tested; the rule of what is tested is unchanged.
- WAY-111 (`the cycle's`, a framing clause added by the fix): the question at the start of a definition whether the project changes a decision or fits it only frames the conversation; the consent is the choice of the option.

No kept row tied to an entry already stated; no invariant test, surface or *Violated* mark changed.

## Minor findings

none

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task: at refinement the decisions of the foundation are material and bind only from the start of a task's cycle; sources — the frozen task document of the record and the-way's `foundations` at `354d37d` (the task cites `a3206c1`; the places that moved were read again, the technology step now shows choices in one message and not a table).
- **Process pin:** not applicable — the-way itself, the base `354d37d`; the gate on it: exit 0, 804 tests.
- **Spec:** none written; the task leaves no open design choice, its five questions settle the shape and rows 1–5 are accepted.
- **Route:** one author without a plan, class `same`: Markdown wording across three parts, one agent holds it; the review of the whole change, one fix of its four Minor findings, a review of that fix, the return step. Correction 1 for the human's remark on item 4 of the earlier description (the remarks: `reports/correction_remarks.md` of the record; reset base: none, the branch moved forward from `ff395cf`): the author resumed, commit `c8bf864`, its review `PASS`, the gate, the return step repeated, the record added and removed again.
- **Plan:** none.
- **Choices:** 6 other choices of the cycle (Q3–Q8 of the questions table), see the questions table of the committed record.
- **Blocking findings left:** none.
- **Record:** commit `53ed6b528e61858b998a93151a909bbd34361bc2`: https://github.com/mariusznazar/the-way/blob/53ed6b528e61858b998a93151a909bbd34361bc2/docs/task-cycles/decisions-as-material-at-refinement/cycle.md ; table of stages: https://github.com/mariusznazar/the-way/blob/53ed6b528e61858b998a93151a909bbd34361bc2/docs/task-cycles/decisions-as-material-at-refinement/stages.md ; the questions table is in `cycle.md`.
