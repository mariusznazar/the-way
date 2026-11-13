# Measures of the cycle run

- Calls in all: 179
- Calls of the orchestrator: 50
- Calls of subagents: 129
- Mean context per call: 134651
- Mean context per call of the orchestrator: 112818
- Share of the context in calls above 200000 tokens: 19.8%
- Context of the orchestrator's first call: 47190
- Context of the orchestrator's middle call: 116702
- Context of the orchestrator's last call: 153723
- Cache written, 5 minutes: 628246
- Cache written, 1 hour: 133465
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 196876
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator bb3371c6-5fde-46e9-af19-6b48a05ccc9e | Claude Code | 50 | 47190 | 116702 | 153723 | 0 | 133465 | 0 | 0 |
| Review the whole change (general-purpose) | Claude Code | 64 | 35784 | 125630 | 218421 | 214004 | 0 | 0 | 0 |
| Author: close decision-pending notes (general-purpose) | Claude Code | 65 | 35858 | 161857 | 217368 | 414242 | 0 | 196876 | 1 |
