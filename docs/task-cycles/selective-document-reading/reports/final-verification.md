# Final required verification

Source commit: `0c266f3da8cb92204d7788c4bce9065bc2e8b92e`. Ending commit: `0c266f3da8cb92204d7788c4bce9065bc2e8b92e`. HEAD remained stable: True.

| Command | Exit | Tests | Result | Full output | Verdict record |
|---|---|---|---|---|---|
| `python -B gate/run_tests.py elements/decisions --record .runs/task-cycles/selective-document-reading/reports/final-elements-decisions.jsonl` | 0 | 169 | pass | [final-elements-decisions.txt](final-elements-decisions.txt) | [final-elements-decisions.jsonl](final-elements-decisions.jsonl) |
| `python -B gate/run_tests.py elements/part-map --record .runs/task-cycles/selective-document-reading/reports/final-elements-part-map.jsonl` | 0 | 162 | pass | [final-elements-part-map.txt](final-elements-part-map.txt) | [final-elements-part-map.jsonl](final-elements-part-map.jsonl) |
| `python -B gate/run_tests.py elements/invariants --record .runs/task-cycles/selective-document-reading/reports/final-elements-invariants.jsonl` | 0 | 233 | pass | [final-elements-invariants.txt](final-elements-invariants.txt) | [final-elements-invariants.jsonl](final-elements-invariants.jsonl) |
| `python -B gate/run_tests.py elements/glossary --record .runs/task-cycles/selective-document-reading/reports/final-elements-glossary.jsonl` | 0 | 204 | pass | [final-elements-glossary.txt](final-elements-glossary.txt) | [final-elements-glossary.jsonl](final-elements-glossary.jsonl) |
| `python -B gate/run_tests.py elements/environment-facts --record .runs/task-cycles/selective-document-reading/reports/final-elements-environment-facts.jsonl` | 0 | 165 | pass | [final-elements-environment-facts.txt](final-elements-environment-facts.txt) | [final-elements-environment-facts.jsonl](final-elements-environment-facts.jsonl) |
| `python -B gate/run_tests.py elements/common --record .runs/task-cycles/selective-document-reading/reports/final-elements-common.jsonl` | 1 | 0 | unchecked: no tests | [final-elements-common.txt](final-elements-common.txt) | [final-elements-common.jsonl](final-elements-common.jsonl) |
| `python -B gate/run_tests.py project-level --record .runs/task-cycles/selective-document-reading/reports/final-project-level.jsonl` | 0 | 193 | pass | [final-project-level.txt](final-project-level.txt) | [final-project-level.jsonl](final-project-level.jsonl) |
| `python -B gate/run_tests.py task-cycle --record .runs/task-cycles/selective-document-reading/reports/final-task-cycle.jsonl` | 0 | 41 | pass | [final-task-cycle.txt](final-task-cycle.txt) | [final-task-cycle.jsonl](final-task-cycle.jsonl) |
| `python -B gate/run_tests.py gate --record .runs/task-cycles/selective-document-reading/reports/final-gate.jsonl` | 0 | 98 | pass | [final-gate.txt](final-gate.txt) | [final-gate.jsonl](final-gate.jsonl) |

Total executed tests: 1265. Common has no tests and is unchecked, not passed. This is the required available changed-part and critical-flow test set, not the unimplemented full gate. Guards and source walkthrough evidence are recorded separately.
