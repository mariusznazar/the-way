# Author report — implementation (turn 2)

Status: **done** — code committed (`c657b2b`), boundary reached before review. No edit to
`foundations/**` or to any invariant test. Author: the same general-purpose subagent as turn 1
(claude-opus-5-5), one-author route.

## Inputs

- Handoff `reports/author-implementation-handoff.md`; worktree at `8720107` at start.
- My foundation commit `596a660` (WAY-121@d0b060e5, WAY-165); invariant sentence `4c251dc`
  (`project-technology-record/1`, read whole); checks and fixtures `8720107` (read:
  `reports/invariant-check.md` whole, `project-level/test_readiness_check.py` lines 1–160 and
  395–700 — `Technology`, `TechnologyMarks`, `Template`).
- Cycle record rulings C6–C11; ruling C12 from the handoff.
- Superpowers 6.4.1 `test-driven-development/SKILL.md` and `writing-good-tests.md`, read from the
  6.4.1 cache root (not the Skill tool).
- Frozen task: To do 1–3, rows 1–6.

## What changed and why

| File | Change | Why |
|---|---|---|
| `project-level/readiness_check.py` (+14/−1) | `AGENT_PATH_MARKS = ("logs:", "interface:", "development data:")`; `check_technology` adds one condition-g finding per mark that no choice item's own text begins with (case-sensitive `startswith` on the text `items()` gives: first line after `- `, joined continuation lines, nested items and prose excluded). It runs after the existing `TODO` and `none` early returns, in both modes (`check` calls `check_technology` with or without `before_approval`). Docstring of condition g extended. | Invariant `project-technology-record/1`; WAY-121 rows 1, 4, 5; C12 (a `TODO` section stays one gap). |
| `project-level/definition_template.md` (+35/−5) | Sections table row; Technology intro; example list gains `logs:`, `interface:`, `development data:` items (`held by` DOC-03..05/1); rules: the three always-present choices with marks and a table of what each asks (WAY-121, WAY-165), the answer where the product lacks the thing, the gate stopping approved definitions too, a mark inside a nested item marks nothing; after WAY-137's rule, WAY-165's rule on an agent's use of an option. | To do 1, rows 1–3, 6; check agent's concern 1 (the template test runs `check_technology` on the example). |
| `project-level/technology/SKILL.md` (+30/−6) | Step 0: a list lacking a marked item gets the missing ones as `— open` (others kept); an approved definition's status goes to `definition — open: Technology`, human told it goes through the gate again and its plan is rechecked; step 1: the three always listed; step 2.1/2.3/2.5: what each asks, agent's use as a consequence, recommendation passes over an unusable option; step 3: a missing-mark finding routes to step 0's rule; closing paragraph. | Carried question (c) as accepted; WAY-165 against WAY-137. |
| `project-level/skill/SKILL.md` (+5/−1) | Step 0, approved definition: a missing-mark finding → step 6, then 7, plan rechecked through `plan-project`. | Row 5; WAY-118. |
| `project-level/task/skill/SKILL.md` (+6/−1) | After the readiness run on an approved definition: a missing-mark finding sends the definition back through `define-project` (technology step, gate), plan rechecked, before refinement goes on; tell the human. | Row 5, To do 3's effect. |
| `project-level/plan/skill/SKILL.md` (+4/−1) | Step 1: same reading of the finding. | Row 5 (another run on an approved definition, C8). |
| `project-level/lead/skill/SKILL.md` (+5/−1) | Step 0: a missing-mark finding from the readiness check or the state reader's `definition` line follows step 5's definition-change route; no task ready for cycle meanwhile. | Row 5; the plan-state reader reports it as `definition fail: g …`. |
| `project-level/test_readiness_marks.py` (new, +199) | Ordinary tests (no invariant citation): whole list passes; each missing mark is a finding of its own naming its mark; `none` keeps its one finding; `TODO` gives no mark finding; a definition approved at `77c8a8b`'s literal (gate fingerprint `a3b6ab99`) is stopped only for the three; once they are added it gives only `e` (goes through the gate again). | TDD of the reporting choices; weakest-point check. A new file because `test_readiness_check.py` is an invariant test (read-only). |

No skill description changed, so `skill_entry_points.py --write` was not needed (check mode:
"entry points are current").

## TDD evidence

1. **Red (invariant checks)** at `8720107`, before any code: `python -B gate/run_tests.py project-level`
   → exit 1, 263 tests, 66 subtest failures, all in `TechnologyMarks` and
   `Command.test_a_definition_lacking_a_mark_exits_one_approved_or_not` —
   [implementation-red-project-level.txt](implementation-red-project-level.txt).
2. **Red (my test)**: `test_readiness_marks.py` written first → exit 1,
   `test_each_missing_mark_is_a_finding_of_its_own_naming_it` fails; the three guards (whole list,
   `none`, `TODO`) pass as controls of behaviour to keep —
   [implementation-red-marks.txt](implementation-red-marks.txt).
3. **Green**: code change → my file OK ([implementation-green-marks.txt](implementation-green-marks.txt));
   `test_readiness_check.py` then had one failure, the template test (concern 1, expected) —
   [implementation-green1-readiness.txt](implementation-green1-readiness.txt).
4. **Green**: template example carries the three → `test_readiness_check.py` 94 OK —
   [implementation-green2-readiness.txt](implementation-green2-readiness.txt).
5. **Weakest-point test red/green**: `ApprovedBefore` tests run against `8720107`'s
   `readiness_check.py` (restored afterwards) → `test_it_is_stopped_for_the_three_missing_choices_alone`
   fails; against the new code → 6 OK —
   [implementation-weakest-red.txt](implementation-weakest-red.txt),
   [implementation-weakest-green.txt](implementation-weakest-green.txt).
   (`test_once_the_choices_are_added_it_goes_through_the_gate_again` passes on both: it guards the
   fingerprint route, which already existed.)

## Check agent's concerns and carried question (c)

1. **Template test** — settled: the example list holds the three marked items (`held by`, so no
   projected heading is needed); the uncited template test passes.
2. **`TODO` section** — settled by C12: `check_technology` returns before the mark rule for a
   section reading `TODO` (as it already did for condition g), so
   `Technology.test_a_section_still_reading_todo_is_one_gap_and_no_g` stays meaningful and passes;
   my `test_a_section_still_reading_todo_gives_no_mark_finding` guards the same. A section reading
   `none` likewise keeps its one finding (the `none` message already asks to list the choices).
   No read-only check contradicts this: `test_none_is_reported` uses `assertIn`.
3. (Concern 3, case) — implemented case-sensitive, as the checks require.
- **Carried question (c)** — implemented as accepted: `settle-technology` step 0 adds the missing
  marked items as `— open` and resumes at step 2; for an approved definition the status reopens
  and the definition goes through the gate again (fingerprint changes, `e`), then the plan is
  rechecked; `define-project` step 0 routes the finding to step 6 then 7.

## Weakest-point check (WAY-164)

- **Requirement most likely missed:** To do 2 / row 5 — "the readiness gate stops a definition
  lacking one of the three, also one approved before this change", on the paths that actually run
  on approved definitions, and the route back through the gate. The invariant checks use a
  synthetic definition; a real older definition (no marks, valid gate record) or the plan-state
  reader that lead-project uses could still pass if, e.g., the rule ran only before approval or
  only in `main`.
- **Checks:** (a) test `ApprovedBefore` in `project-level/test_readiness_marks.py`: the approved
  definition the plan-state checks held at `77c8a8b`, with its original gate fingerprint, gives
  exactly three `g` findings naming the marks; with the three added it gives only `e`.
  (b) Manual check — method: script
  [implementation-weakest-plan-state.py](implementation-weakest-plan-state.py) builds that
  commit's plan, task and definition literals in a temp folder and calls
  `plan_state.sources(plan)`; actor: this author; evidence:
  [implementation-weakest-plan-state.txt](implementation-weakest-plan-state.txt).
- **What it showed:** (a) failed on the old code, passes on the new (red/green above). (b) the
  reader returns code 1 with three lines `definition fail: g — line 46: no choice item begins with
  \`logs:\` / \`interface:\` / \`development data:\` …` — the lead-project path stops the definition.

## Choices, rejected alternatives, cost if wrong

| # | Choice | Rejected | Cost if wrong |
|---|---|---|---|
| I1 | One finding per missing mark, at the section heading line | one finding listing all missing marks — less clear which to add | message wording only |
| I2 | No mark findings for a `none` section (its own finding asks for the list) | three more findings on `none` — noise on an already-rejected section | none: rejected either way (`assertIn` test) |
| I3 | Mark matched on the item's stripped first-line text (`items()`), case-sensitive | regex over raw lines — would count nested items and prose | `-  logs:` (two spaces) counts as a mark (untested by the invariant checks; lenient) |
| I4 | My tests in a new file | adding them to `test_readiness_check.py` — that file is an invariant test (read-only, WAY-03) | one more test file |
| I5 | Approved definition's reopening written in `settle-technology` step 0 and `define-project` step 0; refine/plan/lead name the finding and route to `define-project` | a new step or skill for the catch-up — WAY-121 says the step settles them like any other choice | prose only |
| I6 | Template: a mark inside a nested item "marks nothing" stated beside WAY-112 | silence — the checks already reject it, so a writer should know | none |

## Commands, exit codes, outputs

Run from the worktree root, Git Bash, Python 3.14 (`python -B`), on the final working tree
(identical to `c657b2b` except one rewrap in `technology/SKILL.md` made before commit; the
agent-instructions run, entry-point check and readiness tests were rerun after it).

| Command | Exit | Output | Summary |
|---|---|---|---|
| `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl` | 0 | [implementation-tests-project-level.txt](implementation-tests-project-level.txt) | 269 tests OK; record: project-technology-record/1 pass 30, project-readiness-gate/1 pass 8, project-definition-form/1 pass 6, project-plan-form/1 pass 49, project-plan-check/1 pass 32, project-plan-state-evidence/1 pass 27, project-plan-state-subprocesses/1 pass 2; no fail, no unchecked |
| `python -B gate/run_tests.py gate` | 0 | [implementation-tests-gate.txt](implementation-tests-gate.txt) | 98 OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | [implementation-tests-agent-instructions.txt](implementation-tests-agent-instructions.txt) | 18 OK |
| `python -B agent-instructions/skill_entry_points.py` (check mode) | 0 | [implementation-skill-entry-points.txt](implementation-skill-entry-points.txt) | "entry points are current" |
| `git diff --check 77c8a8b` (working tree incl. new file, before commit) | 0 | [implementation-diff-check.txt](implementation-diff-check.txt) | empty |
| `python -B -m unittest project-level/test_readiness_check.py project-level/test_readiness_marks.py` | 0 | [implementation-tests-readiness-final.txt](implementation-tests-readiness-final.txt) | OK |
| weakest-point manual check | 0 (script) / reader code 1 | [implementation-weakest-plan-state.txt](implementation-weakest-plan-state.txt) | three `definition fail: g` lines |

Warnings: none in any output. Unchecked: none in the project-level record. Failures: none at the
end (the red runs above are intended). Not run: format guards (no foundation file changed in this
turn), the full gate (orchestrator).

## Changed files (`8720107..c657b2b`)

| File | Added | Removed |
|---|---|---|
| `project-level/definition_template.md` | 35 | 5 |
| `project-level/lead/skill/SKILL.md` | 5 | 1 |
| `project-level/plan/skill/SKILL.md` | 4 | 1 |
| `project-level/readiness_check.py` | 14 | 1 |
| `project-level/skill/SKILL.md` | 5 | 1 |
| `project-level/task/skill/SKILL.md` | 6 | 1 |
| `project-level/technology/SKILL.md` | 30 | 6 |
| `project-level/test_readiness_marks.py` | 199 | 0 |

Commit `c657b2b` feat(project-level): require the agent's three ways to the running product in the
technology list (private author address checked). `.runs/` not staged.

## Sharpness inputs from the actual diff

- Criticality: all files in part `project-level` (eleven failure modes, all high). Highest: high.
- Trust-boundary files touched: `project-level/readiness_check.py` (declared boundary). The change
  adds no parsing: three `str.startswith` calls over texts the existing `items()` already yields;
  no regex, no I/O, linear in the number of items. Crafted inputs worth the reviewer's attention:
  marks inside a fenced block in `## Technology` (counted as items, as every line there already
  is), `-  logs:` with two spaces (counted), `* logs:` (not an item, not counted), Unicode
  look-alike colons or non-breaking spaces in `development data:` (not counted).
- Irreversible operations: none.

## Unresolved concerns

1. **A fenced block inside `## Technology`** is read as items by the existing parser, so a marked
   line inside a fence satisfies the mark rule; untested by the invariant checks and unchanged
   behaviour of `items()`. Low risk; a reviewer may want a test or a fence skip.
2. **A definition with no `## Technology` section** (written before the technology step): the
   existing `define-project` step 0 branch still offers "leaving it" with its cost; with row 5 the
   plan, refinement and lead paths stop it anyway (structure finding). Left as is; the request may
   mention it.
3. The request still needs To do 3's line on moving the pin, WAY-121's change of meaning, and the
   candidate part-map failure mode (turn 1 concerns 2–4).

## Fix (turn 3)

Fixes the review's one blocking finding, **Important 1** (`project-level/skill/SKILL.md:68-74`). I
hold it right: WAY-121 sends every definition lacking the three choices back through the step, and
a definition with no `## Technology` section lacks them all; "leaving it" looped (refine-task,
plan-project and lead-project return a structure finding to `define-project`), and its stated cost
("leaves the choices to the breakdown") was false. Minor findings and *Declined to judge* lines
untouched, as the handoff requires.

**What changed** — `define-project` step 0, the branch for a definition with no `## Technology`
section: the question with its "leave it" option is gone. The branch now says the definition was
written before the technology step and goes back through it (WAY-121); tells the human that no
task of its plan can be refined or broken down until it is approved again; adds `## Technology`
reading `TODO` before "Projected foundation changes", sets the status line to
`definition — open: Technology`, goes on at step 6 and through step 7 (WAY-118), and has the plan
of a formerly approved definition checked again through `plan-project`.

**Manual check** (skill text; no behaviour of code changed) — method: build the approved
definition of `ApprovedBefore` (`test_readiness_marks.py`) without its Technology section, run
`readiness_check.py` on it, then apply the branch's edit (section reading `TODO`, status open) and
run it with `--before-approval`; actor: this author; observed: (1) exit 1,
`fail: structure — the section `## Technology` is missing` — the finding every other skill returns
to `define-project`; (2) exit 1, the single gap `` `## Technology` holds TODO ``, which is where
`settle-technology` step 0 begins at step 1, listing the three marked choices; evidence:
[fix-manual-check.txt](fix-manual-check.txt). The weakest-point check is not touched by the fix
(no code changed) and was not rerun.

| Command | Exit | Output | Summary |
|---|---|---|---|
| `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl` | 0 | [fix-tests-project-level.txt](fix-tests-project-level.txt) | 269 OK; record has no `fail` or `unchecked` |
| `python -B gate/run_tests.py gate` | 0 | [fix-tests-gate.txt](fix-tests-gate.txt) | 98 OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | [fix-skill-entry-points.txt](fix-skill-entry-points.txt) | entry points are current |
| `git diff --check 77c8a8b..HEAD` | 0 | [fix-diff-check.txt](fix-diff-check.txt) | empty |

Warnings: none. Unchecked: none. Changed files `c657b2b..0c1dfd5`: `project-level/skill/SKILL.md`
+5 / −6. Commit `0c1dfd5` fix(project-level): send a definition with no technology section back
through the step. Sharpness unchanged: part `project-level` (high), no trust-boundary file, nothing
irreversible.
