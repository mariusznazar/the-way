# Measures of the cycle run

- Calls in all: 178
- Calls of the orchestrator: 58
- Calls of subagents: 120
- Mean context per call: 115245
- Mean context per call of the orchestrator: 133409
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 47272
- Context of the orchestrator's middle call: 140877
- Context of the orchestrator's last call: 173613
- Cache written, 5 minutes: 621975
- Cache written, 1 hour: 153355
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 293112
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator b2ce3676-d004-46d6-a590-e1c0756f6619 | Claude Code | 58 | 47272 | 140877 | 173613 | 0 | 153355 | 0 | 0 |
| Review of whole change (general-purpose) | Claude Code | 37 | 35903 | 95720 | 123075 | 111196 | 0 | 0 | 0 |
| Author of gate-series change (general-purpose) | Claude Code | 73 | 35886 | 127596 | 167565 | 460675 | 0 | 293112 | 2 |
| Review return step commits (general-purpose) | Claude Code | 10 | 35863 | 57042 | 61983 | 50104 | 0 | 0 | 0 |
