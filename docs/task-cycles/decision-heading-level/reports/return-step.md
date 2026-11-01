# Return step — decision-heading-level

**Status:** done. **Commits:** none (head stays `168b055`).

**Foundation compared with code**
- WAY-150 (`foundations/decisions.md:3919`): says an entry is read whole and the rest by selective search; it names no heading level. The insertions add no conflict.
- WAY-256 (`:7348`): a fragment of one step that is one instruction stays in `SKILL.md`; the `change/SKILL.md` insertion is a clause in an existing bullet, so it complies.
- WAY-35 (read earlier): the shared way of working stands once in elements-common; the insertion sits there, and the skill clause only points to the same fact.
- Part map `elements-common` and `task-cycle` (`foundations/part_map.md:65`, `:92`): files `elements/common/**` and `task-cycle/**`, trust boundary none; both edited files belong to them, nothing to change.
- Search of the foundation for an entry stating a heading level or how far an entry runs: `heading`, `next heading`, `###`, `##` over `foundations/` found only `glossary.md:45` (an entry is the text under one or more headings of its own) and `invariants.md:200` (unrelated). Both agree with the insertions. Positive control: the same search style found `part_map.md` headings and `glossary.md:45`.

**Decisions:** none. **Invariants:** none. **Environment facts:** none. **Glossary terms:** none. **Part-map changes:** none.

**Checks:** no new run; the earlier `foundation_check.py .` (exit 0) and `gate/run_tests.py task-cycle` (exit 0) cover the unchanged tree. The full gate not run.

**Searches not found or unclear:** none. The review's Minor finding on line wrapping was left as it stands.
