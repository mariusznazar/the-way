# Return step report — cycle-no-private-names (code head a5ea36f)

**Status:** done. Commit: `b241bb0` (`foundations/decisions.md` only, +13 / -9).

## Foundation compared with the code

Compared against the files as they stand at `a5ea36f`:

| Entry or file | Result |
|---|---|
| WAY-308 (binding, Verification, Rationale) against `task-cycle/skill/SKILL.md` section "The record before it is committed", `request_template.md` (checks of the description, item 12), `record_template.md` | **Corrected**: the item 12 of the request (the request tells the human of a cleaned relation line) was a choice of the correction that bound after the merge and stood only in the skill, the template and Verification; the binding sentence now says it ("a line it lists is cleaned like any other, and the request tells the human, since the reader of a plan's state may then report a conflict"). Marked `the cycle's` (an addition beyond the accepted row 1). |
| WAY-309 against the same files and `private_paths_check.py` | **Corrected**: the order of the two checks and the single rewriting (the orchestrator's autonomous choice for the carried question, now binding after the merge) stood only in the skill. The binding sentence now reads: the check of WAY-294 runs on the original before the copy is made, the cleaning is one rewriting of every text file of the copy, and the check runs once more on the cleaned copy, where an item it lists is made to read the same in the report and in the remarks, not appended again. *Rationale* says why (each item reaches the remarks once before any word changes; a report's item and its entry stay alike). Marked `the cycle's`. The patterns the entry names (a drive letter, a home directory, double-bracket links) are a subset of what the script lists; no mismatch. Wrapped at 100 columns. |
| WAY-294, WAY-295, WAY-260 | no change: WAY-294's run before the commit and "word for word" hold (the cleaning rewrites both places alike); WAY-309 narrows WAY-294 for the run on the copy; the full report path in the record template reads "from the repository's root", consistent with "full report path". |
| WAY-27 and invariant `outbound-link-reach` | no change: the change adds no link into a private repository or note collection; the forms the new texts name are written without a real link. |
| WAY-153 and invariant `project-plan-state-evidence` | no change: the reader's actual output on a cleaned copy (unchecked before the document link, anchored after it) is what the invariant allows (it reports missing provenance as unchecked, proposes nothing it cannot prove) and is pinned by the three tests in `project-level/test_plan_state.py`. `project-level/plan/template.md` line 88 (the document link to the frozen copy "once the task is `done`") still holds: the human sets `done` and the link together, the state the second test reads. |
| WAY-288, WAY-290, WAY-291, WAY-286 | no change: the description check of private paths covers the block in the task document's language; the form check is untouched. |
| WAY-287 | no change: it asks for "everything whose merge needs the human's yes"; item 12 is carried by WAY-308 as the remarks-listing item is carried by WAY-295. |
| WAY-301 | no change (the tag message holds no private title: consistent). |
| Part map: `task-cycle`, `decisions`, `agent-instructions`, `project-level` | no change: the new script and its test sit under `task-cycle/**` and import the standard library only; the README is in `agent-instructions/**`; the test added to `project-level/test_plan_state.py` imports nothing of another part. The Scope of WAY-308/309 names the parts their rule reaches. |
| Invariants `script-language`, `script-imports`, `cross-part-imports`, `skill-rule-source` | no change: the script is Python, imports `argparse`, `codecs`, `re`, `sys`, `dataclasses`, `pathlib` only. |

Search of the whole foundation (`foundations/*.md`) for `private`, `absolute path`, `task-cycles`,
`remarks check`, `Task source`, `Task relation`: the hits are WAY-27, WAY-301, WAY-147 (record path
`docs/task-cycles/...`, unchanged), WAY-294/295/296 and the withdrawn-list rows, and WAY-308/309. No
other entry states what the change alters.

## Written or changed

- Decisions changed: WAY-308, WAY-309 (edited in place; both written whole from rows 1 and 2 in the
  foundation step, the additions above are `the cycle's`).
- Invariants written or changed: none (the task sets none).
- Environment facts: none. The decisions rest on no source outside the product (`Based on: none`); the
  visibility of the repositories is the motive, not a source the decision depends on.
- Glossary terms: none. Words used (cleaning, the original, the copy, working record, private note, note
  link) mean what a reader of the field takes them to mean, so WAY-95 gives them no entry.
- Part-map changes: none.
- Projected entries: none.
- Rows of *Settlements to record*: row 1 -> WAY-308, row 2 -> WAY-309 (written in the foundation step,
  unchanged in meaning).
- Choices that bind after the merge and are now in the foundation: the order and the single rewriting
  (WAY-309); the request telling the human of a cleaned relation line (WAY-308). The `Task source:` line
  cleaned in the committed copy with its cost for the reader was already in WAY-308's rationale.

## Checks (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (after the edit) | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 | 0 listed |

No code changed, so no test run (the parts' tests ran at the correction: `task-cycle` 187, `project-level`
271, `agent-instructions` 18, all exit 0). The full gate is the orchestrator's.

## Own-work check

Requirement most likely unmet: the foundation says no more and no less than the files at `a5ea36f`.
Check: read WAY-308 and WAY-309 against the section and the template side by side, sentence by sentence
(order of the steps; "stay unless listed"; "cleaned like any other"; "the request tells the human";
"made to read the same, not appended again"; the three commits that add the record; the description
edits), and searched the foundation for the six words above for an entry that states otherwise: none.
Weakest point: the two additions are marked `the cycle's`, so the human meets them at the merge without
having seen them in the task document; each is one sentence of rule already in the files.

## Searches not found or unclear

- none.
