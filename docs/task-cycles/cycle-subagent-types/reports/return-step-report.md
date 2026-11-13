# Return step report — cycle `cycle-subagent-types`

**Status:** done

**Commit:** `f1ff7d6` (on `b0ab508`). The worktree is clean.

## Return step (the fields of `task-cycle/record_template.md`)

- **Foundation compared with code:** I compared WAY-255, WAY-368, WAY-369, WAY-370, WAY-09, WAY-34, WAY-125, WAY-127, WAY-148, WAY-229, the part-map entries `task-cycle`, `agent-instructions`, `installation`, `installation-command`, and the invariants `skill-entry-points`, `derived-file-content`, `installation-claude-guidance` with the code at `b0ab508`.
  - WAY-368's binding sentences match the cycle's text (`task-cycle/skill/SKILL.md` paragraph on the types; `foundation_step.md` reading skills as files), the installer (`installation/install.py`: definitions copied unchanged from the commit, own-file rule, delete only its own, refusals) and the generator with its tracked copies test; its *Verification* examples hold (no `tools`, no `model` in a definition; the hour on the author's type only).
  - WAY-369 matches `task-cycle/test_agent_types.py` (no `omitClaudeMd`). WAY-370 matches the paragraph's fallback and `record_template.md` (the record row names the type or says why none).
  - WAY-255's exception matches the definition of the author (`cacheTtl: 1h` inside `experimental`) and `task-cycle/change/SKILL.md` section 3, which keeps the waits under about four minutes.
  - The part map: `agent-instructions` *Files* hold `.claude/agents/**`, which the tracked copies match; the sentences of `task-cycle`, `agent-instructions` and `installation-command` name what the code does; the *Depends on* of the parts hold (the installer and the generator read `task-cycle` files by path only; `agent_type_copies.py` imports `skill_entry_points.py`, one part; `elements/part-map` tests, which hold the imports of the-way to the map, pass).
  - Two things no longer matched and I corrected them: (1) WAY-370's *Rationale* said a Codex agent type "has no list of tools" and turns skills off "by their path", which no passage the entry cites says; it now says only that Codex turns off the skills of an agent one skill at a time, with a setting for each (`codex-agent-skills-config`). (2) the four decisions quoted their Claude Code and Codex sources directly, which the template's "Which facts are written" asks to be facts (below).
- **Decisions written or changed:** WAY-368, WAY-369, WAY-370 (the foundation step); WAY-255 (the foundation step; the return step changed only its *Based on*); WAY-09, WAY-34 (the foundation step). In this step: WAY-368, WAY-369, WAY-370, WAY-255 (*Based on* now names facts; WAY-370's *Rationale* corrected as above).
- **Invariants written or changed:** none. No task, decision or human sets a new rule that a commit can break and a test can see; the generator's test cites the existing `derived-file-content`, and the invariant `skill-entry-points` is about skills only.
- **Environment facts:** seven written, under the template's "Which facts are written" (each a behaviour of a tool the process uses whose change would call a decision into question; WAY-90):
  - `claude-code-subagent-skills-denied` (WAY-368),
  - `claude-code-subagent-cache-ttl` (WAY-368, WAY-255),
  - `claude-code-subagent-cache-ttl-credits` (WAY-255),
  - `claude-code-subagent-agent-directories` (WAY-368, WAY-370),
  - `claude-code-subagent-instruction-files` (WAY-369),
  - `codex-project-agents` (WAY-370),
  - `codex-agent-skills-config` (WAY-370).
  Each is one sentence with its source in the template's second form (a page without editions, with an archived copy that already existed and its date), the passage word for word, the date read 2026-11-13. The Claude Code facts cite `https://code.claude.com/docs/en/sub-agents.md` with the capture `20261019125207` (the latest capture of that address in the archive's index); the Codex facts cite `https://learn.chatgpt.com/docs/agent-configuration/subagents`, the address `https://learn.chatgpt.com/codex/agent-configuration/subagents` now redirects to, with the capture `20261028074900`. I made no capture: both were found by the archive's index of captures, and I did not call a "save" function. The mechanical check of "Write" held: for each of the 11 passages, with markup dropped and whitespace collapsed, I read the live address and the archived copy and the passage stands in both word for word (a script run in the scratchpad, not committed).
  The decisions' other citations (the prompt-caching page quoted in WAY-255) stand as they were; they are older and not this change's.
- **Glossary terms:** none. The words the change uses — "stage", "the one author", "agent type" — mean in the process what a reader who knows the field takes them to mean, and no sentence of the entries reads wrongly in that meaning (WAY-95); the same words stood in the foundation before this change.
- **Part-map changes:** `task-cycle`, `agent-instructions` (sentence and *Files*), `installation-command` (the foundation step); none in the return step.
- **Projected entries written whole or in part:** none (the task has none).
- **Rows of *Settlements to record* written:** row 1 → WAY-368; row 2 → WAY-369; row 3 → WAY-370 (all by the foundation step; the return step corrected the *Based on* of each and the *Rationale* of WAY-370).

## Commands (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors`, before and after the commit |
| `python -B gate/run_tests.py elements/common` | 0 | OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | OK (holds `cross-part-imports`) |
| `python -B gate/run_tests.py elements/decisions`, `elements/environment-facts` | 1 | "no test found in …": these directories hold no test; not a failure of the change |
| a script (scratchpad, not committed) comparing each quoted passage with the live page and the archived copy | 0 | all 11 passages found in both |
| `curl` of the archive's index of captures for the two addresses | 0 | latest captures `20261019125207` (Claude Code page) and `20261028074900` (Codex page) |

Not run: the full gate (the orchestrator's).

## Unread material

None of what the handoff names, beyond: `reports/whole-review-report.md` and `reports/fix-review-report.md` (the handoff gives their verdicts; I did not open them); the template's "Catalogues and obligations" section applies to no fact written here and I read only as far as the section "Which facts are written", "The sentence", "Source", "Changing a fact" and "Withdrawn identifiers".

## Searches not found or unclear

- The archive's index lists, for the Codex page at its old address, only captures with status 308 (redirects); the captures with status 200 are of the new address, so the entries cite the new address. The decisions' earlier quotes cited the old address, which no entry now cites.
- The archive holds an HTML capture of the Claude Code page of 2026-11-09 at the address without `.md`, whose text does not hold `cacheTtl`, `disallowedTools` or `omitClaudeMd`; I did not find out why (the capture may be a shell of the page rendered by a script). The entries cite the `.md` address and its capture of 2026-10-19, in which all passages stand.
- The 2026-10-19 capture predates the read date by 25 days; the passages stand in both, and the template asks for "the closest archived copy that already exists".
