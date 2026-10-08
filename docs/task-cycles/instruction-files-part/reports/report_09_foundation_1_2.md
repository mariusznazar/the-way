# Report 09 — facts agent, foundation 1.2 (returned as text, saved by the orchestrator)

All six facts written into `foundations/environment_facts.md`, between `codex-skill-paths/1` and the withdrawn identifiers list; guard exit 0, 0 errors; every passage checked word for word against the live page and the archived copy cited; nothing staged or committed. None needed the fallback or a missing-capture question; `claude-code-agents-md` is documented for v2.1.277+, so it takes the normal watch method. WAY-08's deliberate break for a fact's method stays the template's open `TODO — decision pending`.

Entries (sentences; full *Source* fields are in the file):

- `claude-code-imports/1` — Claude Code expands a file that a `CLAUDE.md` imports with `@path/to/import` syntax and loads it into context at launch alongside that `CLAUDE.md`, and skips Markdown code spans and fenced code blocks when it parses imports. (code.claude.com/docs/en/memory, archived 2026-10-07, § Import additional files)
- `claude-code-agents-md/1` — By default, Claude Code reads `AGENTS.md` as a repository's project instructions, on v2.1.277 or later, only when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` stands in its working directory or any directory above it. (same page, § AGENTS.md, § When Claude Code reads AGENTS.md)
- `codex-agents-md/1` — When it starts, Codex builds an instruction chain from the `AGENTS.override.md`, or else the `AGENTS.md`, of its home directory and, walking from the project root down to its current working directory, from at most one file in each directory, and stops searching once it reaches its current directory. (learn.chatgpt.com/docs/agent-configuration/agents-md, archived 2026-09-30)
- `cursor-agents-md/1` — Cursor CLI reads `AGENTS.md` and `CLAUDE.md` at the project root, where they are present, and applies them as rules alongside `.cursor/rules`. (cursor.com/docs/cli/using, archived 2026-09-30, § Rules)
- `single-rule-compliance/1` — In McMillan's factorial study of Claude Code CLI sessions, Sonnet 4.6 complied with a trivial target annotation that a single `CLAUDE.md` asked for in 67.7% of the functions it generated, and no model the study ran emitted the annotation without the configuration file. Holds for arXiv:2605.10039v1, Sonnet 4.6 and Opus 4.6 on Claude Code CLI 2.1.92, Opus 4.7 on CLI 2.1.123. (abstract page and PDF of v1; the v1 HTML returns 404)
- `agent-run-variance/1` — On SWE-Bench-Verified, single-run pass@1 estimates of the agents Bjarnason et al. ran vary by 2.2 to 6.0 percentage points depending on which run is selected, with standard deviations exceeding 1.5 percentage points even at temperature 0. Holds for arXiv:2602.07150v3, Qwen/Qwen3-32B, agentica-org/DeepSWE-preview, mistralai/Devstral-2-123B-Instruct-2512, each with nano-agent and R2E-Gym.

Archived copies found through the archive's CDX index, newest capture; studies cite versioned arXiv addresses (editions, no archived copy). Method: a watch of the quoted passages (precedent `claude-code-path-rules`, PR #8 facts); no behaviour probe (would need an agent with credentials and a model).

Fingerprints: claude-code-imports 5b9359fd · claude-code-agents-md e4007cb8 · codex-agents-md 6dc13475 · cursor-agents-md aaa19b03 · single-rule-compliance 2aac5731 · agent-run-variance 538af710.

Guard: `0 error(s), 6 warning(s), 3 unchecked` — six expected "no invariant's *Rests on* and no decision's *Based on* names it" warnings; three unchecked from `none`.

Meaning (Polish):
- claude-code-imports: Claude Code wczytuje na starcie sesji plik zaimportowany w `CLAUDE.md` przez `@ścieżka` razem z tym `CLAUDE.md`, a ścieżki w backtickach i w blokach kodu nie traktuje jako importu.
- claude-code-agents-md: Claude Code od wersji 2.1.277 domyślnie czyta `AGENTS.md` jako instrukcje projektu tylko wtedy, gdy w katalogu roboczym ani w żadnym katalogu nad nim nie ma `CLAUDE.md`, `.claude/CLAUDE.md` ani `CLAUDE.local.md`.
- codex-agents-md: Codex na starcie składa instrukcje z pliku w swoim katalogu domowym, a potem z co najwyżej jednego pliku w każdym katalogu od korzenia projektu w dół do katalogu roboczego — i głębiej już nie szuka.
- cursor-agents-md: Cursor CLI czyta `AGENTS.md` i `CLAUDE.md` z korzenia projektu, jeśli tam są, i stosuje je jako reguły obok `.cursor/rules`.
- single-rule-compliance: W badaniu McMillana Sonnet 4.6 w Claude Code spełnił jedno proste polecenie z `CLAUDE.md` w 67,7% wygenerowanych funkcji, a bez tego pliku żaden z badanych modeli ani razu nie zrobił tego sam z siebie.
- agent-run-variance: W badaniu Bjarnasona i in. wynik pass@1 z jednego przebiegu tego samego agenta na SWE-Bench-Verified różni się o 2,2–6,0 punktu procentowego zależnie od wybranego przebiegu, a odchylenie standardowe przekracza 1,5 punktu nawet przy temperaturze 0.

WAY-33: 1 WAY-129 ↔ `claude-code-imports` (backtick clause added — question 1); 2 WAY-132 ↔ `claude-code-agents-md` consistent; soft point: interactive sessions print "no CLAUDE.md found; AGENTS.md loaded", so "without a sign" in WAY-132 *Rejected* holds only as "the line silently stops appearing"; 3 the page recommends "target under 200 lines per CLAUDE.md file" — no contradiction with WAY-128; 4 `instruction-density-accuracy` related, no link; 5 WAY-52 ↔ WAY-128 consistent; 6 WAY-85 fits WAY-131 (*Review when* none) and WAY-133 (Active state); 7 no glossary term used or paraphrased; 8 Cursor above the working directory not on the page — no fact (WAY-73). For the code step: the Claude Code page documents a subdirectory `AGENTS.md` read on first Read there, and "Not read: AGENTS.local.md, AGENTS.override.md, or anything under a .agents/ directory". For the watch writer: `single-rule-compliance` reads the PDF or abstract page; raw abstract writes "CLAUDE$.$md"; the PDF prints "structural- variable".

Questions with proposed answers: 1 keep the backtick clause in `claude-code-imports`; 2 accept `single-rule-compliance` following the page (67.7%, Sonnet 4.6), with CLI versions in *Holds for*; 3 accept "By default"; 4 accept the home-directory file in `codex-agents-md`.

## Resumed for Q17 — `single-rule-compliance/1` re-sourced to the abstract

Sentence: "In McMillan's factorial study of compliance with a trivial target annotation across Claude Code CLI sessions, none of four structural variables of the configuration files — file size, instruction position, file architecture and contradictions in adjacent files — produces a detectable contrast after multiple-testing correction, while each additional function the agent generates within a session is associated with approximately 5.6% lower odds of compliance per step in the session lengths tested, though the relationship is non-monotonic." *Holds for* arXiv:2605.10039v1, measuring Sonnet 4.6, Opus 4.6 and Opus 4.7. *Source*: https://arxiv.org/abs/2605.10039v1 § Abstract, four passages verbatim, read 2026-10-08. Method unchanged. Fingerprint cf537693 (was 2aac5731); others unchanged. Guard `0 error(s), 6 warning(s), 3 unchecked`, exit 0.

Meaning (Polish): W badaniu McMillana nad sesjami Claude Code żadna z czterech cech budowy pliku konfiguracyjnego (rozmiar, miejsce polecenia, układ plików, sprzeczne polecenia w sąsiednich plikach) nie zmieniła wykrywalnie tego, jak często agent wykonuje proste polecenie; za to z każdą kolejną funkcją pisaną w tej samej sesji szansa wykonania polecenia spada o około 5,6% na krok, choć nie równo z kroku na krok.

Follow-on: WAY-133 cites `single-rule-compliance@cf537693` and quotes no compliance percentage.
