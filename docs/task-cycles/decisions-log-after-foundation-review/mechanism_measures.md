# Measures of the cycle run

- Calls in all: 412
- Calls of the orchestrator: 63
- Calls of subagents: 349
- Mean context per call: 233864
- Mean context per call of the orchestrator: 157295
- Share of the context in calls above 200000 tokens: 73.5%
- Context of the orchestrator's first call: 43424
- Context of the orchestrator's middle call: 165707
- Context of the orchestrator's last call: 229768
- Cache written, 5 minutes: 629468
- Cache written, 1 hour: 641978
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 307062
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 8a81f3da-ed9f-4237-ac3e-c2949e9c56c8 | Claude Code | 63 | 43424 | 165707 | 229768 | 0 | 209200 | 0 | 0 | 14681 | 8 | 0 | 0 |
| One author makes the whole change (the-way-author) | Claude Code | 241 | 23799 | 276685 | 443811 | 0 | 432778 | 0 | 0 | 330102 | 123 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 108 | 23767 | 188678 | 322408 | 629468 | 0 | 307062 | 1 | 131639 | 38 | 86851 | 3 |
