# Measures of the cycle run

- Calls in all: 483
- Calls of the orchestrator: 107
- Calls of subagents: 376
- Mean context per call: 222861
- Mean context per call of the orchestrator: 230955
- Share of the context in calls above 200000 tokens: 75.9%
- Context of the orchestrator's first call: 43667
- Context of the orchestrator's middle call: 227725
- Context of the orchestrator's last call: 353711
- Cache written, 5 minutes: 1053360
- Cache written, 1 hour: 800994
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 469254
- Calls of subagents with a cache write again: 3

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator f11fbba8-1832-4f05-bf20-ede8e7bb2531 | Claude Code | 107 | 43667 | 227725 | 353711 | 0 | 332399 | 0 | 0 | 10278 | 8 | 37087 | 2 |
| Author: audit Q1 contradiction change (the-way-author) | Claude Code | 173 | 23911 | 329133 | 479628 | 0 | 468595 | 0 | 0 | 128706 | 29 | 3071 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 109 | 23929 | 193050 | 294014 | 534208 | 0 | 240196 | 1 | 16475 | 12 | 8499 | 2 |
| Review of correction 1 (the-way-stage) | Claude Code | 60 | 23931 | 129762 | 177447 | 329362 | 0 | 151917 | 1 | 48599 | 7 | 0 | 0 |
| Review of the return step (the-way-stage) | Claude Code | 34 | 23911 | 77920 | 112651 | 189790 | 0 | 77141 | 1 | 11767 | 5 | 0 | 0 |
