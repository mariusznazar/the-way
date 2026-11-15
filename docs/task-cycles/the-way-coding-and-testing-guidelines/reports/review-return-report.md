PASS 3cf54a5db945d9f6a116fb4b6784e594be85a8d2

# Review of the return step's commit (`f0482d0..3cf54a5`)

Method: `task-cycle/review/SKILL.md`, variant "the return step's range". `git rev-parse HEAD` in the worktree is `3cf54a5db945d9f6a116fb4b6784e594be85a8d2`, the head given. `git log f0482d0..3cf54a5` holds one commit. `git diff --stat`: `agent-instructions/test_size_invariant.py` +1, `foundations/decisions.md` +5 -4. The range touches no boundary file and holds no operation that cannot be undone.

## What the range does

1. `foundations/decisions.md`, WAY-385 *Verification* (from line 9898): after `invariants: function-and-file-size.` it adds `tests: that a function is counted with the functions nested in it and that a method is a function.` and changes the lead-in to "For what the invariant and the test leave". It removes the example "the test counts a function with no regard to the functions nested in it" from *violates*.
2. `agent-instructions/test_size_invariant.py:58`: one comment line `decision: WAY-385 "A function of a script of the-way has at most 80 lines, counted with the functions nested in it"` in `Counting.test_a_function_counts_the_functions_nested_in_it_and_a_method_is_a_function`.

## Findings

### Critical

none

### Important

none

### Minor

1. **Pairs of examples in WAY-380 and WAY-388 to WAY-391 repeat what an invariant holds** (`foundations/decisions.md:9729` ff., and the entries of WAY-388, 389, 390 and 391). The template (`elements/decisions/template.md:245-248`, "Verification") says a pair stands "for an agent comparing a change with the part of the sentences that no invariant and no test checks". Examples that restate a held part:
   - WAY-380 *complies* "the test of the invariant runs Ruff with the flag that ignores comments turning rules off" and *violates* "a comment that turns a blocking rule off stays in a file". Both are what `ruff-blocking-rules` checks.
   - WAY-388 *violates* "a generator writes a file in a run with no `--write`", held by `generator-writes-only-with-write`.
   - WAY-389 *violates* "a script of the kind removes or rewrites something in a run without `--apply`", held by `repository-changer-acts-only-when-told`.
   - WAY-390 *violates* "ends with the exit code 1 for every failure of the command", held by `command-runner-passes-exit-code`.
   - WAY-391 *violates* "a module that other scripts import reads its input or writes output when it is imported", held by `shared-module-import-runs-nothing`.

   Grade Minor (WAY-364): the entries' content agrees with the code and the invariants, and no sentence is read wrongly. The return step saw this only for WAY-380 (its concern 5) and left it, because `task-cycle/skill/return_step.md` names only a part that "a test holds". The template's rule is wider (invariant or test). Effect: the same check is written twice and can drift apart; no wrong reading today. Inside the task (the entries are the change's own).
2. **WAY-395, *Time and randomness*: "as the option `--today` gives it"** names a means that `task-cycle/gate_times.py` does not have (the return step's concern 4). `task-cycle/test_gate_times.py:83` gives the script its time by `mock.patch.object(gate_times, "now_ms", ...)`, a double of the clock, which *Doubles* of the same decision allows. The *complies* example "a test gets its time from `--today`" fits only the scripts with that option (`process-audit/audit_count.py`). Wording only, no wrong code; agree with the return step to leave it. Minor.

No finding is out of scope.

## Against the task and the foundation

- Task requirement (return step, `return_step.md`): where a decision the change writes carries a pair and a test holds part of its sentence, remove that part from the pair, name the test by `tests:` and leave a pair only for a part no test holds. WAY-385 is the one decision of the change (WAY-379 to WAY-402) with a test of its own sentence that carries a pair: I read the *Verification* of WAY-379, 388 to 392, 393 to 402 and the grep of `decision: WAY-(379|38x|39x|40x)` over tracked `.py` and `.sh` files finds only the new line. The return step did what the method names, and only that.
- The quotation begins at the start of the first binding sentence, holds more than three words, no `"`, and the foundation check accepts it; with the end of the quotation altered, the check reports `agent-instructions/test_size_invariant.py:58: the quotation stands in no binding sentence of WAY-385` (my mutation, reverted).
- The sentence part named by `tests:` is what the test asserts: the test expects `("inner", 3, 2), ("method", 8, 2), ("outer", 1, 5)`: `outer` counts 5 lines with `inner` nested in it, and a method is counted. A mutation of `function_sizes` (`end_lineno - lineno` for `end_lineno - lineno + 1`) makes `Counting` fail (`FAILED (failures=1)`), so the test fails when the behaviour it protects breaks. The test's expected values stand written out in it (WAY-394).
- The decision still holds an invariant (`function-and-file-size`, `foundations/invariants.md:438`) beside `tests:`; the template's *Verification* allows the two together and the log has precedent (the entries at `decisions.md:7128` and `:7691` carry `invariants:` and `tests:`).
- The remaining example, "the configuration of the test lists a function or a file as an exception; the rule covers test files", is the part the invariant (which names `test_*.py` as no script) and the counting test do not check by a configuration list. It stands correctly. The *Rationale* and *Rejected* stay whole, as the template requires for a decision whose sentence a test holds.
- *Rationale* of WAY-385 says "11 functions and 2 files over" at the commit of the review of the foundation. At the head my count (the size test's own functions over `script_files()`) gives 11 functions and 3 files (`foundation_check.py` 1003, `audit_count.py` 3310, `cycle_stages.py` 1183). The sentence is dated to the commit of the review (989 lines then for `foundation_check.py`), so it stays true; no sentence in `foundations/`, `guidelines/`, `README.md` or the scripts gives a count of files as present state (grep "2 files", "11 functions"). The return step's judgement not to edit it stands.
- Changed invariant test: none. The line added to `test_size_invariant.py` is a comment; the invariant `function-and-file-size` and its expected failure are not touched.
- Guidelines: the added line is a comment; no rule of `guidelines/coding.md` that has no invariant is reached. A reserved choice: none. Trust boundary: none.

## Declined to judge

- The whole of the return step's comparison table (WAY-379 to WAY-402, invariants, part map): the range changes none of them; I read the entries of WAY-379, WAY-380, WAY-381 (start), WAY-385 to WAY-402 and the two invariants named above, not the rest. Whether the return step's table of matches is complete is not a behaviour of this commit.
- Files over the size threshold (`audit_count.py`, `cycle_stages.py`, `foundation_check.py`) and the 25 reports of Ruff: set aside by the task (answers 5, 10, 11) and marked by the invariants as violated.
- The flaky `gate/test_run_tests.py` test (concern 3 of the return step): outside the range.
- The answer 20 against WAY-253 (who checks the mutation, concern 1): a question for the human, not a defect of this commit.

## Checks run

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (head, in the task worktree) | 0 | `0 errors` |
| `python -B gate/run_tests.py agent-instructions` (head) | 0 | 37 tests, `OK (expected failures=2)` |
| mutation in a worktree of `3cf54a5`: `node.end_lineno - node.lineno` in `function_sizes`, then `python -B agent-instructions/test_size_invariant.py Counting` | 1 | `FAILED (failures=1)`; the change reverted with `git checkout` |
| mutation in the same worktree: the end of the quotation of the new line changed to "nested in them", then `python -B elements/common/foundation_check.py` | printed `1 error` at `test_size_invariant.py:58`; I read the output through `tail`, so the exit code is the pipe's (0) and not the script's | the check names the line and reports the quotation as standing in no binding sentence; the change reverted with `git checkout` |
| a script over the worktree: the count of functions over 80 lines and of files over 1000 with `function_sizes` and `file_lines` of the test | 0 | 11 functions and 3 files |
| `git diff --stat f0482d0..3cf54a5` and `git log f0482d0..3cf54a5` | 0 | two files, one commit |

Not run: the full gate (the handoff reserves it for the cycle); `ruff` over the ten directories (the head of the range changes one comment line, and the return step's run is in its report; the focused run of `agent-instructions` includes the linter test, which gave exit 0 above).

## Reaches beyond the handoff

- `elements/decisions/template.md` lines 160-290 (the sections "Verification" and its neighbours): to judge the clause `tests:`, the pair and the coexistence with `invariants:` (what the template says of a sentence held by a test).
- `foundations/invariants.md:430-470` (`ruff-blocking-rules`, `function-and-file-size` and the invariants of the kinds): to judge which examples repeat an invariant.
- `foundations/decisions.md` entries WAY-379, 380, 381 (start), 385 to 402 (their *Verification* and binding sentences), and the grep of `Verification:** invariants.*tests:` for the precedent: to look for another pair of examples that a test or an invariant holds in part.
- `task-cycle/skill/return_step.md`: the return step's rule, which the handoff names by path.
- `task-cycle/test_gate_times.py:83` and `task-cycle/gate_times.py` (the clock): to check the return step's concern 4.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md` lines 1-322 (the task's *To do*, *Questions to settle* answers and the start of *Context*), whole through 322; lines 323-552 not read.

## Working copies

One worktree of `3cf54a5`: stood in `.runs\review-return\wt`; removed with `git worktree remove --force` and `git worktree prune` (`git worktree list` holds no `review-return` entry). The directory `.runs/review-return/` (ignored) and the text file I kept in it for my reading were removed too. The reviewed worktree, its index and branch are unchanged (`git status --short` empty).

## Unread material

- `task.md` lines 323-552 (the *Context* from the audit's list 14 on and what follows): not read; the reasons the range stands on are in the lines 1-322 and in the entries.
- `plan.md`, the reports of the stages other than `return-step-report.md`, `return-step-handoff.md` and `foundation_step.md`: not read. `task-cycle/skill/foundation_step.md` was not opened (the handoff names it as the step before; `return_step.md` holds the rule that bears on this range).
- `foundations/decisions.md`: WAY-382 to WAY-384, WAY-386, 387 (to *Verification*), the *Rationale* parts of WAY-379 to WAY-402 other than WAY-380 and WAY-385: not read whole. WAY-344, WAY-363, WAY-253: read by reference only.
- `guidelines/coding.md`, `guidelines/testing.md` and the kind files: not read (the dispatch names none, and this range does not change them).
- The code: `agent-instructions/test_size_invariant.py` read whole; the other tests of the change not read.

## Searches not found or unclear

- A second test or invariant holding a part of a sentence of WAY-379 (the upkeep sentence of *Scope*) by a line `decision:`: not found by grep; the return step reasons that the two tests of `PARTS` enforce it, but neither carries a line `decision:` or `invariant:` of WAY-379. Unclear whether the template wants one; WAY-379 carries a pair that names the same rule ("a part that holds Python code stands outside this *Scope*"). Left as a question, not a finding, since a line is not required where no test is meant to hold the sentence.
- The handoff's mention of "the entries it compared": the return step's table lists its comparisons; I did not find a rule that the return step's table must be kept anywhere in the repository after the cycle.
