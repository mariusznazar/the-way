# Report 03 — design agent, spec revision (saved by the orchestrator from the returned text)

Revised `spec.md` under R1–R11; stopped before `writing-plans`. Own fix: the product check uses
`git ls-files --stage -- ':/.the-way'` (`:/` = repository top, works from a subdirectory; tested in the worktree).

- R1 entry point: tool-neutral, byte-identical; two product checks — submodule check in the folder holding the
  entry point; the start repository pins `.the-way`. Root from the session's start directory. Line to skip any
  link-resolving instruction.
- R1 fact question: Codex page says its skill list "includes each skill's file path" → a fact. Claude Code's page
  states neither that the agent gets the skill's path nor its start directory → gap stated in a failure mode,
  "not detected", no fact.
- R2 point 5: `## Backlog` carries the vault path; branch proposes an exception inside WAY-27's binding sentence,
  the matching edit of `outbound-link-reach`, renewed WAY-27 fingerprint. Exception chosen over `narrows` from
  WAY-107: WAY-27 binds this repository alone; `narrows` would change WAY-107 for every product while the invariant
  would still need editing. Personal-instructions edit removed.
- R3 WAY-09 edited in place to name `.claude/skills/` and `.agents/skills/`; fingerprint renewed in six invariants;
  "root entry points" argument dropped.
- R4–R6: `Part: every`, `Derives from: WAY-127@<fingerprint>`, `Correction: none`; control test of `problems()`;
  four facts after `claude-code-path-rules`, watches, archived copies (Claude Code: none found yet).
- R7–R11: criterion 2 reworded; local path at `decisions.md:3565` corrected; sibling-order parenthesis dropped;
  WAY-48 position stated with eight installer tests covering its inputs; Codex check added; removal loop
  check-and-continue.
- §7 lists every entry; two change the meaning of an approved decision: WAY-09 (question 1), WAY-27 (question 2),
  `outbound-link-reach` following question 2.

Changed sections: header, §1, §2, §3 A, §4.2–§4.7, §5, §6, §7, §8, §9. Self-review: no placeholders except
`<fingerprint>`; §4.2, §4.4, §7 agree; one plan; the Codex "file path" quote came through a summarising fetch —
read verbatim before writing the fact.
