# Measures of the cycle run

- Calls in all: 419
- Calls of the orchestrator: 106
- Calls of subagents: 313
- Mean context per call: 219392
- Mean context per call of the orchestrator: 180080
- Share of the context in calls above 200000 tokens: 72.9%
- Context of the orchestrator's first call: 43586
- Context of the orchestrator's middle call: 177277
- Context of the orchestrator's last call: 291357
- Cache written, 5 minutes: 959465
- Cache written, 1 hour: 712782
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 618932
- Calls of subagents with a cache write again: 3

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator e651c453-73a8-4340-a83c-7a087605f226 | Claude Code | 106 | 43586 | 177277 | 291357 | 0 | 268551 | 0 | 0 | 8224 | 8 | 6225 | 1 |
| Author: CI replaces local final gate (the-way-author) | Claude Code | 176 | 23896 | 298610 | 455264 | 0 | 444231 | 0 | 0 | 89070 | 55 | 39269 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 30 | 23824 | 78750 | 106013 | 95028 | 0 | 0 | 0 | 57082 | 11 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 107 | 23834 | 173080 | 255854 | 864437 | 0 | 618932 | 3 | 43161 | 11 | 9710 | 2 |
