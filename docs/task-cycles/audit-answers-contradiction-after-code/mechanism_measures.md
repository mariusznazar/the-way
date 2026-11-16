# Measures of the cycle run

- Calls in all: 304
- Calls of the orchestrator: 62
- Calls of subagents: 242
- Mean context per call: 216101
- Mean context per call of the orchestrator: 171820
- Share of the context in calls above 200000 tokens: 75.7%
- Context of the orchestrator's first call: 43667
- Context of the orchestrator's middle call: 175222
- Context of the orchestrator's last call: 260818
- Cache written, 5 minutes: 534208
- Cache written, 1 hour: 640737
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 240196
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator f11fbba8-1832-4f05-bf20-ede8e7bb2531 | Claude Code | 62 | 43667 | 175222 | 260818 | 0 | 240435 | 0 | 0 | 9367 | 5 | 37087 | 2 |
| Author: audit Q1 contradiction change (the-way-author) | Claude Code | 133 | 23911 | 279815 | 411335 | 0 | 400302 | 0 | 0 | 114665 | 21 | 3071 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 109 | 23929 | 193050 | 294014 | 534208 | 0 | 240196 | 1 | 16475 | 12 | 8499 | 2 |
