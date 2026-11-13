PASS f1ff7d6db3f38471e3df6bbece770795c27509fc

# Review of the return step's commit, cycle `cycle-subagent-types`

Range `b0ab508..f1ff7d6` (one commit, `f1ff7d6`, "Write the sources of the agent type decisions as environment facts"), variant "the return step's commits". `git rev-parse HEAD` printed `f1ff7d6db3f38471e3df6bbece770795c27509fc`, as the handoff gives. Two files changed: `foundations/decisions.md` and `foundations/environment_facts.md`. I changed no tracked file and made no commit; my scratch files lie in the session's scratchpad.

## Findings

Blocking: none. Minor: 2 (one in scope, one outside the commit's duty). Out of scope: 1 (the second Minor).

### Minor 1 (in scope) — WAY-370 *Rationale* says "with a setting for each", which no cited passage says

- Place: `foundations/decisions.md` WAY-370, *Rationale*, second sentence (the lines after "probe showed a gain there.").
- The new text: "Codex turns off the skills of an agent one skill at a time, with a setting for each, so the list kept in the process would grow with every skill added to the-way and need care in each change."
- What the cited passage (`codex-agent-skills-config`) says: "Disable individual skills with skills.config or bundled skills with skills.bundled.enabled = false." That names one setting, `skills.config`, that disables individual skills. "One skill at a time" holds. "A setting for each" reads as one setting per skill, which the passage does not say. The page's other sentence (under "Custom agent file schema"): "Skills inherit from the parent, and a custom agent can disable individual skills with skills.config" says the same and no more.
- The second half ("the list ... would grow with every skill ... and need care in each change") is the process's own reasoning (the human's answer to question 4 of the task), not a claim about Codex. It stands as a reason, so I raise nothing against it.
- Why it matters: the handoff asks that the corrected *Rationale* say only what a cited passage says. The overreach is slight and changes no binding sentence, so a reader is not misled about what to do. Suggested wording: "Codex turns off the skills of an agent one skill at a time, with `skills.config`, so ...".
- Grade: Minor (a departure of a rationale clause from the fact it paraphrases; the fact entry itself and the binding sentence agree with the source).

### Minor 2 (outside the commit's duty, so out of scope) — WAY-255 *Based on* still quotes the prompt-caching page

- Place: `foundations/decisions.md` WAY-255, *Based on*, first three quotes (`https://code.claude.com/docs/en/prompt-caching.md`, read 2026-10-27).
- The commit turned the two `sub-agents.md` citations of WAY-255 into fact identifiers but left the three `prompt-caching.md` passages quoted. WAY-90 asks for a fact entry for every citation about the behaviour of a tool the process uses whose change would call the decision into question. "Subagents ... get five minutes even on a subscription until you choose a longer one" is such a citation, and the new binding clause ("falls back to five minutes where a subscription spends usage credits") needs it together with `claude-code-subagent-cache-ttl-credits`.
- These quotes were in WAY-255 before this task; the return step's report says so ("older and not this change's"). The template's duty for the return step is to write "each source outside the product that the change rests on and the foundation does not yet hold": the foundation holds this one, as a quote. So I do not block on it. A later change of WAY-255 or the review of the foundation may turn them into facts.
- Grade: Minor, out of scope.

## What I checked, and held

- **Form of each of the seven facts** against `elements/environment-facts/template.md`: each has an identifier of lower-case words joined by hyphens that names what the fact is about (no value, no edition); one sentence; one `Source` field in the template's second form (a page without editions: address, `(archived: <address>, <date>)`, `§ <place> — "<passage>"`, further passages joined by ` · `, `read <date>`); the same layout as the existing entries (`claude-code-project-skills`, `codex-skill-paths`). The entries stand after the last fact and before "Withdrawn identifiers". The sentences say no more than their passages: for example `claude-code-subagent-cache-ttl-credits` says "ignores the `1h` cache lifetime ... while the user's Claude subscription is using usage credits"; `claude-code-subagent-instruction-files` takes "without the user, project and local `CLAUDE.md` files in its initial context" and "v2.1.271 or later" from the table cell. Version numbers in two sentences are the tool's own requirement for the field, as the sentences of `claude-code-agents-md` do.
- **Each quoted passage word for word.** I fetched `https://code.claude.com/docs/en/sub-agents.md` and `https://learn.chatgpt.com/docs/agent-configuration/subagents` (both HTTP 200) and the archived captures the facts name (`web.archive.org/web/20261019125207id_/...` and `.../20261028074900id_/...`, both HTTP 200). I dropped markup, collapsed whitespace and looked for each of the 11 passages in each of the 4 texts: all stand in all four (the Codex "Disable individual skills ..." passage stands once markup is dropped without inserting a space at the `<code>` tags, which is how a reader sees it). The Claude Code page has straight apostrophes in `subagent's requests` and `scope's first agent file` as the facts quote them (checked on the raw bytes of live and archived copies).
- **Places (`§`).** Claude Code page: "Preload skills into subagents" (a heading), "Frontmatter reference" (a heading; the table rows of `omitClaudeMd` and `experimental` and the sentence "Write `cacheTtl` inside ..." stand under it) and "Write subagent files" (the note with the watcher sentence) all exist. Codex page: the h2 "Custom agents" holds all three passages; "Disable individual skills ..." stands in its h3 "Custom agent file schema", so the place named is the enclosing section, not the narrowest one. I did not count this as a finding.
- **Closest archived copy.** The archive's index (CDX) lists `20261019125207` as the latest capture with status 200 of the `.md` address and `20261028074900` as the latest with status 200 of the Codex address (the fetches of the index were made now, on 2026-11-14), so each is the closest existing copy the template asks for.
- **Decisions' *Based on* name facts that exist, and each fact is named.** WAY-255: `claude-code-subagent-cache-ttl`, `claude-code-subagent-cache-ttl-credits` (after its three quoted passages); WAY-368: `claude-code-subagent-skills-denied`, `claude-code-subagent-cache-ttl`, `claude-code-subagent-agent-directories`; WAY-369: `claude-code-subagent-instruction-files`; WAY-370: `codex-project-agents`, `codex-agent-skills-config`, `claude-code-subagent-agent-directories`. Every new fact is named by at least one decision, and `foundation_check.py` reports 0 errors.
- **Nothing in the decisions went beyond the task.** The diff changes only the *Based on* of WAY-255, WAY-368, WAY-369, WAY-370 and the second *Rationale* sentence of WAY-370; no binding sentence, *Verification*, *Relations*, *Rejected* or figure was edited. WAY-05: the changed prose names no file, script or count and states no tool behaviour of the process. WAY-27: the new entries point only to public pages and their public archived copies; nothing points to a private note. WAY-369's "10.5 thousand ... a figure whose conditions ... are not recorded" and WAY-255's percentages stand as before and are in the task's *Context*.
- **WAY-370's corrected *Rationale*.** The removed claims ("has no list of tools", "by their path") rested on no cited passage (the Codex page has no passage on a tools list and no passage on turning skills off by path), so removing them was a correction the return step may make; the *Rejected* sentence "the list of skills they turn off grows with every skill" is the human's reason (task question 4), unchanged. The one clause that still goes beyond the passage is Minor 1.
- **No change of meaning.** The binding sentences of the four decisions are identical before and after; the two Codex-related *Rationale* claims removed are explanatory only.
- **Facts against the code.** `task-cycle/agent-types/the-way-author.md` has `disallowedTools: Skill` and `experimental:` / `cacheTtl: 1h`; `the-way-stage.md` has `disallowedTools: Skill` and no `experimental`; `task-cycle/test_agent_types.py:68` asserts `omitClaudeMd` is not a field. These match the facts and decisions.
- **Whitespace and line width.** `git diff b0ab508..f1ff7d6 --check` exits 0; no added line of `decisions.md` is over 100 characters.

## Checks run (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` in the worktree | 0 | `f1ff7d6db3f38471e3df6bbece770795c27509fc` |
| `git log b0ab508..f1ff7d6 --oneline`; `git diff b0ab508..f1ff7d6` and `--stat`, `--name-only` | 0 | one commit, two files |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `git diff b0ab508..f1ff7d6 --check` | 0 | no whitespace error |
| `curl -sL` of the two live pages and of the two archived captures (`id_` form) | 0 | HTTP 200 each |
| `python -I check.py` (scratchpad `...\scratchpad\rv\check.py`: drops markup, collapses whitespace, looks for each of the 11 passages in the 4 texts) | 0 | 44 of 44 found once the Codex HTML is read without a space inserted at `<code>` tags (the first run showed "MISSING" for one Codex passage in two texts only because of that spacing; `ctx.py` showed the passage text in both) |
| CDX queries of `web.archive.org/cdx/search/cdx` for the two addresses | 0 | latest status 200 captures `20261019125207` and `20261028074900` |

Not run: the full gate (the cycle's own run), tests of `elements/decisions` and `elements/environment-facts` (no tests there, as the author's report says).

## Declined to judge

- That the exact version numbers of the facts hold on the Claude Code the cycle runs (v2.1.248 and v2.1.271 vs the probe's 2.1.322): the facts say what the page says, which is what a fact is.
- Whether `cacheTtl: 1h` or omitting `tools` works in practice: the cycle's probe and the tests of the change cover it; this commit writes sources only.
- The probe figures in WAY-368, WAY-369 and WAY-255 (36,711 / 21,759 tokens, 10,470 / 123 / 4,786, the percentages): unchanged by this commit; task *Context* gives them.

## Reaches beyond the dispatch

- the author's private rules files for scripts and for searching, before writing the scratch script (user instruction).
- `elements/decisions/template.md` (lines about *Based on*) and `elements/common/rules.md` (the "Identifiers" section by grep): to check that *Based on* may mix fact identifiers and quoted sources, and the identifier form.
- Existing facts `claude-code-project-skills` ... `cursor-agents-md` in `foundations/environment_facts.md` (lines 108 to 160): to compare the form with the new entries.
- `task-cycle/agent-types/*.md` and `task-cycle/test_agent_types.py:68`: to check the facts against the code.
- The Web Archive's CDX index and the live pages: to check "closest archived copy that already exists" and the passages (the handoff asks for the pages; the index is my addition).

## Unread material

- `elements/environment-facts/skill/read.md`, `decide_entry.md`, `draft.md`, `write.md` and `projected.md`: not read. I read `elements/environment-facts/skill/SKILL.md` and `template.md` whole; the five files are what the writer of a fact reads at its steps, and I checked the entries against the template and the author's own claims instead. The author's report says it followed "Write" mechanically; I re-did that check myself (above).
- `task-cycle/record_template.md` (named in the author's report): not read; not needed for the review of the two files.
- `elements/common/rules.md`: only the "Identifiers" and "Withdrawn identifiers" parts (by grep) read, not the whole file.
- The other entries of `foundations/environment_facts.md` and `decisions.md`: only the ones the handoff names, and the existing facts above for form. Whole-file reading is not asked of this variant.
- The `prompt-caching.md` page cited by WAY-255 (read 2026-10-27, outside this commit): not fetched.
- `reports/whole-review-report.md` and `reports/fix-review-report.md` of the cycle: not read (not named by the handoff).

## Searches not found or unclear

- The archive's capture of the Codex page at its old address `https://learn.chatgpt.com/codex/agent-configuration/subagents` (the one the earlier decisions cited): the author reports only redirect captures. I did not search it again; the new facts cite the address the old one redirects to, and the passages stand there.
- The live and archived Claude Code page says in one sentence that, for a session run with `-p` as a custom agent, "`CLAUDE.md` files and project memory still load through the normal message flow, even when the agent's definition sets `omitClaudeMd`" (live `sub-agents.md` line 883), while the table cell the fact cites and the section "What loads at startup" say the opposite for a subagent. The sentence at line 883 follows a paragraph about running the session as an agent, not about a dispatched subagent, so I read it as another case; it is unclear to me. `claude-code-subagent-instruction-files` says what its passage says, and WAY-369's binding sentence (no definition sets the field) does not depend on the outcome. I mention it so the cycle's probe, not this page, stays the evidence of what a type starts with.
- The date read, `2026-11-13`, of every fact: the commit is dated 2026-11-14 00:01 +0100, so the reading falls in the hours before it; I cannot check the day of the reading, only that the passages stand today.
