# Spec — a light cycle for a small change that leaves the foundation unchanged

- Task: `task_frozen.md` in this directory ("the way: lżejsza ścieżka cyklu dla małej zmiany bez
  zmiany fundamentu"), independent, `Status: ready for cycle`.
- Base: `foundations` at c64a607; every quotation below is from that commit.
- Method: Superpowers 6.4.1 `brainstorming`, architectural path (the cycle requires a written spec
  for every ready task). Classification by the skill alone: architectural — the change alters the
  interface other parts depend on (the task-cycle skill every product pins, and two decisions).
- Status of every choice in this spec: proposed by the design agent; the orchestrator's go-ahead is
  provisional; Mariusz accepts the meaning of the changed entries at the merge (WAY-07, WAY-114).

## 1. Understanding

What the task says (source: `task_frozen.md`):

- Add to `implement-task` a lighter way through the cycle: one executor gets the task directly,
  without a spec and a plan, and makes the whole change; afterwards the same checks as the full
  way (the whole product gate and the checks required by what the change touches); one review of
  the whole (point 1).
- Entry by a rule of thumb: the task does not change the foundation; implementation fits in
  10 minutes; it does not need very large or very many files read into context (point 2).
- A change that turns out to touch the foundation simply and obviously stays on the light way and
  its entry goes through its element's skill and one independent assessment (WAY-10); a
  non-obvious touch switches to the full way (point 3).
- WAY-13 changes so size may lighten preparation and implementation (spec, plan, number of
  agents), never the checks after the change (point 4).
- WAY-125 changes so design, spec, plan and per-task reviews bind the full way and the light way
  has its own steps; the rest of WAY-125 stays (point 5).
- Switch: the orchestrator judges the rule at the start, in the same analysis as the foundation
  analysis, and records its reasons; an executor that sees the change outgrow the rule returns to
  the orchestrator with a report without code or diff; the attempt is discarded; a fresh designer
  gets the report with the task; the change is made again on the full way (point 6).
- Acceptance: a task that fails the rule goes through the full way exactly as before.

What this spec assumes (each is a recorded choice in section 9):

- The light way is a lighter form of preparing and making a change inside the foundation route
  WAY-13 already chooses, not a new WAY-13 path (D1).
- In English it is called the *light cycle*, the other the *full cycle* (D2).

## 2. Design in one paragraph

Two independent choices are made at the start of every task, in one analysis: the **foundation
route** (WAY-13's "paths that merge a change": does the task change the foundation?) and, new, the
**cycle** (light or full: is the task small enough for one agent from the task alone?). The light
cycle is open only to tasks whose foundation route is "unchanged". It drops design, spec, plan,
subagent-driven execution and per-task reviews; it keeps everything from step 10 on — the full gate,
the sharpness checks, one final review, the return step, the one independent assessment, the
request. When a light-cycle change touches the foundation simply and obviously, the foundation route
is re-recorded as "changed" and the entry follows that route's rules (element skill, search,
assessment, meaning sentence in the request), so no change that alters a foundation entry ever runs
on the route for tasks that leave it unchanged. Anything larger switches to the full cycle: report
without code, attempt discarded, fresh designer, full cycle exactly as written.

## 3. The light cycle

### 3.1 Entry and who judges it

- The orchestrator judges, in step 4's analysis that settles the foundation route, whether all
  three findings hold:
  1. the task leaves the foundation unchanged — the foundation step of the skill would not run for
     it (no entry or invariant test changed, no projected entry assigned or made true, WAY-126);
  2. one agent can implement it in about ten minutes;
  3. its implementation needs neither very large files nor very many files read into context.
- All three hold → light cycle. Any one fails → full cycle, steps 6–9 exactly as written.
- The choice and the reason for each finding assessed go into a new `## Cycle` section of the
  cycle record (section 6); once one finding fails, the rest may be recorded as not assessed. The ten minutes are an estimate, not a timer (D12); "very large" and "very many" stay
  the orchestrator's judgment, recorded with the files it expects (D3).

### 3.2 Steps

1. **Executor.** One fresh executor receives the frozen task, the applicable source paths, the
   pinned foundation and the skill's dispatch contract. It makes the whole change from the task,
   without a spec or a plan, uses Superpowers `test-driven-development` for behaviour changes (the
   same rule as the full cycle), commits, runs focused checks and returns before any review. It also
   returns, with its work committed, when the change touches the foundation and when the change
   outgrows a finding of 3.1.
2. **Foundation touch** (only when it happens). The orchestrator rules and records whether the
   touch is simple and obvious (3.3). Simple: the foundation route is re-recorded as changed; the
   executor writes the entry through its element's skill, under the rules the skill's foundation
   step gives an entry the cycle writes (whole-foundation search, guards, meaning sentence kept for
   the request; for a decision also *Approved by* `<approver>, merge of <request link>` and
   *Review when* set), before continuing the code that depends on it. Not simple: switch (3.4).
3. **Checks and one review.** Step 10 runs in full and unchanged: focused checks, sharpness
   recalculated from the diff, the product's full gate (the critical-flow tests included, WAY-45),
   adversarial input checks at a trust boundary (WAY-48), visible behaviour in the running product,
   deliberate breaks where a change holds an invariant check (WAY-69). The whole change is the one
   implementation unit, and one Superpowers `requesting-code-review` of the whole change, with the
   frozen task as its requirements, is both that unit's review and the final review. The executor
   fixes the findings, the affected checks run again, and the same reviewer reviews the fix range
   once (D6).
4. **Return step, assessment, request.** Steps 11–14 as written. An entry from 3.2 step 2 joins the
   one assessment of step 11 with the return step's entries; a check the return step writes keeps
   its own author and reviewer as step 11 gives them (WAY-69).

### 3.3 "Simple and obvious" (D4)

A foundation touch is simple and obvious when all of these hold; otherwise it is not:

- the entry's change follows from the task's required outcome with no choice the task leaves open;
- it changes the meaning of no approved decision (that would need a question to the human,
  WAY-114);
- it contradicts no current entry (no WAY-25 or WAY-30 case);
- it writes or changes no invariant and no invariant test (WAY-03 keeps invariant tests out of
  implementation; WAY-69 forbids the code's author writing the sentence or the check).

Example that passes: a part map's *Files* gaining a path for a file the change adds, since every
file belongs to one part (WAY-44). Examples that fail: a decision's binding sentence that no longer
matches the code; an invariant whose sentence the change makes false; a new rule the code now
enforces (the return step's, or the full cycle's).

### 3.4 Switch to the full cycle

- When: while the change is being made or its review findings fixed (D7), the executor — or the
  orchestrator from its work — finds that it outgrows a finding of 3.1 or touches the foundation in a
  way that is not simple and obvious.
- The executor returns a report **without code and without a diff**: why the change grew, which
  files and obstacles it found, what proved not obvious. File paths are allowed; code snippets are
  not. The orchestrator checks the report holds no code and keeps it in `reports/`.
- The orchestrator records the attempt's last commit (a historical name, not a link to follow) and
  the names of the files it changed, then
  discards the attempt — its foundation entries included — by resetting the task branch to the
  recorded base commit (D8). The light cycle never pushes before step 12, so nothing remote changes.
- The orchestrator records the switch and its reason, then continues at step 6: a fresh design
  agent receives the executor's report beside the frozen task, and the full cycle runs as written.
- What stays in the record from the discarded attempt (carried question 2): the `## Cycle` lines
  (choice, any touch ruling, the switch with its reason), the Events rows of the executor's
  dispatch, return and the reset, the executor's full reports in `reports/`, the attempt's last
  commit and file names, and the attempt's choice rows with *Used by* naming the discarded attempt.
  No diff or file copy, as for any commit.

## 4. Changes to `task-cycle/skill/SKILL.md`

Each change quotes the base text and gives the new text. Nothing else in the file changes.

**4.1 Front matter `description`.**
Base: "Use to take one ready the-way task through autonomous design, planning, implementation,
testing, review and a pull or merge request, or to apply review corrections to its open request.
Requires subagents and the Superpowers skills named by this process. The human reviews the request,
not intermediate steps."
New: "Use to take one ready the-way task to a reviewable pull or merge request — through autonomous
design, planning, implementation, testing and review, or, for a small task that leaves the
foundation unchanged, through one agent's implementation, the same checks and one review — or to
apply review corrections to its open request. Requires subagents and the Superpowers skills named by
this process. The human reviews the request, not intermediate steps."

**4.2 Step 4**, after its first sentence ("Determine and record whether the task changes the
foundation (WAY-13), which selects its foundation route before implementation."), insert:
"In the same analysis, choose the light or the full cycle as "Light cycle" below gives it, and
record the choice with the reason for each finding you assessed; once one finding fails, the rest
may be recorded as not assessed."
In the same step, base "Use the full subagent review loop even for low criticality." becomes
"On the full cycle, use the full subagent review loop even for low criticality."

**4.3 New section**, inserted after the paragraph that ends "...except that the code review also
writes the deliberate break of an invariant's check (WAY-69)." and before `## Design and plan`:

> ## Light cycle
>
> A task takes the light cycle when the analysis of step 4 finds all three: the task leaves the
> foundation unchanged, so the foundation step below would not run for it; one agent can implement
> it in about ten minutes; and its implementation needs neither very large files nor very many
> files read into context. Every other task takes the full cycle — steps 6 to 9 — exactly as
> written. The two cycles differ in how a change is prepared and made, never in the outcome the
> task has to reach or the checks run on the finished change (WAY-13, WAY-125); both run inside the
> foundation route of step 4. On the light cycle:
>
> - Dispatch one fresh executor with the frozen task, the applicable source paths, the pinned
>   foundation and the dispatch contract above. It makes the whole change from the task, without a
>   spec or a plan, using Superpowers `test-driven-development` for behavior changes, and commits
>   it. Its boundary is the committed change with its focused checks run; it returns before any
>   review. It also returns, with its work committed, when the change touches the foundation and
>   when the change outgrows a finding of step 4.
> - When the change touches the foundation, rule on the touch and record the ruling. The touch is
>   simple and obvious when the entry's change follows from the task's required outcome with no
>   choice the task leaves open, changes the meaning of no approved decision, contradicts no current
>   entry, and writes or changes no invariant or invariant test. On that ruling, record the
>   foundation route as changed; the executor then writes the entry through its element's skill, as
>   the foundation step below gives an entry the cycle writes, before it continues the code that
>   depends on it, and the entry joins the one independent assessment of step 11. Any other touch
>   switches the task to the full cycle.
> - When the change is made, run step 10 in full. The whole change is its one implementation unit,
>   and one Superpowers `requesting-code-review` of the whole change, with the frozen task as its
>   requirements, is both that unit's review and the final review: the executor fixes its findings,
>   the affected checks run again, and the same reviewer reviews the fix range once. Then continue
>   with steps 11 to 14 as written. Where the harness cannot resume the executor after a ruling or
>   for fixes, a fresh executor on the same branch, given the task and the ruling or the findings,
>   continues in its place.
>
> Switch to the full cycle when the executor, or you from its work, find while the change is being
> made or its review findings fixed that it outgrows a finding of step 4 or touches the foundation in
> a way that is not simple and obvious. The executor returns a report without code and without a
> diff: why the change grew, which files and obstacles it found, and what proved not obvious. Check
> that the report holds no code, keep it in `reports/`, and record the attempt's last commit, as a
> historical name rather than a link to follow, and the names of the files it changed. Then discard the attempt, its foundation entries included, by
> resetting the task branch to the recorded base commit, record the switch with its reason, and
> continue at step 6, whose fresh design agent receives the executor's report beside the frozen
> task.

**4.4 Step 6.** After its first sentence ("Dispatch a fresh design agent with the frozen task,
applicable source paths, the pinned foundation and the dispatch contract above."), insert: "After a
switch from the light cycle, also give it the executor's report, as the findings of a discarded
attempt." Base "because this cycle requires a written spec and plan for every ready task" becomes
"because the full cycle requires a written spec and plan for every task it runs".

**4.5 Step 9.** Base "Use Superpowers `subagent-driven-development`:" becomes "On the full cycle,
use Superpowers `subagent-driven-development`:".

**4.6 Step 13.** Base "The request contains: task goal and relation, source versions, design and
plan links, what changed and why," becomes "The request contains: task goal and relation, source
versions, the cycle taken and its reasons — after a switch, its reason and a link to the
executor's report — design and plan links on the full cycle, what changed and why,".

Not changed: steps 1–3 (all six Superpowers skills stay required, since a light task may switch),
step 5, the foundation step paragraph, steps 7, 8, 10, 11, 12, 14 and "Correction after review" (D15).

## 5. Acceptance criterion

"Zadanie, które nie spełnia reguły kciuka, przechodzi pełną ścieżką tak samo jak przed zmianą."

Holds when, in the diff of `task-cycle/skill/SKILL.md` against c64a607, every change that a task
failing the rule meets is one of: the qualifier "On the full cycle" (4.2, 4.5), "the full cycle
requires ... every task it runs" (4.4), the record of the cycle choice (4.2, section 6) and the
request's line naming the cycle (4.6). None changes a step, an agent, a review, a check or a gate of
the full cycle; the post-switch clause of 4.4 applies only after a switch. The light-cycle section
(4.3) is reached only by a task that passes all three findings.

## 6. Changes to `task-cycle/record_template.md`

- Header list, after the `Foundation route` line, add:
  `- Cycle: <light | full | full after a switch from light>`
  and the `Foundation route` placeholder becomes
  `<unchanged | entry or invariant-test change; affected entries; on the light cycle, the time a
  touch changed it>`.
- New section after "## Sharpness at start and after the final diff":

  ```markdown
  ## Cycle

  - Choice at start: <light | full> — foundation: <unchanged | changed>; one agent's time to
    implement: <estimate and reason | not assessed>; files read into context: <which, and their
    size | not assessed>
  - Foundation touched on the light cycle: <entry, the ruling on whether the touch is simple and
    obvious, and its reason | none>
  - Switch to the full cycle: <time, why the change outgrew the light cycle, the executor's report,
    the discarded attempt's last commit and the files it changed | none>

  Record the reason for each finding assessed; once one finding fails, the rest may read `not
  assessed`. The last commit of a discarded attempt is a historical name, not a link to follow: the
  commit is reachable only until the reflog expires. A choice or ruling of a discarded attempt keeps
  its row in the questions table, with *Used by* naming the discarded attempt.
  ```

- "## Artifacts" paragraph: base "Include the frozen task, `spec.md`, `plan.md`, code commits, tests
  and full agent reports." becomes "Include the frozen task, `spec.md` and `plan.md` on the full
  cycle, code commits, tests and full agent reports, the report of a discarded light-cycle attempt
  among them."
- "## Request handoff": add `- Cycle and its reasons: <as the request states them>` after the
  request URL line.

## 7. Foundation changes

Edited in place (no `main`; guide, WAY-07). Both decisions change meaning, so both are shown to
Mariusz at the merge and their *Approved by* becomes `Mariusz, merge of <request link>` (WAY-14,
skill's foundation step). *Change* stays `new decision`. Written by the cycle's foundation step
through `record-decision`, which may reword; the meaning below is what the spec fixes. Each entry
keeps the log's form: *Rationale* and *Rejected* stand as italic paragraphs after the field list
(`elements/decisions/template.md`), not as list items as they are shown below.

**Ground for changing two approved decisions without a question before the request.** Mariusz
approved the task document (`Status: ready for cycle`, approved 2026-10-08). It orders the WAY-13
change (point 4) and the WAY-125 change (points 5–6), and it settles the questions about them
("Questions to settle"). That approved task is the approver's answer WAY-30 ("approved with it by
the decision's approver") and WAY-114 (a question where "the entry would change the meaning of an
approved decision") ask for, so the foundation step needs no question before the request and no
blocked draft. The change of meaning is shown to Mariusz at the merge (guide, WAY-07).

**Wording beyond the task's words** — the agent's wording, to be shown as such in the request:

1. WAY-13 sentence 1 reworded from "What a task touches, never its size, sets its process" to "sets
   the path that merges its change and how sharply that change is checked"; needed, since the old
   wording contradicts point 4.
2. WAY-13 sentence 3's "never the outcome it has to reach", which restates sentence 2.
3. The switch-and-discard clause in WAY-125's first sentence (D9, from point 6).
4. The four conditions in WAY-125's first sentence that send a touched foundation to the full cycle
   (a choice the task leaves open, a change of an approved decision's meaning, a contradiction with
   a current entry, an invariant or invariant test written or changed), in place of the task's
   "w sposób nieoczywisty" (point 3; D4).
5. The relation WAY-125 → WAY-13 (D10).
6. The agent-written reason in WAY-125's *Rejected* for "a task once made by one agent finishing
   that way" (D13).

### 7.1 WAY-13/1 — What sets the weight of a task's process?

Binding sentences (sentence 2 unchanged):

> What a task touches, never its size, sets the path that merges its change and how sharply that
> change is checked: an agent's analysis at the start of the task settles whether it changes the
> foundation, which chooses among the paths that merge a change, while three things set how sharply
> it is checked — the criticality of the parts it touches, as the part map computes it, whether it
> touches the files of a trust boundary, and whether the change can be undone. Paths that merge a
> change differ in their steps, never in the outcome a task has to reach, and only a human sets a
> task to return knowledge instead of a change, which merges nothing. A task's size may lighten how
> its change is prepared and made — its spec and plan and the number of agents making it — never the
> outcome it has to reach or the checks run on the finished change, and otherwise serves only as a
> signal to split it; an agent may check a change more sharply than the map computes, never less, and
> a human decides on every change that cannot be undone.

Fingerprint of this wording: `97b17d59`, computed by `relation-model/fingerprint.py` from the bytes
of a UTF-8 file holding the sentences (the wording has em dashes; a string piped through a non-UTF-8
console gives other bytes); recompute after any edit. Base fingerprint: `c6b33aa9`.

- **Verification:** level 1 — invariants: foundation-change-path. Level 2 for the rest — an agent
  compares the change with the decision:
  - complies: a one-line format change that breaks users' saved data gets the sharpest checks and
    a human's decision; a copy change that touches no foundation entry is made by one agent without
    a spec or a plan and runs the same checks as any change to the parts it touches;
  - violates: a task takes the path for changes that leave the foundation unchanged because it
    changes few lines; a small task skips a check that the parts it touches call for; a change that
    cannot be undone reaches the main branch without a human's decision; an agent turns a task into
    one that returns knowledge instead of a change without a human setting it so.

  (Removed: "a task gets the heavier path because of the number of lines it changes" — a large task
  may now take the heavier preparation.)
- **Approved by:** Mariusz, merge of <request link>
- *Rationale:* size misleads both ways about what can go wrong: a rename across many files is easy to
  undo, a one-line change to a stored format can destroy every user's data, so what a task touches,
  never its size, sets its path and its checks. Size does tell how much preparation a change needs: a
  spec and a plan written ahead of a small change cost more than the change, while the checks on the
  finished change stay whole and a human still decides on what cannot be undone. Paths differ only in
  steps, because a weaker outcome would bypass the process; returning knowledge alters what a task
  delivers, so a human sets it.
- *Rejected:* one cycle for all tasks — how much process a task needs depends on what can go wrong;
  the path chosen by size — size misleads; a human approving every diff (DORA) — no fewer failed
  changes, and attention spent where it adds nothing; keeping a change that cannot be undone, or one
  touching a trust boundary's files, from the lighter preparation — it would take the lighter
  preparation from small tasks it suits, while a human's decision and checks kept whole already
  stop such a change.
- Other fields (*Scope* task-cycle, *Based on*, *Relations*, *Review when*, *Origin*) unchanged.

Meaning sentence for the request (Polish): "Rozmiar zadania może odchudzić przygotowanie i wykonanie
zmiany (spec, plan, liczbę agentów), ale nigdy wyniku zadania ani sprawdzeń gotowej zmiany; to, czy
zadanie zmienia fundament, i ostrość sprawdzeń dalej wyznacza wyłącznie to, czego zadanie dotyka."

### 7.2 WAY-125/1 — Which Superpowers methods does the autonomous task cycle adopt?

Binding sentences (sentences 2 and 3 unchanged):

> The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written
> spec, writing an implementation plan, test-first implementation, subagent execution with
> independent task and final code reviews, and preparing a pull or merge request, only for a ready
> task run through `implement-task`, which uses them all unless the orchestrator's analysis at its
> start finds it leaving the foundation unchanged and small enough for one agent to make from the
> task alone: that agent then makes it, test-first where it changes behaviour, and one final code
> review covers the whole change, while a change that proves too large for that agent, or whose touch
> of the foundation needs a choice the task leaves open, changes the meaning of an approved decision,
> contradicts a current entry or writes or changes an invariant or an invariant test, is discarded and
> starts again from a fresh design given the agent's report without its code. The orchestrator
> answers workflow questions and gives provisional stage go-aheads under the task owner's
> delegation, never records these as human approval, controls the return between stages, keeps
> agent reports before a borrowed skill cleans its workspace, runs the independent assessment of its
> foundation change and its return step, and brings the request to the human for review. Decisions
> reserved to a human by the foundation remain reserved; when required code cannot proceed without
> one, the cycle opens a blocked draft request; a different Superpowers version requires a reviewed
> change to the-way before use.

Fingerprint of this wording: `68b2d563` (from a UTF-8 file's bytes, as in 7.1); base `4c302238`. The
first sentence drops "independent" before "final code review" and the base draft's "the request is
prepared as for any task", both already said by the method list; the binding part is 246 words
(base 140). Sentence count 3 by the decisions guard's own counter.

- **Based on:** unchanged — the light cycle uses three of the six skills already observed.
- **Relations:** `derives from WAY-100@e7a74a18 · derives from WAY-13@97b17d59` — the fingerprint of
  the wording in 7.1, recomputed if the foundation step rewords it (new link, D10: the light cycle
  rests on WAY-13's third sentence).
- **Verification:** level 2 — an agent compares a cycle with the decision:
  - complies: agents use the named methods at version 6.4.1, return between stages, and show
    provisional choices in the request without claiming human approval; a task found small at its
    start, leaving the foundation unchanged, is made by one agent from the task, test-first where it
    changes behaviour, and its whole change gets one final code review; an attempt that grows too
    large, or whose touch of the foundation writes an invariant, is discarded and the task starts
    again from a fresh design that reads the agent's report;
  - violates: an agent treats its own spec approval as the owner's approval, skips the request
    review, or silently runs a different Superpowers version; a task found small at its start merges
    without a final code review; a spec and a plan are written around an outgrown attempt's code.
- **Approved by:** Mariusz, merge of <request link>
- *Rationale:* base text kept, then: "A small change that leaves the foundation unchanged gains
  nothing from a design, a spec and a plan, so one agent makes it from the task, while the checks on
  the finished change and the final review stay (WAY-13); a change that outgrows that finding starts
  again rather than having a spec and a plan written around partial code, and the agent's report
  passes on what it learned without the shape of its code."
- *Rejected:* base text kept, then: "; a separate skill for small tasks — two skills would hold the
  same rules of the record, the request and the return step, while size only lightens one process
  (WAY-13); an outgrown attempt kept and completed — a spec and a plan would be written around
  partial code; the agent of an outgrown attempt writing the spec and the plan — the spec would carry
  the shape of the abandoned code; a task once made by one agent finishing that way whatever it grows
  into — the grown change would merge without the design it turned out to need." The reason in the
  last item is the agent's: the task rejects the option without stating one (D13).

Meaning sentence for the request (Polish): "Metody Superpowers obowiązują w pełnym cyklu; małe
zadanie bez zmiany fundamentu robi jeden wykonawca, od testów tam, gdzie zmienia zachowanie, z jednym
końcowym przeglądem całości, a zmiana, która przerośnie tę ocenę albo dotknie fundamentu w sposób
wymagający otwartego wyboru, zmiany znaczenia zatwierdzonej decyzji, sprzeczności z wpisem lub
inwariantu albo jego testu, jest odrzucana i zaczyna się od nowa od świeżego projektu z raportem
wykonawcy bez kodu."

### 7.3 Dependent entries

- `foundation-change-path/1` (`foundations/invariants.md`): sentence unchanged — re-read against the
  new WAY-13, it still names the path WAY-13's foundation analysis chooses, and the light cycle is not
  such a path (section 8, row 1). *Derives from* becomes `WAY-13@97b17d59`, or WAY-13's fingerprint
  as finally worded (WAY-31). Version stays 1: a renewed link does not raise it (WAY-31 *Rejected*), and with no main
  branch every entry stays at version 1 (`elements/common/rules.md`, "Version"). Written through
  `record-invariant` (record-decision step 4.4).
- No decision carries `WAY-13@` or `WAY-125@`; no test, code comment or document does (searched the
  whole worktree for `WAY-13@`, `WAY-125@`, `WAY-13/`, `WAY-125`, `foundation-change-path`).
- Glossary, part map, environment facts: no change (section 8).

## 8. Collision search (WAY-33)

Whole foundation read for the task's words (size, path, spec, plan, review, executor, agent,
implement-task, foundation step, return step) and every decision whose *Scope* holds `task-cycle`.

| Entry | What it says | Finding | Resolution |
|---|---|---|---|
| `foundation-change-path/1` | "No change that, against {fork-point}, alters a foundation entry runs on the path for tasks that leave the foundation unchanged." | Point 3 keeps a light change that touches the foundation on the light way. If the light way were one of WAY-13's paths "for tasks that leave the foundation unchanged", that change would break the invariant. | No collision under D1: the light cycle is not a WAY-13 path; WAY-13 keeps "paths" for the foundation route, and the touch re-records the route as changed and runs that route's rules (element skill with search and guards, one WAY-10 assessment, meaning sentence in the request). The required outcome of point 3 is unchanged. The invariant needs only its fingerprint renewed (7.3). |
| WAY-13/1 sentence 3 | "A task's size serves only as a signal to split it" | Contradicts point 4. | Not a collision between two decisions (WAY-25): the task changes WAY-13 itself. Edited in place before `main` (guide, WAY-07). The approved task document orders the change (point 4), so it is the approver's answer WAY-30 and WAY-114 ask for and no question precedes the request (section 7, "Ground"); Mariusz re-accepts its meaning at the merge. |
| WAY-13/1 *Rejected*, *Verification* | "the path chosen by size"; violates: "a task gets the heavier path because of the number of lines it changes" | The first stays true under D1 (size never chooses the path). The second would now condemn the full cycle for a large task. | *Rejected* kept; the violates example rewritten (7.1). |
| WAY-125/1 | methods "apply only to a ready task run through `implement-task`" | Requires all methods for every task. | Changed by point 5 (7.2). |
| WAY-01/1 | a task that sets out to change the foundation does so in its foundation step, and the code follows | A light task does not set out to; its touch is found during implementation. | No collision: the entry is written before the code that depends on it continues; nothing is left for a later task. |
| WAY-03/1, WAY-69/1 | invariant tests read-only during implementation; sentence, check and code from three agents | The executor would write code and entry. | Excluded: a touch writing an invariant or invariant test is not simple (3.3) and switches. Return-step checks keep their own agents (step 11). |
| WAY-10/1 | one independent assessment of a foundation change | Point 3 asks for one assessment. | The touch's entry joins the one assessment of step 11; no second assessment. |
| WAY-11/1, WAY-126/1 | every task ends with the return step; a projected entry enters in the foundation step | — | Return step unchanged on the light cycle. A task with a projected entry has a foundation step, so fails finding 1 and takes the full cycle. |
| WAY-30/1 | a decision change a task needs is written into the task's plan | The light cycle has no plan. | A task that needs a decision changed fails finding 1. A contradiction found during light implementation: aligning or dropping the change stays light; a new wording changes an approved decision's meaning, so is not simple and switches. |
| WAY-25/1 | an unrecorded collision stops the work | — | None remains after 7.1–7.2; WAY-125 gains `derives from WAY-13` (D10). |
| WAY-36/1 | a rule that binds after the merge enters the log | The switch-and-discard rule binds every later task. | Carried in WAY-125's first sentence (D9); the step-by-step mechanics stay in the skill. |
| WAY-45, WAY-48 | critical-flow tests on every change; adversarial checks at a trust boundary | — | Kept: step 10 runs in full on the light cycle. |
| WAY-100/1 | a borrowed method binds only through a decision naming it and where it applies | The light cycle uses three borrowed methods. | Named in WAY-125 (7.2). |
| WAY-114/1 | a question to the human only without a recommendation or when an approved decision's meaning changes | — | Such a touch is not simple (3.3). |
| WAY-47/1 *Rationale* | "a part missing from it sends a change down the light path" | "light path" there means checks less sharp. | No clash under D2: the skill says "light cycle". No edit. |
| WAY-95/99, glossary | a word in a binding part with an unusual or second meaning takes an entry | A label such as "simple and obvious" in WAY-125's binding part would carry a meaning (no invariant or invariant test) a reader of the field would not give it. | WAY-125's binding sentence states the four conditions themselves, not the label; the label stays in the skill only, defined there by the same four conditions. "Light cycle" stays in the skill. "Foundation step", "return step" and "invariant test" keep their glossary meanings (the touch is not called a foundation step). No glossary change; a glossary entry for the label was rejected — one decision would use it, and an entry costs a term and its guard for one sentence. |
| part map `task-cycle` | responsibility: "the steps a task runs through and how sharply a change is checked along them" | Still true. | No change. Failure modes are recorded by a human (WAY-46); the cycle's return step may propose one. |
| `project-level/task/template.md`, `project-level/task/skill/SKILL.md` (not foundation) | "the cycle's record holds the implementation plan"; "The cycle's plan chooses how" | On the light cycle there is no plan; the executor chooses and the record holds the choices. | No edit (D11): the wording is loose, not wrong in effect; a process remark in the record. |

## 9. Choices (for the orchestrator to rule; each provisional)

| ID | Choice | Alternative rejected | Cost if wrong |
|---|---|---|---|
| D1 | The light cycle is a lighter preparation inside WAY-13's foundation route, not a WAY-13 path. | Make it a WAY-13 path chosen by foundation and size: the invariant `foundation-change-path` then needs a reworded sentence and an exception for point 3, and WAY-13's "the path chosen by size" falls. | Low: if Mariusz prefers the light way as a path, WAY-13's wording and the invariant change in a later edit; the skill's steps stay. |
| D2 | English names "light cycle" / "full cycle"; the Polish request writes "lżejsza ścieżka (light cycle)" at first use. | "light path" / "full path": clashes with WAY-13's "paths" (size would seem to choose a path) and with WAY-47's "light path"; needs a disambiguating sentence and a WAY-47 rationale edit with a moved *Approved by*. | Low: a rename in two files of `task-cycle/`. |
| D3 | The ten minutes and "very large / very many files" live in the skill; WAY-125 says "small enough for one agent to make from the task alone". | Numbers in the binding sentence: every tuning would re-open the decision. | Low: if the threshold should bind, a later edit of WAY-125. |
| D4 | "Simple and obvious" has four stated conditions (3.3), invariants and invariant tests excluded; WAY-125 states the conditions, the skill keeps the label defined by them. | Leave it to judgment alone — rulings vary between cycles; allow invariants on the light cycle — needs extra agents mid-implementation (WAY-03, WAY-69), which is the full cycle's machinery. | Low: some small tasks switch when they could have stayed; time only. |
| D5 | The executor returns on any foundation touch; the orchestrator rules; the executor writes the entry through the element skill. | The executor judges alone — the judgment of point 6 is the orchestrator's; the orchestrator writes the entry at the return step — code that needs the entry (a guard, the part map) fails its checks until then. | One round trip per touch. |
| D6 | One `requesting-code-review` of the whole change, the frozen task as requirements; executor fixes; same reviewer re-reads the fix range once. | No re-review — a fix lands unreviewed; a second fresh reviewer — two reviews, against point 1. | One extra short review pass. |
| D7 | Switch window: during implementation and review-fix. After the request opens, "Correction after review" applies unchanged. | Switch at any time including corrections — undefined against an open request. | A light request whose correction grows large has no switch rule; the human sees it at the request. |
| D8 | Discard by resetting the task branch to the recorded base commit; record the attempt's last commit (historical, not a link to follow) and file names. | A new branch — leaves a dead branch; keeping the attempt on a ref — the code stays reachable to later agents. | Low: the commit stays in the reflog until it expires. |
| D9 | The switch-and-discard rule enters WAY-125's binding sentence. | Skill only — WAY-36 puts a rule binding after the merge in the log, and the level-2 example could not cite it. | A longer sentence. |
| D10 | WAY-125 gains `derives from WAY-13@<fp>`. | No link — a later WAY-13 change would not flag WAY-125 (WAY-31). | One more fingerprint to keep. |
| D11 | No edit to the project-level task template or skill. | Edit "the cycle's plan" there — outside the task's parts. | A reader may assume every cycle has a plan; harmless. |
| D12 | The ten minutes are the orchestrator's estimate at the start and the executor's judgment while working, not a timer. | A measured limit — no tool measures an agent's working time today. | Some tasks overrun before switching. |
| D13 | WAY-125's *Rejected* gives an agent-written reason for "once light, always light". | Leave the item out — later agents would propose it again. | Mariusz may reword it at the merge; the request names it. |
| D14 | Fixes after review go to the same executor; where the harness cannot resume one, a fresh executor on the same branch with the task and ruling. | Always a fresh executor — loses the executor's working knowledge. | None beyond context cost. |
| D15 | "Correction after review" unchanged for a light-cycle request. | A light-specific correction rule — not asked. | As D7. |

## 10. Answers to the questions carried to the cycle

1. **Which adopted Superpowers methods does the light cycle use?** `test-driven-development` for
   behaviour changes (the same rule as the full cycle); `requesting-code-review` once for the whole
   change, with the frozen task as its requirements; `finishing-a-development-branch` only as step 12
   already uses it (request preparation without the integration menu). Not used:
   `brainstorming`, `writing-plans`, `subagent-driven-development` (it needs a plan and reviews per
   plan task). After a switch, all six, as on the full cycle.
2. **How is the partial implementation discarded, and what of it stays in the record?** Section 3.4:
   the task branch is reset to the recorded base commit after the attempt's last commit and file names
   are recorded; the record keeps the `## Cycle` lines, the Events rows, the executor's reports and
   the attempt's choice rows marked as discarded; no code or diff.

## 11. Verification of this task's change

`task-cycle/` holds no tests, so the skill and record template are checked by reading only; guards
run with `--merge-onto none` leave relation and link fingerprints unchecked.

1. `python -B gate/run_tests.py gate` — critical-flow tests (WAY-45), against the baseline (96 OK).
2. `python -B gate/run_tests.py elements/decisions` and `python -B gate/run_tests.py
   elements/invariants` — the parts whose foundation files change; baselines 169 and 233 OK.
3. `python -B gate/run_tests.py task-cycle` — expected "NO TESTS RAN"; recorded as unchecked.
4. `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto
   none --record .runs/decisions.jsonl`, `python -B elements/invariants/format_guard.py
   foundations/invariants.md --base none --merge-onto none --record .runs/invariants.jsonl` and
   `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none
   --record .runs/glossary.jsonl` — compare errors, warnings and `unchecked` lines with the baseline
   (decisions 0/5 warnings/5 unchecked, invariants 0/0/3, glossary 0/0/5, all on c64a607); nothing
   new expected.
5. Fingerprints by hand, since step 4 leaves them unchecked: write each changed binding paragraph to
   a UTF-8 file and feed that file's bytes to `python -B relation-model/fingerprint.py` (for example
   `python -B relation-model/fingerprint.py < way13.txt` in Git Bash — never a string piped through a
   non-UTF-8 console, since the wording holds em dashes); expected `97b17d59` for WAY-13 and
   `68b2d563` for WAY-125 as worded in section 7. Then search the whole worktree for `WAY-13@` and
   `WAY-125@`; every carrier holds the computed value.
6. Diagnostic, recorded as such and never as a pass: the decisions and invariants guards with
   `--merge-onto c64a607`, run first on c64a607 itself and then on the task branch, so only lines that
   differ are read. They exercise the relation and link fingerprint checks; differences expected from
   the in-place edits of WAY-13 and WAY-125 are named, anything else is a finding.
7. Acceptance criterion (section 5): read `git diff c64a607 -- task-cycle/skill/SKILL.md` in full and
   confirm that every change met by a task failing the rule is one of those listed there.
8. The cycle's own code review (step 10) and its one independent assessment of the foundation change
   (step 11, WAY-10).

## 12. Out of scope

`agent-instructions/README.md` (the task keeps the guide unchanged); the project-level task template
and skill (D11); `installation/` (it names the skill only); any change to step 12's record commits,
the foundation step, or "Correction after review".
