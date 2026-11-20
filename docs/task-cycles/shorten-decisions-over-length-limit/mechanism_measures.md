# Measures of the cycle run

- Calls in all: 261
- Calls of the orchestrator: 92
- Calls of subagents: 169
- Mean context per call: 185881
- Mean context per call of the orchestrator: 187210
- Share of the context in calls above 200000 tokens: 60.4%
- Context of the orchestrator's first call: 44317
- Context of the orchestrator's middle call: 178496
- Context of the orchestrator's last call: 278948
- Cache written, 5 minutes: 433575
- Cache written, 1 hour: 535247
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 217194
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator eff99e6f-c74f-4608-b080-98e4680f90db | Claude Code | 92 | 44317 | 178496 | 278948 | 0 | 258080 | 0 | 0 | 4137 | 11 | 4402 | 1 |
| One author makes the change (the-way-author) | Claude Code | 108 | 24059 | 215051 | 288394 | 0 | 277167 | 0 | 0 | 244113 | 55 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 61 | 24020 | 156877 | 227560 | 433575 | 0 | 217194 | 1 | 56484 | 18 | 5153 | 2 |
