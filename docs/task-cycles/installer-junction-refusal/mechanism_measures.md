# Measures of the cycle run

- Calls in all: 218
- Calls of the orchestrator: 75
- Calls of subagents: 143
- Mean context per call: 151187
- Mean context per call of the orchestrator: 171866
- Share of the context in calls above 200000 tokens: 39.2%
- Context of the orchestrator's first call: 47556
- Context of the orchestrator's middle call: 177095
- Context of the orchestrator's last call: 241892
- Cache written, 5 minutes: 383589
- Cache written, 1 hour: 450444
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 168326
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 0b894027-ee9d-4c30-8e94-4d40d5fdb5ab | Claude Code | 75 | 47556 | 177095 | 241892 | 0 | 221634 | 0 | 0 |
| Review return step commit (the-way-stage) | Claude Code | 19 | 24124 | 55064 | 82969 | 119836 | 0 | 47852 | 1 |
| One author: junction refusal in installer (the-way-author) | Claude Code | 90 | 24154 | 182846 | 239843 | 0 | 228810 | 0 | 0 |
| Review whole change: junction refusal (the-way-stage) | Claude Code | 34 | 24141 | 106084 | 154264 | 263753 | 0 | 120474 | 1 |
