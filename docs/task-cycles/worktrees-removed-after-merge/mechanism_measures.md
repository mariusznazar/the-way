# Measures of the cycle run

- Calls in all: 294
- Calls of the orchestrator: 71
- Calls of subagents: 223
- Mean context per call: 203494
- Mean context per call of the orchestrator: 156465
- Share of the context in calls above 200000 tokens: 64.1%
- Context of the orchestrator's first call: 43362
- Context of the orchestrator's middle call: 169848
- Context of the orchestrator's last call: 218472
- Cache written, 5 minutes: 581294
- Cache written, 1 hour: 595791
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 271884
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 9f279531-6ffd-4144-9e07-ff0d73fa3bfe | Claude Code | 71 | 43362 | 169848 | 218472 | 0 | 198214 | 0 | 0 |
| Review of the return step (the-way-stage) | Claude Code | 24 | 23750 | 74825 | 95945 | 163303 | 0 | 78343 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 66 | 23766 | 158635 | 234799 | 417991 | 0 | 193541 | 1 |
| Author: worktree cleanup script (the-way-author) | Claude Code | 133 | 23807 | 304310 | 408610 | 0 | 397577 | 0 | 0 |
