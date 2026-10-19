Global constraints for Slice 11:
- Spec §6.5–§6.6: `SKILLS` gains `"maintain-coding-guidelines": "product-guidelines/coding/SKILL.md"`;
  no other installer text changes (surface `installation-command` keeps its wording);
  `installation/README.md` names the skill in its table and its test list; a new ordinary test on
  the pattern of `test_styleguide_installation.py`. C36: `test_styleguide_installation.py:92` 30→32.
  C37: the non-UTF-8 case asserts exit≠0 and nothing written; the pre-existing traceback is a
  concern, not this task.
- `installation/install.py` is a trust boundary (WAY-48): crafted inputs stop before anything is
  written. `installation/test_install.py` (F4, read-only) NAMES tests must pass.
- Covered invariant (deliberate break by you): `installation-claude-guidance/1` through the changed
  NAMES test — remove the new SKILLS entry in a scratch worktree and record that a test citing the
  invariant fails.
- Final check set as the brief lists, every exit code and unchecked line kept.
