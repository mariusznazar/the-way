# Measures of the cycle run

- Calls in all: 252
- Calls of the orchestrator: 67
- Calls of subagents: 185
- Mean context per call: 128356
- Mean context per call of the orchestrator: 146534
- Share of the context in calls above 200000 tokens: 11.5%
- Context of the orchestrator's first call: 44025
- Context of the orchestrator's middle call: 147446
- Context of the orchestrator's last call: 221257
- Cache written, 5 minutes: 520958
- Cache written, 1 hour: 396107
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 151213
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 3accdae2-e092-4074-bed5-ead4d6ab0967 | Claude Code | 67 | 44025 | 147446 | 221257 | 0 | 200999 | 0 | 0 |
| One author makes the change (the-way-author) | Claude Code | 89 | 24082 | 142028 | 205457 | 0 | 195108 | 0 | 0 |
| Review of the return step (the-way-stage) | Claude Code | 7 | 24077 | 46619 | 63738 | 52753 | 0 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 50 | 24070 | 116315 | 176537 | 317401 | 0 | 151213 | 1 |
| Fresh reviewer reads what stayed unread (the-way-stage) | Claude Code | 39 | 24077 | 99876 | 161789 | 150804 | 0 | 0 | 0 |
