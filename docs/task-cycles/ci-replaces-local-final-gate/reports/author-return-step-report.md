# Author report — the return step, ci-replaces-local-final-gate

**Status:** done

**Commit:** one, on top of `1b03ef7`, not pushed: "Return step: bring WAY-381 and WAY-162 in line with two CI jobs and the CI final gate" (`foundations/decisions.md`, 5 insertions, 4 deletions). Its hash is `e384214`.

## What was compared, and with what

The range `8f0c1c3..1b03ef7`, read against: WAY-160 and WAY-16 (written by the change, rows 1, 2, 3, 5), WAY-261, WAY-350, WAY-243 (named by the task), and by a search of the whole decision log, the invariants file, the glossary, the environment facts and the part map for "gate", "final gate", "CI", "Windows", "own system" and "the job of CI". The code compared: `.github/workflows/tests.yml`, `process-audit/audit_count.py`, `process-audit/stage_pricing.py`, `task-cycle/skill/SKILL.md` (steps 2, 4, 9.4, 10, 12), `task-cycle/record_template.md`, `task-cycle/skill/request_template.md`, `correction.md`, `blocked_finding.md`, `reserved_return.md`.

## What no longer matched, and its correction

1. **WAY-381** (How is the version of the linter pinned and installed?) said "the job of CI gains one step that installs it there" and, in *Verification*, "the job of CI differs from before by one step". The CI file now has two jobs and each makes the environment. Corrected to "each job of CI gains one step" in both places. The entry's meaning is the same for the-way's earlier file and now for both jobs; it is a correction to what the code shows (marked `the cycle's`: no row carries it; the human sees it in the request).
   - EN: Each job of CI gains one step that installs the pinned linter into the environment the tests look for.
   - PL: Każde zadanie CI dostaje jeden krok, który instaluje przypięty linter w środowisku, którego szukają testy.
2. **WAY-162**, *Verification* (complies): "runs the gate on the code the revert leaves" now reads "has the gate run on the code the revert leaves as WAY-160 gives", because the final gate there may be the CI run. It is an example of a pair, not a binding sentence; no meaning changed. Marked `the cycle's` (no row).
   - EN: After the revert of a fix, the gate runs on the code the revert leaves as WAY-160 gives it, which may be the CI run.
   - PL: Po cofnięciu poprawki bramka biegnie na kodzie, który zostaje po cofnięciu, tak jak daje to WAY-160; może to być przebieg CI.

Checked and left as they stand (they match the code):
- **WAY-160** and **WAY-16**, as the fix left them: each paragraph, *Verification*, *Rationale*, *Rejected*, against step 10/12 of the cycle, the record template, the CI file and `installation/README.md`.
- **WAY-261** (the red first result stays the gate's result), **WAY-350** (times compared only over local runs; the audit's change touches the message only), **WAY-243** (a rerun never makes a gate pass; step 12 reruns nothing on a red CI result), **WAY-367** (rule in `SKILL.md`: the run on the starting state, still local), **WAY-55** (when the gate runs belongs to the cycle).
- The invariant `ci-checking-commands` (review): the second job runs the one command and an install step only. `foundations/part_map.md`: `process-audit/**` covers `stage_pricing.py`, which reads no file and takes in no outside data, so the trust boundary of the part stays `audit_count.py`; `.github/workflows/**` stays in `agent-instructions`. The glossary entry *gate* ("the one command that runs all of a product's tests") is not used against its meaning.

## Settlements written

- Rows 1, 2, 3 → WAY-160; row 5 → WAY-16; row 4 → the comment of `.github/workflows/tests.yml`; row 6 → `process-audit/SKILL.md` with the audit's messages: all written by the foundation step, none missed. Place of each unchanged by this step.
- A choice that binds after the merge (WAY-36): the source of the failing-tests list for step 4 where the earlier final gate was CI (the merged request's *Checks*): already stands in WAY-160 (a sentence marked `the cycle's` by the fix report) and in `SKILL.md` step 4; no second entry. The names of the two checks (`tests`, `tests-windows`) stand in the CI file's comment, the place for a single text (question 3 of the decisions template). Two jobs rather than a matrix: the same comment.
- No source outside the product that a decision of this change rests on lacks an environment fact: WAY-160 and WAY-16 name no behaviour of GitHub beyond the facts WAY-16 already rests on (`github-required-status-checks`, `github-ruleset-bypass`, `foundations-branch-ruleset`). The CI file also rests on three behaviours of GitHub that no fact holds — that a check can be chosen as required only after it has run once, that `windows-latest` has Git Bash, and that a request opened as a draft still starts a `pull_request` run; they are not sentences of a decision and I did not read a source for them in this step, so I wrote no fact from memory. The first CI run on the request shows the second and third.
- No glossary term: no word of the change is used in a meaning WAY-95 gives an entry. No invariant: none set by the task, a decision or the human. No pair of examples to reduce: no test holds a sentence of WAY-160, WAY-16, WAY-381 or WAY-162 (no line `decision:` names them; `grep` found none).
- The environment fact `foundations-branch-ruleset` stays as it is (its source is unchanged until the human adds the required check); the fix report gave the human's reading to repeat.

## Checks (command, exit code)

| Check | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py` after the correction (`0 errors`) | 0 |
| `grep` for `decision: WAY-381`, `decision: WAY-162` in the tracked `.py` files | 1 (no line found: no test holds those sentences, so none is moved to a `tests:` clause) |

No test directory was run: this step changed one file of the foundation and no code. The full gate was not run.

## Unread material

- `reports/review-whole-report.md` and `reports/review-fix-report.md`: not read; the handoff gives them as context only.
- Decisions of the log whose headings were in the index and did not point to the change (about 100): not opened; the search by words above found the entries listed. WAY-381, WAY-162 and WAY-160's neighbours read in the passages cited.
- `elements/glossary/skill/SKILL.md`, `elements/environment-facts/skill/SKILL.md`: not read, since no term and no fact was written.

## Searches not found or unclear

- None for the compared entries. Unclear: whether the three behaviours of GitHub named above should become environment facts; I judged that they stand under no decision's sentence, as written above. A reviewer may judge otherwise.

## Working copies

`.runs/author-return-step/` held the log of the foundation check; it was removed. Nothing remains.
