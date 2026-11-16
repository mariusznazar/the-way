# Measures of the cycle run

- Calls in all: 439
- Calls of the orchestrator: 98
- Calls of subagents: 341
- Mean context per call: 252233
- Mean context per call of the orchestrator: 185024
- Share of the context in calls above 200000 tokens: 78.8%
- Context of the orchestrator's first call: 43600
- Context of the orchestrator's middle call: 174949
- Context of the orchestrator's last call: 293808
- Cache written, 5 minutes: 554279
- Cache written, 1 hour: 811609
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 601c0a77-f5eb-4452-98ee-05fd086bbaad | Claude Code | 98 | 43600 | 174949 | 293808 | 0 | 270182 | 0 | 0 | 18922 | 15 | 1333 | 1 |
| Author of the whole change (the-way-author) | Claude Code | 185 | 23943 | 391752 | 541429 | 0 | 541427 | 0 | 0 | 254171 | 128 | 75309 | 1 |
| Review of correction 1 and reading (the-way-stage) | Claude Code | 59 | 23927 | 155559 | 235259 | 224910 | 0 | 0 | 0 | 79450 | 22 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 97 | 23888 | 211409 | 339718 | 329369 | 0 | 0 | 0 | 165700 | 36 | 9058 | 2 |
