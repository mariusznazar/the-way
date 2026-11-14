# Measures of the cycle run

- Calls in all: 120
- Calls of the orchestrator: 46
- Calls of subagents: 74
- Mean context per call: 121616
- Mean context per call of the orchestrator: 129036
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 47272
- Context of the orchestrator's middle call: 127459
- Context of the orchestrator's last call: 191310
- Cache written, 5 minutes: 443356
- Cache written, 1 hour: 171052
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 145480
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 3dc16b85-0ea9-4ad1-bef8-28e06808fbe3 | Claude Code | 46 | 47272 | 127459 | 191310 | 0 | 171052 | 0 | 0 |
| Whole-change review of slice limit (general-purpose) | Claude Code | 24 | 35841 | 101578 | 136763 | 124884 | 0 | 0 | 0 |
| One author: slice read limit 150k (general-purpose) | Claude Code | 50 | 35916 | 131415 | 172994 | 318472 | 0 | 145480 | 1 |
