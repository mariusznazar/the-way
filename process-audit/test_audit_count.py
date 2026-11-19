"""Tests of process-audit/audit_count.py, run on temporary git repositories and temporary
locations files, never on the user's own."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "audit_count.py"

# Git reads neither the user's global configuration nor the system's, as in
# project-level/test_plan_state_invariant.py.
NO_USER_GIT_CONFIG = {"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
GIT_ENV = dict(
    os.environ,
    GIT_AUTHOR_NAME="Tester",
    GIT_AUTHOR_EMAIL="tester@example.com",
    GIT_COMMITTER_NAME="Tester",
    GIT_COMMITTER_EMAIL="tester@example.com",
    GIT_TERMINAL_PROMPT="0",
    **NO_USER_GIT_CONFIG,
)

PIN = "0123456789abcdef0123456789abcdef01234567"
BASE = "89abcdef0123456789abcdef0123456789abcdef"
# The four tools that write a file of a cycle's copy and whose change by a cycle the count notes.
STAGE_SCRIPT = "task-cycle/cycle_stages.py"
MEASURES_SCRIPT = "task-cycle/cycle_measures.py"
GATE_SCRIPT = "task-cycle/gate_times.py"
GATE_RUNNER = "gate/run_tests.py"
TOOLS = (STAGE_SCRIPT, MEASURES_SCRIPT, GATE_SCRIPT, GATE_RUNNER)
CHANGED_WHY = "the cycle changed the tool that wrote them"

# The register of problems, as the template gives it; the tests add rows under its headers.
TEMPLATE = (HERE / "problem_register.md").read_text(encoding="utf-8")
CLASSES_HEADER = "| Class | Meaning | Added | Withdrawn |\n|---|---|---|---|\n"
ISSUES_HEADER = "| Issue | What | Fate | Fix |\n|---|---|---|---|\n"
PROBLEMS_HEADER = (
    "| Repository | Record | Stages | What | Class | Weight | Cost of an occurrence "
    "| Issue |\n|---|---|---|---|---|---|---|---|\n"
)


def register_text(classes=(), issues=(), problems=()) -> str:
    """The template of the register with rows added under the headers of its tables."""
    text = TEMPLATE
    for header, rows in (
        (CLASSES_HEADER, classes),
        (ISSUES_HEADER, issues),
        (PROBLEMS_HEADER, problems),
    ):
        assert text.count(header) == 1, header
        text = text.replace(header, header + "".join(row + "\n" for row in rows))
    return text


def issue_row(name, fate="open", fix="none") -> str:
    return f"| {name} | the matter | {fate} | {fix} |"


def problem_row(
    repository, record, issue="none", cls="process-remark", weight="Minor", cost="nothing"
) -> str:
    return (
        f"| {repository} | {record} | author · reviewer | a lapse | {cls} | {weight} | {cost} "
        f"| {issue} |"
    )


def record(
    pin_line=f"- Process pin: `{PIN}`", remarks="- Process remarks on the-way: none", extra=""
):
    """A cycle record in the form of task-cycle/record_template.md."""
    return (
        f"# Cycle record — a task\n\n- Task source: the task document\n"
        f"- Product repository: product\n{pin_line}\n"
        f"- Target branch and base: `main`, `{BASE}`\n- Task branch: task/a\n"
        f"- Status: request open\n\n## Events\n\n| Time | Stage |\n|---|---|\n{extra}\n"
        f"## Request handoff\n\n- Request URL and status: draft\n{remarks}\n"
    )


def split_row(line: str) -> list[str]:
    """The cells of a table row as a GFM reader splits it: a backslash escapes the character
    after it, and every other bar ends a cell."""
    cells, current, escaped = [], [], False
    for char in line.strip():
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            current.append(char)
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    return cells[1:]


class Repository:
    """A git repository whose commits are built from snapshots, without a working tree."""

    def __init__(self, root: Path):
        self.root = root
        root.mkdir(parents=True, exist_ok=True)
        self.git("init", "-q", "-b", "main")
        self.time = 1_760_000_000

    def git(self, *args, data: bytes | None = None) -> str:
        done = subprocess.run(
            ["git", "-C", str(self.root), *args],
            input=data,
            capture_output=True,
            env=self.env(),
            check=True,
        )
        return done.stdout.decode("utf-8").strip()

    def env(self):
        when = f"{getattr(self, 'time', 1_760_000_000)} +0000"
        return dict(GIT_ENV, GIT_AUTHOR_DATE=when, GIT_COMMITTER_DATE=when)

    def blob(self, data: bytes) -> str:
        return self.git("hash-object", "-w", "--stdin", data=data)

    def tree(self, files: dict) -> str:
        """`files` maps a path to its text, bytes, or (mode, bytes) for a symbolic link."""
        here: dict[bytes, tuple[bytes, str, str]] = {}
        nested: dict[str, dict] = {}
        for path, content in files.items():
            head, _, rest = path.partition("/")
            if rest:
                nested.setdefault(head, {})[rest] = content
                continue
            mode = "100644"
            if isinstance(content, tuple):
                mode, content = content
            data = content.encode("utf-8") if isinstance(content, str) else content
            here[head.encode("utf-8")] = (mode.encode(), "blob", self.blob(data))
        for name, inner in nested.items():
            here[name.encode("utf-8")] = (b"040000", "tree", self.tree(inner))
        listing = b"".join(
            mode + b" " + kind.encode() + b" " + sha.encode() + b"\t" + name + b"\0"
            for name, (mode, kind, sha) in sorted(here.items())
        )
        return self.git("mktree", "-z", data=listing)

    def commit(self, files: dict, message: str, *parents: str) -> str:
        self.time += 3600
        arguments = ["commit-tree", self.tree(files), "-m", message]
        for parent in parents:
            arguments += ["-p", parent]
        return self.git(*arguments)

    def commit_dated(self, files: dict, parent: str, stamp: str) -> str:
        """A commit whose author and committer lines carry `stamp` as it is, written as a raw
        object, so that a date git's own commands would refuse can stand in the history."""
        person = f"Tester <tester@example.com> {stamp} +0000"
        text = f"tree {self.tree(files)}\nparent {parent}\nauthor {person}\ncommitter {person}\n\nRaw\n"
        return self.git(
            "hash-object", "-t", "commit", "-w", "--literally", "--stdin", data=text.encode("utf-8")
        )

    def branch(self, name: str, commit: str) -> None:
        self.git("update-ref", f"refs/heads/{name}", commit)

    def cycle(
        self,
        folder: str,
        files: dict,
        base_files: dict | None = None,
        parent: str | None = None,
        branch: str | None = "main",
    ) -> tuple[str, str]:
        """A commit that adds the copy of a record under docs/task-cycles/<folder>/ and the next
        that removes it; returns both."""
        base_files = base_files or {"README.md": "a product\n"}
        if parent is None:
            parent = self.commit(base_files, "Start")
        copy = {
            **base_files,
            **{f"docs/task-cycles/{folder}/{name}": content for name, content in files.items()},
        }
        added = self.commit(copy, "Add the record", parent)
        removed = self.commit(base_files, "Remove the record", added)
        if branch:
            self.branch(branch, removed)
        return added, removed


class AuditCountCase(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.home = Path(self.temporary.name)
        self.results = self.home / "results"
        self.results.mkdir()
        self.register = self.home / "register.md"
        self.register.write_text(TEMPLATE, encoding="utf-8")
        self.locations = self.home / "locations.json"

    def tearDown(self):
        self.temporary.cleanup()

    def repository(self, name="product") -> Repository:
        return Repository(self.home / "repos" / name)

    def write_locations(self, data) -> None:
        text = data if isinstance(data, str) else json.dumps(data)
        self.locations.write_text(text, encoding="utf-8")

    def places(self, **repositories) -> dict:
        """A locations file's content: the-way's two places and each named repository."""
        data = {
            "the-way": {"problem_register": str(self.register), "audit_results": str(self.results)}
        }
        for key, repository in repositories.items():
            data.setdefault(key, {})["repository"] = str(repository.root)
        return data

    def run_count(self, *arguments, locations=True, timeout=None, env=None):
        """The command run as a process. `timeout` is no limit unless a test passes one, since
        only a test that asks whether the count stalls has the limit as its oracle."""
        command = [sys.executable, "-B", str(SCRIPT)]
        return self.run_command(command, arguments, locations, timeout, env)

    def run_count_of_the_copy(self, *arguments):
        """The command as the copy of it that the test of the checkout `checkout` builds, run as a
        process."""
        command = [
            sys.executable,
            "-B",
            str(self.home / "repos" / "checkout" / "process-audit" / "audit_count.py"),
        ]
        return self.run_command(command, arguments, True, None, None)

    def run_command(self, command, arguments, locations, timeout, env):
        if locations:
            command += ["--locations", str(self.locations)]
        try:
            return subprocess.run(
                command + list(arguments),
                capture_output=True,
                stdin=subprocess.DEVNULL,
                timeout=timeout,
                env=dict(os.environ, PYTHONIOENCODING="utf-8", **NO_USER_GIT_CONFIG, **(env or {})),
            )
        except subprocess.TimeoutExpired:
            self.fail(f"the command did not finish within {timeout} s")

    def latest(self) -> str:
        path = self.results / "count-latest.md"
        self.assertTrue(path.is_file(), "the command wrote no result")
        return path.read_bytes().decode("utf-8")

    def rows(self, heading: str) -> list[list[str]]:
        """The rows of the table under `## <heading>` of the latest result, as cells. Of *Unknown
        values* they are the values the table gives as examples, each as repository, record, value
        and reason: the whole list where no pair has more than three values, as the tests that read
        them have; the pairs are in `pair_rows`."""
        if heading == "Unknown values":
            return [
                self.example_row(example, pair[2])
                for pair in self.pair_rows()
                for example in pair[3].split("; ")
            ]
        text = self.latest()
        self.assertIn(f"\n## {heading}\n", text, f"the result has no section `## {heading}`")
        section = text.split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]
        lines = [line for line in section.splitlines() if line.startswith("|")]
        return [split_row(line) for line in lines[2:]]

    @staticmethod
    def example_row(example: str, why: str) -> list[str]:
        """An example of a pair, written `repository record: value`, as repository, record, value
        and reason."""
        repository, rest = example.split(" ", 1)
        record, value = rest.split(": ", 1)
        return [repository, record, value, why]

    def pair_rows(self) -> list[list[str]]:
        """The rows of *Unknown values*: one row for each field and reason, as field, number of
        values, reason and the first examples."""
        text = self.latest()
        self.assertIn(
            "\n## Unknown values\n", text, "the result has no section `## Unknown values`"
        )
        section = text.split("\n## Unknown values\n", 1)[1].split("\n## ", 1)[0]
        lines = [line for line in section.splitlines() if line.startswith("|")]
        return [split_row(line) for line in lines[2:]]

    def register_pair_rows(self) -> list[list[str]]:
        """The rows of *Unknown values* for the values of the register: the pairs whose field is a
        row or a table of it."""
        return [row for row in self.pair_rows() if row[0].startswith(("row of ", "table "))]

    def section(self, kind, number) -> list[list[str]]:
        """The rows of the table under `### <kind>, series <number>` of the latest result."""
        text = self.latest()
        heading = f"\n### {kind}, series {number}\n"
        self.assertIn(heading, text, "the result has no such series")
        part = text.split(heading, 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
        lines = [line for line in part.splitlines() if line.startswith("|")]
        return [split_row(line) for line in lines[2:]]

    def reasons_of(self, rows: list[list[str]], value: str) -> str:
        """The reasons of the rows of *Unknown values* that name `value`, joined: the rows are
        found by their value, since a cycle now has rows of its process questions too."""
        return " ".join(row[3] for row in rows if row[2] == value)

    def cycles(self) -> list[dict]:
        text = self.latest()
        section = text.split("\n## Cycles\n", 1)[1].split("\n## ", 1)[0]
        lines = [line for line in section.splitlines() if line.startswith("|")]
        header = [cell.strip() for cell in lines[0].strip("|").split("|")]
        return [dict(zip(header, row)) for row in self.rows("Cycles")]

    def own_cycle(self, files, changed=None, record_text=None, folder="a-task") -> tuple[str, str]:
        """A cycle of the-way whose copy of the record is in the-way's own history: the version
        the cycle ran on (a commit holding the four tools), a commit of the task branch that
        replaces the files of `changed`, and the commit that adds the copy, whose record names the
        version as its *Process pin* (each PIN of `record_text` is replaced by it). Writes the
        locations file; returns the commit that adds the copy and the version."""
        way = self.repository("the-way")
        base = {"README.md": "the-way\n", **{path: "version one\n" for path in TOOLS}}
        version = way.commit(base, "The version the cycle ran on")
        after = {**base, **(changed or {})}
        work = way.commit(after, "The task branch changes files", version)
        text = (record_text if record_text is not None else record()).replace(PIN, version)
        added, _ = way.cycle(folder, {"cycle.md": text, **files}, base_files=after, parent=work)
        self.write_locations(self.places(**{"the-way": way}))
        return added, version

    def fresh(self) -> None:
        """Start over with new places and an empty result, for the next case of a `subTest`."""
        self.tearDown()
        self.setUp()

    def run_with_prices(self, prices=None):
        """The command run with the test price list (`--prices`), which prices `model-a`."""
        test_prices = self.home / "prices.md"
        test_prices.write_text(TEST_PRICES if prices is None else prices, encoding="utf-8")
        return self.run_count("--prices", str(test_prices))


class CycleFound(AuditCountCase):
    def test_a_record_added_and_then_removed_gives_its_cycle_pin_and_remarks(self):
        product = self.repository()
        remarks = (
            "- Process remarks on the-way:\n"
            "  - author, docs/task-cycles/a-task/reports/author.md: the plan named a moved\n"
            "    file\n"
            "  - reviewer, docs/task-cycles/a-task/reports/review.md: the check was unclear\n"
            "    - a sub-item that belongs to the item above\n"
            "  - the orchestrator: a remark of its own\n"
        )
        added, _ = product.cycle("a-task", {"cycle.md": record(remarks=remarks)})
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        cycles = self.cycles()
        self.assertEqual(1, len(cycles), cycles)
        cycle = cycles[0]
        self.assertEqual("product", cycle["Repository"])
        self.assertEqual(added, cycle["Record"])
        self.assertEqual("a-task", cycle["Folder"])
        self.assertEqual(PIN, cycle["Process pin"])
        self.assertEqual("3", cycle["Remarks"])

    def test_a_record_reached_only_through_a_merge_is_found(self):
        # The merge's tree equals its first parent's, so a history simplified to one parent
        # would never reach the branch that added and removed the record.
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        main = product.commit({"README.md": "a product, changed\n"}, "Change", start)
        added, removed = product.cycle(
            "merged-task", {"cycle.md": record()}, parent=start, branch=None
        )
        merge = product.commit({"README.md": "a product, changed\n"}, "Merge", main, removed)
        product.branch("main", merge)
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([added], [cycle["Record"] for cycle in self.cycles()])

    def test_a_record_on_another_branch_is_found(self):
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        product.branch("main", start)
        added, _ = product.cycle(
            "open-task", {"cycle.md": record()}, parent=start, branch="task/open"
        )
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([added], [cycle["Record"] for cycle in self.cycles()])

    def test_a_cycle_committed_again_after_a_correction_counts_once(self):
        product = self.repository()
        first, removed = product.cycle("fixed-task", {"cycle.md": record()})
        corrected = record(
            remarks="- Process remarks on the-way:\n  - author: one\n  - reviewer: two\n"
        )
        again, _ = product.cycle("fixed-task", {"cycle.md": corrected}, parent=removed)
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        cycles = self.cycles()
        self.assertEqual(1, len(cycles), cycles)
        self.assertEqual(first, cycles[0]["Record"])
        self.assertEqual(again, cycles[0]["Later copies"])
        self.assertEqual("2", cycles[0]["Remarks"])

    def test_a_cycle_md_outside_a_record_folder_is_no_cycle(self):
        product = self.repository()
        product.cycle("deeper/inside", {"cycle.md": record()})
        start = product.commit(
            {
                "README.md": "a product\n",
                "docs/task-cycles/cycle.md": record(),
                "docs/other/some-task/cycle.md": record(),
            },
            "Stray records",
        )
        product.branch("stray", start)
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([], self.cycles())
        self.assertEqual([["product", "0", "yes"]], self.rows("Repositories"))


class ProcessPin(AuditCountCase):
    def pin_of(self, pin_line: str, key: str = "product") -> tuple[str, list[list[str]]]:
        repository = self.repository(key)
        repository.cycle("a-task", {"cycle.md": record(pin_line=pin_line)})
        self.write_locations(self.places(**{key: repository}))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        return self.cycles()[0]["Process pin"], self.rows("Unknown values")

    def test_a_moved_pin_gives_the_commit_it_moved_to(self):
        pin, _ = self.pin_of(
            "- Process pin: `1111111` at start; moved to `2222222abc` by the "
            "task branch's first\n  commit `3333333`"
        )
        self.assertEqual("2222222abc", pin)

    def test_a_cycle_of_the_way_itself_takes_the_commit_of_its_target_base(self):
        pin, _ = self.pin_of("- Process pin: not applicable (the-way itself)", key="the-way")
        self.assertEqual(BASE, pin)

    def test_a_product_pin_naming_no_commit_is_unknown(self):
        pin, unknown = self.pin_of("- Process pin: none — defaced")
        self.assertEqual("unknown", pin)
        self.assertEqual("Process pin", unknown[0][2])

    def test_a_doubled_pin_is_unknown(self):
        pin, unknown = self.pin_of(f"- Process pin: `{PIN}`\n- Process pin: `{BASE}`")
        self.assertEqual("unknown", pin)
        self.assertIn("more than once", unknown[0][3])

    def test_a_missing_pin_is_unknown(self):
        pin, unknown = self.pin_of("- Pin of the process: `1234567`")
        self.assertEqual("unknown", pin)
        self.assertIn("no line `Process pin`", unknown[0][3])

    def test_a_record_that_lacks_every_line_and_item_the_count_reads_is_of_an_earlier_form(self):
        # decision: WAY-344 "Where the command that counts the audit reads a cycle's record that lacks"
        # The record of a product with none of its items and no pin, and the record of a cycle of the
        # way itself with neither the pin nor the target line: no `Error:` line, exit code 0 (asserted
        # below), and for each line or item a reason that names it.
        product = self.repository("product")
        product.cycle("a-task", {"cycle.md": record(pin_line="", remarks="")})
        way = self.repository("the-way")
        bare = record(pin_line="", remarks="")
        target = f"- Target branch and base: `main`, `{BASE}`" + chr(10)
        self.assertIn(target, bare)
        way.cycle("own-task", {"cycle.md": bare.replace(target, "")})
        self.write_locations(self.places(**{"product": product, "the-way": way}))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn(b"Error:", done.stderr)
        reasons = {(row[0], row[2]) for row in self.pair_rows()}
        for field, words in (
            ("Process pin", "the record holds no line `Process pin`"),
            ("Process pin", "the line `Target branch and base` is missing"),
            ("Remarks", "the record holds no item `Process remarks on the-way`"),
            ("Discarded attempt", "the record holds no item `Discarded attempt`"),
            ("Plan", "the record holds no item `Plan`"),
            ("Slices returned too large", "the record holds no item `Slices returned too large`"),
        ):
            with self.subTest(field + ": " + words):
                self.assertTrue(any(f == field and words in why for f, why in reasons), reasons)

    def test_an_earlier_record_joining_the_pin_with_its_base_gives_the_commit(self):
        pin, _ = self.pin_of("- Process pin and target base: `main` at `1234567`")
        self.assertEqual("1234567", pin)

    def test_a_pin_in_a_later_section_is_not_the_header_line(self):
        pin, _ = self.pin_of("- Status: complete")
        self.assertEqual("unknown", pin)


class Remarks(AuditCountCase):
    def remarks_of(self, remarks: str, extra: str = "") -> tuple[str, list[list[str]]]:
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record(remarks=remarks, extra=extra)})
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        return self.cycles()[0]["Remarks"], self.rows("Unknown values")

    def test_none_gives_zero(self):
        self.assertEqual("0", self.remarks_of("- Process remarks on the-way: `none`.")[0])

    def test_remarks_written_on_the_line_are_unknown(self):
        count, unknown = self.remarks_of("- Process remarks on the-way: (1) a remark; (2) another")
        self.assertEqual("unknown", count)
        self.assertEqual("Remarks", unknown[0][2])

    def test_an_earlier_label_is_unknown_not_zero(self):
        count, unknown = self.remarks_of("- Process remarks: none")
        self.assertEqual("unknown", count)
        self.assertIn("earlier form", unknown[0][3])

    def test_a_doubled_item_is_unknown(self):
        count, _ = self.remarks_of(
            "- Process remarks on the-way:\n  - one\n- Process remarks on the-way:\n  - two\n"
        )
        self.assertEqual("unknown", count)

    def test_an_item_inside_fenced_code_is_not_read(self):
        fenced = "```\n- Process remarks on the-way:\n  - a quoted one\n```\n"
        self.assertEqual(
            "1", self.remarks_of("- Process remarks on the-way:\n  - one\n", extra=fenced)[0]
        )

    def test_the_corrections_item_before_the_remarks_item_is_not_among_its_entries(self):
        corrections = (
            "- Corrections after the request opened:\n"
            "  - correction 1, remarks `reports/correction-1-remarks.md`: remark · defect\n"
            "  - correction 2, remarks `reports/correction-2-remarks.md`: "
            "target-branch · none\n"
        )
        count, unknown = self.remarks_of(corrections + "- Process remarks on the-way:\n  - one\n")
        self.assertEqual("1", count)
        self.assertNotIn("Remarks", [row[2] for row in unknown])

    def test_items_after_the_remarks_item_are_not_its_entries(self):
        self.assertEqual(
            "0",
            self.remarks_of(
                "- Process remarks on the-way: none\n- Another item:\n  - its own sub-item\n"
            )[0],
        )


class Times(AuditCountCase):
    # The table of tokens by model of the older form, so that a file read for its times is no file
    # that lacks the section and the table (WAY-344).
    TABLE = (
        "\n| Model | Total tokens | Input | Cached input | Output |\n|---|---|---|---|---|\n"
        "| model-a | 110 | 100 | 0 | 10 |\n"
    )

    def times_of(self, stages) -> tuple[dict, list[list[str]]]:
        product = self.repository()
        files = {"cycle.md": record()}
        if stages is not None:
            files["stages.md"] = stages + self.TABLE
        product.cycle("a-task", files)
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        cycle = self.cycles()[0]
        # The record gives its pin and its remarks: no reading of `stages.md` makes them unknown.
        self.assertEqual([PIN, "0"], [cycle["Process pin"], cycle["Remarks"]])
        return cycle, self.rows("Unknown values")

    WORKING = "Working time without waiting for tools"

    def time_rows(self, unknown: list[list[str]]) -> list[list[str]]:
        """The rows of *Unknown values* about the two times; the cost rows are checked apart."""
        return [row for row in unknown if row[2] in (self.WORKING, "Waiting for tools")]

    def test_the_times_of_stages_md(self):
        cycle, unknown = self.times_of(
            "# Stages\n\n- Working time, orchestrator turns and subagent turns joined: 1:00:05\n"
            "- Waiting for tools: 0:10:05\n- Working time without waiting for tools: 0:50:00\n"
        )
        self.assertEqual("0:50:00", cycle[self.WORKING])
        self.assertEqual("0:10:05", cycle["Waiting for tools"])
        self.assertEqual([], self.time_rows(unknown))

    def test_an_earlier_form_without_the_wait_is_unknown_not_zero(self):
        cycle, unknown = self.times_of(
            "# Stages\n\n- Working time, orchestrator turns and subagent turns joined: 0:30:28\n"
        )
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertEqual(2, len(self.time_rows(unknown)))

    def test_a_wait_stages_md_gives_as_unknown_is_unknown(self):
        cycle, unknown = self.times_of(
            "- Waiting for tools: unknown — at least 0:01:00; 2 call(s) with no readable result\n"
            "- Working time without waiting for tools: unknown — at most 0:20:00\n"
        )
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertEqual(
            [
                "gives the working time without waiting for tools as unknown",
                "gives the waiting for tools as unknown",
            ],
            [row[3].split("` ", 1)[1] for row in self.time_rows(unknown)],
        )

    def test_a_doubled_or_malformed_line_is_unknown(self):
        cycle, unknown = self.times_of(
            "- Waiting for tools: 0:01:00\n- Waiting for tools: 0:02:00\n"
            "- Working time without waiting for tools: 1h 5m\n"
        )
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertEqual(
            ["Working time without waiting for tools", "Waiting for tools"],
            [row[2] for row in self.time_rows(unknown)],
        )

    def test_a_line_inside_a_malformed_table_or_fenced_code_is_not_read(self):
        cycle, _ = self.times_of(
            "| # | Stage |\n|---|\n| - Waiting for tools: 0:01:00 |\n"
            "```\n- Working time without waiting for tools: 0:05:00\n```\n"
        )
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])

    def test_a_missing_stages_md_is_unknown(self):
        cycle, unknown = self.times_of(None)
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertIn("no `stages.md`", self.reasons_of(unknown, "Waiting for tools"))

    # What the stage script writes into a copy, as the cost row and the times of the fix-round
    # stage report of Cost give them: 0.011250 dollars, one fix round, 28.9 % of the cost in it, and
    # the times of STAGES_HEADER. The other two files are given too, to show they are read as
    # before.
    def stage_files(self) -> dict:
        return {
            "stages.md": one_fix_round(),
            MEASURES: measures_file(),
            GATE: gate_file(rows=gate_row(STARTED, 0, "100.000", 0, "gate/a", "100.0")),
        }

    STAGE_VALUES = ["0.011250", "1", "28.9%"]
    STAGE_NAMES = (WORKING, "Waiting for tools", "Cost", "Fix rounds share")

    def own_values(self, changed) -> tuple[str, dict, list[list[str]]]:
        """The copy of an own cycle that changes the files of `changed`: its record, its row of the
        cycle table and the rows of *Unknown values*; the files of the other two groups are read."""
        added, _ = self.own_cycle(self.stage_files(), changed, fix_record())
        done = self.run_with_prices()
        self.assertEqual(0, done.returncode, done.stderr)
        [cost] = self.rows("Cost")
        self.assertEqual(["the-way", added], cost[:2])
        return added, self.cycles()[0], cost

    def test_a_changed_stage_script_gives_the_times_the_cost_and_the_share_unknown(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # The cycle changes `task-cycle/cycle_stages.py` between the version it ran on and its copy:
        # the figures that script wrote are unknown with the reason, and the number of fix rounds,
        # which the record gives, and the two other files stand as before.
        added, cycle, cost = self.own_values({STAGE_SCRIPT: "version two\n"})
        self.assertEqual(["unknown", "unknown"], [cycle[self.WORKING], cycle["Waiting for tools"]])
        self.assertEqual(["unknown", "1", "unknown"], [cost[3], cost[4], cost[5]])
        # The files of the other two groups are read as before.
        self.assertEqual(
            [["the-way", added, *[value for _, value in MEASURE_VALUES]]],
            self.rows("Mechanism measures"),
        )
        self.assertEqual(
            [["the-way", added, STARTED, "0", "100.000", "0", "gate/a 100.0 s"]],
            self.rows("Gate runs"),
        )
        unknown = self.rows("Unknown values")
        for name in self.STAGE_NAMES:
            reason = self.reasons_of(unknown, name)
            self.assertIn(CHANGED_WHY, reason, name)
            self.assertIn("`task-cycle/cycle_stages.py`", reason, name)
            self.assertEqual(1, [row[2] for row in unknown].count(name), name)

    def test_a_cycle_that_changed_none_of_the_stage_tools_gives_the_stage_values_as_before(self):
        # The cycle changes the other three tools and another file, which the stage script does not
        # write: the times and the cost are read as written.
        changed = {
            MEASURES_SCRIPT: "two\n",
            GATE_SCRIPT: "two\n",
            GATE_RUNNER: "two\n",
            "README.md": "two\n",
        }
        _, cycle, cost = self.own_values(changed)
        self.assertEqual(["0:20:00", "0:05:00"], [cycle[self.WORKING], cycle["Waiting for tools"]])
        self.assertEqual(self.STAGE_VALUES, [cost[3], cost[4], cost[5]])
        self.assertEqual(
            [],
            [
                name
                for name in self.STAGE_NAMES
                if self.reasons_of(self.rows("Unknown values"), name)
            ],
        )

    def test_a_cycle_of_a_product_is_not_put_in_doubt_by_a_change_of_a_tool(self):
        # A cycle of another repository holds no tool of the-way in its own change: the script of
        # the-way is not compared with its copy, so the cycle's values stand though the-way's
        # script differs between the pin and the commit of its copy.
        way = self.repository("the-way")
        version = way.commit({"README.md": "the-way\n", STAGE_SCRIPT: "one\n"}, "Version")
        way.commit({"README.md": "the-way\n", STAGE_SCRIPT: "two\n"}, "Later", version)
        product = self.repository()
        product.cycle(
            "a-task",
            {
                "cycle.md": record(pin_line=f"- Process pin: `{version}`"),
                "stages.md": one_fix_round(),
            },
            base_files={"README.md": "a product\n", STAGE_SCRIPT: "other\n"},
        )
        self.write_locations(self.places(**{"the-way": way, "product": product}))
        done = self.run_with_prices()
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = [row for row in self.rows("Cost") if row[0] == "product"]
        self.assertEqual("0.011250", row[3])
        self.assertNotIn(CHANGED_WHY, self.latest())


class CraftedInput(AuditCountCase):
    def test_control_characters_and_bars_stay_inside_one_cell_of_one_line(self):
        product = self.repository()
        product.cycle(
            "evil\x1b[31m|x\nname",
            {
                "cycle.md": record(
                    pin_line="- Process pin: \x1b[2J`zzz` \x07 none",
                    remarks="- Process remarks on the-way:\n  - \x1b]0;title\x07 a remark\n",
                )
            },
        )
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        cycles = self.cycles()
        self.assertEqual(1, len(cycles))
        self.assertEqual(9, len(self.rows("Cycles")[0]))
        self.assertIn("\\x1b", cycles[0]["Folder"])
        self.assertEqual("unknown", cycles[0]["Process pin"])
        self.assertEqual("1", cycles[0]["Remarks"])

    def test_crafted_text_of_a_register_value_reaches_its_pair_as_one_cut_line_with_no_bar(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        # A repository the register names with an escaped bar, a control character and more text
        # than the cut: its value is unknown, and its example is one cut line with no bar in it.
        crafted = "g\\|" + "h" * 300 + "\x07"
        self.register.write_text(
            register_text(problems=[problem_row(crafted, added)]), encoding="utf-8"
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        pairs = self.register_pair_rows()
        self.assertEqual(1, len(pairs), pairs)
        self.assertEqual(["row of `Problems`", "1"], pairs[0][:2])
        # The bar is written as `\x7c`, and the text is cut to 200 characters before the example.
        self.assertIn("\\x7c", pairs[0][3])
        self.assertNotIn("h" * 201, pairs[0][3])
        self.assertLess(len(pairs[0][3]), 400, pairs[0][3])
        self.assertIn(f"{added}: row 1 of `Problems`", pairs[0][3])

    # invariant: audit-count-refuses-record-links
    def test_a_symbolic_link_leaving_the_record_is_not_followed(self):
        outside = self.home / "outside.md"
        outside.write_text("- Waiting for tools: 0:01:00\n", encoding="utf-8")
        product = self.repository()
        product.cycle(
            "linked-task",
            {"cycle.md": record(), "stages.md": ("120000", b"../../../../outside.md")},
        )
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual("unknown", self.cycles()[0]["Waiting for tools"])
        self.assertIn(
            "no regular file", self.reasons_of(self.rows("Unknown values"), "Waiting for tools")
        )

    def test_a_record_not_in_utf8_gives_unknown_values(self):
        product = self.repository()
        product.cycle(
            "utf16-task",
            {
                "cycle.md": record().encode("utf-16"),
                "stages.md": b"- Waiting for tools: \xff0:01:00\n",
            },
        )
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        cycle = self.cycles()[0]
        self.assertEqual(
            ["unknown"] * 3, [cycle["Process pin"], cycle["Remarks"], cycle["Waiting for tools"]]
        )
        self.assertIn("not UTF-8", self.rows("Unknown values")[0][3])

    def test_a_file_too_large_is_not_read(self):
        product = self.repository()
        product.cycle(
            "large-task",
            {"cycle.md": record(), "stages.md": "- Waiting for tools: 0:01:00\n" + "x" * 4_200_000},
        )
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual("unknown", self.cycles()[0]["Waiting for tools"])
        self.assertIn(
            "larger than", self.reasons_of(self.rows("Unknown values"), "Waiting for tools")
        )

    def test_a_header_line_of_blanks_does_not_stall_the_count(self):
        # A header line `-`, a long run of blanks and no colon: a pattern that can split the run
        # between the marker's blanks and the label tries every split before it fails.
        product = self.repository()
        product.cycle(
            "blank-task",
            {"cycle.md": record(pin_line="- " + " " * 150_000 + "x\n" + f"- Process pin: `{PIN}`")},
        )
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count(timeout=60).returncode)
        self.assertEqual(PIN, self.cycles()[0]["Process pin"])

    def test_a_long_continuation_of_a_header_line_does_not_stall_the_count(self):
        product = self.repository()
        product.cycle(
            "long-task", {"cycle.md": record(pin_line="- Process pin: none" + "\n x" * 800_000)}
        )
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count(timeout=60).returncode)
        self.assertEqual("unknown", self.cycles()[0]["Process pin"])

    def test_a_backslash_before_a_bar_stays_inside_its_cell(self):
        product = self.repository()
        product.cycle("x\\|none\\|7777777\\|99\\|0:00:01\\|0:00:02", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        section = self.latest().split("\n## Cycles\n", 1)[1].split("\n## ", 1)[0]
        [row] = [line for line in section.splitlines() if line.startswith("| product ")]
        # Nine cells whether a reader honours backslash escapes or splits at every bar.
        self.assertEqual(9, len(split_row(row)), row)
        self.assertEqual(10, row.count("|"), row)
        cycle = self.cycles()[0]
        self.assertEqual(PIN, cycle["Process pin"])
        self.assertEqual("0", cycle["Remarks"])

    def test_a_commit_dated_beyond_the_readable_years_leaves_its_date_unknown(self):
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        added = product.commit_dated(
            {"README.md": "a product\n", "docs/task-cycles/far-task/cycle.md": record()},
            start,
            "99999999999999",
        )
        removed = product.commit({"README.md": "a product\n"}, "Remove the record", added)
        product.branch("main", removed)
        other = self.repository("other")
        other.cycle("plain-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product, other=other))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        cycles = {cycle["Repository"]: cycle for cycle in self.cycles()}
        self.assertEqual(added, cycles["product"]["Record"])
        self.assertEqual("unknown", cycles["product"]["Committed"])
        self.assertEqual(PIN, cycles["product"]["Process pin"])
        self.assertIn("other", cycles)
        self.assertIn(
            ["product", added, "Committed"], [row[:3] for row in self.rows("Unknown values")]
        )


class Locations(AuditCountCase):
    def assert_refused(self, done, *words):
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        error = done.stderr.decode("utf-8")
        self.assertTrue(error.startswith("Error: "), error)
        self.assertEqual(1, len(error.strip().splitlines()), error)
        for word in words:
            self.assertIn(word, error)
        self.assertEqual([], list(self.results.iterdir()))

    def product(self) -> Repository:
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        return product

    def test_a_missing_file(self):
        done = self.run_count()
        self.assert_refused(done, "does not exist", "--locations")
        # The error names the option, never the path: the path is the user's (WAY-320).
        self.assertNotIn(self.home.name, done.stderr.decode("utf-8"))

    def test_a_price_list_that_is_missing_or_wrong_is_named_by_its_option_not_its_path(self):
        self.write_locations(self.places(product=self.product()))
        prices = self.home / "prices.md"
        done = self.run_count("--prices", str(prices))
        self.assert_refused(done, "does not exist", "--prices")
        self.assertNotIn(self.home.name, done.stderr.decode("utf-8"))
        prices.write_text("# Prices\n\nno date here\n", encoding="utf-8")
        done = self.run_count("--prices", str(prices))
        self.assert_refused(done, "List date", "--prices")
        self.assertNotIn(self.home.name, done.stderr.decode("utf-8"))

    def test_a_price_list_table_without_a_write_column_is_refused_naming_the_option_and_the_column(
        self,
    ):
        # A table that lacks one of the two write columns ends the run with exit code 2, as one
        # that lacks *Input* does, and the error names the option and the column, never the path.
        self.write_locations(self.places(product=self.product()))
        prices = self.home / "prices.md"
        for label, column, other in (
            ("1 hour", "Cache write (1 hour)", "Cache write (5 minutes)"),
            ("5 minutes", "Cache write (5 minutes)", "Cache write (1 hour)"),
        ):
            with self.subTest(label):
                header = (
                    "| Model id in stages.md | Input | Cached input | Output | "
                    + other
                    + " |\n|---|---|---|---|---|\n| model-a | 2 | 1 | 10 | 3 |\n"
                )
                prices.write_text(
                    "# Prices\n\n- List date: 2026-01-01\n\n" + header, encoding="utf-8"
                )
                done = self.run_count("--prices", str(prices))
                self.assert_refused(done, "--prices", column)
                self.assertNotIn(other, done.stderr.decode("utf-8"))
                self.assertNotIn(self.home.name, done.stderr.decode("utf-8"))

    def test_a_file_that_is_not_json_or_no_object(self):
        self.write_locations('{"the-way": ')
        self.assert_refused(self.run_count(), "is not JSON")
        self.write_locations("[1, 2]")
        self.assert_refused(self.run_count(), "is not a JSON object")

    def test_a_number_too_long_to_read_is_not_json_and_no_traceback(self):
        # Python reads an integer of more than 4300 digits as no number at all.
        self.write_locations('{"the-way": {"x": ' + "1" * 5000 + "}}")
        self.assert_refused(self.run_count(), "is not JSON")

    def test_a_missing_key(self):
        product = self.product()
        self.write_locations({"product": {"repository": str(product.root)}})
        self.assert_refused(self.run_count(), "no key `the-way`")
        for entry in ("problem_register", "audit_results"):
            data = self.places(product=product)
            del data["the-way"][entry]
            self.write_locations(data)
            self.assert_refused(self.run_count(), f"no key `{entry}` under `the-way`")

    def test_a_path_that_does_not_exist(self):
        product = self.product()
        for entry in ("problem_register", "audit_results"):
            data = self.places(product=product)
            data["the-way"][entry] = str(self.home / "missing")
            self.write_locations(data)
            self.assert_refused(self.run_count(), f"`{entry}` under `the-way`", "no existing")
        data = self.places(product=product)
        data["product"]["repository"] = str(self.home / "missing")
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`repository` under `product`")

    def test_a_key_holding_a_value_of_a_wrong_type(self):
        product = self.product()
        data = self.places(product=product)
        data["product"]["repository"] = 42
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`repository` under `product`", "not a path")
        data = self.places(product=product)
        data["the-way"] = str(self.results)
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`the-way`", "not a JSON object")
        data = self.places(product=product)
        data["notes"] = ["tasks"]
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`notes`", "not a JSON object")

    def test_a_relative_path(self):
        data = self.places(product=self.product())
        data["product"]["repository"] = "repos/product"
        self.write_locations(data)
        self.assert_refused(self.run_count(), "not an absolute path")

    def test_a_key_written_twice(self):
        product = self.product()
        text = json.dumps(self.places(product=product))
        self.write_locations(text[:-1] + ', "product": {}}')
        self.assert_refused(self.run_count(), "`product` twice")

    def test_a_named_repository_the_file_lacks(self):
        self.write_locations(self.places(product=self.product()))
        self.assert_refused(self.run_count("--repository", "other"), "no key `other`")
        data = self.places(product=self.product())
        data["notes"] = {"tasks": str(self.home)}
        self.write_locations(data)
        self.assert_refused(
            self.run_count("--repository", "notes"), "no key `repository` under `notes`"
        )

    def test_the_way_with_no_repository_key_is_the_checkout_the_script_lies_in(self):
        # decision: WAY-344 "Where the locations file has no key `repository` under `the-way`"
        # The key `repository` under `the-way` is no missing field (WAY-344): the count takes
        # the checkout this script lies in, so a pin of a commit of that checkout is resolved there.
        own = (
            subprocess.run(
                ["git", "-C", str(HERE.parent), "rev-parse", "--verify", "HEAD"],
                capture_output=True,
                env=GIT_ENV,
                check=True,
            )
            .stdout.decode("utf-8")
            .strip()
        )
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record(pin_line=f"- Process pin: `{own}`")})
        self.register.write_text(
            register_text(
                issues=[issue_row("fixed-one", "fixed", own)],
                problems=[problem_row("product", added, "fixed-one")],
            ),
            encoding="utf-8",
        )
        self.write_locations(self.places(product=product))
        self.assertNotIn("repository", self.places(product=product)["the-way"])
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(b"", done.stderr)
        self.assertEqual(own, self.cycles()[0]["Process pin"])
        self.assertEqual(
            [], [row for row in self.rows("Unknown values") if row[2] == "Process pin"]
        )
        self.assertEqual("1", self.rows("Fixed issues")[0][2])

    def test_no_repository_to_read(self):
        self.write_locations(self.places())
        self.assert_refused(self.run_count(), "--repository")

    def test_a_result_directory_inside_a_repository_to_read(self):
        product = self.product()
        data = self.places(product=product)
        inner = product.root / "results"
        inner.mkdir()
        data["the-way"]["audit_results"] = str(inner)
        self.write_locations(data)
        done = self.run_count()
        self.assertEqual(2, done.returncode)
        self.assertIn("inside the repository `product`", done.stderr.decode("utf-8"))
        self.assertEqual([], list(inner.iterdir()))

    def test_a_result_directory_inside_the_way_not_read_in_the_run(self):
        # No repository holds the results, the-way's included, whether or not the run reads it.
        product = self.product()
        way = self.repository("the-way")
        way.branch("main", way.commit({"README.md": "the-way\n"}, "Start"))
        inner = way.root / "results"
        inner.mkdir()
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        data["the-way"]["audit_results"] = str(inner)
        self.write_locations(data)
        done = self.run_count("--repository", "product")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("inside the repository `the-way`", done.stderr.decode("utf-8"))
        self.assertEqual([], list(inner.iterdir()))


FULL_EVENTS = (
    "| Time | Stage | Actor and model | Handoff, skill and inputs "
    "| Output or full report | Short result and next step |\n"
    "|---|---|---|---|---|---|\n"
)
# Events as the archived records write a fix round: no path holds the word `report`.
ARCHIVED_EVENTS = (
    "| 10:00 | fix dispatch | orchestrator | findings | - | dispatched |\n"
    "| 10:20 | fix returned | author | - | reports/fix.md | done |\n"
    "| 10:30 | review of the fix | reviewer | - | reports/review-fix.md | PASS |\n"
)
TEST_PRICES = """# Test prices

- List date: 2026-01-01

## Test provider

| Model id in stages.md | Page name | Input | Cached input | Output | Cache write (5 minutes) | Cache write (1 hour) |
|---|---|---|---|---|---|---|
| model-a | Model A | 2 | 1 | 10 | 3 | 5 |
| model-b | Model B | 4 | 0.5 | 20 | 6 | 8 |
| model-x | Model X | 2 | 1 | 10 | — | — |
| model-y | Model Y | 2 | 1 | 10 | 3 | — |
"""
STAGES_HEADER = (
    "# Stages of the cycle run\n\n- Working time without waiting for tools: 0:20:00\n"
    "- Waiting for tools: 0:05:00\n\n"
    "## Stages: start, waiting for tools and tokens by model\n\n"
    "| # | Stage | Start | Waiting for tools | Model | Input | Cached input "
    "| Output |\n|---|---|---|---|---|---|---|---|\n"
)


STAGES_HEADER_NAMED = STAGES_HEADER.replace(
    "| Output |\n|---|---|---|---|---|---|---|---|\n",
    "| Output | Files named |\n|---|---|---|---|---|---|---|---|---|\n",
)


# The older form of the stage report: no section of stages, only the time lines and the table of
# tokens by model, which every form has.
TIME_LINES = "- Working time without waiting for tools: 0:20:00\n- Waiting for tools: 0:05:00\n"
OLDER_HEADER = "| Model | Total tokens | Input | Cached input | Output |\n|---|---|---|---|---|\n"


def older_row(model, input_, cached, output) -> str:
    return f"| {model} | {input_ + output} | {input_} | {cached} | {output} |\n"


def older_stages(*rows, header=OLDER_HEADER, times=TIME_LINES) -> str:
    """A stage report with no section of stages, as the stage reports before it are."""
    return "# Stages of the cycle run\n\n" + times + "\n" + header + "".join(rows)


def stage_row(number, name, model, input_, cached, output, files=None) -> str:
    """A row of the stages section; with `files`, the row of the form that names the files each
    turn was given."""
    named = "" if files is None else f" {files} |"
    return (
        f"| {number} | {name} | 2026-11-11 10:00:00 | 0:00:00 | {model} | {input_} | {cached} "
        f"| {output} |{named}\n"
    )


WRITE_COLUMNS = ["Cache write (5 minutes)", "Cache write (1 hour)"]
# The newest form of the section: the columns of the form that names files, then the two columns
# of the cache writes, in that order.
STAGES_HEADER_WRITES = STAGES_HEADER.replace(
    "| Output |\n|---|---|---|---|---|---|---|---|\n",
    "| Output | Files named | " + " | ".join(WRITE_COLUMNS) + " |\n" + "|---" * 11 + "|\n",
)


def write_row(number, name, model, input_, cached, output, write_5m, write_1h, files="") -> str:
    """A row of the section of the newest form, with the cache writes of each lifetime."""
    return (
        f"| {number} | {name} | 2026-11-11 10:00:00 | 0:00:00 | {model} | {input_} | {cached} "
        f"| {output} | {files} | {write_5m} | {write_1h} |\n"
    )


WHOLE = "reports/review_whole_findings.md"
SLICE = "reports/review_slice2_findings.md"
ONE_ROUND = (
    f"- Review rounds:\n  - findings `{WHOLE}`: the whole change, range `a1b2c3d..e4f5a6b`,"
    "\n    report `reports/review_whole.md`; fix `reports/fix.md`, its review "
    "`reports/review-fix.md`\n"
)


def fix_record(rounds=ONE_ROUND, events="") -> str:
    """A cycle record whose item `Review rounds` reads `rounds`."""
    text = record(remarks="- Process remarks on the-way: none\n").replace(
        "| Time | Stage |\n|---|---|\n", FULL_EVENTS + events
    )
    return text.replace("- Status: request open\n", "- Status: request open\n" + rounds)


def one_fix_round(
    header=STAGES_HEADER_NAMED,
    fix_files=f"reports/fix_handoff.md, {WHOLE}",
    review_files=f"{WHOLE}, reports/fix.md",
) -> str:
    """Stages of one round of the whole change: the review that found the findings, the fix,
    which ran on two models, and the review of the fix. With the earlier header, the rows have no
    cell of files."""
    named = header == STAGES_HEADER_NAMED

    def files(text):
        return text if named else None

    review = "Review whole change (general-purpose) — turn 1"
    author = "One author (general-purpose) — turn 2"
    reviewer = "Review whole change (general-purpose) — turn 2"
    return (
        header
        + stage_row(1, "orchestrator", "model-a", 1000, 0, 100, files(""))
        + stage_row(2, review, "model-a", 2000, 1000, 200, files("reports/review_handoff.md"))
        + stage_row(3, author, "model-b", 400, 100, 40, files(fix_files))
        + stage_row(3, author, "model-a", 100, 0, 10, files(fix_files))
        + stage_row(4, reviewer, "model-a", 300, 0, 30, files(review_files))
    )


class Cost(AuditCountCase):
    def count(self, stages, record_text=None, prices=TEST_PRICES):
        product = self.repository()
        files = {"cycle.md": record_text if record_text is not None else fix_record()}
        if stages is not None:
            files["stages.md"] = stages
        product.cycle("a-task", files)
        self.write_locations(self.places(product=product))
        test_prices = self.home / "prices.md"
        test_prices.write_text(prices, encoding="utf-8")
        return self.run_count("--prices", str(test_prices))

    def cost_row(self) -> list[str]:
        [row] = self.rows("Cost")
        return row

    def unknown_why(self, value: str) -> list[str]:
        return [row[3] for row in self.rows("Unknown values") if row[2] == value]

    def share_of(self, stages, record_text=None) -> tuple[list[str], list[str]]:
        """The cost row and the reasons the share is unknown."""
        done = self.count(stages, record_text)
        self.assertEqual(0, done.returncode, done.stderr)
        return self.cost_row(), self.unknown_why("Fix rounds share")

    def test_a_round_named_by_its_findings_file_gives_the_share_of_the_turns_that_name_it(self):
        # Worked by hand, in millionths of a dollar: stage 1 is 1000*2 + 100*10 = 3000; stage 2 is
        # 1000*2 + 1000*1 + 200*10 = 5000; stage 3 is 300*4 + 100*0.5 + 40*20 = 2050 on model-b
        # and 100*2 + 10*10 = 300 on model-a; stage 4 is 300*2 + 30*10 = 900. The total is 11250.
        # Stages 3 and 4 name the findings file: 3250 of 11250 is 28.89 %.
        row, why = self.share_of(one_fix_round())
        self.assertEqual(
            ["product", "2026-01-01", "0.011250", "1", "28.9%"],
            [row[0], row[2], row[3], row[4], row[5]],
        )
        self.assertEqual([], why)

    def test_the_stage_report_cycle_stages_writes_gives_the_share(self):
        # Transcripts in Claude Code's form, where the fix and the review of the fix are each a
        # resumed subagent whose message names the findings file. Worked by hand at model-a's
        # prices, which are 3 for a write of 5 minutes and 5 for one of 1 hour: the orchestrator,
        # whose response wrote 100 tokens for 5 minutes and 200 for 1 hour on top of its 1000 plain
        # input, 1000*2 + 100*3 + 200*5 + 100*10 = 4300; the author's first turn 3000 and its fix
        # 500*2 + 50*10 = 1500; the reviewer's first turn 2000*2 + 200*10 = 6000 and its review
        # of the fix 250*2 + 25*10 = 750. 2250 of 15550 is 14.47 %.
        def line(kind, clock, **fields):
            entry = {"type": kind, "timestamp": f"2026-11-11T{clock}.000Z"}
            entry.update(fields)
            return json.dumps(entry) + "\n"

        def told(clock, text, meta=False):
            fields = {"message": {"role": "user", "content": text}}
            if meta:
                fields["isMeta"] = True
            return line("user", clock, **fields)

        def answered(clock, ident, input_, output, write_5m=0, write_1h=0):
            return line(
                "assistant",
                clock,
                message={
                    "id": ident,
                    "model": "model-a",
                    "stop_reason": "end_turn",
                    "content": [{"type": "text"}],
                    "usage": {
                        "input_tokens": input_,
                        "cache_creation_input_tokens": write_5m + write_1h,
                        "cache_read_input_tokens": 0,
                        "output_tokens": output,
                        "cache_creation": {
                            "ephemeral_5m_input_tokens": write_5m,
                            "ephemeral_1h_input_tokens": write_1h,
                        },
                    },
                },
            )

        project = self.home / "claude" / "projects" / "p"
        agents = project / "sess" / "subagents"
        agents.mkdir(parents=True)
        (project / "sess.jsonl").write_text(
            told("09:00:00", "run the cycle")
            + answered("09:00:10", "o1", 1000, 100, write_5m=100, write_1h=200),
            "utf-8",
        )
        (agents / "agent-f.jsonl").write_text(
            told("09:01:00", "Implement; handoff .runs/task-cycles/t/reports/author_handoff.md")
            + answered("09:02:00", "f1", 1000, 100)
            + told("09:20:00", f"Fix the findings in {WHOLE} by reports/fix_handoff.md", True)
            + answered("09:21:00", "f2", 500, 50),
            "utf-8",
        )
        (agents / "agent-r.jsonl").write_text(
            told("09:10:00", "Review the change; handoff reports/review_handoff.md")
            + answered("09:11:00", "r1", 2000, 200)
            + told("09:30:00", f"Review the fix of the findings in {WHOLE}", True)
            + answered("09:31:00", "r2", 250, 25),
            "utf-8",
        )
        for name, description in (("f", "Author"), ("r", "Reviewer")):
            (agents / f"agent-{name}.meta.json").write_text(
                json.dumps({"agentType": "general-purpose", "description": description}), "utf-8"
            )
        output = self.home / "stages.md"
        written = subprocess.run(
            [
                sys.executable,
                "-B",
                str(HERE.parent / "task-cycle" / "cycle_stages.py"),
                "sess",
                "--claude-home",
                str(self.home / "claude"),
                "--codex-home",
                str(self.home / "codex"),
                "--output",
                str(output),
            ],
            capture_output=True,
            stdin=subprocess.DEVNULL,
        )
        self.assertEqual(0, written.returncode, written.stderr)
        row, why = self.share_of(output.read_text(encoding="utf-8"))
        self.assertEqual(["0.015550", "1", "14.5%"], row[3:6])
        self.assertEqual([], why)

    def test_the_same_record_with_an_earlier_form_of_stages_md_leaves_the_share_unknown(self):
        row, why = self.share_of(one_fix_round(header=STAGES_HEADER))
        self.assertEqual(["0.011250", "1", "unknown"], row[3:6])
        self.assertTrue(any("no column `Files named`" in reason for reason in why), why)

    def test_review_rounds_reading_none_gives_a_share_of_zero(self):
        stages = one_fix_round(
            fix_files="reports/author_handoff.md", review_files="reports/review_handoff.md"
        )
        row, why = self.share_of(stages, fix_record(rounds="- Review rounds: none\n"))
        self.assertEqual(["0.011250", "0", "0.0%"], row[3:6])
        self.assertEqual([], why)

    def test_a_turn_naming_the_findings_files_of_two_rounds_counts_once(self):
        # Every stage costs 1000*2 + 100*10 = 3000: 15000 in all. The fix names both findings
        # files, each review one of them: 9000 of 15000 is 60 %; counting the fix once per file
        # would give 80 %.
        stages = (
            STAGES_HEADER_NAMED
            + stage_row(1, "orchestrator", "model-a", 1000, 0, 100, "")
            + stage_row(2, "Fix (general-purpose)", "model-a", 1000, 0, 100, f"{WHOLE}, {SLICE}")
            + stage_row(3, "Review A (general-purpose)", "model-a", 1000, 0, 100, WHOLE)
            + stage_row(4, "Review B (general-purpose)", "model-a", 1000, 0, 100, SLICE)
            + stage_row(
                5, "Other (general-purpose)", "model-a", 1000, 0, 100, "reports/other_handoff.md"
            )
        )
        rounds = f"- Review rounds:\n  - findings `{WHOLE}`: one\n  - findings `{SLICE}`: two\n"
        row, _ = self.share_of(stages, fix_record(rounds=rounds))
        self.assertEqual(["0.015000", "2", "60.0%"], row[3:6])

    def test_rounds_written_in_prose_leave_the_share_unknown_not_zero(self):
        # The archived form: the fix is named, but by no findings file.
        record_text = fix_record(
            events=ARCHIVED_EVENTS,
            rounds="- Review rounds: one whole-change round, one fix and its "
            "review. Closed at 4327974.\n",
        )
        row, why = self.share_of(one_fix_round(), record_text)
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("names no findings file" in reason for reason in why), why)

    def test_a_findings_file_no_turn_names_leaves_the_share_unknown(self):
        stages = one_fix_round(
            fix_files="reports/fix_handoff.md", review_files="reports/review_fix_handoff.md"
        )
        row, why = self.share_of(stages)
        self.assertEqual(["1", "unknown"], row[4:6])
        self.assertTrue(any("named by 0 subagent turn(s)" in reason for reason in why), why)

    def test_a_findings_file_only_one_turn_names_leaves_the_share_unknown(self):
        # The fix was given its findings file only inside its handoff: the share would leave out
        # the fix itself.
        row, why = self.share_of(one_fix_round(fix_files="reports/fix_handoff.md"))
        self.assertEqual(["1", "unknown"], row[4:6])
        self.assertTrue(any("named by 1 subagent turn(s)" in reason for reason in why), why)

    def test_none_beside_a_turn_naming_a_findings_file_leaves_the_share_unknown(self):
        row, why = self.share_of(one_fix_round(), fix_record(rounds="- Review rounds: none\n"))
        self.assertEqual(["0", "unknown"], row[4:6])
        self.assertTrue(any("do not agree" in reason for reason in why), why)

    def test_a_findings_file_the_record_does_not_name_leaves_the_share_unknown(self):
        stages = one_fix_round(review_files=f"{WHOLE}, {SLICE}")
        row, why = self.share_of(stages)
        self.assertEqual(["1", "unknown"], row[4:6])
        self.assertTrue(any("do not agree" in reason for reason in why), why)

    def test_a_doubled_review_rounds_line_leaves_the_share_unknown(self):
        rounds = ONE_ROUND + f"- Review rounds:\n  - findings `{SLICE}`: another\n"
        row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("more than once" in reason for reason in why), why)

    def test_an_entry_of_review_rounds_without_its_findings_file_leaves_the_share_unknown(self):
        rounds = ONE_ROUND + "  - the return step: fix `reports/return_fix.md`\n"
        row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("names no findings file" in reason for reason in why), why)

    def test_a_review_that_passed_with_no_fix_is_no_fix_round_and_a_mark_changes_no_share(self):
        # decision: WAY-337 "The record's item *Review rounds* also takes a sub-item for a review"
        # The same stages as the first test of the share: one round, 3250 of 11250, 28.9 %. The
        # sub-items of reviews that passed add no round and no turn, and the mark of the round's
        # sub-item is no part of the findings file's path.
        passed = (
            "  - review `reports/review_return_step.md`, PASS: the return step\n"
            "  - review `reports/review_fix.md`, PASS: the fix\n"
        )
        marked = ONE_ROUND.replace(f"`{WHOLE}`:", f"`{WHOLE}`, contradiction yes:")
        for label, rounds in (
            ("reviews after the round", ONE_ROUND + passed),
            ("reviews before it", "- Review rounds:\n" + passed + ONE_ROUND.split("\n", 1)[1]),
            ("a mark on the round", marked),
        ):
            with self.subTest(label):
                row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
                self.assertEqual(["0.011250", "1", "28.9%"], row[3:6])
                self.assertEqual([], why)

    def test_reviews_that_passed_alone_say_the_cycle_had_no_fix_round(self):
        # decision: WAY-337 "The record's item *Review rounds* also takes a sub-item for a review"
        stages = one_fix_round(
            fix_files="reports/author_handoff.md", review_files="reports/review_handoff.md"
        )
        rounds = "- Review rounds:\n  - review `reports/review_whole.md`, PASS: the whole change\n"
        row, why = self.share_of(stages, fix_record(rounds=rounds))
        self.assertEqual(["0.011250", "0", "0.0%"], row[3:6])
        self.assertEqual([], why)

    def test_review_rounds_that_contradict_themselves_leave_the_share_unknown(self):
        cases = {
            "none beside sub-items": (
                "- Review rounds: none\n" + ONE_ROUND.split("\n", 1)[1],
                "beside its sub-items",
            ),
            "a findings file twice": (ONE_ROUND + f"  - findings `{WHOLE}`: again\n", "twice"),
        }
        for label, (rounds, words) in cases.items():
            with self.subTest(label):
                row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
                self.assertEqual(["unknown", "unknown"], row[4:6])
                self.assertTrue(any(words in reason for reason in why), why)

    def test_a_record_without_a_review_rounds_line_leaves_the_share_unknown(self):
        row, why = self.share_of(one_fix_round(), fix_record(rounds=""))
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("no item `Review rounds`" in reason for reason in why), why)

    def test_crafted_cells_of_files_leave_the_share_unknown_and_one_row_per_cycle(self):
        for files in (
            f"{WHOLE}, reports/../secret.md",
            f"{WHOLE}, reports/a..b.md",
            f"{WHOLE}, reports/x.md\x1b[2J",
            "reports/" + "a" * 200_000 + ".md",
            f"{WHOLE},, reports/.hidden.md",
        ):
            with self.subTest(files=files[:40]):
                row, why = self.share_of(one_fix_round(fix_files=files))
                self.assertEqual(["0.011250", "1", "unknown"], row[3:6])
                self.assertTrue(
                    any("not a list of files of `reports/`" in reason for reason in why), why
                )
                self.assertEqual(1, len(self.rows("Cost")))

    def test_findings_files_in_review_rounds_are_read_only_in_their_form(self):
        for path in (
            "reports/../x_findings.md",
            "reports/" + "f" * 200_000 + ".md",
            "reports/a|b.md",
        ):
            with self.subTest(path=path[:40]):
                rounds = f"- Review rounds:\n  - findings `{path}`: crafted\n"
                row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
                self.assertEqual(["unknown", "unknown"], row[4:6])
                self.assertTrue(any("names no findings file" in reason for reason in why), why)

    def test_a_stage_with_no_token_usage_leaves_the_cost_unknown(self):
        # cycle_stages.py writes the model mark `—` with zero counts for a stage it found no usage
        # for; where no row of the section is priced, that is not a cost of zero.
        stages = STAGES_HEADER + stage_row(1, "orchestrator", "—", 0, 0, 0)
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("no token usage" in why for why in self.unknown_why("Cost")))

    def test_an_orchestrator_stretch_with_no_token_usage_costs_nothing(self):
        # A stretch of the orchestrator's own work with time and no response: the subagent
        # stages are priced, so the cycle's cost is known.
        stages = one_fix_round() + stage_row(5, "orchestrator", "—", 0, 0, 0, "")
        row, _ = self.share_of(stages)
        self.assertEqual(["0.011250", "1", "28.9%"], row[3:6])
        self.assertEqual([], self.unknown_why("Cost"))

    def test_a_subagent_stage_with_no_token_usage_leaves_the_cost_unknown(self):
        stages = one_fix_round() + stage_row(5, "Idle (general-purpose)", "—", 0, 0, 0, "")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("Idle" in why for why in self.unknown_why("Cost")))

    def test_a_model_the_list_lacks_leaves_the_cost_and_the_share_unknown(self):
        stages = one_fix_round().replace("| model-b |", "| model-c |")
        self.assertEqual(0, self.count(stages).returncode)
        row = self.cost_row()
        self.assertEqual(["unknown", "unknown"], [row[3], row[5]])
        reasons = self.unknown_why("Cost")
        self.assertTrue(any("no price for model `model-c`" in why for why in reasons), reasons)

    def test_stages_md_without_the_section_is_priced_from_the_table_of_tokens_by_model(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        # Worked by hand in millionths of a dollar, at model-a 2 / 1 / 10 and model-b 4 / 0.5 / 20:
        # model-a is (3000 - 1000) * 2 + 1000 * 1 + 300 * 10 = 8000; model-b is (500 - 100) * 4
        # + 100 * 0.5 + 50 * 20 = 2650. The total is 10650.
        stages = older_stages(
            older_row("model-a", 3000, 1000, 300), older_row("model-b", 500, 100, 50)
        )
        done = self.count(stages)
        self.assertEqual(0, done.returncode, done.stderr)
        row = self.cost_row()
        self.assertEqual(["product", "2026-01-01", "0.010650"], [row[0], row[2], row[3]])
        self.assertEqual([], self.unknown_why("Cost"))

    def test_the_older_form_gives_no_share_and_says_why_but_its_rounds_are_read_from_the_record(
        self,
    ):
        stages = older_stages(older_row("model-a", 3000, 1000, 300))
        cases = (
            ("one round", ONE_ROUND, ["0.008000", "1", "unknown"]),
            ("none", "- Review rounds: none\n", ["0.008000", "0", "unknown"]),
            (
                "prose",
                "- Review rounds: one round, fixed and reviewed.\n",
                ["0.008000", "unknown", "unknown"],
            ),
        )
        for label, rounds, expected in cases:
            with self.subTest(label):
                row, why = self.share_of(stages, fix_record(rounds=rounds))
                self.assertEqual(expected, row[3:6])
                self.assertTrue(any("gives no turns" in reason for reason in why), why)

    def test_the_cost_of_the_section_is_read_as_before_where_both_forms_stand(self):
        # `cycle_stages.py` writes the table of tokens by model and the section: the heading names
        # the newer form, which is read as before, whatever the table holds.
        stages = one_fix_round().replace(
            "\n## Stages:",
            "\n" + OLDER_HEADER + older_row("model-a", 9_000_000, 0, 9_000_000) + "\n## Stages:",
        )
        row, why = self.share_of(stages)
        self.assertEqual(["0.011250", "1", "28.9%"], row[3:6])
        self.assertEqual([], why)

    def test_the_older_form_leaves_the_cost_unknown_where_a_row_cannot_be_priced(self):
        good = older_row("model-b", 100, 0, 10)
        cases = {
            "a model the list lacks": (
                good + older_row("model-c", 100, 0, 10),
                "no price for model `model-c`",
            ),
            "a model unknown": (
                good + older_row("unknown", 100, 0, 10),
                "names the model `unknown`",
            ),
            "a cached input above its input": (
                good + older_row("model-a", 100, 500, 10),
                "above its input",
            ),
            "a count that is no number": (
                good + "| model-a | 110 | many | 0 | 10 |\n",
                "token count",
            ),
            "a count of sixteen digits": (
                good + older_row("model-a", int("9" * 16), 0, 10),
                "token count",
            ),
            "a total that is no number": (
                good + "| model-a | lots | 100 | 0 | 10 |\n",
                "token count",
            ),
            "no row": ("", "no model row"),
        }
        for label, (rows, words) in cases.items():
            with self.subTest(label):
                done = self.count(older_stages(rows))
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertNotIn(b"Error:", done.stderr)
                row = self.cost_row()
                self.assertEqual(["unknown", "unknown"], [row[3], row[5]])
                self.assertTrue(
                    any(words in why for why in self.unknown_why("Cost")), self.unknown_why("Cost")
                )

    def test_a_table_of_tokens_by_model_written_twice_leaves_the_cost_unknown_with_no_error(self):
        once = older_stages(older_row("model-a", 3000, 1000, 300))
        done = self.count(once + "\n" + OLDER_HEADER + older_row("model-a", 1, 0, 1))
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn(b"Error:", done.stderr)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("more than once" in why for why in self.unknown_why("Cost")))

    def test_a_table_of_tokens_by_model_in_fenced_code_is_not_read(self):
        stages = (
            "# Stages of the cycle run\n\n"
            + TIME_LINES
            + "\n```\n"
            + OLDER_HEADER
            + older_row("model-a", 3000, 1000, 300)
            + "```\n"
        )
        done = self.count(stages)
        self.assertEqual(1, done.returncode, done.stderr)
        self.assertEqual("unknown", self.cost_row()[3])

    def test_a_table_of_tokens_by_model_in_another_order_or_with_another_column_is_refused(self):
        # Every column the cost needs is there, so no field is missing: the table is refused with
        # a reason, the cost is unknown and the run is not ended with an error.
        row = "| model-a | 3300 | 3000 | 1000 | 300 |\n"
        cases = {
            "swapped columns": (
                OLDER_HEADER.replace("| Input | Cached input |", "| Cached input | Input |"),
                row,
            ),
            "another column beside them": (
                OLDER_HEADER.replace("| Output |", "| Output | Note |").replace(
                    "|---|---|---|---|---|", "|---|---|---|---|---|---|"
                ),
                row[:-1] + " x |\n",
            ),
            "without the total": (
                OLDER_HEADER.replace(" Total tokens |", "").replace(
                    "|---|---|---|---|---|", "|---|---|---|---|"
                ),
                "| model-a | 3000 | 1000 | 300 |\n",
            ),
        }
        for label, (header, body) in cases.items():
            with self.subTest(label):
                done = self.count(older_stages(body, header=header))
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertNotIn(b"Error:", done.stderr)
                self.assertEqual("unknown", self.cost_row()[3])
                self.assertTrue(
                    any("not of the form" in why for why in self.unknown_why("Cost")),
                    self.unknown_why("Cost"),
                )

    def test_cached_input_above_input_leaves_the_cost_unknown(self):
        stages = one_fix_round().replace("| 2000 | 1000 | 200 |", "| 2000 | 5000 | 200 |")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("above its input" in why for why in self.unknown_why("Cost")))

    def test_a_token_count_of_sixteen_digits_leaves_the_cost_unknown(self):
        stages = one_fix_round().replace("| 400 |", "| " + "9" * 16 + " |")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("token count" in why for why in self.unknown_why("Cost")))

    def test_a_cost_at_the_command_limit_is_unknown_not_written_with_overrun_digits(self):
        # 1,200 rows of 999,999,999,999,999 input tokens at 999,999.999999 dollars per million come
        # to about 1.2 * 10^18 dollars, above the limit of 10^18.
        row = stage_row(1, "Stage of a large count", "model-b", 999999999999999, 0, 0)
        stages = STAGES_HEADER + row * 1200
        prices = TEST_PRICES.replace(
            "| model-b | Model B | 4 | 0.5 | 20 |",
            "| model-b | Model B | 999999.999999 | 0.5 | 20 |",
        )
        self.assertEqual(0, self.count(stages, prices=prices).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("limit" in why for why in self.unknown_why("Cost")))

    def test_a_price_list_naming_a_model_twice_refuses_the_run(self):
        doubled = TEST_PRICES + "| model-a | Model A again | 2 | 1 | 10 | 3 | 5 |\n"
        done = self.count(one_fix_round(), prices=doubled)
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("twice", done.stderr.decode("utf-8"))
        self.assertEqual([], list(self.results.iterdir()))

    def test_a_wrong_price_list_refuses_the_run_with_nothing_written(self):
        cases = {
            "a price cell that is no number": (
                TEST_PRICES.replace("| 4 | 0.5 | 20 |", "| 1e9 | 0.5 | 20 |"),
                "neither a number",
            ),
            "a write price that is no number": (
                TEST_PRICES.replace("| 6 | 8 |", "| 6 | free |"),
                "neither a number",
            ),
            "a doubled list date": (
                TEST_PRICES.replace(
                    "- List date: 2026-01-01\n",
                    "- List date: 2026-01-01\n- List date: 2026-02-01\n",
                ),
                "more than once",
            ),
            "a list date that is no date": (
                TEST_PRICES.replace("2026-01-01", "2026-02-30"),
                "no date",
            ),
            "a list larger than the cap": (TEST_PRICES + "x" * 4_200_000, "larger than"),
        }
        for label, (prices, words) in cases.items():
            with self.subTest(label):
                done = self.count(one_fix_round(), prices=prices)
                self.assertEqual(2, done.returncode, done.stdout + done.stderr)
                self.assertIn(words, done.stderr.decode("utf-8"))
                self.assertEqual([], list(self.results.iterdir()))

    def test_a_price_cell_written_as_a_dash_leaves_its_model_unpriced(self):
        prices = TEST_PRICES.replace("| 4 | 0.5 | 20 |", "| — | — | — |")
        done = self.count(one_fix_round(), prices=prices)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(
            any("no price for model `model-b`" in why for why in self.unknown_why("Cost"))
        )

    def test_a_stage_or_model_name_reaches_a_reason_short_and_inside_one_cell(self):
        cases = {
            "a crafted stage name": stage_row(
                5, "Idle\\|x\x1b[2J\\x7c" + "s" * 2_000_000, "—", 0, 0, 0, ""
            ),
            "a crafted model name": stage_row(
                5, "Odd (general-purpose)", "m\\|c\x07" + "m" * 2_000_000, 1, 0, 1, ""
            ),
        }
        for label, row in cases.items():
            with self.subTest(label):
                done = self.count(one_fix_round() + row)
                self.assertEqual(0, done.returncode, done.stderr)
                text = self.latest()
                self.assertLess(len(text), 100_000)
                self.assertEqual(
                    [], [char for char in text if not char.isprintable() and char != "\n"]
                )
                section = text.split("\n## Unknown values\n", 1)[1]
                cost_lines = [line for line in section.splitlines() if "| Cost |" in line]
                self.assertEqual(1, len(cost_lines), cost_lines)
                self.assertEqual(4, len(split_row(cost_lines[0])), cost_lines[0])
                self.assertEqual(5, cost_lines[0].count("|"), cost_lines[0])

    def test_a_section_of_stages_written_twice_leaves_the_cost_unknown(self):
        section = "## " + one_fix_round().split("\n## ", 1)[1]
        stages = one_fix_round() + "\n" + section
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("more than once" in why for why in self.unknown_why("Cost")))

    def test_a_stage_whose_usage_was_not_read_leaves_the_cost_unknown(self):
        # cycle_stages.py writes the model `unknown` for a stage whose transcript holds no usage.
        stages = one_fix_round() + stage_row(5, "orchestrator", "unknown", 0, 0, 0, "")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(
            any("not read" in why for why in self.unknown_why("Cost")), self.unknown_why("Cost")
        )

    def test_an_orchestrator_row_of_parallel_work_with_no_token_usage_costs_nothing(self):
        stages = one_fix_round() + stage_row(
            5,
            "orchestrator while in parallel: Fix (general-purpose), Review (general-purpose)",
            "—",
            0,
            0,
            0,
            "",
        )
        row, _ = self.share_of(stages)
        self.assertEqual(["0.011250", "1", "28.9%"], row[3:6])
        self.assertEqual([], self.unknown_why("Cost"))

    def test_a_subagent_turn_whose_message_was_not_read_leaves_the_share_unknown(self):
        # The turn may have served a fix round, so `none` is not ruled in, nor a share computed
        # without it.
        extra = stage_row(5, "Other (general-purpose)", "model-a", 100, 0, 10, "unknown")
        cases = {
            "under none": (
                one_fix_round(
                    fix_files="reports/fix_handoff.md", review_files="reports/review_handoff.md"
                )
                + extra,
                fix_record(rounds="- Review rounds: none\n"),
            ),
            "under a named round": (one_fix_round() + extra, fix_record()),
        }
        for label, (stages, record_text) in cases.items():
            with self.subTest(label):
                row, why = self.share_of(stages, record_text)
                self.assertEqual("unknown", row[5])
                self.assertTrue(any("could not be read" in reason for reason in why), why)

    def test_rows_of_one_turn_that_disagree_leave_the_share_unknown(self):
        for label, old, new in (
            (
                "in its files",
                f"| model-a | 100 | 0 | 10 | reports/fix_handoff.md, {WHOLE} |",
                "| model-a | 100 | 0 | 10 | reports/fix_handoff.md |",
            ),
            (
                "in its name",
                "| One author (general-purpose) — turn 2 | 2026-11-11 10:00:00 "
                "| 0:00:00 | model-a |",
                "| Another (general-purpose) | 2026-11-11 10:00:00 | 0:00:00 | model-a |",
            ),
        ):
            with self.subTest(label):
                stages = one_fix_round()
                self.assertEqual(1, stages.count(old), old)
                row, why = self.share_of(stages.replace(old, new))
                self.assertEqual("unknown", row[5])
                self.assertTrue(any("disagree" in reason for reason in why), why)

    def written_cost(self, *rows, prices=TEST_PRICES):
        """The run on a section of the newest form made of `rows`: its Cost cell and the reasons
        the cost is unknown. The run ends with exit code 0 and no `Error:` line."""
        done = self.count(STAGES_HEADER_WRITES + "".join(rows), prices=prices)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn(b"Error:", done.stderr)
        return self.cost_row()[3], self.unknown_why("Cost")

    def test_the_cache_writes_of_each_lifetime_are_priced_each_at_its_own_price(self):
        # Worked by hand in millionths of a dollar, at model-a 2 / 1 / 10 and writes of 3 for 5
        # minutes and 5 for 1 hour: of 10000 input tokens, 2000 are read and 3000 + 1000 written,
        # so 4000 are plain: 4000 * 2 + 2000 * 1 + 3000 * 3 + 1000 * 5 + 100 * 10 = 25000. Both
        # lifetimes at the 5-minute price would give 23000.
        cost, why = self.written_cost(
            write_row(1, "orchestrator", "model-a", 10000, 2000, 100, 3000, 1000)
        )
        self.assertEqual("0.025000", cost)
        self.assertEqual([], why)

    def test_the_writes_are_priced_at_the_prices_of_their_own_model(self):
        # model-b, 2000 in of which 500 are read and 200 + 300 written: 1000 plain * 4 + 500 * 0.5
        # + 200 * 6 + 300 * 8 + 10 * 20 = 4000 + 250 + 1200 + 2400 + 200 = 8050; model-a, 550 in
        # of which 100 + 50 are written: 400 plain * 2 + 100 * 3 + 50 * 5 + 20 * 10 = 1550.
        cost, why = self.written_cost(
            write_row(1, "orchestrator", "model-b", 2000, 500, 10, 200, 300),
            write_row(1, "orchestrator", "model-a", 550, 0, 20, 100, 50),
        )
        self.assertEqual("0.009600", cost)
        self.assertEqual([], why)

    def test_a_row_with_no_writes_in_the_newest_form_is_priced_as_before(self):
        # model-a: (3000 - 1000) * 2 + 1000 * 1 + 300 * 10 = 8000.
        cost, why = self.written_cost(
            write_row(1, "orchestrator", "model-a", 3000, 1000, 300, 0, 0)
        )
        self.assertEqual("0.008000", cost)
        self.assertEqual([], why)

    def test_a_codex_row_with_no_writes_is_priced_at_the_old_price_whatever_its_write_cells(self):
        # model-x has `—` in both write columns, as the OpenAI table of the list has: its row of
        # 0 and 0 is priced as a row with no writes: (5000 - 1000) * 2 + 1000 * 1 + 200 * 10 =
        # 11000.
        cost, why = self.written_cost(
            write_row(1, "orchestrator", "model-x", 5000, 1000, 200, 0, 0)
        )
        self.assertEqual("0.011000", cost)
        self.assertEqual([], why)

    def test_a_model_with_no_price_for_a_lifetime_is_unknown_where_its_row_holds_writes_of_it(self):
        # model-y has 3 for the writes of 5 minutes and `—` for those of 1 hour.
        for label, row in (
            (
                "the writes of 1 hour",
                write_row(1, "orchestrator", "model-y", 1000, 0, 100, 400, 100),
            ),
            (
                "only the writes of 1 hour",
                write_row(1, "orchestrator", "model-y", 1000, 0, 100, 0, 100),
            ),
            (
                "a write of one token of 1 hour",
                write_row(1, "orchestrator", "model-y", 1000, 0, 100, 0, 1),
            ),
        ):
            with self.subTest(label):
                cost, why = self.written_cost(row)
                self.assertEqual("unknown", cost)
                self.assertTrue(
                    any(
                        "no price of a cache write of 1 hour for model `model-y`" in reason
                        for reason in why
                    ),
                    why,
                )

    def test_a_model_with_no_price_for_a_lifetime_is_priced_where_its_row_holds_none_of_it(self):
        # model-y: 600 plain * 2 + 400 * 3 + 100 * 10 = 3400 with no writes of 1 hour.
        cost, why = self.written_cost(write_row(1, "orchestrator", "model-y", 1000, 0, 100, 400, 0))
        self.assertEqual("0.003400", cost)
        self.assertEqual([], why)

    def test_a_model_with_a_dash_in_both_write_columns_is_unknown_for_a_write_of_either(self):
        for label, row in (
            ("5 minutes", write_row(1, "orchestrator", "model-x", 1000, 0, 100, 1, 0)),
            ("1 hour", write_row(1, "orchestrator", "model-x", 1000, 0, 100, 0, 1)),
        ):
            with self.subTest(label):
                cost, why = self.written_cost(row)
                self.assertEqual("unknown", cost)
                self.assertTrue(
                    any(
                        f"no price of a cache write of {label} for model `model-x`" in reason
                        for reason in why
                    ),
                    why,
                )

    def test_a_row_whose_cached_input_and_writes_exceed_its_input_leaves_the_cost_unknown(self):
        # 600 read + 300 + 200 written is 1100, above 1000; each of them alone is below it.
        cost, why = self.written_cost(
            write_row(1, "orchestrator", "model-a", 1000, 600, 100, 300, 200)
        )
        self.assertEqual("unknown", cost)
        self.assertTrue(
            any("above its input" in reason and "orchestrator" in reason for reason in why), why
        )

    def test_the_writes_alone_above_the_input_leave_the_cost_unknown(self):
        cost, why = self.written_cost(
            write_row(1, "orchestrator", "model-a", 1000, 0, 100, 700, 301)
        )
        self.assertEqual("unknown", cost)
        self.assertTrue(any("above its input" in reason for reason in why), why)

    def test_a_row_whose_cached_input_and_writes_make_exactly_its_input_is_priced(self):
        # Nothing is plain: 500 * 1 + 300 * 3 + 200 * 5 = 2400.
        cost, why = self.written_cost(
            write_row(1, "orchestrator", "model-a", 1000, 500, 0, 300, 200)
        )
        self.assertEqual("0.002400", cost)
        self.assertEqual([], why)

    def test_a_write_count_that_is_no_number_leaves_the_cost_unknown_and_no_traceback(self):
        for label, cell in (
            ("words", "many"),
            ("sixteen digits", "9" * 16),
            ("negative", "-5"),
            ("empty", ""),
            ("a float", "1.5"),
        ):
            with self.subTest(label):
                done = self.count(
                    STAGES_HEADER_WRITES
                    + write_row(1, "orchestrator", "model-a", 1000, 0, 100, cell, 0)
                )
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertNotIn(b"Traceback", done.stderr)
                self.assertEqual("unknown", self.cost_row()[3])
                self.assertTrue(any("token count" in why for why in self.unknown_why("Cost")))

    def test_the_share_of_a_fix_round_counts_the_writes_of_its_turns(self):
        # Orchestrator: 1000 * 2 + 100 * 10 = 3000. The fix, with 1000 in and 300 of them written
        # for 5 minutes: 700 plain * 2 + 300 * 3 + 50 * 10 = 2800; its review, with 500 in and 400
        # of them written for 1 hour: 100 * 2 + 400 * 5 + 100 * 10 = 3200. The total is 9000; the
        # fix and its review, 6000 of it, are 66.7 %.
        stages = (
            STAGES_HEADER_WRITES
            + write_row(1, "orchestrator", "model-a", 1000, 0, 100, 0, 0)
            + write_row(
                2,
                "One author (general-purpose) — turn 2",
                "model-a",
                1000,
                0,
                50,
                300,
                0,
                f"reports/fix_handoff.md, {WHOLE}",
            )
            + write_row(
                3,
                "Review whole change (general-purpose) — turn 2",
                "model-a",
                500,
                0,
                100,
                0,
                400,
                WHOLE + ", reports/fix.md",
            )
        )
        row, why = self.share_of(stages)
        self.assertEqual(["0.009000", "1", "66.7%"], row[3:6])
        self.assertEqual([], why)


SECTION = "Stages: start, waiting for tools and tokens by model"
NEWER_COLUMNS = [
    "#",
    "Stage",
    "Start",
    "Waiting for tools",
    "Model",
    "Input",
    "Cached input",
    "Output",
]


class StagesForms(AuditCountCase):
    """The reading of `stages.md` by its form, and a field the form needs that the file lacks
    (WAY-344, as the settlement 6 of the task puts it for the count of the audit): the cost or the
    time that needs it is unknown, the result is written, and the run ends with exit code 1 and an
    `Error:` line that names the file and the field."""

    def count(self, stages, folder="a-task"):
        product = self.repository()
        product.cycle(folder, {"cycle.md": record(), "stages.md": stages})
        self.write_locations(self.places(product=product))
        test_prices = self.home / "prices.md"
        test_prices.write_text(TEST_PRICES, encoding="utf-8")
        return self.run_count("--prices", str(test_prices))

    def newer(self, columns=NEWER_COLUMNS, times=TIME_LINES, table=True, row=None) -> str:
        """The newer form: the table of tokens by model, then the section whose table has the
        columns given and the row `row` (one of eight cells where it is none)."""
        text = (
            "# Stages of the cycle run\n\n"
            + times
            + "\n"
            + OLDER_HEADER
            + older_row("model-a", 1000, 0, 100)
            + f"\n## {SECTION}\n\nTimes are UTC.\n"
        )
        if table:
            text += (
                "\n| "
                + " | ".join(columns)
                + " |\n|"
                + "---|" * len(columns)
                + "\n"
                + (row or stage_row(1, "orchestrator", "model-a", 1000, 0, 100))
            )
        return text

    def error_line(self, field, folder="a-task") -> str:
        return (
            f"Error: repository `product`: cycle `{folder}`: the file `stages.md` of the copy "
            f"lacks the field `{field}`"
        )

    def assert_missing(self, done, fields, cost_unknown=True) -> None:
        """Exit code 1, the result written, one `Error:` line for each field and no other, and
        the field named in a row of *Unknown values*."""
        self.assertEqual(1, done.returncode, done.stderr)
        errors = [
            line for line in done.stderr.decode("utf-8").splitlines() if line.startswith("Error:")
        ]
        self.assertEqual([self.error_line(field) for field in fields], errors)
        [row] = self.rows("Cost")
        self.assertEqual("unknown" if cost_unknown else "0.003000", row[3])
        reasons = [unknown[3] for unknown in self.rows("Unknown values")]
        for field in fields:
            self.assertTrue(any(field in reason for reason in reasons), (field, reasons))

    def test_a_column_of_the_newer_table_that_the_file_lacks_is_a_missing_field(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        for column in NEWER_COLUMNS:
            with self.subTest(column):
                columns = [name for name in NEWER_COLUMNS if name != column]
                done = self.count(self.newer(columns))
                self.assert_missing(
                    done, [f"column {column} of the table of the section {SECTION}"]
                )

    def test_a_column_that_stands_under_another_name_is_a_missing_field(self):
        columns = [("Begin" if name == "Start" else name) for name in NEWER_COLUMNS]
        done = self.count(self.newer(columns))
        self.assert_missing(done, [f"column Start of the table of the section {SECTION}"])

    def test_every_column_of_the_newer_table_that_is_lacking_is_named_once(self):
        columns = [name for name in NEWER_COLUMNS if name not in ("Stage", "Output")]
        done = self.count(self.newer(columns))
        self.assert_missing(
            done,
            [
                f"column Stage of the table of the section {SECTION}",
                f"column Output of the table of the section {SECTION}",
            ],
        )

    def test_a_heading_with_no_table_at_all_misses_the_table(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        done = self.count(self.newer(table=False))
        self.assert_missing(done, [f"table of the section {SECTION}"])

    def test_a_column_of_the_older_table_that_the_file_lacks_is_a_missing_field(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        for column in ("Input", "Cached input", "Output"):
            with self.subTest(column):
                names = ["Model", "Total tokens", "Input", "Cached input", "Output"]
                names.remove(column)
                header = "| " + " | ".join(names) + " |\n|" + "---|" * len(names) + "\n"
                done = self.count(older_stages("| model-a | 3300 | 3000 | 300 |\n", header=header))
                self.assert_missing(
                    done, [f"column {column} of the table with the first cell Model"]
                )

    def test_a_file_with_neither_the_section_nor_the_table_misses_both(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        for label, stages in (
            ("only times", "# Stages\n\n" + TIME_LINES),
            (
                "a table of another kind",
                "# Stages\n\n" + TIME_LINES + "\n| Name | Tokens |\n|---|---|\n| model-a | 100 |\n",
            ),
            ("an empty file", ""),
        ):
            with self.subTest(label):
                done = self.count(stages)
                self.assert_missing(done, [f"section {SECTION}", "table with the first cell Model"])

    def test_a_time_line_without_the_other_is_a_missing_field(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        cases = (
            (
                "the wait",
                "- Working time without waiting for tools: 0:20:00\n",
                "line Waiting for tools",
                "0:20:00",
            ),
            (
                "the working time",
                "- Waiting for tools: 0:05:00\n",
                "line Working time without waiting for tools",
                "0:05:00",
            ),
        )
        for label, times, field, known in cases:
            with self.subTest(label):
                done = self.count(older_stages(older_row("model-a", 1000, 0, 100), times=times))
                self.assert_missing(done, [field], cost_unknown=False)
                [cycle] = self.cycles()
                both = [cycle["Working time without waiting for tools"], cycle["Waiting for tools"]]
                self.assertEqual(sorted([known, "unknown"]), sorted(both))

    def test_neither_time_line_is_the_earlier_form_and_no_missing_field(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        done = self.count(
            older_stages(
                older_row("model-a", 1000, 0, 100),
                times="- Working time, orchestrator turns and subagent turns joined: 0:30:28\n",
            )
        )
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn(b"Error:", done.stderr)
        [cycle] = self.cycles()
        self.assertEqual(
            ["unknown", "unknown"],
            [cycle["Working time without waiting for tools"], cycle["Waiting for tools"]],
        )

    def test_the_column_files_named_is_never_a_missing_field(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        done = self.count(self.newer())
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn(b"Error:", done.stderr)
        self.assertEqual("0.003000", self.rows("Cost")[0][3])

    def test_a_table_with_neither_write_column_is_the_earlier_form_and_misses_nothing(self):
        # decision: WAY-344 "Where a stage report has neither of the two columns"
        # With and without the column *Files named*: the cost is the one the rows gave before the
        # write columns stood in the form, the run ends with exit code 0, and no `Error:` line and
        # no value unknown is added for the columns that were never there.
        named = NEWER_COLUMNS + ["Files named"]
        for label, columns, row in (
            ("without the files", NEWER_COLUMNS, None),
            ("with the files", named, stage_row(1, "orchestrator", "model-a", 1000, 0, 100, "")),
        ):
            with self.subTest(label):
                done = self.count(self.newer(columns, row=row))
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertNotIn(b"Error:", done.stderr)
                self.assertEqual("0.003000", self.rows("Cost")[0][3])
                self.assertEqual(
                    [],
                    [
                        unknown
                        for unknown in self.rows("Unknown values")
                        if "Cache write" in unknown[3]
                    ],
                )

    def test_a_table_with_one_write_column_and_not_the_other_misses_the_other(self):
        # decision: WAY-344 "Where a stage report has neither of the two columns"
        # The cost is unknown with the reason, the result is written, the run ends with exit code 1
        # and one `Error:` line names `stages.md` and the column that is missing.
        named = NEWER_COLUMNS + ["Files named"]
        first, second = WRITE_COLUMNS
        for label, columns, absent in (
            ("the 5 minutes alone", named + [first], second),
            ("the 1 hour alone", named + [second], first),
        ):
            with self.subTest(label):
                row = stage_row(1, "orchestrator", "model-a", 1000, 0, 100, "")[:-1] + " 0 |\n"
                done = self.count(self.newer(columns, row=row))
                field = f"column {absent} of the table of the section {SECTION}"
                self.assert_missing(done, [field])

    def test_one_write_column_is_missing_whatever_else_stands_in_the_header(self):
        # decision: WAY-344 "Where a stage report has neither of the two columns"
        first, second = WRITE_COLUMNS
        for label, columns, absent in (
            ("with no files named", NEWER_COLUMNS + [first], second),
            ("before the files named", NEWER_COLUMNS + [second, "Files named"], first),
        ):
            with self.subTest(label):
                done = self.count(self.newer(columns))
                field = f"column {absent} of the table of the section {SECTION}"
                self.assert_missing(done, [field])

    def test_the_two_write_columns_without_the_files_or_in_another_order_are_refused(self):
        # Every column the cost needs is there and both write columns stand, so no field is
        # missing: the header is of no form the stage report gives, and the cost is unknown.
        first, second = WRITE_COLUMNS
        named = NEWER_COLUMNS + ["Files named"]
        for label, columns in (
            ("no files", NEWER_COLUMNS + WRITE_COLUMNS),
            ("the writes swapped", named + [second, first]),
            ("a column after them", named + WRITE_COLUMNS + ["Note"]),
        ):
            with self.subTest(label):
                done = self.count(self.newer(columns))
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertNotIn(b"Error:", done.stderr)
                self.assertEqual("unknown", self.rows("Cost")[0][3])
                self.assertTrue(
                    any("not of the form" in row[3] for row in self.rows("Unknown values"))
                )

    def test_a_table_with_both_write_columns_is_priced_at_the_prices_of_both_lifetimes(self):
        # model-a: 600 plain * 2 + 300 * 3 + 100 * 5 + 100 * 10 = 3600.
        row = write_row(1, "orchestrator", "model-a", 1000, 0, 100, 300, 100)
        done = self.count(self.newer(NEWER_COLUMNS + ["Files named"] + WRITE_COLUMNS, row=row))
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn(b"Error:", done.stderr)
        self.assertEqual("0.003600", self.rows("Cost")[0][3])

    def test_columns_in_another_order_or_with_another_column_miss_nothing_and_are_refused(self):
        swapped = [
            ("Cached input" if name == "Input" else "Input" if name == "Cached input" else name)
            for name in NEWER_COLUMNS
        ]
        for label, columns in (("swapped", swapped), ("a column beside", NEWER_COLUMNS + ["Note"])):
            with self.subTest(label):
                done = self.count(self.newer(columns))
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertNotIn(b"Error:", done.stderr)
                self.assertEqual("unknown", self.rows("Cost")[0][3])
                self.assertTrue(
                    any("not of the form" in row[3] for row in self.rows("Unknown values"))
                )

    def test_the_text_of_a_missing_field_error_is_cut_and_escaped(self):
        folder = "x|" + "y" * 300 + "\x1b[2J" + "z"
        done = self.count("# Stages\n", folder=folder)
        self.assertEqual(1, done.returncode, done.stderr)
        errors = [
            line for line in done.stderr.decode("utf-8").splitlines() if line.startswith("Error:")
        ]
        self.assertEqual(2, len(errors), errors)
        for line in errors:
            self.assertTrue(line.startswith("Error: repository `product`: cycle `x|yyy"), line)
            self.assertIn("the file `stages.md` of the copy lacks the field `", line)
            self.assertLess(len(line), 500)
            self.assertEqual([], [char for char in line if not char.isprintable()])
        self.assertEqual(
            [], [char for char in self.latest() if not char.isprintable() and char != "\n"]
        )

    def test_a_file_lacking_a_field_does_not_stop_the_count_of_the_other_cycles(self):
        product = self.repository()
        _, parent = product.cycle(
            "bad", {"cycle.md": record(), "stages.md": "# Stages\n"}, branch=None
        )
        product.cycle(
            "good", {"cycle.md": record(), "stages.md": self.newer()}, parent=parent, branch="main"
        )
        self.write_locations(self.places(product=product))
        test_prices = self.home / "prices.md"
        test_prices.write_text(TEST_PRICES, encoding="utf-8")
        done = self.run_count("--prices", str(test_prices))
        self.assertEqual(1, done.returncode, done.stderr)
        self.assertEqual(["0.003000", "unknown"], sorted(row[3] for row in self.rows("Cost")))
        errors = [
            line for line in done.stderr.decode("utf-8").splitlines() if line.startswith("Error:")
        ]
        self.assertEqual(2, len(errors), errors)
        self.assertTrue(all("cycle `bad`" in line for line in errors), errors)


MEASURES = "mechanism_measures.md"
GATE = "gate_times.md"
# The cycle-level lines of mechanism_measures.md, each with a value worked out by hand for the
# test; the labels are those task-cycle/cycle_measures.py writes.
MEASURE_VALUES = [
    ("Calls in all", "12"),
    ("Calls of the orchestrator", "5"),
    ("Calls of subagents", "7"),
    ("Mean context per call", "51000"),
    ("Mean context per call of the orchestrator", "62000"),
    ("Share of the context in calls above 200000 tokens", "12.5%"),
    ("Context of the orchestrator's first call", "20000"),
    ("Context of the orchestrator's middle call", "60000"),
    ("Context of the orchestrator's last call", "90000"),
    ("Cache written, 5 minutes", "3000"),
    ("Cache written, 1 hour", "0"),
    ("Cache written again by the orchestrator", "1500"),
    ("Calls of the orchestrator with a cache write again", "2"),
    ("Cache written again by subagents", "800"),
    ("Calls of subagents with a cache write again", "1"),
]
MEASURE_LABELS = [label for label, _ in MEASURE_VALUES]
GATE_HEADING = (
    "# Gate runs of the cycle\n\nEach row is one run by this script; times are seconds.\n\n"
)
GATE_TABLE = (
    "| Started (UTC) | Exit code | Total seconds | Other gate runs at the same time "
    "| Directory | Directory seconds |\n| --- | --- | --- | --- | --- | --- |\n"
)
STARTED = "2026-11-11 10:00:00.000"


def measures_file(values=MEASURE_VALUES) -> str:
    """mechanism_measures.md as task-cycle/cycle_measures.py writes it, with the cycle-level lines
    given and one row of the table of agents."""
    lines = "".join(f"- {label}: {value}\n" for label, value in values)
    return (
        "# Measures of the cycle run\n\n" + lines + "\n## Agents\n\n"
        "| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes "
        "| Cache written, 1 hour | Cache written again | Calls with a cache write again |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        "| orchestrator a1 | Claude Code | 5 | 20000 | 60000 | 90000 | 3000 | 0 | 1500 | 2 |\n"
    )


def gate_row(started, code, total, others, directory="—", seconds="—") -> str:
    return f"| {started} | {code} | {total} | {others} | {directory} | {seconds} |\n"


def gate_file(table=GATE_TABLE, rows="") -> str:
    """gate_times.md as task-cycle/gate_times.py writes it, with the table header given."""
    return GATE_HEADING + table + rows


class MeasuresCase(AuditCountCase):
    """The two files of a cycle's record the count reads: a copy holding
    neither is an earlier form, and a file lacking a field it needs is an error (WAY-344)."""

    def count(self, files, folder="a-task"):
        product = self.repository()
        added, _ = product.cycle(folder, {"cycle.md": record(), **files})
        self.write_locations(self.places(product=product))
        return self.run_count(), added

    def assert_missing(self, done, file, field, folder="a-task") -> None:
        """Exit code 1 and one `Error:` line naming the file and the field, the result written."""
        self.assertEqual(1, done.returncode, done.stderr)
        errors = [
            line for line in done.stderr.decode("utf-8").splitlines() if line.startswith("Error:")
        ]
        self.assertEqual(
            [
                f"Error: repository `product`: cycle `{folder}`: the file `{file}` of "
                f"the copy lacks the field `{field}`"
            ],
            errors,
        )
        self.latest()

    def unknown_rows(self, *values) -> list[list[str]]:
        """The rows of *Unknown values* whose value is one of `values` or starts with `Gate runs`."""
        return [
            row
            for row in self.rows("Unknown values")
            if row[2] in values or row[2].startswith("Gate runs")
        ]

    def own_files(self) -> dict:
        """The three files of a copy that the three groups of tools write, each with a value worked
        out by hand: the times 0:20:00 and 0:05:00 and the cost of 100 input and 10 output tokens of
        model-a, 100*2 + 10*10 = 300 millionths of a dollar; the values of MEASURE_VALUES; one run
        of 100.000 seconds with the directory gate/a."""
        return {
            "stages.md": older_stages(older_row("model-a", 100, 0, 10)),
            MEASURES: measures_file(),
            GATE: gate_file(rows=gate_row(STARTED, 0, "100.000", 0, "gate/a", "100.0")),
        }

    def own_run(self, changed, files=None) -> str:
        """The command run on an own cycle that changes the files of `changed`: ends with exit
        code 0 and no `Error:` line; returns the commit of its record."""
        added, _ = self.own_cycle(self.own_files() if files is None else files, changed)
        done = self.run_with_prices()
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn("Error:", done.stderr.decode("utf-8"))
        return added

    def assert_stage_values_stand(self, added) -> None:
        """What the stage script writes, as worked out in `own_files`."""
        self.assertEqual(
            ["0:20:00", "0:05:00"],
            [
                self.cycles()[0]["Working time without waiting for tools"],
                self.cycles()[0]["Waiting for tools"],
            ],
        )
        self.assertEqual("0.000300", self.rows("Cost")[0][3])

    def assert_measures_stand(self, added) -> None:
        self.assertEqual(
            [["the-way", added, *[value for _, value in MEASURE_VALUES]]],
            self.rows("Mechanism measures"),
        )

    def assert_runs_stand(self, added) -> None:
        self.assertEqual(
            [["the-way", added, STARTED, "0", "100.000", "0", "gate/a 100.0 s"]],
            self.rows("Gate runs"),
        )


class MechanismMeasures(MeasuresCase):
    def test_both_files_give_the_values_and_the_runs_of_the_cycle_worked_out_by_hand(self):
        runs = (
            gate_row(STARTED, 0, "100.000", 0, "gate/b", "59.9")
            + gate_row(STARTED, 0, "100.000", 0, "gate/a", "40.1")
            + gate_row("2026-11-11 11:00:00.000", 1, "20.000", 2)
        )
        done, added = self.count({MEASURES: measures_file(), GATE: gate_file(rows=runs)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", added, *[value for _, value in MEASURE_VALUES]]],
            self.rows("Mechanism measures"),
        )
        self.assertEqual(
            [
                ["product", added, STARTED, "0", "100.000", "0", "gate/b 59.9 s · gate/a 40.1 s"],
                ["product", added, "2026-11-11 11:00:00.000", "1", "20.000", "2", "—"],
            ],
            self.rows("Gate runs"),
        )

    def test_a_copy_without_the_files_gives_unknown_values_with_their_reasons_and_no_error(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn("Error:", done.stderr.decode("utf-8"))
        self.assertEqual(
            [["product", added, *["unknown"] * len(MEASURE_LABELS)]],
            self.rows("Mechanism measures"),
        )
        self.assertEqual([], self.rows("Gate runs"))
        self.assertIn(
            [
                "product",
                added,
                "Mechanism measures",
                "the copy holds no `mechanism_measures.md`: an earlier cycle, or a script that "
                "failed (the record's *Verification* says which)",
            ],
            self.rows("Unknown values"),
        )
        # Where no gate ran on the cycle's own system, the final gate ran in CI and `gate_times.md`
        # is not written (WAY-160): the reason names that cause as the task's row 6 gives.
        self.assertIn(
            [
                "product",
                added,
                "Gate runs",
                "the copy holds no `gate_times.md`: an earlier cycle, a final gate that ran "
                "in CI, or a script that failed (the record's *Verification* says which)",
            ],
            self.rows("Unknown values"),
        )

    def test_the_last_copy_is_read_where_a_later_copy_differs(self):
        product = self.repository()
        first, removed = product.cycle(
            "a-task",
            {
                "cycle.md": record(),
                MEASURES: measures_file(),
                GATE: gate_file(rows=gate_row(STARTED, 0, "1.000", 0)),
            },
        )
        later = [("Calls in all", "99"), *MEASURE_VALUES[1:]]
        again, _ = product.cycle(
            "a-task",
            {"cycle.md": record(), MEASURES: measures_file(later), GATE: gate_file()},
            parent=removed,
        )
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        # The record column names the first copy; the values are those of the last one.
        self.assertEqual(
            [["product", first, *[value for _, value in later]]], self.rows("Mechanism measures")
        )
        self.assertEqual(again, self.cycles()[0]["Later copies"])
        self.assertEqual([], self.rows("Gate runs"))

    def test_a_measures_file_without_a_label_gives_every_value_unknown_and_exits_one(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        values = [pair for pair in MEASURE_VALUES if pair[0] != "Calls of subagents"]
        done, added = self.count({MEASURES: measures_file(values)})
        self.assert_missing(done, MEASURES, "Calls of subagents")
        self.assertEqual(
            [["product", added, *["unknown"] * len(MEASURE_LABELS)]],
            self.rows("Mechanism measures"),
        )
        self.assertIn(
            [
                "product",
                added,
                "Calls of subagents",
                "the file `mechanism_measures.md` of the copy lacks the field `Calls of subagents`",
            ],
            self.rows("Unknown values"),
        )

    def test_a_doubled_label_and_malformed_values_are_unknown_with_no_error(self):
        changed = dict(MEASURE_VALUES)
        changed["Mean context per call"] = "5x"
        changed["Cache written, 1 hour"] = "unknown"
        changed["Share of the context in calls above 200000 tokens"] = "150.0%"
        done, added = self.count(
            {MEASURES: measures_file([("Calls in all", "13"), *changed.items()])}
        )
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn("Error:", done.stderr.decode("utf-8"))
        expected = {
            label: "unknown"
            for label in (
                "Calls in all",
                "Mean context per call",
                "Cache written, 1 hour",
                "Share of the context in calls above 200000 tokens",
            )
        }
        values = [expected.get(label, value) for label, value in MEASURE_VALUES]
        self.assertEqual([["product", added, *values]], self.rows("Mechanism measures"))
        reasons = {row[2]: row[3] for row in self.unknown_rows(*MEASURE_LABELS)}
        self.assertIn("more than once", reasons["Calls in all"])
        self.assertIn("not what its label gives", reasons["Mean context per call"])
        self.assertIn(
            "not what its label gives", reasons["Share of the context in calls above 200000 tokens"]
        )
        self.assertIn("as unknown", reasons["Cache written, 1 hour"])

    def test_crafted_values_break_no_cell_and_read_no_text_into_a_reason(self):
        changed = dict(MEASURE_VALUES)
        changed["Calls in all"] = "1|2\x1b[2J" + "9" * 300
        changed["Mean context per call"] = "x" * 5000
        done, _ = self.count({MEASURES: measures_file(list(changed.items()))})
        self.assertEqual(0, done.returncode, done.stderr)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        [row] = self.rows("Mechanism measures")
        self.assertEqual(2 + len(MEASURE_LABELS), len(row))
        self.assertEqual("unknown", row[2])
        self.assertEqual("unknown", row[5])
        self.assertNotIn("x" * 50, text)

    def test_a_changed_measures_script_gives_its_measures_unknown_and_the_rest_as_before(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        added = self.own_run({MEASURES_SCRIPT: "version two\n"})
        self.assertEqual(
            [["the-way", added, *["unknown"] * len(MEASURE_LABELS)]],
            self.rows("Mechanism measures"),
        )
        reason = self.reasons_of(self.rows("Unknown values"), "Mechanism measures")
        self.assertIn(CHANGED_WHY, reason)
        self.assertIn("`task-cycle/cycle_measures.py`", reason)
        self.assertEqual(
            1, [row[2] for row in self.rows("Unknown values")].count("Mechanism measures")
        )
        # What the other two scripts wrote is read as before.
        self.assert_stage_values_stand(added)
        self.assert_runs_stand(added)
        self.assertNotIn("Gate runs", [row[2] for row in self.rows("Unknown values")])

    def test_a_cycle_that_changed_none_of_the_measures_tools_gives_its_measures_as_before(self):
        # The cycle changes the other three tools, which write other files, and another file.
        added = self.own_run(
            {
                STAGE_SCRIPT: "two\n",
                GATE_SCRIPT: "two\n",
                GATE_RUNNER: "two\n",
                "README.md": "two\n",
            }
        )
        self.assert_measures_stand(added)
        self.assertEqual("", self.reasons_of(self.rows("Unknown values"), "Mechanism measures"))

    def test_a_field_missing_from_the_file_of_a_changed_tool_is_not_read_and_ends_no_run(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        # The values of that file are unknown for the change of the tool, so no field of it is read
        # as missing and the run ends with exit code 0.
        values = [pair for pair in MEASURE_VALUES if pair[0] != "Calls of subagents"]
        added = self.own_run(
            {MEASURES_SCRIPT: "version two\n"},
            {**self.own_files(), MEASURES: measures_file(values)},
        )
        self.assertEqual(
            [["the-way", added, *["unknown"] * len(MEASURE_LABELS)]],
            self.rows("Mechanism measures"),
        )
        self.assertIn(
            CHANGED_WHY, self.reasons_of(self.rows("Unknown values"), "Mechanism measures")
        )
        self.assertEqual("", self.reasons_of(self.rows("Unknown values"), "Calls of subagents"))

    def test_a_copy_of_an_earlier_cycle_holding_no_such_file_keeps_its_own_reason(self):
        # The cycle changed the script, but its copy holds no `mechanism_measures.md`: nothing was
        # written by the script, so the copy is of an earlier form and is not put in doubt.
        files = {name: text for name, text in self.own_files().items() if name != MEASURES}
        self.own_run({MEASURES_SCRIPT: "version two\n"}, files)
        reason = self.reasons_of(self.rows("Unknown values"), "Mechanism measures")
        self.assertIn("the copy holds no `mechanism_measures.md`: an earlier cycle", reason)
        self.assertNotIn(CHANGED_WHY, self.latest())


class GateRunsMeasures(MeasuresCase):
    def test_a_changed_tool_of_the_gate_gives_its_runs_unknown_and_the_rest_as_before(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # Either tool of the gate: the script that records the times, and the test runner whose
        # output gives the time of each directory.
        for path in (GATE_SCRIPT, GATE_RUNNER):
            with self.subTest(path):
                self.fresh()
                added = self.own_run({path: "version two\n"})
                self.assertEqual([], self.rows("Gate runs"))
                reason = self.reasons_of(self.rows("Unknown values"), "Gate runs")
                self.assertIn(CHANGED_WHY, reason)
                self.assertIn(f"`{path}`", reason)
                self.assertEqual(
                    1, [row[2] for row in self.rows("Unknown values")].count("Gate runs")
                )
                self.assert_stage_values_stand(added)
                self.assert_measures_stand(added)

    def test_a_cycle_that_changed_none_of_the_tools_of_the_gate_gives_its_runs_as_before(self):
        added = self.own_run(
            {STAGE_SCRIPT: "two\n", MEASURES_SCRIPT: "two\n", "README.md": "two\n"}
        )
        self.assert_runs_stand(added)
        self.assertEqual("", self.reasons_of(self.rows("Unknown values"), "Gate runs"))

    def test_changing_every_tool_gives_all_three_groups_unknown_with_their_own_reasons(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        added = self.own_run({path: "version two\n" for path in TOOLS})
        self.assertEqual([], self.rows("Gate runs"))
        self.assertEqual(
            [["the-way", added, *["unknown"] * len(MEASURE_LABELS)]],
            self.rows("Mechanism measures"),
        )
        self.assertEqual("unknown", self.cycles()[0]["Waiting for tools"])
        self.assertEqual("unknown", self.rows("Cost")[0][3])
        unknown = self.rows("Unknown values")
        for name, path in (
            ("Gate runs", GATE_SCRIPT),
            ("Mechanism measures", MEASURES_SCRIPT),
            ("Cost", STAGE_SCRIPT),
        ):
            reason = self.reasons_of(unknown, name)
            self.assertIn(CHANGED_WHY, reason, name)
            self.assertIn(f"`{path}`", reason, name)

    def test_a_cycle_of_the_way_whose_pin_does_not_resolve_is_not_put_in_doubt(self):
        # The version the cycle ran on is not in the-way's history, so no change of a tool can be
        # told: the values stand as the copy gives them, and the pin is unknown as before.
        way = self.repository("the-way")
        work = way.commit({"README.md": "the-way\n", **{path: "two\n" for path in TOOLS}}, "Task")
        added, _ = way.cycle(
            "a-task",
            {"cycle.md": record(), **self.own_files()},
            base_files={"README.md": "the-way\n"},
            parent=work,
        )
        self.write_locations(self.places(**{"the-way": way}))
        done = self.run_with_prices()
        self.assertEqual(0, done.returncode, done.stderr)
        self.assert_measures_stand(added)
        self.assert_runs_stand(added)
        self.assertNotIn(CHANGED_WHY, self.latest())

    def test_a_cycle_that_changed_no_tool_gives_the_values_of_all_three_groups_as_before(self):
        added = self.own_run({})
        self.assert_runs_stand(added)
        self.assert_measures_stand(added)
        self.assert_stage_values_stand(added)

    def test_a_cycle_corrected_after_the_tool_changed_is_judged_by_its_last_copy(self):
        # The first copy of the record is added before the tool is changed, the last one after it:
        # the change counts, since it lies between the version and the last copy.
        way = self.repository("the-way")
        base = {"README.md": "the-way\n", **{path: "version one\n" for path in TOOLS}}
        version = way.commit(base, "The version the cycle ran on")
        text = record().replace(PIN, version)
        _, removed = way.cycle(
            "a-task", {"cycle.md": text, **self.own_files()}, base_files=base, parent=version
        )
        changed = {**base, GATE_SCRIPT: "version two\n"}
        work = way.commit(changed, "The task branch changes the script", removed)
        way.cycle("a-task", {"cycle.md": text, **self.own_files()}, base_files=changed, parent=work)
        self.write_locations(self.places(**{"the-way": way}))
        done = self.run_with_prices()
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([], self.rows("Gate runs"))
        self.assertIn(CHANGED_WHY, self.reasons_of(self.rows("Unknown values"), "Gate runs"))
        self.assert_measures_stand(self.cycles()[0]["Record"])

    def test_a_gate_file_without_a_column_is_a_missing_field_and_exits_one(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        table = (
            "| Started (UTC) | Total seconds | Other gate runs at the same time | Directory "
            "| Directory seconds |\n| --- | --- | --- | --- | --- |\n"
        )
        done, _ = self.count({GATE: gate_file(table=table)})
        self.assert_missing(done, GATE, "column Exit code of the table")
        self.assertEqual([], self.rows("Gate runs"))

    def test_a_gate_file_without_a_table_is_a_missing_field_and_exits_one(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        done, _ = self.count({GATE: gate_file(table="")})
        self.assert_missing(done, GATE, "table of the runs")
        self.assertEqual([], self.rows("Gate runs"))

    def test_an_empty_gate_file_is_a_missing_field_and_not_an_empty_list_of_runs(self):
        # decision: WAY-344 "The rule binds a script that a change adds and, in a script"
        # An empty file holds no table: the absence of the table is named, never read as no run.
        done, _ = self.count({GATE: ""})
        self.assert_missing(done, GATE, "table of the runs")
        self.assertEqual([], self.rows("Gate runs"))

    def test_a_table_with_no_run_gives_no_rows_and_no_error(self):
        done, _ = self.count({GATE: gate_file()})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([], self.rows("Gate runs"))

    def test_a_row_of_the_wrong_number_of_cells_is_its_own_unknown_run(self):
        rows = (
            gate_row(STARTED, 0, "5.000", 0, "gate/a", "5.0")
            + "| 2026-11-11 12:00:00.000 | 0 | 5.000 | 0 | gate/a |\n"
        )
        done, added = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [
                ["product", added, STARTED, "0", "5.000", "0", "gate/a 5.0 s"],
                ["product", added, "unknown", "unknown", "unknown", "unknown", "unknown"],
            ],
            self.rows("Gate runs"),
        )
        self.assertIn(
            [
                "product",
                added,
                "Gate runs",
                "a row of the table in `gate_times.md` has 5 cells, not 6",
            ],
            self.rows("Unknown values"),
        )

    def test_an_unreadable_total_and_seconds_are_unknown_with_their_reasons(self):
        rows = gate_row("2026-11-11 13:00:00.000", 0, "12,5", 0, "gate/a", "one")
        done, added = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", added, "2026-11-11 13:00:00.000", "0", "unknown", "0", "gate/a unknown"]],
            self.rows("Gate runs"),
        )
        values = [row[2] for row in self.unknown_rows()]
        self.assertIn("Gate runs: Total seconds", values)
        self.assertIn("Gate runs: Directory seconds", values)

    def test_bars_and_control_characters_in_a_directory_stay_in_one_cell(self):
        rows = gate_row(STARTED, 0, "1.000", 0, "gate\\|x\x1b[2J\x07y", "1.0")
        done, _ = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        [row] = self.rows("Gate runs")
        self.assertEqual(7, len(row))
        self.assertIn("gate", row[6])

    def test_a_long_directory_name_is_cut(self):
        rows = gate_row(STARTED, 0, "1.000", 0, "d" * 500, "1.0")
        done, _ = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertNotIn("d" * 201, self.latest())
        self.assertIn("d" * 200, self.latest())

    def test_runs_beyond_the_limit_are_not_read_and_say_so(self):
        rows = "".join(
            gate_row(f"2026-11-11 10:00:00.{index:03}", 0, "1.000", 0, "gate/a", "1.0")
            for index in range(600)
        )
        done, _ = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(500, len(self.rows("Gate runs")))
        self.assertTrue(any("more than 500 runs" in row[3] for row in self.unknown_rows()))

    def test_a_flood_of_wrong_width_rows_after_a_valid_header_is_capped_too(self):
        # Every row of the wrong number of cells is a run of its own, and the limit counts it:
        # a crafted file of such rows costs bounded work and writes bounded rows.
        rows = "| a | b |\n" * 600
        done, _ = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(500, len(self.rows("Gate runs")))
        self.assertTrue(any("more than 500 runs" in row[3] for row in self.unknown_rows()))

    def test_an_exit_code_above_255_is_read_as_written(self):
        # A gate that crashes on Windows ends with a code such as 0xC000013A, as an unsigned number.
        rows = gate_row(STARTED, 3221225786, "5.000", 0, "gate/a", "5.0")
        done, added = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", added, STARTED, "3221225786", "5.000", "0", "gate/a 5.0 s"]],
            self.rows("Gate runs"),
        )
        self.assertEqual([], [row for row in self.unknown_rows() if "Exit code" in row[2]])

    def test_an_exit_code_that_is_not_a_whole_number_is_unknown(self):
        rows = gate_row(STARTED, "-1", "5.000", 0, "gate/a", "5.0")
        done, added = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", added, STARTED, "unknown", "5.000", "0", "gate/a 5.0 s"]],
            self.rows("Gate runs"),
        )
        self.assertIn(
            "an exit code is not a whole number",
            self.reasons_of(self.rows("Unknown values"), "Gate runs: Exit code"),
        )

    def test_a_row_after_a_line_that_ends_the_table_is_not_read_and_says_so(self):
        rows = (
            gate_row(STARTED, 0, "5.000", 0, "gate/a", "5.0")
            + "\n"
            + gate_row("2026-11-11 11:00:00.000", 0, "6.000", 0, "gate/b", "6.0")
        )
        done, added = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", added, STARTED, "0", "5.000", "0", "gate/a 5.0 s"]], self.rows("Gate runs")
        )
        self.assertIn(
            [
                "product",
                added,
                "Gate runs",
                "`gate_times.md` holds a row after a line that is not a row of the table: "
                "the rows after it are not read",
            ],
            self.rows("Unknown values"),
        )

    def test_text_after_the_table_with_no_row_in_it_says_nothing(self):
        rows = gate_row(STARTED, 0, "5.000", 0, "gate/a", "5.0") + "\nA closing note.\n"
        done, _ = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(1, len(self.rows("Gate runs")))
        self.assertEqual([], self.unknown_rows())

    def test_a_git_failure_on_the_gate_file_leaves_the_files_that_were_read(self):
        sys.path.insert(0, str(HERE))
        import audit_count

        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record(), GATE: gate_file()})
        gate_blob = product.git("rev-parse", f"{added}:docs/task-cycles/a-task/{GATE}")

        class Failing(audit_count.Git):
            def run(self, *arguments):
                if arguments[:2] == ("cat-file", "blob") and arguments[2] == gate_blob:
                    raise audit_count.GitError("git cat-file failed (128): made up")
                return super().run(*arguments)

        cycle = audit_count.Cycle("product", "a-task", added, added)
        audit_count.fill(
            cycle,
            Failing(product.root),
            added,
            b"a-task",
            True,
            audit_count.Prices("2026-11-11", {}),
        )
        reasons = dict(cycle.unknown)
        self.assertIn("git could not read the copy", reasons["Gate runs"])
        # The record was read: its remarks are counted and no reason about git stands for them.
        self.assertEqual(0, cycle.remarks)
        self.assertNotIn("Remarks", reasons)

    def test_directories_beyond_the_limit_of_one_run_are_not_listed_and_say_so(self):
        rows = "".join(
            gate_row(STARTED, 0, "1.000", 0, f"gate/d{index:02}", "1.0") for index in range(60)
        )
        done, _ = self.count({GATE: gate_file(rows=rows)})
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = self.rows("Gate runs")
        self.assertEqual(50, len(row[6].split(" · ")))
        self.assertTrue(
            any("more than 50 directories" in unknown[3] for unknown in self.unknown_rows())
        )


class RegisterCount(AuditCountCase):
    """The register of problems counted against the cycles (WAY-330)."""

    def use_register(self, **rows) -> None:
        self.register.write_text(register_text(**rows), encoding="utf-8")

    def the_way_with_a_fix(self):
        """A checkout of the-way: the fix commit, a commit that holds it, and one that does not."""
        way = self.repository("the-way")
        start = way.commit({"README.md": "the-way\n"}, "Start")
        fix = way.commit({"README.md": "the-way, fixed\n"}, "Fix the process", start)
        with_fix = way.commit({"README.md": "the-way, later\n"}, "Later change", fix)
        without = way.commit({"README.md": "the-way, other\n"}, "Other change", start)
        way.branch("main", with_fix)
        return way, fix, with_fix, without

    def test_a_fixed_issue_counts_apart_the_cycles_whose_pin_holds_the_fix(self):
        way, fix, with_fix, without = self.the_way_with_a_fix()
        product = self.repository()
        holding, removed = product.cycle(
            "holds-task", {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")}
        )
        lacking, _ = product.cycle(
            "lacks-task",
            {"cycle.md": record(pin_line=f"- Process pin: `{without}`")},
            parent=removed,
        )
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix)],
            problems=[
                problem_row("product", holding, "fixed-one"),
                problem_row("product", lacking, "fixed-one"),
            ],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", fix, "1", "1", "0", "0", "0"]], self.rows("Fixed issues"))

    def test_the_template_with_no_rows_counts_nothing_and_refuses_nothing(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", added, "none", "0", "0", "0", "0", "0"]], self.rows("Problems by cycle")
        )
        self.assertEqual([], self.rows("Fixed issues"))
        self.assertEqual([], self.register_pair_rows())

    def test_a_problem_whose_repository_is_not_read_stays_unknown(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(problems=[problem_row("ghost", added)])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [
                [
                    "row of `Problems`",
                    "1",
                    "no named repository holds the cycle of its record; name its key with "
                    "--repository",
                    f"ghost {added}: row 1 of `Problems`",
                ]
            ],
            self.register_pair_rows(),
        )
        self.assertEqual(
            [["product", added, "none", "0", "0", "0", "0", "0"]], self.rows("Problems by cycle")
        )

    def test_crafted_rows_of_the_register_are_refused_with_a_reason_and_the_rest_counted(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            classes=[
                "| Not Lower | x | start | none |",
                "| dated-class | x | 2026-02-30 | none |",
                "| evil\x1b[2J-class | x | start | none |",
                "| " + "a" * 200_000 + " | x | start | none |",
            ],
            issues=[issue_row("good-issue"), "| bad-fix | the matter | fixed | 1234567 |"],
            problems=[
                problem_row("product", added, "good-issue"),
                problem_row("product", added, "good-issue", cls="no-such-class"),
                problem_row("product", "nothex", "good-issue"),
                problem_row("product", added, "good-issue", weight="Blocker"),
                problem_row("product", added, "bad-fix"),
                problem_row("product", added, "missing-issue"),
                problem_row("r" * 200_000, added, "good-issue"),
            ],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        pairs = self.pair_rows()
        self.assertEqual(
            [
                [
                    "row of `Classes`",
                    "3",
                    "the class name is not lower-case letters, digits and hyphens, or it is `none`",
                    f"the-way none: row 1 of `Classes`; "
                    "the-way none: row 3 of `Classes`; the-way none: row 4 of `Classes`",
                ],
                [
                    "row of `Classes`",
                    "1",
                    "the column Added is neither `start` nor a date written YYYY-MM-DD",
                    "the-way none: row 2 of `Classes`",
                ],
            ],
            [row for row in pairs if row[0] == "row of `Classes`"],
        )
        self.assertIn("row of `Issues`", [row[0] for row in pairs])
        issue_reason = "the issue is in no valid row of Issues"
        self.assertEqual(
            [
                "row of `Problems`",
                "2",
                issue_reason,
                f"product {added}: row 5 of `Problems`; product {added}: row 6 of `Problems`",
            ],
            [row for row in pairs if row[2] == issue_reason][0],
        )
        self.assertIn("row of `Problems`", [row[0] for row in pairs])
        self.assertTrue(all(len(cell) < 1000 for row in pairs for cell in row), pairs)
        # Four of the seven rows name this cycle and are refused (class, weight, issue, issue); the
        # valid one is counted; the count with refused rows of the cycle reads `at least`.
        self.assertEqual(
            [
                [
                    "product",
                    added,
                    "process-remark",
                    "at least 0",
                    "at least 1",
                    "at least 0",
                    "at least 0",
                    "4",
                ]
            ],
            self.rows("Problems by cycle"),
        )
        self.assertEqual(["good-issue"], [row[0] for row in self.rows("Open issues")])

    def test_a_class_named_in_two_rows_refuses_both_and_its_problems_with_it(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            classes=["| process-remark | again | start | none |"],
            problems=[problem_row("product", added)],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [
                [
                    "row of `Classes`",
                    "2",
                    "the name is written in two rows",
                    "the-way none: row 1 of `Classes`; the-way none: row 8 of `Classes`",
                ]
            ],
            [row for row in self.pair_rows() if row[0] == "row of `Classes`"],
        )
        self.assertEqual(
            [
                [
                    "product",
                    added,
                    "none",
                    "at least 0",
                    "at least 0",
                    "at least 0",
                    "at least 0",
                    "1",
                ]
            ],
            self.rows("Problems by cycle"),
        )
        self.assertIn(
            [
                "row of `Problems`",
                "1",
                "the class is not in the list of classes",
                f"product {added}: row 1 of `Problems`",
            ],
            self.pair_rows(),
        )

    def test_a_refused_row_of_a_cycle_and_an_issue_is_counted_not_hidden(self):
        # Scratch A of the review of slice 5: one open issue, one problem of it in one cycle with a
        # weight the scale lacks. The row is refused; the cycle and the issue must not read as
        # having no problem, since the refused row belongs to both.
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            issues=[issue_row("open-one")],
            problems=[problem_row("product", added, "open-one", weight="Blocker")],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [
                [
                    "product",
                    added,
                    "none",
                    "at least 0",
                    "at least 0",
                    "at least 0",
                    "at least 0",
                    "1",
                ]
            ],
            self.rows("Problems by cycle"),
        )
        self.assertEqual(
            [["open-one", "at least 0", "at least 0", "at least 0", "unknown", "1"]],
            self.rows("Open issues"),
        )
        self.assertIn(
            "the weight is not one of the four levels", [row[2] for row in self.pair_rows()]
        )

    def test_a_long_run_of_blanks_in_a_class_name_does_not_stall_the_count(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(classes=["| a" + " " * 150_000 + "b | x | start | none |"])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11", timeout=60)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", added, "none", "0", "0", "0", "0", "0"]], self.rows("Problems by cycle")
        )

    def test_a_register_lacking_a_field_ends_the_run_with_an_error_naming_it(self):
        # WAY-344: a heading, a table or a column the count needs and cannot find is no empty
        # value; the run ends with exit code 2, nothing written, and the error names the field.
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.assertEqual(1, TEMPLATE.count("## Issues\n"))
        self.assertEqual(1, TEMPLATE.count("## Costs of an occurrence\n"))
        without_cost = PROBLEMS_HEADER.replace("| Cost of an occurrence ", "").replace(
            "---|", "", 1
        )
        self.assertEqual(1, TEMPLATE.count(PROBLEMS_HEADER))
        costs_header = "| Cost of an occurrence | Meaning |\n|---|---|\n"
        self.assertEqual(1, TEMPLATE.count(costs_header))
        cases = (
            ("a heading", TEMPLATE.replace("## Issues\n", "## Issue list\n"), "## Issues"),
            (
                "the heading of the table of costs",
                TEMPLATE.replace("## Costs of an occurrence\n", "## Costs\n"),
                "## Costs of an occurrence",
            ),
            (
                "a table",
                TEMPLATE.replace("| Issue | What | Fate | Fix |\n|---|---|---|---|\n", ""),
                "table under the heading `## Issues`",
            ),
            (
                "the column of the cost, as the old form of the register has it",
                TEMPLATE.replace(PROBLEMS_HEADER, without_cost),
                "`Cost of an occurrence`",
            ),
            (
                "the column of the cost under another name",
                TEMPLATE.replace("| Weight | Cost of an occurrence |", "| Weight | Cost |"),
                "`Cost of an occurrence`",
            ),
            (
                "the column of the meaning of a cost",
                TEMPLATE.replace(costs_header, "| Cost of an occurrence |\n|---|\n"),
                "`Meaning`",
            ),
        )
        self.write_locations(self.places(product=product))
        for label, text, field in cases:
            with self.subTest(label):
                self.assertNotEqual(TEMPLATE, text)
                self.register.write_text(text, encoding="utf-8")
                done = self.run_count("--today", "2026-11-11")
                self.assertEqual(2, done.returncode, done.stderr)
                error = done.stderr.decode("utf-8")
                self.assertIn("Error: the register of problems", error)
                self.assertIn(field, error)
                self.assertEqual([], list(self.results.iterdir()))

    def test_every_field_missing_from_the_register_is_named_in_one_error(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        text = TEMPLATE.replace("## Issues\n", "## Issue list\n").replace(
            "## Classes\n", "## Class list\n"
        )
        self.register.write_text(text, encoding="utf-8")
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(2, done.returncode, done.stderr)
        error = done.stderr.decode("utf-8")
        self.assertIn("## Issues", error)
        self.assertIn("## Classes", error)

    def test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing(self):
        # Every column the count needs stands in the header row, but not in the template's order,
        # or another stands beside them: no field is missing, so the table is refused with a reason
        # as before, and the run is not ended.
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.assertEqual(1, TEMPLATE.count(PROBLEMS_HEADER))
        extra = PROBLEMS_HEADER.replace("| Issue |", "| Issue | Note |").replace(
            "---|", "---|---|", 1
        )
        swapped = PROBLEMS_HEADER.replace(
            "| Weight | Cost of an occurrence |", "| Cost of an occurrence | Weight |"
        )
        self.assertNotEqual(PROBLEMS_HEADER, swapped)
        self.write_locations(self.places(product=product))
        for label, header in (("an extra column", extra), ("two columns swapped", swapped)):
            with self.subTest(label):
                self.register.write_text(
                    TEMPLATE.replace(PROBLEMS_HEADER, header), encoding="utf-8"
                )
                done = self.run_count("--today", "2026-11-11")
                self.assertEqual(1, done.returncode, done.stderr)
                self.assertIn("table `Problems`", [row[0] for row in self.pair_rows()])
                self.assertEqual(
                    [["product", added, "none", "0", "0", "0", "0", "0"]],
                    self.rows("Problems by cycle"),
                )

    def test_a_register_larger_than_the_cap_stops_the_run_with_nothing_written(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.register.write_text(TEMPLATE + "x" * 4_200_000, encoding="utf-8")
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(2, done.returncode)
        self.assertIn(b"Error: ", done.stderr)
        self.assertEqual([], list(self.results.iterdir()))

    def test_open_issues_wait_from_the_cycle_commit_to_the_day_of_the_run(self):
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        # 1760000000 is 2025-10-09 in UTC.
        added = product.commit_dated(
            {"README.md": "a product\n", "docs/task-cycles/slow-task/cycle.md": record()},
            start,
            "1760000000",
        )
        removed = product.commit({"README.md": "a product\n"}, "Remove the record", added)
        product.branch("main", removed)
        self.use_register(
            issues=[issue_row("slow-one")], problems=[problem_row("product", added, "slow-one")]
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2025-10-19")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["slow-one", "0", "1", "0", "10", "0"]], self.rows("Open issues"))
        done = self.run_count("--today", "2025-10-08")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual("unknown", self.rows("Open issues")[0][4])

    def test_open_issues_are_listed_in_the_register_order_not_by_their_returns(self):
        product = self.repository()
        first, removed = product.cycle("a-task", {"cycle.md": record()})
        second, removed = product.cycle("b-task", {"cycle.md": record()}, parent=removed)
        third, _ = product.cycle("c-task", {"cycle.md": record()}, parent=removed)
        self.use_register(
            issues=[issue_row("first-issue"), issue_row("second-issue")],
            problems=[
                problem_row("product", first, "first-issue"),
                problem_row("product", second, "second-issue"),
                problem_row("product", third, "second-issue"),
            ],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["first-issue", "0", "1", "0"], ["second-issue", "1", "2", "0"]],
            [row[:4] for row in self.rows("Open issues")],
        )

    def test_an_open_issue_counts_the_cycles_its_problems_came_back_in(self):
        # Three cycles hold problems of one issue, one of them two: the problem stands in the first
        # and came back in the other two, so the count is 2, not 3.
        product = self.repository()
        first, removed = product.cycle("a-task", {"cycle.md": record()})
        second, removed = product.cycle("b-task", {"cycle.md": record()}, parent=removed)
        third, _ = product.cycle("c-task", {"cycle.md": record()}, parent=removed)
        self.use_register(
            issues=[issue_row("seen-once"), issue_row("seen-thrice")],
            problems=[
                problem_row("product", first, "seen-once"),
                problem_row("product", first, "seen-thrice"),
                problem_row("product", first, "seen-thrice"),
                problem_row("product", second, "seen-thrice"),
                problem_row("product", third, "seen-thrice"),
            ],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn("| Issue | Cycles its problems came back in | Problems |", self.latest())
        self.assertEqual(
            [["seen-once", "0", "1", "0"], ["seen-thrice", "2", "4", "0"]],
            [row[:4] for row in self.rows("Open issues")],
        )

    def test_the_count_of_returns_reads_at_least_where_a_row_or_a_cycle_is_missing(self):
        product = self.repository()
        first, removed = product.cycle("a-task", {"cycle.md": record()})
        second, removed = product.cycle("b-task", {"cycle.md": record()}, parent=removed)
        third, _ = product.cycle("c-task", {"cycle.md": record()}, parent=removed)
        self.use_register(
            issues=[issue_row("exact"), issue_row("cycle-lost"), issue_row("row-refused")],
            problems=[
                problem_row("product", first, "exact"),
                problem_row("product", second, "exact"),
                problem_row("product", first, "cycle-lost"),
                problem_row("product", second, "cycle-lost"),
                problem_row("product", third, "cycle-lost"),
                problem_row("ghost", first, "cycle-lost"),
                problem_row("product", first, "row-refused"),
                problem_row("product", second, "row-refused"),
                problem_row("product", third, "row-refused", weight="Blocker"),
            ],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        # `cycle-lost`: its problem of an unread cycle may stand in a fourth cycle, so at least 2.
        # `row-refused`: the refused row may name another cycle, so at least 1.
        self.assertEqual(
            [
                ["exact", "1", "2", "0"],
                ["cycle-lost", "at least 2", "4", "1"],
                ["row-refused", "at least 1", "at least 2", "at least 0"],
            ],
            [row[:4] for row in self.rows("Open issues")],
        )

    def test_a_cycle_copied_again_is_one_cycle_in_the_count_of_returns(self):
        product = self.repository()
        first, removed = product.cycle("a-task", {"cycle.md": record()})
        again, removed = product.cycle(
            "a-task",
            {"cycle.md": record(remarks="- Process remarks on the-way:\n  - one\n")},
            parent=removed,
        )
        second, _ = product.cycle("b-task", {"cycle.md": record()}, parent=removed)
        self.use_register(
            issues=[issue_row("one-cycle"), issue_row("two-cycles")],
            problems=[
                problem_row("product", first, "one-cycle"),
                problem_row("product", again, "one-cycle"),
                problem_row("product", again, "two-cycles"),
                problem_row("product", second, "two-cycles"),
            ],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["one-cycle", "0", "2", "0"], ["two-cycles", "1", "2", "0"]],
            [row[:4] for row in self.rows("Open issues")],
        )

    def test_a_cycle_committed_again_counts_its_problem_once(self):
        product = self.repository()
        first, removed = product.cycle("fixed-task", {"cycle.md": record()})
        again, _ = product.cycle(
            "fixed-task",
            {"cycle.md": record(remarks="- Process remarks on the-way:\n  - author: one\n")},
            parent=removed,
        )
        self.use_register(problems=[problem_row("product", again)])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", first, "process-remark", "0", "1", "0", "0", "0"]],
            self.rows("Problems by cycle"),
        )

    def test_an_unknown_pin_or_a_pin_the_history_lacks_is_unknown_for_its_side(self):
        way, fix, with_fix, _ = self.the_way_with_a_fix()
        product = self.repository()
        no_pin, removed = product.cycle(
            "no-pin-task", {"cycle.md": record(pin_line="- Process pin: none")}
        )
        lacking, removed = product.cycle(
            "lacking-task",
            {
                "cycle.md": record(
                    pin_line="- Process pin: `fedcba9876543210fedcba9876543210fedcba98`"
                )
            },
            parent=removed,
        )
        holding, _ = product.cycle(
            "holding-task",
            {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")},
            parent=removed,
        )
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix)],
            problems=[
                problem_row("product", no_pin, "fixed-one"),
                problem_row("product", lacking, "fixed-one"),
                problem_row("product", holding, "fixed-one"),
            ],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", fix, "1", "0", "2", "0", "0"]], self.rows("Fixed issues"))
        reasons = [
            row[3]
            for row in self.rows("Unknown values")
            if row[:3] == ["product", lacking, "Process pin"]
        ]
        self.assertEqual(1, len(reasons), reasons)
        self.assertIn("lacks commit", reasons[0])

    def test_the_cycles_whose_pin_is_unknown_for_a_fixed_issue_make_one_pair_with_three_examples(
        self,
    ):
        # Four cycles whose pin the history lacks, all the same pin: more than the three examples
        # of a pair, so the pair counts four and shows the first three cycles in the order of the
        # result (WAY-330).
        way, fix, _, _ = self.the_way_with_a_fix()
        product = self.repository()
        cycles, parent = [], None
        for number in range(1, 5):
            added, removed = product.cycle(
                f"pin-task-{number}",
                {"cycle.md": record(pin_line=f"- Process pin: `{'7' * 40}`")},
                parent=parent,
            )
            cycles.append(added)
            parent = removed
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix)],
            problems=[problem_row("product", added, "fixed-one") for added in cycles],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        pairs = [row for row in self.pair_rows() if row[0] == "Process pin"]
        self.assertEqual(1, len(pairs), pairs)
        self.assertEqual("4", pairs[0][1])
        self.assertIn("lacks commit", pairs[0][2])
        order = [cycle["Record"] for cycle in self.cycles()]
        self.assertEqual(
            "; ".join(f"product {first}: Process pin" for first in order[:3]), pairs[0][3]
        )

    def test_more_than_three_values_of_a_pair_are_counted_and_three_are_listed(self):
        # Five cycles with no `stages.md`: five values of each of the four fields of the stage
        # report, with one reason each, so four lines of five values, and no value past the third
        # of a pair in the result.
        product = self.repository()
        parent = None
        for number in range(1, 6):
            _, parent = product.cycle(f"a-task-{number}", {"cycle.md": record()}, parent=parent)
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        order = [cycle["Record"] for cycle in self.cycles()]
        self.assertEqual(5, len(order))
        pairs = [row for row in self.pair_rows() if row[0] == "Cost"]
        self.assertEqual(
            [
                [
                    "Cost",
                    "5",
                    "the copy holds no `stages.md`",
                    "; ".join(f"product {first}: Cost" for first in order[:3]),
                ]
            ],
            pairs,
        )
        text = self.latest()
        for later in order[3:]:
            self.assertNotIn(f"product {later}: Cost", text)
        self.assertEqual(1, sum(1 for line in text.splitlines() if line.startswith("| Cost | ")))

    def test_the_section_says_where_the_full_list_of_a_pair_stands_and_names_no_run_of_the_count(
        self,
    ):
        # The result keeps three examples of each pair, and a new run of the count writes the same
        # table, so the section names the register and the copies of the records in git history
        # for the full lists, says the count lists no more, and names no new run as a place.
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        text = self.latest()
        section = text.split("\n## Unknown values\n", 1)[1].split("\n## ", 1)[0]
        intro = " ".join(section.split("| Field |", 1)[0].split())
        self.assertIn("no option of the count lists the rest", intro)
        self.assertIn("in the register", intro)
        self.assertIn("in the copies of the cycles' records in the history of git", intro)
        self.assertIn("about an issue or a version are made by the count", intro)
        self.assertNotIn("new run", intro)

    def test_issues_that_differ_only_in_their_names_make_one_pair_for_each_kind_of_value(self):
        # Three fixed issues with one fix the history lacks, two open issues each with a problem of
        # a cycle no repository holds: the fix of an issue and the waiting of an issue are one pair
        # each, whatever the names, and the examples carry the names.
        way, _, _, _ = self.the_way_with_a_fix()
        missing = "1234567890abcdef1234567890abcdef12345678"
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            issues=[issue_row(name, "fixed", missing) for name in ("one", "two", "three")]
            + [issue_row(name) for name in ("open-a", "open-b")],
            problems=[problem_row("ghost", added, name) for name in ("open-a", "open-b")],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        pairs = self.pair_rows()
        fixes = [row for row in pairs if row[0] == "the fix of an issue"]
        self.assertEqual(1, len(fixes), pairs)
        self.assertEqual("3", fixes[0][1])
        self.assertEqual(
            "; ".join(
                f"the-way none: the fix of issue `{name}`" for name in ("one", "two", "three")
            ),
            fixes[0][3],
        )
        waits = [row for row in pairs if row[0] == "waiting of an issue"]
        self.assertEqual(1, len(waits), pairs)
        self.assertEqual("2", waits[0][1])
        self.assertEqual(
            "the-way none: waiting of issue `open-a`; the-way none: waiting of issue `open-b`",
            waits[0][3],
        )

    def test_a_refused_problem_of_a_fixed_issue_is_counted_in_its_row(self):
        way, fix, with_fix, _ = self.the_way_with_a_fix()
        product = self.repository()
        holding, _ = product.cycle(
            "holding-task", {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")}
        )
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix)],
            problems=[
                problem_row("product", holding, "fixed-one"),
                problem_row("product", holding, "fixed-one", weight="Blocker"),
            ],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        # Every count beside the refused row reads `at least`: the row could belong to any column.
        self.assertEqual(
            [["fixed-one", fix, "at least 1", "at least 0", "at least 0", "at least 0", "1"]],
            self.rows("Fixed issues"),
        )

    def test_a_record_that_adds_the_records_of_two_cycles_names_neither(self):
        # One commit adds the records of two cycles: a problem naming it belongs to no one cycle.
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        both = product.commit(
            {
                "README.md": "a product\n",
                "docs/task-cycles/a/cycle.md": record(),
                "docs/task-cycles/b/cycle.md": record(),
            },
            "Add two records",
            start,
        )
        product.branch("main", product.commit({"README.md": "a product\n"}, "Remove", both))
        self.use_register(
            issues=[issue_row("open-one")],
            problems=[problem_row("product", both, "open-one", cls="foundation-gap")],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["product", both, "none", "at least 0", "at least 0", "at least 0", "at least 0", "0"]]
            * 2,
            self.rows("Problems by cycle"),
        )
        reasons = [row[2] for row in self.pair_rows() if "row 1 of `Problems`" in row[3]]
        self.assertEqual(1, len(reasons), reasons)
        self.assertIn("more than one cycle", reasons[0])
        self.assertEqual(
            [["open-one", "at least 0", "1", "1", "unknown", "0"]], self.rows("Open issues")
        )

    def test_an_open_issue_waits_from_the_copy_its_problem_names(self):
        # 1760000000 is 2025-10-09 and 1760864000 is 2025-10-19 in UTC. The problem stands in the
        # second copy of a corrected cycle: it waits from that copy, 10 days, not from the first.
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        first = product.commit_dated(
            {"README.md": "a product\n", "docs/task-cycles/slow-task/cycle.md": record()},
            start,
            "1760000000",
        )
        removed = product.commit({"README.md": "a product\n"}, "Remove the record", first)
        again = product.commit_dated(
            {
                "README.md": "a product\n",
                "docs/task-cycles/slow-task/cycle.md": record(
                    remarks="- Process remarks on the-way:\n  - one\n"
                ),
            },
            removed,
            "1760864000",
        )
        product.branch("main", product.commit({"README.md": "a product\n"}, "Remove", again))
        self.use_register(
            issues=[issue_row("slow-one")], problems=[problem_row("product", again, "slow-one")]
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2025-10-29")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [[first, again]], [[c["Record"], c["Later copies"]] for c in self.cycles()]
        )
        self.assertEqual([["slow-one", "0", "1", "0", "10", "0"]], self.rows("Open issues"))

    def test_a_register_far_larger_than_a_real_one_gives_one_line_for_each_pair(self):
        # 830 problems whose cycle no repository holds, about the lines the result gave for a
        # register of that size, and two refused for a weight the scale lacks: two pairs, one line
        # each, with the count of its values and the first three of them as examples.
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            problems=[problem_row("ghost", added) for _ in range(830)]
            + [problem_row("product", added, weight="Blocker") for _ in range(2)]
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        pairs = self.register_pair_rows()
        self.assertEqual(2, len(pairs), pairs)
        self.assertEqual(
            [
                "row of `Problems`",
                "2",
                "the weight is not one of the four levels",
                f"product {added}: row 831 of `Problems`; product {added}: row 832 of `Problems`",
            ],
            pairs[0],
        )
        self.assertEqual(
            [
                "row of `Problems`",
                "830",
                "no named repository holds the cycle of its record; name its key with --repository",
                "; ".join(f"ghost {added}: row {number} of `Problems`" for number in (1, 2, 3)),
            ],
            pairs[1],
        )

    def test_problems_whose_cycle_is_not_read_count_apart_for_fixed_and_dropped_issues(self):
        way, fix, _, _ = self.the_way_with_a_fix()
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix), issue_row("gone", "dropped")],
            problems=[
                problem_row("ghost", added, "fixed-one"),
                problem_row("ghost", added, "gone"),
            ],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", fix, "0", "0", "0", "1", "0"]], self.rows("Fixed issues"))
        self.assertEqual([["gone", "0", "1", "1", "0"]], self.rows("Dropped issues"))

    def test_a_pin_written_as_a_short_hash_is_resolved_in_the_way(self):
        way, fix, with_fix, _ = self.the_way_with_a_fix()
        product = self.repository()
        holding, _ = product.cycle(
            "short-task", {"cycle.md": record(pin_line=f"- Process pin: `{with_fix[:7]}`")}
        )
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix)],
            problems=[problem_row("product", holding, "fixed-one")],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", fix, "1", "0", "0", "0", "0"]], self.rows("Fixed issues"))

    def test_a_short_hash_two_objects_share_is_ambiguous(self):
        import hashlib

        way, fix, with_fix, _ = self.the_way_with_a_fix()
        # Two blobs whose names share their first seven characters, found by their hashes.
        seen: dict[str, bytes] = {}
        for number in range(1_000_000):
            data = f"{number}\n".encode("ascii")
            name = hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()
            # A pin is read as a commit only with a digit in it.
            if (
                name[:7] in seen
                and name[:7] not in (fix[:7], with_fix[:7])
                and any(char.isdigit() for char in name[:7])
            ):
                break
            seen[name[:7]] = data
        prefix = name[:7]
        for blob in (seen[prefix], data):
            way.blob(blob)
        product = self.repository()
        cycle, _ = product.cycle(
            "odd-task", {"cycle.md": record(pin_line=f"- Process pin: `{prefix}`")}
        )
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix)],
            problems=[problem_row("product", cycle, "fixed-one")],
        )
        places = self.places(product=product)
        places["the-way"]["repository"] = str(way.root)
        self.write_locations(places)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", fix, "0", "0", "1", "0", "0"]], self.rows("Fixed issues"))
        self.assertIn(
            "ambiguous",
            " ".join(
                row[3]
                for row in self.rows("Unknown values")
                if row[:3] == ["product", cycle, "Process pin"]
            ),
        )

    def test_a_shallow_clone_of_the_way_lacking_the_fix_says_so(self):
        way, fix, with_fix, _ = self.the_way_with_a_fix()
        shallow = self.home / "repos" / "shallow-way"
        subprocess.run(
            ["git", "clone", "-q", "--depth", "1", way.root.as_uri(), str(shallow)],
            capture_output=True,
            env=GIT_ENV,
            check=True,
        )
        product = self.repository()
        holding, _ = product.cycle(
            "holding-task", {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")}
        )
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", fix)],
            problems=[problem_row("product", holding, "fixed-one")],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(shallow)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["fixed-one", fix, "unknown", "unknown", "0", "0", "0"]], self.rows("Fixed issues")
        )
        self.assertIn(
            "shallow clone",
            " ".join(
                row[3]
                for row in self.rows("Unknown values")
                if row[2] == "the fix of issue `fixed-one`"
            ),
        )

    def test_a_doubled_heading_or_header_row_of_the_register_is_refused(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.register.write_text(
            register_text() + "\n## Classes\n\n" + CLASSES_HEADER, encoding="utf-8"
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(1, done.returncode, done.stderr)
        self.assertIn("`## Classes` more than once", done.stderr.decode("utf-8"))
        self.use_register(
            problems=[PROBLEMS_HEADER.split("\n", 1)[0], problem_row("product", added)]
        )
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn(
            ["row of `Problems`", "1", "the Record is no commit of 40 hexadecimal characters"],
            [row[:3] for row in self.pair_rows()],
        )
        self.assertEqual(
            [["product", added, "process-remark", "0", "1", "0", "0", "0"]],
            self.rows("Problems by cycle"),
        )

    def test_a_fix_the_history_lacks_leaves_its_issue_unknown(self):
        way, _, with_fix, _ = self.the_way_with_a_fix()
        missing = "1234567890abcdef1234567890abcdef12345678"
        product = self.repository()
        holding, _ = product.cycle(
            "holding-task", {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")}
        )
        self.use_register(
            issues=[issue_row("fixed-one", "fixed", missing)],
            problems=[problem_row("product", holding, "fixed-one")],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [["fixed-one", missing, "unknown", "unknown", "0", "0", "0"]], self.rows("Fixed issues")
        )
        reasons = [
            row[3]
            for row in self.rows("Unknown values")
            if row[2] == "the fix of issue `fixed-one`"
        ]
        self.assertEqual(1, len(reasons), reasons)
        self.assertIn("lacks commit", reasons[0])

    def test_the_problems_of_each_issue_are_counted_on_each_level_of_the_cost_of_an_occurrence(
        self,
    ):
        way, fix, _, _ = self.the_way_with_a_fix()
        product = self.repository()
        first, removed = product.cycle("a-task", {"cycle.md": record()})
        second, _ = product.cycle("b-task", {"cycle.md": record()}, parent=removed)
        self.use_register(
            issues=[
                issue_row("open-one"),
                issue_row("fixed-one", "fixed", fix),
                issue_row("gone", "dropped"),
            ],
            problems=[
                problem_row("product", first, "open-one", weight="Minor", cost="steps"),
                problem_row("product", first, "open-one", weight="Important", cost="steps"),
                problem_row("product", first, "fixed-one", weight="Minor", cost="round"),
                problem_row("product", second, "open-one", weight="Critical", cost="human"),
                problem_row("product", second, "fixed-one", weight="no problem", cost="nothing"),
                problem_row("product", second, "gone", weight="Minor", cost="stage"),
                problem_row("product", second, "none", weight="Minor", cost="human"),
                # The cost stands in the row, so a problem of a cycle that is not read counts too.
                problem_row("ghost", first, "open-one", weight="Minor", cost="round"),
            ],
        )
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        # Issue, fate, then the problems on nothing, steps, stage, round and human, in the order
        # of the register; the problem that belongs to no issue is in no row.
        self.assertEqual(
            [
                ["open-one", "open", "0", "2", "0", "1", "1", "0"],
                ["fixed-one", "fixed", "1", "0", "0", "1", "0", "0"],
                ["gone", "dropped", "0", "0", "1", "0", "0", "0"],
            ],
            self.rows("Cost of an occurrence by issue"),
        )
        # The cost is no weight: the counts by weight stay as the rows give them.
        self.assertEqual(
            [
                ["product", first, "process-remark", "0", "2", "1", "0", "0"],
                ["product", second, "process-remark", "1", "2", "0", "1", "0"],
            ],
            self.rows("Problems by cycle"),
        )
        self.assertEqual("4", self.rows("Open issues")[0][2])

    def test_a_cost_that_is_no_level_refuses_its_row_and_reads_at_least_in_its_issue(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            issues=[issue_row("open-one")],
            problems=[
                problem_row("product", added, "open-one", cost="steps"),
                problem_row("product", added, "open-one", cost="Steps"),
                problem_row("product", added, "open-one", cost="free"),
                problem_row("product", added, "open-one", cost=""),
                problem_row("product", added, "open-one", cost="Minor"),
                problem_row("product", added, "open-one", cost="steps\x1b[2J"),
                problem_row("product", added, "open-one", cost="st|eps"),
                # A line break in a cell ends the row, and the table with it.
                problem_row("product", added, "open-one", cost="steps\nhuman"),
            ],
        )
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        self.assertEqual(
            [
                [
                    "open-one",
                    "open",
                    "at least 0",
                    "at least 1",
                    "at least 0",
                    "at least 0",
                    "at least 0",
                    "5",
                ]
            ],
            self.rows("Cost of an occurrence by issue"),
        )
        # Rows 2 to 6 share one reason, and rows 7 and 8 have one each; rows 2 to 4 are examples.
        self.assertEqual(
            [
                [
                    "row of `Problems`",
                    "5",
                    "the cost of an occurrence is not one of the five levels",
                    f"product {added}: row 2 of `Problems`; product {added}: row 3 of `Problems`; "
                    f"product {added}: row 4 of `Problems`",
                ],
                [
                    "row of `Problems`",
                    "1",
                    "the row has 9 cells, not 8",
                    f"product {added}: row 7 of `Problems`",
                ],
                [
                    "row of `Problems`",
                    "1",
                    "the row has 7 cells, not 8",
                    f"product {added}: row 8 of `Problems`",
                ],
            ],
            [row for row in self.pair_rows() if row[0] == "row of `Problems`"],
        )

    def test_a_table_of_costs_that_lacks_a_level_is_treated_as_the_table_of_weights_is(self):
        # decision: WAY-344 "The command that counts the audit, where a table of weights"
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        lines = TEMPLATE.splitlines(keepends=True)
        self.assertEqual(1, sum(1 for line in lines if line.startswith("| stage |")))
        self.assertEqual(1, sum(1 for line in lines if line.startswith("| steps |")))
        missing = "".join(line for line in lines if not line.startswith("| stage |"))
        doubled = "".join(
            line + ("| steps | once more |\n" if line.startswith("| steps |") else "")
            for line in lines
        )
        both = "".join(
            line + ("| steps | once more |\n" if line.startswith("| steps |") else "")
            for line in lines
            if not line.startswith("| stage |")
        )
        self.write_locations(self.places(product=product))
        cases = (
            ("a level missing", missing, "must name each level once: it lacks `stage`"),
            (
                "a level written twice",
                doubled,
                "must name each level once: it writes `steps` in two rows",
            ),
            (
                "a level missing and another written twice",
                both,
                "must name each level once: it lacks `stage` and writes `steps` in two rows",
            ),
        )
        for label, text, words in cases:
            with self.subTest(label):
                self.register.write_text(text, encoding="utf-8")
                done = self.run_count("--today", "2026-11-11")
                self.assertEqual(1, done.returncode, done.stderr)
                self.assertIn(
                    "Error: the register of problems: the table `Costs of an occurrence` " + words,
                    done.stderr.decode("utf-8"),
                )
                self.assertIn(
                    "table `Costs of an occurrence`", [row[0] for row in self.pair_rows()]
                )
                self.assertEqual(
                    [["product", added, "none", "0", "0", "0", "0", "0"]],
                    self.rows("Problems by cycle"),
                )
        with self.subTest("a level the scale lacks, beside the five"):
            # As an unknown weight beside the four: its row is refused and the five stand.
            self.register.write_text(
                TEMPLATE.replace("| human |", "| free | no such level |\n| human |"),
                encoding="utf-8",
            )
            done = self.run_count("--today", "2026-11-11")
            self.assertEqual(0, done.returncode, done.stderr)
            self.assertIn("row of `Costs of an occurrence`", [row[0] for row in self.pair_rows()])
        with self.subTest("the template as it stands"):
            self.register.write_text(TEMPLATE, encoding="utf-8")
            done = self.run_count("--today", "2026-11-11")
            self.assertEqual(0, done.returncode, done.stderr)
            self.assertEqual(b"", done.stderr)

    def test_a_table_of_weights_that_lacks_a_level_names_the_level(self):
        # decision: WAY-344 "The command that counts the audit, where a table of weights"
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        lines = TEMPLATE.splitlines(keepends=True)
        self.assertEqual(1, sum(1 for line in lines if line.startswith("| Minor |")))
        self.assertEqual(1, sum(1 for line in lines if line.startswith("| Important |")))
        missing = "".join(line for line in lines if not line.startswith("| Minor |"))
        doubled = "".join(
            line + ("| Important | once more |\n" if line.startswith("| Important |") else "")
            for line in lines
        )
        both = "".join(
            line + ("| Important | once more |\n" if line.startswith("| Important |") else "")
            for line in lines
            if not line.startswith("| Minor |")
        )
        self.write_locations(self.places(product=product))
        cases = (
            ("a level missing", missing, "must name each level once: it lacks `Minor`"),
            (
                "a level written twice",
                doubled,
                "must name each level once: it writes `Important` in two rows",
            ),
            (
                "a level missing and another written twice",
                both,
                "must name each level once: it lacks `Minor` and writes `Important` in two rows",
            ),
        )
        for label, text, words in cases:
            with self.subTest(label):
                self.register.write_text(text, encoding="utf-8")
                done = self.run_count("--today", "2026-11-11")
                self.assertEqual(1, done.returncode, done.stderr)
                self.assertIn(
                    "Error: the register of problems: the table `Weights` " + words,
                    done.stderr.decode("utf-8"),
                )
                self.assertIn("table `Weights`", [row[0] for row in self.pair_rows()])
                self.assertEqual(
                    [["product", added, "none", "0", "0", "0", "0", "0"]],
                    self.rows("Problems by cycle"),
                )


class Run(AuditCountCase):
    def test_it_reads_nothing_from_stdin(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        # stdin stays open and empty: a command that read it would wait until the timeout.
        with subprocess.Popen(
            [sys.executable, "-B", str(SCRIPT), "--locations", str(self.locations)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ, **NO_USER_GIT_CONFIG),
        ) as process:
            try:
                process.wait(timeout=60)
            except subprocess.TimeoutExpired:
                process.kill()
                self.fail("the command waited on stdin")
            self.assertEqual(0, process.returncode, process.stderr.read())

    def test_the_same_input_gives_the_same_bytes_in_both_files(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        # The day is given, so that no midnight between the two runs gives them two names.
        self.assertEqual(0, self.run_count("--today", "2026-11-11").returncode)
        first = (self.results / "count-latest.md").read_bytes()
        self.assertEqual(0, self.run_count("--today", "2026-11-11").returncode)
        names = sorted(path.name for path in self.results.iterdir())
        self.assertEqual(["count-2026-11-11.md", "count-latest.md"], names)
        self.assertEqual(first, (self.results / names[0]).read_bytes())
        self.assertEqual(first, (self.results / "count-latest.md").read_bytes())
        self.assertNotIn(b"\r", first)
        self.assertNotIn(str(self.home).encode("utf-8"), first)

    def test_without_a_name_it_reads_every_key_with_a_repository(self):
        first, second = self.repository("first"), self.repository("second")
        first.cycle("one", {"cycle.md": record()})
        second.cycle("two", {"cycle.md": record()})
        data = self.places(first=first, second=second)
        data["notes"] = {"tasks": str(self.home)}
        self.write_locations(data)
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([["first", "1", "yes"], ["second", "1", "yes"]], self.rows("Repositories"))
        self.assertEqual(0, self.run_count("--repository", "second").returncode)
        self.assertEqual([["second", "1", "yes"]], self.rows("Repositories"))

    def test_a_repository_git_cannot_read_is_named_and_the_rest_written(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        plain = self.home / "plain"
        plain.mkdir()
        data = self.places(product=product)
        data["plain"] = {"repository": str(plain)}
        self.write_locations(data)
        done = self.run_count()
        self.assertEqual(1, done.returncode, done.stderr)
        self.assertIn("Error: repository `plain`", done.stderr.decode("utf-8"))
        rows = self.rows("Repositories")
        self.assertEqual(["plain", "0"], rows[0][:2])
        self.assertTrue(rows[0][2].startswith("no: "), rows[0])
        self.assertEqual(["product", "1", "yes"], rows[1])

    def test_git_reads_the_named_checkout_whatever_git_variables_the_run_inherits(self):
        # A scheduler or a hook may start the command with GIT_DIR set to another repository.
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        other = self.repository("other")
        other.cycle("other-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        done = self.run_count(
            env={"GIT_DIR": str(other.root / ".git"), "GIT_WORK_TREE": str(other.root)}
        )
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            [("product", added, "a-task")],
            [(c["Repository"], c["Record"], c["Folder"]) for c in self.cycles()],
        )

    def test_the_way_without_a_repository_key_is_this_checkout(self):
        # decision: WAY-344 "Where the locations file has no key `repository` under `the-way`"
        # The script lies in a checkout built here: a copy of it with the files it reads beside it,
        # and a history that holds one cycle, so that the cycles it counts say whose history it read.
        checkout = self.repository("checkout")
        files = {}
        for name in (
            "process-audit/audit_count.py",
            "process-audit/record_items.py",
            "process-audit/stage_pricing.py",
            "process-audit/price_list.md",
            "task-cycle/remarks_check.py",
        ):
            files[name] = (HERE.parent / name).read_bytes()
            (checkout.root / name).parent.mkdir(parents=True, exist_ok=True)
            (checkout.root / name).write_bytes(files[name])
        checkout.cycle("a-task", {"cycle.md": record()}, base_files=files)
        self.write_locations(self.places())
        done = self.run_count_of_the_copy("--repository", "the-way")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["the-way", "1", "yes"]], self.rows("Repositories"))


NL = chr(10)


def process_record(
    pin,
    discarded="none",
    plan="none on the one-author route",
    too_large="none",
    rounds="none",
    extra="",
) -> str:
    """A cycle record whose items the questions of a process version read; `extra` adds lines
    under the status line, for a doubled item."""
    items = (
        f"- Discarded attempt: {discarded}\n- Plan: {plan}\n"
        f"- Slices returned too large: {too_large}\n- Review rounds: {rounds}\n{extra}"
    )
    return record(pin_line=f"- Process pin: `{pin}`").replace(
        "- Status: request open\n", "- Status: request open\n" + items
    )


class ProcessVersions(AuditCountCase):
    """The process versions, their series and the three questions (WAY-339)."""

    FIRST = 1759968000  # 2025-10-09, UTC midnight
    LATER = 1760054400  # 2025-10-10
    MARCH = 1772323200  # 2026-03-01
    BASE_FILES = {
        "README.md": "the-way\n",
        "task-cycle/change/SKILL.md": "change\n",
        "task-cycle/cycle_stages.py": "stages\n",
    }

    def the_way(self) -> Repository:
        way = self.repository("the-way")
        return way

    def version_at(self, way, when, parent=None, changed=None) -> str:
        """A commit of the-way dated `when`: the base files, with the files of `changed` replaced
        or added."""
        way.time = when - 3600
        files = {**self.BASE_FILES, **(changed or {})}
        return way.commit(files, f"Version at {when}", *([parent] if parent else []))

    def stages_of(self, tokens) -> str:
        return STAGES_HEADER + stage_row(1, "orchestrator", "model-a", tokens, 0, 0)

    def add_cycles(self, product, specs) -> None:
        """Each cycle as (folder, record text, tokens), chained so that all stay in the history;
        a fourth item is the text of its `stages.md`, where it is not the newer form."""
        parent = product.commit({"README.md": "a product\n"}, "Start")
        for folder, text, tokens, *stages in specs:
            _, parent = product.cycle(
                folder,
                {"cycle.md": text, "stages.md": stages[0] if stages else self.stages_of(tokens)},
                parent=parent,
                branch=None,
            )
        product.branch("main", parent)

    def run_versions(self, way, product, prices=TEST_PRICES):
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        test_prices = self.home / "prices.md"
        test_prices.write_text(prices, encoding="utf-8")
        done = self.run_count("--prices", str(test_prices), "--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)

    def cost_series(self, number) -> list[list[str]]:
        """The rows of a series of the cost: version, day, cycles, cycles with a known cost, median
        cost and Q3."""
        return self.section("Cost", number)

    def count_series(self, number) -> list[list[str]]:
        """The rows of a series of the count of remarks: version, day, cycles, Q1, plans read and
        Q2."""
        return self.section("Count of remarks", number)

    def test_the_cost_is_compared_inside_a_series_of_the_cost_across_a_new_class(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # v1 and v2 share a series of both kinds; a class added on the day of v3 starts a series of
        # the count of remarks and none of the cost. Medians: v1 is (2 + 4) / 2 = 3 dollars, v2 is
        # 1 dollar, v3 is 0.5 dollar. v2 falls against v1, and so does v3 against v2 (0.5 < 1):
        # the cost of v3 is compared with v2's, the count of remarks of v3 is not.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(way, self.LATER, parent=v1)
        v3 = self.version_at(way, self.MARCH, parent=v2)
        product = self.repository()
        self.add_cycles(
            product,
            [
                ("one", process_record(v1), 1_000_000),
                ("two", process_record(v1), 2_000_000),
                ("three", process_record(v2), 500_000),
                ("four", process_record(v3), 250_000),
                ("five", process_record("none"), 100),
            ],
        )
        # The class is added on the day of v3, which counts as between the two versions.
        self.register.write_text(
            register_text(classes=["| sharp | x | 2026-03-01 | none |"]), encoding="utf-8"
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "2025-10-09", "2", "2", "3.000000", "unknown"],
                [v2, "2025-10-10", "1", "1", "1.000000", "yes"],
                [v3, "2026-03-01", "1", "1", "0.500000", "yes"],
            ],
            self.cost_series(1),
        )
        self.assertNotIn("### Cost, series 2", self.latest())
        self.assertEqual(
            [
                [v1, "2025-10-09", "2", "no", "0 of 0", "unknown"],
                [v2, "2025-10-10", "1", "no", "0 of 0", "unknown"],
            ],
            self.count_series(1),
        )
        self.assertEqual([[v3, "2026-03-01", "1", "no", "0 of 0", "unknown"]], self.count_series(2))
        self.assertIn("### No version", self.latest())
        self.assertIn("## Process versions", self.latest())
        self.assertIn(
            "Begins at this version: the register's list of classes changed between "
            "the two versions.",
            self.latest(),
        )

    def test_no_row_of_a_series_of_one_kind_holds_a_figure_of_the_other(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # A table of the cost holds the median and Q3 and none of Q1 and Q2; a table of the count
        # of remarks holds Q1 and Q2 and none of the cost.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(product, [("one", process_record(v1), 1_000_000)])
        self.run_versions(way, product)
        text = self.latest()
        parts = []
        for heading in ("\n### Cost, series 1\n", "\n### Count of remarks, series 1\n"):
            self.assertIn(heading, text)
            parts.append(text.split(heading, 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0])
        cost, count = parts
        for name in ("Median cost (USD)", "Q3: cost falls"):
            self.assertIn(name, cost)
            self.assertNotIn(name, count)
        for name in ("Q1: contradiction only after code", "Q2: more than a third", "Plans read"):
            self.assertIn(name, count)
            self.assertNotIn(name, cost)

    def test_a_change_under_the_change_starts_a_series_of_the_count_and_none_of_the_cost(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # task-cycle/change is one of the files the form of a stage report is taken from; v2's
        # cost (0.5) falls against v1's (2) in a series of the cost that the change does not end.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way, self.LATER, parent=v1, changed={"task-cycle/change/SKILL.md": "changed\n"}
        )
        product = self.repository()
        self.add_cycles(
            product, [("one", process_record(v1), 1_000_000), ("two", process_record(v2), 250_000)]
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "2025-10-09", "1", "1", "2.000000", "unknown"],
                [v2, "2025-10-10", "1", "1", "0.500000", "yes"],
            ],
            self.cost_series(1),
        )
        self.assertNotIn("### Cost, series 2", self.latest())
        self.assertEqual([[v1, "2025-10-09", "1", "no", "0 of 0", "unknown"]], self.count_series(1))
        self.assertEqual([[v2, "2025-10-10", "1", "no", "0 of 0", "unknown"]], self.count_series(2))

    def test_a_change_under_the_review_starts_a_series_of_the_count_and_none_of_the_cost(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # The reviewer's instructions: a change of `task-cycle/review` ends the count of remarks
        # and none of the cost, whose median of v2 (0.5) is compared with v1's (2).
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way, self.LATER, parent=v1, changed={"task-cycle/review/SKILL.md": "reviewer\n"}
        )
        product = self.repository()
        self.add_cycles(
            product, [("one", process_record(v1), 1_000_000), ("two", process_record(v2), 250_000)]
        )
        self.run_versions(way, product)
        self.assertEqual(["unknown", "yes"], [row[5] for row in self.cost_series(1)])
        self.assertNotIn("### Cost, series 2", self.latest())
        self.assertEqual(
            [[v1], [v2]], [[row[0] for row in self.count_series(number)] for number in (1, 2)]
        )
        self.assertIn(
            "Begins at this version: `task-cycle/review` changed between the two versions.",
            self.latest(),
        )

    def test_a_change_of_the_reviewers_type_of_agent_starts_a_series_of_the_count_alone(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # `the-way-stage.md` is the instruction the reviewer receives: a change of it ends the
        # count of remarks and none of the cost. A change of `the-way-author.md`, beside it in
        # the same folder, ends neither.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way,
            self.LATER,
            parent=v1,
            changed={"task-cycle/agent-types/the-way-stage.md": "reviewer\n"},
        )
        v3 = self.version_at(
            way,
            self.MARCH,
            parent=v2,
            changed={
                "task-cycle/agent-types/the-way-stage.md": "reviewer\n",
                "task-cycle/agent-types/the-way-author.md": "author\n",
            },
        )
        product = self.repository()
        self.add_cycles(
            product,
            [
                ("one", process_record(v1), 1_000_000),
                ("two", process_record(v2), 500_000),
                ("three", process_record(v3), 250_000),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(["unknown", "yes", "yes"], [row[5] for row in self.cost_series(1)])
        self.assertNotIn("### Cost, series 2", self.latest())
        self.assertEqual(
            [[v1], [v2, v3]], [[row[0] for row in self.count_series(number)] for number in (1, 2)]
        )
        self.assertNotIn("### Count of remarks, series 3", self.latest())
        self.assertIn(
            "Begins at this version: `task-cycle/agent-types/the-way-stage.md` changed "
            "between the two versions.",
            self.latest(),
        )

    def test_a_change_of_the_stage_script_starts_a_series_of_both_kinds(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way, self.LATER, parent=v1, changed={"task-cycle/cycle_stages.py": "changed\n"}
        )
        product = self.repository()
        self.add_cycles(
            product, [("one", process_record(v1), 1_000_000), ("two", process_record(v2), 250_000)]
        )
        self.run_versions(way, product)
        self.assertEqual([[v1, "2025-10-09", "1", "1", "2.000000", "unknown"]], self.cost_series(1))
        self.assertEqual([[v2, "2025-10-10", "1", "1", "0.500000", "unknown"]], self.cost_series(2))
        self.assertEqual(
            [[v1], [v2]], [[row[0] for row in self.count_series(number)] for number in (1, 2)]
        )
        self.assertEqual(
            2,
            self.latest().count(
                "Begins at this version: "
                "`task-cycle/cycle_stages.py` changed between the "
                "two versions."
            ),
        )

    def test_a_cycle_that_changed_the_stage_script_stays_in_its_version_with_no_known_cost(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # The cycle stays in the version it ran on and in its series: its row counts it, its
        # answers are those of the record, and only its cost is out of the median. Unchanged, the
        # same cycle costs 1,000,000 * 2 / 1,000,000 = 2 dollars.
        day = "2025-10-09"
        for changed, cost, known in (
            ({STAGE_SCRIPT: "version two\n"}, "unknown", "0"),
            ({}, "2.000000", "1"),
        ):
            with self.subTest(sorted(changed)):
                self.fresh()
                _, version = self.own_cycle(
                    {"stages.md": self.stages_of(1_000_000)}, changed, process_record(PIN)
                )
                done = self.run_with_prices()
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertEqual([[version, day, "1", known, cost, "unknown"]], self.cost_series(1))
                self.assertEqual(
                    [[version, day, "1", "no", "0 of 0", "unknown"]], self.count_series(1)
                )
                self.assertNotIn("### Cost, series 2", self.latest())

    # Each path, with whether a change of the file starts a series of the cost and of the count of
    # remarks, and the reason the count gives: the files of the count are named by the path of the
    # list (a folder, or the one file), and the stage script stands in both.
    BOUNDARIES = (
        ("task-cycle/change/SKILL.md", False, "`task-cycle/change`"),
        ("task-cycle/plan/SKILL.md", False, "`task-cycle/plan`"),
        ("task-cycle/review/SKILL.md", False, "`task-cycle/review`"),
        ("task-cycle/spec/SKILL.md", False, "`task-cycle/spec`"),
        (
            "task-cycle/agent-types/the-way-stage.md",
            False,
            "`task-cycle/agent-types/the-way-stage.md`",
        ),
        ("task-cycle/cycle_stages.py", True, "`task-cycle/cycle_stages.py`"),
        # Files that start neither: the other type of agent, the other scripts, the rest of the
        # method of the cycle and a file of another part.
        ("task-cycle/agent-types/the-way-author.md", False, None),
        ("task-cycle/cycle_measures.py", False, None),
        ("task-cycle/gate_times.py", False, None),
        ("gate/run_tests.py", False, None),
        ("task-cycle/skill/SKILL.md", False, None),
        ("README.md", False, None),
    )

    def two_versions(self, name, path):
        """Two commits of a temporary the-way that hold every file of BOUNDARIES, the second with
        `path` changed (None: unchanged), as the versions the audit compares, and the Ancestry that
        reads the repository."""
        sys.path.insert(0, str(HERE))
        import audit_count

        way = self.repository(name)
        files = {listed: "a\n" for listed, _, _ in self.BOUNDARIES}
        first = way.commit(files, "First")
        second = way.commit({**files, **({path: "b\n"} if path else {})}, "Second", first)
        return (
            audit_count.Version(first, 1, "2025-10-09", "2026-01-01", []),
            audit_count.Version(second, 2, "2025-10-10", "2026-01-01", []),
            audit_count.Ancestry(audit_count.Git(way.root)),
        )

    def test_each_file_starts_the_series_of_its_own_kind_and_no_other(self):
        sys.path.insert(0, str(HERE))
        import audit_count

        for number, (path, in_cost, reason) in enumerate(self.BOUNDARIES):
            with self.subTest(path):
                earlier, later, ancestry = self.two_versions(f"way-{number}", path)
                cost = audit_count.cost_boundary(earlier, later, ancestry)
                count = audit_count.count_boundary(earlier, later, audit_count.Register(), ancestry)
                if reason is None:
                    self.assertIsNone(cost)
                    self.assertIsNone(count)
                    continue
                expected = f"{reason} changed between the two versions"
                self.assertEqual(expected if in_cost else None, cost)
                self.assertEqual(expected, count)

    def test_two_identical_versions_share_a_series_of_each_kind(self):
        sys.path.insert(0, str(HERE))
        import audit_count

        earlier, later, ancestry = self.two_versions("way-same", None)
        self.assertIsNone(audit_count.cost_boundary(earlier, later, ancestry))
        self.assertIsNone(
            audit_count.count_boundary(earlier, later, audit_count.Register(), ancestry)
        )

    def test_a_date_of_the_list_of_classes_starts_a_series_of_the_count_alone(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        sys.path.insert(0, str(HERE))
        import audit_count

        earlier, later, ancestry = self.two_versions("way-classes", None)
        known = audit_count.Register(class_dates=["2025-10-10"])
        self.assertIsNone(audit_count.cost_boundary(earlier, later, ancestry))
        self.assertEqual(
            "the register's list of classes changed between the two versions",
            audit_count.count_boundary(earlier, later, known, ancestry),
        )
        # A date after the two versions, and one before them, divide nothing.
        for days in (["2025-10-08"], ["2025-10-11"]):
            with self.subTest(days):
                self.assertIsNone(
                    audit_count.count_boundary(
                        earlier, later, audit_count.Register(class_dates=days), ancestry
                    )
                )
        unknown = audit_count.Register(class_dates_unknown=True)
        self.assertIsNone(audit_count.cost_boundary(earlier, later, ancestry))
        self.assertIn(
            "not given in full", audit_count.count_boundary(earlier, later, unknown, ancestry)
        )

    def test_a_git_that_cannot_compare_the_two_versions_counts_as_a_change_of_both_kinds(self):
        # Versions that the checkout does not hold: `git diff --quiet` ends with exit 128, and a
        # series is never joined by mistake.
        sys.path.insert(0, str(HERE))
        import audit_count

        _, _, ancestry = self.two_versions("way-failing", None)
        earlier = audit_count.Version("a" * 40, 1, "2025-10-09", "2026-01-01", [])
        later = audit_count.Version("b" * 40, 2, "2025-10-10", "2026-01-01", [])
        stage = "`task-cycle/cycle_stages.py` changed between the two versions"
        self.assertEqual(stage, audit_count.cost_boundary(earlier, later, ancestry))
        self.assertEqual(
            stage, audit_count.count_boundary(earlier, later, audit_count.Register(), ancestry)
        )

    def test_each_path_that_starts_a_series_is_a_path_git_tracks(self):
        # Break caught: a rename of one of these files while the audit keeps the old path: the
        # history of a path that does not exist is empty, so no change would ever start a series.
        sys.path.insert(0, str(HERE))
        import audit_count

        for path in (*audit_count.COST_SCRIPTS, *audit_count.COUNT_PATHS):
            with self.subTest(path):
                done = subprocess.run(
                    ["git", "-C", str(HERE.parent), "ls-files", "-z", "--", ":(literal)" + path],
                    capture_output=True,
                    env=GIT_ENV,
                    check=True,
                )
                self.assertTrue(done.stdout, f"git tracks no file at {path}")
        self.assertEqual(("task-cycle/cycle_stages.py",), audit_count.COST_SCRIPTS)
        self.assertEqual(
            (
                "task-cycle/change",
                "task-cycle/plan",
                "task-cycle/review",
                "task-cycle/spec",
                "task-cycle/agent-types/the-way-stage.md",
            ),
            audit_count.COUNT_PATHS,
        )

    def test_the_older_and_the_newer_form_of_the_stage_report_are_never_in_one_comparison(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # The form changes with `cycle_stages.py`, a file whose change starts a series of both
        # kinds; a change of the scripts that measure the mechanism or the gate does not. v1 to v3
        # are of the older form, v4 of the newer; the costs are 2, 1, 0.5 and 0.25 dollars. The
        # median of v4 is not set against v3's: it begins its own series.
        way = self.the_way()
        measures = {"task-cycle/cycle_measures.py": "measures\n"}
        gate = {**measures, "task-cycle/gate_times.py": "gate\n"}
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(way, self.FIRST + 86400, parent=v1, changed=measures)
        v3 = self.version_at(way, self.FIRST + 2 * 86400, parent=v2, changed=gate)
        v4 = self.version_at(
            way,
            self.FIRST + 3 * 86400,
            parent=v3,
            changed={**gate, "task-cycle/cycle_stages.py": "newer form\n"},
        )
        product = self.repository()

        def older(tokens):
            return older_stages(older_row("model-a", tokens, 0, 0))

        self.add_cycles(
            product,
            [
                ("one", process_record(v1), 1_000_000, older(1_000_000)),
                ("two", process_record(v2), 500_000, older(500_000)),
                ("three", process_record(v3), 250_000, older(250_000)),
                ("four", process_record(v4), 125_000),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "2025-10-09", "1", "1", "2.000000", "unknown"],
                [v2, "2025-10-10", "1", "1", "1.000000", "yes"],
                [v3, "2025-10-11", "1", "1", "0.500000", "yes"],
            ],
            self.cost_series(1),
        )
        self.assertEqual([[v4, "2025-10-12", "1", "1", "0.250000", "unknown"]], self.cost_series(2))
        self.assertNotIn("### Cost, series 3", self.latest())
        self.assertEqual(
            [[v1, v2, v3], [v4]],
            [[row[0] for row in self.count_series(number)] for number in (1, 2)],
        )

    def test_the_questions_read_the_record_items_and_say_unknown_otherwise(self):
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        listed = "\n  - slice 2\n  - slice 4\n  - slice 7\n  - slice 8"
        self.add_cycles(
            product,
            [
                (
                    "reading-a",
                    process_record(
                        v1,
                        discarded="reason: `open design choice`; the spec left the field open",
                        plan="11 slices and 12 foundation entries",
                        too_large=listed,
                    ),
                    1_000_000,
                ),
                (
                    "reading-b",
                    process_record(v1, plan="3 slices", too_large="\n  - slice 1"),
                    1_000_000,
                ),
                (
                    "reading-c",
                    process_record(v1, plan="5 slices", extra="- Plan: 6 slices\n"),
                    1_000_000,
                ),
            ],
        )
        self.run_versions(way, product)
        # Q1 is yes from reading-a's discarded attempt. Q2 is unknown: reading-c's doubled item
        # is not read, and its slices could change the share of the other two plans.
        self.assertEqual(
            [[v1, "2025-10-09", "3", "yes", "2 of 3", "unknown"]], self.count_series(1)
        )
        self.assertEqual([[v1, "2025-10-09", "3", "3", "2.000000", "unknown"]], self.cost_series(1))
        plan_reasons = [row[3] for row in self.rows("Unknown values") if row[2] == "Plan"]
        self.assertEqual(["the record holds the item `Plan` more than once"], plan_reasons)
        self.assertIn(
            "1 cycle(s) are not read",
            self.reasons_of(self.rows("Unknown values"), f"slices too large, version {v1}"),
        )

    def test_the_slices_of_every_plan_of_a_version_are_summed(self):
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        listed = "\n  - slice 2\n  - slice 4\n  - slice 7\n  - slice 8"
        self.add_cycles(
            product,
            [
                (
                    "reading-a",
                    process_record(
                        v1, plan="11 slices and 12 foundation entries", too_large=listed
                    ),
                    1_000_000,
                ),
                (
                    "reading-b",
                    process_record(v1, plan="3 slices", too_large="\n  - slice 1"),
                    1_000_000,
                ),
                ("one-author", process_record(v1), 1_000_000),
            ],
        )
        self.run_versions(way, product)
        # 4 + 1 too large of 11 + 3 planned: 15 > 14, so yes; the one-author cycle has no plan.
        self.assertEqual(["2 of 2", "yes"], self.count_series(1)[0][4:6])

    def test_the_count_of_slices_is_the_figure_just_before_the_word(self):
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (
                    "apart",
                    process_record(
                        v1, plan="reviewed by 2 agents; slices: 8", too_large="\n  - slice 1"
                    ),
                    1_000_000,
                ),
                (
                    "tight",
                    process_record(
                        v1,
                        plan="the plan has 4 slices, reviewed by 2 agents",
                        too_large="\n  - slice 1",
                    ),
                    1_000_000,
                ),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual("1 of 2", self.count_series(1)[0][4])
        self.assertEqual(
            ["the item `Plan` does not give one count of slices before the word `slices`"],
            [row[3] for row in self.rows("Unknown values") if row[2] == "Plan"],
        )

    def versions(self, way, count):
        """`count` versions of the-way dated one day apart, the first of them FIRST: each commit
        holds the base files, so they all stand in one series of the count of remarks."""
        versions = []
        for number in range(count):
            versions.append(
                self.version_at(
                    way, self.FIRST + number * 86_400, parent=versions[-1] if versions else None
                )
            )
        return versions

    def q1_of_each_version(self, texts, rounds="none"):
        """Q1 of the series of the count of remarks, version by version, where the cycle of each
        version has the text `texts[n]` as its item *Discarded attempt* and `rounds` as its item
        *Review rounds*; `rounds` may be a list of one text for each version."""
        way = self.the_way()
        versions = self.versions(way, len(texts))
        product = self.repository()
        self.add_cycles(
            product,
            [
                (
                    f"cycle-{number}",
                    process_record(
                        version,
                        discarded=texts[number],
                        rounds=rounds[number] if isinstance(rounds, list) else rounds,
                    ),
                    1_000,
                )
                for number, version in enumerate(versions)
            ],
        )
        self.run_versions(way, product)
        return [row[3] for row in self.count_series(1)]

    def test_the_marker_of_a_discarded_attempt_gives_q1(self):
        # decision: WAY-405 "The reason of a discarded attempt stands at the start of the record's item"
        # The form of `task-cycle/record_template.md`: the marker first, in backticks, then the time,
        # the report and the rest, which holds `none` in its other parts.
        rest = "; 10:32, report reports/x.md; foundation entries none; reset to abc1234"
        answers = self.q1_of_each_version(
            [
                "reason: `open design choice`" + rest,
                "reason: `reserved choice`" + rest,
                "reason: `size`" + rest,
                "none",
                NL + "  - reason: `open design choice`" + rest + NL + "  - reason: `size`; 14:05",
                NL + "  - reason: `size`; 14:05" + NL + "  - reason: `reserved choice`" + rest,
                NL + "  reason: `open design choice`" + rest + NL + "  - reason: `size`; 14:05",
                NL + "  reason: `open design choice`" + rest + NL + "  - report reports/x.md",
            ]
        )
        self.assertEqual(["yes", "no", "no", "no", "yes", "no", "unknown", "yes"], answers)

    def test_the_four_denials_of_review_100_leave_q1_unknown(self):
        # decision: WAY-405 "The audit of the process takes from this item, for its answer whether"
        # The texts are the four examples of remark 6 of the review of the foundation of 2026-11-14:
        # each names an open design choice in words and none carries the marker, so none is a yes.
        texts = (
            "open design choice not found",
            "an open design choice did not apply",
            "no sign whatsoever that this was an open design choice",
            "No attempt was discarded for a reserved choice, an oversized change or an open "
            "design choice",
        )
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (f"denial-{number}", process_record(v1, discarded=text), 1_000)
                for number, text in enumerate(texts)
            ],
        )
        self.run_versions(way, product)
        self.assertEqual("unknown", self.count_series(1)[0][3])
        [pair] = [row for row in self.pair_rows() if row[0] == "Discarded attempt"]
        self.assertEqual("4", pair[1])
        self.assertIn("opens with no marker of its reason", pair[2])

    def test_a_marker_that_is_not_at_the_start_or_not_in_its_form_is_not_read(self):
        # decision: WAY-405 "The audit of the process takes from this item, for its answer whether"
        texts = [
            "10:32; reason: `open design choice`",
            "reason: open design choice",
            "none — reason: `size`",
            "reason: `size`; reason: `open design choice`",
        ]
        self.assertEqual(["unknown"] * 4, self.q1_of_each_version(texts))

    def test_a_second_reason_in_a_detail_or_at_the_margin_is_not_read_and_gives_the_first_one(self):
        # decision: WAY-405 "Where the lines are sub-items at one indent alone and nothing stands beside the colon"
        # decision: WAY-405 "The item reads down to the next line at the left margin"
        # The shapes the rule names as not read: a marker in a deeper line of a sub-item, a second
        # attempt in other words than the marker among the details of the first, and a line at the
        # left margin. Each gives the answer of the first attempt, `size`, which is no contradiction.
        odc = "reason: `open design choice`"
        texts = [
            NL + "  - reason: `size`; 14:05" + NL + "    " + odc,
            NL + "  reason: `size`; 10:32" + NL + "  - reason: open design choice",
            " reason: `size`; 10:32" + NL + "  - report reports/x.md",
            NL + "  - reason: `size`; 14:05" + NL + odc,
        ]
        self.assertEqual(["no"] * 4, self.q1_of_each_version(texts))

    def test_the_crafted_discarded_attempts_break_no_cell_and_no_pattern(self):
        sys.path.insert(0, str(HERE))
        import audit_count

        remarks_check = audit_count.remarks_check
        crafted = (
            ("very long", "reason: `open design choice` " + "x " * 100_000),
            ("very long before", "no " * 200_000 + "reason: `open design choice`"),
            ("long without clause marks", "x" * 500_000 + " reason: `open design choice`"),
            ("control characters", "\x1b[2J reason: `open design choice` \x00\x07 | no | x"),
            ("many markers", "reason: `size` " * 50_000),
            ("a bar", "reason: `open design choice` a | b | c"),
        )
        for label, text in crafted:
            with self.subTest(label):
                lines = remarks_check.split_lines(f"- Discarded attempt: {text}\n")
                answer, why = audit_count.read_contradiction(
                    lines, remarks_check.fenced_flags(lines)
                )
                self.assertIn(answer, ("yes", None))
                self.assertEqual(answer is None, why is not None)
        # Run whole: no cell of the result holds a bar or a control character from the item.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (f"crafted-{number}", process_record(v1, discarded=text.replace("\n", " ")), 1_000)
                for number, (_, text) in enumerate(crafted)
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [], [char for char in self.latest() if not char.isprintable() and char != "\n"]
        )
        self.assertEqual(["yes"], [self.count_series(1)[0][3]])

    def test_a_round_marked_as_a_contradiction_gives_yes_and_an_unmarked_round_unknown(self):
        # decision: WAY-404 "The cycle writes the mark into the sub-item of the round in the record's item"
        # Four cycles, each in a version of its own; the item *Discarded attempt* reads `none`. The
        # sub-item of the fourth is the form from before the mark, the third one has a mark that is
        # none of the two: both give the one reason.
        marked = "\n  - findings `reports/a_findings.md`, contradiction {}: the whole change"
        rounds = [
            marked.format("yes"),
            marked.format("no") + "\n  - review `reports/r.md`, PASS: the return step",
            marked.format("maybe"),
            "\n  - findings `reports/a_findings.md`: the whole change, range a1b2c3d..e4f5a6b",
        ]
        self.assertEqual(
            ["yes", "no", "unknown", "unknown"], self.q1_of_each_version(["none"] * 4, rounds)
        )
        [pair] = [row for row in self.pair_rows() if row[0] == "Discarded attempt"]
        self.assertEqual("2", pair[1])
        self.assertEqual(
            "the sub-item of a round does not say whether there was a contradiction", pair[2]
        )

    def test_crafted_entries_of_review_rounds_break_no_cell_and_give_no_answer_they_do_not_state(
        self,
    ):
        # decision: WAY-404 "The cycle writes the mark into the sub-item of the round in the record's item"
        # A sub-item that is in neither form, a path with a control
        # character, a bar or a `..`, a mark
        # that runs on, and forty thousand sub-items give Q1 unknown, or the answer the sub-items
        # state (the mark that runs on is none); no text of a sub-item reaches a cell of the result, which names only fixed reasons.
        many = "".join(
            f"\n  - findings `reports/f{number}.md`, contradiction no: x"
            for number in range(40_000)
        )
        rounds = [
            "\n  - findings `reports/a\x1b[2J.md`, contradiction yes: x",
            "\n  - findings `reports/a|b.md`, contradiction yes: x",
            "\n  - review `reports/../a.md`, PASS: x",
            "\n  - findings `reports/a.md`, contradiction yes | no: x" + "x" * 300_000,
            many,
        ]
        answers = self.q1_of_each_version(["none"] * len(rounds), rounds)
        self.assertEqual(["unknown", "unknown", "unknown", "unknown", "no"], answers)
        self.assertEqual(
            [], [char for char in self.latest() if not char.isprintable() and char != "\n"]
        )

    def test_a_record_without_the_item_discarded_attempt_or_review_rounds_gives_q1_unknown(self):
        # decision: WAY-344 "Each reading of a file that the rule covers has one test"
        # A record of an earlier form lacks the items, as the records the count reads from history
        # do: Q1 is unknown, the reason names the item, and the exit code stays 0 (run_versions
        # asserts it), as for the other items of the record.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(way, self.LATER, parent=v1)
        product = self.repository()
        no_discarded = process_record(v1).replace("- Discarded attempt: none\n", "")
        no_rounds = process_record(v2).replace("- Review rounds: none\n", "")
        self.add_cycles(
            product, [("no-discarded", no_discarded, 1_000), ("no-rounds", no_rounds, 1_000)]
        )
        self.run_versions(way, product)
        self.assertEqual(["unknown", "unknown"], [row[3] for row in self.count_series(1)])
        reasons = {row[2] for row in self.pair_rows() if row[0] == "Discarded attempt"}
        self.assertEqual(
            {
                "the record holds no item `Discarded attempt`",
                "the item `Review rounds` does not give its sub-items, so whether a "
                "review round found a contradiction is not known",
            },
            reasons,
        )

    def test_a_third_is_not_above_a_third(self):
        # One slice too large of three planned is exactly a third, which is not above it: no.
        way = self.the_way()
        v2 = self.version_at(way, self.LATER)
        product = self.repository()
        self.add_cycles(
            product,
            [("exact", process_record(v2, plan="3 slices", too_large="\n  - slice 1"), 1_000_000)],
        )
        self.run_versions(way, product)
        self.assertEqual(["1 of 1", "no"], self.count_series(1)[0][4:6])

    def test_unknown_reads_stay_unknown(self):
        # The prose discarded attempt makes Q1 unknown; the cycle whose plan has no figure just
        # before the word `slices` makes Q2 unknown with its reason, and does not stall the run.
        way = self.the_way()
        v2 = self.version_at(way, self.LATER)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (
                    "exact",
                    process_record(v2, plan="3 slices", too_large="\n  - slice 1"),
                    1_000_000,
                ),
                ("prose", process_record(v2, discarded="a time overrun"), 1_000_000),
                ("crawling", process_record(v2, plan="9" * 200_000 + " slices"), 1_000_000),
            ],
        )
        self.run_versions(way, product)
        [row] = self.count_series(1)
        self.assertEqual([v2, "2025-10-10", "3", "unknown", "1 of 2", "unknown"], row)
        self.assertEqual([[v2, "2025-10-10", "3", "3", "2.000000", "unknown"]], self.cost_series(1))
        unknown = self.rows("Unknown values")
        self.assertEqual(1, len([row for row in unknown if row[2] == "Discarded attempt"]))
        self.assertEqual(
            ["the item `Plan` does not give one count of slices before the word `slices`"],
            [row[3] for row in unknown if row[2] == "Plan"],
        )


def gate_run(second, others, total, *directories, code=0) -> str:
    """The rows of one run of gate_times.md: its start differs with `second`, so that runs stay
    apart; each directory is (name, seconds), and a run with none has the one row with dashes;
    `code` is the exit code written."""
    started = f"2026-11-11 10:00:{second:02}.000"
    if not directories:
        return gate_row(started, code, total, others)
    return "".join(
        gate_row(started, code, total, others, name, seconds) for name, seconds in directories
    )


TOTAL = "Total time of the run"


class MeasureVersions(AuditCountCase):
    """The series of the mechanism measures and of the gate times, each by the change of its own
    instrument alone, and the median of each measure of each version (WAY-339, WAY-350).
    The helpers are those of ProcessVersions."""

    FIRST = ProcessVersions.FIRST
    BASE_FILES = ProcessVersions.BASE_FILES
    the_way = ProcessVersions.the_way
    version_at = ProcessVersions.version_at
    run_versions = ProcessVersions.run_versions
    cost_series = ProcessVersions.cost_series
    count_series = ProcessVersions.count_series

    def day(self, number) -> int:
        return self.FIRST + number * 86400

    def add_measured(self, product, specs) -> None:
        """Each cycle as (folder, pin, values, runs), chained so that all stay in the history:
        `values` maps a label of mechanism_measures.md to its value, the other labels keeping the
        value of MEASURE_VALUES, and is None for a copy with no such file; `runs` is the rows of
        gate_times.md, None for a copy with no such file."""
        parent = product.commit({"README.md": "a product\n"}, "Start")
        for folder, pin, values, runs in specs:
            files = {"cycle.md": process_record(pin)}
            if values is not None:
                files[MEASURES] = measures_file(
                    [(label, values.get(label, default)) for label, default in MEASURE_VALUES]
                )
            if runs is not None:
                files[GATE] = gate_file(rows=runs)
            _, parent = product.cycle(folder, files, parent=parent, branch=None)
        product.branch("main", parent)

    def measure(self, number, label) -> list[list[str]]:
        """The rows of a series of mechanism measures that are of one measure."""
        return [row for row in self.section("Mechanism measures", number) if row[1] == label]

    def gate(self, number, measure=TOTAL) -> list[list[str]]:
        return [row for row in self.section("Gate times", number) if row[1] == measure]

    def test_a_change_of_an_instrument_starts_only_the_series_of_its_own_measures(self):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # v2 changes the script of the measures, v3 the script of the gate times, v4 the reviewer's
        # instructions and `cycle_stages.py`. The cost splits at v4 alone; the mechanism measures
        # at v2 alone; the gate times at v3 alone, and no median is set across a split.
        way = self.the_way()
        measures = {"task-cycle/cycle_measures.py": "measures\n"}
        both = {**measures, "task-cycle/gate_times.py": "gate\n"}
        reviewed = {
            **both,
            "task-cycle/review/SKILL.md": "reviewer\n",
            "task-cycle/cycle_stages.py": "newer form\n",
        }
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1, changed=measures)
        v3 = self.version_at(way, self.day(2), parent=v2, changed=both)
        v4 = self.version_at(way, self.day(3), parent=v3, changed=reviewed)
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, {"Calls in all": "8"}, gate_run(2, 0, "90.000")),
                ("three", v3, {"Calls in all": "9"}, gate_run(3, 0, "80.000")),
                ("four", v4, {"Calls in all": "5"}, gate_run(4, 0, "70.000")),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual([v1, v2, v3], [row[0] for row in self.cost_series(1)])
        self.assertEqual([v4], [row[0] for row in self.cost_series(2)])
        self.assertNotIn("### Cost, series 3", self.latest())
        self.assertEqual([v1, v2, v3], [row[0] for row in self.count_series(1)])
        self.assertEqual([v4], [row[0] for row in self.count_series(2)])
        self.assertNotIn("### Count of remarks, series 3", self.latest())
        calls = "Calls in all"
        self.assertEqual([[v1, calls, "1", "10", "unknown"]], self.measure(1, calls))
        self.assertEqual(
            [
                [v2, calls, "1", "8", "unknown"],
                [v3, calls, "1", "9", "no"],
                [v4, calls, "1", "5", "yes"],
            ],
            self.measure(2, calls),
        )
        self.assertNotIn("### Mechanism measures, series 3", self.latest())
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"],
                [v2, TOTAL, "1", "90.000", "yes", "0", "unknown"],
            ],
            self.gate(1),
        )
        self.assertEqual(
            [
                [v3, TOTAL, "1", "80.000", "unknown", "0", "unknown"],
                [v4, TOTAL, "1", "70.000", "yes", "0", "unknown"],
            ],
            self.gate(2),
        )
        self.assertNotIn("### Gate times, series 3", self.latest())
        text = self.latest()
        self.assertLess(text.index("## Process versions"), text.index("## Measure versions"))
        self.assertLess(text.index("## Measure versions"), text.index("## Problems by cycle"))

    def test_a_changed_tool_of_a_measure_gives_no_value_to_the_median_of_its_version(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # One own cycle with both files, in the version it ran on. Where it changed the script of
        # the measures, its version gives no value of them and its gate times stand; where it
        # changed the test runner, the gate times are the ones without a value and the mechanism
        # measures stand; where it changed none, both give their one value (12 calls, 100 seconds).
        calls = "Calls in all"
        for changed, mechanism, runs in (
            ({"task-cycle/cycle_measures.py": "two\n"}, False, True),
            ({"gate/run_tests.py": "two\n"}, True, False),
            ({"task-cycle/gate_times.py": "two\n"}, True, False),
            ({}, True, True),
        ):
            with self.subTest(sorted(changed)):
                self.fresh()
                files = {MEASURES: measures_file(), GATE: gate_file(rows=gate_run(1, 0, "100.000"))}
                _, version = self.own_cycle(files, changed, process_record(PIN))
                done = self.run_with_prices()
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertEqual(
                    [[version, calls, "1", "12", "unknown"]]
                    if mechanism
                    else [[version, "—", "0", "unknown", "unknown"]],
                    self.measure(1, calls if mechanism else "—"),
                )
                self.assertEqual(
                    [[version, TOTAL, "1", "100.000", "unknown", "0", "unknown"]]
                    if runs
                    else [[version, "—", "0", "unknown", "unknown", "0", "unknown"]],
                    self.gate(1, TOTAL if runs else "—"),
                )

    def test_a_change_of_the_test_runner_starts_a_new_series_of_gate_times_only(self):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # v2 changes the test runner of the gate, v3 the script of the measures. The gate times
        # split at v2 alone, the mechanism measures at v3 alone, and the reason of the split
        # names the file that changed. Medians: the gate series of v2 and v3 has 90 and 80, so v3
        # falls; v1 stands alone in its series.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1, changed={"gate/run_tests.py": "runner\n"})
        # A commit lists the files it keeps, so v3 lists the runner again, unchanged.
        v3 = self.version_at(
            way,
            self.day(2),
            parent=v2,
            changed={"gate/run_tests.py": "runner\n", "task-cycle/cycle_measures.py": "measures\n"},
        )
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, {"Calls in all": "9"}, gate_run(2, 0, "90.000")),
                ("three", v3, {"Calls in all": "8"}, gate_run(3, 0, "80.000")),
            ],
        )
        self.run_versions(way, product)
        calls = "Calls in all"
        self.assertEqual(
            [[v1, calls, "1", "10", "unknown"], [v2, calls, "1", "9", "yes"]],
            self.measure(1, calls),
        )
        self.assertEqual([[v3, calls, "1", "8", "unknown"]], self.measure(2, calls))
        self.assertEqual([[v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"]], self.gate(1))
        self.assertEqual(
            [
                [v2, TOTAL, "1", "90.000", "unknown", "0", "unknown"],
                [v3, TOTAL, "1", "80.000", "yes", "0", "unknown"],
            ],
            self.gate(2),
        )
        self.assertIn(
            "Begins at this version: `gate/run_tests.py` changed between the two versions.",
            self.latest(),
        )

    def test_the_reason_of_a_gate_split_names_the_scripts_that_changed(self):
        # Asked of two versions directly: the gate times split at a change of either of their
        # scripts and the reason names the ones that changed, in the order of the scripts; the
        # mechanism measures split at no change of the test runner.
        sys.path.insert(0, str(HERE))
        import audit_count

        class Changed:
            def __init__(self, paths):
                self.paths = paths

            def differs(self, earlier, later, paths):
                return any(path in self.paths for path in paths)

        scripts = ("task-cycle/gate_times.py", "gate/run_tests.py")
        earlier = audit_count.Version("a" * 40, 1, "2025-10-09", "2026-01-01", [])
        later = audit_count.Version("b" * 40, 2, "2025-10-10", "2026-02-01", [])
        runner = audit_count.instrument_series(
            [earlier, later], Changed({"gate/run_tests.py"}), scripts
        )
        self.assertEqual("`gate/run_tests.py` changed between the two versions", runner[1].begins)
        both = audit_count.instrument_series([earlier, later], Changed(set(scripts)), scripts)
        self.assertEqual(
            "`task-cycle/gate_times.py` and `gate/run_tests.py` changed between the two versions",
            both[1].begins,
        )
        measures = audit_count.instrument_series(
            [earlier, later], Changed({"gate/run_tests.py"}), ("task-cycle/cycle_measures.py",)
        )
        self.assertEqual([[earlier, later]], [block.versions for block in measures])

    def test_the_reviewer_the_stage_script_and_the_list_of_classes_split_no_series_of_measures(
        self,
    ):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # v2 changes the reviewer's instructions, v3 `cycle_stages.py`, and a class is added on the
        # day of v4: each splits the series of the count of remarks, `cycle_stages.py` alone the
        # series of the cost, and none splits the measures, whose medians fall from version to
        # version across all three.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(
            way, self.day(1), parent=v1, changed={"task-cycle/review/SKILL.md": "reviewer\n"}
        )
        v3 = self.version_at(
            way,
            self.day(2),
            parent=v2,
            changed={
                "task-cycle/review/SKILL.md": "reviewer\n",
                "task-cycle/cycle_stages.py": "newer form\n",
            },
        )
        v4 = self.version_at(
            way,
            self.day(3),
            parent=v3,
            changed={
                "task-cycle/review/SKILL.md": "reviewer\n",
                "task-cycle/cycle_stages.py": "newer form\n",
            },
        )
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, {"Calls in all": "9"}, gate_run(2, 0, "90.000")),
                ("three", v3, {"Calls in all": "8"}, gate_run(3, 0, "80.000")),
                ("four", v4, {"Calls in all": "7"}, gate_run(4, 0, "70.000")),
            ],
        )
        self.register.write_text(
            register_text(classes=["| sharp | x | 2025-10-12 | none |"]), encoding="utf-8"
        )
        self.run_versions(way, product)
        self.assertEqual(
            [[v1], [v2], [v3], [v4]],
            [[row[0] for row in self.count_series(number)] for number in (1, 2, 3, 4)],
        )
        self.assertEqual(
            [[v1, v2], [v3, v4]],
            [[row[0] for row in self.cost_series(number)] for number in (1, 2)],
        )
        self.assertNotIn("### Cost, series 3", self.latest())
        self.assertEqual(
            [
                [v1, "Calls in all", "1", "10", "unknown"],
                [v2, "Calls in all", "1", "9", "yes"],
                [v3, "Calls in all", "1", "8", "yes"],
                [v4, "Calls in all", "1", "7", "yes"],
            ],
            self.measure(1, "Calls in all"),
        )
        self.assertEqual(["unknown", "yes", "yes", "yes"], [row[4] for row in self.gate(1)])
        self.assertNotIn("### Mechanism measures, series 2", self.latest())
        self.assertNotIn("### Gate times, series 2", self.latest())

    def test_a_new_price_list_splits_no_series_of_measures(self):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # One price list prices a whole run, so no real run splits at it: the series of the
        # measures are asked of the two versions directly, and ask git about their scripts alone.
        sys.path.insert(0, str(HERE))
        import audit_count

        asked = []

        class Unchanged:
            def differs(self, earlier, later, paths):
                asked.append(tuple(paths))
                return False

        earlier = audit_count.Version("a" * 40, 1, "2025-10-09", "2026-01-01", [])
        later = audit_count.Version("b" * 40, 2, "2025-10-10", "2026-02-01", [])
        for scripts in (
            ("task-cycle/cycle_measures.py",),
            ("task-cycle/gate_times.py", "gate/run_tests.py"),
        ):
            with self.subTest(scripts):
                blocks = audit_count.instrument_series([earlier, later], Unchanged(), scripts)
                self.assertEqual([[earlier, later]], [block.versions for block in blocks])
                self.assertEqual(scripts, asked[-1])
        self.assertEqual("the price list changed", audit_count.cost_boundary(earlier, later, None))

    def test_medians_and_falls_of_three_versions_over_an_odd_and_an_even_number_of_cycles(self):
        # Calls in all: v1 has 10, 4 and 7 (median 7, odd), v2 has 6 and 9 (median 7.5, even, so
        # not lower than 7), v3 has 2, 8, 5 and 6 (sorted 2, 5, 6, 8: median 5.5, lower than 7.5).
        # The share has a value in 2 of 3 cycles of v1 (12.5 and 13.0: 12.75), in 1 of 2 of v2
        # (12.0, lower) and in 2 of 4 of v3 (12.0 and 12.5: 12.25, not lower than 12.0). A cycle
        # of no version, with 1 call, stands in no median.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        v3 = self.version_at(way, self.day(2), parent=v2)
        share = "Share of the context in calls above 200000 tokens"
        product = self.repository()
        self.add_measured(
            product,
            [
                ("a", v1, {"Calls in all": "10", share: "12.5%"}, None),
                ("b", v1, {"Calls in all": "4", share: "13.0%"}, None),
                ("c", v1, {"Calls in all": "7", share: "unknown"}, None),
                ("d", v2, {"Calls in all": "6", share: "12.0%"}, None),
                ("e", v2, {"Calls in all": "9", share: "unknown"}, None),
                ("f", v3, {"Calls in all": "2", share: "12.0%"}, None),
                ("g", v3, {"Calls in all": "8", share: "12.5%"}, None),
                ("h", v3, {"Calls in all": "5", share: "unknown"}, None),
                ("i", v3, {"Calls in all": "6", share: "unknown"}, None),
                ("stray", "none", {"Calls in all": "1"}, None),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "Calls in all", "3", "7", "unknown"],
                [v2, "Calls in all", "2", "7.5", "no"],
                [v3, "Calls in all", "4", "5.5", "yes"],
            ],
            self.measure(1, "Calls in all"),
        )
        self.assertEqual(
            [
                [v1, share, "2", "12.75%", "unknown"],
                [v2, share, "1", "12.0%", "yes"],
                [v3, share, "2", "12.25%", "no"],
            ],
            self.measure(1, share),
        )
        # A measure that does not change does not fall; every one of the fifteen has a row.
        self.assertEqual(
            [
                [v1, "Calls of subagents", "3", "7", "unknown"],
                [v2, "Calls of subagents", "2", "7", "no"],
                [v3, "Calls of subagents", "4", "7", "no"],
            ],
            self.measure(1, "Calls of subagents"),
        )
        self.assertEqual(3 * len(MEASURE_LABELS), len(self.section("Mechanism measures", 1)))
        unknown = self.rows("Unknown values")
        self.assertEqual(
            "no previous version in the series",
            self.reasons_of(unknown, f"Measure falls: Calls in all, version {v1}"),
        )
        self.assertEqual("", self.reasons_of(unknown, f"Measure falls: Calls in all, version {v2}"))

    def test_the_gate_times_take_only_runs_with_no_other_gate_and_show_the_others_apart(self):
        # Medians by hand. v1: total of the runs alone 100 and 110 (105.000), apart 200 (company: 1
        # other gate) and 300 (count unknown): 250.000; gate/a alone 60.0 and 70.0 (65.0), apart
        # 135.0; gate/b alone 40.0, apart 80.0. v2: alone 90 and 95 (92.500, lower than 105), apart
        # 10.000 (it would pull the median down if it entered); gate/a 51.0, apart 1.0; no gate/b
        # run. v3: total alone 100 (not lower than 92.5: apart 1.000 enters no comparison),
        # gate/a in a run with company only, gate/b alone 41.0 with no previous gate/b. v4: every
        # run has company, so no comparison.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        v3 = self.version_at(way, self.day(2), parent=v2)
        v4 = self.version_at(way, self.day(3), parent=v3)
        product = self.repository()
        self.add_measured(
            product,
            [
                (
                    "a",
                    v1,
                    {},
                    gate_run(1, 0, "100.000", ("gate/a", "60.0"), ("gate/b", "40.0"))
                    + gate_run(2, 1, "200.000", ("gate/a", "120.0"), ("gate/b", "80.0")),
                ),
                (
                    "b",
                    v1,
                    {},
                    gate_run(3, 0, "110.000", ("gate/a", "70.0"))
                    + gate_run(4, "unknown", "300.000", ("gate/a", "150.0")),
                ),
                (
                    "c",
                    v2,
                    {},
                    gate_run(5, 0, "90.000", ("gate/a", "50.0"))
                    + gate_run(6, 0, "95.000", ("gate/a", "52.0"))
                    + gate_run(7, 3, "10.000", ("gate/a", "1.0")),
                ),
                (
                    "d",
                    v3,
                    {},
                    gate_run(8, 0, "100.000", ("gate/b", "41.0"))
                    + gate_run(9, 1, "1.000", ("gate/a", "0.5")),
                ),
                ("e", v4, {}, gate_run(10, 2, "50.000", ("gate/a", "20.0"))),
            ],
        )
        self.run_versions(way, product)
        a, b = "Directory: gate/a", "Directory: gate/b"
        self.assertEqual(
            [
                [v1, TOTAL, "2", "105.000", "unknown", "2", "250.000"],
                [v1, a, "2", "65.0", "unknown", "2", "135.0"],
                [v1, b, "1", "40.0", "unknown", "1", "80.0"],
                [v2, TOTAL, "2", "92.500", "yes", "1", "10.000"],
                [v2, a, "2", "51.0", "yes", "1", "1.0"],
                [v3, TOTAL, "1", "100.000", "no", "1", "1.000"],
                [v3, a, "0", "unknown", "unknown", "1", "0.5"],
                [v3, b, "1", "41.0", "unknown", "0", "unknown"],
                [v4, TOTAL, "0", "unknown", "unknown", "1", "50.000"],
                [v4, a, "0", "unknown", "unknown", "1", "20.0"],
            ],
            self.section("Gate times", 1),
        )
        unknown = self.rows("Unknown values")
        self.assertIn(
            "no previous version in the series",
            self.reasons_of(unknown, f"Gate time falls: {TOTAL}, version {v1}"),
        )
        self.assertIn(
            "no run of the version that passed with no other gate",
            self.reasons_of(unknown, f"Gate time falls: {TOTAL}, version {v4}"),
        )
        self.assertIn(
            "no run of the previous version that passed with no other gate",
            self.reasons_of(unknown, f"Gate time falls: {b}, version {v3}"),
        )

    def test_a_version_with_no_cycle_that_gave_a_value_has_one_row_and_one_line_of_reason(self):
        # v2's cycle has neither file: one row in each table, `—` for the measure and no median, and
        # one line in *Unknown values* for each instrument instead of one for each measure. v3 has
        # values, keeps its rows as they are, and is not compared with v2.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        v3 = self.version_at(way, self.day(2), parent=v2)
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, None, None),
                ("three", v3, {"Calls in all": "9"}, gate_run(3, 0, "90.000")),
            ],
        )
        self.run_versions(way, product)
        calls = "Calls in all"
        self.assertEqual(
            [[v1, calls, "1", "10", "unknown"], [v3, calls, "1", "9", "unknown"]],
            self.measure(1, calls),
        )
        self.assertEqual([[v2, "—", "0", "unknown", "unknown"]], self.measure(1, "—"))
        self.assertEqual(2 * len(MEASURE_LABELS) + 1, len(self.section("Mechanism measures", 1)))
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"],
                [v3, TOTAL, "1", "90.000", "unknown", "0", "unknown"],
            ],
            self.gate(1),
        )
        self.assertEqual([[v2, "—", "0", "unknown", "unknown", "0", "unknown"]], self.gate(1, "—"))
        unknown = self.rows("Unknown values")
        self.assertIn(
            "no cycle of this version gives a value",
            self.reasons_of(unknown, f"Mechanism measures of version {v2}"),
        )
        self.assertIn(
            "an earlier cycle, or a script that failed",
            self.reasons_of(unknown, f"Mechanism measures of version {v2}"),
        )
        self.assertIn(
            "no run of this version gives a time",
            self.reasons_of(unknown, f"Gate times of version {v2}"),
        )
        # The cause named for a version with no gate times is the task's row 6: a final gate that
        # ran in CI; the mechanism measures, which no CI run leaves out, do not name it.
        self.assertIn(
            "a final gate that ran in CI", self.reasons_of(unknown, f"Gate times of version {v2}")
        )
        self.assertNotIn(
            "a final gate that ran in CI",
            self.reasons_of(unknown, f"Mechanism measures of version {v2}"),
        )
        self.assertEqual(
            [],
            [
                row
                for row in unknown
                if row[2].startswith("Measure falls") and f"version {v2}" in row[2]
            ],
        )
        self.assertEqual(
            "no cycle of the previous version gives a value",
            self.reasons_of(unknown, f"Measure falls: {calls}, version {v3}"),
        )

    def test_a_failed_run_enters_no_median_and_is_shown_apart_with_the_runs_with_company(self):
        # v1: passed and alone: 100.000 (gate/a 60.0). A run alone that exited 2 (5.000, gate/a
        # 1.0) and one alone whose exit code is unknown (300.000) are not compared: apart, the
        # median of 5.000 and 300.000 is 152.500. v2: passed and alone 90.000 (gate/a 50.0), so the
        # total falls from 100.000 and gate/a from 60.0; a failed run alone, 2.000, is apart.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        product = self.repository()
        self.add_measured(
            product,
            [
                (
                    "a",
                    v1,
                    {},
                    gate_run(1, 0, "100.000", ("gate/a", "60.0"))
                    + gate_run(2, 0, "5.000", ("gate/a", "1.0"), code=2)
                    + gate_run(3, 0, "300.000", code="unknown"),
                ),
                (
                    "b",
                    v2,
                    {},
                    gate_run(4, 0, "90.000", ("gate/a", "50.0")) + gate_run(5, 0, "2.000", code=1),
                ),
            ],
        )
        self.run_versions(way, product)
        a = "Directory: gate/a"
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "2", "152.500"],
                [v1, a, "1", "60.0", "unknown", "1", "1.0"],
                [v2, TOTAL, "1", "90.000", "yes", "1", "2.000"],
                [v2, a, "1", "50.0", "yes", "0", "unknown"],
            ],
            self.section("Gate times", 1),
        )

    def test_a_version_whose_only_run_failed_has_no_median_and_no_comparison(self):
        # v1 passed (100.000); v2's only run failed (4.000): v2 has no median, no comparison, and
        # its run is apart.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        product = self.repository()
        self.add_measured(
            product,
            [
                ("a", v1, {}, gate_run(1, 0, "100.000")),
                ("b", v2, {}, gate_run(2, 0, "4.000", code=2)),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"],
                [v2, TOTAL, "0", "unknown", "unknown", "1", "4.000"],
            ],
            self.gate(1),
        )
        self.assertIn(
            "no run of the version that passed with no other gate",
            self.reasons_of(self.rows("Unknown values"), f"Gate time falls: {TOTAL}, version {v2}"),
        )

    def test_a_directory_written_twice_in_one_run_counts_once_and_says_so(self):
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        product = self.repository()
        self.add_measured(
            product, [("a", v1, {}, gate_run(1, 0, "10.000", ("gate/a", "5.0"), ("gate/a", "7.0")))]
        )
        self.run_versions(way, product)
        self.assertEqual(
            [[v1, "Directory: gate/a", "1", "5.0", "unknown", "0", "unknown"]],
            self.gate(1, "Directory: gate/a"),
        )
        self.assertTrue(any("twice" in row[3] for row in self.rows("Unknown values")))

    def test_crafted_directories_and_runs_break_no_cell_and_cost_bounded_work(self):
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        product = self.repository()
        crafted = (
            gate_run(1, 0, "1.000", ("gate\\|x\x1b[2J\x07y", "1.0"), ("d" * 500, "2.0"))
            + "".join(
                gate_row(f"2026-11-11 11:00:00.{index:03}", 0, "1.000", 0, f"gate/d{index}", "1.0")
                for index in range(700)
            )
            + "| a | b |\n" * 30
        )
        self.add_measured(product, [("a", v1, {}, crafted)])
        self.run_versions(way, product)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        self.assertNotIn("d" * 201, text)
        rows = self.section("Gate times", 1)
        self.assertEqual({7}, {len(row) for row in rows})
        # 500 runs are read, the first of them the crafted one: the total, its two directories and
        # the 499 directories of the runs after it.
        self.assertEqual(1 + 2 + 499, len(rows))
        self.assertIn(["Directory: " + "d" * 200], [[row[1]] for row in rows])


class PriceBoundary(unittest.TestCase):
    def test_a_new_price_list_starts_a_new_series_of_the_cost_and_of_the_count_of_remarks(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        sys.path.insert(0, str(HERE))
        import audit_count

        earlier = audit_count.Version("a" * 40, 1, "2025-10-09", "2026-01-01", [])
        later = audit_count.Version("b" * 40, 2, "2025-10-10", "2026-02-01", [])
        self.assertEqual("the price list changed", audit_count.cost_boundary(earlier, later, None))
        self.assertEqual(
            "the price list changed",
            audit_count.count_boundary(earlier, later, audit_count.Register(), None),
        )


if __name__ == "__main__":
    unittest.main()
