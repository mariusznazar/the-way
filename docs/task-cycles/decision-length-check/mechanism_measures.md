# Measures of the cycle run

- Calls in all: 303
- Calls of the orchestrator: 95
- Calls of subagents: 208
- Mean context per call: 187556
- Mean context per call of the orchestrator: 200197
- Share of the context in calls above 200000 tokens: 62.4%
- Context of the orchestrator's first call: 44281
- Context of the orchestrator's middle call: 209098
- Context of the orchestrator's last call: 303301
- Cache written, 5 minutes: 480043
- Cache written, 1 hour: 553233
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 5e78bb61-df89-4942-8244-96c8accc7f42 | Claude Code | 95 | 44281 | 209098 | 303301 | 0 | 283863 | 0 | 0 | 19625 | 14 | 20687 | 2 |
| Review whole change (fable) (the-way-stage) | Claude Code | 79 | 24024 | 214487 | 298599 | 298597 | 0 | 0 | 0 | 66959 | 17 | 52109 | 3 |
| Author: decision length check (the-way-author) | Claude Code | 96 | 24085 | 193305 | 269372 | 0 | 269370 | 0 | 0 | 29430 | 25 | 18652 | 1 |
| Review correction 1 (fable) (the-way-stage) | Claude Code | 33 | 24026 | 125839 | 181448 | 181446 | 0 | 0 | 0 | 92038 | 16 | 0 | 0 |
