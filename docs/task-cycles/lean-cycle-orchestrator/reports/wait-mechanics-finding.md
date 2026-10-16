# Waiting mechanics finding

Input: foundation commit 18602fd699410b2906f04a4492bcdbdea743759e, WAY-157/1.
No implementation files edited yet. This is a mechanics finding, not a new desired outcome.

## Evidence

Codex live tool contract: `collaboration.wait_agent` waits for mailbox activity, accepts
`timeout_ms` up to 3600000, ends on messages/input, and returns a timeout indication separately.
The active developer instruction limits blocking waits to 60000 ms in this session. Use the
largest duration permitted by both; never list/poll agents or sleep to emulate waiting.

Installed Claude Code: `claude --version` returned `2.1.302 (Claude Code)` on 2026-10-16.
Read-only `rg -a -o` inspection of the installed executable found its instruction:

> Execute autonomously and minimize interruptions. If the only work left is waiting for a background task or monitor you started, end your turn now: you will be notified when it finishes or fires. Do not poll, sleep, or re-read its output while you wait.

The same executable says:

> Deprecated: no longer has any effect (the TaskOutput tool was removed). Read a background task's output file with the Read tool instead.

These are shipped strings, not a live Claude tool invocation; no agent was launched.
The official documentation independently confirms that foreground subagents block the main
conversation until completion and background results arrive as completion notifications. Fork
mode can force background operation, and a resumed subagent runs in the background.
Source read 2026-10-16: [Claude Code subagents, foreground/background](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)
and [resumption](https://code.claude.com/docs/en/sub-agents#resume-subagents).
No public source supplies a configurable timeout for that notification wait.

## Wording issue and recommendation

WAY-157 currently requires one blocking call with a duration. That fits Codex, but in current
Claude Code a resumed author has a notification-based continuation with no such timeout. Retaining
that literal requirement makes the accepted one-author route appear unavailable or encourages
inventing a removed TaskOutput call. The task explicitly leaves tool-specific mechanics to this
cycle and asks to eliminate polls/sleeps; notification-based suspension fulfills that intent.

Recommend revising WAY-157 in a foundation-only commit before dependent instructions. Full
proposed binding paragraph:

> The task-cycle orchestrator waits for an agent's completion through the harness's completion notification or one blocking wait set to the longest duration the available tool and active instructions permit, without repeated status polls or sleeps between checks. It renews a bounded wait only after a genuine timeout or an interruption leaves the agent's work pending, handling any returned question or new input before continuing.

Also add the corresponding complying example for a notification-driven harness; keep its
question, meaning, level 2 verification and no numeric tool limit. No current entry refers to
WAY-157 by fingerprint. The cost of this wording is a named second mechanism; keeping the current
wording would make the task's cross-harness instruction false. This changes no human settlement:
one event-driven waiting period remains, no polling or sleeping is introduced.

Requested orchestrator ruling: permit this foundation clarification, then continue implementation,
or identify a binding reason it requires another route. No human confirmation requested.
