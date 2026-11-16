# Measures of the cycle run

- Calls in all: 171
- Calls of the orchestrator: 57
- Calls of subagents: 114
- Mean context per call: 129371
- Mean context per call of the orchestrator: 129074
- Share of the context in calls above 200000 tokens: 0.9%
- Context of the orchestrator's first call: 43583
- Context of the orchestrator's middle call: 134801
- Context of the orchestrator's last call: 186686
- Cache written, 5 minutes: 446828
- Cache written, 1 hour: 366112
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 280721
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator dfc0998c-60c0-4d4d-a3fc-58024e166a4c | Claude Code | 57 | 43583 | 134801 | 186686 | 0 | 165655 | 0 | 0 | 9443 | 4 | 2562 | 1 |
| Author of installer line-ending change (the-way-author) | Claude Code | 52 | 23877 | 144568 | 200459 | 0 | 200457 | 0 | 0 | 7987 | 5 | 29562 | 1 |
| Review of whole installer change (the-way-stage) | Claude Code | 62 | 23810 | 129011 | 176456 | 446828 | 0 | 280721 | 2 | 17311 | 4 | 43969 | 2 |
