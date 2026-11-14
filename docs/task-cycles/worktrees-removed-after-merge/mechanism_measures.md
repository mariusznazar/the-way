# Measures of the cycle run

- Calls in all: 356
- Calls of the orchestrator: 118
- Calls of subagents: 238
- Mean context per call: 219300
- Mean context per call of the orchestrator: 209373
- Share of the context in calls above 200000 tokens: 71.9%
- Context of the orchestrator's first call: 43362
- Context of the orchestrator's middle call: 200295
- Context of the orchestrator's last call: 330408
- Cache written, 5 minutes: 677015
- Cache written, 1 hour: 717953
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 357480
- Calls of subagents with a cache write again: 3

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 9f279531-6ffd-4144-9e07-ff0d73fa3bfe | Claude Code | 118 | 43362 | 200295 | 330408 | 0 | 310150 | 0 | 0 |
| Review of the return step (the-way-stage) | Claude Code | 29 | 23750 | 81951 | 106070 | 259024 | 0 | 163939 | 2 |
| Review of the whole change (the-way-stage) | Claude Code | 66 | 23766 | 158635 | 234799 | 417991 | 0 | 193541 | 1 |
| Author: worktree cleanup script (the-way-author) | Claude Code | 143 | 23807 | 310960 | 418836 | 0 | 407803 | 0 | 0 |
