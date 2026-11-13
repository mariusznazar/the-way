# Measures of the cycle run

- Calls in all: 233
- Calls of the orchestrator: 51
- Calls of subagents: 182
- Mean context per call: 176998
- Mean context per call of the orchestrator: 152836
- Share of the context in calls above 200000 tokens: 48.4%
- Context of the orchestrator's first call: 47144
- Context of the orchestrator's middle call: 160059
- Context of the orchestrator's last call: 193726
- Cache written, 5 minutes: 873304
- Cache written, 1 hour: 175237
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 407153
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 74cb4adf-a7bb-4219-8069-9e18b8fdc041 | Claude Code | 51 | 47144 | 160059 | 193726 | 0 | 175237 | 0 | 0 |
| One author makes the change (general-purpose) | Claude Code | 124 | 35648 | 225257 | 286851 | 544688 | 0 | 257839 | 1 |
| Review of the whole change (general-purpose) | Claude Code | 58 | 35712 | 137711 | 191181 | 328616 | 0 | 149314 | 1 |
