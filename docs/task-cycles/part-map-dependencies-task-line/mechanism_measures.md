# Measures of the cycle run

- Calls in all: 221
- Calls of the orchestrator: 51
- Calls of subagents: 170
- Mean context per call: 184142
- Mean context per call of the orchestrator: 144179
- Share of the context in calls above 200000 tokens: 60.7%
- Context of the orchestrator's first call: 43382
- Context of the orchestrator's middle call: 150820
- Context of the orchestrator's last call: 208702
- Cache written, 5 minutes: 233926
- Cache written, 1 hour: 505387
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 0
- Calls of subagents with a cache write again: 0

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 777280c9-9741-4f22-86df-3621b2ac7c7d | Claude Code | 51 | 43382 | 150820 | 208702 | 0 | 186946 | 0 | 0 | 2045 | 4 | 46666 | 2 |
| Review whole change (the-way-stage) | Claude Code | 77 | 23749 | 153546 | 244275 | 233926 | 0 | 0 | 0 | 101770 | 18 | 67659 | 3 |
| Author: part map deps and task line (the-way-author) | Claude Code | 93 | 23767 | 246777 | 331648 | 0 | 318441 | 0 | 0 | 91009 | 42 | 40174 | 1 |
