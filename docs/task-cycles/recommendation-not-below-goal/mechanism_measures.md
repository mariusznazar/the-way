# Measures of the cycle run

- Calls in all: 261
- Calls of the orchestrator: 90
- Calls of subagents: 171
- Mean context per call: 143561
- Mean context per call of the orchestrator: 192243
- Share of the context in calls above 200000 tokens: 31.2%
- Context of the orchestrator's first call: 43417
- Context of the orchestrator's middle call: 199374
- Context of the orchestrator's last call: 311952
- Cache written, 5 minutes: 500412
- Cache written, 1 hour: 487434
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 177204
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator b4ff38e1-93f8-45a1-8e5d-202afef9cf3d | Claude Code | 90 | 43417 | 199374 | 311952 | 0 | 292929 | 0 | 0 | 29815 | 17 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 31 | 24816 | 97592 | 134388 | 123043 | 0 | 0 | 0 | 62577 | 17 | 32952 | 3 |
| Author of the change (the-way-author) | Claude Code | 78 | 24873 | 125290 | 194507 | 0 | 194505 | 0 | 0 | 83555 | 48 | 0 | 0 |
| Second review of whole change (the-way-stage) | Claude Code | 62 | 24816 | 119432 | 200167 | 377369 | 0 | 177204 | 1 | 80226 | 22 | 51093 | 2 |
