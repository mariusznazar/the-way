# Waiting mechanics ruling

Apply the proposed WAY-157 binding paragraph in wait-mechanics-finding.md in a foundation-only commit before instructions, then continue the already assigned implementation stage. This is the tool-specific implementation question expressly carried into this cycle, not a new outcome or approval by the human.

Evidence read: full finding and whole existing WAY-157; orchestrator independently read official Claude Code subagent documentation on 2026-10-16, foreground/background section (lines 808?818), which says foreground calls block and background results are delivered in a later-turn completion notification. The live Codex contract is available to this session. No need to require a removed tool or name an unverified numeric limit.

The two permitted implementations are native completion notification or one blocking call at the effective maximum. Both avoid polling/sleeps. Keeping literal blocking-call-only wording would falsely exclude current Claude background execution; accepting the clarification adds one explicit mechanism and preserves the accepted waiting behavior. Renewal remains only after actual expiry or interruption with work pending.

No new spec needed: tool mechanics, explicitly carried by task. No new empirical foundation fact needed if policy remains capability-relative. Put verified evidence and limits in implementation report; keep product instructions generic enough to use current tool schema. Record the revised foundation commit, focused validation and fingerprint propagation before implementation commit. Do not rerun unchanged suites solely for this prose clarification; run applicable guard/checks, and implementation verification follows.
