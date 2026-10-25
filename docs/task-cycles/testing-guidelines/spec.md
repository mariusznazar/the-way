# Spec — the way: testy jako osobna dyscyplina wytycznych produktu

- Task: `.runs/task-cycles/testing-guidelines/task.md` (frozen copy of
  `_zadania/wytyczne_produktu_testy.md`, `Status: ready for cycle`, sources at `foundations` `4302f72`)
- Open choice: (1) the English words the-way's entries use for a test level, a property test, a
  level's exemplar test and the source of the expected value, and whether the glossary entry
  `exemplar` widens; (2) the wording of WAY-228 in its new place; (3) whether the shared reading
  selects the testing guidelines by *Applies to* alone or also by `## When to read`; (4) how the
  installer brings the new skill to a product that already pins the-way; (5) how the 25 rows of
  *Settlements to record* map onto the foundation.

The task binds over this spec. "Row N" is a row of the task's *Settlements to record*, "Q N" its
question N ("Pytanie N"), "item N" an item of its *To do*. The meaning of every row is the human's
and needs no new approval (WAY-30); how each becomes an entry, and its wording, is the cycle's: the
foundation step writes each entry through the skill of its element. Orchestrator rulings cited:
C3 (row 25) and C4 (row 12), recorded in the cycle record.

## Intent

An agent that writes or changes a test of a product finds one source for it: `guidelines/testing.md`,
written from a new template of the testing discipline, which names the product's test levels, how
to choose a level for a named break, where the expected value comes from, what a change to an
existing test needs, what an assertion may check, the refusal test of every trust boundary, how AI
enters tests, how flaky tests are treated, a recipe for each level and what the product deliberately
does not test. A new skill, `maintain-testing-guidelines`, leads the refinement of the task that
writes or extends that file with the human, as `maintain-styleguide` and
`maintain-coding-guidelines` lead theirs. The one rule of tests the coding template carries today
(WAY-228) moves to the testing template, which also lets property tests stand; a product without
testing guidelines stops a task that writes or changes tests in refinement, as it stops one that
lacks a styleguide or coding guidelines.

## Goals and non-goals

Goals:

- `product-guidelines/testing/template.md` and `product-guidelines/testing/SKILL.md` exist in the
  shape of the two other disciplines (items 1, 2), with the skill's entry points and its entry in the
  installer's `SKILLS`.
- The coding template and skill lose the rule of tests; WAY-228 binds from the testing template and
  covers property tests; kinds of code of coding guidelines exclude tests (item 3).
- The shared reading, refinement and project breakdown name the testing discipline beside the two
  others (item 4); WAY-174 covers the testing skill (item 5); one guidelines task may write coding and
  testing guidelines together (item 6).
- The foundation carries each row 1–24 as an entry the task settles, and row 25's meaning in the
  decisions that carry each borrowed piece (C3).

Non-goals (task, *Out of scope*, and what no item asks):

- `loop2`'s testing guidelines and the move of its pin — a separate `loop2` task.
- Process gaps that are not rules of guidelines: signals that code special-cases a test, and the
  return without code when a test contradicts the requirement (`raport_wytyczne_testow.md` §8).
- Any change to the steps of the author and the reviewer of the task cycle (Q11):
  `task-cycle/change/SKILL.md` and `task-cycle/review/SKILL.md` stay as they are.
- A script that checks the form of testing guidelines (WAY-170: none exists for any discipline).
- A test plan in a task document (Q7, row 8; `project-level/task/skill/SKILL.md:233-235` already
  forbids it).
- Testing guidelines for the-way itself.

## Constraints

From the task:

- Every item of *To do* 1–6 and every answer of Q1–Q14 as written; the cut list of Q14 stays cut
  (no exception for snapshots or characterization tests, no red replacement of an old test, no "a fix
  gets a test red without the fix", no second reviewer question about the change that turns a test
  red, no "a flaky test is fixed before the next change", no single test in the exclusions section, no
  separate commands of the test tool, no naming of an exemplar's change in the change description, no
  example of a valueless test that already has a rule).
- The headings of the required rules are those the accepted proposal names
  (`research_wytyczne_testow/propozycja_szablonu_i_skilla.md`, rows A3–A11), accepted whole in Q14.
- Reports of the skill go under `.runs/testing/` (item 2, B3).

From the foundation:

- WAY-167 stays as it is: `guidelines/testing.md` is a file `guidelines/<discipline>.md` (C6 of the
  proposal); its *Verification* already names `guidelines/testing.md`.
- WAY-171: the common form, headings and fields in English, a dropped required part reads `none —`
  with the departing decision; the testing template adds sections only at places it names.
- WAY-168: a binding rule names its product decision; an invariant only where a cheap test checks it,
  otherwise review; what names no decision is an example.
- WAY-173: the template's rules and the skill's proposals bind a product only through its adopting
  decision; a decision of the-way on them binds the template and the skill.
- WAY-172: a new or changed meaning — a level, an exemplar test, an exclusion — is a product decision
  approved before the code, in the task document.
- WAY-05: one to three binding sentences per decision; rationale names no file, script or count.
- WAY-19 and `elements/decisions/template.md:40-42`: "what do we take from X" is no question; what
  such a list carries goes to the decisions that carry each rule. Three decisions of that shape were
  withdrawn (WAY-175, WAY-195, WAY-222).
- WAY-07 and `agent-instructions/README.md`: an existing decision is edited in place.
- WAY-27: no pointer to a source a reader cannot open — the 10xDevs course is private.
- WAY-90 and WAY-80: a citation that, once untrue, would call a decision into question — a finding
  about agents or models — is an environment fact; any other source is quoted with its address, the
  place, the passage word for word and the date read.
- WAY-16: one command runs every test; no instruction lists commands of its own.
- WAY-08: an invariant's test is seen failing once; WAY-51: an invariant the product does not meet is
  marked violated by a foundation change a human accepts; WAY-48: a trust boundary is recorded at its
  part of the map.
- WAY-121: a new tool is a technology choice, a question of the task, never the skill's.
- WAY-119 is withdrawn: no decision carries a *Review when* field, so a return condition stands in a
  decision's binding sentences.
- WAY-127 and the invariant `skill-entry-points`: entry points are generated by
  `python -B agent-instructions/skill_entry_points.py --write`; its parser refuses a description that
  starts with one of `-?:,[]{}#&*!|>'"%@` or a backtick, holds `: ` or ` #`, or ends with `:`
  (`agent-instructions/skill_entry_points.py:42,118-120`).

From the code as it stands:

- `installation/install.py:25-44` `SKILLS`; `installation/test_coding_guidelines_installation.py:97` and
  `installation/test_styleguide_installation.py:91` assert exactly 38 installed entry points
  (19 skills × 2).
- `product-guidelines/coding/template.md:44,59-62,156-161` and `product-guidelines/coding/SKILL.md:220-222`
  carry the rule of WAY-228 today; nothing else in the-way names WAY-228 outside the foundation.

Quotations. `raport_wytyczne_testow.md` ("Jak czytać ten raport") warns that most quotations were
extracted by a page-fetching tool and are exact only for thoughtbot, Freeman et al. 2004, Barr et al.
2015, Goldstein et al. 2024, the Claude 3.7 Sonnet system card ch. 6 and ISTQB CTFL 4.0.1. Every
quotation an entry carries is read again by the entry's writer on the source at a fixed address and
copied from there, never from the research notes; a source the writer cannot reach stops the writer,
who asks through the orchestrator. The quotations the entries are expected to carry:

| Source (as the research names it) | Expected entry | Research's mark |
|---|---|---|
| OWASP, *Authorization Regression Testing Cheat Sheet* — "Authorization implementation is rarely static."; the suite "must be a required check in the CI/CD pipeline" | WAY-235 *Based on* | tool-extracted; check |
| SWE@Google ch. 12 — "bug fixes typically shouldn't require updates to existing tests." / "the ideal test is unchanging …" | WAY-233, WAY-234 *Based on* | tool-extracted; check |
| SWE@Google ch. 13 — "A real implementation is preferred if it is fast, deterministic, and has simple dependencies." | WAY-241 *Based on* | tool-extracted; check |
| SWE@Google ch. 11 — "rerunning a test is only delaying the need to address the root cause of flakiness." | WAY-243 *Based on* | tool-extracted; check |
| Open Mercato skills, `om-code-review/references/review-checklist.md:106` (repository `open-mercato/skills`, read at `e320bd5`) — the list of weakened assertions | WAY-233 *Based on* | verbatim from a local clone; check at a commit address |
| Limen, `github.com/overment/limen` at `89ef378`, its kinds of tests without value | WAY-237 *Rationale*, with its address and passage (not *Based on*: WAY-237 does not rest on it) | verbatim from a clone; check at a commit address |
| Anthropic, *Demystifying evals for AI agents* — "We recommend choosing deterministic graders where possible, LLM graders where necessary …" | WAY-236 *Based on* | tool-extracted; check |
| Vocke, *The Practical Test Pyramid* — "If a higher-level test spots an error and there's no lower-level test failing, you need to write a lower-level test" | WAY-238, WAY-239 *Based on* | tool-extracted; check |
| Konstantinou et al., arXiv 2410.21136 — LLM oracles "capture the actual program implementation" | a new environment fact under WAY-232, if the decision rests on it | tool-extracted; check |
| ImpossibleBench (existing fact `impossiblebench-test-modification`) | WAY-233 *Based on* | fact already checked |
| WebTestBench, arXiv 2603.25226 — "All evaluated models failed to achieve an F1 score exceeding 30%." | a new environment fact under WAY-236, if the decision rests on it | quote marked exact, rest paraphrase |
| Hypothesis, *Stateful testing*; Goldstein et al. ICSE 2024 | WAY-228 rationale or *Based on* | Goldstein exact; Hypothesis check |
| ISTQB CTFL 4.0.1 — "risk acceptance" | WAY-237 *Based on* | exact |

## Decisions

> Settled after the review of the whole change (cycle record C13, fix `a2f1165`): a level's first
> exemplar test is approved in refinement only where the task's required behaviour is itself a test
> of that level, refinement naming the level and never tests or paths (WAY-238); where the cycle's
> author picks a level with an empty *Exemplar*, the designation goes to a blocked draft request
> (WAY-172). Where D5, D6 and the rows for WAY-242 and WAY-218 below say otherwise, this holds.

### D1. Words (open choice 1)

- **A level's exemplar test — widen `exemplar` in place.** The entry's definition grows from "the
  model after which later code of its kind is written" to a file a product's decision designates as
  the model after which later files of its sort are written — code of a kind of code, or tests of a
  test level. *Not* stays `none`. Through `record-glossary-term`.
  - Rejected: a term of its own, "exemplar test" — a phrase holding the word itself for a second
    sense, the shape WAY-99 refuses as a carrier, and two entries for one concept (a file a decision
    designates as the model); the entry left as it stands — row 15 takes tests out of the kinds of code,
    so "later code of its kind" would read two ways for a test.
  - Cost if wrong: one glossary edit back and the words of WAY-242.
- **"test level", "property test", "the source of the expected value" — plain words, no entry**
  (WAY-95: the-way uses each as the field does; a product's own name for a level that means
  something other than in the field is an entry of the product's glossary, row 10, WAY-226).
  - "test oracle" is not used for the source of the expected value: the field counts the previous
    version of the program among oracles, which row 2 excludes, so the word would carry back what the
    rule forbids.
  - Rejected: entries for "test level" and "property test" — plain meanings take none (WAY-95's
    "digest" case); "oracle" with an entry narrowing it — a field word read in its field sense
    beside every use.
  - Cost if wrong: the glossary skill's WAY-95 test on the final sentences finds a word used other
    than the field uses it; the foundation author then writes its entry and the request lists it.
- "refusal invariant" is no term: entries say "an invariant that the boundary refuses crafted input
  or unauthorised access" in plain words.

### D2. Where it lives (units)

| Path | Change | Unit's job |
|---|---|---|
| `product-guidelines/testing/template.md` | new (D3) | what testing guidelines add to the common form and how the cycle's author writes them |
| `product-guidelines/testing/SKILL.md` | new (D5) | the skill `maintain-testing-guidelines`: order of work in the refinement of a testing-guidelines task |
| `product-guidelines/coding/template.md`, `product-guidelines/coding/SKILL.md` | changed (D4) | lose the rule of tests; kinds exclude tests; one clause for row 21 |
| `product-guidelines/reading.md` | changed (D6) | names test work and the testing gaps |
| `project-level/task/skill/SKILL.md` (step 3), `project-level/plan/skill/SKILL.md` (step 2) | changed (D6) | name the testing discipline and its skill |
| `installation/install.py`, `installation/README.md`, installation tests | changed (D7) | the new skill reaches products |
| `.claude/skills/the-way-*/SKILL.md`, `.agents/skills/the-way-*/SKILL.md` | regenerated (D8) | entry points |
| `README.md` | changed (D8) | lists the testing discipline's directory and skill |
| `foundations/decisions.md`, `foundations/glossary.md`, `foundations/environment_facts.md` | foundation step (*Foundation entries*) | |

`product-guidelines/**` already belongs to `product-guidelines`, whose responsibility ("the template
of each discipline of guidelines with the skill that leads the work on them") and WAY-09 ("for each
discipline of work whose guidelines the-way gives a template of, that template with the skill") cover
the new directory; neither changes. `product-guidelines/template.md` stays: its "Where guidelines go"
already places `guidelines/<discipline>.md`.

### D3. The template of the testing discipline (`product-guidelines/testing/template.md`)

It opens as the coding and styleguide templates do: whom it is written for, that a product keeps one
file `guidelines/testing.md` (WAY-167), that its rules bind a product only through an adopting
decision and a departure only through a decision with its reason (WAY-173), that each rule below cites
the decision of the-way that sets it, and that the rules of form every file keeps stand in
`product-guidelines/template.md`. Its sections: "Required form", "What each section carries",
"Writing the file". No script checks it (WAY-170).

**Required form.** The common form with these additions, in this order, in a fenced block as the
other templates give it:

1. header `# Testing guidelines — <the product>`, *Discipline* `testing`, *Applies to*;
2. `## When to read`;
3. `## Levels`;
4. `## Rules` with the required rules in this order, each with *Decision*, *Invariant*, *Good*, *Bad*:
   `### Choosing the level`, `### A lower test for a bug caught high`,
   `### Where the expected value comes from`, `### Test inputs and expected values`,
   `### Changing an existing test`, `### Behaviour, not implementation`, `### Trust boundaries`,
   `### AI in tests`, `### Flaky tests`, then `### <further rules of the product>`;
5. `## Recipes`, one `### <level>` for each level of `## Levels`;
6. `## Not tested on purpose`;
7. `## Examples`;
8. `## Where in code`.

A required rule or section the product drops reads `none — <PREFIX-NN>` (WAY-171).

**What each section carries** (rule or example; for a rule, the product decision and invariant the
skill proposes):

- *Applies to* — every part of the product's map whose code the product's tests check, and every part
  holding test files; before the first test, the parts the product's plan gives tests (WAY-246, D6).
- `## When to read` — before writing or changing a test (WAY-246).
- `## Levels` — two tables. The levels: one row each, *Level* (the name the product uses) and
  *Decision* (the product decision that sets the level), with no column of its own for a definition:
  a level whose name means in the product something other than in the field is a term of the
  product's glossary, defined there by the resources a test of it may touch — files, network, a
  browser — and the table names that term and copies no definition, so the meaning stands once; a
  level whose name means what the field means takes no definition (WAY-240). The parts: one row for each part of *Applies to*, *Part* and one sentence of
  whether its complexity lies in computation or in connections (WAY-240). The tables hold no
  proportion of levels (WAY-238).
- `### Choosing the level` — rule. *Decision*: the adopting decision. *Invariant*: `none`. A test
  stands at the lowest level at which the break it names turns it red, unless going lower would mean
  replacing exactly what can break; the author of the change chooses in the cycle, naming the break,
  and the reviewer checks the choice against the guidelines; how to apply: the yes/no table of
  `raport_wytyczne_testow.md` §1, its four questions about a property test among them (do–undo, a
  simpler version, something kept after every step, a result easier to check than to compute), in
  English; no percentages (WAY-238).
- `### A lower test for a bug caught high` — rule. *Decision*: adopting. *Invariant*: `none`. A bug
  that only a high-level test or a human caught also gets a test at the lowest level that catches it
  (WAY-239).
- `### Where the expected value comes from` — rule. *Decision*: adopting, and the product's decision
  naming its documents that are sources (its decision log, glossary, task descriptions …).
  *Invariant*: `none`. The expected value of every test comes from one of: those documents; a
  relation the code under test does not compute (Q13); a crash counted as a failure; a human's
  judgement; never from what the code gives today, snapshots and characterization tests included;
  where the test's name does not show the source, a comment names it (a document's line, or a human
  and a date); the reviewer asks of each assertion where its value comes from (WAY-232).
- `### Test inputs and expected values` — rule. *Decision*: adopting. *Invariant*: `none`. WAY-228's
  rule as D4 words it, with its property-test clause, and the sentence moved from the coding template
  that which files a test names, so that a fixture or a builder cannot change underneath it, the
  template does not settle.
- `### Changing an existing test` — rule. *Decision*: adopting. *Invariant*: `none`. Changing an
  expected value, deleting a test, weakening an assertion, skipping or disabling a test are one
  category, each with its cause on the side of the data or the requirement and a pointer to the
  evidence, otherwise the reviewer reads it as masking a defect; how to apply: the list of
  weakenings — equality loosened to "contains", a count removed, a tolerance raised, a skip, a
  deletion (WAY-233).
- `### Behaviour, not implementation` — rule. *Decision*: adopting. *Invariant*: `none`. Assertions
  check the behaviour the rule or the task requires; the reviewer asks whether the code can be changed
  so that the required behaviour stays and the assertion breaks — yes means a detail; a check of the
  case's setup is allowed when it stands before the action, is marked as a precondition and checks a
  property of the case the requirement names, never a data structure; three deliberately different
  examples: a rule's index in place of a lasting identifier, the exact wording of a message where the
  requirement asks only for a refusal, the order of internal calls where only the result counts; no
  general exception for comparing a whole state (WAY-234; task *Context*).
- `### Trust boundaries` — rule. *Decision*: adopting, and the product's decisions on permissions.
  *Invariant*: the refusal invariant of each trust boundary of the product's map, each with a standing
  test that checks the refusal directly, takes the expected refusal from the product's decision on
  permissions and is seen failing once (WAY-08); a boundary that does not refuse today has its
  invariant marked violated (WAY-51); a boundary that is only the configuration of someone else's
  service stays with the review (WAY-235). This is the only required rule whose *Invariant* is not
  `none`. For authorization, the rule's text in `guidelines/testing.md` holds the table who ×
  resource × action → expected result, as the styleguide holds `## Roles`: each row names by
  identifier the product decision on permissions it comes from, those decisions grouped so that each
  keeps to three binding sentences (WAY-05), and the table copies no rationale. No decision holds the
  table (a decision has no place for one, `elements/decisions/template.md:20-38`).
- `### AI in tests` — rule. *Decision*: adopting, and the product's decision adopting each AI tool its
  tests use. *Invariant*: `none`. AI is no level; a test an AI wrote follows every rule; an exploring
  agent finds cases that become ordinary tests; an AI judge enters standing tests only where the
  behaviour cannot be checked by a plain comparison, its verdict is yes/no, it is checked on examples a
  human judged and has a pinned model version, and the guidelines say how they treat the spread of its
  results; a self-healing tool may fix only how an element is found, and changing an assertion or
  turning a red test into a skipped one is a change of `### Changing an existing test`; each AI tool
  the product uses has a product environment fact with its version and the date read (WAY-236).
- `### Flaky tests` — rule. *Decision*: adopting. *Invariant*: `none`. Re-running serves diagnosis,
  never turning the gate green; disabling or deleting such a test is a change of
  `### Changing an existing test` (WAY-243).
- Further rules — rule each, an invariant where a cheap test checks it on a convention of the code,
  otherwise `none` (WAY-168).
- `## Recipes` — for each level the same fields in this order, each field naming by identifier the
  product decision that carries it where it binds, and otherwise standing as an example (WAY-241); a
  field may read "as in `<level>`":
  1. *Purpose* — what the level is for and when not to use it;
  2. *Files* — where its files lie and how they are named;
  3. *Shape* — the name and build of a test: a sentence about behaviour, three phases, one behaviour,
     no logic in the test;
  4. *Doubles* — a real dependency where it is fast, deterministic and simple, then a working
     simplified version, then a stub or a mock; foreign types wrapped in an adapter of the product's
     own; the code under test never replaced; an assertion on a call only for an effect visible outside
     the product;
  5. *Data* — a value an assertion depends on stands in the test; shared setup only where nothing
     changes it;
  6. *Time and randomness* — clock and seed given from outside; waiting for an event with a limit in
     place of a fixed sleep;
  7. *Exemplar* — the level's exemplar test by path with the decision designating it; empty until one
     is designated (WAY-242);
  8. *Command* — the gate's one command and how it narrows to the level, a file or a test, where the
     gate can; `none` where it cannot (Q12, WAY-16);
  9. *Time limit* — a pointer to the configuration file that holds it, never the value.
  The defaults of fields 3–6 are what the template proposes; a product adopts or departs from them by
  decision (WAY-173).
- `## Not tested on purpose` — a section the template requires: one entry for each category of
  behaviour or code, never a single file or test, each naming the product decision whose binding
  sentences carry the condition under which the category is tested again and whose rationale gives
  the reason (WAY-05); `none` when
  nothing is excluded; a trust boundary never stands here (WAY-237).
- `## Examples` — example. The kinds of tests without value that no other rule carries: a duplicate
  of another test, a test of trivial code, a loop over nearly identical inputs (Q14, A15); nothing
  here binds.
- `## Where in code` — the configuration of the test tools, the directories of each level's tests and
  the exemplar tests, each a path git tracks, no value copied (WAY-171); before the product's first
  test it names what git already tracks of these and may hold no item, as the coding template's table
  of kinds keeps its header with no row.

**Writing the file** (for the cycle's author): take every level, source document, exemplar,
exclusion, departure and recipe field that binds from the task's settlements and the decisions its
foundation step wrote, never from memory (WAY-172); point to configuration and to tests, copy no
value; a choice the task did not settle stops the cycle at a blocked draft request (WAY-172).

### D4. WAY-228 and the coding discipline (open choice 2; item 3)

- **WAY-228 edited in place** (row 14). The question stays ("Where does a test take the input it
  asserts on and the value it expects?"). Its meaning: the testing template requires the rule — input
  and expected value written out wherever the code under test would compute either, only the compared
  side from the run; a property test takes its inputs from a test library's generator and its expected
  value from a relation the code under test does not compute — undoing the operation, an invariant's
  sentence, or a simpler version written from the requirement, not copied from the code — and a
  counterexample the library finds is kept as an ordinary test with values written out; a product
  departs only by a decision with its reason, and the rule binds from the task that writes its testing
  guidelines. Three binding sentences at most. *Relations*: derives from WAY-173 · derives from
  WAY-231. *Rationale*: the rule stands where an agent reads before writing or changing a test
  (WAY-246), no longer leaning on WAY-212. *Rejected* gains: the rule left in the coding guidelines —
  a test written apart from code would meet no rule; no property tests — a whole class of tests that
  check a relation over many inputs would be barred; WAY-228 left ambiguous for them.
  - Ways rejected: withdraw WAY-228 and write a new number — the same question gets a second number
    (WAY-19), and WAY-70's successor would point to a withdrawn entry; keep WAY-228 in coding with a
    narrowing decision for tests — contradicts Q9.
  - Cost if wrong: one entry reworded; no product adopted the rule (Q9), so no product migrates.
- **Coding template**: `### Test inputs and expected values` leaves the required form, the bullet on
  the order of the required rules (only the three standing checks remain) and "What each section
  carries"; the kinds of code are code of the product other than its tests (WAY-231), said where the
  template introduces `## Kinds of code` and the form of a kind.
- **Coding skill**: the step-4 bullet on the rule of tests goes; step 1's "kinds of code it already
  holds files of" excludes tests (WAY-231); "Where the skill works" gains that one task may carry the
  coding and the testing guidelines together, each skill leading its own matters (WAY-247). Its
  `description` stays unchanged.

### D5. The skill `maintain-testing-guidelines` (`product-guidelines/testing/SKILL.md`)

Frontmatter: `name: maintain-testing-guidelines`; a one-line description starting "Use when", on the
pattern of the two other skills (a product's tests need testing guidelines written before its first
test, its existing tests audited for them, or its testing guidelines refreshed or extended — leading
those matters of a testing-guidelines task's refinement with the human), passing the generator's
YAML checks. Its sections mirror `maintain-coding-guidelines` one for one, with no mode or step the
coding skill lacks (C4):

- Opening paragraphs: what it leads; where the rules stand (`product-guidelines/template.md`, the
  testing template, `elements/common/way_of_working.md`, `elements/common/critique/SKILL.md`, the
  skill of each element); where the-way lies (the checkout or worktree in the-way, `.the-way` in a
  product) and the `the-way-` prefix.
- **Where the skill works**: inside the refinement of one task whose outcome is testing guidelines —
  written, refreshed or extended — or the exemplar test of a level; takes over at `refine-task` step 3
  and hands back to step 4; finds guidelines through `product-guidelines/reading.md`; the task writing
  the missing file does not wait for its own output (WAY-215); one task may carry coding and testing
  guidelines together (WAY-247); a product that pinned the-way before this skill existed reaches it
  once a task moves the pin (D7). Table: the skill writes the task document and reports under
  `.runs/testing/`, never the foundation, the guidelines, tests or any tracked file (WAY-01, WAY-28);
  the cycle's author writes the product's entries, `guidelines/testing.md`, the test of each new
  invariant seen failing once (WAY-08), the instruction-file and part-map changes, never a meaning the
  task did not settle (WAY-172). The paragraph on how a meaning reaches the code only through the task
  document, as in both skills.
- **What reaches the task document** (B1, item 2): *To do* — write `guidelines/testing.md` from
  `.the-way/product-guidelines/testing/template.md` as its "Writing the file" gives; write the test of
  each new invariant, seen failing once; apply `maintain-instruction-files` for one line of the root
  `AGENTS.md`, outside the installer's block, naming `guidelines/testing.md` in backticks with the
  condition of writing or changing a test and no command (WAY-245, WAY-16); for the product's first
  guidelines, add `guidelines/**` to the part that directs agents through `update-part-map`
  (WAY-167); add a part step 1 found missing for planned tests through `update-part-map`; each item
  the audit calls for. *Questions to settle* — every choice of step 4 with the human's words and date.
  *Context* — the audit's charges with file and line, deferred ones with their reason, the research's
  sources with versions, what the audit could not see. *Settlements to record* — through
  `find-foundation-entries` in `refine-task` step 5; a part-map change is never a row.
- **Orchestrated mode**: as the coding skill's — turns carry the questions; research agents and the
  critique are requested from the project orchestrator, their reports under `.runs/testing/`; the skill
  starts no child agent.
- **0. Read**: both templates in full; `refine-task` and the task template; "How a skill asks" and
  "Critique before collective review"; the critique skill; the product's root `AGENTS.md` and every file
  under `guidelines/`; its foundation by "Reading the foundation", including the decisions of its
  technology, every decision already adopting a test tool, a level, an exemplar test or an exclusion,
  and the trust boundaries of its map.
- **1. Recognize** (WAY-248): the parts with tests or, before the first test, the parts the plan gives
  tests (a missing part a question of the task and an item of *To do*); what the product has — a test
  tool, levels, test directories, doubles, invariant tests — or nothing, said plainly; the modes,
  mirroring the coding skill's: no tests (step 2, so that the guidelines come before the first task
  that writes tests, WAY-244); tests and no guidelines (steps 2 and 3); a task that writes the first
  test of a level ("A new level" in step 3, the mirror of the coding skill's "A new kind"); existing
  guidelines refreshed or extended (steps 2 and 3). Extend what exists; a new test tool or a library
  of property tests is a technology choice, recorded as a question of the task, never settled
  (WAY-121).
- **2. Starting set** (WAY-249): one question of assessment for the human's preferences ("I do not
  know" is an answer); without them, research for the product's technology split into questions, each to a fresh agent with its report at
  `.runs/testing/<question>.md`, each source a page with its version; one fresh critic refutes every
  unsupported claim, the report ends with `critique: passed`; no fresh agent, no research — stop and say
  so; what research finds is proposed in step 4, never imposed.
- **3. Audit** (WAY-250), where tests exist: for each level, compare its tests and propose its
  exemplar test with one sentence of what the product gains; three to five charges, each with
  `file:line` and one sentence of its effect, deferred ones in *Context*; for each trust boundary of the
  map, whether it has a test of refusal. **A new level**: where the task writes the first test of a
  level, that test is the level's exemplar, and step 4 settles its path (WAY-242, C4). A choice read
  off the tests is a proposal until the human settles it; an existing choice kept becomes a decision
  whose rationale is the human's words or `unknown` (WAY-29).
- **4. Settle with the human**: *How to show* — every choice, a recommended one included, by its
  effect on the product, never by the name of a technique or a tool, a term of the field said in plain
  words before its first use, then the one question "How a skill asks" gives (WAY-174). *What it
  settles* — the levels and the product glossary entries of diverging names (WAY-240); the adopting
  decision and each departure with its reason (WAY-173); the product's documents that are sources of
  expected values (WAY-232); the binding fields of each recipe (WAY-241); each exemplar test (WAY-242);
  each exclusion with its reason and return condition (WAY-237); the product's decisions on
  permissions from which the authorization table's rows come (WAY-235); each AI tool and its environment fact (WAY-236). *Invariants* — the refusal invariant of
  each trust boundary with its test seen failing once, marked violated where the boundary does not
  refuse today by a foundation change the human accepts, its weak point said when proposed (WAY-235,
  WAY-51); an invariant for any other rule a cheap test checks (WAY-168). *Weak points* — named with
  their choice: an exclusion ages unless someone checks its return condition; the refusal rule is as
  good as the map's trust boundaries; a simpler version copied from the code makes a property test a
  mirror of it, which only the reviewer catches. *Critique* of the complete set before it is shown
  together (WAY-120). Each answer written before the next question.
- **5. Hand back**: check the document holds what "What reaches the task document" names and that no
  choice stands settled without the human's words; hand back to `refine-task` step 4.

### D6. Reading, refinement and breakdown (open choice 3; item 4)

**Selection: *Applies to* alone.** The shared reading selects `guidelines/testing.md` like every
non-kind file: read whole where its *Applies to* names an affected part. `## When to read` serves the
pointer of `AGENTS.md` and an agent outside the cycle, as the general coding file's condition does
today. WAY-213 stays as it is: its first clause ("every file whose *Applies to* names such a part")
already selects the file.

- Rejected: also checking `## When to read` ("before writing or changing a test") — the condition is
  judged before a diff exists, and a wrong "no" drops the file from an agent that then writes a test,
  the miss WAY-213 exists to prevent; it would add a second conditional mechanism beside the kind
  index. Testing guidelines as a row of the coding index — contradicts Q9 and row 1.
- Cost if wrong: an agent whose work touches a part with tests but writes none reads one more short
  file.

**What "a part with tests" means (row 20, read one way).** *Applies to* names every part whose code
the product's tests check and every part that holds test files. Rejected: only parts holding test
files — a change to the code of a part whose tests lie in another part would not select the file;
only parts whose code is tested — a change to test files alone would not. Cost if wrong: a wider
*Applies to*; no file goes unselected.

**`product-guidelines/reading.md`:**

- the opening sentence and "Name the affected work" add, beside "changes a user interface or writes
  code", whether the work writes or changes a test;
- "Distinguish the gaps", first bullet: test work in a product with no `guidelines/testing.md` lacks
  discipline guidelines, as a user interface with no styleguide does;
- "Distinguish the gaps", a new bullet shaped like the WAY-216 bullet (C4): where the work writes the
  first test of a level whose recipe in `guidelines/testing.md` has an empty *Exemplar*, its designation
  belongs to this task through `maintain-testing-guidelines`, with no separate exemplar wait;
- "Select and read" stays; the kind bullets stay, kinds being code other than tests (WAY-231).

**`project-level/task/skill/SKILL.md` step 3**: "Use `maintain-styleguide`,
`maintain-coding-guidelines` or `maintain-testing-guidelines` for their matters"; the first-level
exemplar-test case beside the first-kind case; one clause that a missing coding and a missing testing
guidelines may be one prerequisite task (WAY-247).

**`project-level/plan/skill/SKILL.md` step 2**: "each missing styleguide, general coding file or
testing guidelines"; one guidelines task may carry both a missing coding and a missing testing file
(WAY-247); a level's first exemplar test with the task writing its first test.

**WAY-214, WAY-215, WAY-218 edited in place** (row 16 and item 4; *Foundation entries*).

### D7. Installer (open choice 4; item 2)

**No new mechanism.** `SKILLS` gains `"maintain-testing-guidelines": "product-guidelines/testing/SKILL.md"`.
Evidence that a pin move brings it to a product that already pins the-way, such as `loop2`:

- `installation/install.py:343-346` (`plan`) builds an entry point for every name of `SKILLS` in both
  `.claude/skills/` and `.agents/skills/`; `file_action` (`:431-436`) gives `CREATE` for a path that
  does not exist, and `run` writes it (`:580-584`);
- `product_guidance` (`:147-162`) lists every name of `SKILLS`, so the block differs at the new commit
  and `agents_change` rewrites it in place (`:245-250`); every sibling entry point's list of names
  changes too and is rewritten as its own (`owned_entry_point`, `:291-305`);
- `stale_entry_points` (`:308-321`) deletes only the installer's own entry points of names no longer
  in `SKILLS`;
- `installation/test_install.py:278-319` (`test_moving_the_pin_rewrites_what_the_installer_owns_in_one_run`)
  adds `extra-skill` to `SKILLS` at a later commit and asserts that the move creates
  `the-way-extra-skill/SKILL.md` in both directories and rewrites the siblings and the block;
  `installation/README.md` "Moving the pin" says the same.

Ways rejected: a command or step of its own for pinned products — a second route beside the pin move
(WAY-34); nothing in the installer — the skill would never reach a product (item 2).
Cost if wrong: none found; the move is already tested.

**Trust boundary (WAY-48; `installation/install.py` is the part's boundary).** The change adds one
constant pair and no parsing. The skill's text is read from the-way's own commit (`committed`,
`:81-82`), never from the product. The only new product path it touches is the constant entry-point
path in both directories; the other text it changes — the `AGENTS.md` block and every sibling entry
point's list of names — goes through the paths the installer already writes, under the same checks.
The existing checks guard the new path before anything is written: `check_parents`
(`:283-288`) refuses a parent that is a symlink or not a directory; `owned_entry_point` refuses a file
there that is not the installer's own, a directory, a symlink or non-UTF-8 text ("Existing integration
file differs"). So a crafted file at that path cannot make the run write outside the installer's own
files. The tests show it for the new path: in each of `.claude` and `.agents`, a foreign file, a
directory and a non-UTF-8 file at `the-way-maintain-testing-guidelines/SKILL.md` stop the preview and
`--apply` with a non-zero exit, the tree byte for byte as before and nothing staged — as
`installation/test_coding_guidelines_installation.py:127-160` shows for the coding skill.

Tests and text:

- the exact counts `38` in `installation/test_coding_guidelines_installation.py:97` and
  `installation/test_styleguide_installation.py:91` become `40`, kept exact;
- a test of the testing skill's installation covering what the coding skill's test covers: preview
  lists both new entry points; `--apply` creates them byte-identical, with the skill's description and
  the `.the-way/product-guidelines/testing/SKILL.md` path; every sibling names
  `maintain-testing-guidelines`; the block names `the-way-maintain-testing-guidelines`; a repeated run
  changes nothing; the crafted-input refusals above;
- `installation/README.md`: the skill in the table's list of entry points and in the list of what the
  tests check.

### D8. Entry points and READMEs

- `python -B agent-instructions/skill_entry_points.py --write` after the skill exists, and the
  regenerated files committed: the two new entry points and every existing one, whose sibling list
  gains the name (invariant `skill-entry-points`).
- `README.md`: the `product-guidelines/` item names the testing discipline's directory beside the two
  others, and "Using the skills" names `product-guidelines/testing/`.

### D9. Rows onto the foundation (open choice 5)

| Row | Entry | How |
|---|---|---|
| 1, 15 | WAY-231 | new, one decision: one question — where the rules of a product's tests stand, and whether a test is a kind of code |
| 2–13 | WAY-232 … WAY-243 | new, one each, in row order |
| 14 | WAY-228 | edited in place (D4) |
| 16 | WAY-215, WAY-218 | edited in place |
| 17 | WAY-244 | new |
| 18 | WAY-174 | edited in place |
| 19, 20, 21, 22, 23, 24 | WAY-245 … WAY-250 | new, one each, in row order |
| 25 | no entry of its own (C3) | carried by WAY-233, WAY-235, WAY-236, WAY-237, WAY-238, WAY-241, WAY-243 |

- Row 21 is a decision of its own, not a sentence of WAY-215: WAY-215 already holds three binding
  sentences (WAY-05), and a new rule next to an existing decision is a new question (WAY-19).
- Rows 8 and 9 stay apart: the level of a test and what a bug caught high gets are two questions.
- Rows 22–24 stay apart, as WAY-210, WAY-211 and WAY-201 do for the coding skill.
- **Row 25 (C3).** `elements/decisions/template.md:40-42` and WAY-19 hold that "what do we take from X"
  is no question and that what such a list carries goes to the decisions that carry each rule; WAY-175,
  WAY-195 and WAY-222 were withdrawn for that reason. So each piece taken goes into the *Based on* of
  the decision that carries it — as an environment fact where WAY-90 calls for one, otherwise
  address, place, quoted passage and date: OWASP (refusal tests as a required check) → WAY-235; Google
  (a test changes only with its requirement) → WAY-233; Google (a real dependency before a double) →
  WAY-241; Open Mercato (the list of weakenings) → WAY-233; Limen (tests without value) → named with its
  address and passage in the *Rationale* of WAY-237, the decision on what is deliberately not tested,
  never in a *Based on*: the piece lands in `## Examples`, which carries no decision (WAY-168,
  withdrawn WAY-179), so no decision rests on it, and a *Based on* would send the search of a later
  change to the source (WAY-33) to a decision that does not depend on it;
  Anthropic (deterministic checks before an AI judge) → WAY-236; the
  10xDevs course (a section of what is deliberately not tested, each entry with a reason and a trigger
  to re-evaluate) → described in WAY-237's rationale with no pointer (WAY-27). Each piece left goes
  into the *Rejected* of the decision whose question it answers: a project test plan, a project risk
  map and proportions of levels → WAY-238; the red replacement of an old test → WAY-233; quarantine of
  flaky tests → WAY-243. The request names row 25 under *What this request settles* as tied to these
  decisions, with this reason.
- Choice weighed: rows 2–13 as one or a few decisions on "the template's rules of tests" — rejected:
  each rule is a question someone could answer otherwise (the styleguide's rules stand one per
  decision, WAY-176–WAY-180), and one decision could not hold them in three sentences. Cost if wrong:
  twenty entries where fewer would do; merging later rewrites references only inside the-way.

## Foundation entries

All decisions take *Scope* `product-guidelines` unless noted, *Origin* `none`, and stand at the end of
the log after WAY-230 in this order. Each derives from WAY-173 unless noted otherwise; the writer adds
the further relations named. Rationale and rejected options come from the task's answers and sources
(the task's rejected ways); wording is the writer's.

### New decisions

| No. | Row | Question (proposed) and meaning | Relations beyond WAY-173 | *Based on* (expected) |
|---|---|---|---|---|
| WAY-231 | 1, 15 | Where do the rules of a product's tests stand? — testing is a discipline of guidelines of its own: a product keeps `guidelines/testing.md`, written from the-way's testing template, and the-way's skill `maintain-testing-guidelines` creates and keeps it; a kind of code of coding guidelines is code of the product other than its tests, and the patterns of tests stand in the testing guidelines at their level | derives from WAY-167 | none |
| WAY-232 | 2 | Where does a test's expected value come from? — row 2 as D3 gives it | derives from WAY-228 | Konstantinou et al. as a new fact, if relied on |
| WAY-233 | 3 | What does a change to an existing test need? — row 3 | — | `impossiblebench-test-modification` · Google ch. 12 · Open Mercato checklist; *Rejected*: the red replacement |
| WAY-234 | 4 | What may a test's assertion check? — row 4, the precondition check included | — | Google ch. 12 |
| WAY-235 | 5 | How is a trust boundary of a product kept by its tests? — the template requires and the skill proposes a refusal invariant for each boundary of the map, its test seen failing once, for authorization a table in the guidelines' rule whose rows name the product's decisions on permissions, marked violated where the boundary does not refuse today, configuration of someone else's service left to review; *Scope* + invariants | derives from WAY-48 · WAY-08 · WAY-51 | OWASP cheat sheet |
| WAY-236 | 6 | How does AI enter a product's tests? — row 6 | — | Anthropic evals article; WebTestBench as a new fact, if relied on |
| WAY-237 | 7 | What does a product deliberately not test, and where is it said? — row 7, the return condition in the product decision's binding sentences and its reason in that decision's rationale | — | ISTQB; 10xDevs described in rationale; Limen named in rationale |
| WAY-238 | 8 | At which level does a test stand, and who chooses it? — row 8; *Rejected*: project test plan, risk map, proportions; *Scope* `product-guidelines, task-cycle, project-level`, since it binds who chooses in the cycle and that refinement holds no test plan (WAY-21) | — | Vocke · Microsoft Learn |
| WAY-239 | 9 | What does a bug caught only high get? — row 9 | derives from WAY-238 | Vocke |
| WAY-240 | 10 | How do a product's guidelines name its test levels? — row 10; a diverging name is an entry of the product's glossary defined by resources | derives from WAY-226 | none |
| WAY-241 | 11 | What does a level's recipe hold? — row 11: the same fields for each level, binding fields naming a product decision, the command field the gate's command with its narrowing or `none`, the time limit a pointer, no separate commands | derives from WAY-16 · WAY-168 | Google ch. 13 |
| WAY-242 | 12 | How is a level's exemplar test designated? — by a product decision, as a kind's exemplar is (C4): where tests of the level exist, the skill's audit proposes it from their comparison; where none exists, the task writing its first test designates it, approved in refinement; the field stays empty until then; designating another is a change of that decision | derives from WAY-200 · WAY-172 | none |
| WAY-243 | 13 | How is a flaky test treated? — row 13; *Rejected*: quarantine, automatic re-runs in the gate | derives from WAY-68 · WAY-233 | Google ch. 11 |
| WAY-244 | 17 | When do a product's testing guidelines come into being? — the skill proposes before the first task that writes the product's tests | — | none |
| WAY-245 | 19 | How does a product's instruction file lead to its testing guidelines? — one line of the root `AGENTS.md`, outside the installer's block, naming `guidelines/testing.md` with the condition of writing or changing a test, written as the skill of `instruction-files` gives a pointer, with no command; *Scope* + instruction-files | derives from WAY-128 · WAY-129 · WAY-167 · WAY-16 | none |
| WAY-246 | 20 | Which parts do testing guidelines apply to, and when are they read? — *Applies to* names every part whose code the tests check and every part holding test files, before the first test the parts the plan gives tests; read before writing or changing a test (D6) | — | none |
| WAY-247 | 21 | May one task write a product's coding and testing guidelines together? — yes; each discipline's skill leads its matters in that one refinement; *Scope* + project-level | derives from WAY-215 | none |
| WAY-248 | 22 | What does the testing skill look at first? — what the product has; extend it; a new test tool or a library of property tests is a technology question of the task | derives from WAY-121 | none |
| WAY-249 | 23 | Where does the testing skill's starting set come from? — the human's preferences, else research with sources, a fresh agent per question and critique before the human; no research again at a refresh where the human has preferences (row 23 carries none) | derives from WAY-122 · WAY-120 | none |
| WAY-250 | 24 | How does the testing skill's audit of a product with tests end? — for each level a proposed exemplar test and three to five charges with `file:line` and one sentence of effect; for each trust boundary whether it has a refusal test | derives from WAY-242 | none |

Each new decision carries a *Verification* pair of examples; none names an invariant of the-way. A
writer who finds a row better carried by an existing entry, or two rows that are one question, stops
and asks through the orchestrator.

### Decisions edited in place

- **WAY-228** (row 14) — D4.
- **WAY-174** (row 18) — the skills of guidelines that put every choice to the human in plain words
  include `maintain-testing-guidelines`, which shows testing guidelines' choices by their effect on the
  product, never by the name of a technique or a tool.
- **WAY-215** (row 16) — a task writing or changing a test in a product with no testing guidelines
  waits in refinement as the other two disciplines' tasks do; *Relations* gain WAY-244 only (WAY-247 derives from WAY-215, so WAY-215 names it not; a pair of
  entries deriving from each other would make each the higher of the other).
- **WAY-218** (row 16) — breakdown places a task for missing testing guidelines before the tasks that
  need it, one guidelines task may carry coding and testing guidelines (WAY-247), and a level's first
  exemplar test goes with the task writing that level's first test (WAY-242); *Relations* gain WAY-244,
  WAY-242.
- **WAY-214** (item 4) — refinement identifies, besides parts, user interfaces, code and kinds of code,
  whether the work writes or changes tests; the consequence of an absence follows when testing
  guidelines come into being (WAY-244 beside WAY-184 and WAY-209).
- Not edited: WAY-167, WAY-171, WAY-173, WAY-213 (D6), WAY-09, WAY-198, WAY-200.

### Glossary

- `exemplar` — edited in place (D1).

### Environment facts

- New facts only where a decision's *Based on* rests on a finding about agents or models (WAY-90):
  expected for WAY-232 (LLM-written oracles capture the implementation) and, if relied on, WAY-236
  (WebTestBench); WAY-233 names the existing `impossiblebench-test-modification`. Each new fact
  through `record-environment-fact`, its source the publisher's page (WAY-80).

### Part map and invariants

- Part map: no change (D2).
- Invariants of the-way: none new or changed; `skill-entry-points` covers the new skill through the
  generator.
- Withdrawn identifiers: none.

## Left to the maker

- The wording of every template, skill and README sentence and of every entry, within the meanings
  above; the English rendering of the yes/no table of `raport_wytyczne_testow.md` §1.
- The exact labels of the recipe fields and how a binding field names its decision (an identifier
  beside the field's text, or a trailing field), as long as each binding field names its decision by
  identifier and a field naming none reads as an example.
- Whether the testing skill's installation test is a new file or the coding skill's test generalized
  over both skills, as long as every case of D7 runs for the new path.
- Whether `installation/test_install.py` `NAMES` gains the skill.
- The *Good* and *Bad* lines of each required rule, or `none`.
- The order of the work, the slices, and the checks run: at least `python -B gate/run_tests.py
  installation`, `agent-instructions` and `elements/common`, the entry-point generator showing
  "entry points are current", `python -B elements/common/foundation_check.py` on the-way, and the whole
  gate on the change as it goes into the request.
