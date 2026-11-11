# Findings of the review of the whole change (`reports/04-review-report.md`, `FAIL 0d59ce9e4b4e5cd76029c405b878f94cb33df56f`)

Cut from the report in the reviewer's words.

## Blocking

**I-1. The scope of "a change that leaves one there" is stated wide in three places and narrow in the
request template that carries it out (WAY-263).**
Places:
- `task-cycle/skill/request_template.md:249-253` (item 15) gives an item only for a `TODO` "that the
  change writes, or keeps in an entry it edits", and says "A `TODO` in an entry the change does not
  touch is not the change's and gives no item".
- `foundations/decisions.md:1681-1682` (WAY-71): "a change that leaves one there puts it before the
  human"; `elements/common/rules.md:20-22`: the same; `foundations/decisions.md:9077-9078` (WAY-287
  binding sentence): "each descriptive `TODO` in an invariant's *Rests on* that the change leaves on
  the main branch"; `foundations/decisions.md:9114-9116` (WAY-287 rationale): "A descriptive `TODO`
  left in an invariant's *Rests on* ... stands here".
- The task's To do 7 reads "każde opisowe `TODO` w *Rests on*, które zmiana zostawia na gałęzi
  głównej".

What is wrong: the three entries the change writes say that every descriptive `TODO` the merge leaves
on the main branch is put before the human; the template, which is the only place that tells the cycle
what to do, narrows that to the entries the change edits. A reader of WAY-287 (the reviewer of a later
request, or the cycle comparing a request with the decision) will count an old `TODO` in an untouched
entry as missing from the request; a reader of the template will not put it there. WAY-263 grades a
file that "restates [an entry] differently, including more broadly or without a qualification"
Important. The author named this as the weakest point of the work and asked for a ruling.

My answer to the author's question: the narrow reading is workable, and the reason the author gives
(every request would repeat the same old gap) is sound. But then the decisions and `rules.md` have
to say the narrow thing, because they are what a later agent is compared with. The task's sentence is
ambiguous ("zostawia" can mean written or kept in an edited entry, or merely not removed), and the
task's own Out of scope line about loop2's bare `TODO` (it is reported by the script after the pin and
described by "that update in loop2") fits the narrow reading, since that update edits the entry.

Evidence: the five quotations above; nothing in WAY-71, `rules.md` or WAY-287 carries the qualification
"in an entry the change edits".

Fix: either add the qualification to the WAY-71 binding sentence, `rules.md:20-22` and the WAY-287
binding sentence and rationale (the task's sentence of To do 6 is then changed, which is a decision of
the human, not of the cycle), or widen item 15 to every `TODO` on the tree after the change. The first
changes the wording the task gives for WAY-71 and `rules.md`; the second is the task's literal wording
and costs one item per request for as long as an old gap stands. Scope: within the task. Slice: none
(one author, no plan).

## Minor findings of the review of the whole change within the task

**M-1. `task-cycle/skill/SKILL.md:48`, the pin-move run, still says "Run the product's gate on that
commit as step 10 gives" while step 10 now says to start the gate after the return step.** The author
changed the same phrase in sub-step 9.4 (`SKILL.md:326`) and in `blocked_finding.md:8` ("at once"), and
left this one, calling it "a run on a commit, not on the finished change". The result of this run is
handed to steps 4, 8 and 9 (same paragraph), so it must not wait for step 11; a literal reader of
"as step 10 gives" is told to wait. Add "at once" here too (WAY-33). Within the task (it is a
consequence of To do 2).

**M-2. `task-cycle/skill/SKILL.md:326` is a 131-character line in a file wrapped at 100, and the added
clause makes the sentence a chain of commas:** "change as step 10 gives, at once, since no return step
runs, run `task-cycle/cycle_stages.py`, prepare ...". The reader can take "since no return step runs,
run" as one clause. Rewrap and set the clause off (a dash or parentheses). Also `SKILL.md:362` ends a
line after "The authors' focused checks are not", a short line left by inserting the task's two
sentences (cosmetic). Within the task.

**M-3. A bare `TODO` inside a list in *Rests on* still passes
(`elements/common/foundation_check.py:102-103`, `:397-409`).** `TODO_VALUE` matches only a value that
begins with `TODO` followed by a blank, a backtick or the end. I ran `foundation_check.py` on a scratch
copy of the foundation with these values in an invariant's *Rests on* (exit 1 for the copy's other
errors, none about this field): `git-state · TODO` gives only "names no fact" for `git-state`, no
bare-`TODO` error; `TODO,` gives no error at all; `TODO — x · TODO` gives no error; `TODO—the fact` and
`TODO: the fact` give "is no identifier of a fact" (an error, but not the hint the task asks for).
The task's answer to question 6 says the bare `TODO` in *Rests on* "jest błędem"; To do 5 words it as
a value that begins with `TODO`, which the check meets. So this is polish: either say in the
docstring that only a value that begins with `TODO` is read, or report a bare `TODO` item anywhere in
the field. Also note the check accepts a description without the dash (`TODO the store`) though the
rule (WAY-71, `rules.md:20-21`) states the form with it; the author reported this (*Choices* 5). Within
the task.

**M-5. WAY-71 now governs what a request shows the human, but its *Scope* does not name
`task-cycle` or `agent-instructions` (`foundations/decisions.md:1685`), and WAY-287's *Verification*
(`:9082-9100`) has no example of the new item.** A cycle that selects decisions by *Scope* "task-cycle"
(the method of `way_of_working.md`, "Reading the foundation", step 2) for a change to the request
template will not find WAY-71. Adding the part, or a *Relations* link from WAY-287 to WAY-71, is a
change to approved decisions; it is not in the task. Mostly outside the task; the *Verification*
example of WAY-287 is within it.

**M-6 (new in the amendment). WAY-160 states in its rationale prose a rule that binds later work, which
WAY-05 says stands in a binding sentence or a field (`foundations/decisions.md:4582-4583`).** The added
rationale says: "The price is that a failure of the gate comes after the return step, so the fix of
that failure sends the return step back to its range." The rule itself ("Where the gate then fails and
its fix changes code, the return step compares that fix's range too") lives in
`task-cycle/skill/SKILL.md:361-362` (the task's To do 2 gives it there), but neither WAY-160's
binding sentence nor its *Verification* (`:4565-4568`) carries it, so a reviewer comparing a cycle with
WAY-160 has nothing to check it against, and a later edit of step 10 could drop it without
contradicting an entry (WAY-05: "what a decision forces on later work stands in a binding sentence or
a field, never in prose"). The rationale sentence is the author's, not the task's (the task changes
only the *complies* example and *Rejected*). Fix: say the rule in the *complies* line (for example,
"and where the gate fails and its fix changes code, compares that fix's range in the return step too")
or leave the sentence as a plain statement of the price without "sends ... back". Within the task.
