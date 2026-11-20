# Author correction 1 report — shorten-decisions-over-length-limit

## Status

`done`

## Commits

Range `010d9b39..711a146c`:

- `711a146c` — Say the part of a question in the numbering rule of the template as WAY-19 says it. One file, `elements/decisions/template.md`, 5 added and 5 removed lines.

## Each remark as made, and how

**Remark 1 (fix in this request):** "The template agents follow when they change a saved decision still describes the numbering rule's 'part of a question' in the old words … Bring the template's sentence in line with the new WAY-19: 'a part of another question that an existing entry answers, or a part of its own question that it sets apart'." — **made.**

The bullet of "Changing a decision" now reads (the sentence it replaces: "A part of the question an existing entry answers is a sentence of that entry, in a paragraph of its own as "Binding sentences" gives, where it cannot change without changing that entry; a part that can change on its own is a question of its own with its own number (WAY-19)."):

> A part of another question that an existing entry answers, or a part of its own question that it sets apart, is a sentence of that entry where it cannot change without changing that entry; the first stands in a paragraph of its own and the second may, as "Binding sentences" gives. A part that can change on its own is a question of its own with its own number (WAY-19).

The words of WAY-19 are kept; the pointer to "Binding sentences" is kept, now saying what that section and WAY-05 give: a part of another question has a paragraph of its own, a part of the entry's own question may. The replaced sentence is split into two at the semicolon so that the paragraph clause fits. I changed no other sentence of the template (the bullet's first sentence and its last sentence stand; only line breaks of this bullet moved) and no entry of the log.

**Remark 2 (let through, no task):** asks for nothing; nothing done.

**Last paragraph of the remarks** (items 3–6 accepted; Mariusz reads the new binding sentences of WAY-344, WAY-416, WAY-287 and WAY-19 before the merge): asks for nothing to change; nothing done.

## Search of the whole foundation for other copies of the old wording (WAY-33)

`git grep -n -i -E "part of (a|the|another|its own|an?) (own )?question|parts? of (a|the) question"` and the more exact "part of the question an existing…" over `elements`, `foundations`, `product-guidelines`, `agent-instructions`, `guidelines`, `task-cycle`, `project-level`, `instruction-files` and `installation` (`docs/task-cycles` left out, records). Hits and what I did:

- `elements/decisions/template.md:210` — the old wording, the one corrected.
- `elements/decisions/template.md:31, 34, 138-139` — the entry form and "Binding sentences": already say "a part of another question" and "a part of the question of the heading that the entry sets apart"; stay.
- `foundations/decisions.md:686-687, 719-724, 733, 761-763` (WAY-05): already the two kinds; stay.
- `foundations/decisions.md:881-882` (WAY-19): the new wording; stays.
- `foundations/decisions.md:903` (WAY-19 *Rationale*, "a part of a question that cannot change apart from its entry stands in that entry for the same reason"): a general statement of the reason, no statement of the numbering rule's two kinds; it is a log entry, which the handoff leaves unchanged; stays.
- `foundations/decisions.md:5502` (WAY-134 pair of examples, "another part of the question") and `foundations/decisions.md:11683` (withdrawn number WAY-358, "a part of the question that WAY-357 answered"): about other things; stay.
- No hit in `elements/*/skill`, `product-guidelines/`, `agent-instructions/`, `guidelines/`, `task-cycle/`, `project-level/`, `instruction-files/`, `installation/`.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, no line `listed:`, run on the working tree before the commit; the commit changes nothing else.
- `elements/decisions` holds no `test_*.py`, so no focused test run exists for the directory changed; I ran none.
- Not run: the full gate (CI runs on the request).

## Own-work check

- Requirement most likely unmet: that the new sentence says nothing against WAY-19 or WAY-05 on the paragraph of each kind.
- Check: read it against WAY-19 (no paragraph named; "a part of another question that an existing entry answers, or a part of its own question that it sets apart … where it cannot change without changing that entry") and against WAY-05 and "Binding sentences" (a paragraph for each part of another question; a further paragraph a part of its own question may carry): "the first stands in a paragraph of its own and the second may" agrees with both, and the second sentence keeps the rule that a part that can change on its own has a number of its own.
- Showed: no contradiction found. A weaker point, named: "the first … the second" refers to the two kinds named in the sentence before; I judged it clear against writing the paragraph rule twice.

## Working copies

The text of the commit message in `.runs/author/`, removed. Left: `compare_binding.py` and `compare_prose.py`.

## Unread material

The handoff and the remarks read whole. WAY-19 (read whole in the first step; its wording at the head is the one I edited), WAY-05 (read whole in the first step, unchanged) and the template sections "Binding sentences" and "Changing a decision" (read whole in the first step; I re-read the lines around the bullet) — not re-read whole in this step. `task-cycle/change/SKILL.md` not re-read; the method is the one of the earlier steps.

## Searches not found or unclear

none
