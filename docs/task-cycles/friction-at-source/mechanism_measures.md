# Measures of the cycle run

- Calls in all: 194
- Calls of the orchestrator: 59
- Calls of subagents: 135
- Mean context per call: 157980
- Mean context per call of the orchestrator: 138630
- Share of the context in calls above 200000 tokens: 30.4%
- Context of the orchestrator's first call: 47165
- Context of the orchestrator's middle call: 144803
- Context of the orchestrator's last call: 193081
- Cache written, 5 minutes: 635196
- Cache written, 1 hour: 172245
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 206211
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 8a37a2c8-29d4-4020-a58b-48d132eb4390 | Claude Code | 59 | 47165 | 144803 | 193081 | 0 | 172245 | 0 | 0 |
| Review the whole change (general-purpose) | Claude Code | 41 | 35683 | 133983 | 195003 | 183124 | 0 | 0 | 0 |
| Author of friction-at-source change (general-purpose) | Claude Code | 94 | 35637 | 192901 | 257740 | 452072 | 0 | 206211 | 1 |
