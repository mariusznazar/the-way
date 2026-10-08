# Report 16 — final whole-branch review c64a607..bb9f8ad (saved by the orchestrator from the returned text)

Read the whole package, spec with R12, N1–N5, ledger; ran checks in a throwaway clone in its scratchpad (deleted).
Confirmed: the gate test unchanged since 47dcbe3; nothing tracked in `docs/`, `.gitmodules`, `.the-way`; `.runs/` and
`.superpowers/` untracked (the second via `.git/info/exclude`); gate 98, agent-instructions 12, installation 17 OK;
`entry points are current`; guards `--base none`: decisions 0 errors 8 warnings, others 0 errors; fingerprints by
`relation-model/fingerprint.py` match every reference (WAY-127 4439a64a, WAY-09 16b8026b, WAY-27 0b40467e, WAY-44
2f2b6227); guards with `--merge-onto c64a607`: no stale relation, expected pre-main edits in place and three
`<request link>` placeholders (`decisions.md:279, 750, 3670`); `.gitattributes` `* text=auto eol=lf`, entry points
`i/lf w/lf`; all 11 entry-point frontmatters load with `yaml.safe_load`; "Installed globally", "global install",
"junction", "realpath", "Get-Item" only in the `assertNotIn` at `installation/test_install.py:116`; the only tracked
vault path `AGENTS.md:19`.

Strengths: approach A as written (tracked, generated, byte-identical pairs; gate check with its own `git ls-files`,
importing nothing from the generator, expected values from the sentence, WAY-69); R12 applied everywhere; both product
checks in place — Claude Code loads `.the-way/.claude/skills/` once a file there is read, Codex does not scan it from the
product root; check 2 fires in any product session whose working directory the agent knows, and Claude Code always tells
the agent its working directory; check 1 covers an agent that knows the entry point's path (the qualified name
`.the-way:the-way-*` gives it away); what is left is exactly the recorded not-detected failure mode
(`part_map.md:189`); a pin move needs no new step (installer reads skill and wrapper from the same `SOURCE` HEAD;
`installation/README.md:69-76`); the foundation describes the code (WAY-01; `skill-entry-points/1` lists exactly what
`entry_problems`/`problems` check; R12 wording pinned by `test_text_is_the_written_out_form`).

Important:
1. The gate passes an entry point whose frontmatter is not valid YAML; no failure mode records it.
   `agent-instructions/skill_entry_points.py:42, 114, 152`; `gate/test_skills_reach_the_way_sessions.py:98-110, 133`;
   `foundations/part_map.md:187`. The generator copies the raw text after `description:` and appends the suffix; the gate
   decodes YAML quoting before comparing. Ran: source `description: "Use for alpha."` → `description: "Use for alpha."
   Use this checkout's own the-way.`, `problems()` `[]`, PyYAML ParserError; source `description: Use for alpha: beta.`
   → `problems()` `[]`, PyYAML ScannerError. A strict loader may skip such a skill. Fix: the generator rejects a
   description that is not a safe plain scalar (starts with `"'&*!|>%@` or a backtick, or contains `": "` or `" #"`),
   the same property in `entry_problems`, one control case; fallback: record "entry-point frontmatter that a tool cannot
   parse — not detected" at `agent-instructions`. No current skill triggers it.
2. The WAY-27 / `outbound-link-reach` exception is limited by what is pointed at, not where the pointer stands
   (`decisions.md:731-734`, `invariants.md:469`): any tracked file may point at that place, e.g. a decision's *Origin*
   at the tasks file or a task description in `_zadania\` — against WAY-27's own violating example "*Origin* points to a
   private note" (`:746`); the colon now hangs "every entry carries its whole reasoning…" on the exception. Fix, e.g.
   WAY-27: "Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries
   its whole reasoning, … pointed to. The one exception is the place of its tasks, which only the `## Backlog` section of
   its root `AGENTS.md` names."; invariant: "…or into a private note collection, other than the `## Backlog` section of
   the root `AGENTS.md` naming the place of tasks."; renew the fingerprint.

Minor:
3. No instruction when the skill file is missing in the session's checkout (`skill_entry_points.py:170`; Claude Code ≥
   2.1.277 fallback; a 12th skill from `task/instruction-files`). Fix: "If `<path>` is absent there, stop and say so."
4. Gate and generator disagree on a tracked `SKILL.md` gone from disk (`gate/test_…:54-62, 168` vs `skill_paths`): after
   an unstaged `mv` the gate says "cannot be read" until staged. No fix needed (the invariant says "that git tracks").
5. WAY-127's rejected-option reason "in Claude Code a personal skill wins over a project skill" (`decisions.md:3686`)
   rests on behaviour no fact records (WAY-90); add a fact or reword to the task's reason (not relying on how tools
   resolve two skills of one name).
6. `installation/README.md:66-76` does not say that `.the-way` now carries `.claude/skills/` and `.agents/skills/`
   (products will see `.the-way:the-way-*`); one README sentence recommended.

Triage of the ledger: none must be fixed before merge except the quoted-description minor, raised to Important 1. U+FEFF
literal cosmetic (prefer `"﻿"`); multi-line plain description caught by the gate; argparse exit 2, empty
`sibling_names`, dry-run orphan and git-failure tests, mid-write OSError, one-line paragraphs, `TrackedEntryPoints`
wider, flow without coverage, terse wording, 105 columns, no `Projects:` line, narrow `assertNotIn` — accept. Ruling P1
sound; red commits 8be6a53..c12d4dd accepted, the request must state them; R12 fully applied; no `${CLAUDE_SKILL_DIR}`
check sound.

Recommendations: fix Important 1–2 before step 11 (the single independent assessment); step 12 owes the placeholder swap,
the point-6 commands with the N1 fix, the two blocked-draft questions; optionally Minor 3 and 6.

Declined to judge: `task-cycle/skill/SKILL.md` assuming a gitlink (spec §5.10); the installer's skill list (§5.10); tool
behaviour beyond the quoted facts; the watches' network runs; the request and the point-6 PowerShell (not yet existing);
removing the junctions; whether WAY-09 and WAY-27 should change meaning (reserved to Mariusz); bisectability of the red
commits; skill-list clutter in products.

Assessment: Ready to merge — with fixes (Important 1 and 2).
