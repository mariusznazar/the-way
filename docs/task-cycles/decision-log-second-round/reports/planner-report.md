# Planner report — decision-log-second-round

Status: done with concerns.

- Plan: `.runs\task-cycles\decision-log-second-round\plan.md` (23 slices, 8 foundation-entry rows F1 to F8).
- Final size report: `.runs\task-cycles\decision-log-second-round\plan-size.md` — every slice `fits` (largest: Slice 9, about 90 700 tokens; Slice 13 changes 10 files).
- Checks run: `python -B task-cycle/slice_size.py` exit 0. Nothing else was run: no code, no test, no gate. A script of mine confirmed that every one of the 537 references to a withdrawn number in the 111 files outside `foundations/` appears in the plan (0 uncovered) and that the line of each really holds the number (0 mismatches).

## What the plan does, in one view

- Every edit of `foundations/` (the log, three invariants, one part-map row, one glossary line) is a foundation entry, written by the agent of *Foundation entries* before Slice 1. Reason: `foundations/decisions.md` is 971 571 characters; `slice_size.py` reads a file of *Change* whole, so a slice that changes it measures about 389 000 tokens against the limit of 150 000 and can never fit (the previous round's plan for the log, `co-trafia-do-dziennika-decyzji`, did the same: entries by one agent before slice 1).
- Slices change only files outside `foundations/`: Slice 1 (decisions template and `read.md`: To do 5 and 6, plus the reason of WAY-32), Slice 2 (spec step: To do 6), Slices 3 to 23 (the withdrawals, cut by directory; each file in exactly one slice).
- Order: rule changes first (F1, F2 in the foundation entries; Slices 1, 2), the `derives from WAY-100` pattern before any withdrawal (F3 before F4), then withdrawals by directory. None of the 24 + 12 entries of F3 is withdrawn by F4, so no row edits an entry another row withdraws; where F3 and F6 edit the same entry (WAY-121, 128, 142, 203, 204, 212, 228, 268, 273, 280) the same agent does both.
- Withdrawn: 143 numbers: 111 of group A, 26 of group C, 6 of group D. Group D numbers go to their target as successor (WAY-358 to WAY-357, which leaves too). Not withdrawn: 4 entries returned to the human (below).

## Table against the log (the handoff's check)

All 331 identifiers of the table (A 115, B 29, C 26, D 6, E 2, F 153) exist in the log at `ec7929d` with exactly the question the table gives (0 mismatches). The log has 334 entries; WAY-374, WAY-375 and WAY-376 are not in the table and stay. WAY-374 has `derives from WAY-100`: it makes the number 24, not 23, and F3 holds it. None of the 23 named entries is in groups A, C, D, so no item of To do 4 is void by a withdrawal (the handoff expected some; none is).

## Entries to return to the human

Out of F4 and of every slice; the orchestrator keeps them in the log and says so in the request. Each is my judgment after reading the entry (the survey agents raised 5, I kept 4 and added 1).

1. WAY-263 (Which foundation mismatches are Important findings?) — its *Rejected* names the table's move as a rejected way: "leave the criterion only in the skill — the foundation would not hold it and a later change could remove it without contradicting an entry" (`foundations/decisions.md` lines 8469-8494). A withdrawal does the thing the entry rejected, with its reason; one sentence of reason cannot hold that.
2. WAY-294 (How does the cycle make sure its process remarks hold every item its stage reports give?) — `Relations: derives from WAY-260 · narrows WAY-344`; its last rejected way: "no exception at all, with WAY-344 unchanged — a reviewer who compares the script with WAY-344 would take it for a breach". WAY-344 binds every script of the-way; the entry is the only place that records the exception (WAY-25 asks for the precedence to be recorded in the entry that prevails); WAY-309 also `narrows WAY-294`. A skill sentence cannot carry a precedence over a decision.
3. WAY-295 (What does the cycle do with a listing of the remarks check that it holds wrong?) — `Relations: narrows WAY-294`; withdrawn while WAY-294 stays, it leaves an exception to a staying decision with no entry; it goes with WAY-294.
4. WAY-287 (What does a request put before the human for a decision?) — 111 lines, eight rejected ways with costs; WAY-289 `derives from` it and WAY-293 cites it; its *Rationale* says "WAY-274 counts on the human seeing them at the merge" (a staying entry relies on what this one says the request shows). The request template can state the rule, not that dependence in one sentence.

Raised by the survey and kept in F4 (the file can state each in one sentence; the review should read them against the entry): WAY-345 (three rejected ways of the cost scale; the one sentence is "a fixed scale the count can order; a widened list would break series of measures"), WAY-353 (a measure of the author's own register that the reader cannot open: the sentence takes the line-number reason and leaves the number out), WAY-354, WAY-366, WAY-259, WAY-333, WAY-343, WAY-348, WAY-352 (reason fits one sentence, entry priced).

Not decided here and affecting these four: their references stay as they are (the plan removes none of them, and `foundation_check.py` does not object, the entries stay in the log).

## To do 4: the lists of F3 (the survey's classification is a hypothesis; the entry decides)

Each entry was read whole by a survey agent (output `reports\planner-survey-adoptions.json`; 58 candidates: the 24 with the relation, every entry whose *Based on* quotes an outside source or whose text names an outside practice).
- (a) keeps the relation, pattern applied: WAY-121, 138, 142, 143, 144, 146, 147, 164, 256, 268, 270, 273, 280, 374.
- (b) gets the relation: WAY-167, 199, 203, 206, 212, 228, 229, 233, 236, 237 (the ten adopt without it).
- (c) loses the relation, source stays in *Based on*: WAY-128, 129, 130, 131, 132, 133, 137, 139, 140, 173. WAY-173 and WAY-140 are the ones I doubt (see question 3).
- (d) borderline, left without the relation unless told: WAY-204 (the criterion is WAY-203's), WAY-258 (follows a vendor guide's one-level-deep recommendation).
- Sentences the writer cannot write from the entry: `Based on` of WAY-138, 142, 143, 144, 146, 147, 164 names no source for the practice (a roadmap, vertical slices, an agent harness): the field takes `TODO — <what is missing>`, which the form of its field allows. *Leaves out* (what the practice does not bring) is missing in WAY-143, 146, 147, 164, 167, 199, 206, 212, 228, 233, 236, 268, 270, 273, 374 (and in 138); a bare `TODO` is not allowed in *Rejected*, so see question 1.

## Choices the plan took (also in its *Choices* table)

1. All log work in the foundation entries; slices touch no file of `foundations/`.
2. Checks of a withdrawal slice read the lines `foundation_check.py` prints for the slice's own files; exit code 0 is asked of Slice 23 only, because the log loses the numbers before the files do (the check reports a reference to a withdrawn number in any tracked file).
3. Slices cut by directory, not by group of the table: `product-guidelines/coding/template.md` alone carries 41 references to 14 entries of three groups.
4. The reason sentence is written in the file from the withdrawn entry's *Rationale* read at the base; the plan gives the place and the clause, not the text.
5. Where the survey found the rule elsewhere than the table's "Miejsce", the sentence goes where the rule stands: WAY-338 to `task-cycle/cycle_stages.py` (the table says `audit_count.py`, which only reads the times), WAY-112 to `project-level/skill/idea.md`, WAY-331 to the part-map entry (F8).
6. Seventeen references that lean on the number for meaning are rewritten, eleven repointed, three lines that are only the number deleted.
7. The spec step's question is a bullet of `task-cycle/spec/design.md`, "Settle the design".

## Concerns

- Order against the cycle skill: `task-cycle/skill/SKILL.md` step 9 dispatches the foundation entries before Slice 1, so between the foundation entries and the last slice `foundation_check.py` is red for the files not yet made, and a slice reads the withdrawn entries at the base (`git show ec7929d:foundations/decisions.md`; the ranges in *Read* are base lines). Withdrawing the entries after the last slice would keep every check green and the entries readable, but the cycle skill has no such step (question 4).
- One agent writes all log work: 143 withdrawals (each a row in the withdrawn list with its *Why*), 47 live entries edited for references, 36 pattern rewrites, 6 merges, 4 invariants. That is large for one handoff; the plan cannot split it (the skill has one agent for the plan's *Foundation entries*).
- The reason sentences in the plan are hypotheses of survey agents on 147 entries: "the file states no reason" was judged `no` for 128, `yes` for 13 (no sentence added), and not assessed for the 6 of group D; a sample of five matched, and the reviewer should read each added sentence against the entry.
- `elements/invariants/template.md:76` leans on WAY-56's complying/violating pair; Slice 6 states the pair in the template (it is an example, which a template may carry). The note of the survey is in the plan.
- Guidelines: the-way holds no guideline files of its own (the part map's `product-guidelines` part is the template of products; WAY-328 records the departure from the general coding and testing guidelines). I found no guideline for the-way's parts, so `product-guidelines/reading.md` selected nothing. The styleguide's order-of-work example does not apply (no screen).
- `product-guidelines/coding/template.md` says "a rule carries no reason: the reasons stand in the decisions it names" (lines 190-191) and has each rule cite its decision (lines 15, 190; SKILL.md:14); `product-guidelines/template.md` allows one sentence of reason for a rule with *Decision* `none` (the previous round's To do 4). Slices 13 and 14 add reasons to rules whose decision leaves, so the rule with the decision named in the template must read `none` and the sentence of reason may stand: the executor reads both templates; uncertain which lines of `coding/template.md` the previous round already adapted.

## Questions for the orchestrator, with proposed answers

1. *Rejected* where an entry of F3 says nothing of what the practice leaves out: the pattern wants the sentence, the field cannot read `TODO` (`elements/common/rules.md`: `TODO` only where the template gives it; `elements/decisions/template.md` gives *Rejected* only `none considered` and `unknown`). Proposed: leave *Rejected* as the entry has it and list those entries in the request under *Fix or let through* with the missing item, for the human to supply. Evidence: survey `planner-survey-adoptions.json`, field `leaves_out` = missing (15 entries). Cost of a wrong answer: a sentence invented from memory looks like a recorded choice (the task's own rule on `TODO`).
2. Borderline WAY-204 and WAY-258, and WAY-167 (names a table, says nothing of what it leaves out): proposed — 204 and 258 no relation, 167 the relation. Evidence: survey notes; WAY-204's criterion is WAY-203's.
3. WAY-173 and WAY-140 lose `derives from WAY-100` by the task's rule of answer 3 (no adopted practice named); the survey: WAY-173 "applies WAY-100 to the-way's own template, adopts none", WAY-140 "no outside practice at all". Forty-six entries stand on WAY-173. Proposed: follow the rule as the task gives it; confirm if the relation is read as "serves", not "adopts".
4. Order: dispatch the withdrawal rows (F4 to F8) after the last slice instead of before Slice 1 (checks green, entries readable)? Proposed: keep as planned unless the first slice's review finds the red checks a burden; the plan reads in either order, only the checks' wording changes.
5. Invariants whose only decision leaves (`project-definition-form`, `map-reference-target`): *Derives from* `none` (the rule stands in a template as a rule with no choice behind it, WAY-22) or the nearest staying decision (`map-reference-target` to WAY-02, whose *Verification* then names it, as the survey suggests). Proposed: `none` for the first, WAY-02 for the second; the foundation agent states its choice in its report.
6. The four entries of "Entries to return": proposed to keep them out of this round and to name the reason in the request (a precedence record, a rejected way that is the withdrawal, a dependence of a staying entry).

## Reaches beyond the dispatch

- `task-cycle/skill/SKILL.md` lines 370-450 (the dispatch of the plan's *Foundation entries*) and `task-cycle/skill/foundation_step.md`: to learn who writes the log and in what order.
- `git show 4d9174e:docs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md` and `plan-size.md`: the previous plan that edited the log, for its form (entries before slice 1).
- `elements/invariants/template.md` (grep on *Derives from*), `foundations/environment_facts.md` (greps by survey agents), `foundations/invariants.md` lines 84-94, 150-166, 205-216, 344-358, `foundations/part_map.md` lines 253-267, `foundations/glossary.md` line 5: for F8.
- `task-cycle/spec/SKILL.md` and `design.md` whole: for To do 6.
- `gate/run_tests.py` (head) and the directories that hold `test_*.py`: for the *Checks*.
- Fourteen read-only surveys by sub-agents (general-purpose, no write to tracked files): ten of the withdrawals by directory, four of the adoptions; their JSON is in `reports\planner-survey-withdrawals.json` and `planner-survey-adoptions.json`. Their claims are treated as hypotheses; I verified every reference line by script and read entries WAY-263, 294, 345, 353, 287, 295, 312, 09, 29, 100, 293, 19 myself.

## Working copies

No worktree and no clone. Scripts and the survey inputs and outputs stood in `.runs\planner\`; I kept in `reports\` what this report needs (`planner-survey-withdrawals.json`, `planner-survey-adoptions.json`, `planner-refs-by-number.txt`, `planner-refs-ranges.txt`) and removed `.runs\planner\`. Where the removal failed it is named below.

## Unread material

- `elements/common/way_of_working.md`: read by grep for references and the lines my survey agents quoted, not whole.
- `elements/common/skill/task_variant.md`: not read (To do 5 names `read.md`; the task's Context says `task_variant.md` already reads the questions but does not point to the rule, and it is not in To do 5).
- `elements/common/foundation_check.py`: read the docstring and the parts on withdrawn numbers and references (lines 1-140, 399-560); not the rest.
- `elements/decisions/template.md`: read through "Origin" and "Recovered decisions"; the section "Examples" not read.
- `foundations/part_map.md`, `foundations/invariants.md`: read by grep and at the lines named above, not whole.
- `foundations/decisions.md`: entries WAY-01, 02, 19, 29, 100, 293, 263, 294, 295, 287 (head and *Rationale*), 345, 353, 312, 09 read by me; the other withdrawn entries only through the survey agents (each read its entries whole); the log's earlier history (git log of `foundations/decisions.md`, the merged request #37, `f0b2130`) not read — the form of a withdrawal comes from the existing list of withdrawn numbers in the log.
- `product-guidelines/reading.md`, the guideline files: not read; the-way holds none for its own parts.
- `task.md`: lines 1-490 read whole; the note after line 489 not read, as the handoff says.

## Searches not found or unclear

- A guideline file for the-way's own parts: not found (none exists).
- Whether any test or script cites a withdrawn number by a line `decision:`: searched `git grep "decision: WAY-"`; the only decisions cited are WAY-03, 12, 375, 376 (none withdrawn or edited in its binding sentence).
- Where the rule of WAY-358 (what causes the correction line gives) stands: not found by the survey (it skipped group D); Slice 21 asks its executor to check `task-cycle/record_template.md`.
- Whether `installation/README.md:92` ("as WAY-309 and WAY-323 name them", a sentence that a product's invariant holds) is meant to name the-way's numbers in a product: unclear; the plan repoints to WAY-309 alone as the survey suggested.
- Whether a staying entry's `decision:`-held sentence changes: none of the 47 entries of F6 is held by a test.
