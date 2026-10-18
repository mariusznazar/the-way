### Spec Compliance
✅ Compliant.
- The diff `784284c..fbf008b` touches exactly the ten files the brief lists (5 skills x `.claude` and `.agents`), each +1 -1. No other file changed.
- The one changed line in each file is the sibling list. It gains `maintain-styleguide` between `maintain-instruction-files` and `lead-project`. Nothing else differs.
- Independent check, read-only and in process: I imported `agent-instructions/skill_entry_points.py` and compared the bytes of `produce(discover(ROOT))` for the ten paths with the files on disk at head. All ten are byte-identical. None contains CR, so the line endings are LF as the generator writes them.
- The generator's output is a dict of 32 paths. The weakest-point check depends on the 20 paths outside the ten staying stale, and the diff shows the ten are the only ones touched.
- The report's other claims are consistent with the diff. I did not re-run the suites, as instructed.
- ⚠️ I ran `git checkout --detach fbf008b` in the worktree by mistake, then ran `git switch task/product-guidelines-styleguide`. HEAD is still `fbf008b` and the tree is clean, so there is no lasting effect.

### Strengths
- The files were written from `produce(...)` with no `--write` and no hand edits. The change is mechanical and was checked against the generator, not against how it looks.
- The commit message is in the repository's style and in English.
- The report records each check with its exit code and output path, and states the expected red states (the stale-entry-point failures of the other 20 files).
- The weakest-point check names the right risk, "exactly as the generator produces them", and tests it by comparing against the generator.

### Issues
**Critical:** none.

**Important:** none.

**Minor:**
- The weakest-point check relies on the generator's dry run, the `cmp` of each pair and `git status`. It does not compare against `produce(...)` byte for byte. This is covered indirectly: a clean dry run means no `would change` for those ten paths, and I confirmed the byte comparison independently. No change is needed.
- The report says the write script and its outputs live under `.runs/task-cycles/product-guidelines-styleguide/reports/`. They are not in the commit, so evidence that exists only outside the commit cannot be checked from the diff alone. I did not open them.

### Assessment
**Task quality:** Approved.

The ten files match the generator byte for byte (checked independently), there is no scope creep, and the line endings are unchanged. The weakest-point check (WAY-164) is adequate: it names the right requirement, tests it in a way that could fail, and its result holds up under my independent byte comparison.
