# Measures of the cycle run

- Calls in all: 715
- Calls of the orchestrator: 168
- Calls of subagents: 547
- Mean context per call: 192439
- Mean context per call of the orchestrator: 173053
- Share of the context in calls above 200000 tokens: 67.1%
- Context of the orchestrator's first call: 43389
- Context of the orchestrator's middle call: 70452
- Context of the orchestrator's last call: 247743
- Cache written, 5 minutes: 1244173
- Cache written, 1 hour: 1077090
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 591939
- Calls of subagents with a cache write again: 3

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 1559074a-e15e-41be-8a4d-39f679c2419e | Claude Code | 88 | 43195 | 168633 | 247743 | 0 | 227302 | 0 | 0 | 48769 | 31 | 0 | 0 |
| Recenzja korekty 1 (the-way-stage) | Claude Code | 32 | 23786 | 67818 | 91638 | 80653 | 0 | 0 | 0 | 29771 | 8 | 2701 | 1 |
| Autor korekty 1 (fakt o regule gałęzi) (the-way-author) | Claude Code | 68 | 23842 | 103784 | 146327 | 0 | 135978 | 0 | 0 | 76305 | 17 | 0 | 0 |
| Recenzja scalenia z gałęzią docelową (the-way-stage) | Claude Code | 89 | 23807 | 126301 | 191115 | 490598 | 0 | 310468 | 2 | 35034 | 15 | 24538 | 1 |
| orchestrator 18447244-14b9-49f0-b45f-ffc03d45a126 | Claude Code | 80 | 43389 | 199280 | 279735 | 0 | 259368 | 0 | 0 | 20313 | 6 | 0 | 0 |
| Author of CI-on-merge-requests change (the-way-author) | Claude Code | 219 | 23804 | 300154 | 464791 | 0 | 454442 | 0 | 0 | 56751 | 34 | 0 | 0 |
| Review of the return step commit (the-way-stage) | Claude Code | 25 | 23716 | 66100 | 77524 | 67175 | 0 | 0 | 0 | 24171 | 10 | 0 | 0 |
| Review of whole change (the-way-stage) | Claude Code | 114 | 23741 | 222213 | 335261 | 605747 | 0 | 281471 | 1 | 241275 | 34 | 0 | 0 |
