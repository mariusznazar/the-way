# Measures of the cycle run

- Calls in all: 172
- Calls of the orchestrator: 49
- Calls of subagents: 123
- Mean context per call: 145952
- Mean context per call of the orchestrator: 149850
- Share of the context in calls above 200000 tokens: 15.3%
- Context of the orchestrator's first call: 42641
- Context of the orchestrator's middle call: 147136
- Context of the orchestrator's last call: 225189
- Cache written, 5 minutes: 211676
- Cache written, 1 hour: 398389
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator ee3ff5bf-1f2f-4329-915c-ed15e22a8058 | Claude Code | 49 | 42641 | 147136 | 225189 | 0 | 203564 | 0 | 0 | 2740 | 3 | 10022 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 63 | 24730 | 167730 | 222855 | 211676 | 0 | 0 | 0 | 31816 | 5 | 61469 | 3 |
| Author of the small-fixes change (the-way-author) | Claude Code | 60 | 24789 | 140009 | 194827 | 0 | 194825 | 0 | 0 | 11681 | 7 | 0 | 0 |
