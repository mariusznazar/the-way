Global constraints for Slice 4:
- Spec §5.2 item 5 and §5.3 bullets 4, 5, 7, with rulings: C11 (a rule whose *Invariant* is
  `guidelines-form` needs no blocks), C18 (one `good <identifier> <path>` and one
  `bad <identifier> <path>` block per named invariant other than `guidelines-form`; a block naming an
  invariant the rule does not name is an error), C21 (a bare fence inside a case closes it; the
  stray block is a malformed test case), C33 (no line inside a case that, after ANY leading
  whitespace, starts with three backticks or three tildes; the form check reports it), C12 (short
  files, path limits, 1048576-byte file limit). Info string read only from an opening fence; every
  fenced block of a rule that carries test cases is a test case.
- `product-guidelines/template.md` "Test cases of a rule" (Slice 1) promises these reports — each
  must now exist. The coding template (`coding/template.md`, section on the product's copy of
  `guidelines-form`) promises the copy's checks — complete after this slice.
- WAY-38 stdlib only; WAY-48 trust boundary: no case path opened, given to git or written; no
  regular expression with nested repetition; bounded time. Command, options, exit codes unchanged.
- Covered invariant (deliberate break by you): `guidelines-check-example-files/1`.
