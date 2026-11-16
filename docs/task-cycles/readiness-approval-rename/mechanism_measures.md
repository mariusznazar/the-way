# Measures of the cycle run

- Calls in all: 368
- Calls of the orchestrator: 67
- Calls of subagents: 301
- Mean context per call: 199155
- Mean context per call of the orchestrator: 147535
- Share of the context in calls above 200000 tokens: 69.2%
- Context of the orchestrator's first call: 43644
- Context of the orchestrator's middle call: 152371
- Context of the orchestrator's last call: 228475
- Cache written, 5 minutes: 641274
- Cache written, 1 hour: 533173
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 269472
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator d7bf39e7-fa87-4d58-910a-68df82a8e98e | Claude Code | 67 | 43644 | 152371 | 228475 | 0 | 208140 | 0 | 0 | 1614 | 5 | 0 | 0 |
| Review whole change (opus) (the-way-stage) | Claude Code | 107 | 23826 | 225511 | 306779 | 565266 | 0 | 269472 | 1 | 8596 | 12 | 10868 | 2 |
| Review merge with target (opus) (the-way-stage) | Claude Code | 26 | 23850 | 74908 | 86993 | 76008 | 0 | 0 | 0 | 54395 | 7 | 0 | 0 |
| Author: rename readiness gate (the-way-author) | Claude Code | 168 | 23867 | 249572 | 336066 | 0 | 325033 | 0 | 0 | 168328 | 47 | 0 | 0 |
