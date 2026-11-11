# Findings of the review of the correction (head 047a9e7606e90dc164762bebb0c6bc48dcd46eeb), in the reviewer's words

Source: `reports/correction-review-report.md`, the section "New defect in the correction", copied without change. The one blocking finding; the three Minor findings of that review are not fixed in this round and go to the request's list. Paths are relative to the worktree.

## New defect in the correction

### B1 (Important, within the task). Four skill files give a refiner a write that WAY-154 does not give it

- Place: `project-level/task/skill/orchestrated_mode.md:41-43` ("bring it and the lines of the tasks tied
  to it into agreement"), `project-level/lead/conversation_template.md:22-24`, `project-level/lead/skill/SKILL.md:105-106`
  ("each makes its task's line and brings the lines of the tasks tied to it into agreement"),
  `project-level/plan/skill/delegated_mode.md:9-10` ("refiners write only separate task documents/conversations
  and the backlog lines of their tasks and of the tasks tied to them (WAY-154)"), and
  `project-level/task_line.md:42-47`; against WAY-154's binding sentence in `foundations/decisions.md`
  ("...the line of its task in the backlog the product names (WAY-107), where none stands, with the
  dependencies the plan gives the task ...").
- What is wrong: WAY-154 lists what a refiner may write besides what the order asks, and the list holds
  the refiner's own line, made in its first turn or the first later one, where none stands. The skills now
  have the refiner also write the lines of the tasks it waits on and that wait on it (a different task's
  line, one that already exists). That is a broader write than the entry gives, in the files and in
  `delegated_mode.md`, which cites WAY-154 for it (WAY-263: files that restate an entry more broadly than
  it says are an Important departure). WAY-107's new sentence names "the agreement of the lines at both
  ends of a dependency" only as a matter of the place's rules; it says nothing of who writes. `grep -rn
  "tied to" foundations project-level product-guidelines` finds the phrase in the four skill files and in
  no entry. WAY-154's *Verification* (complies and violates), its *Rationale* (the accepted cost covers
  "two writes to the one backlog file in the same instant can lose a line", of lines being made, not of
  several refiners editing one task's existing line) and WAY-329's relation to it are likewise silent.
  The second direction says the-way keeps what only it knows, and who writes what is the-way's own: the
  same direction keeps "a refiner never moves a line to ready" in WAY-154.
- Why it matters: a later agent reads WAY-154 as the authority for what a refiner may write and the
  four skill files as what to do; one of them tells refiners to edit other tasks' lines, the other does
  not allow it. A reviewer or a refiner that follows the entry will not touch a tied task's line, and
  the human's rule of item 1 is then not carried out, or is carried out against the entry.
- Fix (either is enough, the first is the smaller): add to WAY-154's second binding sentence that the
  refiner also brings the lines of the tasks tied to it into agreement with the plan's dependencies as
  the rules of the task place give, mark it as the human's remark at the request, and add the same to the
  *Verification* examples and to the *Rationale*'s accepted risk; or take "and of the tasks tied to
  them" out of the four skill files and leave the write only in the one sentence of `task_line.md`,
  which would still need the entry to say it. I recommend the first.
- Evidence: the texts side by side; the word diff above shows WAY-154's text in `047a9e7` differs from
  `7ca8642` only in the three joins, so the entry was not given the tied-line write.
