# Measures of the cycle run

- Calls in all: 1677
- Calls of the orchestrator: 198
- Calls of subagents: 1479
- Mean context per call: 155986
- Mean context per call of the orchestrator: 271635
- Share of the context in calls above 200000 tokens: 54.0%
- Context of the orchestrator's first call: 43348
- Context of the orchestrator's middle call: 282095
- Context of the orchestrator's last call: 405011
- Cache written, 5 minutes: 5520199
- Cache written, 1 hour: 382250
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 528269
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 038d1f4f-1524-4537-8b75-d65fae2784fd | Claude Code | 198 | 43348 | 282095 | 405011 | 0 | 382250 | 0 | 0 | 4456 | 7 | 4465 | 2 |
| Executor of slice 19 (the-way-stage) | Claude Code | 46 | 23860 | 100240 | 168515 | 157530 | 0 | 0 | 0 | 58312 | 9 | 0 | 0 |
| Executor of slice 9 (the-way-stage) | Claude Code | 28 | 23860 | 119702 | 150135 | 263511 | 0 | 113378 | 1 | 2408 | 2 | 0 | 0 |
| Fix of the whole-change findings (the-way-stage) | Claude Code | 114 | 23880 | 124678 | 184829 | 173844 | 0 | 0 | 0 | 5082 | 4 | 0 | 0 |
| Executor of slice 3 (the-way-stage) | Claude Code | 34 | 23860 | 137078 | 160329 | 149344 | 0 | 0 | 0 | 17330 | 6 | 0 | 0 |
| Planner of the guidelines task (the-way-stage) | Claude Code | 68 | 23887 | 229961 | 383247 | 372898 | 0 | 0 | 0 | 7466 | 10 | 65019 | 2 |
| Executor of slice 18 (the-way-stage) | Claude Code | 31 | 23860 | 114294 | 145067 | 134082 | 0 | 0 | 0 | 39409 | 8 | 0 | 0 |
| Review of the whole change (restart) (the-way-stage) | Claude Code | 174 | 23899 | 335913 | 469041 | 872947 | 0 | 414891 | 1 | 17886 | 5 | 45811 | 3 |
| Executor of slice 8 (the-way-stage) | Claude Code | 63 | 23862 | 107164 | 131239 | 120254 | 0 | 0 | 0 | 31336 | 5 | 0 | 0 |
| Executor of slice 1 (the-way-stage) | Claude Code | 40 | 23860 | 126170 | 162967 | 162965 | 0 | 0 | 0 | 27611 | 6 | 0 | 0 |
| Executor of slice 17 (the-way-stage) | Claude Code | 27 | 23860 | 83401 | 115368 | 104383 | 0 | 0 | 0 | 26051 | 6 | 0 | 0 |
| The return step (the-way-stage) | Claude Code | 82 | 23848 | 167443 | 279582 | 268597 | 0 | 0 | 0 | 88862 | 18 | 0 | 0 |
| Review of slice 11 (the-way-stage) | Claude Code | 9 | 23852 | 46796 | 52875 | 41890 | 0 | 0 | 0 | 247 | 1 | 0 | 0 |
| Executor of slice 16 (the-way-stage) | Claude Code | 16 | 23862 | 59290 | 76352 | 66003 | 0 | 0 | 0 | 15921 | 3 | 0 | 0 |
| Review of slice 2 (the-way-stage) | Claude Code | 10 | 23852 | 49791 | 61667 | 51318 | 0 | 0 | 0 | 4333 | 2 | 0 | 0 |
| Review of slice 8 (the-way-stage) | Claude Code | 15 | 23852 | 53817 | 62819 | 51834 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Review of slice 5 (the-way-stage) | Claude Code | 12 | 23890 | 49585 | 60016 | 49031 | 0 | 0 | 0 | 246 | 1 | 0 | 0 |
| Review of slice 6 (the-way-stage) | Claude Code | 15 | 23852 | 72159 | 84621 | 73636 | 0 | 0 | 0 | 5228 | 4 | 0 | 0 |
| Executor of slice 7 (the-way-stage) | Claude Code | 49 | 23860 | 96313 | 130222 | 119237 | 0 | 0 | 0 | 11620 | 3 | 0 | 0 |
| Review of slice 4 (the-way-stage) | Claude Code | 36 | 23852 | 65841 | 112436 | 101451 | 0 | 0 | 0 | 30141 | 6 | 0 | 0 |
| Executor of slice 15 (the-way-stage) | Claude Code | 23 | 23860 | 72095 | 83972 | 72987 | 0 | 0 | 0 | 27127 | 6 | 0 | 0 |
| Executor of slice 2 (the-way-stage) | Claude Code | 27 | 23860 | 90735 | 116707 | 105722 | 0 | 0 | 0 | 25688 | 5 | 0 | 0 |
| Executor of slice 20 (the-way-stage) | Claude Code | 36 | 23860 | 137045 | 169485 | 158500 | 0 | 0 | 0 | 29381 | 8 | 0 | 0 |
| Executor of slice 23 (the-way-stage) | Claude Code | 21 | 23915 | 68404 | 85240 | 85238 | 0 | 0 | 0 | 14414 | 5 | 0 | 0 |
| Executor of slice 21 (the-way-stage) | Claude Code | 39 | 23862 | 124162 | 153004 | 142655 | 0 | 0 | 0 | 97989 | 11 | 0 | 0 |
| Review of the return step (the-way-stage) | Claude Code | 22 | 23848 | 78601 | 100410 | 89425 | 0 | 0 | 0 | 35629 | 7 | 0 | 0 |
| Executor of slice 6 (the-way-stage) | Claude Code | 31 | 23862 | 99477 | 119245 | 108260 | 0 | 0 | 0 | 16684 | 7 | 0 | 0 |
| Executor of slice 5 (the-way-stage) | Claude Code | 32 | 23860 | 64753 | 90896 | 90894 | 0 | 0 | 0 | 9281 | 4 | 0 | 0 |
| Write the plan's foundation entries (the-way-stage) | Claude Code | 97 | 23850 | 282906 | 418445 | 407460 | 0 | 0 | 0 | 167731 | 33 | 9429 | 2 |
| Executor of slice 13 (the-way-stage) | Claude Code | 62 | 23860 | 121371 | 155172 | 144187 | 0 | 0 | 0 | 10953 | 5 | 0 | 0 |
| Executor of slice 14 (the-way-stage) | Claude Code | 23 | 23860 | 69301 | 88958 | 77973 | 0 | 0 | 0 | 24759 | 5 | 0 | 0 |
| Executor of slice 11 (the-way-stage) | Claude Code | 29 | 23860 | 65688 | 86268 | 75283 | 0 | 0 | 0 | 10650 | 2 | 0 | 0 |
| Executor of slice 4 (the-way-stage) | Claude Code | 61 | 23862 | 103597 | 153814 | 143465 | 0 | 0 | 0 | 25597 | 4 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 26 | 23860 | 119936 | 187587 | 176602 | 0 | 0 | 0 | 6220 | 2 | 85676 | 3 |
| Executor of slice 22 (the-way-stage) | Claude Code | 25 | 23873 | 110368 | 144275 | 133290 | 0 | 0 | 0 | 91460 | 12 | 0 | 0 |
| Executor of slice 12 (the-way-stage) | Claude Code | 25 | 23860 | 79628 | 92341 | 81356 | 0 | 0 | 0 | 9817 | 6 | 0 | 0 |
| Executor of slice 10 (the-way-stage) | Claude Code | 31 | 23860 | 85434 | 103132 | 92147 | 0 | 0 | 0 | 25319 | 4 | 0 | 0 |
