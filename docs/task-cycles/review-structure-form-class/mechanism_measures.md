# Measures of the cycle run

- Calls in all: 342
- Calls of the orchestrator: 113
- Calls of subagents: 229
- Mean context per call: 224049
- Mean context per call of the orchestrator: 233829
- Share of the context in calls above 200000 tokens: 81.1%
- Context of the orchestrator's first call: 47227
- Context of the orchestrator's middle call: 244725
- Context of the orchestrator's last call: 342823
- Cache written, 5 minutes: 2048129
- Cache written, 1 hour: 322529
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 1237062
- Calls of subagents with a cache write again: 4

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 5139add8-d3b2-4951-90ae-9c8c845090fb | Claude Code | 113 | 47227 | 244725 | 342823 | 0 | 322529 | 0 | 0 |
| Review of the merge with the target (general-purpose) | Claude Code | 13 | 35799 | 69886 | 89070 | 77191 | 0 | 0 | 0 |
| One author makes the change (general-purpose) | Claude Code | 143 | 35678 | 279310 | 379903 | 1362946 | 0 | 983045 | 3 |
| Review of the whole change (general-purpose) | Claude Code | 60 | 35791 | 186998 | 269034 | 523049 | 0 | 254017 | 1 |
| Review of the gate fix commit (general-purpose) | Claude Code | 5 | 35789 | 48685 | 51275 | 39396 | 0 | 0 | 0 |
| Review of the return step commit (general-purpose) | Claude Code | 8 | 35773 | 48549 | 57426 | 45547 | 0 | 0 | 0 |
