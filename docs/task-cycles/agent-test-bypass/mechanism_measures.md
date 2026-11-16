# Measures of the cycle run

- Calls in all: 290
- Calls of the orchestrator: 71
- Calls of subagents: 219
- Mean context per call: 178843
- Mean context per call of the orchestrator: 155077
- Share of the context in calls above 200000 tokens: 59.9%
- Context of the orchestrator's first call: 43531
- Context of the orchestrator's middle call: 154772
- Context of the orchestrator's last call: 241396
- Cache written, 5 minutes: 333075
- Cache written, 1 hour: 554323
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator c058f437-ab1e-4363-9055-6a9e9c8cba10 | Claude Code | 71 | 43531 | 154772 | 241396 | 0 | 220735 | 0 | 0 | 8290 | 12 | 67470 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 71 | 23814 | 157852 | 227564 | 217215 | 0 | 0 | 0 | 18704 | 11 | 78317 | 3 |
| One author makes the change (the-way-author) | Claude Code | 117 | 23830 | 260858 | 344621 | 0 | 333588 | 0 | 0 | 105479 | 35 | 60678 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 31 | 23808 | 85708 | 126845 | 115860 | 0 | 0 | 0 | 43416 | 10 | 0 | 0 |
