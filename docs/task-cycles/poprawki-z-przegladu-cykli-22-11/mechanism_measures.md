# Measures of the cycle run

- Calls in all: 439
- Calls of the orchestrator: 54
- Calls of subagents: 385
- Mean context per call: 269629
- Mean context per call of the orchestrator: 166235
- Share of the context in calls above 200000 tokens: 84.8%
- Context of the orchestrator's first call: 42610
- Context of the orchestrator's middle call: 173274
- Context of the orchestrator's last call: 251306
- Cache written, 5 minutes: 764842
- Cache written, 1 hour: 756553
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 308099
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 960e9d08-1869-4341-ba56-6cf1fa576473 | Claude Code | 54 | 42610 | 173274 | 251306 | 0 | 232449 | 0 | 0 | 3165 | 3 | 0 | 0 |
| One author makes whole change (the-way-author) | Claude Code | 233 | 24827 | 374068 | 524106 | 0 | 524104 | 0 | 0 | 59519 | 33 | 59155 | 2 |
| Review of return step commit (the-way-stage) | Claude Code | 41 | 24766 | 101096 | 123768 | 112589 | 0 | 0 | 0 | 32736 | 7 | 1510 | 1 |
| Review of whole change (the-way-stage) | Claude Code | 111 | 24795 | 236782 | 344156 | 652253 | 0 | 308099 | 1 | 38779 | 14 | 10639 | 3 |
