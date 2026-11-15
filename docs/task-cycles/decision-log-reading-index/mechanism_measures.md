# Measures of the cycle run

- Calls in all: 777
- Calls of the orchestrator: 121
- Calls of subagents: 656
- Mean context per call: 158768
- Mean context per call of the orchestrator: 194665
- Share of the context in calls above 200000 tokens: 41.3%
- Context of the orchestrator's first call: 43354
- Context of the orchestrator's middle call: 200912
- Context of the orchestrator's last call: 286995
- Cache written, 5 minutes: 3013095
- Cache written, 1 hour: 266672
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 880535
- Calls of subagents with a cache write again: 4

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 426c81e4-8c78-4ebb-926d-8e0e7991dc4a | Claude Code | 121 | 43354 | 200912 | 286995 | 0 | 266672 | 0 | 0 | 21130 | 23 | 0 | 0 |
| Review the whole change (the-way-stage) | Claude Code | 92 | 23807 | 256847 | 345392 | 634027 | 0 | 299620 | 1 | 123551 | 24 | 68804 | 4 |
| Slice 2: compare script and check (the-way-stage) | Claude Code | 47 | 23739 | 168236 | 191951 | 180966 | 0 | 0 | 0 | 22027 | 7 | 0 | 0 |
| Fix whole-change review findings (the-way-stage) | Claude Code | 63 | 23795 | 141256 | 212865 | 201880 | 0 | 0 | 0 | 55430 | 19 | 362 | 1 |
| Slice 1: decision index script (the-way-stage) | Claude Code | 37 | 23739 | 128429 | 153230 | 153228 | 0 | 0 | 0 | 74247 | 17 | 3720 | 2 |
| Slice 4: reviewer, report, request (the-way-stage) | Claude Code | 22 | 23739 | 105187 | 120661 | 120657 | 0 | 0 | 0 | 26773 | 3 | 0 | 0 |
| Plan decision-log reading change (the-way-stage) | Claude Code | 64 | 23865 | 152667 | 253285 | 253283 | 0 | 0 | 0 | 140062 | 31 | 0 | 0 |
| Review slice 5 (trust boundary) (the-way-stage) | Claude Code | 52 | 23776 | 143550 | 192520 | 357504 | 0 | 164986 | 1 | 37473 | 6 | 0 | 0 |
| Slice 3: reading rule and template (the-way-stage) | Claude Code | 29 | 23741 | 99391 | 118415 | 107430 | 0 | 0 | 0 | 48431 | 11 | 7717 | 3 |
| Slice 5: measure of log in context (the-way-stage) | Claude Code | 109 | 23770 | 167330 | 215624 | 387417 | 0 | 182142 | 1 | 35539 | 12 | 0 | 0 |
| Write foundation entries F1-F10 (the-way-stage) | Claude Code | 91 | 23745 | 180629 | 255665 | 478467 | 0 | 233787 | 1 | 169629 | 85 | 0 | 0 |
| Return step comparison of foundation (the-way-stage) | Claude Code | 50 | 23738 | 107158 | 148585 | 138236 | 0 | 0 | 0 | 56752 | 16 | 466 | 1 |
