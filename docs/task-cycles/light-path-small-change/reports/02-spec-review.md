# Spec review: light cycle for a small change (implement-task, step 7)

Reviewer: spec reviewer (general-purpose, Opus 5.5). I did not write the spec. Inputs: `spec.md`,
`task_frozen.md`, and the repository at c64a607 (`task-cycle/skill/SKILL.md`,
`task-cycle/record_template.md`, `agent-instructions/README.md`, `foundations/decisions.md`
(WAY-01, 03, 05, 07, 10, 11, 13, 14, 25, 30, 31, 33, 36, 44–48, 69, 95–99, 100, 113, 114,
124–126, and the binding sentences of every other decision whose *Scope* holds task-cycle: 09, 16,
21, 26, 27, 28, 34, 37, 38, 51, 55, 57, 62, 63, 65, 68, 82, 89, 101, 102, 103, 106, 120),
`foundations/invariants.md`, `foundations/glossary.md`, `foundations/part_map.md`,
`elements/decisions/template.md`, `elements/decisions/skill/SKILL.md`, `elements/common/rules.md`,
`elements/decisions/format_guard.py`). Calibration: Superpowers 6.4.1
`spec-document-reviewer-prompt.md`. I flag only what would cause real problems; everything else is
under Recommendations.

## Spec Review

**Status:** Issues Found

All three issues are small fixes to the text. None of them changes the design. Once they are fixed,
the spec is ready for `writing-plans`.

---

## Issues

### Issue 1: WAY-125's new binding sentence requires test-first for every light change, but the skill and the spec require it only for behaviour changes

- **Section:** 7.2 (binding sentences, Verification, meaning sentence), compared with 3.2 step 1 and 4.3.
- **Evidence:**
  - `spec.md:323` (proposed WAY-125): "that agent then makes it test-first, one independent final
    code review covers the whole change".
  - `spec.md:341–343` (Verification complies): "a task found small at its start … is made
    test-first by one agent from the task".
  - `spec.md:363` (Polish meaning sentence): "małe zadanie bez zmiany fundamentu robi jeden
    wykonawca od testów".
  - `spec.md:73–74` (3.2 step 1): "uses Superpowers `test-driven-development` for behaviour changes
    (the same rule as the full cycle)". The skill text at `spec.md:168` says the same, and so does
    the base skill at `task-cycle/skill/SKILL.md:137` ("Have implementers use
    `test-driven-development` for behavior changes").
- **Why it matters:** The task's own example of a light task is a copy change (`task_frozen.md:22`).
  Under the proposed binding sentence, a copy change made without a failing test first violates
  WAY-125. Under the skill, it is correct. The plan would write a decision that contradicts the
  skill it governs. A level-2 check of WAY-125 would then condemn exactly the tasks the light cycle
  exists for. The alternative is that an executor writes pointless tests to satisfy the decision,
  which goes against point 1's intent. The base WAY-125 avoids this because it only *adopts*
  "test-first implementation" as a method, and the skill says where it applies.
- **What has to change:** Qualify the clause in all three places. For example: "that agent then
  makes it, test-first where it changes behaviour, …". Alternatively, drop "test-first" from the
  light clause, since sentence 1 already adopts the method. Make the matching edit to the complies
  example and the Polish meaning sentence. Recompute the WAY-125 fingerprint (nothing carries
  `WAY-125@` today, so no dependent changes).

### Issue 2: "Simple and obvious" enters WAY-125's binding part, but its operative meaning lives only in the skill, and the collision table says no new term enters a binding part

- **Section:** 7.2 binding sentence; 8, row "WAY-95/99, glossary"; 3.3.
- **Evidence:**
  - `spec.md:324–325`: "a change that proves too large for that agent, or touches the foundation in
    a way that is not simple and obvious, is discarded".
  - `spec.md:401`: "No new term enters a binding part ("light cycle" stays in the skill)".
  - `spec.md:98–105`: "simple and obvious" means four conditions, including "it writes or changes
    no invariant and no invariant test". A reader of the field would not take that from the plain
    words. A one-line invariant that the task obviously requires is "simple and obvious" in the
    ordinary sense.
  - WAY-95 (`foundations/decisions.md:2562–2566`): a word in a binding part whose use "carries a
    meaning a reader who knows the product's field would not give it" takes a glossary entry.
    WAY-05 (`decisions.md:139–145`): "what a decision forces on later work stands in a binding
    sentence or a field, never in prose".
- **Why it matters:** WAY-125's level-2 check compares a cycle with the decision. The decision
  alone cannot tell whether a light cycle that wrote an invariant should have been discarded. The
  rule that decides it binds every later task but sits only in a skill, which a product can read
  differently from the log. The collision table's statement is also factually wrong, so the WAY-33
  search record the plan copies from it would be wrong too.
- **What has to change:** Pick one of these and record it as a choice:
  - (a) Put the operative content in the binding sentence instead of the label. For example: "…
    or needs a foundation change that the task's required outcome does not settle, that changes
    an approved decision's meaning, or that writes an invariant or an invariant test, is
    discarded …".
  - (b) Keep the phrase and add a glossary entry through `record-glossary-term`. The glossary would
    then join the foundation change and the WAY-10 assessment.

  Either way, correct row "WAY-95/99" in section 8. Option (a) is cheaper and keeps the glossary
  untouched. Watch the sentence length (see Recommendation R1).

### Issue 3: The spec's ground for changing two approved decisions cites WAY-30's plan, but WAY-30 requires the decision's approver to approve that plan

- **Section:** 8, row "WAY-13/1 sentence 3"; 7 (preamble).
- **Evidence:**
  - `spec.md:387`: "the change the task needs is stated in the task and goes into the plan (WAY-30);
    Mariusz re-accepts its meaning at the merge."
  - WAY-30 (`decisions.md:818–819`): "A change to a decision that a task needs is written into the
    task's plan and approved with it by the decision's approver." In this cycle, the orchestrator
    approves the plan only provisionally (`SKILL.md:109`).
  - The skill's foundation step (`SKILL.md:124–126`): "Ask the human before the request only where
    you have no recommendation or an entry would change the meaning of an approved decision,
    through a blocked draft request holding the question." WAY-114 (`decisions.md:3172–3173`) says
    the same, and its violates example (`decisions.md:3184–3185`) is "an entry changes the meaning
    of an approved decision without a question."
- **Why it matters:** Both entries change the meaning of approved decisions (`spec.md:258`). Read
  literally, the skill's foundation step would make the orchestrator stop this cycle with a
  blocked draft request. Alternatively, the request would show a meaning change with no recorded
  question, which is WAY-114's violates example. The real ground exists, but the spec does not name
  it: Mariusz approved the task document, which orders both meaning changes (points 4–5) and
  answers the questions about them (`task_frozen.md:52–61`). The WAY-10 assessor and Mariusz will
  look for that ground.
- **What has to change:** In section 7 or in row "WAY-13/1 sentence 3", state that the approved task
  is the approver's answer that WAY-30 and WAY-114 require. Point 4 covers the WAY-13 change; points
  5–6 and the settled questions cover the WAY-125 change. State therefore that no pre-request
  question is needed. Then list each element of the proposed wordings that goes beyond the task's
  words, so the request can show it to Mariusz as the agent's wording rather than his:
  - WAY-13 sentence 1 now reads "sets the path that merges its change and how sharply that change
    is checked". This rewording is necessary, because "never its size, sets its process" would
    contradict point 4.
  - "never the outcome it has to reach" restates sentence 2.
  - The switch-and-discard clause in WAY-125 (D9, from point 6).
  - The WAY-125 → WAY-13 relation (D10).
  - The agent-written *Rejected* reason (D13).

  Keep the rest of the row.

---

## Checks that found no concern

### 1. Missing requirements: none

| Task item | Covered in the spec |
|---|---|
| Point 1: one executor, task in the prompt, no spec or plan, whole change | 3.2 step 1; 4.3 first bullet |
| Point 1: same checks as the full cycle (whole gate, checks for what the change touches, e.g. trust-boundary input) | 3.2 step 3; 4.3 third bullet ("run step 10 in full"); row WAY-45/48 |
| Point 1: one review of the whole | 3.2 step 3; D6. A re-read of the fix range by the same reviewer still counts as one review. |
| Point 2: entry rule (foundation unchanged, ~10 min, no very large or very many files) | 3.1; 4.3 first paragraph; D3, D12 |
| Point 3: simple touch stays light, goes through the element skill and one WAY-10 assessment; non-obvious touch switches | 3.2 step 2; 3.3; 3.4; 4.3 second bullet |
| Point 4: WAY-13 change | 7.1 |
| Point 5: WAY-125 change, rest unchanged | 7.2. Sentences 2 and 3 are verbatim. |
| Point 6: orchestrator judges at start in the same analysis and records reasons; executor returns; report without code or diff; attempt discarded; fresh designer gets the report; full cycle from scratch | 3.1, 3.4; 4.2, 4.3 last paragraph, 4.4; section 6 |
| Acceptance criterion | Section 5, with a reading check in 11.7 |
| Carried question 1 (which Superpowers methods) | 10.1 |
| Carried question 2 (how to discard, what stays in the record) | 3.4, 10.2 |

### 2. Invented behaviour: all of it is a necessary consequence or acceptably small

| Addition | Classification |
|---|---|
| Re-recording the foundation route as "changed" on a simple touch (3.2 step 2) | Necessary: needed by the invariant `foundation-change-path/1` (`invariants.md:256–258`) together with point 3. |
| Four conditions for "simple and obvious" (3.3, D4) | Necessary interpretation of point 3. The invariant and invariant-test exclusion follows from WAY-03 (`decisions.md:73–77`) and WAY-69 (`decisions.md:1916–1918`). Where these conditions live is Issue 2. |
| The executor returns on any touch and the orchestrator rules (D5) | Necessary: point 6 makes the judgment the orchestrator's. |
| Same reviewer re-reads the fix range once (D6) | Mild growth. It matches how the full cycle's review loop treats fixes. |
| Switch window limited to implementation and review fixes; "Correction after review" unchanged (D7, D15) | Necessary scoping. Without it, the switch is undefined against an open request. |
| Reset to the recorded base commit (D8) | Answer to carried question 2. |
| Switch rule in WAY-125's binding sentence (D9) | Necessary under WAY-36 (`decisions.md:1004–1006`): the rule binds every later task. |
| WAY-125 `derives from WAY-13@…` (D10) | Small growth, justified by WAY-31 (`decisions.md:849–854`). It lets a later WAY-13 change flag WAY-125. |
| Agent-written reason in WAY-125 *Rejected* (D13) | Small growth. Prose only, and it is named for the request. |
| Fresh-executor fallback (D14) | Operational only. |
| Request names the cycle and its reasons (4.6); record template `Cycle` line and section (section 6) | Necessary: point 6 requires the reasons to be recorded in the cycle record. The request line follows WAY-125's "show provisional choices in the request". |
| New front-matter description (4.1) | Necessary: otherwise the description would say every task goes through design and planning. |

### 3. Contradictions with the foundation (beyond Issues 1–3)

- **`foundation-change-path/1`:** The spec's claim holds. Under D1, the light cycle is not one of
  WAY-13's "paths". A simple touch re-records the route as changed and runs that route's rules:
  element skill, whole-foundation search, guards, one assessment, meaning sentence. So no change
  that alters an entry runs on the unchanged-foundation path. The base cycle already writes entries
  after the start analysis (return step, `SKILL.md:150–153`; WAY-30's mid-implementation proposal),
  so a later re-recording does not conflict with WAY-13's "analysis at the start … settles". The
  only change the invariant needs is its *Derives from* fingerprint. Version 1 is right: WAY-31
  *Rejected* (`decisions.md:880`) says "a renewed link raising the invariant's version", and
  `elements/common/rules.md:121–123` keeps every entry at version 1 while there is no main branch.
- **WAY-13's size sentence:** The new sentence 3 matches point 4 ("spec, plan, liczbę agentów …
  nigdy sprawdzeń po zmianie"). Rewording sentence 1 is necessary (see Issue 3). Dropping the
  review loop on the light cycle does not breach "never less [sharply] than the map computes",
  because the new sentence 3 counts the number of agents as preparation, not as checks on the
  finished change. The task's settled answer (`task_frozen.md:55`) explicitly accepts this, and it
  rejects excluding irreversible and trust-boundary changes. Fingerprints: the new wording is
  `97b17d59` and the base is `c6b33aa9`. I recomputed both with `relation-model/fingerprint.py`
  from UTF-8 files, and both match the spec. The violates example the spec removed ("heavier path
  because of the number of lines") would now condemn the full cycle for a large task, so removing
  it is right.
- **WAY-30:** Apart from Issue 3, row WAY-30 is consistent. A task needing a decision change fails
  finding 1. Mid-implementation, aligning or dropping the change stays light, and a new wording
  switches. This is stricter than WAY-30 requires, never looser.
- **WAY-36:** The switch rule is carried in WAY-125 (D9). The step mechanics stay in the skill.
  Consistent.
- **WAY-47:** "light path" in its *Rationale* (`decisions.md:1304`) means a change that escapes a
  flow's checks. The skill's term is "light cycle" (D2) and no binding part uses either phrase, so
  there is no clash and no edit is needed. The only other occurrence is a test fixture string
  (`elements/part-map/test_format_guard.py:76`), which is unrelated.
- **WAY-03 / WAY-69:** Excluding invariants and invariant tests from a light touch keeps the
  executor from writing a sentence, a check and the code together. Checks written by the return
  step keep their own author and reviewer (step 11 unchanged). Consistent.
- **WAY-10:** The touch's entry joins the single step-11 assessment, so there is no second
  assessment. Consistent with "a settlement … does not reopen its assessment".
- **Other task-cycle decisions** (09, 16, 21, 26, 27, 28, 34, 37, 38, 51, 55, 57, 62, 63, 65, 68, 82,
  89, 101, 102, 103, 106, 120, plus 11, 44–48, 100, 124, 126): I read the binding sentences and
  found no collision. WAY-16's single gate command and WAY-45's flow tests on every change are kept
  by "step 10 in full". WAY-120 critique equals WAY-10 assessment, unchanged.
- **Glossary and part map:** Apart from Issue 2, "foundation step" and "return step" keep their
  glossary meanings. The responsibility of part map `task-cycle` ("the steps a task runs through
  and … how sharply a change is checked along them") stays true.
- **Decisions template:**
  - *Binding-sentence count:* `count_sentences` from `elements/decisions/format_guard.py` gives 3
    for the proposed WAY-13 and 3 for WAY-125, within the template's 1–3 (`template.md:92`).
  - *Forbidden words:* no *should*, *will* or RFC 2119 capitals.
  - *Fields:* all present. *Change* stays `new decision` (version 1, edited in place). *Approved
    by* becomes `Mariusz, merge of <request link>`, the agent form (`template.md:275–280`); this is
    right because the meaning changes (WAY-07). *Rationale* and *Rejected* name no file, script or
    measured count.
  - *Relations format:* valid. On c64a607, `derives from WAY-100@e7a74a18` passes the decisions
    guard with `--merge-onto c64a607`.
  - *Length:* the template sets no length limit. See R1.
- **Spec's own quotations of base text** (4.1–4.6, section 6): every quoted base passage matches
  c64a607 verbatim, and the insertion point of 4.3 exists (`SKILL.md:83–84`).

### 4. Ambiguity and placeholders

There are no `TBD` or `TODO` markers. `<request link>` and the template's `<…>` slots are the
intended placeholders. The judgment calls ("about ten minutes", "very large / very many") are
deliberate and are recorded with reasons (D3, D12), as the task's "reguła kciuka" asks. Issue 1 is
the one ambiguity that would let a planner build the wrong thing.

### 5. Can the verification run? Yes

- The guard flags in 11.4 exist on all three guards (`--base`, `--merge-onto`, `--record`).
- The diagnostic in 11.6 runs. On c64a607 I got:
  - decisions guard `--base none --merge-onto c64a607`: exit 0, 0 errors, 5 warnings (the passed
    check-by dates of WAY-03, 21, 52, 55, 69), 2 unchecked;
  - invariants guard `--base none --merge-onto c64a607`: 0 errors, 0 warnings, 1 unchecked.

  On the task branch, the in-place edits of WAY-13 and WAY-125 will make the copy comparison report
  differences. The spec already says to name those. The invariants guard's `--merge-onto` run
  checks the renewed `WAY-13@` fingerprint for real.
- Fingerprinting (11.5) works from a UTF-8 file (`cat file | python -B relation-model/fingerprint.py`).
- 11.3 is correctly expected to report "NO TESTS RAN".

---

## Recommendations (advisory, do not block approval)

- **R1. WAY-125 sentence length.** The proposed binding part is 230 words, and its first sentence is
  137 words. That is the second-longest binding part and second-longest sentence in the log, after
  WAY-09's 275 and 163; the base WAY-125 is 140 words. No rule caps length, but WAY-05's rationale
  (`decisions.md:166–168`) wants "what binds stays short and checkable". "and the request is
  prepared as for any task" adds nothing that the method list and sentence 2 do not already say,
  and can go. Fixing Issue 2 by option (a) lengthens the sentence, so trim when you fix it.
- **R2. Fingerprint input encoding (11.5).** Say to pipe the bytes of a UTF-8 file. The new WAY-13
  wording has em dashes, and piping a string from Windows PowerShell 5.1 (or printing through a
  cp1252 console) feeds different bytes and gives a wrong fingerprint. I hit this while checking:
  `fingerprint.py` raised UnicodeDecodeError.
- **R3. Glossary guard baseline (11.4).** The cycle record has no glossary baseline. On c64a607,
  `elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` gives
  0 errors, 0 warnings, 5 unchecked. Record it as the baseline before the post-change run.
- **R4. Step 13 (4.6).** "after a switch, its reason and the executor's report" could be read as
  pasting the report into the request. Say "a link to the executor's report", since the request
  already links the record by SHA.
- **R5. Step 4 (4.2).** "record the choice with the reason for each of its findings". For a task
  that plainly fails finding 1 (for example, one that changes the foundation, like this one), say
  whether the other two findings still need reasons. Recording only the failing finding is enough
  for the full cycle.
- **R6. Log form for 7.1 and 7.2.** In the log, *Rationale* and *Rejected* are italic paragraphs
  after the field list (`template.md:40–41`), not list items as the spec shows them. The plan
  should keep the log's form.
- **R7. D8.** The recorded "last commit" of a discarded attempt becomes unreachable once the reflog
  expires. The record should call it historical, not a link to follow.
