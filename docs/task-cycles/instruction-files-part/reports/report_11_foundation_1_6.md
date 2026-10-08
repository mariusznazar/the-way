# Report 11 — invariants agent (sentence author), foundation 1.6 (returned as text, saved by the orchestrator)

Wrote and staged `foundations/invariants.md` (git holds the entries; sentences quoted here because the check author receives them alone). Nothing committed.

Process root missing at the time: `C:\Storage\repos\the-way-process` did not exist; the agent read the skill, `way_of_working.md`, `rules.md`, template and examples with `git show 252152a:<path>` from `C:\Storage\repos\the-way` — same content.

## New entries (after `skill-entry-points/1`)

- `instruction-file-imports/1` — "No repository instruction file of the-way holds, outside code spans and fenced code blocks, an `@` that stands at the start of a line or right after whitespace, `(`, `[`, `{`, `"`, `'`, `“`, `‘` or `„` and is followed, before the next whitespace, by a `.` or a `/`, except the first line of the root `CLAUDE.md` when it reads `@AGENTS.md` and nothing else; the root `AGENTS.md` or `CLAUDE.md` names by its path a Markdown file that git tracks, one whose name ends in `.md` or `.markdown`, when that file's path from the repository's root, written with `/` or with `\` between directories, stands anywhere in its text with no ASCII letter or digit and none of `.`, `-`, `_`, `/` and `\` right before it, a code span runs from a run of backticks to the next run of as many backticks on the same line, and a fenced code block runs from a line whose first characters other than spaces are three backticks or three tildes to the next such line." Method `python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl`; Rests on none; Derives from WAY-129@1336c32b; Part every; Correction none.
- `root-claude-md-import/1` — "Where git tracks a `CLAUDE.md` at the repository's root, its text begins with `@AGENTS.md` followed directly by a line break, `\n` or `\r\n`, or by the end of the text." Same method; Rests on none; Derives from WAY-132@1242ac75; Part agent-instructions; Correction none.

Wording choices: the glossary term (Q15.2); a checkable "names by its path" with a boundary (without it the root `README.md` would count, being inside `agent-instructions/README.md`); "Markdown file", "code span", "fenced code block" defined by characters; own choices: the quotation marks `“ ‘ „`, the `\` form of a path; known gap `./docs/x.md` not counted; byte-level literals in `root-claude-md-import` (a BOM or trailing spaces break it). Scratch scan on today's tree: covered `AGENTS.md`, `CLAUDE.md`, `agent-instructions/README.md`, 0 breaches; positive control flags `See @docs/style.md`, `(@deep/import.md)`, skips an email, code span, fence, root `README.md`.

## Renewals (wording unchanged, versions /1)

`repository-file-location`, `element-directory-contents`, `relation-model-directory-contents`, `invariant-example-target`, `map-example-target`, `glossary-example-target`: WAY-09@16b8026b → e360ca30; `skill-entry-points`: WAY-127@4439a64a → 69651fc7.

## Checks

Invariants guard exit 0, `0 error(s), 0 warning(s), 3 unchecked` (all from `none`). `stale_refs.py`: `references checked 397, stale 0`. Decisions guard 0 errors, 13 warnings. `--uses "repository instruction file"`: 8 uses (seven decision lines plus `foundations/invariants.md:2043`). Part map, glossary, facts guards 0/0.

## Meaning (Polish)

- instruction-file-imports: Żaden plik instrukcji repozytorium the-way (każdy śledzony `AGENTS.md` i `CLAUDE.md` oraz każdy śledzony plik Markdown, którego ścieżkę wymienia główny `AGENTS.md` albo `CLAUDE.md`) nie zawiera poza kodem w backtickach i blokami kodu importu `@ścieżka`; jedynym wyjątkiem jest pierwsza linia głównego `CLAUDE.md`, gdy brzmi dokładnie `@AGENTS.md`.
- root-claude-md-import: Jeśli w korzeniu repozytorium jest śledzony `CLAUDE.md`, jego pierwsza linia to dokładnie `@AGENTS.md` i nic więcej.

## WAY-33

1 `claude-code-imports` and *Rests on* — question 1; 2 level-1 links from WAY-129/132 pass both ends; 3 no failure mode at `agent-instructions` for what these detect — question 2; 4 part map edits of §5.1 still missing (owned by 1.7); 5 `skill-entry-points` fails until the entry points exist; 6 the term in its glossary meaning; 7 consistent: `outbound-link-reach`, `run-record-path`, `script-subprocesses`, WAY-60, WAY-73 for `root-claude-md-import`, not recovered invariants.

## Instruction for the checks (handed to the orchestrator)

Write `agent-instructions/test_instruction_files.py` (part `agent-instructions`), one test per invariant, `# invariant: instruction-file-imports/1` and `# invariant: root-claude-md-import/1`, run by the method; inputs the two entries and the glossary entry; assert every property with its literals (covered files by the test's own `git ls-files`; path boundary for `/` and `\`; characters before a counted `@`; `.` or `/` before the next whitespace; code-span and fence rules; the first-line exception; the byte-level start of `CLAUDE.md`); import nothing from `instruction-files/` or the files the change adds; expected values as literals; read-only afterwards (WAY-03); assessed (WAY-10); the deliberate break is the code reviewer's.

## Questions

1 add `claude-code-imports@5b9359fd` to *Rests on* (recommended by the agent); 2 add a failure mode to `agent-instructions` (recommended, optional); 3 accept excluding `./docs/x.md` (recommended).
