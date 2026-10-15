# R2 affected review and final subprocess-check acceptance

Verdict: **PASS. R2 resolved; project-plan-state-subprocesses/1 accepted on the final check.** No new findings or outstanding correctness concerns in this bounded range. The previously missed owned-record non-Git subprocess is now detected by the actual repaired protected check. A separately derived non-Git start on the operational-error path is also detected. Both tests pass after byte restoration.

## Reviewed boundary and sources

Worktree: C:/Storage/repos/the-way-wt/lead-project; branch task/lead-project. Exact range:

`114c68960670e31a878ff00fbdf9ed5c00689089..f1f878ee5c847f6407bdb55823adca09244022be`

Only changed path: [project-level/test_plan_state_subprocesses_invariant.py](https://github.com/mariusznazar/the-way/blob/4c454b5757a695685af1ecd2d0c9cf74843cad93/project-level/test_plan_state_subprocesses_invariant.py). Actual complete diff inspected: 19 additions, 3 deletions. Read the complete final file, complete subprocess-acceptance-handoff.md and complete subprocess-check-repair.md. The original R2 report, identity-review.md, and its exact mutations/results remain the governing finding and were retained in this review context. Source copies and runner live outside reports under the ignored cycle directory; no Git-held source file or diff is included as a report artifact.

This is only the requested R2 affected rereview and final acceptance under task-cycle step 11, WAY-69 and WAY-149. It is not another independent assessment, whole-branch review or new fix wave. The prior complete foundation selection/readings remain applicable: project-level is unchanged as the subject; both entire foundation files are byte-identical to the prior reviewed boundary. The final sentences, WAY-153 and source/provenance contract are unchanged. No new foundation meaning is inferred from a test repair.

## R2 resolution and independence

At [test_plan_state_subprocesses_invariant.py:106](https://github.com/mariusznazar/the-way/blob/4c454b5757a695685af1ecd2d0c9cf74843cad93/project-level/test_plan_state_subprocesses_invariant.py#L106), the publisher now commits a record carrying original Task source, Task relation, Artifacts and a retained frozen task with its Project relation. It uses the independently authored literal CYCLE_RECORD and TASK inputs. Its original source matches the supplied plan's Document cell; the relative frozen membership resolves to that plan. Record and retained task are both published to the disposable remote before the observation.

The record includes the literal pointer `https://example.invalid/pull/41`. At [test_plan_state_subprocesses_invariant.py:161](https://github.com/mariusznazar/the-way/blob/4c454b5757a695685af1ecd2d0c9cf74843cad93/project-level/test_plan_state_subprocesses_invariant.py#L161), the success test requires exactly the two literal proposal rows, that pointer, the exact archive directory and integration header with the publisher's delivered commit. Thus exit 0 and ref movement alone no longer allow the old unchecked, unowned record to masquerade as complete successful evidence reading. The pointer comes from the owned record in this controlled fixture, with no host lookup or pointer borrowed from another task.

The audit wrapper, nonempty observation assertion, executable assertions, previous exit assertions, actual remote-ref movement and failure-path unchanged-ref assertions are preserved. The error fixture still has its own invariant citation. No expected answer comes from production helpers; the shared inputs are literal test data, not a production-derived oracle. The existing independently dispatched check author repaired the check, not the reader author or this reviewer.

The author's assertion-first RED result establishes that the added positive requirements reject the previous fixture; the final repaired input passes. This review accepts R2 on the actual final diff and independently repeated original break, not on the author's interpretation alone. No new issue was established by the repair.

## Product PASS inspected before mutation

Read the final executor logs and structurally parsed the current exact Method JSONL before introducing either mutation:

- `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`: executor exit 0, **250 tests in 101.408s, OK**. Full log subprocess-check-repair-method.txt.
- The JSONL has **141 invariant-attributed records, all pass**: 27 for project-plan-state-evidence/1 and 2 for project-plan-state-subprocesses/1. The attribution count is distinct from the complete 250-test suite.
- `python -B gate/run_tests.py gate`: executor exit 0, **98 tests in 22.894s, OK**. Full log subprocess-check-repair-gate.txt.

No broad green suite was repeated by this reviewer. Those product runs precede the following acceptance breaks. They are not themselves evidence that a violation is detected.

## Final versions and preservation of prior acceptance

The final subprocess sentence remains: **“Every subprocess the plan-state reader starts runs Git.”** Its binding fingerprint is `a4d1867f`, introduced at return-step foundation commit 4d705b597cb4634f1c58a056558635f63f9cd407. Its incoming WAY-153 reference is `9874911d`, refreshed at 9ae98fe0b8421c5b486785a462648f51f9c50f08; that refresh did not change the subprocess sentence. The final evidence sentence fingerprint remains `d7b8cc0b` at 9ae98fe.

| Final file | Commit authority | SHA-256 |
|---|---|---|
| project-level/test_plan_state_subprocesses_invariant.py | f1f878ee5c847f6407bdb55823adca09244022be | 67906326775091b35e4ab61faf4fff15c806b28c6122792cbce7f6619762f8b0 |
| project-level/plan_state.py | 114c68960670e31a878ff00fbdf9ed5c00689089 | 027a95f1f60c2e185555146015d168f26b39b574a3fe1cee5fe680a39d554970 |
| project-level/test_plan_state_invariant.py | a9e766d99672bf3c7693ebd4a5519e7fb8d30acf | 1bb9a2a2bad076ec4a424278e3ae2958458c17b7b344209726a081791f50b206 |
| foundations/decisions.md | 9ae98fe0b8421c5b486785a462648f51f9c50f08 | af55d319b598ff1a25bfec61806d97fb31315b5c6a6f3df44be6c40cd81c65aa |
| foundations/invariants.md | 9ae98fe0b8421c5b486785a462648f51f9c50f08 | 0c112cd3cd13edd7860dabb4512632bb773e5295dff7f4d150319a94b8ae60a5 |

The reader, evidence check and both complete foundation files match the hashes recorded at the accepted 114c689 boundary. Therefore the earlier successful identity/freshness deliberate breaks and clean restoration in identity-review.md remain current. They were not repeated. Original real-product acceptance also remains unchanged; this one-file check repair does not invalidate its covered reader behavior.

## Reviewer-derived deliberate breaks

The independent reviewer derived these violations from the unchanged final subprocess sentence. Only the copied reader in `.runs/task-cycles/lead-project/subprocess-acceptance-source-breaks/project-level/plan_state.py` was mutated. The copied project-level and relation-model Python files preserve the dependency layout. **Both real protected checks and the real reader remained read-only.** Even the copied protected checks were unmodified.

Each replacement asserts one exact source anchor. Each run restores original reader bytes in a `finally` block. The runner is retained outside reports as `.runs/task-cycles/lead-project/subprocess-acceptance-run.py`; exact command vectors, hashes, exits and restoration status are retained in [subprocess-acceptance-results.json](subprocess-acceptance-results.json). Commands below run from the copied project-level directory with the current Python executable and `-B`.

### A. Repeat the original missed owned-record violation

Immediately before the Git grep in `record_pointers`, insert exactly the same non-Git start used for the original R2 finding:

```python
subprocess.run([sys.executable, "-c", "pass"], check=True)
```

Run the actual final protected success test, with no reviewer subclass or fixture augmentation:

```text
python -B -m unittest -v test_plan_state_subprocesses_invariant.PlanStateSubprocesses.test_successful_evidence_read_starts_only_git
```

**Exit 1; one test in 2.202s; meaningful failure.** All preceding exit/proposal/pointer/integration assertions are reached and pass; `assert_only_git` fails at final check line 153 with:

```text
AssertionError: 'python.exe' not found in ('git', 'git.exe') : Non-Git reader subprocess
```

The observed audit event is `subprocess.Popen`, program is the actual Python interpreter, arguments end in `-c`, `pass`. This is the forbidden program observed inside the reader, not a syntax, import, fixture or setup error. Full log: [subprocess-acceptance-owned-break.txt](subprocess-acceptance-owned-break.txt).

The original missed mutation was retained, not replaced by an easier unconditional process start. This directly closes the previously demonstrated coverage gap.

### B. Operational-error path

In `observe`, inside the first `except (GitError, UnicodeError) as error` handler, insert the same non-Git start before recording the observation error. Leave all original error recording and incomplete-observation behavior intact:

```python
except (GitError, UnicodeError) as error:
    subprocess.run([sys.executable, "-c", "pass"], check=True)
    observation.errors.append(display(error))
    observation.complete = False
```

Run:

```text
python -B -m unittest -v test_plan_state_subprocesses_invariant.PlanStateSubprocesses.test_failed_fetch_read_starts_only_git
```

**Exit 1; one test in 1.600s; meaningful failure.** The preserved exit-2 assertion passes, then the audit assertion rejects the actual `python.exe` start with the same explicit `Non-Git reader subprocess` failure. Full log: [subprocess-acceptance-error-break.txt](subprocess-acceptance-error-break.txt).

This exercises the fixture's actual missing-remote failure, which occurs at remote access before an actual fetch. The name of the test is not evidence that every possible fetch failure was exercised; the accepted observation here is a non-Git fallback on the real exercised error path.

### Restoration and final clean check

After both mutations had been restored, run:

```text
python -B -m unittest -v test_plan_state_subprocesses_invariant
```

**Exit 0; two tests in 3.375s; OK.** Full log: [subprocess-acceptance-restored-clean.txt](subprocess-acceptance-restored-clean.txt).

Byte assertions confirm the restored copied reader equals the real reader; both copied protected tests equal the real files; all five real files in the hash table remain identical to their pre-run bytes. `git status --short` is empty and HEAD remains f1f878ee5c847f6407bdb55823adca09244022be. No discarded setup attempts or false failure runs occurred. No source, index, HEAD, private product, plan or definition was changed by this reviewer.

## Acceptance and limits

**project-plan-state-subprocesses/1: ACCEPTED on final check f1f878e and covered code 114c689.** The current product pass preceded reviewer-derived failures on both the originally missed successful owned-record path and the actual operational-error path. Both restored checks pass. R2 is resolved; its historical failure evidence remains in identity-review.md rather than being overwritten.

**project-plan-state-evidence/1: earlier acceptance remains current**, verified through unchanged sentence/check/code bytes rather than an unnecessary rerun.

The audit observes standard Python process-start events in the reader interpreter, not programs Git itself starts. It does not prove resistance to unaudited native process creation or an impostor binary named Git. Windows was exercised; POSIX execution and exhaustive input/error-path coverage were not. These are the previously disclosed tool/scope limits, not newly claimed coverage. The tests do not prove future agents follow workflow prose; no full foundation gate, human approval or merge authorization is asserted.

No remaining review finding in this range. Root owns subsequent reconciliation and task-cycle stages. This reviewer stopped at the requested report boundary without child dispatch, push or cleanup.
