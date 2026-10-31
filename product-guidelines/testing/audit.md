# Audit

Where the product has tests (WAY-250):

- **Levels** (WAY-242, WAY-250). Name the levels the product's tests already stand at, each with its
  tests; the audit covers every one of them. For each level, judge its tests, compare them, and
  propose:
  - its exemplar test, with one sentence of what the product gains by it, such as "every new
    integration test sets up its data through the fixtures as this one does";
  - three to five charges, each with its file and line and one sentence of its effect, measured
    against the rules of the testing template and those the product holds — such as a test that
    builds the value it expects by calling the function under test, so that it passes whatever the
    code gives. A charge the task does not take up stays in *Context*, marked deferred with its
    reason.
- **Trust boundaries** (WAY-250, WAY-235). For each trust boundary of the product's map, say whether
  a test checks its refusal directly, with that test's file and line, or that none does.
- A choice found in the product's tests — a configuration of the test tool, a habit its tests share
  — is a proposal, never a rule, until the human settles it. An existing choice the human keeps
  becomes a decision whose rationale is the human's words or `unknown`, never one the agent infers
  (WAY-29).
