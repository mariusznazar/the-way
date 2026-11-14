# Measures of the cycle run

- Calls in all: 243
- Calls of the orchestrator: 110
- Calls of subagents: 133
- Mean context per call: 154181
- Mean context per call of the orchestrator: 207514
- Share of the context in calls above 200000 tokens: 45.3%
- Context of the orchestrator's first call: 43935
- Context of the orchestrator's middle call: 212518
- Context of the orchestrator's last call: 312059
- Cache written, 5 minutes: 455945
- Cache written, 1 hour: 465795
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 138028
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 9c2f7bcd-1ba0-4faa-bb51-63dcff56c03c | Claude Code | 110 | 43935 | 212518 | 312059 | 0 | 291801 | 0 | 0 |
| Correction 1: read nine unread decisions (the-way-stage) | Claude Code | 21 | 24048 | 77919 | 104343 | 93994 | 0 | 0 | 0 |
| Review merge with target branch (the-way-stage) | Claude Code | 9 | 24011 | 51762 | 60353 | 50004 | 0 | 0 | 0 |
| Author: split-only-for-gain change (the-way-author) | Claude Code | 61 | 24079 | 127787 | 185027 | 0 | 173994 | 0 | 0 |
| Review whole change split-only-for-gain (the-way-stage) | Claude Code | 42 | 24061 | 127093 | 184268 | 311947 | 0 | 138028 | 1 |
