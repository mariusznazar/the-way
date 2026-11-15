# Measures of the cycle run

- Calls in all: 322
- Calls of the orchestrator: 97
- Calls of subagents: 225
- Mean context per call: 211597
- Mean context per call of the orchestrator: 213584
- Share of the context in calls above 200000 tokens: 75.8%
- Context of the orchestrator's first call: 43382
- Context of the orchestrator's middle call: 207120
- Context of the orchestrator's last call: 335754
- Cache written, 5 minutes: 530530
- Cache written, 1 hour: 670310
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 233926
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 777280c9-9741-4f22-86df-3621b2ac7c7d | Claude Code | 97 | 43382 | 207120 | 335754 | 0 | 312455 | 0 | 0 | 21125 | 9 | 46666 | 2 |
| Review return step commit (the-way-stage) | Claude Code | 13 | 23741 | 42627 | 49067 | 38082 | 0 | 0 | 0 | 6782 | 2 | 0 | 0 |
| Review whole change (the-way-stage) | Claude Code | 91 | 23749 | 173417 | 268871 | 492448 | 0 | 233926 | 1 | 102287 | 20 | 67659 | 3 |
| Author: part map deps and task line (the-way-author) | Claude Code | 121 | 23767 | 272110 | 371062 | 0 | 357855 | 0 | 0 | 101528 | 52 | 40174 | 1 |
