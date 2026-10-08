# Cursor measurement, 2026-10-08

Release: 2026.10.01-e373342 (cursor_version.txt). Account: the one logged in on this machine.
Command: `cursor-agent.cmd -p [--trust] --mode ask --output-format text "<P>"`, one fresh session per variant, fixtures in scratch (marker phrases only).

Deviations from the brief: (1) `--sandbox enabled` fails on Windows ("Sandbox requires macOS or Linux"), so it was dropped (mode ask is read-only). (2) Without `--trust`, V1-V4 stopped on workspace trust (exit 1), so V1-V4 were rerun with `--trust` (scratch dirs). V5 never got `--trust`.

| Variant | exit | answer | positive control (MK-ROOT-7000 + "# Repository file") | verdict |
|---|---|---|---|---|
| V1 root, file above outside git | 0 | MK-ROOT-7000, MK-OUTER-7001, # Repository file, # Outer file | yes | outer file loaded |
| V2 start in sub/ | 0 | same four | yes | loaded from a subdirectory |
| V3 directory above is a git repo | 0 | same four | yes | loaded |
| V4 file above is a symlink | 0 | same four | yes | link followed |
| V5 process root, no --trust | 1 | workspace trust prompt | n/a | NOT RUN |

Negative control for V5 (global file absent from V1) could not be evaluated: V5 did not run.
Process root `git status --short --ignored` before: empty; after: empty; identical (cursor_V5_status_before/after.txt).
No cursor-agent process remained (tasklist).
Task point 5: met for a plain file and for a linked file in a scratch setup; the real case (link two directories above, user's global file) is not established.
