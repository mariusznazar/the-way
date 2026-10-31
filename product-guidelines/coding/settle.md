# Settle with the human

On the route of one kind, settle of the choices and invariants below only what "The route of one
kind" in `SKILL.md` gives; the critique below stands.

- **New tools.** For each new tool or library left as a technology question of the task, read
  `new_tools.md` beside this skill.
- **What it settles.**
  - for each standing check, the product's decision adopting it or departing from it with its
    reason; the task is not ready without one for each (WAY-202);
  - for the linter, its tool, its set, the set's edition, the parts it reads and the split of the
    set, said together with what the split means later: a fault of one file is fixed in that file,
    and turning a rule off for the whole product takes a change of this decision, approved by the
    human (WAY-203, WAY-204, WAY-207);
  - for the formatter, its tool and its configuration;
  - for the audit of dependencies, its tool, the advisory database it reads and the severity from
    which a vulnerability counts, every severity among the ways (WAY-206);
  - for each kind the product holds files of, and each new kind, its exemplar, the status of each
    of its files and the rules a script checks of the exemplar (WAY-198, WAY-199, WAY-200,
    WAY-201);
  - the product's decision adopting the coding template, and each departure from it by a decision
    with its reason (WAY-173).
- **Invariants.** A binding rule gets an invariant where a cheap test checks it on a convention of
  the product's code, the rule of each standing check always; a rule no such test checks gets none,
  and the review of each change it reaches compares the change with it (WAY-168, WAY-202). Propose,
  each with a test of the product's suite (WAY-61):
  - for the rule of each standing check, the invariants the coding template's section "What each
    section carries" names for it, with the parts it gives them;
  - for the linter, the flag or the configuration by which its test makes a comment that turns a
    rule off have no effect, where the tool has one, and the review of each change to the linter's
    configuration as what keeps that configuration to the decision (WAY-203, WAY-207);
  - where the code breaks the rules that block, the linter's invariant marked violated by a change
    of the foundation the human accepts, until the code is cleaned (WAY-205, WAY-51); its weak
    point, that until then no test shows a report coming back into a cleaned file or reaching a new
    one and only the review of each change to those files keeps them from gaining one, is said when
    it is proposed;
  - for each rule a script checks of an exemplar, an invariant that checks it (WAY-198), and for
    each further rule of the whole product, an invariant where a cheap test checks it (WAY-168).
- **Weak points.** Name each when its choice is proposed:
  - for a product with no code, that the recommended rules block with no evidence from the
    product's code, and that the first report of one that leads to no change worth making takes it
    among the examples by a change of the decision, which the human approves (WAY-204);
  - for the audit of dependencies, that a vulnerability found in a dependency the product already
    holds gives no signal while no change brings in a version of it, and that a later run on the
    same commit can fail where an earlier one passed, once an advisory is published for a version
    that commit brings in (WAY-206).
- **Critique.** Once the set of proposals is complete, one fresh agent critiques it before it is
  shown together, as "Critique before collective review" in `elements/common/way_of_working.md`
  gives (WAY-120). Read that section and, unless step 2 did, `elements/common/critique/SKILL.md`.
