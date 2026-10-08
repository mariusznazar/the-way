# Dispatch — foundation step reopened for the settlement of the independent assessment

Read the common rules first: `C:\Storage\repos\the-way-instruction-files-part\reports\sdd\foundation-common.md`
(boundaries, where to read skills — the process root `C:\Storage\repos\the-way-process` — search,
reporting). You are the foundation-correction agent: you change entries the cycle already wrote,
each through its element's skill from the process root, in the task worktree
`C:\Storage\repos\the-way-instruction-files-part`. Write only `foundations/glossary.md`,
`foundations/environment_facts.md`, `foundations/decisions.md`, `foundations/part_map.md`,
`foundations/invariants.md`. Commit nothing; never touch any test or code file.

The independent assessment's report and the orchestrator's settlement are at
`C:\Storage\repos\the-way-instruction-files-part\.runs\task-cycles\instruction-files-part\reports\assessment.md`
— read the observations and the "Settlement" table. Apply the settlement's foundation rows, in this
order (each entry written before the one that uses it):

1. **Glossary (row 3)** — `repository instruction file` also counts a `.claude/CLAUDE.md` and a
   `CLAUDE.local.md` that git tracks (Claude Code loads both at start — fact `claude-code-agents-md`
   names them). Keep the definition one sentence in WAY-96's form; re-read every use of the term
   (`python -B elements/glossary/format_guard.py --uses "repository instruction file"`) against the
   new definition and report each.
2. **Fact (row 11)** — `claude-code-agents-md/1`: add to its *Source* the passages of
   https://code.claude.com/docs/en/memory (§ AGENTS.md / § When Claude Code reads AGENTS.md) that say
   "In some sessions Claude can't read AGENTS.md, so import it from a CLAUDE.md there instead" and the
   advice to import rather than symlink on Windows — read the page now and copy them verbatim, with
   the archived copy the entry already cites if it holds them (otherwise follow the facts skill for
   a passage the archived copy lacks). The sentence does not change unless a passage requires it.
   Report the fingerprint before and after (WAY-78 says what it covers); if it changes, renew every
   `claude-code-agents-md@…` reference (WAY-132's *Based on*).
3. **Decision (row 11)** — WAY-132 *Rejected*: the clause "relying on Claude Code reading the shared
   file by itself — … the only sign … stops appearing without a word" is reworded to rest on what the
   fact now quotes (in some sessions Claude Code cannot read the shared file, and its documentation
   advises importing it from a file of its own). *Rejected* is outside the binding part; confirm the
   fingerprint stays 1242ac75.
4. **Part map (rows 4, 8)** — part `instruction-files`: the first two failure modes' severity becomes
   high (raising needs no reason, WAY-46); *Depends on* gains `installation`. Stage and run the guard.
5. **Invariant (row 1)** — `instruction-file-imports/1`: the counted `@` is every `@` that stands at the
   start of a line or right after whitespace, `(`, `[`, `{`, `"`, `'`, `“`, `‘` or `„`, whatever follows
   it (drop "and is followed, before the next whitespace, by a `.` or a `/`"); keep everything else of
   the sentence (the term, the exception for the first line of the root `CLAUDE.md` reading `@AGENTS.md`
   alone, the code-span and fence definitions, the naming-by-path definition), and make sure the
   population follows the changed term. The sentence must still state every property its check will
   assert, with its literals (the check's author receives only the sentence, its method and the glossary
   entry — WAY-69). The version stays /1 (edit in place before `main`); WAY-129 is not changed (its
   sentence already forbids every `@` import). Do not change `root-claude-md-import`.

After all five: run the five guards (`--base none`, `--merge-onto none` where available) and
`python -B -I .runs/stale_refs.py`; run the WAY-33 search for each changed entry and return its
findings. Return as the text of your final message: each change (before → after), the fingerprints that
changed, the guard outputs' last lines, the stale-refs line, one Polish meaning sentence per changed
entry, the search findings, and every question. Also return, separately, the exact new sentence of
`instruction-file-imports/1` and the glossary entry — they go to the check's author.
