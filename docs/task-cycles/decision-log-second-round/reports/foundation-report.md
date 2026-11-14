# Foundation entries report — decision-log-second-round

## Turn 1 — rows F1, F2, F3

**Status:** done with concerns (the second check of the handoff cannot exit 0; see Checks).

**Commit:** `8d04d89` on `task/decision-log-second-round` (one file, `foundations/decisions.md`, 126 insertions, 72 deletions at the first count; no other file of the worktree changed). Nothing pushed.

### Checks (command and exit code)

| Command | Exit | Printed |
|---|---|---|
| `python -B elements/common/foundation_check.py` (before my first edit) | 0 | `0 errors` |
| `python -B elements/common/foundation_check.py` (after the edits, before the commit) | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/decisions` | 1 | `no test found in elements/decisions` |
| `python -B gate/run_tests.py elements/common` (extra; the directory that holds `test_foundation_check.py`) | 0 | `Ran 201 tests ... OK` |

Mismatch with the handoff: `elements/decisions` holds no test, so the runner exits 1 on any change. This is not a failure of my work; the tests that read `foundations/decisions.md` are those of `elements/common`, which pass. The planner's slice 1 names the same kind of check for `elements/common` and `elements/part-map`. The exit code 0 asked of the foundation check before turn 2 is met.

### Own-work check (make-change section 3)

- Requirement most likely unmet: the addition to WAY-100 in the exact words of the task's answer 2 (the task: "copied word for word").
- Check: a script took the English text between the Polish quotation marks of line 430 of the frozen task, collapsed every run of whitespace, and looked for it in the collapsed text of the entry WAY-100 of the log (the paragraph wraps lines). Result: found (`True`, 471 characters). Run once; no failing run to record.
- Second check: a script read the `Relations` line of every decision and compared it with the lists of the plan. Result: all 14 entries of (a) and 10 of (b) have `derives from WAY-100`; none of (c) and (d) has it; no decision outside (a) and (b) has it.

### Entries written (each marked by the plan's row; the task's *Settlements to record* reads `TODO`, so the plan's rows F1 to F3 are the rows)

Row F1
- WAY-100 (changed): the second paragraph is the task's addition word for word; *Verification* gets a complying example (and a violating one), *Rationale* a sentence of why, *Rejected* the way the task's answer 2 rejects (the sentence only in the skill that looks for candidates).
  - EN: A decision that adopts an outside practice names the practice and what it takes, names the source in *Based on* (or describes a source nobody can open in *Rationale*), and puts what it leaves out in *Rejected*; a list of what is taken is no decision.
  - PL: Decyzja, która przejmuje praktykę z zewnątrz, nazywa praktykę i to, co z niej bierze, podaje źródło w *Based on* (a źródło, którego nikt nie otworzy, opisuje w *Rationale*) i zapisuje w *Rejected*, czego nie bierze; lista tego, co się bierze, nie jest decyzją.

Row F2
- WAY-29 (changed): a third binding sentence; *Verification*, *Rationale* follow it.
  - EN: The description of the commit, or of the merged request, that brought the shape of the code is a source an agent looks at before it writes `unknown` and quotes with the identifier of the commit.
  - PL: Opis commita albo scalonej prośby, który wprowadził kształt kodu, jest źródłem, do którego agent zagląda, zanim wpisze `unknown`, i które cytuje z identyfikatorem commita.

Row F3 (a), relation stays — changed
- WAY-121: the lesson's hard limit moved from *Rationale* to *Rejected*. EN: The step takes from the lesson the question of how an agent sees the running product and leaves out the lesson's hard limit. PL: Krok bierze z lekcji pytanie, jak agent widzi działający produkt, i pomija twardy limit lekcji.
- WAY-138: *Based on* `TODO` (the source of the three tests). EN: The step takes three tests of a recommendation (a devil's advocate, a pre-mortem, a search for unknown unknowns), source not given. PL: Krok bierze trzy testy rekomendacji (adwokat diabła, pre-mortem, szukanie nieznanych niewiadomych); źródła brak.
- WAY-142: *Based on* `TODO`; the left-out milestones, estimates and interview moved to *Rejected*. EN: The step takes the breaking of a project into tasks before any task is planned from a roadmap of vertical slices and leaves out its milestones, estimates and interview. PL: Krok bierze z planu drogowego pionowych plasterków podział projektu na zadania przed planowaniem zadań i pomija kamienie milowe, estymaty i wywiad.
- WAY-143: *Based on* `TODO`. EN: The rule takes from vertical slices the cut by what can be checked in the running product and from its enabling work the naming of what it opens the way for. PL: Reguła bierze z pionowych plasterków podział według tego, co da się sprawdzić w działającym produkcie, a z pracy przygotowawczej wskazanie, czemu otwiera drogę.
- WAY-144: *Based on* `TODO`; the left-out field of work that can run alongside stands in *Rejected*. EN: The rule takes from a roadmap its graph of dependencies and leaves out its field of work that can run alongside. PL: Reguła bierze z planu drogowego graf zależności i pomija jego pole pracy równoległej.
- WAY-146: *Based on* `TODO`. EN: The rule takes from a roadmap the review of the plan before handing it on, split between a script and a reader who did not write it. PL: Reguła bierze z planu drogowego przegląd planu przed przekazaniem, podzielony między skrypt i czytelnika, który go nie pisał.
- WAY-147: *Based on* `TODO`. EN: The rule takes from a roadmap the stable name each item carries into later work. PL: Reguła bierze z planu drogowego stałą nazwę, którą każda pozycja niesie do dalszej pracy.
- WAY-164: *Based on* `TODO`. EN: The rule takes from an agent harness's practice the naming of the requirement most likely to be false and the check that would catch it. PL: Reguła bierze z praktyki środowiska agentów nazwanie wymagania najpewniej niespełnionego i sprawdzenia, które by to wykryło.
- Not changed, already by the pattern or missing only the item listed below: WAY-256, WAY-268, WAY-270, WAY-273, WAY-280, WAY-374. WAY-256 and WAY-280 name the practice, what is taken and what is left out (WAY-256 in *Rationale* and *Rejected*, WAY-280 in a binding sentence and *Rejected*); WAY-268, WAY-270, WAY-273 and WAY-374 name the practice and what is taken in *Rationale* (lesson label of a private course) and say nothing of what is left out (list below).

Row F3 (b), relation added — changed
- WAY-167 EN: The general coding file's table takes its shape from Open Mercato's table leading from a task to the guides to read. PL: Tabela ogólnego pliku kodowania bierze kształt z tabeli Open Mercato prowadzącej od zadania do przewodników do przeczytania.
- WAY-199 EN: The status beside each path is taken from Open Mercato's statuses. PL: Status przy każdej ścieżce pochodzi ze statusów Open Mercato.
- WAY-203 EN: A change is blocked only by a check whose every report developers would act on, taken from Google's practice. PL: Zmianę blokuje tylko sprawdzenie, którego każdy raport wywołałby reakcję programistów; to praktyka Google.
- WAY-206 EN: The audit of dependencies checks what the change brings against a base, as Open Mercato's audit does. PL: Audyt zależności sprawdza to, co wnosi zmiana, względem bazy, jak audyt Open Mercato.
- WAY-212 EN: The lead from a task to the files to read through a table in a second step is taken from Open Mercato's table. PL: Prowadzenie od zadania do plików do przeczytania tabelą w drugim kroku pochodzi z tabeli Open Mercato.
- WAY-228 EN: The relations that give a property test its expected value are taken from the practice of property tests. PL: Relacje dające testowi własności oczekiwaną wartość pochodzą z praktyki testów własności.
- WAY-229 EN: A class of model for each step and one retry a class higher are taken from Open Mercato's skills; their default tier for typical implementation is left out (now in *Rejected*). PL: Klasa modelu dla każdego kroku i jedna ponowna próba klasę wyżej pochodzą z umiejętności Open Mercato; ich domyślny poziom dla typowej implementacji jest pominięty (teraz w *Rejected*).
- WAY-233 EN: The list of weakenings of a test is taken from Open Mercato's review checklist. PL: Lista osłabień testu pochodzi z listy kontrolnej przeglądu Open Mercato.
- WAY-236 EN: The order "a deterministic check first, a judge only where none exists" is taken from Anthropic's recommendation. PL: Kolejność „najpierw sprawdzenie deterministyczne, sędzia tylko tam, gdzie go nie ma” pochodzi z zalecenia Anthropic.
- WAY-237 EN: The section of what is deliberately not tested is taken from the 10xDevs course; the course's plan of tests is left out (now in *Rejected*). PL: Sekcja tego, czego celowo się nie testuje, pochodzi z kursu 10xDevs; plan testów kursu jest pominięty (teraz w *Rejected*).

Row F3 (c), relation removed, source stays in *Based on* — changed (only the `Relations` line)
- WAY-128, WAY-129, WAY-130, WAY-131, WAY-132, WAY-133: *Relations* now `none`. WAY-137: `narrows WAY-123`. WAY-139: `derives from WAY-267 · derives from WAY-270 · derives from WAY-165`. WAY-140: `derives from WAY-107 · derives from WAY-227`. WAY-173: `derives from WAY-168`. Their meaning is unchanged. EN: the entry no longer claims to adopt a practice from outside. PL: wpis nie twierdzi już, że przejmuje praktykę z zewnątrz.

Row F3 (d), unchanged by the orchestrator's answer 2: WAY-204 and WAY-258 (no relation to WAY-100, no edit); WAY-167 got the relation (b).

### For the human (the request puts them forward)

1. WAY-173 and WAY-140 lose `derives from WAY-100` by the task's rule (answer 3 of *Questions to settle*), as the orchestrator's answer 3 says. Note against the rule: the *Rationale* of WAY-173 says that the-way's template "bind[s] what the-way offers, and the product takes it as a practice from outside is taken (WAY-100)"; that is WAY-100 applied to the-way's own template, and 46 entries (per the planner) stand on WAY-173. I followed the task and did not decide for the human.
2. `Based on` reads `TODO — <what is missing>` in seven entries because the entry names the practice and no source: WAY-138, WAY-142, WAY-143, WAY-144, WAY-146, WAY-147, WAY-164 (the form of the field allows it; the main branch may hold it, and the request puts it before the human).
3. Entries whose *Rejected* I left as the entry has it, because the entry says nothing of what the practice leaves out (the orchestrator's answer 1); per entry, the missing item:
   - WAY-138: what the devil's advocate, the pre-mortem and the search for unknown unknowns leave out (the entry also never says what each consists of).
   - WAY-143: what the rule leaves out of the practice of vertical slices and of its enabling work.
   - WAY-146: what the rule leaves out of the review of a roadmap.
   - WAY-147: what the rule leaves out of the roadmap's stable names.
   - WAY-164: what the rule leaves out of the harness's practice.
   - WAY-268: what the rule leaves out of lesson m2l4 (the entry says "one thing" is taken).
   - WAY-270: what the step leaves out of lesson m3l5 (the entry names the two questions taken).
   - WAY-273: what the rule leaves out of lesson m3l5 (the entry says "this one rule").
   - WAY-374: what the decision leaves out of lesson m2l2 (the entry says what it adds, its bounds, not what it leaves out).
   - WAY-167, WAY-206, WAY-212: what is left out of Open Mercato's table / audit.
   - WAY-199: what is left out of Open Mercato's statuses (the entry has three statuses where its quoted source has two, and does not say why).
   - WAY-228: what is left out of property-based testing.
   - WAY-233: what is left out of Open Mercato's review checklist.
   - WAY-236: what is left out of Anthropic's recommendation.
   - WAY-203 partly: *Rejected* holds the 10-percent allowance and the correctness-only rule as ways not taken, but the entry does not mark which are the source's; left so.
4. Sources I could not tell as openable or not (the entry does not say): the lesson "Towards Autonomous Product Development" (WAY-121); the lessons m2l4, m3l5, m2l2 of the 10xDevs course (WAY-268, WAY-270, WAY-273, WAY-280, WAY-374); the course on steering models through context (WAY-256); the 10xDevs course (WAY-237). I wrote no claim that any of them cannot be opened. They stay described in *Rationale* with *Based on* `none` or the facts the entry already had. The source of WAY-29's new sentence (a card of the human's private analysis) is not named in the entry; WAY-29 is not an entry of list (a) to (d) and I wrote no description of what was seen there.

### Choices (way rejected, cost if wrong)

- WAY-100 *Verification* gets a violating example beside the complying one (the task asks a complying one): a pair is the form of the field. Rejected: the complying example alone. Cost if wrong: one extra line.
- WAY-100 *Rationale* and *Rejected* get one sentence each, from the task's answer 2 (the way not chosen, its cost). Rejected: leaving them as they were (the entry would not say why the paragraph exists). Cost if wrong: the sentences are the writer's wording of the task's own reasons.
- WAY-29: the third binding sentence is added to the first paragraph (three sentences, the limit); no *Rejected* item added, because the only way I could name is one I would derive (WAY-134). *Rationale* has one writer's sentence. Cost if wrong: the human may want the status quo in *Rejected*.
- F3 (a): where the entry already named what is taken, I changed nothing but moving "leaves out" to *Rejected*. Rejected: a uniform "takes ... and leaves out" sentence in every entry (it would restate binding sentences and invent). Cost if wrong: some entries read differently from others.
- F3 (b): each entry gets one sentence of the form "the decision takes ... from ... (WAY-100)" in *Rationale* from the words the entry already had; the relation is added. Rejected: naming the practice in a binding sentence (a binding sentence would change the meaning).
- F3: relation lines of (c) with no other relation read `none`. WAY-128 reads `none`, so WAY-256 `derives from WAY-128` stays valid.
- Where the plan contradicts the entry: none found. The plan's note on WAY-229 as (b) holds (the entry's *Based on* is Open Mercato's skills; its measurement is the product's own, which I left untouched).

### Questions

None blocking. Recommended for the request: the human to supply the sources of the seven `TODO` entries and the missing "leaves out" items listed above.

### Reaches beyond the handoff

- `elements/decisions/skill/read.md` and `decide_entry.md` (named by `SKILL.md` as steps 1 and 2) read whole.
- `elements/decisions/template.md` whole and `elements/common/rules.md` whole (named by the handoff).
- `planner-survey-adoptions.json` rows for the 36 entries of F3 (hypotheses, checked against the entries).
- `git grep` of the words "roadmap", "vertical slice", "devil's advocate", "harness" in the foundation and the Markdown files, for any source of those practices: none found.

### Unread material

- `plan.md` lines 262 to 561 (the slices 12 to 23 and the coverage table): not read; not needed for rows F1 to F3 (read lines 1 to 261 and 562 to 589).
- `task.md` lines 200 to 379 (the tables B to F of the assessment) and from line 495 (the note before refinement): not read; read 1 to 199 and 380 to 494.
- `reports/planner-survey-withdrawals.json`, `planner-refs-by-number.txt`, `planner-refs-ranges.txt`: not read in this turn (turn 2 and 3 material).
- `elements/common/foundation_check.py`: not read; only run.
- `elements/decisions/skill/projected.md`: not read (projected mode).
- WAY-90: read to the middle of *Rejected*; WAY-19 and WAY-293: read to the middle of *Rationale*. WAY-02, WAY-07, WAY-14, WAY-25, WAY-27, WAY-29, WAY-36, WAY-100, WAY-114 read whole; WAY-293 first two paragraphs and *Verification* whole.
- The withdrawals of the first round in the history of `foundations/decisions.md` (`git log -S"Withdrawn"`): not read; I read `git show f0b2130 --stat` and the current list of withdrawn identifiers of the log for the form.
- The 34 entries of F3: each read whole (WAY-121, 138, 142, 143, 144, 146, 147, 164, 256, 268, 270, 273, 280, 374, 167, 199, 203, 206, 212, 228, 229, 233, 236, 237, 128, 129, 130, 131, 132, 133, 137, 139, 140, 173); WAY-204 and WAY-258 not read (not edited; judged by the survey and the orchestrator's answer 2).

### Searches not found or unclear

- A source for the roadmap, the vertical slices, the three tests of WAY-138 and the agent harness of WAY-164: not found anywhere in the foundation or the Markdown files.
- Whether the sources named above (lessons of the courses) can be opened by a reader: unclear in every entry.
- `elements/decisions` holds no test, so the check named by the handoff exits 1; the template and skill of the element are covered by the tests of `elements/common`.

### Working copies

None made. Scripts of mine stand in `.runs\foundation\` (`entry.py` prints an entry of the log; `f3b.py` the relations and rationale edits; `survey_f3.txt`, `a1.txt` to `c2.txt`, `diff_all.txt` copies of entries and the diff for reading). I keep them for turns 2 and 3 and remove them in the last turn.

## Turn 2 — rows F4 and F5

**Status:** done with concerns (six entries of the plan's F4 held back, a choice of mine; the foundation check exits 1 as expected).

**Commit:** `e643371` on `task/decision-log-second-round` (one file, `foundations/decisions.md`: 291 insertions, 4279 deletions). Nothing pushed.

### Checks (command and exit code)

| Command | Exit | What it printed / showed |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 1 | first lines: `foundations/invariants.md:92: `WAY-323` is withdrawn; name its successor`, `foundations/invariants.md:162: `WAY-41` ...`, `foundations/invariants.md:213: `WAY-108` ...`; last line `617 errors`. All 617 errors are of that one kind (a reference to a withdrawn number). No other kind: no entry stands both as entry and on the list, no number twice, no successor the log does not hold. |
| `python -B gate/run_tests.py elements/common` | 1 | 201 tests, 200 pass, 1 fails: `test_foundation_check.FoundationCheckTest.test_the_way_foundation_passes` (`AssertionError: 1 != 0`), because it runs the foundation check on this repository. Nothing else fails. |

I ran no other check; none can exit 0 until turn 3 and the slices.

Counts of the 617 lines by file (the lines are the references the later work removes or repoints): foundations/decisions.md 102 (in 48 live entries; all 47 entries of the plan's F6 and WAY-93, which is new to that list because I held it back, below); foundations/glossary.md 1; foundations/invariants.md 5; foundations/part_map.md 1 (these three are F8); and 104 files outside `foundations/`, every one of them a file of a slice of the plan: agent-instructions/README.md 3; elements/common/projected_mode.md 1; elements/common/rules.md 16; elements/common/skill/SKILL.md 1; elements/common/skill/build_table.md 1; elements/common/way_of_working.md 4; elements/decisions/skill/SKILL.md 1; elements/decisions/template.md 1; elements/environment-facts/skill/SKILL.md 1; elements/environment-facts/skill/read.md 1; elements/environment-facts/template.md 28; elements/glossary/skill/SKILL.md 1; elements/glossary/template.md 5; elements/invariants/skill/SKILL.md 1; elements/invariants/template.md 14; elements/part-map/skill/SKILL.md 1; elements/part-map/template.md 16; foundation-review/SKILL.md 13; foundation-review/proposals.md 2; foundation-review/remarks.md 2; foundation-review/weak_points.md 2; foundation-review/with_the_human.md 3; installation/README.md 1; instruction-files/SKILL.md 1; instruction-files/judging.md 2; process-audit/SKILL.md 11; process-audit/audit_count.py 47; process-audit/problem_register.md 6; process-audit/test_audit_count.py 8; product-guidelines/audit_end.md 8; product-guidelines/coding/SKILL.md 5; product-guidelines/coding/hand_back.md 2; product-guidelines/coding/kinds.md 5; product-guidelines/coding/new_tools.md 2; product-guidelines/coding/recognize.md 5; product-guidelines/coding/research.md 1; product-guidelines/coding/settle.md 17; product-guidelines/coding/starting_set.md 4; product-guidelines/coding/task_document.md 3; product-guidelines/coding/template.md 40; product-guidelines/coding/trial_run.md 1; product-guidelines/reading.md 6; product-guidelines/styleguide/SKILL.md 1; product-guidelines/styleguide/audit.md 2; product-guidelines/styleguide/new_tools.md 2; product-guidelines/styleguide/recognize.md 3; product-guidelines/styleguide/research.md 1; product-guidelines/styleguide/settle.md 7; product-guidelines/styleguide/starting_rules.md 4; product-guidelines/styleguide/task_document.md 2; product-guidelines/styleguide/template.md 38; product-guidelines/template.md 13; product-guidelines/testing/SKILL.md 2; product-guidelines/testing/audit.md 4; product-guidelines/testing/new_tools.md 2; product-guidelines/testing/recognize.md 3; product-guidelines/testing/research.md 1; product-guidelines/testing/settle.md 1; product-guidelines/testing/starting_set.md 2; product-guidelines/testing/task_document.md 1; product-guidelines/testing/template.md 10; project-level/definition_template.md 17; project-level/lead/skill/SKILL.md 2; project-level/lead/skill/route_changes.md 1; project-level/plan/skill/SKILL.md 2; project-level/plan/skill/critique_plan.md 1; project-level/plan/skill/delegated_mode.md 1; project-level/plan/skill/existing_plan.md 1; project-level/plan/skill/guideline_tasks.md 1; project-level/plan/skill/hand_over.md 1; project-level/plan/skill/read.md 2; project-level/plan/skill/reading_definition_and_plan.md 1; project-level/plan/template.md 1; project-level/skill/SKILL.md 3; project-level/skill/delegated_mode.md 1; project-level/skill/first_write.md 1; project-level/skill/read_foundation.md 1; project-level/skill/rounds.md 1; project-level/task/skill/draft.md 2; project-level/task/skill/final_review.md 1; project-level/task/skill/find_settlements.md 1; project-level/task/skill/guideline_findings.md 1; project-level/task/skill/read_sources.md 1; project-level/task/template.md 3; project-level/task_line.md 1; project-level/technology/failure_notice.md 1; project-level/technology/list.md 1; project-level/technology/reserved_choices.md 2; project-level/technology/running_product.md 1; project-level/technology/start.md 2; task-cycle/change/SKILL.md 1; task-cycle/change/ui_check.md 3; task-cycle/change_file_sizes.py 1; task-cycle/gate_times.py 1; task-cycle/record_template.md 3; task-cycle/request_check.py 1; task-cycle/review/SKILL.md 5; task-cycle/review/whole_change.md 1; task-cycle/skill/SKILL.md 15; task-cycle/skill/blocked_finding.md 1; task-cycle/skill/correction.md 6; task-cycle/skill/request_template.md 21; task-cycle/test_gate_times.py 1; task-cycle/tracked_private_paths_check.py 1.

A script compared those 104 files with the *Change* lines of the plan's slices: each is in a slice; nine files of slices have no line (reason sentences or held entries only): elements/common/skill/read.md, gate/run_tests.py, installation/install.py, project-level/skill/idea.md, task-cycle/cycle_measures.py, task-cycle/cycle_stages.py, task-cycle/plan/SKILL.md, task-cycle/skill/spec_review.md, task-cycle/spec/design.md.

### F4 — what I did

- Read each of the 137 entries of the plan's F4 row whole (seven files of copies under `.runs/foundation/w00.txt` to `w06.txt`, 4255 lines) before withdrawing any.
- Withdrew 131 of them: the entry is removed from the log and its number stands in the list *Withdrawn identifiers*, in order of number, with *Why* of the form `its rule, the answer to "<the entry's question>", stands in `<place>`` and *Successors* `none`. The place is the plan's, per entry (the plan's place for WAY-338 is `task-cycle/cycle_stages.py`, WAY-112 `project-level/skill/idea.md`, WAY-331 `foundations/part_map.md`, WAY-115 `elements/common/skill/build_table.md`; the table's others are not used).
- The log holds 197 entries (334 less 137: 131 plus the six of F5).

### Entries I held back from F4 (they stay in the log; the orchestrator decides)

The criterion: the entry's `Relations` line `narrows` a decision that stays in the log, so the entry is the one record of the precedence that WAY-25 asks for in the prevailing decision; a skill or a template cannot hold it (the plan held WAY-294 and WAY-295 on the same ground). Each of the six is in group A of the human's table.

1. WAY-93 (`narrows WAY-02`): the glossary entry is headed by its term and not by an identifier; its place is `elements/glossary/template.md`.
2. WAY-94 (`narrows WAY-02 · derives from WAY-04`): a glossary entry holds the definition and *Not*, with no fingerprint at a use; its place is `elements/glossary/template.md`.
3. WAY-97 (`narrows WAY-02`): a sentence relies on a term by its word, and the author of a changed definition searches for the word; its place is `elements/glossary/template.md`.
4. WAY-297 (`narrows WAY-161`): the grade of a finding about a missing glossary entry or qualifier; its place is `task-cycle/review/SKILL.md`.
5. WAY-363 (`narrows WAY-161`): the grade of a finding about the structure of code; its place is `task-cycle/review/SKILL.md`.
6. WAY-364 (`narrows WAY-161`): the grade of a finding that an entry departs from the form of its template; its place is `task-cycle/review/SKILL.md`.

Consequences for the plan: the numbers of these six stay valid, so a reference to them in a file is no error (the check reports none); the slices that name them (slice 5 for WAY-93, WAY-94 and WAY-97; the slice of `task-cycle/review/SKILL.md` for WAY-297, WAY-363 and WAY-364) need not remove those numbers or add a sentence of reason for them. WAY-93 cites withdrawn WAY-64 in its *Rationale* and WAY-93's text must be repointed in turn 3 (it is the one entry with errors that the plan's F6 list lacks; I add it to F6 then). Cost if my choice is wrong: six entries stay in the log for a later round; cost of the other way: the precedence over WAY-02 and WAY-161 would be recorded nowhere. If the human prefers them withdrawn, the same script withdraws them.

The four entries the plan already keeps out (WAY-263, WAY-287, WAY-294, WAY-295) stay; I changed nothing in them.

Withdrawn although the entry has a measurement or a long *Rejected* (judged as the table of the human says, the place able to carry a sentence of the reason; the review of the whole change reads each added sentence): WAY-80, WAY-86, WAY-299, WAY-345, WAY-353, WAY-362, WAY-366, WAY-371. I found no entry among the 131 whose binding sentence a place cannot state; I list these only because the cost of their reason is higher than the others.

### F5 — what I did

Each of the five entries below took the binding sentences of its group-D entry as a second (or third) paragraph, the pair of examples of the entry as a further `complies`/`violates` block in its *Verification*, its *Rationale* and *Rejected* added to the target's, its *Scope* and *Based on* joined; the group-D number stands in the list with the target as successor.

- WAY-292 into WAY-288: paragraph on the block holding `none` where the task document is English; *Relations* of WAY-288 now `derives from WAY-286 · narrows WAY-114` (WAY-292's `narrows WAY-114` kept; its `narrows WAY-288` is the merge itself; its `narrows WAY-290` is dropped because WAY-290 left the log in F4).
- WAY-317 into WAY-316: paragraph on a product with no place for screenshots; *Relations* gain `derives from WAY-287` (from WAY-317; its `derives from WAY-316` is the merge, its `derives from WAY-219` was already there); the text still says `WAY-219` where the entry said it: turn 3 repoints it (F6 lists WAY-316).
- WAY-323 into WAY-309: paragraph on what the script takes for an absolute path and for a note link (the words "of WAY-309" read "the script"); the rationale and rejected ways of WAY-323 added; WAY-323's `narrows WAY-309` is the merge.
- WAY-347 into WAY-339: paragraph that the measures of context and cache use are counted by a script and into a file of their own; WAY-347's `derives from WAY-339` is the merge. WAY-339 still cites `WAY-347` and `WAY-349`; turn 3 repoints them (F6 lists WAY-339).
- WAY-369 into WAY-368: paragraph that the agent types start with the instruction files; *Based on* gains `claude-code-subagent-instruction-files`; WAY-369's `derives from WAY-368` is the merge.
- WAY-358 into WAY-357 — exactly what I did: WAY-357 is withdrawn by F4, so there is no entry to take a paragraph. I removed the entry WAY-358 and put its number on the list with *Why* "its rule, what causes the line of a correction gives, is a part of the question that WAY-357 answered, and both stand in `task-cycle/record_template.md`" and *Successors* `WAY-357` (a withdrawn number). Why it holds: (1) the list's form lets a successor be "a decision or a withdrawn number of the log", and the foundation check accepts it (no error of that kind); (2) the rule stands in the place named: `task-cycle/record_template.md` lines 214 to 225 already carry the pairs `<source> · <kind>`, the three sources, the test of `defect` / `not-required` / `none` (I checked by `grep`; line 225 cites `(WAY-358)` and `(WAY-357)` at line 215, which slice 21 repoints), and `task-cycle/skill/correction.md:62` repeats the kinds. What is lost: the *Rejected* of WAY-358 (the five judged causes, with the measurement of 20 corrections examined, 15 of them `raised-by-cycle`) does not stand in the template; the table of the human put WAY-358 in group D and WAY-357 in group A, and the plan chose this; I did not decide for the human, and name the loss for the review of the whole change to read against slice 21.

### Choices (way rejected, cost if wrong)

- The held six (above). Rejected: withdraw all 137 as the plan says. Cost if wrong: six entries stay.
- *Why* from the question of the entry in one generated form, and not hand-written per entry. Rejected: a hand-written clause for each of 131 entries (it would say what the question already says). Cost if wrong: a reader finds the question where a phrase would be shorter.
- Group-D text moved whole (paragraph, examples, rationale, rejected), with the self-references of the group-D entry removed or changed to its target. Rejected: a one-sentence summary of each group-D entry (it would lose rejected ways, which WAY-293 says the entry must keep). Cost if wrong: the target entries are longer (WAY-309 by about 40 lines).
- No reference inside a live entry was edited in this turn (F6 is turn 3), except the text of the merged paragraphs, which I copied as it stood.

### Reaches beyond the handoff

- `task-cycle/record_template.md` (grep and lines 205 to 230) and `task-cycle/skill/correction.md` (grep): to decide whether the rule of WAY-358 stands in its place.
- `git grep`/`grep` of `not-required` in the tracked Markdown and Python files, for the same.

### Unread material

- Everything the handoff names was read: the 137 entries of F4 and the six entries of F5 with their five targets (WAY-288, 316, 309, 339, 368), each whole. Not read in this turn: `plan.md` lines 262 to 561 (slices), `task.md` lines 200 to 379, `reports/planner-survey-withdrawals.json` (the survey of the withdrawals; the entries themselves were read in its place), `planner-refs-by-number.txt`, `planner-refs-ranges.txt`.
- The entries WAY-255, 161, 02, 340 and the others that the withdrawn entries cite were not read (cited, not changed).

### Searches not found or unclear

- Whether the plan's F6 list should name WAY-93: found by the check (one reference to a withdrawn number in WAY-93); the plan's list lacks it.
- Whether the human's table meant WAY-93, 94, 97, 297, 363, 364 withdrawn with their `narrows` lost: unclear; the table's reason column says only "stands in the skill or template".
- Whether `task-cycle/record_template.md` states the *Rejected* of WAY-358: it does not.

### Working copies

None beyond the scripts and copies in `.runs\foundation\` (`entry.py`, `f4.py`, `f5.py`, the entry copies `w00.txt` to `w06.txt`, `d1.txt`, `d2.txt`, `after.txt`, the check output `check_t2.txt` and the counts `check_t2_counts.txt`). Kept for turn 3; removed at its end.

## Turn 3 — rows F6, F7, F8 (and WAY-93)

**Status:** done with concerns (one listing of the foundation check stands in `foundations/invariants.md`, see Checks; nothing blocked).

**Commits** on `task/decision-log-second-round`, each of one or more files under `foundations/` only, pushed nowhere:
- `ece1f71` — F6: every reference in a live decision to a withdrawn number (`foundations/decisions.md`).
- `208f63c` — F7: WAY-09 and WAY-312 (`foundations/decisions.md`).
- `5c10ee4` — F8: four invariants, WAY-02's *Verification*, the part map, the glossary (`foundations/invariants.md`, `foundations/decisions.md`, `foundations/part_map.md`, `foundations/glossary.md`).

### Checks (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 1 | `508 errors`, every one of the kind "`WAY-n` is withdrawn; name its successor", all in 104 files outside `foundations/` (the same 104 files and the same counts per file as after turn 2, so no file outside `foundations/` was touched; the counts by file are in `reports/foundation-work/foundation_check_counts_after_turn3.txt`, the whole output in `foundation_check_after_turn3.txt`). **No error is reported for any file under `foundations/`.** One more line is printed under `foundations/`, which is a listing and no error (see below). |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK. |
| `python -B gate/run_tests.py elements/invariants` | 1 | `no test found in elements/invariants`: the directory holds no test (the tests that cite the invariants stand in other directories). |
| `python -B gate/run_tests.py elements/decisions` | 1 | `no test found in elements/decisions`: no test. |
| `python -B gate/run_tests.py elements/common` | 1 | 201 tests, 200 pass; the one failure is `test_the_way_foundation_passes`, which runs the foundation check on this repository and fails on the 508 errors outside `foundations/`. |

Proof that no error is in `foundations/`: the script that tallied the output by file found `foundations/invariants.md` as the only `foundations/` file with a line, and that line is of the other kind (below); the 508 errors equal the sum of the 104 files outside it, and that sum is the one after turn 2.

The one line under `foundations/`: `foundations/invariants.md:86: listed: `tracked-file-private-paths` reads `test` and its sentence is changed by this change, while no file citing it changed (task-cycle/test_tracked_files_private_paths.py): name it in the request, saying what the sentence now says`. It is the listing of WAY-03 ("The listing stops no change"), caused by the necessary change of that invariant's sentence (it named the withdrawn WAY-323). It does not count among the errors and is not mine to clear: the only file that cites the invariant and could change is `task-cycle/test_tracked_files_private_paths.py`, which no row of mine may change. For the request: the sentence now reads "...as WAY-309 names them" (it named WAY-309 and WAY-323 before; the rules for a path and a note link are the same, WAY-323 being now a paragraph of WAY-309), and the test that checks it was left as it was. If the orchestrator wants the listing gone, a slice must change a file that cites the invariant (for example a comment in `task-cycle/test_tracked_files_private_paths.py`); I did not.

### F6 — what I did

I took the 102 lines of the check in `foundations/decisions.md` (48 live entries: the 47 of the plan's F6 and WAY-93), read each line with the lines around it, and wrote each change by a script (`reports/foundation-work/f6.py`, `f6b.py`).
- A `derives from` or `narrows` to a withdrawn number is removed (no live entry holds the thing; the thing stands in a template, skill or script, or in a paragraph of a live entry). Where nothing remains the line reads `none`: WAY-44, WAY-48, WAY-276, WAY-350. WAY-216 keeps `narrows WAY-251` alone; WAY-288 `narrows WAY-114` alone; WAY-316 `derives from WAY-308 · derives from WAY-287`.
- A bracket that only cites a withdrawn number is removed (the sentence keeps its full stop): WAY-09 (WAY-331), WAY-71, WAY-84 (two), WAY-90, WAY-93, WAY-125, WAY-142, WAY-168, WAY-203, WAY-204 (three), WAY-212 (WAY-170), WAY-228, WAY-244, WAY-268 (WAY-219 and the list of six), WAY-280, WAY-284 (two), WAY-287 (WAY-291, WAY-358), WAY-300, WAY-315 (WAY-115), WAY-360 (WAY-202 twice, WAY-278 once), WAY-216 (WAY-211, WAY-202).
- Where the sentence leans on the number for its meaning I wrote the thing in words (the wording is mine; each is below):
  - WAY-90: "a new form of source beside those of WAY-80" → "beside those an environment fact takes".
  - WAY-121 and, by the group D successor, WAY-317 → WAY-316.
  - WAY-128 (binding): "answer to WAY-35, WAY-127, WAY-256 and WAY-259" → "answer to WAY-35, WAY-127 and WAY-256, and to the text the installer writes in an entry point".
  - WAY-134 (binding): "in the form WAY-115 gives" → "in the form of the candidate table of the skills of the elements (`elements/common/skill/build_table.md`)".
  - WAY-206: "answered as WAY-68 gives it" → "answered as any check that gives different verdicts on one commit is, by a fix of the test with no quarantine recorded"; its *Rejected* item likewise "the rule on a check that gives different verdicts on one commit".
  - WAY-212 *Rejected*: "as WAY-192 has for each styleguide" → "as it has for each styleguide".
  - WAY-215 (binding): "a departure under WAY-217" → "an approved departure under the shared reading of product guidelines".
  - WAY-216 (binding): "under WAY-200" → "as the skill `maintain-coding-guidelines` gives it" and "the comparison that skill gives"; "no audit under WAY-201" → "no audit of a product with code"; *Rejected* "against WAY-211" → "against the rule that an extension researches".
  - WAY-243: "WAY-68 gives the test of an invariant the same answer" → "The rule on a check that gives different verdicts on one commit gives..."; "as WAY-68 refuses it" → "as that rule refuses it".
  - WAY-267: "(WAY-118, WAY-156)" → "(WAY-118)". WAY-247: "(WAY-209, WAY-244)" → "(WAY-244)".
  - WAY-276 (binding): "prevails over WAY-272" → "prevails over the rule that a failure is written with its original error"; "prevailing over WAY-275" → "over the rule that a line of a case flow carries the identifiers the logging scope lists"; its `narrows` lines go with the numbers.
  - WAY-287: "the skeleton of WAY-286" → "the skeleton of the request's description".
  - WAY-316 (the text F5 merged; binding, *Verification*, *Rationale*, *Rejected*): "WAY-219 gives" → "the author's check of a user-interface change gives" (and "that check gives").
  - WAY-328 (binding): "under WAY-217" → "under the shared reading of product guidelines".
  - WAY-339: "(WAY-347)" and "(WAY-349)" removed from the first paragraph; "the tables of WAY-349 and WAY-350" → "the tables of the gate times and of WAY-350".
  - WAY-360 (binding): "as WAY-278 gives it" → "as the skill `maintain-coding-guidelines` gives it".
- Every binding sentence reworded keeps its meaning: each number stood for a rule that now stands, with the same words, in the place its *Why* names. Where I was not sure the number can be turned into words without a change, I would have left it and asked; none is left.
- No sentence a test holds by a line `decision:` was touched; the foundation check, which compares them, reports none.

### F7 — what I did

- WAY-09: the binding sentence that listed the directories of the repository and the contents of each directory is shortened. It now says "a directory for each part of the process other than `repository`, which the part map of the-way names with its files", and the rule that a directory reaches the main branch only when complete reads: an element its template and rules, examples or a pointer, and a skill that writes its entries; "any other directory what the sentence of its part in the part map names". The part map already holds each part's directory and contents (checked: `foundations/part_map.md` lines 7 to 190). The ban on a `tools/` directory and the other *Verification* examples stay. The *Rationale* lost its bracket `(WAY-331)`.
- WAY-312: the first binding sentence ("The shared template of a product's guidelines holds that a rule lists no state of the product's code ...") is taken out of the first paragraph; the paragraph now begins with the ban on rewriting known practices, and the sentence about the cleaning refers to "the sentences that the shared template of a product's guidelines rules out — a rule lists no state of the product's code or of the product and repeats neither a decision of the product's log nor a value taken from a configuration file". The *Rationale* lost `WAY-171`.
- **What slice 13 must add to `product-guidelines/template.md`**, quoting the sentence (taken from WAY-312 at the base `ec7929d`, `foundations/decisions.md` line 7603): "A rule lists no state of the product's code or of the product and repeats neither a decision of the product's log nor a value taken from a configuration file, so that what remains is what the author of the code is to do." With it the one sentence of its reason, from the *Rationale* of WAY-312: a sentence that lists what the code or the product is today goes stale when the code changes, and a sentence that repeats a decision or a value of a configuration file is a second copy that drifts from the first. The template must hold the sentence, because WAY-312 now says only what the template rules out by reference to it.
  - WAY-312's *Origin*, *Based on* (`shorter-guidelines-trial`) and the ban on rewriting known practices stay in the log.

### F8 — what I did

- `project-definition-form`: *Derives from* `none` (the orchestrator's answer 5; the rule stands in `project-level/definition_template.md` as a rule with no choice behind it, WAY-22).
- `map-reference-target`: *Derives from* `WAY-02` (the nearest staying decision: a reference names an entry the foundation holds); WAY-02's *Verification* now reads "invariants: fingerprint-definition · map-reference-target." (its binding sentences and examples unchanged).
- `cross-part-imports`: *Derives from* `WAY-44` alone (WAY-299 is withdrawn; its rule stands in `elements/part-map/template.md` as a duty with its reason).
- `tracked-file-private-paths`: the sentence names WAY-309 alone ("as WAY-309 names them"); *Derives from* `WAY-320 · WAY-309 · WAY-324` (WAY-323 is a paragraph of WAY-309). The sentence changes, so the listing above.
- `foundations/part_map.md`: the withdrawn row `guidelines-form-check-command` lost its bracket (WAY-170); the part `process-audit` holds one added sentence of why it is a part of its own: "It is a part of its own because it answers how the whole process fares over many cycles, which is not how one task is carried out, so what only work on the audit needs stays out of what every agent of the cycle reads."
- `foundations/glossary.md`: "A product takes these words from the-way at the commit it pins." (the bracket `(WAY-226)` removed).
- The tests that cite an invariant by identifier are not changed.

### Entries written (rows F6 to F8: meaning in English and in Polish)

- Row F6 (48 entries, WAY-09 · 44 · 48 · 52 · 60 · 71 · 84 · 90 · 93 · 104 · 121 · 125 · 128 · 134 · 142 · 168 · 203 · 204 · 206 · 212 · 213 · 215 · 216 · 228 · 240 · 242 · 243 · 244 · 247 · 267 · 268 · 273 · 274 · 276 · 280 · 284 · 287 · 288 · 300 · 312 · 315 · 316 · 319 · 328 · 339 · 350 · 360 · 375): EN: the entry names no withdrawn decision; its meaning is as before. PL: wpis nie wskazuje wycofanej decyzji; jego znaczenie jest takie jak przedtem.
- Row F7, WAY-09: EN: the repository holds a directory for each part the part map names, and a directory reaches the main branch only when complete. PL: repozytorium ma katalog dla każdej części z mapy części, a katalog trafia do głównej gałęzi dopiero, gdy jest kompletny.
- Row F7, WAY-312: EN: nothing that edits guidelines replaces a sentence naming a known practice with its name or removes a case that follows from a rule's purpose; a product's task cleans existing guidelines of what the template rules out. PL: nic, co zmienia wytyczne, nie zastępuje zdania o znanej praktyce jej nazwą ani nie usuwa przypadku wynikającego z celu reguły; zadanie produktu czyści wytyczne z tego, co wyklucza szablon.
- Row F8, `project-definition-form`, `map-reference-target`, `cross-part-imports`, `tracked-file-private-paths`: EN: each names, in *Derives from*, a decision that still holds or `none`. PL: każda wskazuje w *Derives from* decyzję, która nadal obowiązuje, albo `none`. Part map, `process-audit`: EN: the audit is a part of its own because it answers how the whole process fares over many cycles. PL: audyt jest osobną częścią, bo odpowiada na pytanie, jak cały proces sprawdza się w wielu cyklach. Glossary: EN: the line names no withdrawn decision. PL: wiersz nie wskazuje wycofanej decyzji.

### Choices (way rejected, cost if wrong)

- A relation to a withdrawn number is removed, not moved to the successor or to the withdrawn entry's own parent. Rejected: `derives from WAY-04` for entries that derived from WAY-40 (nothing follows along a chain, WAY-25). Cost if wrong: an entry misses a relation a reviewer would have wanted.
- WAY-276's `narrows WAY-272 · narrows WAY-275` go (those entries are gone) and the precedence stays in its binding sentences, in words. Rejected: leaving the numbers (the check reports them). Cost if wrong: a reader of the template sees no entry for the precedence.
- WAY-09's lists of directory contents are removed from the binding sentence, not moved. Rejected: moving them into the part map (it already holds each part's sentence, lines 7 to 190). Cost if wrong: a detail such as "with its tests" for some directories stands only in the *Verification* examples.
- WAY-312: the sentence that went to the template is quoted inside the first binding paragraph by reference. Rejected: dropping it with no pointer (the paragraph would say "the sentences the template rules out" and name none).

### Questions

1. The listing for `tracked-file-private-paths` (above): the request must name it in plain words; does the orchestrator want a slice to change a citing test to clear it? Recommended: name it in the request, as WAY-03 asks; do not change a test only to clear a listing.
2. None other.

### Unread material

- `plan.md` lines 262 to 561 (slices) not read; the slices are not my work. The *Verification* parts of the 48 live entries were read only where a flagged line lay near them. The survey JSONs not read in this turn.
- `elements/invariants/skill/SKILL.md` and the template of invariants: read by grep (the lines on *Derives from*), not whole; the four invariants were read whole in the file.

### Searches not found or unclear

- A test that holds a sentence of the entries I changed by a line `decision:` in any of the 48 entries: none found (the check reports none; `git grep "decision: WAY-"` in turn 1 found WAY-03, 12, 375, 376).
- Whether a staying entry, other than WAY-93, held a reference to a withdrawn number that the plan's F6 list missed: none; the check's lines for `foundations/decisions.md` after the commit are none.
- `elements/invariants` and `elements/decisions` hold no test.

### Working copies

Kept in `reports/foundation-work/` beside this report: the scripts that made the edits (`entry.py`, `f4.py`, `f5.py`, `f6.py`, `f6b.py`), the places of the withdrawals (`f4_places.json`), and the output and counts of the check after this turn. The directory `.runs\foundation\` (copies of the entries, the intermediate outputs of the check, the scripts) is removed at the end of this turn; where the removal failed it is named in the line below.

Removal result: `.runs/foundation/` removed whole; no remainder. (The scripts kept in `reports/foundation-work/` read `.runs/foundation/...` paths and are for reading, not for running again.)
