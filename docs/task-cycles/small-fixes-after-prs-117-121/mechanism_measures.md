# Measures of the cycle run

- Calls in all: 435
- Calls of the orchestrator: 124
- Calls of subagents: 311
- Mean context per call: 215522
- Mean context per call of the orchestrator: 206787
- Share of the context in calls above 200000 tokens: 75.2%
- Context of the orchestrator's first call: 43555
- Context of the orchestrator's middle call: 202851
- Context of the orchestrator's last call: 321934
- Cache written, 5 minutes: 970019
- Cache written, 1 hour: 662819
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 544056
- Calls of subagents with a cache write again: 2

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator 0673e475-e1c3-433e-8f0b-b2ef981be4c3 | Claude Code | 124 | 43555 | 202851 | 321934 | 0 | 298594 | 0 | 0 | 16027 | 15 | 2487 | 1 |
| Review of the return step (the-way-stage) | Claude Code | 30 | 23772 | 82744 | 108796 | 108794 | 0 | 0 | 0 | 34280 | 9 | 0 | 0 |
| Author of the small-fixes change (the-way-author) | Claude Code | 176 | 23862 | 260298 | 375258 | 0 | 364225 | 0 | 0 | 121831 | 52 | 66959 | 1 |
| Review of the whole change (the-way-stage) | Claude Code | 105 | 23781 | 207340 | 317171 | 861225 | 0 | 544056 | 2 | 92401 | 20 | 10472 | 2 |
