# Settle with the human

- **New tools.** For each new tool or library left as a technology question of the task, read
  `new_tools.md` beside this skill.
- **What it settles.**
  - the product's decision adopting the testing template, and each departure from it by a decision
    with its reason (WAY-173);
  - the levels of the product's tests, each with the decision that sets it; for a level whose name
    means in the product something other than in the field, the entry of the product's glossary
    that defines it by the resources its test may touch; and, for each part the guidelines apply to,
    whether its complexity lies in computation or in its connections (WAY-240, WAY-226);
  - the product's documents that are sources of expected values (WAY-232);
  - for each level, the fields of its recipe that bind, each with the decision that carries it, the
    template's defaults adopted or departed from (WAY-241);
  - for each level with tests, its exemplar test, and for a new level of step 3 (`new_level.md`),
    that the task's first test of it becomes the exemplar (WAY-242). Where the level of a task's tests
    is its cycle's choice, the refinement designates no exemplar test: the cycle's author who writes
    a level's first test proposes its designation at a blocked draft request (WAY-242, WAY-172);
  - each category the product deliberately does not test, with the decision that gives its reason
    and the condition under which it is tested again; a trust boundary is never one (WAY-237);
  - the product's decisions on permissions from which the rows of the authorization table come
    (WAY-235);
  - each AI tool the product's tests use, with the environment fact of how it behaves at the version
    the product uses (WAY-236);
  - for the parts whose complexity lies in computation, whether the product adopts a mutation tool,
    with the tool, a technology choice as "New tools" gives it, and the parts it runs on, or departs
    from the rule of mutation testing with its reason (WAY-252).
- **Invariants.** A binding rule gets an invariant where a cheap test checks it on a convention of
  the product's code; a rule no such test checks gets none, and the review of each change it reaches
  compares the change with it (WAY-168). The rule of trust boundaries always gets its invariants
  (WAY-235). Propose, each with a test of the product's suite (WAY-61):
  - for each trust boundary of the product's map, at least one invariant that the boundary refuses
    crafted input or unauthorised access, its test checking the refusal directly, taking the
    expected refusal from the product's decisions on permissions and seen failing once (WAY-235,
    WAY-08); a boundary that is only the configuration of someone else's service stays with the
    review of each change that touches it (WAY-48);
  - where a boundary does not refuse today, its invariant marked violated by a change of the
    foundation the human accepts, until the boundary refuses (WAY-51); its weak point, that until
    then no test guards the boundary and only the review of each change touching it keeps that
    change from letting more through, is said when it is proposed;
  - for each further rule that a cheap test checks, an invariant that checks it (WAY-168).
- **Weak points.** Name each when its choice is proposed:
  - for an exclusion, that it ages unless someone checks its condition of return whenever a change
    reaches its category (WAY-237);
  - for the rule of trust boundaries, that it is only as good as the part map that names the
    boundaries (WAY-235);
  - for property tests, that a simpler version copied from the code makes a property test a mirror
    of it, which only the review catches (WAY-228).
- **Critique.** Once the set of proposals is complete, one fresh agent critiques it before it is
  shown together, as "Critique before collective review" in `elements/common/way_of_working.md`
  gives (WAY-120). Read that section and, unless step 2 did, `elements/common/critique/SKILL.md`.
