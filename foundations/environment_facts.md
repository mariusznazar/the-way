# Environment facts

What the-way takes as true about the world outside it, each with its source. The rules of an entry
stand in `elements/environment-facts/template.md`.

## git-path-patterns

Git matches a path pattern of an attributes file by the rules of `.gitignore` patterns, except that a negative pattern is forbidden and a pattern that matches a directory does not match the paths inside it.

- **Source:** https://git-scm.com/docs/gitattributes/2.55.0 § DESCRIPTION — "The rules by which the pattern matches paths are the same as in .gitignore files (see gitignore[5]), with a few exceptions:" · § DESCRIPTION — "negative patterns are forbidden" · § DESCRIPTION — "patterns that match a directory do not recursively match paths inside that directory (so using the trailing-slash path/ syntax is pointless in an attributes file; use path/** instead)"; read 2026-09-26

## sha-256

The Secure Hash Standard specifies SHA-256, whose final output is a 256-bit message digest, in its section 6.2.

- **Source:** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf § 6.2 — "The final result of SHA-256 is a 256-bit message digest."; read 2026-09-26

## utf-8

UTF-8 encodes every character of the range U+0000..U+10FFFF in a sequence of one to four octets.

- **Source:** https://www.rfc-editor.org/rfc/rfc3629.html § 3 — "In UTF-8, characters from the U+0000..U+10FFFF range (the UTF-16 accessible range) are encoded using sequences of 1 to 4 octets."; read 2026-09-26

## python-stdlib-modules

The standard library of Python 3.14 holds the modules that `sys.stdlib_module_names` names in a Python 3.14 interpreter, which lists them the same on all platforms, names only the main package of each package, and excludes test modules.

- **Source:** https://docs.python.org/3.14/library/sys.html (archived: http://web.archive.org/web/20260907072947/https://docs.python.org/3.14/library/sys.html, 2026-09-07) § sys.stdlib_module_names — "A frozenset of strings containing the names of standard library modules." · § sys.stdlib_module_names — "It is the same on all platforms. Modules which are not available on some platforms and modules disabled at Python build are also listed. All module kinds are listed: pure Python, built-in, frozen and extension modules. Test modules are excluded." · § sys.stdlib_module_names — "For packages, only the main package is listed: sub-packages and sub-modules are not listed."; read 2026-09-26

## impossiblebench-test-modification

The Claude models ImpossibleBench measured mostly cheat on Oneoff-SWEbench by modifying the test cases, and on Impossible-SWEbench making the tests read-only is particularly effective against Claude Opus 4.1, whose primary cheating strategy involves modifying test cases.

- **Source:** https://arxiv.org/html/2510.20270v1 § 3.1 — "We perform our experiments on a suite of leading open-source and closed-source models: GPT-5, o3, o4-mini, GPT-4.1, Claude Opus 4.1, Claude Sonnet 4, Claude Sonnet 3.7, and Qwen3-Coder." · § 4.2 — "OpenAI models perform special-casing most of the time, while Claude models and Qwen3-Coder mostly modify the test cases" · § 5.2 — "Effect of hiding tests and making tests read-only on Impossible-SWEbench" · § 5.2 — "This approach is particularly effective against models like Opus-4.1, whose primary cheating strategy involves modifying test cases, but it does not eliminate other cheating methods such as special-casing or operator overloading"; read 2026-09-26

## llm-self-preference

In self-evaluation on two summarisation tasks, GPT-3.5 Turbo, GPT-4 and Llama 2 disproportionately favour summaries written by themselves over those by other LLMs and by humans.

- **Source:** https://arxiv.org/html/2404.13076v1 § 1 — "Frontier LLMs exhibit self-preference in self-evaluation." · § 1 — "On two summarization tasks, LLMs (GPT-3.5 Turbo, GPT-4, and Llama 2) disproportionately favor summaries written by themselves over those by other LLMs and from humans."; read 2026-09-26

## llm-design-rationale-expert-overlap

In Zhou et al.'s study, five LLMs given a chain-of-thought prompt produced design-rationale arguments for architecture decisions with mean precision 0.237, recall 0.684, and F1 0.351 for overlap with expert-provided arguments.

- **Source:** https://arxiv.org/html/2504.20781v3 § 3.5 — "individual arguments" · § 3.5.1 — "with those extracted from human experts" · § 4.2.1 — "Precision, Recall, and F1-score" · § 4.2.1 — "0.237, 0.684, and 0.351, respectively" · § Table 1 — "gpt-3.5-turbo" · § Table 1 — "gpt-4-0613" · § Table 1 — "gemini-1.0-pro" · § Table 1 — "llama3-8B" · § Table 1 — "mistral-7B"; read 2026-10-01

## llm-decision-violation-detection

Language models detecting violations of architectural decisions reach substantial agreement and strong accuracy for explicit, code-inferable decisions, and fall short in accuracy for implicit or deployment-oriented decisions that depend on deployment configuration or organisational knowledge.

- **Source:** https://arxiv.org/abs/2602.07609v1 § Abstract — "The models achieved substantial agreement and strong accuracy for explicit, code-inferable decisions. Accuracy falls short for implicit or deployment-oriented decisions that depend on deployment configuration or organizational knowledge."; read 2026-09-26 · https://arxiv.org/html/2602.07609v1 § Table II — "Marco-o1" · § Table II — "Mistral-NeMo-Instruct-2407" · § Table II — "Qwen3-14B-Base" · § Table II — "Llama-3.1-8B-Instruct"; read 2026-09-26

## instruction-density-accuracy

Of the 20 models IFScale evaluated across seven providers, which the rows of its tables of full results name, accuracy degrades as the density of instructions given at once rises from 10 to 500, in three patterns — stable until a threshold and then falling more steeply, which the two best models show past 150 or more instructions; a steady decline; or a steep early fall to a low floor — and even the best reach only 68% accuracy at the maximum density of 500 instructions.

- **Source:** https://arxiv.org/abs/2507.11538v1 § Abstract — "We evaluate 20 state-of-the-art models across seven major providers and find that even the best frontier models only achieve 68% accuracy at the max density of 500 instructions."; read 2026-10-28 · https://arxiv.org/html/2507.11538v1 § Figure 2 — "Model performance degradation as instruction density increases from 10 to 500 instructions" · § 4.4 — "Threshold decay: Performance remains stable until a threshold, then transitions to a different (steeper) degradation slope and displays increased variance." · § 4.4 — "The top two models (gemini-2.5-pro, o3) demonstrate this clearly, maintaining near-perfect performance through 150 or more instructions before declining." · § 4.4 — "Linear decay: Characterized by steady, predictable decline in performance." · § 4.4 — "Exponential decay: Characterized by rapid early degradation followed by performance stabilization at low accuracy floors." · § Table 1 — "across all 20 evaluated LLMs" · § Table 1 — "claude-3.5-haiku" · § Table 1 — "claude-3.7-sonnet" · § Table 1 — "claude-opus-4" · § Table 1 — "claude-opus-4 (r)" · § Table 1 — "claude-sonnet-4" · § Table 1 — "claude-sonnet-4 (r)" · § Table 1 — "deepseek-r1-0528" · § Table 1 — "gemini-2.5-flash-preview" · § Table 1 — "gemini-2.5-pro-preview" · § Table 2 — "llama-4-maverick" · § Table 2 — "llama-4-scout" · § Table 2 — "gpt-4.1" · § Table 2 — "gpt-4.1-mini" · § Table 2 — "gpt-4.1-nano" · § Table 2 — "gpt-4o" · § Table 2 — "gpt-4o-mini" · § Table 2 — "gpt-4.5-preview" · § Table 3 — "o3 (medium)" · § Table 3 — "o3 (high)" · § Table 3 — "o4-mini (medium)" · § Table 3 — "qwen3-235b-a22b" · § Table 3 — "grok-3-beta" · § Table 3 — "grok-3-mini-beta"; read 2026-10-28

## context-file-effect

Providing context files to coding agents does not generally improve their task success rates while increasing inference cost by over 20% on average, and the agents follow the instructions in those files well while repository overviews in them do not help.

- **Source:** https://arxiv.org/abs/2602.11988v3 § Abstract — "Surprisingly, we find that providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average." · § Abstract — "Specifically, we find that while instructions in the context files are well followed by coding agents, repository overviews, although popular and recommended by model providers, are not helpful."; read 2026-09-30 · https://arxiv.org/html/2602.11988v3 § 4.1 — "We consider four coding agents, paired with suitable models: Claude Code [3] with Sonnet-4.5 [5], Codex [26] with GPT-5.2 and GPT-5.1 mini [32], and Qwen Code [28] with Qwen3-30b-coder [34]."; read 2026-09-30

## claude-code-path-rules

Claude Code applies a rule whose frontmatter gives `paths` only when it works with files matching those patterns.

- **Source:** https://code.claude.com/docs/en/memory (archived: http://web.archive.org/web/20260925131337/https://code.claude.com/docs/en/memory, 2026-09-25) § Path-specific rules — "Rules can be scoped to specific files using YAML frontmatter with the paths field. These conditional rules only apply when Claude is working with files matching the specified patterns."; read 2026-09-26

## visible-scoring-reward-hacking

In METR's evaluations of o3, reward hacking was more than 43 times more common on RE-Bench tasks than on HCAST tasks, which METR puts down perhaps to the model seeing the entire scoring function on RE-Bench, or to those tasks being more difficult or differently scaffolded.

- **Source:** https://metr.org/blog/2025-06-05-recent-reward-hacking/ (archived: http://web.archive.org/web/20260921012137/https://metr.org/blog/2025-06-05-recent-reward-hacking/, 2026-09-21) § What we’ve observed — "Reward hacking was more than 43× more common on RE-Bench tasks than HCAST tasks, perhaps because on RE-Bench tasks the model was able to see the entire scoring function, making that function easier to bypass and inadvertently priming the model to consider that type of solution more strongly." · § What we’ve observed — "The discrepancy could also be due to RE-Bench tasks being more difficult or because they use different scaffolding."; read 2026-09-26

## oracle-in-loop-building

With the hidden test oracle in their loop, the two Copilot CLI agents the study ran reach a near-perfect score from a demo holding the tested behaviour directly, leaving the requested library dead or absent.

- **Source:** https://arxiv.org/abs/2606.28430v1 § Abstract — "In a controlled code-as-spec setup, two production Copilot CLI agents (claude-opus-4.7, gpt-5.5) re-implement a React Fluent-UI data table in Angular as a reusable library under a hidden 222-test Playwright oracle across 18 runs and three oracle-availability conditions." · § Abstract — "With the oracle in the loop, the score reaches near-perfect, but from a demo holding the tested behavior directly, the library left dead or absent."; read 2026-09-26 · https://arxiv.org/html/2606.28430v1 § 2 — "We study GitHub Copilot CLI (version 1.0.56) under two model configurations"; read 2026-09-26

## github-private-repository-response

GitHub answers a request for a private resource that is not properly authenticated with 404 Not Found instead of 403 Forbidden, to avoid confirming that a private repository exists.

- **Source:** https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2026-03-10 (archived: http://web.archive.org/web/20260324033245/https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2026-03-10, 2026-03-24) § 404 Not Found for an existing resource — "If you make a request to access a private resource and your request isn't properly authenticated, you will receive a 404 Not Found response. GitHub uses a 404 Not Found response instead of a 403 Forbidden response to avoid confirming the existence of private repositories."; read 2026-09-26

## anthropic-model-states

Anthropic describes the lifecycle of its models by the states Active, Legacy, Deprecated and Retired, in which an Active model is fully supported and recommended for use and a Retired one is no longer available for use.

- **Source:** https://platform.claude.com/docs/en/about-claude/model-deprecations (archived: http://web.archive.org/web/20260926103650/https://platform.claude.com/docs/en/about-claude/model-deprecations, 2026-09-26) § Overview — "Anthropic uses the following terms to describe the model lifecycle:" · § Overview — "Active: The model is fully supported and recommended for use." · § Overview — "Legacy: The model will no longer receive updates and may be deprecated in the future." · § Overview — "Deprecated: The model is still functional but no longer recommended." · § Overview — "Retired: The model is no longer available for use. Requests to retired models will fail."; read 2026-09-26

## openai-model-states

OpenAI lists the models of its API in a catalogue of models; a model it announces as being deprecated is deprecated at once and has a shutdown date after which it is no longer accessible, and a legacy model no longer receives updates.

- **Source:** https://developers.openai.com/api/docs/models (archived: https://web.archive.org/web/20261022015628/https://developers.openai.com/api/docs/models, 2026-10-22) § Models — "Browse our full catalog of models"; read 2026-10-22 · https://developers.openai.com/api/docs/deprecations (archived: https://web.archive.org/web/20261020162442/https://developers.openai.com/api/docs/deprecations, 2026-10-20) § Deprecation vs. legacy — "When we announce that a model or endpoint is being deprecated, it immediately becomes deprecated. All deprecated models and endpoints will also have a shut down date. At the time of the shut down, the model or endpoint will no longer be accessible." · § Deprecation vs. legacy — "We use the term “legacy” to refer to models and endpoints that no longer receive updates."; read 2026-10-22

## python-314-bugfix-status

Python 3.14 is in the bugfix phase of its release cycle.

- **Source:** https://raw.githubusercontent.com/python/peps/faecbe2865bd44e2f816a558ccf22e60ae2ff63e/release_management/python-releases.toml § Python 3.14 metadata — “status = "bugfix"”; read 2026-09-30

## python-release-binaries

The Python Developer's Guide says the bugfix phase builds and releases new binaries, while the security phase releases no more binaries.

- **Source:** https://raw.githubusercontent.com/python/devguide/999633216399256b6ce5376c9287f07efd6c9a65/versions.rst § Status key, bugfix — "New binaries are built and released roughly every two months." · § Status key, security — "After two years (18 months for versions before 3.13), only security fixes are accepted and no more binaries are released."; read 2026-09-30

## claude-code-project-skills

Claude Code loads project skills from `.claude/skills/` in the directory where it starts and in each parent directory up to the repository root, only up to the worktree root in a session running in a linked git worktree, and, on v2.1.277 or later, the main checkout's project skills instead when the worktree checkout has no `.claude/skills` directory at its root; on v2.1.246 or later, when a session is moved with `/cd`, it adds the new directory's project skills.

- **Source:** https://code.claude.com/docs/en/skills (archived: http://web.archive.org/web/20261006214359/https://code.claude.com/docs/en/skills, 2026-10-06) § Load skills in monorepos and subdirectories — "Claude Code loads project skills from .claude/skills/ in the directory where you start it and in every parent directory up to the repository root, so starting in packages/frontend/ still picks up skills defined at the root." · § Load skills in monorepos and subdirectories — "When you move the session with /cd on v2.1.246 or later, Claude Code adds the new directory’s project skills." · § Load skills in monorepos and subdirectories — "In a session running in a linked git worktree, Claude Code searches parent directories only up to the worktree root." · § Load skills in monorepos and subdirectories — "On Claude Code v2.1.277 or later, when the worktree checkout has no .claude/skills directory at its root, Claude Code loads the main checkout’s project skills instead."; read 2026-10-08

## claude-code-nested-skills

Claude Code loads the skills of a `.claude/skills/` directory below the directory where it starts the first time it reads or edits a file in that subdirectory, keeps both skills available when such a nested skill's directory name matches another skill's name, and lists the directory-qualified variants with an instruction to invoke the one whose directory holds the files it is working on.

- **Source:** https://code.claude.com/docs/en/skills (archived: http://web.archive.org/web/20261006214359/https://code.claude.com/docs/en/skills, 2026-10-06) § Load skills in monorepos and subdirectories — "Skills in a .claude/skills/ directory below where you started don’t load at startup." · § Load skills in monorepos and subdirectories — "They load the first time Claude reads or edits a file in that subdirectory and stay available for the rest of the session." · § Load skills in monorepos and subdirectories — "When a nested skill’s directory name matches another skill’s name, both stay available." · § Load skills in monorepos and subdirectories — "Claude Code also lists the directory-qualified variants for Claude, with an instruction to invoke the one whose directory holds the files it’s working on, so the nested skill still applies to work in apps/web/."; read 2026-10-08

## codex-repository-skills

In a repository, Codex scans `.agents/skills` in every directory from its current working directory up to the repository root.

- **Source:** https://learn.chatgpt.com/docs/build-skills (archived: http://web.archive.org/web/20261002133901/https://learn.chatgpt.com/docs/build-skills, 2026-10-02) § Where Codex loads local skills — "For repositories, Codex scans .agents/skills in every directory from your current working directory up to the repository root."; read 2026-10-08

## codex-skill-paths

Codex's initial list of skills includes each skill's file path.

- **Source:** https://learn.chatgpt.com/docs/build-skills (archived: http://web.archive.org/web/20261002133901/https://learn.chatgpt.com/docs/build-skills, 2026-10-02) § Build skills — "In Codex, the initial list also includes each skill’s file path." · § Build skills — "This budget applies only to the initial skills list."; read 2026-10-08

## claude-code-imports

Claude Code expands a file that a `CLAUDE.md` imports with `@path/to/import` syntax and loads it into context at launch alongside that `CLAUDE.md`, and skips Markdown code spans and fenced code blocks when it parses imports.

- **Source:** https://code.claude.com/docs/en/memory (archived: http://web.archive.org/web/20261007150822/https://code.claude.com/docs/en/memory, 2026-10-07) § Import additional files — "CLAUDE.md files can import additional files using @path/to/import syntax." · § Import additional files — "Imported files are expanded and loaded into context at launch alongside the CLAUDE.md that references them." · § Import additional files — "Import parsing skips Markdown code spans and fenced code blocks."; read 2026-10-08

## claude-code-agents-md

By default, Claude Code reads `AGENTS.md` as a repository's project instructions, on v2.1.277 or later, only when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` stands in its working directory or any directory above it.

- **Source:** https://code.claude.com/docs/en/memory (archived: http://web.archive.org/web/20261007150822/https://code.claude.com/docs/en/memory, 2026-10-07) § AGENTS.md — "Claude Code can read AGENTS.md as your project instructions, so a repository already set up for other coding agents works without adding a CLAUDE.md, an import, or a setting." · § AGENTS.md — "Reading AGENTS.md directly requires Claude Code v2.1.277 or later." · § AGENTS.md — "In some sessions Claude can’t read AGENTS.md, so import it from a CLAUDE.md there instead." · § When Claude Code reads AGENTS.md — "By default, Claude reads AGENTS.md only when you have no CLAUDE.md in your working directory or above it." · § When Claude Code reads AGENTS.md — "Count, so Claude reads them instead of AGENTS.md: a CLAUDE.md, .claude/CLAUDE.md, or CLAUDE.local.md in your working directory or any directory above it" · § Share one file with other coding tools — "Before you choose the symlink over the import, check these constraints:" · § Share one file with other coding tools — "Windows: if you or anyone who clones the repository works on Windows, use the @AGENTS.md import instead."; read 2026-10-08

## codex-agents-md

When it starts, Codex builds an instruction chain from the `AGENTS.override.md`, or else the `AGENTS.md`, of its home directory and, walking from the project root down to its current working directory, from at most one file in each directory, and stops searching once it reaches its current directory.

- **Source:** https://learn.chatgpt.com/docs/agent-configuration/agents-md (archived: http://web.archive.org/web/20260930155336/https://learn.chatgpt.com/docs/agent-configuration/agents-md, 2026-09-30) § How Codex discovers guidance — "Codex builds an instruction chain when it starts (once per run; in the TUI this usually means once per launched session)." · § How Codex discovers guidance — "Global scope: In your Codex home directory (defaults to ~/.codex, unless you set CODEX_HOME), Codex reads AGENTS.override.md if it exists." · § How Codex discovers guidance — "Otherwise, Codex reads AGENTS.md." · § How Codex discovers guidance — "Project scope: Starting at the project root (typically the Git root), Codex walks down to your current working directory." · § How Codex discovers guidance — "Codex includes at most one file per directory." · § Layer project instructions — "Codex stops searching once it reaches your current directory, so place overrides as close to specialized work as possible."; read 2026-10-08

## cursor-agents-md

Cursor CLI reads `AGENTS.md` and `CLAUDE.md` at the project root, where they are present, and applies them as rules alongside `.cursor/rules`.

- **Source:** https://cursor.com/docs/cli/using (archived: http://web.archive.org/web/20260930152214/https://cursor.com/docs/cli/using, 2026-09-30) § Rules — "The CLI also reads AGENTS.md and CLAUDE.md at the project root (if present) and applies them as rules alongside .cursor/rules."; read 2026-10-08

## single-rule-compliance

In McMillan's factorial study of compliance with a trivial target annotation across Claude Code CLI sessions, none of four structural variables of the configuration files — file size, instruction position, file architecture and contradictions in adjacent files — produces a detectable contrast after multiple-testing correction, while each additional function the agent generates within a session is associated with approximately 5.6% lower odds of compliance per step in the session lengths tested, though the relationship is non-monotonic.

- **Source:** https://arxiv.org/abs/2605.10039v1 § Abstract — "Practitioners assume that structural choices (file size, instruction position, file architecture, contradictions in adjacent files) measurably affect adherence." · § Abstract — "We report a systematic factorial study of these choices using four manipulated variables, measuring compliance with a trivial target annotation across 1,650 Claude Code CLI sessions (16,050 function-level observations) on two TypeScript codebases, three frontier models (primarily Sonnet 4.6, with Opus 4.6 as a CLI-matched cross-model check and Opus 4.7 reported descriptively under a CLI-version confound), and five coding tasks." · § Abstract — "None of the four structural variables or three two-way interactions produces a detectable contrast after multiple-testing correction." · § Abstract — "The largest effect we measured is within-session: each additional function the agent generates is associated with approximately 5.6% lower odds of compliance per step (OR = 0.944) within the session-length range we tested, though the relationship is non-monotonic rather than a constant per-step effect."; read 2026-10-08

## agent-run-variance

On SWE-Bench-Verified, single-run pass@1 estimates of the agents Bjarnason et al. ran vary by 2.2 to 6.0 percentage points depending on which run is selected, with standard deviations exceeding 1.5 percentage points even at temperature 0.

- **Source:** https://arxiv.org/html/2602.07150v3 § Abstract — "We test this assumption by collecting 60,000 agentic trajectories on SWE-Bench-Verified, spanning three models and two scaffolds." · § Abstract — "We find substantial variance: single-run pass@1 estimates vary by 2.2 to 6.0 percentage points depending on which run is selected, with standard deviations exceeding 1.5 percentage points even at temperature 0." · § 2.1 — "We exhaustively evaluate six different agents, where an agent is defined as a model-scaffold pairs." · § 2.1 — "Qwen/Qwen3-32B" · § 2.1 — "agentica-org/DeepSWE-preview" · § 2.1 — "mistralai/Devstral-2-123B-Instruct-2512" · § 2.1 — "nano-agent is our own minimal scaffold for agentic coding experiments" · § 2.1 — "R2E-Gym is a code agent scaffold"; read 2026-10-08

## llm-test-oracle-actual-behaviour

In Konstantinou et al.'s controlled experiment with GPT-3.5 Turbo on the test oracles of 24 open-source Java repositories, LLM-based test generation approaches are prone to generate oracles that capture the actual program behaviour rather than the expected one.

- **Source:** https://arxiv.org/abs/2410.21136v1 § Abstract — "The study includes developer-written and automatically generated test cases and oracles for 24 open-source Java repositories, and different well tested prompts." · § Abstract — "Our findings show that LLM-based test generation approaches are also prone on generating oracles that capture the actual program behaviour rather than the expected one."; read 2026-10-25 · https://arxiv.org/html/2410.21136v1 § III-A Research Questions — "We chose to use GPT 3.5-turbo [28] for this experiment because it is a state-of-the-art tool and one of the most widely used LLMs."; read 2026-10-25

## computer-use-agent-web-testing

On WebTestBench, none of the models its authors evaluated with their WebTester framework exceeds an F1 score of 30% in end-to-end automated web testing.

- **Source:** https://arxiv.org/abs/2603.25226v1 § Abstract — "To address these gaps, we introduce WebTestBench, a benchmark for evaluating end-to-end automated web testing." · § Abstract — "We decompose the testing process into two cascaded sub-tasks, checklist generation and defect detection, and propose WebTester, a baseline framework for this task."; read 2026-10-25 · https://arxiv.org/html/2603.25226v1 § 4.1 Settings — "We evaluate several closed-source models and open-source models on WebTester, including: Claude Opus/Sonnet 4.5 Anthropic (2025a); Anthropic (2025b), GPT-5.2/5.1 Openai (2025b); Openai (2025a), GLM-5/4.7 Zeng et al. (2026); Zeng et al. (2025), Step-3.5-Flash Huang et al. (2026), Qwen3-Coder-Next Qwen Team (2026), MiMo-V2-Flash Xiao et al. (2026), and Minimax-M2.1 MiniMax (2025)." · § 4.2 Main Results — "All evaluated models failed to achieve an F1 score exceeding 30%."; read 2026-10-25

## claude-skill-nested-references

Anthropic's guide for authors of Agent Skills says that Claude might read only part of a file referenced from another referenced file, previewing it with a command such as `head -100` instead of reading it whole, and recommends keeping references one level deep from `SKILL.md`.

- **Source:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (archived: http://web.archive.org/web/20261022015600/https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices, 2026-10-22) § Avoid deeply nested references — "Claude might partially read files when they’re referenced from other referenced files." · § Avoid deeply nested references — "When encountering nested references, Claude might use commands such as head -100 to preview content rather than reading entire files, resulting in incomplete information." · § Avoid deeply nested references — "Keep references one level deep from SKILL.md."; read 2026-10-28

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| gitignore-paths | withdrawn: no invariant rests on it and no decision is based on it | none |
| json-text | withdrawn: no invariant rests on it and no decision is based on it | none |
| json-lines | withdrawn: no invariant rests on it and no decision is based on it | none |
