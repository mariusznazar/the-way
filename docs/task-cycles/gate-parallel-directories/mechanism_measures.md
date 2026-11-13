# Measures of the cycle run

- Calls in all: 233
- Calls of the orchestrator: 49
- Calls of subagents: 184
- Mean context per call: 175896
- Mean context per call of the orchestrator: 139234
- Share of the context in calls above 200000 tokens: 48.4%
- Context of the orchestrator's first call: 47197
- Context of the orchestrator's middle call: 143645
- Context of the orchestrator's last call: 193026
- Cache written, 5 minutes: 1119537
- Cache written, 1 hour: 172768
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 568498
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 922dc11d-4cb5-4618-a7b8-a587a7f12f4c | Claude Code | 49 | 47197 | 143645 | 193026 | 0 | 172768 | 0 | 0 |
| Review the whole change (general-purpose) | Claude Code | 63 | 35840 | 137363 | 239885 | 228006 | 0 | 0 | 0 |
| One author makes the change (general-purpose) | Claude Code | 121 | 35795 | 221934 | 323035 | 891531 | 0 | 568498 | 2 |
