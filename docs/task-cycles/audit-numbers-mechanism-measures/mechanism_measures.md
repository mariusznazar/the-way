# Measures of the cycle run

- Calls in all: 898
- Calls of the orchestrator: 129
- Calls of subagents: 769
- Mean context per call: 158718
- Mean context per call of the orchestrator: 223769
- Share of the context in calls above 200000 tokens: 47.0%
- Context of the orchestrator's first call: 47012
- Context of the orchestrator's middle call: 225094
- Context of the orchestrator's last call: 358710
- Cache written, 5 minutes: 3747996
- Cache written, 1 hour: 340449
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 460942
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 1ea0e6ed-e19d-442a-92c8-fc967ef95fa1 | Claude Code | 129 | 47012 | 225094 | 358710 | 0 | 340449 | 0 | 0 |
| Write the plan's foundation entries (general-purpose) | Claude Code | 30 | 35512 | 149142 | 192073 | 180184 | 0 | 0 | 0 |
| Review the return step (general-purpose) | Claude Code | 24 | 35543 | 91334 | 116079 | 104190 | 0 | 0 | 0 |
| Review slice 5 (general-purpose) | Claude Code | 20 | 35469 | 94005 | 107999 | 96110 | 0 | 0 | 0 |
| Review slice 6 (general-purpose) | Claude Code | 26 | 35478 | 91148 | 120181 | 229338 | 0 | 109159 | 1 |
| Review slice 7 (general-purpose) | Claude Code | 18 | 35484 | 94412 | 109701 | 97812 | 0 | 0 | 0 |
| Make slice 7: series, medians, comparison (general-purpose) | Claude Code | 41 | 35568 | 178994 | 199659 | 187770 | 0 | 0 | 0 |
| Make slice 1: measures script (general-purpose) | Claude Code | 39 | 35479 | 137474 | 171519 | 171517 | 0 | 0 | 0 |
| Plan the task's change (general-purpose) | Claude Code | 52 | 35491 | 187022 | 297303 | 297301 | 0 | 0 | 0 |
| Review the whole change (general-purpose) | Claude Code | 79 | 35484 | 274976 | 412000 | 751894 | 0 | 351783 | 1 |
| Review slice 1 (general-purpose) | Claude Code | 22 | 35462 | 90240 | 120060 | 120058 | 0 | 0 | 0 |
| Review slice 2 (general-purpose) | Claude Code | 17 | 35455 | 95686 | 109849 | 109847 | 0 | 0 | 0 |
| Fix whole-change review findings (general-purpose) | Claude Code | 94 | 35583 | 136448 | 231706 | 219817 | 0 | 0 | 0 |
| Make slice 2: Codex reading (general-purpose) | Claude Code | 21 | 35484 | 119164 | 146757 | 134868 | 0 | 0 | 0 |
| Make slice 3: gate times script (general-purpose) | Claude Code | 29 | 35474 | 124533 | 152696 | 140807 | 0 | 0 | 0 |
| Make slice 6: audit reads new files (general-purpose) | Claude Code | 74 | 35542 | 191292 | 227180 | 227178 | 0 | 0 | 0 |
| Make slice 4: instruction and template (general-purpose) | Claude Code | 27 | 35469 | 107172 | 123970 | 112081 | 0 | 0 | 0 |
| Make slice 5: cost from either form (general-purpose) | Claude Code | 63 | 35529 | 192711 | 232816 | 232814 | 0 | 0 | 0 |
| Take the return step (general-purpose) | Claude Code | 59 | 35593 | 172078 | 235714 | 223825 | 0 | 0 | 0 |
| Make slice 8: audit session instruction (general-purpose) | Claude Code | 34 | 35557 | 88496 | 110587 | 110585 | 0 | 0 | 0 |
