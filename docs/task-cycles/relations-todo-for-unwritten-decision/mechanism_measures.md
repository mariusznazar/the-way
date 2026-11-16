# Measures of the cycle run

- Calls in all: 250
- Calls of the orchestrator: 67
- Calls of subagents: 183
- Mean context per call: 149249
- Mean context per call of the orchestrator: 166994
- Share of the context in calls above 200000 tokens: 34.0%
- Context of the orchestrator's first call: 43625
- Context of the orchestrator's middle call: 163194
- Context of the orchestrator's last call: 253344
- Cache written, 5 minutes: 497084
- Cache written, 1 hour: 456683
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 185436
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 346ed898-132f-4c72-92c6-904f4a0f7f2d | Claude Code | 67 | 43625 | 163194 | 253344 | 0 | 230966 | 0 | 0 | 14348 | 12 | 2536 | 3 |
| Author: Relations TODO change (the-way-author) | Claude Code | 90 | 23905 | 167761 | 236750 | 0 | 225717 | 0 | 0 | 79990 | 35 | 599 | 1 |
| Review return step (opus) (the-way-stage) | Claude Code | 31 | 23841 | 75998 | 111063 | 100078 | 0 | 0 | 0 | 40969 | 16 | 0 | 0 |
| Review whole change (opus) (the-way-stage) | Claude Code | 62 | 23844 | 157645 | 222555 | 397006 | 0 | 185436 | 1 | 43181 | 13 | 47536 | 2 |
