# Independent assessment — the agent's way to the running product (77c8a8b..0c1dfd5)

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product-assess` at `0c1dfd5`.
Line numbers below are of the files at `0c1dfd5`. Critic: fresh agent following
`elements/common/critique/SKILL.md`; diff and files only, no chronicle or author reasoning.

## What was read and run

- Whole: WAY-121, WAY-165, `project-technology-record/1`; related WAY-118, WAY-100, WAY-106,
  WAY-116, WAY-122, WAY-123, WAY-137, WAY-108, and the entries the new text cites: WAY-34,
  WAY-102, WAY-139, WAY-140, WAY-112, WAY-10, WAY-05, WAY-07, WAY-19, WAY-113 (heading), WAY-124.
- `elements/decisions/template.md`, `elements/invariants/template.md`, `elements/common/rules.md`,
  `foundations/glossary.md`, part `project-level` of `foundations/part_map.md`,
  `agent-instructions/README.md` (the pre-`main` route: edit in place, re-accept a change of
  meaning).
- Changed code, template, skills and tests whole: `project-level/readiness_check.py`,
  `project-level/definition_template.md` (Technology section), `project-level/technology/SKILL.md`,
  `project-level/skill/SKILL.md` step 0, `project-level/task/skill/SKILL.md`,
  `project-level/plan/skill/SKILL.md`, `project-level/lead/skill/SKILL.md`,
  `project-level/test_readiness_check.py`, `project-level/test_readiness_marks.py`,
  `project-level/test_plan_state.py`, `project-level/test_plan_state_invariant.py`,
  `project-level/plan_state.py` (lines 370–396), `task-cycle/skill/SKILL.md` step 10 and
  `elements/common/way_of_working.md` "Reading the foundation" for the moment of use.
- Ran: `python -B gate/run_tests.py project-level` — 269 tests, OK. Decisions format guard —
  0 errors, 7 warnings (two are the `merge of <request link>` placeholders of WAY-121 and
  WAY-165, expected before the request exists; the guard's own `MERGE_PLACEHOLDER` accepts them).
  Invariants format guard — 0 errors. Fingerprints recomputed with `relation-model/fingerprint.py`
  from the binding sentences at `0c1dfd5`: WAY-121 `d0b060e5`, WAY-137 `86b2a30d`, WAY-123
  `f3b45293`, WAY-118 `5af868b3`, WAY-100 `e7a74a18`, WAY-106 `63eddf70`, WAY-116 `afbcd2fa` —
  every relation and *Derives from* in the change carries the current value; all four
  `WAY-121@` references in `foundations/` are renewed.

## Observations

Weights: **high** — would mislead a reader or let the rule fail in a case it targets;
**medium** — the change carries text or code that another place already gives, or a binding
sentence says more than it needs to; **low** — wording, an edge case, or a note for later.

### A1 — WAY-121's third binding sentence carries the mechanism of when a tool runs (medium)

Checked: whether each binding sentence describes "a state that is to be true, concrete enough to
check" (WAY-05, `foundations/decisions.md:139-140`) and whether what it says is already settled
elsewhere.

Evidence: `foundations/decisions.md:3441-3444` — "a definition approved before the three were
required goes back to the step and through the readiness gate again once its product moves the
commit of the-way it pins and the readiness check first runs on it, as the refinement of a task of
its plan runs it."

- "once its product moves the commit of the-way it pins" restates WAY-34
  (`foundations/decisions.md:985-987`); the *Rationale* already cites it at :3485-3486.
- "the readiness check first runs on it, as the refinement of a task of its plan runs it" names
  one of four places that run the check: `refine-task` (`project-level/task/skill/SKILL.md:78-80`),
  `plan-project` (`project-level/plan/skill/SKILL.md:62-64`), `define-project` step 0
  (`project-level/skill/SKILL.md:59-61`) and the plan state reader
  (`project-level/plan_state.py:385`), which the lead skill names
  (`project-level/lead/skill/SKILL.md:38-39`). A binding sentence that picks one of them tells how
  the process's tools behave today, which WAY-05 keeps out of prose and does not ask into a binding
  sentence.
- "approved before the three were required" states the rule by its history. The invariant says the
  same as a state: "approved or not" (`foundations/invariants.md:2023`).

What would change: cut the sentence after "the readiness gate stops a definition whose list lacks
one of the three" to "approved or not, and such a definition goes back to the step and through the
readiness gate again." The *complies*/*violates* examples at :3458-3459 and :3463-3464 keep the
pin-move case as examples, which is where WAY-05 places it. The fingerprint changes; the four
dependents are renewed in the same change (they are already touched).

### A2 — Three skills restate the route the template and `define-project` already give (medium)

Checked: WAY-35 (`foundations/decisions.md:1014-1018`): a skill holds only the way of working
particular to it; a rule stands once in the template. Whether the new text in `plan-project`,
`refine-task` and `lead-project` adds anything to what each skill said before the change.

Evidence:
- Template: `project-level/definition_template.md:197-200` — the gate stops a list lacking a
  mark, an approved definition's too, and it goes back to `settle-technology` and the gate.
- `define-project` step 0: `project-level/skill/SKILL.md:63-67` — on that finding, go to step 6,
  then step 7, then the plan is checked again.
- Before the change each caller already said "a finding returns the definition to
  `define-project`" (`project-level/plan/skill/SKILL.md:63-64`; `project-level/task/skill/SKILL.md:80`;
  lead: "A changed definition follows step 5 below", `project-level/lead/skill/SKILL.md:37-38`).
- Added restatements: `project-level/plan/skill/SKILL.md:65-68`,
  `project-level/task/skill/SKILL.md:80-85`, `project-level/lead/skill/SKILL.md:38-42`. Each repeats
  the three mark strings, "approved before those three choices were required", and the route.
  The lead's "before any task of it becomes ready for cycle" is already in `define-project`
  (`project-level/skill/SKILL.md:49-51`).

What would change: cut the three additions; the pre-existing "a finding returns to
`define-project`" routes the finding to the one place that explains it. If one line is wanted so a
reader does not mistake the finding for a broken definition, keep the lead's, since the lead
reads the state reader's `definition` finding rather than running the check itself, and cut the
other two. Three copies of the mark strings are three places to change when a mark changes.

### A3 — The moment of use has no pointer to the three choices; independent tasks are outside the rule (medium)

Checked: who benefits and at what moment the rule acts; whether it acts in the case that prompted
it (an agent that "either leaves that check out or improvises a way to the product in the middle of
a task", `foundations/decisions.md:3476-3479`).

Evidence:
- The need arises in task-cycle step 10: "For visible behavior, verify it in the running product
  as well" (`task-cycle/skill/SKILL.md:339-340`). Nothing in the change names the three choices
  there or in the task document.
- The choices reach a task only by selection: `refine-task` selects "technology ... relevant to
  the stated task" for a source-only task (`project-level/task/skill/SKILL.md:76-77`), and the
  cycle's foundation reading selects decisions by *Scope* against touched parts
  (`elements/common/way_of_working.md:73-78`). A logs decision whose *Scope* names a part the
  task does not touch is not selected.
- An independent task "requires neither definition nor plan"
  (`project-level/task/skill/SKILL.md:77-78`). WAY-121 binds "every list" of a project
  definition; a product whose work runs as independent tasks before its first project has no
  settled way, and the *Rejected* of WAY-121 rejects the deployment skill as home for exactly the
  reason that "a product run on a developer's machine has no such guarantee" (:3502-3503) — the
  chosen home leaves the same gap for independent tasks.

What would change: this is not a cut; it is a gap the *Review when* of WAY-121 (:3465-3467)
would catch, and it is worth saying in the request. The cheapest closing: one clause in
`refine-task` naming the three choices among the decisions every task document carries, or a
sentence in the task-cycle step 10. Whether to do it in this change is the author's call; the
decision as written does not reach the moment it is for by its own text.

### A4 — WAY-121's *Rationale* names a source no reader of the repository can reach (low–medium)

Checked: source fidelity of every substantive claim. The claim about the lesson "Towards
Autonomous Product Development" (`foundations/decisions.md:3486-3491`): that it describes an
agent's way to the product through logs, interface and development data, and a hard limit (no
production database, no root access) that WAY-121 does not take.

Evidence: the title appears nowhere in the worktree (`grep -rn` over `*.md`); *Origin* reads
`none` (:3468). The template says *Origin* points to where the full reasoning lives
(`elements/decisions/template.md:260-265`) and WAY-100 asks a borrowing decision to name "what is
adopted, where it applies, and why" (`foundations/decisions.md:2790-2792`). The "what" and "why"
are in the *Rationale*; the "where it applies" is the step; but the lesson itself cannot be
checked against the claim from this repository. I could not verify the fidelity of the quoted
scope of the lesson, nor whether "development data" is its term or the author's.

What would change: *Origin* naming where the lesson lives (a URL or a file at a fixed commit), or
*Based on* quoting the sentence of it that gives the three. WAY-137 and WAY-139 also derive from
WAY-100 without a locatable source, so this is a pattern of the log, not a fault introduced here —
but WAY-121 is the first to name a source title and characterize its content.

### A5 — WAY-139 and the logs choice both settle how an agent reads the logs (low)

Checked: contradictions and duplicated settlements across current entries.

Evidence: WAY-139 binds the product's deployment skill to cover "how to read the logs"
(`foundations/decisions.md:4311-4313`); WAY-165 makes the logs choice ask "where the record of what
the running product does goes and how an agent reads it" (:5353-5354), settled as a decision of
the foundation. WAY-121's *Rejected* says why the deployment skill is not the home (:3501-3503)
but neither entry says that the deployment skill's item takes its content from the logs decision,
or which prevails when they differ.

What would change: not a contradiction today; one clause in WAY-165 ("the deployment skill's
account of reading the logs (WAY-139) follows the decision of the logs") would keep the two from
drifting. Low because WAY-139's check runs only on deploying tasks and both are level 2.

### A6 — WAY-165 gives no rule when every option of a choice is one the agent cannot use (low)

Checked: error when applied too widely.

Evidence: "the recommendation passes over it" (`foundations/decisions.md:5362`). Where a product's
only reachable logs are a vendor panel with no export, every option is passed over and the step
recommends nothing; `settle-technology` step 5 then forms a recommendation it cannot form
(`project-level/technology/SKILL.md:127-129`). The *Rationale* says the human "can still take it"
(:5400), which covers the case in effect but not in the binding sentence.

What would change: "where no option remains, the step recommends none and says so" — or leave it,
since WAY-123 already has the human choose and the table shows every option with its lack. Low.

### A7 — WAY-165 restates WAY-137's tie rule inside its binding sentence (low)

Checked: whether a binding sentence says what another decision already binds (WAY-19: a sentence
answered in passing stays in one place, `foundations/decisions.md:569-571`).

Evidence: `foundations/decisions.md:5362-5364` — "and the rule that settles a tie between places to
run by how well an agent works with them stays with the choice of a place to run." The relation
`narrows WAY-137` (:5369-5370) and WAY-137's own sentence already bound this; the clause marks the
boundary of the narrowing, which is what *Relations* and the binding area statement are for
(`elements/decisions/template.md:172-174` asks the prevailing decision to "state the area where it
prevails" — which the first clause "In each of the three ... even where the option is a place the
product runs" already does).

What would change: cut the clause; the *Rationale* keeps the sentence about WAY-137 (:5401-5403).
Fingerprint of WAY-165 changes; nothing depends on it yet.

### A8 — `test_readiness_marks.py` partly repeats `TechnologyMarks` (low)

Checked: the tests test what the sentence says and only that; duplicated checks.

Evidence: `project-level/test_readiness_marks.py:92-93` (whole list has no finding) ≈
`test_readiness_check.py:605-611`; `:103-106` (`none` gives one finding) ≈
`test_readiness_check.py:436-438`. New in the file and worth keeping: the per-mark finding naming
its mark (`:95-100`), `TODO` giving no mark finding (`:108-109`), and `ApprovedBefore` (`:112-199`)
with the 77c8a8b fixture and its fingerprint `a3b6ab99` — a true regression of a definition
approved before the change, and the only test showing the "approved" path end to end (three `g`
findings, then only `e` once the items are added). The file cites no invariant, by design
(`:8-9`); the citing checks stand in `test_readiness_check.py`.

What would change: cut the two duplicated cases; keep the rest. Low — the cost is a few seconds
of test time.

### A9 — "mark" beside "marker" in one template section (low)

Checked: glossary terms and words used in two meanings.

Evidence: `project-level/definition_template.md:171-173` — a choice "ends with one marker in
English"; `:184-186` — "Each begins with its mark in English ... before its name ... and its
marker". The two near-identical words name the prefix and the suffix of one item; the readiness
check calls the prefix a mark in code (`readiness_check.py:70-72`) and the finding text does not use
either word (`:260-263`). WAY-108 calls them all "markers read by the readiness check"
(`foundations/decisions.md:3048`).

What would change: nothing binding; if anything, call the prefix "its kind" or "its English
head" in the template. Low.

### A10 — Frequency of the problem cannot be measured from the repository (note)

Checked: how often an agent improvised a way to the running product, or left the check out.

Evidence: the worktree holds no session transcripts or task-cycle records; `.runs/` holds only
the two guard records written by my run, and the recent history removed cycle evidence from the
tree (commits 0a32a43, 8b70631 in `git log`). No case can be counted; no case is cited in the
entries. The *Rationale* gives the mechanism (:3476-3479) and the *Review when* names the
observable (:3465-3467), which is the right form for a rule with no measured past frequency. I did
not search outside the worktree, as instructed.

## Checks that found no concern

- **Template conformance, WAY-121 and WAY-165:** every field present with a word its template
  gives; three binding sentences each (count passes the guard); no forbidden words; *Approved
  by* in the placeholder form the guard accepts before the request exists; *Review when* has an
  observable state and a date; *Rejected* describes options, not the route taken; *Rationale*
  names no file, script or count. WAY-121 edited in place with *Approved by* reset to the
  placeholder, as the pre-`main` route asks for a change of meaning
  (`agent-instructions/README.md:20-24`, WAY-07).
- **WAY-121 vs WAY-19 "a new rule next to an existing decision is a new question":** the three
  choices are a rule about what the list holds, the question WAY-121 answers; the split with
  WAY-165 (what each asks, how agent-use weighs) is a different question. No duplicated
  settlement between the two: WAY-121 holds presence, form, grandfathering; WAY-165 holds content
  and weighing. The template cites each where its rule stands (`definition_template.md:181-200`
  WAY-121, `:186-192` and `:237-242` WAY-165).
- **Invariant sentence vs. check vs. tests:** one sentence (guard passes). The code rejects a
  missing `logs:`/`interface:`/`development data:` item in both modes
  (`readiness_check.py:257-263`, called at `:329` outside the `before_approval` branch);
  `TechnologyMarks` runs every case "before approval" and "with its gate record"
  (`test_readiness_check.py:560-566`), reads a rejection as a finding beyond those of the same
  definition with the item added — correct, since the invariant fixes no message — and covers
  text-begins-with exactly: another case, no colon, not at the start, continuation line, nested
  item, prose line, another section, two marks in one item, an open marked item rejected only as
  open. `Command.test_a_definition_lacking_a_mark_exits_one_approved_or_not` covers the exit
  code. Nothing tested goes beyond the sentence.
- **Invariant first clause "before approval":** the code also rejects `none`, open and malformed
  items after approval; the sentence under-claims there, but that wording is unchanged from
  before the range and is not false.
- **Fixtures:** `test_plan_state.py` and `test_plan_state_invariant.py` gain the three items
  because `plan_state.py:385` runs the readiness check on the definition; the new literal
  `dcb10529` is confirmed by the passing header/gate-record comparison.
- **Relations:** WAY-165 `narrows WAY-137` is the right type — WAY-137 says agent-fit is weighed
  against no consequence for a place to run; WAY-165 goes against that in the narrower area of
  the three choices. `derives from WAY-123` is right — agent-use is declared a consequence, so it
  decides under WAY-123's own rule. No `narrows` pair. WAY-121's new `derives from WAY-118`
  (gate again) and `WAY-100` (borrowed practice) are apt.
- **Contradictions with current entries:** none found with WAY-118 (gate again after a change to
  fingerprinted sections; the plan recheck is already `plan-project`'s stated use,
  `project-level/plan/skill/SKILL.md:3`), WAY-106 (the step writes the definition only), WAY-116,
  WAY-122, WAY-123, WAY-108 (English marks, content in the definition's language), WAY-34,
  WAY-140 (a production copy's taking is a human action — matches the glossary's "human
  action").
- **Glossary:** `surface` is not used anywhere in the diff; `human action` is used in the
  glossary's meaning; "running product", "interface", "logs" are not glossary terms and are used
  in their field meaning.
- **Code:** `AGENT_PATH_MARKS` and `startswith` on the item's own text (`items()` joins
  continuation lines and stops at a nested item, `readiness_check.py:204-221`) implement "text
  begins with" exactly; the finding sits on the heading line, so the sorted output puts the three
  mark findings first — `test_readiness_marks.py:95-100` relies on that order. The docstring's
  condition g is updated (`:27-33`).
- **`define-project` step 0, no-Technology branch** (`project-level/skill/SKILL.md:68-73`): the
  human's option to leave an old definition without the step is gone; this follows from WAY-121's
  new sentence, since such a definition is one "approved before the three were required", and
  the readiness check reports the missing section as `structure` before condition g
  (`readiness_check.py:321-323`), so the separate branch is needed.
- **`settle-technology`** (`project-level/technology/SKILL.md:37-45, 60-64, 96-98, 110-113,
  127-129, 167-170, 173-177`): each addition cites its decision and holds only the order of work;
  the content of the three choices stays in the template's table. Step 0 keeps every other item
  and marker as they stand; a resumed definition with status `approved` goes to
  `definition — open: Technology`, as WAY-118 asks.
- **Cheaper ways:** the *Rejected* of WAY-121 covers the alternatives I would have raised (one
  item for all three, as many items as the product needs, a requirement beside the list, the
  deployment skill, no grandfathering, grandfathering by hand, English names). The check is nine
  lines of code and one loop; the template row is the cheapest form for the content. No cheaper
  way found for the rule itself; the cheaper ways found are the cuts in A1, A2, A7, A8.
- **Part map:** `project-level/**` covers the new test file; the failure mode "a technology choice
  the project needs is missing from the definition's list — not detected"
  (`foundations/part_map.md:116-117`) is now partly detected for the three choices, but the row
  is about any choice, so it stays true.

## Cut verdict

Something can be cut, without loss to what the change settles:

1. From WAY-121's third binding sentence, the pin-move and "as the refinement ... runs it"
   mechanism and the historical phrasing (A1) — keep the rule "approved or not, goes back to
   the step and through the gate again".
2. The restatements in `plan-project`, `refine-task` and (optionally) `lead-project` (A2) —
   "a finding returns to `define-project`" already stood there.
3. The WAY-137 restatement clause in WAY-165's binding sentence (A7).
4. The two duplicated cases of `test_readiness_marks.py` (A8).

Nothing of the rule, the invariant, the check, the template's table or `settle-technology`'s
steps can be cut. A3 (no pointer at the moment of use; independent tasks outside the rule) and
A4 (unlocatable source) are not cuts; they are the two things I would want answered in the
request before the merge.

Counts: high 0 · medium 3 (A1, A2, A3) · low 6 (A4 low–medium, A5, A6, A7, A8, A9) · note 1 (A10).
