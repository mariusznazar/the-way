# Task 6 report

## Changed
- `installation/install.py:128`: one literal in `skill_wrapper`, "Its paragraph about resolving a global skill link applies only to a global install; " replaced by "Where it says where the-way lies, the product's case applies: ". Nothing else (no new input, path, argument or subprocess).
- `installation/test_install.py`: new method `test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies`, before `test_guidance_names_no_commit_and_covers_the_product_rules`, verbatim from the brief.

## TDD
- RED: `python -B gate/run_tests.py installation` -> exit 1, `Ran 17 tests`, `FAILED (failures=11)`; each subTest failed with `AssertionError: "Where it says where the-way lies, the product's case applies: here the process root is `.the-way`." not found in "---\nname: the-way-record-decision ..."`. Expected: the old literal was still in place.
- GREEN: same command after the change -> exit 0, `Ran 17 tests`, `OK` (output in `.runs/task-cycles/the-way-skills-in-the-way/reports/check_6_tests_installation.txt`).
- `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl` -> exit 0, `Ran 98 tests`, `OK`. Partial check, not a pass of the full gate.

## Commit
bb9f8ad fix(installation): Point a product's skill wrapper to the product case of where the-way lies (author <author email>), by explicit paths.

## Self-review
Diff is 1 line changed in install.py and 9 added in the test. Line 129 untouched. The existing adversarial installer tests ran in the same green suite.

## Concerns
None.
