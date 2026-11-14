# Measures of the cycle run

- Calls in all: 130
- Calls of the orchestrator: 48
- Calls of subagents: 82
- Mean context per call: 121601
- Mean context per call of the orchestrator: 131527
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 43411
- Context of the orchestrator's middle call: 137029
- Context of the orchestrator's last call: 168096
- Cache written, 5 minutes: 146522
- Cache written, 1 hour: 311372
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 169e58eb-7ed9-4e6f-89b0-9b2ac66ff9d1 | Claude Code | 48 | 43411 | 137029 | 168096 | 0 | 147838 | 0 | 0 |
| Review of whole change (the-way-stage) | Claude Code | 36 | 24038 | 116314 | 156871 | 146522 | 0 | 0 | 0 |
| Author of the one-author change (the-way-author) | Claude Code | 46 | 24096 | 131305 | 163536 | 0 | 163534 | 0 | 0 |
