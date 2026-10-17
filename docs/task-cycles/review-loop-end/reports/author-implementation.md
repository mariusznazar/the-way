# Author report — implementation (turn 2)

Status: **done** — code committed, boundary reached before review. Same author as the foundation
step (general-purpose subagent, claude-opus-5-5), one-author route.

## Inputs and commits

- Handoff `reports/author-implementation-handoff.md` (rulings C5–C9 on the six concerns).
- Input commit `0761d6d` (foundation step), base `e7f7c3a`.
- Authority: frozen `task.md`; WAY-125 (edited) and WAY-161..164 as written in `0761d6d`.
- Read: `task-cycle/skill/SKILL.md` and `task-cycle/record_template.md` whole; skill conventions
  note (read only) — applied its rule that a correction replaces the sentence that stood rather than
  appending beside it; `task-cycle/plan/SKILL.md` searched (no review-loop or executor duty to change).
- Superpowers `test-driven-development` not applied: the change is prose of a skill and a record
  template, no behaviour change in code (handoff; WAY-12/22).
- Commit: `d88728d` docs(task-cycle): end the whole-change review loop and add the weakest-point
  check.

## Changed files (`0761d6d..d88728d`)

| File | Added | Removed |
|---|---|---|
| `task-cycle/skill/SKILL.md` | 100 | 35 |
| `task-cycle/record_template.md` | 12 | 0 |

Skill name, description and path unchanged; `python -B agent-instructions/skill_entry_points.py`
reports "entry points are current" (no `--write` needed).

## Coverage (line numbers in `task-cycle/skill/SKILL.md` at `d88728d` unless named)

| Item | Where |
|---|---|
| To do 1 / row 1 — one fix, one review of the fix, then a blocked draft with remaining findings (place, reason), what the fix tried, cost from `stages.md` with review rounds; no orchestrator ruling; slice loops unchanged | intro `:17-19`; new section "The end of a code review" `:392-428` (`:403-408` fix bound, `:414-422` blocked path, `:424-428` replaced Superpowers steps and unchanged slice loops); step 9 `:303-305`, `:315`; step 13 `:485-489`; template `:46-49`, `:154-156` |
| Row 2 — remaining finding not into step 11's settlements; new Critical/Important in the fix counts as remaining | `:407-408`, `:414-415`; step 11 `:373-375` |
| Row 3 — same bound for later code reviews (step 11 settlement, step 12 reconciliation, correction) | `:408-412`; step 11 `:373-375`; step 12 `:439-440`; correction `:507-508` |
| Row 4 — gate and record before the blocked request; return step and assessment not run, named, run after the human's decision | `:415-422`; step 10 `:340-342`; step 12 `:432-433`; step 13 `:485-489`; correction `:508-511`; template `:154-156` |
| To do 2 / row 5 — Critical/Important block unless marked outside scope; no blocking finding → request without a fix; Minor listed | `:394-401`; step 13 `:468-472`; template `:151-153` |
| To do 3 / row 6 — reviewer's own out-of-scope marks ("Declined to judge" line or described as beyond the task) not fixed whatever the grade, listed with reviewer's words and place (or a note that none is named, ruling C6), human creates tasks; no moving between kinds | `:396-400`; step 13 `:468-472`; template `:151-153` |
| To do 4 / row 7 — author and each executor: requirement most likely unmet, check, report; reviewer receives report; request lists it | step 9 `:290-297`; step 13 `:468`; template `:50-51` |
| Ruling C5 — later reviews' non-blocking findings cause no fix and stay in their reports linked from the record; no request list | `:411-412` |
| WAY-125 departures named in the skill | `:424-428` |
| "Nothing is deferred" limited to foundation entries | step 11 `:356-358` |
| Record of review rounds | step 14 `:492-493`; template `:46-49` |

## Choices

| # | Choice | Rejected | Cost if wrong |
|---|---|---|---|
| I1 | One new section "The end of a code review" holds the rule once; steps 9–13 and the correction point to it. | The rule repeated in each step — copies drift. | Low; a reader follows one reference. |
| I2 | A request blocked by its review skips step 12's reconciliation (recheck against the target, refreshed selection, its reviews and assessment) and starts at opening the request; the correction after review starts with merging the target branch anyway. Basis: answer 7's principle — no agent work on code the review has not accepted; the full gate already ran in step 10. | Reconciling before a blocked request — its affected code review and assessment would run on unaccepted code, against WAY-163. | If the human wants the blocked draft reconciled first, one sentence of step 12 changes. Flagged for the reviewer. |
| I3 | Review of the fix: same reviewer for a one-author change, `subagent-driven-development`'s scoped re-review for a planned change (both kept from the current text and method). | Requiring the same reviewer on both routes — not in WAY-162. | None. |
| I4 | Step 10's "resolve review findings from their evidence" becomes "resolve questions about review findings … within 'The end of a code review'". | Leaving it — it read as the orchestrator resolving findings itself. | Low. |
| I5 | Record template: two new fields in "Spec and execution route" (Review rounds, Weakest-point checks) and two in "Request handoff" (Review findings listed, Blocked by review). | Folding everything into "Whole-change review" — later reviews have no place there. | Low. |
| I6 | No change to `task-cycle/plan/SKILL.md`: WAY-164 binds executors when they make a slice, which step 9 already sets; the plan holds no review loop. | Adding the duty to slice briefs in the plan skill — a second copy. | If executors miss it, the dispatch handoff must carry it (orchestrator's step 9). |

## Weakest-point check (WAY-164)

- **Requirement most likely unmet:** To do 1 with rows 1–3 — "no third round and no ruling by the
  orchestrator" holds only if no older sentence elsewhere in the skill still lets the orchestrator
  rule on, park, defer or keep fixing review findings, or allows more fix rounds.
- **Check:** scripted search (scratch script `weakest_point_check.py`, run as
  `python -B <scratchpad>/weakest_point_check.py .`): (a) prints every line of the skill and the
  template that speaks of findings, fixes, rulings, parking, deferral, minor findings, re-review or
  resolving, for classification; (b) asserts 24 anchor phrases, one or more per row 1–7, the
  intro stop, the scoped no-deferral rule and the four template fields. Output:
  [implementation-weakest-point-check.txt](implementation-weakest-point-check.txt), exit 0.
- **What it showed:** (b) 0 missing. (a) classified by hand: the superseded sentences are gone
  (old step 9 fix sentence, "final review and fixes", "Nothing is deferred", "resolve review
  findings"). Two older sentences remain that let the orchestrator "settle a finding"
  (`:158`, WAY-148) or give "a ruling" on a finding after reading its evidence (`:299`, WAY-158).
  They govern evidence reading and are not superseded by WAY-161/162, which bind the outcome; I
  left them, but they leave room for an orchestrator to argue a blocking finding away before its
  fix — see concern 1. All other hits are unrelated (open design choice while fixing, undetected
  break, unresolved concerns).

## Commands, exit codes, outputs

| Command | Exit | Output | Summary |
|---|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | [implementation-tests-task-cycle.txt](implementation-tests-task-cycle.txt) | 41 tests OK |
| `python -B gate/run_tests.py gate` | 0 | [implementation-tests-gate.txt](implementation-tests-gate.txt) | 98 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | [implementation-tests-agent-instructions.txt](implementation-tests-agent-instructions.txt) | 18 tests OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | [implementation-skill-entry-points.txt](implementation-skill-entry-points.txt) | entry points are current |
| `git diff --check` (before commit) | 0 | [implementation-diff-check.txt](implementation-diff-check.txt) | empty |
| weakest-point check (above) | 0 | [implementation-weakest-point-check.txt](implementation-weakest-point-check.txt) | 0 anchors missing; classification above |

No foundation file changed in this stage, so no format guard ran. No warnings or `unchecked`
results in these outputs. Not run: the full required gate (orchestrator, step 10).

## Sharpness inputs from the actual diff

- Criticality: both files belong to part `task-cycle` — three failure modes, all high, not
  detected. High.
- Trust-boundary files: none (`task-cycle` declares none).
- Irreversible operations: none.

## Unresolved concerns

1. Before the fix, `:158` (WAY-148) and `:299` (WAY-158) still let the orchestrator settle or rule
   on a finding after reading its evidence; neither WAY-161 nor WAY-162 says whether the
   orchestrator may set aside a blocking finding as wrong before its one fix (requesting-code-review
   "Push back if reviewer is wrong"). WAY-161's "the orchestrator moves no finding from one of these
   kinds to another" covers re-grading, not rejecting. A reviewer should judge whether this is a
   loophole; closing it would be a foundation question, not a skill edit.
2. Choice I2 (blocked request skips step 12's reconciliation) is mine, from answer 7's principle;
   the reviewer should check it against WAY-163.
3. The failure-mode candidate from turn 1 waits for the return step (ruling C9).

## Addendum 2b

Input `d88728d`; handoff `author-implementation-fix-handoff.md` (rulings C10, C11). Commit
`ac65ac3` docs(task-cycle): keep blocking findings from being overruled before their fix.

### Changes (line numbers in `task-cycle/skill/SKILL.md` at `ac65ac3`)

- C10, "The end of a code review" `:406-410`: the orchestrator never overrules a blocking finding
  or skips its fix; an author or executor that holds a blocking finding wrong answers it with
  evidence in its fix report, and the review of the fix keeps or drops it.
- C10, general sentences qualified: `:157-159` "settling a finding within 'The end of a code
  review'"; `:299-301` "a question about a finding needs a ruling, which never overrules the
  reviewer's grade or scope marking ('The end of a code review')".
- C11: the blocked path names "the reconciliation with the target branch of step 12" (`:423-424`);
  step 13 lists it among what has not run, beside the return step and the assessment (`:495-497`);
  record template "Blocked by review" names it (`record_template.md:156-157`).
- Lines over 100 characters that these replacements produced were split in place without
  reflowing the rest of their paragraphs (ragged but minimal diff), including one from `d88728d`
  (`:449-450`).

### Changed files (`d88728d..ac65ac3`)

| File | Added | Removed |
|---|---|---|
| `task-cycle/skill/SKILL.md` | 24 | 15 |
| `task-cycle/record_template.md` | 2 | 1 |

### Checks rerun (on `ac65ac3`)

| Command | Exit | Output | Summary |
|---|---|---|---|
| `git diff --check d88728d HEAD` | 0 | [implementation-2b-diff-check.txt](implementation-2b-diff-check.txt) | empty |
| `python -B gate/run_tests.py task-cycle` | 0 | [implementation-2b-tests-task-cycle.txt](implementation-2b-tests-task-cycle.txt) | 41 tests OK |
| `python -B gate/run_tests.py gate` | 0 | [implementation-2b-tests-gate.txt](implementation-2b-tests-gate.txt) | 98 tests OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | [implementation-2b-skill-entry-points.txt](implementation-2b-skill-entry-points.txt) | entry points are current |
| weakest-point check (`python -B <scratchpad>/weakest_point_check.py .`) | 0 | [implementation-2b-weakest-point-check.txt](implementation-2b-weakest-point-check.txt) | 0 anchors missing |

No warnings or `unchecked` results. `agent-instructions` tests not rerun (no file of that part
changed since turn 2).

### Weakest-point check result

Changed: the two lines it flagged (`:158`, `:299`) now point to "The end of a code review" and
say a ruling never overrules the reviewer's grade or scope marking, and that section forbids
overruling a blocking finding before its fix. Concern 1 of turn 2 is resolved; concern 2 is
accepted (C11) and the reconciliation is now named in the blocked request. No other hit changed
class.

## Fix (turn 3)

Input `ac65ac3`; handoff `author-fix-handoff.md` (rulings C12–C14); review `review.md`
(With fixes: 0 Critical, 2 Important, 4 Minor). Commit `78df576` fix(task-cycle): describe the
replaced review steps and order the blocked request (new commit; no amend).

### Per finding (line numbers at `78df576`)

- **Important 1 (C12, route ii).** WAY-125's binding sentence now names the replaced steps as the
  methods have them: the orchestrator adjudicates and parks the findings left after the review of
  the final fix, the final fix takes in deferred minor findings, and the executor rules on each
  "Declined to judge" line; "findings outside the task wait in the method's ledger" is gone
  (`foundations/decisions.md:3624-3628`). Its *violates* and rationale already matched and are
  unchanged. WAY-161's *Based on* no longer quotes "Out-of-scope observations go to the ledger …"
  (no sentence of WAY-161/162 relies on it; `:5105-5106`). WAY-125's fingerprint moved
  `18d08c16` → `f3e6afcf` and was renewed in WAY-140 (`:4320`), WAY-148 (`:4642`), WAY-157
  (`:4979`), WAY-161 (`:5107`), WAY-162 (`:5173`), each checked against the new binding part.
  WAY-161..164 binding parts are unchanged (fingerprints as before). Skill: the replaced-steps
  paragraph is corrected the same way (`task-cycle/skill/SKILL.md:434-438`), and the section says
  an issue the scoped re-review reports outside the fix diff stays a deferred minor finding and goes
  to the request's list of Minor findings (`:414-416`).
- **Important 2 (C13).** Before opening a blocked draft the cycle now runs
  `task-cycle/cycle_stages.py` for `stages.md`, writes the record and commits its copy and removal,
  then opens the draft, swaps `<request link>`, links the record by the SHA of its adding commit
  and marks it `blocked` (`:426-430`); step 12's first sentence says the same (`:442-444`).
  WAY-163 not reworded.
- **Minor 1.** The section opens with "the review of step 9 of a one-author change or a plan of one
  slice, or the final whole-branch review of a plan of more slices" (`:396-397`), and the fix of a
  plan of one slice is reviewed "by the same reviewer for a one-author change or a plan of one
  slice" (`:409-411`).
- **Minor 2.** Step 9's planned boundary: "the final review, its one fix and the review of that
  fix" (`:306-307`).
- **Minor 3.** One sentence: the handoff of the review of the fix asks the reviewer to state, for
  each finding contested with evidence, whether it keeps the finding, since the scoped re-review's
  "NOT ADDRESSED" alone does not settle it (`:411-413`); the earlier "keeps or drops" clause is
  replaced by it.
- **Minor 4.** Reflowed to ≤ 100 characters the paragraphs I had touched with ragged lines:
  `:157-166` (reading rule), step 9 `:288-301` and its first bullet `:302-310`, the first paragraph
  of step 11 `:345-366` (it held "No foundation entry is deferred"), the whole section
  `:394-438`, step 12 `:442-472`, step 13 `:474-497`. Only wording changes noted above; the rest of
  those paragraphs is rewrapped, not reworded. Lines over 100 characters left in the file
  (frontmatter description, `:207`, `:242`, `:339`) predate this task.

### Changed files (`ac65ac3..78df576`)

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 10 | 11 |
| `task-cycle/skill/SKILL.md` | 136 | 135 |

(`task-cycle/record_template.md` unchanged in this fix.)

### Checks (on the working tree identical to `78df576`)

| Command | Exit | Output | Summary |
|---|---|---|---|
| `git diff --check` | 0 | [fix-diff-check.txt](fix-diff-check.txt) | empty |
| `python -B gate/run_tests.py task-cycle` | 0 | [fix-tests-task-cycle.txt](fix-tests-task-cycle.txt) | 41 tests OK |
| `python -B gate/run_tests.py elements/decisions` | 0 | [fix-tests-decisions.txt](fix-tests-decisions.txt) | 169 tests OK |
| `python -B gate/run_tests.py gate` | 0 | [fix-tests-gate.txt](fix-tests-gate.txt) | 98 tests OK |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | [fix-guard-decisions.txt](fix-guard-decisions.txt) | 0 errors, 10 warnings (5 pre-existing passed check-by dates WAY-03/21/52/55/69; 5 placeholders WAY-125, 161–164), 5 unchecked from the `none` options |
| `python -B agent-instructions/skill_entry_points.py` | 0 | [fix-skill-entry-points.txt](fix-skill-entry-points.txt) | entry points are current |
| whole-log fingerprint recount (scratch script, guard parser + `relation-model/fingerprint.py`; manual method, output kept) | 0 | [fix-fingerprints.txt](fix-fingerprints.txt) | 446 relation and invariant links checked, 0 stale |
| weakest-point check (`python -B <scratchpad>/weakest_point_check.py .`) | 0 | [fix-weakest-point-check.txt](fix-weakest-point-check.txt) | 0 anchors missing |

### Polish meaning sentence of WAY-125

Changed. New sentence: Cykl nadal przyjmuje metody Superpowers 6.4.1, ale w recenzji całej zmiany
ustępują WAY-161 i WAY-162 te kroki tych metod, w których orkiestrator rozstrzyga i odkłada uwagi
pozostałe po ponownej recenzji końcowej poprawki, końcowa poprawka obejmuje odłożone uwagi Minor, a
wykonawca rozstrzyga każdą pozycję listy „Declined to judge”. The meaning sentences of WAY-161..164
are unchanged; the ledger step for observations outside the fix diff stays (they reach the request
as Minor findings, which WAY-161's sentence already covers).
