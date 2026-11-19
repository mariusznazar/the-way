# Measures of the cycle run

- Calls in all: 284
- Calls of the orchestrator: 87
- Calls of subagents: 197
- Mean context per call: 197005
- Mean context per call of the orchestrator: 171493
- Share of the context in calls above 200000 tokens: 65.9%
- Context of the orchestrator's first call: 44479
- Context of the orchestrator's middle call: 170164
- Context of the orchestrator's last call: 257794
- Cache written, 5 minutes: 868986
- Cache written, 1 hour: 505484
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 549486
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 6df616db-85eb-4ad5-a81a-6a795abd1993 | Claude Code | 87 | 44479 | 170164 | 257794 | 0 | 236294 | 0 | 0 | 4367 | 11 | 3713 | 1 |
| Author makes the whole change (the-way-author) | Claude Code | 118 | 24108 | 206594 | 280417 | 0 | 269190 | 0 | 0 | 81759 | 56 | 51462 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 79 | 23981 | 214112 | 319502 | 868986 | 0 | 549486 | 2 | 87479 | 21 | 81739 | 3 |
