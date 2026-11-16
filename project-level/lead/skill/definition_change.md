# Change of the definition and its readiness approval

Read from step 5 of `SKILL.md`, and from step 0 when a pending readiness approval of the definition or plan recheck
is found.

- Before a definition edit, record in the conversation that its readiness approval and subsequent plan recheck
  are pending; make that block visible in every affected pending task conversation. A newly
  created conversation checks the same definition and pending change. These files, the definition
  Status/approval record and plan log retain resumption evidence; introduce no second state store.
  You may edit definition text only when its full text is already before you and no reading of
  other definition sections or foundation is needed. Otherwise delegate the edit. In both cases
  a subagent always performs `define-project` step 7 in delegated mode.
- You dispatch the independent critique of the readiness approval and pass observations back
  through the files; the approval agent performs the whole foundation collision search, checks and corrections required
  by that step. Present its human approval material yourself and record the human's approval
  before the approval agent writes approval/fingerprint/record. Never approve on the human's behalf
  or replace the delegated readiness approval with your own check. Missing child/critic capability blocks it.
- After the readiness approval succeeds, dispatch a fresh `plan-project` agent from its step 0 to recheck the plan
  against the newly approved definition, with serialized shared-plan ownership and logged
  corrections. Keep readiness writes blocked until that recheck and its required checks/critique/
  human decisions finish. Record completion and the new source identities in the conversations
  and plan's change log before fresh affected refiners resume. A check passing the old fingerprint
  or approval alone does not complete the definition change.
