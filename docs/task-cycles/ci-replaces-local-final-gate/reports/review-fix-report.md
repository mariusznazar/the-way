PASS 1b03ef71fb4fbd634282b6a9123913c06c0387e6

# Review of the fix — ci-replaces-local-final-gate

- Range: `b64608400f4fb55bb5508f71e2c4c2aadbcd6a60..1b03ef71fb4fbd634282b6a9123913c06c0387e6`. Commit `33c98c2` moves code out of `process-audit/audit_count.py` into `process-audit/stage_pricing.py`; commit `1b03ef7` holds the other fixes. `git rev-parse HEAD` gives the head named.
- Bounds: the findings file `reports/review-whole-findings.md` (I-1 to I-4, M-1 to M-3) and the fix diff (`task-cycle/review/fix.md`).
- Counts: no new Critical or Important finding. All four Important findings are fixed, with I-2 fixed in its main part and the rest withdrawn as blocking (see I-2). M-2 remains and is Minor. New Minor notes: 3.

## The findings, one by one

### I-1: fixed

- Step 10 (`task-cycle/skill/SKILL.md:497-503`) now writes a row into the record's *Verification* before the record is copied. The row says that the final gate is the CI run on the request's last head, that the cycle has no local time of it, and that its result stands in *Checks* of the request's description.
- Step 4 (`SKILL.md:166-177`) reads that row in the merged branch's copy. It then takes the list of failing tests from *Checks* of the merged request's description. It finds the request at the address in the copy's *Request URL and status*; the record template gives that field at `record_template.md:207`, and step 12 writes the URL there before the copy is made. A green run gives an empty list. The fallback (run the gate on the base) stays only for a copy with no result and no request to read.
- Step 12 (`SKILL.md:625-632`) and `request_template.md:487-491` now have *Checks* name the tests that failed in a red run, read from the run's log. That closes the gap that "each check by name" gave only the two jobs.
- The sentence of step 4 that contradicted step 12 is gone.
- The defect is gone on the new head: a cycle that follows a cycle whose final gate was CI has a source for its list, and runs no full gate on its base just for lack of one.
- Choice 1 of the fix report, the source of the list: the merged description already holds the result, and step 12 checks it for private paths before publishing. Reading it is a read of the host, not a new run. Where the read fails, the existing fallback applies, so it cannot produce a wrong pass. I accept the choice.

### I-2: fixed in its main part; the rest is withdrawn as blocking

- **Fixed:** the statement "the final gate ran in CI" now stands in the row of step 10, which the committed copy holds (`record_template.md:152-160`, `SKILL.md:497-503`). The audit's pointer "(the record's *Verification* says which)" now leads to a record that answers it.
- **Not fixed: the time of a fallback local run.** The author contests this part with evidence. The fallback run is made only because CI gave no result on the head that removes the copy. Bringing its time into a copy would mean repeating the pair of commits, which pushes a new head and starts the CI run and its wait again. I keep the evidence and withdraw this part as blocking:
  - the measuring still happens: the run goes through `gate_times.py` into the original record's `gate_times.md`;
  - the fallback is rare by its nature;
  - the files now say the limit plainly (`record_template.md:160-162`: "that run's time reaches the original's `gate_times.md` and no copy"; `SKILL.md:501-503`).
- **What the audit then shows for such a cycle:**
  - the copy holds the step-10 row saying the final gate is CI, and `gate_times.md` only where the run of step 2 or step 4 wrote it;
  - where no such file is held, the audit names the three causes and points to *Verification*, which says CI. Strictly, in that case the gate did run locally as the fallback, but the original record and the description say so. This is a note, not a finding.

### I-3: fixed

- WAY-160's first paragraph (`foundations/decisions.md:2818-2820`) now reads: "where CI runs on no request, or the request is left blocked for unfinished code, the orchestrator runs the gate itself on the tree that goes into it, save where that tree is one already run".
- The exception covers the request blocked for a reserved choice. Its tree is the base or the commit that moved the pin, which have already been run, and `reserved_return.md:65-69` says the gate does not run again.
- *Verification* (complies, `:2848-2849`) now adds that the orchestrator ran the gate on the code a blocked request holds.
- The entry and `blocked_finding.md`, step 9.4 and step 10 now say the same.

### I-4: fixed

- Commit `33c98c2` moves the pricing of stage rows out of the file, with the five constants it uses: `ModelPrice`, `Prices`, `StageTokens`, `is_orchestrator_row`, `priced`, `cost_at`, `priced_older`.
- `audit_count.py` goes from 3316 lines (reviewed head) to 3181 lines (fix head, `wc -l`), below its 3310 lines on the base. The new `stage_pricing.py` has 149 lines.
- No change of behaviour. I compared the sorted non-empty lines removed from `audit_count.py` in `33c98c2` with the lines of `stage_pricing.py`. They are identical apart from the module's docstring, its two imports, and the reworded comment on `TEXT_CAP` (see N-2).
- The 235 process-audit tests pass on the fix head.
- The size test, run with its expected-failure mark taken off, lists on the fix head the same functions as on the reviewed head (`read_gate` 108, `read_register` 82, `analyse` 154, `render` 157). It lists `audit_count.py` at 3181 lines and nothing from `stage_pricing.py`.
- The order of the commits is in N-1.

### M-1: fixed

`process-audit/test_audit_count.py:4143-4144`: a comment names the task's row 6 as the source of the two assertions.

### M-2: remains (Minor, blocks nothing)

`foundations/environment_facts.md`, entry `foundations-branch-ruleset`, is unchanged. That is right before the human acts, because the source still says what the fact says. The fix report gives text for the human action, in English and Polish, that names the stale fact and asks for its correction after the second check is set. That text is not in a file of the range, so the orchestrator should carry it into the request's description. The fact itself still needs a correction once the human has acted.

### M-3: fixed

WAY-16 *Rejected* (`decisions.md:2691-2695`) now gives the two ways in general terms, with the-way's junctions on Windows in a parenthesis as the example.

## What the fix itself broke

Nothing at Critical or Important.

- **Trust boundary.** `stage_pricing.py` takes in nothing from outside. It computes over rows that `audit_count.py` has already read and checked. It puts stage and model names into reasons, cut to `TEXT_CAP` exactly as before the move. WAY-48 records a boundary at the files "which take in what the product does not control", so the part map's boundary, `process-audit/audit_count.py`, needs no new line. The import does not change what reaches the rendering.
- **Invariants.**
  - `cross-part-imports`: the module is in the same part. Its test passes.
  - `script-imports`: the module uses the standard library only.
  - `ruff-blocking-rules`: Ruff with `--ignore-noqa` gives the same four reports on the reviewed head and on the fix head (RUF059 once, UP037 three times), with nothing from `stage_pricing.py`.
  - `function-and-file-size`: see I-4.
  - `audit-count-refuses-record-links`: the process-audit tests pass.
- **The new module is imported correctly.** `audit_count.py` imports it as `from stage_pricing import ...`, which rests on the script's own directory being on `sys.path`. That holds for the documented run, `python -B process-audit/audit_count.py` (`process-audit/SKILL.md:121`). The test that builds a copy of the script now copies the module too (`test_audit_count.py:3218-3219`).
- **The new sentence in WAY-160** ("Where CI is the final gate, the cycle's record says so before it is copied, and names the request whose description gives the result, so that the next cycle takes the list of failing tests from there.") goes beyond the task's rows. The fix report marks it `the cycle's`, the mark `foundation_step.md` gives an entry that no row of the task carries. It matches what steps 4, 10 and 12 now do. The request must list it among the entries the human did not see (`request_template.md`, the list at line 504). I make no finding of it.

## New Minor notes

- **N-1** (within the task). WAY-365 says: "The author of a change without a plan makes that move the first commit that changes the code". Its *Verification* (violates) names an author who "moves in the same commit or after it". In this range the move `33c98c2` stands after the reviewed commits, not first. The room is made, and the file ends below its size on the base. Putting the move first would mean rewriting the three commits the review judged, which is the larger harm. The order departs from the letter of WAY-365 only, and nothing on the final tree shows it. Minor.
- **N-2** (within the task). `process-audit/stage_pricing.py:16`: the comment on `TEXT_CAP` changed from "A text copied from the register into the result is cut to this many characters." to "A text copied from a file into a reason is cut to this many characters." `audit_count.py` still uses the constant for text of the register (`display(model[:TEXT_CAP])` at :946, :956, and elsewhere). The new comment is narrower than those uses but still true for them. Minor wording.
- **N-3** (within the task). `stage_pricing.py` is a module that other scripts import, the kind `shared-module` in the index of `guidelines/coding.md`. But `guidelines/coding-shared-module.md` names only `relation-model` under *Applies to*, and no kind table lists the new file. The module meets the kind's rule anyway: it defines only constants, classes and functions, so importing it runs nothing. `product-guidelines/reading.md` asks that such a gap be named. The fix is a line in the guidelines that places the file. Minor.
- **Wording, Minor** (within the task). `record_template.md:158-160`: "The committed copy holds the row of step 10 and the result's row only for the runs before its own head" can be read as limiting both rows. `SKILL.md:629-632` says it unambiguously ("holds the row that step 10 wrote ..., and the result's row only for the runs before its own head").

## Declined to judge

- How an orchestrator reads a merged request's *Checks* on a host other than GitHub. Step 4 says only "through the host's tool". The task names only GitHub, and the fallback covers a host that cannot be read.

## Checks run

1. `git diff`, `git log`, `git show 33c98c2` on the range: read whole.
2. The lines of `audit_count.py` removed in `33c98c2`, sorted with empty lines dropped, compared with the lines of `stage_pricing.py`: equal, save the docstring, the two imports and the `TEXT_CAP` comment.
3. `ruff.exe check --config ruff.toml --no-cache --ignore-noqa --output-format concise process-audit/audit_count.py process-audit/stage_pricing.py`, using ``.runs/quality-venv` of the main checkout/Scripts/ruff.exe`, on the fix head: exit 1, with 4 reports. The same on `audit_count.py` in a worktree of the reviewed head: exit 1, with the same 4 reports.
4. In worktrees of the reviewed head and of the fix head, with the expected-failure mark taken off and then restored: `python -B -m unittest agent-instructions.test_size_invariant.Size`, exit 1 on both. The fix head lists `audit_count.py` at 3181 lines and nothing new.
5. In a worktree of the fix head: `python -B gate/run_tests.py process-audit`, exit 0 (235 tests).
6. In a worktree of the fix head: `python -B gate/run_tests.py task-cycle`, exit 0 (534 tests, 1 skipped).
7. In a worktree of the fix head: `python -B -m unittest elements/part-map/test_cross_part_imports.py`, exit 0 (40 tests).
8. In a worktree of the fix head: `python -B elements/common/foundation_check.py`, exit 0 (`0 errors`, no `listed:` line).
- Not run: the full gate (the orchestrator's alone, WAY-160) and the Windows CI job (I cannot run GitHub; still unchecked, as in the review of the whole change).

## Reaches beyond the dispatch

- `foundations/decisions.md`, WAY-48: its binding sentences, to judge whether `stage_pricing.py` enters the trust boundary.
- `foundations/invariants.md`: `script-imports`, `cross-part-imports` and `shared-module-import-runs-nothing`, read whole, for the new module.
- `guidelines/coding-shared-module.md`, read whole: the kind of the new module.
- `task-cycle/skill/foundation_step.md:30-45` and `request_template.md:297-301, 504-505`: how an entry marked `the cycle's` reaches the request.
- `agent-instructions/test_linter_invariant.py:49-79`: how the linter test runs Ruff.

## Working copies

- `.runs/review-fix/base` (a worktree of the reviewed head `b646084`) and `.runs/review-fix/head` (a worktree of `1b03ef7`): removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-fix/`, which held the logs, the Ruff outputs and the sorted line lists: removed.
- `git worktree list` shows nothing under `.runs/review-fix/`. Nothing remains.

## Unread material

- The fix review reads what `fix.md` names: the findings file, the fix report and the fix diff, all read whole. The decisions selected in the review of the whole change were not re-read; of those the fix touches, WAY-160 and WAY-16 were read in the new text of the diff, and WAY-365 was read whole before.
- `task-cycle/skill/SKILL.md`, `record_template.md` and `request_template.md`: read in the diff and the passages around it, not whole.
- `process-audit/stage_pricing.py`: lines 1 to 60 read, and the rest through the line comparison and searches (`TEXT_CAP`, f-strings), not line by line.
- `reports/author-fix-move.py`, the cutting script: not read, since the move was checked against its result.

## Searches not found or unclear

- I found no rule saying whether a module that a script of `process-audit` imports needs a row among the kinds (N-3).
- That the merged request's *Checks* can be read through `gh` at the time of a later cycle is untested here, because I cannot run GitHub; step 4's fallback covers a failure.
