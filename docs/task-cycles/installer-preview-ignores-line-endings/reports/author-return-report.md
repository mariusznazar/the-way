# Return step report — installer-preview-ignores-line-endings

**Status:** done
**Commits:** none. No foundation entry needed writing or correcting, so nothing was committed in this step.
**Head at the start of the step:** `ee4cbe35` (change `b2c31cc2`, fix commit `ee4cbe35`).

## Items of the record's *Return step*

- **Foundation compared with the code:** done. Compared the entries the task names and the entries the
  search of the foundation found with what the change now does:
  - WAY-34: about the process pin; unaffected.
  - WAY-328: withdrawn; not compared.
  - WAY-379 and WAY-392: the coding and testing guidelines the new tests follow; unaffected.
  - Part map entry `installation` (trust boundary `installation/install.py`) and entry
    `installation-command` (`foundations/part_map.md:222-235`): the entry says the command rewrites only
    its own files and keeps its preview and confirmation. The change keeps both; the entry does not
    describe the byte comparison, so it still matches.
  - Invariants `installation-claude-guidance` (`foundations/invariants.md:301-309`, `CLAUDE.md` kept byte
    for byte; the change does not touch `CLAUDE.md`) and `installation-paths-through-links`
    (`:311-319`; the change adds no write path): both still match.
  - A search of `foundations/` for the preview's `KEEP` and `REPLACE`, the byte comparison, `CRLF`,
    `autocrlf` and line endings found no entry describing the behaviour the change changes.
- **Decisions written or changed:** none. No decision was written and none changed.
- **Invariants written or changed:** none. The task sets the rule (To do item 1). An invariant could carry
  it, but the permanent tests in `installation/test_install.py` already check it and the choices behind it
  are an implementation detail. See the judgement below.
- **Environment facts written or changed:** none. The change rests on git's `core.autocrlf` behaviour,
  which the foundation does not hold. An environment fact can stand only while an invariant's *Rests on* or
  a decision's *Based on* names it (`foundations/environment_facts.md` template, "A fact stands only while…";
  WAY-73). This change adds neither, so an entry written now would name nothing. I did not fetch the git
  documentation for one.
- **Glossary terms written or changed:** none. The change uses `KEEP`, `REPLACE` and `CRLF`/`LF` in their
  ordinary senses; no glossary term holds them (`foundations/glossary.md` has no entry for a line ending or
  for the preview's action words).
- **Part-map changes:** none. The change adds no file to a part and no part.
- **Projected entries and rows of *Settlements to record*:** none; the task carries neither.

## Judgement: does the change settle a choice that binds after the merge (WAY-36)?

Yes, three choices in the comparison bind the installer after the merge, because any later change to
the comparison must keep them or revisit them:

1. Only `\r\n` is folded to `\n`; a lone `\r` is text (the file is replaced). Rejected: universal newlines
   or `splitlines()` before the comparison, which fold a lone `\r`. Cost if wrong: a file with a lone `\r`
   would be kept although its text differs.
2. A file with the same text and mixed line endings is kept. Rejected: requiring all-CRLF, which would
   rewrite such a file as LF. Cost if wrong: a mixed file stays mixed in the product.
3. A file missing its last line ending is replaced. Rejected: treating the missing ending as a line-ending
   difference. Cost if wrong: such a file would be kept without its final newline.

Where it goes: WAY-293 (`foundations/decisions.md:1034-1076`) gives the default for a choice that binds
after the merge: it stays a row of the cycle record's questions table, and the task does not exclude an
entry for it. The task's *Settlements to record* is empty, so this is not an exclusion. Each row above is
therefore for the orchestrator to place in the questions table. I did not read `cycle.md` and did not
write into it. The choices are also pinned by the tests named in the author report.

Open question for the human, with my recommendation: does the task's rule earn an invariant (a method
`test`, `Rests on` the git fact)? Recommendation: no. The permanent tests already check it, and an
invariant would repeat them. If the human wants the rule as an invariant, the environment fact about git's
`core.autocrlf` is written with it, and the fact is then named by that invariant's *Rests on*.

## Checks

- No check run in this step. No file changed in this step, and no foundation file changed, so the foundation
  check and the tests have nothing new to check. The last runs are in the author report
  (`installation` tests: exit 0, 73 tests, OK; pinned ruff on the changed test file: exit 0).

## Note outside this step

The fix round's one Minor finding, the README's agent-definitions row broken over two lines (lines 60–61),
is left as the handoff says. It is for the request's list.

## Unread material

- `foundations/decisions.md`: WAY-36 (`:1008-1032`) and WAY-293 (`:1034-1076`) read; WAY-11 and WAY-134 not
  read. WAY-293 names the default I applied.
- `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`: read whole.
- `elements/environment-facts/skill/SKILL.md` and `elements/environment-facts/template.md`: read whole. The
  skill's own step files (`read.md`, `decide_entry.md`, `draft.md`, `write.md`) and `elements/common/rules.md`
  were not read, since no entry is written.
- `foundations/glossary.md`: its headings and the grep for preview and line-ending terms only.
- `foundations/environment_facts.md`: headings, its first lines and a few entries read; the rest not read.
- `foundations/invariants.md`: `installation-claude-guidance` and `installation-paths-through-links` read (from
  earlier steps), no others in this step.
- `cycle.md` and other agents' files: not read, as the handoff says.

## Searches not found or unclear

- Foundation search for line-ending, `autocrlf` and `CRLF` terms (`foundations/`): no match in the glossary,
  the environment facts or the decisions read.
- Glossary for `KEEP`, `REPLACE`, `preview`: no entry. The terms are the installer's own words, used in
  their ordinary senses.
- Unclear: whether a rule set by a task, with a permanent test but no invariant, counts as a rule the
  foundation must hold. I judged no and put the question to the human above.

## Working copies

- None made in this step. `.runs/author/` is empty; nothing to remove.
