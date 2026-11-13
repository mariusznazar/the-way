# Return step report — close-decision-pending-templates

**Status:** done — nothing mismatched, nothing committed.
**Head compared:** `faee0f8` (base `fca8491`). Working tree clean.
**Commits:** none. The return step finds no mismatch, so no commit is made.

## Return step lines (for the record's *Return step* section)

- **Foundation compared with code:** the seven files the change edits (`elements/common/missing_element_file.md`, `elements/common/way_of_working.md`, `elements/environment-facts/template.md`, `elements/glossary/template.md`, `elements/invariants/skill/decide_entry.md`, `elements/invariants/template.md`, `elements/part-map/template.md`) and `elements/common/rules.md`, read in full. Every rule the rewritten text states agrees with the rules file: the `TODO` forms of *Rests on* and *Based on* (WAY-71), the identifier and withdrawn-identifier rules, and the "no version" rule. No mismatch.
- **Decisions:** the task's *Decisions in play* and the cited decisions (WAY-01 to WAY-150 as the author report lists them) are unchanged in the log, as the task requires. Each citation in the changed text was checked against its entry (author report, own-work check; fix report for WAY-321). No decision quotes the removed text. No mismatch.
- **Invariants:** `element-directory-contents` (no directory added), `skill-rule-source` (`decide_entry.md` names its element's template and `elements/common/` as before), `tracked-file-private-paths` (grep of the seven changed files and of `elements/common/rules.md` for absolute paths and note links: none), `return-step-record` (see below). No invariant's sentence names the removed text (grep of `foundations/invariants.md`, `environment_facts.md`, `glossary.md`, `part_map.md` for "template", "draft", "how a skill asks", "decision pending", "present tense"). No mismatch.
- **Environment facts:** none written, none shown false. The change rests on no outside source; its sources are the-way's own rules. No mismatch.
- **Glossary terms:** none written. The new text uses "entry", "fact", "invariant", "decision", "source", "product" in the meanings the glossary gives them; the new phrase "a word the product shows its users in another language" uses "word" in the sense WAY-99 gives it. No term is used against its entry. No mismatch.
- **Part map changes:** none needed. Touched parts: `elements-common`, `invariants`, `part-map`, `environment-facts`, `glossary`. No file added or moved, so every *Files* pattern still matches git-tracked files (`foundation_check.py --skip-test-citations`: 0 errors, rechecked after the fix). No *Depends on* or *Trust boundary* changes. No mismatch.
- **Projected entries:** none (the task carries none).
- **Rows of settlements written:** none (*Settlements to record*: 0 accepted).

## Notes on the method

- **`return-step-record`** (invariant, *Part* every, method review): the change must hold the record of its task's return step in one of its commits. This report is the record's return-step report, kept in the record directory, which is gitignored (`.runs/`). Whether the cycle wants the record committed is the cycle's decision (the earlier record commits `7965305` and `29b2ea5` added and then removed such records from the final tree). Flagged, not committed here.
- **Pre-existing, not changed (author report C7):** `elements/invariants/skill/decide_entry.md` holds a rule of entries, against WAY-35; the return step corrects only what the change made mismatched, so it is left for a later task.
- The return step's search is by grep (the whole foundation was not read whole); the decisions it checked are the ones the grep and the dispatch name.

## Unread material

- `foundations/decisions.md` — read only where the cited entries are and where grep matched; the whole log was not read.
- Element skills other than `elements/invariants/skill/decide_entry.md` (for example `elements/environment-facts/skill/write.md`, `elements/glossary/skill/write.md`) — not read; grep only.
- `elements/common/projected_mode.md` and the templates' `examples.md` files — not read.
- Glossary entries — only the headings were read; the entries of "entry", "foundation", "invariant", "environment fact" were not read whole.
- `elements/common/rules.md` — now read whole (89 lines); it was previously unread.

## Searches not found or unclear

- A glossary entry or invariant that names the removed text: none found (grep of the four foundation files).
- Whether the cycle wants the `return-step-record` committed: unclear; the earlier cycle records were committed and removed from the final tree.
- The return step found no word with a second meaning introduced by the change; I did not run `record-glossary-term`, since no term needed an entry.
