# Measures of the cycle run

- Calls in all: 400
- Calls of the orchestrator: 129
- Calls of subagents: 271
- Mean context per call: 222246
- Mean context per call of the orchestrator: 235958
- Share of the context in calls above 200000 tokens: 76.0%
- Context of the orchestrator's first call: 44281
- Context of the orchestrator's middle call: 252064
- Context of the orchestrator's last call: 365611
- Cache written, 5 minutes: 869321
- Cache written, 1 hour: 690280
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 298597
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 5e78bb61-df89-4942-8244-96c8accc7f42 | Claude Code | 129 | 44281 | 252064 | 365611 | 0 | 346173 | 0 | 0 | 19833 | 15 | 20687 | 2 |
| Review whole change (fable) (the-way-stage) | Claude Code | 104 | 24024 | 245483 | 389280 | 687875 | 0 | 298597 | 1 | 87903 | 27 | 55357 | 4 |
| Author: decision length check (the-way-author) | Claude Code | 134 | 24085 | 233903 | 344109 | 0 | 344107 | 0 | 0 | 57919 | 39 | 36596 | 3 |
| Review correction 1 (fable) (the-way-stage) | Claude Code | 33 | 24026 | 125839 | 181448 | 181446 | 0 | 0 | 0 | 92038 | 16 | 0 | 0 |
