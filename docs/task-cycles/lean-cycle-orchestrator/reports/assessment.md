# Independent assessment

Assessed range: `41cfbe55c17981500490ffddd24fc1fe0ec1c6ef..cf5f104fb5fe1dcfb64ece84614efc5f784166cb`.

Assessed files: `foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`. References below are to the latter commit. This is an advisory assessment under WAY-10 and the checkout's critique skill; the author settles remarks and the human accepts the meaning. No tracked files, index or branch were changed.

## Finding requiring correction

### A1 — Limit command-output completeness rules to checks executed as commands

Evidence: `task-cycle/record_template.md:91` still expressly admits a “Command or manual check”, but lines 94–96 require complete stdout/stderr and return a report for repair whenever its command, exit code or output is missing. `task-cycle/skill/SKILL.md:140–141` likewise says unconditionally that a check report missing its command, exit code or full output returns to its agent. These sentences broaden WAY-159's execution-evidence contract to manual checks. WAY-61 explicitly permits a path to material assessed by a person as an invariant method; WAY-83 records that person's verdict, identity, date and assessed commit. Step 10 also retains verification of visible behavior in the running product.

Consequence: a legitimate manual observation has no process exit code or stdout/stderr to repair. Applying the new completeness rule literally either blocks progression forever or encourages invented execution fields. The preceding “Where applicable” in the dispatch paragraph helps, but the template and the unconditional repair sentence do not preserve that qualification.

Required change: qualify both repair sentences and the template's stdout/stderr requirement as applying to command executions. Explicitly allow manual checks to use `not applicable` for exit code/output and instead link their method, actor, observed result and evidence. Keep missing evidence for an executed command a blocking incomplete report. WAY-159 itself can stay as written: its binding text already concerns commands, exit codes and recorded execution.

Suggested replacement for the template paragraph's first three sentences:

> Record the baseline separately from post-change runs. A check's result is one line. For an executed command, keep its complete sanitized stdout and stderr in `reports/`; a missing command, exit code or output returns to the reporting agent for repair. For a manual check, record its method, actor, observed result and evidence, with `not applicable` in the command-execution fields. Focused checks are not rerun merely to advance the cycle.

Suggested replacement for the skill's repair sentence:

> A report of an executed check command missing its command, exit code or full output returns to its agent for repair (WAY-159); a manual check instead records its method, actor, observed result and evidence.

Cost of leaving this unchanged: contradictory instructions recur whenever a cycle records a manual check. Cost of correction: two local wording changes, preserving the stronger command-evidence requirement without creating another workflow.

## Checks finding no additional concern

- **Purpose and moment of use:** the change helps the coordinating agent at stage dispatch, return, review and final verification. It explicitly assigns complete method/source reads to the agent performing the stage, retains independent full-diff review, and leaves authoritative-source reading mandatory for questions, findings and acceptance of foundation meaning. This does not authorize resolving a disputed result from a short return alone.
- **Review ownership:** WAY-158, steps 9–10 and step 12 agree that the reviewer reads the full committed range and the orchestrator uses range, changed-file/line-count information and verdict for routine progression. The loss of a second routine correctness read is explicitly acknowledged in WAY-158's rationale. Existing requirements for independent review and whole-change review remain in place.
- **Verification ownership:** WAY-159 removes a duplicate focused run, not the executor's run. WAY-160 keeps the completed change's full required gate with the orchestrator. Step 12 requires a new full gate when the final change differs; corrections and disputed/stale evidence still require affected verification. Gate summaries must include warnings and every unchecked result, consistent with WAY-63's zero exit code being insufficient to establish that all entries passed.
- **Waiting:** WAY-157 accommodates both native notifications and bounded blocking waits, respects smaller active-instruction limits and distinguishes timeout from completion. The skill requires current tool contracts instead of assuming a remembered timeout. I found no instruction here to exceed an active wait limit or to treat an interrupted wait as a completed agent.
- **Assessment independence:** the changed instructions preserve step 11's filtered assessor inputs and do not replace foundation assessment with code review. They preserve required source reads by their assigned owners.
- **Record alignment:** the template exposes review range, verdict, execution actor and retained full-output paths. Its gate-output requirements match step 10, subject to A1's command/manual distinction.
- **Static whitespace:** `git diff --check` on the three assessed paths returned exit code 0. This is not a format-guard run or a full-gate pass.

## History, frequency and cost

The existing file-based transfer rule entered as WAY-148 in `dba4cf81769446484d68b6260424260f7f1da85e` on 2026-10-14, and its cycle instructions entered in `19c9cfee3fce8284712e2e1e2273fd1f5ce6a48f` on the same date. The assessed commit makes routine duplicate reads/runs explicit violations and splits the ownership obligations into WAY-157–160. Thus this strengthens a recently introduced rule rather than introducing file-based coordination for the first time.

Agent-behavior frequency is **not measured**. Session transcripts, run logs and operational cycle records were excluded by the assessment boundary, so zero such records were examined; no dated behavioral examples or recurrence after the prior rule can be established. The assessment therefore establishes instruction consistency and costs, not observed frequency or measured token/time savings. The existence of the prior permissive rule does not itself prove agents applied it or ignored it.

Keeping the former rules would retain more discretion and less record detail, but could still allow routine duplicate reads and runs. The proposal makes ownership explicit and avoids that duplicate work when followed. Its ongoing costs are complete execution-output retention and sanitization, diff statistics, verification of report/range currency, and dependence on the reviewer's reading and the executor's evidence. A bad or incomplete short return still needs investigation; reduced routine context is not proof of evidence completeness. The evidence-reading exceptions are therefore necessary, not optional overhead to cut.

## What can be cut

The unconditional application of command/exit/stdout requirements to manual checks can and should be cut as A1 specifies. No substantive ownership, full-diff-review, gate-retention, stale-evidence or evidence-reading safeguard should be cut on the material checked. The separate waiting-record field is additional bookkeeping, but records the active limit needed to audit WAY-157; I do not recommend removing it without equivalent event evidence.

## Unchecked limits

- No task, spec, plan, operational reports, handoffs or session transcripts were used. Source fidelity to the excluded task and human settlements cannot be established from this package. The request still needs renewed human acceptance of the modified approved meanings.
- Borrowed Superpowers 6.4.1 skill bodies are not among the assessed tracked sources. Their actual internal prompts, completeness requirements and harness behavior were not independently verified; the assessment checks the adapter's declared ownership and retained boundaries.
- This was a focused semantic review of the full assessed diff, full cycle skill and record template, relevant foundation entries and rule history. Some large combined source outputs were truncated; I revisited the decision entries used for the observations, but did not complete an exhaustive whole-log/whole-foundation semantic collision audit. Do not count this report as the author's required WAY-33 searches or exhaustive WAY-150 selection evidence.
- No runtime tests, foundation format guards, fingerprint recomputation or full product gate were executed by this assessor. Operational report completeness, claimed prior checks and actual artifact/range correspondence were not inspected.
- Independence of model choice must be recorded by the orchestrator; this assessor was not given the author's model identity and cannot verify that condition.

Assessment outcome: **one required wording correction (A1); no additional verified substantive conflict in the checked material**. The author's settlement remains required.
