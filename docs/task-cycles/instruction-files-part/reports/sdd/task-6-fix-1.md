# Task 6 — fix round 1 (findings and the controller's ruling)

Task review (opus) of f97cbdd..9c5c722: the text equals the brief's block apart from the two listed
adjustments; README exact; WAY-127, WAY-132, WAY-133 carried. Fix in `instruction-files/SKILL.md` only:

1. **Important — SKILL.md:37-39 undoes the check script's safety boundary.** "Read too what its `info`
   lines say was left out — a link out of the repository, a network path, a file cut at its size limit"
   tells the agent to open exactly what the script refuses (spec §4.6), and the targets come from
   untrusted files. **Fix:** those lines are reported in the judgement (as Judge item 1 says), never
   followed: a network path is never read; a link out of the repository is read only after the human
   confirms it; the part of a file cut at the size limit may be read.
2. **Important — WAY-130's exception is missing** (SKILL.md:85-86, 108). WAY-130 (read it in
   `foundations/decisions.md`) lets a rule in without a repeated mistake when it "carries a decision the
   repository records or a step of an activity in the file that leads that activity". **Fix:** add the
   exception to Judge's ground (a third ground: the decision or the activity step it carries, named) and
   to Place step 1.
3. **Minor 3 — removal against WAY-130** (SKILL.md:87-88 says a removal whose mistake cannot be named is
   "proposed as a removal test, never as a plain cut"; WAY-130 says the skill proposes to take out a rule
   "once that mistake can no longer be named, or once agents working without it show that it is not
   needed"). **Fix:** a rule whose mistake can no longer be named is proposed for removal; a rule whose
   mistake is named but may no longer happen is proposed as a removal test. (Task 7 will align
   `principles.md` §7 with the same words.)
4. **Minor 1** — "(a network path is refused, with exit code 2)": say it holds on Windows, or drop it.
5. **Minor 2** — the list of what was left out also has "a link to a directory, not followed" and "a
   directory that cannot be listed"; make the list complete or say "for example".
6. **Minor 4** — when `.the-way/` holds no `instruction-files/`, tell a pin without it (move the pin)
   from an uninitialised submodule (initialise it): check
   `git -C <repository>/.the-way cat-file -e HEAD:instruction-files/SKILL.md` and whether `.the-way/`
   is empty.
7. **Minor 5** — the mistakes-table row "using `@path` as a pointer → a path in backticks" gains "with
   the condition under which to read it".

Keep the frontmatter unchanged (`skill_entry_points.py` must still print `entry points are current`);
no private paths, no `.runs/`. Write/Edit tools only. Commit by path with the `Claude-Session:` line.
Append "Fix round 1" to `task-6-report.md` (each change with the sentence before and after) and reply
with the short status contract.
