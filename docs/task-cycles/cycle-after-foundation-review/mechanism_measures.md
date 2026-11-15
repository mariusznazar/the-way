# Measures of the cycle run

- Calls in all: 176
- Calls of the orchestrator: 50
- Calls of subagents: 126
- Mean context per call: 144318
- Mean context per call of the orchestrator: 139348
- Share of the context in calls above 200000 tokens: 15.0%
- Context of the orchestrator's first call: 43399
- Context of the orchestrator's middle call: 146200
- Context of the orchestrator's last call: 183026
- Cache written, 5 minutes: 149760
- Cache written, 1 hour: 371769
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator a6a1e1b7-5f47-41a4-9533-43afd5ede04a | Claude Code | 50 | 43399 | 146200 | 183026 | 0 | 161477 | 0 | 0 | 4090 | 5 | 213 | 1 |
| Author: whole change, one author (the-way-author) | Claude Code | 81 | 23797 | 174621 | 221325 | 0 | 210292 | 0 | 0 | 83244 | 51 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 45 | 23789 | 123795 | 160109 | 149760 | 0 | 0 | 0 | 66873 | 14 | 48563 | 3 |
