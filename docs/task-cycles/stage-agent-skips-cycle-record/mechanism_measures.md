# Measures of the cycle run

- Calls in all: 126
- Calls of the orchestrator: 52
- Calls of subagents: 74
- Mean context per call: 102859
- Mean context per call of the orchestrator: 127730
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 44210
- Context of the orchestrator's middle call: 123652
- Context of the orchestrator's last call: 197907
- Cache written, 5 minutes: 123295
- Cache written, 1 hour: 277280
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator eabeb72f-c908-40af-a5a1-d3981236c66a | Claude Code | 52 | 44210 | 123652 | 197907 | 0 | 177354 | 0 | 0 | 24560 | 14 | 0 | 0 |
| Make the change as the one author (the-way-author) | Claude Code | 35 | 23838 | 91881 | 110959 | 0 | 99926 | 0 | 0 | 46849 | 23 | 0 | 0 |
| Review the whole change (the-way-stage) | Claude Code | 39 | 23796 | 84685 | 134280 | 123295 | 0 | 0 | 0 | 38139 | 7 | 40761 | 2 |
