**State: ready** — corrected for your remarks; nothing here waits for your answer, and what you accept by merging is listed below.

## What you will see

When an agent leads a project plan, each task it refines now gets its line in the product's backlog, with the right status, instead of you adding the lines by hand after every round. The refiner of a task that has no line yet makes it in the first turn in which it writes the task's document: it links the document, gives the line the status of a task still being refined, and, for a task of a plan, puts the plan's dependencies on it. The refiners of one round do this at the same time, with no queue; the small risk that two writes to the file land in the same instant and one line is lost is accepted, as you decided. When you accept a document, the agent leading the round moves the line to ready together with the document's status and the plan's row; a refiner never does. If a line could not be made in the first turn, because the rules for it were not yet known, or never existed, it is made in the first later turn that can, and at acceptance the leading agent makes it already ready.

A refiner that knows from the plan that one task waits on another also brings the lines of the tasks tied to its own into agreement, as the rules of the place give, whichever of the two tasks it is refining. The rules for a line are no longer written at the product or in the-way's skills: the status of a new line, its move to ready, the form of its dependencies, and now also how a line is handled — how it is found, that a task has one line only, which fields may change, how the two ends of a dependency are kept in agreement, and what to do when two lines would carry one identifier. The agent reads them from the rules of the place where the product keeps its tasks, which it finds through a second entry, next to the tasks' place, in your private locations file. In your vault the rulebook holds them; the paragraph on the line of a plan's task was written there in this session, at your word, and is no part of this request. Where the entry or the rules are missing, or say nothing of how to handle a line, the agent asks you once and offers to add the entry. The same holds for refining a task by hand. The instruction file of the-way itself names the new entry instead of repeating the old sentence about moving a line to ready.

### Underneath

The line's identifier, which dependencies point at, is computed by a rule from the plan's file name and the task's name in the plan, so that a refiner can write it into a dependent task's line before the other task's line exists. The-way keeps only what it alone knows — when a line is made, who moves it to ready, where the dependencies come from, how the identifier is derived; the way a line is handled is left to the rules of the place.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. The identifier of a plan task's line is the plan's file name without its extension, joined by a hyphen to the task's name in the plan, in lower case, each run of other characters turned into one hyphen. It is unique in the tasks' place only while plan file names differ and no two plan-and-task pairs join into the same text; what an agent does where another line already carries it is a rule of the place, not of the-way. The task left the derivation to the cycle; the cycle chose the simplest form computable from the plan alone, and rejected one counted when a line is made, since a refiner could not know it before the other line exists. The decision that records it has no source listed, because the source is the rules in your private notes, which no file of the repository may quote; you may prefer a marker for the missing source instead.
2. Choices the task did not settle. A refiner also writes the lines of the tasks tied to its own, which is your rule from this request. After the agent that edits the plan changes a dependency, the leading agent corrects the lines. A refiner, after you agree in the conversation, writes a missing entry for the rules into your locations file itself, instead of the leading agent doing it. Where the leading agent finds no line at acceptance, it makes it already ready, a narrow fallback to the duty you declined to give it in general, kept so that a line lost in the race you accepted still comes back. A task that already has a line gets no second one; the rules of the place say what to do with it. Where the place has no rules at all, the agent only asks, as the task said.
3. The cycle wrote or changed entries beyond what the task listed: the decision about the identifier (item 1); a correction of the rule that lets the instruction file point outside the repository, so that it also covers the rules' entry; one clause in the map of parts saying that the part for the project level also answers for how a task's line is made, given its dependencies and moved to ready; the rule added to the decision on where the backlog stands, that how a line is handled comes from the rules of the place, which is your direction; and the refiner's write to the lines of tied tasks in the decision on how a refinement round works, which is your rule.
4. The rules for handling a line stand in your rulebook alone and in no file of this repository, so that the merge of this request relies on a paragraph that is not in it. A checkout of the-way merged without that paragraph in your rulebook would make an agent ask you once, as it does for any missing rule.

## Cost

About 1 hour 28 minutes of working time and about 71 million tokens, all on one model family: one author, five reviews of code, two fixes and one correction. The whole change failed its review once and the correction failed its review once; each fix and the return step passed theirs. The full table of stages stands in the record: `stages.md` in the committed record.

## How to merge

Merge with a merge commit, which keeps the commits; the link to the record survives only then. The foundation has waited for a review through 23 merges since the last tag, below the threshold of 30, so nothing is asked of you here.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — poprawiony po Twoich uwagach; nic tu nie czeka na Twoją odpowiedź, a to, co akceptujesz scaleniem, jest wypisane niżej.

## Co zobaczysz

Gdy agent prowadzi plan projektu, każde zadanie, które doprecyzowuje, dostaje teraz linię w backlogu produktu z właściwym statusem, zamiast dopisywania linii ręcznie po każdej rundzie. Refiner zadania, które nie ma jeszcze linii, zakłada ją w pierwszej turze, w której pisze dokument zadania: linkuje dokument, nadaje status zadania w doprecyzowaniu, a dla zadania z planu wpisuje na linię zależności z planu. Refinerzy jednej rundy robią to równolegle, bez kolejki; małe ryzyko, że dwa zapisy do pliku trafią w tę samą chwilę i jedna linia zginie, jest przyjęte, tak jak zdecydowałeś. Gdy akceptujesz dokument, agent prowadzący rundę przestawia linię na gotową razem ze statusem dokumentu i wierszem planu; refiner nigdy tego nie robi. Jeśli linii nie dało się założyć w pierwszej turze, bo nie znano jeszcze zasad, albo nigdy jej nie było, powstaje w pierwszej późniejszej turze, która może, a przy akceptacji agent prowadzący zakłada ją od razu jako gotową.

Refiner, który wie z planu, że jedno zadanie czeka na drugie, doprowadza też do zgodności linie zadań powiązanych z jego zadaniem, tak jak mówią zasady miejsca, niezależnie od tego, które z dwóch zadań doprecyzowuje. Zasady linii nie są już zapisane przy produkcie ani w skillach the way: status nowej linii, jej przejście na gotową, forma zależności, a teraz także to, jak się z linią obchodzić — jak ją znaleźć, że zadanie ma tylko jedną linię, które pola wolno zmienić, jak utrzymać w zgodzie oba końce zależności i co robić, gdy dwie linie miałyby nosić jeden identyfikator. Agent czyta je z zasad miejsca, w którym produkt trzyma zadania, a dochodzi do nich przez drugi wpis, obok miejsca zadań, w Twoim prywatnym pliku lokalizacji. W Twoim vaulcie trzyma je rulebook; akapit o linii zadania z planu został tam dopisany w tej sesji, na Twoje słowo, i nie należy do tego requestu. Gdy wpisu albo zasad brakuje, albo nie mówią, jak obchodzić się z linią, agent pyta Cię raz i proponuje dopisanie wpisu. To samo obowiązuje przy doprecyzowaniu ręcznym. Plik instrukcji samego the way wymienia teraz ten wpis zamiast starego zdania o przestawianiu linii na gotową.

### Pod spodem

Identyfikator linii, na który wskazują zależności, jest liczony regułą z nazwy pliku planu i nazwy zadania w planie, żeby refiner mógł wpisać go w linię zadania zależnego, zanim linia tamtego zadania powstanie. The way trzyma tylko to, co wie wyłącznie ono — kiedy linia powstaje, kto przestawia ją na gotową, skąd biorą się zależności, jak liczy się identyfikator; sposób obchodzenia się z linią zostawia zasadom miejsca.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawienia albo przepuszczenia

none

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

1. Identyfikator linii zadania z planu to nazwa pliku planu bez rozszerzenia, połączona myślnikiem z nazwą zadania w planie, małymi literami, a każdy ciąg innych znaków zamieniony na jeden myślnik. Jest jednoznaczny w miejscu zadań tylko, gdy nazwy plików planów się różnią i żadne dwie pary plan–zadanie nie sklejają się w ten sam tekst; co agent robi, gdy inna linia już go nosi, jest regułą miejsca, nie the way. Zadanie zostawiło wyprowadzenie cyklowi; cykl wybrał najprostszą formę liczoną z samego planu i odrzucił formę liczoną przy zakładaniu linii, bo refiner nie mógłby jej znać, zanim powstanie linia tamtego zadania. Decyzja, która to zapisuje, nie ma wymienionego źródła, bo źródłem są zasady w Twoich prywatnych notatkach, których żaden plik repozytorium nie może cytować; możesz woleć znacznik braku źródła.
2. Wybory, których zadanie nie rozstrzygnęło. Refiner zapisuje też linie zadań powiązanych ze swoim, co jest Twoją regułą z tego requestu. Po zmianie zależności przez agenta edytującego plan agent prowadzący poprawia linie. Refiner, po Twojej zgodzie w rozmowie, sam dopisuje brakujący wpis z zasadami do Twojego pliku lokalizacji, zamiast agenta prowadzącego. Gdy agent prowadzący nie znajdzie linii przy akceptacji, zakłada ją od razu jako gotową — wąski zapas do obowiązku, którego mu w ogóle nie dałeś, zostawiony po to, żeby linia zgubiona w wyścigu, który przyjąłeś, jednak wracała. Zadanie, które ma już linię, nie dostaje drugiej; co z nią zrobić, mówią zasady miejsca. Gdy miejsce nie ma żadnych zasad, agent tylko pyta, jak mówiło zadanie.
3. Cykl zapisał albo zmienił wpisy poza tym, co wymieniało zadanie: decyzję o identyfikatorze (pozycja 1); poprawkę reguły, która pozwala plikowi instrukcji wskazywać poza repozytorium, żeby obejmowała też wpis z zasadami; jedną klauzulę w mapie części mówiącą, że część poziomu projektu odpowiada też za to, jak powstaje linia zadania, jak dostaje zależności i jak przechodzi na gotową; regułę dodaną do decyzji o tym, gdzie stoi backlog — że sposób obchodzenia się z linią pochodzi z zasad miejsca — co jest Twoim kierunkiem; oraz zapis refinera do linii zadań powiązanych w decyzji o przebiegu rundy doprecyzowania, co jest Twoją regułą.
4. Zasady obchodzenia się z linią stoją tylko w Twoim rulebooku i w żadnym pliku tego repozytorium, więc scalenie tego requestu opiera się na akapicie, którego w nim nie ma. Kopia the way scalona bez tego akapitu w Twoim rulebooku sprawiłaby, że agent zapyta Cię raz, jak przy każdej brakującej regule.

## Koszt

Około 1 godziny 28 minut czasu pracy i około 71 milionów tokenów, wszystko na jednej rodzinie modeli: jeden autor, pięć przeglądów kodu, dwie poprawki i jedna korekta. Przegląd całości zmiany nie przeszedł raz, przegląd korekty nie przeszedł raz, a każda poprawka i krok powrotu przeszły swój przegląd. Pełna tabela etapów jest w zapisie cyklu: `stages.md` in the committed record.

## Jak scalić

Scal commitem scalającym, który zachowuje commity; link do zapisu cyklu przeżywa tylko tak. Fundament czekał na przegląd przez 23 scalenia od ostatniego tagu, poniżej progu 30, więc nic tu od Ciebie nie jest wymagane.

</details>

## Technical changes

The change has eight commits on top of the base `52f8164`, then the record's pair; each paragraph opens with what it means for someone working with the process.

- `74fbd01` — the decisions that bind the new behaviour are written: a refiner may write what the leading agent orders, among it a task's line; nobody but the leading agent, after the human's word, takes the step that belongs to acceptance (WAY-154, WAY-107, WAY-320, WAY-27 in `foundations/decisions.md`).
- `9eb2bd6` — the skills and templates say what the decisions say: a new file `project-level/task_line.md`, `project-level/backlog_place.md` finds the `task-rules` entry, the refiner and leading-agent skills carry the new split of writes, `AGENTS.md` names the new entry. Three files lie outside what the author's handoff listed (`route_changes.md`, `task/template.md`, `plan/skill/delegated_mode.md`); the review judged each within the task.
- `9d5743d` — the one fix for the review of the whole change: its blocking finding (no route for a line the first turn could not make) and its six Minor findings; the rule of when a line is made now stands in `project-level/task_line.md` alone.
- `06144e9` — the return step: WAY-329 written, an example of WAY-154 extended, one clause added to the `project-level` entry of `foundations/part_map.md`.
- `047a9e7` — the correction for your remarks: how a line is handled left the-way's skills and decisions for the rules of the place (`project-level/task_line.md`, WAY-154, WAY-107, WAY-329 and the pointers in four skill files), WAY-329 lost the clash clause, the long lines and the sentence counts of the entries were put right, the word "line" replaced "entry" in `project-level/task/skill/read_sources.md`. The author rewrapped whole paragraphs of five entries, so the diff of `foundations/decisions.md` is large; the reviewer compared them word by word and found only line breaks changed in WAY-27 and WAY-320.
- `80126da` — the one fix for the blocking finding of the review of that correction: WAY-154 now gives the refiner the write to the lines of tied tasks that the four skill files already carried.
- The record of the cycle is added by one commit and removed by the next, so that the target branch never holds it.

## Checks

- Gate on the final tree `80126da`: `python -B gate/run_tests.py`, exit 0, 919 tests in 9 directories, every directory passed. On the base `52f8164`, in a separate checkout: exit 0, 919 tests in 9 directories, every directory passed. On the earlier tree `06144e9` the same run also passed.
- Focused runs by the agents, all exit 0 at each stage: `python -B elements/common/foundation_check.py` ("0 errors"), `python -B instruction-files/check_instructions.py .` ("0 error, 0 warn, 3 info"), `python -B task-cycle/test_tracked_files_private_paths.py` (1 test OK); by the first author also `python -B gate/run_tests.py task-cycle` (263 OK), `agent-instructions` (18 OK), `gate` (20 OK) and `project-level` (275 OK on the second run; the first run printed an unexplained `F` and was cut by the author's own timeout, exit 124). The two gate runs on the final trees covered that directory again without a failure.
- Own-work checks: the identifier derivation (a double hyphen found in the first wording, corrected; a run on four inputs, exit 0); `grep` for one place of the moment of making a line; `grep` that no tracked file of the-way holds a rule of handling a line (exit 0, every hit read); `grep` for the phrase "tied to" (the write now stands in WAY-154 and in the four skill files). They are reading and `grep`, not tests; no test reaches skill text.
- Reviews: whole change `FAIL`, fix `PASS`; return step `PASS`; correction `FAIL` (one blocking finding), its fix `PASS`.
- Form check of this description: pending the last run. Check of private paths on this description: pending the last run.
- On the copy of the record: pending the copy.
- Not checked: how the tasks plugin reads a dependency on an identifier nobody carries (outside the repository). The review of the whole change read 28 decisions whole and 114 by title, and named six decisions that bear on the change as not read; you let that through.

## Foundation entries

- WAY-154 (rows 1, 2, 5; the cycle's for the tied lines): a refiner writes what the leading agent orders, among it the task's line with the plan's dependencies in its first turn that creates the document (or the first later turn that can), in parallel with the round's other refiners and with no queue of writes, and brings the lines of the tasks tied to its task into agreement with the plan's dependencies as the rules of the task place give; no agent but the leading agent, on the human's word, moves the line to ready or writes `ready for cycle`; the leading agent moves the line with the status and the plan's row, makes it already ready where none stands, and keeps the lines' dependencies in step when the plan's dependencies change; the cost of the dependency copy is accepted.
- WAY-107 (rows 3, 4; the cycle's for the added rule): the status of a new line, its move to ready, the form of its dependencies and how a line is handled come from the rules of the task place, never from text at the product or in the-way's skills; the section names them by the entry `task-rules` under the product's name, and where it or its file is missing the agent asks once and offers to add the entry.
- WAY-320 (row 4): the locations file also holds the entry `task-rules` per product, beside `tasks` and `projects`; a single entry shared by all products is a rejected way.
- WAY-27 (the cycle's): the one exception to "no pointer outside the repository" covers the rules of the task place named in `## Backlog` by an entry of the locations file, beside the place of the tasks.
- WAY-329 (the cycle's): a refiner computes the identifier of a plan task's line from the plan's file name and the task's plan name, lower-cased, runs of other characters as one hyphen, so that it can write it in another task's dependency before that line exists; it is unambiguous only while plan file names differ and no two pairs join alike.
- Part map, `project-level` (the cycle's): the part also answers for how a task's line is made, given dependencies and moved to ready.
- Rows of *Settlements to record*: row 1 → WAY-154; row 2 → WAY-154; row 3 → WAY-107; row 4 → WAY-107 and WAY-320; row 5 → WAY-154. No invariant, environment fact or glossary entry was written or changed.

## Minor findings

Unfixed, with the reviewers' words and places. The Minor findings of the first reviews were all fixed by the fixes and the correction; these are those of the review of the correction and of its fix.

1. Review of the correction: "Four skill files have lines over 100 characters, which the correction report says do not exist. `project-level/lead/skill/SKILL.md:105-106` (the last line of the item is 158 characters, new in this commit), `project-level/lead/conversation_template.md:23` (102), `project-level/task_line.md:56` (101), and `product-guidelines/coding/orchestrated_mode.md:9` (111, from the earlier fix) […] the skills' lines are cosmetic."
2. Review of the correction: "The part map says the part answers for 'how the line of a task ... is made'. `foundations/part_map.md` (the `project-level` entry) and `project-level/backlog_place.md:15-20` ('`project-level/task_line.md` says how a line is written by them') now read broader than the-way's side after the correction, which moved how a line is handled to the rules of the task place. […] reword 'how ... is made' to 'when and by whom ...' at the next touch." (Neither the part map nor `backlog_place.md` was reworded; they stand as the finding found them.)
3. Review of the correction: "`project-level/task_line.md:10` still says 'where the rules give none of the three forms', after the opening list grew to six matters (`:3-9`), so 'three' has no referent; and `task_line.md:22-23` and `:55-56` say what a line carries, which WAY-107's new sentence leaves to the place's rules only for 'how a line is found and which fields may change', so no breach, but the boundary is not drawn in the file. Reword 'the three forms' to 'the forms'."
4. Review of the fix of the correction: "WAY-154 uses 'tied' without defining it, and the *complies* example covers only one direction. Only `task_line.md` says tied means a task it waits on or one that waits on it."

## Findings outside the task's scope

1. Review of the whole change: "A task returned to refinement keeps a Ready line. `project-level/task/skill/draft.md:11-15` and `project-level/lead/skill/task_return.md:7-10` return a task (document `refining`, plan row `to refine`) with no word about its backlog line, so after this change a line moved to Ready stays Ready while the document is in refinement, and the vault's check of notes against lines would report it. The task's *Out of scope* names only `in cycle` and `done`; this transition is in neither the task nor its sources. Minor, for the human to put into a task." You let it through ("a to bym olał").
2. Review of the return step, earlier counted here: a task that already has a line gets no identifier from the refiner. The correction addresses it: the rules of the place, in your rulebook, now say that a refiner adds the missing identifier and dependency fields to existing lines at both ends of a dependency, and WAY-154 gives the refiner that write. Not a finding left open.

## Course of the cycle

- **Task and sources:** an independent task from the author's private notes, `Status: ready for cycle`, settlements accepted 2026-11-11; its goal: every task of a project plan gets a backlog line with the right status. Its human action (the `task-rules` entry in the locations file) was done before the cycle. Source revision: base `52f8164`.
- **Process pin:** not applicable; the cycle ran on the-way's own checkout and the task moves no pin.
- **Spec:** none; no open design choice at the start (the five settlements settle the decisions; how the identifier is derived was left as a choice of making).
- **Route:** one author without a plan, on the same class as the orchestrator (Sonnet 5.5), because the change crosses three parts and rewords decisions in place; the whole change reviewed by a fresh agent, one fix, a review of the fix, the return step, a review of the return step (interrupted once by a restart of the computer and resumed on the same range), then a correction for your remarks, the review of it, one fix and a review of that fix.
- **Plan:** none.
- **Choices:** 11 other choices, in the record's questions table: `cycle.md` in the committed record.
- **Blocking findings left:** none.
- **Record:** pending the commit that adds it
