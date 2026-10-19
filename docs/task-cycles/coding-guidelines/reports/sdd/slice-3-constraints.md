Global constraints for Slice 3:
- Spec §5.2 items 3 and 4 and §5.3 (crafted inputs for paths, index rows, exemplar tables,
  decisions, 1 MiB lines). Item 3: every `guidelines/coding-<kind>.md` git lists named by a row of
  `## Kinds of code` whose *File* is that path; every row names a kind file git lists; a kind file
  with no `guidelines/coding.md` an error; plus (C31) a row whose *Kind* is not its file's kind or
  whose *When to read* is empty. Item 4: in `## Files of this kind` exactly one `exemplar` row; every
  *Status* on the closed list (`exemplar`, `copy`, `do not copy`); every *File* passing `refused()`
  and naming something git tracks; the exemplar row's *Decision* a decision of the log whose binding
  sentences hold `` `<path>` `` and `` `<kind>` `` after whitespace is collapsed; `—` on other rows;
  its fingerprint checked as every reference is. No completeness asked (C13). *File* cells in
  backticks (C32).
- WAY-38 stdlib only; WAY-48 trust boundary: no crafted path reaches git or is opened, no socket,
  bounded time, no regular expression with nested repetition. Command, options, exit codes
  unchanged; each finding an error of `guidelines-form/1`.
- Covered invariants (deliberate break by you): `guidelines-check-kind-index/1`,
  `guidelines-check-exemplar/1`.
