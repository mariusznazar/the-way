# Measures of the cycle run

- Calls in all: 329
- Calls of the orchestrator: 93
- Calls of subagents: 236
- Mean context per call: 169663
- Mean context per call of the orchestrator: 179539
- Share of the context in calls above 200000 tokens: 53.6%
- Context of the orchestrator's first call: 44633
- Context of the orchestrator's middle call: 179480
- Context of the orchestrator's last call: 271289
- Cache written, 5 minutes: 589680
- Cache written, 1 hour: 554224
- Cache written again by the orchestrator: 0
- Calls of the orchestrator with a cache write again: 0
- Cache written again by subagents: 209243
- Calls of subagents with a cache write again: 1

## Agents

| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes | Cache written, 1 hour | Cache written again | Calls with a cache write again | Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrator bc1faf0d-ccd5-41c7-a59d-63a7a71fee45 | Claude Code | 93 | 44633 | 179480 | 271289 | 0 | 252392 | 0 | 0 | 17715 | 8 | 0 | 0 |
| One author makes the change (the-way-author) | Claude Code | 127 | 24490 | 213881 | 301834 | 0 | 301832 | 0 | 0 | 60460 | 31 | 0 | 0 |
| Fresh review of correction 1 (the-way-stage) | Claude Code | 27 | 24469 | 78064 | 107532 | 96353 | 0 | 0 | 0 | 33590 | 6 | 0 | 0 |
| Review of the whole change (the-way-stage) | Claude Code | 77 | 24466 | 174094 | 248159 | 457400 | 0 | 209243 | 1 | 30543 | 10 | 5480 | 2 |
| Agent skills spec frontmatter fields (web-fetch) | Claude Code | 2 | 3876 | 3876 | 14335 | 11748 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Codex SKILL.md frontmatter fields (web-fetch) | Claude Code | 3 | 3965 | 4856 | 24181 | 24179 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
