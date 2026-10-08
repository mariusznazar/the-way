# Report 04 — spec re-check (spec reviewer, returned as text, saved by the orchestrator)

Verdict: **approved after fixes.** Of findings 1–21: 14 resolved, 6 partly (1, 2, 6 minor, 8 minor, 20 and via N-items), 13 not resolved (V5). Two new blocking problems, both cheap.

## New problems

- **N1 (blocking):** the definition of "the-way's own instruction files" stands in WAY-128's binding sentence; WAY-95: "A word's definition stands in the glossary alone"; the phrase means something a reader would not assume (excludes skills); WAY-129–133 `derives from WAY-128` only borrow the definition, which WAY-32's "a higher decision this one serves" does not fit; A16 admits five decisions flagged by any rewording of WAY-128. Fix: a glossary term through `record-glossary-term` ("<term> is <genus> that <difference>", WAY-96), decisions use it (WAY-97), drop the `derives from` relations, revise §5.8, A16, O6.
- **N2 (blocking):** the R2 product check runs `git ls-files --stage -- ':/.the-way'` in the session's working directory, but this skill names its target repository; sessions start in the vault and work on `loop2` (task point 3, notes line 39) and would judge `loop2` with the main checkout's copy (WAY-34); a session in `loop2` judging the global file would stop for no reason. Fix: `git -C <repository under review> ls-files --stage -- ':/.the-way'`; skip for `--file`-only targets; outside any git repository = no product; the WAY-127 narrowing's "in a product that pins the-way" means the repository under review.
- **N3 (should fix):** A17 overlooks the check script: through the link the main checkout runs `check_instructions.py` (the trust boundary) on untrusted repositories; a half-finished edit runs with no human acceptance. Fix: the junction targets a dedicated detached worktree at the merged `foundations` tip, or record a failure mode.
- **N4 (should fix):** V5 in the task worktree: ignored `.runs/` holds copies of private notes an ask-mode session may read; `git status` does not show ignored files; the answer carries the global `CLAUDE.md`'s content to Cursor; a heading in the answer does not show the route (`C:\Storage\AGENTS.md` vs user rules). Fix: run V5 in `C:\Storage\repos\the-way-process`; negative control from a directory not below `C:\Storage`; name the global file's content leaving the machine in O2; add `--sandbox enabled` (`-p` "has access to all tools, including write and shell"; `--mode ask` exists).
- **N5 (should fix):** WAY-133 *complies* praises the regenerate line that §5.0 counts against WAY-128; §5.0 judges "a mechanism that runs without the agent choosing to" two ways. Fix: another example; one reading.
- **N6 (minor):** `instruction-file-imports` states the present state of every tracked file while WAY-129 binds only what a change adds. Fix: WAY-129 states the present state ("the-way's own instruction files hold no `@` import other than …"), true today.
- **N7 (minor):** "cite the page without an archived copy … say so in the request" still breaks WAY-80. Fix: a missing capture is the facts skill's question or path 1 of §5.2.
- **N8 (minor):** WAY-129 "adds … a file for an agent to read as its path" reads as adding a file; WAY-131's "a change … that states a rule works" unclear; fix-A timing test machine-dependent — compare two input sizes or count operations; path 1 of §5.2 reruns `claude -p` (credentials) — belongs in O2.

## Status table (1–21)

1 partly (N1, N5) · 2 partly (N2, N3) · 3–5 resolved · 6 resolved (N6 minor) · 7 resolved · 8 resolved (N8 minor) · 9–12 resolved (10: markers checked against `installation/install.py:39–42`) · 13 not resolved (N4) · 14–17 resolved · 18 resolved (edge: a `CLAUDE.md` with no `AGENTS.md` beside it and `@AGENTS.md` on a later line reported by neither check) · 19 resolved · 20 partly (N7) · 21 resolved.

## Points named

§5.0's reading that existing lines are not bound is consistent with WAY-01. The R2 order is right (a copy in `.the-way` governs; the main checkout defers); only the directory is wrong. The WAY-127 narrowing is acceptable once N2 is fixed; its *Verification* should gain a complies/violates pair for the link and the product check.

## Not checked

Whether `--mode ask` keeps Cursor from reading or indexing ignored files; other routes for the global file into Cursor; the part-map guard on the fifth failure mode; the facts guard on a page without an archived copy; live pages.
