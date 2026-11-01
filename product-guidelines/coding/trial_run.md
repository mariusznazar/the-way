# Trial run

Where the product has code:

- **Trial run** (WAY-204). Run the linter's set — the one the product runs with the additions or
  corrections step 2 proposes, or the one step 2 proposes from preferences or research — at the
  version read from the product's files or the proposed tool's documentation, on the product's
  code in a scratch worktree of its commit or in a temporary environment, outside its working
  tree: the tool is installed only there, never into a file git tracks, and the scratch worktree
  is removed afterwards. Its output goes to `.runs/coding/`.
- Give one fresh agent that wrote none of that code each report with the code it points to, and
  ask it to judge whether the report leads to a change of code worth making, whether the report is
  technically right or not; its verdicts go beside the output. A rule with one report that leads to
  no such change goes among the examples, and the rest of the set blocks. Where the set cannot run
  there, or no fresh agent can judge, no split is proposed: stop and say so. The split goes to
  step 4 with its evidence.
- In the same place, count the files that break the rules that block and the files the formatter
  would rewrite: where the code breaks those rules, step 4 proposes the linter's invariant marked
  violated; where the formatter would rewrite it, the one reformatting of the whole of the code
  (WAY-205).
- Group the reports of the rules that block by one reason: each reason is a cause of the audit's
  list, told by its effect, its place the number of files, with no rule's name, and the output's
  path stays in *Context* (WAY-281). The rules that went among the examples flagged sound code and
  yield no cause. The formatter's count never enters the list: a reformatting is no finding.
