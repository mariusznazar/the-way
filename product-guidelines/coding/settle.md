# Settle with the human

On the route of one kind, settle of the choices and invariants below only what "The route of one
kind" in `SKILL.md` gives; the critique below stands.

- **New tools.** For each new tool or library left as a technology question of the task, read
  `new_tools.md` beside this skill.
- **The library that writes a log line.** Look first at what the product has: a way of writing the
  chosen form of a line that the product or its language already gives raises no question (WAY-210).
  Where the form needs a library, the choice stands as a technology question of the task, put to the
  human by `new_tools.md`, with no research, and a library chosen is a decision of its own in the
  product's log (WAY-277). Where that library meets the test of
  `project-level/technology/reserved_choices.md`, as one that adds something to run or pay for, it
  is a reserved choice: refinement runs `settle-technology` at the task document instead, and the
  task is not ready until the human has settled it (WAY-268).
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
    with its reason (WAY-173);
  - where `guidelines/coding.md` does not yet hold them, at the first guidelines, at any extension
    whatever else the task is about, and at a refresh `recognize.md` sends here, the product's one
    decision on the rules on failures and logs, adopting them or departing from them with its reason,
    apart from the decision adopting the coding template; the task is not ready without it
    (WAY-271, WAY-278, WAY-279). It takes:
    - the rules, asked of as a whole. First say in plain words what logs are: the running record of
      what the product does, which someone reads when something has gone wrong. Then show the rules
      by their effect: when something goes wrong for a user the logs say what broke and why, the
      product never pretends all went well, what happened to one order can be found, and no password
      or personal detail lands there;
    - a departure, taken when the human reports it, from one rule or from the ban on personal data.
      Say first what goes with it, as "Departing from the rules on failures and logs" in the coding
      template gives: a human who leaves `### Logging scope` hears that two more rules go, and one who
      drops `### Secrets and personal data` hears that the ban on secrets goes. A wish to log what
      points to a person is put first as an item of the list (WAY-174, WAY-273, WAY-274, WAY-276);
    - the form of a log line (WAY-275). The human hears a case flow as everything the product did
      for one order or one request;
    - the principle of the logging scope: which identifiers and which business events the product
      logs, and the boundary of what an agent adds alone, an item that fits the principle, an
      identifier of a thing among them, while whatever points to a person takes the human's consent
      (WAY-274);
    - the list of today, at adoption from what the product has in its code or in its plan, and the
      number the product gives a user, put to the human at that moment, which takes the human's
      consent if added later (WAY-274).
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
    each further rule of the whole product, an invariant where a cheap test checks it (WAY-168);
  - for a rule on failures and logs, none, unless a cheap test checks the whole rule. A test that
    catches only a fragment of one, such as an empty block that catches an error, is a rule of the
    linter's set under the linter's invariant, once it passes the trial WAY-203 gives, and no rule
    of these (WAY-271).
- **Weak points.** Name each when its choice is proposed:
  - for a product with no code, that the recommended rules block with no evidence from the
    product's code, and that the first report of one that leads to no change worth making takes it
    among the examples by a change of the decision, which the human approves (WAY-204);
  - for the audit of dependencies, that a vulnerability found in a dependency the product already
    holds gives no signal while no change brings in a version of it, and that a later run on the
    same commit can fail where an earlier one passed, once an advisory is published for a version
    that commit brings in (WAY-206);
  - for the logging scope, that a list written by hand can drift from the code, and that an agent
    judges whether an item fits the principle (WAY-274);
  - for the ban on secrets and personal data, that the reviewer sees code and not what an error holds
    at run time, so an unusual leak can pass, and that whether a user's number in the logs is lawful
    stays the product's to judge (WAY-276);
  - for what counts as a failure, that an agent and the reviewer judge the line between a failure
    and a refusal, and that a degraded mode leaves a line while the user sees a working page, so
    nobody knows unless someone reads the logs; how a human learns of a failure belongs to the step
    that settles technology (WAY-272, WAY-273, WAY-270);
  - for the business events, that the rule covers only listed events and the agent adds them, so a
    function nobody lists leaves no line (WAY-275);
  - for the last-resort handler, that it usually writes without identifiers, and that a program that
    dies whole writes only what it manages to (WAY-272).
- **Critique.** Once the set of proposals is complete, one fresh agent critiques it before it is
  shown together, as "Critique before collective review" in `elements/common/way_of_working.md`
  gives (WAY-120). Read that section and, unless step 2 did, `elements/common/critique/SKILL.md`.
