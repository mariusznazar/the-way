# Affected review — turn 3

- Reviewer: the same general-purpose subagent as the first two reviews (claude-opus-5-5); no subagents spawned
- Method: Superpowers 6.4.1 `requesting-code-review`, reviewer prompt in `review-handoff.md`, scoped by `review-affected-handoff.md`
- Requirements: the frozen `task.md`, plus the settlement in `assessment-settlement.md` (A1, A2 and A8 applied)
- Range: `0c1dfd5..4239271`, one commit `4239271` "fix(foundations): settle the independent assessment of the technology change", by the private author address
- Read: the whole diff of the range, `assessment-settlement.md`, the section "Assessment settlement (turn 5)" of `author-return.md`, WAY-121 in full in its new wording, `lead/skill/SKILL.md:28-45`, and the `none` tests of `test_readiness_check.py`
- The checkout was not modified. All runs happened in a temporary detached worktree of `4239271`, which has since been removed.

## Changed files

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 8 | 9 |
| `foundations/invariants.md` | 1 | 1 |
| `project-level/lead/skill/SKILL.md` | 3 | 5 |
| `project-level/plan/skill/SKILL.md` | 1 | 4 |
| `project-level/task/skill/SKILL.md` | 1 | 6 |
| `project-level/test_readiness_marks.py` | 0 | 10 |

## Does each applied remark match the settlement?

| Remark | Settlement | What the range does | Verdict |
|---|---|---|---|
| A1 | Turn the gate clause into a state ("approved or not … goes back to the step and through the gate again"). Keep the pin move and the refinement only in the examples and the *Rationale*. Renew every fingerprint of WAY-121 | WAY-121 sentence 3 (`foundations/decisions.md:3439-3443`) now reads: "The readiness gate stops a definition whose list lacks one of the three, approved or not, and such a definition goes back to the step and through the readiness gate again; when the foundation already holds every choice the list needs, the step records the decision that holds each and settles nothing." The *Verification* examples (pin move, refinement) and the *Rationale* (WAY-34) are unchanged. The fingerprint `d0b060e5` → `068d878b` is renewed in WAY-122 (`:3529`), WAY-123 (`:3581`), WAY-165 (`:5368`) and the invariant (`invariants.md:2027`) | matches; nothing beyond it |
| A2 | Cut the additions in `plan-project` and `refine-task`. Keep one line in `lead-project` with no mark string, pointing to `define-project` | `plan/skill/SKILL.md` and `task/skill/SKILL.md` are byte-identical to the base `77c8a8b` (`git diff --stat` empty). `lead/skill/SKILL.md:38-40` keeps one clause with no mark string, pointing to `define-project` step 0 | matches (see Minor 2 for the line's reach) |
| A8 | Cut the two cases that duplicate `TechnologyMarks` | `test_the_whole_list_has_no_finding`, `test_a_section_reading_none_gives_its_one_finding` and their constants `LOGS` and `DATA` are removed. Kept: the per-mark finding, the `TODO` case and `ApprovedBefore` | matches the settlement; one of the two cases was not in fact a duplicate (Minor 1) |

Nothing outside A1, A2 and A8 changed. A3 to A7, A9 and A10 are untouched, as the settlement says.

### Rows 1, 4 and 5 in WAY-121's new wording

- **Row 1:** sentence 2 is unchanged.
- **Row 4:** "The readiness gate stops a definition whose list lacks one of the three".
- **Row 5:** "approved or not, and such a definition goes back to the step and through the readiness gate again". A definition approved before the change is an approved definition lacking one of the three, so it goes back to the step and through the gate. Row 5's meaning is kept. When the rule reaches a product is now WAY-34's business. It is still shown in the *complies* example ("a definition approved without its interface goes back to the step when the first task of its plan is refined after its product moved its pin") and in the *violates* example and the *Rationale*.
- **The exit clause:** "every such choice" became "every choice the list needs". This is the same set, the three included, as the *complies* example "its logs, its interface and its development data among them" confirms. The change is editorial and adds no meaning.
- **Sentence count:** still three binding sentences. The format guard reports 0 errors.

### My Minor 1 of the first review: settled

The gate clause now leads sentence 3, and the "when the foundation already holds…" exit clause follows the semicolon. The gate rule can no longer be read as conditional on the exit clause.

## Foundation consistency and scope

- **Fingerprints**, recomputed with `relation-model/fingerprint.py` in my scan script (`review-fingerprint-links.py`), output `review-affected-fingerprint-links.txt`:
  - WAY-121 is now `068d878b`; WAY-165 stays `a179dbe4`; the invariant `project-technology-record` stays `7fb7ab2b`.
  - 460 links scanned, 9 stale. All 9 are the deliberate fixtures in `elements/*/test_format_guard.py`, the same as in the first review.
  - No stale link anywhere in `foundations/`.
  - `d0b060e5` appears nowhere in the tree (`git grep` exit 1).
- **`foundations/invariants.md`:** the only change is the *Derives from* link (`:2027`). The sentence and its fingerprint `7fb7ab2b` are unchanged.
- **No `# invariant:` test changed:** `test_readiness_check.py`, `test_plan_state_invariant.py`, `test_plan_state_subprocesses_invariant.py` and `readiness_check.py` have an empty diff in the range. `test_readiness_marks.py` carries no `# invariant:` marker. Evidence: `review-affected-scope.txt`.

## The deliberate break still holds

`project-level/readiness_check.py` and every test that cites `project-technology-record/1` are unchanged in the range. I reran the method on `4239271`: `python -B gate/run_tests.py project-level --record <scratch>/project-level-tests-affected.jsonl` exited 0 with 267 tests OK. The record shows `project-technology-record/1` passing 30 times, the same 30 checks that failed under B1, B2 and B3 in the first review.

The test cut by A8 cites no invariant and played no part in detecting the breaks. B1 was also caught by `ApprovedBefore`, which is kept. The first review's result therefore still holds: all three breaks are detected by the unchanged checks.

## Strengths

- The A1 rewording is exactly the state the settlement asked for. It keeps row 5 through "approved or not" and moves the pin and refinement mechanics to the examples and the *Rationale*, where WAY-05 wants them. It also closes my Minor 1 with no added meaning.
- The fingerprint renewal is complete: four links, none missed, no trace of the old value left.
- A2 restores `plan-project` and `refine-task` to their base text byte for byte, rather than rewording them a third time.

## Issues

### Critical (Must Fix)

none

### Important (Should Fix)

none

### Minor (Nice to Have)

#### 1. A8 removed the only test that a section reading `none` gets exactly one finding

**Anchor:** `project-level/test_readiness_marks.py:90-99` (cut by the range); `project-level/test_readiness_check.py:436-438`

**To paste:** The settlement cut `test_a_section_reading_none_gives_its_one_finding` as a duplicate. The invariant test it was meant to duplicate, `test_none_is_reported`, uses `assertIn`, so nothing now holds that a `none` section gets its one finding and no mark findings. Restore the one case, or let the choice go unguarded on purpose?

**Why I report it:** The author chose that a `none` section gets only its "reads `none`" finding, with no three mark findings on top (I2 in `author-implementation.md`). The cut test was the only one holding that choice.

The `none` test in `TechnologyMarks` (`test_readiness_check.py:436-438`) was loosened to `assertIn` on purpose (C12), because the invariant fixes no message. It still passes if a later edit moves the mark loop above the `none` early return in `check_technology`, making a `none` section report 4 findings. The definition stays rejected, so no invariant breaks.

The effect is on routing. `settle-technology` step 3 sends "a finding that no choice item begins with one of the three marks" to step 0's rule for a list lacking one, and "any other finding of condition g" to step 1. A `none` section reporting both kinds would give the agent two routes, one of them for a list that does not exist.

The other cut case (the whole list gives no finding) really is held, by `test_a_definition_holding_all_three_marks_is_not_rejected_for_them`. The cost is low either way: `settle-technology` never writes `none`, and the fix is a four-line test.

#### 2. The kept lead-project line names only the state reader, although lead-project step 0 also runs the readiness check itself

**Anchor:** `project-level/lead/skill/SKILL.md:33-40`

**To paste:** Step 0 runs `readiness_check.py` on the definition itself (`:33`), but the kept clause sends only the state reader's `definition` finding for a missing choice to `define-project` step 0. Would "one the readiness check or the state reader reports as lacking a choice its Technology list must hold" match both places where lead-project meets the finding?

**Why I report it:** The settlement kept the line because "the lead meets the finding through another tool". In fact the lead meets it twice: once from its own readiness check run at step 0 (`:33`), and later from the state reader.

For the first, the text still reaches the right place, but only through general wording: "A draft, finding … is an obstacle" (`:35`) and "ordinary plan findings return to its owning workflow". A definition finding's owning workflow is `define-project`, so no project goes wrong. The specific clause just covers only one of the two places, which is uneven rather than harmful.

Separately, the reflow leaves a short line, "ordinary plan findings return to its" (`:40`), before "owning workflow, not a task-body repair." This is cosmetic.

## Checks

All run in a temporary worktree at `4239271`, with Git Bash and Python 3.14.

| Command | Exit | Result | Output |
|---|---|---|---|
| `python -B gate/run_tests.py project-level --record <scratch>/project-level-tests-affected.jsonl` | 0 | 267 tests OK; record: every check `pass` (`project-technology-record/1` 30, `project-plan-form/1` 49, `project-plan-check/1` 32, `project-plan-state-evidence/1` 27, `project-readiness-gate/1` 8, `project-definition-form/1` 6, `project-plan-state-subprocesses/1` 2) | `review-affected-tests-project-level.txt` |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | 0 errors, 7 warnings, 5 unchecked | `review-affected-guard-decisions.txt` |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 3 unchecked | `review-affected-guard-invariants.txt` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current | `review-affected-skill-entry-points.txt` |
| `git diff --check 77c8a8b..4239271` | 0 | no output | `review-affected-scope.txt` |
| scope: `git diff --numstat`, diff of covered code and invariant tests, `# invariant:` marker in `test_readiness_marks.py` | 0 / 0 / 1 | 6 files as listed; covered code and invariant tests unchanged; no marker | `review-affected-scope.txt` |
| fingerprint link scan and `git grep d0b060e5` | 0 / 1 | 460 links, 9 stale (the deliberate test fixtures); old value absent | `review-affected-fingerprint-links.txt` |

**Warnings, named:**
- Five pre-existing overdue check-by dates: WAY-03, 21, 52, 55, 69.
- Two expected placeholders `merge of <request link>`: WAY-121 at `decisions.md:3468` and WAY-165 at `:5388`.

**Unchecked, named:**
- With `--base none`: main-branch lines and versions, template change without a version, invariant identifiers, versions, corrections and the violated list.
- With `--merge-onto none`: `TODO`, copies of versions, relation and link fingerprints. My fingerprint scan covers these for this change.

**Not run:**
- The critical-flow tests: the handoff does not ask for them, and the author ran them with exit 0, 98 OK.
- The part-map guard: `part_map.md` did not change.
- The full gate: it does not exist yet.

## Declined to judge

- The editorial change from "every such choice" to "every choice the list needs" in WAY-121: it has the same reference, so there is no meaning to judge, and the human re-accepts WAY-121's wording at the merge anyway.
- A3 to A7, A9 and A10, which the settlement did not apply: these are the orchestrator's rulings, outside this range.
- My Minor 2 and Minor 3 of the first review (catch-up without a `held by` search; fence under a nested detail): not in this range, and unchanged.
- Whether the request lists the human-facing remarks A3 and A4 as the settlement says: that belongs to the request stage.

## Assessment

**Ready to merge?** Yes

**Reasoning:** The range applies A1, A2 and A8 as settled. Rows 1, 4 and 5 keep their meaning, and row 5 is now carried by "approved or not". Every fingerprint of WAY-121 is renewed, the invariant changed only its link, no invariant test or covered code changed, and the deliberate-break result still holds on `4239271`. The two Minor findings are a lost guard of a reporting choice and an uneven clause; neither lets a definition through.
