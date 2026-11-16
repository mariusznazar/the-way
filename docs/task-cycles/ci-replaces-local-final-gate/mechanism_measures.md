# Measures of the cycle run

- Calls in all: 342
- Calls of the orchestrator: 67
- Calls of subagents: 275
- Mean context per call: 199725
- Mean context per call of the orchestrator: 135758
- Share of the context in calls above 200000 tokens: 63.9%
- Context of the orchestrator's first call: 43586
- Context of the orchestrator's middle call: 129134
- Context of the orchestrator's last call: 196648
- Cache written, 5 minutes: 713960
- Cache written, 1 hour: 573104
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 395277
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator e651c453-73a8-4340-a83c-7a087605f226 | Claude Code | 67 | 43586 | 129134 | 196648 | 0 | 174197 | 0 | 0 | 5581 | 6 | 6225 | 1 |
| Author: CI replaces local final gate (the-way-author) | Claude Code | 154 | 23896 | 286760 | 409940 | 0 | 398907 | 0 | 0 | 89070 | 55 | 39269 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 30 | 23824 | 78750 | 106013 | 95028 | 0 | 0 | 0 | 57082 | 11 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 91 | 23834 | 162974 | 234004 | 618932 | 0 | 395277 | 2 | 43161 | 11 | 9710 | 2 |
