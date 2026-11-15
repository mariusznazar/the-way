# Measures of the cycle run

- Calls in all: 221
- Calls of the orchestrator: 104
- Calls of subagents: 117
- Mean context per call: 148745
- Mean context per call of the orchestrator: 171162
- Share of the context in calls above 200000 tokens: 27.4%
- Context of the orchestrator's first call: 43425
- Context of the orchestrator's middle call: 167393
- Context of the orchestrator's last call: 264736
- Cache written, 5 minutes: 429017
- Cache written, 1 hour: 430688
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 276492
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 397f5de7-5d0a-4193-9103-86ff4b0cf1c1 | Claude Code | 104 | 43425 | 167393 | 264736 | 0 | 241783 | 0 | 0 | 20895 | 11 | 6535 | 1 |
| One author makes the change (the-way-author) | Claude Code | 71 | 23774 | 144541 | 199938 | 0 | 188905 | 0 | 0 | 62671 | 45 | 45105 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 46 | 23734 | 122030 | 162874 | 429017 | 0 | 276492 | 2 | 41371 | 11 | 36706 | 2 |
