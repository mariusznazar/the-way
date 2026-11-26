# Measures of the cycle run

- Calls in all: 210
- Calls of the orchestrator: 48
- Calls of subagents: 162
- Mean context per call: 156199
- Mean context per call of the orchestrator: 128483
- Share of the context in calls above 200000 tokens: 35.3%
- Context of the orchestrator's first call: 43526
- Context of the orchestrator's middle call: 133371
- Context of the orchestrator's last call: 183408
- Cache written, 5 minutes: 336798
- Cache written, 1 hour: 429948
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 154516
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 8b8b8599-10bb-4a35-926a-f251f6eb5bd2 | Claude Code | 48 | 43526 | 133371 | 183408 | 0 | 163745 | 0 | 0 | 242 | 1 | 0 | 0 |
| Review of whole change (the-way-stage) | Claude Code | 63 | 24839 | 135891 | 192991 | 336798 | 0 | 154516 | 1 | 36130 | 11 | 3913 | 1 |
| Author of the change (the-way-author) | Claude Code | 99 | 24883 | 200926 | 266205 | 0 | 266203 | 0 | 0 | 85927 | 51 | 0 | 0 |
