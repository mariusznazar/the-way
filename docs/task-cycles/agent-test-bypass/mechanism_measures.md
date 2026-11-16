# Measures of the cycle run

- Calls in all: 464
- Calls of the orchestrator: 151
- Calls of subagents: 313
- Mean context per call: 230621
- Mean context per call of the orchestrator: 252286
- Share of the context in calls above 200000 tokens: 76.1%
- Context of the orchestrator's first call: 43531
- Context of the orchestrator's middle call: 264708
- Context of the orchestrator's last call: 405043
- Cache written, 5 minutes: 938111
- Cache written, 1 hour: 805522
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 503730
- Calls of subagents with a cache write again: 3

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator c058f437-ab1e-4363-9055-6a9e9c8cba10 | Claude Code | 151 | 43531 | 264708 | 405043 | 0 | 382191 | 0 | 0 | 10984 | 20 | 67470 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 71 | 23814 | 157852 | 227564 | 217215 | 0 | 0 | 0 | 18704 | 11 | 78317 | 3 |
| One author makes the change (the-way-author) | Claude Code | 168 | 23830 | 295181 | 434364 | 0 | 423331 | 0 | 0 | 158618 | 55 | 60678 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 74 | 23808 | 148251 | 228151 | 720896 | 0 | 503730 | 3 | 63636 | 16 | 0 | 0 |
