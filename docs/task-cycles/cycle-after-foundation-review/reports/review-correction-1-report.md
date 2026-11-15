PASS f92d9dd7f77abee93508be4a89c9a35854aa4e5d

# Review of correction 1 (the human's remarks on the request)

Range `bd50b60..f92d9dd` (one commit). `git rev-parse HEAD` is `f92d9dd7f77abee93508be4a89c9a35854aa4e5d`.
The diff holds one file, `foundations/decisions.md`, 11 lines added and 3 removed, all in WAY-316
(binding paragraph, *Relations*, *Rationale*). No merge came in (the target branch has not moved).

## The remarks

1. **Remark 1 (fix it in this request): made.** WAY-316 (`foundations/decisions.md` lines 6933-6940) now
   says, in a third paragraph of binding sentences, that "a screenshot that is shown to the human lies in
   the place the product's foundation settles for screenshots and not in the agent's directory of working
   copies, and for it this decision prevails over WAY-373, which keeps its reach over every other
   screenshot and every copy made to check something", and its *Relations* now end `· narrows WAY-373`.
   - Form: the decisions template ("Relations and precedence", `elements/decisions/template.md` lines
     209-225) and WAY-25 (read whole) give the relation on the entry that prevails and the area in its
     binding sentences; the correction does exactly that, and the remark leaves the form to the template.
     WAY-373 is unchanged (its *Relations* read `derives from WAY-148`).
   - Area: the paragraph names it as the remark does (shown screenshot; WAY-373 keeps every other
     screenshot and every copy made to check something). The paragraph has one sentence, within the template's 1-3, and
     stands apart as "a part of another question this entry answers" (template line 31).
   - No chain and no mutual narrowing: `git grep -n "narrows WAY-316\|narrows WAY-373" -- foundations`
     finds only WAY-316's line 6940. The author's claim is true.
   - *Rationale*: one added sentence says why the rule on working copies yields for a shown screenshot (it must
     outlive the task's directory until acceptance), and "for it and for nothing else". It matches WAY-373's
     own *Rationale* (copies go with the task's directory).
   - Skill and `ui_check.md` agree, as claimed: `task-cycle/skill/SKILL.md` "Working copies" sends a shown
     screenshot where `ui_check.md` says and keeps it in the agent's directory only where no place is settled; `task-cycle/change/ui_check.md`
     lines 13-20 say the same. Where no place is settled the screenshot is not shown (WAY-316 second
     paragraph), so the new paragraph does not reach that case. My earlier Minor finding 3 is answered.
2. **Remark 2 (let through, WAY-138's source): no change asked, none made.** The range does not touch WAY-138.

## Findings

Critical: none. Important: none.

Minor (does not block; goes to the request's list):

- `foundations/decisions.md` WAY-316 *Verification* (lines ~6942-6968) was not extended for the new paragraph: no `complies`/`violates`
  line says what a conforming or violating change looks like for a shown screenshot against WAY-373 (for
  example, a shown screenshot left only in the agent's directory). The existing lines cover the place and the
  committed file, not this precedence; an agent comparing a change with the decision has no example for it.
  The remark did not ask for it; the correction's own-work check names no such line. Evidence: reading the
  *Verification* of WAY-316 whole after the change. Within the correction's reach, low consequence.

## Checks I ran

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `f92d9dd7f77abee93508be4a89c9a35854aa4e5d` |
| `git diff bd50b60..f92d9dd` and `--stat` | 0 | one file as above |
| `git grep -n "narrows WAY-316\|narrows WAY-373" -- foundations` | 0 | one hit, WAY-316 line 6940 |
| `git grep -n "WAY-316" -- . ':!foundations/decisions.md' ':!.runs'` | 0 | invariants cite it by `Derives from`; no `decision:` test line holds its sentences |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors`, no `listed:` line |

Not run: the whole gate (the orchestrator's) and the test directories (the author ran them; the change is
one entry of the decision log, and the foundation check, which compares the quotations the tests hold, passes).

## Unread material

none of the dispatch. Read whole: the handoff, `fix.md`, `review/SKILL.md` (earlier), the remarks, the author's
report, the diff, WAY-25 and WAY-316 (whole, in the earlier review), WAY-373 (whole, earlier), the decisions
template's "Relations and precedence" and the template's first lines. The rest of the decisions template I did
not reread.

## Searches not found or unclear

none

## Working copies

None made; `.runs/review-whole/` stands empty (the index of the earlier review was removed). No worktree, no clone.
