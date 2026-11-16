FAIL 452f123d65de88143c91fe37b5633ecd341d88ee

# Review of the whole change — relations-todo-for-unwritten-decision

Range: `30c947f686b3d304f5a952cb6efe547762cfa247..452f123` (one commit, `452f123`, one author, no
plan, no slices). `git rev-parse HEAD` in the worktree gave `452f123d65de88143c91fe37b5633ecd341d88ee`,
the head of the dispatch. Trust boundary: no; irreversible operation: no (step 4 answers, confirmed:
the change touches no boundary the part map names).

## Findings

### Critical

none

### Important

**I1 — A bare `TODO` in *Relations* that carries a relation type passes the check (within the task; blocking; comes from the one commit `452f123`, there is no plan).**

- Place: `elements/common/foundation_check.py:264` (`todo_item`) and `:573-577`
  (`check_foundation_references`, the new *Relations* branch); the claim it fails stands in
  `elements/decisions/template.md:75-76` and in WAY-71 `foundations/decisions.md:612`.
- What is wrong: `todo_item` finds a `TODO` item only where the piece of the value *begins* with
  `TODO`. In *Relations* every item naturally begins with its type, `derives from` or `narrows`, so
  the value `derives from TODO`, or `derives from WAY-01 · derives from TODO`, has no piece that
  begins with `TODO`: the script reads it as an ordinary relation, finds no decision number in it
  and reports nothing. A bare `TODO` stands in *Relations* and passes. With a description, `derives
  from TODO — <the decision>` also passes as a plain relation, and where the description holds a
  decision number, the script reports that number as a reference ("names no decision of the log"),
  which points the author at the wrong thing instead of at the form.
- Why it matters: To do 4 asks that a bare `TODO` in *Relations* be reported as an error with the
  hint of the form, and the template sentence this change writes says "The script reports a bare
  `TODO` in *Relations* ... as an error (WAY-71)". WAY-71's *Rejected* names the cost: "letting a
  bare `TODO` pass — the main branch would hold a gap that names no fact". *Rests on*, *Derives from*
  and *Based on* carry no type word before an item, so this gap is new with *Relations*; and the
  form an author is most likely to write by analogy with the other items of the field, `derives
  from TODO …`, is exactly the one that slips through. The files do not do what the entry they
  change requires (WAY-263), so the grade is Important. Before the change the same value also passed
  (the old check matched `TODO` only at the start of the value), but the old rule forbade `TODO` in
  *Relations* altogether, and this change is the one that invites the word into the field.
- Evidence: scratch run in a worktree of the head under `.runs/review-whole/head`, WAY-71's
  *Relations* line (`foundations/decisions.md:617`) replaced in turn, then
  `python -B elements/common/foundation_check.py`:
  - `- **Relations:** derives from WAY-01 · derives from TODO` → `0 errors`, exit 0;
  - `- **Relations:** derives from TODO` → `0 errors`, exit 0;
  - `- **Relations:** derives from WAY-01 · derives from TODO — WAY-9999, expected later` →
    `foundations/decisions.md:617: \`WAY-9999\` names no decision of the log`, 1 error.
  No test of `elements/common/test_foundation_check.py` holds a value with a type before `TODO`
  (`test_relations_a_bare_todo_names_no_decision` tries `TODO`, `` `TODO` ``, `TODO —`, `TODO — `,
  `derives from ABC-01 · TODO`, `derives from ABC-01 · `TODO``, `derives from ABC-01 · TODO —`).
  The author's own-work check (four values on the real log) did not try this form either.
- What a fix may do (not prescribed): in *Relations*, read a `TODO` that follows a relation type at
  the start of an item as the start of a `TODO` item too, and report it — bare, with the hint of the
  form, or with a description, with a message that the `TODO` item takes no type — with a test for
  each.

### Minor

**M1 — WAY-126's new sentence says the `TODO` is replaced "with its identifier", which for *Relations* drops the relation type (within the task).**
`foundations/decisions.md:3736-3738`: "A change that writes a projected entry into the foundation
replaces with its identifier each descriptive `TODO` that points at it, in a decision's *Relations*
and in an invariant's *Derives from*." The complying example at `:3751-3753` says the same ("replaces
with its number the `TODO` that names it in the *Relations* of a decision"). In an invariant's
*Derives from* the identifier alone is the right value; in a decision's *Relations* an item is a type
and a number (`derives from WAY-NN`, template "Relations and precedence"), and the script checks no
type, so a literal reading would leave `WAY-NN` with no type and pass. The template's closed list and
its example `derives from WAY-01` steer most writers right, which keeps this Minor. Wording such as
"replaces each descriptive `TODO` that points at it with a reference to it by its identifier — in a
decision's *Relations* as `derives from <number>`" would close it.

**M2 — No test holds the check of a decision number on a continuation line of the known part of *Relations* (within the task).**
`elements/common/foundation_check.py:573-577` now skips every line of *Relations* in
`check_decision_numbers` (`relation_lines`) and checks the known part line by line through
`zip(lines, value.split("\n"))`. The only test of a wrong number in a known relation,
`test_decision_relation_that_does_not_exist` (`test_foundation_check.py:390`) and the new
`test_relations_a_decision_before_a_todo_is_still_checked` (`:748`), use a one-line value, so a
mutation that checks only the first line of the known part (for example `lines[:1]`) passes every
test. The behaviour is right today: my scratch run with `WAY-9999` on the second line of WAY-126's
*Relations*, `foundations/decisions.md:3744`, gave `foundations/decisions.md:3744: \`WAY-9999\` names
no decision of the log`, 1 error. Before the change the generic line check covered such lines, so the
protection the change removed from there has no test in the new place. One test with a value over
two lines and an unknown number on the second, with no `TODO`, would hold it.

**M3 — One docstring line runs past the width of the rest after the reflow (within the task).**
`elements/common/foundation_check.py:49`: "is an error (WAY-71). A `TODO` after a comma or a line
break instead of ` · ` begins such an item too: a bare" — about 111 characters, while the paragraph
around it wraps at 100. No blocking rule of the linter covers line length (`ruff.toml` selects no
`E501`), so this is style only.

**M4 — WAY-287 lists three fields for the descriptive `TODO` while item 16 of the request template now lists four (outside the task's scope: the task fixes WAY-287 as unchanged; named so because it is a defect the task mandates).**
`foundations/decisions.md:7007-7009` (binding sentence: "each descriptive `TODO` in an invariant's
*Rests on* or *Derives from* or in a decision's *Based on* that stands on the main branch after the
change (WAY-71)"), `:7065-7067` (*violates*) and `:7083-7084` (*Rationale*) name three fields;
`task-cycle/skill/request_template.md:271-274` and WAY-71 (`:603-611`, "a change that leaves one there
puts it before the human") now name *Relations* too. Nothing contradicts — WAY-287 does not exclude
the fourth field, and the orchestrator writes the request from item 16 — but a reviewer comparing a
request with WAY-287's examples finds no case for a *Relations* `TODO`, and WAY-287's own *Rejected*
names this very risk of an enumeration in its sentence: "a forgotten change giving the same gap
between the decision and this entry". Leaving it costs nothing today; the fix is one clause ("or
*Relations*") in three places and changes the wording of an approved decision, so it is the human's
to decide. The author raised it as concern 1.

**M5 — The template's table of readers does not name what now reads *Relations* (outside the task's scope).**
`elements/decisions/template.md:116`: "| Relations | an agent meeting two decisions that collide
(WAY-25); the author's search of the foundation (WAY-33) |". `foundation_check.py` reads the field
(a decision number that names no decision, and now a bare `TODO`), the orchestrator reads it for item
16 of the request, and the writer of a projected entry reads it for WAY-126's new sentence. The row
of *Based on* names `foundation_check.py`; the row of *Relations* never did, so the gap predates the
change and only widens with it.

## Against the task, item by item

- To do 1 (WAY-71): the binding sentence names *Relations* in the form
  `TODO — <the decision, and where it is expected>`, for any decision the entry derives from, whether
  or not a definition projects it; the last-item clause covers it; *Origin* stays without `TODO`;
  *Rationale*, *Verification* and *Rejected* follow, the three ways not chosen of questions 1 and 2
  stand in *Rejected* with their costs, matching the task's *Not chosen*. Met.
- To do 2 (`elements/common/rules.md:22-30`): word for word with WAY-71. Met.
- To do 3 (template): the line of the block and the sentence on *Relations* and *Origin* are as asked.
  Met in text; the sentence's claim about the script is what I1 shows unmet for one form.
- To do 4 (script and tests): `MISSING` gains *Relations*, `DECISION_WORDS` loses it, the description
  is read as no reference, the known part stays checked, the docstring follows, and the three test
  cases the task names are present. Met except the bare `TODO` behind a type (I1).
- To do 5 (WAY-126): the sentence stands, in a paragraph of its own. Met; wording M1. The second
  paragraph is sound by WAY-05: the first paragraph already holds three sentences, and the new one
  answers a part of another question (what happens to entries that wait for something when it
  arrives, the rule of withdrawn WAY-37, now in `elements/common/way_of_working.md` step 2).
- To do 6 (request template item 16): met.
- *Questions to settle* 1–4: the form, its reach to any unwritten decision, the WAY-126 sentence and
  the going on without waiting for guidelines are all as answered. *Out of scope*: no check against a
  definition, *Origin* unchanged, nothing of `loop2` touched. Met.
- *Settlements to record*: `none`; no row to meet.
- Additions beyond the task: the sentence in "Relations and precedence" of the template
  (`elements/decisions/template.md:221-222`) carries the task's own note on WAY-32 ("opisowe `TODO`
  nie jest trzecim typem powiązania") into the place where WAY-32's rule now stands, and keeps the
  closed list from contradicting the new word; no finding. The pair of examples added to WAY-126 and
  the changed pair of WAY-71 make both entries `the cycle's`; both would reach the human at the merge
  anyway (WAY-114, no settlement row), so the pairs add no item of acceptance; no finding.
- The orchestrator's facts: (1) `guidelines/` exists and binds — read whole, below; (2) WAY-37 and
  WAY-32 are withdrawn — the change names neither, and edits only the places that carry their rules;
  (3) the author's concerns — WAY-287 is M4; the second paragraph and the pairs are judged above; the
  extra template sentence is judged above; `ruff` is unavailable here too (Checks); `way_of_working.md`
  read whole by me: step 3 ("What stays open after step 4 is written as `rules.md` gives it") and step
  2 (what the change brings that entries wait for) already cover the *Relations* `TODO` through
  `rules.md`; no step needs a sentence of its own.

## Against the guidelines

- `guidelines/coding.md`: *Linter* — not run (Checks); I read every added line of the two Python files
  for the blocking kinds most likely here (unused or undefined names, unused imports): none found.
  *Size* — the file grew 984 → 992 (threshold 1000), no function over 80 lines added (size test
  below). *How a script starts and ends* — unchanged. *A field missing from a file a script reads*
  (WAY-344) — a missing *Relations* gives `("", [])` and no reference, and the field itself stays in
  `DECISION_FIELDS`, so a missing field is still reported; as before.
- `guidelines/coding-check.md`: no rules (WAY-386); the exemplar's way is an example only.
- `guidelines/testing.md`: the new tests are files-and-git tests like their neighbours, at the level
  of the behaviour; expected messages are written out, the hint text is asserted because To do 4 asks
  for the hint of the form; the deleted half of `test_relations_and_origin_take_no_todo` has its cause
  on the side of the requirement (To do 4, WAY-71 changed in the same commit), named in the author's
  report. Coverage gaps: I1, M2.

## Structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 30c947f686b3d304f5a952cb6efe547762cfa247 452f123` (exit 0):
`foundation_check.py` 984 → 992 (+8), `test_foundation_check.py` 1675 → 1719, `rules.md` 93 → 95,
`decisions/template.md` 314 → 320, `foundations/decisions.md` 10739 → 10761,
`request_template.md` 563 → 564. The size invariant's test, unmarked, gives the same list on the base
and the head (11 functions and 2 files, none in `elements/common/`): the change pushed nothing over a
threshold. `check_foundation_references` grew by five lines and stays well under 80. No code left
without a user, no name that stopped being true (`relation_lines` sits beside `based_lines` and
`derived_lines`).

## Declined to judge

- How a projected decision in a project definition writes its *Relations* to another projected
  decision (`elements/decisions/skill/projected.md` gives no form, while
  `elements/invariants/skill/SKILL.md:58-60` gives one for an invariant's *Derives from*): the task
  is about the main branch and leaves projected mode alone.
- The script accepting a `TODO` item in *Relations* after a `narrows` relation, or a `TODO` that
  points at a decision this one would narrow: WAY-71 speaks of a decision the entry derives from, but
  the task rejects any check of the description by the script (*Out of scope*), and the type is
  inside the description.
- The test helper `assertPasses` matching `"0 errors"` as a substring (it also matches `10 errors`)
  and `assertFails` matching `"1 error"` (also in `11 errors`): the helpers predate the change, and the
  exit code assertion beside them keeps the passing tests honest.

## Checks

- `git rev-parse HEAD` — `452f123d65de88143c91fe37b5633ecd341d88ee`, the dispatch's head.
- `python -B gate/run_tests.py elements/common` — exit 0, 252 tests OK (94.8 s).
- `python -B elements/common/foundation_check.py` (reviewed worktree) — exit 0, `0 errors`.
- `python -B task-cycle/change_file_sizes.py 30c947f686b3d304f5a952cb6efe547762cfa247 452f123` —
  exit 0 (figures above).
- `python -B -m unittest agent-instructions.test_size_invariant` in worktrees of the base and the head,
  the `@unittest.expectedFailure` mark of
  `test_no_function_or_file_of_a_script_is_over_its_threshold` taken off — exit 1 on both, the same
  11 functions and 2 files listed on both, none of them a file of this change.
- Scratch runs of `python -B elements/common/foundation_check.py` in the head worktree with WAY-71's
  or WAY-126's *Relations* edited: the three values of I1 (exit 0, 0, 1 as given there); `WAY-9999` on
  the second line of a known part (exit 1, the right line and message, M2); a description over two
  lines after known relations with numbers in it (exit 0, `0 errors`); a bare `TODO` alone on the
  second line after ` ·` (exit 1, `foundations/decisions.md:3745: *Relations* reads \`TODO\` and names
  no decision: write \`TODO — <the decision, and where it is expected>\``). Each file restored after.
- Not run: `ruff` — not installed (`ruff: command not found`; `python -m ruff`: `No module named
  ruff`; no `uv`, `uvx` or `pipx` on the path), so the linter's blocking rules on the two changed
  Python files are unverified here; the gate's run covers them. The full gate — the orchestrator's
  (WAY-160).

## Reach beyond my selection

- `elements/decisions/skill/projected.md`, `elements/common/projected_mode.md`,
  `elements/invariants/skill/SKILL.md:50-64`: to see whether projected mode gives a form for a
  relation to an unwritten decision (Declined to judge).
- `task-cycle/skill/foundation_step.md:20-45`: how an entry with an added pair is marked.
- `task-cycle/skill/request_template.md:200-300`: the groups and item 16 in context.
- A search of every `*.py` for `Relations` and of `task-cycle/*.py` for `Rests on|TODO`: whether
  another script parses the field (only `migrate_foundation.py`, for the earlier form; no request
  check reads item 16).

## Working copies

- `.runs/review-whole/base` and
  `...\head` — git worktrees of `30c947f` and `452f123`, for the size test and the scratch runs;
  removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-whole/` — the
  index, the list of sections and the outputs of the test runs; removed. The index is kept beside
  this report as `review-whole-index.txt`. The reviewed worktree, its index and branch are unchanged
  (`git status --short` empty).

## Unread material

Index of my selection: 33 decisions listed in full, 123 by heading (sections "The foundation and its
entries", "Decision entries and the decision log", "Project definition", "The request and the
human"; parts `elements-common`, `decisions`, `task-cycle`; decisions WAY-71, WAY-126, WAY-17,
WAY-287, WAY-385, WAY-263, WAY-33, WAY-114). I read the whole index, ran through the 123 headings,
and read whole 6 of its decisions: WAY-17, WAY-54, WAY-71, WAY-05, WAY-12, WAY-126. The other 27
decisions listed in full were read by their binding sentences in the index.

- WAY-287, which bears on the change (M4): read its binding sentences, *Verification*, *Rationale*
  and its *Rejected* up to the options on the incomplete reading (`foundations/decisions.md:6995-7113`);
  the rest of its *Rejected* not read.
- WAY-114 and WAY-33, named in the change's context: read by their binding sentences in the index,
  not whole.
- Guideline files: none unread — `guidelines/coding.md`, `guidelines/coding-check.md` and
  `guidelines/testing.md` read whole; the other kind files apply to parts or kinds the change does not
  touch.
- `foundations/invariants.md`: not read; the change touches no invariant's *Part* in a way I searched
  for, and the size invariant I ran by its test. Part map read whole; glossary not read (the change
  adds no term).

## Searches not found or unclear

- Whether a `TODO` item in *Relations* may carry a relation type before it (`derives from TODO — …`):
  neither WAY-71, `rules.md` nor the template says; the template's example puts no type before it
  (`derives from WAY-x · TODO — …`). Unclear in the sources, and the script neither accepts it as the
  form nor reports it (I1).
- `ruff` in this environment: not found (Checks).
