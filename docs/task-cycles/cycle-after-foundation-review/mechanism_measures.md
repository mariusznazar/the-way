# Measures of the cycle run

- Calls in all: 236
- Calls of the orchestrator: 92
- Calls of subagents: 144
- Mean context per call: 167250
- Mean context per call of the orchestrator: 187554
- Share of the context in calls above 200000 tokens: 41.8%
- Context of the orchestrator's first call: 43399
- Context of the orchestrator's middle call: 180339
- Context of the orchestrator's last call: 277487
- Cache written, 5 minutes: 311752
- Cache written, 1 hour: 481421
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 149760
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator a6a1e1b7-5f47-41a4-9533-43afd5ede04a | Claude Code | 92 | 43399 | 180339 | 277487 | 0 | 253820 | 0 | 0 | 38647 | 14 | 213 | 1 |
| Author: whole change, one author (the-way-author) | Claude Code | 93 | 23797 | 184797 | 238634 | 0 | 227601 | 0 | 0 | 98885 | 63 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 51 | 23789 | 127337 | 172341 | 311752 | 0 | 149760 | 1 | 72334 | 17 | 48563 | 3 |
