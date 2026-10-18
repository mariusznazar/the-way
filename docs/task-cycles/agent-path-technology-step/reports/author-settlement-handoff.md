# Settlement changes handoff — author, turn 4

Worktree and branch as before. Input commit: `9587b0d`. Make exactly the changes [assessment-settlement.md](assessment-settlement.md) marks **Apply**, nothing more:

1. A1 — `foundations/decisions.md`, WAY-166 *Relations*: add `narrows WAY-137@86b2a30d` (recompute WAY-137's fingerprint with `relation-model/fingerprint.py` and use the value it gives; report it if it differs). Confirm the `narrows-pairs` rule and the decisions guard hold.
2. A5 — WAY-121 *Review when*: drop the first condition ("a project lists a matter … for the behaviour the project brings"); keep the second condition and `check by: 2027-03-31`, reworded only as grammar needs. Confirm WAY-121's binding fingerprint does not change; if it does, renew every link to it.
3. A7 — `project-level/technology/SKILL.md` step 0: the bullet "Where it holds a list, …" reads: "Where it holds a list, first take the look step 1 gives at the logs, the interface and the development data, add each matter it finds missing as an item ending `— open`, and, where it adds one, show the list again as step 1 does before going on (WAY-121). A definition the gate has approved does not come back to this step for these matters."
4. A8 — same file, step 2.5: cut "; that tie rule serves a place to run alone" (keep the sentence end correct).

Checks, with full output under `reports/` (prefix `settlement-`) and exit codes: decisions format guard (`--base none --merge-onto none`), `python -B gate/run_tests.py elements/decisions`, `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py gate`, entry points check, `git diff --check 77c8a8b..HEAD`; manual fingerprint count, 0 stale.

Write boundary as before; one commit by explicit paths, English message. Append a section "Assessment settlement (turn 4)" to `reports/author-return.md` with the commit, changed files and line counts for `9587b0d..HEAD`, commands, exit codes, output paths, and any concern. Short return message as before.
