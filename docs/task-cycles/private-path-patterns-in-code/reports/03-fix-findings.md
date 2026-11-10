# Findings for the fix — Minor findings of the review of the whole change (report 02)

The review of the whole change returned `PASS 287a02712e683f4a3694d5ef46b795b253a1b1fc` with no
blocking finding. These are its Minor findings within the task, in the reviewer's words; the
reviewer alone graded and scoped them.

1. **`foundations/decisions.md:10316-10318` — a number in WAY-320's rationale is not the source's.**
   The sentence reads: "in code the same brackets are an array inside an array or a test of the
   shell, and a run of the check over every tracked file of one public product on 2026-11-09 listed
   73 such texts among 88 findings." The task (`task.md:27`) gives 73 `[[...]]` hits of which 70 are
   arrays in arrays and 1 a shell class — 71 "such texts" — while the other 2 are specification slots
   in a Markdown file, which the `.md`-only rule of WAY-320 does not remove (WAY-323 does). The
   rationale therefore credits the rule it argues for with two hits it does not remove. It binds no
   behaviour, so Minor; fix: "71 such texts" or "73 note-link-shaped texts, 71 of them in code".
   Evidence: `task.md:27`; WAY-323's rationale (`foundations/decisions.md:10445-10447`) states the
   split correctly.

2. **`installation/README.md:109-112` — the exit codes a product relies on are given in part.**
   The README is the only text a product reads before writing its test, and WAY-324 makes the
   command's exit codes something the product relies on. The README names exit 2 only for "the
   identifier is missing from the invariants file or the sentence names a file git does not track";
   the command also exits 2 for a missing argument, a directory outside a git repository, a missing
   `foundations/invariants.md`, and a tracked file that is not UTF-8
   (`task-cycle/tracked_private_paths_check.py:20-23`). The last one is the one a product is likely
   to meet (a tracked text file in another encoding) and the README says nothing about it. Also
   unsaid at `installation/README.md:85-86`: every backticked text of the sentence is taken as a file
   name, so a product that writes, say, a backticked word in its sentence gets exit 2. The test fails
   with the message in both cases, so nothing passes silently; Minor.

3. **`installation/README.md:82-87` — the invariant a product is told to write lacks its
   *Derives from*.** The README tells the product to write the invariant "as WAY-309 and WAY-323 name
   them" and gives its method, but not what it derives from. `elements/invariants/template.md:122-124`
   makes *Derives from* mandatory and `:139-142` says a decision of the-way at the pinned commit "is no
   decision entry" of the product, so a product following the README alone has no valid value
   (WAY-324 or WAY-320 of the-way would be wrong there). An agent writing the entry through
   `the-way-record-invariant` will meet this and write `TODO` or ask; the README could say that the
   product records its own decision (its repository is public, no private paths in tracked files) or
   names a source. Minor: the task's item 6 asks for the invariant with the list and the method
   `test`, which the README gives.
