Global constraints for Slice 1 (from the spec and rulings, verbatim where possible):
- Spec §5.1 (all bullets) as amended by C33: a test case's text holds no line that, after any
  leading whitespace, starts with three backticks or three tildes.
- C1: the test-case rule applies to every discipline. C11: a rule whose *Invariant* is
  `guidelines-form` gives *Good*/*Bad* as descriptions, no blocks. C18: one `good <identifier> <path>`
  and one `bad <identifier> <path>` block per named invariant other than `guidelines-form`, after the
  four fields. C19: a listed invariant read against the commit's own result; per-file companion
  strict. C21: a bare fence inside a case closes the block; the form check reports the malformed case.
- WAY-171: each rule of a template cites the decision that sets it; templates follow decisions, no
  value copied. WAY-167 (edited) file names: `guidelines/coding.md` with its table of kind files,
  `guidelines/coding-<kind>.md`.
- The required form of the common template must still parse exactly as before (the form check reads
  it); no field name changes.
