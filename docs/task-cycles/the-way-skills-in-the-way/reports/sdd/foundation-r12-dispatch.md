You are the foundation-correction agent of one the-way task cycle: the foundation step is reopened for one amendment.
The orchestrator dispatched you. Mariusz delegated intermediate choices to the orchestrator; questions go to the
orchestrator; nothing you write is his approval.

Read first: amendment R12, `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md` §10
(end of the file), and the finding behind it, `…\reports\report_13_review_task3.md` ("Important 1"). For the current
entries read `…\reports\report_06_foundation_1_1.md`, `report_08_foundation_1_3.md`, `report_09_foundation_1_5.md`,
`report_10_foundation_1_6.md`.

Make these changes, each following its element skill from the PROCESS ROOT `C:\Storage\repos\the-way-process\elements\<element>\skill\SKILL.md`
with the files it names (skip "Installed globally … resolve it first"; never a global skill, never the task worktree's
copy of a skill), in this order, in the task worktree `C:\Storage\repos\the-way-skills-self`:

1. `foundations/environment_facts.md`, `claude-code-project-skills/1` (environment-facts skill): the sentence and *Source*
   gain the `/cd` behaviour — the page's passage "When you move the session with /cd on v2.1.246 or later, Claude Code adds
   the new directory’s project skills." (re-read it with `probes/fact_probes.py` `page_runs` at
   https://code.claude.com/docs/en/skills; typographic ’). Edited in place before main; the version stays `/1` unless the
   skill requires otherwise; the watch (`probes/claude-code-project-skills/`) reads the *Source* passages, so rerun it.
2. `foundations/decisions.md`, WAY-127/1 (decisions skill): the binding sentence says the entry point reads its skill from
   the checkout or worktree the session works in — where it was started, or where it was last moved — instead of "was
   started in"; the *Rationale* sentence on the start directory follows; *Based on* carries the fact's new fingerprint.
3. `foundations/invariants.md`, `skill-entry-points/1` (invariants skill): the sentence is UNCHANGED; *Derives from* carries
   WAY-127's new fingerprint. Confirm the sentence names no "start directory" wording (it should not).
4. `foundations/part_map.md`, `agent-instructions` (part-map skill): the not-detected failure mode says "the session's
   working directory" instead of "the session's start directory".

Fingerprints: `python -B -I .runs/stale_refs.py <NAME>`; `python -B -I .runs/stale_refs.py` compares every reference
(must end `stale 0`). Run the guards of the four files (`--base none`, `--merge-onto none` where available) and
`python -B gate/run_tests.py probes/claude-code-project-skills --record .runs/fact-claude-code-project-skills.jsonl`.
Search the whole foundation (WAY-33) for any other "started in" / "start directory" wording this amendment reaches and
report it (change it only in the four files above). Commit nothing; write only those four files.

Return as text: each change as written, old and new fingerprints, the guard and watch results, the comparison's last
line, search findings, and one Polish sentence per changed entry (WAY-114).
