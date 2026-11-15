# Author report — correction 1

**Status:** done

**Commit:** `f92d9dd` on `task/cycle-after-foundation-review` (after `bd50b60`). One file changed,
`foundations/decisions.md`, 9 added lines. The target branch had not moved, so no merge came in. The
worktree is clean.

## The remarks and how each was carried out

1. **Remark 1 (Fix it in this request), word for word in `reports/correction-1-remarks.md`:** write down
   that for a screenshot shown to the human the rule that keeps it where the product's foundation
   settles it prevails over WAY-373, WAY-373 keeps its reach over every other screenshot and copy made to
   check something, in the foundation's own form for one rule narrowing another.
   - Done in WAY-316 (the decision that settles where the screenshots lie): `narrows WAY-373` added to its
     *Relations*; a third paragraph of binding sentences states the area; one sentence of its *Rationale*
     says why. WAY-373 is unchanged: it narrows nothing, and nothing but WAY-316 narrows it
     (`git grep "narrows WAY-316\|narrows WAY-373"` finds only WAY-316's line; WAY-373's *Relations*
     reads `derives from WAY-148`).
   - The form: the passages that settle that it is the relation on the narrowing rule and not an
     exception in WAY-373: WAY-25's binding sentence, "the one that prevails names the other in *Relations*
     as `narrows`, and its binding sentences state the area where it prevails", and the decisions
     template ("Relations and precedence": "Where two decisions both apply and collide, the one that
     prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where
     it prevails"). The remark's own words leave the form to "whichever the decision template asks for".
   - The passages of what the human accepted that give the outcome (WAY-25), quoted from the remark: "for a
     screenshot shown to the human, the rule that keeps it where the product's foundation settles it
     prevails over WAY-373; WAY-373 keeps its reach over every other screenshot and copy made to check
     something."
2. **Remark 2 (Let through):** the missing source of WAY-138. No change; WAY-138 is untouched.

## Foundation entry written or changed

- **WAY-316**, third paragraph of the binding sentences, *Relations*, *Rationale* (edited in place) — mark:
  `the cycle's` (no row of *Settlements to record* carries it; the remark is its source). The new
  paragraph: "A screenshot that is shown to the human lies in the place the product's foundation settles
  for screenshots and not in the agent's directory of working copies, and for it this decision prevails
  over WAY-373, which keeps its reach over every other screenshot and every copy made to check
  something."
  - EN: For a screenshot shown to the human, WAY-316 prevails over WAY-373; WAY-373 keeps its reach over
    every other screenshot and every copy made to check something.
  - PL: Dla zrzutu ekranu pokazywanego człowiekowi WAY-316 przeważa nad WAY-373; WAY-373 zachowuje zasięg
    wobec każdego innego zrzutu i każdej kopii robionej do sprawdzenia czegokolwiek.

## Choices (with the way rejected and its cost if wrong)

1. **The precedence sits in a third paragraph of WAY-316**, not in a sentence added to the first two. The
   first paragraph already holds three sentences, the second two; the template allows a paragraph for a
   part of another question that the entry answers, and where a shown screenshot lies is a part of
   WAY-373's question. Rejected: a fourth sentence in the first paragraph (breaks the 1-3 limit); an
   exception written into WAY-373 (WAY-25 has the decision that prevails hold the record). Cost if wrong:
   a reviewer prefers it elsewhere in WAY-316; mechanical to move.
2. **No change to WAY-373, its *Rejected*, the skill or `ui_check.md`.** The search of the foundation
   (WAY-33) for entries that name a screenshot in the agent's directory found only WAY-373; the paragraph
   of "Working copies" in `task-cycle/skill/SKILL.md` already has the exception (from the first change)
   and `task-cycle/change/ui_check.md` already sends a shown screenshot to the settled place. Both agree
   with the new paragraph. Cost if wrong: a word of agreement wanted in the skill, such as a reference to
   WAY-316; one line.
3. **No *Rejected* way added to WAY-316**: the remark names no way it rejects, and a way I derive does not
   belong in *Rejected* (WAY-134).

## Checks (command, exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (full, no `--skip-test-citations`) | 0 (`0 errors`) |
| `python -B gate/run_tests.py elements/common` | 0 (235 tests OK) |
| `python -B gate/run_tests.py task-cycle` | 0 (483 tests OK) |
| `python -B gate/run_tests.py agent-instructions` | 0 (25 tests OK) |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 (`0 listed`) |

The whole gate was not run, as instructed. `agent-instructions` was run though no file it checks changed.

## Own-work check

- Requirement most likely unmet: that two decisions do not narrow each other (WAY-25) and that the
  quoted wording the tests read in WAY-316 still stands. Check: `git grep -n "narrows WAY-316\|narrows
  WAY-373" -- foundations/decisions.md` finds only WAY-316's own line; no `decision: WAY-316` line exists
  in any test (found earlier by the grep of the first change; invariants cite WAY-316 by `derives from`
  only); the foundation check passes. No line I added is over 100 columns.

## Reaches beyond the handoff

None.

## Unread material

none. (WAY-25, WAY-316 and WAY-373 whole; the decisions template, `rules.md`, `way_of_working.md`,
`foundation_step.md`, the skill of the decisions element, the invariants and the glossary were read
whole earlier in this session, in the first dispatch, and not read again; `ui_check.md` and the skill's
"Working copies" paragraph were read in the first dispatch and not read again.)

## Searches not found or unclear

none

## Working copies

None remain. I made three test logs in `.runs/author/` and removed them with
`find .runs/author -mindepth 1 -delete`; the directory stands empty.
