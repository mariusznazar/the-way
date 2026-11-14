# Measures of the cycle run

- Calls in all: 191
- Calls of the orchestrator: 59
- Calls of subagents: 132
- Mean context per call: 145597
- Mean context per call of the orchestrator: 137610
- Share of the context in calls above 200000 tokens: 28.0%
- Context of the orchestrator's first call: 43993
- Context of the orchestrator's middle call: 140526
- Context of the orchestrator's last call: 212290
- Cache written, 5 minutes: 367958
- Cache written, 1 hour: 420420
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 173352
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 791810ec-3a83-4605-9d8f-03eaf0547ebb | Claude Code | 59 | 43993 | 140526 | 212290 | 0 | 192032 | 0 | 0 |
| Author of the change (the-way-author) | Claude Code | 86 | 24117 | 169659 | 238737 | 0 | 228388 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 46 | 24082 | 138710 | 204955 | 367958 | 0 | 173352 | 1 |
