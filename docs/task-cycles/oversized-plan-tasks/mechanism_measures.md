# Measures of the cycle run

- Calls in all: 151
- Calls of the orchestrator: 58
- Calls of subagents: 93
- Mean context per call: 106241
- Mean context per call of the orchestrator: 124069
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 43292
- Context of the orchestrator's middle call: 123142
- Context of the orchestrator's last call: 185816
- Cache written, 5 minutes: 198158
- Cache written, 1 hour: 309574
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 94216
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 581fe42d-87bf-41f3-98d6-359680ee2254 | Claude Code | 58 | 43292 | 123142 | 185816 | 0 | 165558 | 0 | 0 |
| Author of oversized-plan-tasks change (the-way-author) | Claude Code | 60 | 24109 | 105173 | 144018 | 0 | 144016 | 0 | 0 |
| Review whole change (the-way-stage) | Claude Code | 33 | 24005 | 92198 | 114291 | 198158 | 0 | 94216 | 1 |
