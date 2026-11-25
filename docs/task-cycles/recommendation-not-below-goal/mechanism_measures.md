# Measures of the cycle run

- Calls in all: 218
- Calls of the orchestrator: 70
- Calls of subagents: 148
- Mean context per call: 126141
- Mean context per call of the orchestrator: 164450
- Share of the context in calls above 200000 tokens: 20.7%
- Context of the orchestrator's first call: 43417
- Context of the orchestrator's middle call: 160579
- Context of the orchestrator's last call: 262496
- Cache written, 5 minutes: 300247
- Cache written, 1 hour: 404803
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator b4ff38e1-93f8-45a1-8e5d-202afef9cf3d | Claude Code | 70 | 43417 | 160579 | 262496 | 0 | 243473 | 0 | 0 | 29545 | 15 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 31 | 24816 | 97592 | 134388 | 123043 | 0 | 0 | 0 | 62577 | 17 | 32952 | 3 |
| Author of the change (the-way-author) | Claude Code | 61 | 24873 | 107738 | 161332 | 0 | 161330 | 0 | 0 | 71252 | 38 | 0 | 0 |
| Second review of whole change (the-way-stage) | Claude Code | 56 | 24816 | 116509 | 177206 | 177204 | 0 | 0 | 0 | 76679 | 19 | 51093 | 2 |
