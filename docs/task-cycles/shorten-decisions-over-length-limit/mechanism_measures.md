# Measures of the cycle run

- Calls in all: 198
- Calls of the orchestrator: 47
- Calls of subagents: 151
- Mean context per call: 166133
- Mean context per call of the orchestrator: 134537
- Share of the context in calls above 200000 tokens: 44.0%
- Context of the orchestrator's first call: 44317
- Context of the orchestrator's middle call: 131856
- Context of the orchestrator's last call: 178940
- Cache written, 5 minutes: 206017
- Cache written, 1 hour: 420225
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator eff99e6f-c74f-4608-b080-98e4680f90db | Claude Code | 47 | 44317 | 131856 | 178940 | 0 | 158074 | 0 | 0 | 1192 | 5 | 4402 | 1 |
| One author makes the change (the-way-author) | Claude Code | 96 | 24059 | 207694 | 273378 | 0 | 262151 | 0 | 0 | 236733 | 51 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 55 | 24020 | 152493 | 217196 | 206017 | 0 | 0 | 0 | 56231 | 17 | 5153 | 2 |
