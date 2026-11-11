# Price list of the audit of the process

Prices of the models the cycles' `stages.md` name, read from the providers' published price pages.
`process-audit/audit_count.py` reads this file to give each cycle's cost at constant prices (WAY-334).

- List date: 2026-11-11

Unit: USD per million tokens, as the pages state them. The date above is the day the pages were
read; a new list with another date starts a new series of measures (WAY-336).

How the command uses the columns: *Input* of `stages.md` includes the part of the input read from a
cache, so a stage's cost is its input minus its cached input at the *Input* price, its cached input at
the *Cached input* price and its output at the *Output* price. The Anthropic page calls the cached
input "cache hits". Cache writes (*Cache write (5 minutes)*) are not priced: `task-cycle/cycle_stages.py`
folds them into *Input*, so they are priced there as input, an approximation.

The prices are the short-context rows of each page: Haiku 5.5 up to 100,000 input tokens, and the
OpenAI models up to 272K input tokens. The command does not know a call's size, so a call above those
limits costs more than this list gives. A model whose price no page gives has `—` in its price cells,
and the command gives its cost as `unknown`; a model of `stages.md` that no row of this list names is
`unknown` too.

## Anthropic

- Page: https://platform.claude.com/docs/en/about-claude/pricing (read 2026-11-11)

| Model id in stages.md | Page name | Input | Cached input | Output | Cache write (5 minutes) |
|---|---|---|---|---|---|
| claude-opus-5-5 | Claude Opus 5.5 | 4 | 0.20 | 20 | 5 |
| claude-sonnet-5-5 | Claude Sonnet 5.5 | 2 | 0.10 | 10 | 2.50 |
| claude-haiku-5-5 | Claude Haiku 5.5 (prompts up to 100,000 tokens) | 0.10 | 0.01 | 0.50 | 0.125 |
| claude-fable-5-1 | Claude Fable 5.1 | 10 | 0.25 | 50 | 12.50 |

Notes of the page: Haiku 5.5 over 100,000 tokens: input 0.50, cache hits 0.05, output 2.50. Batch is
50% off; data residency `us` is x1.1; fast mode of Opus 5.5 is 8 in / 40 out. None of these applies to
the plain first-party API use the cycles make.

## OpenAI

- Page: https://developers.openai.com/api/docs/pricing (read 2026-11-11; the address
  https://platform.openai.com/docs/pricing redirects to it)

| Model id in stages.md | Page name | Input | Cached input | Output |
|---|---|---|---|---|
| gpt-6-astra | gpt-6-astra | 10.00 | 1.00 | 50.00 |
| gpt-6.1-sol | gpt-6.1-sol | 2.00 | 0.10 | 10.00 |
| gpt-6-sol | gpt-6-sol | 2.00 | 0.20 | 10.00 |
| gpt-6-luna | gpt-6-luna | 0.10 | 0.01 | 0.50 |

Notes of the page: over 272K input tokens the prices rise (astra 20/2/75, 6.1-sol 4/0.20/15, 6-sol
4/0.40/15, luna 0.20/0.02/0.75); batch is half. The page header says "Prices per 1M tokens" and names
no currency code beside "$"; the list reads the "$" as USD, as the unit line above states.
