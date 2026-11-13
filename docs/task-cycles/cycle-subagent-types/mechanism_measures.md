# Measures of the cycle run

- Calls in all: 317
- Calls of the orchestrator: 63
- Calls of subagents: 254
- Mean context per call: 244218
- Mean context per call of the orchestrator: 150790
- Share of the context in calls above 200000 tokens: 76.4%
- Context of the orchestrator's first call: 47198
- Context of the orchestrator's middle call: 162329
- Context of the orchestrator's last call: 218703
- Cache written, 5 minutes: 1326039
- Cache written, 1 hour: 198445
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 548575
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 1e39933f-4c26-427e-be30-00e812d5a036 | Claude Code | 63 | 47198 | 162329 | 218703 | 0 | 198445 | 0 | 0 |
| Review the whole change (general-purpose) | Claude Code | 49 | 35776 | 149509 | 210057 | 365566 | 0 | 167388 | 1 |
| Author the whole change (general-purpose) | Claude Code | 183 | 35766 | 343166 | 481366 | 862551 | 0 | 381187 | 1 |
| Review the return step commit (general-purpose) | Claude Code | 22 | 35832 | 84106 | 109801 | 97922 | 0 | 0 | 0 |
