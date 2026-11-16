# Findings of the review of the whole change — for the fix

Reviewer's words, cut from `reports/review-whole-report.md` (head `940893de`, FAIL). Blocking findings first, then the Minor findings within the task (WAY-161), each with the reviewer's mark of contradiction where it gave one. This round has a contradiction with the settlements: yes.

## Blocking findings (Important, within the task)

### I1. The plan's column "By what" lets a case be checked by reading the code

- **Place:** `task-cycle/change/walkthrough.md:47` (the table of section 4).
- **What is wrong:** the column "By what" is defined as "the way of the product that checks it: a
  screen in a browser, a call of an API, a command in a terminal, a reading of the data, a reading of
  the code". A reading of the code is no way to the running product (the glossary entry the change
  itself edits defines that way as the means to check behaviour "in a product while it runs"). The
  task settles the column as filled by the product's way: *To do* 1 ("z kolumną „czym sprawdzam”
  wypełnianą drogą produktu") and the answer under the question on `test-run` ("plan przypadków z
  kolumną „czym” wypełnianą drogą produktu"; the tools of the team are replaced by "droga ustalona
  przez produkt"). The source skill `test-run` has "odczyt kodu · oko" in that column; the change kept
  the first, against the answer.
- **Why it matters:** the walk exists to check what tests do not cover in the running product. With
  this row an author can write a case "by: a reading of the code", give it a verdict, and the case
  does not count as unchecked: the report and kind 4 of the request then show nothing left unchecked,
  and the human believes the behaviour was seen in the running product. It also undoes section 5's
  rule that a case whose way does not work is not called checked, and the rule that without a settled
  way every case is unchecked (a reading of code is always available).
- **Evidence:** the line quoted above; `walkthrough.md:25-27` and `:78-80` (unchecked without a way,
  evidence from the layer checked "instead of calling the case checked").
- **Slice:** none (no plan).

Contradiction: yes — the answer under the question "Co z `test-run` przechodzi do the way…" and row 8
of *Settlements to record*.

### I2. The request template says both that the walk's cases stay in the reports and that *Checks* lists them

- **Place:** `task-cycle/skill/request_template.md:185-187` (top part, "What you will see") against
  `task-cycle/skill/request_template.md:497-498` (lower part, *Checks*). Both sentences are added by
  this change.
- **What is wrong:** the top part now says "Of the artifacts of the check only screenshots reach the
  description: … leave logs and outputs in the reports, the cases and verdicts of the author's walk
  through the running product among them." *Checks* now says the description lists "where an author
  walked through the running product, its cases with the verdict of each (WAY-406)". The two
  instructions to the writer of the description contradict each other. No item of the task asks for
  the cases in the description: *To do* 5 asks only for unchecked cases in item 4 and out-of-scope
  errors in the section for the human's decisions; the task's *Context* records that textual traces
  stay in the reports of the record, and *Out of scope* puts "Gdzie leżą zrzuty ekranu i ślady
  sprawdzenia" outside the task as already settled in the template. WAY-406 and WAY-407, written by
  this change, say the walk stands in "the report the review reads" and that "the human sees in the
  request what was not checked" — not the plan.
- **Why it matters:** the orchestrator writing every request with a walk follows one sentence or the
  other; descriptions then differ from cycle to cycle, and the *Checks* addition moves textual traces
  into the description, which the template had settled against.
- **Evidence:** the two passages quoted; `git diff 9cffc9ba..940893de -- task-cycle/skill/request_template.md`.
- **Slice:** none.

Contradiction: no.

### I3. An error outside the scope that the walk finds can drop out of the request, and WAY-408 adds a kind of item without naming its group

- **Place:** `foundations/decisions.md:6864-6865` (WAY-408, second paragraph) and
  `task-cycle/skill/request_template.md:250-263` (kind 8).
- **What is wrong:** WAY-408, written by this change, binds: "An error outside the task's scope that
  the walk finds the author reports and does not correct, and the description of the request puts it
  before the human as one to make a task of or to let through" — for every such error. The template
  puts these errors into kind 8, whose rule reads each listed thing "and judge … whether the product's
  user or the human working with the process will feel it. Restate each such finding…". An error the
  orchestrator judges not felt is therefore not restated, and unlike a reviewer's finding it has no
  list in the lower part (*Minor findings* and *Findings outside the task's scope* hold reviewers'
  findings only, `request_template.md:526-537`), so it reaches no part of the description. The
  template does what WAY-408 forbids, and WAY-408's own *violates* example names it: "the description
  of the request does not mention such an error". Second, WAY-408 adds a kind of item to the section
  for the human's decisions without naming the group, which WAY-287 requires ("Another decision may
  add a kind of item to one of the three groups, naming the group"), and whose *violates* reads "a
  decision adds a kind of item to the section without naming the group that takes it". Third, WAY-408
  *derives from* WAY-289 while its unconditional sentence collides with WAY-289's judgment of what is
  felt, with no precedence recorded (WAY-25).
- **Why it matters:** *To do* 5 and row 5 send every such error to the human ("trafia do sekcji dla
  decyzji człowieka jako sprawa do rozstrzygnięcia"); an error the walk found and the author was told
  not to correct can disappear between the author's report and the human, which is the loss the task
  closes.
- **Evidence:** the passages quoted; `request_template.md:526-537`; WAY-287 second paragraph and its
  *violates*; WAY-25.
- **Slice:** none.

Contradiction: yes — WAY-408 (written by the change), WAY-287, row 5 of *Settlements to record*.

### I4. The method looks for the product's skill through the decision, while WAY-121 has the skill cite the decision

- **Place:** `task-cycle/change/walkthrough.md:19-21`.
- **What is wrong:** section 1 says: "Read the decisions that settle them, and the skill of the
  product that holds the steps of operation where the decision cites one." The sentence this change
  adds to WAY-121 (and to question 1 of `elements/decisions/template.md:155-159`) gives the link the
  other way: "a skill of the product may hold the steps of operation and cites that decision". The
  decision is not required to cite the skill, and a decision log writes a link at one end only
  (WAY-18). The method thus restates WAY-121 differently (WAY-263).
- **Why it matters:** in a product that follows WAY-121 — a skill such as one that starts the game
  and cites the decision on the way to it — the decision names no skill, so the author reads no skill
  and improvises the steps of operation, the failure WAY-121's rationale names ("improvises its access
  in the middle of the cycle").
- **Evidence:** the two sentences quoted.
- **Slice:** none.

Contradiction: yes — WAY-121 (the sentence the change adds).

### I5. WAY-406 records as left out two course items the human placed outside this task, with no reason

- **Place:** `foundations/decisions.md:6824-6825` (the end of WAY-406's *Rejected*).
- **What is wrong:** *Rejected* ends "Left out of the practices: … and, of the courses, a limit on
  simultaneous instances of agents and a field of how to check in each part of the part map." The
  task's answer under the question on the addendum of 12.11.2026 classes these two as "Poza
  zadaniem" (outside the task), and *Out of scope* lists both as outside this task, not as ways
  weighed and not chosen. The decisions template (`elements/decisions/template.md:88-93`) has the
  *Rejected* of a decision written from rows hold the ways not chosen that the source keeps "each with
  the cost or the reason kept beside it", and never a way the writer derives (WAY-134). Here both
  items stand with no reason, in the list that WAY-100 reads as what the adopting decision weighed and
  refused; the reason the source keeps — outside this task, to be decided apart — is dropped.
- **Why it matters:** a later task that proposes a limit on simultaneous instances, or the field in
  the part map, meets a binding decision that reads as having refused it, and has to argue against a
  refusal nobody made (WAY-134's rationale: "A rejected option the writer of an entry derives reads as
  one the human weighed").
- **Evidence:** the sentence quoted; the task's answer under "Które pozycje dopisku z 12.11.2026
  wchodzą do tego zadania?" ("Poza zadaniem: limit jednoczesnych instancji, pole „jak to sprawdzić” w
  mapie części") and *Out of scope*. The rest of that list — the `test-run` items "Zostaje przy VOX" —
  is the human's own list and agrees with its source.
- **Slice:** none.

Contradiction: yes — the answer under the question on the addendum of 12.11.2026, and WAY-134.

### I6. WAY-407 binds the refinement of a task but its *Scope* names only the task cycle

- **Place:** `foundations/decisions.md:6834` (WAY-407 *Scope*), against its sentence "The refinement
  of a task writes no list of inputs to try into the task document."
- **What is wrong:** the refinement of a task belongs to `project-level` by the part map ("the
  refinement of a task before its implementation cycle"; its skill is
  `project-level/task/skill/SKILL.md`). WAY-21 has *Scope* name the parts a decision governs "so that
  the decisions governing a change are found from the files it touches". WAY-238, which carries the
  parallel rule that a task's refinement holds no plan of tests, names `project-level` in its scope.
- **Why it matters:** a change to the refinement skill selects decisions by `--part project-level`
  and does not find WAY-407, so it can add the list of inputs to try that the human refused under the
  question on who approves the plan.
- **Evidence:** the *Scope* line; part map entry `project-level`; WAY-238 *Scope*.
- **Slice:** none.

Contradiction: yes — WAY-21.

## Minor findings within the task (fixed in the same fix, WAY-161)

- **M1.** `foundations/decisions.md:6741-6756` and `:4877-4882` — form of the binding sentences.
  WAY-406 answers the question of its heading in two paragraphs of six sentences, and its second
  paragraph folds in parts of other questions (what happens where no way is settled; one item for the
  screenshot and the walk); WAY-319's added sentence answers another question (how the condition
  reaches a product) inside the paragraph of its main question instead of a paragraph of its own. The
  template ("Binding sentences", `elements/decisions/template.md:125-127`) wants one to three
  sentences answering the heading in the first paragraph, and a paragraph of its own for each part of
  another question, as the change does correctly in WAY-121. Minor by WAY-364: the content agrees with
  the files.
- **M2.** `foundations/decisions.md:6789` — WAY-406's *Rationale* says "a practice of testing one task
  that a team of the author's uses": throughout WAY-406 "the author" is the author of a change, an
  agent, so the phrase reads as the agent's team. And `:6778` "no step of the cycle made an agent find
  what the tests leave out" tells what the process lacked before the decision, which the template's
  rule on *Rationale* keeps out (WAY-05: "nor what the process's own tools do or lack today, and does
  not tell how the decision was reached").
- **M3.** `task-cycle/change/SKILL.md:155-159` — the new bullet of section 6 ("for a change that alters
  behaviour a user sees …, the walk of `walkthrough.md` …; or … that it alters none") stands in the
  report of every variant of `make-change`, the fix and the correction included, while section 3 and
  WAY-406 say the fix does not walk. A fix of a screen change is asked to report a walk it must not
  make. Naming the readers here as in section 3 removes the clash.
- **M4.** `foundations/decisions.md:3884-3886` — WAY-121's *violates* keeps a broken line: "a
  definition" / "reaches the gate" / "with a store of data …" — the short middle line is a remnant of
  the insertion; cosmetic.
- **M5.** `task-cycle/change/walkthrough.md:66-70` — the block of effects that cost or cannot be undone
  cites WAY-13, which covers only operations that cannot be undone; a paid call of an API is not one.
  The block's source is the practice WAY-406 adopts; naming WAY-406 there would not mislead.
- **M6.** `foundations/decisions.md:6829-6832` and `:6859-6862` — WAY-407 and WAY-408 say "the
  author" only, while the walk is also the executor of a slice's (WAY-406, `walkthrough.md:4-6`,
  `:96-99`). A reader of WAY-408 alone can take the correction before review as the one author's duty
  only.
