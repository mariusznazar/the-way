# Measures of the cycle run

- Calls in all: 197
- Calls of the orchestrator: 85
- Calls of subagents: 112
- Mean context per call: 146677
- Mean context per call of the orchestrator: 185154
- Share of the context in calls above 200000 tokens: 34.3%
- Context of the orchestrator's first call: 43935
- Context of the orchestrator's middle call: 198636
- Context of the orchestrator's last call: 265874
- Cache written, 5 minutes: 361951
- Cache written, 1 hour: 419610
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 138028
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 9c2f7bcd-1ba0-4faa-bb51-63dcff56c03c | Claude Code | 85 | 43935 | 198636 | 265874 | 0 | 245616 | 0 | 0 |
| Review merge with target branch (the-way-stage) | Claude Code | 9 | 24011 | 51762 | 60353 | 50004 | 0 | 0 | 0 |
| Author: split-only-for-gain change (the-way-author) | Claude Code | 61 | 24079 | 127787 | 185027 | 0 | 173994 | 0 | 0 |
| Review whole change split-only-for-gain (the-way-stage) | Claude Code | 42 | 24061 | 127093 | 184268 | 311947 | 0 | 138028 | 1 |
