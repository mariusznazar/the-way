FAIL 4a3ee37

# Review of the whole change — logs-life-and-failure-notice

Range `5d66387..4a3ee37`, one commit, one author, no plan, so every finding comes from that commit and
no slice stands apart. `git rev-parse HEAD` is the head given. Trust boundary: no file the part map
names changes. Operation that cannot be undone: none. No invariant test changes.

Counts: 4 blocking (Important), 0 Critical, 6 Minor, 0 out-of-scope findings; 3 lines under Declined
to judge.

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

## Minor

1. `project-level/technology/start.md:24-26`: the lookup ends the item `— projected` and does not remove
   the nested line, though spec D1 says "The nested line goes when the item ends `— projected`, here and
   in the lookup of trap 1"; `settle.md` sub-step 7 does remove it. After an interrupted write, a stale
   `Changes:` line reaches the gate. A scratch run shows the readiness check passes it, so the harm is
   a stale line in an approved definition.
2. `foundations/decisions.md:4474-4476`: WAY-165's complying example gives only `— held by`; spec D1 asks
   for both markers. The `— projected` case stands only among the violations.
3. `foundations/decisions.md:4492`: "(WAY-270)" stands on the sentence about an entry that answers part of
   a matter, and WAY-270 says nothing of that. The sentence's rule is WAY-165's own; the citation sends
   a reader to the wrong entry.
4. `project-level/technology/failure_notice.md:15`: "ending `— open`" reads against `list.md`'s step for a
   projected decision of the definition on the same matter, which gives `— projected`. A new list could
   research a choice already projected; `start.md`'s lookup corrects it only at a resume.
5. `project-level/task/skill/resolve_gaps.md:63`: "once and for each item apart" can read as two questions;
   spec D6 and WAY-139's example have one question, which the human may answer item by item.
6. Form: lines the change leaves unwrapped, `research.md:14` (153 characters), `research.md:24`,
   `settle.md:73`, and the violating examples of WAY-139 in `foundations/decisions.md`; the course is
   written `10xDEVS` at `:7955` and `10xDevs` at `:6713` and `:7809`.

## Coverage

| Item | State |
|---|---|
| To do 1, row 1 | met: template, WAY-165, `running_product.md` |
| To do 2, row 2 | met except finding 1 (the alert); the rest in WAY-270, the template, `failure_notice.md` |
| To do 3, row 3 | met; D4's reading in the same words in `SKILL.md` step 1, `list.md`, `failure_notice.md`, WAY-270 |
| To do 4, row 4 | met in `resolve_gaps.md`; WAY-139 restates it with finding 3 |
| To do 5 | met; no tool named in the step's files; the absence in the template, `research.md` and WAY-270; WAY-138 covers it; WAY-166 worded for its family |
| To do 6 | met; no script changes; template, `failure_notice.md`, WAY-270, WAY-165 |
| Questions carried to cycle | answered by spec D1, D2 and made, with finding 4 and Minor 1 at the edges |
| Answers 1, 3, 4, 5, 6 | met; answer 3 in WAY-270's rationale and *Verification*, and no text states the old boundary (a search confirms spec D8); answer 4 replaced, with no trace of it left in the files of the step |
| Answer 2 and its mark | criterion met; finding 2 keeps the replaced part |
| *Rejected* (WAY-134) | checked way by way against answers 1, 2, 5, 6 and the Context line; nothing derived; the omission of answer 2's way "only at a definition" is right, since the final design is that way in part |
| Restriction of the task's Context | no product and no tool named in the step's files; `grep` for `loop2`, `mikrus` and tool names finds nothing; I opened nothing it forbids |

## Readings of the spec judged and accepted

- D4 reads row 3's criterion so that silence counts as yes. D6 quotes an entry's answer instead of
  asking, where row 4's words say the refinement asks. Both are named in the spec with their cost, both
  stand in the entries written and in the author's meaning sentences, and the second follows the rule
  `resolve_gaps.md` already opens with. No finding; the human sees both at the merge.

## Own-work check of the author

The requirement it names, a resumed list not turning back, fits a weak place, and the chain does close
for the marker. Its check was a read, and "Reading showed the chain closed" misses Minor 1 and, by
reading resumed lists alone, finding 4.

## Declined to judge

- A failure item the human strikes from the list comes back at the next resume, since the look adds what
  it finds missing: the three matters behave so already, and the spec's table asks for it; a change of
  that behaviour is outside the task.
- Whether "the matter" should reach a product that is no running service, such as a library: row 3 and
  D4 settle the criterion, and a deliberate absence answers it once.
- WAY-166's complying example recommends the container's output with no word on its life: its subject is
  whether an agent can use an option, and the task names no change there.

## Checks

- `python -B elements/common/foundation_check.py .`: exit 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py`: exit 0, "entry points are current".
- `python -B gate/run_tests.py project-level`: exit 0, 268 tests OK.
- `git diff --check 5d66387..4a3ee37`: exit 0. `git ls-files --eol` on the new file: LF, as the repository
  gives.
- Scratch script in my scratchpad, importing `readiness_check` and the helpers of
  `project-level/test_readiness_check.py`, nothing written to the worktree, exit 0: an open item with a
  nested `Changes:` line of either form gives only the open-item finding; a projected item with a stale
  nested line and a projected item under `#### DOC-02 — <question>` give no finding of condition g. The
  spec's claim that the nested lines pass the check holds.
- Manual: read the step's files as an agent would, for a new list, a resumed list at each marker, a run
  at a task, and a deployment task with a skill, without one, with a refusal and with an answering
  entry. Searches of tracked files for the old logs wording, `running_product`, `failure_notice`,
  "deployment skill", WAY-139, WAY-165, "without touching" and "bez dotykania".
- Not run: the full gate, which is the cycle's own; the behaviour of an agent following the texts, which
  no test exercises.

## Reading and reaches

Selection by "Reading the foundation", parts `project-level` and `decisions`: invariants of
`project-level` and `every` by their sentences where they bear on the change, the part map's entry, the
glossary's entry, and the decisions whose *Scope* names either part, each whole, with this exception:
of the `project-level` selection, WAY-216, WAY-217, WAY-218, WAY-230, WAY-238, WAY-242 and WAY-247 were
judged by their headings alone, as guidelines and plan order the change does not reach, and WAY-215 and
WAY-256 were read in part. WAY-263, not in the selection's parts, was read for grading.

Reaches beyond the dispatch: `elements/decisions/skill/SKILL.md` and `elements/common/projected_mode.md`
for projected mode, to test finding 4 and spec D1; `project-level/skill/SKILL.md` steps 0 and 7, for how
a definition resumes; `project-level/readiness_check.py` and its test helpers, for the nested lines;
`project-level/technology/reserved_choices.md`, as section 2 asks.

## Searches not found or unclear

- `alert` in the change: not found (finding 1).
- The phrase of answer 3's old boundary: not found in the repository, as spec D8 says.
- Unclear: whether WAY-270's *Verification* wording "no tool for now" keeps row 2's "na początek", which
  the spec's constraint keeps out of the binding sentences; I read it as allowed in an example.
- Unclear: nothing tells a resumed step what to do at `ready for gate`; `start.md` speaks only of an
  approved definition. `project-level/skill/SKILL.md` step 0 routes by the status line, so the step is
  not reached, and I read the spec's non-goal as met.
