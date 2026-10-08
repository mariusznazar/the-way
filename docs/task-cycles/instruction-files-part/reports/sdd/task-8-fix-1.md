# Task 8 — fix round 1 (findings and the controller's ruling)

Task review (opus) of c1669c6..9b6e86f: documentation sources hold; the Cursor measurement is reported
as it ran. Fix in `instruction-files/tool_loading.md` only:

1. **Important — Codex "How to check" says the method is undocumented** (`:107-108`), but
   https://learn.chatgpt.com/docs/agent-configuration/agents-md gives
   `codex --ask-for-approval never "Summarize the current instructions."` (Verify step, Troubleshooting).
   Cite the page and use the documented command.
2. **Important — Codex source links on `blob/main`** (`:90`, `:104`); the spec requires a commit. Pin to
   a commit SHA (main was `137f25f6439ce8be758f15dbd1e1b297c6cd0c3b` at review) after checking that both
   files hold the cited lines at that SHA (fetch the raw files at the SHA).
3. **Important — the Cursor method omits `--trust`** (`:157`, `:200`): V1–V4 ran only with `--trust`
   (scratch directories). State it in both places, and that V5 was not given it.
4. **Important — `codex-skill-paths` cited beyond its fact** (`:100-101`): the fact holds the file path
   only; put "name, description" under the build-skills address, or narrow the clause.
5. **From ⚠️ — two "measured" skill-directory claims have no record in the material** (`:55`, `:106`,
   and in `## Measurements`: Claude Code does not read `.agents/skills/`; Codex does not read
   `.claude/skills/`). Rest each on its documentation fact (`claude-code-project-skills`,
   `codex-repository-skills` — read what they say) where the fact states it; otherwise mark it
   "not established". Remove the measurement description that no record supports.
6. Minor 5 — the Cursor "At session start" label: drop it or add "(measured, see below)".
7. Minor 6 — `~/.claude/rules/` sits under § User-level rules of the memory page; cite that section.
8. Minor 7 — `catalog_prompt.rs`: "Codex's skills prompt tells the model not to carry skills across
   turns unless re-mentioned".
9. Minor 8 — V1 and V2 share one fixture; V2 starts in its `sub/`.
10. Minor 9 — say the evidence of V1–V4 is the model's own list of markers (text output records no tool
    calls; the prompt forbade reading files).
11. Minor 10 — say that only one directory above was measured; how far up Cursor walks is not
    established.
12. Minor 11 — remove trailing spaces; wrap the long prose lines to ~100 columns.

Rerun the brief's checks (sources check, local-path grep, fact identifiers). Write/Edit tools only; no
path of this machine; no `.runs/`. Commit by path with the `Claude-Session:` line. Append "Fix round 1"
to `task-8-report.md` and reply with the short status contract.
