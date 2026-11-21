# Measures of the cycle run

- Calls in all: 257
- Calls of the orchestrator: 56
- Calls of subagents: 201
- Mean context per call: 165546
- Mean context per call of the orchestrator: 138428
- Share of the context in calls above 200000 tokens: 44.6%
- Context of the orchestrator's first call: 44633
- Context of the orchestrator's middle call: 140745
- Context of the orchestrator's last call: 189176
- Cache written, 5 minutes: 493327
- Cache written, 1 hour: 457124
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 209243
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator bc1faf0d-ccd5-41c7-a59d-63a7a71fee45 | Claude Code | 56 | 44633 | 140745 | 189176 | 0 | 170281 | 0 | 0 | 14620 | 3 | 0 | 0 |
| One author makes the change (the-way-author) | Claude Code | 119 | 24490 | 204107 | 286845 | 0 | 286843 | 0 | 0 | 60460 | 31 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 77 | 24466 | 174094 | 248159 | 457400 | 0 | 209243 | 1 | 30543 | 10 | 5480 | 2 |
| Agent skills spec frontmatter fields (web-fetch) | Claude Code | 2 | 3876 | 3876 | 14335 | 11748 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Codex SKILL.md frontmatter fields (web-fetch) | Claude Code | 3 | 3965 | 4856 | 24181 | 24179 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
