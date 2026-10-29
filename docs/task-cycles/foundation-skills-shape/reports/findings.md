## Blocking findings

### R1. Extract the missing-element-file variant from the shared reading step

**Grade:** Important. **Scope:** within the task, To do 2 and its assessment requirement. **Thread:** new. **Slice:** none; one-author change.

**Anchor:** `elements/common/way_of_working.md:47`; related assessment: `.runs/task-cycles/foundation-skills-shape/reports/assessment.md:160`.

**Do wklejenia:** The shared Read step still carries the complete procedure for a product that has no file for the element, although that procedure is needed only in that variant. The assessment combines it with ordinary reading and keeps the whole group, so To do 2's required variant split is incomplete. Move this procedure unchanged to a common companion, leave a conditional pointer at step 1, and update the assessment and route counts.

**Dlaczego to zgłaszam:** The task extends the split to fragments of `way_of_working.md` needed only in one mode or variant, naming Projected mode as the principal example rather than the entire scope. Its exception protects sections named by external readers; it does not protect every part of the ordinary shared stages. The remaining fragment is:

```text
- Where the product has no file of the element's entries, ask whether it starts that file here; if
  not, stop
  (`TODO — decision pending: which decision sets that a product starts an element's file only on
  the human's word`). If so, the same change gives the new file to a part of the map through
  `update-part-map` (WAY-44). Where the missing file is the part map itself, the current
  `update-part-map` invocation writes the first map directly, using its "The first map of a
  product" section. Where another element's file is missing and the product has no part map,
  `update-part-map` writes the map first (WAY-28, for a product the process enters;
  `TODO — decision pending: which decision sets that the part map is written before another
  element's first file`).
```

This contains several actions: obtain the start-file choice, stop on refusal, assign a new file to the map, avoid a recursive first-map invocation, and create the missing map before another element's first file. It therefore does not qualify for the one-instruction exception. For example, updating an existing decision log with an existing part map reads this entire procedure through the mandatory whole reading of the shared file, though none of these actions can apply. The projected route also carries it despite its explicit override not to start foundation files or write a map first. This is exactly the unnecessary variant reading To do 2 asks this change to remove; no numerical size threshold or claim about measured compliance is needed to establish the missed requirement.

The assessment's row for baseline lines 39–56 calls the whole group needed "At 1. Read" and keeps it because "Scope permits mode/variant extraction, not a new split of the common stages." That reasoning overlooks the distinct missing-file condition inside the group. The full caller search finds external references to the three named shared sections, and the source-finding skill's whole-file read; no external named-section reference protects this paragraph. A conditional pointer preserves those routes without splitting ordinary shared steps. Keep all existing TODOs and choices unchanged in the companion, and preserve the projected override. Recalculate the required counts; routes entering the missing-file variant should name its additional read explicitly. This correction needs neither a template change nor a new foundation decision.

The author's own-work verification checks that retained text is still present, not whether the assessment correctly identifies its trigger; therefore its successful run cannot catch this gap.
