# Measures of the cycle run

- Calls in all: 414
- Calls of the orchestrator: 128
- Calls of subagents: 286
- Mean context per call: 150992
- Mean context per call of the orchestrator: 158356
- Share of the context in calls above 200000 tokens: 39.4%
- Context of the orchestrator's first call: 47144
- Context of the orchestrator's middle call: 233724
- Context of the orchestrator's last call: 202112
- Cache written, 5 minutes: 1244290
- Cache written, 1 hour: 406377
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 490865
- Calls of subagents with a cache write again: 3

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 74cb4adf-a7bb-4219-8069-9e18b8fdc041 | Claude Code | 70 | 47144 | 177070 | 243853 | 0 | 225364 | 0 | 0 |
| One author makes the change (general-purpose) | Claude Code | 124 | 35648 | 225257 | 286851 | 544688 | 0 | 257839 | 1 |
| Review of the whole change (general-purpose) | Claude Code | 58 | 35712 | 137711 | 191181 | 328616 | 0 | 149314 | 1 |
| orchestrator d0bcc7ef-db77-46e6-8c08-87e6b6618829 | Claude Code | 58 | 46165 | 139680 | 202112 | 0 | 181013 | 0 | 0 |
| Review correction 1 of PR 107 (general-purpose) | Claude Code | 15 | 35638 | 67549 | 80532 | 68653 | 0 | 0 | 0 |
| Review merge of target branch into PR 107 (general-purpose) | Claude Code | 45 | 35670 | 97180 | 129379 | 117500 | 0 | 0 | 0 |
| Author of correction 1 for PR 107 (general-purpose) | Claude Code | 44 | 35601 | 87733 | 113000 | 184833 | 0 | 83712 | 1 |
