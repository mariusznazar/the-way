FAIL 3bd9e37b60cb4c91613dddfa517c445841016688

# Review of the whole change — task `testing-guidelines`

Range `4302f72..3bd9e37` (7 commits), worktree `C:/Storage/repos/the-way-wt/testing-guidelines`,
branch `task/testing-guidelines`; `git rev-parse HEAD` = `3bd9e37b60cb4c91613dddfa517c445841016688`,
the head given. Worktree clean before and after the review.

Blocking: 1 (Important). Minor: 4. Out of scope: 1.

## Findings

### Critical

None.

### Important

1. **Two decisions this change writes collide on who fixes the first test of a level, with no
   precedence recorded (WAY-25).** Comes from no slice alone: from the plan's *Foundation entries*
   (WAY-242 and the WAY-218 edit in `57917c3`, against WAY-238 in `4f207dd`, by the spec's ruling C4),
   carried into slice 3 (`2b5b1c0`) and slice 4 (`467a2af`).
   - WAY-238 (`foundations/decisions.md:6528-6531`) binds: "The author of a change chooses, in the
     task's cycle, which behaviour gets a permanent test and at which level … while a task's
     refinement holds no plan of tests"; its *Verification* marks as violating "a task's document
     lists the tests its change is to add" (`:6550-6551`). This is row 8 and Q7, the human's.
   - WAY-242 (`foundations/decisions.md:6678-6679`) binds: "where it has none, the task that writes
     its first test designates that test, approved in the task's refinement", and its complying
     example is "the task that writes a product's first end-to-end test designates that test, its
     document carrying the decision" (`:6688-6689`). WAY-218 (`:5868-5870`, `:5881-5882`) places that
     designation in the project breakdown. The skill's "A new level"
     (`product-guidelines/testing/SKILL.md:162-164`) has refinement settle "the level, its recipe and
     the path the test takes"; `product-guidelines/reading.md:77-79`,
     `project-level/task/skill/SKILL.md:170-172` and `project-level/plan/skill/SKILL.md:121-123` route
     it there.
   - What goes wrong: to apply WAY-242, the refinement (or the breakdown) has to decide that the task
     writes a test at a given level, and at which path — the choice WAY-238 gives the cycle's author
     and the list of tests WAY-238 names as a violation. An agent refining such a task meets two
     binding entries that pull opposite ways; WAY-25 forbids it to settle that itself. The coding
     analogue it was modelled on (WAY-200, WAY-216) has no such collision, because the kind of a file
     follows from the requirement, while the level of a test is the cycle's choice.
   - Why it lies within the task: rows 8 and 12 are both the task's; the collision is between entries
     the change writes, and "contradictions between the new or edited entries" is part of this review.
   - Evidence: the quoted lines; `foundation_check.py` passes because it checks references, not
     meaning.
   - Ways out, for the orchestrator to choose (the first two stay within row 8 and row 12; the third
     records a precedence, which WAY-25 gives to a human): (a) WAY-242's "where it has none" clause
     approves the designation in refinement only where the task's required behaviour itself is a
     test of that level, and otherwise, where the cycle's author chooses a level with an empty
     *Exemplar*, at a blocked draft request as WAY-172 already provides — the skill's "A new level",
     the reading bullet and the two project-level bullets follow; (b) the first test's designation
     left to the cycle's request under WAY-172 alone, refinement naming no test; (c) WAY-242
     `narrows WAY-238` with its area in a binding sentence, recorded by the human.

### Minor

1. **`installation/test_testing_guidelines_installation.py:149-152` — the non-UTF-8 case is exempted
   from the message check on a false premise** (slice 5, `3bd9e37`; the slice-5 review's Minor,
   graded here again). The comment says the case "stops on an uncaught UnicodeDecodeError
   (pre-existing, C37)"; at this head `owned_entry_point` catches the decode error and returns False
   (`installation/install.py:298-302`), so the installer refuses with "Existing integration file
   differs" like the other crafted files. The test therefore cannot tell that clean refusal from a
   crash (the slice-5 review showed a mutant without the `try/except` passing the whole installation
   suite). Minor, not Important: what D7 requires — non-zero exit, tree unchanged, nothing staged —
   is asserted; a regression would cost a traceback in place of a message, with nothing written.
   "C37" names a question of another cycle. Fix: drop the `if kind != "non-UTF-8 file":` exemption
   and its comment.
2. **A level the testing guidelines do not name yet gets no routing in refinement**
   (`product-guidelines/reading.md:77-79`, `project-level/task/skill/SKILL.md:170-172`; slice 4,
   `467a2af`, worded as spec D6 gives it, so a gap of the spec). Both bullets fire only for "a level
   whose recipe … has an empty *Exemplar*". WAY-242 covers every level with no test, and the WAY-216
   bullet the new one models (ruling C4) fires for a kind *absent* from the index. A task whose
   tests open a level that `## Levels` lacks — a later end-to-end level, say — is not routed through
   `maintain-testing-guidelines` for the level, its recipe and its exemplar; the gap surfaces only in
   the cycle, as an unsettled meaning (WAY-172). Ties to Important 1: whatever way out is chosen
   there, these two bullets should name the absent level too.
3. **The AI tool that takes an environment fact is narrowed from "the product's" to "the one its
   tests use"** (`foundations/decisions.md:6434-6435`, WAY-236; `product-guidelines/testing/template.md:203-205`;
   foundation entries, `4f207dd`). Row 6 reads "narzędzie AI produktu ma fakt środowiska z wersją i
   datą odczytu" and item 1 "narzędzie AI, którego produkt używa"; the entry and the template say
   "each AI tool the product's tests use". Within a rule on AI in tests the narrower reading is
   reasonable (the proposal's A10 stands inside `### AI in tests`), and ruling C11 settled only the
   wording of the version, not this scope. Name the reading in the request beside C11 so the human
   sees it.
4. **Wording** (`project-level/task/skill/SKILL.md:160-161`; slice 4): "A missing coding and a
   missing testing guidelines may be one prerequisite task" — "a … guidelines" reads as a slip; e.g.
   "Missing coding guidelines and missing testing guidelines may be one prerequisite task (WAY-247)".

### Out of scope

1. `installation/test_coding_guidelines_installation.py:149-155` holds the same stale comment and
   exemption, predating this change (the change touches that file only for its count, `:97`).
   Out of scope: not part of the task; fixable together with Minor 1.

## Coverage of the task

- *To do* 1 (template): `product-guidelines/testing/template.md` holds the required form with the
  nine required rules in D3's order (`:44-52`), "What each section carries" with each rule's
  *Decision* and *Invariant* and rule/example marking, and "Writing the file". Checked item by
  item: *Applies to* and `## When to read` (WAY-246); `## Levels` with the glossary rule for a
  diverging name and the per-part sentence (WAY-240); the level rule with the yes/no table — compared
  row by row with `raport_wytyczne_testow.md` §1: nine rows, the source column dropped, "czerwony
  przed poprawką" dropped (Q14), no proportion; the bug-caught-high rule; the source of the expected
  value with no exception for snapshots or characterization tests; WAY-228's rule with the property
  clause and the fixture sentence moved from the coding template; changing an existing test with
  the list of weakenings; behaviour not detail with the three different examples and the
  precondition check; trust boundaries with the authorization table, violated marking and the
  someone-else's-configuration exception; AI in tests; flaky tests; `## Recipes` with the nine
  fields, binding fields naming a decision, "as in `<level>`", command `none`, time limit as a
  pointer; exemplar field empty until designated; `## Not tested on purpose`; `## Examples` with
  the three kinds; `## Where in code`.
- *To do* 2 (skill): `product-guidelines/testing/SKILL.md` mirrors `maintain-coding-guidelines`
  section for section (compared whole): where it works with its table, what reaches the task
  document (the five *To do* items B1 names), orchestrated mode, steps 0–5, invariants, weak points,
  critique; reports under `.runs/testing/`; entry points generated; `SKILLS` entry and
  `installation/README.md:57`, `:172`.
- *To do* 3: the coding template and skill lose the rule (`git grep` for WAY-228 and the heading in
  `product-guidelines/coding/` exits 1); kinds exclude tests (`product-guidelines/coding/template.md:68-69`,
  `:106`; `product-guidelines/coding/SKILL.md:120-121`); WAY-228 edited in place with the property
  clause.
- *To do* 4: WAY-214, WAY-215, WAY-218 edited; `product-guidelines/reading.md`, refine-task step 3
  and plan-project step 2 name the discipline (but see Important 1 and Minor 2).
- *To do* 5: WAY-174 edited; skill step 4 "How to show". *To do* 6: WAY-247; coding skill, testing
  skill, both project-level skills.
- Q1–Q14: each answer found in the entries or files; the Q14 cut list absent (grep of added lines
  for snapshot, characterization, quarantine, "before the fix", single test, "fixed before the
  next" finds each only as a ban or under *Rejected*).
- Rows 1–24: WAY-231 (1, 15), WAY-232–WAY-243 (2–13 in order), WAY-228 (14), WAY-215 and WAY-218
  (16), WAY-244 (17), WAY-174 (18), WAY-245–WAY-250 (19–24), each with the row's meaning. Row 25 per
  C3: OWASP in WAY-235, Google ch. 12 in WAY-233/WAY-234, ch. 13 in WAY-241, ch. 11 in WAY-243,
  Open Mercato in WAY-233, Anthropic in WAY-236, Limen and 10xDevs (no link) in WAY-237's rationale;
  test plan, risk map and proportions in WAY-238 *Rejected*, the red replacement in WAY-233, the
  quarantine in WAY-243.
- Spec *Foundation entries*: every new and edited entry present with the relations named; the two
  facts written; `exemplar` widened; no part-map or invariant change.
- Carried questions 1–4: D1 (`exemplar` widened, plain words), D4 (WAY-228), D6 (*Applies to*
  alone, WAY-213 unchanged), D7 (one `SKILLS` entry, counts 40).

## Slices without a review of their own

- **Foundation entries** (`4f207dd`, `57917c3`): read every new and edited entry whole. Binding
  sentences at most three; *Rationale* names no file of its own (the Limen address is a quoted
  source, which `elements/decisions/template.md:53-55` allows). Own-work check (quotations at fixed
  addresses, 33/33 by script) fits the weakest point; spot-checked six passages myself (Open Mercato
  line 106, Hypothesis, OWASP ×2, Limen ×3, Google ch. 12) — all found on the cited commit
  addresses. Collision: Important 1. Narrowing: Minor 3.
- **Slice 1** (`083ab5d`): matches D3 and the entries; the table faithful to the research; its
  own-work check (every bullet cites a decision; cut-list grep) fits and would catch a missing
  citation. Its two concerns: "(WAY-48, WAY-235)" for the review of a configuration boundary is
  consistent with WAY-235 "the review of WAY-48"; the table's "one end-to-end test for each such
  journey" is the research's, not a proportion — no finding.
- **Slice 2** (`87b600e`): the executor read only part of its *Read*; the output does not suffer
  from it — the removal is complete, the order bullet names three standing checks, the WAY-231
  clause stands where the plan asks, nothing else in the coding discipline relied on WAY-228. Its
  own-work check (leftover references) fits.
- **Slice 3** (`2b5b1c0`): the skill mirrors the coding skill; the 42 generated entry points are
  the generator's output ("entry points are current"). Its concern 2 (forward references to
  `reading.md` and `installation/README.md`) is resolved at the head. Its "A new level" carries
  Important 1. Own-work check (heading diff against the coding skill) fits the mirror requirement
  but not the collision, which lies in the entries it follows.
- **Slice 4** (`467a2af`): the three files carry D6. Its own-work check is a grep for the skill's
  name, which shows presence, not meaning; it would not catch Important 1 or Minor 2.
- **Slice 5** (`3bd9e37`): reviewed on its own (`PASS 3bd9e37`); its Minor and out-of-scope graded
  above. Trust boundary: this change bears on `installation/install.py` only through one constant
  pair in `SKILLS`; the skill text comes from the-way's commit; `owned_entry_point`
  (`installation/install.py:290-306`) refuses a foreign, directory, symlinked or non-UTF-8 file at
  the new path before any write. Nothing found beyond the slice review's probe.

## Declined to judge

- The request's own text (row 25 under *What this request settles*, C10's `narrows WAY-168`, both
  definitions of `exemplar`) and the backlog write closing the task of line 24 (Q10) — they come
  after this review, outside the commits.
- `maintain-instruction-files` not being installed in products — a shared, pre-existing gap the
  coding skill has too; the task does not ask for it.
- Whether WAY-212's "changing the product's code" also leads an agent changing only a test to the
  coding guidelines — pre-existing; the task leaves WAY-212 unchanged.
- Added prose lines over 100 columns (`product-guidelines/reading.md:3`, `:26`;
  `project-level/plan/skill/SKILL.md:118`; `project-level/task/skill/SKILL.md:170`) — no rule or
  check of the-way sets a width.

## Checks run

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `git diff --check 4302f72..3bd9e37` | 0 | empty |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 259 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK, 5 skipped |
| `python -B gate/run_tests.py gate` | 0 | OK |
| `python -B installation/test_testing_guidelines_installation.py` | 0 | 2 tests OK |
| `python -B installation/test_coding_guidelines_installation.py` | 0 | 2 tests OK (count 40) |
| `python -B installation/test_styleguide_installation.py` | 0 | 2 tests OK (count 40) |
| `git grep -n "WAY-228\|Test inputs and expected values" -- product-guidelines/coding/` | 1 | no output |
| `curl` of the Limen, Google ch. 12, Goldstein PDF and both arXiv addresses | — | HTTP 200 each (invariant `outbound-link-reach`) |
| `curl` + `grep` of six quoted passages on their cited addresses | — | each found |
| Manual: yes/no table against `raport_wytyczne_testow.md` §1; testing skill against coding skill, whole; grep of added lines for the Q14 cut list | — | as reported above |

Not run: the full `python -B gate/run_tests.py installation` (about four minutes; the cycle's own
full run — the slice-5 executor reports exit 0, 44 tests) and the whole gate (the cycle's run before
the request). No crafted-input probe of my own: the slice-5 review ran 16, and this change adds
nothing at the boundary beyond that slice.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-25, WAY-168, WAY-172, WAY-200, WAY-213, WAY-214, WAY-216, WAY-217,
  each whole — the entries the collision and the reading bullets are judged against.
- `elements/decisions/template.md:20-61` — whether a quoted source may stand in a *Rationale*.
- `foundations/invariants.md` `outbound-link-reach`; `foundations/part_map.md` whole — touched parts.
- `product-guidelines/coding/SKILL.md` and `product-guidelines/coding/template.md`, read in full
  (mirror and removal); `product-guidelines/template.md:1-40`; `product-guidelines/styleguide/template.md`
  headings (how sister templates mark sections).
- `installation/install.py:290-306` — the refusal path for Minor 1.
- Outside the repository: `research_wytyczne_testow/raport_wytyczne_testow.md` §1 (the table) and
  `propozycja_szablonu_i_skilla.md` rows A10, A12, A13, A15, B4 (fidelity of the template and of
  WAY-236).

## Review of the fix

PASS a2f11659043955f741c5c51a88d36f9f981572b2

Fix range `3bd9e37..a2f1165` (one commit, `a2f1165`); `git rev-parse HEAD` = the given head;
worktree clean. Bounded by `reports/fix-findings.md` (Important 1 of this review), fixed by way (a),
ruling C13; fix report `reports/fix.md`.

### Finding 1 (Important) — fixed

- WAY-242 (`foundations/decisions.md:6677-6686`) now has refinement approve a level's first exemplar
  test only where the task's required outcome is itself a test of that level, the document naming
  the level and "no list of tests and no path". Where the author chooses the level in the cycle, the
  designation goes to a blocked draft request, the route WAY-172 already gives a meaning the task
  document does not settle. In both cases the refinement no longer chooses a level or lists tests.
  So WAY-238's binding sentence and its violating example ("a task's document lists the tests its
  change is to add") no longer collide with it. The new complying example (a task whose outcome is
  the sign-up end-to-end test; the cycle writes the path) and the violating one (the discount-rule
  task's refinement giving its first unit test and path) mark the line between the two
  decisions. The *Rationale* names WAY-216 and WAY-238, and *Rejected* gains ways (b) and
  "every first-test task".
- WAY-218 (`:5869-5871`, `:5881-5887`), the skill's step 1 mode, "A new level" and step 4
  (`product-guidelines/testing/SKILL.md:117`, `:162-167`, `:193-194`), `product-guidelines/reading.md:77-82`,
  `project-level/task/skill/SKILL.md:170-174` and `project-level/plan/skill/SKILL.md:121-124` follow
  the same split. A search outside `.runs/` for the old phrasings (`path the test takes`,
  `approved in the task's refinement`, `task writing that level's first test`, `writes the first
  test of a level`, `each new level`) finds nothing (exit 1).
- WAY-242 keeps three binding sentences (WAY-05).

### What the fix itself changed — no new Critical or Important finding

- *Scope* of WAY-242 widened to `product-guidelines, project-level` (the fixer's own choice). This is
  sound: its binding sentences now say what a task's refinement and a breakdown approve, as WAY-216
  (`project-level, product-guidelines`) does, and WAY-21 finds a decision through *Scope*. The part
  exists; `foundation_check.py` passes.
- No `derives from WAY-238` was added. That is acceptable: WAY-242 no longer collides with WAY-238,
  so no `narrows` is needed (WAY-25), and the rationale names it.
- The spec (`spec.md:139`) carries the C13 note over D5, D6 and the WAY-242/WAY-218 rows, as the
  fix report asked; it is outside the commit range.
- Outside the fix, not reopening the review: Minor 2 of this review (a level that `## Levels` lacks
  gets no routing) still stands in `reading.md:77-82` and `project-level/task/skill/SKILL.md:170-174`,
  whose condition remains "a level whose recipe has an empty *Exemplar*". Minor 1, 3 and 4 and the
  out-of-scope finding are unchanged, as WAY-161 leaves them.

### Checks run on `a2f1165`

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `git diff --check 3bd9e37..a2f1165` | 0 | empty |
| `git grep` for the old phrasings, outside `.runs/` | 1 | no hit |
| `python -B gate/run_tests.py elements/common` | 0 | OK |
| `python -B gate/run_tests.py project-level` | 0 | OK |

Not run: the installation suite and the whole gate. The fix touches no code or test, and the whole
gate is the cycle's run before the request.

### Reaches

None beyond the fix diff, the findings file, the fix report and `spec.md:139`.
