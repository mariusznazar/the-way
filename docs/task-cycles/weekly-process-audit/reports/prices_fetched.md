# Prices read from the providers' pages (fetched by a web-fetch agent for the orchestrator, read 2026-11-11)

Unit: USD per million tokens, as the pages state them. Short-context rows (Anthropic: Haiku up to 100,000 tokens; OpenAI: up to 272K input tokens).

Anthropic — https://platform.claude.com/docs/en/about-claude/pricing (read 2026-11-11)

| Model id in stages.md | Page name | Input | Cache hits (cached input) | Output | Cache write (5 minutes) |
|---|---|---|---|---|---|
| claude-opus-5-5 | Claude Opus 5.5 | 4 | 0.20 | 20 | 5 |
| claude-sonnet-5-5 | Claude Sonnet 5.5 | 2 | 0.10 | 10 | 2.50 |
| claude-haiku-5-5 | Claude Haiku 5.5 (prompts up to 100,000 tokens) | 0.10 | 0.01 | 0.50 | 0.125 |
| claude-fable-5-1 | Claude Fable 5.1 | 10 | 0.25 | 50 | 12.50 |

Notes of the page: Haiku 5.5 over 100,000 tokens: input 0.50, cache hits 0.05, output 2.50. Batch is 50% off; data residency `us` is x1.1; fast mode of Opus 5.5 is 8 in / 40 out. None of these applies to the plain first-party API use the cycles make.

OpenAI — https://platform.openai.com/docs/pricing, which redirects to https://developers.openai.com/api/docs/pricing (read 2026-11-11)

| Model id in stages.md | Page name | Input | Cached input | Output |
|---|---|---|---|---|
| gpt-6-astra | gpt-6-astra | 10.00 | 1.00 | 50.00 |
| gpt-6.1-sol | gpt-6.1-sol | 2.00 | 0.10 | 10.00 |
| gpt-6-sol | gpt-6-sol | 2.00 | 0.20 | 10.00 |
| gpt-6-luna | gpt-6-luna | 0.10 | 0.01 | 0.50 |

Notes of the page: over 272K input tokens the prices rise (astra 20/2/75, 6.1-sol 4/0.20/15, 6-sol 4/0.40/15, luna 0.20/0.02/0.75); batch is half; the page header says "Prices per 1M tokens" and names no currency code beside "$".

The model ids come from the archived `stages.md` files of the-way's own history (counts of rows: opus-5-5 889, sonnet-5-5 591, gpt-6-astra 208, gpt-6.1-sol 95, haiku-5-5 38, gpt-6-sol 38, gpt-6-luna 32, fable-5-1 16).
