# Measures of the cycle run

- Calls in all: 339
- Calls of the orchestrator: 112
- Calls of subagents: 227
- Mean context per call: 169291
- Mean context per call of the orchestrator: 218409
- Share of the context in calls above 200000 tokens: 54.2%
- Context of the orchestrator's first call: 43625
- Context of the orchestrator's middle call: 220593
- Context of the orchestrator's last call: 329999
- Cache written, 5 minutes: 578095
- Cache written, 1 hour: 570844
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 185436
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 346ed898-132f-4c72-92c6-904f4a0f7f2d | Claude Code | 112 | 43625 | 220593 | 329999 | 0 | 307112 | 0 | 0 | 27763 | 18 | 2536 | 3 |
| Review correction 1 (opus) (the-way-stage) | Claude Code | 24 | 23858 | 78160 | 91996 | 81011 | 0 | 0 | 0 | 28640 | 8 | 0 | 0 |
| Author: Relations TODO change (the-way-author) | Claude Code | 110 | 23905 | 186951 | 274765 | 0 | 263732 | 0 | 0 | 108923 | 42 | 599 | 1 |
| Review return step (opus) (the-way-stage) | Claude Code | 31 | 23841 | 75998 | 111063 | 100078 | 0 | 0 | 0 | 40969 | 16 | 0 | 0 |
| Review whole change (opus) (the-way-stage) | Claude Code | 62 | 23844 | 157645 | 222555 | 397006 | 0 | 185436 | 1 | 43181 | 13 | 47536 | 2 |
