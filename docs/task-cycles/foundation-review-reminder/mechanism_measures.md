# Measures of the cycle run

- Calls in all: 222
- Calls of the orchestrator: 69
- Calls of subagents: 153
- Mean context per call: 150622
- Mean context per call of the orchestrator: 169213
- Share of the context in calls above 200000 tokens: 36.7%
- Context of the orchestrator's first call: 43360
- Context of the orchestrator's middle call: 172439
- Context of the orchestrator's last call: 246657
- Cache written, 5 minutes: 235570
- Cache written, 1 hour: 448286
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 4954eb60-59de-4f07-b6e3-618504cc8167 | Claude Code | 69 | 43360 | 172439 | 246657 | 0 | 221975 | 0 | 0 | 13079 | 9 | 58769 | 2 |
| Review of the return step (the-way-stage) | Claude Code | 13 | 23893 | 52169 | 61560 | 50575 | 0 | 0 | 0 | 23653 | 5 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 47 | 23906 | 129417 | 195344 | 184995 | 0 | 0 | 0 | 19234 | 7 | 67636 | 3 |
| Author of the whole change (the-way-author) | Claude Code | 93 | 23907 | 175690 | 236660 | 0 | 226311 | 0 | 0 | 102885 | 48 | 0 | 0 |
