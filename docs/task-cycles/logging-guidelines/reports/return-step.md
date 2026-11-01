# Return step — logging-guidelines

**Status:** `done`

The step corrected three things, in commit `70976ac`, on head `d78f148`. Two of them touch entries, so
the commit needs its review as the return step's commits. One of the three overlaps note A of
`reports/whole-review-2.md`; see below for why it is taken here.

## Foundation compared with code

Compared with the files of the repository: WAY-271 to WAY-279; those the task names, WAY-168, WAY-170,
WAY-171, WAY-172, WAY-173, WAY-174, WAY-202, WAY-203, WAY-210, WAY-211, WAY-225, WAY-251, WAY-268,
WAY-270, WAY-30, WAY-86, WAY-100; and those the search found, WAY-139, WAY-169, WAY-207, WAY-208,
WAY-209, WAY-212, WAY-216, plus WAY-21 and WAY-11 for this step. Each binding sentence of the nine was
read against the template, `settle.md`, `recognize.md`, `task_document.md`, `hand_back.md`, `SKILL.md`,
`task-cycle/review/SKILL.md` and `reserved_choices.md`.

What no longer matched, each corrected:

1. **WAY-275 and WAY-276 met with no relation.** Once WAY-275 has a line carry the identifiers the list
   names, it and WAY-276 both apply to a listed identifier that is a secret, and pull opposite ways.
   WAY-276's sentence already kept the list's exception to the ban on personal data, and the template
   already says such an identifier stays out, so the outcome was settled, but WAY-25 asks the entry that
   prevails to name the other and to state the area. My fix of WAY-275 changed its binding part, so the
   search of WAY-33 owed this link, and I missed it then. Corrected in WAY-276: a clause in its second
   sentence and `narrows WAY-275` in *Relations*. The meaning is the one the spec's D3 row already gives,
   "an identifier that is a secret stays out even where it stands on the list".

   The second review raised this as Minor note A. The handoff says the review's findings are not taken
   up as such; I take it on the ground of the entries' own comparison, WAY-25 and WAY-33. If you would
   rather it went to the request untouched, the clause and the relation are the whole of what to revert.
2. **WAY-168 and WAY-170 did not reach the file that now carries them.** WAY-21 has a decision's *Scope*
   name the parts it governs, so that the decisions of a change are found from its files. Both entries
   say what the review of a change does, and `task-cycle/review/SKILL.md` now cites them, the only two of
   its eleven cited entries without `task-cycle` in *Scope*. A later change to that file would not have
   found them. Corrected: `task-cycle` added to each *Scope*. No binding part moves.
3. **The template restated WAY-274 differently, and used a glossary term loosely.** *Writing the files*
   said the list is "never read off the code", while WAY-274 and the rule's bullet say it is written at
   adoption "from what the product has in its code or in its plan", and the glossary's `read off` means
   a value a tool gives. Corrected: the clause is gone; the sentence says the list is the product's
   promise, written from the task's settlements.

Compared and left as they stand:

- WAY-275's *Rationale* names the limit of the rule for events and not for identifiers. It holds nothing
  false, so it is no mismatch, and it goes to the request with note B.
- The six Minor findings of `reports/whole-review.md` and note B: not taken up, as the handoff gives. The
  anchors of that report below `template.md:198` move as the second review says; this step's edit changes
  no line count in that file.
- The two passages of the blocking fix, WAY-275 and the bullet, still agree.

## Decisions written or changed

Written by this step: none. Changed by this step:

| Entry | What changed | Sentence for the request |
|---|---|---|
| WAY-276 | second binding sentence gains the secret on the list; *Relations* gains `narrows WAY-275` | Szablon zakazuje w logach sekretów, danych osobowych (wyjątkiem są tylko identyfikatory z listy) oraz całych obiektów i treści żądań; gdy oryginalny błąd cytuje takie wartości, zakaz ma pierwszeństwo nad WAY-272, identyfikator z listy będący sekretem nie trafia do linii, co ma pierwszeństwo nad WAY-275, a od zakazu danych osobowych produkt może odstąpić z powodem, bo to wybór szablonu, nie prawo. |
| WAY-168 | *Scope* gains `task-cycle`; no change of meaning | Zakres decyzji obejmuje teraz cykl zadania, bo skill przeglądu stosuje ją wprost, więc zmiana tego skilla ją odnajdzie. |
| WAY-170 | *Scope* gains `task-cycle`; no change of meaning | Zakres decyzji obejmuje teraz cykl zadania, bo skill przeglądu stosuje ją wprost, więc zmiana tego skilla ją odnajdzie. |

The sentence for WAY-276 replaces the one in `reports/author.md`. WAY-275's stands in `reports/fix.md`.

## Invariants

None written. No rule of the task, a decision or the human sets one; the spec gives none. No invariant
test changed. `outbound-link-reach`, whose method is a review: the three new addresses are public pages
of `gdpr-info.eu`, and no line links into a repository or a private note.

## Environment facts

None written. The passages in WAY-276 stand as sources quoted in *Based on*: the decision would stand if
they changed, so WAY-90 asks no fact. The lesson in WAY-273 is described in its *Rationale*, as WAY-27
gives and as WAY-270 does.

## Glossary terms

None written. `case flow` and `the rules on failures and logs` say what their words say, and `failure`
is carried by WAY-272, as the spec's D2 gives; `logging scope`, `expected refusal`, `degraded mode` and
`last-resort handler` mean what a reader of the field takes them to mean. `read off` was the one term
used against its entry, corrected above.

## Part-map changes

None. No file was added, moved or removed, so *Files* stand. No file the map names as a trust boundary
changed. The dependencies the change brings are allowed: `product-guidelines` on `project-level`
(`settle.md` names `reserved_choices.md`), `task-cycle` on `product-guidelines` (the review names the
templates), `project-level` on `product-guidelines` and `decisions`. The responsibility sentences of the
three parts stay true. No surface changes: the map's surfaces are commands, and the form of guidelines
is none.

## Projected entries

None: the task is independent and carries no project's entries.

## Rows of *Settlements to record* written

All eight were written in the foundation step; this step adds none.

| Row | Entry |
|---|---|
| 1 | WAY-271 |
| 2 | WAY-272 |
| 3 | WAY-273 |
| 4 | WAY-274 |
| 5 | WAY-275 |
| 6 | WAY-276 |
| 7 | WAY-277 |
| 8 | WAY-278 |

The spec's own entry, E9, is WAY-279 and carries no row.

## Commit and files

- `70976ac` docs: the return step gives WAY-276 its precedence over WAY-275 and the review's entries the
  task cycle's scope

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 5 | 4 |
| `product-guidelines/coding/template.md` | 1 | 1 |

Tree clean, nothing pushed.

## Checks run

Each on `70976ac`, each exit code taken directly, its output going to a file.

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py .` | 0, 0 errors |
| `python -B gate/run_tests.py instruction-files` | 0 |
| `python -B gate/run_tests.py gate` | 0 |
| `python -B gate/run_tests.py agent-instructions` | 0 |
| `python -B gate/run_tests.py task-cycle` | 0 |
| own-work script, `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/6e875913-ea61-4094-be96-22e216469b8d/scratchpad/own_check.py` | 0, 0 problems |
| scope script, `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/6e875913-ea61-4094-be96-22e216469b8d/scratchpad/scope_check.py` | 0; no entry the review skill cites lacks `task-cycle` |
| `git diff --check d78f148 HEAD` | 0 |

Not run: the full gate, as the handoff gives; `project-level`, `installation`, `elements/common` and
`relation-model`, none of whose files this step touches; a test of how an agent acts on the text.

## Reaches beyond the dispatch

- WAY-21, WAY-11 and WAY-36, read to judge *Scope* and what this step writes.
- The part map's opening and its surfaces, beside the three touched parts.
- `reports/whole-review.md`, `reports/whole-review-2.md`: named by the handoff, read so as not to
  take up a finding unknowingly.
- `foundations/glossary.md`, the entry `read off`.

No note of the author and no repository of any product was read in this step.

## Searches not found or unclear

- Unclear: whether WAY-21's "governs" reaches every entry a part's files cite. For `product-guidelines`
  it plainly does not, as 25 of its 65 cited entries lack that part, most of them entries it only leans
  on. I corrected the two where the entry's own sentence says what the review does, and left the rest.
- Unclear: whether a collision over a state the rules already forbid needs a relation at all, as the
  second review also asks. WAY-25 speaks of two decisions that both apply and collide; I read a listed
  secret as that case.
