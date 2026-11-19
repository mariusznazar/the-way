# Measures of the cycle run

- Calls in all: 335
- Calls of the orchestrator: 68
- Calls of subagents: 267
- Mean context per call: 239528
- Mean context per call of the orchestrator: 146040
- Share of the context in calls above 200000 tokens: 81.2%
- Context of the orchestrator's first call: 44321
- Context of the orchestrator's middle call: 137766
- Context of the orchestrator's last call: 211954
- Cache written, 5 minutes: 843942
- Cache written, 1 hour: 616234
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 333497
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator da0af92c-74ab-4e4f-a2e7-1c7cc043108d | Claude Code | 68 | 44321 | 137766 | 211954 | 0 | 191088 | 0 | 0 | 6547 | 6 | 4084 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 21 | 24139 | 80314 | 113721 | 102542 | 0 | 0 | 0 | 27202 | 11 | 0 | 0 |
| One author: project closure step (the-way-author) | Claude Code | 159 | 24116 | 315827 | 435689 | 0 | 425146 | 0 | 0 | 180688 | 40 | 2046 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 87 | 24141 | 271994 | 407905 | 741400 | 0 | 333497 | 1 | 181743 | 27 | 80770 | 3 |
