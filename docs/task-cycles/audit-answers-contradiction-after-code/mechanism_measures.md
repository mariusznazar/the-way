# Measures of the cycle run

- Calls in all: 925
- Calls of the orchestrator: 232
- Calls of subagents: 693
- Mean context per call: 182870
- Mean context per call of the orchestrator: 212177
- Share of the context in calls above 200000 tokens: 60.0%
- Context of the orchestrator's first call: 43667
- Context of the orchestrator's middle call: 369855
- Context of the orchestrator's last call: 258320
- Cache written, 5 minutes: 1764834
- Cache written, 1 hour: 1308360
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 682845
- Calls of subagents with a cache write again: 5

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 9f7eaed7-7f7c-4eb2-b044-65293d8e42ed | Claude Code | 111 | 43437 | 182587 | 258320 | 0 | 237932 | 0 | 0 | 15939 | 16 | 0 | 0 |
| Review renumbering and second merge (the-way-stage) | Claude Code | 41 | 23842 | 85244 | 105849 | 94864 | 0 | 0 | 0 | 38930 | 8 | 0 | 0 |
| Review correction 2 (the-way-stage) | Claude Code | 54 | 23859 | 102842 | 155175 | 253080 | 0 | 108890 | 1 | 24864 | 6 | 0 | 0 |
| Review return step (the-way-stage) | Claude Code | 72 | 23860 | 110552 | 153182 | 246898 | 0 | 104701 | 1 | 21889 | 9 | 0 | 0 |
| Author correction 2 (the-way-author) | Claude Code | 96 | 23952 | 158383 | 247529 | 0 | 236496 | 0 | 0 | 67503 | 26 | 0 | 0 |
| Review merge of target branch (the-way-stage) | Claude Code | 54 | 23853 | 102912 | 126981 | 116632 | 0 | 0 | 0 | 1347 | 3 | 0 | 0 |
| orchestrator f11fbba8-1832-4f05-bf20-ede8e7bb2531 | Claude Code | 121 | 43667 | 258328 | 386649 | 0 | 365337 | 0 | 0 | 10520 | 9 | 37087 | 2 |
| Author: audit Q1 contradiction change (the-way-author) | Claude Code | 173 | 23911 | 329133 | 479628 | 0 | 468595 | 0 | 0 | 128706 | 29 | 3071 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 109 | 23929 | 193050 | 294014 | 534208 | 0 | 240196 | 1 | 16475 | 12 | 8499 | 2 |
| Review of correction 1 (the-way-stage) | Claude Code | 60 | 23931 | 129762 | 177447 | 329362 | 0 | 151917 | 1 | 48599 | 7 | 0 | 0 |
| Review of the return step (the-way-stage) | Claude Code | 34 | 23911 | 77920 | 112651 | 189790 | 0 | 77141 | 1 | 11767 | 5 | 0 | 0 |
