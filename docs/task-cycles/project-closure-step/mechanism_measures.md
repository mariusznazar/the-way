# Measures of the cycle run

- Calls in all: 451
- Calls of the orchestrator: 119
- Calls of subagents: 332
- Mean context per call: 244419
- Mean context per call of the orchestrator: 202596
- Share of the context in calls above 200000 tokens: 81.6%
- Context of the orchestrator's first call: 44321
- Context of the orchestrator's middle call: 204325
- Context of the orchestrator's last call: 321434
- Cache written, 5 minutes: 1030197
- Cache written, 1 hour: 763899
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 333497
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator da0af92c-74ab-4e4f-a2e7-1c7cc043108d | Claude Code | 119 | 44321 | 204325 | 321434 | 0 | 299960 | 0 | 0 | 24199 | 11 | 4084 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 21 | 24139 | 80314 | 113721 | 102542 | 0 | 0 | 0 | 27202 | 11 | 0 | 0 |
| Review of correction 1 (the-way-stage) | Claude Code | 42 | 24164 | 128887 | 186257 | 186255 | 0 | 0 | 0 | 26216 | 12 | 0 | 0 |
| One author: project closure step (the-way-author) | Claude Code | 182 | 24116 | 327625 | 474482 | 0 | 463939 | 0 | 0 | 186969 | 42 | 2046 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 87 | 24141 | 271994 | 407905 | 741400 | 0 | 333497 | 1 | 181743 | 27 | 80770 | 3 |
