# Measures of the cycle run

- Calls in all: 342
- Calls of the orchestrator: 67
- Calls of subagents: 275
- Mean context per call: 191742
- Mean context per call of the orchestrator: 144568
- Share of the context in calls above 200000 tokens: 64.5%
- Context of the orchestrator's first call: 43555
- Context of the orchestrator's middle call: 140503
- Context of the orchestrator's last call: 206850
- Cache written, 5 minutes: 652850
- Cache written, 1 hour: 520589
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 256649
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 0673e475-e1c3-433e-8f0b-b2ef981be4c3 | Claude Code | 67 | 43555 | 140503 | 206850 | 0 | 186509 | 0 | 0 | 9971 | 7 | 2487 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 30 | 23772 | 82744 | 108796 | 108794 | 0 | 0 | 0 | 34280 | 9 | 0 | 0 |
| Author of the small-fixes change (the-way-author) | Claude Code | 154 | 23862 | 246596 | 345113 | 0 | 334080 | 0 | 0 | 113607 | 45 | 66959 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 91 | 23781 | 201667 | 287409 | 544056 | 0 | 256649 | 1 | 76783 | 13 | 10472 | 2 |
