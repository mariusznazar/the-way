# Measures of the cycle run

- Calls in all: 486
- Calls of the orchestrator: 101
- Calls of subagents: 385
- Mean context per call: 234994
- Mean context per call of the orchestrator: 182521
- Share of the context in calls above 200000 tokens: 80.2%
- Context of the orchestrator's first call: 43644
- Context of the orchestrator's middle call: 176635
- Context of the orchestrator's last call: 280810
- Cache written, 5 minutes: 1012840
- Cache written, 1 hour: 691356
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 565902
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator d7bf39e7-fa87-4d58-910a-68df82a8e98e | Claude Code | 101 | 43644 | 176635 | 280810 | 0 | 259874 | 0 | 0 | 1664 | 6 | 0 | 0 |
| Review whole change (opus) (the-way-stage) | Claude Code | 137 | 23826 | 264066 | 381915 | 936832 | 0 | 565902 | 2 | 13665 | 18 | 10868 | 2 |
| Review merge with target (opus) (the-way-stage) | Claude Code | 26 | 23850 | 74908 | 86993 | 76008 | 0 | 0 | 0 | 54395 | 7 | 0 | 0 |
| Author: rename readiness gate (the-way-author) | Claude Code | 222 | 23867 | 272716 | 442515 | 0 | 431482 | 0 | 0 | 202174 | 59 | 0 | 0 |
