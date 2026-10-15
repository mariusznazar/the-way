# Independent check contract

Allowed check path: `project-level/test_plan_state_subprocesses_invariant.py`.

```markdown
## project-plan-state-subprocesses/1

Every subprocess the plan-state reader starts runs Git.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
- **Rests on:** none
- **Derives from:** WAY-153@33b10f25
- **Part:** project-level
- **Correction:** none
```

The observable subject is the program started by each subprocess the plan-state reader itself starts. This sentence does not assert a restriction on programs that Git itself starts. The reader's public invocation is `python -B project-level/plan_state.py PLAN PRODUCT_REPOSITORY`.

The receiving check author is distinct from the sentence and covered-code authors. No existing sentence or check is retired. The shared Method produces per-invariant verdicts in one record; absence of a verdict for this identifier is not pass.
