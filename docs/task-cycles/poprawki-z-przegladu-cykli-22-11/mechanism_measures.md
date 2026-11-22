# Measures of the cycle run

- Calls in all: 507
- Calls of the orchestrator: 100
- Calls of subagents: 407
- Mean context per call: 279418
- Mean context per call of the orchestrator: 230055
- Share of the context in calls above 200000 tokens: 87.3%
- Context of the orchestrator's first call: 42610
- Context of the orchestrator's middle call: 225572
- Context of the orchestrator's last call: 351617
- Cache written, 5 minutes: 1133083
- Cache written, 1 hour: 869287
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 652253
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 960e9d08-1869-4341-ba56-6cf1fa576473 | Claude Code | 100 | 42610 | 225572 | 351617 | 0 | 332461 | 0 | 0 | 3413 | 4 | 0 | 0 |
| One author makes whole change (the-way-author) | Claude Code | 241 | 24827 | 383047 | 536828 | 0 | 536826 | 0 | 0 | 59519 | 33 | 59155 | 2 |
| Review of return step commit (the-way-stage) | Claude Code | 41 | 24766 | 101096 | 123768 | 112589 | 0 | 0 | 0 | 32736 | 7 | 1510 | 1 |
| Review of whole change (the-way-stage) | Claude Code | 125 | 24795 | 245357 | 368243 | 1020494 | 0 | 652253 | 2 | 45570 | 16 | 10639 | 3 |
