# Measures of the cycle run

- Calls in all: 417
- Calls of the orchestrator: 59
- Calls of subagents: 358
- Mean context per call: 237475
- Mean context per call of the orchestrator: 159625
- Share of the context in calls above 200000 tokens: 80.8%
- Context of the orchestrator's first call: 43389
- Context of the orchestrator's middle call: 157497
- Context of the orchestrator's last call: 221528
- Cache written, 5 minutes: 672922
- Cache written, 1 hour: 655603
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 281471
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 18447244-14b9-49f0-b45f-ffc03d45a126 | Claude Code | 59 | 43389 | 157497 | 221528 | 0 | 201161 | 0 | 0 |
| Author of CI-on-merge-requests change (the-way-author) | Claude Code | 219 | 23804 | 300154 | 464791 | 0 | 454442 | 0 | 0 |
| Review of the return step commit (the-way-stage) | Claude Code | 25 | 23716 | 66100 | 77524 | 67175 | 0 | 0 | 0 |
| Review of whole change (the-way-stage) | Claude Code | 114 | 23741 | 222213 | 335261 | 605747 | 0 | 281471 | 1 |
