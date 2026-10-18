# Whole-branch review — product guidelines, with the styleguide as the first guidelines

Reviewer: final whole-branch reviewer (claude-opus-5-5), never an author of this change.
Method: Superpowers 6.4.1 `requesting-code-review`, template
`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/requesting-code-review/code-reviewer.md`.
Range: base `96623ed` .. head `9dd9880` (18 commits, 46 files, +4687/−61).
Requirements read: frozen `task.md` (all 27 rows of *Settlements to record*, *To do* 1–11, *Out of
scope*), `spec.md`, `cycle.md` rulings C1–C30, the ledger lines, `agent-instructions/README.md`
(through the repository's `AGENTS.md`).

**How the review was done.** In passes, all of it by me, with no subagents. (1) The task, the spec and
the rulings. (2) At head, in a detached worktree (`C:/Storage/repos/the-way-wt/pg-final-review`,
removed when done): `product-guidelines/template.md`, `product-guidelines/styleguide/template.md`,
`product-guidelines/form_check.py` and `product-guidelines/styleguide/SKILL.md` read whole; WAY-09 and
WAY-167–WAY-192 read whole; the diffs of the glossary, the invariants file, the part map, the
installer, `installation/README.md`, `README.md` and one regenerated entry point; the new
`installation/test_styleguide_installation.py` read whole; the fixture and helpers of
`product-guidelines/test_form_check_invariants.py`, and the parts of `test_form_check.py` the ledger
names. (3) Each ledger line checked against the code at head. (4) Focused probes for specific doubts
only, using the F4 test fixture (`C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/3c9695bb-97dd-4f98-b7ec-dff4bae7e82e/scratchpad/probes/probe.py`,
output `probe-out.txt` next to it). I did not re-run whole suites: the root's `completed-*.txt` show
all 22 checks exiting 0 at `9dd9880`.

## Strengths

- **Every row of *Settlements to record* is written as an entry of its kind, with its meaning
  unchanged.** I mapped each row to its entry: row 1 → WAY-167, 2 → WAY-168, 3 → WAY-169, 4 → WAY-170,
  5 and 6 → WAY-176, 7 → WAY-177, 8 → WAY-178, 9 → WAY-179, 10 → WAY-180, 11 → WAY-181, 12 → WAY-182,
  13 → WAY-183, 14 → WAY-185, 15 → WAY-184, 16 → WAY-186, 17 → WAY-187, 18 → WAY-188, 19 → WAY-189,
  20 → WAY-190, 21 → WAY-191, 22 → WAY-192, 23 → WAY-174, 24 → WAY-172, 25 → glossary "guidelines",
  26 → WAY-173, 27 → WAY-174 together with WAY-172 (`foundations/decisions.md:5439-6369`,
  `foundations/glossary.md:105-110`). Each keeps the human's rejected options and weak points: the
  renamed file that looks new (WAY-190), a product that can drop a rule that would have protected
  it (WAY-173), the untried mode before the first screen (WAY-184 *Review when*). The two
  departures from WAY-114 carry `narrows WAY-114` and state their areas (WAY-172, WAY-174), as C19
  rules.
- **The form check is careful at its trust boundary.** It reads files with `lstat` on each path
  component, refuses reparse points, checks that the file opened (by device and inode) is the file
  it looked at, and reads at most 1 MiB, so a file that grows during the read is cut off
  (`product-guidelines/form_check.py:198-255`). No path written in a file of guidelines reaches git
  or the file system: git is asked once for everything it tracks, and the matching happens in
  Python (`:1090-1112`, `:876-923`; ruling C29). Every value taken from a file is escaped and cut to
  200 characters before it is printed (`:176-181`). The regular expressions have no nested
  repetition, and the pattern for references is bounded by a look-behind (`:131`).
- **The rules of form live only in the templates.** The script reads the form from the fenced
  block of each template's `## Required form` (`:291-363`), so a template and its check cannot drift
  apart unseen. The parsers of the format guards are borrowed, and their findings are discarded
  (`:613-621`), so a fault the decision log has against its own rules never fails the form check.
- **The invariant tests were written apart from the code (WAY-69), and they hold up.** The six
  invariants on the script have a separate test author. Every deliberate break, applied by removing
  a line of the check, was detected (`slice-2-break-*.txt`, `slice-3-break-*.txt`). The one break that
  first went undetected went back to the check author and was then caught (`8d97ab9`).
- **Choosing "user interface", "discipline" and "design token" pays off.** No new sentence says
  bare "interface", "domain" or "token", so none collides with the senses WAY-165, WAY-95/104 and
  WAY-84 give those words. The part is named `product-guidelines`, so it does not collide with the
  glossary term "guidelines" (WAY-93).
- **The skill corrects the spec where the spec was wrong, and says why.** A change of the part map
  goes into *To do*, never into a row of *Settlements to record*
  (`product-guidelines/styleguide/SKILL.md:74-76`), because a part-map change is no row of that
  table.
- **The installer change is small, and its test does what the product will do.** It runs both
  form-check commands the guidance names, from inside an installed product, and they judge the
  product's own files (`installation/test_styleguide_installation.py:119-147`). It also refuses a
  block left by an earlier pin (`:149-165`).

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

1. **The product guidance runs the form check only for some of the changes that can break the
   styleguide.**
   - File: `installation/install.py:176-179` (also asserted in
     `installation/test_styleguide_installation.py:18-19`).
   - What: the sentence tells a product's agents to run the form check "before a merge in which a
     file of `guidelines/` or of `foundations/` changed". The-way's own template gives the invariant
     `guidelines-form` the *Part* `every`, because "a renamed file of the product, a renamed part or
     a moved pin can make it false whatever part a change touches"
     (`product-guidelines/template.md:171-172`). It gives `guidelines-reference-current` the part
     holding `.the-way`, "whose move can change how fingerprints are read" (`:173-175`). Two of those
     changes fall outside the guidance's trigger: renaming a file that `## Where in code` points to,
     such as the tokens file, and moving the `.the-way` pin.
   - Why it matters: in a product, nothing else runs these checks. The guidance itself says
     "Nothing runs these checks automatically", and no gate script runs a product's invariants by
     *Part* (`gate/` holds only `run_tests.py` and `method_script.py`). So a task that renames the
     tokens file, or moves the pin to a commit with a changed template, merges with the styleguide
     pointing at a file that no longer exists, or failing the new form, and nothing shows it. The
     next task that touches `guidelines/` or `foundations/` then fails the form check for something
     it did not do. This is what a reasonable person expects an invariant with *Part* `every` to
     prevent.
   - The plan, not only the code: spec §8 gives this sentence word for word. The executor and the
     slice-8 review followed the spec. The finding is against the spec.
   - Fix: "Where this repository holds `guidelines/`, run … and … before every merge." The script
     takes seconds on a product's files, and the sentence gets shorter. Update `SENTENCE` in
     `installation/test_styleguide_installation.py:18-19`. A product that moves its pin then removes
     the old block, as `installation/README.md` already says.

### Minor (Nice to Have)

New in this review (each confirmed by a probe where marked):

1. **The required examples are not checked (probe).**
   - File: `product-guidelines/form_check.py:733-744`. Only `form.required[RULES]` is ever read. Compare
     `product-guidelines/styleguide/template.md:19-21`, which says the form check reads "the
     required rules and examples of the styleguide in their places".
   - What: a styleguide with `### Mockups` and `### Plan of a user-interface change` both removed
     exits 0.
   - Why: rows 9 and 11 put both into the template. Under WAY-173 a product leaves out what the
     template carries only by a decision of its own, and here nothing notices that it happened. The
     impact is limited: examples bind nothing.
   - Fix: either check the required headings under `## Examples` the way the required rules are
     checked, with `none —` for a dropped one, or reword the template's sentence so it no longer
     promises that check.
2. **An example that carries a *Decision* field passes (probe).**
   - File: `product-guidelines/template.md:75-76` says an example "carries no *Decision* field", and
     no check enforces it.
   - Why: a rule placed under `## Examples` with a *Decision* field escapes WAY-188's demand for an
     invariant. If the decision it names is a role decision, it also escapes the check that "Each
     role in its meaning" names every role decision. An agent reading the file may still treat the
     example as binding.
   - Fix: report a *Decision* field under `## Examples`, under `guidelines-form`.
3. **The order of the product's further rules is not checked (probe).**
   - File: `product-guidelines/styleguide/template.md:63-64` says "The product's further rules follow
     the required ones". A further rule placed before `### Each role in its meaning` passes.
   - Fix: check that order, or drop the sentence.
4. ***Applies to* and the part in the file's name are not compared.**
   - File: `product-guidelines/form_check.py:844-868`.
   - What: `guidelines/styleguide-web.md` whose *Applies to* names `admin` passes, as long as both
     parts are in the map. `product-guidelines/styleguide/template.md:68-69` and WAY-167 tie the two
     to the same user interface.
   - Fix: for a per-part discipline, require *Applies to* to name exactly the part in the file's
     name.

Ledger lines graded Minor are listed under "Ledger lines graded" below. They are not repeated here.

## Declined to judge

- **Whether `refine-task` or `lead-project` route a styleguide task to `maintain-styleguide`.** Set
  aside: the task's *Out of scope* and ruling C30 give this to the backlog task "cykl zadania przy
  zmianie widoku". The request must name it as a limitation.
- **The row-to-text table that spec §10 has the request carry for rows 5–24, 26 and 27.** Set aside:
  the request is not written yet (`cycle.md`, *Request handoff* "—"). I mapped each row to its entry
  myself (Strengths, first bullet), and to the skill's or template's sentence for rows 5–13, 16,
  17, 20–23 and 26. The table itself is still to be written and checked at the request.
- **Whether git, run by the form check, honours repository-local settings that run programs, such
  as `core.fsmonitor`.** Set aside: `guard_shared.call_git` is shared by every format guard and is
  not changed here. Any hardening belongs to `elements-common`, not to this change.
- **The *Part* of the-way's own `guidelines-reference-current` (`product-guidelines · decisions ·
  invariants`), which leaves out `relation-model` and `elements-common` although the script's code
  runs through them.** Set aside: spec §3.3 gives exactly these three. In the-way the invariant is
  true for want of any guidelines file. The six `guidelines-check-*` invariants carry the wider
  *Part* and cover the script.
- **The quality of the skill's prose as a conversation.** Set aside: no test asserts it (spec §10).
  The independent assessment of the change (WAY-10) and the first use in `loop2` judge it, the
  latter after the merge (task, question 1).
- **The cost recorded under C5, that every styleguide change, however small, goes through a
  refinement and a full cycle.** Set aside: this is a provisional reading the root made under the
  user's delegation. The request is to show it, and the human decides.
- **The departures of the F1 authors that C27 accepts provisionally** (WAY-173 derives from WAY-168
  and WAY-100, WAY-170 also from WAY-16, WAY-172 also from WAY-125, extra *Scope* values). Set aside
  as a choice of relations, not code. I found nothing in them that contradicts a settlement row. The
  independent assessment rules on them.

## Recommendations

- Fix Important 1 in this branch. It is one sentence and its test.
- Close Minor 1–3 together with ledger M5 of Task 1, the pair rule naming `guidelines-form`: they
  are the same kind of gap, where a template says something about the form that no check enforces.
  Either the check enforces it, or the template stops saying it. One small slice in
  `form_check.py`, with ordinary tests, would cover all four.
- Settle ledger M6 of Task 1 (the name `guidelines/<discipline>-<part>.md`) in the foundation, not in
  the code. Either WAY-167 gives that name for any discipline, or the form check refuses it. As it
  stands, a decision and its check disagree in the permissive direction.
- At the request, name: before `main` exists, `guidelines-reference-current` records `pass` beside
  `unchecked` (C23); the 1 MiB limit on the decision log, of which the-way's own log uses 41%; and the
  routing limitation (C30).

## Assessment

**Ready to merge?** With fixes

**Reasoning:** The foundation entries carry all 27 settlement rows faithfully. The form check is
sound, careful at its trust boundary, and its tests were written independently and caught every
deliberate break. The one Important finding is that the product guidance under-triggers the form
check: a pin move or a rename of a file the styleguide points to escapes it, against the invariant's
own *Part* `every`. It traces to spec §8 and is a one-sentence fix. The Minor findings are gaps
between what the templates say about the form and what the check enforces, plus wording.

## Ledger lines graded

Each `minor (deferred)` and `note` line of
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.superpowers/sdd/plan-tasks/final-review-ledger-lines.md`,
checked against `9dd9880`. Rulings (lines 1, 2, 9, 10, 11, 19, 28) are not graded. Line 19 is graded
through Task 3 M3.

| Ledger line | Grade | Place at head | Why |
|---|---|---|---|
| Task 1 M1 — "nothing of this template is copied" vs the invariant copies | Minor | `product-guidelines/template.md:13-14` vs `:142-145` | Still present: the template says nothing of it is copied, then gives two sentences a product copies. Fix: "save the two invariants' sentences below". |
| Task 1 M2 — heading "No emphasis words" vs a body allowing one rule | Resolved at head, no finding | `product-guidelines/template.md:128-130` | The fix `e62ca49` moved this into the note, which now says "one rule per file at most". The heading is gone. |
| Task 1 M3 — "part" used for divisions of a styleguide beside the map's part | Minor | `product-guidelines/styleguide/template.md:4,73,75` | "Part" is a glossary term of the-way, and the same file also uses it in the map's sense (`:7`, `:68`, `:96-97`). Fix: "section" or "entry of the template". |
| Task 1 M4 — the language rule does not name the column headings of `## Roles` | Minor | `product-guidelines/template.md:109-113`; `form_check.py:791-795` | A translated header row fails loudly, so the gap is in the text only. Fix: add "the headings of a table's columns". |
| Task 1 M5 — "Every background with its text" proposes `guidelines-form`, whose sentence says nothing of pairs | Minor | `product-guidelines/styleguide/template.md:98-102`; `form_check.py:813-818` cites `FORM` | The product's check reports a pair under an invariant whose sentence does not state it. The-way's `guidelines-check-colour-pair` covers the script, but a product's invariant then has a verdict wider than its sentence. Fix: name pairs, kinds and the coverage of role decisions in the `guidelines-form` sentence, which raises its version and the citation together (C8), or give the rule an invariant of the product's own. |
| Task 1 M6 — the *Part* of the role-meaning invariant lacks a WAY-62 citation; the name `<discipline>-<part>` is accepted but not given by WAY-167 | Minor | `product-guidelines/styleguide/template.md:96-97` (cites WAY-189 for the *Part*); `form_check.py:863-873` vs `foundations/decisions.md:5441-5445` | The citation is a small slip. The name is a decision and its check disagreeing in the permissive direction; settle it in WAY-167 or in the check (Recommendations). |
| Task 2 M3 — an unreadable part-map template exits 1 with a traceback, not 2 | Minor | `product-guidelines/form_check.py:1172-1176` | `ValueError` and `KeyError` from `read_rules()` are not caught. The template is the-way's own, so the failure is rare and loud. |
| Task 2 M4 — any `:` or `\` in a path is refused | Minor | `form_check.py:880-883` | Safe and documented (`:39-40`). A product file with `:` in its name cannot be pointed to, which is rare. |
| Task 2 M5 — de-duplication of guidelines files is quadratic | Minor (negligible) | `form_check.py:1049` | Its size is set by the number of files in `guidelines/`, a handful. |
| Task 2 M6 — a test calls `self.setUp()` inside a subtest loop | Minor | `product-guidelines/test_form_check.py:322, 395, 399, 415, 420, 435, 480, 643, 665` (the lines have moved since the ledger) | Test hygiene: it piles up cleanups, and the results are still correct. |
| Task 2 M7 — missing sections reported at line 0 | Minor | `form_check.py:671` (`missing_at=None` → `:0:`) | Visible as `guidelines/styleguide-web.md:0: error:` (`installation/test_styleguide_installation.py:146`). Line 1, or the line of the heading that should hold it, would read better. |
| Task 2 M8 — the name test matches a discipline prefix plus `-`, a latent clash for templates `a` and `a-b` | Minor (latent) | `form_check.py:856-862` | The-way has one template today. Fix it when a second discipline template whose name starts with another's arrives. |
| Task 2 M9 — `setUp()` inside a loop, again | Minor | `test_form_check.py` (same pattern as M6) | As M6. |
| Task 3 M1 — the merge check records `pass` though it never ran when the log is unreadable | Minor | `form_check.py:1140` (`ran` before the read), `:1202-1204` | The invariant's result is still `fail`, because the check on the same commit fails (WAY-65). Only the line for that one check misleads. Fix: mark it `unchecked` when `foundation.known` is false. |
| Task 3 M2 — the merge re-checks only references current on the branch | Minor | `form_check.py:955-971` | Only a malformed `x@v2` that names an identifier which exists only on the commit merged onto escapes. Anything stale on the branch already fails the check on the same commit. |
| Task 3 M3 (and ruling line 19) — the 1 MiB limit binds the decision log and the invariants file | Minor | `form_check.py:109`, `:560-561` | The failure is loud. The-way's own log is at 426,585 B, and it is read only where guidelines exist. Name it at the request. |
| Task 3 M4 — decision numbers are normalised (`ABC-5` = `ABC-05`; 10 or more digits are not a reference) | Minor | `form_check.py:133`, `:445-451` | Matches how the log writes numbers; the bound protects `int()`. |
| Task 3 M5 — untested branches at the trust boundary and in the narrowing | Minor | `form_check.py` (e.g. `:236`, a file changed while it is opened; `:1022-1025`, `guidelines` unreadable) | Hard to provoke in a test, and each fails closed. |
| Task 3 M6 — `PARSE_ERRORS` includes `AttributeError` and `TypeError` | Minor | `form_check.py:108` | It can mask a bug in borrowed code as "cannot be parsed", which is still reported as an error with exit 1. |
| Task 3 M7 — the report's list of borrowed functions omits `versions_of` | Outside the task's scope | slice report, not the code | The docstring at `form_check.py:54-57` does not list the functions. |
| Task 3 M8 — the file grew to 1247 lines | Outside the task's scope | `form_check.py` | No defect; in line with the element guards. |
| Task 4 M1 — row 20: the companion invariant is never said to be withdrawn once the full one holds | Minor | `product-guidelines/styleguide/SKILL.md:197-200`; `product-guidelines/styleguide/template.md:106-109` | WAY-190 (`decisions.md:6269`) carries the withdrawal, but the skill, which is what proposes the companion, does not say it. A forgotten companion still holds, so the cost is one redundant run. |
| Task 4 M2 — row 26: the adopting decision covers the template, not what the skill proposes | Minor | `product-guidelines/styleguide/template.md:10-11`; `SKILL.md:173-174` | WAY-173 names both. The skill's proposals still become product decisions through the task's settlements, so nothing binds unadopted. Wording only. |
| Task 4 M3 — "only through the task document" overstates WAY-172 | Minor | `SKILL.md:38-41` vs `decisions.md:5659-5663` | WAY-172 also allows approval at a blocked draft request. Add the second route. |
| Task 4 M4 — the WCAG edition's address and passages are not among what reaches the task document | Minor | `SKILL.md:69-73` vs `:185-186` | Step 4 demands the address and the passage word for word, but "What reaches the task document" lists only "answer on accessibility". Add both to *Context* or *Questions to settle*. |
| Task 4 M5 — no numbered step to run `refine-task` steps 1–2 first | Minor | `SKILL.md:28-31` | Stated in prose; a numbered step 0 would make it harder to skip. |
| Task 4 M6 — no stop when the foundation settles no technology for the user interface | Minor | `SKILL.md:122-123` | Before a first screen this is likely. Say: record it as an open question and stop the research, as `:115-116` does for a new library. |
| Task 4 M7 — the part's identifier is used in report paths while it may still be an open question | Minor | `SKILL.md:35, 130` vs `:105-108` | Name a provisional identifier, or a path for when it is not yet settled. |
| Task 4 M8 — the audit's "ask every time" reads as a question to the human | Minor | `SKILL.md:150` | Fix: "Check every time …". |
| Task 4 M9 — README suggests every discipline has a template and a skill | Minor | `README.md:81-83`; also WAY-09 `decisions.md:259-261` | The second place is in a binding part, so a later rewording there costs a renewal. |
| Task 4 M10 — unclear whether one critic reads all research reports or one critic reads each | Minor | `SKILL.md:131` | Say "one fresh agent, given all the reports". |
| Task 4 note (a) — spec §6.2 lists the part-map change under *Settlements to record* | Outside the task's scope (a justified deviation; no finding) | `SKILL.md:74-76` | The skill is right and the spec is wrong. |
| Task 4 note (b) — no research where screens exist but no styleguide does, while WAY-186 has no such limit | Minor | `SKILL.md:112-114` vs `decisions.md:6120-6127` | *To do* 8 scopes the research to a product with no screens, and the skill follows it. WAY-186's binding sentence is wider. Fix: give WAY-186 the scope of *To do* 8 (with no screens yet, and at every refresh or extension). The edit is in place before `main`. |
| Task 8 M1 — the test hard-codes 30 wrappers | Minor | `installation/test_styleguide_installation.py:90` | The next skill added breaks this test, which no one would think to update. Fix: derive it as `2 * len(install.SKILLS)`. |
| Task 8 M2 — "always name this repository's file or directory" vs form-check commands that name no folder | Minor | `installation/install.py:158` vs `:177-178` | The commands work run from the root (`installation/test_styleguide_installation.py:132-147`), but the guidance contradicts itself. Fix: add `.` to both commands, or except the form check in the sentence. |
| Task 8 note — with `--merge-onto` the form check prints a "0 error(s)" count line before a file's errors | Minor | `form_check.py:1222-1223` | Confirmed (probe: the run's own count line, then the file's error). A reader can stop at the first count line. Fix: print the run's report last, or add a total line. |

## Review of the fix

Fix range: `9dd9880..896071a`, one commit `896071a`, read whole from
`.superpowers/sdd/plan-tasks/review-9dd9880..896071a.diff`, together with the section "Final-review
fix" of `.superpowers/sdd/plan-tasks/task-8-report.md`. Read-only; I re-ran no suites.

**Important 1: ADDRESSED.**

- `installation/install.py:176-179` at `896071a`: the guidance now reads "Where this repository
  holds `guidelines/`, run `python -B .the-way/product-guidelines/form_check.py` and `python -B
  .the-way/product-guidelines/form_check.py --merge-onto <main commit>` before every merge." No
  change is excluded any more, so a rename of a file `## Where in code` points to and a moved
  `.the-way` pin are both covered. This matches *Part* `every` of `guidelines-form`
  (`product-guidelines/template.md:171-172`) and the `.the-way` part of
  `guidelines-reference-current` (`:173-175`).
- `installation/test_styleguide_installation.py:18-21`: `SENTENCE` follows the new wording, and a
  comment names why. The three tests assert it:
  - the preview and the applied block (`:74`, `:100`);
  - the guidance in a real installed product (`:124`);
  - the refusal of an earlier block (`:155`). `SENTENCE + " "` still matches, because the sentence
    is followed by " A check that did not run…".
- Evidence that the test drove the fix:
  - `reports/slice-8-fix-red.txt`: 3 failures with `install.py` untouched;
  - `reports/slice-8-fix-green.txt`: 3 OK;
  - `reports/slice-8-fix-tests-installation.txt`: 33 OK. I read these tails only.
- `git grep` at `896071a` finds the old trigger ("or of `foundations/` changed") nowhere outside
  `.runs/` and `.superpowers/`. `installation/README.md:58` ("running the checks before a merge, the
  form check of `guidelines/` included") stays true.

**New issues introduced by the fix:** none.

- Not new, and not a code issue: spec §8 (`.runs/task-cycles/product-guidelines-styleguide/spec.md:628-631`)
  still gives the old trigger. That is the root's to settle: record the revision in the request, or
  in the spec, so that a later reader does not take the spec's wording as binding.
- Ledger Task 8 M1 and M2 stand as graded above; the fix neither worsens them nor resolves them.

**Ready to merge?** Yes, as far as this review's blocking findings go. The Minor findings stay as
graded, for the request.
