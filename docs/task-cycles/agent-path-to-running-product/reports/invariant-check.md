# Invariant check — project-technology-record/1 (foundation stage)

Status: done. Commit `8720107` on `task/agent-path-to-running-product` (parent `4c251dc`), not pushed.

## Inputs

- Handoff: `.runs/task-cycles/agent-path-to-running-product/reports/invariant-check-handoff.md`.
- Invariant `project-technology-record/1`, `foundations/invariants.md` at `4c251dc` (version stays 1:
  no main branch to compare with, `elements/common/rules.md`).
- Method: `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl`.
- Read: `.claude/skills/the-way-record-invariant/SKILL.md` → `elements/invariants/skill/SKILL.md`
  (check handed to an agent that wrote neither sentence nor code, WAY-69);
  `elements/common/rules.md` (a check cites `<identifier>/<version>`);
  `project-level/test_readiness_check.py` whole; `project-level/definition_template.md` § Technology
  (nested items "are no choices of the list", WAY-112).
- The readiness check was used only through `readiness_check.check(text, before_approval)`,
  `readiness_check.main([...])` and the `--fingerprint` command; its implementation was not read.
  `readiness_check.Finding`'s signature was read by introspection, only for the throwaway simulation
  below (not used by any check).

## How a rejection is asserted

The invariant fixes no message or condition letter for the new clause. Each new check therefore
compares two definitions: the input (lacking the mark) and the same input with the mark's valid item
(`MARKS[mark]`) added to `## Technology`. The input is rejected for the missing mark when it has a
finding the second one lacks (multiset difference non-empty). Where the input is otherwise valid
(`clean`), the check also asserts the second definition has no finding at all, so the rejection can
only be the missing mark's. Every case runs twice (`subTest`): before approval
(`Status: ready for gate`, no gate record, `before_approval=True`) and on a definition holding its
gate record (`Status: approved …`, valid fingerprint, default run).

Helpers added in `project-level/test_readiness_check.py`: `MARKS` (line 61, three valid items —
`- logs: …`, `- interface: …`, `- development data: …`, each `held by: ARC-0x/1`), `MARKED`,
`BASE_CHOICE` (67), `marked(body)` (70), `lacking(mark)` (75: base choice + the two other marks),
`after_mark(mark)` (80).

## New checks (all `# invariant: project-technology-record/1`)

Class `TechnologyMarks` (`project-level/test_readiness_check.py:560`), per mark and per run unless said:

| Test | Input (Technology section unless said) | Result the sentence requires |
|---|---|---|
| `test_a_definition_lacking_one_mark_is_rejected` (591) | base choice + the other two marked items | rejected |
| `test_a_definition_lacking_every_mark_is_rejected` (596) | base choice only (control: `marked(base)` has no finding) | rejected |
| `test_a_definition_holding_all_three_marks_is_not_rejected_for_them` (603) | `marked(base)`; the three alone; the three before the base; `- logs:Logi…` (no space after the colon) | no finding |
| `test_a_mark_in_another_case_is_no_mark` (611) | `- Logs: …` / `- LOGS: …` etc. (capitalised and upper case) | rejected |
| `test_a_mark_without_its_colon_is_no_mark` (618) | `- logs Logi…` / `- interface …` / `- development data …` | rejected |
| `test_a_mark_not_at_the_start_of_the_text_is_no_mark` (624) | `- Dla agenta logs: …` | rejected |
| `test_a_mark_on_the_continuation_line_of_a_choice_is_no_mark` (630) | `- Dla agenta` + continuation line `  logs: … — held by: …` | rejected |
| `test_a_mark_only_in_a_nested_item_is_no_mark` (636) | valid choice with nested `  - logs: …` | rejected |
| `test_a_mark_only_in_the_prose_of_the_section_is_no_mark` (643) | prose line `logs: … — held by: …` (not `clean`: the prose line is itself rejected; the check asserts a finding beyond it) | rejected for the mark |
| `test_a_mark_only_in_another_section_is_no_mark` (649) | mark as a list item in `## In scope`; mark as prose in `## Background`; Technology lacks it | rejected |
| `test_one_item_carrying_two_marks_holds_only_the_first` (656) | `- logs: interface: …` + development data item → interface lacking | rejected |
| `test_an_open_choice_carrying_a_mark_is_rejected_only_as_open` (662) | `- logs: Logi aplikacji — open` + other two, before approval | exactly `[("g", OPEN_MESSAGE)]` — the open item is a choice item whose text begins with `logs:` |

Class `Command`: `test_a_definition_lacking_a_mark_exits_one_approved_or_not` (748) — a definition
lacking `development data:` exits 1 through `main`, with and without `--before-approval`.

## Inputs left untested (the sentence does not determine them)

- A choice item with a list marker other than `- ` (`* logs:`, `+ logs:`) — the sentence's "text"
  is defined after the `- ` marker; whether `*`/`+` items are choice items is not said.
- Extra space after the list marker (`-  logs: …`): its text after `- ` begins with a space.
- Whitespace variants inside `development data:` (two spaces, a non-breaking space, a tab).
- A marked item inside a fenced block within `## Technology`.
- Two items carrying the same mark (sentence only requires "no … none" to reject).
- A marked item with nothing after the mark (`- logs: — held by: ARC-03/1`).
- A `## Technology` section reading `TODO` (see concerns: an existing uncited check fixes its result).

## Existing checks of this invariant kept meaningful

In `project-level/test_readiness_check.py`, class `Technology`:

- `BODIES["Technology"]` (line 104) → `marked(BASE_CHOICE)`: the default definition holds the three
  items, so every check built on `definition()` still tests only its own defect.
- `TECHNOLOGY_PROJECTED` → wrapped in `marked(...)`.
- Bodies wrapped in `marked(...)` (exact assertions unchanged): choice without its entry, open
  choice before approval, held-by off form, projected question no heading holds, projected naming
  an invariant heading, held-by without version, open after a held marker, projected with no
  decision heading, projected matching the candidates line, projected naming part of a question,
  decision heading outside projected changes, open after a settled choice, indented prose, prose,
  and the passing checks (all held, dash in the name, two-line choice, nested detail).
- `test_none_is_reported` (438): `assertEqual(…, [NONE])` → `assertIn(NONE, …)`. A section reading
  `none` cannot hold the marked items, and the sentence rejects it also for lacking them; whether the
  check reports that as further findings is not determined, so the exact assertion was loosened.
- `test_none_followed_by_choices_is_reported` and `test_a_definition_without_the_technology_section_is_reported`
  use `assertIn` and were left unchanged.

## Fixtures of other invariants' checks changed (C10)

| File:line | Check it serves | Change | Why |
|---|---|---|---|
| `project-level/test_readiness_check.py:104` (`BODIES`) | `project-readiness-gate/1`, `project-definition-form/1` and uncited checks | Technology holds the three marked items | the shared definition would be rejected only for lacking them |
| `project-level/test_plan_state_invariant.py:61-63` (`DEFINITION_BODY`) | `project-plan-state-evidence/1` (and `test_plan_state_subprocesses_invariant.py`, which imports it) | three marked items added (`APP-02/1`…`APP-04/1`) | `plan_state.py` runs `readiness_check.check` on the definition |
| `project-level/test_plan_state_invariant.py:73` | same | `FINGERPRINT` `a3b6ab99` → `dcb10529` | recomputed with `python -B project-level/readiness_check.py <definition> --fingerprint` and, independently, by WAY-02 over the literal body; both `dcb10529`; the same independent method gives `a3b6ab99` on the file at `4c251dc` |
| `project-level/test_plan_state.py:60-62` (`BODY`) | plan-state checks (break-caught tests) | three marked items added | same reader; its `FINGERPRINT` is computed from `BODY` in the file |

No assertion of another invariant's check changed. Searched and left unchanged:
`project-level/test_plan_check.py:106` — `plan_check.py` reads the definition's sections and
fingerprint but never calls `readiness_check.check`, so its fixture is not rejected; no other `.py`
in the repository uses `readiness_check` or holds a definition text; no `.md` definition under
`project-level/` is run by a check except the template (see concerns).

## Commands, exit codes, output

| Command | Exit | Output |
|---|---|---|
| `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl` | 1 (expected) | `reports/invariant-check-project-level-tests.txt` — 263 tests, 66 subtest failures, 0 errors |
| `python -B gate/run_tests.py gate` | 0 | `reports/invariant-check-gate-tests.txt` — 98 tests OK |
| `git diff --check` | 0 | `reports/invariant-check-diff-check.txt` |
| simulation (throwaway, not in the repo): tests run with `readiness_check.check` patched to add a finding when no top-level `- ` item of `## Technology` begins with a mark | 1 | `reports/invariant-check-simulated-rule.txt`, script `reports/invariant-check-simulate.py` — every new check passes; the only failure is `Technology.test_a_section_still_reading_todo_is_one_gap_and_no_g` (see concerns) |

(`reports/` = `.runs/task-cycles/agent-path-to-running-product/reports/`; output files are in the
console code page, not UTF-8.)

Baseline before any change: 250 tests OK.

## Expected-failing tests (against current code)

All failures are `AssertionError` of the expected kind (`no rejection for the missing … item: [...]`,
`[] == []` in the `assertNotEqual`, `0 != 1` for the exit code); none is an error, and none is the
`clean` control (the input with the mark added always had no finding, so each input is otherwise
valid):

- `TechnologyMarks.test_a_definition_lacking_one_mark_is_rejected` (6 subtests)
- `TechnologyMarks.test_a_definition_lacking_every_mark_is_rejected` (2)
- `TechnologyMarks.test_a_mark_in_another_case_is_no_mark` (12)
- `TechnologyMarks.test_a_mark_without_its_colon_is_no_mark` (6)
- `TechnologyMarks.test_a_mark_not_at_the_start_of_the_text_is_no_mark` (6)
- `TechnologyMarks.test_a_mark_on_the_continuation_line_of_a_choice_is_no_mark` (6)
- `TechnologyMarks.test_a_mark_only_in_a_nested_item_is_no_mark` (6)
- `TechnologyMarks.test_a_mark_only_in_the_prose_of_the_section_is_no_mark` (6)
- `TechnologyMarks.test_a_mark_only_in_another_section_is_no_mark` (12)
- `TechnologyMarks.test_one_item_carrying_two_marks_holds_only_the_first` (2)
- `Command.test_a_definition_lacking_a_mark_exits_one_approved_or_not` (2)

Passing new checks: `test_a_definition_holding_all_three_marks_is_not_rejected_for_them`,
`test_an_open_choice_carrying_a_mark_is_rejected_only_as_open`. Every other project-level test passes.

## Changed files

| File | Added | Removed |
|---|---|---|
| `project-level/test_readiness_check.py` | 169 | 22 |
| `project-level/test_plan_state_invariant.py` | 4 | 1 |
| `project-level/test_plan_state.py` | 3 | 0 |

## Concerns

1. **Template test will break with the code.** `Template.test_the_technology_section_the_template_gives_passes_its_checks`
   (uncited) runs `check_technology` on the example block in `project-level/definition_template.md`
   § Technology, which holds no marked item. Once the code requires the marks there, that test fails
   unless the template's example gains the three items — a non-test file outside this stage's
   boundary; the code stage should update it.
2. **`TODO` section conflict.** `Technology.test_a_section_still_reading_todo_is_one_gap_and_no_g`
   (uncited) asserts a `TODO` Technology section gives exactly one finding. The sentence rejects such
   a definition also for lacking the marks ("approved or not"); it is rejected either way, so the
   test does not contradict the sentence, but a straightforward implementation adds mark findings
   and fails it (shown by the simulation). The code must either skip the mark clause for a section
   still reading `TODO`, as it skips `g`, or the test needs a decision. Left unchanged and untested
   by the new checks.
3. **Case.** The sentence quotes the marks in code form; the checks read "begins with `logs:`" as
   case-sensitive and literal (`Logs:` is no mark). If case-insensitive matching was meant, the
   sentence should say so and `test_a_mark_in_another_case_is_no_mark` would invert.
4. **"Choice item" is not defined in the glossary.** The nested-item and continuation-line checks
   rest on the template's reading (nested items are no choices of the list, WAY-112; a choice may
   span two lines) rather than on the sentence alone.
5. `test_none_is_reported` was loosened from an exact list to `assertIn` (reason above).
