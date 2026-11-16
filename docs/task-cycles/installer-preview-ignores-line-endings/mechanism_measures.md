# Measures of the cycle run

- Calls in all: 217
- Calls of the orchestrator: 91
- Calls of subagents: 126
- Mean context per call: 146026
- Mean context per call of the orchestrator: 160571
- Share of the context in calls above 200000 tokens: 23.7%
- Context of the orchestrator's first call: 43583
- Context of the orchestrator's middle call: 158105
- Context of the orchestrator's last call: 233350
- Cache written, 5 minutes: 618886
- Cache written, 1 hour: 419408
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 446192
- Calls of subagents with a cache write again: 3

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator dfc0998c-60c0-4d4d-a3fc-58024e166a4c | Claude Code | 91 | 43583 | 158105 | 233350 | 0 | 212061 | 0 | 0 | 9443 | 4 | 2562 | 1 |
| Author of installer line-ending change (the-way-author) | Claude Code | 58 | 23877 | 148359 | 207349 | 0 | 207347 | 0 | 0 | 7987 | 5 | 29562 | 1 |
| Review of whole installer change (the-way-stage) | Claude Code | 68 | 23810 | 132685 | 183043 | 618886 | 0 | 446192 | 3 | 17311 | 4 | 43969 | 2 |
