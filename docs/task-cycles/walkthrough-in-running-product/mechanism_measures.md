# Measures of the cycle run

- Calls in all: 335
- Calls of the orchestrator: 63
- Calls of subagents: 272
- Mean context per call: 192932
- Mean context per call of the orchestrator: 158062
- Share of the context in calls above 200000 tokens: 70.7%
- Context of the orchestrator's first call: 43578
- Context of the orchestrator's middle call: 163640
- Context of the orchestrator's last call: 219754
- Cache written, 5 minutes: 637567
- Cache written, 1 hour: 508404
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 258901
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 73cc4931-d2ac-479a-8af2-c63fbf047496 | Claude Code | 63 | 43578 | 163640 | 219754 | 0 | 198552 | 0 | 0 | 4458 | 7 | 5143 | 2 |
| Review of the return step (opus) (the-way-stage) | Claude Code | 33 | 23822 | 79731 | 101951 | 90966 | 0 | 0 | 0 | 45049 | 14 | 0 | 0 |
| Author of the whole change (the-way-author) | Claude Code | 166 | 23845 | 233156 | 320885 | 0 | 309852 | 0 | 0 | 84018 | 53 | 72005 | 1 |
| Whole-change review (opus) (the-way-stage) | Claude Code | 73 | 23861 | 223168 | 298049 | 546601 | 0 | 258901 | 1 | 31927 | 16 | 11108 | 2 |
