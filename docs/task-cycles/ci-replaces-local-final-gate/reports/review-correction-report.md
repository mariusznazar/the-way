PASS cdfcf480a4751a10fe57a198d9ed41b553fe67af

# Review of correction 1 — ci-replaces-local-final-gate

- Range: `026308ff53ac44fe7ba43862974435d017f3891e..cdfcf480a4751a10fe57a198d9ed41b553fe67af`. One commit, `cdfcf48`, which changes `guidelines/coding-shared-module.md` only. `git rev-parse HEAD` gives the head named.
- What bounds this review: the human's remarks in `reports/correction-1-remarks.md`, used in place of a findings file (`task-cycle/review/fix.md`, the case of a correction), and the correction's diff.
- Counts: 0 new Critical or Important findings, 2 new Minor notes.

## The remarks, one by one

- **Remark 1** (the required check `tests-windows`, the environment fact left as it is, the request marked ready): **made** for the part a commit can hold. No file in the range changes `foundations/environment_facts.md`, so `foundations-branch-ruleset` stays as the remark asks. The description and the request's state are the orchestrator's and lie outside this range.
- **Remark 2** (fix N-3: the line that places `process-audit/stage_pricing.py` under the kind `shared-module`, in its *Applies to*, beside `relation-model`): **made**. `- **Applies to:** relation-model` now reads `relation-model · process-audit`.
  - This adds the part of `stage_pricing.py`. The part map assigns `process-audit/**` to the part `process-audit`.
  - `product-guidelines/reading.md` makes an agent read a guideline file whole where its *Applies to* names an affected part. The kind row in `guidelines/coding.md:21` sends to this file whoever adds or changes a module that other scripts import. So the next author of such a module in `process-audit` now finds the kind.
  - The added `- \`process-audit/\`` under *Where in code* follows the file's own convention: every kind file lists there the directories of the parts its *Applies to* names, for example `coding-measuring-report.md`. Without it the two fields would disagree. I accept the addition.
- **Remarks 3–4** ("Accepted"): nothing to make.

## What else could disagree with the new *Applies to*

- `elements/common/foundation_check.py` checks that each part a guideline's *Applies to* names exists (`:859`). It exits 0 with `0 errors` on the head.
- `foundations/invariants.md`, `shared-module-import-runs-nothing`, keeps *Part* `relation-model` and its test checks only `relation-model/fingerprint.py`. WAY-391 names the exemplar alone. Neither now says anything false: the guideline's rule "Importing runs nothing" binds `process-audit` through the review of each change, and `stage_pricing.py` meets it, since it defines only constants, classes and functions. See N-2 for a reading the rule's text invites.
- The kind index row in `guidelines/coding.md:21` and the sentence at `:100` are unchanged and still agree with the new line.
- The tests of `product-guidelines` and `agent-instructions` pass on the head (checks below).

## New Minor notes

- **N-1** (within the task; it falls among the Minor findings the human let through). `guidelines/coding-shared-module.md`, *Files of this kind*: the table still lists only `relation-model/fingerprint.py`.
  - The author's report says a row would need a status and "`copy` would be a new designation". It would not be. `copy` and `do not copy` are the statuses every other kind file uses for files that are not the exemplar: `coding-check.md:16-23`, `coding-command-runner.md:16`, `coding-generator.md:17`, `coding-measuring-report.md:17-22`.
  - The remark asked for the *Applies to* line, which is made, so the correction is complete. A row `process-audit/stage_pricing.py | copy | —` would follow the convention of the other kinds. It is left for the guidelines' own upkeep.
- **N-2** (within the task, Minor). The rule "Importing runs nothing" names the invariant `shared-module-import-runs-nothing` and says "The invariant's test starts a new interpreter that imports the module". Now that the file applies to `process-audit` too, a reader may take "the module" to include `stage_pricing.py`, while the invariant's sentence and *Part* cover `relation-model/fingerprint.py` only. Nothing fails, and the review of each change carries the rule for the new module. The fact that the test covers the exemplar alone is not written down.

## Declined to judge

none

## Checks run

1. `git diff 026308f..cdfcf48`: read whole.
2. In a worktree of the head: `python -B elements/common/foundation_check.py`, exit 0 (`0 errors`, no `listed:` line).
3. In a worktree of the head: `python -B gate/run_tests.py product-guidelines`, exit 0 (14 tests).
4. In a worktree of the head: `python -B gate/run_tests.py agent-instructions`, exit 0 (37 tests, 2 expected failures, as before).
5. Manual: searched the tracked `.py` and `.md` files for `shared-module`, `Applies to` and `Where in code` (`.runs/` and `docs/` left out). The hits are the kind file, `guidelines/coding.md:21,100`, `foundations/invariants.md:478`, `relation-model/test_fingerprint.py:122` and `elements/common/foundation_check.py`. None disagrees with the new line.
- Not run: the full gate (the orchestrator's alone).

## Reaches beyond the dispatch

- `guidelines/coding-check.md`, `coding-command-runner.md`, `coding-generator.md` and `coding-measuring-report.md`, their tables *Files of this kind*: the status convention for N-1.
- `elements/common/foundation_check.py:32, 859`: how a guideline's *Applies to* is checked.

## Working copies

- `.runs/review-correction/head`, a worktree of `cdfcf48`: removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-correction/`, which held the logs: removed.
- `git worktree list` shows nothing under `.runs/review-correction/`. Nothing remains.

## Unread material

- `guidelines/coding-shared-module.md`: read whole. `guidelines/coding.md`, `guidelines/testing.md` and `product-guidelines/reading.md`: read whole earlier in this cycle's reviews and not read again. `foundations/invariants.md`, entry `shared-module-import-runs-nothing`: read whole earlier in this cycle.
- WAY-391: not read whole; its binding sentence is known only from the author's report and the kind file's *Decision* line. It bears on the exemplar only, which the correction does not change.

## Searches not found or unclear

- I found no rule that makes a row in *Files of this kind* required for each file of a kind (N-1).
- The remark's wording, "finds no row for it", could mean a row of the table rather than the *Applies to* line. The remark's own instruction ("its *Applies to* ..., beside `relation-model`") settles that it means the line, and I judged the correction by that.
