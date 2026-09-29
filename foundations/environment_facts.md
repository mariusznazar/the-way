# Environment facts

What the-way takes as true about the world outside it, each with its method of checking. The rules
of an entry stand in `elements/environment-facts/template.md`.

## git-path-patterns/1

Git matches a path pattern of an attributes file by the rules of `.gitignore` patterns, except that a negative pattern is forbidden and a pattern that matches a directory does not match the paths inside it.

- **Holds for:** git 2.55.0
- **Source:** https://git-scm.com/docs/gitattributes/2.55.0 § DESCRIPTION — "The rules by which the pattern matches paths are the same as in .gitignore files (see gitignore[5]), with a few exceptions:" · § DESCRIPTION — "negative patterns are forbidden" · § DESCRIPTION — "patterns that match a directory do not recursively match paths inside that directory (so using the trailing-slash path/ syntax is pointless in an attributes file; use path/** instead)"; read 2026-09-26
- **Method:** `python -B gate/run_tests.py probes/git-path-patterns --record .runs/fact-git-path-patterns.jsonl`

## gitignore-paths/1

Within one level of precedence of its gitignore sources, the last pattern that matches a path decides whether git ignores it, and a file whose parent directory is excluded cannot be re-included.

- **Holds for:** git 2.55.0
- **Source:** https://git-scm.com/docs/gitignore/2.55.0 § DESCRIPTION — "within one level of precedence, the last matching pattern decides the outcome" · § PATTERN FORMAT — "It is not possible to re-include a file if a parent directory of that file is excluded."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/gitignore-paths --record .runs/fact-gitignore-paths.jsonl`
- **Correction:** none

## sha-256/1

The Secure Hash Standard specifies SHA-256, whose final output is a 256-bit message digest, in its section 6.2.

- **Holds for:** FIPS 180-4 (August 2015)
- **Source:** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf § 6.2 — "The final result of SHA-256 is a 256-bit message digest."; read 2026-09-26
- **Method:** `python -B gate/run_tests.py probes/sha-256 --record .runs/fact-sha-256.jsonl`

## utf-8/1

UTF-8 encodes every character of the range U+0000..U+10FFFF in a sequence of one to four octets.

- **Holds for:** RFC 3629 (November 2003)
- **Source:** https://www.rfc-editor.org/rfc/rfc3629.html § 3 — "In UTF-8, characters from the U+0000..U+10FFFF range (the UTF-16 accessible range) are encoded using sequences of 1 to 4 octets."; read 2026-09-26
- **Method:** `python -B gate/run_tests.py probes/utf-8 --record .runs/fact-utf-8.jsonl`

## json-text/1

A JSON text is a serialized value, in which numeric values that the grammar cannot represent, such as Infinity and NaN, are not permitted and the names within an object should be unique.

- **Holds for:** RFC 8259 (December 2017)
- **Source:** https://www.rfc-editor.org/rfc/rfc8259.html § 2 — "A JSON text is a serialized value." · § 6 — "Numeric values that cannot be represented in the grammar below (such as Infinity and NaN) are not permitted." · § 4 — "The names within an object SHOULD be unique."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/json-text --record .runs/fact-json-text.jsonl`
- **Correction:** none

## json-lines/1

A JSON Lines file holds one valid JSON value on each line, ends each line with '\n', which admits '\r\n', and may omit the terminator after the last value.

- **Holds for:** JSON Lines, which jsonlines.org publishes without versions
- **Source:** https://jsonlines.org/ (archived: http://web.archive.org/web/20260918132122/https://jsonlines.org/, 2026-09-18) § 2 — "Each Line is a Valid JSON Value" · § 3 — "Line Terminator is '\n'" · § 3 — "This means '\r\n' is also supported because surrounding white space is implicitly ignored when parsing JSON values." · § 3 — "Including a line terminator after the last JSON value in a file is strongly recommended but not required."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/json-lines --record .runs/fact-json-lines.jsonl`
- **Correction:** none

## python-stdlib-modules/1

The standard library of Python 3.14 holds the modules that `sys.stdlib_module_names` names in a Python 3.14 interpreter, which lists them the same on all platforms, names only the main package of each package, and excludes test modules.

- **Holds for:** CPython 3.14, whose documentation docs.python.org publishes for the 3.14 series with no page for each bugfix release
- **Source:** https://docs.python.org/3.14/library/sys.html (archived: http://web.archive.org/web/20260907072947/https://docs.python.org/3.14/library/sys.html, 2026-09-07) § sys.stdlib_module_names — "A frozenset of strings containing the names of standard library modules." · § sys.stdlib_module_names — "It is the same on all platforms. Modules which are not available on some platforms and modules disabled at Python build are also listed. All module kinds are listed: pure Python, built-in, frozen and extension modules. Test modules are excluded." · § sys.stdlib_module_names — "For packages, only the main package is listed: sub-packages and sub-modules are not listed."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/python-stdlib-modules --record .runs/fact-python-stdlib-modules.jsonl`
- **Correction:** none

## dequelabs-axe-core-visibility/1

The repository dequelabs/axe-core on github.com is public.

- **Holds for:** the repository dequelabs/axe-core on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/dequelabs/axe-core` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/dequelabs-axe-core-visibility --record .runs/fact-dequelabs-axe-core-visibility.jsonl`
- **Correction:** none

## github-spec-kit-visibility/1

The repository github/spec-kit on github.com is public.

- **Holds for:** the repository github/spec-kit on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/github/spec-kit` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/github-spec-kit-visibility --record .runs/fact-github-spec-kit-visibility.jsonl`
- **Correction:** none

## doorstop-dev-doorstop-visibility/1

The repository doorstop-dev/doorstop on github.com is public.

- **Holds for:** the repository doorstop-dev/doorstop on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/doorstop-dev/doorstop` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/doorstop-dev-doorstop-visibility --record .runs/fact-doorstop-dev-doorstop-visibility.jsonl`
- **Correction:** none

## obi1kenobi-cargo-semver-checks-visibility/1

The repository obi1kenobi/cargo-semver-checks on github.com is public.

- **Holds for:** the repository obi1kenobi/cargo-semver-checks on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/obi1kenobi/cargo-semver-checks` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/obi1kenobi-cargo-semver-checks-visibility --record .runs/fact-obi1kenobi-cargo-semver-checks-visibility.jsonl`
- **Correction:** none

## shopify-packwerk-visibility/1

The repository Shopify/packwerk on github.com is public.

- **Holds for:** the repository Shopify/packwerk on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/Shopify/packwerk` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/shopify-packwerk-visibility --record .runs/fact-shopify-packwerk-visibility.jsonl`
- **Correction:** none

## backstage-backstage-visibility/1

The repository backstage/backstage on github.com is public.

- **Holds for:** the repository backstage/backstage on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/backstage/backstage` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/backstage-backstage-visibility --record .runs/fact-backstage-backstage-visibility.jsonl`
- **Correction:** none

## kubernetes-enhancements-visibility/1

The repository kubernetes/enhancements on github.com is public.

- **Holds for:** the repository kubernetes/enhancements on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/kubernetes/enhancements` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/kubernetes-enhancements-visibility --record .runs/fact-kubernetes-enhancements-visibility.jsonl`
- **Correction:** none

## owasp-pytm-visibility/1

The repository OWASP/pytm on github.com is public.

- **Holds for:** the repository OWASP/pytm on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/OWASP/pytm` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/owasp-pytm-visibility --record .runs/fact-owasp-pytm-visibility.jsonl`
- **Correction:** none

## oasdiff-oasdiff-visibility/1

The repository oasdiff/oasdiff on github.com is public.

- **Holds for:** the repository oasdiff/oasdiff on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/oasdiff/oasdiff` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/oasdiff-oasdiff-visibility --record .runs/fact-oasdiff-oasdiff-visibility.jsonl`
- **Correction:** none

## chromium-src-visibility/1

The repository chromium/src on chromium.googlesource.com opens to a reader who is not signed in.

- **Holds for:** the repository chromium/src on chromium.googlesource.com, for which the host gives no version
- **Source:** observed: `curl https://chromium.googlesource.com/chromium/src/?format=JSON` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/chromium-src-visibility --record .runs/fact-chromium-src-visibility.jsonl`
- **Correction:** none

## impossiblebench-test-modification/1

The Claude models ImpossibleBench measured mostly cheat on Oneoff-SWEbench by modifying the test cases, and on Impossible-SWEbench making the tests read-only is particularly effective against Claude Opus 4.1, whose primary cheating strategy involves modifying test cases.

- **Holds for:** arXiv:2510.20270v1, measuring Claude Opus 4.1, Claude Sonnet 4 and Claude Sonnet 3.7
- **Source:** https://arxiv.org/html/2510.20270v1 § 3.1 — "We perform our experiments on a suite of leading open-source and closed-source models: GPT-5, o3, o4-mini, GPT-4.1, Claude Opus 4.1, Claude Sonnet 4, Claude Sonnet 3.7, and Qwen3-Coder." · § 4.2 — "OpenAI models perform special-casing most of the time, while Claude models and Qwen3-Coder mostly modify the test cases" · § 5.2 — "Effect of hiding tests and making tests read-only on Impossible-SWEbench" · § 5.2 — "This approach is particularly effective against models like Opus-4.1, whose primary cheating strategy involves modifying test cases, but it does not eliminate other cheating methods such as special-casing or operator overloading"; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/impossiblebench-test-modification --record .runs/fact-impossiblebench-test-modification.jsonl`
- **Correction:** none

## llm-self-preference/1

In self-evaluation on two summarisation tasks, GPT-3.5 Turbo, GPT-4 and Llama 2 disproportionately favour summaries written by themselves over those by other LLMs and by humans.

- **Holds for:** arXiv:2404.13076v1, measuring GPT-3.5 Turbo, GPT-4 and Llama 2
- **Source:** https://arxiv.org/html/2404.13076v1 § 1 — "Frontier LLMs exhibit self-preference in self-evaluation." · § 1 — "On two summarization tasks, LLMs (GPT-3.5 Turbo, GPT-4, and Llama 2) disproportionately favor summaries written by themselves over those by other LLMs and from humans."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/llm-self-preference --record .runs/fact-llm-self-preference.jsonl`
- **Correction:** none

## llm-decision-violation-detection/1

Language models detecting violations of architectural decisions reach substantial agreement and strong accuracy for explicit, code-inferable decisions, and fall short in accuracy for implicit or deployment-oriented decisions that depend on deployment configuration or organisational knowledge.

- **Holds for:** arXiv:2602.07609v1, measuring Marco-o1, Mistral-NeMo-Instruct-2407, Qwen3-14B-Base and Llama-3.1-8B-Instruct
- **Source:** https://arxiv.org/abs/2602.07609v1 § Abstract — "The models achieved substantial agreement and strong accuracy for explicit, code-inferable decisions. Accuracy falls short for implicit or deployment-oriented decisions that depend on deployment configuration or organizational knowledge."; read 2026-09-26 · https://arxiv.org/html/2602.07609v1 § Table II — "Marco-o1" · § Table II — "Mistral-NeMo-Instruct-2407" · § Table II — "Qwen3-14B-Base" · § Table II — "Llama-3.1-8B-Instruct"; read 2026-09-26
- **Method:** `python -B gate/run_tests.py probes/llm-decision-violation-detection --record .runs/fact-llm-decision-violation-detection.jsonl`

## instruction-density-accuracy/1

Of the 20 models IFScale evaluated across seven providers, even the best reach only 68% accuracy at its maximum density of 500 instructions.

- **Holds for:** arXiv:2507.11538v1, measuring claude-3.5-haiku, claude-3.7-sonnet, claude-opus-4, claude-sonnet-4, deepseek-r1-0528, gemini-2.5-flash-preview, gemini-2.5-pro-preview, llama-4-maverick, llama-4-scout, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-mini, gpt-4.5-preview, o3, o4-mini, qwen3-235b-a22b, grok-3-beta and grok-3-mini-beta
- **Source:** https://arxiv.org/abs/2507.11538v1 § Abstract — "We evaluate 20 state-of-the-art models across seven major providers and find that even the best frontier models only achieve 68% accuracy at the max density of 500 instructions."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/instruction-density-accuracy --record .runs/fact-instruction-density-accuracy.jsonl`
- **Correction:** none

## context-file-effect/1

Providing context files to coding agents does not generally improve their task success rates while increasing inference cost by over 20% on average, and the agents follow the instructions in those files well while repository overviews in them do not help.

- **Holds for:** arXiv:2602.11988v2, measuring Claude Code with Sonnet-4.5, Codex with GPT-5.2 and GPT-5.1 mini, and Qwen Code with Qwen3-30b-coder
- **Source:** https://arxiv.org/abs/2602.11988v2 § Abstract — "Surprisingly, we find that providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average." · § Abstract — "Specifically, we find that while instructions in the context files are well followed by coding agents, repository overviews, although popular and recommended by model providers, are not helpful."; read 2026-09-26 · https://arxiv.org/html/2602.11988v2 § 4.1 — "We consider four coding agents, paired with suitable models: Claude Code [3] with Sonnet-4.5 [4], Codex [26] with GPT-5.2 and GPT-5.1 mini [32], and Qwen Code [28] with Qwen3-30b-coder [34]."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/context-file-effect --record .runs/fact-context-file-effect.jsonl`
- **Correction:** none

## claude-code-path-rules/1

Claude Code applies a rule whose frontmatter gives `paths` only when it works with files matching those patterns.

- **Holds for:** Claude Code, whose documentation code.claude.com publishes for its current release without versions
- **Source:** https://code.claude.com/docs/en/memory (archived: http://web.archive.org/web/20260925131337/https://code.claude.com/docs/en/memory, 2026-09-25) § Path-specific rules — "Rules can be scoped to specific files using YAML frontmatter with the paths field. These conditional rules only apply when Claude is working with files matching the specified patterns."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/claude-code-path-rules --record .runs/fact-claude-code-path-rules.jsonl`
- **Correction:** none

## visible-scoring-reward-hacking/1

In METR's evaluations of o3, reward hacking was more than 43 times more common on RE-Bench tasks than on HCAST tasks, which METR puts down perhaps to the model seeing the entire scoring function on RE-Bench, or to those tasks being more difficult or differently scaffolded.

- **Holds for:** METR's post of 2025-06-05, measuring o3, which metr.org publishes without versions
- **Source:** https://metr.org/blog/2025-06-05-recent-reward-hacking/ (archived: http://web.archive.org/web/20260921012137/https://metr.org/blog/2025-06-05-recent-reward-hacking/, 2026-09-21) § What we’ve observed — "Reward hacking was more than 43× more common on RE-Bench tasks than HCAST tasks, perhaps because on RE-Bench tasks the model was able to see the entire scoring function, making that function easier to bypass and inadvertently priming the model to consider that type of solution more strongly." · § What we’ve observed — "The discrepancy could also be due to RE-Bench tasks being more difficult or because they use different scaffolding."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/visible-scoring-reward-hacking --record .runs/fact-visible-scoring-reward-hacking.jsonl`
- **Correction:** none

## oracle-in-loop-building/1

With the hidden test oracle in their loop, the two Copilot CLI agents the study ran reach a near-perfect score from a demo holding the tested behaviour directly, leaving the requested library dead or absent.

- **Holds for:** arXiv:2606.28430v1, measuring GitHub Copilot CLI 1.0.56 with claude-opus-4.7 and with gpt-5.5
- **Source:** https://arxiv.org/abs/2606.28430v1 § Abstract — "In a controlled code-as-spec setup, two production Copilot CLI agents (claude-opus-4.7, gpt-5.5) re-implement a React Fluent-UI data table in Angular as a reusable library under a hidden 222-test Playwright oracle across 18 runs and three oracle-availability conditions." · § Abstract — "With the oracle in the loop, the score reaches near-perfect, but from a demo holding the tested behavior directly, the library left dead or absent."; read 2026-09-26 · https://arxiv.org/html/2606.28430v1 § 2 — "We study GitHub Copilot CLI (version 1.0.56) under two model configurations"; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/oracle-in-loop-building --record .runs/fact-oracle-in-loop-building.jsonl`
- **Correction:** none

## github-private-repository-response/1

GitHub answers a request for a private resource that is not properly authenticated with 404 Not Found instead of 403 Forbidden, to avoid confirming that a private repository exists.

- **Holds for:** the GitHub REST API version 2026-03-10, whose documentation docs.github.com publishes for each API version without editions of its own
- **Source:** https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2026-03-10 (archived: http://web.archive.org/web/20260324033245/https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2026-03-10, 2026-03-24) § 404 Not Found for an existing resource — "If you make a request to access a private resource and your request isn't properly authenticated, you will receive a 404 Not Found response. GitHub uses a 404 Not Found response instead of a 403 Forbidden response to avoid confirming the existence of private repositories."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/github-private-repository-response --record .runs/fact-github-private-repository-response.jsonl`
- **Correction:** none

## anthropic-model-states/1

Anthropic describes the lifecycle of its models by the states Active, Legacy, Deprecated and Retired, in which an Active model is fully supported and recommended for use and a Retired one is no longer available for use.

- **Holds for:** the model deprecations page of the Claude Platform documentation, which platform.claude.com publishes without versions
- **Source:** https://platform.claude.com/docs/en/about-claude/model-deprecations (archived: http://web.archive.org/web/20260926103650/https://platform.claude.com/docs/en/about-claude/model-deprecations, 2026-09-26) § Overview — "Anthropic uses the following terms to describe the model lifecycle:" · § Overview — "Active: The model is fully supported and recommended for use." · § Overview — "Legacy: The model will no longer receive updates and may be deprecated in the future." · § Overview — "Deprecated: The model is still functional but no longer recommended." · § Overview — "Retired: The model is no longer available for use. Requests to retired models will fail."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py probes/anthropic-model-states --record .runs/fact-anthropic-model-states.jsonl`
- **Correction:** none

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
