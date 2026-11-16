# Measures of the cycle run

- Calls in all: 411
- Calls of the orchestrator: 126
- Calls of subagents: 285
- Mean context per call: 212655
- Mean context per call of the orchestrator: 225795
- Share of the context in calls above 200000 tokens: 70.7%
- Context of the orchestrator's first call: 43531
- Context of the orchestrator's middle call: 232264
- Context of the orchestrator's last call: 363893
- Cache written, 5 minutes: 720945
- Cache written, 1 hour: 735696
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 302011
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator c058f437-ab1e-4363-9055-6a9e9c8cba10 | Claude Code | 126 | 43531 | 232264 | 363893 | 0 | 342410 | 0 | 0 | 10592 | 18 | 67470 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 71 | 23814 | 157852 | 227564 | 217215 | 0 | 0 | 0 | 18704 | 11 | 78317 | 3 |
| One author makes the change (the-way-author) | Claude Code | 149 | 23830 | 275079 | 404319 | 0 | 393286 | 0 | 0 | 146527 | 49 | 60678 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 65 | 23808 | 130502 | 212704 | 503730 | 0 | 302011 | 2 | 63420 | 15 | 0 | 0 |
