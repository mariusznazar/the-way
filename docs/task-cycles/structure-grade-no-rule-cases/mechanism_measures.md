# Measures of the cycle run

- Calls in all: 114
- Calls of the orchestrator: 55
- Calls of subagents: 59
- Mean context per call: 102020
- Mean context per call of the orchestrator: 134805
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 47649
- Context of the orchestrator's middle call: 135026
- Context of the orchestrator's last call: 183766
- Cache written, 5 minutes: 173841
- Cache written, 1 hour: 260972
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 57372
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 07a4756c-bb67-40a5-86d3-f282fdd9b6fd | Claude Code | 55 | 47649 | 135026 | 183766 | 0 | 163508 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 23 | 24150 | 68357 | 116471 | 173841 | 0 | 57372 | 1 |
| Author of the structure-grade change (the-way-author) | Claude Code | 36 | 24208 | 75516 | 97466 | 0 | 97464 | 0 | 0 |
