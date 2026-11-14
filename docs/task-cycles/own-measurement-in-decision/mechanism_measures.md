# Measures of the cycle run

- Calls in all: 158
- Calls of the orchestrator: 37
- Calls of subagents: 121
- Mean context per call: 130972
- Mean context per call of the orchestrator: 124255
- Share of the context in calls above 200000 tokens: 17.1%
- Context of the orchestrator's first call: 47547
- Context of the orchestrator's middle call: 127079
- Context of the orchestrator's last call: 169637
- Cache written, 5 minutes: 118177
- Cache written, 1 hour: 368015
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 45239487-7cb1-4f75-9374-fbf9b57bd5b1 | Claude Code | 37 | 47547 | 127079 | 169637 | 0 | 149379 | 0 | 0 |
| Review whole change (the-way-stage) | Claude Code | 38 | 24165 | 82701 | 128526 | 118177 | 0 | 0 | 0 |
| One author: own measurement in decisions (the-way-author) | Claude Code | 83 | 24211 | 171026 | 218638 | 0 | 218636 | 0 | 0 |
