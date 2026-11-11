# Remarks of the correction after the human's answer on the request

The human answered the request's *For you to decide*: items 1 and 3 are done in this request; items 2 and 4 are let through. The remarks below bind the correction. Paths are relative to the worktree.

## The human's rule for item 1, in his words and then in the rule's form

His words (in Polish, as he wrote them): "jeśli agent wie, że od jakiegoś zadania zależą inne zadania powinien to [ogarnąć] niezależnie od przypadku"; "gdyby A czekało na Z to refiner A też musiałby zapisać identyfikator do Z i zapisać zależność u siebie tak samo jak zrobiłby to refiner B w stosunku do A — przecież to jest ten sam przypadek"; "no oczywiście, że musiałby sprawdzić, przecież na ślepo by tej linii nie edytował"; "jeśli refiner A wie, że od jego zadania ma coś zależeć to dopisze zależność w B, jeśli nie to nic chyba nie zrobimy".

The rule, as the orchestrator restated it to him and he let stand: a refiner that knows from the plan that the task X it refines waits on Z, or that Y waits on X, brings the lines that exist into agreement: X's line carries its identifier and its own dependencies; the line of each task Z that X waits on carries that task's identifier; the line of each task Y that waits on X carries the dependency on X's identifier. It reads a line before it writes and adds only a field that is missing; it writes no line that does not exist yet for anyone, since that line's own refiner makes it complete. The rule holds for a new line and an existing line alike, and in whatever order the refiners of a round run. The orchestrator's correction of dependencies when the plan changes stays as it is. Make the one place of the rule `project-level/task_line.md`; the files that point to it keep pointing; where WAY-154 or WAY-329 describe who writes the identifier and the dependencies, make them say the same (the entries are edited in place, WAY-07; change nothing the human has not accepted beyond what this rule needs).

## Item 1 — the finding behind it (review of the return step, out of scope), in the reviewer's words

### Out of scope (beyond this dispatch, so counted here and not re-graded)

1. **A task that already has a line gets no identifier from the refiner.** `project-level/task_line.md:23-25`
   (code of the reviewed commits, `9eb2bd6` and `9d5743d`, not this range): where a line already
   stands for the task (for example one made by `/park`), the refiner links the document and writes
   nothing else, so that line carries no `🆔` derived under WAY-329, while a dependent task's line
   names that identifier in `⛔`. If the Tasks plugin treats a `⛔` naming an absent identifier as no
   dependency (my recollection, not checked), the ordering is dropped silently, and the clash check at
   `task_line.md:28-29` cannot see it. WAY-329's text ("the identifier of the line of a task of a
   project plan is ...") reads as if every plan task's line carries it. This is a gap of the reviewed
   code against the new entry, and it lies inside the task (row 5, *Questions carried to cycle*), so
   the orchestrator should decide whether it goes to the human's list; I make no verdict on it as
   blocking because the handoff says the reviewed code is not to be reviewed again.

## Item 3 — five Minor findings the human asked to have fixed, in the reviewers' words

The first four are from the review of the return step (its Minor findings 1-4); the fifth is Minor 2 of the review of the fix.

### Minor (within the task, not blocking)

1. **WAY-329's second binding sentence says "another line" without "of another task".**
   `foundations/decisions.md:10895-10898` (binding sentence: "an agent that finds another line
   carrying the identifier it derived writes nothing and asks the human"; the *complies* example
   speaks of a first and a second plan's task). Where the line carrying the identifier is the
   task's own earlier line (a late line, a parked task), `project-level/task_line.md:23-25` says make
   no second line and link the document, with no question; only a line of a different task is the
   clash (`task_line.md:28-29`, which says "another line" right after the own-line bullet). A reader
   of the entry alone would ask the human in the own-line case too. Effect: one needless question, no
   wrong write, so Minor. Evidence: the two texts side by side.
2. **The citation `(WAY-329)` stands on a sentence the entry does not say.**
   `project-level/task_line.md:40-41`: "A task that belongs to no plan has no identifier from the-way;
   a line of it takes one only where the rules require it (WAY-329)." WAY-329 states the derivation
   for "a task of a project plan" and holds nothing about a task of no plan; the derivation sentence,
   `task_line.md:35-38`, is the one WAY-329 says, and it carries no citation. A reader who follows
   the citation finds no support for the sentence it sits on. Effect: a misdirected pointer,
   cosmetic. Put the citation after the derivation sentence.
3. **The rewrap of WAY-320 does not do what the return report says.** The report says the lines were
   "rewrapped" from over 100 columns. `foundations/decisions.md:10532` is now 160 characters (the
   old 250-character line was only split once), and `foundations/decisions.md:10482` is 106;
   `foundations/decisions.md:2491` in WAY-107 is a 62-character line followed by a 101-character one.
   I found no written width rule and `foundation_check.py` passes, so the effect is only that the
   report's claim is not accurate and the diff stays hard to read. Minor. Evidence: line lengths read
   with a short PowerShell loop over the worktree file.
4. **WAY-154 and WAY-107 now hold more than three binding sentences.** The template and WAY-05 say
   one to three (`elements/decisions/template.md:25,104`; `foundations/decisions.md:126`). WAY-154's
   first paragraph now has five sentences (`foundations/decisions.md:4436-4458`; it had three at
   `52f8164`) and WAY-107's has four (`foundations/decisions.md:2437-2448`; three at `52f8164`). The
   foundation step's commit `74fbd01` made them so, outside this range, but the return step corrected
   both entries (it extended WAY-154's *Verification* and rewrapped WAY-107) and so owned reading
   them against the template. WAY-05's reason is that what binds stays short and checkable. No check
   catches it and each sentence is itself concrete, so the effect is a heavier binding part for the
   reader, not a wrong rule: Minor. I graded it Minor within the task rather than blocking because the
   rules the sentences hold are the ones the human accepted, and only their grouping departs from
   the form.

2. **Adjacent vocabulary in `read_sources.md`.** `project-level/task/skill/read_sources.md:17-24`: "link
   it from that entry" (older text) stands one paragraph above "Where the task has no line there yet".
   Both name the same object; Minor 6 asked for the two named places only, which are fixed. Cosmetic; and
   one wrapped line in `foundations/decisions.md:2488-2489` ("... reports a mismatch; a status of a line
   fixed in the-way's skills — a skill of the-way would assume") runs to about 140 characters.
