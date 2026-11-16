# Measures of the cycle run

- Calls in all: 304
- Calls of the orchestrator: 51
- Calls of subagents: 253
- Mean context per call: 248531
- Mean context per call of the orchestrator: 126732
- Share of the context in calls above 200000 tokens: 78.0%
- Context of the orchestrator's first call: 43600
- Context of the orchestrator's middle call: 119149
- Context of the orchestrator's last call: 176026
- Cache written, 5 minutes: 329369
- Cache written, 1 hour: 644950
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 601c0a77-f5eb-4452-98ee-05fd086bbaad | Claude Code | 51 | 43600 | 119149 | 176026 | 0 | 154817 | 0 | 0 | 5624 | 8 | 1333 | 1 |
| Author of the whole change (the-way-author) | Claude Code | 156 | 23943 | 333867 | 490135 | 0 | 490133 | 0 | 0 | 219717 | 106 | 75309 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 97 | 23888 | 211409 | 339718 | 329369 | 0 | 0 | 0 | 165700 | 36 | 9058 | 2 |
