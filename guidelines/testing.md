# Testing guidelines — the-way

- **Discipline:** testing
- **Applies to:** elements-common · part-map · relation-model · project-level · task-cycle · gate · agent-instructions · instruction-files · installation · process-audit · product-guidelines

## When to read

Before writing or changing a test of the-way, in a part named above, or deleting one. These are the
testing guidelines of the-way's own tests, which WAY-392 adopts.

## Levels

| Level | Decision |
|---|---|
| `unit` | WAY-393 |
| `files test` | WAY-393 · the glossary term `files test` |
| `git test` | WAY-393 · the glossary term `git test` |
| `repository test` | WAY-393 · the glossary term `repository test` |
| `e2e` | WAY-393 |

| Part | Where its complexity lies |
|---|---|
| `elements-common` | In computation: its script decides, by rules over text, whether the identifiers, references and files of a foundation hold together. |
| `part-map` | In computation: its test decides whether the imports of the code stay within the dependencies the map allows. |
| `relation-model` | In computation: it computes the fingerprint of a text. |
| `project-level` | In computation: its checks decide, by rules over text, whether a project definition and a project plan keep their form and whether the evidence for a task's state holds. |
| `task-cycle` | In computation: its scripts count the stages, measures and times of a cycle and check the form of the files it keeps. |
| `gate` | In its connections: it starts the test directories as processes and joins their reports. |
| `agent-instructions` | In its connections: it joins the skills, the definitions of agent types and the instructions that sessions read to the files they stand for. |
| `instruction-files` | In computation: its script decides, by rules over text, whether an instruction file keeps the rules and whether the paths it names exist. |
| `installation` | In its connections: the installer joins a product's repository, its pinned checkout, its links and its instruction files. |
| `process-audit` | In computation: its command counts the figures of the audit from the records of cycles. |
| `product-guidelines` | In computation: its test reads the text of the skills and checks each reference in it against the files. |

## Rules

### Choosing the level

- **Decision:** WAY-392 · WAY-393
- **Invariant:** none
- **Good:** none
- **Bad:** none

A test stands at the lowest level at which the break it names turns it red, unless going lower
would mean replacing with a double exactly what can break. The author of a change chooses which
behaviour gets a permanent test and at which level, and names the break each test catches; the
review checks the choice against these guidelines. The guidelines give no proportion of levels. The
table asks a question about the behaviour and gives the test a yes calls for.

| Question about the behaviour | If yes |
|---|---|
| Is it a rule or a calculation that needs no file, process or git? | a unit test |
| Does it need the resources of a files test and no more? | a files test |
| Does it need the resources of a git test and no more? | a git test |
| Is it a property of the real checkout of the-way itself, which a repository test checks? | a repository test |
| Is it a path of a session through several scripts, whose break a person would report as "the process does not work"? | one e2e test for each such path |
| Was the bug caught only by a test of a higher level or by a human? | a test at the lowest level that catches the bug |
| Does the code only copy or pass data on, with no rule of its own? | no permanent test, unless it lies on a trust boundary |
| Can the test not be kept in a state where it gives the same result on the same code every time? | no permanent test; the review, or a check made once |

### A lower test for a bug caught high

- **Decision:** WAY-392
- **Invariant:** none
- **Good:** none
- **Bad:** none

A bug that only a test of a higher level or a human caught also gets a test at the lowest level that
catches it.

### Where the expected value comes from

- **Decision:** WAY-392 · WAY-394
- **Invariant:** none
- **Good:** a test of an exit code names, in a comment at the value, the description at the head of its script that gives it
- **Bad:** a test takes its expected value from a constant or a function of the code it checks

The expected value of every test comes from one of: the sources WAY-394 names; a relation the code
under test does not compute; a crash counted as a failure; a human's judgement. It never comes from
what the code gives today, snapshots and characterization tests included. Where a test's name does
not show the source of a value, a comment in the test names it, by the line of the document or by
the human and the date. The review of a change asks of each assertion where its value comes from.

### Test inputs and expected values

- **Decision:** WAY-392
- **Invariant:** none
- **Good:** none
- **Bad:** none

A test takes the input it asserts on and the value it expects written out, wherever the code under
test would otherwise compute either; only the side it compares against comes from the run. The
review of each change compares its tests with this rule.

### Changing an existing test

- **Decision:** WAY-392
- **Invariant:** none
- **Good:** none
- **Bad:** none

Changing the expected value of an existing test, deleting a test, weakening an assertion, and
skipping or disabling a test are one kind of change, each made with its cause on the side of the
data or of the requirement and a pointer to the evidence of that cause. The review reads such a
change made without them as masking a defect. The ways a test is weakened: equality loosened to
"contains", a count removed, a tolerance raised, a skip, a deletion.

### Behaviour, not implementation

- **Decision:** WAY-392
- **Invariant:** none
- **Good:** none
- **Bad:** none

A test's assertions check the behaviour its rule or its task requires; a detail of how the code
carries it out that the requirement does not ask for is no condition of the test passing. The review
asks of each assertion whether the code could change so that the required behaviour stays and the
assertion breaks; a yes marks a detail. A check of the case's setup is allowed where it stands before
the action, is marked as a precondition and checks a property of the case that the requirement
names, never the structure of the data that builds the case. Three details an assertion does not
pin: a rule's index where a lasting identifier would serve the same behaviour, the exact wording of a
message where the requirement asks only for a refusal, and the order of internal calls where only
the result counts. No exception allows comparing a whole state.

### Trust boundaries

- **Decision:** WAY-392
- **Invariant:** readiness-check-refuses-non-utf-8 · project-plan-form · project-plan-state-evidence · cycle-stages-refuses-crafted-names · cycle-measures-refuses-nested-line · gate-times-refuses-impossible-entry · audit-count-refuses-record-links · check-instructions-refuses-outside-links · installation-paths-through-links
- **Good:** none
- **Bad:** none

Each trust boundary the part map names has at least one invariant that the boundary refuses crafted
input, checked by a permanent test that checks the refusal directly and is seen failing once. The
sentence of the invariant gives the expected refusal. A boundary that does not refuse today has its
invariant marked violated; a boundary that is only the configuration of someone else's service
stays with the review of each change that touches it. The-way has no users and no permissions, so
the table of who, which resource and which action holds no row.

| Who | Resource | Action | Expected result | Decision |
|---|---|---|---|---|

### AI in tests

- **Decision:** WAY-392
- **Invariant:** none
- **Good:** none
- **Bad:** none

AI is no level of test: a test an AI wrote follows every rule of these guidelines, and an agent
exploring the running product finds cases that become ordinary tests. An AI judge enters a
permanent test only where the behaviour cannot be checked by a plain comparison, its verdict is yes
or no, it has been checked on examples a human judged and it runs on a pinned version of its model;
a decision of this log adopts the tool first, and the guidelines then say how they treat the spread
of its verdicts. A tool that heals a test by itself changes only how the test finds what it acts
on; a changed assertion or a red test turned into a skipped one is a change of
`### Changing an existing test`.

### Mutation testing

none — WAY-402

### Flaky tests

- **Decision:** WAY-392
- **Invariant:** none
- **Good:** none
- **Bad:** none

Running a flaky test again serves only the diagnosis of what makes it flaky, never making a run of
the gate pass; disabling or deleting such a test is a change of `### Changing an existing test`.

## Recipes

### unit

- **Purpose:** a rule or a calculation of a script, checked with no file, process or git; not for behaviour that needs more, which belongs to a test of a higher level (WAY-395)
- **Files:** the tests are files `test_*.py` in the directory of the part, beside the script they test, under `unittest` (WAY-395)
- **Shape:** a test is named by a sentence about the behaviour it checks, goes in three phases — set up, act, assert — checks one behaviour and holds no logic
- **Doubles:** a double only of the clock and of what a test cannot do on a git repository it builds in a temporary directory; git and the file system are real and stand in a temporary directory (WAY-395)
- **Data:** the values a test depends on are written out in it, each with its source in a comment (WAY-395)
- **Time and randomness:** the test gives the script its time, by replacing the clock function of the script in the process of the test or by giving a fixed time to a script that takes one, and no test waits a fixed time for another process (WAY-395)
- **Exemplar:** `relation-model/test_fingerprint.py`, the test `Fingerprint.test_a_tab_is_kept` (WAY-395 · WAY-396)
- **Command:** `python -B gate/run_tests.py <directory>`; the gate narrows to a directory and no further (WAY-395)
- **Time limit:** none — WAY-395

### files test

- **Purpose:** the behaviour of a script that depends on the files it reads or writes, or on its running as a process; the test starts no git, and a rule that needs neither is a unit test (WAY-395)
- **Files:** as in `unit`
- **Shape:** as in `unit`
- **Doubles:** as in `unit` (WAY-395)
- **Data:** as in `unit`
- **Time and randomness:** as in `unit`
- **Exemplar:** `task-cycle/test_cycle_measures.py`, the test `RewriteEdgesTest.test_a_rewrite_of_2000_tokens_is_not_counted` (WAY-395 · WAY-397)
- **Command:** as in `unit`
- **Time limit:** none — WAY-395

### git test

- **Purpose:** the behaviour that depends on a git repository, which the test builds in a temporary directory; not for a property of the real checkout, which a repository test checks (WAY-395)
- **Files:** as in `unit`
- **Shape:** as in `unit`
- **Doubles:** the repository is built in a temporary directory and nothing but the clock is replaced (WAY-395)
- **Data:** as in `unit`
- **Time and randomness:** as in `unit`
- **Exemplar:** `project-level/test_plan_state_invariant.py`, the test `PlanStateEvidence.test_fresh_remote_record_composes_both_transitions` (WAY-395 · WAY-398)
- **Command:** as in `unit`
- **Time limit:** none — WAY-395

### repository test

- **Purpose:** a property of the repository itself that its real checkout shows; not for behaviour that a repository built in a temporary directory shows as well, which is a git test or a files test (WAY-395)
- **Files:** as in `unit`
- **Shape:** as in `unit`
- **Doubles:** the checkout is real (WAY-395)
- **Data:** as in `unit`
- **Time and randomness:** as in `unit`
- **Exemplar:** `elements/common/test_elements_pending_marker.py`, the test `TrackedFilesUnderElementsTest.test_no_tracked_file_under_elements_holds_the_pending_marker` (WAY-395 · WAY-399)
- **Command:** as in `unit`
- **Time limit:** none — WAY-395

### e2e

- **Purpose:** a whole path of a session through several scripts, whose break a person would report as "the process does not work", one test for each such path; not for a rule that a test of a lower level catches (WAY-395)
- **Files:** as in `unit`
- **Shape:** as in `unit`
- **Doubles:** as in `unit` (WAY-395)
- **Data:** as in `unit`
- **Time and randomness:** as in `unit`
- **Exemplar:** `process-audit/test_audit_count.py`, the test `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` (WAY-395 · WAY-400)
- **Command:** as in `unit`
- **Time limit:** none — WAY-395

## Not tested on purpose

- what an agent does when it follows a skill: the tests check the form of the texts of the skills and their consistency (WAY-401)

## Examples

### Tests without value

A test that duplicates another test, a test of trivial code and a loop over nearly identical inputs
are tests without value that no rule above carries. Nothing here binds.

### Mutating the code in the head

Before finishing a change, its author mutates the code in their head — a wrong constant or branch, a
missing side effect, an empty return, unchecked empty or hostile input — and treats a mutation no
test catches as behaviour left unprotected. WAY-402 departs from the mutation tool of the template
and keeps this check (WAY-253). Nothing here binds.

## Where in code

- `gate/run_tests.py`
- `relation-model/test_fingerprint.py`
- `task-cycle/test_cycle_measures.py`
- `project-level/test_plan_state_invariant.py`
- `elements/common/test_elements_pending_marker.py`
- `process-audit/test_audit_count.py`
- `elements/common/`
- `elements/part-map/`
- `relation-model/`
- `project-level/`
- `task-cycle/`
- `gate/`
- `agent-instructions/`
- `instruction-files/`
- `installation/`
- `process-audit/`
- `product-guidelines/`
