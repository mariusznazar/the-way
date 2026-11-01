# Return step: skipped-test-names

**Status:** done. Commits: none (nothing needed correcting).

- Foundation compared with code (at 546eb52): WAY-16, WAY-63, WAY-215, WAY-217; invariant `gate-exit-code`; part map `## gate` and `## test-runner-command`; `agent-instructions/README.md` "Check the change". None says anything about the content of the runner's report beyond the exit codes, the closing count line and the unittest OK line, all unchanged by the code (skipped lines come before the closing lines, exit codes untouched; the README's "ends with a line counting the tests" still holds). The `gate-exit-code` test still passes.
- Decisions: none written or changed.
- Invariants: none written or changed.
- Environment facts: none (the change rests on no outside source).
- Glossary terms: none.
- Part-map changes: none (`test-runner-command` promises name, argument and exit codes, not report content).
- Projected entries: none (the task carries none).
- Rows of *Settlements to record*: none.
- Searches not found or unclear: none
