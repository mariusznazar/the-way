# Measures of the cycle run

- Calls in all: 205
- Calls of the orchestrator: 51
- Calls of subagents: 154
- Mean context per call: 139927
- Mean context per call of the orchestrator: 118128
- Share of the context in calls above 200000 tokens: 17.8%
- Context of the orchestrator's first call: 43267
- Context of the orchestrator's middle call: 123517
- Context of the orchestrator's last call: 164103
- Cache written, 5 minutes: 320960
- Cache written, 1 hour: 360817
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 141215
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator e5f1bf51-f799-4991-8c45-1a10cdd3be91 | Claude Code | 51 | 43267 | 123517 | 164103 | 0 | 143845 | 0 | 0 |
| Review whole change (the-way-stage) | Claude Code | 74 | 23993 | 140378 | 190730 | 320960 | 0 | 141215 | 1 |
| One author of deployment-skill guide (the-way-author) | Claude Code | 80 | 24090 | 160598 | 227321 | 0 | 216972 | 0 | 0 |
