# Findings for the fix — blocking findings of the review of the return step (report 06)

The review of the return step's commit `3057f16` (range `578a8bd..3057f16`) returned
`FAIL 3057f161ed49c7a4de582243f334dc8807b71d04`, with two blocking findings, both Important and
within the task. These are the findings in the reviewer's words; the reviewer alone graded and
scoped them.

1. **`foundations/part_map.md:213-214` — the surface drops the qualification "in a Markdown
   file" for note links.** The entry says the command "checks the files git tracks ... for
   absolute paths and note links". The code looks for note links only in a file whose name ends in
   `.md` (`task-cycle/tracked_private_paths_check.py:110`,
   `note_links=name.lower().endswith(MARKDOWN_SUFFIX)`; test
   `task-cycle/test_tracked_private_paths_check.py:78`
   `test_a_note_link_is_listed_in_a_markdown_file_only`). That restriction is the settlement of the
   task's question 1 (*Settlements to record* row 1), and every other account of it in the change
   carries the qualification: the invariant (`foundations/invariants.md:88`, "an absolute path or,
   in a Markdown file, a note link") and the installation section (`installation/README.md:116`,
   "each note link in a Markdown file"). The surface is the entry a product reads as the promise of
   the command; read as written, a product expects a `[[...]]` in a `.txt` or `.py` file it tracks
   to be listed, and it is not. A foundation entry the change writes that restates the rule without
   its qualification is Important by WAY-263. Fix: "for absolute paths, and for note links in
   Markdown files," or drop the "for ..." clause and identify the command by its path.

2. **`installation/README.md:121` — the installation section restates the promise the new
   surface makes, differently.** It says "the command keeps its name, argument and exit codes, the
   functions are not promised"; the surface (`foundations/part_map.md:215-216`) says the command
   "keeps its path, its argument, the meaning of the backticked texts in that sentence and its exit
   codes". Two differences: *name* against *path* — the product's test in the same section
   hardcodes the directory (`installation/README.md:104`), so a move inside the-way that keeps the
   file name breaks every product while the section says nothing was promised there; and the meaning
   of the backticked texts, which the surface promises and the README's sentence of promise leaves
   out (item 1 at `:84-87` describes the reading, but not as something kept across moves of the
   pin). The README line predates this range (`578a8bd`), but writing the surface made it a second
   account of the entry, and the return step corrects in the same change whatever no longer matches
   it (`task-cycle/skill/return_step.md:6-8`, WAY-11); the README is the file of *To do* 6, within
   the task. Another changed file repeating an entry the change writes, differently, is Important by
   WAY-263. Fix: "the command keeps its path, its argument, the meaning of the backticked texts and
   its exit codes (the surface `tracked-private-paths-command` of the-way's part map); its functions
   are not promised."
