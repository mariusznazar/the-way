**State: ready** — nothing blocks the merge; four items below wait for your answer.

## What you will see

When you refine a task or a project, a decision that the foundation already holds stops acting as a lock. The agent shows an option that changes such a decision the same way as any other option: it names the decision the option would change, gives its recommendation (also when it recommends the change), and asks no permission first. Your choice of that option is the one consent to the change; accepting the whole document afterwards does not ask about it again.

The challenge question after your answer is now asked at refinement only when your answer contradicts a sentence you said earlier yourself, and the question quotes that sentence. A loose remark or a change of a decision no longer draws one.

A row of the candidate table that only repeats a choice you made between options shown to you enters the table already accepted and marked. You strike it if you disagree; you cut only the rows the agent derived itself.

Nothing changes once a task's cycle starts: from its start, the spec written inside the cycle included, the agent of the cycle does not depart from a decision and comes back with the question. A decision projected by an approved project definition stays outside this; changing it still goes through the definition and its readiness gate.

### Underneath

The change is wording in the skills of refinement and in the foundation's log of decisions: three new decisions and eight edited ones. No script and no test changed.

## For you to decide

1. Two entries you did not see at the task document. First: a choice the technology step opened over a held decision is no longer held, so its recommended option is tested like any other (a consequence of the new rule). Second: at the start of a project definition the question whether the project changes an existing decision or fits it only frames the conversation, and the consent to a change is your choice of the option. Accept?
2. The task says the challenge question stays as it is "when an entry is written", and narrows it at refinement; it is silent on the entries of a project definition that are written during its refinement. The change reads them as part of the refinement, so they get the narrow question; the full question stays in a task's cycle and for entries written outside a refinement. Accept this reading, or should the full question stay for those entries?
3. When a task's run meets a held decision that is silent on part of a matter of logs, interface or development data, the step may open it, not must: the list shows in one sentence what the decision leaves unsaid and you open it by changing the list. The other way, always open, would grow your list at every such run. Accept?
4. One explanation of the decision on how an agent asks still says the full question stays "where an entry is written", which is true only outside a refinement; the binding sentence and the skill text are clear and agree. Fix it in this request, or make a task of it? (Minor findings, 1)

## Cost

About 36 minutes of working time in all. Every stage ran on one model, Sonnet 5.5: 33.5 million tokens in total, almost all of them read from cache (32.1 million), 0.17 million written as output. Two code reviews ran, one of the whole change and one of its fix, and neither found a blocking problem. The table of stages is in the committed record, linked under **Course of the cycle**.

## How to merge

Merge with a merge commit that keeps the commits; the link to the record survives only then. The record is added and removed in two commits at the end of the branch, so the changed files show only the change.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — nic nie blokuje scalenia; cztery punkty poniżej czekają na Twoją odpowiedź.

### Co zobaczysz

Gdy doprecyzowujesz zadanie albo projekt, decyzja, którą fundament już trzyma, przestaje działać jak zamek. Agent pokazuje opcję zmieniającą taką decyzję tak samo jak każdą inną: nazywa decyzję, którą opcja zmieniłaby, daje rekomendację (także gdy poleca zmianę) i nie pyta wcześniej o pozwolenie. Twój wybór tej opcji jest jedyną zgodą na zmianę; akceptacja całego dokumentu potem o nią nie pyta drugi raz.

Pytanie przeciw odpowiedzi pada teraz przy doprecyzowaniu tylko wtedy, gdy Twoja odpowiedź przeczy zdaniu, które sam wcześniej wypowiedziałeś, a pytanie to zdanie cytuje. Luźna uwaga ani zmiana decyzji go już nie wywołują.

Wiersz tabeli kandydatów, który tylko powtarza wybór dokonany przez Ciebie między pokazanymi opcjami, wchodzi do tabeli już przyjęty i oznaczony. Skreślasz go, jeśli się nie zgadzasz; tniesz tylko wiersze, które agent wyprowadził sam.

Gdy cykl zadania się zaczyna, nic się nie zmienia: od jego startu, z pisaniem specu w cyklu włącznie, agent cyklu nie odchodzi od decyzji i wraca z pytaniem. Decyzja rzutowana zatwierdzonej definicji projektu zostaje poza tą zmianą; jej zmiana nadal idzie przez definicję i jej bramkę gotowości.

#### Pod spodem

Zmiana to brzmienie w skillach doprecyzowania i w dzienniku decyzji fundamentu: trzy nowe decyzje i osiem poprawionych. Żaden skrypt ani test się nie zmienił.

### Do rozstrzygnięcia

1. Dwa wpisy, których nie widziałeś w dokumencie zadania. Pierwszy: wybór, który krok technologii otworzył nad trzymaną decyzją, przestaje być trzymany, więc jego polecana opcja jest testowana jak każda inna (skutek nowej reguły). Drugi: na początku definicji projektu pytanie, czy projekt zmienia istniejącą decyzję, czy się do niej dopasowuje, tylko ramuje rozmowę, a zgodą na zmianę jest Twój wybór opcji. Przyjmujesz?
2. Zadanie mówi, że pytanie przeciw odpowiedzi „przy zapisie wpisu” zostaje jak dziś, a przy doprecyzowaniu się zawęża; milczy o wpisach definicji projektu zapisywanych w trakcie jej doprecyzowania. Zmiana czyta je jako część doprecyzowania, więc dostają wąskie pytanie; pełne pytanie zostaje w cyklu zadania i dla wpisów zapisywanych poza doprecyzowaniem. Przyjmujesz to odczytanie, czy dla tych wpisów ma zostać pełne pytanie?
3. Gdy przebieg przy zadaniu trafia na trzymaną decyzję, która milczy o części sprawy dotyczącej logów, interfejsu albo danych deweloperskich, krok może ją otworzyć, ale nie musi: lista pokazuje jednym zdaniem, czego decyzja nie mówi, a Ty otwierasz ją zmianą listy. Droga odwrotna, zawsze otwierać, wydłużałaby Twoją listę przy każdym takim przebiegu. Przyjmujesz?
4. Jedno uzasadnienie decyzji o tym, jak agent pyta, wciąż mówi, że pełne pytanie zostaje „przy zapisie wpisu”, co jest prawdą tylko poza doprecyzowaniem; zdanie wiążące i tekst skilla są jasne i zgodne. Poprawić to w tym requeście, czy zrobić z tego zadanie? (Minor findings, 1)

### Koszt

łącznie ok. 36 minut pracy. Wszystkie etapy poszły na jednym modelu, Sonnet 5.5: 33,5 mln tokenów, prawie wszystkie odczytane z pamięci podręcznej (32,1 mln), 0,17 mln wyniku. Przeszły dwa przeglądy kodu, całej zmiany i jej poprawki, żaden nie znalazł problemu blokującego. Tabela etapów jest w zatwierdzonym zapisie przebiegu, z odnośnikiem w „Course of the cycle”.

### Jak scalić

Scal commitem scalającym, który zachowuje commity; odnośnik do zapisu przeżywa tylko wtedy. Zapis jest dodany i usunięty dwoma commitami na końcu brancha, więc zmienione pliki pokazują tylko zmianę.

</details>

## Technical changes

The change reaches three parts in two groups of commits, then a fix. Item 1 of each paragraph says what a reader sees; the places follow.

- Commit `8316d28`, the log of decisions (`foundations/decisions.md`): three new decisions and edits of eight; see **Foundation entries**.
- Commit `3cf2a09`, 18 files of the skills and templates: `project-level/technology/` (the list, the choice step, the run at a task, the running-product matters), `project-level/task/skill/` (resolve gaps, carry foundation, find settlements, orchestrated mode) and `project-level/task/template.md`, `project-level/definition_template.md`, `project-level/lead/`, `elements/common/way_of_working.md` and `elements/common/skill/` (the table of candidates, both variants). They carry the same rules as the decisions and say that the looser rules hold only before the cycle starts.
- Commit `d496942`, the fix for the four Minor findings of the review of the whole change (7 files, +56/-45): the definition-start question framed as no consent (`project-level/skill/read_foundation.md`, decision WAY-111), the narrow question at a definition's entry writing (WAY-113 and `elements/common/way_of_working.md`), the step "may open" a silent held decision (WAY-165, `project-level/technology/task_run.md`), and line wrapping. Its review passed.
- Not an edit of this request: a sibling task (`ready for cycle` in the backlog) rewords the same sentence of WAY-165. Whichever of the two merges second will find the wording of the first; the conflict, if any, is textual.

## Checks

- The gate, `python -B gate/run_tests.py`, run by the orchestrator on the final tree (`d496942`, the tree the request contains): exit 0, 804 tests in 9 directories, every directory passed. The same command on the base `354d37d`, before the change: exit 0, 804 tests; no check failed on the base. Nothing failed or did not run in the gate.
- Own-work checks: the author's check of the two acceptance criteria — a grep over the skills, templates and decisions for the old reservations, and a walk of one decision change through the files in the order an agent meets them — showed no old reservation left and one place that still asked at a definition's start (the Minor finding fixed in `d496942`). The reviewer repeated the grep and the walk.
- Focused checks of the author and the reviewers, each exit 0: `python -B elements/common/foundation_check.py` (0 errors), `python -B gate/run_tests.py` for `elements/common`, `project-level`, `task-cycle`, `agent-instructions` and `installation`, and `python -B agent-instructions/skill_entry_points.py` (entry points current). The `installation` directory was not rerun after the fix; the gate ran it on the final tree.
- Form check, `python -B task-cycle/request_check.py ... --task <frozen task>`: last run recorded in the record after the final edit.
- Check of private paths, `python -B task-cycle/private_paths_check.py`, on this description and on the copy of the record: recorded in the record after the final edit.
- Process remarks check, `python -B task-cycle/remarks_check.py`, on the original in `.runs/` (2 runs, the last exit 0, after appending the 10 items the reports gave) and on the copy of the record: recorded in the record after the final edit.
- No test was written: the change is Markdown, and no test of the-way reads the wording of these places.
- No user-interface state or screenshot applies.
- The part of each changed file: `project-level`, `elements-common` and `decisions` — the parts the task names; no file belongs to a part outside them.

## Foundation entries

Entries written whole from the accepted rows of the task (marked `row <n>`):

- WAY-313 (`row 1`, new): while a project definition or a task is refined, a decision of the foundation is material for revision, not a limit; a projected decision of an approved definition is outside.
- WAY-314 (`row 2`, new): the option that changes a decision names it in its line, and the human's choice of that option is the one consent.
- WAY-315 (`row 5`, new): a decision binds from the start of a task's cycle, the spec included; in the cycle no agent departs from a decision on its own.
- WAY-113 (`row 3`, edited): at refinement the question against an answer is asked only where the answer contradicts a quoted earlier sentence of the human; in the cycle and where an entry is written outside a refinement it stays as before.
- WAY-115, WAY-124, WAY-134 (`row 4`, edited): a row repeating a choice the human made between ways shown enters the table accepted and marked, stays unless the human strikes it, and counts as accepted for readiness.
- WAY-165, WAY-267 (`row 1`, edited): the reservation "opens only on the human's word" is gone; the step may open a choice a decision holds when it sees a reason to change it, and the human's choice is the consent.

Entries the human did not see at the task document (marked `the cycle's`, also in **For you to decide**, item 1):

- WAY-138 (`the cycle's`, wording): a choice the step opened over a decision is no longer held, so its recommended option is tested; the rule of what is tested is unchanged.
- WAY-111 (`the cycle's`, a framing clause added by the fix): the question at the start of a definition whether the project changes a decision or fits it only frames the conversation; the consent is the choice of the option.

No kept row tied to an entry already stated; no invariant test, surface or *Violated* mark changed.

## Minor findings

1. Fix of the Minor findings left this one: the *Rationale* of WAY-113 in `foundations/decisions.md` still says "Where an entry is written or a cycle runs, the answer is about to bind, so the question stays." After the fix the binding sentence says the entries written during a definition's refinement do not get the full question, so the sentence is true only of entries written outside such a refinement and of the cycle. The *Verification* of WAY-113 also speaks only of "the refinement of a task", not of a definition's refinement or its entries. The reviewer: "The *Rationale* should say "outside a refinement", and the *Verification* might name the definition. A reader of the rationale could take the stale sentence to override the binding sentence. Polish-level; the binding sentence and `way_of_working.md` are clear and agree." It lies within the task. The return step compared the entry with the files and did not name it; the orchestrator left it, since a Minor finding that remains after the fix goes to this list.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task: at refinement the decisions of the foundation are material and bind only from the start of a task's cycle; sources — the frozen task document of the record and the-way's `foundations` at `354d37d` (the task cites `a3206c1`; the places that moved were read again, the technology step now shows choices in one message and not a table).
- **Process pin:** not applicable — the-way itself, the base `354d37d`; the gate on it: exit 0, 804 tests.
- **Spec:** none written; the task leaves no open design choice, its five questions settle the shape and rows 1–5 are accepted.
- **Route:** one author without a plan, class `same`: Markdown wording across three parts, one agent holds it; the review of the whole change, one fix of its four Minor findings, a review of that fix, the return step.
- **Plan:** none.
- **Choices:** 5 other choices of the cycle (Q3–Q7 of the questions table), see the questions table of the committed record.
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds the record is written after that commit.
