# Measures of the cycle run

- Calls in all: 264
- Calls of the orchestrator: 62
- Calls of subagents: 202
- Mean context per call: 161164
- Mean context per call of the orchestrator: 145171
- Share of the context in calls above 200000 tokens: 36.0%
- Context of the orchestrator's first call: 43382
- Context of the orchestrator's middle call: 153495
- Context of the orchestrator's last call: 199524
- Cache written, 5 minutes: 415718
- Cache written, 1 hour: 470935
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 176043
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator a73c4ad5-ce29-4378-9d67-245e48598da4 | Claude Code | 62 | 43382 | 153495 | 199524 | 0 | 178729 | 0 | 0 | 10956 | 5 | 4107 | 2 |
| Review of the return step (the-way-stage) | Claude Code | 17 | 23750 | 55994 | 62533 | 51548 | 0 | 0 | 0 | 14583 | 4 | 0 | 0 |
| One author: weak point in questions (the-way-author) | Claude Code | 112 | 23808 | 221560 | 292208 | 0 | 292206 | 0 | 0 | 130806 | 49 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 73 | 23752 | 155848 | 199112 | 364170 | 0 | 176043 | 1 | 69515 | 15 | 69479 | 3 |
