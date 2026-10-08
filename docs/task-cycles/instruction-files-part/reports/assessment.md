# Independent assessment (WAY-10) — returned as text, saved by the orchestrator

- Assessed range: dd0c234..2d9c32e (the change after the merge of `foundations`), 42 files (`git diff --name-only dd0c234..2d9c32e`).
- Assessor: general-purpose subagent on **fable** (claude-fable-5-1); authors of the assessed entries and checks: opus (foundation entries, invariant checks), the code: sonnet and haiku.
- Material given: `git archive 2d9c32e` and the diff, nothing else (no spec, plan, task, reports, prompts or commit messages); the critique skill from the process root.

## What the assessor ran (no concern unless noted)

Fingerprints recomputed for every value the change writes (WAY-09@e360ca30, WAY-127@69651fc7, WAY-129@1336c32b, WAY-132@1242ac75, WAY-100@e7a74a18, WAY-44@2f2b6227, WAY-10@db68de1c, ten facts) — all match; no stale fingerprint remains. Five guards 0 errors (8 placeholders, 5 pre-existing overdue check-by dates). `agent-instructions` 18 OK, `gate` 98 OK, `instruction-files` 104 OK (5 skipped). Deliberate break: `@agent-instructions/README.md` in `AGENTS.md` and `# Title` above `@AGENTS.md` — both checks fail. Six watches pass on live sources; WAY-130's passages stand. Each new fact named by a decision; sentences say no more than their passages; WAY-85 handled. `principles.md`, `SKILL.md`, `tool_loading.md` agree with WAY-128–133 where they cite them.

## Observations

1. The imports invariant counts only an `@` followed by `.` or `/` (`invariants.md:2043`; test `AFTER_AT` :39, :134; script `AT_IMPORT` :52, :507); the memory page the fact `claude-code-imports` cites says a bare `@README` outside backticks imports the file; fixture line 12 (`@nothing here`) fixes the gap as intended. Do: count every `@` at a line start or after whitespace/opening marks, or record the narrowing in the fact.
2. The root-import test asserts the population (`AGENTS.md`, `CLAUDE.md`, `agent-instructions/README.md`) and a tracked `CLAUDE.md` before its check (`test_instruction_files.py:306-314`); renaming the README or untracking `CLAUDE.md` (sentence vacuously true) records `fail` (WAY-61). Do: drop the control there; consider "and git tracks a root `AGENTS.md`" in the sentence.
3. The term leaves out `.claude/CLAUDE.md` and `CLAUDE.local.md` (loaded at start, take imports; named by `claude-code-agents-md`); `.claude/rules/*.md` without `paths` loads at launch; the script's `MAIN_NAMES` covers them — the instruments disagree. Do: add the two files to the term, or accept knowingly.
4. Severity of the part's first three failure modes "low" against the scale (products pin the check script and the loading account). Do: raise the first two to high.
5. Six `derives from WAY-100@e7a74a18` relations — the six are the adopting decisions rather than ones serving WAY-100; precedent WAY-120; a rewording of WAY-100 flags seven dependants. Do: `Relations: none`.
6. The `@AGENTS.md` first-line form stands in WAY-129 and WAY-132. Do: WAY-129 "other than the import WAY-132 sets". Low.
7. Which principles bind is not marked (`principles.md:6-7`; the skill applies sections 5 and 6 as rules). Do: one sentence that uncited sections are the skill's method, offered as proposals. Low.
8. `instruction-files` *Depends on* lacks `installation` (the skill relies on the installer's markers, `install.py:39-42`); `agent-instructions → instruction-files` checks nothing. Do: add `installation`; the other row can go.
9. WAY-09 keeps "root agent instruction files" beside the term (WAY-97). Low.
10. Script and invariant disagree on `-@dash.md`; which matches Claude Code is not established. Do: note in `tool_loading.md`.
11. WAY-132 *Rejected* ("the only sign … stops appearing without a word") rests on no cited fact; the memory page says "In some sessions Claude can't read AGENTS.md, so import it from a CLAUDE.md there instead". Do: add the passages to `claude-code-agents-md` (Source) and rest the rationale on them. Low.
12. Author names in fact sentences but not in passages (precedent "Zhou et al."); no change.

## What can be cut (assessor)

The six `derives from WAY-100` relations; `instruction-files` in `agent-instructions`' *Depends on*; the positive-control assertions in the root-import test; the duplicate `@AGENTS.md` form in WAY-129. Nothing else.

## Not checked (assessor)

WAY-69 authorship; tool behaviour beyond documentation (bare `@name`, `-@x.md`, `~~~` closing a backtick fence); the "measured" statements; frequency (no session records: the invariants rest on documented behaviour, zero recorded cases); the five skipped tests; what the guards leave unchecked without a main branch; Mariusz's renewed acceptance of WAY-09 and WAY-127.

## Settlement (by the orchestrator)

| # | Settlement | Applied by |
|---|---|---|
| 1 | accepted: `instruction-file-imports` counts every `@` at a line start or after whitespace or an opening mark, whatever follows (the-way's files hold no mention; the population is the-way's own files); its check rewritten by a check author from the new sentence (WAY-69); the advisory check script keeps its narrow form and says so (a bare `@name` in another repository is often a mention) | foundation-correction agent (sentence), check author (test), fix agent (script docstring) |
| 2 | accepted: the root-import test asserts only what its sentence states; the population control stays in the imports test | check author |
| 3 | accepted: the term also counts a tracked `.claude/CLAUDE.md` and `CLAUDE.local.md`; its uses re-read | foundation-correction agent (glossary skill) |
| 4 | accepted: the first two failure modes of `instruction-files` raised to high (raising needs no reason, WAY-46) | foundation-correction agent (part-map skill) |
| 5 | rejected: the six adopting decisions keep `derives from WAY-100` — the precedent WAY-120 does the same, and a change to when a borrowed practice binds should flag every adoption for review (WAY-31) | — |
| 6 | rejected: WAY-129 (how a file points to another) and WAY-132 (which file carries shared instructions) answer different questions; the line is where they meet, and a cross-reference in a binding sentence would tie WAY-129's fingerprint to WAY-132 | — |
| 7 | accepted: one sentence at the head of `principles.md` — sections that name no decision are the skill's method, offered as proposals, not rules binding a repository | fix agent |
| 8 | accepted in part: `instruction-files` *Depends on* gains `installation`; `agent-instructions → instruction-files` stays — the entry-point generator reads `instruction-files/SKILL.md` | foundation-correction agent (part-map skill) |
| 9 | rejected: "root agent instruction files" in WAY-09 names the root `AGENTS.md` and `CLAUDE.md`, a narrower set than the term (which also counts the files they name); ordinary meaning, as settled at writing (Q15.6, Q19.5) | — |
| 10 | accepted: `tool_loading.md` notes that whether Claude Code imports an `@` after `-` is not established | fix agent |
| 11 | accepted: the passages added to `claude-code-agents-md`'s *Source*; WAY-132 *Rejected* rests on them | foundation-correction agent (facts and decisions skills) |
| 12 | no change (precedent) | — |
| Q31 | carried from the final review: the check script's docstring says link targets are judged on Windows only; the two tests stub `lexists` | fix agent |
