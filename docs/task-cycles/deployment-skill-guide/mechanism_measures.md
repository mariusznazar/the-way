# Measures of the cycle run

- Calls in all: 303
- Calls of the orchestrator: 112
- Calls of subagents: 191
- Mean context per call: 153747
- Mean context per call of the orchestrator: 174529
- Share of the context in calls above 200000 tokens: 38.2%
- Context of the orchestrator's first call: 43267
- Context of the orchestrator's middle call: 179196
- Context of the orchestrator's last call: 260812
- Cache written, 5 minutes: 602054
- Cache written, 1 hour: 671142
- Cache written again by the orchestrator: 208283
- Calls of the orchestrator with a cache write again: 1
- Cache written again by subagents: 321596
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator e5f1bf51-f799-4991-8c45-1a10cdd3be91 | Claude Code | 112 | 43267 | 179196 | 260812 | 0 | 448835 | 208283 | 1 |
| Review merge with target branch (the-way-stage) | Claude Code | 25 | 24087 | 79982 | 101805 | 91456 | 0 | 0 | 0 |
| Review whole change (the-way-stage) | Claude Code | 80 | 23993 | 152200 | 199987 | 510598 | 0 | 321596 | 2 |
| One author of deployment-skill guide (the-way-author) | Claude Code | 86 | 24090 | 163688 | 232656 | 0 | 222307 | 0 | 0 |
