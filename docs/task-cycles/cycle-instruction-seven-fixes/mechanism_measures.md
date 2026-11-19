# Measures of the cycle run

- Calls in all: 195
- Calls of the orchestrator: 49
- Calls of subagents: 146
- Mean context per call: 169374
- Mean context per call of the orchestrator: 129145
- Share of the context in calls above 200000 tokens: 45.0%
- Context of the orchestrator's first call: 44479
- Context of the orchestrator's middle call: 131424
- Context of the orchestrator's last call: 176152
- Cache written, 5 minutes: 549486
- Cache written, 1 hour: 389901
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 266888
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 6df616db-85eb-4ad5-a81a-6a795abd1993 | Claude Code | 49 | 44479 | 131424 | 176152 | 0 | 155120 | 0 | 0 | 3467 | 7 | 3713 | 1 |
| Author makes the whole change (the-way-author) | Claude Code | 88 | 24108 | 192528 | 246008 | 0 | 234781 | 0 | 0 | 79197 | 50 | 51462 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 58 | 23981 | 193858 | 282600 | 549486 | 0 | 266888 | 1 | 83656 | 17 | 81739 | 3 |
