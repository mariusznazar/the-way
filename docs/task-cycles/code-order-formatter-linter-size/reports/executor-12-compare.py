import importlib.util
import sys

WORKTREE = "the worktree's root"
sys.path.insert(0, WORKTREE + "/task-cycle")
sys.dont_write_bytecode = True
import test_request_check as fixtures  # noqa: E402  (the fixtures of the test file)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


old = load("request_check_old", WORKTREE + "/.runs/executor-12/request_check_orig.py")
new = load("request_check_new", WORKTREE + "/task-cycle/request_check.py")

descriptions = [
    fixtures.VALID,
    fixtures.with_block(fixtures.VALID, fixtures.ENGLISH_BLOCK),
    fixtures.with_block(fixtures.VALID, "none"),
    fixtures.with_block(fixtures.VALID, "   "),
    fixtures.with_block(fixtures.VALID, "  "),
    fixtures.with_block(fixtures.VALID, "  "),
]
tasks = [fixtures.POLISH_TASK, fixtures.ENGLISH_TASK, fixtures.POLISH_PLAN, fixtures.ENGLISH_PLAN, fixtures.SHORT_TASK]

cases = []
for description in descriptions:
    lines = description.split("\n")
    cases.append(description)
    for index in range(len(lines)):
        cases.append("\n".join(lines[:index] + lines[index + 1 :]))
        cases.append("\n".join(lines[:index] + ["## Extra", ""] + lines[index:]))
        cases.append("\n".join(lines[:index] + ["<details>", ""] + lines[index:]))
        cases.append("\n".join(lines[:index] + ["### Underneath", ""] + lines[index:]))
        cases.append("\n".join(lines[:index] + ["### Needed from you", "- item", ""] + lines[index:]))
        cases.append("\n".join(lines[:index] + ["```", ""] + lines[index:]))
        cases.append("\n".join(lines[:index] + ["<!-- note -->", "Some words here are in English so the language is judged."] + lines[index:]))
        cases.append("\n".join(lines[:index] + ["## <…>"] + lines[index:]))
    cases.append(description[: len(description) // 2])
    cases.append(description[: len(description) // 3])
    cases.append("")
    cases.append("\n\n")

compared = 0
differences = 0
for description in cases:
    for task in tasks:
        left = old.check(description, task)
        right = new.check(description, task)
        compared += 1
        if (
            left.problems != right.problems
            or left.sections != right.sections
            or (left.task_language, left.task_words) != (right.task_language, right.task_words)
            or (left.block_language, left.block_words) != (right.block_language, right.block_words)
        ):
            differences += 1
            if differences <= 3:
                print("DIFF on case", compared)

problem_total = 0
for description in cases:
    problem_total += len(old.check(description, tasks[0]).problems)
print("cases", len(cases), "tasks", len(tasks), "compared", compared, "differences", differences, "problems seen", problem_total)
