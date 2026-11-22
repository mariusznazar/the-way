# Measures of the cycle run

- Calls in all: 192
- Calls of the orchestrator: 43
- Calls of subagents: 149
- Mean context per call: 124995
- Mean context per call of the orchestrator: 130403
- Share of the context in calls above 200000 tokens: 0.0%
- Context of the orchestrator's first call: 42620
- Context of the orchestrator's middle call: 135693
- Context of the orchestrator's last call: 191754
- Cache written, 5 minutes: 387749
- Cache written, 1 hour: 362742
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 162856
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 4b94aae0-e9a1-4086-8f7a-2b4338bd9cda | Claude Code | 43 | 42620 | 135693 | 191754 | 0 | 172897 | 0 | 0 | 668 | 3 | 0 | 0 |
| Author of the installer change (the-way-author) | Claude Code | 65 | 24691 | 149181 | 189847 | 0 | 189845 | 0 | 0 | 36540 | 17 | 0 | 0 |
| Review of whole change (the-way-stage) | Claude Code | 69 | 24633 | 123308 | 178455 | 341309 | 0 | 162856 | 1 | 25599 | 12 | 37066 | 2 |
| Review of return step commit (the-way-stage) | Claude Code | 15 | 24633 | 50366 | 57619 | 46440 | 0 | 0 | 0 | 3936 | 2 | 0 | 0 |
