# Measures of the cycle run

- Calls in all: 282
- Calls of the orchestrator: 72
- Calls of subagents: 210
- Mean context per call: 203584
- Mean context per call of the orchestrator: 189088
- Share of the context in calls above 200000 tokens: 74.8%
- Context of the orchestrator's first call: 47227
- Context of the orchestrator's middle call: 197998
- Context of the orchestrator's last call: 262217
- Cache written, 5 minutes: 1411073
- Cache written, 1 hour: 241923
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 633729
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 5139add8-d3b2-4951-90ae-9c8c845090fb | Claude Code | 72 | 47227 | 197998 | 262217 | 0 | 241923 | 0 | 0 |
| Review of the merge with the target (general-purpose) | Claude Code | 13 | 35799 | 69886 | 89070 | 77191 | 0 | 0 | 0 |
| One author makes the change (general-purpose) | Claude Code | 130 | 35678 | 271416 | 361195 | 994922 | 0 | 633729 | 2 |
| Review of the whole change (general-purpose) | Claude Code | 54 | 35791 | 177472 | 254019 | 254017 | 0 | 0 | 0 |
| Review of the gate fix commit (general-purpose) | Claude Code | 5 | 35789 | 48685 | 51275 | 39396 | 0 | 0 | 0 |
| Review of the return step commit (general-purpose) | Claude Code | 8 | 35773 | 48549 | 57426 | 45547 | 0 | 0 | 0 |
