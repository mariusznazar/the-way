# Measures of the cycle run

- Calls in all: 902
- Calls of the orchestrator: 243
- Calls of subagents: 659
- Mean context per call: 197478
- Mean context per call of the orchestrator: 222003
- Share of the context in calls above 200000 tokens: 68.4%
- Context of the orchestrator's first call: 43389
- Context of the orchestrator's middle call: 162893
- Context of the orchestrator's last call: 386368
- Cache written, 5 minutes: 1749210
- Cache written, 1 hour: 1274798
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 968735
- Calls of subagents with a cache write again: 5

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 1559074a-e15e-41be-8a4d-39f679c2419e | Claude Code | 163 | 43195 | 243935 | 386368 | 0 | 362028 | 0 | 0 | 51931 | 35 | 0 | 0 |
| Recenzja korekty 1 (the-way-stage) | Claude Code | 32 | 23786 | 67818 | 91638 | 80653 | 0 | 0 | 0 | 29771 | 8 | 2701 | 1 |
| Autor korekty 1 (fakt o regule gałęzi) (the-way-author) | Claude Code | 110 | 23842 | 138006 | 209309 | 0 | 198960 | 0 | 0 | 106834 | 26 | 4336 | 1 |
| Recenzja drugiego scalenia z celem (the-way-stage) | Claude Code | 50 | 23788 | 88654 | 110961 | 99976 | 0 | 0 | 0 | 38085 | 4 | 3007 | 1 |
| Recenzja scalenia z gałęzią docelową (the-way-stage) | Claude Code | 109 | 23807 | 143948 | 219380 | 895659 | 0 | 687264 | 4 | 35257 | 16 | 24538 | 1 |
| orchestrator 18447244-14b9-49f0-b45f-ffc03d45a126 | Claude Code | 80 | 43389 | 199280 | 279735 | 0 | 259368 | 0 | 0 | 20313 | 6 | 0 | 0 |
| Author of CI-on-merge-requests change (the-way-author) | Claude Code | 219 | 23804 | 300154 | 464791 | 0 | 454442 | 0 | 0 | 56751 | 34 | 0 | 0 |
| Review of the return step commit (the-way-stage) | Claude Code | 25 | 23716 | 66100 | 77524 | 67175 | 0 | 0 | 0 | 24171 | 10 | 0 | 0 |
| Review of whole change (the-way-stage) | Claude Code | 114 | 23741 | 222213 | 335261 | 605747 | 0 | 281471 | 1 | 241275 | 34 | 0 | 0 |
