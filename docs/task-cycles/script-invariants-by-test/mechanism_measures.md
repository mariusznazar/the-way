# Measures of the cycle run

- Calls in all: 219
- Calls of the orchestrator: 64
- Calls of subagents: 155
- Mean context per call: 151831
- Mean context per call of the orchestrator: 161902
- Share of the context in calls above 200000 tokens: 33.8%
- Context of the orchestrator's first call: 44220
- Context of the orchestrator's middle call: 162801
- Context of the orchestrator's last call: 253010
- Cache written, 5 minutes: 296331
- Cache written, 1 hour: 457944
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 33e16c15-ab7f-43d2-9373-c99401ce69af | Claude Code | 64 | 44220 | 162801 | 253010 | 0 | 230786 | 0 | 0 | 1671 | 4 | 52906 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 63 | 23820 | 164772 | 228896 | 217911 | 0 | 0 | 0 | 63254 | 9 | 41887 | 2 |
| Review of the return step (the-way-stage) | Claude Code | 20 | 23792 | 68210 | 89405 | 78420 | 0 | 0 | 0 | 21409 | 4 | 0 | 0 |
| One author: invariant tests (the-way-author) | Claude Code | 72 | 23847 | 174443 | 238191 | 0 | 227158 | 0 | 0 | 16993 | 3 | 0 | 0 |
