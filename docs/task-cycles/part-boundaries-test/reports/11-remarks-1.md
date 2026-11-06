# Remarks 1 — the human's remarks on the request

Request: https://github.com/mariusznazar/the-way/pull/77 (draft, head `79bd480`; reviewed tree `fbea390`).
Given by Mariusz in the orchestrator's session on 2026-11-06, in answer to the orchestrator's
summary, which recommended making item 4 of *For you to decide* a separate task before the loop2
task. Not posted on the request; quoted here word for word.

> "Rekomenduję zrobić z tego osobne zadanie przed zadaniem loop2. - a ja bym to jeszcze dociągnął w
> ramach tego tak samo poszerzenie zdania niezmiennika i testu"

(The first sentence is the orchestrator's recommendation, quoted by Mariusz; the words after the
dash are his.)

## What the remarks ask, as the orchestrator reads them

1. **Item 4 of *For you to decide* is made in this request, not as a separate task:** the review's
   Minor findings M1 and M2 (`reports/04-review-report.md`), in the reviewer's words:
   - **M1** — "a name that resolves to no file the check can see is dropped in silence, so an import
     that reaches another part through a directory another file put on `sys.path` passes unseen."
     Place: `elements/part-map/test_cross_part_imports.py:216-225` (`resolve`) and the docstring at
     :7-8. The reviewer's cheap fix: "report as a problem an absolute import whose first name is
     neither in `sys.stdlib_module_names` nor resolved — the same boundary `script-imports` states
     and `python-stdlib-modules` already supports."
   - **M2** — "several branches the author's report and docstring claim have no fixture, and
     mutating them leaves the whole file green": `extend` (:174-175), `sys.path = […]` and `+=`
     (:183-184), relative imports (:238-242), the `__init__.py` candidate (:219), dotted prefixes
     (:227-229), the file's own directory (:213), a marked sentence wrapped over lines (:98-104).
     "A fixture per claimed form would close it."
2. **Item 1 of *For you to decide* is answered by widening ("tak samo poszerzenie zdania
   niezmiennika i testu"):** running a Python file of another part as a script — by
   `runpy.run_path`, `runpy.run_module`, or a new process of the running interpreter
   (`sys.executable`) given a path or `-m` module — counts under the invariant as an import does,
   and its test reads such runs. The orchestrator's earlier answer Q1 ("No") is replaced by this.

Not asked: M3 and M4 stay Minor findings of the request.
