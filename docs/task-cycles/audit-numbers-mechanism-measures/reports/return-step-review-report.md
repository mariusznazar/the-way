FAIL a1b2d471b96479ab9e26d5e3cfdcaad20f90a23b

# Review of the return step's commits, `1e2c028..a1b2d47`

`git rev-parse HEAD` is `a1b2d471b96479ab9e26d5e3cfdcaad20f90a23b`, the head given. One commit in the range, `a1b2d47`.

Blocking: 1. Minor: 2. Out of scope: 1.

## Changed files

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` (WAY-344 only) | 26 | 21 |
| `foundations/part_map.md` | 2 | 1 |

No code file and no test file changed in the range.

## Findings

### Important (blocking, within the task)

**I1. WAY-344 now lists two earlier-form readings; the code makes a third, and a test pins it.**
`foundations/decisions.md:11349-11353` (binding paragraph), `:11375-11378` (*complies*), and the *Rationale* price at `:11414-11418`.

What the entry says: the count reads a file as an earlier form, with no `Error:` and no change of the exit code, "for a stage report that has no heading of its detailed section and holds a table of tokens by model, and for one that has neither of its two time lines". The return step's report calls these two cases "the whole of what the count reads as an earlier form".

What the code does: a third case. `process-audit/audit_count.py:938-941` (`section_table`) says "the column *Files named* is never one [a missing field]: a section without it is the earlier form of the section". `audit_count.py:957` sets `named` from the header row, and `:1357-1358` (`fix_rounds_share`) turns a missing column into the share of fix rounds as unknown with the reason "`stages.md` has no column `Files named`: an earlier form", with no `Error:`. Test `process-audit/test_audit_count.py:1342` (`test_the_column_files_named_is_never_a_missing_field`) pins exit 0, no `Error:` and a cost, for a newer section without the column. I ran it: OK.

Why it matters: the paragraph's rule is that a missing field ends the count with exit 1 and an `Error:` line, and the two cases are its only listed exceptions. By the entry as worded, a detailed section whose table lacks the column *Files named* is a missing field and must give `Error:`. The code gives none, and its own test requires none. The entry says something narrower than what the code does, so a later reader or reviewer holding the code to WAY-344 would call the third reading a violation, and the *Rationale* price does not name it either (WAY-263: an entry the change writes that restates the code differently). The whole-change fix wording (`8bb47d5`, "where the file's other signs name that form") covered this case in general; the narrowing by this commit is what dropped it. The return step read `audit_count.py` lines 915-1026, which include the docstring at `:940`, and its comparison table does not mention the column.

Fix, one clause in three places: add to the cases in the binding sentence "and for a detailed section whose table has no column *Files named*", to the *complies* case "a stage report whose detailed section has no column *Files named*" and to the price in the *Rationale* ("or its section without the column *Files named*"). Keep the paragraph at three sentences.

### Minor

**M1. `foundations/part_map.md:240` — "the script of the gate" is ambiguous.** The part map has a part `gate` with `gate/run_tests.py`, and the registry is kept by `task-cycle/gate_times.py`, which is in `task-cycle`. A reader of the external-context table can read "the script of the gate" as `gate/run_tests.py`. Name it: "the script that runs the gate for the task cycle". The row's grammar is also stretched: "the places its entries name, such as ..., and the registry ..." reads the registry as a place an entry names, and it is a fixed place (`~/.the-way/gate_runs`, WAY-350) that no entry of the locations file names. Not blocking: no reading of the row is false.

**M2. `foundations/decisions.md:11349-11353` — the second binding sentence is one 14-line sentence.** The return step folded the clause into it to keep three sentences (the sentence count is right: three). The clause after the dash is hard to parse in one pass; with I1 fixed it grows again. Splitting the sentence would give four, which the template's "Binding sentences" does not allow, so a shorter wording of the clause is the way; for example name the cases once as a list inside the one sentence. Polish.

### Out of scope (code not in this range; named because the boundary exists for it)

**O1. `task-cycle/gate_times.py:189-209, 211-232` — a crafted registry entry is never pruned and counts forever.** An ended entry named `<start>_<far-future end>_<token>.run` is deleted only when `end < now - DAY_MS` (`:199`), so it stays, and `met = begin < end and finish > start` (`:228`) counts it as another run in every later run. The audit then finds a company at every gate run and gives no median. This is the crafted-input risk that the trust boundary recorded in this range exists to have reviewed; it supports recording the boundary and is a Minor finding for the next change of the script. A decision on it is not this step's.

## Judgment of the points the handoff names

1. **WAY-344 says what the code does and nothing wider.** Nothing wider: both listed cases match the code. The time-line case: `audit_count.py:1657-1671` (`fill`) gives a time as unknown with no `Error:` where neither line is there, and a missing field (with `Error:`) where one is there and not the other (tests `:1317` and `:1332`). The case of the older form: `stage_table` (`:923-934`) and `older_table` read a table of tokens by model where the heading is absent, and miss `FIELD_SECTION` and `FIELD_OLDER_TABLE` where the table is absent too. The new *violates* item ("holds one of its two time lines and not the other as the earlier form") is the code's behaviour. It is not complete: I1.
2. **Folded into the second binding sentence.** The paragraph has three sentences. Holds.
3. **The part-map change holds against WAY-48. Grade: holds, no finding.** WAY-48 and the template (`elements/part-map/template.md:119-121`) name "files that come from outside the product, such as one on the user's disk" and exclude only "a script that only checks the product's own files". `gate_times.py` does more than check the product's own files: it lists, parses by name, creates, renames and deletes entries in `~/.the-way/gate_runs`, a place outside every repository that other sessions write to, and the external-context row already marks such places untrusted. The whole-change review's choice (c) (`reports/whole-change-review-report.md:62-65`) is not contradicted: it judged the other ground, the output of the product's own gate, which is the product's. The return step's Choice 6 names both grounds; only the registry ground carries, and the output-of-the-gate ground alone would not. O1 shows what a review aimed at crafted input has to look at in the script.
4. **The external-context row change** matches WAY-350, which says where the registry lies.
5. **Foundation check passes:** `python -B elements/common/foundation_check.py`, exit 0, `0 errors`.
6. **It writes no entry the task or a decision does not call for.** The diff holds WAY-344 (settlements row 6) and the part map (the return step's duty by `task-cycle/skill/return_step.md:6-8`, corrected to match the code). No new decision, invariant, glossary term or environment fact.

## Declined to judge

- The correctness of `audit_count.py` and `gate_times.py` beyond what the two entries say of them: reviewed and passed in the whole-change review, `2292f33..1e2c028`, not part of this range.
- The foundation entries WAY-347 to WAY-352 and WAY-339: unchanged in this range.
- Whether the human prefers a stricter code reading of the time lines (the report's Choice 1): the choice stands within the task, which wants an earlier form read by its own marks.

## Checks run

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `a1b2d471b96479ab9e26d5e3cfdcaad20f90a23b`, matches |
| `git diff --numstat 1e2c028..a1b2d47` | 2 files, as above |
| `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| `python -B -m unittest process-audit.test_audit_count -k test_the_column_files_named` | exit 0, 1 test OK |
| the product's gate | not run, as instructed |

Manual: read `audit_count.py:905-1026, 1340-1362, 1630-1672`; `task-cycle/gate_times.py` whole (315 lines); WAY-344 whole (`foundations/decisions.md:11336-11440`); WAY-48 whole; the part-map `task-cycle` entry and the external context; `task-cycle/review/SKILL.md` sections 1-4.

## Reaches beyond the dispatch

- `elements/part-map/template.md:115-155` (the trust boundary and the external-context rules): to judge the part-map change against what the template says a boundary is.
- `task-cycle/skill/return_step.md:1-30`: to see what the return step is bound to write.
- `process-audit/test_audit_count.py:1317-1350`: to check which earlier-form readings a test pins (it found the test of I1).
- `git show 2292f33:process-audit/audit_count.py` (grep only): the reading of *Files named* is from before the change, so the third case is not new code.

## Unread material

- `process-audit/audit_count.py`: read lines 720-750, 905-1026, 1340-1362 and 1630-1672 of its length; not read: the rest (the whole-change review read it).
- `process-audit/test_audit_count.py`: read by name (`grep`) and lines 850-866 and 1317-1350; not whole.
- `task-cycle/gate_times.py`: read whole.
- The whole-change review report: read the grade lines on choice (c), the table row 45 and M5-M7; not whole.
- `task-cycle/skill/foundation_step.md`: grepped for part-map rules, not read whole.
- The rest of the decision log and the invariants: not read; only WAY-344 and WAY-48 whole.
- `plan.md` and the other reports of the cycle: not read.

## Searches not found or unclear

- A decision or invariant that says a column of the stage report counts as a field of the count: not found; WAY-344 defines a field generally ("any named thing the script looks for data by in the file: ... a table column"), so *Files named* is one by that definition, which is why I1 stands.
- Whether the human saw the clause as worded: unclear; the report says the human did not (mark "the cycle's"), so I1's fix needs no human decision beyond the orchestrator's.
