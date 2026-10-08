# Report 02 — spec review (returned as text, saved by the orchestrator)

Verdict: **approved after fixes.** Structure holds (layout, four fixes, fingerprint lists, order of work, fact method). Three blocking findings change the drafts of foundation entries or the question put to Mariusz.

## Readings asked for

- Point 1, flattened layout (A1): defensible. Flattening alone brings the skill text into line with WAY-127's *violates* example; WAY-127's third binding sentence concerns the junction of point 9. Under option B the old `skill/` layout would also work, so A1 follows only from A or C. The request lists it as a deviation.
- Point 7, part one (watches instead of probes from measurements): defensible — WAY-81 allows a watch alone; `script-subprocesses/1` forbids a script starting `claude`/`codex`/`cursor-agent`; the task's Context calls existing watches "sondy". Still a narrowing; the spec puts it to Mariusz.
- Point 7, part two (facts only for what decisions rest on): close to forced by WAY-73. Rests on §5.2's premise that every behaviour a decision needs is documented — unverified (finding 5).

## Findings

1. **Blocking — the six decisions bind files outside the-way, never define "the-way's own instruction files", and the-way's current files break them at merge** (§5.5, §5.6, A9, A14). "In … those the skill … writes or judges" claims a state false for exactly the files the skill judges (WAY-05). Undefined which files count: if skills count, WAY-130 governs every rule in the-way's skills and *Scope* misses their parts (WAY-21). The-way's root `AGENTS.md` `## Skills` repeats README.md:90's generator command — WAY-128's own *violates* example. WAY-133 says "In the-way's own work" with a two-part *Scope*; `agent-instructions/README.md` keeps always-rules as instructions. Fix: bind the skill's output and the-way's own files; define the files once; set *Scope* from it; narrow WAY-133 to rules of instruction files; judge the-way's files against WAY-128–133 and record each breach.
2. **Blocking — option A, and C too, contradict WAY-34 in products that pin the-way** (§5.4, §5.9, Q-M1). WAY-34 *violates*: "a skill in a product session comes from a copy of the-way other than the pinned commit". The global link serves `loop2` (pins the-way; the skill's main test target) from the main checkout. A's rationale "serves repositories that pin no the-way" misdescribes use; §5.9 omits WAY-34; C does need a foundation change; A serves whatever the main checkout has checked out, uncommitted edits included, with no failure mode. Fix: add WAY-34; offer the variant where the skill stops in a product that pins the-way (the entry points' two git checks), or name the WAY-34 narrowing; re-weigh.
3. **Blocking — trust-boundary table misses file links found by the walk** (§4.6). A file found by `os.walk` that is a symlink (`AGENTS.md -> ~/.config/gh/hosts.yml`) is opened; fragments printed; the skill tells the agent to read every listed file — the high failure mode §5.1 records. Fix: an instruction file whose real path lies outside the root is not read and not listed; `INFO` "a link out of the repository"; test with a file symlink, skip where links cannot be made.
4. **Should fix — three thresholds for adding a rule** (WAY-130 "more than once", principles §7 "for one occurrence the smallest possible", skill §4.2 "not found"). Pick one, write it into all three; list for Mariusz.
5. **Should fix — §5.2 assumes every behaviour a decision rests on is documented**; `AGENTS.md`-without-`CLAUDE.md` is marked "measured" in the prototype; WAY-132 rests on it; dropping the fact would leave a tool-behaviour reason without a fact (WAY-90). Fix: fallback to an observation-source fact with *Method* `TODO`, naming the template's open `TODO — decision pending` as debt, or reword the decision.
6. **Should fix — `instruction-file-imports` ambiguous and reaches private notes**: "Markdown file the root `AGENTS.md` names" includes the vault backlog file (WAY-68 machine-dependence); "an `@` that starts a word" reads two ways. Fix: "that git tracks"; define the start (start of line, after whitespace, opening bracket or quote); `root-claude-md-import`: "whose first line is `@AGENTS.md` alone", and what holds with no root `CLAUDE.md`.
7. **Should fix — new reading steps take in secrets and untrusted text** (§4.2, §11, §5.1): configuration files with tokens; session records with arbitrary tool output; guard line deferred; no failure mode. Fix: read named settings by key search, never print whole files; search records by pattern; bring the one-line guard into scope or record the failure mode.
8. **Should fix — fix A's tests do not test its case; the directory rule is an unrequested widening**: the case path ends in `\`, so the directory rule alone passes the test; the rule lowers every dead directory pointer to `INFO`; per-path paragraph search can turn quadratic on a crafted 1 MiB paragraph. Fix: test with a file path; list the widening; one linear pass per paragraph or a cap, with a test.
9. **Should fix — network paths defined by examples; printed file names not escaped**: `/\host\share`, `\/host/share`, `\??\UNC\host\share`; NTFS names with U+202E. Fix: normalise `/`→`\`, a token starting `\\` or `\??\` never reaches the file system; escape and cut every printed path.
10. **Should fix — WAY-132 would have the skill rewrite files the installer owns** (`installation-command` surface; WAY-107). Fix: leave installer-owned files and blocks out of proposals; report the mismatch as a note on the installer.
11. **Should fix — WAY-133 lists a git hook among "every time" mechanisms**; WAY-03 *Rejected* "a local hook — one switch skips it". Fix: say a local git hook keeps a rule against slips, not against an agent that can turn it off; keep "hook gita".
12. **Should fix — WAY-131's rationale must say it takes `agent-run-variance` across publishers** (WAY-85).
13. **Should fix — Cursor measurement omits the case's link** (`C:\Storage\AGENTS.md` is a link to the global file). Add V4 with a linked `outer/AGENTS.md`; if not established, the request says point 5 is unmet.
14. **Should fix — §8 lacks the second WAY-33 search against the `foundations` tip, and the deliberate breaks of the two invariant tests** (WAY-08).
15. Minor — the skill hard-codes the-way decision numbers; describe how to find them instead.
16. Minor — README "Using the skills" (README.md:79–80) lists skills under `skill/`; update for the flat layout too.
17. Minor — no tracked test fixtures named `SKILL.md`, `AGENTS.md`, `CLAUDE.md`; build them in temporary directories.
18. Minor — the check script accepts `@AGENTS.md` on any line of any `CLAUDE.md`; requiring the first line costs one line.
19. Minor — WAY-129's "tools that do not import read the `@` line as plain text" is a tool claim with no fact (WAY-90); drop or add a fact.
20. Minor — counts in WAY-131 *Rejected* and WAY-132 *Rationale* (WAY-05); name the fallback for a page without an archived copy.
21. Minor — §4.6 heading "(point 9; …)" confusable with task point 9; §7 step 1 leaves `instruction-files/**` with no part (red part-map guard) until step 2 — say so.

## Checked and found sound

Fingerprint renewals: `WAY-09@16b8026b` in exactly the six invariants of §5.3; `WAY-127@4439a64a` only in `skill-entry-points`. WAY-100 fingerprint `e7a74a18` recomputed. Part entry dependencies, criticality, trust-boundary pattern (WAY-48 inside boundary, no external row). Invariant authorship and placement (WAY-69, WAY-73); order of work (WAY-01, WAY-03). Fixes B, C, D meet their cases with opposite-failure tests; fix C on the global file yields only `scripts/locations.json` as a new `WARN`. §8 matches `agent-instructions/README.md` apart from finding 14. No hidden trade-off principle. Each new fact named by a decision.

## Not checked

Live documentation and papers; the scratch reproductions; Windows network lookups of `\??\UNC\…`, `/\host\…`; the Cursor case; whether the private research note supports the addresses.
