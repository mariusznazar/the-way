# Measures of the cycle run

- Calls in all: 228
- Calls of the orchestrator: 87
- Calls of subagents: 141
- Mean context per call: 153935
- Mean context per call of the orchestrator: 172283
- Share of the context in calls above 200000 tokens: 41.7%
- Context of the orchestrator's first call: 43993
- Context of the orchestrator's middle call: 173782
- Context of the orchestrator's last call: 268283
- Cache written, 5 minutes: 430428
- Cache written, 1 hour: 476413
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 173352
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 791810ec-3a83-4605-9d8f-03eaf0547ebb | Claude Code | 87 | 43993 | 173782 | 268283 | 0 | 248025 | 0 | 0 |
| Author of the change (the-way-author) | Claude Code | 86 | 24117 | 169659 | 238737 | 0 | 228388 | 0 | 0 |
| Fresh review of six unread decisions (the-way-stage) | Claude Code | 9 | 24146 | 40006 | 72819 | 62470 | 0 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 46 | 24082 | 138710 | 204955 | 367958 | 0 | 173352 | 1 |
