# Measures of the cycle run

- Calls in all: 199
- Calls of the orchestrator: 65
- Calls of subagents: 134
- Mean context per call: 128308
- Mean context per call of the orchestrator: 134613
- Share of the context in calls above 200000 tokens: 6.5%
- Context of the orchestrator's first call: 43594
- Context of the orchestrator's middle call: 134970
- Context of the orchestrator's last call: 213513
- Cache written, 5 minutes: 320421
- Cache written, 1 hour: 374713
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 147885
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator d71eadfd-2aa6-4ef2-a694-f1e5c90850b7 | Claude Code | 65 | 43594 | 134970 | 213513 | 0 | 193255 | 0 | 0 | 15799 | 11 | 6746 | 2 |
| Review whole change (opus) (the-way-stage) | Claude Code | 57 | 23911 | 134171 | 183521 | 320421 | 0 | 147885 | 1 | 83191 | 12 | 52880 | 2 |
| One author: renumber decisions rule (the-way-author) | Claude Code | 77 | 23940 | 133717 | 192491 | 0 | 181458 | 0 | 0 | 58467 | 28 | 3076 | 1 |
