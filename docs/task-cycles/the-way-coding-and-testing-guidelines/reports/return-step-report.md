# Report — the return step

**Status:** done with concerns (the concerns are listed below; none needs the human's answer before the merge).

**Commits:** `3cf54a5` ("Name the test of the counting of a function in WAY-385 by the clause tests and a line decision"), on `task/the-way-coding-and-testing-guidelines` after `f0482d0`. One commit; no other change.

**Files changed:** `foundations/decisions.md` (+5 / -4, the *Verification* of WAY-385), `agent-instructions/test_size_invariant.py` (+1, one comment line `decision: WAY-385 "..."`).

## Checks (command, exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (whole, before and after the edit) | 0 (`0 errors`) |
| the same with the quotation of the new line `decision:` altered to "81 lines" (mutation, restored) | 1 line `agent-instructions/test_size_invariant.py:58: the quotation stands in no binding sentence of WAY-385`, then 0 after the restore |
| `python -B gate/run_tests.py agent-instructions` | 0 (37 tests, `OK (expected failures=2)`) |
| `python -B gate/run_tests.py elements/part-map` | 0 (40 tests) |
| `python -B gate/run_tests.py elements/common` | 0 (242 tests) |
| `ruff check --config ruff.toml --no-cache --ignore-noqa` over the ten directories (pinned 0.17.1 of the main checkout) | 1, 25 reports (the violated invariant `ruff-blocking-rules` stands; none in the exemplars) |

The full gate was not run.

## Foundation compared with code

### Entries the change writes, changes or withdraws

| Entry | Compared with | Result |
|---|---|---|
| WAY-379, WAY-392 (*Scope*) | `git ls-files '*.py'` by directory | the eleven parts with Python code (`agent-instructions`, `elements-common`, `part-map`, `gate`, `installation`, `instruction-files`, `process-audit`, `product-guidelines`, `project-level`, `relation-model`, `task-cycle`) are exactly the *Scope*; both tests of `PARTS` (linter, size) fail on a tracked `.py` file outside it. Matches. |
| WAY-380 | `ruff.toml`, the fact `ruff-default-rules`, the test of the linter | `select` holds 389 distinct codes = the 407 of the fact less the 18 of the decision, none of the 18 in it (script, exit 0); `preview = false`, `target-version = "py314"` (`.python-version` 3.14), `required-version`; the test runs with `--ignore-noqa`. Matches. |
| WAY-381 | `requirements-quality.in/.txt`, README "Installing the linter", `tests.yml` | `.in` holds `ruff==0.17.1` and `--only-binary`, `.txt` holds the sums, the README tells the environment `.runs/quality-venv`, CI gains one step. Matches. |
| WAY-382, WAY-383, WAY-384 | `guidelines/coding.md` | the eight headings read `none — WAY-382/383/384` and nothing else. Matches. |
| WAY-385, `function-and-file-size` | the counting of `test_size_invariant.py` run on the head | 11 functions and 3 files over (`audit_count.py` 3310, `cycle_stages.py` 1183, `foundation_check.py` 1003); see "The three files" below. One change made. |
| WAY-386 to WAY-391 | `guidelines/coding-<kind>.md` tables, the exemplar files, the invariants | each exemplar is listed `exemplar` beside its decision; `cycle_measures.py`, `skill_entry_points.py`, `tracked_private_paths_check.py` give no report of the linter; `skill_entry_points.py` ends with exit 2 at a missing `name:` or `description:`. WAY-389 as narrowed by the fix ("other than a report that the human names with `--report`") equals the invariant and the kind's guidelines. Matches. |
| WAY-393 to WAY-400 | `guidelines/testing.md`, the five exemplar tests | each test exists under the named class and method (grep, five hits); the git exemplar builds its repository in a temporary directory with git's user configuration shut out; the e2e file runs git with `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM` set (WAY-400). The table of levels names the three terms and copies none. Matches. |
| WAY-395 | the recipes, the tests | *Time limit* reads `none — WAY-395` in five recipes; the *Command* is the gate's. One looseness, not changed: the tests of `gate_times.py` give the time by replacing the script's clock function in the test's own process (a double of the clock, allowed by *Doubles*), where the sentence says "as the option `--today` gives it" (`gate_times.py` has no such option; the plan's *Choices* row on that chose this). |
| WAY-401, WAY-402 | `## Not tested on purpose`, `### Mutation testing`, `## Examples` | read `WAY-401` and `none — WAY-402`. Matches. |
| WAY-09 | `foundations/part_map.md`, README | the sentence names `guidelines/` and `agent-instructions` holds `guidelines/**`; the invariant `repository-file-location` and the check agree. Matches. |
| WAY-328 | the list of withdrawn numbers | the row stands with successors WAY-379 · WAY-392; no text in the foundation, the guidelines or the README names WAY-328 but that row (grep). Matches. |
| WAY-344, WAY-363 | their text | the sentence of the *Rationale*, the item of *Rejected* and the example of *Verification* speak of the state after the guidelines. Matches. |
| WAY-38, `script-subprocesses` | `test_linter_invariant.py` (starts the pinned Ruff from the environment, `git rev-parse` for its place), `test_size_invariant.py` (starts git) | the added sentence covers the one program started beyond git and the interpreter. Matches. |
| `ruff-blocking-rules`, `generator-writes-only-with-write`, `repository-changer-acts-only-when-told`, `command-runner-passes-exit-code`, `shared-module-import-runs-nothing` | the cited tests | each sentence says what its test checks (the tests read: `--ignore-noqa` over ten directories; both generators without `--write` list a file to create, to change and an orphan and change nothing; the three changers' preview and declined confirmation; exit codes 2, 3, 255 and 128 + signal; the import in a new process with an open empty input). `Violated: yes` stands for `ruff-blocking-rules` (25 reports) and `function-and-file-size`. Matches. |
| the six refusal invariants (`readiness-check-refuses-non-utf-8`, `cycle-stages-refuses-crafted-names`, `cycle-measures-refuses-nested-line`, `gate-times-refuses-impossible-entry`, `audit-count-refuses-record-links`, `check-instructions-refuses-outside-links`) | the six cited tests (plus the second clause test of `gate_times`) | each sentence equals what its test asserts (exit 2 and the message; eleven cells and only well-formed names; exit 2, `Error:`, file and line, no output; entries deleted and counted for nothing; a link out of the record gives `unknown`; a link out of the repository neither read nor listed). Matches. |
| `files test`, `git test`, `repository test` | `guidelines/testing.md`, the whole foundation | the headings are used in the table of levels and the recipes and nowhere else with another meaning (grep over every `.md` outside `.runs`). Matches. |
| `ruff-default-rules`, `ruff-required-version` | `ruff.toml`, the decisions | 407 codes in the fact; the source passage was checked by the entries step. Matches. |

### The part map of the touched parts

- `agent-instructions`: its sentence now names "the guidelines of the-way's own code that those instructions point to"; *Files* holds `guidelines/**`; its *Depends on* lists `repository`, which the linter test's reading of `ruff.toml` needs; `elements/part-map` passes (40 tests, exit 0).
- `repository`: *Files* holds `ruff.toml`, `requirements-quality.in`, `requirements-quality.txt`; the sentence ("the files that configure the repository itself rather than any one part") covers them.
- `README.md` has one line each for `guidelines/` and the three linter files (the reviewer's finding, fixed by `f0482d0`). `AGENTS.md` has the two pointers (WAY-212).
- The other touched parts (`task-cycle`, `process-audit`, `project-level`, `installation`, `instruction-files`, `elements-common`, `relation-model`, `gate`) changed tests and, in `task-cycle` and `agent-instructions`, two scripts; no sentence, *Files* pattern, *Depends on* or trust boundary of theirs is made false (the nine trust boundaries of the map equal the nine invariants of `### Trust boundaries`). No change to the map.
- The External context table: the installation of Ruff from wheels is no exchange in which code of the-way takes in data, so no row is added (the template ties a row to the recording of a trust boundary).

### The three files over 1000 lines

At the head: `process-audit/audit_count.py` (3310), `task-cycle/cycle_stages.py` (1183) and `elements/common/foundation_check.py` (1003). The last was 989 lines at the commit of the review of the foundation (`21ecb62`), as `cycle_stages.py` was 1009 and `audit_count.py` 2991, and was 1003 already at the base `2d59321`; the change does not touch it. The rationale of WAY-385 says "at the commit of the review of the foundation ... 11 functions and 2 files over" and *Rejected* gives the other counts "in the same run": both are measurements of that commit, so they are true as dated. No entry names the number of files over a threshold as a state of the product, and the invariant `function-and-file-size` (`Violated: yes`) holds the rule whole, so the third file is inside what it holds. I changed nothing for it. A reader who takes "2 files" for the state at the merge finds the third in the failure of the test, which names every file over.

### Searches not found or unclear, and the concerns of the reports

- *The order of the plan's Choices*: I did not find a concern of the reports that names an order of the *Choices*; the rows of *Choices* read in plan order match what the slices did (the move before an edit is waived by answer 11; the linter and the size test read eleven parts). Left.
- *Cause labels of slice 19* (`slice_size.py` line 162 labelled 16, `plan_state.py` line 478): they stand in the task's Context, not in an entry or a guideline; the statuses `do not copy` stand against the code. No entry says a cause number. Left.
- *Glossary headings*: `files test`, `git test`, `repository test` (not the bare words). Accepted; no use of the bare words in the foundation.
- *The part-map sentence of `agent-instructions`*: written by the fix; checked above.
- *Sentences of the entries beyond a row* (entries report, concern 6): WAY-379/392 upkeep sentence is enforced by the two tests of `PARTS`, so it is true of the code; WAY-383, WAY-382, WAY-393 (the e2e description, true of the exemplar), WAY-388 to WAY-391 (each kind's rule in the binding sentence) match the guidelines and the invariants.
- *Slices 17 to 23 and the Coverage* (unread by the entries step): compared with what they wrote. Slice 17: the size test has the two tests and the cited expected failure (a third, the coverage of `PARTS`, from the fix). Slices 18 to 20: the six kind files; statuses as the plan gives; `## Rules` of `check` and `measuring-report` read `none — WAY-386/387`. Slice 21: `guidelines/coding.md` has the six kinds, the linter rule naming WAY-380 · WAY-381 and `ruff-blocking-rules`, the eight `none —` headings, the size rule, the two rules of the whole of the code (rows 16 and 17), the 18 examples with the names the tool gives, no mention of WAY-328. Slice 22: `guidelines/testing.md` has the five levels with the glossary terms, the table of parts (the row of `product-guidelines` is the orchestrator's proposal and was left as it stands), the nine invariants of the trust boundaries with an empty authorization table, `### Mutation testing` reading `none — WAY-402`, five recipes with `none — WAY-395` as *Time limit*, `## Not tested on purpose` naming WAY-401. Slice 23: the two pointers. Every row of *Settlements to record* (1 to 34) has its place: rows 5, 16, 17 and 24 in code, README and guidelines; the rest in the entries.
- *The plan's Coverage "Row 24"* and the part of the table for `task-cycle`: the plan chose computation for it (it has both); matches the task's row.

## What I wrote or changed, each

- **Decisions written or changed:** WAY-385 only — its *Verification* now reads "invariants: function-and-file-size. tests: that a function is counted with the functions nested in it and that a method is a function. For what the invariant and the test leave, an agent compares a change with the decision:" and the example "the test counts a function with no regard to the functions nested in it" is removed from *violates*, because a test holds that part. The test `Counting.test_a_function_counts_the_functions_nested_in_it_and_a_method_is_a_function` carries the line `decision: WAY-385 "A function of a script of the-way has at most 80 lines, counted with the functions nested in it"`; the foundation check accepts it and, with the quotation altered, reports it (the mutation above).
- **Invariants written or changed:** none. (No rule that the task, a decision or the human sets lacks one; none written for behaviour that merely has no invariant.)
- **Environment facts written or changed:** none. I weighed two candidates and wrote neither: (1) pip's hash checking (the sums of WAY-381 let an installation be verified): WAY-381's version claim rests on `ruff-required-version`, and the decision would stand if pip stopped checking, since the sums keep their other use; I found no pinned edition of pip's documentation (the versioned address of 25.3 on the documentation host answers 404, only `stable` exists), only the source file at the tag `25.3`; (2) the flag `--ignore-noqa`: it is how a tool behaves under the runner's configuration, which the template says is no fact an invariant rests on (WAY-73), and WAY-203 already carries the rule. If the human meant either as a fact, each is one entry and a *Based on* line of WAY-381 or WAY-380.
- **Glossary terms written or changed:** none (the three terms stand as the foundation step wrote them; the words `exemplar` and `standing check` already have entries; no other word the change uses is narrower than the field's in a sentence read differently).
- **Part-map changes:** none (the lines of E39 and E40 and the sentence stand as slices 1 and 18 and the fix wrote them).
- **Projected entries and rows written or changed:** none missed; rows 1 to 34 each stand in their place (above).
- **A choice that binds after the merge (WAY-36) with no entry:** none found.

## Concerns for the orchestrator

1. **Answer 20 and WAY-253** (the entries report's concern 3, still open): the task's answer says "the reviewer checks it in the head (WAY-253)"; WAY-253, which WAY-402 cites, and the skill of the change say the author does. WAY-402 and `guidelines/testing.md` follow WAY-253. If the human meant the reviewer, WAY-253 changes too.
2. **"Ten parts" became eleven** in all entries (entries report, concern 1); the removal is described there.
3. **A flaky test outside the findings:** `gate/test_run_tests.py::DirectoriesAtOnce::test_a_number_of_jobs_limits_the_directories_that_run_at_once` fails about 5 runs in 40 at the base as at the head (the fix report); it can turn the one run of the gate red. Not touched.
4. **WAY-395's *Time and randomness* looseness** (above) is a wording question, not a fault of the code.
5. **Duplicated example in WAY-380:** its pair still names "the test of the invariant runs Ruff with the flag ..." and "a comment that turns a blocking rule off stays in a file", which the invariant `ruff-blocking-rules` already holds; I left them, since the method asks the removal for a part a *test* holds by the clause `tests:`, and a held invariant is named by `invariants:` with "for what the invariant leaves".

## Reaches beyond the handoff

- `elements/decisions/template.md` (the *Verification* section, whole in part), `elements/environment-facts/template.md` and `elements/environment-facts/skill/read.md`, `elements/part-map/template.md` (the external context), `elements/glossary/skill/SKILL.md`, WAY-95 and WAY-321: to decide the clause `tests:`, the two candidate facts, the External context and the glossary.
- `https://raw.githubusercontent.com/pypa/pip/25.3/docs/html/topics/secure-installs.md` and `https://pip.pypa.io/en/25.3/...` (404) and `.../en/stable/...`: to see whether a fact of pip's hash checking has a frozen source. Nothing was written from it.
- The reports of all stages (their concerns and *Searches not found*), the task's *Questions to settle* (answers 8 to 11, 19 to 23), `foundations/part_map.md`, `foundations/glossary.md` headings, `foundations/environment_facts.md` headings.

## Working copies

`.runs/return-step/pipdoc/` (the pip documentation pages I downloaded to look for a frozen source of the candidate fact): stood in `.runs\return-step\` and was removed (`rm -rf`); nothing else was made; nothing is kept in `reports/` beside this report.

## Unread material

- `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`: read the *Settlements to record*, *Decisions in play*, *Human actions*, *Questions to settle* answers 6, 7, 8 to 11, 19 to 23 and 25 in part; the *Context* (lines 209 to 447) not read except the lines the executors quote; *To do* lines 25 to 47 not read.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md`: lines 1 to 648 (slices 1 to 16 and the table) not read; I read 649 to 1042.
- `decision_index_orchestrator.md`, `cycle.md`, `sections.md`, `plan-size.md`: not read.
- The reports of the stages: only their *Searches not found or unclear*, *Questions*, *Concerns* and *Problems* sections (by a script), the whole of `entries-report.md`, `executor-19-report.md` and the first 60 lines of `fix-whole-report.md`; `review-whole-report.md` and the executors' other sections not read.
- `foundations/decisions.md`: WAY-09, WAY-38 (to its *Rejected*), WAY-379 to WAY-402, WAY-95 (whole), WAY-321 (in part) read; WAY-344 and WAY-363 only through the diff of the change; WAY-253, WAY-12, WAY-203, WAY-204 only by the passages the other entries quote.
- `foundations/invariants.md`: the diff of the change; not the whole file. `foundations/environment_facts.md`: the two new entries (the long list of 407 codes by a script), not the rest.
- The code: `ruff.toml` (head, tail and the select list by script), `requirements-quality.txt` (head), `test_linter_invariant.py` and `test_size_invariant.py` whole; the cited tests of the invariants by passages around their citations; `cycle_stages.py` (head only), `skill_entry_points.py` and `cycle_measures.py` by their diffs; the other tests of the change not read.
- `guidelines/coding.md`, `guidelines/testing.md` and the six kind files: read whole.

## Searches not found or unclear

- A frozen (edition) address of pip's documentation for `--require-hashes`: not found (404 for `en/25.3`); only the source file at the tag `25.3`, which the templates accept as a source of code but which is documentation text; the decision to write no fact does not depend on it.
- The concern "the order of the plan's *Choices*" of the handoff: not found as a concern in any report; read as the plan's table of *Choices* and compared as above.
- Whether the part-map's External context should hold the package host the linter comes from: the template ties a row to a trust boundary; unclear for an installation step, decided as no row.
- Whether the invariants that hold part of a decision's pair should also have it removed (WAY-380): the method names only a test's `decision:` line and the clause `tests:`; unclear, left (concern 5).
