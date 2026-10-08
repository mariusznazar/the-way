You are the final whole-branch code reviewer of one the-way task cycle (Superpowers 6.4.1
`subagent-driven-development` final review, using `requesting-code-review`). Read and follow the template
C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/requesting-code-review/code-reviewer.md
with these values:

- DESCRIPTION: Adds a "light cycle" to the-way's `implement-task` skill — one executor makes a small task
  that leaves the foundation unchanged straight from the task, the same checks run on the finished change,
  one review covers the whole, and a change that outgrows the rule is discarded and restarted on the full
  cycle — and edits decisions WAY-13/1 and WAY-125/1 in place (no `main` branch yet) so the foundation
  allows it, renewing the WAY-13 fingerprint carried by WAY-125 and invariant `foundation-change-path/1`.
- PLAN_OR_REQUIREMENTS: the requirements are the frozen task
  docs/task-cycles/light-path-small-change/task_frozen.md (Polish;
  points 1–6 and the acceptance criterion) and the spec
  docs/task-cycles/light-path-small-change/spec.md; the plan is
  .../plan.md in the same directory.
- BASE_SHA: c64a6071384fb57cdb9d7e9db4560ddc43e3b355  HEAD_SHA: c64d49a
- The whole diff with commit list and stat is in one file:
  docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) review-c64a607..c64d49a.diff
- Repository (read-only for you): C:/Storage/repos/the-way-light-path. Binding rules for the-way's own
  changes: `agent-instructions/README.md`; the decisions template `elements/decisions/template.md`;
  `elements/common/rules.md`; the foundation in `foundations/`.

Also triage the deferred minors and rulings in the ledger
docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) progress.md: say which, if any, must be fixed
before merge.

Look in particular at: (1) whether the skill text, the record template and WAY-13/WAY-125 say the same
thing (the four "simple and obvious" conditions, test-first only for behaviour changes, the switch and
discard); (2) whether a task that fails the light-cycle rule goes through the full cycle exactly as before
(the acceptance criterion); (3) whether any other foundation entry, element skill or project-level file now
contradicts the light cycle; (4) fingerprints: WAY-13's binding part must hash to the `WAY-13@` value WAY-125
and `foundation-change-path/1` carry (`python -B relation-model/fingerprint.py < file` on a UTF-8 file holding
the binding paragraph's bytes; never pipe through a PowerShell console).

No invariant check (test) is written or changed in this branch; say so if you find otherwise.

Mariusz delegated intermediate choices to the orchestrator; report to the orchestrator only. Write nothing
except your full review to
docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) final-review.md, then return the verdict and the
findings by severity in under 25 lines.
