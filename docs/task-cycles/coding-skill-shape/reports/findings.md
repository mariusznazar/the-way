# Findings to fix — blocking findings of the review of 097123e, in the reviewer's words

Copied from `review.md`, lines 19-99, unchanged.

## Blocking findings

### 1. The opening of `task_document.md` drops items of the task document on the route of one kind (Important, within To do 10; new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/product-guidelines/coding/task_document.md:3`
(with `:15`, `:34-38`; same form at `settle.md:3`)

**To paste:** On the route of one kind this sentence limits the whole task document to what "The route
of one kind" gives, and that rule gives *To do* only the kind's file with its index row. The item "write
the test of each new invariant" is then not written, though that route settles invariants; *Context*
loses the comparison's `do not copy` places too.

**Why I report it:**

- What the sentence is for: To do 10 limits what steps 4 and 5 *settle and check*, and adds what *To do*
  gains. The rule in `SKILL.md:70-74` says exactly that. The opening of `task_document.md` is text the
  author added, listed in `reports/assessment.md:109` as a pointer. It says something wider: "write into
  the task document only what ... gives, of the items below".
- The mechanism: an agent on the route reads the rule, whose only sentence about *To do* is "the task's
  *To do* gains `guidelines/coding-<kind>.md` with its row in the index". "Gains" alone excludes nothing;
  "only ... of the items below" makes it exclusive. The presence of each item in the list below is what
  the opening cancels.
- Example: a product has nine unindexed endpoints. Step 3 compares them; step 4 settles the exemplar and
  one rule a script checks, with its invariant, "each with a test of the product's suite"
  (`settle.md:25-26`, `:37`). The agent writes *To do* from `task_document.md`: the file and the row. The
  item at `task_document.md:15-16` falls out. The kind file's rule then names an invariant "whose test
  checks the rule" (`template.md:102-103`), and no item of *To do* asks for that test; under WAY-61 the
  invariant reads `review` until a test cites it, so the rule a script was to check is checked by no
  script, and the review of the task, which compares with *To do*, has nothing to hold it to. *Context*
  (`task_document.md:34-38`) goes the same way: `kinds.md:15-16` makes the agent find each `do not copy`
  file with its file and line, and the cycle's author, who "reads only the task document", gets the
  status without the place. The route has no prior use (task *Context*), so nothing but this text
  decides what an agent does.
- The same form at `settle.md:3`: "settle only ... of the items below" covers the item **Critique**
  (`settle.md:47-49`), which is no matter to settle. The author's own counting has that critique run on
  this route (`reports/word-counts.md:314`), and WAY-120 sends a completed set through it, so the text
  should not leave that open.
- What the author's check missed: its weakest point was rule preservation by sentence comparison and a
  walk. A sentence comparison cannot see a new sentence that switches old sentences off, and its walk of
  route 6 (`author.md:117-119`) records that "steps 4 and 5 open with the pointer", not what the pointer
  leaves.
- Rule of the task: "Outside To do 9-13 no rule disappears". The route lies inside To do 9-13, but To do
  10 names the invariants as within it, so losing their test is not what To do 10 settles.
- Fix, for example at `task_document.md:3`: "On the route of one kind, take from the items below what
  concerns that kind, as "The route of one kind" in `SKILL.md` gives: its file with the index row, the
  test of each new invariant, its choices, and what the comparison found." `settle.md:3` likewise names
  what it limits ("of the choices and invariants below") so that the critique stands. `hand_back.md:3`
  fits To do 10 as it is ("check only").

### 2. The *Rationale* of WAY-216 holds a reason nobody gave, and it is false of a trial run (Important, within To do 13; new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/foundations/decisions.md:5969`
(lines 5969-5972)

**To paste:** "Research and a trial run answer a new scope" is the author's own reason for a decision the
human settled, and no source of the task gives it. It is also untrue of the trial run: a refresh covers
no new scope and still runs one (`recognize.md:25-26`). The reason should come from the row's source or
go.

**Why I report it:**

- What the sentence is for: the template has a changed decision's *Rationale* describe the decision as it
  then stands, and an agent reads it in a borderline case.
- The rule: WAY-29, binding sentence: "A rationale an agent proposes for a human's decision goes to the
  human as a question, never into the entry; the rationale of a decision an agent takes in a task is the
  agent's to write." Rows 1 and 2 are the human's ("Zostaję przy B", "Tak, przyjmuję"). The review of the
  whole change also checks "nothing the change takes from them altered or invented". The author says so
  itself: "The *Rationale* sentence is my wording (no source gives one)" (`author.md:174`, `:211`).
- Mechanism and values: the sentence pairs research and a trial run as both answering a new scope. For
  research that holds, and the foundation says so (WAY-211, WAY-251 rationales). For a trial run it does
  not. `recognize.md:25-26` gives "existing coding guidelines, refreshed or extended: step 2, and step 3,
  which tries the set", WAY-251 has a refresh stay "within the scope they already cover", and WAY-204
  prices the trial run as "each time a set is adopted". So the entry the change writes and the file the
  change writes disagree on when a trial run happens; an agent reasoning from the rationale in a
  borderline case would drop the trial run at a refresh. WAY-29 gives the danger itself: "a reason an
  agent writes looks exactly like a recorded one".
- Its last clause is sourced and can stay: "a task that is an extension for another reason keeps its
  research (WAY-211)" is row 1's own reason for rejecting the other wording.
- Fix: replace the first clause by what the rows keep: row 2's cost (without it every task creating a
  first file of a kind could pull research of all the standing checks) and question 3's (an agent on
  the comparison improvises and may make a full audit); say nothing of why a trial run exists.
