# Measures of the cycle run

- Calls in all: 205
- Calls of the orchestrator: 45
- Calls of subagents: 160
- Mean context per call: 175785
- Mean context per call of the orchestrator: 135060
- Share of the context in calls above 200000 tokens: 51.7%
- Context of the orchestrator's first call: 44281
- Context of the orchestrator's middle call: 135139
- Context of the orchestrator's last call: 203683
- Cache written, 5 minutes: 298597
- Cache written, 1 hour: 436538
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 5e78bb61-df89-4942-8244-96c8accc7f42 | Claude Code | 45 | 44281 | 135139 | 203683 | 0 | 184245 | 0 | 0 | 2512 | 6 | 20687 | 2 |
| Review whole change (fable) (the-way-stage) | Claude Code | 79 | 24024 | 214487 | 298599 | 298597 | 0 | 0 | 0 | 66959 | 17 | 52109 | 3 |
| Author: decision length check (the-way-author) | Claude Code | 81 | 24085 | 184590 | 252295 | 0 | 252293 | 0 | 0 | 23780 | 20 | 18652 | 1 |
