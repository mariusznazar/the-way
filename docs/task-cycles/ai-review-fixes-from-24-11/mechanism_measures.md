# Measures of the cycle run

- Calls in all: 287
- Calls of the orchestrator: 65
- Calls of subagents: 222
- Mean context per call: 160090
- Mean context per call of the orchestrator: 155428
- Share of the context in calls above 200000 tokens: 42.2%
- Context of the orchestrator's first call: 43450
- Context of the orchestrator's middle call: 160032
- Context of the orchestrator's last call: 225806
- Cache written, 5 minutes: 390640
- Cache written, 1 hour: 497216
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 370390df-cbe0-4508-a11e-262c25bed673 | Claude Code | 65 | 43450 | 160032 | 225806 | 0 | 225804 | 0 | 0 | 16698 | 6 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 41 | 24807 | 111675 | 154172 | 143463 | 0 | 0 | 0 | 17096 | 5 | 54353 | 2 |
| One author makes the whole change (the-way-author) | Claude Code | 101 | 24900 | 193122 | 271414 | 0 | 271412 | 0 | 0 | 67301 | 35 | 0 | 0 |
| Second review of the whole change (the-way-stage) | Claude Code | 80 | 24807 | 168871 | 247179 | 247177 | 0 | 0 | 0 | 69521 | 13 | 49442 | 1 |
