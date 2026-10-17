# Foundation stage handoff — invariant check agent

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product` (branch `task/agent-path-to-running-product`), at `4c251dc`.
Base of the task: `77c8a8b`.

## Authority and delegation

- Mariusz invoked the task cycle and delegated intermediate choices to the orchestrator; ask him nothing. Return questions to the orchestrator.
- You write the check of one invariant. Under WAY-69 its sentence, its check and the code it covers come from three different agents. You receive the sentence and its method only; another agent will write the code later. Do not change `project-level/readiness_check.py` or any other non-test file.

## The invariant (from `foundations/invariants.md`, entry `project-technology-record/1`, commit `4c251dc`)

> The project readiness check rejects, before approval, a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>/<version>` nor a question a heading of a projected decision holds, and rejects a definition, approved or not, whose Technology section holds no choice item whose text begins with `logs:`, none whose text begins with `interface:`, or none whose text begins with `development data:`.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl`

"Text" of a choice item is the item's text after its `- ` list marker. "Approved or not" covers both the run before approval (`--before-approval`) and the run on a definition holding its gate record (the run without that option).

## Read first

1. The-way's `record-invariant` skill `.claude/skills/the-way-record-invariant/SKILL.md`, its parts about an invariant's check (how a check cites its invariant, `# invariant: <id>/<version>`), and `elements/common/rules.md` where it names checks.
2. `project-level/test_readiness_check.py` whole — the existing checks citing `project-technology-record/1` (lines around 404–495) and the shared fixtures. Use the readiness check only through the interface those tests already use (function and command-line calls); do not read its implementation to shape the checks.
3. `project-level/definition_template.md` section Technology (around lines 148–185), for the form of an item today.

## What this stage does

1. Write the checks of the invariant's new part in `project-level/test_readiness_check.py`, each marked `# invariant: project-technology-record/1`: for each of the three marks separately, a definition lacking it is rejected — before approval and on a definition with its gate record; a definition holding all three, each a valid choice item, is not rejected for them. Include adversarial inputs (the file is a trust boundary, WAY-48): e.g. a mark with different case, a mark not at the start of the item's text, a mark only inside a nested item, a mark in a line that is not a choice item, a mark only in the Technology section's prose, a mark in another section. Decide each expected result from the sentence alone; where the sentence leaves an input's result undetermined, do not test it and list it in your report.
2. Keep every existing check of this invariant meaningful: where a fixture that previously passed would now be rejected only because the three marks are missing, add the three marked items to the fixture so the check still tests what it tested.
3. Ruling C10 of the orchestrator: other invariants' checks hold definition fixtures whose Technology section lacks the three marks and will be rejected once the code follows the invariant — `project-level/test_plan_state_invariant.py` (cites `project-plan-state-evidence/1`; a definition fixture near lines 58–60 and a `FINGERPRINT` constant of that definition), `project-level/test_plan_state_subprocesses_invariant.py` (imports it), and shared fixtures in `test_readiness_check.py` used by checks citing `project-readiness-gate/1` and `project-definition-form/1`; search `project-level/` for any other such fixture (also `test_plan_check.py`, `test_plan_state.py`, and any definition text in `project-level/**`). Update those fixtures by adding the three marked items, and recompute any fingerprint constant of a changed definition with the existing command `python -B project-level/readiness_check.py <definition> --fingerprint` (or the function those tests use). Change no assertion of another invariant's check; report every fixture you changed and why.
4. Run the method. The new checks of the three marks are expected to fail against the current code (it does not yet require them); every other test must pass. Report exactly which fail and confirm each failure is the expected rejection missing, not an error in the test.

## Checks

Save complete stdout+stderr under `.runs/task-cycles/agent-path-to-running-product/reports/` (prefix `invariant-check-`), with exit codes: `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl`; `python -B gate/run_tests.py gate`; `git diff --check`.

## Write boundary

Only test files under `project-level/` in this worktree. Preserve line endings (byte I/O or `newline=''`). Commit by explicit paths, English message in the repository's style; never stage `.runs/`. No push. Do not spawn agents. No secrets or personal data in reports.

## Output

Full report: `.runs/task-cycles/agent-path-to-running-product/reports/invariant-check.md` — inputs; each new check with the input it uses and the result the sentence requires; inputs left untested as undetermined by the sentence; fixtures changed (file, line, which invariant's check, why) and recomputed fingerprints; commands, exit codes, output paths; the expected-failing tests by name; changed files with added/removed lines; commit; concerns (including any place the sentence was unclear).

Return message (short): status, report path, commit, check results with the expected-failing tests named, concerns.
