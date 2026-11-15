# Measures of the cycle run

- Calls in all: 283
- Calls of the orchestrator: 108
- Calls of subagents: 175
- Mean context per call: 198417
- Mean context per call of the orchestrator: 254344
- Share of the context in calls above 200000 tokens: 64.4%
- Context of the orchestrator's first call: 43903
- Context of the orchestrator's middle call: 262051
- Context of the orchestrator's last call: 374287
- Cache written, 5 minutes: 459222
- Cache written, 1 hour: 639174
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 161786
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator a65511a5-afea-42b5-b4c8-d70407f014de | Claude Code | 108 | 43903 | 262051 | 374287 | 0 | 353584 | 0 | 0 | 20117 | 9 | 0 | 0 |
| Review of the return step (the-way-stage) | Claude Code | 24 | 24903 | 88751 | 122284 | 111299 | 0 | 0 | 0 | 29433 | 3 | 0 | 0 |
| Whole-change review of Docker repair (the-way-stage) | Claude Code | 47 | 24908 | 147789 | 196486 | 347923 | 0 | 161786 | 1 | 9014 | 6 | 0 | 0 |
| One author: Docker start repair (the-way-author) | Claude Code | 104 | 24969 | 199819 | 296623 | 0 | 285590 | 0 | 0 | 38087 | 17 | 0 | 0 |
