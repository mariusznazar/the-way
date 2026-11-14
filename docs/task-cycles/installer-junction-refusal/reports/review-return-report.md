PASS e899494ac7d7a860f56af738694753b0d7257524

# Review of the return step's commits — installer-junction-refusal

Range `ee6126cd7899630918d1e3b07dbfd18df5150904..e899494`, one commit; `git rev-parse HEAD` in the worktree is `e899494ac7d7a860f56af738694753b0d7257524`, the head given. The diff is two lines of `foundations/environment_facts.md` (+2/-2): the sentence and the *Source* of `python-junction-detection`. No code, no test.

Counts: blocking 0, Minor 0, out of scope 0 (one observation below, not a finding).

## Findings

None.

Observation, not graded: the page says "Currently only Windows supports junctions"; the sentence says "only Windows supports junctions" under "In Python 3.14". Dropping "Currently" is what WAY-77 requires (no word whose meaning moves with the date), and the edition the sentence names carries the date. The sentence says no more than the passage.

## What was checked

1. **The sentence against the passage.** Sentence: "In Python 3.14, `Path.is_junction` returns true if the path points to a junction and false for any other type of file, and only Windows supports junctions." Passage: "Return True if the path points to a junction, and False for any other type of file. Currently only Windows supports junctions." Both halves of the sentence are in the one run of text; nothing is added (no claim about symlinks, the installer or other platforms' behaviour beyond "only Windows supports junctions"). One entry, one method of one page, one reason to change: fits WAY-76. It names no moving word.
2. **The quotation word for word, live page and archive.** Both fetched with `curl -sL` (exit 0), the passage matched as an exact substring of the page text (markup dropped, whitespace collapsed, one paragraph, once on each page); the text after it is "Added in version 3.12.", so the passage is the whole paragraph of `Path.is_junction()`.
   - `curl -sL -o live.html https://docs.python.org/3.14/library/pathlib.html` — HTTP 200, 272107 bytes; passage found, count 1.
   - `curl -sL -o arch.html http://web.archive.org/web/20261021035154/https://docs.python.org/3.14/library/pathlib.html` — HTTP 200, 278544 bytes, final URL the same (no redirect to another capture); passage found, count 1.
3. **The archive date is a real capture and the latest.** `curl -sL "http://archive.org/wayback/available?url=docs.python.org/3.14/library/pathlib.html&timestamp=20261021035154"` returns the closest snapshot `20261021035154`, status 200, the very address in the entry. The CDX index (`curl -sL "http://web.archive.org/cdx/search/cdx?url=docs.python.org/3.14/library/pathlib.html&output=txt&fl=timestamp,statuscode&from=20261001"`) ends with `20261021035154 200`, so it is the latest existing capture and an earlier capture series exists (2026-10-04 and on): the copy was not made for the entry, as `elements/environment-facts/template.md` requires. Dates in order: capture 2026-10-21, read 2026-11-14, the commit 2026-11-14. The form of the source matches the page-with-archive form: address (archived: address, date) § place — "passage"; read date. The `§ Path.is_junction` place is the heading of the paragraph.
4. **The fit to what the invariant rests on, and that it is used (WAY-73).** `foundations/invariants.md:306`, `installation-paths-through-links`: `Rests on: python-junction-detection`; its sentence speaks of "a Windows junction", which "only Windows supports junctions" supports, and its means is `Path.is_junction`. `installation/install.py:308` is `return path.is_symlink() or path.is_junction()`; tests call `is_junction()` at `installation/test_install.py:681` and `:734`. The old wording named `os.path.isjunction`, which `installation/` does not call; the new one names the call made. The fact stays used (named by the invariant's *Rests on*); no other foundation entry named `os.path.isjunction` (grep of the worktree: remaining hits are only `instruction-files/check_instructions.py:181` and its test, code of another part that no foundation entry rests on this fact for).
5. **The identifier** `python-junction-detection` names what the fact is about, not the method or the value, so it stays true after the edit (identifier rule of the template). It is the only entry naming it; the invariant's reference is unchanged and resolves.
6. **The return step's decisions in its report.**
   - No decision (WAY-36, read whole): the rule that binds after the merge is already the invariant with its test; the choice "skip a stale entry through a link, refuse a write" is behaviour the installer already has for a symlink, and the rejected way ("only the write path") lives in the task document, which leaves the final tree. A rule that ends with the work belongs in the cycle record, which fits WAY-36. Holds.
   - No glossary term (WAY-95, read whole): "junction" has the field's meaning (a Windows directory link), and the invariant's sentence defines "link" in place ("a symbolic link or a Windows junction"). No sentence of the files is read wrongly by a reader with the field's meaning. Holds.
   - No part-map change: `foundations/environment_facts.md` and `foundations/invariants.md` stay under their parts; the commit touched only the first. The surface `installation-command` promises that the installer rewrites and deletes only its own files; the invariant keeps that true. Holds.
   - README note A not made: I did not read the README; the report's reasoning (nothing there says `.git` is checked, so the added sentence stays true as written) is a claim I did not verify, and it concerns a clause the commit does not touch. It is not a defect of this range.
7. **The return step's own check** (`grep` shows only `Path.is_junction()` at `install.py:308` in the installer) reproduced.

## Declined to judge

- `instruction-files/check_instructions.py:181` still calls `os.path.isjunction`; no entry of the foundation rests on that call and the change does not touch it, so whether it needs a fact is outside the task.
- Whether the installer's tests and behaviour match the invariant: the earlier reviews (whole change, fix) judged them; this range holds no code.

## Checks run

| Check | Command | Result |
|---|---|---|
| range and head | `git rev-parse HEAD`; `git show e899494`; `git diff --stat ee6126c..e899494` | head `e899494ac7d7...`, 1 file, +2/-2 |
| foundation check | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| live page | `curl -sL` of `https://docs.python.org/3.14/library/pathlib.html` | HTTP 200; passage found once |
| archived copy | `curl -sL` of `http://web.archive.org/web/20261021035154/https://docs.python.org/3.14/library/pathlib.html` | HTTP 200; passage found once |
| capture is real and latest | archive.org availability API; CDX index from 2026-10-01 | closest snapshot is 20261021035154, status 200; last in the index |
| use of the call | `grep -n is_junction\|isjunction -r installation` | `install.py:308`, `test_install.py:681`, `:734` |

Not run: the installer's tests (the range holds no code or test; the fix's run is the author's claim, not repeated here).

## Reaches beyond the dispatch

- `foundations/decisions.md`: WAY-36 (line 981) and WAY-95 (line 2168), read whole, to check the report's decisions.
- Grep of the worktree for `isjunction` to find other users of the old wording.
- archive.org availability API and CDX index, to confirm the capture is real and the latest.
- Decision `WAY-73` and `WAY-80` by their statements as quoted in the template (`elements/environment-facts/template.md`), not opened in `decisions.md`.

## Unread material

- Read whole: the handoff, `task-cycle/review/SKILL.md`, the author's return report, the frozen task, `elements/environment-facts/template.md`, the invariant `installation-paths-through-links`, the fact `python-stdlib-modules`, the fact `python-junction-detection`, WAY-36 and WAY-95.
- `elements/common/rules.md`: read its first 150 lines (all its sections: language, fields, references, identifiers, withdrawn identifiers, `{fork-point}`, no version); the tail of the file, if any, not read.
- Not read: the README and the part map's `installation` and `installation-command` entries (the latter two only found by grep, not read whole); the earlier review reports; WAY-73 and WAY-80 in `decisions.md`; the glossary.

## Searches not found or unclear

- none
