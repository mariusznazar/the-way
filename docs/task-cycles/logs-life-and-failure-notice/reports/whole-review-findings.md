# Findings to fix — whole-change review `FAIL 4a3ee37`

The blocking findings of `reports/whole-review.md`, in the reviewer's words. Its Minor findings are not yours to fix.

## Important (blocking)

### 1. WAY-270 drops the alert that row 2 and To do 2 name

- **Place:** `foundations/decisions.md:7900-7912` (binding part) and the *Verification* below it.
- **What is wrong:** row 2 and To do 2 give the matter's answers as a tracking tool, an alert or a
  deliberate absence. Spec D5 says the step's files name only the deliberate absence *because* "The
  kinds in row 2 stand in the new decision only". WAY-270 holds tools and the absence; the alert stands
  nowhere in the change.
- **Why it matters:** WAY-134 has the cycle write each kept row whole, keeping its meaning. The step's
  files are silent by design, so the decision was the one place the kinds could stand. With only "the
  tools found" and "no tool for now" in the entry, a later reader takes the matter for tool or no tool,
  and the human's settled kind of answer is lost; answer 1 also names an alert built on the logs as
  the accepted weak point, which then has no anchor.
- **Evidence:** `git diff 5d66387..4a3ee37 | grep '^+' | grep -i 'alert\|track'` prints nothing. The
  author's report describes only the tool wording.
- **Fix in one line:** name the alert in WAY-270, in a complying example at least, beside a tool that
  collects failures and the deliberate absence, with no product's name.

### 2. WAY-270's rationale keeps the reason answer 5 replaced

- **Place:** `foundations/decisions.md:7941-7942`: "a first deployment needs a place to run, a choice
  that goes through the step whenever nothing settles it, so the question comes with it."
- **What is wrong:** this is answer 2's reason word for word ("ten wybór zawsze przechodzi przez krok,
  jeśli nic go nie rozstrzyga, więc pytanie pada i przy projekcie, i przy zadaniu"). The mark under
  answer 2 says it is replaced in part: the criterion stays at a definition, and at a task the question
  comes through the deployment skill's list. A place to run chosen in a run at a task goes through the
  step, and the failure item does not come with it unless the note touches it.
- **Why it matters:** the sentence contradicts its own entry: the binding part at `:7904` ("it enters
  the list only where the note touches it") and the *Rejected* way at `:7973`. WAY-05's own rationale
  says agents generalise from the reasons they are given, so a run at a task that picks a place to run
  has a written reason to add the item, which WAY-270's *Verification* lists as a violation.
- **Evidence:** the task's marks under answers 2 and 4; the lines above. The author left the matching
  way out of *Rejected* for this very reason (report, "Choices"), and kept the reason in *Rationale*.
- **Fix in one line:** bound the sentence to a definition, and leave the task to the deployment skill's
  check, which the next sentences of the rationale already name.

### 3. WAY-139 says "the last two items" of a list whose last two items are not the two

- **Place:** `foundations/decisions.md:3504-3505` and `:3509`; `project-level/task/skill/resolve_gaps.md:56-57`.
- **What is wrong:** the list is punctuated into six items, the fifth being "how to read the logs and
  how long the record lives, between deployments too". So "For the last two items" covers how to read
  the logs as well. `resolve_gaps.md` says the two items are how long the record lives and how a human
  learns of a failure, and spec D6 says the check "goes on for the five items as today".
- **Why it matters:** the two accounts differ: read by the entry, a deployment skill silent on how to
  read the logs goes the quote, ask or refuse way, and a refusal would then cover it; read by the file,
  it gains a *To do* item as today. WAY-263 grades this Important: a changed file restates the entry
  differently. Row 4 says the list gains two items, and the entry shows one and a half.
- **Evidence:** the two passages; task To do 4 ("dostaje dwa punkty").
- **Fix in one line:** give the record's life its own item: "how to read the logs; how long the record
  lives, between deployments too; and how a human learns of a failure".

### 4. A new list over a silent decision is not nested, so the result depends on when the list was written

- **Place:** `project-level/technology/list.md:23-24`, `project-level/technology/running_product.md:22-33`.
- **What is wrong:** the nested line, `Changes:`, is prescribed only under the heading "A list already
  written". A definition whose section reads `TODO` takes the path `SKILL.md` step 1 → `list.md`; there
  a silent decision "does not hold" the matter and the item is `— open`, with no word on nesting. The
  template (`definition_template.md`, nested items) only permits the line.
- **Why it matters:** this is the path the task's Context names as the main effect, the next definition
  of a product with a silent logs decision. With nothing nested, `settle.md` sub-step 1 and the opening
  of `research.md` do not give the research agent that decision, `research.md` step 1 does not enter its
  answer, so a human who wants to keep today's logs does not see that option, and sub-step 7 names no
  entry. `record-decision`'s own search of the log will probably still find the entry, so the likely
  damage is a comparison without today's answer rather than a second entry. Spec D1 states the rule "for
  a new list and for a list already written", its goal is that "A resumed definition behaves as a new
  list does", and it rejects a way because "the result depends on when the list was written". The
  author's own-work check read the chain for resumed lists only.
- **The same sentence reaches a run at a task:** `task_run.md` keeps `list.md`, and its exception nests
  the decision only for "A choice a decision of the foundation holds". Taken literally, the new
  sentence says a silent decision holds nothing, so the exception would not fire, against spec D6's
  second reading ("the item stands `— open` with that decision nested").
- **Evidence:** a read of the two paths, file by file; there is no test of the step's text.
- **Fix in one line:** in `list.md:23-24`, say that such a decision does not hold the matter and the item
  stands `— open` with that decision nested under it as `running_product.md` gives; the section heading
  there, or its fourth bullet, then fits both.

