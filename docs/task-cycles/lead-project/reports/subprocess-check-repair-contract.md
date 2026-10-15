# Final subprocess invariant contract

Current source: foundations/invariants.md at 114c68960670e31a878ff00fbdf9ed5c00689089.

## project-plan-state-subprocesses/1

Every subprocess the plan-state reader starts runs Git.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
- **Rests on:** none
- **Derives from:** WAY-153@9874911d
- **Part:** project-level
- **Correction:** none

Public invocation: `python -B project-level/plan_state.py PLAN PRODUCT_REPOSITORY`.
The observable subject is the reader's own starts, not programs that Git starts.
The current evidence contract requires archived provenance to identify the supplied plan's task.
Use the public record/task/plan templates for a valid successful observation. Positive control
must establish successful evidence reading, the expected composed transitions and the retained
PR pointer from that record, not just exit0
or that a ref moved. A failed-fetch observation remains separately required. Keep the observer's
nonempty event check and actual program verification. Derive the repair from these sources;
no production reasoning, reviewer mutation or expected private implementation is provided.
