# Delegated definition change and gate

The variant of the skill `define-project`, whose `SKILL.md` lies beside this file, for a turn that
`lead-project` dispatches; "this same workflow" below is the steps that `SKILL.md` gives.

When `lead-project` dispatches a definition edit or step 7 through a refinement conversation
path, read that file and `project-level/lead/conversation_template.md` first, verify its sources
and process pin, and use this same workflow with file-mediated routing (WAY-156). Edit only the
definition and your conversation turn; write no task body, shared plan or product foundation.
Every question or presentation this workflow or a borrowed skill addresses to the human returns
through the conversation, with complete material and the ways/costs/recommendation required by
"How a skill asks". End the turn for the project orchestrator to obtain and record the answer;
never speak to the human directly, approve for them or start a child agent.

A subagent always performs step 7, including the whole-foundation collision search and all checks.
At 7.3 request the independent critique through the conversation with full proposal and source
paths; the project orchestrator dispatches it and returns observations through files. Verify the
observations and correct through the existing element skills in projected mode, returning conflicts
and additional child-work requests instead of launching children. Missing independent critique
blocks the readiness gate. Present the approval material through the project orchestrator and wait
for its recorded human approval before writing the fingerprint, gate record and approved Status; a
provisional agent ruling is not approval.

Keep the pending readiness gate and next actor visible in the conversation and the definition's
actual Status. On completion return its checks, new source identity and next action through the
file: a fresh plan-project subagent starts at step 0 against this newly approved definition. No task
receives `ready for cycle` while that readiness gate or the subsequent plan recheck remains pending;
neither this agent nor the project orchestrator starts task implementation.
