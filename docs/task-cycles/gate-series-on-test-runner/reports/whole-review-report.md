FAIL 909fcb9a1f804545ff0baa6c29697e3fc7ce0b8d

# Review of the whole change — gate-series-on-test-runner

Range: base `715ae20d9e817299bd81554e5fdcb6baaf465099` to head `909fcb9a1f804545ff0baa6c29697e3fc7ce0b8d` (one commit, `909fcb9`). `git rev-parse HEAD` in the worktree is the head given. Worktree clean before and after my checks.

Changed files (`python -B task-cycle/change_file_sizes.py 715ae20 909fcb9`, exit 0):

| File | Before | After | Change |
|---|---|---|---|
| `foundations/decisions.md` | 12341 | 12353 | +12 |
| `process-audit/SKILL.md` | 225 | 227 | +2 |
| `process-audit/audit_count.py` | 2972 | 2983 | +11 |
| `process-audit/test_audit_count.py` | 3128 | 3186 | +58 |

Diff stat by the commit: decisions.md 32 lines, SKILL.md 6, audit_count.py 49, test_audit_count.py 68.

## Findings

### Critical

none

### Important (blocking, within the task)

**1. `foundations/decisions.md`, WAY-339 *Verification*, `violates:` list. The change deletes a correct violating example on a false claim and the task did not ask for it.**

The base wording was: "a change of the script that records the gate times leaves their series whole". The author's report calls this a "pre-existing inconsistency" that "contradicted the binding sentence (the recording script does start a series)". It does not contradict it. The binding sentence says a new series of the gate times "starts only with a change of the script that counts them or of the script that records them". An example under `violates:` is a change that goes against the decision. A change of the recording script (`task-cycle/gate_times.py`) that leaves the series whole goes against exactly that sentence, so the bullet was a correct violating example. The edit replaced it with "a change of the test runner of the gate leaves the series of the gate times whole".

Effect: after the change, *Verification* has no example for a change of `task-cycle/gate_times.py`. That is the only trigger of a gate-time series before this task, and the one the task text names ("tak jak dziś zmiana `task-cycle/gate_times.py`"). The code still splits there (the existing tests pass), so the entry's binding meaning is intact. But the task asks for *Verification* to say the same as the new rule, not to lose one of its cases. A human who accepts the merge is told the edit fixed an inconsistency that was not there (author report, "Pre-existing inconsistency fixed"). Frame: WAY-263 (the entry's own sentences restate the rule differently from what it requires) and the task's "added that nobody asked for".

Fix: keep the recorder bullet as it was and add the test-runner bullet beside it (both under `violates:`, with the runner case also under `complies:` as now). Evidence: `git diff 715ae20..909fcb9 -- foundations/decisions.md`, hunk at old lines 11246-11256; base text read in this worktree's history. Comes from the single commit `909fcb9` (no plan, no slices).

### Minor

**2. `foundations/decisions.md`, WAY-339 binding sentence: "a change of the test runner of the gate".** The code and SKILL.md watch one file, the process's `gate/run_tests.py`. WAY-349 and WAY-366 say "the test runner of the process"; "of the gate" can be read as a product's own runner, which the audit cannot see (the task's *Context* says changes to a product's gate command are not seen). Say "the test runner of the process, whose output gives the time of each directory". Within the task. (Graded Minor because the entry's content agrees with what the code does inside the-way's own checkout; WAY-364.)

**3. `foundations/decisions.md`, WAY-339 *Rejected*, "...mixed with the earlier ones until this change is merged".** An entry describes the decision as it stands, never the change that edits it (WAY-07, template "Changing a decision"). After the merge the phrase refers to a moment that has passed. The task's *Not chosen* text holds the same fact ("do scalenia tego zadania"), so this is fidelity to the source with the wrong tense for a log entry. Write it without the change: the runs made between the move to parallel directories and this decision stay mixed with the earlier ones. Within the task.

**4. `foundations/decisions.md`, WAY-339 *Rationale*, last sentence: "it measures nothing itself, but it fixes what the measuring script records".** The task's *Decisions in play* asks for the reason "that the test script is part of the measurement of the times". The sentence says the opposite half of it ("measures nothing itself"). The author's wording is defensible, but it departs from the task's stated reason. Also the sentence "The test runner decides how the directories of the gate run, one after another or together" states what a process tool does today, which the template keeps out of *Rationale* ("nor what the process's own tools do or lack today"); WAY-366 holds it as a binding sentence. Within the task.

**5. Structure (WAY-362/363).** `process-audit/audit_count.py` is 2983 lines and `test_audit_count.py` 3186; the change adds 11 and 58 lines. The-way has no coding guidelines and no rule of size (WAY-328), so there is no threshold test to run. The functions the diff reaches (`instrument_series`, `measure_versions`, `measure_versions_lines`) grew by a few lines each; `instrument_series` is about 20 lines. No code without a user (the constant `GATE_SCRIPT` still has users; `GATE_SCRIPTS` is used once). No name has stopped being true. Nothing to grade above Minor; noted for completeness, no change asked.

### Out of scope

none

### Declined to judge

- A product's own gate command or its own test runner (the task's *Out of scope* and *Context* say the audit does not see it).
- The audit's weekly session, wording of its later steps beyond the paragraph changed (not changed by this commit).
- The author's claim that `price_list.md`, `problem_register.md` and `cycle_stages.py` are still true: I read the lines that mention a series (`price_list.md:9`, `problem_register.md:70-71`, `cycle_stages.py:66`); they speak of the cost and of "no mechanism measure or gate time" and stay true. Not a finding.

## Against the task

- *To do* 1: met. `GATE_SCRIPTS = (task-cycle/gate_times.py, gate/run_tests.py)` is passed for the gate series; the reason names the changed file or files; the mechanism series split only on `task-cycle/cycle_measures.py`; the cost series are not touched (`series_boundary` is unchanged). Checked in the diff and by the new tests.
- *To do* 2: partly. SKILL.md (paragraph "Measures are compared inside a series only"), the module docstring (`audit_count.py:127`) and the printed text of *Measure versions* (`:2646`) say the same as the code. WAY-339's binding sentence, *Scope* (adds `gate`, which owns `gate/run_tests.py` under WAY-55) and *Verification* `complies:` say it too; finding 1 is against the `violates:` list.
- Row 1 of *Settlements to record* (every change of `gate/run_tests.py` starts a new series of the gate times, as one of `gate_times.py` does; WAY-339 changed): met in the binding sentence. Nothing invented beyond what the source gives: the added *Rejected* text matches the two *Not chosen* items of the task with their costs (finding 3 on tense).
- Nothing added that nobody asked for, apart from finding 1's deletion.

## Against the foundation

- Decisions read whole: WAY-339 (all of it, before and after), WAY-347, WAY-348, WAY-349, WAY-350, WAY-366, WAY-55, WAY-328. None contradicts the change. WAY-350's concurrency rule is unaffected: only which versions form a series changes.
- The edit to WAY-339 follows the template's "Changing a decision" (in place, no history) except where findings 1-4 say. `Relations: none`, `Based on: none` stay true. The `Scope` change is valid (`gate` is a part; `python -B elements/common/foundation_check.py` reports 0 errors, exit 0).
- No invariant test is changed by the commit. Invariants selected by the parts `process-audit`, `task-cycle` and `gate` were not read beyond those whose names the author cited; see *Unread material*.

## Hostile input at the trust boundary (`process-audit/audit_count.py`)

- A path in the list of instrument files: the two names are constants of the module (`MEASURES_SCRIPT`, `GATE_SCRIPT`, `GATE_TEST_RUNNER`), not read from any file or argument, and are passed to `git diff --quiet <earlier> <later> -- <paths>` after full commit hashes. No input from outside reaches them. Nothing to check beyond that.
- A repository whose history lacks `gate/run_tests.py`: scratch repository, `git diff --quiet HEAD~1 HEAD -- task-cycle/gate_times.py gate/run_tests.py` with both paths absent exits 0 (no split, no error); with `gate/run_tests.py` added in the later commit it exits 1 (split). So a pin that does not yet hold the runner gives no spurious split, and the version that first holds it starts a series, as the existing rule does for `gate_times.py`.
- Malformed `gate_times.md`: this commit does not touch the reading of the file or the rows; the existing refusal path is unchanged. A git failure counts as changed (`Ancestry.differs`, `audit_count.py:2098`); in `instrument_series` the per-script check on a combined "changed" result falls back to naming every script (`or list(scripts)`), so the reason is never empty. The reason line holds only constants, so no crafted text reaches it.
- No operation that cannot be undone is added; the command only reads git.

## Tests

- The two new tests protect the behaviour: `test_a_change_of_the_test_runner_starts_a_new_series_of_gate_times_only` runs real git commits, so dropping `GATE_TEST_RUNNER` from `GATE_SCRIPTS`, or using the runner for the mechanism series, changes the medians and the reason text and it fails; its expected values are fixed numbers (90, 80) not computed by the code. `test_the_reason_of_a_gate_split_names_the_scripts_that_changed` asserts the reason of one changed script, of both in the order of the scripts, and that a runner change splits no mechanism series. The price-list test asserts the exact tuple passed to git. They fail on the old signature, so they pass for a reason other than the code computing its own value.
- Own-work check of the author: the requirement it names (a change of the runner starts the gate series only, names itself in the reason) fits the weakest place of the change; its two tests would catch it unmet. Accepted.

## Checks I ran

| Check | Command | Exit code |
|---|---|---|
| Sizes of the changed files | `python -B task-cycle/change_file_sizes.py 715ae20d9e817299bd81554e5fdcb6baaf465099 909fcb9` | 0 |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| Tests of the part | `python -B gate/run_tests.py process-audit` | 0 (182 tests, 647 s) |
| Series tests only | `python -B -m unittest test_audit_count.MeasureVersions` in `process-audit/` | 0 (12 tests) |
| Whitespace | `git diff --check 715ae20..909fcb9` | 0 |
| Scratch git run | `git diff --quiet HEAD~1 HEAD -- task-cycle/gate_times.py gate/run_tests.py` in a scratch repository, path absent, then added | 0, then 1 |

Not run: the product's whole gate (the orchestrator's run). No size-threshold test (the-way has none, WAY-328), so none was run on the base or the head.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-328, WAY-55: whether the-way's code is held to guidelines and which part owns `gate/run_tests.py`; read whole.
- `elements/decisions/template.md`: rules of a decision entry (*Rationale*, *Rejected*, *Verification*, changing a decision); read whole.
- `foundations/part_map.md` lines 93-135 (parts `task-cycle`, `process-audit`, `gate`): trust boundary and files; read as lines.
- A search of the repository for `gate_times.py`, `GATE_SCRIPT` and "series" outside the changed files, to find other statements of what splits a series.

## Unread material

Decisions of my selection (Scope names `process-audit` or `gate`): 46 found by search of the *Scope* lines. Read whole: 8 (WAY-339, WAY-347, WAY-348, WAY-349 [selected by the task], WAY-350, WAY-366, WAY-55, WAY-328). By title only: 39 (WAY-09, 16, 38, 51, 53, 60, 61, 62, 63, 65, 68, 69, 82, 89, 100, 102, 320, 321, 330, 331, 332, 333, 334, 335, 336, 337, 338, 340, 341, 342, 343, 344, 345, 346, 351, 352, 355, 356, 359). None of those titles points to a bearing on the change except WAY-335 (what decides whether a fix works) and WAY-338 (the time of a cycle), which concern what the series compare, not what splits them; WAY-348 and WAY-350 (read whole) cover that. WAY-134 and WAY-263/WAY-364 were consulted only through the rules quoted in `template.md` and `SKILL.md`, not read as entries.

Other material not read whole:

- `process-audit/audit_count.py` (about 2983 lines): read the diff, the module docstring at 120-140, constants around 365-410, `Ancestry.differs`, `instrument_series`, `measure_versions`, `measure_versions_lines` and `gate_lines`. Not read whole.
- `process-audit/test_audit_count.py` (about 3186 lines): read the diff and the helpers it uses; not whole.
- `process-audit/SKILL.md`: read lines 40-80 and 195-210; not whole.
- `foundations/invariants.md` and `foundations/glossary.md`: first left unopened, then read as the *Addendum: invariants and glossary* below gives it (19 invariants whose *Part* names `process-audit`, `task-cycle`, `gate` or `every`, each read whole; the glossary entries of the terms the change uses, read whole). Nothing of them stays unread.
- Guidelines: none exist for the-way (WAY-328), so none read.

## Searches not found or unclear

- Coding guidelines and testing guidelines of the-way: not found, by WAY-328 they do not exist for its own code.
- The rule `### Size of a function and a file` of a product's `guidelines/coding.md`: no `guidelines/` directory in the-way; so no size test.
- The base text of WAY-339 was not available as a file at the base commit in this worktree beyond the diff; I read it from the diff (`git diff 715ae20..909fcb9`), which is complete for that entry.

## Addendum: invariants and glossary

Range and head unchanged (`715ae20d9e817299bd81554e5fdcb6baaf465099` to `909fcb9`); read-only.

### Invariants read whole

Selected by a search of the *Part* lines of `foundations/invariants.md` (33 invariants, 19 selected; no invariant names `process-audit` as its part):

- *Part* `every` (17): `foundation-file-kinds`, `foundation-change-merge-route`, `repository-file-location`, `return-step-record`, `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `tracked-file-private-paths`, `script-language`, `script-imports`, `script-subprocesses`, `map-reference-target`, `test-method-citation`, `skill-entry-points`, `instruction-file-imports`, `cross-part-imports`, `record-copy-image-files`.
- *Part* `gate` (1): `gate-exit-code`.
- *Part* `task-cycle` (1): `record-copy-image-check`.

What the change reaches, and the result:

- `script-language`, `script-imports`, `script-subprocesses`: `audit_count.py` and the tests add no import and no program started other than git (the change adds a tuple parameter and a loop over constants). Met.
- `cross-part-imports`: the new tests import `audit_count` of their own part only. Met.
- `test-method-citation`: no invariant of method `test` is newly cited or uncited by the change; no invariant test is changed. Met.
- `tracked-file-private-paths`: I searched the added lines of the diff for absolute paths and note links; the only hits are test index expressions, no path or link. Met.
- `skill-entry-points`: the change edits the body of `process-audit/SKILL.md`, not its frontmatter. The invariant requires a byte-identical pair of entry points that name the skill and lead a session to it; neither entry point is a copy of the body, so no entry point needs a rewrite. Met.
- `gate-exit-code`: `gate/run_tests.py` is not changed by the commit (it only becomes a watched file); the invariant does not concern the series. Not reached.
- The other invariants (`foundation-file-kinds`, `foundation-change-merge-route`, `repository-file-location`, `return-step-record`, `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `map-reference-target`, `instruction-file-imports`, `record-copy-image-*`) concern the route of the change, the places of files and the form of links; the commit adds no file, no link, no CI configuration and no map identifier other than `gate` in WAY-339's *Scope*, which the part map holds (`foundation_check.py`, exit 0, 0 errors). Not reached or met.
- No invariant test is changed by the commit.

### Glossary read whole

`foundations/glossary.md` is 191 lines; read the entries of the terms the change uses: `gate` ("the one command that runs all of a product's tests"), `part`, `foundation`, `standing check`, `cost of an occurrence`, `transitional state` (the last four because they sit near the terms and could be misread as ones the change uses; none is). The glossary holds no entry for `series`, `test runner` or `version of the process`.

### Findings

no finding.

- The words `series` and `version of the process` carry one meaning in WAY-339, WAY-348 and the code, and no sentence the commit writes would be read wrongly for lack of an entry; a missing entry would be Minor (SKILL.md section 3, WAY-104), and none is asked for.
- `gate` has the glossary meaning of a command, so WAY-339's "the test runner of the gate" reads, in a product, as the runner of the product's gate command. That supports Minor finding 2 (say "of the process"); it does not change its grade, since the sentence stays correct inside the-way.
