# Measures of the cycle run

- Calls in all: 163
- Calls of the orchestrator: 60
- Calls of subagents: 103
- Mean context per call: 122234
- Mean context per call of the orchestrator: 124201
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 43425
- Context of the orchestrator's middle call: 121262
- Context of the orchestrator's last call: 177974
- Cache written, 5 minutes: 276492
- Cache written, 1 hour: 336746
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 130653
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 397f5de7-5d0a-4193-9103-86ff4b0cf1c1 | Claude Code | 60 | 43425 | 121262 | 177974 | 0 | 157604 | 0 | 0 | 5564 | 7 | 6535 | 1 |
| One author makes the change (the-way-author) | Claude Code | 61 | 23774 | 140551 | 190175 | 0 | 179142 | 0 | 0 | 53645 | 35 | 45105 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 42 | 23734 | 118571 | 156188 | 276492 | 0 | 130653 | 1 | 40495 | 9 | 36706 | 2 |
