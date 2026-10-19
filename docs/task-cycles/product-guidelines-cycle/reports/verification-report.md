# Orchestrator verification

Actor: /root. Completed change: `fc0c946351154a8ee5747160dad55a857522fe86`. Windows, local Python.

These are the required available checks under agent-instructions/README.md. The full gate does not exist and is not claimed as passed.

| Command | Exit | Result | Complete output and execution metadata |
|---|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | Ran 41 tests in 0.737s; OK | [Output](orchestrator-tests-task-cycle.txt), [metadata](orchestrator-tests-task-cycle.json) |
| `python -B gate/run_tests.py project-level` | 0 | Ran 250 tests in 145.433s; OK | [Output](orchestrator-tests-project-level.txt), [metadata](orchestrator-tests-project-level.json) |
| `python -B gate/run_tests.py product-guidelines` | 0 | Ran 140 tests in 404.867s; OK | [Output](orchestrator-tests-product-guidelines.txt), [metadata](orchestrator-tests-product-guidelines.json) |
| `python -B gate/run_tests.py elements/decisions` | 0 | Ran 169 tests in 46.363s; OK | [Output](orchestrator-tests-elements-decisions.txt), [metadata](orchestrator-tests-elements-decisions.json) |
| `python -B gate/run_tests.py elements/part-map` | 0 | Ran 162 tests in 97.713s; OK | [Output](orchestrator-tests-elements-part-map.txt), [metadata](orchestrator-tests-elements-part-map.json) |
| `python -B gate/run_tests.py gate` | 0 | Ran 98 tests in 32.732s; OK | [Output](orchestrator-tests-gate.txt), [metadata](orchestrator-tests-gate.json) |
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 error(s), 16 warning(s), 5 unchecked | [Output](orchestrator-guard-decisions.txt), [metadata](orchestrator-guard-decisions.json) |
| `python -B elements/part-map/format_guard.py --base none` | 0 | 0 error(s), 0 warning(s), 7 unchecked | [Output](orchestrator-guard-part-map.txt), [metadata](orchestrator-guard-part-map.json) |

Total executed test cases: 860.

## Warnings and unchecked work

### guard-decisions

```text
foundations\decisions.md:71: warning: WAY-03: check-by date 2026-10-02 has passed without a review record
foundations\decisions.md:635: warning: WAY-21: check-by date 2026-10-02 has passed without a review record
foundations\decisions.md:1476: warning: WAY-52: check-by date 2026-10-02 has passed without a review record
foundations\decisions.md:1558: warning: WAY-55: check-by date 2026-10-02 has passed without a review record
foundations\decisions.md:1972: warning: WAY-69: check-by date 2026-10-02 has passed without a review record
foundations\decisions.md:7249: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7291: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7329: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7368: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7401: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7427: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7458: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7493: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7521: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7550: warning: *Approved by* is the placeholder `merge of <request link>`
foundations\decisions.md:7584: warning: *Approved by* is the placeholder `merge of <request link>`
unchecked: the lines the log holds on the main branch, and the versions it gains per number — --base none: there is no commit the branch left the main branch from
unchecked: a change to the template without a new version in the log — --base none: there is no commit the branch left the main branch from
unchecked: `TODO` in the log — --merge-onto none: there is no commit to merge onto
unchecked: the copies of a version both logs hold — --merge-onto none: there is no commit to merge onto
unchecked: the fingerprints relations carry — --merge-onto none: there is no commit to merge onto
0 error(s), 16 warning(s), 5 unchecked
```

### guard-part-map

```text
unchecked: the list of parts of `wording-reaches-dependants` — its test leaves no coverage file
unchecked: the list of parts of `skills-reach-the-way-sessions` — its test leaves no coverage file
unchecked: the change path of every promise level in use — the levels sit at the declarations, and no command of the product reports them
unchecked: the dependencies between parts, and new or stale violations — no command of the product reports the dependency graph
unchecked: the list of known violations — --base none: there is no commit the branch left the main branch from
unchecked: the identifiers of the map — --base none: there is no commit the branch left the main branch from
unchecked: the lowering of a part's computed criticality — --base none: there is no commit the branch left the main branch from
0 error(s), 0 warning(s), 7 unchecked
```

The eleven request-link placeholders will be replaced only after a real PR exists. The five pre-existing overdue-review warnings remain outside this change. No unchecked guard result is relabelled as passed.

The author's unchanged invariant, glossary and environment guards remain current as recorded in foundation-report.md, including their eleven unchecked results. No runtime UI was changed, so a running-product screenshot is not applicable; the new instructions' screenshot behavior was checked by the recorded manual scenarios.
