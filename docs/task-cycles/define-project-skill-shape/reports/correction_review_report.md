PASS 3f25d610fc803a36837e05e0498c1432757235b9

# Review of correction 1 - the human's remarks on request #85

Reviewed: a later change to an open request, a correction for the human's remarks.
Range `a0c56bb..3f25d61`, one commit, "Apply the request's proposals 1, 4, 5 and 6 at the human's
request". `git rev-parse HEAD` is `3f25d610fc803a36837e05e0498c1432757235b9`, the head given.
`git diff --stat 09b0dd0..a0c56bb` is empty, so the code before the correction is that of `09b0dd0`,
as the handoff says. Method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md`.

Read: `remarks.md`; section 4 of `assessment.md` as committed in `4f508f8`
(`docs/task-cycles/define-project-skill-shape/reports/assessment.md`); the frozen `task.md` (To do
and Acceptance criteria); `correction_report.md`; the regenerated `assessment.md` (sections 1, 2
rows touched, 4) and `word-counts.md`; `check_correction.py`; the diff, by
`git diff --word-diff=plain a0c56bb..3f25d61`.

## Findings

### Critical

None.

### Important

None.

### Minor

- **`assessment.md` section 4, proposals 4 and 5 (record file, not code).** Each keeps its old
  reasoning for not applying ("Verdict: not recommended in this change", "Proposed rather than
  applied because the series keeps the rebuild to a change of place") and then adds "Applied
  (correction 1)". The "Applied" line resolves it, and the section's opening paragraph names the
  correction, but a reader skimming the bullets meets two answers. This is a record of the cycle,
  not a file of the-way; it blocks nothing.

Blocking findings: none. Out-of-scope findings: none.

## Each remark, as made or not

1. **Proposal 1 - made.** `project-level/skill/delegated_mode.md` no longer holds "The project
   orchestrator may make the initial text edit ...; otherwise it delegates the edit."; its second
   paragraph now begins "A subagent always performs step 7, including the whole-foundation
   collision search and all checks." (`delegated_mode.md:15`), which stays. The word diff shows
   only the removal and the three "readiness" insertions of proposal 4; the paragraph was
   rewrapped, the first paragraph not. The paragraph reads on: the removed sentence's "that full
   text" referred to nothing the next sentence needs. No act of the dispatched agent depended on
   it; the rule stays with its actor at `project-level/lead/skill/SKILL.md:206-208` ("You may edit
   definition text only when its full text is already before you ... Otherwise delegate the
   edit."), which I read to confirm. No acceptance criterion names the sentence; the criterion on
   the delegated mode reaching step 7 (no own question to the human, no own critique, no
   fingerprint or `approved` before recorded approval) still holds by `delegated_mode.md:15-22`.
2. **Proposal 5 - made.** `project-level/skill/SKILL.md:13` and `:45` now name
   `project-level/definition_template.md`. `grep -rn "definition_template\|template"
   project-level/skill/` finds no other mention by file name: the step files say "the template"
   (`first_write.md:7`, `:9`, `rounds.md:7`, `:15`, `:20`, `technology.md:9`, `SKILL.md:34`), which
   names no path to get wrong. `check_instructions.py` on the ten files gives no line naming
   `definition_template` (count 0).
3. **Proposal 6 - made.** The five rewordings read "each skill named below or in the files beside
   this skill is the project skill of that name with the `the-way-` prefix", in
   `elements/common/skill/SKILL.md:19`, `product-guidelines/coding/SKILL.md:22`,
   `product-guidelines/styleguide/SKILL.md:21`, `product-guidelines/testing/SKILL.md:21`,
   `project-level/plan/skill/SKILL.md:17`. I checked each against its files beside it: each has a
   file beside it naming a skill of the-way that its `SKILL.md` does not name (for example
   `elements/common/skill/definition_variant.md` names `find-foundation-entries` and the four
   `record-*` skills; `product-guidelines/coding/research.md` names `critique`;
   `project-level/plan/skill/critique_plan.md` names `critique`). `task-cycle/plan/SKILL.md` is left
   as it is, and rightly: its one file beside it, `task-cycle/plan/too_large.md`, names no skill
   (read whole). The grep finds seven files; the seventh is `project-level/skill/SKILL.md`, already
   reworded. No other words of those files changed (word diff; `check_correction.py`), no
   `description` changed.
4. **Proposal 4 inside this skill - made.** Eight uses now read "the readiness gate" or "readiness
   gate": `SKILL.md:40` (two), `delegated_mode.md:20`, `:24`, `:27`, `existing_definition.md:11`,
   `:15`, `readiness_gate.md:23`, `:24`. `grep -rn -i gate project-level/skill/` leaves only fixed
   names: the heading "Delegated definition change and gate" (`SKILL.md:26`,
   `delegated_mode.md:1`), "gate record" (`delegated_mode.md:21`, `first_write.md:9`,
   `readiness_gate.md:8`, `:40`), the quoted status `ready for gate` (`technology.md:9`), the file
   name `readiness_gate.md` and its heading "The readiness gate". No "gate" changed outside
   `project-level/skill/` (word diff). `foundations/decisions.md` (WAY-118),
   `project-level/definition_template.md` and `foundations/glossary.md` are not in the diff.

Nothing else changed: the diff touches nine Markdown files; `check_correction.py 3f25d61` shows
each equals its parent after only the named substitutions, line breaks ignored.

## The regenerated figures, recomputed

Per-file counts with `LC_ALL=C.UTF-8 wc -w` on `git show` of each file, parent `a0c56bb` -> head:
`SKILL.md` 570 -> 572, `delegated_mode.md` 342 -> 314, `existing_definition.md` 205 -> 207,
`readiness_gate.md` 567 -> 569, the six other files unchanged (108, 98, 82, 109, 240, 66); all ten
files 2387 -> 2365. The net -22 is -31 (proposal 1's sentence, recounted by hand: 31 tokens) + 9
"readiness" insertions, and proposal 5's path is one token either way. These match
`word-counts.md` ("After").

Route sums recomputed from those counts and the unchanged files read beside (3221 + 208 + 503 for
route 1; 3221 + 208 for routes 2, 4, 5; plus 1419 for 3a and 3b): skill text 1844 / 1522 / 1662 /
2365 / 1348 / 1414, totals 5776 / 4951 / 6510 / 7213 / 4777 / 4843, and the percentages -4.8 /
-21.4 / -14.2 / +22.1 / -30.4 / -27.0 and -1.6 / -7.7 / -4.1 / +6.3 / -11.0 / -9.7 all match
`word-counts.md` and the table of `correction_report.md`. The six recorded runs recomputed: 3a
9840 / 36593 (-15.3%, -4.6%), 3b 12652 / 39405 (+8.9%, +2.7%), matching. `SKILL.md` alone 572
stays inside the task's estimate of 500-600.

The new places in the regenerated `assessment.md` rows I checked against the head files:
`delegated_mode.md` 15-17, 17-22, 24-28; `existing_definition.md` 6-12, 13-19;
`readiness_gate.md` item 2 at 17-27; `SKILL.md` 6-15 - each holds the fragment its row names.

## Declined to judge

- The wording "after the readiness gate goes through the readiness gate again" (`SKILL.md:40`):
  heavy, but the remark asks for "the readiness gate" literally, and the author names the choice.
- The resulting difference of words between the skill and WAY-118 / the template: the human
  accepted it in the remark.

## Checks

All in the worktree at `3f25d61`.

| Command | Exit code / result |
|---|---|
| `git diff --word-diff=plain a0c56bb..3f25d61` | manual: only the four remarks' substitutions and rewraps |
| `python -B <reports>/check_correction.py 3f25d61` | 0; "9 files changed; 0 differ beyond the named substitutions" |
| `python -B <reports>/check_correction.py eeca32c` (shown failing) | 1 |
| `python -B <reports>/compare_sentences.py` | 0 (it rewrote its own output `compare_sentences.txt`; see below) |
| `python -B <reports>/check_pointers.py` | 0; "10 files; 0 failures" |
| `python -B <reports>/verify_counts.py <reports>/word-counts.md <reports>/assessment.md <reports>/correction_report.md` | 0; "263 figures compared, 0 differ" |
| `LC_ALL=C.UTF-8 wc -w` per file of `project-level/skill/` at `a0c56bb` and `3f25d61` | manual recount, above; matches |
| `python -B agent-instructions/skill_entry_points.py` | 0; "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file <each of the ten files of project-level/skill/>` | 0; `0 error, 1 warn, 12 info`; no line on `definition_template` |
| `python -B instruction-files/check_instructions.py . --file <each of the nine changed files>` | 0; `0 error, 6 warn, 8 info` |
| `python -B elements/common/foundation_check.py .` | 0; "0 errors" |
| `python -B gate/run_tests.py project-level` | 0; 271 tests OK |
| `python -B gate/run_tests.py elements/common` | 0; 109 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0; 18 tests OK |
| `awk 'length>100'` on each changed file, parent and head | manual: no new line over 100 characters |
| `git grep "skill named below"` outside `SKILL.md`, and `git grep -i "after the gate goes\|blocks the gate\|pending gate"` | manual: no file quotes the old wording |

Not run: `gate/run_tests.py product-guidelines` (the directory holds no test; the author reports
exit 1 "no test found" on parent and head alike), `task-cycle` and `installation` tests (no file
there changed), the whole gate (the orchestrator's).

Note on a write: running `compare_sentences.py` rewrote its own output file
`reports/compare_sentences.txt` (same size, 2642 bytes; the script is deterministic over the same
tree). No other file was written besides this report.

## Reaches beyond the dispatch

- `project-level/lead/skill/SKILL.md:200-212`: to confirm the orchestrator keeps the removed
  sentence's rule (proposal 1).
- `task-cycle/plan/too_large.md` whole, and the backticked skill names in the files beside each of
  the other five candidate skills: to judge which way proposal 6 should go for each.
- `task-cycle/review/fix.md`: named by the method for a correction.

## Searches not found or unclear

- The handoff's "Answers of step 4" (trust boundary, irreversible operation) does not match a step
  of `task-cycle/review/SKILL.md`, whose section 4 is the report; I read it as the answers the
  review's section 2 asks about trust boundaries and irreversible operations.
