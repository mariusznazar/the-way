# Measures of the cycle run

- Calls in all: 471
- Calls of the orchestrator: 135
- Calls of subagents: 336
- Mean context per call: 234010
- Mean context per call of the orchestrator: 209593
- Share of the context in calls above 200000 tokens: 77.4%
- Context of the orchestrator's first call: 43586
- Context of the orchestrator's middle call: 198376
- Context of the orchestrator's last call: 340787
- Cache written, 5 minutes: 1215405
- Cache written, 1 hour: 779213
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 863801
- Calls of subagents with a cache write again: 4

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator e651c453-73a8-4340-a83c-7a087605f226 | Claude Code | 135 | 43586 | 198376 | 340787 | 0 | 316386 | 0 | 0 | 8224 | 8 | 6225 | 1 |
| Author: CI replaces local final gate (the-way-author) | Claude Code | 191 | 23896 | 308019 | 473860 | 0 | 462827 | 0 | 0 | 95972 | 58 | 39269 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 30 | 23824 | 78750 | 106013 | 95028 | 0 | 0 | 0 | 57082 | 11 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 115 | 23834 | 174512 | 266925 | 1120377 | 0 | 863801 | 4 | 43161 | 11 | 9710 | 2 |
