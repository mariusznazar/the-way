PASS ff69628c34effd01c1b886ef90a2a80245f60719

# Review of the return step's commits (`aef5b88..ff69628`)

Head confirmed: `git rev-parse HEAD` = `ff69628c34effd01c1b886ef90a2a80245f60719`. Three commits (`c8a4c32`, `bdd1b1d`, `ff69628`), diff computed with `git diff aef5b88..HEAD`. The reviewed worktree is unchanged (`git status --short` empty). Changed tests: no invariant test is changed; the test with a line `decision:` added is `test_one_of_two_citing_files_deleted_is_a_change_and_not_listed` (holds WAY-03).

Blocking findings: 0. Minor findings: 2 (one new, one carried: N2). Out of scope: 0.

## Findings

### Critical
none

### Important
none

### Minor

**m1. A stale citation of WAY-168 in WAY-241's *Rationale* and in `product-guidelines/testing/template.md:229`** (the return step's concern 1; I agree with it and its grade).
- Place: `foundations/decisions.md`, WAY-241 *Rationale* ("A field binds only where a decision of the product carries it (WAY-168)"), and `product-guidelines/testing/template.md:229` ("a field naming no decision stands as an example (WAY-241, WAY-168)").
- What: before this task WAY-168 said a rule that names no decision is an example. The task (row 4) changed WAY-168: a rule that only says how to write code, tests or the look of the product reads `none` in *Decision* and still binds. The two places cite WAY-168 for a sentence it no longer says.
- Why it is Minor and not Important: WAY-241's own binding sentence ("each field that binds naming the product's decision that carries it, a field naming none standing as an example") is a rule of its own about the `## Recipes` section, not of `## Rules` where WAY-168's `none` applies, and WAY-241 stands whether or not WAY-168 is cited. So no binding sentence of any entry is contradicted; only the reason cited for it is imprecise. A reader of the template line reads "the example rule comes from WAY-168" wrongly, which costs a wrong lookup, no wrong behaviour. The files are not files the change wrote (neither is in the range or in the task's list), so WAY-263 does not reach them.
- Settle: either leave it (no cost today; after a month a reader of WAY-168 finds a different rule than the citation promises), or in one more small commit cite WAY-173 (the decision under which a product adopts the recipes) or drop the citation in both places; editing a *Rationale* does not change a binding sentence, so no decision becomes "changed" for the check of WAY-12. Not blocking; fits the request's list of Minor findings.

**m2 (carried N2). One over-long table cell in `project-level/task/template.md:209`** (131 characters; the file's other table rows run to 161). Cosmetic, within the task, not blocking. Settle by reflowing it or leaving it on the request's list. Not a new finding of this range.

Not a finding: the new row in `elements/invariants/template.md` (217 characters) is a table row; its neighbours are as long (the *Derives from* row is longer), so the file's convention holds. No added line of `foundations/decisions.md` or the Python file exceeds 100 characters (`git diff aef5b88..HEAD | grep '^+'` measured).

## Points of the handoff

### `c8a4c32` — the clause `tests:` and the trimmed pairs of WAY-12 and WAY-03

Compared with the template `elements/decisions/template.md` ("Verification": the form `tests: <the parts of the sentences they hold, in words>. An agent compares a change with the part no invariant and no test holds:`) and with WAY-12's first paragraph: the clause has no path, no test name and no number; the form matches.

WAY-12 — each part named is held by a test whose line `decision:` quotes a sentence of WAY-12:
- "a line `decision:` of a test names a decision of the log and quotes the start of one of its binding sentences": `test_decision_line_quoting_a_sentence_passes` (line 1067, quotes "A test that holds a sentence of a decision carries beside it a line"), with the failing cases beside it (`..._quoting_no_sentence_fails`, `..._only_rationale_fails`, `..._inside_a_sentence_fails`, `..._naming_no_decision_fails`, and others, 1071-1130). Only the first carries a line `decision:`; the others hold the same sentence without one. That is no gap: one test per sentence suffices to make the decision held, and the script does not demand a line at every test.
- "which decisions the check counts as held": the three tests that quote "A decision is held when its" (lines 1291-1301: by invariant, by pair, by line).
- "the error for a decision a change adds or alters that nothing holds, and the list of any other": lines 1285, 1333 ("The check of the foundation reports as an error"), 1346, 1364 ("Any other decision that nothing holds stands").
The pair left to WAY-12 covers what no test holds: that a test holding a sentence carries the line (the script checks the line only where it exists), that a decision names invariants and tests in the given forms (the script reads the invariants named, not the form of `tests:`; it does not read the clause), the pair only for the uncovered part, rationale and rejected options kept whole, and the form of the violating example. I found no part of the pair that a test holds. One part of the clause is slightly broader than a test line shows: the check that an *invariant a decision names derives from that decision* is in the violating example ("names an invariant whose *Derives from* names another decision") and is left to the pair, which is right unless a test of the script holds it (I did not find one with a line `decision:` for WAY-12; no such line exists).

WAY-03 — "which invariants the check lists for a reworded sentence, and that the listing stops no change": the tests quoting "The check of the foundation lists an invariant whose method" (lines 1429, 1442, 1451, 1458, 1464, 1470, and the new one) and "The listing stops no change" (1477, 1485, 1497), and "A change whose check lists such an invariant" (1436, which holds the case of the changed citing file). What stays in the pair is naming in the request (altered invariant test, changed or dropped line `decision:`, reworded sentence left with its test), which no test of the script holds. Right.

*Rationale* and *Rejected* of both entries are untouched (the diff shows only the *Verification* line changes). Their binding sentences are unchanged, so the check does not count them as changed; `python -B elements/common/foundation_check.py` printed `0 errors`, no `listed:` line.

### `bdd1b1d` — `elements/common/foundation_check.py`, `test_foundation_check.py`

- Right against spec D4 ("a file counts as changed when its content differs, or it was added or deleted") and WAY-03 ("when no file that cites it has changed"): a deleted citing file is a changed file, so the invariant is not listed even when another citing file is as it was. With one citing file deleted, the existing rule (no citing file left, so no listing; the uncited-`test` error reports it) is unchanged.
- The mechanism: `git diff --name-only --no-renames --diff-filter=D -z <base>`, then `cited_names(at_commit(base, path))` for each deleted non-Markdown file; `name not in lost` joins the existing condition. A deleted Markdown file never cites (the same as `tracked` and `read`). A failing `git diff` returns with no listing, as the old call did. A rename (with `--no-renames` a delete plus an add) cites by its new file, which is in `changed`; no listing either way. Paths are as `git diff` and `git show <commit>:<path>` give them, relative to the repository's top, the same convention as `base_files` (line 673) in the same file.
- The new test fails without the correction: I removed `name not in lost` in a copy of the head at the scratchpad (`a file in the cycle's scratch directory`) and ran it: `FAILED (failures=1)`, the report held the listing. With the correction it passes. It fails for a reason (it does not compute its own expectation): it deletes a committed second citing file by `git rm` and asserts the whole report is `["0 errors"]`.
- Every other test that pins the listing passed: the full `elements.common.test_foundation_check` module, 180 tests OK (below).
- The surface `foundation-check-command` (`foundations/part_map.md:215`: path, argument, exit codes): unchanged. The correction only removes a listing (`listed:` lines change no exit code); the change adds no argument and keeps the exit codes 0, 1 and 2. The docstring of the file and of `list_invariants` say the new rule. Part `elements-common`: no sentence of the part map becomes false.

### `ff69628` — `elements/invariants/skill/decide_entry.md`, `elements/invariants/template.md`

- `decide_entry.md`: its bullet said that a rule that records a choice goes to `record-decision` first and "the invariant is written as derived from it", with no exception. WAY-22 (changed by this task, row 9) now says no derived invariant for a sentence a test holds by a line `decision:`; `elements/decisions/template.md` ("Decision or invariant", the bullet that opens "A test holds a decision's sentence by a line `decision:`") says the same. The skill, left as it was, would instruct an agent to write the second entry WAY-22 forbids, so the edit is needed and it adds only the exception and the citation (WAY-22). Within the task (row 9 is the rule; this is a file that applies the test).
- `template.md`, row *sentence* of "Fields and their readers": WAY-05 (and the template's own sentence "A field stays in this template only while someone or something reads it") ask that a reader of a field be named; the script now reads the sentence to list a reworded invariant (WAY-03, row 12), so naming it is needed, and the added text cites WAY-03. The decisions template names its readers the same way. Needed and no more.
- The part `invariants` (`foundations/part_map.md:36`, files `elements/invariants/**` and `foundations/invariants.md`; depends on `decisions`, `part-map`, `environment-facts`, `elements-common`): its statement ("what a product states as an invariant and how that statement is checked, and the invariants of the-way itself") still holds; both files belong to it; the added reader is `elements/common/foundation_check.py`, a file of `elements-common`, a part the entry already depends on. No change to the part map is needed. I agree with the return step that no part-map sentence says something false. No test reads either file (`grep` of `*.py` for both paths: no hit).

### What the return step left

- The concerns of the report: WAY-241 / `testing/template.md:229` — see m1; N2 — see m2; the long line in WAY-168's *Rationale* ("... A cheap test on a convention of the code catches a breach of its rule on every change for") stands in the log as the task's earlier commit left it (`aef5b88` and before). I measured it at over 100 characters; it is cosmetic and I grade it Minor, in the same note as m2 (settle by reflowing the paragraph in a later commit; no behaviour depends on it). It is not in the range of these three commits.
- The return step's claim that N1 is corrected: true (see `bdd1b1d`). The orchestrator's list of Minor findings can drop N1.
- The return step's claim that rows 11 and 12 stand as attached paragraphs of WAY-12 and WAY-03: true (the two entries carry them as second paragraphs; I read both whole).
- The return step's table of rows and their places: I checked rows 8, 9, 11, 12 (WAY-12, WAY-22 and WAY-03, WAY-12, WAY-03) in the text; the others are the foundation step's and were reviewed earlier (`reports/whole-review-report.md`).
- No new Critical or Important finding stands in the range.

## Declined to judge

- Whether the review skill (`task-cycle/review/SKILL.md:70`, "A changed invariant test is named in your report") should also name tests with a line `decision:`: the return step left it, the task does not carry it, and the rule of the request template (kind 7) and WAY-03 already say it. Outside the task.
- The switch `--skip-test-citations` and its name (WAY-321): the cycle's ruling stands.
- The exact set of the sentences of the part map's `elements-common` entry (it does not list every report of the script): no sentence became false; outside this range.

## Checks I ran (command and exit code)

| Command | Exit |
|---|---|
| `git rev-parse HEAD` | 0, `ff69628c34effd01c1b886ef90a2a80245f60719` |
| `git diff aef5b88..HEAD`, `git log --stat aef5b88..HEAD`, `git status --short` | 0; status empty |
| `python -B -m unittest elements.common.test_foundation_check` in the worktree (run in the background, 214 s) | 0, `Ran 180 tests ... OK` |
| `python -B elements/common/foundation_check.py` in the worktree | 0, `0 errors`, no `listed:` line |
| Mutation: in a copy of the head at the scratchpad (`...\scratchpad\mut2`, made by `git archive HEAD`), `name not in lost` removed, then `python -B -m unittest elements.common.test_foundation_check -k one_of_two_citing` | 1, `FAILED (failures=1)` (the new test fails when the correction is gone) |
| `awk 'length($0)>100'` on the added lines of the range, and on `project-level/task/template.md` | 0; only one added table row over 100 characters (a table row, in the file's convention) |

Not run: the gate with no directory (the orchestrator's alone), `gate/run_tests.py elements/invariants` (no test in that directory), the tests of other directories (no file there is in the range). I did not repeat the 199-test run of `elements/common` the return step reports: I ran the whole module that holds the listing's tests, and the check of the foundation on the worktree, which covers the trimmed `foundations/decisions.md`.

## Reach beyond the handoff (what, where, why)

- `foundations/decisions.md` WAY-02, WAY-22, WAY-241 and WAY-168 (whole entries; and WAY-168 at `ac75340` by `git show`, to compare the old and the new sentence): WAY-02 for the form of a line `decision:`, WAY-22 for the exception the skill now names, WAY-241 and WAY-168 for m1.
- `elements/decisions/template.md` ("Verification", "Decision or invariant"): to check the form of the clause `tests:` and the exception the skill now names.
- `foundations/part_map.md` (parts `invariants` and `foundation-check-command`): for the points of the handoff.
- `elements/common/foundation_check.py` (`git`, `at_commit`, `cited_names`, `list_invariants`) and `elements/common/test_foundation_check.py` lines 1040-1130, 1255-1500: to judge the correction and which test holds which part.
- `task.md` (rows 9, 11, 12) and `spec.md` (D4 and the lines that name the files that apply the rules): to judge whether the edits of `ff69628` lie within the task.
- `product-guidelines/testing/template.md:225-232`: to judge m1.

## Unread material

- The handoff and `task-cycle/review/SKILL.md`: read whole. The return step's report: read whole. `return_step.md` and `foundation_step.md` (the method the return step followed): not read; I judged against the entries and the diff, and the report's claims about their text I did not verify.
- `task.md` and `spec.md`: read the passages above (rows 9, 11, 12 of the table; lines 48, 103-107, 141, 149-166, 204 of the spec), not whole.
- The decisions: WAY-02, WAY-03, WAY-12, WAY-22, WAY-168 and WAY-241 whole; no other entry of `foundations/decisions.md`.
- `foundations/part_map.md`: the entries `invariants` and `foundation-check-command` only.
- `foundation_check.py`: the functions named above and the docstring at its head (lines 80-100), not the whole file.
- Guidelines: none read (the change holds no product code with a rule of guidelines and no interface); `reports/whole-review-report.md` and `reports/fix-review-report.md`: not read; the handoff's summary of them was taken as given.

## Searches not found or unclear

- A test of `elements/common/test_foundation_check.py` that holds the check of a decision's invariant whose *Derives from* names another decision (the first violating example of WAY-12): not found; it is left to the pair, as the report says.
- A test that reads `elements/invariants/template.md` or `elements/invariants/skill/decide_entry.md`: not found (`grep` of `*.py` for their paths).
- Whether the new row of the invariants template should name the other readers of *sentence* in the foundation (for example the review of a change): unclear and not a finding; the row is correct for the reader it names.
- Background processes: the one I started (the test run) ended; none remain.
